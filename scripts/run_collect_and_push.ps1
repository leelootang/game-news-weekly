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

function Invoke-GitPullWithRetry {
    param(
        [int] $MaxAttempts = 3,
        [int] $DelaySeconds = 30
    )

    for ($attempt = 1; $attempt -le $MaxAttempts; $attempt++) {
        git pull --ff-only
        if ($LASTEXITCODE -eq 0) {
            return $true
        }
        Write-Host "[scheduled] git pull attempt $attempt/$MaxAttempts failed (exit $LASTEXITCODE)."
        if ($attempt -lt $MaxAttempts) {
            Write-Host "[scheduled] retrying git pull in $DelaySeconds s..."
            Start-Sleep -Seconds $DelaySeconds
        }
    }

    # Pull is only to sync other machines' commits; collection does not depend on
    # remote being current. Degrade to a warning and keep collecting so a transient
    # network blip no longer wipes out a whole day of data. The commit lands locally
    # and the push at the end (or the next scheduled run) will sync it upstream.
    Write-Host "[scheduled] git pull failed after $MaxAttempts attempts; continuing with collection (data will be committed locally and pushed later)."
    return $false
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

$pullOk = Invoke-GitPullWithRetry -MaxAttempts 3 -DelaySeconds 30

$collectorFailed = $false
# Steam 榜单板块已从日/周/月报下线,不再采集 pc_rankings(见 steamdb_rankings.py 保留但休眠)。
$runnerArgs = @(
    "run_daily_collectors.py",
    "--preset",
    "yesterday",
    "--sections",
    "industry_news,ai_trends,release_calendar,community_discourse,deep_analysis",
    "--workers",
    "1",
    "--no-progress"
)

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

    # If the initial pull failed, the network may have recovered during the
    # (multi-minute) collection; try once more so push can fast-forward.
    if (-not $pullOk) {
        Invoke-GitPullWithRetry -MaxAttempts 1 -DelaySeconds 0 | Out-Null
    }

    git push
    if ($LASTEXITCODE -ne 0) {
        # Do not hard-fail: the commit is safely on the local branch and the next
        # scheduled run (which pulls first) will push it upstream.
        Write-Host "[scheduled] git push failed (exit $LASTEXITCODE); commit retained locally and will be pushed on the next successful run."
        $collectorFailed = $true
    }
} else {
    throw "git diff --cached --quiet failed with exit code $LASTEXITCODE"
}

if ($collectorFailed) {
    Write-Host "[scheduled] finished with collector failures at $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"
    exit 1
}

Write-Host "[scheduled] finished at $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"
