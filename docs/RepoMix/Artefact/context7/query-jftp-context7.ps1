param(
    [Parameter(Mandatory = $true)][string]$Query,
    [ValidateSet('docs', 'library')][string]$Command = 'docs',
    [int]$Port = 8765
)

$ErrorActionPreference = 'Stop'
$dataRoot = Join-Path $env:LOCALAPPDATA 'Codex\jftp-context7'
$client = Join-Path $dataRoot 'client\node_modules\.bin\ctx7.cmd'
$xdg = Join-Path $dataRoot 'xdg'
if (-not (Test-Path -LiteralPath $client)) { throw "ctx7 CLI not found at '$client'." }

$env:XDG_CONFIG_HOME = Join-Path $xdg 'config'
$env:XDG_STATE_HOME = Join-Path $xdg 'state'
$env:XDG_CACHE_HOME = Join-Path $xdg 'cache'
$env:XDG_DATA_HOME = Join-Path $xdg 'data'
$env:CTX7_TELEMETRY_DISABLED = '1'
New-Item -ItemType Directory -Force -Path (Join-Path $env:XDG_CONFIG_HOME 'context7'),$env:XDG_STATE_HOME,$env:XDG_CACHE_HOME,$env:XDG_DATA_HOME | Out-Null
$credentials = Join-Path $env:XDG_CONFIG_HOME 'context7\credentials.json'
if (-not (Test-Path -LiteralPath $credentials)) { Set-Content -LiteralPath $credentials -Value '{}' -NoNewline }
$baseArgs = @('--base-url', "http://127.0.0.1:$Port")
if ($Command -eq 'library') {
    & $client @baseArgs library jftp $Query --json
} else {
    & $client @baseArgs docs /local/jftp $Query --json
}
if ($LASTEXITCODE -ne 0) { throw "Local Context7 query failed with exit code $LASTEXITCODE." }
