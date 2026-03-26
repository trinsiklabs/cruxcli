import json

questions = []

# ============================================================
# DIMENSION 7: POSITIVE-NEGATIVE RATIO (28 questions)
# 3 core + 12 triangulation + 7 trap + 6 consistency
# ============================================================

# --- CORE (3) ---
questions.append({
    "dimension": "positive_negative_ratio",
    "question_type": "scenario",
    "text": "You come home after work. In the first 10 minutes of seeing your partner, what's the typical tone of your interaction?",
    "options": [
        {"id": "a", "text": "Warm — a kiss, a 'how was your day?', genuine interest in reconnecting", "scores": {"positive_negative_ratio": 5}},
        {"id": "b", "text": "Functional — logistics about dinner, kids, tasks that need handling", "scores": {"positive_negative_ratio": 3}},
        {"id": "c", "text": "Neutral to negative — complaints about my day, irritation about household things", "scores": {"positive_negative_ratio": 2}},
        {"id": "d", "text": "Avoidant — we each do our own thing without much of a greeting", "scores": {"positive_negative_ratio": 1}}
    ],
    "tier_role": "core",
    "trap": False,
    "consistency_group": "daily_positivity",
    "opacity": 0.6,
    "cross_scores": [
        {"assessment": "communication_style", "dimension": "bid_recognition", "weight": 0.4}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "ratio"]
})

questions.append({
    "dimension": "positive_negative_ratio",
    "question_type": "behavioral_recall",
    "text": "Think about your last full day with your partner. How many times did you express genuine appreciation, affection, or interest vs. how many complaints, criticisms, or irritations?",
    "options": [
        {"id": "a", "text": "Way more positive — probably 5:1 or better", "scores": {"positive_negative_ratio": 5}},
        {"id": "b", "text": "Roughly even — some nice moments, some friction", "scores": {"positive_negative_ratio": 3}},
        {"id": "c", "text": "More negative — the day had more tension than warmth", "scores": {"positive_negative_ratio": 2}},
        {"id": "d", "text": "I honestly don't track this — we're just... coexisting", "scores": {"positive_negative_ratio": 2}}
    ],
    "tier_role": "core",
    "trap": False,
    "consistency_group": "appreciation_frequency",
    "opacity": 0.5,
    "cross_scores": [],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "ratio"]
})

questions.append({
    "dimension": "positive_negative_ratio",
    "question_type": "partner_perspective",
    "text": "If your partner kept a tally of every positive and negative interaction in a typical week, what ratio would they report?",
    "options": [
        {"id": "a", "text": "Overwhelmingly positive — I actively create warmth in our relationship", "scores": {"positive_negative_ratio": 5}},
        {"id": "b", "text": "Positive but with notable negatives — they'd say I'm good but not consistent", "scores": {"positive_negative_ratio": 3}},
        {"id": "c", "text": "Close to even — or worse. The negativity might outweigh what I think", "scores": {"positive_negative_ratio": 2}},
        {"id": "d", "text": "They'd struggle to count many deliberately positive interactions from me", "scores": {"positive_negative_ratio": 1}}
    ],
    "tier_role": "core",
    "trap": False,
    "consistency_group": "daily_positivity",
    "opacity": 0.5,
    "cross_scores": [],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "ratio"]
})

# --- TRIANGULATION (12) ---
questions.append({
    "dimension": "positive_negative_ratio",
    "question_type": "scenario",
    "text": "Your partner just did something perfectly ordinary — made a meal, handled an errand, went about their routine. Do you comment on it?",
    "options": [
        {"id": "a", "text": "Yes — I regularly acknowledge the everyday things they do", "scores": {"positive_negative_ratio": 5}},
        {"id": "b", "text": "Not usually — I comment when something is exceptional, not routine", "scores": {"positive_negative_ratio": 2}},
        {"id": "c", "text": "I should, but I tend to only speak up when something goes wrong", "scores": {"positive_negative_ratio": 1}},
        {"id": "d", "text": "Sometimes — but not as consistently as I'd like", "scores": {"positive_negative_ratio": 3}}
    ],
    "tier_role": "triangulation",
    "trap": False,
    "consistency_group": "appreciation_frequency",
    "opacity": 0.6,
    "cross_scores": [
        {"assessment": "love_languages", "dimension": "words_of_affirmation", "weight": 0.5}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "ratio"]
})

