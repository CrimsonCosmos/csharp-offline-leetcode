# Usage: .\run.ps1 <problem number or part of the name> [--unordered] [--all] [--stop]
#   .\run.ps1 2
#   .\run.ps1 longest-substring
#   .\run.ps1 46 --unordered
param(
    [Parameter(Mandatory = $true, Position = 0)][string]$Query,
    [Parameter(ValueFromRemainingArguments = $true)][string[]]$Rest
)
$root = $PSScriptRoot
$dirs = Get-ChildItem -Path (Join-Path $root 'problems') -Directory | Select-Object -ExpandProperty Name

if ($Query -match '^\d+$') {
    $prefix = ('{0:D4}-' -f [int]$Query)
    $dir = $dirs | Where-Object { $_.StartsWith($prefix) } | Select-Object -First 1
} else {
    $dir = $dirs | Where-Object { $_ -like "*$Query*" } | Select-Object -First 1
}
if (-not $dir) { Write-Host "No problem matching '$Query'. See INDEX.md."; exit 2 }

Write-Host "== $dir"
dotnet run --project (Join-Path $root 'Practice') "-p:Problem=$dir" --nologo -v q -- (Join-Path (Join-Path $root 'problems') $dir) @Rest
exit $LASTEXITCODE
