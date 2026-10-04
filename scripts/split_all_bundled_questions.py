import json
import re
import sys
from chapter_classifier import determine_chapter

def clean_preview(content):
    # Strip markdown and take first 80 chars
    text = re.sub(r'[*#_$`\\]', '', content)
    text = re.sub(r'\s+', ' ', text).strip()
    return text[:90] + ('...' if len(text) > 90 else '')

def split_bundled_questions():
    with open('data/questions.json', encoding='utf-8') as f:
        data = json.load(f)

    new_data = {}
    total_original = 0
    total_split = 0

    for sub_id, q_list in data.items():
        new_list = []
        for q in q_list:
            total_original += 1
            content = q.get('content', '')
            if '**OR / अथवा**' in content:
                parts = re.split(r'\n+\s*\*\*OR\s*/\s*अथवा\*\*\s*\n+', content)
                if len(parts) == 2:
                    p1_content = parts[0].strip()
                    p2_content = parts[1].strip()

                    # Base id and alt id
                    p1_id = q['id']
                    p2_id = f"{q['id']}_alt"

                    # Generate previews
                    p1_preview = clean_preview(p1_content)
                    p2_preview = clean_preview(p2_content)

                    # Determine chapters
                    p1_ch = q.get('chapter') or determine_chapter(sub_id, p1_content, p1_preview)
                    p2_ch = determine_chapter(sub_id, p2_content, p2_preview) or p1_ch

                    q1 = dict(q)
                    q1['id'] = p1_id
                    q1['content'] = p1_content
                    q1['preview'] = p1_preview
                    q1['chapter'] = p1_ch
                    q1['hasOrChoice'] = False
                    q1['defaultOrPartnerId'] = p2_id

                    q2 = dict(q)
                    q2['id'] = p2_id
                    q2['content'] = p2_content
                    q2['preview'] = p2_preview
                    q2['chapter'] = p2_ch
                    q2['hasOrChoice'] = False
                    q2['defaultOrPartnerId'] = p1_id
                    q2['orderInSet'] = q.get('orderInSet', 0) + 0.5

                    new_list.append(q1)
                    new_list.append(q2)
                    total_split += 1
                else:
                    # In case of irregular split, keep as is
                    q['hasOrChoice'] = False
                    new_list.append(q)
            else:
                q['hasOrChoice'] = False
                new_list.append(q)

        new_data[sub_id] = new_list

    with open('data/questions.json', 'w', encoding='utf-8') as f:
        json.dump(new_data, f, indent=2, ensure_ascii=False)

    print(f"Successfully processed {total_original} questions.")
    print(f"Split {total_split} bundled questions into {total_split * 2} standalone questions.")
    print("New question counts per subject:")
    for k, v in new_data.items():
        print(f"  {k}: {len(v)} questions")

if __name__ == '__main__':
    split_bundled_questions()