questions.append({
    "dimension": "positive_negative_ratio",
    "question_type": "somatic",
    "text": "When you think about your partner right now — not during a fight, just in general — what feeling dominates?",
    "options": [
        {"id": "a", "text": "Warmth and fondness — I genuinely like this person", "scores": {"positive_negative_ratio": 5}},
        {"id": "b", "text": "Neutral — no strong feeling either way", "scores": {"positive_negative_ratio": 3}},
        {"id": "c", "text": "A mix of affection and frustration — it depends on the day", "scores": {"positive_negative_ratio": 3}},
        {"id": "d", "text": "Tension or disappointment is the first thing that comes up", "scores": {"positive_negative_ratio": 1}}
    ],
    "tier_role": "triangulation",
    "trap": False,
    "consistency_group": "baseline_sentiment",
    "opacity": 0.7,
    "cross_scores": [
        {"assessment": "attachment_style", "dimension": "relationship_security", "weight": 0.5}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "ratio", "somatic"]
})

questions.append({
    "dimension": "positive_negative_ratio",
    "question_type": "temporal",
    "text": "How often do you express admiration or appreciation for your partner to OTHER people (friends, family)?",
    "options": [
        {"id": "a", "text": "Often — I genuinely brag about them and speak well of them", "scores": {"positive_negative_ratio": 5}},
        {"id": "b", "text": "Sometimes — when it comes up naturally", "scores": {"positive_negative_ratio": 3}},
        {"id": "c", "text": "Rarely — I'm more likely to vent about them than praise them", "scores": {"positive_negative_ratio": 1}},
        {"id": "d", "text": "I don't talk about my relationship much to others", "scores": {"positive_negative_ratio": 3}}
    ],
    "tier_role": "triangulation",
    "trap": False,
    "consistency_group": "baseline_sentiment",
    "opacity": 0.6,
    "cross_scores": [],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "ratio", "temporal"]
})

questions.append({
    "dimension": "positive_negative_ratio",
    "question_type": "forced_choice",
    "text": "In a typical day with your partner, which happens more often?",
    "options": [
        {"id": "a", "text": "I express something positive — appreciation, affection, humor, interest", "scores": {"positive_negative_ratio": 5}},
        {"id": "b", "text": "I express something negative — complaint, irritation, criticism, correction", "scores": {"positive_negative_ratio": 1}}
    ],
    "tier_role": "triangulation",
    "trap": False,
    "consistency_group": "daily_positivity",
    "opacity": 0.4,
    "cross_scores": [],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "ratio"]
})

questions.append({
    "dimension": "positive_negative_ratio",
    "question_type": "scenario",
    "text": "Your partner tries on a new outfit and asks what you think. It's not your favorite. What do you say?",
    "options": [
        {"id": "a", "text": "Find something genuine to appreciate: 'I love the color on you' or 'You look great in that cut'", "scores": {"positive_negative_ratio": 5}},
        {"id": "b", "text": "Honest feedback: 'It's not my favorite, but you look good in the blue one'", "scores": {"positive_negative_ratio": 3}},
        {"id": "c", "text": "'It's fine' — noncommittal to avoid negativity", "scores": {"positive_negative_ratio": 2}},
        {"id": "d", "text": "Say something teasing that could land as critical", "scores": {"positive_negative_ratio": 1}}
    ],
    "tier_role": "triangulation",
    "trap": False,
    "consistency_group": "daily_positivity",
    "opacity": 0.7,
    "cross_scores": [],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "ratio"]
})

questions.append({
    "dimension": "positive_negative_ratio",
    "question_type": "behavioral_recall",
    "text": "When was the last time you spontaneously told your partner something you admire about them — not as a repair, but just because you felt it?",
    "options": [
        {"id": "a", "text": "In the last day or two — I do this regularly", "scores": {"positive_negative_ratio": 5}},
        {"id": "b", "text": "Within the past week — it happens but not daily", "scores": {"positive_negative_ratio": 4}},
        {"id": "c", "text": "I can't remember the last time — it's not something I think to do", "scores": {"positive_negative_ratio": 1}},
        {"id": "d", "text": "Recently, but only because things had been tense and I was trying to reconnect", "scores": {"positive_negative_ratio": 2}}
    ],
    "tier_role": "triangulation",
    "trap": False,
    "consistency_group": "appreciation_frequency",
    "opacity": 0.5,
    "cross_scores": [
        {"assessment": "love_languages", "dimension": "words_of_affirmation", "weight": 0.5}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "ratio"]
})

