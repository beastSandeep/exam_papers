# scripts/add_textbook_questions_all_classes.py
# Ingests authentic NCERT textbook exercise questions for Classes 5 Maths, 6 Maths, 7 Maths, 6 Science, and 7 Science.
import os, sys, json

sys.stdout.reconfigure(encoding='utf-8')

QUESTIONS_PATH = os.path.join("data", "questions.json")

# ==========================================
# 1. CLASS 6 SCIENCE TEXTBOOK QUESTIONS
# ==========================================
TB_6_SCIENCE = [
    # Ch 6: Sorting Materials
    {
        "id": "6sci_tb_ch6_mcq1",
        "subjectId": "6_science",
        "sectionKey": "sec_1",
        "set": "Textbook",
        "orderInSet": 1,
        "originalNum": "TB Q1",
        "marks": 1,
        "hasOrChoice": False,
        "preview": "Which of the following materials is completely transparent?",
        "content": "**Which of the following materials is completely transparent?**  \n**निम्नलिखित में से कौन-सा पदार्थ पूर्णतः पारदर्शी है?**  \n(a) Clear glass / स्वच्छ काँच  \n(b) Wood / लकड़ी  \n(c) Butter paper / बटर पेपर  \n(d) Cardboard / गत्ता",
        "chapter": "Ch 6: Sorting Materials (पदार्थों का समूहन)"
    },
    {
        "id": "6sci_tb_ch6_mcq2",
        "subjectId": "6_science",
        "sectionKey": "sec_1",
        "set": "Textbook",
        "orderInSet": 2,
        "originalNum": "TB Q2",
        "marks": 1,
        "hasOrChoice": False,
        "preview": "Which of the following liquids is completely soluble in water?",
        "content": "**Which of the following liquids is completely soluble (miscible) in water?**  \n**निम्नलिखित में से कौन-सा द्रव जल में पूर्णतः विलेय है?**  \n(a) Vinegar / सिरका  \n(b) Kerosene / मिट्टी का तेल  \n(c) Mustard oil / सरसों का तेल  \n(d) Coconut oil / नारियल का तेल",
        "chapter": "Ch 6: Sorting Materials (पदार्थों का समूहन)"
    },
    {
        "id": "6sci_tb_ch6_fib1",
        "subjectId": "6_science",
        "sectionKey": "sec_2",
        "set": "Textbook",
        "orderInSet": 3,
        "originalNum": "TB Q3",
        "marks": 1,
        "hasOrChoice": False,
        "preview": "Materials through which things cannot be seen are called _______.",
        "content": "**Materials through which things cannot be seen are called _______ objects.**  \n**वे पदार्थ जिनके आर-पार वस्तुओं को नहीं देखा जा सकता, _______ कहलाते हैं।**",
        "chapter": "Ch 6: Sorting Materials (पदार्थों का समूहन)"
    },
    {
        "id": "6sci_tb_ch6_tf1",
        "subjectId": "6_science",
        "sectionKey": "sec_3",
        "set": "Textbook",
        "orderInSet": 4,
        "originalNum": "TB Q4",
        "marks": 1,
        "hasOrChoice": False,
        "preview": "Chalk dissolves completely in water.",
        "content": "**State True (T) or False (F): Chalk dissolves completely in water.**  \n**सत्य (T) अथवा असत्य (F) बताइए: चॉक जल में पूर्णतः विलीन हो जाता है।**",
        "chapter": "Ch 6: Sorting Materials (पदार्थों का समूहन)"
    },
    {
        "id": "6sci_tb_ch6_vsa1",
        "subjectId": "6_science",
        "sectionKey": "sec_4",
        "set": "Textbook",
        "orderInSet": 5,
        "originalNum": "TB Q5",
        "marks": 2,
        "hasOrChoice": False,
        "preview": "Name two objects each made from (a) Wood and (b) Leather.",
        "content": "**Name two objects each made from the following materials:**  \n**निम्नलिखित पदार्थों से बनी दो-दो वस्तुओं के नाम लिखिए:**  \n(a) Wood / लकड़ी  \n(b) Leather / चमड़ा",
        "chapter": "Ch 6: Sorting Materials (पदार्थों का समूहन)"
    },
    {
        "id": "6sci_tb_ch6_sa1",
        "subjectId": "6_science",
        "sectionKey": "sec_5",
        "set": "Textbook",
        "orderInSet": 6,
        "originalNum": "TB Q6",
        "marks": 3,
        "hasOrChoice": False,
        "preview": "Why is a tumbler not made with a piece of cloth? Explain.",
        "content": "**Why is a tumbler not made with a piece of cloth? Explain with reasons.**  \n**कपड़े के टुकड़े से गिलास क्यों नहीं बनाया जाता? कारण सहित व्याख्या कीजिए।**",
        "chapter": "Ch 6: Sorting Materials (पदार्थों का समूहन)"
    },
    {
        "id": "6sci_tb_ch6_la1",
        "subjectId": "6_science",
        "sectionKey": "sec_6",
        "set": "Textbook",
        "orderInSet": 7,
        "originalNum": "TB Q7",
        "marks": 5,
        "hasOrChoice": False,
        "preview": "Differentiate between transparent, translucent and opaque materials with two examples of each.",
        "content": "**Differentiate between transparent, translucent and opaque materials. Give two examples of each.**  \n**पारदर्शी, पारभासी एवं अपारदर्शी पदार्थों में अंतर स्पष्ट कीजिए। प्रत्येक के दो-दो उदाहरण दीजिए।**",
        "chapter": "Ch 6: Sorting Materials (पदार्थों का समूहन)"
    },

    # Ch 7: Temperature and Heat
    {
        "id": "6sci_tb_ch7_mcq1",
        "subjectId": "6_science",
        "sectionKey": "sec_1",
        "set": "Textbook",
        "orderInSet": 8,
        "originalNum": "TB Q8",
        "marks": 1,
        "hasOrChoice": False,
        "preview": "The normal temperature of a healthy human body is:",
        "content": "**The normal temperature of a healthy human body is:**  \n**स्वस्थ मानव शरीर का सामान्य तापमान होता है:**  \n(a) $35^\\circ\\text{C}$  \n(b) $37^\\circ\\text{C}$  \n(c) $40^\\circ\\text{C}$  \n(d) $42^\\circ\\text{C}$",
        "chapter": "Ch 7: Temperature and Heat (तापमान एवं ऊष्मा)"
    },
    {
        "id": "6sci_tb_ch7_fib1",
        "subjectId": "6_science",
        "sectionKey": "sec_2",
        "set": "Textbook",
        "orderInSet": 9,
        "originalNum": "TB Q9",
        "marks": 1,
        "hasOrChoice": False,
        "preview": "A reliable measure of the hotness of an object is its _______.",
        "content": "**A reliable measure of the hotness of an object is its _______.**  \n**किसी वस्तु की उष्णता (गर्मी) की विश्वसनीय माप उसका _______ है।**",
        "chapter": "Ch 7: Temperature and Heat (तापमान एवं ऊष्मा)"
    },
    {
        "id": "6sci_tb_ch7_tf1",
        "subjectId": "6_science",
        "sectionKey": "sec_3",
        "set": "Textbook",
        "orderInSet": 10,
        "originalNum": "TB Q10",
        "marks": 1,
        "hasOrChoice": False,
        "preview": "Temperature of boiling water can be measured by a clinical thermometer.",
        "content": "**State True (T) or False (F): Temperature of boiling water can be measured by a clinical thermometer.**  \n**सत्य (T) अथवा असत्य (F) बताइए: उबलते हुए पानी का तापमान डॉक्टरी थर्मामीटर से मापा जा सकता है।**",
        "chapter": "Ch 7: Temperature and Heat (तापमान एवं ऊष्मा)"
    },
    {
        "id": "6sci_tb_ch7_vsa1",
        "subjectId": "6_science",
        "sectionKey": "sec_4",
        "set": "Textbook",
        "orderInSet": 11,
        "originalNum": "TB Q11",
        "marks": 2,
        "hasOrChoice": False,
        "preview": "State the measuring range of a Clinical Thermometer and a Laboratory Thermometer.",
        "content": "**State the temperature measurement range of:**  \n**निम्नलिखित थर्मामीटरों का तापमान मापन परिसर बताइए:**  \n(a) Clinical Thermometer / डॉक्टरी थर्मामीटर  \n(b) Laboratory Thermometer / प्रयोगशाला थर्मामीटर",
        "chapter": "Ch 7: Temperature and Heat (तापमान एवं ऊष्मा)"
    },
    {
        "id": "6sci_tb_ch7_sa1",
        "subjectId": "6_science",
        "sectionKey": "sec_5",
        "set": "Textbook",
        "orderInSet": 12,
        "originalNum": "TB Q12",
        "marks": 3,
        "hasOrChoice": False,
        "preview": "Why is mercury used in thermometers? Give three reasons.",
        "content": "**Why is mercury widely used in liquid-in-glass thermometers? State three reasons.**  \n**थर्मामीटर में पारे (मरकरी) का उपयोग क्यों किया जाता है? कोई तीन कारण लिखिए।**",
        "chapter": "Ch 7: Temperature and Heat (तापमान एवं ऊष्मा)"
    },
    {
        "id": "6sci_tb_ch7_la1",
        "subjectId": "6_science",
        "sectionKey": "sec_6",
        "set": "Textbook",
        "orderInSet": 13,
        "originalNum": "TB Q13",
        "marks": 5,
        "hasOrChoice": False,
        "preview": "Give two similarities and three differences between laboratory and clinical thermometers.",
        "content": "**State two similarities and three differences between a laboratory thermometer and a clinical thermometer.**  \n**प्रयोगशाला थर्मामीटर तथा डॉक्टरी थर्मामीटर के बीच दो समानताएँ एवं तीन अंतर लिखिए।**",
        "chapter": "Ch 7: Temperature and Heat (तापमान एवं ऊष्मा)"
    },

    # Ch 8: Water in the Atmosphere
    {
        "id": "6sci_tb_ch8_mcq1",
        "subjectId": "6_science",
        "sectionKey": "sec_1",
        "set": "Textbook",
        "orderInSet": 14,
        "originalNum": "TB Q14",
        "marks": 1,
        "hasOrChoice": False,
        "preview": "The process of conversion of water vapour into water droplets is called:",
        "content": "**The process of conversion of water vapour into its liquid state is called:**  \n**जलवाष्प के द्रव (जल) में परिवर्तित होने के प्रक्रम को कहते हैं:**  \n(a) Evaporation / वाष्पीकरण  \n(b) Condensation / संघनन  \n(c) Transpiration / वाष्पोत्सर्जन  \n(d) Precipitation / वर्षण",
        "chapter": "Ch 8: Water in the Atmosphere (जल एवं जलवाष्प)"
    },
    {
        "id": "6sci_tb_ch8_fib1",
        "subjectId": "6_science",
        "sectionKey": "sec_2",
        "set": "Textbook",
        "orderInSet": 15,
        "originalNum": "TB Q15",
        "marks": 1,
        "hasOrChoice": False,
        "preview": "The circulation of water between ocean and land is known as the _______.",
        "content": "**The continuous circulation of water between ocean, atmosphere and land is known as the _______ cycle.**  \n**महासागर और भूमि के बीच जल के निरंतर परिसंचरण को _______ चक्र कहते हैं।**",
        "chapter": "Ch 8: Water in the Atmosphere (जल एवं जलवाष्प)"
    },
    {
        "id": "6sci_tb_ch8_tf1",
        "subjectId": "6_science",
        "sectionKey": "sec_3",
        "set": "Textbook",
        "orderInSet": 16,
        "originalNum": "TB Q16",
        "marks": 1,
        "hasOrChoice": False,
        "preview": "Water evaporates only in sunlight.",
        "content": "**State True (T) or False (F): Water evaporates only in the presence of direct sunlight.**  \n**सत्य (T) अथवा असत्य (F) बताइए: जल केवल सूर्य के सीधे प्रकाश में ही वाष्पित होता है।**",
        "chapter": "Ch 8: Water in the Atmosphere (जल एवं जलवाष्प)"
    },
    {
        "id": "6sci_tb_ch8_vsa1",
        "subjectId": "6_science",
        "sectionKey": "sec_4",
        "set": "Textbook",
        "orderInSet": 17,
        "originalNum": "TB Q17",
        "marks": 2,
        "hasOrChoice": False,
        "preview": "Why do droplets of water appear on the outer surface of a glass containing ice-cold water?",
        "content": "**Why do tiny droplets of water appear on the outer surface of a glass containing ice-cold water?**  \n**बर्फ के ठंडे पानी से भरे गिलास की बाहरी सतह पर जल की छोटी-छोटी बूँदें क्यों दिखाई देती हैं?**",
        "chapter": "Ch 8: Water in the Atmosphere (जल एवं जलवाष्प)"
    },
    {
        "id": "6sci_tb_ch8_sa1",
        "subjectId": "6_science",
        "sectionKey": "sec_5",
        "set": "Textbook",
        "orderInSet": 18,
        "originalNum": "TB Q18",
        "marks": 3,
        "hasOrChoice": False,
        "preview": "What is rainwater harvesting? Mention two basic techniques for it.",
        "content": "**What is rainwater harvesting? Mention two basic techniques used to harvest rainwater.**  \n**वर्षा जल संचयन क्या है? इसके लिए उपयोग की जाने वाली दो प्रमुख तकनीकों का उल्लेख कीजिए।**",
        "chapter": "Ch 8: Water in the Atmosphere (जल एवं जलवाष्प)"
    },
    {
        "id": "6sci_tb_ch8_la1",
        "subjectId": "6_science",
        "sectionKey": "sec_6",
        "set": "Textbook",
        "orderInSet": 19,
        "originalNum": "TB Q19",
        "marks": 5,
        "hasOrChoice": False,
        "preview": "Explain the water cycle with the roles of evaporation, transpiration, and condensation.",
        "content": "**Explain the complete water cycle in nature. Clearly describe the roles of evaporation, transpiration, and condensation.**  \n**प्रकृति में जल चक्र को विस्तार से समझाइए। वाष्पीकरण, वाष्पोत्सर्जन एवं संघनन की भूमिका का स्पष्ट वर्णन कीजिए।**",
        "chapter": "Ch 8: Water in the Atmosphere (जल एवं जलवाष्प)"
    },

    # Ch 9: Separation of Substances
    {
        "id": "6sci_tb_ch9_mcq1",
        "subjectId": "6_science",
        "sectionKey": "sec_1",
        "set": "Textbook",
        "orderInSet": 20,
        "originalNum": "TB Q20",
        "marks": 1,
        "hasOrChoice": False,
        "preview": "Method used to separate heavier seeds from lighter husk by wind is:",
        "content": "**The method used to separate heavier grains from lighter husk with the help of blowing wind is:**  \n**हवा के झोंकों द्वारा भारी अनाज के दानों को हल्के भूसे से अलग करने की विधि कहलाती है:**  \n(a) Threshing / थ्रेशिंग  \n(b) Winnowing / निष्पावन (फटकना)  \n(c) Sieving / चालना  \n(d) Filtration / निस्यंदन",
        "chapter": "Ch 9: Separation of Substances (पदार्थों का पृथक्करण)"
    },
    {
        "id": "6sci_tb_ch9_fib1",
        "subjectId": "6_science",
        "sectionKey": "sec_2",
        "set": "Textbook",
        "orderInSet": 21,
        "originalNum": "TB Q21",
        "marks": 1,
        "hasOrChoice": False,
        "preview": "The method of separating seeds of paddy from its stalks is called _______.",
        "content": "**The method of separating grains or seeds from their stalks is called _______.**  \n**सूखे पौधों की डंडियों से अन्नकणों (अनाज) को अलग करने की विधि _______ कहलाती है।**",
        "chapter": "Ch 9: Separation of Substances (पदार्थों का पृथक्करण)"
    },
    {
        "id": "6sci_tb_ch9_tf1",
        "subjectId": "6_science",
        "sectionKey": "sec_3",
        "set": "Textbook",
        "orderInSet": 22,
        "originalNum": "TB Q22",
        "marks": 1,
        "hasOrChoice": False,
        "preview": "A mixture of milk and water can be separated by filtration.",
        "content": "**State True (T) or False (F): A mixture of milk and water can be separated by filtration.**  \n**सत्य (T) अथवा असत्य (F) बताइए: दूध और जल के मिश्रण को निस्यंदन (छानकर) अलग किया जा सकता है।**",
        "chapter": "Ch 9: Separation of Substances (पदार्थों का पृथक्करण)"
    },
    {
        "id": "6sci_tb_ch9_vsa1",
        "subjectId": "6_science",
        "sectionKey": "sec_4",
        "set": "Textbook",
        "orderInSet": 23,
        "originalNum": "TB Q23",
        "marks": 2,
        "hasOrChoice": False,
        "preview": "Define sedimentation and decantation with a daily life example.",
        "content": "**Define sedimentation and decantation with an example of muddy water.**  \n**अवसादन (Sedimentation) तथा निस्तारण (Decantation) को गंदले जल के उदाहरण द्वारा परिभाषित कीजिए।**",
        "chapter": "Ch 9: Separation of Substances (पदार्थों का पृथक्करण)"
    },
    {
        "id": "6sci_tb_ch9_sa1",
        "subjectId": "6_science",
        "sectionKey": "sec_5",
        "set": "Textbook",
        "orderInSet": 24,
        "originalNum": "TB Q24",
        "marks": 3,
        "hasOrChoice": False,
        "preview": "How will you separate sand and water from their mixture using filtration?",
        "content": "**How will you separate sand and water from their mixture? Describe the steps using a filter paper.**  \n**आप रेत और जल के मिश्रण को कैसे अलग करेंगे? फिल्टर पेपर का उपयोग करके चरणों का वर्णन कीजिए।**",
        "chapter": "Ch 9: Separation of Substances (पदार्थों का पृथक्करण)"
    },
    {
        "id": "6sci_tb_ch9_la1",
        "subjectId": "6_science",
        "sectionKey": "sec_6",
        "set": "Textbook",
        "orderInSet": 25,
        "originalNum": "TB Q25",
        "marks": 5,
        "hasOrChoice": False,
        "preview": "How can you separate a mixture of salt, sand, and water? Explain sequence of steps.",
        "content": "**How can you separate a mixture containing salt, sand, and water? Explain the complete sequence of separation processes involved.**  \n**नमक, रेत और जल के मिश्रण को आप किस प्रकार पृथक करेंगे? इसमें प्रयुक्त सभी विधियों के क्रमबद्ध चरणों की व्याख्या कीजिए।**",
        "chapter": "Ch 9: Separation of Substances (पदार्थों का पृथक्करण)"
    }
]

