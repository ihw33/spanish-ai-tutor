// learningData.js - 문법과 단어 학습 데이터
const grammarExercises = {
    serEstar: [
        {
            sentence: "Mi hermano ___ médico.",
            answer: "es",
            explanation: "직업은 항상 SER를 사용합니다.",
            translation: "내 형/동생은 의사다."
        },
        {
            sentence: "El café ___ frío.",
            answer: "está",
            explanation: "음식의 온도는 일시적 상태이므로 ESTAR를 사용합니다.",
            translation: "커피가 차갑다."
        },
        {
            sentence: "María ___ en casa.",
            answer: "está",
            explanation: "위치를 나타낼 때는 ESTAR를 사용합니다.",
            translation: "마리아는 집에 있다."
        },
        {
            sentence: "Nosotros ___ coreanos.",
            answer: "somos",
            explanation: "국적은 변하지 않는 특성이므로 SER를 사용합니다.",
            translation: "우리는 한국인이다."
        },
        {
            sentence: "La fiesta ___ mañana.",
            answer: "es",
            explanation: "이벤트의 시간은 SER를 사용합니다.",
            translation: "파티는 내일이다."
        },
        {
            sentence: "Juan ___ muy cansado hoy.",
            answer: "está",
            explanation: "피곤함은 일시적 상태이므로 ESTAR를 사용합니다.",
            translation: "후안은 오늘 매우 피곤하다."
        },
        {
            sentence: "El libro ___ interesante.",
            answer: "es",
            explanation: "책의 본질적 특성이므로 SER를 사용합니다.",
            translation: "그 책은 흥미롭다."
        },
        {
            sentence: "La puerta ___ abierta.",
            answer: "está",
            explanation: "문이 열려있는 것은 일시적 상태이므로 ESTAR를 사용합니다.",
            translation: "문이 열려있다."
        }
    ],
    
    prepositions: [
        {
            sentence: "Voy ___ la escuela.",
            options: ["a", "de", "en", "por"],
            answer: "a",
            explanation: "장소로 가는 것을 나타낼 때는 'a'를 사용합니다.",
            translation: "나는 학교에 간다."
        },
        {
            sentence: "El libro es ___ María.",
            options: ["a", "de", "para", "por"],
            answer: "de",
            explanation: "소유를 나타낼 때는 'de'를 사용합니다.",
            translation: "그 책은 마리아의 것이다."
        },
        {
            sentence: "Estoy ___ casa.",
            options: ["a", "de", "en", "por"],
            answer: "en",
            explanation: "위치를 나타낼 때는 'en'을 사용합니다.",
            translation: "나는 집에 있다."
        },
        {
            sentence: "Este regalo es ___ ti.",
            options: ["a", "de", "para", "por"],
            answer: "para",
            explanation: "목적이나 수신자를 나타낼 때는 'para'를 사용합니다.",
            translation: "이 선물은 너를 위한 것이다."
        },
        {
            sentence: "Hablo ___ teléfono.",
            options: ["en", "por", "con", "de"],
            answer: "por",
            explanation: "수단을 나타낼 때는 'por'를 사용합니다.",
            translation: "나는 전화로 이야기한다."
        },
        {
            sentence: "Vivo ___ mi familia.",
            options: ["a", "de", "con", "por"],
            answer: "con",
            explanation: "함께함을 나타낼 때는 'con'을 사용합니다.",
            translation: "나는 가족과 함께 산다."
        }
    ],
    
    questionWords: [
        {
            question: "___ vives?",
            translation: "너는 어디에 살아?",
            hint: "장소를 묻는 의문사",
            options: ["¿Qué", "¿Dónde", "¿Cuándo", "¿Quién"],
            answer: "¿Dónde"
        },
        {
            question: "___ es tu cumpleaños?",
            translation: "너의 생일은 언제야?",
            hint: "시간을 묻는 의문사",
            options: ["¿Qué", "¿Dónde", "¿Cuándo", "¿Por qué"],
            answer: "¿Cuándo"
        },
        {
            question: "___ estudias español?",
            translation: "왜 스페인어를 공부해?",
            hint: "이유를 묻는 의문사",
            options: ["¿Por qué", "¿Para qué", "¿Cómo", "¿Cuál"],
            answer: "¿Por qué"
        },
        {
            question: "___ cuesta esto?",
            translation: "이거 얼마야?",
            hint: "양이나 가격을 묻는 의문사",
            options: ["¿Cuál", "¿Qué", "¿Cuánto", "¿Cómo"],
            answer: "¿Cuánto"
        },
        {
            question: "___ es tu profesor?",
            translation: "너의 선생님은 누구야?",
            hint: "사람을 묻는 의문사",
            options: ["¿Qué", "¿Quién", "¿Cuál", "¿Dónde"],
            answer: "¿Quién"
        }
    ]
};

