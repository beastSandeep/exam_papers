import json
import re

def inspect_split():
    with open('data/questions.json', encoding='utf-8') as f:
        data = json.load(f)

    split_counts = {}
    for sub_id, q_list in data.items():
        count = 0
        for q in q_list:
            if 'OR / अथवा' in q.get('content', ''):
                parts = re.split(r'\n+\s*\*\*OR\s*/\s*अथवा\*\*\s*\n+', q['content'])
                count += 1
                if len(parts) != 2:
                    print(f"Warning: {q['id']} split into {len(parts)} parts!")
        split_counts[sub_id] = count

    print("Bundled OR questions count per subject:")
    for k, v in split_counts.items():
        print(f"  {k}: {v}")

if __name__ == '__main__':
    inspect_split()