# ==========================================
# 2. CLASS 7 SCIENCE TEXTBOOK QUESTIONS
# ==========================================
TB_7_SCIENCE = [
    # Ch 6: Reaching the Age of Adolescence
    {
        "id": "7sci_tb_ch6_mcq1",
        "subjectId": "7_science",
        "sectionKey": "sec_1",
        "set": "Textbook",
        "orderInSet": 1,
        "originalNum": "TB Q1",
        "marks": 1,
        "hasOrChoice": False,
        "preview": "Adolescents should be careful about what they eat because:",
        "content": "**Adolescents should be careful about what they eat because:**  \n**किशोरों को अपने भोजन के प्रति सतर्क रहना चाहिए क्योंकि:**  \n(a) Proper diet develops their brains rapidly / उचित आहार मस्तिष्क को तेजी से विकसित करता है  \n(b) Proper diet is needed for rapid body growth / शरीर में तीव्र वृद्धि के लिए उचित पोषण आवश्यक है  \n(c) Adolescents feel hungry all the time / किशोरों को हर समय भूख लगती है  \n(d) Taste buds are well developed in teenagers / किशोरों में स्वाद ग्रंथियां अधिक सक्रिय होती हैं",
        "chapter": "Ch 6: Reaching the Age of Adolescence (किशोरावस्था)"
    },
    {
        "id": "7sci_tb_ch6_fib1",
        "subjectId": "7_science",
        "sectionKey": "sec_2",
        "set": "Textbook",
        "orderInSet": 2,
        "originalNum": "TB Q2",
        "marks": 1,
        "hasOrChoice": False,
        "preview": "The hormone responsible for voice change in boys during puberty is _______.",
        "content": "**The male sex hormone released by testes during puberty is _______.**  \n**यौवनारंभ के समय वृषण द्वारा स्रावित होने वाला नर लिंग हार्मोन _______ है।**",
        "chapter": "Ch 6: Reaching the Age of Adolescence (किशोरावस्था)"
    },
    {
        "id": "7sci_tb_ch6_tf1",
        "subjectId": "7_science",
        "sectionKey": "sec_3",
        "set": "Textbook",
        "orderInSet": 3,
        "originalNum": "TB Q3",
        "marks": 1,
        "hasOrChoice": False,
        "preview": "The legal age for marriage in India is 18 years for girls and 21 years for boys.",
        "content": "**State True (T) or False (F): In India, the legal age for marriage is 18 years for girls and 21 years for boys.**  \n**सत्य (T) अथवा असत्य (F) बताइए: भारत में विवाह की कानूनी आयु लड़कियों के लिए 18 वर्ष तथा लड़कों के लिए 21 वर्ष है।**",
        "chapter": "Ch 6: Reaching the Age of Adolescence (किशोरावस्था)"
    },
    {
        "id": "7sci_tb_ch6_vsa1",
        "subjectId": "7_science",
        "sectionKey": "sec_4",
        "set": "Textbook",
        "orderInSet": 4,
        "originalNum": "TB Q4",
        "marks": 2,
        "hasOrChoice": False,
        "preview": "What is Adam's apple? In whom is it prominent?",
        "content": "**What is Adam's apple? In which sex does it become prominent during puberty?**  \n**एडम्स एप्पल (कंठमणि) क्या है? यौवनारंभ में यह किसमें स्पष्ट रूप से दिखाई देता है?**",
        "chapter": "Ch 6: Reaching the Age of Adolescence (किशोरावस्था)"
    },
    {
        "id": "7sci_tb_ch6_sa1",
        "subjectId": "7_science",
        "sectionKey": "sec_5",
        "set": "Textbook",
        "orderInSet": 5,
        "originalNum": "TB Q5",
        "marks": 3,
        "hasOrChoice": False,
        "preview": "What are secondary sexual characteristics? List two in boys and two in girls.",
        "content": "**What are secondary sexual characteristics? State two such features in boys and two in girls.**  \n**गौण लैंगिक लक्षण क्या हैं? लड़कों में दो तथा लड़कियों में दो गौण लैंगिक लक्षण लिखिए।**",
        "chapter": "Ch 6: Reaching the Age of Adolescence (किशोरावस्था)"
    },
    {
        "id": "7sci_tb_ch6_la1",
        "subjectId": "7_science",
        "sectionKey": "sec_6",
        "set": "Textbook",
        "orderInSet": 6,
        "originalNum": "TB Q6",
        "marks": 5,
        "hasOrChoice": False,
        "preview": "Write notes on: (a) Pituitary gland (b) Thyroid gland (c) Pancreas and (d) Adrenal glands.",
        "content": "**Write short explanatory notes on the functions and hormones of:**  \n**निम्नलिखित अंतःस्रावी ग्रंथियों के हार्मोन एवं कार्यों पर संक्षिप्त टिप्पणी लिखिए:**  \n(a) Pituitary Gland / पीयूष ग्रंथि  \n(b) Thyroid Gland / थायरॉइड ग्रंथि  \n(c) Pancreas / अग्न्याशय  \n(d) Adrenal Glands / अधिवृक्क (एड्रीनल) ग्रंथि",
        "chapter": "Ch 6: Reaching the Age of Adolescence (किशोरावस्था)"
    },

    # Ch 7: Heat & Transfer of Heat
    {
        "id": "7sci_tb_ch7_mcq1",
        "subjectId": "7_science",
        "sectionKey": "sec_1",
        "set": "Textbook",
        "orderInSet": 7,
        "originalNum": "TB Q7",
        "marks": 1,
        "hasOrChoice": False,
        "preview": "Heat from the Sun reaches the Earth through the mode of:",
        "content": "**Heat from the Sun reaches the Earth mainly through the mode of:**  \n**सूर्य की ऊष्मा पृथ्वी तक मुख्य रूप से किस विधि द्वारा पहुँचती है?**  \n(a) Conduction / चालन  \n(b) Convection / संवहन  \n(c) Radiation / विकिरण  \n(d) Absorption / अवशोषण",
        "chapter": "Ch 7: Heat & Transfer of Heat (ऊष्मा एवं स्थानांतरण)"
    },
    {
        "id": "7sci_tb_ch7_fib1",
        "subjectId": "7_science",
        "sectionKey": "sec_2",
        "set": "Textbook",
        "orderInSet": 8,
        "originalNum": "TB Q8",
        "marks": 1,
        "hasOrChoice": False,
        "preview": "No medium is required for transfer of heat by the process of _______.",
        "content": "**No material medium is required for the transfer of heat by the process of _______.**  \n**_______ प्रक्रम द्वारा ऊष्मा के स्थानांतरण के लिए किसी माध्यम की आवश्यकता नहीं होती।**",
        "chapter": "Ch 7: Heat & Transfer of Heat (ऊष्मा एवं स्थानांतरण)"
    },
    {
        "id": "7sci_tb_ch7_tf1",
        "subjectId": "7_science",
        "sectionKey": "sec_3",
        "set": "Textbook",
        "orderInSet": 9,
        "originalNum": "TB Q9",
        "marks": 1,
        "hasOrChoice": False,
        "preview": "A cold steel spoon dipped in a cup of hot milk transfers heat by convection.",
        "content": "**State True (T) or False (F): A cold steel spoon dipped in a cup of hot milk transfers heat to its other end by convection.**  \n**सत्य (T) अथवा असत्य (F) बताइए: गर्म दूध में डूबा हुआ ठंडा स्टील का चम्मच संवहन द्वारा अपने दूसरे सिरे तक ऊष्मा स्थानांतरित करता है।**",
        "chapter": "Ch 7: Heat & Transfer of Heat (ऊष्मा एवं स्थानांतरण)"
    },
    {
        "id": "7sci_tb_ch7_vsa1",
        "subjectId": "7_science",
        "sectionKey": "sec_4",
        "set": "Textbook",
        "orderInSet": 10,
        "originalNum": "TB Q10",
        "marks": 2,
        "hasOrChoice": False,
        "preview": "Give two examples each of conductors and insulators of heat.",
        "content": "**Give two examples each of:**  \n**निम्नलिखित के दो-दो उदाहरण दीजिए:**  \n(a) Conductors of heat / ऊष्मा के चालक  \n(b) Insulators of heat / ऊष्मा के रोधी (कुचालक)",
        "chapter": "Ch 7: Heat & Transfer of Heat (ऊष्मा एवं स्थानांतरण)"
    },
    {
        "id": "7sci_tb_ch7_sa1",
        "subjectId": "7_science",
        "sectionKey": "sec_5",
        "set": "Textbook",
        "orderInSet": 11,
        "originalNum": "TB Q11",
        "marks": 3,
        "hasOrChoice": False,
        "preview": "Explain why sea breeze blows during daytime in coastal areas.",
        "content": "**Explain how sea breeze occurs during daytime in coastal areas.**  \n**तटीय क्षेत्रों में दिन के समय समुद्र समीर (Sea breeze) क्यों और कैसे चलती है? व्याख्या कीजिए।**",
        "chapter": "Ch 7: Heat & Transfer of Heat (ऊष्मा एवं स्थानांतरण)"
    },
    {
        "id": "7sci_tb_ch7_la1",
        "subjectId": "7_science",
        "sectionKey": "sec_6",
        "set": "Textbook",
        "orderInSet": 12,
        "originalNum": "TB Q12",
        "marks": 5,
        "hasOrChoice": False,
        "preview": "Explain the three modes of heat transfer: Conduction, Convection, and Radiation with suitable examples.",
        "content": "**Describe the three modes of heat transfer: Conduction, Convection, and Radiation with one daily life example for each.**  \n**ऊष्मा स्थानांतरण की तीनों विधियों: चालन, संवहन एवं विकिरण का सचित्र/सोदाहरण विस्तृत वर्णन कीजिए।**",
        "chapter": "Ch 7: Heat & Transfer of Heat (ऊष्मा एवं स्थानांतरण)"
    },

    # Ch 8: Motion and Time
    {
        "id": "7sci_tb_ch8_mcq1",
        "subjectId": "7_science",
        "sectionKey": "sec_1",
        "set": "Textbook",
        "orderInSet": 13,
        "originalNum": "TB Q13",
        "marks": 1,
        "hasOrChoice": False,
        "preview": "The basic unit of speed is:",
        "content": "**The basic SI unit of speed is:**  \n**चाल का मूल मात्रक है:**  \n(a) $\\text{km/min}$  \n(b) $\\text{m/min}$  \n(c) $\\text{km/h}$  \n(d) $\\text{m/s}$",
        "chapter": "Ch 8: Motion and Time (गति एवं समय)"
    },
    {
        "id": "7sci_tb_ch8_fib1",
        "subjectId": "7_science",
        "sectionKey": "sec_2",
        "set": "Textbook",
        "orderInSet": 14,
        "originalNum": "TB Q14",
        "marks": 1,
        "hasOrChoice": False,
        "preview": "Distance covered by an object in a unit time is called its _______.",
        "content": "**The distance covered by an object in a unit time is called its _______.**  \n**किसी वस्तु द्वारा एकांक समय में तय की गई दूरी को उसकी _______ कहते हैं।**",
        "chapter": "Ch 8: Motion and Time (गति एवं समय)"
    },
    {
        "id": "7sci_tb_ch8_tf1",
        "subjectId": "7_science",
        "sectionKey": "sec_3",
        "set": "Textbook",
        "orderInSet": 15,
        "originalNum": "TB Q15",
        "marks": 1,
        "hasOrChoice": False,
        "preview": "The motion of a simple pendulum is periodic and oscillatory.",
        "content": "**State True (T) or False (F): The motion of a simple pendulum is an example of periodic and oscillatory motion.**  \n**सत्य (T) अथवा असत्य (F) बताइए: सरल लोलक की गति आवर्ती एवं दोलन गति का उदाहरण है।**",
        "chapter": "Ch 8: Motion and Time (गति एवं समय)"
    },
    {
        "id": "7sci_tb_ch8_vsa1",
        "subjectId": "7_science",
        "sectionKey": "sec_4",
        "set": "Textbook",
        "orderInSet": 16,
        "originalNum": "TB Q16",
        "marks": 2,
        "hasOrChoice": False,
        "preview": "A car covers 120 km in 2 hours. Calculate its speed in km/h and m/s.",
        "content": "**A car covers a distance of $120\\text{ km}$ in $2\\text{ hours}$. Calculate its speed in $\\text{km/h}$ and $\\text{m/s}$.**  \n**एक कार $2$ घंटे में $120\\text{ किमी}$ की दूरी तय करती है। इसकी चाल $\\text{किमी/घंटा}$ तथा $\\text{मी/से}$ में ज्ञात कीजिए।**",
        "chapter": "Ch 8: Motion and Time (गति एवं समय)"
    },
    {
        "id": "7sci_tb_ch8_sa1",
        "subjectId": "7_science",
        "sectionKey": "sec_5",
        "set": "Textbook",
        "orderInSet": 17,
        "originalNum": "TB Q17",
        "marks": 3,
        "hasOrChoice": False,
        "preview": "Define Time Period of a simple pendulum. A pendulum completes 20 oscillations in 32 seconds, find its time period.",
        "content": "**What is the Time Period of a simple pendulum? A simple pendulum takes $32\\text{ seconds}$ to complete $20$ oscillations. What is its time period?**  \n**सरल लोलक का आवर्तकाल क्या है? एक सरल लोलक $20$ दोलन पूरे करने में $32\\text{ सेकंड}$ लेता है। इसका आवर्तकाल ज्ञात कीजिए।**",
        "chapter": "Ch 8: Motion and Time (गति एवं समय)"
    },
    {
        "id": "7sci_tb_ch8_la1",
        "subjectId": "7_science",
        "sectionKey": "sec_6",
        "set": "Textbook",
        "orderInSet": 18,
        "originalNum": "TB Q18",
        "marks": 5,
        "hasOrChoice": False,
        "preview": "Explain distance-time graph for: (a) Uniform speed (b) Stationary object and (c) Non-uniform speed.",
        "content": "**Draw and explain the nature of Distance-Time graphs for:**  \n**निम्नलिखित स्थितियों के लिए दूरी-समय ग्राफ का स्वरूप बनाकर व्याख्या कीजिए:**  \n(a) An object moving with a constant speed / एकसमान चाल से गतिशील वस्तु  \n(b) A stationary object parked on a road side / सड़क किनारे खड़ी विराम अवस्था में वस्तु  \n(c) An object moving with non-uniform speed / असमान चाल से गतिशील वस्तु",
        "chapter": "Ch 8: Motion and Time (गति एवं समय)"
    },

    # Ch 9: Nutrition & Respiration in Organisms
    {
        "id": "7sci_tb_ch9_mcq1",
        "subjectId": "7_science",
        "sectionKey": "sec_1",
        "set": "Textbook",
        "orderInSet": 19,
        "originalNum": "TB Q19",
        "marks": 1,
        "hasOrChoice": False,
        "preview": "In cockroaches, air enters the body through:",
        "content": "**In cockroaches and other insects, atmospheric air enters the body through:**  \n**तिलचट्टे (कॉकरोच) के शरीर में वायु किसके माध्यम से प्रवेश करती है?**  \n(a) Lungs / फेफड़े  \n(b) Gills / क्लोम  \n(c) Spiracles / श्वास रंध्र  \n(d) Skin / त्वचा",
        "chapter": "Ch 9: Nutrition & Respiration in Organisms (पोषण एवं श्वसन)"
    },
    {
        "id": "7sci_tb_ch9_fib1",
        "subjectId": "7_science",
        "sectionKey": "sec_2",
        "set": "Textbook",
        "orderInSet": 20,
        "originalNum": "TB Q20",
        "marks": 1,
        "hasOrChoice": False,
        "preview": "During cellular respiration, glucose is broken down into _______ and _______ with the release of energy.",
        "content": "**During aerobic respiration, glucose is broken down into _______ and _______ along with the release of energy.**  \n**वायवीय श्वसन के दौरान, ग्लूकोज ऊर्जा की विमुक्ति के साथ _______ तथा _______ में विखंडित होता है।**",
        "chapter": "Ch 9: Nutrition & Respiration in Organisms (पोषण एवं श्वसन)"
    },
    {
        "id": "7sci_tb_ch9_tf1",
        "subjectId": "7_science",
        "sectionKey": "sec_3",
        "set": "Textbook",
        "orderInSet": 21,
        "originalNum": "TB Q21",
        "marks": 1,
        "hasOrChoice": False,
        "preview": "Plants perform photosynthesis during daytime and respiration only during night.",
        "content": "**State True (T) or False (F): Cellular respiration in plant cells occurs only during the night.**  \n**सत्य (T) अथवा असत्य (F) बताइए: पादप कोशिकाओं में कोशिकीय श्वसन केवल रात के समय ही होता है।**",
        "chapter": "Ch 9: Nutrition & Respiration in Organisms (पोषण एवं श्वसन)"
    },
    {
        "id": "7sci_tb_ch9_vsa1",
        "subjectId": "7_science",
        "sectionKey": "sec_4",
        "set": "Textbook",
        "orderInSet": 22,
        "originalNum": "TB Q22",
        "marks": 2,
        "hasOrChoice": False,
        "preview": "Why do athletes breathe faster and deeper after finishing a race?",
        "content": "**Why does an athlete breathe faster and deeper than usual after finishing a race?**  \n**दौड़ समाप्त करने के बाद कोई धावक सामान्य से अधिक तेजी और गहराई से साँस क्यों लेता है?**",
        "chapter": "Ch 9: Nutrition & Respiration in Organisms (पोषण एवं श्वसन)"
    },
    {
        "id": "7sci_tb_ch9_sa1",
        "subjectId": "7_science",
        "sectionKey": "sec_5",
        "set": "Textbook",
        "orderInSet": 23,
        "originalNum": "TB Q23",
        "marks": 3,
        "hasOrChoice": False,
        "preview": "Differentiate between aerobic and anaerobic respiration with chemical word equations.",
        "content": "**Differentiate between Aerobic Respiration and Anaerobic Respiration. Give the word equations for both.**  \n**वायवीय एवं अवायवीय श्वसन में अंतर स्पष्ट कीजिए। दोनों के लिए शब्द समीकरण लिखिए।**",
        "chapter": "Ch 9: Nutrition & Respiration in Organisms (पोषण एवं श्वसन)"
    },
    {
        "id": "7sci_tb_ch9_la1",
        "subjectId": "7_science",
        "sectionKey": "sec_6",
        "set": "Textbook",
        "orderInSet": 24,
        "originalNum": "TB Q24",
        "marks": 5,
        "hasOrChoice": False,
        "preview": "Describe human respiratory system: inhalation, exhalation and the role of diaphragm.",
        "content": "**Describe the mechanism of breathing in human beings. Explain how the diaphragm and rib cage move during inhalation and exhalation.**  \n**मानव में श्वसन क्रियाविधि का वर्णन कीजिए। अंतःश्वसन और उच्छ्वसन के दौरान डायाफ्राम तथा पसलियों की गति को स्पष्ट कीजिए।**",
        "chapter": "Ch 9: Nutrition & Respiration in Organisms (पोषण एवं श्वसन)"
    }
]

