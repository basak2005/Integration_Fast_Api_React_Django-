# Quick Start Script - Run All Three Services
# Usage: .\start_all_services.ps1

Write-Host "🚀 Starting FastAPI-Django-React Application..." -ForegroundColor Green
Write-Host "===============================================" -ForegroundColor Cyan

# Get current directory
$ProjectRoot = Get-Location
$VenvActivate = "$ProjectRoot\FastAPi\Scripts\Activate.ps1"

# Activate virtual environment
Write-Host "🔧 Activating virtual environment..." -ForegroundColor Yellow
& $VenvActivate

# Start Django Backend Server
Write-Host "1️⃣ Starting Django Backend Server (Port 8002)..." -ForegroundColor Cyan
Start-Process powershell -ArgumentList "-NoExit", "-Command", "& '$VenvActivate'; cd '$ProjectRoot\django_backend'; python manage.py runserver 127.0.0.1:8002"

# Wait for Django to start
Start-Sleep -Seconds 3

# Start FastAPI Integration Layer  
Write-Host "2️⃣ Starting FastAPI Integration Layer (Port 8000)..." -ForegroundColor Cyan
Start-Process powershell -ArgumentList "-NoExit", "-Command", "& '$VenvActivate'; cd '$ProjectRoot'; E:/IntegrationFastapi+react+django/FastAPi/Scripts/python.exe -m uvicorn index:app --reload --port 8000"

# Wait for FastAPI to start
Start-Sleep -Seconds 3

# Start React Frontend
Write-Host "3️⃣ Starting React Frontend (Port 3000)..." -ForegroundColor Cyan
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd '$ProjectRoot\react_frontend'; npm start"

# Wait a bit for React to start
Start-Sleep -Seconds 5

Write-Host ""
Write-Host "✅ All services are starting up!" -ForegroundColor Green
Write-Host "🌐 Access points:" -ForegroundColor Cyan
Write-Host "   📱 React App:    http://localhost:3000" -ForegroundColor White
Write-Host "   🔗 FastAPI Docs: http://localhost:8000/docs" -ForegroundColor White  
Write-Host "   ⚙️  Django Admin: http://localhost:8002/admin" -ForegroundColor White
Write-Host ""
Write-Host "💡 Health Check: http://localhost:8000/api/integration/health" -ForegroundColor Yellow
Write-Host ""
Write-Host "🔴 To stop all services, close the terminal windows or press Ctrl+C in each" -ForegroundColor Red

# Optional: Open browser
$openBrowser = Read-Host "Open React app in browser? (y/n)"
if ($openBrowser -eq "y" -or $openBrowser -eq "Y") {
    Start-Sleep -Seconds 5
    Start-Process "http://localhost:3000"
}