# scripts/extract_textbook_questions.py
# Comprehensive Textbook Question Extractor & Integrator for all classes
import os, sys, json, re

sys.stdout.reconfigure(encoding='utf-8')

BLUEPRINTS_PATH = os.path.join("data", "blueprints.json")
QUESTIONS_PATH = os.path.join("data", "questions.json")

# Chapter mappings for 8th Science
CH_NAMES_8_SCI = {
    1: "Ch 1: Crop Production and Management (फसल उत्पादन एवं प्रबंध)",
    2: "Ch 2: Microorganisms: Friend and Foe (सूक्ष्मजीव: मित्र एवं शत्रु)",
    3: "Ch 3: Coal and Petroleum (कोयला और पेट्रोलियम)",
    4: "Ch 4: Combustion and Flame (दहन और ज्वाला)",
    5: "Ch 5: Conservation of Plants and Animals (पौधे एवं जंतुओं का संरक्षण)",
    6: "Ch 6: Reproduction in Animals (जंतुओं में जनन)",
    7: "Ch 7: Reaching the Age of Adolescence (किशोरावस्था की ओर)",
    8: "Ch 8: Force and Pressure (बल तथा दाब)",
    9: "Ch 9: Friction (घर्षण)"
}

def extract_8th_science():
    source_dir = r"F:\8th Science\questions"
    extracted = []
    
    for ch_num in range(1, 10):
        ch_name = CH_NAMES_8_SCI[ch_num]
        
        # Locate file
        matching_files = [
            f for f in os.listdir(source_dir)
            if f.startswith(f"Chapter_0{ch_num}") or f.startswith(f"Chapter_{ch_num}_")
        ]
        if not matching_files:
            continue
        filepath = os.path.join(source_dir, matching_files[0])
        
        with open(filepath, "r", encoding="utf-8") as f:
            text = f.read()
            
        if ch_num <= 7:
            # Parse format for Chapters 1-7
            parts = re.split(r'###\s+PART\s+[AB]:', text, flags=re.IGNORECASE)
            mcq_text = parts[1] if len(parts) > 1 else ''
            sa_text = parts[2] if len(parts) > 2 else ''
            
            # --- Part A: MCQs ---
            mcq_blocks = re.split(r'\n(?=\*\*Q\d+\.)', mcq_text)
            mcq_idx = 0
            for b in mcq_blocks:
                if not b.strip() or not b.strip().startswith('**Q'):
                    continue
                q_en_m = re.search(r'\*\*Q\d+\.\s*(.*?)\*\*', b)
                q_hi_m = re.search(r'\*\*प्रश्न\s*\d+\.\s*(.*?)\*\*', b)
                if not q_en_m or not q_hi_m:
                    continue
                q_en = q_en_m.group(1).strip()
                q_hi = q_hi_m.group(1).strip()
                opts = re.findall(r'\*\s*Option\s*([A-D]):\s*([^\n]+)', b)
                if len(opts) == 4:
                    mcq_idx += 1
                    content = (
                        f"**{q_en}**  \n"
                        f"**{q_hi}**  \n"
                        f"(a) {opts[0][1].strip()}  \n"
                        f"(b) {opts[1][1].strip()}  \n"
                        f"(c) {opts[2][1].strip()}  \n"
                        f"(d) {opts[3][1].strip()}"
                    )
                    extracted.append({
                        "id": f"8_sci_ch{ch_num}_mcq_{mcq_idx}",
                        "subjectId": "8_science",
                        "sectionKey": "sec_1",
                        "set": "Textbook",
                        "orderInSet": mcq_idx,
                        "originalNum": f"Q{mcq_idx}",
                        "marks": 1,
                        "hasOrChoice": False,
                        "preview": q_en,
                        "content": content,
                        "chapter": ch_name
                    })

            # --- Part B: Short & Long Answers ---
            sa_blocks = re.split(r'\n(?=\*\*Q\d+\.)', sa_text)
            sa_idx = 0
            for b in sa_blocks:
                if not b.strip() or not b.strip().startswith('**Q'):
                    continue
                q_en_m = re.search(r'\*\*Q\d+\.\s*(.*?)\*\*', b)
                q_hi_m = re.search(r'\*\*प्रश्न\s*\d+\.\s*(.*?)\*\*', b)
                if not q_en_m or not q_hi_m:
                    continue
                q_en = q_en_m.group(1).strip()
                q_hi = q_hi_m.group(1).strip()
                sa_idx += 1
                
                content = f"**{q_en}**  \n**{q_hi}**"
                
                # Distribute short answers across sec_4 (VSA: 2M), sec_5 (SA: 3M), sec_6 (LA: 5M)
                if sa_idx <= 6:
                    sec_key = "sec_4"
                    marks = 2
                elif sa_idx <= 14:
                    sec_key = "sec_5"
                    marks = 3
                else:
                    sec_key = "sec_6"
                    marks = 5
                    
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
                    "content": content,
                    "chapter": ch_name
                })
                
        else:
            # Parse format for Chapters 8-9
            parts = re.split(r'###\s+Part\s+[AB]:', text, flags=re.IGNORECASE)
            mcq_text = parts[1] if len(parts) > 1 else ''
            sa_text = parts[2] if len(parts) > 2 else ''
            
            blocks = re.split(r'\n(?=\d+\.\s+\*\*Question:)', mcq_text)
            mcq_idx = 0
            for b in blocks:
                if not b.strip() or not re.match(r'^\d+\.\s+\*\*Question:', b.strip()):
                    continue
                q_en_m = re.search(r'\*\*Question:\*\*\s*(.*?)\n', b)
                q_hi_m = re.search(r'\*\*प्रश्न:\*\*\s*(.*?)\n', b)
                if not q_en_m or not q_hi_m:
                    continue
                q_en = q_en_m.group(1).strip()
                q_hi = q_hi_m.group(1).strip()
                opts = re.findall(r'\*\s*([A-D])\)\s*([^\n]+)', b)
                if len(opts) == 4:
                    mcq_idx += 1
                    content = (
                        f"**{q_en}**  \n"
                        f"**{q_hi}**  \n"
                        f"(a) {opts[0][1].strip()}  \n"
                        f"(b) {opts[1][1].strip()}  \n"
                        f"(c) {opts[2][1].strip()}  \n"
                        f"(d) {opts[3][1].strip()}"
                    )
                    extracted.append({
                        "id": f"8_sci_ch{ch_num}_mcq_{mcq_idx}",
                        "subjectId": "8_science",
                        "sectionKey": "sec_1",
                        "set": "Textbook",
                        "orderInSet": mcq_idx,
                        "originalNum": f"Q{mcq_idx}",
                        "marks": 1,
                        "hasOrChoice": False,
                        "preview": q_en,
                        "content": content,
                        "chapter": ch_name
                    })

            sa_blocks = re.split(r'\n(?=\d+\.\s+\*\*Question:)', sa_text)
            sa_idx = 0
            for b in sa_blocks:
                if not b.strip() or not re.match(r'^\d+\.\s+\*\*Question:', b.strip()):
                    continue
                q_en_m = re.search(r'\*\*Question:\*\*\s*(.*?)\n', b)
                q_hi_m = re.search(r'\*\*प्रश्न:\*\*\s*(.*?)\n', b)
                if not q_en_m or not q_hi_m:
                    continue
                q_en = q_en_m.group(1).strip()
                q_hi = q_hi_m.group(1).strip()
                sa_idx += 1
                content = f"**{q_en}**  \n**{q_hi}**"
                
                if sa_idx <= 3:
                    sec_key = "sec_4"
                    marks = 2
                elif sa_idx <= 7:
                    sec_key = "sec_5"
                    marks = 3
                else:
                    sec_key = "sec_6"
                    marks = 5
                    
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
                    "content": content,
                    "chapter": ch_name
                })
                
        # Generate Core Fill in Blanks (sec_2: 1M) & True/False (sec_3: 1M) for each chapter
        tb_fib_tf = get_8th_science_fib_tf(ch_num, ch_name)
        extracted.extend(tb_fib_tf)

    return extracted