# ==========================================
# 3. CLASS 5 MATHS TEXTBOOK QUESTIONS
# ==========================================
TB_5_MATHS = [
    # Ch 5: Does it Look the Same?
    {
        "id": "5m_tb_ch5_1",
        "subjectId": "5_maths",
        "sectionKey": "sec_a",
        "set": "Textbook",
        "orderInSet": 1,
        "originalNum": "TB Q1",
        "marks": 1,
        "hasOrChoice": False,
        "preview": "Which English letters look the same after half a turn (1/2 turn)?",
        "content": "**Which of the following English capital letters look exactly the same after half a turn ($\\frac{1}{2}$ turn)?**  \n**निम्नलिखित अंग्रेजी के बड़े अक्षरों में से कौन-से आधा घुमाने ($\\frac{1}{2}$ घूर्णन) पर भी बिल्कुल वैसे ही दिखाई देते हैं?**  \n$$\\mathbf{H}, \\quad \\mathbf{I}, \\quad \\mathbf{N}, \\quad \\mathbf{S}, \\quad \\mathbf{X}, \\quad \\mathbf{Z}$$"
    },
    {
        "id": "5m_tb_ch5_2",
        "subjectId": "5_maths",
        "sectionKey": "sec_b",
        "set": "Textbook",
        "orderInSet": 2,
        "originalNum": "TB Q2",
        "marks": 1,
        "hasOrChoice": False,
        "preview": "MCQ: Shape that looks the same after 1/4 turn",
        "content": "**Which shape looks exactly the same after a quarter turn ($\\frac{1}{4}$ turn)?**  \n**कौन-सी आकृति एक-चौथाई घुमाने ($\\frac{1}{4}$ घूर्णन) के बाद भी बिल्कुल वैसी ही दिखाई देती है?**  \n(a) Square / वर्ग  \n(b) Rectangle / आयत  \n(c) Scalene triangle / विषमबाहु त्रिभुज  \n(d) Trapezium / समलंब चतुर्भुज"
    },
    {
        "id": "5m_tb_ch5_3",
        "subjectId": "5_maths",
        "sectionKey": "sec_c",
        "set": "Textbook",
        "orderInSet": 3,
        "originalNum": "TB Q3",
        "marks": 2,
        "hasOrChoice": False,
        "preview": "Draw how the digits 0, 1, and 8 look after a half turn.",
        "content": "**Write all the single digit numbers that look the same on a half turn ($\\frac{1}{2}$ turn).**  \n**वे सभी एक अंकीय संख्याएँ लिखिए जो आधा घुमाने ($\\frac{1}{2}$ घूर्णन) पर भी एक जैसी ही दिखती हैं।**"
    },

    # Ch 7: Can You See the Pattern?
    {
        "id": "5m_tb_ch7_1",
        "subjectId": "5_maths",
        "sectionKey": "sec_a",
        "set": "Textbook",
        "orderInSet": 4,
        "originalNum": "TB Q4",
        "marks": 1,
        "hasOrChoice": False,
        "preview": "Rule for pattern: 15 + 24 + 36 = 24 + ... + 15",
        "content": "**Complete the commutative equality pattern:**  \n**क्रम-विनिमेयता पैटर्न को पूरा कीजिए:**  \n$$15 + 24 + 36 = 24 + \\underline{\\hspace{1.5cm}} + 15$$"
    },
    {
        "id": "5m_tb_ch7_2",
        "subjectId": "5_maths",
        "sectionKey": "sec_c",
        "set": "Textbook",
        "orderInSet": 5,
        "originalNum": "TB Q5",
        "marks": 2,
        "hasOrChoice": False,
        "preview": "Magic square with numbers from 1 to 9 where each line sums to 15",
        "content": "**Fill a $3 \\times 3$ grid using numbers from $1$ to $9$ so that the rule states: 'The sum of each row, column, and diagonal is 15'.**  \n**संख्या $1$ से $9$ तक का प्रयोग करके एक $3 \\times 3$ जादुई वर्ग बनाइए ताकि प्रत्येक पंक्ति, स्तंभ और विकर्ण का योग $15$ हो।**"
    },
    {
        "id": "5m_tb_ch7_3",
        "subjectId": "5_maths",
        "sectionKey": "sec_d",
        "set": "Textbook",
        "orderInSet": 6,
        "originalNum": "TB Q6",
        "marks": 3,
        "hasOrChoice": False,
        "preview": "Observe the pattern and find the next two terms: 1x8+1=9, 12x8+2=98...",
        "content": "**Look at the pattern and write the next two steps:**  \n**पैटर्न को देखिए और अगले दो चरण लिखिए:**  \n$$1 \\times 8 + 1 = 9$$  \n$$12 \\times 8 + 2 = 98$$  \n$$123 \\times 8 + 3 = 987$$  \n$$1234 \\times 8 + 4 = \\underline{\\hspace{2cm}}$$  \n$$12345 \\times 8 + 5 = \\underline{\\hspace{2cm}}$$"
    },

    # Ch 8: Mapping Your Way
    {
        "id": "5m_tb_ch8_1",
        "subjectId": "5_maths",
        "sectionKey": "sec_b",
        "set": "Textbook",
        "orderInSet": 7,
        "originalNum": "TB Q7",
        "marks": 1,
        "hasOrChoice": False,
        "preview": "If scale is 1 cm = 200 km, then 2.5 cm on map represents:",
        "content": "**If the scale on a map is $1\\text{ cm} = 200\\text{ km}$, then a distance of $2.5\\text{ cm}$ on the map represents an actual distance of:**  \n**यदि मानचित्र पर पैमाना $1\\text{ सेमी} = 200\\text{ किमी}$ है, तो मानचित्र पर $2.5\\text{ सेमी}$ की दूरी वास्तविक दूरी दर्शाती है:**  \n(a) $400\\text{ km}$  \n(b) $500\\text{ km}$  \n(c) $250\\text{ km}$  \n(d) $600\\text{ km}$"
    },
    {
        "id": "5m_tb_ch8_2",
        "subjectId": "5_maths",
        "sectionKey": "sec_c",
        "set": "Textbook",
        "orderInSet": 8,
        "originalNum": "TB Q8",
        "marks": 2,
        "hasOrChoice": False,
        "preview": "Calculate ground distance if map scale is 2 cm = 1 km and distance measured is 7 cm.",
        "content": "**On a city map, the scale is $2\\text{ cm} = 1\\text{ km}$. If the distance between two monuments on the map is $7\\text{ cm}$, find the real ground distance in kilometres and metres.**  \n**एक शहर के नक्शे पर पैमाना $2\\text{ सेमी} = 1\\text{ किमी}$ है। यदि नक्शे पर दो स्मारकों के बीच की दूरी $7\\text{ सेमी}$ है, तो जमीन पर उनकी वास्तविक दूरी ज्ञात कीजिए।**"
    },

    # Ch 11: Area and its Boundary
    {
        "id": "5m_tb_ch11_1",
        "subjectId": "5_maths",
        "sectionKey": "sec_d",
        "set": "Textbook",
        "orderInSet": 9,
        "originalNum": "TB Q9",
        "marks": 3,
        "hasOrChoice": False,
        "preview": "Find perimeter and area of a rectangular garden of length 15m and breadth 8m.",
        "content": "**A rectangular garden is $15\\text{ m}$ long and $8\\text{ m}$ wide. Find:**  \n**एक आयताकार बगीचे की लंबाई $15\\text{ मी}$ तथा चौड़ाई $8\\text{ मी}$ है। ज्ञात कीजिए:**  \n(a) Its perimeter (घेरा)  \n(b) Its area (क्षेत्रफल)  \n(c) Cost of fencing it at ₹ $25$ per metre."
    },
    {
        "id": "5m_tb_ch11_2",
        "subjectId": "5_maths",
        "sectionKey": "sec_e",
        "set": "Textbook",
        "orderInSet": 10,
        "originalNum": "TB Q10",
        "marks": 4,
        "hasOrChoice": False,
        "preview": "A square carrom board has a perimeter of 320 cm. Find its side and area.",
        "content": "**A square carrom board has a perimeter of $320\\text{ cm}$.**  \n**एक वर्गाकार कैरम बोर्ड का परिमाप (घेरा) $320\\text{ सेमी}$ है।**  \n(a) Find the length of each side of the carrom board. / कैरम बोर्ड की प्रत्येक भुजा की लंबाई ज्ञात कीजिए।  \n(b) What is its total surface area in $\\text{cm}^2$? / इसका कुल क्षेत्रफल कितने वर्ग सेमी होगा?"
    },

    # Ch 13: Ways to Multiply and Divide
    {
        "id": "5m_tb_ch13_1",
        "subjectId": "5_maths",
        "sectionKey": "sec_d",
        "set": "Textbook",
        "orderInSet": 11,
        "originalNum": "TB Q11",
        "marks": 3,
        "hasOrChoice": False,
        "preview": "A farmer packs 24 apples in one box. How many boxes are needed for 1560 apples?",
        "content": "**A fruit seller packs $24$ apples into one carton. How many cartons are needed to pack $1560$ apples? Will any apples be left over?**  \n**एक फल विक्रेता एक डिब्बे में $24$ सेब पैक करता है। $1560$ सेब पैक करने के लिए कितने डिब्बों की आवश्यकता होगी? क्या कोई सेब शेष बचेगा?**"
    },
    {
        "id": "5m_tb_ch13_2",
        "subjectId": "5_maths",
        "sectionKey": "sec_e",
        "set": "Textbook",
        "orderInSet": 12,
        "originalNum": "TB Q12",
        "marks": 4,
        "hasOrChoice": False,
        "preview": "Sohan drinks 8 glasses of water every day. Find water consumed in a year and for 125 people in a day.",
        "content": "**Sohan drinks $8$ glasses of water every day.**  \n**सोहन प्रतिदिन $8$ गिलास पानी पीता है।**  \n(a) How many glasses will he drink in one non-leap year ($365$ days)? / वह एक वर्ष ($365$ दिन) में कितने गिलास पानी पिएगा?  \n(b) If $125$ people live in a hostel and each drinks $8$ glasses daily, how many glasses of water are consumed in the month of September ($30$ days)? / यदि छात्रावास में $125$ लोग रहते हैं, तो सितंबर माह ($30$ दिन) में कुल कितने गिलास पानी पिया जाएगा?"
    }
]

