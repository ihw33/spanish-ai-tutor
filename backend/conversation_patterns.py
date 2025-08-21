"""
Spanish Learning Pattern Generator
교재 구조를 참고하되, 자체 예문과 패턴으로 학습 콘텐츠 생성
"""

from typing import List, Dict
import random

class ConversationPatternService:
    """회화 패턴 중심의 반복 학습 서비스"""
    
    def __init__(self):
        # 교재 구조를 참고한 주제별 회화 패턴
        self.conversation_topics = {
            "greetings": {
                "title": "인사와 소개",
                "patterns": [
                    {
                        "pattern": "¡Hola! Me llamo [NAME]. ¿Y tú?",
                        "variations": [
                            {"NAME": ["Carlos", "María", "Luis", "Ana"]},
                        ],
                        "response_patterns": [
                            "Mucho gusto. Yo soy [NAME].",
                            "Encantado/a. Me llamo [NAME]."
                        ]
                    },
                    {
                        "pattern": "¿Cómo estás?",
                        "variations": [],
                        "response_patterns": [
                            "Muy bien, gracias. ¿Y tú?",
                            "Bien, gracias.",
                            "Regular. ¿Y tú?"
                        ]
                    }
                ]
            },
            "restaurant": {
                "title": "레스토랑에서",
                "patterns": [
                    {
                        "pattern": "¿Qué desea [TIME]?",
                        "variations": [
                            {"TIME": ["tomar", "comer", "beber"]},
                        ],
                        "response_patterns": [
                            "Quisiera [ITEM], por favor.",
                            "Para mí, [ITEM].",
                            "¿Tienen [ITEM]?"
                        ],
                        "vocabulary": {
                            "ITEM": {
                                "food": ["paella", "tortilla", "gazpacho", "tapas"],
                                "drink": ["agua", "vino", "café", "cerveza"]
                            }
                        }
                    }
                ]
            },
            "shopping": {
                "title": "쇼핑하기",
                "patterns": [
                    {
                        "pattern": "¿Cuánto cuesta [ITEM]?",
                        "variations": [
                            {"ITEM": ["esto", "eso", "esta camisa", "ese pantalón"]}
                        ],
                        "response_patterns": [
                            "Cuesta [PRICE] euros.",
                            "Son [PRICE] euros.",
                            "Está en oferta. Solo [PRICE] euros."
                        ],
                        "vocabulary": {
                            "PRICE": ["cinco", "diez", "veinte", "treinta", "cincuenta"]
                        }
                    }
                ]
            }
        }
        
        # 문법 포인트 빠른 참조
        self.grammar_quick_ref = {
            "ser_vs_estar": {
                "title": "SER vs ESTAR",
                "quick_rule": "SER = 영구적/본질적, ESTAR = 일시적/위치",
                "examples": {
                    "ser": ["Soy profesor", "Es alto", "Somos amigos"],
                    "estar": ["Estoy cansado", "Está en casa", "Están contentos"]
                }
            },
            "gender": {
                "title": "명사의 성",
                "quick_rule": "-o는 보통 남성, -a는 보통 여성",
                "exceptions": ["el problema", "la mano", "el día"]
            },
            "plural": {
                "title": "복수형",
                "quick_rule": "모음+s, 자음+es",
                "examples": ["libro→libros", "ciudad→ciudades"]
            }
        }
    
    def generate_daily_practice(self, topic: str, count: int = 5) -> List[Dict]:
        """일일 회화 연습 생성"""
        if topic not in self.conversation_topics:
            return []
        
        topic_data = self.conversation_topics[topic]
        practices = []
        
        for _ in range(count):
            # 랜덤하게 패턴 선택
            pattern_data = random.choice(topic_data["patterns"])
            pattern = pattern_data["pattern"]
            
            # 변형 적용
            for variation in pattern_data.get("variations", []):
                for placeholder, options in variation.items():
                    choice = random.choice(options)
                    pattern = pattern.replace(f"[{placeholder}]", choice)
            
            # 응답 옵션 생성
            responses = []
            for response_pattern in pattern_data.get("response_patterns", []):
                response = response_pattern
                
                # 어휘 치환
                if "vocabulary" in pattern_data:
                    for placeholder, vocab_data in pattern_data["vocabulary"].items():
                        if f"[{placeholder}]" in response:
                            category = random.choice(list(vocab_data.keys()))
                            word = random.choice(vocab_data[category])
                            response = response.replace(f"[{placeholder}]", word)
                
                responses.append(response)
            
            practices.append({
                "prompt": pattern,
                "responses": responses,
                "topic": topic_data["title"]
            })
        
        return practices
    
    def create_spaced_repetition_session(self, user_level: str = "beginner") -> Dict:
        """간격 반복 학습 세션 생성"""
        session = {
            "warm_up": [],
            "new_content": [],
            "review": [],
            "quick_quiz": []
        }
        
        # 1. 워밍업 - 기본 인사
        session["warm_up"] = self.generate_daily_practice("greetings", 2)
        
        # 2. 새로운 내용 - 오늘의 주제
        today_topic = random.choice(list(self.conversation_topics.keys()))
        session["new_content"] = self.generate_daily_practice(today_topic, 3)
        
        # 3. 복습 - 이전 주제들
        other_topics = [t for t in self.conversation_topics.keys() if t != today_topic]
        if other_topics:
            review_topic = random.choice(other_topics)
            session["review"] = self.generate_daily_practice(review_topic, 2)
        
        # 4. 퀴즈 - 빠른 응답 연습
        session["quick_quiz"] = self._generate_quick_quiz()
        
        return session
    
    def _generate_quick_quiz(self) -> List[Dict]:
        """빠른 퀴즈 생성"""
        quiz_types = [
            {
                "type": "fill_blank",
                "question": "¿Cómo ___ llamas?",
                "answer": "te",
                "hint": "너는 ~라고 불린다"
            },
            {
                "type": "choose_correct",
                "question": "'나는 학생입니다'의 올바른 표현은?",
                "options": ["Soy estudiante", "Estoy estudiante", "Ser estudiante"],
                "answer": 0,
                "hint": "직업은 SER 동사"
            },
            {
                "type": "translate",
                "question": "안녕하세요",
                "answer": ["Hola", "Buenos días", "Buenas tardes"],
                "hint": "시간대별로 다른 인사"
            }
        ]
        
        return random.sample(quiz_types, min(3, len(quiz_types)))
    
    def get_grammar_tooltip(self, word: str, context: str = "") -> Dict:
        """단어의 문법 정보 툴팁"""
        # 간단한 분석 (실제로는 더 정교한 NLP 필요)
        tooltip = {
            "word": word,
            "info": []
        }
        
        # 동사인지 확인
        if word.endswith(('ar', 'er', 'ir')):
            tooltip["info"].append({
                "type": "동사 원형",
                "conjugation_hint": f"{word[:-2]}__ + 어미"
            })
        
        # 성별 확인
        if word.endswith('o'):
            tooltip["info"].append({
                "type": "남성 명사",
                "plural": word + "s"
            })
        elif word.endswith('a'):
            tooltip["info"].append({
                "type": "여성 명사", 
                "plural": word + "s"
            })
        
        # ser/estar 확인
        if word in ['soy', 'eres', 'es', 'somos', 'sois', 'son']:
            tooltip["info"].append({
                "type": "SER 동사",
                "usage": "본질적 특성",
                "link": "#ser_vs_estar"
            })
        elif word in ['estoy', 'estás', 'está', 'estamos', 'estáis', 'están']:
            tooltip["info"].append({
                "type": "ESTAR 동사",
                "usage": "일시적 상태/위치",
                "link": "#ser_vs_estar"
            })
        
        return tooltip

# 사용 예시
if __name__ == "__main__":
    service = ConversationPatternService()
    
    # 일일 연습 생성
    print("=== 오늘의 회화 연습 ===")
    practices = service.generate_daily_practice("restaurant", 3)
    
    for i, practice in enumerate(practices, 1):
        print(f"\n연습 {i}:")
        print(f"상황: {practice['topic']}")
        print(f"제시: {practice['prompt']}")
        print("가능한 응답:")
        for response in practice['responses']:
            print(f"  - {response}")
    
    # 간격 반복 세션
    print("\n\n=== 간격 반복 학습 세션 ===")
    session = service.create_spaced_repetition_session()
    
    print(f"\n1. 워밍업 ({len(session['warm_up'])}개)")
    print(f"2. 새로운 내용 ({len(session['new_content'])}개)")
    print(f"3. 복습 ({len(session['review'])}개)")
    print(f"4. 퀴즈 ({len(session['quick_quiz'])}개)")
