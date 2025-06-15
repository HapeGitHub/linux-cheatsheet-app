# Linux Cheatsheet App

A FastAPI-based web application to display categorized Linux command-line examples with clipboard support and expandable help text.

# .gitignore
```__pycache__/
*.pyc
venv/
.env
```

# requirements.txt
fastapi
uvicorn
jinja2

## Features
- JSON-based content for easy editing
- Static CSS for styling
- Template rendering with Jinja2
- Copy-to-clipboard and command help buttons

## Development
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload --port 8002
```