# ==========================================
# 4. CLASS 6 MATHS TEXTBOOK QUESTIONS
# ==========================================
TB_6_MATHS = [
    # Ch 9: Symmetry and Geometry
    {
        "id": "6m_tb_ch9_1",
        "subjectId": "6_maths",
        "sectionKey": "sec_a",
        "set": "Textbook",
        "orderInSet": 1,
        "originalNum": "TB Q1",
        "marks": 1,
        "hasOrChoice": False,
        "preview": "How many lines of symmetry does a regular hexagon have?",
        "content": "**How many lines of symmetry does a regular hexagon have?**  \n**एक सम षट्भुज (Regular hexagon) में कितनी सममिति रेखाएँ होती हैं?**  \n$$\\text{Number of lines of symmetry (सममिति रेखाओं की संख्या)} = 6$$"
    },
    {
        "id": "6m_tb_ch9_2",
        "subjectId": "6_maths",
        "sectionKey": "sec_b",
        "set": "Textbook",
        "orderInSet": 2,
        "originalNum": "TB Q2",
        "marks": 1,
        "hasOrChoice": False,
        "preview": "MCQ: Which of the following letters has both horizontal and vertical lines of symmetry?",
        "content": "**Which of the following capital letters has both horizontal and vertical lines of symmetry?**  \n**निम्नलिखित में से किस बड़े अक्षर में क्षैतिज और ऊर्ध्वाधर दोनों सममिति रेखाएँ होती हैं?**  \n(a) $\\mathbf{A}$  \n(b) $\\mathbf{B}$  \n(c) $\\mathbf{H}$  \n(d) $\\mathbf{M}$"
    },
    {
        "id": "6m_tb_ch9_3",
        "subjectId": "6_maths",
        "sectionKey": "sec_c",
        "set": "Textbook",
        "orderInSet": 3,
        "originalNum": "TB Q3",
        "marks": 2,
        "hasOrChoice": False,
        "preview": "Draw a rough sketch of an isosceles triangle and draw its line of symmetry.",
        "content": "**Draw a rough sketch of an isosceles triangle and indicate its line(s) of symmetry. How many lines of symmetry does it have?**  \n**एक समद्विबाहु त्रिभुज का कच्चा चित्र खींचिए तथा इसकी सममिति रेखा(एँ) दर्शाइए। इसमें कितनी सममिति रेखाएँ होती हैं?**"
    },
    {
        "id": "6m_tb_ch9_4",
        "subjectId": "6_maths",
        "sectionKey": "sec_d",
        "set": "Textbook",
        "orderInSet": 4,
        "originalNum": "TB Q4",
        "marks": 3,
        "hasOrChoice": False,
        "preview": "State the number of lines of symmetry for: (a) Equilateral triangle (b) Square (c) Circle.",
        "content": "**State the number of lines of symmetry for each of the following geometrical shapes:**  \n**निम्नलिखित ज्यामितीय आकृतियों में से प्रत्येक की सममिति रेखाओं की संख्या बताइए:**  \n(a) An Equilateral triangle / समबाहु त्रिभुज  \n(b) A Square / वर्ग  \n(c) A Circle / वृत्त"
    },
    {
        "id": "6m_tb_ch9_5",
        "subjectId": "6_maths",
        "sectionKey": "sec_e",
        "set": "Textbook",
        "orderInSet": 5,
        "originalNum": "TB Q5",
        "marks": 4,
        "hasOrChoice": False,
        "preview": "Construct a line segment AB of length 7.3 cm using ruler and compasses, and find its axis of symmetry.",
        "content": "**Draw a line segment $AB$ of length $7.3\\text{ cm}$ and construct its perpendicular bisector (axis of symmetry) using ruler and compasses. Write the steps of construction.**  \n**पटरी और परकार की सहायता से $7.3\\text{ सेमी}$ लंबा एक रेखाखंड $AB$ खींचिए तथा इसका लंब समद्विभाजक (सममिति अक्ष) खींचिए। रचना के पद लिखिए।**"
    }
]

