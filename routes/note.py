from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import httpx


note=APIRouter()
templates = Jinja2Templates(directory="templates")



@note.get("/", response_class=HTMLResponse)
async def read_home(request: Request):
    # Call Django API to get notes
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get("http://localhost:8000/api/notes/")
            if response.status_code == 200:
                docs = response.json()
                newdoc = []
                for doc in docs:
                    newdoc.append({
                        "id": doc["id"],
                        "title": doc["title"],
                        "desc": doc["desc"],
                        "note": doc["note"],
                        "important": doc["important"]
                    })
            else:
                newdoc = []
        except httpx.ConnectError:
            # If Django backend is not running, return empty list
            newdoc = []
    return templates.TemplateResponse(name="index.html", context={"request": request, "newdoc":newdoc})



@note.post("/")
async def create_item(request: Request):
    form = await request.form()
    note_data = {
        "title": form.get("title"),
        "desc": form.get("desc"), 
        "note": form.get("note"),
        "important": form.get("important") == "on"
    }
    
    # Call Django API to create note
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post("http://localhost:8000/api/notes/", json=note_data)
        except httpx.ConnectError:
            # If Django backend is not running, handle gracefully
            pass
    
    # Redirect to GET route to show updated list
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get("http://localhost:8000/api/notes/")
            if response.status_code == 200:
                docs = response.json()
                newdoc = []
                for doc in docs:
                    newdoc.append({
                        "id": doc["id"],
                        "title": doc["title"],
                        "desc": doc["desc"],
                        "note": doc["note"],
                        "important": doc["important"]
                    })
            else:
                newdoc = []
        except httpx.ConnectError:
            newdoc = []
    return templates.TemplateResponse(name="index.html", context={"request": request, "newdoc": newdoc})
