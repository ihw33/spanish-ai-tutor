"""
Daily Practice API
매일 가벼운 회화 연습을 위한 API 엔드포인트
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict, Optional
from datetime import datetime, date
import random

from conversation_patterns import ConversationPatternService
from conjugation_service import VerbConjugationService

app = FastAPI(title="Spanish Daily Practice API")

# CORS 설정 (모바일 웹 지원)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 서비스 초기화
conversation_service = ConversationPatternService()
verb_service = VerbConjugationService()

# 데이터 모델
class PracticeSession(BaseModel):
    date: str
    practices: List[Dict]
    completed: int = 0
    total: int = 10

class UserProgress(BaseModel):
    user_id: str
    streak: int = 0
    last_practice_date: Optional[str] = None
    total_practices: int = 0
    level: str = "beginner"

# 임시 저장소 (실제로는 DB 사용)
user_progress_db = {}
daily_sessions = {}

@app.get("/")
def read_root():
    return {
        "message": "¡Hola! Spanish Daily Practice API",
        "version": "1.0.0"
    }

@app.get("/api/daily-practice/{user_id}")
def get_daily_practice(user_id: str):
    """오늘의 회화 연습 가져오기"""
    today = date.today().isoformat()
    session_key = f"{user_id}_{today}"
    
    # 이미 생성된 세션이 있으면 반환
    if session_key in daily_sessions:
        return daily_sessions[session_key]
    
    # 새로운 세션 생성
    session_data = conversation_service.create_spaced_repetition_session()
    
    # 평면화하여 10개 연습으로 만들기
    all_practices = []
    
    # 워밍업 (2개)
    for practice in session_data["warm_up"][:2]:
        all_practices.append({
            "id": len(all_practices),
            "type": "warm_up",
            **practice
        })
    
    # 새로운 내용 (5개)
    for practice in session_data["new_content"][:5]:
        all_practices.append({
            "id": len(all_practices),
            "type": "new",
            **practice
        })
    
    # 복습 (3개)
    for practice in session_data["review"][:3]:
        all_practices.append({
            "id": len(all_practices),
            "type": "review",
            **practice
        })
    
    session = PracticeSession(
        date=today,
        practices=all_practices,
        total=len(all_practices)
    )
    
    daily_sessions[session_key] = session
    return session

@app.post("/api/complete-practice/{user_id}/{practice_id}")
def complete_practice(user_id: str, practice_id: int, selected_response: str):
    """연습 완료 기록"""
    today = date.today().isoformat()
    session_key = f"{user_id}_{today}"
    
    if session_key not in daily_sessions:
        raise HTTPException(status_code=404, detail="Session not found")
    
    session = daily_sessions[session_key]
    session.completed += 1
    
    # 사용자 진도 업데이트
    update_user_progress(user_id)
    
    return {
        "completed": session.completed,
        "total": session.total,
        "is_daily_complete": session.completed >= session.total
    }

@app.get("/api/user-progress/{user_id}")
def get_user_progress(user_id: str):
    """사용자 진도 조회"""
    if user_id not in user_progress_db:
        user_progress_db[user_id] = UserProgress(user_id=user_id)
    
    return user_progress_db[user_id]

@app.get("/api/grammar-tooltip/{word}")
def get_grammar_tooltip(word: str, context: str = ""):
    """단어의 문법 정보 툴팁"""
    tooltip_info = conversation_service.get_grammar_tooltip(word, context)
    return tooltip_info

@app.get("/api/quick-review/{user_id}")
def get_quick_review(user_id: str):
    """빠른 복습 (3개 문제)"""
    # 랜덤 주제에서 3개 연습 선택
    topics = list(conversation_service.conversation_topics.keys())
    practices = []
    
    for _ in range(3):
        topic = random.choice(topics)
        practice = conversation_service.generate_daily_practice(topic, 1)[0]
        practices.append(practice)
    
    return {
        "practices": practices,
        "type": "quick_review"
    }

# 유틸리티 함수
def update_user_progress(user_id: str):
    """사용자 진도 업데이트"""
    if user_id not in user_progress_db:
        user_progress_db[user_id] = UserProgress(user_id=user_id)
    
    progress = user_progress_db[user_id]
    today = date.today().isoformat()
    
    # 연속 학습 체크
    if progress.last_practice_date:
        last_date = date.fromisoformat(progress.last_practice_date)
        days_diff = (date.today() - last_date).days
        
        if days_diff == 1:
            progress.streak += 1
        elif days_diff > 1:
            progress.streak = 1
    else:
        progress.streak = 1
    
    progress.last_practice_date = today
    progress.total_practices += 1
    
    # 레벨 업데이트 (10일마다)
    if progress.total_practices >= 30:
        progress.level = "intermediate"
    elif progress.total_practices >= 60:
        progress.level = "advanced"

# 서버 실행
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
