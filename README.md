# 🇪🇸 Spanish AI Tutor

AI 기반 스페인어 학습 도우미 - 교재 내용을 바탕으로 한 맞춤형 연습

## 📚 프로젝트 소개

"Nuevo Español en Marcha" 교재를 기반으로 한 인터랙티브 스페인어 학습 시스템입니다.

### 주요 기능

- 🔄 **동사 활용 연습**: 모든 시제의 동사 변화 자동 생성 및 연습
- 📝 **어순 트레이너**: 한국어 → 스페인어 어순 변환 연습
- 🎭 **대화 시뮬레이션**: 실제 상황별 회화 연습
- 📊 **진도 추적**: 개인별 학습 진도 및 약점 분석
- 🎯 **맞춤형 커리큘럼**: AI가 분석한 개인별 학습 계획

## 🚀 시작하기

### 필요 사항
- Python 3.9+
- Node.js 18+
- PDF 교재 파일

### 설치 방법

```bash
# 백엔드 설치
cd backend
pip install -r requirements.txt

# 프론트엔드 설치
cd frontend
npm install
```

### 실행 방법

```bash
# 백엔드 서버 시작
cd backend
uvicorn main:app --reload

# 프론트엔드 시작
cd frontend
npm run dev
```

## 📖 교재 데이터 준비

1. PDF 스캔 파일을 `data/textbook/` 폴더에 저장
2. 텍스트 추출 스크립트 실행:
   ```bash
   python scripts/pdf_extractor.py
   ```

## 🎯 학습 모드

### 1. 동사 마스터
- 규칙/불규칙 동사 활용
- 시제별 집중 연습
- 실시간 피드백

### 2. 문법 드릴
- ser vs estar
- 목적어 대명사
- 시제 선택

### 3. 회화 연습
- 상황별 대화
- 발음 교정
- 문화 팁

## 🤝 기여하기

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 라이선스

이 프로젝트는 MIT 라이선스를 따릅니다.
