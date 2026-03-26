import json

with open("/Users/user/personal/sb/trueassess/priv/question_bank/conflict_resolution.json") as f:
    questions = json.load(f)

# Add one more collaborating question
questions.append({
    "uid": "cr_120",
    "assessment_id": "conflict_resolution",
    "dimension": "collaborating",
    "question_type": "scenario",
    "text": "Your team is post-morteming a failed project. Blame is flying. You believe multiple people share responsibility, including yourself. How do you handle it?",
    "options": [
        {"id": "a", "text": "Start by owning your part publicly, then invite others to reflect on theirs without blame", "scores": {"collaborating": 5}},
        {"id": "b", "text": "Point out specifically who dropped the ball and when—clarity prevents repeat failures", "scores": {"competing": 5}},
        {"id": "c", "text": "Suggest focusing on process improvements rather than individual blame", "scores": {"compromising": 4, "avoiding": 2}},
        {"id": "d", "text": "Stay quiet—post-mortems are just blame sessions dressed up in process language", "scores": {"avoiding": 5}}
    ],
    "cross_scores": [],
    "anti_gaming": {
        "opacity": 0.7,
        "social_desirability_trap": False,
        "consistency_group": "collab_accountability_1",
        "reversal": False
    },
    "cultural_adaptability": {
        "universal": True,
        "adaptations_needed": [],
        "adaptation_notes": None
    },
    "content_rating": "G",
    "content_categories": [],
    "depth_tier": "moderate",
    "tier_role": "triangulation",
    "tags": ["conflict_resolution", "collaborating", "triangulation", "work"]
})

dim_counts = {}
type_counts = {}
tier_counts = {}
trap_count = 0
for q in questions:
    dim_counts[q["dimension"]] = dim_counts.get(q["dimension"], 0) + 1
    type_counts[q["question_type"]] = type_counts.get(q["question_type"], 0) + 1
    tier_counts[q["tier_role"]] = tier_counts.get(q["tier_role"], 0) + 1
    if q["anti_gaming"]["social_desirability_trap"]:
        trap_count += 1

print(f"Total: {len(questions)}")
print(f"Dimensions: {dim_counts}")
print(f"Types: {type_counts}")
print(f"Tiers: {tier_counts}")
print(f"SD traps: {trap_count}")

with open("/Users/user/personal/sb/trueassess/priv/question_bank/conflict_resolution.json", "w") as f:
    json.dump(questions, f, indent=2)

print("Updated conflict_resolution.json")
