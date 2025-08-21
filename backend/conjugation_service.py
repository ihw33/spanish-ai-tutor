"""
Spanish Verb Conjugation Service
동사 활용 연습을 위한 핵심 서비스
"""

from typing import Dict, List, Optional
from enum import Enum

class Tense(Enum):
    PRESENTE = "presente"
    PRETERITO = "pretérito"
    IMPERFECTO = "imperfecto"
    FUTURO = "futuro"
    CONDICIONAL = "condicional"
    PRESENTE_SUBJUNTIVO = "presente_subjuntivo"

class VerbConjugationService:
    def __init__(self):
        self.pronouns = ["yo", "tú", "él/ella/usted", "nosotros", "vosotros", "ellos/ellas/ustedes"]
        
        # 규칙 동사 어미
        self.regular_endings = {
            "ar": {
                Tense.PRESENTE: ["o", "as", "a", "amos", "áis", "an"],
                Tense.PRETERITO: ["é", "aste", "ó", "amos", "asteis", "aron"],
                Tense.IMPERFECTO: ["aba", "abas", "aba", "ábamos", "abais", "aban"],
            },
            "er": {
                Tense.PRESENTE: ["o", "es", "e", "emos", "éis", "en"],
                Tense.PRETERITO: ["í", "iste", "ió", "imos", "isteis", "ieron"],
                Tense.IMPERFECTO: ["ía", "ías", "ía", "íamos", "íais", "ían"],
            },
            "ir": {
                Tense.PRESENTE: ["o", "es", "e", "imos", "ís", "en"],
                Tense.PRETERITO: ["í", "iste", "ió", "imos", "isteis", "ieron"],
                Tense.IMPERFECTO: ["ía", "ías", "ía", "íamos", "íais", "ían"],
            }
        }
        
        # 불규칙 동사 데이터베이스
        self.irregular_verbs = {
            "ser": {
                Tense.PRESENTE: ["soy", "eres", "es", "somos", "sois", "son"],
                Tense.PRETERITO: ["fui", "fuiste", "fue", "fuimos", "fuisteis", "fueron"],
                Tense.IMPERFECTO: ["era", "eras", "era", "éramos", "erais", "eran"],
            },
            "estar": {
                Tense.PRESENTE: ["estoy", "estás", "está", "estamos", "estáis", "están"],
                Tense.PRETERITO: ["estuve", "estuviste", "estuvo", "estuvimos", "estuvisteis", "estuvieron"],
            },
            "tener": {
                Tense.PRESENTE: ["tengo", "tienes", "tiene", "tenemos", "tenéis", "tienen"],
                Tense.PRETERITO: ["tuve", "tuviste", "tuvo", "tuvimos", "tuvisteis", "tuvieron"],
            }
        }
    
    def conjugate(self, verb: str, tense: Tense) -> Dict[str, str]:
        """동사를 주어진 시제로 활용"""
        # 불규칙 동사 확인
        if verb in self.irregular_verbs and tense in self.irregular_verbs[verb]:
            conjugations = self.irregular_verbs[verb][tense]
        else:
            # 규칙 동사 활용
            stem, ending = self._get_stem_and_ending(verb)
            if ending in self.regular_endings and tense in self.regular_endings[ending]:
                endings = self.regular_endings[ending][tense]
                conjugations = [stem + e for e in endings]
            else:
                return {"error": f"Cannot conjugate {verb} in {tense.value}"}
        
        return {pronoun: conj for pronoun, conj in zip(self.pronouns, conjugations)}
    
    def _get_stem_and_ending(self, verb: str) -> tuple:
        """동사의 어간과 어미 분리"""
        if verb.endswith("ar"):
            return verb[:-2], "ar"
        elif verb.endswith("er"):
            return verb[:-2], "er"
        elif verb.endswith("ir"):
            return verb[:-2], "ir"
        else:
            return verb, ""
    
    def generate_practice_sentence(self, verb: str, tense: Tense, pronoun: str) -> Dict:
        """연습 문장 생성"""
        conjugation = self.conjugate(verb, tense)
        
        if "error" in conjugation:
            return conjugation
        
        correct_form = conjugation.get(pronoun, "")
        
        # 문맥에 맞는 예문 생성
        context_examples = {
            "hablar": {
                "yo": "_____ español todos los días. (나는 매일 스페인어를 말합니다)",
                "tú": "¿_____ inglés? (너는 영어를 말하니?)",
                "él/ella/usted": "Mi profesor _____ muy rápido. (우리 선생님은 매우 빨리 말합니다)",
            },
            "comer": {
                "yo": "_____ paella los domingos. (나는 일요일마다 빠에야를 먹습니다)",
                "nosotros": "_____ juntos en el restaurante. (우리는 레스토랑에서 함께 먹습니다)",
            }
        }
        
        base_verb = verb
        if base_verb in context_examples and pronoun in context_examples[base_verb]:
            sentence = context_examples[base_verb][pronoun]
        else:
            sentence = f"{pronoun} _____ (verb: {verb})"
        
        return {
            "sentence": sentence,
            "correct_answer": correct_form,
            "hint": f"{tense.value} 시제의 {pronoun} 형태"
        }
    
    def check_answer(self, user_answer: str, correct_answer: str) -> Dict:
        """사용자 답변 확인 및 피드백"""
        user_answer = user_answer.strip().lower()
        correct_answer = correct_answer.lower()
        
        if user_answer == correct_answer:
            return {
                "correct": True,
                "message": "¡Excelente! 정답입니다! 🎉"
            }
        else:
            # 일반적인 실수 패턴 확인
            feedback = self._get_specific_feedback(user_answer, correct_answer)
            
            return {
                "correct": False,
                "message": f"아쉽네요. 정답은 '{correct_answer}'입니다.",
                "feedback": feedback
            }
    
    def _get_specific_feedback(self, user_answer: str, correct_answer: str) -> str:
        """구체적인 피드백 제공"""
        # 악센트 빠뜨림
        if user_answer.replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u") == \
           correct_answer.replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u"):
            return "악센트 표시에 주의하세요! 스페인어에서 악센트는 발음과 의미에 중요합니다."
        
        # 어미 실수
        if len(user_answer) > 2 and len(correct_answer) > 2 and user_answer[:-2] == correct_answer[:-2]:
            return "어미 부분을 다시 확인해보세요. 주어에 따라 동사 어미가 달라집니다."
        
        return "동사 활용표를 다시 확인해보세요."

# 사용 예시
if __name__ == "__main__":
    service = VerbConjugationService()
    
    # hablar 동사 현재형 활용
    print("=== HABLAR (말하다) - Presente ===")
    result = service.conjugate("hablar", Tense.PRESENTE)
    for pronoun, form in result.items():
        print(f"{pronoun}: {form}")
    
    # 연습 문제 생성
    print("\n=== 연습 문제 ===")
    practice = service.generate_practice_sentence("hablar", Tense.PRESENTE, "yo")
    print(f"문제: {practice['sentence']}")
    print(f"힌트: {practice['hint']}")
    
    # 답변 확인
    user_input = "hablo"
    check = service.check_answer(user_input, practice['correct_answer'])
    print(f"답변 확인: {check['message']}")
