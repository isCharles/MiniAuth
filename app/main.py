from fastapi import FastAPI
from .schemas import UserCreate
from .models import create_user

app = FastAPI()

@app.get("/")
def home():
    return {"message": "MiniAuth API is running!"}

@app.post("/register")
def register_user(user: UserCreate):
    success = create_user(user.username, user.password)
    if not success:
        raise HTTPException(status_code=400, detail="Username already exists")
    return {"message": "User registered successfully"}