def get_8th_science_fib_tf(ch_num, ch_name):
    items = []
    
    FIB_TF_DATA = {
        1: [
            # FIB
            ("The same kind of plants grown and cultivated on a large scale at a place is called _______.",
             "एक ही स्थान पर बड़े पैमाने पर उगाए जाने वाले एक ही किस्म के पौधों को _______ कहते हैं।", "sec_2"),
            ("The first step before growing crops is _______ of the soil.",
             "फसल उगाने से पहले प्रथम चरण मिट्टी की _______ करना है।", "sec_2"),
            ("Damaged seeds would _______ on top of water.",
             "क्षतिग्रस्त बीज जल की सतह पर _______ लगेंगे।", "sec_2"),
            ("For growing a crop, sufficient sunlight and _______ and _______ from the soil are essential.",
             "फसल उगाने के लिए पर्याप्त सूर्य का प्रकाश एवं मिट्टी से _______ तथा _______ आवश्यक हैं।", "sec_2"),
            # TF
            ("Kharif crops are sown in the winter season.",
             "खरीफ फसलें शीत ऋतु में बोई जाती हैं।", "sec_3"),
            ("Manure is an inorganic salt obtained from chemical factories.",
             "खाद एक अकार्बनिक लवण है जो रासायनिक कारखानों से प्राप्त होता है।", "sec_3"),
            ("Drip irrigation is the best technique for watering fruit plants and gardens.",
             "ड्रिप (बूंद-बूंद) सिंचाई फलदार पौधों और बगीचों को पानी देने की सबसे अच्छी विधि है।", "sec_3"),
            ("Weeds are undesirable plants that grow naturally along with the crop.",
             "खरपतवार वे अवांछित पौधे हैं जो फसल के साथ प्राकृतिक रूप से उग आते हैं।", "sec_3")
        ],
        2: [
            # FIB
            ("Microorganisms can be seen with the help of a _______.",
             "सूक्ष्मजीवों को _______ की सहायता से देखा जा सकता है।", "sec_2"),
            ("Blue green algae fix _______ directly from air and enhance fertility of soil.",
             "नीले-हरे शैवाल सीधे वायु से _______ का स्थिरीकरण करते हैं जिससे मिट्टी की उर्वरता बढ़ती है।", "sec_2"),
            ("Alcohol is produced with the help of _______.",
             "अल्कोहल का उत्पादन _______ की सहायता से किया जाता है।", "sec_2"),
            ("Cholera is caused by _______.",
             "हैजा _______ द्वारा फैलता है।", "sec_2"),
            # TF
            ("Yeast reproduces rapidly and produces oxygen gas during respiration.",
             "यीस्ट तीव्रता से जनन करता है और श्वसन के दौरान ऑक्सीजन गैस उत्पादित करता है।", "sec_3"),
            ("Antibiotics are effective against viral infections like common cold.",
             "एंटीबायोटिक्स जुकाम जैसे वायरल संक्रमण के विरुद्ध अत्यधिक प्रभावी होते हैं।", "sec_3"),
            ("Lactobacillus bacterium promotes the formation of curd from milk.",
             "लैक्टोबैसिलस जीवाणु दूध से दही बनने को बढ़ावा देता है।", "sec_3"),
            ("Female Anopheles mosquito acts as a carrier of the malaria parasite.",
             "मादा एनोफिलीज मच्छर मलेरिया परजीवी का वाहक होती है।", "sec_3")
        ],
        3: [
            # FIB
            ("Fossil fuels are coal, petroleum and _______.",
             "जीवाश्म ईंधन कोयला, पेट्रोलियम और _______ हैं।", "sec_2"),
            ("Process of separation of different constituents from petroleum is called _______.",
             "पेट्रोलियम के विभिन्न संघटकों को पृथक करने का प्रक्रम _______ कहलाता है।", "sec_2"),
            ("Least polluting fuel for vehicles is _______.",
             "वाहनों के लिए सबसे कम प्रदूषक ईंधन _______ है।", "sec_2"),
            ("The slow process of conversion of dead vegetation into coal is called _______.",
             "मृत वनस्पति के धीमे प्रक्रम द्वारा कोयले में परिवर्तन को _______ कहते हैं।", "sec_2"),
            # TF
            ("Fossil fuels can be made in the laboratory within a few weeks.",
             "जीवाश्म ईंधन को प्रयोगशाला में कुछ ही हफ्तों में बनाया जा सकता है।", "sec_3"),
            ("CNG is more polluting fuel than petrol.",
             "सीएनजी पेट्रोल की तुलना में अधिक प्रदूषणकारी ईंधन है।", "sec_3"),
            ("Coke is an almost pure form of carbon.",
             "कोक कार्बन का लगभग शुद्ध रूप है।", "sec_3"),
            ("Coal tar is a mixture of various substances used in surfacing roads and dyes.",
             "कोलतार विभिन्न पदार्थों का मिश्रण है जिसका उपयोग सड़कों के निर्माण और रंजक में होता है।", "sec_3")
        ],
        4: [
            # FIB
            ("The lowest temperature at which a substance catches fire is called its _______ temperature.",
             "वह न्यूनतम तापमान जिस पर कोई पदार्थ आग पकड़ता है, उसका _______ तापमान कहलाता है।", "sec_2"),
            ("Substances which have very low ignition temperature are called _______ substances.",
             "जिन पदार्थों का ज्वलन ताप बहुत कम होता है, उन्हें _______ पदार्थ कहते हैं।", "sec_2"),
            ("The middle zone of a candle flame is _______ in colour and is luminous.",
             "मोमबत्ती की ज्वाला का मध्य क्षेत्र _______ रंग का और दीप्त होता है।", "sec_2"),
            ("The amount of heat energy produced on complete combustion of 1 kg of fuel is its _______ value.",
             "1 किग्रा ईंधन के पूर्ण दहन से उत्पन्न ऊष्मा ऊर्जा की मात्रा उसका _______ मान कहलाती है।", "sec_2"),
            # TF
            ("Water is the best extinguishing agent for fires involving electrical equipment.",
             "विद्युत उपकरणों में लगी आग के लिए पानी सबसे अच्छा अग्निशामक है।", "sec_3"),
            ("LPG has a higher calorific value than wood.",
             "एलपीजी का ऊष्मीय मान लकड़ी से अधिक होता है।", "sec_3"),
            ("Carbon monoxide is a harmless gas produced during incomplete combustion.",
             "कार्बन मोनोऑक्साइड अपूर्ण दहन से उत्पन्न होने वाली एक हानिरहित गैस है।", "sec_3"),
            ("The non-luminous zone of a flame is the hottest part.",
             "ज्वाला का अदीप्त (बाहरी) क्षेत्र सबसे गर्म भाग होता है।", "sec_3")
        ],
        5: [
            # FIB
            ("A place where animals are protected in their natural habitat is called a _______.",
             "वह स्थान जहाँ जंतु अपने प्राकृतिक आवास में सुरक्षित रहते हैं, _______ कहलाता है।", "sec_2"),
            ("Species found only in a particular area are known as _______ species.",
             "किसी विशेष क्षेत्र में ही पाई जाने वाली प्रजातियों को _______ प्रजाति कहते हैं।", "sec_2"),
            ("Migratory birds fly to faraway places because of _______ changes.",
             "प्रवासी पक्षी _______ परिवर्तनों के कारण सुदूर स्थानों तक उड़कर जाते हैं।", "sec_2"),
            ("The source book which keeps a record of all endangered animals and plants is _______.",
             "सभी संकटापन्न जंतुओं और पौधों का रिकॉर्ड रखने वाली पुस्तक _______ है।", "sec_2"),
            # TF
            ("Deforestation leads to an increase in groundwater level.",
             "वनोन्मूलन से भौम जल स्तर में वृद्धि होती है।", "sec_3"),
            ("Endemic species are found everywhere on Earth.",
             "स्थानिक (Endemic) प्रजातियाँ पृथ्वी पर सभी जगह पाई जाती हैं।", "sec_3"),
            ("Biosphere reserves help to maintain the biodiversity and culture of that area.",
             "जैवमंडल आरक्षित क्षेत्र उस क्षेत्र की जैव विविधता और संस्कृति को बनाए रखने में मदद करते हैं।", "sec_3"),
            ("Reforestation is the restocking of destroyed forests by planting new trees.",
             "पुनर्वनरोपण नष्ट हुए वनों को नए पेड़ लगाकर पुनः स्थापित करना है।", "sec_3")
        ],
        6: [
            # FIB
            ("The fusion of ovum and sperm is called _______.",
             "अंडाणु और शुक्राणु का संलयन _______ कहलाता है।", "sec_2"),
            ("Internal fertilization occurs inside the _______ body.",
             "आंतरिक निषेचन _______ के शरीर के अंदर होता है।", "sec_2"),
            ("A tadpole develops into an adult frog through the process of _______.",
             "टैडपोल का कायांतरण द्वारा वयस्क मेंढक में विकसित होना _______ कहलाता है।", "sec_2"),
            ("The stage of embryo in which all body parts can be identified is called a _______.",
             "भ्रूण की वह अवस्था जिसमें सभी शारीरिक अंगों की पहचान हो सकती है, _______ कहलाती है।", "sec_2"),
            # TF
            ("Oviparous animals give birth to young ones directly.",
             "अंडप्रजक जंतु सीधे शिशुओं को जन्म देते हैं।", "sec_3"),
            ("Each sperm is a single cell containing nucleus and other cell components.",
             "प्रत्येक शुक्राणु एक एकल कोशिका है जिसमें केंद्रक और अन्य घटक होते हैं।", "sec_3"),
            ("External fertilization takes place in hens.",
             "मुर्गी में बाह्य निषेचन होता है।", "sec_3"),
            ("Amoeba reproduces by budding.",
             "अमीबा मुकुलन द्वारा जनन करता है।", "sec_3")
        ],
        7: [
            # FIB
            ("The period of life when the body undergoes changes leading to reproductive maturity is _______.",
             "जीवन का वह काल जब शरीर में प्रजनन परिपक्वता लाने वाले परिवर्तन होते हैं, _______ कहलाता है।", "sec_2"),
            ("The chemical substances secreted by endocrine glands are called _______.",
             "अंतःस्रावी ग्रंथियों द्वारा स्रावित रासायनिक पदार्थों को _______ कहते हैं।", "sec_2"),
            ("The master gland that controls the secretion of other endocrine glands is the _______ gland.",
             "अन्य अंतःस्रावी ग्रंथियों के स्राव को नियंत्रित करने वाली मास्टर ग्रंथि _______ ग्रंथि है।", "sec_2"),
            ("The male hormone released by testes at the onset of puberty is _______.",
             "यौवनारंभ के समय वृषण द्वारा स्रावित होने वाला पुरुष हार्मोन _______ है।", "sec_2"),
            # TF
            ("The onset of puberty in human females occurs around 45 to 50 years of age.",
             "मानव मादाओं में यौवनारंभ 45 से 50 वर्ष की आयु के आसपास होता है।", "sec_3"),
            ("Insulin hormone deficiency causes diabetes.",
             "इंसुलिन हार्मोन की कमी से मधुमेह (डायबिटीज) रोग होता है।", "sec_3"),
            ("Adolescents need a balanced diet rich in proteins, carbohydrates and iron.",
             "किशोरों को प्रोटीन, कार्बोहाइड्रेट और आयरन से भरपूर संतुलित आहार की आवश्यकता होती है।", "sec_3"),
            ("Adam's apple is the protruding voice box (larynx) seen in boys during puberty.",
             "एडम्स एप्पल लड़कों में यौवनारंभ के दौरान उभरा हुआ स्वर यंत्र (लैरिंक्स) होता है।", "sec_3")
        ],
        8: [
            # FIB
            ("A push or a pull on an object is called a _______.",
             "किसी वस्तु पर लगने वाले धक्के या खिंचाव को _______ कहते हैं।", "sec_2"),
            ("Force acting on a unit area of a surface is called _______.",
             "प्रति एकांक क्षेत्रफल पर लगने वाले बल को _______ कहते हैं।", "sec_2"),
            ("Atmospheric pressure _______ as we go higher into the atmosphere.",
             "वायुमंडल में ऊपर जाने पर वायुमंडलीय दाब _______ जाता है।", "sec_2"),
            ("The SI unit of force is _______.",
             "बल का अंतर्राष्ट्रीय (SI) मात्रक _______ है।", "sec_2"),
            # TF
            ("Forces applied on an object in opposite directions add to each other.",
             "विपरीत दिशाओं में किसी वस्तु पर लगाए गए बल एक-दूसरे से जुड़ जाते हैं।", "sec_3"),
            ("Liquids exert pressure on the walls of the container.",
             "द्रव बर्तन की दीवारों पर दाब डालते हैं।", "sec_3"),
            ("Magnetic force is a contact force.",
             "चुंबकीय बल एक संपर्क बल है।", "sec_3"),
            ("A non-zero net force can change the direction of motion of a moving body.",
             "एक अशून्य कुल बल गतिमान वस्तु की गति की दिशा को बदल सकता है।", "sec_3")
        ],
        9: [
            # FIB
            ("Friction opposes the _______ motion between two surfaces in contact.",
             "घर्षण संपर्क में आने वाली दो सतहों के बीच _______ गति का विरोध करता है।", "sec_2"),
            ("Friction produces _______ when two hands are rubbed together.",
             "दोनों हाथों को आपस में रगड़ने पर घर्षण _______ उत्पन्न करता है।", "sec_2"),
            ("Sprinkling powder on the carrom board _______ friction.",
             "कैरम बोर्ड पर पाउडर छिड़कने से घर्षण _______ जाता है।", "sec_2"),
            ("Sliding friction is slightly _______ than static friction.",
             "सर्पी घर्षण स्थैतिक घर्षण से थोड़ा _______ होता है।", "sec_2"),
            # TF
            ("Friction can never be entirely eliminated.",
             "घर्षण को कभी भी पूरी तरह समाप्त नहीं किया जा सकता।", "sec_3"),
            ("Ball bearings increase friction in machine shafts.",
             "बॉल बेयरिंग मशीन के शाफ्ट में घर्षण को बढ़ाते हैं।", "sec_3"),
            ("Fluids exert frictional force called drag on objects moving through them.",
             "तरल पदार्थ अपने से होकर गति करने वाली वस्तुओं पर घर्षण बल लगाते हैं जिसे ड्रैग कहते हैं।", "sec_3"),
            ("Friction between vehicle tyres and road is essential for safe driving.",
             "सुरक्षित ड्राइविंग के लिए वाहन के टायरों और सड़क के बीच घर्षण आवश्यक है।", "sec_3")
        ]
    }
    
    data = FIB_TF_DATA.get(ch_num, [])
    for idx, (en, hi, sec_key) in enumerate(data, 1):
        q_type = "fib" if sec_key == "sec_2" else "tf"
        content = f"**{en}**  \n**{hi}**"
        items.append({
            "id": f"8_sci_ch{ch_num}_{q_type}_{idx}",
            "subjectId": "8_science",
            "sectionKey": sec_key,
            "set": "Textbook",
            "orderInSet": idx,
            "originalNum": f"Q{idx}",
            "marks": 1,
            "hasOrChoice": False,
            "preview": en,
            "content": content,
            "chapter": ch_name
        })
        
    return items

