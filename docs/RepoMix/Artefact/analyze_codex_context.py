#!/usr/bin/env python3
"""Summarize Codex rollout JSONL sizes and recorded token usage.

This is a local, read-only analyzer. It prints aggregate counts only; it never
prints message, command, or tool-result contents. Token estimates for text
components use ceil(Unicode characters / 4) and are not tokenizer counts.

Examples:
  python docs/RepoMix/Artefact/analyze_codex_context.py --input C:/Users/me/.codex/sessions/2026/10/08/rollout.jsonl
  python docs/RepoMix/Artefact/analyze_codex_context.py --input C:/Users/me/.codex/sessions/2026/10/08 --measure skill/SKILL.md
  python docs/RepoMix/Artefact/analyze_codex_context.py --input rollout.jsonl --json --output report.json
"""

from __future__ import annotations

import argparse
import collections
import gzip
import json
import math
import re
import sys
from pathlib import Path
from typing import Any, Iterable


TOOL_PATTERN = re.compile(r"\btools\.([A-Za-z][A-Za-z0-9_]*?)\s*\(")
SKILL_MARKERS = ("SKILL.md", "legacy-codebase-workflows", "openai-docs")


def compact_bytes(value: Any) -> int:
    return len(json.dumps(value, ensure_ascii=False, separators=(",", ":")).encode("utf-8"))


def collect_strings(value: Any) -> Iterable[str]:
    if isinstance(value, str):
        yield value
    elif isinstance(value, dict):
        for nested in value.values():
            yield from collect_strings(nested)
    elif isinstance(value, (list, tuple)):
        for nested in value:
            yield from collect_strings(nested)


def text_stats(value: Any) -> tuple[int, int]:
    strings = list(collect_strings(value))
    chars = sum(len(s) for s in strings)
    return chars, sum(len(s.encode("utf-8")) for s in strings)


def expand_inputs(paths: list[Path]) -> list[Path]:
    found: set[Path] = set()
    for path in paths:
        if path.is_dir():
            found.update(p.resolve() for p in path.rglob("*.jsonl"))
            found.update(p.resolve() for p in path.rglob("*.jsonl.gz"))
        elif path.is_file():
            found.add(path.resolve())
        else:
            raise FileNotFoundError(path)
    return sorted(found)


def open_jsonl(path: Path):
    return gzip.open(path, "rt", encoding="utf-8", errors="replace") if path.name.endswith(".gz") else path.open("r", encoding="utf-8", errors="replace")


def usage_fields(payload: dict[str, Any]) -> dict[str, Any] | None:
    usage = payload.get("usage")
    if isinstance(usage, dict):
        return usage
    info = payload.get("info")
    if isinstance(info, dict) and isinstance(info.get("last_token_usage"), dict):
        return info["last_token_usage"]
    return None


