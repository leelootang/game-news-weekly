<#
Run the previous-day collectors locally, then commit and push news_data changes.

This script is intended for the Windows scheduled task registered by
scripts/register_scheduled_task.ps1.
#>

$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest

$ProjectRoot = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$PythonExe = (Get-Command python).Source
$RunDate = (Get-Date).AddDays(-1).ToString("yyyy-MM-dd")

Set-Location $ProjectRoot
$env:PYTHONUTF8 = "1"
$env:PYTHONIOENCODING = "utf-8"

function Invoke-Checked {
    param(
        [Parameter(Mandatory = $true)]
        [string] $FilePath,

        [Parameter(Mandatory = $true)]
        [string[]] $Arguments
    )

    & $FilePath @Arguments
    if ($LASTEXITCODE -ne 0) {
        throw "Command failed with exit code ${LASTEXITCODE}: $FilePath $($Arguments -join ' ')"
    }
}

Write-Host "============================================================"
Write-Host "[scheduled] started at $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"
Write-Host "[scheduled] project: $ProjectRoot"
Write-Host "[scheduled] run date: $RunDate"

$dirtyBefore = git status --porcelain
if ($dirtyBefore) {
    Write-Host "[scheduled] working tree is not clean; refusing to mix scheduled output with local edits."
    Write-Host $dirtyBefore
    exit 1
}

Invoke-Checked "git" @("pull", "--ff-only")

$collectorFailed = $false

& $PythonExe @(
    "run_daily_collectors.py",
    "--preset",
    "yesterday",
    "--workers",
    "1",
    "--no-progress"
)
if ($LASTEXITCODE -ne 0) {
    $collectorFailed = $true
    Write-Host "[scheduled] collector runner exited with code $LASTEXITCODE; continuing to index and push collected data."
}

Invoke-Checked $PythonExe @("scripts/build_article_indexes.py")

Invoke-Checked "git" @("add", "news_data")

git diff --cached --quiet
if ($LASTEXITCODE -eq 0) {
    Write-Host "[scheduled] no news_data changes to commit."
} elseif ($LASTEXITCODE -eq 1) {
    if ($collectorFailed) {
        Invoke-Checked "git" @("commit", "-m", "Collect game news for $RunDate (partial)")
    } else {
        Invoke-Checked "git" @("commit", "-m", "Collect game news for $RunDate")
    }
    Invoke-Checked "git" @("push")
} else {
    throw "git diff --cached --quiet failed with exit code $LASTEXITCODE"
}

if ($collectorFailed) {
    Write-Host "[scheduled] finished with collector failures at $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"
    exit 1
}

Write-Host "[scheduled] finished at $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"
