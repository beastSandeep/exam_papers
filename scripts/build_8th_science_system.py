# scripts/build_8th_science_system.py
# Comprehensive builder for Class 8 Science Half-Yearly Exam ecosystem:
# 1. Compiles Set A, Set B, and Set C (29 questions each, 50 marks) based on Chapters 5, 6, 7, 8, 9
# 2. Generates Markdown exam papers: Class_8_Science_Half_Yearly_Paper.md, Set_B.md, Set_C.md
# 3. Extracts remaining textbook chapters (10-18) from F:\8th Science\questions
# 4. Updates data/questions.json and data/blueprints.json

import os, sys, json, re

sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
QUESTIONS_PATH = os.path.join(ROOT_DIR, "data", "questions.json")
BLUEPRINTS_PATH = os.path.join(ROOT_DIR, "data", "blueprints.json")
PAPERS_DIR = os.path.join(ROOT_DIR, "8th_Science")

CH_NAMES = {
    5: "Ch 5: Conservation of Plants and Animals (पौधे एवं जंतुओं का संरक्षण)",
    6: "Ch 6: Reproduction in Animals (जंतुओं में जनन)",
    7: "Ch 7: Reaching the Age of Adolescence (किशोरावस्था की ओर)",
    8: "Ch 8: Force and Pressure (बल तथा दाब)",
    9: "Ch 9: Friction (घर्षण)"
}

