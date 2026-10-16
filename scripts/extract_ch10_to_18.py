# scripts/extract_ch10_to_18.py
import os, sys, re, json

sys.stdout.reconfigure(encoding='utf-8')

sys_dir = r"F:\8th Science\questions"

CH_MAP = {
    10: "Ch 10: Sound (ध्वनि)",
    11: "Ch 11: Chemical Effects of Electric Current (विद्युत धारा के रासायनिक प्रभाव)",
    12: "Ch 12: Some Natural Phenomena (कुछ प्राकृतिक परिघटनाएँ)",
    13: "Ch 13: Light (प्रकाश)",
    17: "Ch 17: Stars and the Solar System (तारे एवं सौर परिवार)",
    18: "Ch 18: Pollution of Air and Water (वायु तथा जल का प्रदूषण)"
}

FIB_TF_DATA = {
    10: [
        ("Sound is produced by a _______ body.", "ध्वनि किसी _______ वस्तु द्वारा उत्पन्न होती है।", "sec_2"),
        ("The number of oscillations per second is called the _______ of oscillation.", "प्रति सेकंड होने वाले दोलनों की संख्या को दोलन की _______ कहते हैं।", "sec_2"),
        ("Unwanted or unpleasant sound is called _______.", "अप्रिय या अवांछित ध्वनि को _______ कहते हैं।", "sec_2"),
        ("The SI unit of frequency is _______.", "आवृत्ति का अंतर्राष्ट्रीय (SI) मात्रक _______ है।", "sec_2"),
        ("Sound cannot travel through a vacuum.", "ध्वनि निर्वात में संचरित नहीं हो सकती।", "sec_3"),
        ("The unit of loudness of sound is decibel (dB).", "ध्वनि की प्रबलता का मात्रक डेसिबल (dB) है।", "sec_3"),
        ("The audible frequency range for human ears is 20 Hz to 20,000 Hz.", "मानव कानों के लिए श्रव्य आवृत्ति का परास 20 Hz से 20,000 Hz तक होता है।", "sec_3"),
        ("If the amplitude of vibration is large, the sound is very feeble.", "यदि कंपन का आयाम बड़ा हो, तो ध्वनि बहुत मंद होती है।", "sec_3")
    ],
    11: [
        ("Most liquids that conduct electricity are solutions of acids, bases and _______.", "अधिकांश द्रव जो विद्युत का चालन करते हैं, वे अम्लों, क्षारकों और _______ के विलयन होते हैं।", "sec_2"),
        ("The passage of an electric current through a conducting liquid causes _______ effects.", "किसी चालक द्रव से विद्युत धारा प्रवाहित होने पर _______ प्रभाव उत्पन्न होते हैं।", "sec_2"),
        ("The process of depositing a layer of any desired metal on another material by means of electricity is called _______.", "विद्युत द्वारा किसी अन्य पदार्थ पर वांछित धातु की परत निक्षेपित करने की प्रक्रिया को _______ कहते हैं।", "sec_2"),
        ("LED stands for Light Emitting _______.", "LED का पूरा नाम प्रकाश उत्सर्जक _______ है।", "sec_2"),
        ("Pure distilled water is a good conductor of electricity.", "आसुत (शुद्ध) जल विद्युत का एक अच्छा सुचालक होता है।", "sec_3"),
        ("Electroplating is widely used to prevent corrosion and rusting of metals.", "धातुओं के क्षरण और जंग को रोकने के लिए विद्युत लेपन का व्यापक उपयोग किया जाता है।", "sec_3"),
        ("Chromium plating is done on car parts, bicycle handlebars and bath taps.", "कार के पुर्जों, साइकिल के हैंडल और नल पर क्रोमियम का लेपन किया जाता है।", "sec_3"),
        ("An electric current produces a magnetic effect around a conducting wire.", "विद्युत धारा किसी चालक तार के चारों ओर चुंबकीय प्रभाव उत्पन्न करती है।", "sec_3")
    ],
    12: [
        ("The process of transferring of electric charge from a charged object to the Earth is called _______.", "किसी आवेशित वस्तु से आवेश को पृथ्वी में भेजने की प्रक्रिया को _______ कहते हैं।", "sec_2"),
        ("An instrument used to test whether an object is carrying charge or not is called an _______.", "यह परीक्षण करने के लिए प्रयुक्त उपकरण कि कोई वस्तु आवेशित है या नहीं, _______ कहलाता है।", "sec_2"),
        ("The power of an earthquake is expressed in terms of a magnitude on a scale called _______ scale.", "किसी भूकंप की शक्ति का परिमाण एक पैमाने पर व्यक्त किया जाता है जिसे _______ पैमाना कहते हैं।", "sec_2"),
        ("Seismic waves produced by earthquakes are recorded by an instrument called a _______.", "भूकंप द्वारा उत्पन्न भूकम्पी तरंगों को एक उपकरण द्वारा रिकॉर्ड किया जाता है जिसे _______ कहते हैं।", "sec_2"),
        ("Like electric charges attract each other and unlike charges repel.", "सजातीय (समान) आवेश एक-दूसरे को आकर्षित करते हैं तथा विजातीय आवेश प्रतिकर्षित करते हैं।", "sec_3"),
        ("Lightning is a massive electric spark occurring naturally in the atmosphere.", "तड़ित (आकाशीय बिजली) वायुमंडल में प्राकृतिक रूप से होने वाली एक विशाल विद्युत चिंगारी है।", "sec_3"),
        ("A lightning conductor protects tall buildings from the damage of lightning strikes.", "तड़ित चालक बहुमंजिला भवनों को आकाशीय बिजली के आघात से सुरक्षित रखता है।", "sec_3"),
        ("Earthquakes can be precisely predicted well in advance with current scientific instruments.", "वर्तमान वैज्ञानिक उपकरणों द्वारा भूकंप की सटीक भविष्यवाणी काफी पहले की जा सकती है।", "sec_3")
    ],
    13: [
        ("The angle of incidence is always _______ to the angle of reflection.", "आपतन कोण सदैव परावर्तन कोण के _______ होता है।", "sec_2"),
        ("The image formed by a plane mirror is always virtual, behind the mirror, and _______.", "समतल दर्पण द्वारा बना प्रतिबिंब सदैव आभासी, दर्पण के पीछे और _______ होता है।", "sec_2"),
        ("Splitting of white light into its seven constituent colors is called _______ of light.", "श्वेत प्रकाश का अपने सात संघटक रंगों में विभाजित होना प्रकाश का _______ कहलाता है।", "sec_2"),
        ("The transparent front part of the human eye is called the _______.", "मानव नेत्र के सबसे आगे स्थित पारदर्शी भाग को _______ कहते हैं।", "sec_2"),
        ("Diffused reflection is caused by the irregularities of a rough surface.", "विसरित परावर्तन किसी खुरदरे पृष्ठ की अनियमितताओं के कारण होता है।", "sec_3"),
        ("Rod cells on the human retina are sensitive to bright light and color.", "मानव रेटिना पर स्थित शलाकाएँ (Rods) तीव्र प्रकाश और रंगों के प्रति संवेदनशील होती हैं।", "sec_3"),
        ("A visually impaired person can read and write using the Braille system.", "दृष्टि-बाधित व्यक्ति ब्रेल पद्धति की सहायता से पढ़ और लिख सकते हैं।", "sec_3"),
        ("The impression of an image persists on the human retina for about 1/16th of a second.", "मानव रेटिना पर किसी प्रतिबिंब का प्रभाव लगभग 1/16 सेकंड तक बना रहता है।", "sec_3")
    ],
    17: [
        ("The distance between stars and galaxies is measured in large units called _______ years.", "तारों और आकाशगंगाओं के बीच की दूरी को _______ वर्ष नामक विशाल मात्रक में मापा जाता है।", "sec_2"),
        ("The brightest planet seen in the night sky from Earth is _______.", "पृथ्वी से रात्रि के आकाश में दिखने वाला सबसे चमकीला ग्रह _______ है।", "sec_2"),
        ("The largest planet of our Solar System is _______.", "हमारे सौरमंडल का सबसे बड़ा ग्रह _______ है।", "sec_2"),
        ("Celestial bodies that revolve around planets are called ______.", "ग्रहों के चारों ओर परिक्रमा करने वाले खगोलीय पिंडों को _______ कहते हैं।", "sec_2"),
        ("The Pole Star appears stationary in the sky because it lies near the axis of rotation of the Earth.", "ध्रुव तारा आकाश में स्थिर दिखाई देता है क्योंकि यह पृथ्वी की घूर्णन अक्ष की दिशा में स्थित है।", "sec_3"),
        ("The Sun revolves around the Earth in an elliptical orbit.", "सूर्य एक दीर्घवृत्ताकार कक्षा में पृथ्वी के चारों ओर परिक्रमा करता है।", "sec_3"),
        ("Shooting stars are not actually stars; they are small meteors entering Earth's atmosphere.", "टूटते तारे वास्तव में तारे नहीं होते, वे पृथ्वी के वायुमंडल में प्रवेश करने वाले उल्कापिंड होते हैं।", "sec_3"),
        ("INSAT is an Indian artificial satellite used for weather forecasting and communication.", "INSAT एक भारतीय कृत्रिम उपग्रह है जिसका उपयोग मौसम पूर्वानुमान और संचार के लिए किया जाता है।", "sec_3")
    ],
    18: [
        ("The poisonous gas which reduces the oxygen-carrying capacity of blood is carbon _______.", "वह जहरीली गैस जो रक्त की ऑक्सीजन ले जाने की क्षमता को कम करती है, कार्बन _______ है।", "sec_2"),
        ("The phenomenon of trapping heat radiation by Earth's atmosphere is known as the _______ effect.", "पृथ्वी के वायुमंडल द्वारा ऊष्मीय विकिरण को रोक लेने की परिघटना को _______ प्रभाव कहते हैं।", "sec_2"),
        ("The gas layer in the stratosphere that protects living beings from harmful ultraviolet rays is _______.", "समताप मंडल में स्थित वह गैस परत जो सजीवों को हानिकारक पराबैंगनी किरणों से बचाती है, _______ है।", "sec_2"),
        ("Water which is purified, clean and safe for drinking is called _______ water.", "पीने के लिए शुद्ध, स्वच्छ और सुरक्षित जल को _______ जल कहते हैं।", "sec_2"),
        ("Chlorofluorocarbons (CFCs) cause depletion of the protective ozone layer.", "क्लोरोफ्लोरोकार्बन (CFC) सुरक्षात्मक ओजोन परत को क्षति पहुँचाते हैं।", "sec_3"),
        ("Acid rain is caused by excessive levels of sulphur dioxide and nitrogen dioxide gases.", "अम्ल वर्षा सल्फर डाइऑक्साइड और नाइट्रोजन डाइऑक्साइड गैसों के अत्यधिक स्तर के कारण होती है।", "sec_3"),
        ("Glaciers like Gangotri are expanding rapidly due to global warming.", "ग्लोबल वार्मिंग (विश्व ऊष्णन) के कारण गंगोत्री जैसे ग्लेशियर तेजी से बढ़ रहे हैं।", "sec_3"),
        ("Chlorination is a common chemical method used for disinfecting drinking water.", "क्लोरीनीकरण पेयजल को रोगाणुमुक्त करने के लिए व्यापक रूप से उपयोग की जाने वाली एक सामान्य रासायनिक विधि है।", "sec_3")
    ]
}

