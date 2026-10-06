import os, json, re

# Define chapters for each subject
CHAPTERS_MAP = {
    "5_maths": [
        "Ch 1: The Fish Tale (मछली उछली)",
        "Ch 2: Shapes and Angles (आकृतियाँ और कोण)",
        "Ch 3: How Many Squares? (कितने वर्ग?)",
        "Ch 4: Parts and Wholes (हिस्से और पूरे)",
        "Ch 5: Does it Look the Same? (क्या यह एक जैसा दिखता है?)",
        "Ch 6: Multiples and Factors (गुणज और गुणनखंड)",
        "Ch 7: Can You See the Pattern? (पैटर्न)",
        "Ch 8: Mapping Your Way (नक्शा)",
        "Ch 9: Boxes and Sketches (डिब्बे और रेखाचित्र)",
        "Ch 10: Tenths and Hundredths (दसवाँ और सौवाँ भाग)",
        "Ch 11: Area and its Boundary (क्षेत्रफल और घेरा)",
        "Ch 13: Ways to Multiply and Divide (गुणा और भाग)"
    ],
    "6_maths": [
        "Ch 4: Playing with Numbers (संख्याओं के साथ खेलना)",
        "Ch 5: Integers (पूर्णांक)",
        "Ch 6: Fractions (भिन्न)",
        "Ch 7: Decimals (दशमलव)",
        "Ch 8: Introduction to Algebra (बीजगणित)",
        "Ch 9: Symmetry and Geometry (सममिति एवं ज्यामिति)"
    ],
    "7_maths": [
        "Ch 5: Exponents and Powers (घातांक और घात)",
        "Ch 7: Comparing Quantities (राशियों की तुलना)",
        "Ch 9: Rational Numbers (परिमेय संख्याएँ)",
        "Ch 11: Perimeter, Area & Speed (परिमाप, क्षेत्रफल एवं चाल)",
        "Ch 12: Algebraic Expressions (बीजीय व्यंजक)",
        "Ch 14: Symmetry (सममिति)",
        "Ch 15: Visualising Solid Shapes (ठोस आकारों का चित्रण)"
    ],
    "6_science": [
        "Ch 5: Measurement & Motion (गति एवं दूरियों का मापन)",
        "Ch 6: Sorting Materials (पदार्थों का समूहन)",
        "Ch 7: Temperature and Heat (तापमान एवं ऊष्मा)",
        "Ch 8: Water in the Atmosphere (जल एवं जलवाष्प)",
        "Ch 9: Separation of Substances (पदार्थों का पृथक्करण)"
    ],
    "7_science": [
        "Ch 5: Physical and Chemical Changes (भौतिक एवं रासायनिक परिवर्तन)",
        "Ch 6: Reaching the Age of Adolescence (किशोरावस्था)",
        "Ch 7: Heat & Transfer of Heat (ऊष्मा एवं स्थानांतरण)",
        "Ch 8: Motion and Time (गति एवं समय)",
        "Ch 9: Nutrition & Respiration in Organisms (पोषण एवं श्वसन)"
    ],
    "8_science": [
        "Ch 1: Crop Production and Management (फसल उत्पादन एवं प्रबंध)",
        "Ch 2: Microorganisms: Friend and Foe (सूक्ष्मजीव: मित्र एवं शत्रु)",
        "Ch 3: Coal and Petroleum (कोयला और पेट्रोलियम)",
        "Ch 4: Combustion and Flame (दहन और ज्वाला)",
        "Ch 5: Conservation of Plants and Animals (पौधे एवं जंतुओं का संरक्षण)",
        "Ch 6: Reproduction in Animals (जंतुओं में जनन)",
        "Ch 7: Reaching the Age of Adolescence (किशोरावस्था की ओर)",
        "Ch 8: Force and Pressure (बल तथा दाब)",
        "Ch 9: Friction (घर्षण)"
    ]
}

