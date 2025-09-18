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
FastApi/
├── django_backend/           # Django backend application
│   ├── manage.py
│   ├── requirements.txt
│   ├── django_backend/       # Django project settings
│   └── notes/               # Django notes app
├── react_frontend/          # React frontend application
│   ├── package.json
│   ├── public/
│   └── src/
├── routes/
│   ├── note.py             # Original FastAPI routes (HTML)
│   └── integration.py      # New integration routes (JSON API)
├── index.py                # FastAPI main application
└── requirements.txt        # FastAPI requirements
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

# Run Django server on port 8001
python manage.py runserver 8001
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

1. **Start all three servers** (in separate terminal windows):
   - Django: `python manage.py runserver 8001`
   - FastAPI: `uvicorn index:app --reload --port 8000`
   - React: `npm start`

2. **Access the application**:
   - React Frontend: http://localhost:3000
   - FastAPI Docs: http://localhost:8000/docs
   - Django Admin: http://localhost:8001/admin

3. **Create, edit, and delete notes** through the React interface

## API Endpoints

### FastAPI Integration Layer (Port 8000)
- `GET /api/integration/notes` - Get all notes
- `POST /api/integration/notes` - Create new note
- `GET /api/integration/notes/{id}` - Get specific note
- `PUT /api/integration/notes/{id}` - Update note
- `DELETE /api/integration/notes/{id}` - Delete note
- `GET /api/integration/health` - Health check

### Django Backend (Port 8001)
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
1. start_app.ps1 (Recommended - Full Featured)
Features: Comprehensive PowerShell script with health checks, port verification, colored output
Usage: Right-click → "Run with PowerShell" or start_app.ps1
Benefits:
✅ Checks port availability before starting
✅ Performs health checks after startup
✅ Colored status output
✅ Optional browser opening
✅ Detailed error reporting
2. start_app.bat (Windows Batch - Simple)
Features: Simple batch file for Windows
Usage: Double-click the file or run from command prompt
Benefits:
✅ No PowerShell execution policy issues
✅ Works on any Windows system
✅ Simple and reliable
3. start_app.py (Cross-platform Python)
Features: Advanced Python script with cross-platform support
Usage: python start_app.py
Benefits:
✅ Works on Windows, Mac, Linux
✅ Advanced health checking
✅ Colored terminal output
✅ Concurrent service management
4. quick_start.ps1 (Minimal - Fast Launch)
Features: Minimal script for quick startup
Usage: quick_start.ps1
Benefits:
✅ Fastest startup (no checks)
✅ Minimal output
✅ Just starts everything
### 🚀 How to Use:
## Option 1: Full Featured (Recommended)
```
cd E:\FastApi
.\start_app.ps1
```
## Option 2: Simple Batch
```
cd E:\FastApi
start_app.bat
```
## Option 3: Python Cross-platform
```
cd E:\FastApi
python start_app.py
```
## Option 4: Quick Launch
```
cd E:\FastApi
.\quick_start.ps1
```
<br>
📋 What Each Script Does:
Activates the Python virtual environment (FastAPi)
Starts Django backend server on port 8002
Starts FastAPI integration layer on port 8000
Starts React frontend on port 3000
Opens separate terminal windows for each service (for monitoring)
Performs health checks (in full versions)
Optionally opens browser to React app
💡 Recommended Usage:
For daily development: Use start_app.ps1 (full featured)
For quick testing: Use quick_start.ps1 (minimal)
For CI/CD or automation: Use start_app.py (programmatic)
For compatibility: Use start_app.bat (simple batch)
All scripts will start your complete application stack with just one command!