def analyze(paths: list[Path], measure_paths: list[Path]) -> dict[str, Any]:
    files = expand_inputs(paths)
    totals: dict[str, Any] = {
        "files": [],
        "record_types": collections.Counter(),
        "message_roles": collections.Counter(),
        "message_components": collections.defaultdict(lambda: {"records": 0, "chars": 0, "utf8_bytes": 0}),
        "tool_calls": collections.defaultdict(lambda: {"calls": 0, "input_chars": 0, "input_bytes": 0, "outputs": 0, "output_chars": 0, "output_bytes": 0}),
        "nested_tools": collections.Counter(),
        "mcp_direct_calls": collections.Counter(),
        "event_types": collections.Counter(),
        "skill_marker_records": {"records": 0, "serialized_bytes": 0, "markers": collections.Counter()},
        "invalid_json_lines": 0,
    }
    usage_by_id: dict[str, dict[str, Any]] = {}
    fallback_usage: list[tuple[str, int, dict[str, Any], int | None]] = []
    output_call_names: dict[str, str] = {}

    for path in files:
        file_info = {"file": path.name, "bytes": path.stat().st_size, "records": 0, "record_types": collections.Counter()}
        with open_jsonl(path) as stream:
            for ordinal, line in enumerate(stream, 1):
                if not line.strip():
                    continue
                file_info["records"] += 1
                totals["record_types"]["_lines_"] += 1
                try:
                    record = json.loads(line)
                except json.JSONDecodeError:
                    totals["invalid_json_lines"] += 1
                    continue
                kind = str(record.get("type", "unknown"))
                file_info["record_types"][kind] += 1
                totals["record_types"][kind] += 1
                payload = record.get("payload") if isinstance(record.get("payload"), dict) else {}
                payload_kind = str(payload.get("type", ""))

                if kind == "response_item":
                    item_type = str(payload.get("type", "unknown"))
                    if item_type == "message":
                        role = str(payload.get("role", "unknown"))
                        chars, byte_count = text_stats(payload.get("content", []))
                        totals["message_roles"][role] += 1
                        comp = totals["message_components"][role]
                        comp["records"] += 1
                        comp["chars"] += chars
                        comp["utf8_bytes"] += byte_count
                    elif item_type == "reasoning":
                        chars, byte_count = text_stats(payload.get("summary", []))
                        encrypted = payload.get("encrypted_content")
                        encrypted_bytes = len(encrypted.encode("utf-8")) if isinstance(encrypted, str) else 0
                        comp = totals["message_components"]["reasoning_summary_and_encrypted_payload"]
                        comp["records"] += 1
                        comp["chars"] += chars
                        comp["utf8_bytes"] += byte_count + encrypted_bytes
                    elif item_type in ("custom_tool_call", "function_call"):
                        name = str(payload.get("name", "unknown"))
                        call_id = str(payload.get("call_id", ""))
                        output_call_names[call_id] = name
                        chars, byte_count = text_stats(payload.get("input", payload.get("arguments", "")))
                        bucket = totals["tool_calls"][name]
                        bucket["calls"] += 1
                        bucket["input_chars"] += chars
                        bucket["input_bytes"] += byte_count
                        serialized = json.dumps(payload.get("input", payload.get("arguments", "")), ensure_ascii=False)
                        totals["nested_tools"].update(TOOL_PATTERN.findall(serialized))
                        if name.startswith("mcp__"):
                            totals["mcp_direct_calls"][name.split("__", 2)[1]] += 1
                    elif item_type in ("custom_tool_call_output", "function_call_output"):
                        call_id = str(payload.get("call_id", ""))
                        name = output_call_names.get(call_id, "unattributed output")
                        chars, byte_count = text_stats(payload.get("output", ""))
                        bucket = totals["tool_calls"][name]
                        bucket["outputs"] += 1
                        bucket["output_chars"] += chars
                        bucket["output_bytes"] += byte_count
                elif kind == "event_msg":
                    event_type = payload_kind or str(payload.get("event", "unknown"))
                    totals["event_types"][event_type] += 1
                    if payload_kind == "token_count":
                        usage = usage_fields(payload)
                        if usage:
                            info = payload.get("info", {})
                            window = info.get("model_context_window") if isinstance(info, dict) else None
                            fallback_usage.append((str(record.get("timestamp", "")), ordinal, usage, window))
                elif kind == "token_usage_record":
                    usage = payload.get("usage")
                    if isinstance(usage, dict):
                        key = str(payload.get("response_id") or f"{path.name}:{ordinal}")
                        usage_by_id[key] = {
                            "usage": usage,
                            "thread_usage": payload.get("thread_token_usage"),
                            "window": payload.get("model_context_window"),
                            "timestamp": str(record.get("timestamp", "")),
                        }

                serialized = json.dumps(record, ensure_ascii=False)
                found_markers = [marker for marker in SKILL_MARKERS if marker.casefold() in serialized.casefold()]
                if found_markers:
                    totals["skill_marker_records"]["records"] += 1
                    totals["skill_marker_records"]["serialized_bytes"] += len(line.encode("utf-8"))
                    totals["skill_marker_records"]["markers"].update(found_markers)
        file_info["record_types"] = dict(file_info["record_types"])
        totals["files"].append(file_info)

    if usage_by_id:
        selected = list(usage_by_id.values())
        usage_source = "token_usage_record"
    else:
        # Older logs may only contain event_msg.token_count; these carry the
        # last call's delta plus cumulative totals. Deduplicate identical
        # adjacent snapshots conservatively.
        selected = []
        seen = set()
        for timestamp, ordinal, usage, window in fallback_usage:
            signature = tuple(sorted((k, v) for k, v in usage.items() if isinstance(v, (int, float))))
            if signature not in seen:
                selected.append({"usage": usage, "thread_usage": usage, "window": window, "timestamp": timestamp})
                seen.add(signature)
        usage_source = "event_msg.token_count.last_token_usage (deduplicated)" if selected else "not present"

    sums = collections.Counter()
    windows: list[int] = [row[3] for row in fallback_usage if isinstance(row[3], int)]
    peak_input = 0
    peak_total = 0
    latest_thread_usage: dict[str, Any] | None = None
    for row in selected:
        usage = row.get("usage") or {}
        for key in ("input_tokens", "cached_input_tokens", "cache_write_input_tokens", "output_tokens", "reasoning_output_tokens", "total_tokens"):
            value = usage.get(key)
            if isinstance(value, (int, float)):
                sums[key] += value
        peak_input = max(peak_input, int(usage.get("input_tokens", 0) or 0))
        peak_total = max(peak_total, int(usage.get("total_tokens", 0) or 0))
        if isinstance(row.get("window"), int):
            windows.append(row["window"])
        thread_usage = row.get("thread_usage")
        if isinstance(thread_usage, dict) and (latest_thread_usage is None or int(thread_usage.get("total_tokens", 0) or 0) >= int(latest_thread_usage.get("total_tokens", 0) or 0)):
            latest_thread_usage = thread_usage

    measured_files = []
    for path in measure_paths:
        if not path.is_file():
            raise FileNotFoundError(path)
        raw = path.read_bytes()
        try:
            text = raw.decode("utf-8")
            chars = len(text)
        except UnicodeDecodeError:
            chars = None
        resolved = path.resolve()
        try:
            display_path = resolved.relative_to(Path.cwd().resolve()).as_posix()
        except ValueError:
            try:
                display_path = "~/" + resolved.relative_to(Path.home().resolve()).as_posix()
            except ValueError:
                display_path = path.name
        measured_files.append({"file": display_path, "bytes": len(raw), "utf8_chars": chars, "approx_tokens_chars_div_4": math.ceil(chars / 4) if chars is not None else None})

    serializable = {
        "files": totals["files"],
        "file_count": len(files),
        "total_file_bytes": sum(item["bytes"] for item in totals["files"]),
        "total_jsonl_records": sum(item["records"] for item in totals["files"]),
        "record_types": dict(totals["record_types"]),
        "invalid_json_lines": totals["invalid_json_lines"],
        "message_roles": dict(totals["message_roles"]),
        "message_components": {k: v | {"approx_tokens_chars_div_4": math.ceil(v["chars"] / 4)} for k, v in totals["message_components"].items()},
        "tool_calls_and_outputs": {k: v | {"input_approx_tokens_chars_div_4": math.ceil(v["input_chars"] / 4), "output_approx_tokens_chars_div_4": math.ceil(v["output_chars"] / 4)} for k, v in totals["tool_calls"].items()},
        "nested_tool_names": dict(totals["nested_tools"]),
        "direct_mcp_server_calls": dict(totals["mcp_direct_calls"]),
        "event_types": dict(totals["event_types"]),
        "skill_marker_records": {"records": totals["skill_marker_records"]["records"], "serialized_bytes_overlapping_other_counts": totals["skill_marker_records"]["serialized_bytes"], "markers": dict(totals["skill_marker_records"]["markers"])},
        "usage_source": usage_source,
        "usage_records_counted": len(selected),
        "model_usage_sums_across_recorded_calls": dict(sums),
        "cached_input_fraction_of_recorded_input": sums["cached_input_tokens"] / sums["input_tokens"] if sums["input_tokens"] else None,
        "latest_or_max_cumulative_thread_usage": latest_thread_usage,
        "peak_single_call_input_tokens": peak_input,
        "peak_single_call_total_tokens": peak_total,
        "model_context_window_tokens": max(windows) if windows else None,
        "peak_input_window_ratio": peak_input / max(windows) if windows else None,
        "measured_files": measured_files,
        "limits": [
            "Logged input_tokens count the whole model input on that call; they cannot be apportioned exactly among skills, messages, tool schemas, and MCP definitions from rollout JSONL alone.",
            "Text component token figures are approximate ceil(Unicode characters / 4), not tokenizer counts.",
            "Skill markers are heuristic and overlapping; they do not prove how much of a skill was inserted into model context.",
            "MCP calls made inside a wrapper may only be represented as nested tool-name text or aggregated wrapper output; server schema/token overhead is not recorded here.",
            "This script reports only the paths supplied with --input and --measure; it does not crawl the whole profile by default.",
        ],
    }
    return serializable


