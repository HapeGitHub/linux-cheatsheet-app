from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import json
import os

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "cheatsheet_data.json")

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/api/cheatsheet")
def get_cheatsheet():
    try:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
        return JSONResponse(content=data)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