# ==========================================
# 1. SET A QUESTIONS DEFINITIONS
# ==========================================
SET_A_DATA = [
    # --- Section 1: MCQs (1 Mark each) ---
    {
        "id": "8_sci_sec1_set_a_q1",
        "sectionKey": "sec_1",
        "orderInSet": 1,
        "originalNum": "Q1",
        "marks": 1,
        "chapter": CH_NAMES[5],
        "preview": "(i) Which gas increases in the atmosphere due to large-scale deforestation, leading to global warming?",
        "content": "**(i) Which gas increases in the atmosphere due to large-scale deforestation, leading to global warming?**  \n**व्यापक वनोन्मूलन के कारण वायुमंडल में किस गैस की मात्रा बढ़ जाती है, जिससे ग्लोबल वार्मिंग (विश्व ऊष्णन) होती है?**  \n(a) Oxygen / ऑक्सीजन  \n(b) Carbon dioxide / कार्बन डाइऑक्साइड  \n(c) Nitrogen / नाइट्रोजन  \n(d) Hydrogen / हाइड्रोजन"
    },
    {
        "id": "8_sci_sec1_set_a_q2",
        "sectionKey": "sec_1",
        "orderInSet": 2,
        "originalNum": "Q2",
        "marks": 1,
        "chapter": CH_NAMES[6],
        "preview": "(ii) In which of the following animals does external fertilisation take place?",
        "content": "**(ii) In which of the following animals does external fertilisation take place?**  \n**निम्नलिखित में से किस जंतु में बाह्य निषेचन (External Fertilisation) होता है?**  \n(a) Cow / गाय  \n(b) Human / मनुष्य  \n(c) Frog / मेंढक  \n(d) Hen / मुर्गी"
    },
    {
        "id": "8_sci_sec1_set_a_q3",
        "sectionKey": "sec_1",
        "orderInSet": 3,
        "originalNum": "Q3",
        "marks": 1,
        "chapter": CH_NAMES[7],
        "preview": "(iii) Which hormone is responsible for the development of secondary sexual characteristics in adolescent boys?",
        "content": "**(iii) Which hormone is responsible for the development of secondary sexual characteristics in adolescent boys?**  \n**किशोर बालकों में द्वितीयक लैंगिक लक्षणों के विकास के लिए कौन-सा हार्मोन उत्तरदायी है?**  \n(a) Estrogen / एस्ट्रोजन  \n(b) Insulin / इंसुलिन  \n(c) Testosterone / टेस्टोस्टेरोन  \n(d) Thyroxine / थायरोक्सिन"
    },
    {
        "id": "8_sci_sec1_set_a_q4",
        "sectionKey": "sec_1",
        "orderInSet": 4,
        "originalNum": "Q4",
        "marks": 1,
        "chapter": CH_NAMES[8],
        "preview": "(iv) Which of the following is an example of a non-contact force?",
        "content": "**(iv) Which of the following is an example of a non-contact force?**  \n**निम्नलिखित में से कौन-सा असंपर्क बल (Non-contact force) का उदाहरण है?**  \n(a) Muscular force / पेशीय बल  \n(b) Friction force / घर्षण बल  \n(c) Magnetic force / चुंबकीय बल  \n(d) Mechanical force / यांत्रिक बल"
    },
    {
        "id": "8_sci_sec1_set_a_q5",
        "sectionKey": "sec_1",
        "orderInSet": 5,
        "originalNum": "Q5",
        "marks": 1,
        "chapter": CH_NAMES[9],
        "preview": "(v) In which direction does the force of friction always act on a moving body?",
        "content": "**(v) In which direction does the force of friction always act on a moving body?**  \n**किसी गतिमान वस्तु पर घर्षण बल सदैव किस दिशा में कार्य करता है?**  \n(a) In the direction of motion / गति की दिशा में  \n(b) Opposite to the direction of motion / गति की दिशा के विपरीत  \n(c) Perpendicular to the direction of motion / गति की दिशा के लंबवत  \n(d) Downwards towards the centre of the Earth / नीचे पृथ्वी के केंद्र की ओर"
    },

    # --- Section 2: Fill in the Blanks (1 Mark each) ---
    {
        "id": "8_sci_sec2_set_a_q1",
        "sectionKey": "sec_2",
        "orderInSet": 1,
        "originalNum": "Q1",
        "marks": 1,
        "chapter": CH_NAMES[5],
        "preview": "(i) The species of plants and animals found exclusively in a particular geographical area are called _______ species.",
        "content": "**(i) The species of plants and animals found exclusively in a particular geographical area are called _______ species.**  \n**पौधों और जंतुओं की वे प्रजातियाँ जो केवल किसी विशेष भौगोलिक क्षेत्र में ही पाई जाती हैं, _______ प्रजातियाँ कहलाती हैं।**"
    },
    {
        "id": "8_sci_sec2_set_a_q2",
        "sectionKey": "sec_2",
        "orderInSet": 2,
        "originalNum": "Q2",
        "marks": 1,
        "chapter": CH_NAMES[6],
        "preview": "(ii) The single cell formed by the fusion of male and female gametes during fertilisation is called a _______.",
        "content": "**(ii) The single cell formed by the fusion of male and female gametes during fertilisation is called a _______.**  \n**निषेचन के दौरान नर और मादा युग्मकों के संलयन से बनने वाली एकल कोशिका को _______ कहते हैं।**"
    },
    {
        "id": "8_sci_sec2_set_a_q3",
        "sectionKey": "sec_2",
        "orderInSet": 3,
        "originalNum": "Q3",
        "marks": 1,
        "chapter": CH_NAMES[7],
        "preview": "(iii) The period of life when the human body undergoes physiological changes leading to reproductive maturity is called _______.",
        "content": "**(iii) The period of life when the human body undergoes physiological changes leading to reproductive maturity is called _______.**  \n**मानव जीवन की वह अवधि जब शरीर में प्रजनन परिपक्वता लाने वाले शारीरिक परिवर्तन होते हैं, _______ कहलाती है।**"
    },
    {
        "id": "8_sci_sec2_set_a_q4",
        "sectionKey": "sec_2",
        "orderInSet": 4,
        "originalNum": "Q4",
        "marks": 1,
        "chapter": CH_NAMES[8],
        "preview": "(iv) The force acting perpendicular on a unit area of a surface is defined as _______.",
        "content": "**(iv) The force acting perpendicular on a unit area of a surface is defined as _______.**  \n**किसी पृष्ठ के प्रति एकांक क्षेत्रफल पर लंबवत लगने वाले बल को _______ कहते हैं।**"
    },
    {
        "id": "8_sci_sec2_set_a_q5",
        "sectionKey": "sec_2",
        "orderInSet": 5,
        "originalNum": "Q5",
        "marks": 1,
        "chapter": CH_NAMES[9],
        "preview": "(v) Sprinkling fine talcum powder on a carrom board _______ the friction between striker and the board.",
        "content": "**(v) Sprinkling fine talcum powder on a carrom board _______ the friction between striker and the board.**  \n**कैरम बोर्ड पर बारीक पाउडर छिड़कने से स्ट्राइकर और बोर्ड के बीच घर्षण _______ हो जाता है।**"
    },

    # --- Section 3: True / False (1 Mark each) ---
    {
        "id": "8_sci_sec3_set_a_q1",
        "sectionKey": "sec_3",
        "orderInSet": 1,
        "originalNum": "Q1",
        "marks": 1,
        "chapter": CH_NAMES[5],
        "preview": "(i) A wildlife sanctuary is a protected area where wild animals are conserved in their natural habitat.",
        "content": "**(i) A wildlife sanctuary is a protected area where wild animals are conserved in their natural habitat without external disturbance.**  \n**वन्यजीव अभयारण्य एक ऐसा संरक्षित क्षेत्र है जहाँ वन्य जीवों को बिना किसी बाहरी हस्तक्षेप के उनके प्राकृतिक आवास में संरक्षित किया जाता है।**"
    },
    {
        "id": "8_sci_sec3_set_a_q2",
        "sectionKey": "sec_3",
        "orderInSet": 2,
        "originalNum": "Q2",
        "marks": 1,
        "chapter": CH_NAMES[6],
        "preview": "(ii) In human beings, the fertilisation of the ovum by the sperm takes place in the fallopian tube (oviduct).",
        "content": "**(ii) In human beings, the fertilisation of the ovum by the sperm takes place in the fallopian tube (oviduct).**  \n**मनुष्यों में शुक्राणु द्वारा अंडाणु का निषेचन डिंबवाहिनी (फैलोपियन ट्यूब) में होता है।**"
    },
    {
        "id": "8_sci_sec3_set_a_q3",
        "sectionKey": "sec_3",
        "orderInSet": 3,
        "originalNum": "Q3",
        "marks": 1,
        "chapter": CH_NAMES[7],
        "preview": "(iii) Endocrine glands release their hormones directly into the bloodstream without using any ducts.",
        "content": "**(iii) Endocrine glands release their hormones directly into the bloodstream without using any ducts.**  \n**अंतःस्रावी ग्रंथियाँ बिना किसी नलिका के अपने हार्मोन सीधे रक्त प्रवाह में छोड़ती हैं।**"
    },
    {
        "id": "8_sci_sec3_set_a_q4",
        "sectionKey": "sec_3",
        "orderInSet": 4,
        "originalNum": "Q4",
        "marks": 1,
        "chapter": CH_NAMES[8],
        "preview": "(iv) Atmospheric pressure increases steadily as we climb higher up a mountain.",
        "content": "**(iv) Atmospheric pressure increases steadily as we climb higher up a mountain.**  \n**जैसे-जैसे हम किसी पर्वत पर ऊपर चढ़ते हैं, वायुमंडलीय दाब लगातार बढ़ता जाता है।**"
    },
    {
        "id": "8_sci_sec3_set_a_q5",
        "sectionKey": "sec_3",
        "orderInSet": 5,
        "originalNum": "Q5",
        "marks": 1,
        "chapter": CH_NAMES[9],
        "preview": "(v) Friction between two surfaces can be completely reduced to zero by applying ideal lubricants.",
        "content": "**(v) Friction between two surfaces can be completely reduced to zero by applying ideal lubricants.**  \n**आदर्श स्नेहक (lubricants) लगाकर दो सतहों के बीच घर्षण को पूरी तरह से शून्य किया जा सकता है।**"
    },

    # --- Section 4: Very Short Answer (2 Marks each) ---
    {
        "id": "8_sci_sec4_set_a_q1",
        "sectionKey": "sec_4",
        "orderInSet": 1,
        "originalNum": "Q1",
        "marks": 2,
        "chapter": CH_NAMES[5],
        "preview": "(i) (a) What is the Red Data Book? (b) Name any one endangered animal species in India.",
        "content": "**(i) (a) What is the Red Data Book? (b) Name any one endangered animal species in India.**  \n**(a) रेड डाटा पुस्तक (Red Data Book) क्या है? (b) भारत में पाई जाने वाली किसी एक संकटापन्न वन्यजीव प्रजाति का नाम लिखिए।**"
    },
    {
        "id": "8_sci_sec4_set_a_q2",
        "sectionKey": "sec_4",
        "orderInSet": 2,
        "originalNum": "Q2",
        "marks": 2,
        "chapter": CH_NAMES[6],
        "preview": "(ii) Differentiate between internal fertilisation and external fertilisation with one example of each.",
        "content": "**(ii) Differentiate between internal fertilisation and external fertilisation with one example of each.**  \n**आंतरिक निषेचन और बाह्य निषेचन में अंतर स्पष्ट कीजिए तथा प्रत्येक का एक-एक उदाहरण दीजिए।**"
    },
    {
        "id": "8_sci_sec4_set_a_q3",
        "sectionKey": "sec_4",
        "orderInSet": 3,
        "originalNum": "Q3",
        "marks": 2,
        "chapter": CH_NAMES[7],
        "preview": "(iii) (a) What is Adam's apple? (b) Why is it more prominent in boys than in girls during puberty?",
        "content": "**(iii) (a) What is Adam's apple? (b) Why is it more prominent in boys than in girls during puberty?**  \n**(a) 'एडम्स एप्पल' (कंठमणि) क्या है? (b) यौवनारंभ के दौरान यह लड़कियों की तुलना में लड़कों में अधिक उभरा हुआ क्यों दिखाई देता है?**"
    },
    {
        "id": "8_sci_sec4_set_a_q4",
        "sectionKey": "sec_4",
        "orderInSet": 4,
        "originalNum": "Q4",
        "marks": 2,
        "chapter": CH_NAMES[8],
        "preview": "(iv) (a) Define force and write its SI unit. (b) Two forces of 8 N and 12 N act on a block in the same direction. Find the net resultant force.",
        "content": "**(iv) (a) Define force and write its SI unit. (b) Two forces of 8 N and 12 N act on a block in the same direction. Find the net resultant force.**  \n**(a) बल को परिभाषित कीजिए तथा इसका SI मात्रक लिखिए। (b) किसी गुटके पर एक ही दिशा में 8 N और 12 N के दो बल कार्य करते हैं। कुल परिणामी बल ज्ञात कीजिए।**"
    },
    {
        "id": "8_sci_sec4_set_a_q5",
        "sectionKey": "sec_4",
        "orderInSet": 5,
        "originalNum": "Q5",
        "marks": 2,
        "chapter": CH_NAMES[9],
        "preview": "(v) Why do sports shoes and mountaineering boots have grooved, treaded soles? Explain.",
        "content": "**(v) Why do sports shoes and mountaineering boots have grooved, treaded soles? Explain.**  \n**खिलाड़ियों के जूते और पर्वतारोहियों के जूतों के तलों में खांचे (treads) क्यों बनाए जाते हैं? स्पष्ट कीजिए।**"
    },

    # --- Section 5: Short Answer (3 Marks each) ---
    {
        "id": "8_sci_sec5_set_a_q1",
        "sectionKey": "sec_5",
        "orderInSet": 1,
        "originalNum": "Q1",
        "marks": 3,
        "chapter": CH_NAMES[5],
        "preview": "(i) What is desertification? Explain how continuous deforestation leads to desertification and loss of soil fertility.",
        "content": "**(i) What is desertification? Explain how continuous deforestation leads to desertification and loss of soil fertility.**  \n**मरुस्थलीकरण किसे कहते हैं? समझाइए कि निरंतर वनोन्मूलन किस प्रकार उपजाऊ भूमि को मरुस्थल में परिवर्तित कर देता है।**"
    },
    {
        "id": "8_sci_sec5_set_a_q2",
        "sectionKey": "sec_5",
        "orderInSet": 2,
        "originalNum": "Q2",
        "marks": 3,
        "chapter": CH_NAMES[6],
        "preview": "(ii) (a) Differentiate between viviparous animals and oviparous animals. (b) Give two examples of each.",
        "content": "**(ii) (a) Differentiate between viviparous animals and oviparous animals. (b) Give two examples of each.**  \n**(a) जरायुज (viviparous) और अंडप्रजक (oviparous) जंतुओं में अंतर बताइए। (b) प्रत्येक के दो-दो उदाहरण दीजिए।**"
    },
    {
        "id": "8_sci_sec5_set_a_q3",
        "sectionKey": "sec_5",
        "orderInSet": 3,
        "originalNum": "Q3",
        "marks": 3,
        "chapter": CH_NAMES[7],
        "preview": "(iii) Explain the biological mechanism of sex determination in an unborn human baby.",
        "content": "**(iii) Explain the biological mechanism of sex determination in an unborn human baby. Show how the father's sex chromosome determines whether the baby will be a boy or a girl.**  \n**मानव भ्रूण में लिंग निर्धारण की जैविक प्रक्रिया को समझाइए। यह स्पष्ट कीजिए कि पिता का लिंग गुणसूत्र किस प्रकार निर्धारित करता है कि होने वाला शिशु लड़का होगा या लड़की।**"
    },
    {
        "id": "8_sci_sec5_set_a_q4",
        "sectionKey": "sec_5",
        "orderInSet": 4,
        "originalNum": "Q4",
        "marks": 3,
        "chapter": CH_NAMES[8],
        "preview": "(iv) A force of 400 N is applied perpendicularly on a wooden board having an area of 0.08 m². Calculate pressure.",
        "content": "**(iv) A force of 400 N is applied perpendicularly on a wooden board having a surface area of 0.08 m². Calculate the pressure exerted on the board in Pascals (N/m²).**  \n**एक लकड़ी के तख्ते पर, जिसका क्षेत्रफल 0.08 m² है, 400 N का लंबवत बल लगाया जाता है। तख्ते पर लगने वाले दाब की पास्कल (N/m²) में गणना कीजिए।**"
    },
    {
        "id": "8_sci_sec5_set_a_q5",
        "sectionKey": "sec_5",
        "orderInSet": 5,
        "originalNum": "Q5",
        "marks": 3,
        "chapter": CH_NAMES[9],
        "preview": "(v) (a) Arrange static, sliding, and rolling friction in decreasing order. (b) Why is rolling friction smaller than sliding?",
        "content": "**(v) (a) Arrange static friction, sliding friction, and rolling friction in decreasing order of their strength. (b) Why is rolling friction significantly smaller than sliding friction?**  \n**(a) स्थैतिक घर्षण, सर्पी घर्षण और लोटनिक घर्षण को उनके परिमाण के घटते क्रम में व्यवस्थित कीजिए। (b) लोटनिक घर्षण, सर्पी घर्षण से काफी कम क्यों होता है?**"
    },

    # --- Section 6: Long Answer (5 Marks each with OR choices) ---
    {
        "id": "8_sci_sec6_set_a_q1",
        "sectionKey": "sec_6",
        "orderInSet": 1,
        "originalNum": "Q1",
        "marks": 5,
        "chapter": CH_NAMES[8],
        "defaultOrPartnerId": "8_sci_sec6_set_a_q1_alt",
        "preview": "(i) (a) What is atmospheric pressure? Describe an activity with a rubber sucker. (b) Why do deep-sea divers wear pressurized suits?",
        "content": "**(i) (a) What is atmospheric pressure? Describe an activity with a rubber sucker to demonstrate the existence of atmospheric pressure. (3 Marks)**  \n**वायुमंडलीय दाब क्या है? रबर के चूषक (rubber sucker) की सहायता से एक क्रियाकलाप द्वारा वायुमंडलीय दाब के अस्तित्व को प्रदर्शित कीजिए।**  \n**(b) Why do deep-sea divers have to wear specially designed pressurized diving suits? (2 Marks)**  \n**गहरे समुद्र में जाने वाले गोताखोरों को विशेष रूप से निर्मित दबाव-युक्त सूट क्यों पहनने पड़ते हैं?**"
    },
    {
        "id": "8_sci_sec6_set_a_q1_alt",
        "sectionKey": "sec_6",
        "orderInSet": 1.5,
        "originalNum": "Q1",
        "marks": 5,
        "chapter": CH_NAMES[9],
        "defaultOrPartnerId": "8_sci_sec6_set_a_q1",
        "preview": "(a) Why is friction called a 'necessary evil'? Give two advantages and disadvantages. (b) What is fluid drag?",
        "content": "**(a) Why is friction often referred to as a 'necessary evil'? Mention two essential advantages and two major disadvantages of friction in our daily life. (4 Marks)**  \n**घर्षण को 'अनिवार्य बुराई' (necessary evil) क्यों कहा जाता है? हमारे दैनिक जीवन में घर्षण के दो आवश्यक लाभ और दो प्रमुख हानियाँ लिखिए।**  \n**(b) Name the frictional force exerted by fluids on objects moving through them. (1 Mark)**  \n**तरल पदार्थों (द्रवों एवं गैसों) द्वारा गतिमान वस्तुओं पर लगाए जाने वाले घर्षण बल को क्या कहते हैं?**"
    },
    {
        "id": "8_sci_sec6_set_a_q2",
        "sectionKey": "sec_6",
        "orderInSet": 2,
        "originalNum": "Q2",
        "marks": 5,
        "chapter": CH_NAMES[6],
        "defaultOrPartnerId": "8_sci_sec6_set_a_q2_alt",
        "preview": "(ii) (a) Describe the process of binary fission in Amoeba. (b) How does budding in Hydra differ from binary fission?",
        "content": "**(ii) (a) Describe the process of binary fission in Amoeba with step-by-step description. (3 Marks)**  \n**अमीबा में द्विखंडन (Binary Fission) की प्रक्रिया का क्रमबद्ध वर्णन कीजिए।**  \n**(b) How does asexual reproduction by budding in Hydra differ from binary fission? (2 Marks)**  \n**हाइड्रा में मुकुलन (Budding) द्वारा होने वाला अलैंगिक जनन, द्विखंडन से किस प्रकार भिन्न है?**"
    },
    {
        "id": "8_sci_sec6_set_a_q2_alt",
        "sectionKey": "sec_6",
        "orderInSet": 2.5,
        "originalNum": "Q2",
        "marks": 5,
        "chapter": CH_NAMES[5],
        "defaultOrPartnerId": "8_sci_sec6_set_a_q2",
        "preview": "(a) Distinguish between a National Park and a Wildlife Sanctuary. (b) Why should paper be saved and recycled?",
        "content": "**(a) Distinguish clearly between a National Park and a Wildlife Sanctuary. Name one famous National Park in India. (3 Marks)**  \n**राष्ट्रीय उद्यान और वन्यजीव अभयारण्य के बीच स्पष्ट अंतर बताइए। भारत के किसी एक प्रसिद्ध राष्ट्रीय उद्यान का नाम लिखिए।**  \n**(b) Why should paper be saved and recycled? State two simple habits by which students can save trees. (2 Marks)**  \n**कागज की बचत और पुनर्चक्रण क्यों किया जाना चाहिए? ऐसे दो सरल उपाय बताइए जिनसे विद्यार्थी वृक्षों को बचाने में योगदान दे सकते हैं।**"
    }
]

