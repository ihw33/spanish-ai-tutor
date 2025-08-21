# 🌐 온라인으로 사용하기 (모바일 포함!)

## GitHub Pages 설정 방법

1. **GitHub 레포지토리로 이동**
   - https://github.com/ihw33/spanish-ai-tutor

2. **Settings 클릭** (상단 메뉴)

3. **Pages 섹션 찾기** (왼쪽 사이드바)

4. **Source 설정**
   - Source: Deploy from a branch
   - Branch: main
   - Folder: / (root)
   - Save 클릭

5. **잠시 기다리면 배포 완료!**
   - 주소: https://ihw33.github.io/spanish-ai-tutor/

## 📱 모바일에서 사용하기

### 방법 1: GitHub Pages (추천)
위 설정 후 몇 분 기다리면:
- https://ihw33.github.io/spanish-ai-tutor/
- 모든 기기에서 접속 가능!

### 방법 2: 로컬 네트워크 공유
```bash
# 맥에서 실행
cd /Users/m4_macbook/Projects/spanish-ai-tutor
python3 -m http.server 8000

# 같은 와이파이에 연결된 폰에서:
# http://[맥의IP주소]:8000/demo.html
# 맥 IP 확인: ifconfig | grep inet
```

### 방법 3: ngrok으로 임시 공유
```bash
# ngrok 설치 (homebrew 필요)
brew install ngrok

# 서버 실행
cd /Users/m4_macbook/Projects/spanish-ai-tutor
python3 -m http.server 8000

# 다른 터미널에서
ngrok http 8000
# → https://xxxxx.ngrok.io 주소 생성됨
```

### 방법 4: Netlify Drop (즉시 배포)
1. https://app.netlify.com/drop 접속
2. 프로젝트 폴더 전체를 드래그&드롭
3. 즉시 URL 생성!

## 🔗 PWA로 설치하기

모바일에서 "홈 화면에 추가"하면 앱처럼 사용 가능!

1. Safari/Chrome에서 사이트 열기
2. 공유 버튼 탭
3. "홈 화면에 추가" 선택
4. 앱처럼 사용!

---

**추천: GitHub Pages가 가장 간단하고 영구적입니다!**