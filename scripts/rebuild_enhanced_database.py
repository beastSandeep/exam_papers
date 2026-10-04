import os, json, re
from chapter_classifier import determine_chapter, CHAPTERS_MAP
from extract_sample_questions import SAMPLE_QUESTIONS_7_MATHS

# Additional authentic questions for Class 6 Maths
EXTRA_QUESTIONS_6_MATHS = [
    # --- Section A: Formulas & Definitions ---
    {
        "id": "6m_extra_f1",
        "subjectId": "6_maths",
        "sectionKey": "sec_a",
        "set": "Sample Paper",
        "orderInSet": 1,
        "originalNum": "Q1(i)",
        "marks": 1,
        "chapter": "Ch 4: Playing with Numbers (संख्याओं के साथ खेलना)",
        "hasOrChoice": False,
        "preview": "Definition: Prime Number / अभाज्य संख्या",
        "content": "**Define a Prime Number. Write the smallest prime number.**  \n**अभाज्य संख्या (Prime number) की परिभाषा लिखिए तथा सबसे छोटी अभाज्य संख्या बताइए।**"
    },
    {
        "id": "6m_extra_f2",
        "subjectId": "6_maths",
        "sectionKey": "sec_a",
        "set": "Sample Paper",
        "orderInSet": 2,
        "originalNum": "Q1(ii)",
        "marks": 1,
        "chapter": "Ch 4: Playing with Numbers (संख्याओं के साथ खेलना)",
        "hasOrChoice": False,
        "preview": "Definition: Co-prime Numbers / सह-अभाज्य संख्याएँ",
        "content": "**What are Co-prime numbers? Give one pair of co-prime numbers.**  \n**सह-अभाज्य संख्याएँ (Co-prime numbers) किन्हें कहते हैं? एक उदाहरण दीजिए।**"
    },
    {
        "id": "6m_extra_f3",
        "subjectId": "6_maths",
        "sectionKey": "sec_a",
        "set": "Sample Paper",
        "orderInSet": 3,
        "originalNum": "Q1(iii)",
        "marks": 1,
        "chapter": "Ch 5: Integers (पूर्णांक)",
        "hasOrChoice": False,
        "preview": "Concept: Additive Inverse / योज्य प्रतिलोम",
        "content": "**What is the Additive Inverse of an integer? State the additive inverse of $-48$.**  \n**किसी पूर्णांक का योज्य प्रतिलोम (Additive inverse) क्या होता है? $-48$ का योज्य प्रतिलोम लिखिए।**"
    },
    {
        "id": "6m_extra_f4",
        "subjectId": "6_maths",
        "sectionKey": "sec_a",
        "set": "Sample Paper",
        "orderInSet": 4,
        "originalNum": "Q1(iv)",
        "marks": 1,
        "chapter": "Ch 8: Introduction to Algebra (बीजगणित)",
        "hasOrChoice": False,
        "preview": "Formula: Perimeter of a regular hexagon / सम षट्भुज का परिमाप",
        "content": "**Write the algebraic formula for the perimeter of a regular hexagon with side $s$.**  \n**भुजा $s$ वाले एक सम षट्भुज के परिमाप का बीजीय सूत्र लिखिए:**  \n$$\\text{Perimeter (परिमाप)} = 6s$$"
    },
    {
        "id": "6m_extra_f5",
        "subjectId": "6_maths",
        "sectionKey": "sec_a",
        "set": "Sample Paper",
        "orderInSet": 5,
        "originalNum": "Q1(v)",
        "marks": 1,
        "chapter": "Ch 6: Fractions (भिन्न)",
        "hasOrChoice": False,
        "preview": "Definition: Proper Fraction / उचित भिन्न",
        "content": "**Define a Proper Fraction with an example.**  \n**उचित भिन्न (Proper fraction) की परिभाषा लिखिए तथा एक उदाहरण दीजिए।**"
    },

    # --- Section B: MCQs & True/False ---
    {
        "id": "6m_extra_b1",
        "subjectId": "6_maths",
        "sectionKey": "sec_b",
        "set": "Sample Paper",
        "orderInSet": 6,
        "originalNum": "Q2(i)",
        "marks": 1,
        "chapter": "Ch 4: Playing with Numbers (संख्याओं के साथ खेलना)",
        "hasOrChoice": False,
        "preview": "MCQ: Smallest composite number / सबसे छोटी भाज्य संख्या",
        "content": "**The smallest composite number is:**  \n**सबसे छोटी भाज्य संख्या है:**  \n(a) $1$  \n(b) $2$  \n(c) $4$  \n(d) $6$"
    },
    {
        "id": "6m_extra_b2",
        "subjectId": "6_maths",
        "sectionKey": "sec_b",
        "set": "Sample Paper",
        "orderInSet": 7,
        "originalNum": "Q2(ii)",
        "marks": 1,
        "chapter": "Ch 5: Integers (पूर्णांक)",
        "hasOrChoice": False,
        "preview": "True/False: Zero is greater than every negative integer",
        "content": "**State True (T) or False (F): Zero is greater than every negative integer.**  \n**सत्य (T) अथवा असत्य (F) बताइए: शून्य प्रत्येक ऋणात्मक पूर्णांक से बड़ा होता है।**"
    },
    {
        "id": "6m_extra_b3",
        "subjectId": "6_maths",
        "sectionKey": "sec_b",
        "set": "Sample Paper",
        "orderInSet": 8,
        "originalNum": "Q2(iii)",
        "marks": 1,
        "chapter": "Ch 7: Decimals (दशमलव)",
        "hasOrChoice": False,
        "preview": "MCQ: 7 rupees 5 paise written in decimals / 7 रुपये 5 पैसे",
        "content": "**7 rupees 5 paise can be written in decimals as:**  \n**7 रुपये 5 पैसे को दशमलव रूप में लिखा जाता है:**  \n(a) ₹ $7.5$  \n(b) ₹ $7.05$  \n(c) ₹ $7.50$  \n(d) ₹ $0.75$"
    },
    {
        "id": "6m_extra_b4",
        "subjectId": "6_maths",
        "sectionKey": "sec_b",
        "set": "Sample Paper",
        "orderInSet": 9,
        "originalNum": "Q2(iv)",
        "marks": 1,
        "chapter": "Ch 9: Symmetry and Geometry (सममिति एवं ज्यामिति)",
        "hasOrChoice": False,
        "preview": "MCQ: Number of lines of symmetry in an equilateral triangle",
        "content": "**The number of lines of symmetry in an equilateral triangle is:**  \n**एक समबाहु त्रिभुज में सममिति रेखाओं की संख्या होती है:**  \n(a) $1$  \n(b) $2$  \n(c) $3$  \n(d) $0$"
    },
    {
        "id": "6m_extra_b5",
        "subjectId": "6_maths",
        "sectionKey": "sec_b",
        "set": "Sample Paper",
        "orderInSet": 10,
        "originalNum": "Q2(v)",
        "marks": 1,
        "chapter": "Ch 8: Introduction to Algebra (बीजगणित)",
        "hasOrChoice": False,
        "preview": "True/False: Expression 3x + 5 is an equation",
        "content": "**State True (T) or False (F): $3x + 5$ is an equation.**  \n**सत्य (T) अथवा असत्य (F) बताइए: $3x + 5$ एक समीकरण है।**"
    },

    # --- Section C: Very Short Answer, Patterns & Symmetry ---
    {
        "id": "6m_extra_c1",
        "subjectId": "6_maths",
        "sectionKey": "sec_c",
        "set": "Sample Paper",
        "orderInSet": 11,
        "originalNum": "Q3",
        "marks": 2,
        "chapter": "Ch 5: Integers (पूर्णांक)",
        "hasOrChoice": False,
        "preview": "Represent integers on number line: -5 and +3",
        "content": "**Represent the following integers on a number line:**  \n**निम्नलिखित पूर्णांकों को एक संख्या रेखा पर निरूपित कीजिए:**  \n(a) $-5$  \n(b) $+3$"
    },
    {
        "id": "6m_extra_c2",
        "subjectId": "6_maths",
        "sectionKey": "sec_c",
        "set": "Sample Paper",
        "orderInSet": 12,
        "originalNum": "Q4",
        "marks": 2,
        "chapter": "Ch 4: Playing with Numbers (संख्याओं के साथ खेलना)",
        "hasOrChoice": False,
        "preview": "Pattern: Divisibility test for 11 / 11 की विभाज्यता जाँच",
        "content": "**Using divisibility test, determine whether $5445$ is divisible by $11$. Show steps.**  \n**विभाज्यता परीक्षण के नियमों का प्रयोग करते हुए बताइए कि क्या संख्या $5445$, $11$ से विभाज्य है?**"
    },
    {
        "id": "6m_extra_c3",
        "subjectId": "6_maths",
        "sectionKey": "sec_c",
        "set": "Sample Paper",
        "orderInSet": 13,
        "originalNum": "Q5",
        "marks": 2,
        "chapter": "Ch 6: Fractions (भिन्न)",
        "hasOrChoice": False,
        "preview": "Write two equivalent fractions of 3/5",
        "content": "**Write two equivalent fractions of $\\frac{3}{5}$, one with numerator $15$ and one with denominator $30$.**  \n**भिन्न $\\frac{3}{5}$ के दो तुल्य भिन्न लिखिए, एक का अंश $15$ हो तथा दूसरे का हर $30$ हो।**"
    },
    {
        "id": "6m_extra_c4",
        "subjectId": "6_maths",
        "sectionKey": "sec_c",
        "set": "Sample Paper",
        "orderInSet": 14,
        "originalNum": "Q6",
        "marks": 2,
        "chapter": "Ch 9: Symmetry and Geometry (सममिति एवं ज्यामिति)",
        "hasOrChoice": False,
        "preview": "Draw lines of symmetry for letters M and H",
        "content": "**Draw the lines of symmetry for each of the following capital English letters:**  \n**निम्नलिखित अंग्रेजी के बड़े अक्षरों की सममिति रेखाएँ खींचिए:**  \n(a) $\\mathbf{M}$  \n(b) $\\mathbf{H}$"
    },
    {
        "id": "6m_extra_c5",
        "subjectId": "6_maths",
        "sectionKey": "sec_c",
        "set": "Sample Paper",
        "orderInSet": 15,
        "originalNum": "Q7",
        "marks": 2,
        "chapter": "Ch 7: Decimals (दशमलव)",
        "hasOrChoice": False,
        "preview": "Evaluate: 280.69 + 25.2 + 38",
        "content": "**Find the sum:**  \n**योगफल ज्ञात कीजिए:**  \n$$280.69 + 25.2 + 38$$"
    },
    {
        "id": "6m_extra_c6",
        "subjectId": "6_maths",
        "sectionKey": "sec_c",
        "set": "Sample Paper",
        "orderInSet": 16,
        "originalNum": "Q8",
        "marks": 2,
        "chapter": "Ch 8: Introduction to Algebra (बीजगणित)",
        "hasOrChoice": False,
        "preview": "Write algebraic expression for statements",
        "content": "**Write an algebraic expression for each of the following statements:**  \n**निम्नलिखित कथनों के लिए बीजीय व्यंजक लिखिए:**  \n(a) $7$ added to $p$ / $p$ में $7$ जोड़ना  \n(b) $5$ times $y$ from which $3$ is subtracted / $y$ के $5$ गुने में से $3$ घटाना"
    },

    # --- Section D: Short Answer & Calculations (3 Marks) ---
    {
        "id": "6m_extra_d1",
        "subjectId": "6_maths",
        "sectionKey": "sec_d",
        "set": "Sample Paper",
        "orderInSet": 17,
        "originalNum": "Q9",
        "marks": 3,
        "chapter": "Ch 4: Playing with Numbers (संख्याओं के साथ खेलना)",
        "hasOrChoice": False,
        "preview": "Find HCF of 18, 54, 81 by prime factorisation",
        "content": "**Find the Highest Common Factor (HCF) of $18, 54,$ and $81$ using prime factorisation method.**  \n**अभाज्य गुणनखंड विधि द्वारा $18, 54$ और $81$ का महत्तम समापवर्तक (HCF / म.स.प.) ज्ञात कीजिए।**"
    },
    {
        "id": "6m_extra_d2",
        "subjectId": "6_maths",
        "sectionKey": "sec_d",
        "set": "Sample Paper",
        "orderInSet": 18,
        "originalNum": "Q10",
        "marks": 3,
        "chapter": "Ch 5: Integers (पूर्णांक)",
        "hasOrChoice": False,
        "preview": "Simplify: (-13) + 32 - 8 - 1",
        "content": "**Simplify step by step:**  \n**क्रमबद्ध हल कीजिए:**  \n$$(-13) + 32 - 8 - 1$$"
    },
    {
        "id": "6m_extra_d3",
        "subjectId": "6_maths",
        "sectionKey": "sec_d",
        "set": "Sample Paper",
        "orderInSet": 19,
        "originalNum": "Q11",
        "marks": 3,
        "chapter": "Ch 6: Fractions (भिन्न)",
        "hasOrChoice": False,
        "preview": "Fraction operation: 2/3 + 3/4 + 1/2",
        "content": "**Solve and write the answer as a mixed fraction:**  \n**हल कीजिए तथा उत्तर को मिश्रित भिन्न में लिखिए:**  \n$$\\frac{2}{3} + \\frac{3}{4} + \\frac{1}{2}$$"
    },
    {
        "id": "6m_extra_d4",
        "subjectId": "6_maths",
        "sectionKey": "sec_d",
        "set": "Sample Paper",
        "orderInSet": 20,
        "originalNum": "Q12",
        "marks": 3,
        "chapter": "Ch 7: Decimals (दशमलव)",
        "hasOrChoice": False,
        "preview": "Word problem: Rashid spent Rs 35.75 for Maths book and Rs 32.60 for Science",
        "content": "**Rashid spent ₹ $35.75$ for a Maths book and ₹ $32.60$ for a Science book. Find the total amount spent by Rashid.**  \n**राशिद ने गणित की पुस्तक के लिए ₹ $35.75$ और विज्ञान की पुस्तक के लिए ₹ $32.60$ खर्च किए। राशिद द्वारा खर्च किया गया कुल धन ज्ञात कीजिए।**"
    },

    # --- Section E: Long Answer, Word Problems & Construction (4 Marks) ---
    {
        "id": "6m_extra_e1",
        "subjectId": "6_maths",
        "sectionKey": "sec_e",
        "set": "Sample Paper",
        "orderInSet": 21,
        "originalNum": "Q13",
        "marks": 4,
        "chapter": "Ch 4: Playing with Numbers (संख्याओं के साथ खेलना)",
        "hasOrChoice": True,
        "preview": "Find LCM of 20, 25 and 30 OR Three bells toll together",
        "content": "**Find the Least Common Multiple (LCM) of $20, 25,$ and $30$ using the division method.**  \n**भाग विधि द्वारा $20, 25$ तथा $30$ का लघुत्तम समापवर्त्य (LCM / ल.स.प.) ज्ञात कीजिए।**  \n\n**OR / अथवा**  \n\n**Three traffic lights change after every $48$ seconds, $72$ seconds, and $108$ seconds respectively. If they change simultaneously at 7:00 a.m., at what time will they change simultaneously again?**  \n**तीन विभिन्न चौराहों की ट्रैफिक लाइटें क्रमशः प्रत्येक $48$ सेकंड, $72$ सेकंड तथा $108$ सेकंड बाद बदलती हैं। यदि वे प्रातः 7:00 बजे एक साथ बदलें, तो वे पुनः एक साथ कितने बजे बदलेंगी?**"
    },
    {
        "id": "6m_extra_e2",
        "subjectId": "6_maths",
        "sectionKey": "sec_e",
        "set": "Sample Paper",
        "orderInSet": 22,
        "originalNum": "Q14",
        "marks": 4,
        "chapter": "Ch 6: Fractions (भिन्न)",
        "hasOrChoice": True,
        "preview": "Word problem: Sarita bought 2/5 metre ribbon and Lalita 3/4 metre OR simplify fractions",
        "content": "**Sarita bought $\\frac{2}{5}\\text{ metre}$ of ribbon and Lalita $\\frac{3}{4}\\text{ metre}$ of ribbon. What is the total length of ribbon they bought together?**  \n**सरिता ने $\\frac{2}{5}$ मीटर रिबन खरीदा और ललिता ने $\\frac{3}{4}$ मीटर रिबन खरीदा। दोनों ने मिलकर कुल कितना रिबन खरीदा?**  \n\n**OR / अथवा**  \n\n**A piece of wire $\\frac{7}{8}\\text{ metre}$ long broke into two pieces. One piece was $\\frac{1}{4}\\text{ metre}$ long. How long is the other piece?**  \n**एक तार का टुकड़ा $\\frac{7}{8}$ मीटर लंबा है। यह दो टुकड़ों में टूट जाता है। एक टुकड़ा $\\frac{1}{4}$ मीटर लंबा है। दूसरे टुकड़े की लंबाई क्या है?**"
    },
    {
        "id": "6m_extra_e3",
        "subjectId": "6_maths",
        "sectionKey": "sec_e",
        "set": "Sample Paper",
        "orderInSet": 23,
        "originalNum": "Q15",
        "marks": 4,
        "chapter": "Ch 9: Symmetry and Geometry (सममिति एवं ज्यामिति)",
        "hasOrChoice": True,
        "preview": "Draw line segment AB = 7.3 cm and construct perpendicular bisector",
        "content": "**Draw a line segment $\\overline{AB}$ of length $7.3\\text{ cm}$ and construct its perpendicular bisector using ruler and compasses.**  \n**रूलर और परकार की सहायता से $7.3$ सेमी लंबाई का रेखाखंड $\\overline{AB}$ खींचिए तथा उसका लंब समद्विभाजक खींचिए।**  \n\n**OR / अथवा**  \n\n**Draw an angle of measure $60^\\circ$ using ruler and compasses and bisect it to obtain a $30^\\circ$ angle.**  \n**रूलर और परकार की सहायता से $60^\\circ$ का कोण बनाइए तथा इसे समद्विभाजित करके $30^\\circ$ का कोण प्राप्त कीजिए।**"
    },
    {
        "id": "6m_extra_e4",
        "subjectId": "6_maths",
        "sectionKey": "sec_e",
        "set": "Sample Paper",
        "orderInSet": 24,
        "originalNum": "Q16",
        "marks": 4,
        "chapter": "Ch 8: Introduction to Algebra (बीजगणित)",
        "hasOrChoice": True,
        "preview": "Cost of a notebook is Rs p and a pen is Rs q OR solve matchstick pattern equation",
        "content": "**(a) If the cost of one notebook is ₹ $p$ and the cost of one pen is ₹ $q$, find the total cost of $5$ notebooks and $8$ pens in terms of $p$ and $q$. (2 Marks)**  \n**यदि एक नोटबुक का मूल्य ₹ $p$ तथा एक पेन का मूल्य ₹ $q$ है, तो $5$ नोटबुक और $8$ पेन का कुल मूल्य $p$ और $q$ के रूप में ज्ञात कीजिए।**  \n**(b) Solve the equation: $2x + 7 = 19$. (2 Marks)**  \n**समीकरण को हल कीजिए: $2x + 7 = 19$।**  \n\n**OR / अथवा**  \n\n**Sarita's present age is $y$ years. What will be her age $5$ years from now? What was her age $3$ years ago? If her grandfather's age is $6$ times her age, what is grandfather's age?**  \n**सरिता की वर्तमान आयु $y$ वर्ष है। आज से $5$ वर्ष बाद उसकी आयु क्या होगी? $3$ वर्ष पहले उसकी आयु क्या थी? यदि उसके दादाजी की आयु उसकी आयु की $6$ गुनी है, तो दादाजी की आयु क्या है?**"
    }
]