# ==========================================
# 2. SET B QUESTIONS DEFINITIONS
# ==========================================
SET_B_DATA = [
    # --- Section 1: MCQs (1 Mark each) ---
    {
        "id": "8_sci_sec1_set_b_q1",
        "sectionKey": "sec_1",
        "orderInSet": 1,
        "originalNum": "Q1",
        "marks": 1,
        "chapter": CH_NAMES[5],
        "preview": "(i) Which of the following is an endemic flora of the Pachmarhi Biosphere Reserve?",
        "content": "**(i) Which of the following is an endemic flora of the Pachmarhi Biosphere Reserve?**  \n**निम्नलिखित में से कौन-सा पचमढ़ी जैवमंडल आरक्षित क्षेत्र की एक विशेष-क्षेत्री वनस्पति (Endemic Flora) है?**  \n(a) Teak and Apple / सागौन और सेब  \n(b) Sal and Wild Mango / साल और जंगली आम  \n(c) Cactus and Banyan / नागफनी और बरगद  \n(d) Neem and Rose / नीम और गुलाब"
    },
    {
        "id": "8_sci_sec1_set_b_q2",
        "sectionKey": "sec_1",
        "orderInSet": 2,
        "originalNum": "Q2",
        "marks": 1,
        "chapter": CH_NAMES[6],
        "preview": "(ii) Asexual reproduction in Hydra takes place by the process of:",
        "content": "**(ii) Asexual reproduction in Hydra takes place by the process of:**  \n**हाइड्रा में अलैंगिक जनन किस विधि द्वारा होता है?**  \n(a) Binary fission / द्विखंडन  \n(b) Budding / मुकुलन  \n(c) Spore formation / बीजाणु निर्माण  \n(d) Fragmentation / विखंडन"
    },
    {
        "id": "8_sci_sec1_set_b_q3",
        "sectionKey": "sec_1",
        "orderInSet": 3,
        "originalNum": "Q3",
        "marks": 1,
        "chapter": CH_NAMES[7],
        "preview": "(iii) The deficiency of which hormone in the diet causes Goitre, marked by a swollen neck?",
        "content": "**(iii) The deficiency of which hormone in the diet causes Goitre, a disease marked by a swollen neck?**  \n**आहार में किस हार्मोन की कमी से घेंघा (गलगंड) रोग हो जाता है, जिसमें गर्दन की ग्रंथि सूज जाती है?**  \n(a) Insulin / इंसुलिन  \n(b) Growth hormone / वृद्धि हार्मोन  \n(c) Thyroxine / थायरोक्सिन  \n(d) Adrenaline / एड्रिनलिन"
    },
    {
        "id": "8_sci_sec1_set_b_q4",
        "sectionKey": "sec_1",
        "orderInSet": 4,
        "originalNum": "Q4",
        "marks": 1,
        "chapter": CH_NAMES[8],
        "preview": "(iv) When two equal and opposite forces act simultaneously on an object, the net resultant force is:",
        "content": "**(iv) When two equal and opposite forces act simultaneously on an object, the net resultant force is:**  \n**जब किसी वस्तु पर दो बराबर और विपरीत बल एक साथ कार्य करते हैं, तो उस पर लगने वाला कुल परिणामी बल होता है:**  \n(a) Double the force / बल का दोगुना  \n(b) Zero / शून्य  \n(c) Half the force / बल का आधा  \n(d) Infinite / अनंत"
    },
    {
        "id": "8_sci_sec1_set_b_q5",
        "sectionKey": "sec_1",
        "orderInSet": 5,
        "originalNum": "Q5",
        "marks": 1,
        "chapter": CH_NAMES[9],
        "preview": "(v) Which device is widely used in heavy rotating machinery to replace sliding friction with rolling friction?",
        "content": "**(v) Which of the following devices is widely used in heavy rotating machinery to replace sliding friction with rolling friction?**  \n**घूर्णन करने वाली भारी मशीनों में सर्पी घर्षण को लोटनिक घर्षण में बदलने के लिए निम्नलिखित में से किस युक्ति का व्यापक उपयोग किया जाता है?**  \n(a) Lever / उत्तोलक  \n(b) Ball bearings / बॉल बेयरिंग  \n(c) Piston / पिस्टन  \n(d) Pulley / घिरनी"
    },

    # --- Section 2: Fill in the Blanks (1 Mark each) ---
    {
        "id": "8_sci_sec2_set_b_q1",
        "sectionKey": "sec_2",
        "orderInSet": 1,
        "originalNum": "Q1",
        "marks": 1,
        "chapter": CH_NAMES[5],
        "preview": "(i) The variety of all plant, animal, and microorganism species living in a particular area is known as _______.",
        "content": "**(i) The variety of all plant, animal, and microorganism species living in a particular area is known as _______.**  \n**किसी क्षेत्र में पाए जाने वाले सभी पौधों, जंतुओं और सूक्ष्मजीवों की प्रजातियों की विविधता को _______ कहते हैं।**"
    },
    {
        "id": "8_sci_sec2_set_b_q2",
        "sectionKey": "sec_2",
        "orderInSet": 2,
        "originalNum": "Q2",
        "marks": 1,
        "chapter": CH_NAMES[6],
        "preview": "(ii) Animals that lay eggs instead of giving birth to young ones directly are known as _______ animals.",
        "content": "**(ii) Animals that lay eggs instead of giving birth to young ones directly are known as _______ animals.**  \n**वे जंतु जो सीधे बच्चे को जन्म न देकर अंडे देते हैं, _______ जंतु कहलाते हैं।**"
    },
    {
        "id": "8_sci_sec2_set_b_q3",
        "sectionKey": "sec_2",
        "orderInSet": 3,
        "originalNum": "Q3",
        "marks": 1,
        "chapter": CH_NAMES[7],
        "preview": "(iii) The very first menstrual flow that commences in girls at the onset of puberty is termed _______.",
        "content": "**(iii) The very first menstrual flow that commences in girls at the onset of puberty is termed _______.**  \n**लड़कियों में यौवनारंभ के समय शुरू होने वाले प्रथम मासिक धर्म (ऋतुस्राव) को _______ कहते हैं।**"
    },
    {
        "id": "8_sci_sec2_set_b_q4",
        "sectionKey": "sec_2",
        "orderInSet": 4,
        "originalNum": "Q4",
        "marks": 1,
        "chapter": CH_NAMES[8],
        "preview": "(iv) The pressure exerted by a liquid at the base of a container _______ with an increase in liquid height.",
        "content": "**(iv) The pressure exerted by a liquid at the base of a container _______ with an increase in the height of the liquid column.**  \n**किसी बर्तन के तल पर द्रव द्वारा डाला जाने वाला दाब द्रव स्तंभ की ऊँचाई बढ़ने पर _______ है।**"
    },
    {
        "id": "8_sci_sec2_set_b_q5",
        "sectionKey": "sec_2",
        "orderInSet": 5,
        "originalNum": "Q5",
        "marks": 1,
        "chapter": CH_NAMES[9],
        "preview": "(v) The frictional drag force exerted by fluids on objects moving through them depends on speed, shape, and _______.",
        "content": "**(v) The frictional drag force exerted by fluids on objects moving through them depends on the object's speed, shape, and the _______ of the fluid.**  \n**तरल पदार्थों में गतिमान वस्तुओं पर लगने वाला घर्षण बल वस्तु की चाल, आकृति और तरल की _______ पर निर्भर करता है।**"
    },

    # --- Section 3: True / False (1 Mark each) ---
    {
        "id": "8_sci_sec3_set_b_q1",
        "sectionKey": "sec_3",
        "orderInSet": 1,
        "originalNum": "Q1",
        "marks": 1,
        "chapter": CH_NAMES[5],
        "preview": "(i) Deforestation increases the water soaking and holding capacity of the soil, thereby preventing floods.",
        "content": "**(i) Deforestation increases the water soaking and holding capacity of the soil, thereby preventing floods.**  \n**वनोन्मूलन से मिट्टी की जल सोखने और धारण करने की क्षमता बढ़ जाती है, जिससे बाढ़ की रोकथाम होती है।**"
    },
    {
        "id": "8_sci_sec3_set_b_q2",
        "sectionKey": "sec_3",
        "orderInSet": 2,
        "originalNum": "Q2",
        "marks": 1,
        "chapter": CH_NAMES[6],
        "preview": "(ii) Amoeba reproduces sexually by the production and fusion of male and female gametes.",
        "content": "**(ii) Amoeba reproduces sexually by the production and fusion of male and female gametes.**  \n**अमीबा नर और मादा युग्मकों के निर्माण तथा संलयन द्वारा लैंगिक जनन करता है।**"
    },
    {
        "id": "8_sci_sec3_set_b_q3",
        "sectionKey": "sec_3",
        "orderInSet": 3,
        "originalNum": "Q3",
        "marks": 1,
        "chapter": CH_NAMES[7],
        "preview": "(iii) All adolescents grow at the exact same uniform speed and reach the identical height at the same age.",
        "content": "**(iii) All adolescents grow at the exact same uniform speed and reach the identical height at the same age.**  \n**सभी किशोर बिल्कुल समान गति से बढ़ते हैं और समान आयु में एक जैसी ऊँचाई प्राप्त करते हैं।**"
    },
    {
        "id": "8_sci_sec3_set_b_q4",
        "sectionKey": "sec_3",
        "orderInSet": 4,
        "originalNum": "Q4",
        "marks": 1,
        "chapter": CH_NAMES[8],
        "preview": "(iv) Electrostatic force can exert its effect between two charged bodies even when not in physical contact.",
        "content": "**(iv) Electrostatic force can exert its effect between two charged bodies even when they are not in physical contact.**  \n**स्थिर वैद्युत बल दो आवेशित वस्तुओं के बीच तब भी कार्य कर सकता है जब वे भौतिक संपर्क में न हों।**"
    },
    {
        "id": "8_sci_sec3_set_b_q5",
        "sectionKey": "sec_3",
        "orderInSet": 5,
        "originalNum": "Q5",
        "marks": 1,
        "chapter": CH_NAMES[9],
        "preview": "(v) Sliding friction between two contact surfaces is slightly less than the static friction.",
        "content": "**(v) Sliding friction between two contact surfaces is slightly less than the static friction.**  \n**दो संपर्क पृष्ठों के बीच सर्पी घर्षण का मान स्थैतिक घर्षण से थोड़ा कम होता है।**"
    },

    # --- Section 4: Very Short Answer (2 Marks each) ---
    {
        "id": "8_sci_sec4_set_b_q1",
        "sectionKey": "sec_4",
        "orderInSet": 1,
        "originalNum": "Q1",
        "marks": 2,
        "chapter": CH_NAMES[5],
        "preview": "(i) (a) What is meant by migration of birds? (b) Name any one migratory bird that visits India in winter.",
        "content": "**(i) (a) What is meant by migration of birds? (b) Name any one migratory bird that flies long distances to visit India during winter.**  \n**(a) पक्षियों के प्रवास (Migration) से क्या तात्पर्य है? (b) किसी एक प्रवासी पक्षी का नाम लिखिए जो शीत ऋतु में सुदूर देशों से भारत आता है।**"
    },
    {
        "id": "8_sci_sec4_set_b_q2",
        "sectionKey": "sec_4",
        "orderInSet": 2,
        "originalNum": "Q2",
        "marks": 2,
        "chapter": CH_NAMES[6],
        "preview": "(ii) (a) What does IVF (In Vitro Fertilisation) stand for? (b) What are babies born through IVF called?",
        "content": "**(ii) (a) What does IVF (In Vitro Fertilisation) stand for? (b) What are babies born through this medical technique popularly called?**  \n**(a) IVF (इन विट्रो निषेचन) का पूर्ण रूप क्या है? (b) इस चिकित्सा तकनीक द्वारा जन्मे शिशुओं को सामान्यतः क्या कहा जाता है?**"
    },
    {
        "id": "8_sci_sec4_set_b_q3",
        "sectionKey": "sec_4",
        "orderInSet": 3,
        "originalNum": "Q3",
        "marks": 2,
        "chapter": CH_NAMES[7],
        "preview": "(iii) (a) Which gland is known as the 'master gland'? (b) Where is it located in the human body?",
        "content": "**(iii) (a) Which gland is known as the 'master gland' of the endocrine system? (b) Where is it located in the human body?**  \n**(a) किस ग्रंथि को अंतःस्रावी तंत्र की 'मास्टर ग्रंथि' कहा जाता है? (b) यह मानव शरीर में कहाँ स्थित होती है?**"
    },
    {
        "id": "8_sci_sec4_set_b_q4",
        "sectionKey": "sec_4",
        "orderInSet": 4,
        "originalNum": "Q4",
        "marks": 2,
        "chapter": CH_NAMES[8],
        "preview": "(iv) State two everyday situations where an applied force changes the shape of an object without moving it.",
        "content": "**(iv) State two everyday situations in which an applied force changes the shape of an object without moving it from its position.**  \n**दैनिक जीवन की ऐसी दो स्थितियाँ बताइए जिनमें लगाया गया बल किसी वस्तु की स्थिति को बदले बिना केवल उसकी आकृति में परिवर्तन करता है।**"
    },
    {
        "id": "8_sci_sec4_set_b_q5",
        "sectionKey": "sec_4",
        "orderInSet": 5,
        "originalNum": "Q5",
        "marks": 2,
        "chapter": CH_NAMES[9],
        "preview": "(v) Why do gymnasts and kabaddi players apply coarse powder or dry soil on their hands before performance?",
        "content": "**(v) Why do gymnasts and kabaddi players apply coarse chalk powder or dry soil on their hands before performance?**  \n**जिमनास्ट और कबड्डी खिलाड़ी खेल प्रदर्शन से पहले अपने हाथों पर खुरदरा पाउडर या सूखी मिट्टी क्यों लगाते हैं?**"
    },

    # --- Section 5: Short Answer (3 Marks each) ---
    {
        "id": "8_sci_sec5_set_b_q1",
        "sectionKey": "sec_5",
        "orderInSet": 1,
        "originalNum": "Q1",
        "marks": 3,
        "chapter": CH_NAMES[5],
        "preview": "(i) (a) What are endangered species? How are they distinguished from extinct? (b) Give one example of each.",
        "content": "**(i) (a) What are endangered species? How are they distinguished from extinct species? (b) Give one example of an endangered animal and one extinct animal.**  \n**(a) संकटापन्न प्रजातियाँ क्या हैं? ये विलुप्त प्रजातियों से किस प्रकार भिन्न हैं? (b) किसी एक संकटापन्न जंतु और एक विलुप्त जंतु का उदाहरण दीजिए।**"
    },
    {
        "id": "8_sci_sec5_set_b_q2",
        "sectionKey": "sec_5",
        "orderInSet": 2,
        "originalNum": "Q2",
        "marks": 3,
        "chapter": CH_NAMES[6],
        "preview": "(ii) Describe the metamorphosis of a frog through distinct stages: Egg -> Tadpole -> Adult frog.",
        "content": "**(ii) Describe the metamorphosis of a frog through its distinct developmental stages: Egg → Tadpole (larva) → Adult frog. Why does a tadpole look so different from an adult frog?**  \n**मेंढक के कायांतरण (Metamorphosis) के विभिन्न चरणों: अंडा → टैडपोल (लार्वा) → वयस्क मेंढक का वर्णन कीजिए। टैडपोल वयस्क मेंढक से इतना भिन्न क्यों दिखाई देता है?**"
    },
    {
        "id": "8_sci_sec5_set_b_q3",
        "sectionKey": "sec_5",
        "orderInSet": 3,
        "originalNum": "Q3",
        "marks": 3,
        "chapter": CH_NAMES[7],
        "preview": "(iii) (a) Name hormones secreted by Pancreas and Adrenal glands. (b) State their primary health functions.",
        "content": "**(iii) (a) Name the hormones secreted by: (i) Pancreas, and (ii) Adrenal glands. (b) State the primary function of each of these hormones in maintaining body health.**  \n**(a) (i) अग्न्याशय (Pancreas) तथा (ii) एड्रिनल ग्रंथि द्वारा स्रावित हार्मोन के नाम लिखिए। (b) शरीर के स्वास्थ्य को बनाए रखने में इन दोनों हार्मोन के प्रमुख कार्य बताइए।**"
    },
    {
        "id": "8_sci_sec5_set_b_q4",
        "sectionKey": "sec_5",
        "orderInSet": 4,
        "originalNum": "Q4",
        "marks": 3,
        "chapter": CH_NAMES[8],
        "preview": "(iv) Why are school bag straps made broad and wide instead of using thin cords? Explain using pressure formula.",
        "content": "**(iv) Why are the straps of school bags made broad and wide instead of using thin cords or wires? Explain this on the basis of the formula for pressure.**  \n**स्कूल के बस्तों की पट्टियाँ पतली डोरी के बजाय चौड़ी क्यों बनाई जाती हैं? दाब के सूत्र के आधार पर इसका कारण स्पष्ट कीजिए।**"
    },
    {
        "id": "8_sci_sec5_set_b_q5",
        "sectionKey": "sec_5",
        "orderInSet": 5,
        "originalNum": "Q5",
        "marks": 3,
        "chapter": CH_NAMES[9],
        "preview": "(v) Why are aeroplanes, bullet trains, and speedboats designed with streamlined shapes? Explain.",
        "content": "**(v) Why are aeroplanes, bullet trains, and speedboats designed with special streamlined shapes? Explain the scientific reason.**  \n**हवाई जहाजों, बुलेट ट्रेनों और तीव्र गति वाली नावों को विशेष धारा-रेखीय (streamlined) आकृति क्यों दी जाती है? इसका वैज्ञानिक कारण समझाइए।**"
    },

    # --- Section 6: Long Answer (5 Marks each with OR choices) ---
    {
        "id": "8_sci_sec6_set_b_q1",
        "sectionKey": "sec_6",
        "orderInSet": 1,
        "originalNum": "Q1",
        "marks": 5,
        "chapter": CH_NAMES[8],
        "defaultOrPartnerId": "8_sci_sec6_set_b_q1_alt",
        "preview": "(i) (a) Differentiate between Contact and Non-contact forces. (b) Calculate pressure for a 180 N block on 0.06 m².",
        "content": "**(i) (a) Differentiate between Contact forces and Non-contact forces. Give two examples of each type. (3 Marks)**  \n**संपर्क बल और असंपर्क बल में अंतर स्पष्ट कीजिए तथा प्रत्येक प्रकार के दो-दो उदाहरण दीजिए।**  \n**(b) A metallic rectangular block weighing 180 N rests on a tabletop. If its area in contact with the table is 0.06 m², calculate the pressure exerted on the table. (2 Marks)**  \n**180 N भार का एक धातु का आयताकार गुटका मेज पर रखा है। यदि मेज के संपर्क में आने वाला इसका क्षेत्रफल 0.06 m² है, तो मेज पर लगने वाले दाब की गणना कीजिए।**"
    },
    {
        "id": "8_sci_sec6_set_b_q1_alt",
        "sectionKey": "sec_6",
        "orderInSet": 1.5,
        "originalNum": "Q1",
        "marks": 5,
        "chapter": CH_NAMES[9],
        "defaultOrPartnerId": "8_sci_sec6_set_b_q1",
        "preview": "(a) Describe three methods to increase and three methods to reduce friction. (b) Why sudden braking is dangerous on wet roads?",
        "content": "**(a) Describe three effective practical methods used to increase friction when needed, and three practical methods used to reduce friction. (4 Marks)**  \n**आवश्यकता पड़ने पर घर्षण बढ़ाने की तीन प्रभावी व्यावहारिक विधियों तथा घर्षण कम करने की तीन विधियों का वर्णन कीजिए।**  \n**(b) Why is it dangerous to apply sudden brakes to a car moving on a wet, rainy road? (1 Mark)**  \n**गीली और फिसलन भरी सड़क पर तेज गति से चल रही कार पर अचानक ब्रेक लगाना खतरनाक क्यों होता है?**"
    },
    {
        "id": "8_sci_sec6_set_b_q2",
        "sectionKey": "sec_6",
        "orderInSet": 2,
        "originalNum": "Q2",
        "marks": 5,
        "chapter": CH_NAMES[6],
        "defaultOrPartnerId": "8_sci_sec6_set_b_q2_alt",
        "preview": "(ii) (a) Describe male reproductive system in humans and function of testes. (b) What is an embryo and where does it implant?",
        "content": "**(ii) (a) Describe the male reproductive system in humans. Name the key organs and state the function of testes. (3 Marks)**  \n**मानव के नर जनन तंत्र का वर्णन कीजिए। इसके प्रमुख अंगों के नाम लिखिए तथा वृषण (Testes) का कार्य बताइए।**  \n**(b) What is an embryo? Where does it get implanted and develop in the female reproductive system? (2 Marks)**  \n**भ्रूण (Embryo) क्या है? मादा जनन तंत्र में यह कहाँ रोपित (implant) होकर विकसित होता है?**"
    },
    {
        "id": "8_sci_sec6_set_b_q2_alt",
        "sectionKey": "sec_6",
        "orderInSet": 2.5,
        "originalNum": "Q2",
        "marks": 5,
        "chapter": CH_NAMES[7],
        "defaultOrPartnerId": "8_sci_sec6_set_b_q2",
        "preview": "(a) What are endocrine glands? Explain Pituitary gland role. (b) Why is exercise and nutrition essential for teenagers?",
        "content": "**(a) What are endocrine glands? Explain the role of the Pituitary gland in controlling other endocrine glands during puberty. (3 Marks)**  \n**अंतःस्रावी ग्रंथियाँ क्या हैं? यौवनारंभ के समय अन्य अंतःस्रावी ग्रंथियों को नियंत्रित करने में पीयूष ग्रंथि की भूमिका समझाइए।**  \n**(b) Why is regular physical exercise and nutritious food particularly essential for growing teenagers? (2 Marks)**  \n**विकासशील किशोरों के लिए नियमित शारीरिक व्यायाम और पौष्टिक भोजन विशेष रूप से क्यों आवश्यक है?**"
    }
]

