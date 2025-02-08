from fastapi import FastAPI, File, UploadFile, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from utils.document_parser import DocumentParser
from llm.rag import RAG
from config import Config
import os

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="src/admin_ui/templates")

rag = RAG()

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/upload")
async def upload_file(request: Request, file: UploadFile = File(...)):
    try:
        file_path = os.path.join(Config.DOCUMENTS_DIR, file.filename)
        with open(file_path, "wb") as f:
            f.write(file.file.read())

        text = DocumentParser.parse_file(file_path)
        rag.add_document(text)

        return templates.TemplateResponse("index.html", {"request": request, "message": "File upload successfully!"})
    except Exception as e:
        return templates.TemplateResponse("index.html", {"request": request, "error": str(e)})