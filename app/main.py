from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Medical Device Recommender API is running!"}