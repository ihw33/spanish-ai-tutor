const vocabularyData = [
    // 인사/기본
    { spanish: "hola", korean: "안녕하세요", category: "인사", gender: null, type: "감탄사" },
    { spanish: "buenos días", korean: "좋은 아침", category: "인사", gender: null, type: "구" },
    { spanish: "buenas tardes", korean: "좋은 오후/저녁", category: "인사", gender: null, type: "구" },
    { spanish: "adiós", korean: "안녕히 가세요", category: "인사", gender: null, type: "감탄사" },
    { spanish: "por favor", korean: "부탁합니다", category: "인사", gender: null, type: "구" },
    { spanish: "gracias", korean: "감사합니다", category: "인사", gender: null, type: "명사" },
    { spanish: "perdón", korean: "실례합니다/죄송합니다", category: "인사", gender: "m", type: "명사" },
    
    // 가족
    { spanish: "familia", korean: "가족", category: "가족", gender: "f", type: "명사",
      example: { spanish: "Mi familia es grande", korean: "우리 가족은 대가족이에요" }},
    { spanish: "padre", korean: "아버지", category: "가족", gender: "m", type: "명사" },
    { spanish: "madre", korean: "어머니", category: "가족", gender: "f", type: "명사" },
    { spanish: "hermano", korean: "남자 형제", category: "가족", gender: "m", type: "명사" },
    { spanish: "hermana", korean: "여자 형제", category: "가족", gender: "f", type: "명사" },
    { spanish: "hijo", korean: "아들", category: "가족", gender: "m", type: "명사" },
    { spanish: "hija", korean: "딸", category: "가족", gender: "f", type: "명사" },
    { spanish: "abuelo", korean: "할아버지", category: "가족", gender: "m", type: "명사" },
    { spanish: "abuela", korean: "할머니", category: "가족", gender: "f", type: "명사" },
    
    // 숫자
    { spanish: "uno", korean: "1", category: "숫자", gender: null, type: "수사" },
    { spanish: "dos", korean: "2", category: "숫자", gender: null, type: "수사" },
    { spanish: "tres", korean: "3", category: "숫자", gender: null, type: "수사" },
    { spanish: "cuatro", korean: "4", category: "숫자", gender: null, type: "수사" },
    { spanish: "cinco", korean: "5", category: "숫자", gender: null, type: "수사" },
    { spanish: "diez", korean: "10", category: "숫자", gender: null, type: "수사" },
    { spanish: "veinte", korean: "20", category: "숫자", gender: null, type: "수사" },
    { spanish: "cien", korean: "100", category: "숫자", gender: null, type: "수사" },
    
    // 시간
    { spanish: "hora", korean: "시간", category: "시간", gender: "f", type: "명사",
      example: { spanish: "¿Qué hora es?", korean: "몇 시예요?" }},
    { spanish: "día", korean: "날/하루", category: "시간", gender: "m", type: "명사" },
    { spanish: "semana", korean: "주", category: "시간", gender: "f", type: "명사" },
    { spanish: "mes", korean: "달", category: "시간", gender: "m", type: "명사" },
    { spanish: "año", korean: "년", category: "시간", gender: "m", type: "명사" },
    { spanish: "hoy", korean: "오늘", category: "시간", gender: null, type: "부사" },
    { spanish: "mañana", korean: "내일/아침", category: "시간", gender: "f", type: "명사" },
    { spanish: "ayer", korean: "어제", category: "시간", gender: null, type: "부사" },
    
    // 장소
    { spanish: "casa", korean: "집", category: "장소", gender: "f", type: "명사",
      example: { spanish: "Voy a casa", korean: "집에 가요" }},
    { spanish: "escuela", korean: "학교", category: "장소", gender: "f", type: "명사" },
    { spanish: "tienda", korean: "가게", category: "장소", gender: "f", type: "명사" },
    { spanish: "restaurante", korean: "레스토랑", category: "장소", gender: "m", type: "명사" },
    { spanish: "hospital", korean: "병원", category: "장소", gender: "m", type: "명사" },
    { spanish: "banco", korean: "은행", category: "장소", gender: "m", type: "명사" },
    { spanish: "calle", korean: "거리", category: "장소", gender: "f", type: "명사" },
    { spanish: "ciudad", korean: "도시", category: "장소", gender: "f", type: "명사" },
    
    // 음식
    { spanish: "comida", korean: "음식", category: "음식", gender: "f", type: "명사" },
    { spanish: "agua", korean: "물", category: "음식", gender: "f", type: "명사",
      example: { spanish: "El agua está fría", korean: "물이 차갑습니다" }},
    { spanish: "pan", korean: "빵", category: "음식", gender: "m", type: "명사" },
    { spanish: "café", korean: "커피", category: "음식", gender: "m", type: "명사" },
    { spanish: "leche", korean: "우유", category: "음식", gender: "f", type: "명사" },
    { spanish: "carne", korean: "고기", category: "음식", gender: "f", type: "명사" },
    { spanish: "pollo", korean: "닭고기", category: "음식", gender: "m", type: "명사" },
    { spanish: "pescado", korean: "생선", category: "음식", gender: "m", type: "명사" },
    { spanish: "fruta", korean: "과일", category: "음식", gender: "f", type: "명사" },
    { spanish: "verdura", korean: "채소", category: "음식", gender: "f", type: "명사" }
];