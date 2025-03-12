from fastapi import FastAPI
from .routs import router

app = FastAPI()

# Include API routes
app.include_router(router)

@app.get("/")
def home():
    return {"message": "Medical Device Recommender API is running!"}