def update_blueprints():
    with open(BLUEPRINTS_PATH, "r", encoding="utf-8") as f:
        bps = json.load(f)
        
    bps["8_science"] = {
        "id": "8_science",
        "name": "Class 8 Science (विज्ञान)",
        "class": "VIII",
        "subject": "SCIENCE (विज्ञान)",
        "time": "2½ HOURS",
        "maxMarks": 50,
        "isScience": True,
        "schoolName": "NEW M.V.M. SENIOR SECONDARY SCHOOL, ALWAR",
        "examTitle": "HALF YEARLY EXAMINATION: 2026 – 27",
        "sections": [
            {
                "key": "sec_1",
                "title": "### SECTION 1 / खंड 1",
                "subTitle": "Tick (✓) the correct answer in answer sheet / उत्तर पुस्तिका में सही उत्तर पर सही (✓) का निशान लगाएँ",
                "marksEach": 1,
                "requiredCount": 5,
                "totalMarks": 5
            },
            {
                "key": "sec_2",
                "title": "### SECTION 2 / खंड 2",
                "subTitle": "Fill in the blanks / रिक्त स्थानों की पूर्ति कीजिए",
                "marksEach": 1,
                "requiredCount": 5,
                "totalMarks": 5
            },
            {
                "key": "sec_3",
                "title": "### SECTION 3 / खंड 3",
                "subTitle": "State whether the given statements are True (T) or False (F) / बताएँ कि निम्नलिखित कथन सत्य (T) हैं या असत्य (F)",
                "marksEach": 1,
                "requiredCount": 5,
                "totalMarks": 5
            },
            {
                "key": "sec_4",
                "title": "### SECTION 4 / खंड 4",
                "subTitle": "Very Short Answer type questions / अति लघु उत्तरीय प्रश्न",
                "marksEach": 2,
                "requiredCount": 5,
                "totalMarks": 10
            },
            {
                "key": "sec_5",
                "title": "### SECTION 5 / खंड 5",
                "subTitle": "Short Answer type questions / लघु उत्तरीय प्रश्न",
                "marksEach": 3,
                "requiredCount": 5,
                "totalMarks": 15
            },
            {
                "key": "sec_6",
                "title": "### SECTION 6 / खंड 6",
                "subTitle": "Long Answer type questions / दीर्घ उत्तरीय प्रश्न",
                "marksEach": 5,
                "requiredCount": 2,
                "totalMarks": 10
            }
        ]
    }
    
    with open(BLUEPRINTS_PATH, "w", encoding="utf-8") as f:
        json.dump(bps, f, indent=2, ensure_ascii=False)
    print("blueprints.json updated with 8_science!")

if __name__ == "__main__":
    print("Extracting Class 8 Science questions...")
    extracted_8 = extract_8th_science()
    print(f"Extracted {len(extracted_8)} questions for Class 8 Science!")
    
    update_blueprints()
    
    with open(QUESTIONS_PATH, "r", encoding="utf-8") as f:
        q_db = json.load(f)
        
    q_db["8_science"] = extracted_8
    
    with open(QUESTIONS_PATH, "w", encoding="utf-8") as f:
        json.dump(q_db, f, indent=2, ensure_ascii=False)
        
    print(f"Saved {len(extracted_8)} questions into data/questions.json under 8_science!")
