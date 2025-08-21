# 📱 Hola Español - 매일 5분 스페인어 회화

가볍게, 하지만 꾸준히! 모바일에 최적화된 스페인어 회화 학습 앱

## 🎯 프로젝트 철학

- **저작권 안전**: 교재 구조는 참고하되, 모든 예문과 내용은 자체 제작
- **회화 중심**: 문법보다는 반복을 통한 자연스러운 습득
- **모바일 우선**: 언제 어디서나 5분 투자로 꾸준한 학습
- **간편한 참조**: 탭 한 번으로 문법 정보 확인

## 🚀 주요 기능

### 1. 일일 회화 연습
- 10개의 짧은 대화 연습
- 워밍업 → 새로운 내용 → 복습 구조
- 실제 상황별 회화 패턴

### 2. 스마트 반복 학습
- 간격 반복 알고리즘
- 개인 진도에 맞춘 난이도 조정
- 연속 학습 일수 추적 (🔥 스트릭)

### 3. 즉시 문법 참조
- 단어 탭하면 문법 정보 팝업
- ser vs estar 구분
- 성별, 단복수 정보
- 동사 변화 힌트

### 4. 모바일 최적화
- PWA (Progressive Web App)
- 오프라인 지원
- 매일 알림
- 한 손 조작 가능한 UI

## 📱 사용 방법

### 설치 없이 바로 시작
```
1. 휴대폰에서 https://your-domain.com 접속
2. "홈 화면에 추가" 선택
3. 매일 5분씩 연습!
```

### 로컬 개발 환경
```bash
# 백엔드 시작
cd backend
pip install -r requirements.txt
uvicorn main:app --reload --host 0.0.0.0 --port 8000

# 프론트엔드 시작
cd frontend
npm install
npm run dev
```

## 🎮 학습 흐름

### 매일 10분 루틴
```
1. 🌅 아침 알림 (설정 가능)
2. 💬 워밍업: 기본 인사 (2개)
3. 📚 오늘의 학습: 새로운 패턴 (5개)
4. 🔄 복습: 어제 배운 내용 (3개)
5. 🎯 완료: 연속 학습 일수 +1
```

### 회화 연습 예시
```
상황: 카페에서
제시: "¿Qué desea tomar?"

선택지:
1. "Un café con leche, por favor."
2. "Quisiera un café, por favor."
3. "Para mí, un café."

👆 탭하여 선택 → 즉시 피드백
```

## 🏗️ 기술 스택

- **Backend**: FastAPI + Python
- **Frontend**: Next.js + React + TypeScript
- **UI**: Tailwind CSS (모바일 우선)
- **PWA**: Service Worker + Web Push
- **배포**: Vercel + Railway

## 📊 학습 데이터 구조

```python
{
  "daily_practice": {
    "warm_up": ["인사", "안부"],
    "new_content": ["카페", "레스토랑", "쇼핑"],
    "review": ["어제 학습 내용"]
  },
  "progress": {
    "streak": 7,  # 연속 학습 일수
    "total_practices": 156,
    "level": "beginner"
  }
}
```

## 🤝 기여 방법

1. 새로운 회화 패턴 추가
2. 문법 설명 개선
3. UI/UX 개선 제안
4. 버그 리포트

## 📝 라이선스

MIT License - 자유롭게 사용하세요!

---

**"매일 5분, 스페인어가 쉬워집니다"** 🇪🇸
