"""
PDF 교재 텍스트 추출 및 구조화
Nuevo Español en Marcha 교재를 학습 가능한 형태로 변환
"""

import PyPDF2
import sys
import json
import re
from pathlib import Path
from typing import Dict, List

class TextbookExtractor:
    def __init__(self, pdf_path: str):
        self.pdf_path = pdf_path
        self.extracted_data = {
            "units": {},
            "vocabulary": {},
            "dialogues": [],
            "exercises": []
        }
    
    def extract_text(self) -> str:
        """PDF에서 텍스트 추출"""
        text = ""
        with open(self.pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text += page.extract_text() + "\n"
        
        return text
    
    def parse_unit_structure(self, text: str) -> Dict:
        """교재 단원 구조 파싱"""
        units = {}
        
        # 단원 패턴 찾기 (예: "Unidad 1", "UNIDAD 1", etc.)
        unit_pattern = r"(?:Unidad|UNIDAD)\s+(\d+)"
        unit_matches = re.finditer(unit_pattern, text, re.IGNORECASE)
        
        for match in unit_matches:
            unit_number = match.group(1)
            unit_start = match.start()
            
            # 다음 단원 시작점 찾기
            next_unit = re.search(unit_pattern, text[unit_start + 10:])
            unit_end = next_unit.start() + unit_start + 10 if next_unit else len(text)
            
            unit_content = text[unit_start:unit_end]
            
            units[f"unidad_{unit_number}"] = {
                "number": unit_number,
                "content": unit_content,
                "sections": self._parse_sections(unit_content)
            }
        
        return units
    
    def _parse_sections(self, unit_text: str) -> Dict:
        """단원 내 섹션 파싱"""
        sections = {
            "vocabulary": [],
            "grammar": [],
            "dialogues": [],
            "exercises": []
        }
        
        # 어휘 섹션 찾기
        vocab_pattern = r"(?:Vocabulario|VOCABULARIO|Léxico)(.*?)(?=\n[A-Z])"
        vocab_matches = re.findall(vocab_pattern, unit_text, re.DOTALL | re.IGNORECASE)
        
        for vocab in vocab_matches:
            words = self._extract_vocabulary(vocab)
            sections["vocabulary"].extend(words)
        
        # 문법 섹션 찾기
        grammar_pattern = r"(?:Gramática|GRAMÁTICA)(.*?)(?=\n[A-Z])"
        grammar_matches = re.findall(grammar_pattern, unit_text, re.DOTALL | re.IGNORECASE)
        
        for grammar in grammar_matches:
            sections["grammar"].append(self._clean_text(grammar))
        
        return sections
    
    def _extract_vocabulary(self, vocab_text: str) -> List[Dict]:
        """어휘 추출 및 구조화"""
        vocabulary = []
        
        # 스페인어-한국어 패턴 (예: "casa - 집")
        word_pattern = r"([a-záéíóúñ]+)\s*[-–]\s*([가-힣]+)"
        matches = re.findall(word_pattern, vocab_text, re.IGNORECASE)
        
        for spanish, korean in matches:
            vocabulary.append({
                "spanish": spanish.strip(),
                "korean": korean.strip(),
                "type": self._guess_word_type(spanish)
            })
        
        return vocabulary
    
    def _guess_word_type(self, word: str) -> str:
        """단어 유형 추측 (명사, 동사 등)"""
        if word.endswith(('ar', 'er', 'ir')):
            return "verb"
        elif word.endswith(('ción', 'dad', 'ía')):
            return "noun_feminine"
        elif word.endswith(('o', 'e')):
            return "noun"
        else:
            return "other"
    
    def _clean_text(self, text: str) -> str:
        """텍스트 정리"""
        # 불필요한 공백 제거
        text = re.sub(r'\s+', ' ', text)
        # 페이지 번호 제거
        text = re.sub(r'\d+\s*$', '', text)
        return text.strip()
    
    def save_to_json(self, output_path: str):
        """추출된 데이터를 JSON으로 저장"""
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(self.extracted_data, f, ensure_ascii=False, indent=2)
    
    def extract_sample_dialogues(self, text: str) -> List[Dict]:
        """대화문 추출"""
        dialogues = []
        
        # 대화 패턴 찾기
        dialogue_pattern = r"(?:Diálogo|DIÁLOGO|Conversación)\s*\d*(.*?)(?=\n\n)"
        dialogue_matches = re.findall(dialogue_pattern, text, re.DOTALL | re.IGNORECASE)
        
        for dialogue in dialogue_matches:
            lines = dialogue.strip().split('\n')
            parsed_dialogue = []
            
            for line in lines:
                # 화자와 대사 분리 (예: "María: Hola, ¿cómo estás?")
                speaker_pattern = r"^([A-Za-záéíóúñÁÉÍÓÚÑ]+):\s*(.+)"
                match = re.match(speaker_pattern, line.strip())
                
                if match:
                    parsed_dialogue.append({
                        "speaker": match.group(1),
                        "text": match.group(2),
                        "translation": ""  # 나중에 번역 추가
                    })
            
            if parsed_dialogue:
                dialogues.append({
                    "dialogue": parsed_dialogue,
                    "context": "",  # 상황 설명 추가 가능
                    "unit": ""  # 단원 정보
                })
        
        return dialogues
    
    def run_extraction(self):
        """전체 추출 프로세스 실행"""
        print("📚 PDF 텍스트 추출 중...")
        raw_text = self.extract_text()
        
        print("🔍 단원 구조 파싱 중...")
        self.extracted_data["units"] = self.parse_unit_structure(raw_text)
        
        print("💬 대화문 추출 중...")
        self.extracted_data["dialogues"] = self.extract_sample_dialogues(raw_text)
        
        print("✅ 추출 완료!")
        
        # 요약 정보 출력
        print(f"\n📊 추출 결과:")
        print(f"- 단원 수: {len(self.extracted_data['units'])}")
        print(f"- 대화문 수: {len(self.extracted_data['dialogues'])}")
        
        total_vocab = sum(len(unit['sections']['vocabulary']) 
                         for unit in self.extracted_data['units'].values())
        print(f"- 총 어휘 수: {total_vocab}")

# 사용 예시
if __name__ == "__main__":
    # 기본 경로 (인자를 통해 덮어쓸 수 있음)
    pdf_path = "../data/textbook/nuevo_espanol_1.pdf"
    output_path = "../data/textbook/extracted_content.json"

    # 사용법: python pdf_extractor.py [PDF_PATH] [OUTPUT_JSON_PATH]
    if len(sys.argv) >= 2 and sys.argv[1].strip():
        pdf_path = sys.argv[1]
    if len(sys.argv) >= 3 and sys.argv[2].strip():
        output_path = sys.argv[2]

    # 추출기 실행
    extractor = TextbookExtractor(pdf_path)
    extractor.run_extraction()

    # JSON으로 저장
    extractor.save_to_json(output_path)

    print(f"\n💾 추출된 데이터가 {output_path}에 저장되었습니다.")
