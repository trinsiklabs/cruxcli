import json

# Load existing
all_questions = []
for i in range(1, 8):
    with open(f'/tmp/comm_q_part{i}.json') as f:
        all_questions.extend(json.load(f))

# Need 5 more: one each for 5 dimensions that have 28 (need 29 each except one at 27 needs 2)
# Actually: 7 dims * 29 = 203, but we want 200. So some dims get 29 and some get 28.
# With 195, need 5 more to hit 200.
# Dims at 28: all except positive_negative_ratio at 27. Need 2 for pos_neg, and 3 others.
# These should be triangulation (need 7 more) and scenario/somatic type.

extra = []

# positive_negative_ratio needs 2 more (to 29) 
extra.append({
    "dimension": "positive_negative_ratio",
    "question_type": "scenario",
    "text": "You notice your partner did something thoughtful — left you a note, made your coffee, handled something without being asked. What's your response?",
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
    "cross_scores": [
        {"assessment": "love_languages", "dimension": "acts_of_service", "weight": 0.4}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "ratio"]
})

extra.append({
    "dimension": "positive_negative_ratio",
    "question_type": "scenario",
    "text": "You're both at dinner with friends. Your partner tells a story you've heard before. What's your instinct?",
    "options": [
        {"id": "a", "text": "Smile and watch them tell it — they're enjoying themselves and I enjoy watching that", "scores": {"positive_negative_ratio": 5}},
        {"id": "b", "text": "Correct details they got wrong — accuracy matters", "scores": {"positive_negative_ratio": 1}},
        {"id": "c", "text": "Zone out — I've heard this one", "scores": {"positive_negative_ratio": 2}},
        {"id": "d", "text": "Add to the story enthusiastically — we tell it as a team", "scores": {"positive_negative_ratio": 5}}
    ],
    "tier_role": "triangulation",
    "trap": False,
    "consistency_group": "baseline_sentiment",
    "opacity": 0.7,
    "cross_scores": [],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "ratio"]
})

# four_horsemen extra
extra.append({
    "dimension": "four_horsemen",
    "question_type": "scenario",
    "text": "Your partner brings up a valid complaint and you immediately feel the urge to say 'but what about when you...' What do you actually do?",
    "options": [
        {"id": "a", "text": "Give in to the urge — their complaint loses validity if they're doing the same thing", "scores": {"four_horsemen": 1}},
        {"id": "b", "text": "Catch the urge and stay with their complaint first — I can raise mine separately later", "scores": {"four_horsemen": 5}},
        {"id": "c", "text": "Say it but frame it gently — 'I hear you, and I also experience something similar when...'", "scores": {"four_horsemen": 3}},
        {"id": "d", "text": "Go quiet instead — I swallow the counter-complaint but it sits there", "scores": {"four_horsemen": 2}}
    ],
    "tier_role": "triangulation",
    "trap": False,
    "consistency_group": "defensiveness_pattern",
    "opacity": 0.7,
    "cross_scores": [
        {"assessment": "conflict_resolution", "dimension": "accountability", "weight": 0.4}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "defensiveness"]
})

# bid_recognition extra
extra.append({
    "dimension": "bid_recognition",
    "question_type": "scenario",
    "text": "Your partner says 'Remember when we used to...' and trails off with a wistful look. What do you hear?",
    "options": [
        {"id": "a", "text": "A bid for reconnection — they miss something we shared and want to recapture it", "scores": {"bid_recognition": 5}},
        {"id": "b", "text": "A criticism in disguise — they're saying things used to be better", "scores": {"bid_recognition": 2}},
        {"id": "c", "text": "Nostalgia — nice but not something that requires a response", "scores": {"bid_recognition": 2}},
        {"id": "d", "text": "An invitation — I follow up: 'Tell me what you're thinking about. What do you miss?'", "scores": {"bid_recognition": 5, "active_listening": 4}}
    ],
    "tier_role": "triangulation",
    "trap": False,
    "consistency_group": "bid_awareness",
    "opacity": 0.7,
    "cross_scores": [
        {"assessment": "communication_style", "dimension": "active_listening", "weight": 0.4}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "bids"]
})

# active_listening extra
extra.append({
    "dimension": "active_listening",
    "question_type": "scenario",
    "text": "Your partner says 'I just feel like...' and then struggles to articulate something complicated. What do you do with the silence?",
    "options": [
        {"id": "a", "text": "Wait. Let the silence do its work. They're reaching for something important.", "scores": {"active_listening": 5}},
        {"id": "b", "text": "Offer words: 'Do you mean like...?' — trying to help them find it", "scores": {"active_listening": 3}},
        {"id": "c", "text": "Get impatient internally — I wish they could just say what they mean", "scores": {"active_listening": 1}},
        {"id": "d", "text": "Encourage gently: 'Take your time. I'm listening.'", "scores": {"active_listening": 5}}
    ],
    "tier_role": "triangulation",
    "trap": False,
    "consistency_group": "listening_patience",
    "opacity": 0.7,
    "cross_scores": [
        {"assessment": "emotional_regulation", "dimension": "distress_tolerance", "weight": 0.3}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "listening"]
})

all_questions.extend(extra)

# Verify final counts
from collections import Counter

print(f"Total: {len(all_questions)}")

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
with open('/Users/user/personal/sb/trueassess/priv/question_bank/communication_style.json', 'w') as f:
    json.dump(all_questions, f, indent=2)
print(f"\nWritten to communication_style.json")