# ==========================================
# 5. CLASS 7 MATHS TEXTBOOK QUESTIONS
# ==========================================
TB_7_MATHS = [
    # Ch 12: Algebraic Expressions
    {
        "id": "7m_tb_ch12_1",
        "subjectId": "7_maths",
        "sectionKey": "sec_a",
        "set": "Textbook",
        "orderInSet": 1,
        "originalNum": "TB Q1",
        "marks": 1,
        "hasOrChoice": False,
        "preview": "Identify terms and their numerical coefficients in: 5 - 3t^2",
        "content": "**Identify the numerical coefficient of terms (other than constant) in the algebraic expression:**  \n**बीजीय व्यंजक में (अचर पद के अतिरिक्त) पद का संख्यात्मक गुणांक पहचानिए:**  \n$$5 - 3t^2$$"
    },
    {
        "id": "7m_tb_ch12_2",
        "subjectId": "7_maths",
        "sectionKey": "sec_b",
        "set": "Textbook",
        "orderInSet": 2,
        "originalNum": "TB Q2",
        "marks": 1,
        "hasOrChoice": False,
        "preview": "MCQ: The algebraic expression for 'Number 5 added to three times the product of numbers m and n' is:",
        "content": "**The algebraic expression for 'Number 5 added to three times the product of numbers $m$ and $n$' is:**  \n**'संख्याओं $m$ और $n$ के गुणनफल के तीन गुने में संख्या $5$ जोड़ना' के लिए बीजीय व्यंजक है:**  \n(a) $5 + mn$  \n(b) $3mn + 5$  \n(c) $3 + 5mn$  \n(d) $5m + 3n$"
    },
    {
        "id": "7m_tb_ch12_3",
        "subjectId": "7_maths",
        "sectionKey": "sec_c",
        "set": "Textbook",
        "orderInSet": 3,
        "originalNum": "TB Q3",
        "marks": 2,
        "hasOrChoice": False,
        "preview": "Add the algebraic expressions: 7mn + 5, 12mn + 2, 9mn - 8",
        "content": "**Add the algebraic expressions:**  \n**निम्नलिखित बीजीय व्यंजकों का योगफल ज्ञात कीजिए:**  \n$$7mn + 5, \\quad 12mn + 2, \\quad 9mn - 8$$"
    },
    {
        "id": "7m_tb_ch12_4",
        "subjectId": "7_maths",
        "sectionKey": "sec_d",
        "set": "Textbook",
        "orderInSet": 4,
        "originalNum": "TB Q4",
        "marks": 3,
        "hasOrChoice": False,
        "preview": "Subtract 4a - 7ab + 3b + 12 from 12a - 9ab + 5b - 3",
        "content": "**Subtract $(4a - 7ab + 3b + 12)$ from $(12a - 9ab + 5b - 3)$ step by step.**  \n**$(12a - 9ab + 5b - 3)$ में से $(4a - 7ab + 3b + 12)$ को क्रमबद्ध घटाइए।**"
    },
    {
        "id": "7m_tb_ch12_5",
        "subjectId": "7_maths",
        "sectionKey": "sec_e",
        "set": "Textbook",
        "orderInSet": 5,
        "originalNum": "TB Q5",
        "marks": 4,
        "hasOrChoice": False,
        "preview": "Find value of expression 2(a^2 + ab) + 3 - ab when a = 5 and b = -3.",
        "content": "**Simplify the expression and find its value when $a = 5$ and $b = -3$:**  \n**व्यंजक को सरल कीजिए तथा $a = 5$ और $b = -3$ के लिए इसका मान ज्ञात कीजिए:**  \n$$2(a^2 + ab) + 3 - ab$$"
    },

    # Ch 14: Symmetry
    {
        "id": "7m_tb_ch14_1",
        "subjectId": "7_maths",
        "sectionKey": "sec_a",
        "set": "Textbook",
        "orderInSet": 6,
        "originalNum": "TB Q6",
        "marks": 1,
        "hasOrChoice": False,
        "preview": "State the order of rotational symmetry of a square.",
        "content": "**What is the order of rotational symmetry of a Square?**  \n**एक वर्ग की घूर्णन सममिति का क्रम (Order of rotational symmetry) क्या होता है?**  \n$$\\text{Order of Rotational Symmetry} = 4, \\quad \\text{Angle of Rotation} = 90^\\circ$$"
    },
    {
        "id": "7m_tb_ch14_2",
        "subjectId": "7_maths",
        "sectionKey": "sec_c",
        "set": "Textbook",
        "orderInSet": 7,
        "originalNum": "TB Q7",
        "marks": 2,
        "hasOrChoice": False,
        "preview": "Which quadrilaterals have both line symmetry and rotational symmetry of order more than 1?",
        "content": "**Name any two quadrilaterals which have both line symmetry and rotational symmetry of order more than $1$.**  \n**किन्हीं दो ऐसे चतुर्भुजों के नाम लिखिए जिनमें रैखिक सममिति तथा $1$ से अधिक क्रम की घूर्णन सममिति दोनों हों।**"
    },

    # Ch 15: Visualising Solid Shapes
    {
        "id": "7m_tb_ch15_1",
        "subjectId": "7_maths",
        "sectionKey": "sec_b",
        "set": "Textbook",
        "orderInSet": 8,
        "originalNum": "TB Q8",
        "marks": 1,
        "hasOrChoice": False,
        "preview": "MCQ: Number of faces, vertices and edges in a cuboid",
        "content": "**The number of faces ($F$), vertices ($V$), and edges ($E$) in a cuboid are respectively:**  \n**एक घनाभ में फलकों ($F$), शीर्षों ($V$) तथा किनारों ($E$) की संख्या क्रमशः होती है:**  \n(a) $F=6, V=8, E=12$  \n(b) $F=8, V=6, E=12$  \n(c) $F=6, V=12, E=8$  \n(d) $F=12, V=8, E=6$"
    },
    {
        "id": "7m_tb_ch15_2",
        "subjectId": "7_maths",
        "sectionKey": "sec_c",
        "set": "Textbook",
        "orderInSet": 9,
        "originalNum": "TB Q9",
        "marks": 2,
        "hasOrChoice": False,
        "preview": "State Euler's formula for 3D polyhedrons and verify it for a cube.",
        "content": "**State Euler's formula for convex polyhedrons and verify it for a Cube where $F=6, V=8, E=12$.**  \n**ठोस बहुफलकों के लिए आयलर सूत्र (Euler's formula) लिखिए तथा एक घन के लिए इसका सत्यापन कीजिए।**  \n$$F + V - E = 2$$"
    },
    {
        "id": "7m_tb_ch15_3",
        "subjectId": "7_maths",
        "sectionKey": "sec_e",
        "set": "Textbook",
        "orderInSet": 10,
        "originalNum": "TB Q10",
        "marks": 4,
        "hasOrChoice": False,
        "preview": "Draw an oblique sketch and an isometric sketch of a cuboid of dimensions 4 cm x 3 cm x 2 cm.",
        "content": "**Draw the following sketches of a cuboid of dimensions $4\\text{ cm} \\times 3\\text{ cm} \\times 2\\text{ cm}$:**  \n**$4\\text{ सेमी} \\times 3\\text{ सेमी} \\times 2\\text{ सेमी}$ विमाओं वाले एक घनाभ के निम्नलिखित चित्र बनाइए:**  \n(a) An Oblique Sketch / एक तिर्यक चित्र  \n(b) An Isometric Sketch on isometric dot paper / समदूरिक डॉट पेपर पर एक समदूरिक चित्र"
    }
]