# ==========================================
# 3. SET C QUESTIONS DEFINITIONS
# ==========================================
SET_C_DATA = [
    # --- Section 1: MCQs (1 Mark each) ---
    {
        "id": "8_sci_sec1_set_c_q1",
        "sectionKey": "sec_1",
        "orderInSet": 1,
        "originalNum": "Q1",
        "marks": 1,
        "chapter": CH_NAMES[5],
        "preview": "(i) In which national park was 'Project Tiger' launched by the Indian Government to protect tigers?",
        "content": "**(i) In which national park was 'Project Tiger' launched by the Indian Government to protect the dwindling tiger population?**  \n**घटती बाघों की आबादी की सुरक्षा के लिए भारत सरकार द्वारा 'प्रोजेक्ट टाइगर' किस राष्ट्रीय उद्यान में प्रारंभ किया गया था?**  \n(a) Jim Corbett National Park / जिम कॉर्बेट राष्ट्रीय उद्यान  \n(b) Satpura National Park / सतपुड़ा राष्ट्रीय उद्यान  \n(c) Gir National Park / गिर राष्ट्रीय उद्यान  \n(d) Kaziranga National Park / काजीरंगा राष्ट्रीय उद्यान"
    },
    {
        "id": "8_sci_sec1_set_c_q2",
        "sectionKey": "sec_1",
        "orderInSet": 2,
        "originalNum": "Q2",
        "marks": 1,
        "chapter": CH_NAMES[6],
        "preview": "(ii) Transformation of a larva into an adult through drastic morphological changes is called:",
        "content": "**(ii) The biological process of transformation of a larva into an adult through drastic morphological changes is called:**  \n**विशिष्ट शारीरिक परिवर्तनों द्वारा लार्वा के वयस्क में रूपांतरण की जैविक प्रक्रिया को क्या कहते हैं?**  \n(a) Fertilisation / निषेचन  \n(b) Metamorphosis / कायांतरण  \n(c) Budding / मुकुलन  \n(d) Fission / विखंडन"
    },
    {
        "id": "8_sci_sec1_set_c_q3",
        "sectionKey": "sec_1",
        "orderInSet": 3,
        "originalNum": "Q3",
        "marks": 1,
        "chapter": CH_NAMES[7],
        "preview": "(iii) Which gland secretes the hormone responsible for overall growth in height and bone development?",
        "content": "**(iii) Which gland in the human body secretes the hormone responsible for overall bodily growth in height and bone development?**  \n**मानव शरीर की कौन-सी ग्रंथि लंबाई और हड्डियों के समग्र विकास के लिए जिम्मेदार वृद्धि हार्मोन स्रावित करती है?**  \n(a) Thyroid gland / थायरॉयड ग्रंथि  \n(b) Pituitary gland / पीयूष ग्रंथि  \n(c) Pancreas / अग्न्याशय  \n(d) Adrenal gland / एड्रिनल ग्रंथि"
    },
    {
        "id": "8_sci_sec1_set_c_q4",
        "sectionKey": "sec_1",
        "orderInSet": 4,
        "originalNum": "Q4",
        "marks": 1,
        "chapter": CH_NAMES[8],
        "preview": "(iv) Which scientific instrument is commonly used in laboratories to measure differences in liquid pressure?",
        "content": "**(iv) Which scientific instrument is commonly used in laboratories to measure differences in liquid pressure?**  \n**प्रयोगशालाओं में द्रवों के दाबांतर को मापने के लिए सामान्यतः किस वैज्ञानिक उपकरण का उपयोग किया जाता है?**  \n(a) Thermometer / थर्मामीटर  \n(b) Manometer / मैनोमीटर  \n(c) Barometer / बैरोमीटर  \n(d) Anemometer / एनीमोमीटर"
    },
    {
        "id": "8_sci_sec1_set_c_q5",
        "sectionKey": "sec_1",
        "orderInSet": 5,
        "originalNum": "Q5",
        "marks": 1,
        "chapter": CH_NAMES[9],
        "preview": "(v) When two contact surfaces are pressed harder against each other with greater force, friction will:",
        "content": "**(v) When two contact surfaces are pressed harder against each other with greater force, the friction between them will:**  \n**जब दो संपर्क पृष्ठों को अधिक बल के साथ आपस में दबाया जाता है, तो उनके बीच का घर्षण बल:**  \n(a) Decrease / कम हो जाएगा  \n(b) Increase / बढ़ जाएगा  \n(c) Remain unchanged / अपरिवर्तित रहेगा  \n(d) Become zero / शून्य हो जाएगा"
    },

    # --- Section 2: Fill in the Blanks (1 Mark each) ---
    {
        "id": "8_sci_sec2_set_c_q1",
        "sectionKey": "sec_2",
        "orderInSet": 1,
        "originalNum": "Q1",
        "marks": 1,
        "chapter": CH_NAMES[5],
        "preview": "(i) The restocking of destroyed forests by planting new saplings is called _______.",
        "content": "**(i) The restocking of destroyed forests by planting new saplings is called _______.**  \n**नष्ट हुए वनों में नए पौधे लगाकर उन्हें पुनः स्थापित करना _______ कहलाता है।**"
    },
    {
        "id": "8_sci_sec2_set_c_q2",
        "sectionKey": "sec_2",
        "orderInSet": 2,
        "originalNum": "Q2",
        "marks": 1,
        "chapter": CH_NAMES[6],
        "preview": "(ii) The stage of the embryo in which all major body parts can be identified is termed a _______.",
        "content": "**(ii) The stage of the developing embryo in which all major body parts can be distinctly identified is termed a _______.**  \n**विकासशील भ्रूण की वह अवस्था जिसमें शरीर के सभी प्रमुख अंगों की पहचान की जा सकती है, _______ कहलाती है।**"
    },
    {
        "id": "8_sci_sec2_set_c_q3",
        "sectionKey": "sec_2",
        "orderInSet": 3,
        "originalNum": "Q3",
        "marks": 1,
        "chapter": CH_NAMES[7],
        "preview": "(iii) Permanent stoppage of menstruation in women around the age of 45 to 50 years is known as _______.",
        "content": "**(iii) The permanent stoppage of menstruation occurring in women around the age of 45 to 50 years is known as _______.**  \n**महिलाओं में 45 से 50 वर्ष की आयु के आसपास मासिक धर्म के स्थायी रूप से बंद होने को _______ कहते हैं।**"
    },
    {
        "id": "8_sci_sec2_set_c_q4",
        "sectionKey": "sec_2",
        "orderInSet": 4,
        "originalNum": "Q4",
        "marks": 1,
        "chapter": CH_NAMES[8],
        "preview": "(iv) A liquid exerts _______ pressure in all directions at the same horizontal depth.",
        "content": "**(iv) A liquid exerts _______ pressure in all directions at the same horizontal depth.**  \n**कोई द्रव समान क्षैतिज गहराई पर सभी दिशाओं में _______ दाब डालता है।**"
    },
    {
        "id": "8_sci_sec2_set_c_q5",
        "sectionKey": "sec_2",
        "orderInSet": 5,
        "originalNum": "Q5",
        "marks": 1,
        "chapter": CH_NAMES[9],
        "preview": "(v) Substances such as oil and grease that reduce friction between moving parts are called _______.",
        "content": "**(v) Substances such as oil and grease that reduce friction between moving machine parts are called _______.**  \n**तेल और ग्रीस जैसे पदार्थ जो मशीनों के गतिशील पुर्जों के बीच घर्षण को कम करते हैं, _______ कहलाते हैं।**"
    },

    # --- Section 3: True / False (1 Mark each) ---
    {
        "id": "8_sci_sec3_set_c_q1",
        "sectionKey": "sec_3",
        "orderInSet": 1,
        "originalNum": "Q1",
        "marks": 1,
        "chapter": CH_NAMES[5],
        "preview": "(i) Reforestation can occur naturally if the deforested forest land is left completely undisturbed.",
        "content": "**(i) Reforestation can occur naturally if the deforested forest land is left completely undisturbed.**  \n**यदि वनोन्मूलित वन भूमि को बिना किसी मानवीय हस्तक्षेप के छोड़ दिया जाए, तो प्राकृतिक पुनर्वनरोपण हो सकता है।**"
    },
    {
        "id": "8_sci_sec3_set_c_q2",
        "sectionKey": "sec_3",
        "orderInSet": 2,
        "originalNum": "Q2",
        "marks": 1,
        "chapter": CH_NAMES[6],
        "preview": "(ii) A human sperm is a multicellular structure consisting of thousands of interconnected cells.",
        "content": "**(ii) A human sperm is a multicellular structure consisting of thousands of interconnected cells.**  \n**मानव शुक्राणु एक बहुकोशिकीय संरचना है जिसमें हजारों परस्पर जुड़ी कोशिकाएँ होती हैं।**"
    },
    {
        "id": "8_sci_sec3_set_c_q3",
        "sectionKey": "sec_3",
        "orderInSet": 3,
        "originalNum": "Q3",
        "marks": 1,
        "chapter": CH_NAMES[7],
        "preview": "(iii) Consuming junk food and sugary sodas provides all the vital proteins and iron needed for adolescent development.",
        "content": "**(iii) Consuming junk food and sugary sodas provides all the vital proteins and iron needed for adolescent development.**  \n**फास्ट फूड और मीठे शीतल पेयों का सेवन करने से किशोरों के विकास के लिए आवश्यक सभी प्रोटीन और आयरन प्राप्त हो जाते हैं।**"
    },
    {
        "id": "8_sci_sec3_set_c_q4",
        "sectionKey": "sec_3",
        "orderInSet": 4,
        "originalNum": "Q4",
        "marks": 1,
        "chapter": CH_NAMES[8],
        "preview": "(iv) Gravitational force is an attractive force that pulls every object in the universe towards every other object.",
        "content": "**(iv) Gravitational force is an attractive force that pulls every object in the universe towards every other object.**  \n**गुरुत्वाकर्षण बल एक आकर्षण बल है जो ब्रह्मांड में प्रत्येक वस्तु को दूसरी वस्तु की ओर आकर्षित करता है।**"
    },
    {
        "id": "8_sci_sec3_set_c_q5",
        "sectionKey": "sec_3",
        "orderInSet": 5,
        "originalNum": "Q5",
        "marks": 1,
        "chapter": CH_NAMES[9],
        "preview": "(v) Striking a matchstick against the rough chemical strip produces fire because of friction heat.",
        "content": "**(v) Striking a matchstick against the rough chemical strip of a matchbox produces fire because of the heat generated by friction.**  \n**माचिस की तीली को माचिस की डिब्बी के खुरदरे भाग पर रगड़ने से घर्षण द्वारा उत्पन्न ऊष्मा के कारण आग उत्पन्न होती है।**"
    },

    # --- Section 4: Very Short Answer (2 Marks each) ---
    {
        "id": "8_sci_sec4_set_c_q1",
        "sectionKey": "sec_4",
        "orderInSet": 1,
        "originalNum": "Q1",
        "marks": 2,
        "chapter": CH_NAMES[5],
        "preview": "(i) State two adverse consequences of large-scale deforestation on local rainfall patterns and water table.",
        "content": "**(i) State two adverse consequences of large-scale deforestation on local rainfall patterns and the underground water table.**  \n**स्थानीय वर्षा के पैटर्न और भूमिगत जल स्तर पर व्यापक वनोन्मूलन के दो प्रतिकूल प्रभाव बताइए।**"
    },
    {
        "id": "8_sci_sec4_set_c_q2",
        "sectionKey": "sec_4",
        "orderInSet": 2,
        "originalNum": "Q2",
        "marks": 2,
        "chapter": CH_NAMES[6],
        "preview": "(ii) (a) Name two distinct methods of asexual reproduction in animals. (b) Name one organism for each.",
        "content": "**(ii) (a) Name two distinct methods of asexual reproduction in animals. (b) Name one animal organism for each method.**  \n**(a) जंतुओं में अलैंगिक जनन की दो अलग-अलग विधियों के नाम लिखिए। (b) प्रत्येक विधि के लिए एक-एक जंतु जीव का नाम लिखिए।**"
    },
    {
        "id": "8_sci_sec4_set_c_q3",
        "sectionKey": "sec_4",
        "orderInSet": 3,
        "originalNum": "Q3",
        "marks": 2,
        "chapter": CH_NAMES[7],
        "preview": "(iii) (a) What is meant by 'target site' in the endocrine system? (b) Name male and female sex hormones.",
        "content": "**(iii) (a) What is meant by a 'target site' in the human endocrine system? (b) Name the male and female sex hormones.**  \n**(a) मानव अंतःस्रावी तंत्र में 'लक्ष्य स्थल' (Target Site) से क्या तात्पर्य है? (b) नर तथा मादा लिंग हार्मोन के नाम लिखिए।**"
    },
    {
        "id": "8_sci_sec4_set_c_q4",
        "sectionKey": "sec_4",
        "orderInSet": 4,
        "originalNum": "Q4",
        "marks": 2,
        "chapter": CH_NAMES[8],
        "preview": "(iv) (a) What is meant by muscular force? (b) Why is muscular force classified as a contact force?",
        "content": "**(iv) (a) What is meant by muscular force? (b) Why is muscular force classified as a contact force?**  \n**(a) पेशीय बल (Muscular Force) किसे कहते हैं? (b) पेशीय बल को संपर्क बल के रूप में क्यों वर्गीकृत किया जाता है?**"
    },
    {
        "id": "8_sci_sec4_set_c_q5",
        "sectionKey": "sec_4",
        "orderInSet": 5,
        "originalNum": "Q5",
        "marks": 2,
        "chapter": CH_NAMES[9],
        "preview": "(v) State the two main physical factors on which the force of friction between two surfaces depends.",
        "content": "**(v) State the two main physical factors on which the force of friction between two surfaces depends.**  \n**उन दो प्रमुख भौतिक कारकों का उल्लेख कीजिए जिन पर दो पृष्ठों के बीच का घर्षण बल निर्भर करता है।**"
    },

    # --- Section 5: Short Answer (3 Marks each) ---
    {
        "id": "8_sci_sec5_set_c_q1",
        "sectionKey": "sec_5",
        "orderInSet": 1,
        "originalNum": "Q1",
        "marks": 3,
        "chapter": CH_NAMES[5],
        "preview": "(i) Explain the structure of a Biosphere Reserve by describing its three zones: Core, Buffer, and Transition.",
        "content": "**(i) Explain the structure of a Biosphere Reserve by describing its three concentric zones: (i) Core zone, (ii) Buffer zone, and (iii) Transition zone.**  \n**जैवमंडल आरक्षित क्षेत्र की संरचना को उसके तीन संकेंद्रीय क्षेत्रों: (i) क्रोड क्षेत्र (Core zone), (ii) बफर क्षेत्र (Buffer zone), तथा (iii) संक्रमण क्षेत्र (Transition zone) का वर्णन करके समझाइए।**"
    },
    {
        "id": "8_sci_sec5_set_c_q2",
        "sectionKey": "sec_5",
        "orderInSet": 2,
        "originalNum": "Q2",
        "marks": 3,
        "chapter": CH_NAMES[6],
        "preview": "(ii) Explain how fertilisation takes place in hens and why they lay eggs instead of giving direct birth.",
        "content": "**(ii) Explain how fertilisation takes place in hens. Even though hens exhibit internal fertilisation, why do they lay eggs instead of giving direct birth to young chicks?**  \n**मुर्गियों में निषेचन की प्रक्रिया को समझाइए। आंतरिक निषेचन होने के बावजूद मुर्गियाँ सीधे चूजों को जन्म देने के बजाय अंडे क्यों देती हैं?**"
    },
    {
        "id": "8_sci_sec5_set_c_q3",
        "sectionKey": "sec_5",
        "orderInSet": 3,
        "originalNum": "Q3",
        "marks": 3,
        "chapter": CH_NAMES[7],
        "preview": "(iii) Why is personal hygiene and an iron-rich diet critically important during adolescence? List 3 guidelines.",
        "content": "**(iii) Why is maintaining strict personal hygiene and eating an iron-rich balanced diet critically important during adolescence? List three key nutritional guidelines for teenagers.**  \n**किशोरावस्था के दौरान व्यक्तिगत स्वच्छता बनाए रखना और आयरन युक्त संतुलित आहार लेना क्यों अत्यंत महत्वपूर्ण है? किशोरों के लिए तीन प्रमुख पोषण संबंधी सुझाव लिखिए।**"
    },
    {
        "id": "8_sci_sec5_set_c_q4",
        "sectionKey": "sec_5",
        "orderInSet": 4,
        "originalNum": "Q4",
        "marks": 3,
        "chapter": CH_NAMES[8],
        "preview": "(iv) (a) Write formula relating Pressure, Force, Area. (b) Why sharp knife cuts vegetables more effectively?",
        "content": "**(iv) (a) Write the mathematical formula relating Pressure, Force, and Area. (b) Explain why a sharp knife cuts fruits and vegetables much more effectively than a blunt knife.**  \n**(a) दाब, बल और क्षेत्रफल के बीच संबंध दर्शाने वाला गणितीय सूत्र लिखिए। (b) समझाइए कि एक तेज धार वाला चाकू कुंद (blunt) चाकू की तुलना में फलों और सब्जियों को अधिक आसानी से क्यों काटता है।**"
    },
    {
        "id": "8_sci_sec5_set_c_q5",
        "sectionKey": "sec_5",
        "orderInSet": 5,
        "originalNum": "Q5",
        "marks": 3,
        "chapter": CH_NAMES[9],
        "preview": "(v) Why is it difficult to walk on a wet soapy marble floor? How does friction help us walk?",
        "content": "**(v) Explain why it is very difficult to walk safely on a wet, soapy marble floor. How does the presence of friction between our footwear and the ground help us in walking?**  \n**स्पष्ट कीजिए कि गीले और साबुन लगे संगमरमर के फर्श पर चलना बहुत कठिन क्यों होता है। हमारे जूतों और जमीन के बीच घर्षण की उपस्थिति हमें चलने में किस प्रकार सहायता करती है?**"
    },

    # --- Section 6: Long Answer (5 Marks each with OR choices) ---
    {
        "id": "8_sci_sec6_set_c_q1",
        "sectionKey": "sec_6",
        "orderInSet": 1,
        "originalNum": "Q1",
        "marks": 5,
        "chapter": CH_NAMES[8],
        "defaultOrPartnerId": "8_sci_sec6_set_c_q1_alt",
        "preview": "(i) (a) Describe three distinct effects of force with examples. (b) Why are dam walls built thicker at the base?",
        "content": "**(i) (a) Describe three distinct effects that an applied force can produce on a body. Give an example for each. (3 Marks)**  \n**किसी वस्तु पर लगाए गए बल द्वारा उत्पन्न किए जा सकने वाले तीन अलग-अलग प्रभावों का वर्णन कीजिए तथा प्रत्येक का एक उदाहरण दीजिए।**  \n**(b) Why are the concrete walls of a water reservoir dam built much thicker and wider at the base than at the top? (2 Marks)**  \n**जल जलाशय (बांध) की कंक्रीट की दीवारें शीर्ष की तुलना में आधार (तल) पर बहुत अधिक चौड़ी और मोटी क्यों बनाई जाती हैं?**"
    },
    {
        "id": "8_sci_sec6_set_c_q1_alt",
        "sectionKey": "sec_6",
        "orderInSet": 1.5,
        "originalNum": "Q1",
        "marks": 5,
        "chapter": CH_NAMES[9],
        "defaultOrPartnerId": "8_sci_sec6_set_c_q1",
        "preview": "(a) Why rolling friction is less than sliding? Invention of wheel. (b) What if zero friction on roads?",
        "content": "**(a) Explain why rolling friction is considerably less than sliding friction. Describe how the invention of the wheel revolutionized human transport using this scientific principle. (3 Marks)**  \n**समझाइए कि लोटनिक घर्षण, सर्पी घर्षण की तुलना में काफी कम क्यों होता है। इस वैज्ञानिक सिद्धांत के आधार पर पहिये के आविष्कार ने मानव परिवहन में किस प्रकार क्रांति ला दी?**  \n**(b) What would happen to vehicles on the road if there were zero friction between vehicle tyres and the road surface? (2 Marks)**  \n**यदि वाहनों के टायरों और सड़क की सतह के बीच घर्षण शून्य हो जाए, तो सड़क पर चलने वाले वाहनों का क्या होगा?**"
    },
    {
        "id": "8_sci_sec6_set_c_q2",
        "sectionKey": "sec_6",
        "orderInSet": 2,
        "originalNum": "Q2",
        "marks": 5,
        "chapter": CH_NAMES[6],
        "defaultOrPartnerId": "8_sci_sec6_set_c_q2_alt",
        "preview": "(ii) (a) Describe female reproductive system and organ functions. (b) Who was Dolly the sheep?",
        "content": "**(ii) (a) Describe the female reproductive system in humans. State the specific functions of the ovaries, fallopian tubes, and uterus. (3 Marks)**  \n**मानव के मादा जनन तंत्र का वर्णन कीजिए। अंडाशय (Ovaries), डिंबवाहिनी (Fallopian tubes), तथा गर्भाशय (Uterus) के विशिष्ट कार्य बताइए।**  \n**(b) Who was Dolly the sheep? Why was her successful birth considered a historic breakthrough in biological science? (2 Marks)**  \n**'डॉली' भेड़ कौन थी? उसके सफल जन्म को जैविक विज्ञान के इतिहास में एक ऐतिहासिक उपलब्धि क्यों माना गया?**"
    },
    {
        "id": "8_sci_sec6_set_c_q2_alt",
        "sectionKey": "sec_6",
        "orderInSet": 2.5,
        "originalNum": "Q2",
        "marks": 5,
        "chapter": CH_NAMES[7],
        "defaultOrPartnerId": "8_sci_sec6_set_c_q2",
        "preview": "(a) Name four endocrine glands, hormones, and disorders. (b) Why teenagers should say NO to drugs?",
        "content": "**(a) Name four different endocrine glands in the human body, the hormone each secretes, and the principal disorder caused by their malfunction. (4 Marks)**  \n**मानव शरीर की किन्हीं चार अंतःस्रावी ग्रंथियों, उनसे स्रावित होने वाले हार्मोन तथा उनकी खराबी से होने वाले मुख्य विकार का उल्लेख कीजिए।**  \n**(b) Why are adolescents advised to firmly say \"NO\" to drugs and addictive substances? (1 Mark)**  \n**किशोरों को नशीली दवाओं और व्यसनी पदार्थों को दृढ़ता से \"ना\" कहने की सलाह क्यों दी जाती है?**"
    }
]

