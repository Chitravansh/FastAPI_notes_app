from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")

uri = "mongodb+srv://chitravanshmohandevelops:8787230617@cluster0.est0t.mongodb.net"

conn = MongoClient(uri)



# @app.get("/", response_class=HTMLResponse)
# async def read_item(request: Request):

#     docs = conn.Notes.Notes.find({})
#     # for doc  in  docs:
#     #     print(doc) 
#     newDocs = [] 
#     for doc in docs:
#         newDocs.append({
#             "id": doc["_id"],
#             "note": doc["note"]
#         })
#     return templates.TemplateResponse(
#         "index.html", {"request": request, "newDocs" : newDocs})


@app.get("/items/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    return templates.TemplateResponse("item.html",
     {"request": request, "id": id})