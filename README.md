# FastAPI-Django-React Microservice Application

A modern full-stack microservice application built with FastAPI, Django, and React.

## 🏗️ Architecture

This application follows a microservice architecture with three main services:

1. **Django Backend** (Port 8002) - Data persistence and REST API
2. **FastAPI Integration Layer** (Port 8000) - API Gateway and service orchestration  
3. **React Frontend** (Port 3000) - User interface

```
React Frontend (3000) ↔️ FastAPI Integration (8000) ↔️ Django Backend (8002)
```

## Project Structure

```
IntegrationFastapi+react+django/
├── django_backend/           # Django backend application
│   ├── manage.py
│   ├── requirements.txt
│   ├── db.sqlite3           # SQLite database
│   ├── django_backend/      # Django project settings
│   └── notes/              # Django notes app
├── react_frontend/          # React frontend application
│   ├── package.json
│   ├── public/
│   └── src/
├── FastAPi/                 # Python virtual environment
│   ├── Scripts/            # Virtual environment scripts
│   └── Lib/               # Virtual environment libraries
├── routes/
│   ├── note.py             # Original FastAPI routes (HTML)
│   └── integration.py      # New integration routes (JSON API)
├── models/                 # Data models
├── schemas/                # Pydantic schemas
├── config/                 # Configuration files
├── templates/              # HTML templates
├── static/                 # Static files
├── index.py                # FastAPI main application
├── start_all_services.bat  # Automated startup script (Windows)
├── quick_start.ps1         # PowerShell quick start script
└── README.md              # This file
```

## Setup Instructions

### 1. Setup Django Backend

```bash
cd django_backend

# Install Django requirements
pip install -r requirements.txt

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser (optional)
python manage.py createsuperuser

# Run Django server on port 8002
python manage.py runserver 127.0.0.1:8002
```

### 2. Setup FastAPI Integration Layer

```bash
# From main directory (FastApi/)
# Make sure you have the virtual environment activated
.\FastAPi\Scripts\activate

# Install additional requirements
pip install httpx

# Run FastAPI server on port 8000
uvicorn index:app --reload --port 8000
```

### 3. Setup React Frontend

```bash
cd react_frontend

# Install Node.js dependencies
npm install

# Start React development server on port 3000
npm start
```

## Usage

### Quick Start (Automated)

**Option 1: Use the automated startup script (Recommended)**
```bash
# Simply run the batch file to start all services
start_all_services.bat
```

This will automatically:
- Start Django Backend on port 8002 (without virtual environment)
- Start FastAPI Integration Layer on port 8000 (with virtual environment)
- Start React Frontend on port 3000
- Open your browser to the React app

**Option 2: Manual startup** (in separate terminal windows):
   - Django: `cd django_backend && python manage.py runserver 127.0.0.1:8002`
   - FastAPI: `call FastAPi\Scripts\activate.bat && uvicorn index:app --reload --port 8000`
   - React: `cd react_frontend && npm start`

### Access Points
   - 📱 React Frontend: http://localhost:3000
   - 🔗 FastAPI Docs: http://localhost:8000/docs
   - ⚙️ Django Admin: http://localhost:8002/admin
   - 💡 Health Check: http://localhost:8000/api/integration/health

3. **Create, edit, and delete notes** through the React interface

## API Endpoints

### FastAPI Integration Layer (Port 8000)
- `GET /api/integration/notes` - Get all notes
- `POST /api/integration/notes` - Create new note
- `GET /api/integration/notes/{id}` - Get specific note
- `PUT /api/integration/notes/{id}` - Update note
- `DELETE /api/integration/notes/{id}` - Delete note
- `GET /api/integration/health` - Health check

### Django Backend (Port 8002)
- `GET /api/notes/` - Get all notes
- `POST /api/notes/` - Create new note
- `GET /api/notes/{id}/` - Get specific note
- `PATCH /api/notes/{id}/` - Update note
- `DELETE /api/notes/{id}/` - Delete note

## Technologies Used

- **Frontend**: React 18, Axios, CSS3
- **Integration**: FastAPI, httpx, Pydantic
- **Backend**: Django 4.2, Django REST Framework
- **Database**: SQLite (can be changed to PostgreSQL/MySQL)

## Features

- ✅ Full CRUD operations for notes
- ✅ Real-time communication between all layers
- ✅ Error handling and loading states
- ✅ Responsive design
- ✅ Important notes highlighting
- ✅ Health monitoring
- ✅ CORS properly configured
- ✅ Form validation

## Troubleshooting

1. **Connection errors**: Make sure all servers are running on correct ports
2. **CORS issues**: Check FastAPI CORS settings in `index.py`
3. **Database issues**: Run Django migrations
4. **Node modules issues**: Delete `node_modules` and run `npm install`

## Next Steps

- Add authentication and authorization
- Implement WebSocket for real-time updates
- Add file upload functionality
- Deploy to cloud platforms
- Add comprehensive testing




### Available Startup Scripts:

#### 1. start_all_services.bat (Recommended - Windows Batch)
**Features:** Automated startup script for all services
**Usage:** Double-click the file or run from command prompt
```batch
start_all_services.bat
```
**Benefits:**
✅ Starts all three services automatically
✅ Django runs without virtual environment (system Python)
✅ FastAPI runs with virtual environment activation
✅ Opens separate terminal windows for monitoring
✅ Automatically opens browser to React app
✅ No PowerShell execution policy issues
✅ Works on any Windows system

#### 2. quick_start.ps1 (PowerShell - Fast Launch)
**Features:** Minimal PowerShell script for quick startup
**Usage:** Right-click → "Run with PowerShell" or execute
```powershell
.\quick_start.ps1
```
**Benefits:**
✅ Fastest startup (minimal output)
✅ PowerShell-based execution
✅ Quick launch without extra checks

### 🚀 How to Use:

**Option 1: Automated Batch Script (Recommended)**
```cmd
start_all_services.bat
```

**Option 2: PowerShell Quick Start**
```powershell
.\quick_start.ps1
```

### 📋 What the Scripts Do:
- **Django Backend:** Starts on port 8002 using system Python (no virtual environment)
- **FastAPI Integration:** Starts on port 8000 with virtual environment (`FastAPi\Scripts\activate.bat`)
- **React Frontend:** Starts on port 3000 using npm
- Opens separate terminal windows for each service (for monitoring)
- Automatically opens browser to React app after 8 seconds

### 💡 Recommended Usage:
- **For daily development:** Use `start_all_services.bat` (comprehensive and reliable)
- **For quick testing:** Use `quick_start.ps1` (minimal and fast)
- **For troubleshooting:** Use manual startup commands to isolate issues

**All scripts will start your complete application stack with just one command!**