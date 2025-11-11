好，那我给你**专业、利落、无多余表情的 README**，适合面试、简历链接、GitHub 展示。

你直接复制粘贴即可。

---

# MiniAuth

A minimal user authentication system implemented with **FastAPI**, **SQLAlchemy**, and **JWT**.
The project focuses on understanding the **core logic of backend authentication** rather than framework complexity.

---

## Overview

MiniAuth implements three basic authentication capabilities:

1. **User Registration** — Store credentials securely (hashed password).
2. **User Login** — Validate credentials and return a signed JWT.
3. **Protected Resource Access** — Authenticate users via JWT in request headers.

Authentication Flow:

```
[Client] → Register → [Server → Store hashed password]

[Client] → Login → [Server → Validate + Issue JWT] → [Client stores Token]

[Client] → Request with Authorization: Bearer <token> → [Server → Verify Token → Allow Access]
```

---

## Tech Stack

| Component            | Purpose                          | Notes for Understanding                                 |
| -------------------- | -------------------------------- | ------------------------------------------------------- |
| **FastAPI**          | API framework                    | Routing, request model validation, dependency injection |
| **Pydantic**         | Request/response data validation | Defines data schema (`BaseModel`)                       |
| **SQLAlchemy**       | ORM database layer               | Models, sessions, basic CRUD                            |
| **Passlib (bcrypt)** | Password hashing                 | `hash()` and `verify()` logic                           |
| **PyJWT**            | JSON Web Tokens                  | Token creation & signature verification                 |

---

## Directory Structure (Recommended)

```
MiniAuth/
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── auth.py
│   └── utils.py
├── requirements.txt
└── README.md
```

---

## Data Model

```python
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
```

---

## JWT Authentication

A JWT contains:

```
header.payload.signature
```

Server-side validation checks:

1. Token signature integrity
2. Expiration timestamp
3. Extracted `user_id`

---

## API Endpoints

| Method | Endpoint         | Description           | Auth Required      |
| ------ | ---------------- | --------------------- | ------------------ |
| POST   | `/auth/register` | Create new user       | No                 |
| POST   | `/auth/login`    | Login and return JWT  | No                 |
| GET    | `/auth/profile`  | Get current user info | Yes (Bearer Token) |

Protected request header example:

```
Authorization: Bearer <token>
```

---

## Running Locally

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

API docs will be available at:

```
http://127.0.0.1:8000/docs
```

---

## Progress Checklist

| Feature                                   | Status        |
| ----------------------------------------- | ------------- |
| FastAPI routing setup                     | ✅             |
| Database (SQLAlchemy) initialization      | ✅             |
| User model + schema definition            | ✅             |
| Registration endpoint                     | ⬜ In Progress |
| Login + JWT issue                         | ⬜ In Progress |
| Protected profile endpoint                | ⬜ In Progress |
| Optional: password reset / delete account | (Optional)    |

---
