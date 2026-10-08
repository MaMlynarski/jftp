param(
    [string]$PythonExe = $env:JFTP_CONTEXT7_PYTHON,
    [int]$Port = 8765
)

$ErrorActionPreference = 'Stop'
$repoRoot = (Resolve-Path (Join-Path $PSScriptRoot '..\..\..\..')).Path
$dataRoot = Join-Path $env:LOCALAPPDATA 'Codex\jftp-context7'
$database = Join-Path $dataRoot 'jftp.sqlite'
$backend = Join-Path $repoRoot '.agents\skills\legacy-codebase-workflows\scripts\context7_backend.py'

if (-not (Test-Path -LiteralPath $database)) {
    throw "Local index not found at '$database'. Run index-jftp-context7.ps1 first."
}
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

$listener = [System.Net.Sockets.TcpClient]::new()
try {
    $pending = $listener.BeginConnect('127.0.0.1', $Port, $null, $null)
    if ($pending.AsyncWaitHandle.WaitOne(500) -and $listener.Connected) {
        Write-Output "Context7 local server already listens at http://127.0.0.1:$Port"
        exit 0
    }
} finally {
    $listener.Dispose()
}

$stdout = Join-Path $dataRoot 'server.stdout.log'
$stderr = Join-Path $dataRoot 'server.stderr.log'
$arguments = @('-B', $backend, 'serve', '--database', $database, '--host', '127.0.0.1', '--port', "$Port")
$process = Start-Process -FilePath $PythonExe -ArgumentList $arguments -WorkingDirectory $repoRoot -WindowStyle Hidden -PassThru -RedirectStandardOutput $stdout -RedirectStandardError $stderr
Start-Sleep -Milliseconds 800
$listener = [System.Net.Sockets.TcpClient]::new()
try {
    $pending = $listener.BeginConnect('127.0.0.1', $Port, $null, $null)
    if (-not $pending.AsyncWaitHandle.WaitOne(1500) -or -not $listener.Connected) {
        throw "Context7 server did not start. See '$stderr'."
    }
} finally {
    $listener.Dispose()
}
Write-Output "Context7 local server running at http://127.0.0.1:$Port (PID $($process.Id))"
