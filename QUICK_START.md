# 🚀 Spanish AI Tutor - 빠른 시작 가이드

## 1분 만에 시작하기

### 방법 1: 온라인으로 바로 사용 (추천) 🌐
아직 배포 전이지만, 곧 이렇게 사용할 수 있어요:
```
1. 휴대폰에서 https://spanish-tutor.vercel.app 접속
2. "홈 화면에 추가" 탭
3. 바로 학습 시작!
```

### 방법 2: 컴퓨터에서 개발 모드로 실행 💻

#### 1. 터미널 1 - 백엔드 실행
```bash
cd spanish-ai-tutor/backend
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install fastapi uvicorn
python main.py
```

백엔드가 실행되면: http://localhost:8000 에서 확인

#### 2. 터미널 2 - 프론트엔드 실행
```bash
cd spanish-ai-tutor/frontend
npm install
npm run dev
```

프론트엔드가 실행되면: http://localhost:3000 에서 앱 사용!

### 📱 휴대폰에서 테스트하기
같은 WiFi에 연결된 상태에서:
1. 컴퓨터 IP 주소 확인 (예: 192.168.1.100)
2. 휴대폰 브라우저에서 `http://192.168.1.100:3000` 접속

### ⚡ 한 번에 실행하기 (Mac/Linux)
```bash
# 프로젝트 폴더에서
./start_all.sh
```

## 🎯 첫 사용 방법

1. **앱 열기**: 브라우저에서 http://localhost:3000
2. **첫 화면**: "¡Hola! ¿Cómo estás?" 
3. **대답 선택**: 3개 중 하나 탭
4. **계속하기**: 10개 완료하면 오늘 학습 끝!

## 🔧 문제 해결

### "Module not found" 에러
```bash
pip install -r requirements.txt
```

### 포트 이미 사용 중
```bash
# 백엔드 포트 변경
python main.py --port 8001

# 프론트엔드 포트 변경
npm run dev -- -p 3001
```

### 휴대폰에서 안 열림
- 방화벽 확인
- 같은 WiFi 네트워크인지 확인
- IP 주소 정확한지 확인

## 💡 팁

- **매일 같은 시간에**: 습관 만들기
- **5분만**: 부담 없이 꾸준히
- **소리 내어 읽기**: 발음 연습도 함께

---

문제가 있으면 Issues에 남겨주세요! 🙋‍♂️
