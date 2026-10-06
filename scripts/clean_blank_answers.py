# scripts/clean_blank_answers.py
import json, re, sys, os, glob

sys.stdout.reconfigure(encoding='utf-8')

QUESTIONS_PATH = os.path.join("data", "questions.json")

def clean_text(text):
    if not text:
        return text
    # 1. Patterns like _______ (answer) or (answer) _______
    cleaned = re.sub(r'(_{2,})\s*\([^)\n]+\)', r'\1', text)
    cleaned = re.sub(r'\([^)\n]+\)\s*(_{2,})', r'\1', cleaned)
    # 2. Specific Hindi leaked answers
    specific_answers = [
        "जंग", "दीर्घरोम", "यशद लेपन", "पारा", "रूमेन", "किशोरावस्था",
        "कुचालक", "चाल", "समकोण", "सममिति", "द्विपद", "एकपदी", "त्रिपद"
    ]
    for ans in specific_answers:
        cleaned = re.sub(rf'(_{{2,}}\s*[^.\n]*?)\s*\({re.escape(ans)}\)', r'\1', cleaned)
        cleaned = re.sub(rf'\s*\({re.escape(ans)}\)\s*(_{{2,}})', r' \1', cleaned)
    return cleaned

def clean_database():
    with open(QUESTIONS_PATH, "r", encoding="utf-8") as f:
        db = json.load(f)

    cleaned_count = 0
    for sub, qlist in db.items():
        for q in qlist:
            orig = q.get("content", "")
            # Only clean if blanks exist
            if "_" in orig:
                new_c = clean_text(orig)
                if new_c != orig:
                    cleaned_count += 1
                    q["content"] = new_c
                    # Also clean preview if needed
                    if "preview" in q:
                        q["preview"] = clean_text(q["preview"])

    with open(QUESTIONS_PATH, "w", encoding="utf-8") as f:
        json.dump(db, f, indent=2, ensure_ascii=False)

    print(f"Cleaned {cleaned_count} questions in {QUESTIONS_PATH}")

def clean_markdown_files():
    md_files = glob.glob("*/*.md")
    total_md_cleaned = 0
    for md in md_files:
        with open(md, "r", encoding="utf-8") as f:
            content = f.read()
        new_content = clean_text(content)
        if new_content != content:
            total_md_cleaned += 1
            with open(md, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"Cleaned blanks in markdown file: {md}")
    print(f"Total markdown files cleaned: {total_md_cleaned}")

if __name__ == "__main__":
    clean_database()
    clean_markdown_files()
