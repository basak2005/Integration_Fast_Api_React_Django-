# PowerShell Script to Start the Complete FastAPI-Django-React Application
# Author: GitHub Copilot
# Description: Starts Django backend, FastAPI integration layer, and React frontend in separate terminals

Write-Host "🚀 Starting FastAPI-Django-React Application..." -ForegroundColor Green
Write-Host "===============================================" -ForegroundColor Cyan

# Define paths
$ProjectRoot = "E:\FastApi"
$VenvActivate = "$ProjectRoot\FastAPi\Scripts\Activate.ps1"
$DjangoPath = "$ProjectRoot\django_backend"
$ReactPath = "$ProjectRoot\react_frontend"

# Function to check if a port is available
function Test-Port {
    param([int]$Port)
    try {
        $connection = New-Object System.Net.Sockets.TcpClient
        $connection.Connect("localhost", $Port)
        $connection.Close()
        return $false  # Port is in use
    }
    catch {
        return $true   # Port is available
    }
}

# Check if required ports are available
Write-Host "🔍 Checking port availability..." -ForegroundColor Yellow

$portsToCheck = @(
    @{Port=8002; Service="Django Backend"},
    @{Port=8000; Service="FastAPI Integration"},
    @{Port=3000; Service="React Frontend"}
)

foreach ($portInfo in $portsToCheck) {
    if (-not (Test-Port $portInfo.Port)) {
        Write-Host "⚠️  Port $($portInfo.Port) is already in use by another process ($($portInfo.Service))" -ForegroundColor Red
        Write-Host "   Please stop the service or change the port configuration." -ForegroundColor Red
        exit 1
    }
}

Write-Host "✅ All ports are available!" -ForegroundColor Green
Write-Host ""

# Start Django Backend Server
Write-Host "1️⃣ Starting Django Backend Server (Port 8002)..." -ForegroundColor Cyan
$djangoCommand = "& '$VenvActivate'; cd '$DjangoPath'; python manage.py runserver 127.0.0.1:8002"
Start-Process powershell -ArgumentList "-NoExit", "-Command", $djangoCommand
Write-Host "   Django backend starting in new window..." -ForegroundColor Green

# Wait a bit for Django to start
Start-Sleep -Seconds 3

# Start FastAPI Integration Layer
Write-Host "2️⃣ Starting FastAPI Integration Layer (Port 8000)..." -ForegroundColor Cyan
$fastapiCommand = "& '$VenvActivate'; cd '$ProjectRoot'; uvicorn index:app --reload --host 0.0.0.0 --port 8000"
Start-Process powershell -ArgumentList "-NoExit", "-Command", $fastapiCommand
Write-Host "   FastAPI integration layer starting in new window..." -ForegroundColor Green

# Wait a bit for FastAPI to start
Start-Sleep -Seconds 3

# Start React Frontend
Write-Host "3️⃣ Starting React Frontend (Port 3000)..." -ForegroundColor Cyan
$reactCommand = "cd '$ReactPath'; npm start"
Start-Process powershell -ArgumentList "-NoExit", "-Command", $reactCommand
Write-Host "   React frontend starting in new window..." -ForegroundColor Green

# Wait for services to fully start
Write-Host ""
Write-Host "⏳ Waiting for all services to start up..." -ForegroundColor Yellow
Start-Sleep -Seconds 10

# Health check function
function Test-ServiceHealth {
    param([string]$Url, [string]$ServiceName)
    try {
        $response = Invoke-WebRequest -Uri $Url -Method GET -TimeoutSec 5
        if ($response.StatusCode -eq 200) {
            Write-Host "✅ $ServiceName is healthy" -ForegroundColor Green
            return $true
        }
    }
    catch {
        Write-Host "❌ $ServiceName is not responding" -ForegroundColor Red
        return $false
    }
}

# Perform health checks
Write-Host "🔍 Performing health checks..." -ForegroundColor Yellow
Write-Host ""

$djangoHealthy = Test-ServiceHealth "http://localhost:8002/api/notes/" "Django Backend"
$fastapiHealthy = Test-ServiceHealth "http://localhost:8000/api/integration/health" "FastAPI Integration"
$reactHealthy = Test-ServiceHealth "http://localhost:3000" "React Frontend"

Write-Host ""
Write-Host "📊 Service Status Summary:" -ForegroundColor Cyan
Write-Host "=========================" -ForegroundColor Cyan
Write-Host "Django Backend (8002):     $(if($djangoHealthy){'✅ Running'}else{'❌ Not Running'})" -ForegroundColor $(if($djangoHealthy){'Green'}else{'Red'})
Write-Host "FastAPI Integration (8000): $(if($fastapiHealthy){'✅ Running'}else{'❌ Not Running'})" -ForegroundColor $(if($fastapiHealthy){'Green'}else{'Red'})
Write-Host "React Frontend (3000):      $(if($reactHealthy){'✅ Running'}else{'❌ Not Running'})" -ForegroundColor $(if($reactHealthy){'Green'}else{'Red'})

Write-Host ""
if ($djangoHealthy -and $fastapiHealthy -and $reactHealthy) {
    Write-Host "🎉 All services are running successfully!" -ForegroundColor Green
    Write-Host ""
    Write-Host "📱 Access your application:" -ForegroundColor Cyan
    Write-Host "   React Frontend:        http://localhost:3000" -ForegroundColor White
    Write-Host "   FastAPI Integration:   http://localhost:8000" -ForegroundColor White
    Write-Host "   FastAPI Docs:          http://localhost:8000/docs" -ForegroundColor White
    Write-Host "   Django Backend:        http://localhost:8002/api/notes/" -ForegroundColor White
    Write-Host ""
    Write-Host "💡 Tip: Each service is running in its own terminal window for easy monitoring." -ForegroundColor Yellow
    
    # Ask if user wants to open browser
    $openBrowser = Read-Host "Would you like to open the React frontend in your default browser? (y/N)"
    if ($openBrowser -eq 'y' -or $openBrowser -eq 'Y') {
        Start-Process "http://localhost:3000"
        Write-Host "🌐 Opening React frontend in your default browser..." -ForegroundColor Green
    }
} else {
    Write-Host "⚠️  Some services failed to start. Please check the terminal windows for error details." -ForegroundColor Red
    Write-Host "   You may need to:" -ForegroundColor Yellow
    Write-Host "   - Install missing dependencies" -ForegroundColor Yellow
    Write-Host "   - Check port availability" -ForegroundColor Yellow
    Write-Host "   - Verify virtual environment setup" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "🛑 To stop all services, close the terminal windows or press Ctrl+C in each window." -ForegroundColor Yellow
Write-Host "Press any key to continue..." -ForegroundColor Gray
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")