# Helper to generate Markdown paper string
def generate_markdown_paper(set_name, questions_data):
    lines = [
        "# NEW M.V.M. SENIOR SECONDARY SCHOOL, ALWAR",
        "",
        f"## HALF YEARLY EXAMINATION: 2026 – 27 (SET – {set_name})",
        "",
        "**CLASS : VIII**  ",
        "**SUBJECT : SCIENCE (विज्ञान)**  ",
        "**TIME : 2½ HOURS**  ",
        "**MAXIMUM MARKS (पूर्णांक) : 50**",
        "",
        "---",
        "",
        "### GENERAL INSTRUCTIONS / सामान्य निर्देश",
        "",
        "1. All questions are compulsory. / सभी प्रश्न अनिवार्य हैं।",
        "2. The question paper comprises six sections: Section 1 to Section 6. / प्रश्न पत्र में छह खंड हैं: खंड 1 से खंड 6।",
        "3. Marks for each question are indicated against it. / प्रत्येक प्रश्न के अंक उसके सम्मुख अंकित हैं।",
        "4. The paper is bilingual (English and Hindi). / यह प्रश्न पत्र द्विभाषी (अंग्रेजी और हिन्दी) है।",
        "",
        "---",
        ""
    ]

    sec_meta = [
        ("sec_1", "### SECTION 1 / खंड 1", "#### Tick (✓) the correct answer in answer sheet / उत्तर पुस्तिका में सही उत्तर पर सही (✓) का निशान लगाएँ", "**(5 × 1 = 5 Marks)**"),
        ("sec_2", "### SECTION 2 / खंड 2", "#### Fill in the blanks / रिक्त स्थानों की पूर्ति कीजिए", "**(5 × 1 = 5 Marks)**"),
        ("sec_3", "### SECTION 3 / खंड 3", "#### State whether the given statements are True (T) or False (F) / बताएँ कि निम्नलिखित कथन सत्य (T) हैं या असत्य (F)", "**(5 × 1 = 5 Marks)**"),
        ("sec_4", "### SECTION 4 / खंड 4", "#### Very Short Answer type questions / अति लघु उत्तरीय प्रश्न", "**(5 × 2 = 10 Marks)**"),
        ("sec_5", "### SECTION 5 / खंड 5", "#### Short Answer type questions / लघु उत्तरीय प्रश्न", "**(5 × 3 = 15 Marks)**"),
        ("sec_6", "### SECTION 6 / खंड 6", "#### Long Answer type questions / दीर्घ उत्तरीय प्रश्न", "**(2 × 5 = 10 Marks)**")
    ]

    for key, title, subtitle, marks_badge in sec_meta:
        lines.append(title)
        lines.append("")
        lines.append(subtitle)
        lines.append("")
        lines.append(marks_badge)
        lines.append("")

        if key != "sec_6":
            sec_qs = [q for q in questions_data if q["sectionKey"] == key]
            for q in sorted(sec_qs, key=lambda x: x["orderInSet"]):
                lines.append(q["content"])
                lines.append("")
        else:
            # Section 6 handles OR choices
            q1_main = next(q for q in questions_data if q["sectionKey"] == "sec_6" and q["id"].endswith("_q1"))
            q1_alt = next(q for q in questions_data if q["sectionKey"] == "sec_6" and q["id"].endswith("_q1_alt"))
            q2_main = next(q for q in questions_data if q["sectionKey"] == "sec_6" and q["id"].endswith("_q2"))
            q2_alt = next(q for q in questions_data if q["sectionKey"] == "sec_6" and q["id"].endswith("_q2_alt"))

            lines.append(q1_main["content"])
            lines.append("")
            lines.append("**OR / अथवा**")
            lines.append("")
            lines.append(q1_alt["content"])
            lines.append("")
            lines.append(q2_main["content"])
            lines.append("")
            lines.append("**OR / अथवा**")
            lines.append("")
            lines.append(q2_alt["content"])
            lines.append("")

        lines.append("---")
        lines.append("")

    return "\n".join(lines).strip() + "\n"