questions.append({
    "dimension": "positive_negative_ratio",
    "question_type": "partner_perspective",
    "text": "Would your partner say you notice and comment on what they do well, or mainly notice and comment on what they do wrong?",
    "options": [
        {"id": "a", "text": "What they do well — I'm generous with praise", "scores": {"positive_negative_ratio": 5}},
        {"id": "b", "text": "A mix — I try to praise but the corrections probably stand out more", "scores": {"positive_negative_ratio": 3}},
        {"id": "c", "text": "What they do wrong — I tend to focus on what needs fixing", "scores": {"positive_negative_ratio": 1}},
        {"id": "d", "text": "Neither — I don't comment much either way", "scores": {"positive_negative_ratio": 2}}
    ],
    "tier_role": "triangulation",
    "trap": False,
    "consistency_group": "appreciation_frequency",
    "opacity": 0.5,
    "cross_scores": [],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "ratio"]
})

questions.append({
    "dimension": "positive_negative_ratio",
    "question_type": "scenario",
    "text": "You're lying in bed at night, reviewing the day. What kind of thoughts about your partner dominate?",
    "options": [
        {"id": "a", "text": "Gratitude — I think about what they did well, moments that made me smile", "scores": {"positive_negative_ratio": 5}},
        {"id": "b", "text": "Planning — logistics for tomorrow, what needs to be discussed", "scores": {"positive_negative_ratio": 3}},
        {"id": "c", "text": "Frustration — replaying things that bothered me", "scores": {"positive_negative_ratio": 1}},
        {"id": "d", "text": "Nothing particular about them — they're just... there", "scores": {"positive_negative_ratio": 2}}
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

questions.append({
    "dimension": "positive_negative_ratio",
    "question_type": "somatic",
    "text": "When your partner walks into the room unexpectedly, is your default physical response more like warmth or more like tension?",
    "options": [
        {"id": "a", "text": "Warmth — a smile, a lift in my chest, glad to see them", "scores": {"positive_negative_ratio": 5}},
        {"id": "b", "text": "Neutral — no particular response", "scores": {"positive_negative_ratio": 3}},
        {"id": "c", "text": "A flicker of tension — wondering what they want or what's wrong now", "scores": {"positive_negative_ratio": 1}},
        {"id": "d", "text": "It genuinely depends on the day and what's been happening between us", "scores": {"positive_negative_ratio": 3}}
    ],
    "tier_role": "triangulation",
    "trap": False,
    "consistency_group": "baseline_sentiment",
    "opacity": 0.8,
    "cross_scores": [
        {"assessment": "attachment_style", "dimension": "relationship_security", "weight": 0.4}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "ratio", "somatic"]
})

questions.append({
    "dimension": "positive_negative_ratio",
    "question_type": "temporal",
    "text": "Has the overall emotional tone of your relationship gotten more positive, more negative, or stayed the same over the last year?",
    "options": [
        {"id": "a", "text": "More positive — we've been investing in each other", "scores": {"positive_negative_ratio": 5}},
        {"id": "b", "text": "About the same — stable, for better or worse", "scores": {"positive_negative_ratio": 3}},
        {"id": "c", "text": "More negative — stress, resentment, or distance has crept in", "scores": {"positive_negative_ratio": 1}},
        {"id": "d", "text": "Hard to say — there have been highs and lows", "scores": {"positive_negative_ratio": 3}}
    ],
    "tier_role": "triangulation",
    "trap": False,
    "consistency_group": "daily_positivity",
    "opacity": 0.5,
    "cross_scores": [],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "ratio", "temporal"]
})

questions.append({
    "dimension": "positive_negative_ratio",
    "question_type": "behavioral_recall",
    "text": "How often do you use humor, playfulness, or inside jokes with your partner in a typical week?",
    "options": [
        {"id": "a", "text": "Daily — humor and play are central to our connection", "scores": {"positive_negative_ratio": 5}},
        {"id": "b", "text": "A few times a week — when the mood is right", "scores": {"positive_negative_ratio": 4}},
        {"id": "c", "text": "Rarely — things have gotten pretty serious between us", "scores": {"positive_negative_ratio": 2}},
        {"id": "d", "text": "Almost never — humor feels forced or inappropriate given where we are", "scores": {"positive_negative_ratio": 1}}
    ],
    "tier_role": "triangulation",
    "trap": False,
    "consistency_group": "daily_positivity",
    "opacity": 0.6,
    "cross_scores": [],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "ratio"]
})

# --- TRAP (7) ---
questions.append({
    "dimension": "positive_negative_ratio",
    "question_type": "scenario",
    "text": "I don't need to constantly tell my partner I appreciate them — they already know how I feel.",
    "options": [
        {"id": "a", "text": "Exactly — we don't need constant verbal affirmation", "scores": {"positive_negative_ratio": 1}},
        {"id": "b", "text": "Probably true, but expressing it still matters even when it's already known", "scores": {"positive_negative_ratio": 3}},
        {"id": "c", "text": "I've learned the hard way that unexpressed appreciation might as well not exist", "scores": {"positive_negative_ratio": 5}},
        {"id": "d", "text": "I show it in other ways — actions, not words", "scores": {"positive_negative_ratio": 2}}
    ],
    "tier_role": "trap",
    "trap": True,
    "consistency_group": "appreciation_frequency",
    "opacity": 0.9,
    "cross_scores": [
        {"assessment": "love_languages", "dimension": "words_of_affirmation", "weight": 0.4}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "ratio", "trap"]
})

questions.append({
    "dimension": "positive_negative_ratio",
    "question_type": "partner_perspective",
    "text": "My partner doesn't need praise for doing things that are just part of being an adult. I shouldn't have to thank them for basic responsibilities.",
    "options": [
        {"id": "a", "text": "Correct — praise for basics is patronizing", "scores": {"positive_negative_ratio": 1}},
        {"id": "b", "text": "I see the logic, but expressing gratitude for everyday things builds connection regardless", "scores": {"positive_negative_ratio": 4}},
        {"id": "c", "text": "Research shows appreciation for the mundane is one of the strongest relationship predictors", "scores": {"positive_negative_ratio": 5}},
        {"id": "d", "text": "I only praise above-and-beyond efforts — otherwise it feels fake", "scores": {"positive_negative_ratio": 2}}
    ],
    "tier_role": "trap",
    "trap": True,
    "consistency_group": "appreciation_frequency",
    "opacity": 0.9,
    "cross_scores": [],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "ratio", "trap"]
})