# Additional authentic questions for Class 5 Maths
EXTRA_QUESTIONS_5_MATHS = [
    # --- Section A: Formulas, Definitions & Basic Concepts ---
    {
        "id": "5m_extra_f1",
        "subjectId": "5_maths",
        "sectionKey": "sec_a",
        "set": "Sample Paper",
        "orderInSet": 1,
        "originalNum": "Q1(i)",
        "marks": 1,
        "chapter": "Ch 2: Shapes and Angles (आकृतियाँ और कोण)",
        "hasOrChoice": False,
        "preview": "Definition: Right angle / समकोण की परिभाषा",
        "content": "**Define a Right Angle. What is its measure in degrees?**  \n**समकोण (Right angle) की परिभाषा लिखिए। अंश (डिग्री) में इसका मान कितना होता है?**"
    },
    {
        "id": "5m_extra_f2",
        "subjectId": "5_maths",
        "sectionKey": "sec_a",
        "set": "Sample Paper",
        "orderInSet": 2,
        "originalNum": "Q1(ii)",
        "marks": 1,
        "chapter": "Ch 11: Area and its Boundary (क्षेत्रफल और घेरा)",
        "hasOrChoice": False,
        "preview": "Formula: Area of a square / वर्ग का क्षेत्रफल",
        "content": "**State the formula for the Area of a Square with side $s$.**  \n**भुजा $s$ वाले एक वर्ग का क्षेत्रफल ज्ञात करने का सूत्र लिखिए:**  \n$$\\text{Area of Square} = \\text{Side} \\times \\text{Side} / \\text{भुजा} \\times \\text{भुजा}$$"
    },
    {
        "id": "5m_extra_f3",
        "subjectId": "5_maths",
        "sectionKey": "sec_a",
        "set": "Sample Paper",
        "orderInSet": 3,
        "originalNum": "Q1(iii)",
        "marks": 1,
        "chapter": "Ch 1: The Fish Tale (मछली उछली)",
        "hasOrChoice": False,
        "preview": "Formula: Speed, Distance and Time / चाल, दूरी और समय",
        "content": "**Write the formula to calculate Speed when distance and time are given.**  \n**दूरी और समय ज्ञात होने पर चाल (Speed) ज्ञात करने का सूत्र लिखिए:**  \n$$\\text{Speed (चाल)} = \\frac{\\text{Distance (दूरी)}}{\\text{Time (समय)}}$$"
    },
    {
        "id": "5m_extra_f4",
        "subjectId": "5_maths",
        "sectionKey": "sec_a",
        "set": "Sample Paper",
        "orderInSet": 4,
        "originalNum": "Q1(iv)",
        "marks": 1,
        "chapter": "Ch 9: Boxes and Sketches (डिब्बे और रेखाचित्र)",
        "hasOrChoice": False,
        "preview": "Number of faces, edges and vertices of a cube / घन के फलक, किनारे और शीर्ष",
        "content": "**State the number of faces, edges, and vertices of a Cube.**  \n**एक घन (Cube) के फलकों (Faces), किनारों (Edges) और शीर्षों (Vertices) की संख्या लिखिए।**"
    },
    {
        "id": "5m_extra_f5",
        "subjectId": "5_maths",
        "sectionKey": "sec_a",
        "set": "Sample Paper",
        "orderInSet": 5,
        "originalNum": "Q1(v)",
        "marks": 1,
        "chapter": "Ch 10: Tenths and Hundredths (दसवाँ और सौवाँ भाग)",
        "hasOrChoice": False,
        "preview": "1 centimetre is equal to how many millimetres? / 1 सेमी में कितने मिमी",
        "content": "**Fill in the blank: $1\\text{ cm} =$ _______ $\\text{mm}$.**  \n**रिक्त स्थान भरिए: $1$ सेमी $=$ _______ मिलीमीटर।**"
    },

    # --- Section B: MCQs & True/False ---
    {
        "id": "5m_extra_b1",
        "subjectId": "5_maths",
        "sectionKey": "sec_b",
        "set": "Sample Paper",
        "orderInSet": 6,
        "originalNum": "Q2(i)",
        "marks": 1,
        "chapter": "Ch 1: The Fish Tale (मछली उछली)",
        "hasOrChoice": False,
        "preview": "MCQ: One lakh is equal to / एक लाख बराबर होता है",
        "content": "**One lakh is equal to:**  \n**एक लाख बराबर होता है:**  \n(a) $10$ Thousands / दस हजार  \n(b) $100$ Thousands / सौ हजार  \n(c) $1,000$ Thousands / एक हजार हजार  \n(d) $10$ Crores / दस करोड़"
    },
    {
        "id": "5m_extra_b2",
        "subjectId": "5_maths",
        "sectionKey": "sec_b",
        "set": "Sample Paper",
        "orderInSet": 7,
        "originalNum": "Q2(ii)",
        "marks": 1,
        "chapter": "Ch 2: Shapes and Angles (आकृतियाँ और कोण)",
        "hasOrChoice": False,
        "preview": "MCQ: Angle made by hands of clock at 3:00 / घड़ी में 3:00 बजे कोण",
        "content": "**The angle made by the hands of a clock at 3:00 is:**  \n**घड़ी में 3:00 बजे सुइयों के बीच बना कोण होता है:**  \n(a) Acute angle / न्यून कोण  \n(b) Right angle / समकोण  \n(c) Obtuse angle / अधिक कोण  \n(d) Straight angle / सरल कोण"
    },
    {
        "id": "5m_extra_b3",
        "subjectId": "5_maths",
        "sectionKey": "sec_b",
        "set": "Sample Paper",
        "orderInSet": 8,
        "originalNum": "Q2(iii)",
        "marks": 1,
        "chapter": "Ch 4: Parts and Wholes (हिस्से और पूरे)",
        "hasOrChoice": False,
        "preview": "True/False: 2/4 is equivalent to 1/2",
        "content": "**State True (T) or False (F): The fraction $\\frac{2}{4}$ is equal to $\\frac{1}{2}$.**  \n**सत्य (T) अथवा असत्य (F) बताइए: भिन्न $\\frac{2}{4}$ का मान $\\frac{1}{2}$ के बराबर है।**"
    },
    {
        "id": "5m_extra_b4",
        "subjectId": "5_maths",
        "sectionKey": "sec_b",
        "set": "Sample Paper",
        "orderInSet": 9,
        "originalNum": "Q2(iv)",
        "marks": 1,
        "chapter": "Ch 5: Does it Look the Same? (क्या यह एक जैसा दिखता है?)",
        "hasOrChoice": False,
        "preview": "True/False: The letter 'O' looks the same after half a turn",
        "content": "**State True (T) or False (F): The English letter 'O' looks exactly the same after half a turn ($180^\\circ$).**  \n**सत्य (T) अथवा असत्य (F) बताइए: आधा घुमाने ($180^\\circ$) पर अंग्रेजी का अक्षर 'O' बिल्कुल वैसा ही दिखाई देता है।**"
    },
    {
        "id": "5m_extra_b5",
        "subjectId": "5_maths",
        "sectionKey": "sec_b",
        "set": "Sample Paper",
        "orderInSet": 10,
        "originalNum": "Q2(v)",
        "marks": 1,
        "chapter": "Ch 6: Multiples and Factors (गुणज और गुणनखंड)",
        "hasOrChoice": False,
        "preview": "MCQ: Smallest common multiple of 4 and 6 / 4 और 6 का सबसे छोटा साझा गुणज",
        "content": "**The smallest common multiple (LCM) of $4$ and $6$ is:**  \n**$4$ और $6$ का सबसे छोटा साझा गुणज (LCM) है:**  \n(a) $6$  \n(b) $12$  \n(c) $24$  \n(d) $2$"
    },

    # --- Section C: Very Short Answer, Patterns & Symmetry ---
    {
        "id": "5m_extra_c1",
        "subjectId": "5_maths",
        "sectionKey": "sec_c",
        "set": "Sample Paper",
        "orderInSet": 11,
        "originalNum": "Q3",
        "marks": 2,
        "chapter": "Ch 7: Can You See the Pattern? (पैटर्न)",
        "hasOrChoice": False,
        "preview": "Pattern: 1×1=1, 11×11=121, 111×111=?",
        "content": "**Observe the pattern and write the next two steps:**  \n**पैटर्न को देखकर अगले दो चरण लिखिए:**  \n$$1 \\times 1 = 1$$  \n$$11 \\times 11 = 121$$  \n$$111 \\times 111 = 12321$$  \n$$1111 \\times 1111 = \\underline{\\hspace{2.5cm}}$$  \n$$11111 \\times 11111 = \\underline{\\hspace{2.5cm}}$$"
    },
    {
        "id": "5m_extra_c2",
        "subjectId": "5_maths",
        "sectionKey": "sec_c",
        "set": "Sample Paper",
        "orderInSet": 12,
        "originalNum": "Q4",
        "marks": 2,
        "chapter": "Ch 2: Shapes and Angles (आकृतियाँ और कोण)",
        "hasOrChoice": False,
        "preview": "Angles at 2:00 and 7:00 / 2:00 और 7:00 बजे कोण का प्रकार",
        "content": "**What kind of angle (acute, obtuse, or right) is formed by the hands of a clock at:**  \n**घड़ी की सुइयों द्वारा निम्नलिखित समय पर किस प्रकार का कोण बनता है (न्यून कोण, अधिक कोण अथवा समकोण):**  \n(a) 2:00  \n(b) 7:00"
    },
    {
        "id": "5m_extra_c3",
        "subjectId": "5_maths",
        "sectionKey": "sec_c",
        "set": "Sample Paper",
        "orderInSet": 13,
        "originalNum": "Q5",
        "marks": 2,
        "chapter": "Ch 4: Parts and Wholes (हिस्से और पूरे)",
        "hasOrChoice": False,
        "preview": "Shade 3/4 part of a rectangle",
        "content": "**A rectangle is divided into $8$ equal parts. How many parts should be shaded to show $\\frac{3}{4}$ of the rectangle?**  \n**एक आयत को $8$ बराबर भागों में बाँटा गया है। आयत का $\\frac{3}{4}$ भाग दर्शाने के लिए कितने भागों में रंग भरना होगा?**"
    },
    {
        "id": "5m_extra_c4",
        "subjectId": "5_maths",
        "sectionKey": "sec_c",
        "set": "Sample Paper",
        "orderInSet": 14,
        "originalNum": "Q6",
        "marks": 2,
        "chapter": "Ch 6: Multiples and Factors (गुणज और गुणनखंड)",
        "hasOrChoice": False,
        "preview": "Draw factor tree for 36 / 36 का गुणनखंड वृक्ष",
        "content": "**Draw a Factor Tree for the number $36$.**  \n**संख्या $36$ के लिए एक गुणनखंड वृक्ष (Factor Tree) बनाइए।**"
    },
    {
        "id": "5m_extra_c5",
        "subjectId": "5_maths",
        "sectionKey": "sec_c",
        "set": "Sample Paper",
        "orderInSet": 15,
        "originalNum": "Q7",
        "marks": 2,
        "chapter": "Ch 10: Tenths and Hundredths (दसवाँ और सौवाँ भाग)",
        "hasOrChoice": False,
        "preview": "Convert into decimals: 45/100 and 7/10",
        "content": "**Write the following as decimal numbers:**  \n**निम्नलिखित को दशमलव संख्या के रूप में लिखिए:**  \n(a) $\\frac{7}{10}$  \n(b) $\\frac{45}{100}$"
    },
    {
        "id": "5m_extra_c6",
        "subjectId": "5_maths",
        "sectionKey": "sec_c",
        "set": "Sample Paper",
        "orderInSet": 16,
        "originalNum": "Q8",
        "marks": 2,
        "chapter": "Ch 8: Mapping Your Way (नक्शा)",
        "hasOrChoice": False,
        "preview": "Map scale: 1 cm = 100 km, distance between Delhi and Jaipur",
        "content": "**On a map, the scale is $1\\text{ cm} = 100\\text{ km}$. If the distance between two towns on the map is $4.5\\text{ cm}$, what is the actual distance on the ground?**  \n**एक नक्शे पर पैमाना $1$ सेमी $= 100$ किमी है। यदि नक्शे पर दो शहरों के बीच की दूरी $4.5$ सेमी है, तो जमीन पर उनकी वास्तविक दूरी क्या होगी?**"
    },

    # --- Section D: Short Answer & Calculations (3 Marks) ---
    {
        "id": "5m_extra_d1",
        "subjectId": "5_maths",
        "sectionKey": "sec_d",
        "set": "Sample Paper",
        "orderInSet": 17,
        "originalNum": "Q9",
        "marks": 3,
        "chapter": "Ch 1: The Fish Tale (मछली उछली)",
        "hasOrChoice": False,
        "preview": "Speed calculation: Motor boat travels at 20 km in 1 hour",
        "content": "**A motor boat travels at a speed of $20\\text{ km}$ in one hour.**  \n**एक मोटर बोट एक घंटे में $20$ किमी की दूरी तय करती है।**  \n(a) How far would the motor boat go in three and a half hours?  \nसाढ़े तीन घंटे में यह बोट कितनी दूर जाएगी?  \n(b) How much time will it take to go $85\\text{ km}$?  \n$85$ किमी जाने में इसे कितना समय लगेगा?"
    },
    {
        "id": "5m_extra_d2",
        "subjectId": "5_maths",
        "sectionKey": "sec_d",
        "set": "Sample Paper",
        "orderInSet": 18,
        "originalNum": "Q10",
        "marks": 3,
        "chapter": "Ch 11: Area and its Boundary (क्षेत्रफल और घेरा)",
        "hasOrChoice": False,
        "preview": "Perimeter and Area of a rectangular plot 15m by 8m",
        "content": "**A rectangular garden has a length of $15\\text{ metres}$ and a breadth of $8\\text{ metres}$.**  \n**एक आयताकार बगीचे की लंबाई $15$ मीटर और चौड़ाई $8$ मीटर है।**  \n(a) Find the perimeter of the garden. / बगीचे का परिमाप ज्ञात कीजिए।  \n(b) Find the area of the garden. / बगीचे का क्षेत्रफल ज्ञात कीजिए।"
    },
    {
        "id": "5m_extra_d3",
        "subjectId": "5_maths",
        "sectionKey": "sec_d",
        "set": "Sample Paper",
        "orderInSet": 19,
        "originalNum": "Q11",
        "marks": 3,
        "chapter": "Ch 13: Ways to Multiply and Divide (गुणा और भाग)",
        "hasOrChoice": False,
        "preview": "Bela's method: Multiply 65 × 32 step by step",
        "content": "**Multiply $65 \\times 32$ using Bela's method (column method) and show all the partial products.**  \n**बेला के तरीके (स्तंभ विधि) का उपयोग करते हुए $65 \\times 32$ का गुणा कीजिए तथा सभी चरण दिखाइए।**"
    },
    {
        "id": "5m_extra_d4",
        "subjectId": "5_maths",
        "sectionKey": "sec_d",
        "set": "Sample Paper",
        "orderInSet": 20,
        "originalNum": "Q12",
        "marks": 3,
        "chapter": "Ch 3: How Many Squares? (कितने वर्ग?)",
        "hasOrChoice": False,
        "preview": "A square has a perimeter of 40 cm. Find side and area",
        "content": "**The perimeter of a square chess board is $40\\text{ cm}$.**  \n**एक वर्गाकार शतरंज के बोर्ड का परिमाप $40$ सेमी है।**  \n(a) What is the length of its side? / इसकी प्रत्येक भुजा की लंबाई क्या है?  \n(b) What is its area? / इसका क्षेत्रफल कितना है?"
    },

    # --- Section E: Long Answer, Word Problems & Measurements (4 Marks) ---
    {
        "id": "5m_extra_e1",
        "subjectId": "5_maths",
        "sectionKey": "sec_e",
        "set": "Sample Paper",
        "orderInSet": 21,
        "originalNum": "Q13",
        "marks": 4,
        "chapter": "Ch 1: The Fish Tale (मछली उछली)",
        "hasOrChoice": True,
        "preview": "Fish drying calculation: 6000 kg fresh fish becomes 1/3 when dried",
        "content": "**Floramma wants to dry $6000\\text{ kg}$ of fresh fish. When fresh fish is dried, it becomes $\\frac{1}{3}$ of its weight.**  \n**फ्लोरम्मा $6000$ किग्रा ताजी मछली सुखाना चाहती है। ताजी मछली सूखने पर अपने वजन की $\\frac{1}{3}$ रह जाती है।**  \n(a) How many kilograms of dried fish will she get? (2 Marks)  \nउसे कितनी सूखी मछली प्राप्त होगी?  \n(b) If fresh fish costs ₹ $15$ per kg and dried fish sells for ₹ $70$ per kg, find her profit. (2 Marks)  \nयदि ताजी मछली का क्रय मूल्य ₹ $15$ प्रति किग्रा तथा सूखी मछली का विक्रय मूल्य ₹ $70$ प्रति किग्रा हो, तो उसका लाभ ज्ञात कीजिए।  \n\n**OR / अथवा**  \n\n**Jhansi and her sister took a loan of ₹ $21,000$ to buy a log boat. They paid back a total of ₹ $23,520$ in one year.**  \n**झाँसी और उसकी बहन ने एक लट्ठे की नाव खरीदने के लिए ₹ $21,000$ का कर्ज लिया। उन्होंने एक साल में कुल ₹ $23,520$ वापस दिए।**  \n(a) How much money did they pay back every month? (2 Marks)  \nउन्होंने हर महीने कितना रुपया वापस दिया?  \n(b) How much total extra money (interest) did they pay? (2 Marks)  \nउन्होंने कुल कितना अतिरिक्त धन (ब्याज) दिया?"
    },
    {
        "id": "5m_extra_e2",
        "subjectId": "5_maths",
        "sectionKey": "sec_e",
        "set": "Sample Paper",
        "orderInSet": 22,
        "originalNum": "Q14",
        "marks": 4,
        "chapter": "Ch 11: Area and its Boundary (क्षेत्रफल और घेरा)",
        "hasOrChoice": True,
        "preview": "Floor tiles: Room 4m by 3m to be tiled with 20cm by 20cm square tiles",
        "content": "**A rectangular room floor has length $4\\text{ m}$ and width $3\\text{ m}$. Square tiles of side $20\\text{ cm}$ each are to be laid on the floor.**  \n**एक आयताकार कमरे के फर्श की लंबाई $4$ मीटर और चौड़ाई $3$ मीटर है। फर्श पर $20$ सेमी भुजा वाली वर्गाकार टाइलें बिछाई जानी हैं।**  \n(a) Find the area of the floor in $\\text{cm}^2$. (2 Marks)  \nकमरे के फर्श का क्षेत्रफल वर्ग सेमी में ज्ञात कीजिए।  \n(b) How many tiles will be needed to cover the entire floor? (2 Marks)  \nपूरे फर्श को ढकने के लिए कुल कितनी टाइलों की आवश्यकता होगी?  \n\n**OR / अथवा**  \n\n**Arbaz plans to tile his kitchen floor with green square tiles of side $10\\text{ cm}$. The kitchen is $220\\text{ cm}$ in length and $180\\text{ cm}$ wide. How many tiles will he need? If one tile costs ₹ $8$, find the total cost of tiles.**  \n**अरबाज अपनी रसोई के फर्श पर $10$ सेमी भुजा वाली हरी वर्गाकार टाइलें लगाने की योजना बनाता है। रसोई की लंबाई $220$ सेमी और चौड़ाई $180$ सेमी है। उसे कितनी टाइलों की आवश्यकता होगी? यदि एक टाइल का मूल्य ₹ $8$ है, तो टाइलों का कुल खर्च ज्ञात कीजिए।**"
    },
    {
        "id": "5m_extra_e3",
        "subjectId": "5_maths",
        "sectionKey": "sec_e",
        "set": "Sample Paper",
        "orderInSet": 23,
        "originalNum": "Q15",
        "marks": 4,
        "chapter": "Ch 13: Ways to Multiply and Divide (गुणा और भाग)",
        "hasOrChoice": True,
        "preview": "Word problem on cartons and apples OR Sohan's daily milk calculation",
        "content": "**A fruit seller has $576$ apples. He packs them equally into $24$ cartons.**  \n**एक फल विक्रेता के पास $576$ सेब हैं। वह इन्हें $24$ डिब्बों में बराबर-बराबर पैक करता है।**  \n(a) How many apples are there in each carton? (2 Marks)  \nप्रत्येक डिब्बे में कितने सेब हैं?  \n(b) If he sells each carton for ₹ $450$, how much total money does he receive? (2 Marks)  \nयदि वह प्रत्येक डिब्बा ₹ $450$ में बेचता है, तो उसे कुल कितना धन प्राप्त होगा?  \n\n**OR / अथवा**  \n\n**Sohan drinks $8$ glasses of water every day.**  \n**सोहन प्रतिदिन $8$ गिलास पानी पीता है।**  \n(a) How many glasses of water will he drink in one month of June ($30$ days)? (2 Marks)  \nवह जून के एक महीने ($30$ दिन) में कितने गिलास पानी पिएगा?  \n(b) How many glasses of water will he drink in a full leap year ($366$ days)? (2 Marks)  \nवह पूरे एक लीप वर्ष ($366$ दिन) में कितने गिलास पानी पिएगा?**"
    },
    {
        "id": "5m_extra_e4",
        "subjectId": "5_maths",
        "sectionKey": "sec_e",
        "set": "Sample Paper",
        "orderInSet": 24,
        "originalNum": "Q16",
        "marks": 4,
        "chapter": "Ch 9: Boxes and Sketches (डिब्बे और रेखाचित्र)",
        "hasOrChoice": True,
        "preview": "Nets of a cube: draw which can fold into a box and deep drawing",
        "content": "**(a) Draw two different nets consisting of $6$ connected squares that can fold to form an open/closed cube. (2 Marks)**  \n**$6$ जुड़े हुए वर्गों के ऐसे दो अलग-अलग जाल (Nets) बनाइए जो मुड़कर एक घन बना सकते हों।**  \n**(b) Look at the opposite faces of a dice. If face with $5$ is at the bottom, which number will be at the top? (2 Marks)**  \n**एक पासे के विपरीत फलकों को देखिए। यदि $5$ अंकित फलक नीचे है, तो सबसे ऊपर कौन-सी संख्या होगी?**  \n\n**OR / अथवा**  \n\n**Draw a deep drawing of a cube showing its 3D perspective and label its faces, edges, and vertices.**  \n**एक घन का गहरा चित्र (Deep drawing / 3D दृश्य) बनाइए तथा इसके फलक, किनारे और शीर्ष दर्शाइए।**"
    }
]

