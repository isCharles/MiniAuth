from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "MiniAuth API is running!"}