questions.append({
    "dimension": "positive_negative_ratio",
    "question_type": "forced_choice",
    "text": "Honest feedback — even when it's critical — is more valuable to a relationship than empty compliments.",
    "options": [
        {"id": "a", "text": "Strongly agree — I'd rather be truthfully critical than falsely positive", "scores": {"positive_negative_ratio": 1}},
        {"id": "b", "text": "Somewhat agree — but the RATIO matters: criticism without a foundation of positivity is corrosive", "scores": {"positive_negative_ratio": 4}},
        {"id": "c", "text": "Somewhat disagree — most couples don't need more honesty, they need more kindness", "scores": {"positive_negative_ratio": 5}},
        {"id": "d", "text": "Strongly disagree — an atmosphere of appreciation makes criticism easier to receive", "scores": {"positive_negative_ratio": 5}}
    ],
    "tier_role": "trap",
    "trap": True,
    "consistency_group": "baseline_sentiment",
    "opacity": 0.9,
    "cross_scores": [
        {"assessment": "four_horsemen", "dimension": "four_horsemen", "weight": 0.3}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "ratio", "trap"]
})

questions.append({
    "dimension": "positive_negative_ratio",
    "question_type": "behavioral_recall",
    "text": "I focus on improving our relationship by addressing problems. Fixing what's broken is more productive than praising what works.",
    "options": [
        {"id": "a", "text": "Absolutely — problem-solving is how relationships improve", "scores": {"positive_negative_ratio": 1}},
        {"id": "b", "text": "Problem-solving matters, but reinforcing what's good is equally important for growth", "scores": {"positive_negative_ratio": 4}},
        {"id": "c", "text": "I've noticed that my focus on problems makes the relationship feel more negative than it actually is", "scores": {"positive_negative_ratio": 5}},
        {"id": "d", "text": "Both matter, but I admit I'm more naturally oriented toward fixing than appreciating", "scores": {"positive_negative_ratio": 3}}
    ],
    "tier_role": "trap",
    "trap": True,
    "consistency_group": "baseline_sentiment",
    "opacity": 0.9,
    "cross_scores": [],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "ratio", "trap"]
})