def determine_chapter(subject_id, content, preview):
    text = (content + " " + preview).lower()
    
    if subject_id == "5_maths":
        if any(k in text for k in ["boat", "fish", "मछली", "speed", "लक्खा", "lakh", "crore"]):
            return "Ch 1: The Fish Tale (मछली उछली)"
        if any(k in text for k in ["angle", "कोण", "right angle", "समकोण", "acute", "obtuse", "clock", "घड़ी"]):
            return "Ch 2: Shapes and Angles (आकृतियाँ और कोण)"
        if any(k in text for k in ["tile", "carpet", "square", "rectangle", "how many squares", "वर्ग"]):
            return "Ch 3: How Many Squares? (कितने वर्ग?)"
        if any(k in text for k in ["fraction", "भिन्न", "shaded", "chocolates", "pizza", "half", "quarter"]):
            return "Ch 4: Parts and Wholes (हिस्से और पूरे)"
        if any(k in text for k in ["turn", "घूर्णन", "mirror", "reflection", "प्रतिबिंब", "symmetry", "सममिति"]):
            return "Ch 5: Does it Look the Same? (क्या यह एक जैसा दिखता है?)"
        if any(k in text for k in ["multiple", "factor", "गुणज", "गुणनखंड", "lcm", "hcf"]):
            return "Ch 6: Multiples and Factors (गुणज और गुणनखंड)"
        if any(k in text for k in ["pattern", "पैटर्न", "magic square", "जादुई वर्ग", "sequence"]):
            return "Ch 7: Can You See the Pattern? (पैटर्न)"
        if any(k in text for k in ["map", "नक्शा", "scale", "पैमाना", "ground"]):
            return "Ch 8: Mapping Your Way (नक्शा)"
        if any(k in text for k in ["cube", "cuboid", "box", "net", "डिब्बे", "घन", "घनाभ", "vertices", "edges"]):
            return "Ch 9: Boxes and Sketches (डिब्बे और रेखाचित्र)"
        if any(k in text for k in ["decimal", "दशमलव", "paise", "rupee", "पैसे", "millimetre", "tenths", "hundredths"]):
            return "Ch 10: Tenths and Hundredths (दसवाँ और सौवाँ भाग)"
        if any(k in text for k in ["perimeter", "boundary", "घेरा", "क्षेत्रफल", "cost of carpeting"]):
            return "Ch 11: Area and its Boundary (क्षेत्रफल और घेरा)"
        if any(k in text for k in ["multiply", "divide", "गुणा", "भाग", "carton", "apples"]):
            return "Ch 13: Ways to Multiply and Divide (गुणा और भाग)"
        return "Ch 1: The Fish Tale (मछली उछली)"

    elif subject_id == "6_maths":
        if any(k in text for k in ["prime", "composite", "hcf", "lcm", "factor", "multiple", "अभाज्य", "भाज्य", "म.स.प.", "bracket", "divisible", "विभाज्य"]):
            return "Ch 4: Playing with Numbers (संख्याओं के साथ खेलना)"
        if any(k in text for k in ["integer", "पूर्णांक", "number line", "संख्या रेखा", "predecessor", "additive inverse", "योज्य प्रतिलोम"]):
            return "Ch 5: Integers (पूर्णांक)"
        if any(k in text for k in ["fraction", "भिन्न", "numerator", "denominator", "equivalent", "तुल्य"]):
            return "Ch 6: Fractions (भिन्न)"
        if any(k in text for k in ["decimal", "दशमलव", "place value table", "स्थानीय मान", "petrol", "sugar", "rupees"]):
            return "Ch 7: Decimals (दशमलव)"
        if any(k in text for k in ["algebra", "बीजगणित", "variable", "coefficient", "चर", "गुणांक", "expression", "व्यंजक", "term"]):
            return "Ch 8: Introduction to Algebra (बीजगणित)"
        if any(k in text for k in ["symmetry", "सममिति", "mirror", "angle", "line"]):
            return "Ch 9: Symmetry and Geometry (सममिति एवं ज्यामिति)"
        return "Ch 4: Playing with Numbers (संख्याओं के साथ खेलना)"

    elif subject_id == "7_maths":
        if any(k in text for k in ["exponent", "power", "घात", "घातांक", "a^m", "base", "आधार"]):
            return "Ch 5: Exponents and Powers (घातांक और घात)"
        if any(k in text for k in ["percent", "प्रतिशत", "profit", "loss", "cost price", "selling price", "लाभ", "हानि", "क्रय मूल्य", "विक्रय मूल्य"]):
            return "Ch 7: Comparing Quantities (राशियों की तुलना)"
        if any(k in text for k in ["rational", "परिमेय", "reciprocal", "व्युत्क्रम", "multiplicative inverse"]):
            return "Ch 9: Rational Numbers (परिमेय संख्याएँ)"
        if any(k in text for k in ["speed", "distance", "time", "चाल", "दूरी", "समय", "train", "car", "km/h", "area", "perimeter", "parallelogram", "triangle", "circle", "वृत्त", "परिधि", "circumference"]):
            return "Ch 11: Perimeter, Area & Speed (परिमाप, क्षेत्रफल एवं चाल)"
        if any(k in text for k in ["algebra", "polynomial", "बहुपद", "term", "व्यंजक", "if x =", "if m ="]):
            return "Ch 12: Algebraic Expressions (बीजीय व्यंजक)"
        if any(k in text for k in ["symmetry", "सममिति", "rotational", "घूर्णन", "mirror image", "दर्पण"]):
            return "Ch 14: Symmetry (सममिति)"
        if any(k in text for k in ["cuboid", "cube", "isometric", "रेखाचित्र", "dice", "net", "फलक"]):
            return "Ch 15: Visualising Solid Shapes (ठोस आकारों का चित्रण)"
        return "Ch 5: Exponents and Powers (घातांक और घात)"

    elif subject_id == "6_science":
        if any(k in text for k in ["motion", "गति", "metre", "length", "लंबाई", "ruler", "distance"]):
            return "Ch 5: Measurement & Motion (गति एवं दूरियों का मापन)"
        if any(k in text for k in ["opaque", "transparent", "translucent", "lustre", "hardness", "पदार्थ", "पारदर्शी", "अपारदर्शी"]):
            return "Ch 6: Sorting Materials (पदार्थों का समूहन)"
        if any(k in text for k in ["thermometer", "temperature", "तापमान", "थर्मामीटर", "celsius", "fahrenheit"]):
            return "Ch 7: Temperature and Heat (तापमान एवं ऊष्मा)"
        if any(k in text for k in ["water cycle", "जल चक्र", "evaporation", "condensation", "वाष्पीकरण", "संघनन", "cloud", "बादल"]):
            return "Ch 8: Water in the Atmosphere (जल एवं जलवाष्प)"
        if any(k in text for k in ["separation", "winnowing", "sieving", "filtration", "sedimentation", "decantation", "threshing", "पृथक्करण"]):
            return "Ch 9: Separation of Substances (पदार्थों का पृथक्करण)"
        return "Ch 5: Measurement & Motion (गति एवं दूरियों का मापन)"

    elif subject_id == "7_science":
        if any(k in text for k in ["chemical change", "physical change", "rust", "जंग", "magnesium", "lime water", "galvanis"]):
            return "Ch 5: Physical and Chemical Changes (भौतिक एवं रासायनिक परिवर्तन)"
        if any(k in text for k in ["adolescence", "puberty", "किशोरावस्था", "यौवनारंभ", "hormone", "adam's apple"]):
            return "Ch 6: Reaching the Age of Adolescence (किशोरावस्था)"
        if any(k in text for k in ["heat", "conduction", "convection", "radiation", "चालन", "संवहन", "विकिरण", "breeze"]):
            return "Ch 7: Heat & Transfer of Heat (ऊष्मा एवं स्थानांतरण)"
        if any(k in text for k in ["pendulum", "लोलक", "speedometer", "odometer", "time period", "आवर्तकाल", "uniform motion"]):
            return "Ch 8: Motion and Time (गति एवं समय)"
        if any(k in text for k in ["digestion", "पाचन", "stomach", "intestine", "villi", "bile", "आमाशय", "आंत", "amoeba", "assimilation"]):
            return "Ch 9: Nutrition & Respiration in Organisms (पोषण एवं श्वसन)"
        return "Ch 5: Physical and Chemical Changes (भौतिक एवं रासायनिक परिवर्तन)"

    return "General"

print("Chapter classifier ready.")
