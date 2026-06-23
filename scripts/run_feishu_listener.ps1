# Keeps the Feishu subscribe listener running, restarting it if it ever exits.
# Intended to be launched by a Windows Scheduled Task at logon.
$ErrorActionPreference = "Continue"
$root = Split-Path -Parent $PSScriptRoot
Set-Location $root

$python = "C:\Users\Admin\AppData\Local\Programs\Python\Python314\python.exe"
if (-not (Test-Path $python)) { $python = "python" }

$env:PYTHONUTF8 = "1"
$env:PYTHONIOENCODING = "utf-8"

$logDir = Join-Path $root "logs"
if (-not (Test-Path $logDir)) { New-Item -ItemType Directory -Path $logDir | Out-Null }
$log = Join-Path $logDir "feishu_listener.log"

while ($true) {
    $ts = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    Add-Content -Path $log -Value "[$ts] starting feishu_subscribe_listener.py" -Encoding utf8
    & $python "scripts\feishu_subscribe_listener.py" *>> $log
    $code = $LASTEXITCODE
    $ts = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    Add-Content -Path $log -Value "[$ts] listener exited (code $code); restarting in 10s" -Encoding utf8
    Start-Sleep -Seconds 10
}
