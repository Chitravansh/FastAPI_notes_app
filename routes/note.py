from fastapi import APIRouter, FastAPI, Request
from fastapi.templating import Jinja2Templates
from models.note import Note
from config.db import conn
from schemas.note import noteEntity, notesEntity
from fastapi.responses import HTMLResponse, RedirectResponse


note = APIRouter()
templates = Jinja2Templates(directory="templates")


@note.get("/", response_class=HTMLResponse)
async def read_item(request: Request):

    docs = conn.Notes.Notes.find({})

       
    newDocs = []
    for doc in docs:
        newDocs.append({
            "id": str(doc.get("_id")),  # always safe to convert ObjectId to str
            "title": doc.get("title"),
            "desc": doc.get("desc") # safe access
        })

    return templates.TemplateResponse(
        "index.html", {"request": request, "newDocs": newDocs}
    )





@note.post("/")
async def create_item(request: Request):
    form = await request.form()
    formDict = dict(form)
    
    note = conn.Notes.Notes.insert_one(dict(formDict))
    # return{"Success":True}
    return RedirectResponse(url="/", status_code=303)
 