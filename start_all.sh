#!/bin/bash

echo "🚀 Spanish AI Tutor 시작 중..."

# 백엔드 시작
echo "📡 백엔드 서버 시작..."
cd backend
source venv/bin/activate 2>/dev/null || {
    echo "🔧 Python 환경 설정 중..."
    python3 -m venv venv
    source venv/bin/activate
    pip install fastapi uvicorn
}

# 백그라운드에서 백엔드 실행
python main.py &
BACKEND_PID=$!
echo "✅ 백엔드 실행 중 (PID: $BACKEND_PID)"

# 잠시 대기
sleep 3

# 프론트엔드 시작
echo "🎨 프론트엔드 시작..."
cd ../frontend

# 패키지 설치 확인
if [ ! -d "node_modules" ]; then
    echo "📦 패키지 설치 중..."
    npm install
fi

echo "
✨ Spanish AI Tutor가 준비되었습니다!

🌐 브라우저에서 열기: http://localhost:3000
📱 모바일에서 열기: http://[YOUR-IP]:3000

종료하려면 Ctrl+C를 누르세요.
"

# 프론트엔드 실행
npm run dev

# 종료 시 백엔드도 종료
trap "kill $BACKEND_PID 2>/dev/null" EXIT