def main():
    print("--- 1. Updating blueprints.json with Custom Math Blueprint ---")
    bp_path = os.path.join("data", "blueprints.json")
    with open(bp_path, "r", encoding="utf-8") as f:
        blueprints = json.load(f)

    # 5th Maths Blueprint
    blueprints["5_maths"]["sections"] = [
        {
            "key": "sec_a",
            "title": "### SECTION 'A' / खंड 'क'",
            "subTitle": "Formulas, Definitions & Basic Concepts / सूत्र, परिभाषाएँ एवं मूल अवधारणाएँ",
            "marksEach": 1,
            "requiredCount": 5,
            "totalMarks": 5
        },
        {
            "key": "sec_b",
            "title": "### SECTION 'B' / खंड 'ख'",
            "subTitle": "Multiple Choice & True/False / बहुविकल्पीय एवं सत्य-असत्य प्रश्न",
            "marksEach": 1,
            "requiredCount": 5,
            "totalMarks": 5
        },
        {
            "key": "sec_c",
            "title": "### SECTION 'C' / खंड 'ग'",
            "subTitle": "Very Short Answer, Patterns & Symmetry / अति लघु उत्तरीय, संख्या पैटर्न एवं सममिति",
            "marksEach": 2,
            "requiredCount": 6,
            "totalMarks": 12
        },
        {
            "key": "sec_d",
            "title": "### SECTION 'D' / खंड 'घ'",
            "subTitle": "Short Answer & Step Simplifications / लघु उत्तरीय एवं क्रमबद्ध हल",
            "marksEach": 3,
            "requiredCount": 4,
            "totalMarks": 12
        },
        {
            "key": "sec_e",
            "title": "### SECTION 'E' / खंड 'ङ'",
            "subTitle": "Long Answer, Word Problems & Measurements / दीर्घ उत्तरीय, व्यावहारिक समस्याएँ एवं मापन",
            "marksEach": 4,
            "requiredCount": 4,
            "totalMarks": 16
        }
    ]

    # 6th Maths Blueprint
    blueprints["6_maths"]["sections"] = [
        {
            "key": "sec_a",
            "title": "### SECTION 'A' / खंड 'क'",
            "subTitle": "Formulas & Core Concepts / सूत्र एवं मूल अवधारणाएँ",
            "marksEach": 1,
            "requiredCount": 5,
            "totalMarks": 5
        },
        {
            "key": "sec_b",
            "title": "### SECTION 'B' / खंड 'ख'",
            "subTitle": "Multiple Choice & True/False / बहुविकल्पीय एवं सत्य-असत्य प्रश्न",
            "marksEach": 1,
            "requiredCount": 5,
            "totalMarks": 5
        },
        {
            "key": "sec_c",
            "title": "### SECTION 'C' / खंड 'ग'",
            "subTitle": "Very Short Answer, Patterns & Symmetry / अति लघु उत्तरीय, संख्या पैटर्न एवं सममिति",
            "marksEach": 2,
            "requiredCount": 6,
            "totalMarks": 12
        },
        {
            "key": "sec_d",
            "title": "### SECTION 'D' / खंड 'घ'",
            "subTitle": "Short Answer & Step-by-Step Calculations / लघु उत्तरीय एवं क्रमबद्ध गणनाएँ",
            "marksEach": 3,
            "requiredCount": 4,
            "totalMarks": 12
        },
        {
            "key": "sec_e",
            "title": "### SECTION 'E' / खंड 'ङ'",
            "subTitle": "Long Answer, Word Problems & Construction / दीर्घ उत्तरीय, व्यावहारिक समस्याएँ एवं रचना",
            "marksEach": 4,
            "requiredCount": 4,
            "totalMarks": 16
        }
    ]

    # 7th Maths Blueprint
    blueprints["7_maths"]["sections"] = [
        {
            "key": "sec_a",
            "title": "### SECTION 'A' / खंड 'क'",
            "subTitle": "Formulas & Definitions / सूत्र एवं परिभाषाएँ",
            "marksEach": 1,
            "requiredCount": 5,
            "totalMarks": 5
        },
        {
            "key": "sec_b",
            "title": "### SECTION 'B' / खंड 'ख'",
            "subTitle": "Multiple Choice & True/False with Justification / बहुविकल्पीय एवं कारण सहित सत्य-असत्य",
            "marksEach": 1,
            "requiredCount": 5,
            "totalMarks": 5
        },
        {
            "key": "sec_c",
            "title": "### SECTION 'C' / खंड 'ग'",
            "subTitle": "Very Short Answer, Patterns & Symmetry / अति लघु उत्तरीय, संख्या पैटर्न एवं सममिति",
            "marksEach": 2,
            "requiredCount": 6,
            "totalMarks": 12
        },
        {
            "key": "sec_d",
            "title": "### SECTION 'D' / खंड 'घ'",
            "subTitle": "Short Answer & Step Simplifications / लघु उत्तरीय एवं क्रमबद्ध सरलीकरण",
            "marksEach": 3,
            "requiredCount": 4,
            "totalMarks": 12
        },
        {
            "key": "sec_e",
            "title": "### SECTION 'E' / खंड 'ङ'",
            "subTitle": "Long Answer, Word Problems & Isometric Geometry / दीर्घ उत्तरीय, व्यावहारिक प्रश्न एवं समदूरिक ज्यामिति",
            "marksEach": 4,
            "requiredCount": 4,
            "totalMarks": 16
        }
    ]

    with open(bp_path, "w", encoding="utf-8") as f:
        json.dump(blueprints, f, indent=2, ensure_ascii=False)
    print("blueprints.json successfully updated with customized Math blueprint!")

    print("\n--- 2. Updating questions.json with Chapters and New Question Bank Items ---")
    q_path = os.path.join("data", "questions.json")
    with open(q_path, "r", encoding="utf-8") as f:
        questions_db = json.load(f)

    # 2.1 Assign chapters to all existing questions
    for subject_id, q_list in questions_db.items():
        for q in q_list:
            if "chapter" not in q or not q["chapter"]:
                q["chapter"] = determine_chapter(subject_id, q.get("content", ""), q.get("preview", ""))

    # 2.2 Ingest SAMPLE_QUESTIONS_7_MATHS into 7_maths
    existing_7m_ids = set(q["id"] for q in questions_db["7_maths"])
    added_7m = 0
    for sq in SAMPLE_QUESTIONS_7_MATHS:
        if sq["id"] not in existing_7m_ids:
            questions_db["7_maths"].append(sq)
            existing_7m_ids.add(sq["id"])
            added_7m += 1

    # 2.3 Ingest EXTRA_QUESTIONS_6_MATHS into 6_maths
    existing_6m_ids = set(q["id"] for q in questions_db["6_maths"])
    added_6m = 0
    for sq in EXTRA_QUESTIONS_6_MATHS:
        if sq["id"] not in existing_6m_ids:
            questions_db["6_maths"].append(sq)
            existing_6m_ids.add(sq["id"])
            added_6m += 1

    # 2.4 Ingest EXTRA_QUESTIONS_5_MATHS into 5_maths
    existing_5m_ids = set(q["id"] for q in questions_db["5_maths"])
    added_5m = 0
    for sq in EXTRA_QUESTIONS_5_MATHS:
        if sq["id"] not in existing_5m_ids:
            questions_db["5_maths"].append(sq)
            existing_5m_ids.add(sq["id"])
            added_5m += 1

    with open(q_path, "w", encoding="utf-8") as f:
        json.dump(questions_db, f, indent=2, ensure_ascii=False)

    print(f"Added {added_7m} sample questions to Class 7 Maths.")
    print(f"Added {added_6m} authentic questions to Class 6 Maths.")
    print(f"Added {added_5m} authentic questions to Class 5 Maths.")

    print("\n--- Summary of Questions in Bank by Subject ---")
    for subject_id, q_list in questions_db.items():
        chapters_count = {}
        for q in q_list:
            ch = q.get("chapter", "Unknown")
            chapters_count[ch] = chapters_count.get(ch, 0) + 1
        print(f"Subject: {subject_id} -> Total: {len(q_list)} questions across {len(chapters_count)} chapters:")
        for ch, count in sorted(chapters_count.items()):
            print(f"   * {ch}: {count} questions")

if __name__ == "__main__":
    main()
