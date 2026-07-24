<#
Register the daily 11:00 Feishu report-feedback sync task.
#>

$ErrorActionPreference = "Stop"

$TaskName = "FeishuReportFeedbackSync"
$ProjectRoot = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$Python = "C:\Users\Admin\AppData\Local\Programs\Python\Python314\python.exe"
$SyncScript = Join-Path $ProjectRoot "scripts\sync_feishu_report_feedback.py"
$LogDir = Join-Path $ProjectRoot "logs"
$LogFile = Join-Path $LogDir "feishu_feedback_sync.log"

if (-not (Test-Path $LogDir)) {
    New-Item -ItemType Directory -Path $LogDir | Out-Null
}

$CmdArgs = "/c `"`"$Python`" `"$SyncScript`" >> `"$LogFile`" 2>&1`""
$Action = New-ScheduledTaskAction `
    -Execute "cmd.exe" `
    -Argument $CmdArgs `
    -WorkingDirectory $ProjectRoot
$Trigger = New-ScheduledTaskTrigger -Daily -At 11:00
$Settings = New-ScheduledTaskSettingsSet `
    -StartWhenAvailable `
    -WakeToRun `
    -AllowStartIfOnBatteries `
    -DontStopIfGoingOnBatteries `
    -ExecutionTimeLimit (New-TimeSpan -Minutes 15) `
    -MultipleInstances IgnoreNew
$Principal = New-ScheduledTaskPrincipal `
    -UserId ([System.Security.Principal.WindowsIdentity]::GetCurrent().Name) `
    -LogonType S4U `
    -RunLevel Limited

if (Get-ScheduledTask -TaskName $TaskName -ErrorAction SilentlyContinue) {
    Unregister-ScheduledTask -TaskName $TaskName -Confirm:$false
}

Register-ScheduledTask `
    -TaskName $TaskName `
    -Action $Action `
    -Trigger $Trigger `
    -Settings $Settings `
    -Principal $Principal `
    -Description "Daily 11:00 append new report feedback to the Feishu Wiki feedback table." |
    Out-Null

Write-Host "Registered scheduled task '$TaskName' at 11:00."
