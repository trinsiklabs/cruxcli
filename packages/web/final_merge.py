import json
from collections import Counter

# Load all 7 parts
all_questions = []
for i in range(1, 8):
    with open(f'/tmp/comm_q_part{i}.json') as f:
        all_questions.extend(json.load(f))

print(f"Loaded from parts: {len(all_questions)}")

# Add 5 extra questions
extra = [
{
    "dimension": "positive_negative_ratio",
    "question_type": "scenario",
    "text": "You notice your partner did something thoughtful \u2014 left you a note, made your coffee, handled something without being asked. What's your response?",
    "options": [
        {"id": "a", "text": "I thank them specifically and tell them it made my day", "scores": {"positive_negative_ratio": 5}},
        {"id": "b", "text": "I notice it internally but don't always say something", "scores": {"positive_negative_ratio": 2}},
        {"id": "c", "text": "I appreciate it but also think 'why can't it be like this all the time?'", "scores": {"positive_negative_ratio": 2}},
        {"id": "d", "text": "I reciprocate with my own thoughtful gesture", "scores": {"positive_negative_ratio": 4}}
    ],
    "tier_role": "triangulation",
    "trap": False,
    "consistency_group": "appreciation_frequency",
    "opacity": 0.6,
    "cross_scores": [{"assessment": "love_languages", "dimension": "acts_of_service", "weight": 0.4}],
    "universal": True, "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "ratio"]
},
{
    "dimension": "positive_negative_ratio",
    "question_type": "scenario",
    "text": "You're both at dinner with friends. Your partner tells a story you've heard before. What's your instinct?",
    "options": [
        {"id": "a", "text": "Smile and watch them tell it \u2014 they're enjoying themselves and I enjoy watching that", "scores": {"positive_negative_ratio": 5}},
        {"id": "b", "text": "Correct details they got wrong \u2014 accuracy matters", "scores": {"positive_negative_ratio": 1}},
        {"id": "c", "text": "Zone out \u2014 I've heard this one", "scores": {"positive_negative_ratio": 2}},
        {"id": "d", "text": "Add to the story enthusiastically \u2014 we tell it as a team", "scores": {"positive_negative_ratio": 5}}
    ],
    "tier_role": "triangulation",
    "trap": False,
    "consistency_group": "baseline_sentiment",
    "opacity": 0.7,
    "cross_scores": [],
    "universal": True, "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "ratio"]
},
{
    "dimension": "four_horsemen",
    "question_type": "scenario",
    "text": "Your partner brings up a valid complaint and you immediately feel the urge to say 'but what about when you...' What do you actually do?",
    "options": [
        {"id": "a", "text": "Give in to the urge \u2014 their complaint loses validity if they're doing the same thing", "scores": {"four_horsemen": 1}},
        {"id": "b", "text": "Catch the urge and stay with their complaint first \u2014 I can raise mine separately later", "scores": {"four_horsemen": 5}},
        {"id": "c", "text": "Say it but frame it gently \u2014 'I hear you, and I also experience something similar when...'", "scores": {"four_horsemen": 3}},
        {"id": "d", "text": "Go quiet instead \u2014 I swallow the counter-complaint but it sits there", "scores": {"four_horsemen": 2}}
    ],
    "tier_role": "triangulation",
    "trap": False,
    "consistency_group": "defensiveness_pattern",
    "opacity": 0.7,
    "cross_scores": [{"assessment": "conflict_resolution", "dimension": "accountability", "weight": 0.4}],
    "universal": True, "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "defensiveness"]
},
{
    "dimension": "bid_recognition",
    "question_type": "scenario",
    "text": "Your partner says 'Remember when we used to...' and trails off with a wistful look. What do you hear?",
    "options": [
        {"id": "a", "text": "A bid for reconnection \u2014 they miss something we shared and want to recapture it", "scores": {"bid_recognition": 5}},
        {"id": "b", "text": "A criticism in disguise \u2014 they're saying things used to be better", "scores": {"bid_recognition": 2}},
        {"id": "c", "text": "Nostalgia \u2014 nice but not something that requires a response", "scores": {"bid_recognition": 2}},
        {"id": "d", "text": "An invitation \u2014 I follow up: 'Tell me what you're thinking about. What do you miss?'", "scores": {"bid_recognition": 5, "active_listening": 4}}
    ],
    "tier_role": "triangulation",
    "trap": False,
    "consistency_group": "bid_awareness",
    "opacity": 0.7,
    "cross_scores": [{"assessment": "communication_style", "dimension": "active_listening", "weight": 0.4}],
    "universal": True, "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "bids"]
},
{
    "dimension": "active_listening",
    "question_type": "scenario",
    "text": "Your partner says 'I just feel like...' and then struggles to articulate something complicated. What do you do with the silence?",
    "options": [
        {"id": "a", "text": "Wait. Let the silence do its work. They're reaching for something important.", "scores": {"active_listening": 5}},
        {"id": "b", "text": "Offer words: 'Do you mean like...?' \u2014 trying to help them find it", "scores": {"active_listening": 3}},
        {"id": "c", "text": "Get impatient internally \u2014 I wish they could just say what they mean", "scores": {"active_listening": 1}},
        {"id": "d", "text": "Encourage gently: 'Take your time. I'm listening.'", "scores": {"active_listening": 5}}
    ],
    "tier_role": "triangulation",
    "trap": False,
    "consistency_group": "listening_patience",
    "opacity": 0.7,
    "cross_scores": [{"assessment": "emotional_regulation", "dimension": "distress_tolerance", "weight": 0.3}],
    "universal": True, "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "listening"]
}
]

all_questions.extend(extra)

print(f"Final total: {len(all_questions)}")

dim_counts = Counter(q['dimension'] for q in all_questions)
for dim, count in sorted(dim_counts.items()):
    print(f"  {dim}: {count}")

tier_counts = Counter(q['tier_role'] for q in all_questions)
for tier, count in sorted(tier_counts.items()):
    print(f"  {tier}: {count}")

type_counts = Counter(q['question_type'] for q in all_questions)
for qt, count in sorted(type_counts.items()):
    print(f"  {qt}: {count}")

trap_count = sum(1 for q in all_questions if q['trap'])
print(f"  traps: {trap_count}")

# Write final file
outpath = '/Users/user/personal/sb/trueassess/priv/question_bank/communication_style.json'
with open(outpath, 'w') as f:
    json.dump(all_questions, f, indent=2)
print(f"\nWritten {len(all_questions)} questions to {outpath}")

# Validate JSON roundtrip
with open(outpath) as f:
    check = json.load(f)
print(f"Validation: {len(check)} questions loaded back successfully")
