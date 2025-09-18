# Quick Start Script - One Line Execution
# Usage: Right-click and "Run with PowerShell" or execute: .\quick_start.ps1

# Start all services with minimal output
& "E:\FastApi\FastAPi\Scripts\Activate.ps1"
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd 'E:\FastApi\django_backend'; python manage.py runserver 127.0.0.1:8002"
Start-Sleep 2
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd 'E:\FastApi'; uvicorn index:app --reload --host 0.0.0.0 --port 8000"
Start-Sleep 2  
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd 'E:\FastApi\react_frontend'; npm start"

Write-Host "🚀 All services are starting..." -ForegroundColor Green
Write-Host "Django: http://localhost:8002" -ForegroundColor Cyan
Write-Host "FastAPI: http://localhost:8000" -ForegroundColor Cyan  
Write-Host "React: http://localhost:3000" -ForegroundColor Cyan