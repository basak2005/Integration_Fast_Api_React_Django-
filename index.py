from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from routes.note import note
from routes.integration import integration_router
from fastapi.staticfiles import StaticFiles

app = FastAPI(
    title="FastAPI Integration Layer",
    description="FastAPI service that integrates Django backend with React frontend",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],  # React frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")

# Add a route to serve the demo HTML
@app.get("/demo")
async def demo_page():
    """Serve the integration demo HTML page"""
    with open("frontend_demo.html", "r", encoding="utf-8") as f:
        html_content = f.read()
    return HTMLResponse(content=html_content)

# Include routers
app.include_router(note)  # Original note routes (for HTML templates)
app.include_router(integration_router)  # New integration routes