import json
from collections import Counter

# Load all parts
all_questions = []
for i in range(1, 8):
    with open(f'/tmp/comm_q_part{i}.json') as f:
        part = json.load(f)
        all_questions.extend(part)

print(f"Total questions: {len(all_questions)}")

# Count by dimension
dim_counts = Counter(q['dimension'] for q in all_questions)
for dim, count in sorted(dim_counts.items()):
    print(f"  {dim}: {count}")

# Count by tier_role
tier_counts = Counter(q['tier_role'] for q in all_questions)
for tier, count in sorted(tier_counts.items()):
    print(f"  {tier}: {count}")

# Count by question_type
type_counts = Counter(q['question_type'] for q in all_questions)
for qt, count in sorted(type_counts.items()):
    print(f"  {qt}: {count}")

# Count traps
trap_count = sum(1 for q in all_questions if q['trap'])
print(f"  traps: {trap_count}")

print(f"\nNeed {200 - len(all_questions)} more questions")
print(f"\nTarget type distribution: scenario=70, partner_perspective=30, behavioral_recall=30, somatic=25, temporal=25, forced_choice=20")
print(f"Target tier: core=21, triangulation=84, trap=49, consistency=46")
