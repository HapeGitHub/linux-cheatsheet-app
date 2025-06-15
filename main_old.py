from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, PlainTextResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import subprocess

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/help")
def get_help(cmd: str):
    try:
        output = subprocess.check_output(["man", cmd], stderr=subprocess.STDOUT, timeout=3)
        return PlainTextResponse(output.decode("utf-8")[:3000])  # limit output
    except subprocess.CalledProcessError as e:
        return PlainTextResponse(f"Error fetching help: {e.output.decode('utf-8')}", status_code=400)
    except Exception as e:
        return PlainTextResponse(str(e), status_code=500)
