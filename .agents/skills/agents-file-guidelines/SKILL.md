---
name: agents-file-guidelines
description: Create or revise concise, project-specific AGENTS.md files using copy-first web or desktop templates. Use when establishing repository-wide and folder-scoped agent guidance for a software project.
---

# AGENTS.md authoring

Create guidance that tells every agent entering a project or folder what it cannot reliably infer from the code, standard conventions, or automatically loaded instructions. Keep it short, stable, and scoped. Put task-specific recipes in skills and detailed/project-changing facts in documentation.

## Choose a workflow

- For browser-based web applications, read [the web workflow](references/web-workflow.md) and use `assets/AGENTS.web.template.md`.
- For desktop applications, read [the desktop workflow](references/desktop-workflow.md) and use `assets/AGENTS.desktop.template.md`.
- For hybrid products, choose the workflow that governs the primary user experience; add only the other surface's genuinely universal verification requirements.
- Keep the templates' language and framework fields as placeholders until repository evidence and user preferences identify their values.

## Copy-first rule

Never write a root `AGENTS.md` from scratch. First copy the selected template byte-for-byte to the project's root `AGENTS.md`; only then edit that copied file to replace placeholders and remove irrelevant optional material. Do not combine template creation and project adaptation into one newly drafted file. Preserve the template itself unchanged unless the user asks to revise the reusable template.

When a nested file is warranted, first copy the same selected template byte-for-byte to the target folder's `AGENTS.md`. Then reduce that copy to concise instructions that **every agent working in that folder** needs. Keep the copy-first sequence even when most root workflow sections will be removed from the nested file.

## Scope and information rules

- Root guidance is for every agent entering the repository, regardless of task. Include project purpose/scope, user language preferences, stable non-obvious boundaries, documentation triggers, and the project's shared workflow.
- Nested guidance is for every agent entering that subtree. Include only durable local contracts, conventions, data boundaries, or test constraints that apply to all work there. If an instruction applies only to a particular task, place it in a relevant skill or documentation page instead.
- Create a nested file only when the folder has meaningful always-on guidance. Do not create files just to mirror the source tree.
- Do not spend space on standard language/framework layouts, ordinary package trees, routine commands that are easy to discover, or facts agents can infer directly from manifests and source.
- Describe only non-obvious layout exceptions. Keep detailed explanations, architecture, exact versions, mutable commands, runtime observations, and open investigations in project docs.
- Explain project documentation by **trigger**: say what task or uncertainty should cause an agent to open each page. Do not require loading the whole documentation set for every task.
- Do not list or link AGENTS/CLAUDE files to explain that they exist; folder-scoped instructions are loaded in scope. Avoid duplicating inherited root workflow in nested files.
- Never include a developer's username, machine path, local-only environment state, or workstation-specific assumptions. Use portable relative paths and placeholders. If a project genuinely requires an environment variable or platform-specific step, reference its maintained project documentation.
- Keep repository-facing content in the project's requested documentation language. Fill chat language and repository language from user preference or project convention, not from this generic template.
- Distinguish confirmed constraints from proposed decisions. Do not turn one observed issue into a universal rule or include speculative warnings.

## Authoring and review sequence

1. Identify whether the product is web or desktop and read only that workflow plus its matching template.
2. Inspect existing guidance, project docs, manifests/configuration, and only enough source to confirm durable non-obvious facts. Preserve compatible user instructions; do not silently discard existing guidance.
3. Copy the selected template exactly to the root and then adapt the copy. Populate placeholders with verified, stable project facts; leave detailed/changing values in docs.
4. Add documentation triggers based on real pages and their purpose. Do not invent requirements documents, commands, tools, environments, or testing infrastructure that do not exist.
5. Consider nested files one folder at a time. Add only universal-in-folder instructions and use the copy-first sequence for each file.
6. Review every line with two questions: “Would every agent in this scope need this every time?” and “Could an agent quickly discover this elsewhere?” Remove lines that fail the first or are already obvious under the second.
7. Check for stale exact versions, machine paths, usernames, standard directory inventories, duplicated instructions, conditional task recipes, and unsupported claims. Check links and placeholders, then validate skill/template structure when applicable.
8. Summarize created/updated files, what was intentionally omitted, and the checks actually performed. Do not run application tests or make application changes unless separately authorized.
