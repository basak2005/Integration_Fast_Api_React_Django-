@echo off
echo 🚀 Starting FastAPI-Django-React Application...
echo ===============================================

REM Start Django without virtual environment
echo 1️⃣ Starting Django Backend Server (Port 8002)...
start "Django Backend" cmd /k "cd django_backend && python manage.py runserver 127.0.0.1:8002"

REM Wait 3 seconds
timeout /t 3 /nobreak > nul

REM Start FastAPI Integration Layer
echo 2️⃣ Starting FastAPI Integration Layer (Port 8000)...
start "FastAPI Integration" cmd /k "call FastAPi\Scripts\activate.bat && FastAPi\Scripts\python.exe -m uvicorn index:app --reload --port 8000"

REM Wait 3 seconds  
timeout /t 3 /nobreak > nul

REM Start React Frontend
echo 3️⃣ Starting React Frontend (Port 3000)...
start "React Frontend" cmd /k "cd react_frontend && npm start"

echo.
echo ✅ All services are starting up!
echo 🌐 Access points:
echo    📱 React App:    http://localhost:3000
echo    🔗 FastAPI Docs: http://localhost:8000/docs
echo    ⚙️  Django Admin: http://localhost:8002/admin
echo.
echo 💡 Health Check: http://localhost:8000/api/integration/health
echo.
echo 🔴 Close the individual terminal windows to stop services
echo.

REM Optional: Open browser after 8 seconds
echo Opening React app in browser in 8 seconds...
timeout /t 8 /nobreak > nul
start http://localhost:3000

pause