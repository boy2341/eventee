from fastapi import FastAPI, HTTPException, Body
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import os
import uuid

app = FastAPI(title="Eventee - Render Edition")

# Allow your frontend to talk to this backend even on different URLs
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- NEW: HEALTH CHECK ENDPOINT ---
# Render needs this to confirm the deployment was successful
@app.get("/")
async def root():
    return {"message": "Eventee Backend is Live", "status": "active"}

# --- IN-MEMORY DATA STORAGE ---
db = {
    "users": {
        "2K21/CO/101": {
            "name": "Abhishank Singh",
            "password": "demo123",
            "role": "student",
            "college_id": "DTU",
            "interests": ["AI/ML", "Web Dev"]
        }
    },
    "events": [
        {
            "id": "evt_1",
            "title": "Winter Solstice Hackathon",
            "category": "Tech",
            "date": "2026-12-20T10:00:00",
            "venue": "Great Hall, DTU",
            "description": "A premier coding challenge for innovators.",
            "price": 0,
            "registered": 45,
            "capacity": 100,
            "tags": ["AI", "Hackathon"]
        }
    ]
}

# --- SCHEMAS ---
class SignupRequest(BaseModel):
    name: str
    student_id: str
    email: str
    college_id: str
    password: str
    role: str
    year: int

class LoginRequest(BaseModel):
    student_id: str
    password: str
    role: str

# --- ENDPOINTS ---

@app.post("/api/auth/signup")
async def signup(data: SignupRequest):
    if data.student_id in db["users"]:
        raise HTTPException(status_code=400, detail="Student ID already exists")
    
    db["users"][data.student_id] = {
        "name": data.name,
        "password": data.password,
        "role": data.role,
        "college_id": data.college_id,
        "interests": []
    }
    
    return {
        "access_token": f"token-{uuid.uuid4()}",
        "user": {"name": data.name, "student_id": data.student_id, "role": data.role}
    }

@app.post("/api/auth/login")
async def login(data: LoginRequest):
    user = db["users"].get(data.student_id)
    
    if not user or user["password"] != data.password:
        raise HTTPException(status_code=401, detail="Invalid ID or Password")
    
    return {
        "access_token": f"token-{uuid.uuid4()}",
        "user": {
            "name": user["name"],
            "student_id": data.student_id,
            "role": user["role"]
        },
        "needs_interests": len(user["interests"]) == 0
    }

@app.get("/api/events/")
async def get_events():
    return {"events": db["events"], "page": 1, "pages": 1}