def markdown(report: dict[str, Any]) -> str:
    lines = ["# Codex session context report", "", f"- Rollout files: {report['file_count']}", f"- JSONL records: {report['total_jsonl_records']}", f"- Raw file bytes: {report['total_file_bytes']:,}", f"- Recorded model calls counted: {report['usage_records_counted']} ({report['usage_source']})", ""]
    lines += ["## Recorded token usage", ""]
    for key, value in report["model_usage_sums_across_recorded_calls"].items():
        lines.append(f"- {key}: {value:,}")
    lines += [f"- Peak single-call input: {report['peak_single_call_input_tokens']:,}", f"- Context window: {report['model_context_window_tokens'] or 'not recorded'}", f"- Peak input / context window: {report['peak_input_window_ratio']:.1%}" if report["peak_input_window_ratio"] is not None else "- Peak input / context window: unavailable", f"- Cached input share across calls: {report['cached_input_fraction_of_recorded_input']:.1%}" if report["cached_input_fraction_of_recorded_input"] is not None else "- Cached input share: unavailable", ""]
    lines += ["## Serialized content sizes", "", "| Component | Records | Characters | UTF-8 bytes | Approx. tokens (chars / 4) |", "|---|---:|---:|---:|---:|"]
    for name, row in sorted(report["message_components"].items()):
        lines.append(f"| {name} | {row['records']} | {row['chars']:,} | {row['utf8_bytes']:,} | {row['approx_tokens_chars_div_4']:,} |")
    lines += ["", "## Tools and servers", ""]
    if report["tool_calls_and_outputs"]:
        lines += ["| Tool | Calls | Input bytes (approx tokens) | Output records | Output bytes (approx tokens) |", "|---|---:|---:|---:|---:|"]
        for name, row in sorted(report["tool_calls_and_outputs"].items()):
            lines.append(f"| {name} | {row['calls']} | {row['input_bytes']:,} ({row['input_approx_tokens_chars_div_4']:,} est.) | {row['outputs']} | {row['output_bytes']:,} ({row['output_approx_tokens_chars_div_4']:,} est.) |")
    else:
        lines.append("No tool calls were found in the supplied logs.")
    lines.append("")
    lines.append("Nested tools: " + (", ".join(f"{k} ({v})" for k, v in sorted(report["nested_tool_names"].items())) or "none recorded"))
    lines.append("Direct MCP server calls: " + (", ".join(f"{k} ({v})" for k, v in sorted(report["direct_mcp_server_calls"].items())) or "none found"))
    markers = report["skill_marker_records"]
    lines += ["", "## Skill markers in logged records", "", f"- Matching records: {markers['records']}", f"- Serialized bytes in matching records: {markers['serialized_bytes_overlapping_other_counts']:,} (overlaps message/tool totals; heuristic only)", "- Markers: " + (", ".join(f"{k} ({v})" for k, v in sorted(markers["markers"].items())) or "none found")]
    lines += ["", "## Additional measured files", ""]
    if report["measured_files"]:
        lines += ["| File | Bytes | UTF-8 characters | Approx. tokens (chars / 4) |", "|---|---:|---:|---:|"]
        for row in report["measured_files"]:
            chars = f"{row['utf8_chars']:,}" if row["utf8_chars"] is not None else "not UTF-8"
            tokens = f"{row['approx_tokens_chars_div_4']:,}" if row["approx_tokens_chars_div_4"] is not None else "unavailable"
            lines.append(f"| {row['file']} | {row['bytes']:,} | {chars} | {tokens} |")
    else:
        lines.append("No additional files were supplied with `--measure`.")
    lines += ["", "## Scope limits", ""]
    lines.extend(f"- {limit}" for limit in report["limits"])
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", action="append", type=Path, required=True, help="JSONL file or directory; repeatable")
    parser.add_argument("--measure", action="append", type=Path, default=[], help="Additional UTF-8 files such as skill documents; reports bytes and rough tokens only")
    parser.add_argument("--json", action="store_true", help="Write JSON instead of Markdown")
    parser.add_argument("--output", type=Path, help="Write report to a file instead of stdout")
    args = parser.parse_args()
    try:
        report = analyze(args.input, args.measure)
    except (OSError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    rendered = json.dumps(report, ensure_ascii=False, indent=2) + "\n" if args.json else markdown(report)
    if args.output:
        args.output.write_text(rendered, encoding="utf-8", newline="\n")
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