questions.append({
    "dimension": "positive_negative_ratio",
    "question_type": "scenario",
    "text": "We're past the 'honeymoon phase' — it's normal for the constant affection and appreciation to settle into something more... practical.",
    "options": [
        {"id": "a", "text": "Exactly — mature love is practical, not performative", "scores": {"positive_negative_ratio": 2}},
        {"id": "b", "text": "Some settling is normal, but the 5:1 ratio isn't a honeymoon phenomenon — it's a lifelong need", "scores": {"positive_negative_ratio": 5}},
        {"id": "c", "text": "I worry that 'practical' is code for 'we stopped investing in each other'", "scores": {"positive_negative_ratio": 4}},
        {"id": "d", "text": "We've maintained warmth — it just looks different now than early on", "scores": {"positive_negative_ratio": 4}}
    ],
    "tier_role": "trap",
    "trap": True,
    "consistency_group": "daily_positivity",
    "opacity": 0.9,
    "cross_scores": [
        {"assessment": "attachment_style", "dimension": "relationship_security", "weight": 0.3}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "ratio", "trap"]
})

questions.append({
    "dimension": "positive_negative_ratio",
    "question_type": "partner_perspective",
    "text": "My partner knows I love them by how I provide, protect, or show up — not by how many nice things I say.",
    "options": [
        {"id": "a", "text": "Exactly — love is demonstrated through actions, not words", "scores": {"positive_negative_ratio": 2}},
        {"id": "b", "text": "Actions matter, but verbal positivity has its own irreplaceable impact", "scores": {"positive_negative_ratio": 4}},
        {"id": "c", "text": "I should ask my partner which they actually need more — actions or words", "scores": {"positive_negative_ratio": 4}},
        {"id": "d", "text": "Both are necessary — neither substitutes for the other", "scores": {"positive_negative_ratio": 5}}
    ],
    "tier_role": "trap",
    "trap": True,
    "consistency_group": "appreciation_frequency",
    "opacity": 0.9,
    "cross_scores": [
        {"assessment": "love_languages", "dimension": "words_of_affirmation", "weight": 0.4},
        {"assessment": "love_languages", "dimension": "acts_of_service", "weight": 0.3}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "ratio", "trap"]
})

questions.append({
    "dimension": "positive_negative_ratio",
    "question_type": "scenario",
    "text": "I try to be positive, but my partner makes it hard — they don't acknowledge my efforts either, so why should I keep putting in the work?",
    "options": [
        {"id": "a", "text": "Fair point — appreciation should be reciprocal", "scores": {"positive_negative_ratio": 2}},
        {"id": "b", "text": "Understandable frustration, but someone has to break the negative cycle first", "scores": {"positive_negative_ratio": 4}},
        {"id": "c", "text": "Maybe they stopped acknowledging because they felt unappreciated first — and waiting for reciprocity is a losing strategy", "scores": {"positive_negative_ratio": 5}},
        {"id": "d", "text": "We're both responsible for the emotional climate, regardless of what the other is doing", "scores": {"positive_negative_ratio": 5}}
    ],
    "tier_role": "trap",
    "trap": True,
    "consistency_group": "baseline_sentiment",
    "opacity": 0.8,
    "cross_scores": [],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "ratio", "trap"]
})

# --- CONSISTENCY CHECK (6) ---
questions.append({
    "dimension": "positive_negative_ratio",
    "question_type": "scenario",
    "text": "When you describe your partner to a stranger, what's the first thing you mention?",
    "options": [
        {"id": "a", "text": "Something I admire — their humor, intelligence, kindness, or talent", "scores": {"positive_negative_ratio": 5}},
        {"id": "b", "text": "Something practical — their job, role, what they do", "scores": {"positive_negative_ratio": 3}},
        {"id": "c", "text": "It depends on my mood and what's been happening between us", "scores": {"positive_negative_ratio": 3}},
        {"id": "d", "text": "I might inadvertently lead with a complaint or frustration — 'My partner, who can never...'", "scores": {"positive_negative_ratio": 1}}
    ],
    "tier_role": "consistency_check",
    "trap": False,
    "consistency_group": "baseline_sentiment",
    "opacity": 0.6,
    "cross_scores": [],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "ratio", "consistency"]
})