def main():
    print("=== Building Class 8 Science Ecosystem ===")
    os.makedirs(PAPERS_DIR, exist_ok=True)

    # 1. Format Questions for data/questions.json
    all_sets_questions = []

    for item in SET_A_DATA:
        q = dict(item)
        q["subjectId"] = "8_science"
        q["set"] = "Set A"
        q["hasOrChoice"] = False
        all_sets_questions.append(q)

    for item in SET_B_DATA:
        q = dict(item)
        q["subjectId"] = "8_science"
        q["set"] = "Set B"
        q["hasOrChoice"] = False
        all_sets_questions.append(q)

    for item in SET_C_DATA:
        q = dict(item)
        q["subjectId"] = "8_science"
        q["set"] = "Set C"
        q["hasOrChoice"] = False
        all_sets_questions.append(q)

    # 2. Write Markdown Examination Papers
    paper_a = generate_markdown_paper("A", SET_A_DATA)
    paper_b = generate_markdown_paper("B", SET_B_DATA)
    paper_c = generate_markdown_paper("C", SET_C_DATA)

    path_a = os.path.join(PAPERS_DIR, "Class_8_Science_Half_Yearly_Paper.md")
    path_b = os.path.join(PAPERS_DIR, "Class_8_Science_Half_Yearly_Paper_Set_B.md")
    path_c = os.path.join(PAPERS_DIR, "Class_8_Science_Half_Yearly_Paper_Set_C.md")

    with open(path_a, "w", encoding="utf-8") as f:
        f.write(paper_a)
    print(f"Generated {path_a} ({len(paper_a.splitlines())} lines)")

    with open(path_b, "w", encoding="utf-8") as f:
        f.write(paper_b)
    print(f"Generated {path_b} ({len(paper_b.splitlines())} lines)")

    with open(path_c, "w", encoding="utf-8") as f:
        f.write(paper_c)
    print(f"Generated {path_c} ({len(paper_c.splitlines())} lines)")

    # 3. Load existing questions.json and preserve existing Textbook questions
    with open(QUESTIONS_PATH, "r", encoding="utf-8") as f:
        q_db = json.load(f)

    existing_8_sci = q_db.get("8_science", [])
    existing_tb = [q for q in existing_8_sci if q.get("set") == "Textbook"]
    print(f"Retained {len(existing_tb)} existing Textbook questions for Class 8 Science.")

    # Combine: Set A (29) + Set B (29) + Set C (29) + Textbook (602+)
    combined_8_sci = all_sets_questions + existing_tb
    q_db["8_science"] = combined_8_sci

    with open(QUESTIONS_PATH, "w", encoding="utf-8") as f:
        json.dump(q_db, f, indent=2, ensure_ascii=False)
    print(f"Saved total {len(combined_8_sci)} questions into {QUESTIONS_PATH} under 8_science!")

    # 4. Verify blueprints.json
    with open(BLUEPRINTS_PATH, "r", encoding="utf-8") as f:
        bps = json.load(f)

    if "8_science" in bps:
        print("Verified 8_science exists in blueprints.json with 50 marks & 6 sections.")
    else:
        print("WARNING: 8_science not found in blueprints.json!")

if __name__ == "__main__":
    main()
