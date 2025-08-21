"""
Vocabulary Learning Service
주제별 단어 학습 및 플래시카드 서비스
"""

from typing import Dict, List, Optional
import random
from datetime import datetime, timedelta

class VocabularyService:
    """스페인어 단어 학습 서비스"""
    
    def __init__(self):
        # 주제별 단어 데이터베이스
        self.vocabulary_topics = {
            "greetings": {
                "title": "인사와 기본 표현",
                "words": [
                    {"spanish": "hola", "korean": "안녕", "example": "¡Hola! ¿Cómo estás?", "type": "interjection"},
                    {"spanish": "buenos días", "korean": "좋은 아침", "example": "Buenos días, señora.", "type": "phrase"},
                    {"spanish": "buenas tardes", "korean": "좋은 오후", "example": "Buenas tardes, ¿cómo está?", "type": "phrase"},
                    {"spanish": "buenas noches", "korean": "좋은 저녁/밤", "example": "Buenas noches, que descanses.", "type": "phrase"},
                    {"spanish": "adiós", "korean": "안녕히 가세요", "example": "Adiós, hasta mañana.", "type": "interjection"},
                    {"spanish": "hasta luego", "korean": "나중에 봐", "example": "Hasta luego, amigo.", "type": "phrase"},
                    {"spanish": "por favor", "korean": "부탁해요", "example": "Un café, por favor.", "type": "phrase"},
                    {"spanish": "gracias", "korean": "감사합니다", "example": "Muchas gracias por tu ayuda.", "type": "noun"},
                    {"spanish": "de nada", "korean": "천만에요", "example": "- Gracias. - De nada.", "type": "phrase"},
                    {"spanish": "perdón", "korean": "실례합니다", "example": "Perdón, ¿dónde está el baño?", "type": "noun"}
                ]
            },
            "family": {
                "title": "가족",
                "words": [
                    {"spanish": "familia", "korean": "가족", "example": "Mi familia es grande.", "type": "noun_f"},
                    {"spanish": "padre", "korean": "아버지", "example": "Mi padre trabaja mucho.", "type": "noun_m"},
                    {"spanish": "madre", "korean": "어머니", "example": "Mi madre cocina muy bien.", "type": "noun_f"},
                    {"spanish": "hermano", "korean": "형제/남동생", "example": "Tengo dos hermanos.", "type": "noun_m"},
                    {"spanish": "hermana", "korean": "자매/여동생", "example": "Mi hermana estudia medicina.", "type": "noun_f"},
                    {"spanish": "hijo", "korean": "아들", "example": "Su hijo tiene 10 años.", "type": "noun_m"},
                    {"spanish": "hija", "korean": "딸", "example": "Nuestra hija es profesora.", "type": "noun_f"},
                    {"spanish": "abuelo", "korean": "할아버지", "example": "Mi abuelo vive en el campo.", "type": "noun_m"},
                    {"spanish": "abuela", "korean": "할머니", "example": "La abuela hace galletas.", "type": "noun_f"},
                    {"spanish": "primo/prima", "korean": "사촌", "example": "Mi primo vive en Madrid.", "type": "noun"}
                ]
            },
            "food": {
                "title": "음식",
                "words": [
                    {"spanish": "comida", "korean": "음식", "example": "La comida española es deliciosa.", "type": "noun_f"},
                    {"spanish": "desayuno", "korean": "아침 식사", "example": "El desayuno es a las 8.", "type": "noun_m"},
                    {"spanish": "almuerzo", "korean": "점심", "example": "¿Qué hay para el almuerzo?", "type": "noun_m"},
                    {"spanish": "cena", "korean": "저녁 식사", "example": "La cena está lista.", "type": "noun_f"},
                    {"spanish": "pan", "korean": "빵", "example": "Compro pan todas las mañanas.", "type": "noun_m"},
                    {"spanish": "agua", "korean": "물", "example": "Necesito un vaso de agua.", "type": "noun_f"},
                    {"spanish": "café", "korean": "커피", "example": "¿Quieres café con leche?", "type": "noun_m"},
                    {"spanish": "leche", "korean": "우유", "example": "La leche está en la nevera.", "type": "noun_f"},
                    {"spanish": "carne", "korean": "고기", "example": "No como carne los viernes.", "type": "noun_f"},
                    {"spanish": "pescado", "korean": "생선", "example": "El pescado está muy fresco.", "type": "noun_m"}
                ]
            },
            "numbers": {
                "title": "숫자",
                "words": [
                    {"spanish": "cero", "korean": "0", "example": "Cero más cero es cero.", "type": "number"},
                    {"spanish": "uno", "korean": "1", "example": "Tengo uno perro.", "type": "number"},
                    {"spanish": "dos", "korean": "2", "example": "Dos más dos son cuatro.", "type": "number"},
                    {"spanish": "tres", "korean": "3", "example": "Hay tres libros en la mesa.", "type": "number"},
                    {"spanish": "cuatro", "korean": "4", "example": "Las cuatro estaciones.", "type": "number"},
                    {"spanish": "cinco", "korean": "5", "example": "Cinco dedos en cada mano.", "type": "number"},
                    {"spanish": "seis", "korean": "6", "example": "Trabajo seis días a la semana.", "type": "number"},
                    {"spanish": "siete", "korean": "7", "example": "Los siete días de la semana.", "type": "number"},
                    {"spanish": "ocho", "korean": "8", "example": "Son las ocho de la mañana.", "type": "number"},
                    {"spanish": "nueve", "korean": "9", "example": "Nueve meses de embarazo.", "type": "number"},
                    {"spanish": "diez", "korean": "10", "example": "Diez minutos de descanso.", "type": "number"}
                ]
            },
            "colors": {
                "title": "색깔",
                "words": [
                    {"spanish": "color", "korean": "색", "example": "¿Cuál es tu color favorito?", "type": "noun_m"},
                    {"spanish": "rojo", "korean": "빨간색", "example": "El tomate es rojo.", "type": "adjective"},
                    {"spanish": "azul", "korean": "파란색", "example": "El cielo es azul.", "type": "adjective"},
                    {"spanish": "verde", "korean": "초록색", "example": "La hierba es verde.", "type": "adjective"},
                    {"spanish": "amarillo", "korean": "노란색", "example": "El sol es amarillo.", "type": "adjective"},
                    {"spanish": "negro", "korean": "검은색", "example": "El café es negro.", "type": "adjective"},
                    {"spanish": "blanco", "korean": "흰색", "example": "La nieve es blanca.", "type": "adjective"},
                    {"spanish": "gris", "korean": "회색", "example": "El elefante es gris.", "type": "adjective"},
                    {"spanish": "rosa", "korean": "분홍색", "example": "Las flores son rosas.", "type": "adjective"},
                    {"spanish": "naranja", "korean": "주황색", "example": "La naranja es naranja.", "type": "adjective"}
                ]
            },
            "time": {
                "title": "시간",
                "words": [
                    {"spanish": "tiempo", "korean": "시간", "example": "No tengo tiempo.", "type": "noun_m"},
                    {"spanish": "hora", "korean": "시각/시간", "example": "¿Qué hora es?", "type": "noun_f"},
                    {"spanish": "día", "korean": "날/낮", "example": "Buenos días.", "type": "noun_m"},
                    {"spanish": "semana", "korean": "주", "example": "La próxima semana.", "type": "noun_f"},
                    {"spanish": "mes", "korean": "달", "example": "Este mes es enero.", "type": "noun_m"},
                    {"spanish": "año", "korean": "년", "example": "El año nuevo.", "type": "noun_m"},
                    {"spanish": "hoy", "korean": "오늘", "example": "Hoy es lunes.", "type": "adverb"},
                    {"spanish": "mañana", "korean": "내일/아침", "example": "Hasta mañana.", "type": "noun_f/adverb"},
                    {"spanish": "ayer", "korean": "어제", "example": "Ayer fui al cine.", "type": "adverb"},
                    {"spanish": "ahora", "korean": "지금", "example": "Ahora mismo voy.", "type": "adverb"}
                ]
            },
            "body": {
                "title": "신체",
                "words": [
                    {"spanish": "cuerpo", "korean": "몸", "example": "El cuerpo humano.", "type": "noun_m"},
                    {"spanish": "cabeza", "korean": "머리", "example": "Me duele la cabeza.", "type": "noun_f"},
                    {"spanish": "ojo", "korean": "눈", "example": "Tengo los ojos azules.", "type": "noun_m"},
                    {"spanish": "nariz", "korean": "코", "example": "Tu nariz es pequeña.", "type": "noun_f"},
                    {"spanish": "boca", "korean": "입", "example": "Abre la boca.", "type": "noun_f"},
                    {"spanish": "oreja", "korean": "귀", "example": "Las orejas del conejo.", "type": "noun_f"},
                    {"spanish": "mano", "korean": "손", "example": "Dame la mano.", "type": "noun_f"},
                    {"spanish": "pie", "korean": "발", "example": "Me duele el pie.", "type": "noun_m"},
                    {"spanish": "brazo", "korean": "팔", "example": "Levanta el brazo.", "type": "noun_m"},
                    {"spanish": "pierna", "korean": "다리", "example": "Tengo las piernas cansadas.", "type": "noun_f"}
                ]
            }
        }
        
        # 학습 진도 추적 (실제로는 DB에 저장)
        self.user_progress = {}
        
    def get_topics(self) -> List[Dict]:
        """사용 가능한 주제 목록 반환"""
        return [
            {
                "id": topic_id,
                "title": topic_data["title"],
                "word_count": len(topic_data["words"])
            }
            for topic_id, topic_data in self.vocabulary_topics.items()
        ]
    
    def get_topic_words(self, topic_id: str) -> List[Dict]:
        """특정 주제의 단어 목록 반환"""
        if topic_id in self.vocabulary_topics:
            return self.vocabulary_topics[topic_id]["words"]
        return []
    
    def get_flashcard_session(self, topic_id: str, count: int = 10) -> List[Dict]:
        """플래시카드 세션 생성"""
        words = self.get_topic_words(topic_id)
        if not words:
            return []
        
        # 단어가 부족하면 반복 허용
        session_words = []
        while len(session_words) < count:
            remaining = count - len(session_words)
            sample_size = min(remaining, len(words))
            session_words.extend(random.sample(words, sample_size))
        
        # 플래시카드 형식으로 변환
        flashcards = []
        for word in session_words[:count]:
            # 50% 확률로 스페인어 → 한국어 또는 한국어 → 스페인어
            if random.random() < 0.5:
                flashcards.append({
                    "front": word["spanish"],
                    "back": word["korean"],
                    "example": word.get("example", ""),
                    "type": word.get("type", ""),
                    "direction": "es_to_ko"
                })
            else:
                flashcards.append({
                    "front": word["korean"],
                    "back": word["spanish"],
                    "example": word.get("example", ""),
                    "type": word.get("type", ""),
                    "direction": "ko_to_es"
                })
        
        return flashcards
    
    def get_word_quiz(self, topic_id: str) -> Dict:
        """단어 퀴즈 문제 생성"""
        words = self.get_topic_words(topic_id)
        if len(words) < 4:
            return None
        
        # 정답 선택
        correct_word = random.choice(words)
        
        # 오답 선택 (3개)
        other_words = [w for w in words if w != correct_word]
        wrong_words = random.sample(other_words, min(3, len(other_words)))
        
        # 보기 생성
        options = [correct_word] + wrong_words
        random.shuffle(options)
        
        # 문제 유형 선택
        quiz_type = random.choice(['es_to_ko', 'ko_to_es', 'example'])
        
        if quiz_type == 'es_to_ko':
            return {
                "question": f"'{correct_word['spanish']}'의 뜻은?",
                "options": [opt['korean'] for opt in options],
                "answer": correct_word['korean'],
                "type": "es_to_ko"
            }
        elif quiz_type == 'ko_to_es':
            return {
                "question": f"'{correct_word['korean']}'를 스페인어로?",
                "options": [opt['spanish'] for opt in options],
                "answer": correct_word['spanish'],
                "type": "ko_to_es"
            }
        else:  # example
            if correct_word.get('example'):
                # 예문에서 단어를 빈칸으로
                example = correct_word['example']
                blank_example = example.replace(correct_word['spanish'], '____')
                return {
                    "question": f"빈칸에 들어갈 단어는?\n{blank_example}",
                    "options": [opt['spanish'] for opt in options],
                    "answer": correct_word['spanish'],
                    "hint": correct_word['korean'],
                    "type": "example"
                }
        
        return None
    
    def record_progress(self, user_id: str, word: Dict, correct: bool):
        """학습 진도 기록"""
        if user_id not in self.user_progress:
            self.user_progress[user_id] = {}
        
        word_key = word['spanish']
        if word_key not in self.user_progress[user_id]:
            self.user_progress[user_id][word_key] = {
                'attempts': 0,
                'correct': 0,
                'last_seen': None,
                'mastery_level': 0  # 0-5
            }
        
        progress = self.user_progress[user_id][word_key]
        progress['attempts'] += 1
        if correct:
            progress['correct'] += 1
            progress['mastery_level'] = min(5, progress['mastery_level'] + 1)
        else:
            progress['mastery_level'] = max(0, progress['mastery_level'] - 1)
        
        progress['last_seen'] = datetime.now()
        
    def get_review_words(self, user_id: str, count: int = 10) -> List[Dict]:
        """복습이 필요한 단어 선택"""
        if user_id not in self.user_progress:
            return []
        
        # 마스터리 레벨이 낮거나 오래 안 본 단어 우선
        review_candidates = []
        
        for word_key, progress in self.user_progress[user_id].items():
            if progress['mastery_level'] < 4:  # 마스터리 레벨 4 미만
                # 모든 주제에서 해당 단어 찾기
                for topic_words in self.vocabulary_topics.values():
                    for word in topic_words['words']:
                        if word['spanish'] == word_key:
                            review_candidates.append({
                                'word': word,
                                'priority': 5 - progress['mastery_level']  # 낮은 레벨일수록 높은 우선순위
                            })
                            break
        
        # 우선순위로 정렬
        review_candidates.sort(key=lambda x: x['priority'], reverse=True)
        
        # 상위 N개 반환
        return [candidate['word'] for candidate in review_candidates[:count]]

# 사용 예시
if __name__ == "__main__":
    service = VocabularyService()
    
    print("=== 사용 가능한 주제 ===")
    topics = service.get_topics()
    for topic in topics:
        print(f"- {topic['title']} ({topic['word_count']}개)")
    
    print("\n=== 가족 주제 플래시카드 ===")
    flashcards = service.get_flashcard_session("family", 5)
    for i, card in enumerate(flashcards, 1):
        print(f"{i}. {card['front']} → {card['back']}")
        if card['example']:
            print(f"   예문: {card['example']}")
    
    print("\n=== 단어 퀴즈 ===")
    quiz = service.get_word_quiz("food")
    if quiz:
        print(f"문제: {quiz['question']}")
        for i, option in enumerate(quiz['options'], 1):
            print(f"{i}. {option}")
        print(f"정답: {quiz['answer']}")
