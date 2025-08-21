"""
Grammar Practice Service
문법 연습을 위한 서비스 - Ser/Estar, 전치사, 의문사 등
"""

from typing import Dict, List, Optional
import random

class GrammarPracticeService:
    """스페인어 문법 연습 서비스"""
    
    def __init__(self):
        # Ser vs Estar 연습 데이터
        self.ser_estar_exercises = [
            {
                "sentence": "Mi hermano ___ médico.",
                "answer": "es",
                "explanation": "직업은 항상 SER를 사용합니다.",
                "translation": "내 형/동생은 의사다."
            },
            {
                "sentence": "El café ___ frío.",
                "answer": "está",
                "explanation": "음식의 온도는 일시적 상태이므로 ESTAR를 사용합니다.",
                "translation": "커피가 차갑다."
            },
            {
                "sentence": "María ___ en casa.",
                "answer": "está",
                "explanation": "위치를 나타낼 때는 ESTAR를 사용합니다.",
                "translation": "마리아는 집에 있다."
            },
            {
                "sentence": "Nosotros ___ coreanos.",
                "answer": "somos",
                "explanation": "국적은 변하지 않는 특성이므로 SER를 사용합니다.",
                "translation": "우리는 한국인이다."
            },
            {
                "sentence": "La fiesta ___ mañana.",
                "answer": "es",
                "explanation": "이벤트의 시간은 SER를 사용합니다.",
                "translation": "파티는 내일이다."
            },
            {
                "sentence": "Juan ___ muy cansado hoy.",
                "answer": "está",
                "explanation": "피곤함은 일시적 상태이므로 ESTAR를 사용합니다.",
                "translation": "후안은 오늘 매우 피곤하다."
            },
            {
                "sentence": "El libro ___ interesante.",
                "answer": "es",
                "explanation": "책의 본질적 특성이므로 SER를 사용합니다.",
                "translation": "그 책은 흥미롭다."
            },
            {
                "sentence": "La puerta ___ abierta.",
                "answer": "está",
                "explanation": "문이 열려있는 것은 일시적 상태이므로 ESTAR를 사용합니다.",
                "translation": "문이 열려있다."
            }
        ]
        
        # 전치사 연습 데이터
        self.preposition_exercises = [
            {
                "sentence": "Voy ___ la escuela.",
                "options": ["a", "de", "en", "por"],
                "answer": "a",
                "explanation": "장소로 가는 것을 나타낼 때는 'a'를 사용합니다.",
                "translation": "나는 학교에 간다."
            },
            {
                "sentence": "El libro es ___ María.",
                "options": ["a", "de", "para", "por"],
                "answer": "de",
                "explanation": "소유를 나타낼 때는 'de'를 사용합니다.",
                "translation": "그 책은 마리아의 것이다."
            },
            {
                "sentence": "Estoy ___ casa.",
                "options": ["a", "de", "en", "por"],
                "answer": "en",
                "explanation": "위치를 나타낼 때는 'en'을 사용합니다.",
                "translation": "나는 집에 있다."
            },
            {
                "sentence": "Este regalo es ___ ti.",
                "options": ["a", "de", "para", "por"],
                "answer": "para",
                "explanation": "목적이나 수신자를 나타낼 때는 'para'를 사용합니다.",
                "translation": "이 선물은 너를 위한 것이다."
            },
            {
                "sentence": "Hablo ___ teléfono.",
                "options": ["en", "por", "con", "de"],
                "answer": "por",
                "explanation": "수단을 나타낼 때는 'por'를 사용합니다.",
                "translation": "나는 전화로 이야기한다."
            },
            {
                "sentence": "Vivo ___ mi familia.",
                "options": ["a", "de", "con", "por"],
                "answer": "con",
                "explanation": "함께함을 나타낼 때는 'con'을 사용합니다.",
                "translation": "나는 가족과 함께 산다."
            }
        ]
        
        # 의문사 연습 데이터
        self.question_words_exercises = [
            {
                "answer": "¿Dónde vives?",
                "translation": "너는 어디에 살아?",
                "hint": "장소를 묻는 의문사",
                "options": ["¿Qué?", "¿Dónde?", "¿Cuándo?", "¿Quién?"],
                "correct": "¿Dónde?"
            },
            {
                "answer": "¿Cuándo es tu cumpleaños?",
                "translation": "너의 생일은 언제야?",
                "hint": "시간을 묻는 의문사",
                "options": ["¿Qué?", "¿Dónde?", "¿Cuándo?", "¿Por qué?"],
                "correct": "¿Cuándo?"
            },
            {
                "answer": "¿Por qué estudias español?",
                "translation": "왜 스페인어를 공부해?",
                "hint": "이유를 묻는 의문사",
                "options": ["¿Por qué?", "¿Para qué?", "¿Cómo?", "¿Cuál?"],
                "correct": "¿Por qué?"
            },
            {
                "answer": "¿Cuánto cuesta esto?",
                "translation": "이거 얼마야?",
                "hint": "양이나 가격을 묻는 의문사",
                "options": ["¿Cuál?", "¿Qué?", "¿Cuánto?", "¿Cómo?"],
                "correct": "¿Cuánto?"
            },
            {
                "answer": "¿Quién es tu profesor?",
                "translation": "너의 선생님은 누구야?",
                "hint": "사람을 묻는 의문사",
                "options": ["¿Qué?", "¿Quién?", "¿Cuál?", "¿Dónde?"],
                "correct": "¿Quién?"
            }
        ]
        
        # 목적격 대명사 연습
        self.object_pronoun_exercises = [
            {
                "sentence": "Yo ___ veo. (a ti)",
                "answer": "te",
                "explanation": "2인칭 단수 직접목적격 대명사는 'te'입니다.",
                "translation": "나는 너를 본다."
            },
            {
                "sentence": "___ llamo María. (yo)",
                "answer": "Me",
                "explanation": "1인칭 단수 재귀대명사는 'me'입니다.",
                "translation": "나는 마리아라고 불린다."
            },
            {
                "sentence": "¿___ gusta el café? (a ti)",
                "answer": "Te",
                "explanation": "Gustar 동사와 함께 쓰이는 2인칭 간접목적격 대명사는 'te'입니다.",
                "translation": "너는 커피를 좋아하니?"
            },
            {
                "sentence": "Juan ___ da un regalo. (a mí)",
                "answer": "me",
                "explanation": "1인칭 단수 간접목적격 대명사는 'me'입니다.",
                "translation": "후안은 나에게 선물을 준다."
            }
        ]
    
    def get_ser_estar_exercise(self) -> Dict:
        """Ser/Estar 연습 문제 반환"""
        return random.choice(self.ser_estar_exercises)
    
    def get_preposition_exercise(self) -> Dict:
        """전치사 연습 문제 반환"""
        return random.choice(self.preposition_exercises)
    
    def get_question_word_exercise(self) -> Dict:
        """의문사 연습 문제 반환"""
        return random.choice(self.question_words_exercises)
    
    def get_mixed_grammar_exercise(self) -> Dict:
        """혼합 문법 연습 문제 반환"""
        exercise_type = random.choice(['ser_estar', 'preposition', 'question_word', 'object_pronoun'])
        
        if exercise_type == 'ser_estar':
            ex = self.get_ser_estar_exercise()
            ex['type'] = 'ser_estar'
            ex['instruction'] = "Ser 또는 Estar를 올바른 형태로 넣으세요."
        elif exercise_type == 'preposition':
            ex = self.get_preposition_exercise()
            ex['type'] = 'preposition'
            ex['instruction'] = "올바른 전치사를 선택하세요."
        elif exercise_type == 'question_word':
            ex = self.get_question_word_exercise()
            ex['type'] = 'question_word'
            ex['instruction'] = "올바른 의문사를 선택하세요."
        else:
            ex = random.choice(self.object_pronoun_exercises)
            ex['type'] = 'object_pronoun'
            ex['instruction'] = "올바른 대명사를 넣으세요."
        
        return ex
    
    def check_ser_estar_answer(self, user_answer: str, correct_answer: str) -> bool:
        """Ser/Estar 답변 확인"""
        # 활용형도 정답으로 인정
        ser_forms = ['soy', 'eres', 'es', 'somos', 'sois', 'son']
        estar_forms = ['estoy', 'estás', 'está', 'estamos', 'estáis', 'están']
        
        user_lower = user_answer.strip().lower()
        correct_lower = correct_answer.lower()
        
        # 정확한 답
        if user_lower == correct_lower:
            return True
        
        # Ser의 다른 활용형
        if correct_lower == 'es' and user_lower in ser_forms:
            return True
        
        # Estar의 다른 활용형
        if correct_lower == 'está' and user_lower in estar_forms:
            return True
        
        return False
    
    def get_grammar_tips(self, topic: str) -> List[str]:
        """문법 팁 제공"""
        tips = {
            'ser_estar': [
                "SER = 영구적 특성 (직업, 국적, 성격)",
                "ESTAR = 일시적 상태, 위치",
                "시간과 날짜는 항상 SER",
                "진행형은 ESTAR + gerundio",
                "형용사에 따라 의미가 달라짐: ser bueno (착하다) vs estar bueno (맛있다)"
            ],
            'preposition': [
                "A = 방향, 목적지 (voy a casa)",
                "DE = 소유, 출신, 재료 (el libro de Juan)",
                "EN = 위치, 수단 (estoy en casa)",
                "POR = 이유, 통과, 교환 (por la mañana)",
                "PARA = 목적, 수신자, 기한 (para ti)"
            ],
            'question_word': [
                "¿Qué? = 무엇 (정의를 물을 때)",
                "¿Cuál? = 어느 것 (선택할 때)",
                "¿Quién? = 누구 (단수) / ¿Quiénes? = 누구 (복수)",
                "¿Cuánto? = 얼마나 (양) + 명사 성수 일치",
                "의문사는 항상 악센트 표시!"
            ]
        }
        
        return tips.get(topic, [])

# 사용 예시
if __name__ == "__main__":
    service = GrammarPracticeService()
    
    print("=== Ser/Estar 연습 ===")
    exercise = service.get_ser_estar_exercise()
    print(f"문제: {exercise['sentence']}")
    print(f"번역: {exercise['translation']}")
    print(f"정답: {exercise['answer']}")
    print(f"설명: {exercise['explanation']}")
    
    print("\n=== 전치사 연습 ===")
    prep_ex = service.get_preposition_exercise()
    print(f"문제: {prep_ex['sentence']}")
    print(f"선택지: {', '.join(prep_ex['options'])}")
    print(f"정답: {prep_ex['answer']}")
    
    print("\n=== 문법 팁 ===")
    tips = service.get_grammar_tips('ser_estar')
    for tip in tips:
        print(f"• {tip}")
