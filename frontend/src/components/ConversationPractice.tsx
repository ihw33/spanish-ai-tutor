import React, { useState } from 'react';
import { ChevronRight, Volume2, Info, RefreshCw } from 'lucide-react';

interface ConversationCardProps {
  prompt: string;
  responses: string[];
  topic: string;
  onComplete: (response: string) => void;
}

export const ConversationCard: React.FC<ConversationCardProps> = ({
  prompt,
  responses,
  topic,
  onComplete
}) => {
  const [selectedResponse, setSelectedResponse] = useState<number | null>(null);
  const [showFeedback, setShowFeedback] = useState(false);

  const handleResponseSelect = (index: number) => {
    setSelectedResponse(index);
    setShowFeedback(true);
    
    // 2초 후 다음으로
    setTimeout(() => {
      onComplete(responses[index]);
    }, 2000);
  };

  const playAudio = () => {
    // TTS 구현 (Web Speech API 또는 외부 서비스)
    if ('speechSynthesis' in window) {
      const utterance = new SpeechSynthesisUtterance(prompt);
      utterance.lang = 'es-ES';
      window.speechSynthesis.speak(utterance);
    }
  };

  return (
    <div className="max-w-sm mx-auto p-4">
      {/* 주제 표시 */}
      <div className="text-sm text-gray-500 mb-2">{topic}</div>
      
      {/* 프롬프트 카드 */}
      <div className="bg-blue-50 rounded-lg p-4 mb-4">
        <div className="flex justify-between items-start mb-2">
          <p className="text-lg font-medium text-gray-800 flex-1">{prompt}</p>
          <button 
            onClick={playAudio}
            className="ml-2 p-2 hover:bg-blue-100 rounded-full transition-colors"
          >
            <Volume2 className="w-5 h-5 text-blue-600" />
          </button>
        </div>
        <p className="text-sm text-gray-600">무엇이라고 대답하시겠어요?</p>
      </div>

      {/* 응답 옵션들 */}
      <div className="space-y-2">
        {responses.map((response, index) => (
          <button
            key={index}
            onClick={() => handleResponseSelect(index)}
            disabled={selectedResponse !== null}
            className={`
              w-full text-left p-4 rounded-lg border transition-all
              ${selectedResponse === index 
                ? 'border-green-500 bg-green-50' 
                : 'border-gray-200 hover:border-gray-300 hover:bg-gray-50'
              }
              ${selectedResponse !== null && selectedResponse !== index
                ? 'opacity-50'
                : ''
              }
            `}
          >
            <div className="flex items-center justify-between">
              <span className="text-gray-800">{response}</span>
              <ChevronRight className="w-5 h-5 text-gray-400" />
            </div>
          </button>
        ))}
      </div>

      {/* 피드백 */}
      {showFeedback && (
        <div className="mt-4 p-3 bg-green-100 rounded-lg">
          <p className="text-green-800 text-sm font-medium">
            ¡Muy bien! 좋아요! 계속해봐요 👏
          </p>
        </div>
      )}
    </div>
  );
};

// 문법 툴팁 컴포넌트
interface GrammarTooltipProps {
  word: string;
  info: Array<{
    type: string;
    usage?: string;
    link?: string;
  }>;
}

export const GrammarTooltip: React.FC<GrammarTooltipProps> = ({ word, info }) => {
  const [showTooltip, setShowTooltip] = useState(false);

  return (
    <span className="relative inline-block">
      <span 
        className="border-b-2 border-dotted border-blue-400 cursor-help"
        onClick={() => setShowTooltip(!showTooltip)}
      >
        {word}
      </span>
      
      {showTooltip && (
        <div className="absolute bottom-full left-1/2 transform -translate-x-1/2 mb-2 z-10">
          <div className="bg-white rounded-lg shadow-lg p-3 min-w-[200px] border border-gray-200">
            <button 
              onClick={() => setShowTooltip(false)}
              className="absolute top-1 right-1 text-gray-400 hover:text-gray-600"
            >
              ×
            </button>
            
            <h4 className="font-bold text-sm mb-2">{word}</h4>
            {info.map((item, index) => (
              <div key={index} className="text-xs text-gray-600 mb-1">
                <span className="font-semibold">{item.type}:</span>
                {item.usage && <span> {item.usage}</span>}
                {item.link && (
                  <a href={item.link} className="text-blue-500 ml-1">
                    <Info className="w-3 h-3 inline" />
                  </a>
                )}
              </div>
            ))}
          </div>
        </div>
      )}
    </span>
  );
};

// 일일 진도 표시
interface DailyProgressProps {
  completed: number;
  total: number;
  streak: number;
}

export const DailyProgress: React.FC<DailyProgressProps> = ({ 
  completed, 
  total, 
  streak 
}) => {
  const percentage = (completed / total) * 100;

  return (
    <div className="max-w-sm mx-auto p-4">
      <div className="bg-white rounded-lg shadow-sm border border-gray-200 p-4">
        <div className="flex justify-between items-center mb-3">
          <h3 className="font-semibold text-gray-800">오늘의 학습</h3>
          <span className="text-sm text-orange-600 font-medium">
            🔥 {streak}일 연속
          </span>
        </div>
        
        <div className="mb-2">
          <div className="flex justify-between text-sm text-gray-600 mb-1">
            <span>{completed}/{total} 완료</span>
            <span>{Math.round(percentage)}%</span>
          </div>
          <div className="w-full bg-gray-200 rounded-full h-2">
            <div 
              className="bg-blue-500 h-2 rounded-full transition-all duration-300"
              style={{ width: `${percentage}%` }}
            />
          </div>
        </div>
        
        <p className="text-xs text-gray-500 mt-2">
          매일 조금씩, 꾸준히! 화이팅! 💪
        </p>
      </div>
    </div>
  );
};

// 퀵 리뷰 버튼
export const QuickReviewButton: React.FC<{ onClick: () => void }> = ({ onClick }) => {
  return (
    <button
      onClick={onClick}
      className="fixed bottom-6 right-6 bg-blue-600 text-white rounded-full p-4 shadow-lg hover:bg-blue-700 transition-colors"
    >
      <RefreshCw className="w-6 h-6" />
    </button>
  );
};
