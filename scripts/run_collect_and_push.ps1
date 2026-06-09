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

function Get-DotEnvValue {
    param(
        [Parameter(Mandatory = $true)]
        [string] $Path,

        [Parameter(Mandatory = $true)]
        [string] $Key
    )

    if (-not (Test-Path $Path)) {
        return ""
    }

    foreach ($line in Get-Content $Path) {
        $trimmed = $line.Trim()
        if (-not $trimmed -or $trimmed.StartsWith("#")) {
            continue
        }
        $parts = $trimmed -split "=", 2
        if ($parts.Count -ne 2) {
            continue
        }
        if ($parts[0].Trim() -ne $Key) {
            continue
        }
        return $parts[1].Trim().Trim("'`"")
    }

    return ""
}

function Resolve-GamalyticKey {
    if ($env:GAMALYTIC_API_KEY) {
        return $env:GAMALYTIC_API_KEY
    }

    foreach ($envFile in @(
        (Join-Path $ProjectRoot ".env.local"),
        (Join-Path $ProjectRoot ".env")
    )) {
        $value = Get-DotEnvValue -Path $envFile -Key "GAMALYTIC_API_KEY"
        if ($value) {
            $env:GAMALYTIC_API_KEY = $value
            return $value
        }
    }

    return ""
}

Write-Host "============================================================"
Write-Host "[scheduled] started at $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"
Write-Host "[scheduled] project: $ProjectRoot"
Write-Host "[scheduled] run date: $RunDate"

$dirtyNewsData = git status --porcelain -- news_data
if ($dirtyNewsData) {
    Write-Host "[scheduled] news_data has local edits; refusing to mix scheduled output with existing news_data changes."
    Write-Host $dirtyNewsData
    exit 1
}

Invoke-Checked "git" @("pull", "--ff-only")

$collectorFailed = $false
$gamalyticKey = Resolve-GamalyticKey
$runnerArgs = @(
    "run_daily_collectors.py",
    "--preset",
    "yesterday",
    "--workers",
    "1",
    "--no-progress"
)

if (-not $gamalyticKey) {
    Write-Host "[scheduled] GAMALYTIC_API_KEY not found in env/.env.local/.env; skipping pc_rankings for this run."
    $runnerArgs += @("--sections", "industry_news,ai_trends,release_calendar,community_discourse,deep_analysis")
}

& $PythonExe @runnerArgs
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
