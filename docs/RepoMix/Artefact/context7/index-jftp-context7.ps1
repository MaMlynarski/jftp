param([string]$PythonExe = $env:JFTP_CONTEXT7_PYTHON)

$ErrorActionPreference = 'Stop'
$repoRoot = (Resolve-Path (Join-Path $PSScriptRoot '..\..\..\..')).Path
$dataRoot = Join-Path $env:LOCALAPPDATA 'Codex\jftp-context7'
$database = Join-Path $dataRoot 'jftp.sqlite'
$backend = Join-Path $repoRoot '.agents\skills\legacy-codebase-workflows\scripts\context7_backend.py'

if (-not $PythonExe) {
    $candidate = Join-Path $env:LOCALAPPDATA 'Programs\Python\Python314\python.exe'
    if (Test-Path -LiteralPath $candidate) { $PythonExe = $candidate }
    else {
        $command = Get-Command python -ErrorAction SilentlyContinue
        if ($command) { $PythonExe = $command.Source }
    }
}
if (-not $PythonExe -or -not (Test-Path -LiteralPath $PythonExe)) {
    throw 'Set JFTP_CONTEXT7_PYTHON to a Python 3 executable or add python to PATH.'
}

New-Item -ItemType Directory -Force -Path $dataRoot | Out-Null
& $PythonExe -B $backend index $repoRoot --database $database --library-id /local/jftp --docs-root (Join-Path $repoRoot 'docs') --exclude mpc.json --exclude docs/RepoMix --exclude RepoMix --exclude docs/jftp-repomap.md --exclude jftp-repomap.md
if ($LASTEXITCODE -ne 0) { throw "Context7 indexing failed with exit code $LASTEXITCODE." }