const vocabularyTopics = {
    greetings: {
        title: "인사와 기본 표현",
        words: [
            {spanish: "hola", korean: "안녕", example: "¡Hola! ¿Cómo estás?"},
            {spanish: "buenos días", korean: "좋은 아침", example: "Buenos días, señora."},
            {spanish: "buenas tardes", korean: "좋은 오후", example: "Buenas tardes, ¿cómo está?"},
            {spanish: "buenas noches", korean: "좋은 저녁/밤", example: "Buenas noches, que descanses."},
            {spanish: "adiós", korean: "안녕히 가세요", example: "Adiós, hasta mañana."},
            {spanish: "hasta luego", korean: "나중에 봐", example: "Hasta luego, amigo."},
            {spanish: "por favor", korean: "부탁해요", example: "Un café, por favor."},
            {spanish: "gracias", korean: "감사합니다", example: "Muchas gracias por tu ayuda."},
            {spanish: "de nada", korean: "천만에요", example: "- Gracias. - De nada."},
            {spanish: "perdón", korean: "실례합니다", example: "Perdón, ¿dónde está el baño?"}
        ]
    },
    family: {
        title: "가족",
        words: [
            {spanish: "familia", korean: "가족", example: "Mi familia es grande."},
            {spanish: "padre", korean: "아버지", example: "Mi padre trabaja mucho."},
            {spanish: "madre", korean: "어머니", example: "Mi madre cocina muy bien."},
            {spanish: "hermano", korean: "형제/남동생", example: "Tengo dos hermanos."},
            {spanish: "hermana", korean: "자매/여동생", example: "Mi hermana estudia medicina."},
            {spanish: "hijo", korean: "아들", example: "Su hijo tiene 10 años."},
            {spanish: "hija", korean: "딸", example: "Nuestra hija es profesora."},
            {spanish: "abuelo", korean: "할아버지", example: "Mi abuelo vive en el campo."},
            {spanish: "abuela", korean: "할머니", example: "La abuela hace galletas."},
            {spanish: "primo/prima", korean: "사촌", example: "Mi primo vive en Madrid."}
        ]
    },
    food: {
        title: "음식",
        words: [
            {spanish: "comida", korean: "음식", example: "La comida española es deliciosa."},
            {spanish: "desayuno", korean: "아침 식사", example: "El desayuno es a las 8."},
            {spanish: "almuerzo", korean: "점심", example: "¿Qué hay para el almuerzo?"},
            {spanish: "cena", korean: "저녁 식사", example: "La cena está lista."},
            {spanish: "pan", korean: "빵", example: "Compro pan todas las mañanas."},
            {spanish: "agua", korean: "물", example: "Necesito un vaso de agua."},
            {spanish: "café", korean: "커피", example: "¿Quieres café con leche?"},
            {spanish: "leche", korean: "우유", example: "La leche está en la nevera."},
            {spanish: "carne", korean: "고기", example: "No como carne los viernes."},
            {spanish: "pescado", korean: "생선", example: "El pescado está muy fresco."}
        ]
    },
    numbers: {
        title: "숫자",
        words: [
            {spanish: "cero", korean: "0", example: "Cero más cero es cero."},
            {spanish: "uno", korean: "1", example: "Tengo un perro."},
            {spanish: "dos", korean: "2", example: "Dos más dos son cuatro."},
            {spanish: "tres", korean: "3", example: "Hay tres libros en la mesa."},
            {spanish: "cuatro", korean: "4", example: "Las cuatro estaciones."},
            {spanish: "cinco", korean: "5", example: "Cinco dedos en cada mano."},
            {spanish: "seis", korean: "6", example: "Trabajo seis días a la semana."},
            {spanish: "siete", korean: "7", example: "Los siete días de la semana."},
            {spanish: "ocho", korean: "8", example: "Son las ocho de la mañana."},
            {spanish: "nueve", korean: "9", example: "Nueve meses de embarazo."},
            {spanish: "diez", korean: "10", example: "Diez minutos de descanso."}
        ]
    },
    colors: {
        title: "색깔",
        words: [
            {spanish: "color", korean: "색", example: "¿Cuál es tu color favorito?"},
            {spanish: "rojo", korean: "빨간색", example: "El tomate es rojo."},
            {spanish: "azul", korean: "파란색", example: "El cielo es azul."},
            {spanish: "verde", korean: "초록색", example: "La hierba es verde."},
            {spanish: "amarillo", korean: "노란색", example: "El sol es amarillo."},
            {spanish: "negro", korean: "검은색", example: "El café es negro."},
            {spanish: "blanco", korean: "흰색", example: "La nieve es blanca."},
            {spanish: "gris", korean: "회색", example: "El elefante es gris."},
            {spanish: "rosa", korean: "분홍색", example: "Las flores son rosas."},
            {spanish: "naranja", korean: "주황색", example: "La naranja es naranja."}
        ]
    }
};
