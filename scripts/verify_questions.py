import json
import re

def verify():
    with open('data/questions.json', encoding='utf-8') as f:
        data = json.load(f)

    errors = []
    total = 0

    for sub_id, q_list in data.items():
        for q in q_list:
            total += 1
            content = q['content']
            # Check for unclosed single dollars (inline math)
            # Count double dollars first
            dd_count = content.count('$$')
            if dd_count % 2 != 0:
                errors.append(f"Mismatched $$ in {q['id']}: count={dd_count}")
            
            # Remove all $$ blocks before checking single $
            cleaned = re.sub(r'\$\$.*?\$\$', '', content, flags=re.DOTALL)
            single_d_count = cleaned.count('$')
            if single_d_count % 2 != 0:
                errors.append(f"Mismatched single $ in {q['id']}: count={single_d_count}")

            # Check nested $ inside $$ blocks
            for m in re.finditer(r'\$\$(.*?)\$\$', content, flags=re.DOTALL):
                if '$' in m.group(1):
                    errors.append(f"Nested $ inside $$ in {q['id']}")

    print(f"Total questions checked: {total}")
    print(f"Errors found: {len(errors)}")
    for err in errors[:10]:
        print(f"  - {err}")

if __name__ == '__main__':
    verify()
