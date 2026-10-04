import json

with open('data/questions.json', encoding='utf-8') as f:
    data = json.load(f)

for sub_id in ['5_maths', '6_maths', '7_maths', '6_science', '7_science']:
    for q in data[sub_id]:
        if 'OR / अथवा' in q.get('content', ''):
            print(f"=== {sub_id} : {q['id']} ===")
            lines = q['content'].split('\n')
            for i, l in enumerate(lines):
                if 'OR' in l:
                    print(f"  Line {i}: {repr(l)}")
            break
