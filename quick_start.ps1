# Quick Start Script - One Line Execution
# Usage: Right-click and "Run with PowerShell" or execute: .\quick_start.ps1

# Get current directory and start all services with minimal output
$ProjectRoot = Get-Location
& "$ProjectRoot\FastAPi\Scripts\Activate.ps1"
Start-Process powershell -ArgumentList "-NoExit", "-Command", "& '$ProjectRoot\FastAPi\Scripts\Activate.ps1'; cd '$ProjectRoot\django_backend'; python manage.py runserver 127.0.0.1:8002"
Start-Sleep 2
Start-Process powershell -ArgumentList "-NoExit", "-Command", "& '$ProjectRoot\FastAPi\Scripts\Activate.ps1'; cd '$ProjectRoot'; $ProjectRoot\FastAPi\Scripts\python.exe -m uvicorn index:app --reload --port 8000"
Start-Sleep 2  
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd '$ProjectRoot\react_frontend'; npm start"

Write-Host "🚀 All services are starting..." -ForegroundColor Green
Write-Host "Django: http://localhost:8002" -ForegroundColor Cyan
Write-Host "FastAPI: http://localhost:8000" -ForegroundColor Cyan  
Write-Host "React: http://localhost:3000" -ForegroundColor Cyan