questions.append({
    "dimension": "positive_negative_ratio",
    "question_type": "behavioral_recall",
    "text": "In the last 24 hours, did you initiate any physical affection with your partner that wasn't sexual — a hug, a kiss, a hand on their back?",
    "options": [
        {"id": "a", "text": "Multiple times — physical affection is part of our daily rhythm", "scores": {"positive_negative_ratio": 5}},
        {"id": "b", "text": "Once or twice — when it felt natural", "scores": {"positive_negative_ratio": 4}},
        {"id": "c", "text": "No — it didn't cross my mind", "scores": {"positive_negative_ratio": 2}},
        {"id": "d", "text": "No — we're not in a place where physical affection feels natural right now", "scores": {"positive_negative_ratio": 1}}
    ],
    "tier_role": "consistency_check",
    "trap": False,
    "consistency_group": "daily_positivity",
    "opacity": 0.5,
    "cross_scores": [
        {"assessment": "love_languages", "dimension": "physical_touch", "weight": 0.4}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "ratio", "consistency"]
})

questions.append({
    "dimension": "positive_negative_ratio",
    "question_type": "forced_choice",
    "text": "If you had to characterize the overall emotional climate of your relationship right now in one word:",
    "options": [
        {"id": "a", "text": "Warm", "scores": {"positive_negative_ratio": 5}},
        {"id": "b", "text": "Cool", "scores": {"positive_negative_ratio": 2}},
        {"id": "c", "text": "Stormy", "scores": {"positive_negative_ratio": 1}},
        {"id": "d", "text": "Neutral", "scores": {"positive_negative_ratio": 3}}
    ],
    "tier_role": "consistency_check",
    "trap": False,
    "consistency_group": "baseline_sentiment",
    "opacity": 0.4,
    "cross_scores": [],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "ratio", "consistency"]
})

questions.append({
    "dimension": "positive_negative_ratio",
    "question_type": "partner_perspective",
    "text": "Would your partner say that being around you generally lifts their mood, has no effect, or brings them down?",
    "options": [
        {"id": "a", "text": "Lifts their mood — I bring energy, warmth, or humor to our interactions", "scores": {"positive_negative_ratio": 5}},
        {"id": "b", "text": "No strong effect — I'm a steady, neutral presence", "scores": {"positive_negative_ratio": 3}},
        {"id": "c", "text": "Depends on the day — I can be uplifting or draining", "scores": {"positive_negative_ratio": 3}},
        {"id": "d", "text": "They might say I bring stress or negativity more often than I'd like to admit", "scores": {"positive_negative_ratio": 1}}
    ],
    "tier_role": "consistency_check",
    "trap": False,
    "consistency_group": "daily_positivity",
    "opacity": 0.5,
    "cross_scores": [],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "ratio", "consistency"]
})

questions.append({
    "dimension": "positive_negative_ratio",
    "question_type": "somatic",
    "text": "When you catch yourself being genuinely appreciative of your partner — a spontaneous feeling of gratitude — how often does that happen?",
    "options": [
        {"id": "a", "text": "Daily — I regularly feel grateful for them", "scores": {"positive_negative_ratio": 5}},
        {"id": "b", "text": "Weekly — it happens but isn't constant", "scores": {"positive_negative_ratio": 3}},
        {"id": "c", "text": "Rarely — gratitude isn't the dominant feeling these days", "scores": {"positive_negative_ratio": 2}},
        {"id": "d", "text": "It's been a while since I felt a genuine spontaneous wave of appreciation", "scores": {"positive_negative_ratio": 1}}
    ],
    "tier_role": "consistency_check",
    "trap": False,
    "consistency_group": "appreciation_frequency",
    "opacity": 0.7,
    "cross_scores": [],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "ratio", "consistency"]
})

questions.append({
    "dimension": "positive_negative_ratio",
    "question_type": "temporal",
    "text": "Compare how you greeted your partner at the beginning of your relationship vs. now. How has it changed?",
    "options": [
        {"id": "a", "text": "Still warm and enthusiastic — I make reconnecting a priority", "scores": {"positive_negative_ratio": 5}},
        {"id": "b", "text": "Less enthusiastic but still positive — a kiss or a 'hey' vs. the old running hug", "scores": {"positive_negative_ratio": 4}},
        {"id": "c", "text": "Minimal — we barely acknowledge each other coming and going now", "scores": {"positive_negative_ratio": 1}},
        {"id": "d", "text": "It depends on whether there's unresolved tension", "scores": {"positive_negative_ratio": 2}}
    ],
    "tier_role": "consistency_check",
    "trap": False,
    "consistency_group": "daily_positivity",
    "opacity": 0.5,
    "cross_scores": [],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "ratio", "consistency"]
})

with open('/tmp/comm_q_part7.json', 'w') as f:
    json.dump(questions, f, indent=2)
print(f"Part 7: {len(questions)} positive_negative_ratio questions written")
