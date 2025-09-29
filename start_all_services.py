#!/usr/bin/env python3
"""
Cross-platform startup script for FastAPI-Django-React Application
Usage: python start_all_services.py
"""

import os
import sys
import time
import subprocess
import platform
from pathlib import Path

def colored_print(text, color="white"):
    """Print colored text"""
    colors = {
        "red": "\033[91m",
        "green": "\033[92m", 
        "yellow": "\033[93m",
        "blue": "\033[94m",
        "magenta": "\033[95m",
        "cyan": "\033[96m",
        "white": "\033[97m",
        "reset": "\033[0m"
    }
    print(f"{colors.get(color, colors['white'])}{text}{colors['reset']}")

def main():
    colored_print("🚀 Starting FastAPI-Django-React Application...", "green")
    colored_print("=" * 50, "cyan")
    
    # Get project root directory
    project_root = Path.cwd()
    venv_path = project_root / "FastAPi"
    
    # Determine OS-specific commands
    is_windows = platform.system() == "Windows"
    
    if is_windows:
        python_exe = venv_path / "Scripts" / "python.exe"
        activate_cmd = f'"{venv_path / "Scripts" / "activate"}"'
        terminal_cmd = "start"
        shell_arg = "cmd /k"
    else:
        python_exe = venv_path / "bin" / "python"
        activate_cmd = f"source {venv_path / 'bin' / 'activate'}"
        terminal_cmd = "gnome-terminal" if os.system("which gnome-terminal") == 0 else "xterm"
        shell_arg = "-e"
    
    # Check if virtual environment exists
    if not python_exe.exists():
        colored_print("❌ Virtual environment not found!", "red")
        colored_print(f"Expected: {python_exe}", "red")
        sys.exit(1)
    
    colored_print("🔧 Virtual environment found!", "yellow")
    
    try:
        # Start Django Backend
        colored_print("1️⃣ Starting Django Backend Server (Port 8002)...", "cyan")
        django_cmd = f'{activate_cmd} && cd "{project_root}/django_backend" && python manage.py runserver 127.0.0.1:8002'
        
        if is_windows:
            subprocess.Popen(f'start "Django Backend" cmd /k "{activate_cmd} && cd django_backend && python manage.py runserver 127.0.0.1:8002"', shell=True)
        else:
            subprocess.Popen([terminal_cmd, shell_arg, f'bash -c "{django_cmd}"'])
        
        time.sleep(3)
        
        # Start FastAPI Integration Layer
        colored_print("2️⃣ Starting FastAPI Integration Layer (Port 8000)...", "cyan")
        fastapi_cmd = f'{activate_cmd} && "{python_exe}" -m uvicorn index:app --reload --port 8000'
        
        if is_windows:
            subprocess.Popen(f'start "FastAPI Integration" cmd /k "{activate_cmd} && {python_exe} -m uvicorn index:app --reload --port 8000"', shell=True)
        else:
            subprocess.Popen([terminal_cmd, shell_arg, f'bash -c "{fastapi_cmd}"'])
        
        time.sleep(3)
        
        # Start React Frontend
        colored_print("3️⃣ Starting React Frontend (Port 3000)...", "cyan")
        react_cmd = f'cd "{project_root}/react_frontend" && npm start'
        
        if is_windows:
            subprocess.Popen(f'start "React Frontend" cmd /k "cd react_frontend && npm start"', shell=True)
        else:
            subprocess.Popen([terminal_cmd, shell_arg, f'bash -c "{react_cmd}"'])
        
        time.sleep(5)
        
        # Success message
        colored_print("", "white")
        colored_print("✅ All services are starting up!", "green")
        colored_print("🌐 Access points:", "cyan")
        colored_print("   📱 React App:    http://localhost:3000", "white")
        colored_print("   🔗 FastAPI Docs: http://localhost:8000/docs", "white")
        colored_print("   ⚙️  Django Admin: http://localhost:8002/admin", "white")
        colored_print("", "white")
        colored_print("💡 Health Check: http://localhost:8000/api/integration/health", "yellow")
        colored_print("", "white")
        colored_print("🔴 Close the terminal windows to stop services", "red")
        
        # Optional browser opening
        try:
            import webbrowser
            open_browser = input("Open React app in browser? (y/n): ").lower()
            if open_browser in ['y', 'yes']:
                time.sleep(5)
                webbrowser.open('http://localhost:3000')
        except KeyboardInterrupt:
            colored_print("\n👋 Startup complete!", "green")
            
    except Exception as e:
        colored_print(f"❌ Error starting services: {e}", "red")
        sys.exit(1)

if __name__ == "__main__":
    main()