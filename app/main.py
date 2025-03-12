from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from .routs import router

app = FastAPI()

# Mount the static folder to serve HTML
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Include API routes
app.include_router(router)

@app.get("/")
def home():
    """Serves the HTML frontend."""
    return {"message": "Go to /static/index.html to use the web interface"}