def extract_all_ch10_to_18():
    extracted = []
    
    for ch_num, ch_name in CH_MAP.items():
        matches = [f for f in os.listdir(sys_dir) if f.startswith(f"Chapter_{ch_num:02d}") or f.startswith(f"Chapter_{ch_num}_")]
        if not matches:
            continue
        filepath = os.path.join(sys_dir, matches[0])
        with open(filepath, "r", encoding="utf-8") as f:
            text = f.read()

        parts = re.split(r'###\s+Part\s+[AB]:', text, flags=re.IGNORECASE)
        mcq_text = parts[1] if len(parts) > 1 else ''
        sa_text = parts[2] if len(parts) > 2 else ''

        # 1. MCQs
        if "#### Q" in mcq_text:
            mcq_blocks = re.split(r'\n(?=####\s+Q\d+\.)', mcq_text)
            idx = 0
            for b in mcq_blocks:
                m = re.search(r'####\s+Q\d+\.\s*(.*?)\s*/\s*(.*?)\n', b)
                if not m:
                    continue
                q_en, q_hi = m.group(1).strip(), m.group(2).strip()
                opts = re.findall(r'\*\s*\(([A-D])\)\s*([^/\n]+)(?:\s*/\s*([^\n]+))?', b)
                if len(opts) == 4:
                    idx += 1
                    opt_lines = []
                    for letter, o_en, o_hi in opts:
                        hi_part = f" / {o_hi.strip()}" if o_hi else ""
                        opt_lines.append(f"({letter.lower()}) {o_en.strip()}{hi_part}")
                    content = f"**{q_en}**  \n**{q_hi}**  \n" + "  \n".join(opt_lines)
                    extracted.append({
                        "id": f"8_sci_ch{ch_num}_mcq_{idx}",
                        "subjectId": "8_science",
                        "sectionKey": "sec_1",
                        "set": "Textbook",
                        "orderInSet": idx,
                        "originalNum": f"Q{idx}",
                        "marks": 1,
                        "hasOrChoice": False,
                        "preview": q_en,
                        "content": content,
                        "chapter": ch_name
                    })
        else:
            mcq_blocks = re.split(r'\n(?=\d+\.\s+\*\*)', mcq_text)
            idx = 0
            for b in mcq_blocks:
                m_en = re.search(r'^\d+\.\s+\*\*(?:Question:\*\*\s*)?(.*?)\n', b)
                m_hi = re.search(r'^\s+\*\*(?:प्रश्न:\*\*\s*)?(.*?)\n', b)
                if not m_en or not m_hi:
                    continue
                q_en, q_hi = m_en.group(1).strip(), m_hi.group(1).strip()
                opts = re.findall(r'\*\s*(?:\(([A-D])\)|([A-D])\))\s*([^/\n]+)(?:\s*/\s*([^\n]+))?', b)
                if len(opts) == 4:
                    idx += 1
                    opt_lines = []
                    for o in opts:
                        letter = (o[0] or o[1]).lower()
                        en_val = o[2].strip()
                        hi_val = f" / {o[3].strip()}" if o[3] else ""
                        opt_lines.append(f"({letter}) {en_val}{hi_val}")
                    content = f"**{q_en}**  \n**{q_hi}**  \n" + "  \n".join(opt_lines)
                    extracted.append({
                        "id": f"8_sci_ch{ch_num}_mcq_{idx}",
                        "subjectId": "8_science",
                        "sectionKey": "sec_1",
                        "set": "Textbook",
                        "orderInSet": idx,
                        "originalNum": f"Q{idx}",
                        "marks": 1,
                        "hasOrChoice": False,
                        "preview": q_en,
                        "content": content,
                        "chapter": ch_name
                    })

        # 2. Short & Long Answers
        if "#### Q" in sa_text:
            sa_blocks = re.split(r'\n(?=####\s+Q\d+\.)', sa_text)
            sa_idx = 0
            for b in sa_blocks:
                m = re.search(r'####\s+Q\d+\.\s*(.*?)\s*/\s*(.*?)\n', b)
                if not m:
                    continue
                q_en, q_hi = m.group(1).strip(), m.group(2).strip()
                sa_idx += 1
                sec_key = "sec_4" if sa_idx <= 4 else ("sec_5" if sa_idx <= 8 else "sec_6")
                marks = 2 if sec_key == "sec_4" else (3 if sec_key == "sec_5" else 5)
                extracted.append({
                    "id": f"8_sci_ch{ch_num}_sa_{sa_idx}",
                    "subjectId": "8_science",
                    "sectionKey": sec_key,
                    "set": "Textbook",
                    "orderInSet": sa_idx,
                    "originalNum": f"Q{sa_idx}",
                    "marks": marks,
                    "hasOrChoice": False,
                    "preview": q_en,
                    "content": f"**{q_en}**  \n**{q_hi}**",
                    "chapter": ch_name
                })
        else:
            sa_blocks = re.split(r'\n(?=\d+\.\s+\*\*)', sa_text)
            sa_idx = 0
            for b in sa_blocks:
                m_en = re.search(r'^\d+\.\s+\*\*(?:Question:\*\*\s*)?(.*?)\n', b)
                m_hi = re.search(r'^\s+\*\*(?:प्रश्न:\*\*\s*)?(.*?)\n', b)
                if not m_en or not m_hi:
                    continue
                q_en, q_hi = m_en.group(1).strip(), m_hi.group(1).strip()
                sa_idx += 1
                sec_key = "sec_4" if sa_idx <= 4 else ("sec_5" if sa_idx <= 8 else "sec_6")
                marks = 2 if sec_key == "sec_4" else (3 if sec_key == "sec_5" else 5)
                extracted.append({
                    "id": f"8_sci_ch{ch_num}_sa_{sa_idx}",
                    "subjectId": "8_science",
                    "sectionKey": sec_key,
                    "set": "Textbook",
                    "orderInSet": sa_idx,
                    "originalNum": f"Q{sa_idx}",
                    "marks": marks,
                    "hasOrChoice": False,
                    "preview": q_en,
                    "content": f"**{q_en}**  \n**{q_hi}**",
                    "chapter": ch_name
                })

        # 3. FIB and TF
        fib_tf = FIB_TF_DATA.get(ch_num, [])
        for f_idx, (en, hi, sec_key) in enumerate(fib_tf, 1):
            q_type = "fib" if sec_key == "sec_2" else "tf"
            extracted.append({
                "id": f"8_sci_ch{ch_num}_{q_type}_{f_idx}",
                "subjectId": "8_science",
                "sectionKey": sec_key,
                "set": "Textbook",
                "orderInSet": f_idx,
                "originalNum": f"Q{f_idx}",
                "marks": 1,
                "hasOrChoice": False,
                "preview": en,
                "content": f"**{en}**  \n**{hi}**",
                "chapter": ch_name
            })

    return extracted

if __name__ == "__main__":
    items = extract_all_ch10_to_18()
    print(f"Extracted {len(items)} questions for Chapters 10 to 18.")
    
    # Ingest into data/questions.json
    ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    q_path = os.path.join(ROOT_DIR, "data", "questions.json")
    with open(q_path, "r", encoding="utf-8") as f:
        db = json.load(f)
        
    existing = db.get("8_science", [])
    existing_ids = set(q["id"] for q in existing)
    
    added = 0
    for it in items:
        if it["id"] not in existing_ids:
            existing.append(it)
            existing_ids.add(it["id"])
            added += 1
            
    db["8_science"] = existing
    with open(q_path, "w", encoding="utf-8") as f:
        json.dump(db, f, indent=2, ensure_ascii=False)
        
    print(f"Added {added} new textbook questions to data/questions.json! Total 8_science questions now: {len(existing)}")
