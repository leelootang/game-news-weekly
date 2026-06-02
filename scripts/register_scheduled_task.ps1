<#
Register a Windows scheduled task that runs the daily collectors every morning
at 08:00 for the previous day's window.

Usage (run from an elevated PowerShell):
    powershell -ExecutionPolicy Bypass -File scripts\register_scheduled_task.ps1

To remove the task:
    Unregister-ScheduledTask -TaskName "AIGameIndustry_DailyCollectors" -Confirm:$false
#>

$ErrorActionPreference = "Stop"

$TaskName    = "AIGameIndustry_DailyCollectors"
$ProjectRoot = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$PythonExe   = (Get-Command python).Source
$RunnerPath  = Join-Path $ProjectRoot "run_daily_collectors.py"
$LogDir      = Join-Path $ProjectRoot "collector_logs\scheduled"
$LogFile     = Join-Path $LogDir "scheduled_run.log"

if (-not (Test-Path $LogDir)) {
    New-Item -ItemType Directory -Path $LogDir | Out-Null
}

# Wrap python in cmd.exe so we can redirect stdout/stderr to a rolling log file.
$CmdArgs = "/c `"`"$PythonExe`" `"$RunnerPath`" --preset yesterday --workers 4 --no-progress >> `"$LogFile`" 2>&1`""

$Action = New-ScheduledTaskAction `
    -Execute "cmd.exe" `
    -Argument $CmdArgs `
    -WorkingDirectory $ProjectRoot

$Trigger = New-ScheduledTaskTrigger -Daily -At 08:00

# Settings:
#   - StartWhenAvailable: if the PC was off/asleep at 08:00, run as soon as possible after wake/boot.
#   - WakeToRun: try to wake the PC from sleep to run the task (requires power plan allows wake timers).
#   - ExecutionTimeLimit: cap one run at 2h so a stuck collector won't keep the task busy forever.
#   - DontStopIfGoingOnBatteries / AllowStartIfOnBatteries: keep running on laptops not plugged in.
$Settings = New-ScheduledTaskSettingsSet `
    -StartWhenAvailable `
    -WakeToRun `
    -AllowStartIfOnBatteries `
    -DontStopIfGoingOnBatteries `
    -ExecutionTimeLimit (New-TimeSpan -Hours 2) `
    -MultipleInstances IgnoreNew

# Run as the current interactive user so Playwright / Chromium can use the existing
# user profile. S4U logon means no stored password is required, but the task will
# only run when the user is logged in (or after the next login if missed).
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
    -Description "Daily 08:00 run of run_daily_collectors.py for the previous day." | Out-Null

Write-Host "Registered scheduled task '$TaskName'."
Write-Host "  Project root : $ProjectRoot"
Write-Host "  Python       : $PythonExe"
Write-Host "  Log file     : $LogFile"
Write-Host ""
Write-Host "Run it now to verify:"
Write-Host "  Start-ScheduledTask -TaskName $TaskName"
Write-Host "  Get-ScheduledTaskInfo -TaskName $TaskName"