def main():
    print("Loading data/questions.json...")
    with open(QUESTIONS_PATH, "r", encoding="utf-8") as f:
        db = json.load(f)

    # Ingest for 6_science
    existing_6sci = set(q["id"] for q in db.get("6_science", []))
    added_6sci = 0
    for q in TB_6_SCIENCE:
        if q["id"] not in existing_6sci:
            db["6_science"].append(q)
            existing_6sci.add(q["id"])
            added_6sci += 1

    # Ingest for 7_science
    existing_7sci = set(q["id"] for q in db.get("7_science", []))
    added_7sci = 0
    for q in TB_7_SCIENCE:
        if q["id"] not in existing_7sci:
            db["7_science"].append(q)
            existing_7sci.add(q["id"])
            added_7sci += 1

    # Ingest for 5_maths
    from chapter_classifier import determine_chapter
    existing_5m = set(q["id"] for q in db.get("5_maths", []))
    added_5m = 0
    for q in TB_5_MATHS:
        if "chapter" not in q:
            q["chapter"] = determine_chapter("5_maths", q["content"], q["preview"])
        if q["id"] not in existing_5m:
            db["5_maths"].append(q)
            existing_5m.add(q["id"])
            added_5m += 1

    # Ingest for 6_maths
    existing_6m = set(q["id"] for q in db.get("6_maths", []))
    added_6m = 0
    for q in TB_6_MATHS:
        if "chapter" not in q:
            q["chapter"] = determine_chapter("6_maths", q["content"], q["preview"])
        if q["id"] not in existing_6m:
            db["6_maths"].append(q)
            existing_6m.add(q["id"])
            added_6m += 1

    # Ingest for 7_maths
    existing_7m = set(q["id"] for q in db.get("7_maths", []))
    added_7m = 0
    for q in TB_7_MATHS:
        if "chapter" not in q:
            q["chapter"] = determine_chapter("7_maths", q["content"], q["preview"])
        if q["id"] not in existing_7m:
            db["7_maths"].append(q)
            existing_7m.add(q["id"])
            added_7m += 1

    with open(QUESTIONS_PATH, "w", encoding="utf-8") as f:
        json.dump(db, f, indent=2, ensure_ascii=False)

    print(f"Added {added_6sci} textbook questions to 6_science (Total: {len(db['6_science'])})")
    print(f"Added {added_7sci} textbook questions to 7_science (Total: {len(db['7_science'])})")
    print(f"Added {added_5m} textbook questions to 5_maths (Total: {len(db['5_maths'])})")
    print(f"Added {added_6m} textbook questions to 6_maths (Total: {len(db['6_maths'])})")
    print(f"Added {added_7m} textbook questions to 7_maths (Total: {len(db['7_maths'])})")
    print(f"8_science currently has {len(db.get('8_science', []))} questions.")
    
    total_qs = sum(len(ql) for ql in db.values())
    print(f"\nGRAND TOTAL QUESTIONS IN DATABASE ACROSS ALL CLASSES: {total_qs} questions!")

if __name__ == "__main__":
    main()
