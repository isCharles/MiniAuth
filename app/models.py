from passlib.context import CryptContext
from .database import get_db

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_user(username: str, password:str):
    db= get_db()
    hashed_pw = pwd_context.hash(password)
    db.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT UNIQUE, password TEXT)")
    try:
        db.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_pw))
        db.commit()
        return True
    except:
        return False