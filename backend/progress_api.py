from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime
import json
import os

app = FastAPI()

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 데이터 모델
class Progress(BaseModel):
    mode: str
    completed: int
    total: int
    timestamp: datetime = None

class UserSession(BaseModel):
    session_id: str
    progress: dict = {}
    last_active: datetime = None

# 간단한 파일 기반 저장소
SESSIONS_FILE = "data/sessions.json"

def load_sessions():
    if os.path.exists(SESSIONS_FILE):
        with open(SESSIONS_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_sessions(sessions):
    os.makedirs("data", exist_ok=True)
    with open(SESSIONS_FILE, 'w') as f:
        json.dump(sessions, f, default=str)

@app.get("/")
def read_root():
    return {"message": "¡Hola! Spanish AI Tutor API"}

@app.post("/progress/{session_id}")
def save_progress(session_id: str, progress: Progress):
    sessions = load_sessions()
    
    if session_id not in sessions:
        sessions[session_id] = {
            "session_id": session_id,
            "progress": {},
            "last_active": str(datetime.now())
        }
    
    sessions[session_id]["progress"][progress.mode] = {
        "completed": progress.completed,
        "total": progress.total,
        "timestamp": str(datetime.now())
    }
    sessions[session_id]["last_active"] = str(datetime.now())
    
    save_sessions(sessions)
    return {"status": "saved", "session_id": session_id}

@app.get("/progress/{session_id}")
def get_progress(session_id: str):
    sessions = load_sessions()
    
    if session_id not in sessions:
        raise HTTPException(status_code=404, detail="Session not found")
    
    return sessions[session_id]

@app.get("/stats/{session_id}")
def get_stats(session_id: str):
    sessions = load_sessions()
    
    if session_id not in sessions:
        raise HTTPException(status_code=404, detail="Session not found")
    
    session = sessions[session_id]
    total_completed = sum(p.get("completed", 0) for p in session["progress"].values())
    total_items = sum(p.get("total", 0) for p in session["progress"].values())
    
    return {
        "session_id": session_id,
        "total_completed": total_completed,
        "total_items": total_items,
        "completion_rate": (total_completed / total_items * 100) if total_items > 0 else 0,
        "last_active": session["last_active"]
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)