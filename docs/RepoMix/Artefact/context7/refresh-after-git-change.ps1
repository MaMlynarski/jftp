param(
    [ValidateSet('commit', 'merge', 'checkout', 'rewrite')][string]$Event = 'commit',
    [string]$OldRevision,
    [string]$NewRevision,
    [string]$BranchCheckout
)

$ErrorActionPreference = 'Stop'
if ($Event -eq 'checkout' -and $BranchCheckout -ne '1') { exit 0 }
$repoRoot = (Resolve-Path (Join-Path $PSScriptRoot '..\..\..\..')).Path
$indexer = Join-Path $repoRoot 'docs\RepoMix\Artefact\context7\index-jftp-context7.ps1'
& $indexer
if ($LASTEXITCODE -ne 0) { throw "Automatic Context7 refresh failed after Git $Event." }
