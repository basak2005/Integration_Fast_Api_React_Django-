# FastAPI Integration Layer Routes - Integration with Django Backend
from fastapi import APIRouter, HTTPException
from typing import List, Optional
from pydantic import BaseModel
import httpx
from datetime import datetime

# Pydantic models for request/response
class NoteCreate(BaseModel):
    title: str
    desc: str
    note: str
    important: bool = False

class NoteUpdate(BaseModel):
    title: Optional[str] = None
    desc: Optional[str] = None
    note: Optional[str] = None
    important: Optional[bool] = None

class NoteResponse(BaseModel):
    id: str
    title: str
    desc: str
    note: str
    important: bool
    created_at: str

# FastAPI router
integration_router = APIRouter(prefix="/api/integration", tags=["Integration Layer"])

@integration_router.get("/notes", response_model=List[dict])
async def get_all_notes():
    """
    Get all notes from Django backend
    """
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get("http://localhost:8002/api/notes/")
            if response.status_code == 200:
                notes = response.json()
                # Transform to match expected format
                transformed_notes = []
                for note in notes:
                    transformed_notes.append({
                        "id": str(note["id"]),
                        "title": note["title"],
                        "desc": note["desc"],
                        "note": note["note"],
                        "important": note["important"],
                        "created_at": str(note["created_at"])
                    })
                return transformed_notes
            else:
                raise HTTPException(status_code=response.status_code, detail="Failed to fetch notes from Django")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")

@integration_router.post("/notes", response_model=dict)
async def create_note(note: NoteCreate):
    """
    Create a new note in Django backend
    """
    try:
        async with httpx.AsyncClient() as client:
            data = {
                "title": note.title,
                "desc": note.desc,
                "note": note.note,
                "important": note.important
            }
            response = await client.post("http://localhost:8002/api/notes/", json=data)
            if response.status_code == 201:
                created_note = response.json()
                return {
                    "id": str(created_note["id"]),
                    "title": created_note["title"],
                    "desc": created_note["desc"],
                    "note": created_note["note"],
                    "important": created_note["important"],
                    "created_at": str(created_note["created_at"])
                }
            else:
                raise HTTPException(status_code=response.status_code, detail="Failed to create note")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")

@integration_router.get("/notes/{note_id}", response_model=dict)
async def get_note(note_id: str):
    """
    Get a specific note from Django backend
    """
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"http://localhost:8002/api/notes/{note_id}/")
            if response.status_code == 200:
                note = response.json()
                return {
                    "id": str(note["id"]),
                    "title": note["title"],
                    "desc": note["desc"],
                    "note": note["note"],
                    "important": note["important"],
                    "created_at": str(note["created_at"])
                }
            elif response.status_code == 404:
                raise HTTPException(status_code=404, detail="Note not found")
            else:
                raise HTTPException(status_code=response.status_code, detail="Failed to fetch note")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")

@integration_router.put("/notes/{note_id}", response_model=dict)
async def update_note(note_id: str, note: NoteUpdate):
    """
    Update a note in Django backend
    """
    try:
        async with httpx.AsyncClient() as client:
            data = {k: v for k, v in note.dict().items() if v is not None}
            response = await client.put(f"http://localhost:8002/api/notes/{note_id}/", json=data)
            if response.status_code == 200:
                updated_note = response.json()
                return {
                    "id": str(updated_note["id"]),
                    "title": updated_note["title"],
                    "desc": updated_note["desc"],
                    "note": updated_note["note"],
                    "important": updated_note["important"],
                    "created_at": str(updated_note["created_at"])
                }
            elif response.status_code == 404:
                raise HTTPException(status_code=404, detail="Note not found")
            else:
                raise HTTPException(status_code=response.status_code, detail="Failed to update note")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")

@integration_router.delete("/notes/{note_id}")
async def delete_note(note_id: str):
    """
    Delete a note from Django backend
    """
    try:
        async with httpx.AsyncClient() as client:
            response = await client.delete(f"http://localhost:8002/api/notes/{note_id}/")
            if response.status_code == 204:
                return {"message": "Note deleted successfully"}
            elif response.status_code == 404:
                raise HTTPException(status_code=404, detail="Note not found")
            else:
                raise HTTPException(status_code=response.status_code, detail="Failed to delete note")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")

@integration_router.get("/health")
async def health_check():
    """
    Health check endpoint that checks Django backend connectivity
    """
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get("http://localhost:8002/api/notes/")
            if response.status_code == 200:
                django_status = "connected"
            else:
                django_status = "disconnected"
    except Exception:
        django_status = "disconnected"
    
    return {
        "fastapi_status": "healthy",
        "django_backend_status": django_status,
        "message": "FastAPI Integration Layer is running with Django backend"
    }