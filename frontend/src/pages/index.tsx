import React, { useState, useEffect } from 'react';
import { 
  ConversationCard, 
  DailyProgress, 
  QuickReviewButton 
} from '../components/ConversationPractice';

// 모바일 PWA를 위한 메타 태그는 _document.tsx에서 설정

export default function Home() {
  const [currentPractice, setCurrentPractice] = useState(0);
  const [dailyProgress, setDailyProgress] = useState({
    completed: 0,
    total: 10,
    streak: 7
  });
  
  // 예시 연습 데이터 (실제로는 API에서 가져옴)
  const [practices] = useState([
    {
      prompt: "¡Hola! ¿Cómo estás?",
      responses: [
        "Muy bien, gracias. ¿Y tú?",
        "Bien, gracias.",
        "Regular. ¿Qué tal tú?"
      ],
      topic: "인사하기"
    },
    {
      prompt: "¿Cómo te llamas?",
      responses: [
        "Me llamo María.",
        "Soy Carlos.",
        "Mi nombre es Ana."
      ],
      topic: "자기소개"
    },
    {
      prompt: "¿De dónde eres?",
      responses: [
        "Soy de Corea.",
        "Soy coreano/a.",
        "Vengo de Seúl."
      ],
      topic: "출신 묻기"
    }
  ]);

  const handlePracticeComplete = (response: string) => {
    // 진도 업데이트
    setDailyProgress(prev => ({
      ...prev,
      completed: prev.completed + 1
    }));

    // 다음 연습으로
    if (currentPractice < practices.length - 1) {
      setTimeout(() => {
        setCurrentPractice(prev => prev + 1);
      }, 500);
    } else {
      // 오늘 연습 완료!
      alert('¡Felicidades! 오늘 연습을 모두 완료했어요! 🎉');
    }
  };

  const handleQuickReview = () => {
    // 빠른 복습 모드
    setCurrentPractice(0);
  };

  return (
    <div className="min-h-screen bg-gray-50">
      {/* 헤더 */}
      <header className="bg-white shadow-sm sticky top-0 z-10">
        <div className="max-w-sm mx-auto px-4 py-3">
          <h1 className="text-xl font-bold text-gray-800">
            Hola Español 📚
          </h1>
        </div>
      </header>

      {/* 진도 표시 */}
      <DailyProgress {...dailyProgress} />

      {/* 메인 콘텐츠 */}
      <main className="pb-20">
        {currentPractice < practices.length && (
          <ConversationCard
            {...practices[currentPractice]}
            onComplete={handlePracticeComplete}
          />
        )}
      </main>

      {/* 빠른 복습 버튼 */}
      <QuickReviewButton onClick={handleQuickReview} />

      {/* 하단 네비게이션 */}
      <nav className="fixed bottom-0 left-0 right-0 bg-white border-t border-gray-200">
        <div className="max-w-sm mx-auto px-4">
          <div className="flex justify-around py-2">
            <button className="flex flex-col items-center p-2 text-blue-600">
              <span className="text-2xl">💬</span>
              <span className="text-xs">회화</span>
            </button>
            <button className="flex flex-col items-center p-2 text-gray-400">
              <span className="text-2xl">📖</span>
              <span className="text-xs">문법</span>
            </button>
            <button className="flex flex-col items-center p-2 text-gray-400">
              <span className="text-2xl">📊</span>
              <span className="text-xs">진도</span>
            </button>
            <button className="flex flex-col items-center p-2 text-gray-400">
              <span className="text-2xl">⚙️</span>
              <span className="text-xs">설정</span>
            </button>
          </div>
        </div>
      </nav>
    </div>
  );
}

// 매일 알림 설정을 위한 서비스 워커 등록
if (typeof window !== 'undefined' && 'serviceWorker' in navigator) {
  window.addEventListener('load', () => {
    navigator.serviceWorker.register('/sw.js').then(
      registration => {
        console.log('SW registered: ', registration);
        
        // 푸시 알림 권한 요청
        if ('Notification' in window) {
          Notification.requestPermission().then(permission => {
            if (permission === 'granted') {
              // 매일 오전 9시 알림 설정
              scheduleDaily Notification();
            }
          });
        }
      },
      err => console.log('SW registration failed: ', err)
    );
  });
}

function scheduleDailyNotification() {
  // 매일 알림 로직 (실제 구현 시 백엔드와 연동)
  const now = new Date();
  const scheduledTime = new Date();
  scheduledTime.setHours(9, 0, 0, 0); // 오전 9시
  
  if (scheduledTime <= now) {
    scheduledTime.setDate(scheduledTime.getDate() + 1); // 내일 9시
  }
  
  const timeout = scheduledTime.getTime() - now.getTime();
  
  setTimeout(() => {
    new Notification('¡Hola! 스페인어 연습 시간이에요 🇪🇸', {
      body: '오늘도 5분만 투자해보세요!',
      icon: '/icon-192.png',
      badge: '/badge-72.png'
    });
    
    // 다음 날 알림 예약
    scheduleDailyNotification();
  }, timeout);
}
