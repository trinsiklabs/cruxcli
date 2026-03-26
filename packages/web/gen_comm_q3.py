import json

questions = []

# ============================================================
# DIMENSION 3: REPAIR REPERTOIRE (29 questions)
# 3 core + 12 triangulation + 7 trap + 7 consistency
# ============================================================

# --- CORE (3) ---
questions.append({
    "dimension": "repair_repertoire",
    "question_type": "scenario",
    "text": "An argument with your partner just got more heated than it should have. You both said things. The dust is settling. What's your next move?",
    "options": [
        {"id": "a", "text": "I go to them within the hour and say 'That got away from us. Can we try again?'", "scores": {"repair_repertoire": 5}},
        {"id": "b", "text": "I wait for them to come to me — I don't want to seem weak", "scores": {"repair_repertoire": 1}},
        {"id": "c", "text": "I act normal and let time smooth it over — no need to rehash", "scores": {"repair_repertoire": 2}},
        {"id": "d", "text": "I do something nice for them — make coffee, handle a chore — without directly addressing it", "scores": {"repair_repertoire": 3}}
    ],
    "tier_role": "core",
    "trap": False,
    "consistency_group": "repair_initiation",
    "opacity": 0.6,
    "cross_scores": [
        {"assessment": "conflict_resolution", "dimension": "repair_willingness", "weight": 0.6}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "repair"]
})

questions.append({
    "dimension": "repair_repertoire",
    "question_type": "behavioral_recall",
    "text": "Think about the last time you successfully de-escalated a tense moment with your partner. What did you do?",
    "options": [
        {"id": "a", "text": "Used humor — made us both laugh and broke the tension", "scores": {"repair_repertoire": 5}},
        {"id": "b", "text": "Said something like 'I love you even when we're fighting' or reached out physically", "scores": {"repair_repertoire": 5}},
        {"id": "c", "text": "I honestly can't think of a recent time I successfully de-escalated", "scores": {"repair_repertoire": 1}},
        {"id": "d", "text": "I suggested a break — 'Let's pause and come back to this'", "scores": {"repair_repertoire": 4}}
    ],
    "tier_role": "core",
    "trap": False,
    "consistency_group": "repair_range",
    "opacity": 0.6,
    "cross_scores": [
        {"assessment": "emotional_regulation", "dimension": "de_escalation_skill", "weight": 0.5}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "repair"]
})

questions.append({
    "dimension": "repair_repertoire",
    "question_type": "partner_perspective",
    "text": "After a fight, would your partner say you're good at making things right between you?",
    "options": [
        {"id": "a", "text": "Yes — I have multiple ways to reconnect and they know I'll try", "scores": {"repair_repertoire": 5}},
        {"id": "b", "text": "Sometimes — I can repair but it's hit-or-miss", "scores": {"repair_repertoire": 3}},
        {"id": "c", "text": "They'd say I expect things to just blow over on their own", "scores": {"repair_repertoire": 2}},
        {"id": "d", "text": "They'd say I apologize quickly but don't always mean it deeply", "scores": {"repair_repertoire": 2}}
    ],
    "tier_role": "core",
    "trap": False,
    "consistency_group": "repair_effectiveness",
    "opacity": 0.5,
    "cross_scores": [
        {"assessment": "attachment_style", "dimension": "secure_base", "weight": 0.4}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "repair"]
})

# --- TRIANGULATION (12) ---
questions.append({
    "dimension": "repair_repertoire",
    "question_type": "scenario",
    "text": "You realize mid-argument that you're wrong. What do you actually do — not what you'd like to do?",
    "options": [
        {"id": "a", "text": "Say it out loud: 'You know what, I think you're right. I was wrong about this.'", "scores": {"repair_repertoire": 5}},
        {"id": "b", "text": "Quietly shift my position without explicitly admitting I was wrong", "scores": {"repair_repertoire": 3}},
        {"id": "c", "text": "Keep arguing — I'll acknowledge it later when things are calmer", "scores": {"repair_repertoire": 2}},
        {"id": "d", "text": "Change the subject — the important thing is stopping the fight", "scores": {"repair_repertoire": 2}}
    ],
    "tier_role": "triangulation",
    "trap": False,
    "consistency_group": "repair_initiation",
    "opacity": 0.6,
    "cross_scores": [
        {"assessment": "self_worth", "dimension": "vulnerability_tolerance", "weight": 0.5}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "repair"]
})

questions.append({
    "dimension": "repair_repertoire",
    "question_type": "somatic",
    "text": "After an unresolved argument, when you're lying in bed next to your partner in silence, what does your body feel?",
    "options": [
        {"id": "a", "text": "An ache — I want to reach over and touch them but something holds me back", "scores": {"repair_repertoire": 3}},
        {"id": "b", "text": "Tension — the silence feels heavy and wrong", "scores": {"repair_repertoire": 3}},
        {"id": "c", "text": "Numbness — I've detached to protect myself", "scores": {"repair_repertoire": 1}},
        {"id": "d", "text": "An urge to break the ice — I reach out or say something", "scores": {"repair_repertoire": 5}}
    ],
    "tier_role": "triangulation",
    "trap": False,
    "consistency_group": "repair_initiation",
    "opacity": 0.8,
    "cross_scores": [
        {"assessment": "attachment_style", "dimension": "proximity_seeking", "weight": 0.5}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "repair", "somatic"]
})

questions.append({
    "dimension": "repair_repertoire",
    "question_type": "temporal",
    "text": "How long does it typically take you and your partner to reconnect after a significant disagreement?",
    "options": [
        {"id": "a", "text": "Minutes to hours — one of us always initiates repair quickly", "scores": {"repair_repertoire": 5}},
        {"id": "b", "text": "A day or so — we need space but come back together", "scores": {"repair_repertoire": 3}},
        {"id": "c", "text": "Days — sometimes things just sit unresolved for a while", "scores": {"repair_repertoire": 2}},
        {"id": "d", "text": "We don't really 'reconnect' — we just move on and the tension fades", "scores": {"repair_repertoire": 1}}
    ],
    "tier_role": "triangulation",
    "trap": False,
    "consistency_group": "repair_effectiveness",
    "opacity": 0.5,
    "cross_scores": [
        {"assessment": "conflict_resolution", "dimension": "resolution_timeline", "weight": 0.6}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "repair", "temporal"]
})

questions.append({
    "dimension": "repair_repertoire",
    "question_type": "forced_choice",
    "text": "After a fight, I'm more likely to:",
    "options": [
        {"id": "a", "text": "Use words — apologize, explain, or ask to start over", "scores": {"repair_repertoire": 4}},
        {"id": "b", "text": "Use actions — make a gesture, do something thoughtful, or initiate physical closeness", "scores": {"repair_repertoire": 4}}
    ],
    "tier_role": "triangulation",
    "trap": False,
    "consistency_group": "repair_range",
    "opacity": 0.5,
    "cross_scores": [
        {"assessment": "love_languages", "dimension": "acts_of_service", "weight": 0.3}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "repair"]
})

questions.append({
    "dimension": "repair_repertoire",
    "question_type": "scenario",
    "text": "You made a joke during an argument and your partner got more upset. They said 'This isn't funny.' What do you do?",
    "options": [
        {"id": "a", "text": "Immediately apologize — 'You're right, I shouldn't have joked. I'm taking this seriously.'", "scores": {"repair_repertoire": 5}},
        {"id": "b", "text": "Explain I was trying to lighten things, not dismiss them", "scores": {"repair_repertoire": 3}},
        {"id": "c", "text": "Feel rejected — I was trying to de-escalate and they shut me down", "scores": {"repair_repertoire": 2}},
        {"id": "d", "text": "Go quiet — my one repair tool just failed and I don't have a backup", "scores": {"repair_repertoire": 1}}
    ],
    "tier_role": "triangulation",
    "trap": False,
    "consistency_group": "repair_range",
    "opacity": 0.7,
    "cross_scores": [
        {"assessment": "emotional_regulation", "dimension": "flexibility", "weight": 0.4}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "repair"]
})

questions.append({
    "dimension": "repair_repertoire",
    "question_type": "behavioral_recall",
    "text": "When your partner attempts to repair after an argument — they apologize, crack a joke, or reach out — how do you respond?",
    "options": [
        {"id": "a", "text": "I accept it readily — I'm grateful they're trying", "scores": {"repair_repertoire": 5}},
        {"id": "b", "text": "I need a moment, but I eventually meet them halfway", "scores": {"repair_repertoire": 4}},
        {"id": "c", "text": "I sometimes reject their attempts — I'm not ready yet and it feels forced", "scores": {"repair_repertoire": 2}},
        {"id": "d", "text": "It depends on whether I think the repair is genuine", "scores": {"repair_repertoire": 3}}
    ],
    "tier_role": "triangulation",
    "trap": False,
    "consistency_group": "repair_receptivity",
    "opacity": 0.6,
    "cross_scores": [
        {"assessment": "forgiveness_profile", "dimension": "repair_acceptance", "weight": 0.5}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "repair"]
})

questions.append({
    "dimension": "repair_repertoire",
    "question_type": "partner_perspective",
    "text": "When you apologize to your partner, would they say your apologies are genuine and specific — or vague and performative?",
    "options": [
        {"id": "a", "text": "Genuine and specific — I name what I did and why it was wrong", "scores": {"repair_repertoire": 5}},
        {"id": "b", "text": "Well-intentioned but sometimes vague — 'I'm sorry you feel that way'", "scores": {"repair_repertoire": 2}},
        {"id": "c", "text": "Too quick — they'd say I apologize to end the conflict, not because I've processed it", "scores": {"repair_repertoire": 2}},
        {"id": "d", "text": "Rare — I don't apologize often, but when I do, I mean it", "scores": {"repair_repertoire": 3}}
    ],
    "tier_role": "triangulation",
    "trap": False,
    "consistency_group": "repair_effectiveness",
    "opacity": 0.5,
    "cross_scores": [
        {"assessment": "self_worth", "dimension": "accountability", "weight": 0.4}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "repair"]
})

questions.append({
    "dimension": "repair_repertoire",
    "question_type": "scenario",
    "text": "You snapped at your partner over something minor. You realize it within seconds. What do you do?",
    "options": [
        {"id": "a", "text": "Immediately catch myself: 'Sorry — that came out wrong. I didn't mean it like that.'", "scores": {"repair_repertoire": 5}},
        {"id": "b", "text": "Feel bad but keep going — stopping to apologize mid-conversation feels awkward", "scores": {"repair_repertoire": 2}},
        {"id": "c", "text": "Make a mental note to apologize later when the moment passes", "scores": {"repair_repertoire": 3}},
        {"id": "d", "text": "Hope they didn't notice or weren't bothered by it", "scores": {"repair_repertoire": 1}}
    ],
    "tier_role": "triangulation",
    "trap": False,
    "consistency_group": "repair_initiation",
    "opacity": 0.6,
    "cross_scores": [
        {"assessment": "emotional_regulation", "dimension": "real_time_correction", "weight": 0.5}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "repair"]
})

questions.append({
    "dimension": "repair_repertoire",
    "question_type": "somatic",
    "text": "When you're the one who needs to apologize, what happens in your body as you approach that moment?",
    "options": [
        {"id": "a", "text": "My chest tightens — vulnerability is physically uncomfortable", "scores": {"repair_repertoire": 3}},
        {"id": "b", "text": "I feel relatively calm — I know repair is important and necessary", "scores": {"repair_repertoire": 5}},
        {"id": "c", "text": "My jaw clenches — part of me still thinks I was right", "scores": {"repair_repertoire": 2}},
        {"id": "d", "text": "I feel an urgency to get it over with — the discomfort of unrepaired conflict is worse", "scores": {"repair_repertoire": 4}}
    ],
    "tier_role": "triangulation",
    "trap": False,
    "consistency_group": "repair_initiation",
    "opacity": 0.8,
    "cross_scores": [
        {"assessment": "self_worth", "dimension": "vulnerability_tolerance", "weight": 0.5}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "repair", "somatic"]
})

questions.append({
    "dimension": "repair_repertoire",
    "question_type": "temporal",
    "text": "Has your ability to repair after conflict improved over the course of your current relationship?",
    "options": [
        {"id": "a", "text": "Significantly — we've developed a whole toolkit for reconnecting", "scores": {"repair_repertoire": 5}},
        {"id": "b", "text": "Somewhat — we're better than we were but still struggle sometimes", "scores": {"repair_repertoire": 3}},
        {"id": "c", "text": "Not really — we repair the same way (or don't) as we always have", "scores": {"repair_repertoire": 2}},
        {"id": "d", "text": "It's gotten harder — the accumulated hurt makes repair feel less effective", "scores": {"repair_repertoire": 1}}
    ],
    "tier_role": "triangulation",
    "trap": False,
    "consistency_group": "repair_range",
    "opacity": 0.5,
    "cross_scores": [],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "repair", "temporal"]
})

questions.append({
    "dimension": "repair_repertoire",
    "question_type": "behavioral_recall",
    "text": "How many different repair strategies can you name that you've actually used in the past month? (humor, direct apology, physical touch, taking a break, expressing love mid-fight, etc.)",
    "options": [
        {"id": "a", "text": "Four or more — I have a genuine range of approaches", "scores": {"repair_repertoire": 5}},
        {"id": "b", "text": "Two or three — I have a few go-to moves", "scores": {"repair_repertoire": 3}},
        {"id": "c", "text": "One — I basically have one way of making up", "scores": {"repair_repertoire": 2}},
        {"id": "d", "text": "None that I can think of — repair isn't really a conscious thing for me", "scores": {"repair_repertoire": 1}}
    ],
    "tier_role": "triangulation",
    "trap": False,
    "consistency_group": "repair_range",
    "opacity": 0.5,
    "cross_scores": [],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "repair"]
})

# --- TRAP (7) ---
questions.append({
    "dimension": "repair_repertoire",
    "question_type": "scenario",
    "text": "I believe that if two people really love each other, they shouldn't need elaborate repair attempts — time heals most conflicts naturally.",
    "options": [
        {"id": "a", "text": "Strongly agree — time and love resolve most things", "scores": {"repair_repertoire": 1}},
        {"id": "b", "text": "Somewhat agree — but some issues need direct addressing", "scores": {"repair_repertoire": 2}},
        {"id": "c", "text": "Somewhat disagree — active repair is almost always needed", "scores": {"repair_repertoire": 4}},
        {"id": "d", "text": "Strongly disagree — unrepaired conflicts accumulate and erode trust", "scores": {"repair_repertoire": 5}}
    ],
    "tier_role": "trap",
    "trap": True,
    "consistency_group": "repair_effectiveness",
    "opacity": 0.9,
    "cross_scores": [
        {"assessment": "attachment_style", "dimension": "avoidant_deactivation", "weight": 0.5}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "repair", "trap"]
})

questions.append({
    "dimension": "repair_repertoire",
    "question_type": "forced_choice",
    "text": "I'm quick to apologize — I'd rather say sorry and move on than dwell on conflict.",
    "options": [
        {"id": "a", "text": "Strongly agree — keeping the peace matters most", "scores": {"repair_repertoire": 2}},
        {"id": "b", "text": "Somewhat agree — speed matters but so does sincerity", "scores": {"repair_repertoire": 3}},
        {"id": "c", "text": "Somewhat disagree — a too-quick apology can be dismissive", "scores": {"repair_repertoire": 4}},
        {"id": "d", "text": "Strongly disagree — I need to understand what happened before I can genuinely repair", "scores": {"repair_repertoire": 4}}
    ],
    "tier_role": "trap",
    "trap": True,
    "consistency_group": "repair_initiation",
    "opacity": 0.9,
    "cross_scores": [
        {"assessment": "conflict_resolution", "dimension": "conflict_avoidance", "weight": 0.4}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "repair", "trap"]
})

questions.append({
    "dimension": "repair_repertoire",
    "question_type": "partner_perspective",
    "text": "I'm the one who usually initiates repair in my relationship. My partner rarely comes to me first.",
    "options": [
        {"id": "a", "text": "True, and I'm fine with that — someone has to lead", "scores": {"repair_repertoire": 3}},
        {"id": "b", "text": "True, and it's exhausting — I wish they'd meet me halfway", "scores": {"repair_repertoire": 3, "demand_withdraw": 2}},
        {"id": "c", "text": "We take turns — it depends on who was more out of line", "scores": {"repair_repertoire": 5}},
        {"id": "d", "text": "Neither of us really initiates — things just settle on their own", "scores": {"repair_repertoire": 1}}
    ],
    "tier_role": "trap",
    "trap": True,
    "consistency_group": "repair_initiation",
    "opacity": 0.8,
    "cross_scores": [
        {"assessment": "communication_style", "dimension": "demand_withdraw", "weight": 0.4}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "repair", "trap"]
})

questions.append({
    "dimension": "repair_repertoire",
    "question_type": "scenario",
    "text": "After a bad argument, I buy my partner a gift or plan something special. This is my way of saying sorry without having to have the uncomfortable conversation.",
    "options": [
        {"id": "a", "text": "That's exactly what I do — actions speak louder than words", "scores": {"repair_repertoire": 2}},
        {"id": "b", "text": "I do this sometimes, but I also have the conversation", "scores": {"repair_repertoire": 4}},
        {"id": "c", "text": "I've realized this doesn't actually resolve anything — I need to talk it through", "scores": {"repair_repertoire": 5}},
        {"id": "d", "text": "I don't do grand gestures — I just let time pass", "scores": {"repair_repertoire": 1}}
    ],
    "tier_role": "trap",
    "trap": True,
    "consistency_group": "repair_range",
    "opacity": 0.9,
    "cross_scores": [
        {"assessment": "love_languages", "dimension": "gift_giving", "weight": 0.3}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "repair", "trap"]
})

questions.append({
    "dimension": "repair_repertoire",
    "question_type": "behavioral_recall",
    "text": "When I apologize, I make sure my partner knows how much I care, even if I can't articulate exactly what I did wrong.",
    "options": [
        {"id": "a", "text": "Yes — the feeling behind the apology matters more than the specifics", "scores": {"repair_repertoire": 2}},
        {"id": "b", "text": "I try to be specific about what I'm apologizing for", "scores": {"repair_repertoire": 5}},
        {"id": "c", "text": "I often say 'I'm sorry you feel that way' which I now realize isn't great", "scores": {"repair_repertoire": 3}},
        {"id": "d", "text": "I struggle with apologies in general — they feel forced", "scores": {"repair_repertoire": 1}}
    ],
    "tier_role": "trap",
    "trap": True,
    "consistency_group": "repair_effectiveness",
    "opacity": 0.9,
    "cross_scores": [
        {"assessment": "emotional_regulation", "dimension": "emotional_specificity", "weight": 0.4}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "repair", "trap"]
})

questions.append({
    "dimension": "repair_repertoire",
    "question_type": "scenario",
    "text": "I don't like to over-process arguments. Once we've both cooled down, I prefer to just move forward rather than rehash what happened.",
    "options": [
        {"id": "a", "text": "Strongly agree — looking forward is healthier than looking back", "scores": {"repair_repertoire": 2}},
        {"id": "b", "text": "Somewhat agree — but some arguments need debriefing", "scores": {"repair_repertoire": 3}},
        {"id": "c", "text": "Somewhat disagree — understanding what happened prevents it from recurring", "scores": {"repair_repertoire": 4}},
        {"id": "d", "text": "Strongly disagree — repair without understanding is just avoidance", "scores": {"repair_repertoire": 5}}
    ],
    "tier_role": "trap",
    "trap": True,
    "consistency_group": "repair_effectiveness",
    "opacity": 0.9,
    "cross_scores": [
        {"assessment": "conflict_resolution", "dimension": "conflict_avoidance", "weight": 0.5}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "repair", "trap"]
})

questions.append({
    "dimension": "repair_repertoire",
    "question_type": "partner_perspective",
    "text": "My partner would say that sex or physical intimacy after an argument is one of our main ways of making up.",
    "options": [
        {"id": "a", "text": "Yes — physical reconnection is powerful for us", "scores": {"repair_repertoire": 2}},
        {"id": "b", "text": "Sometimes, but we also talk things through", "scores": {"repair_repertoire": 4}},
        {"id": "c", "text": "Not really — we need to resolve things verbally first", "scores": {"repair_repertoire": 4}},
        {"id": "d", "text": "We don't have a clear pattern for how we make up", "scores": {"repair_repertoire": 2}}
    ],
    "tier_role": "trap",
    "trap": True,
    "consistency_group": "repair_range",
    "opacity": 0.8,
    "cross_scores": [
        {"assessment": "attachment_style", "dimension": "proximity_seeking", "weight": 0.4}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "repair", "trap"]
})

# --- CONSISTENCY CHECK (7) ---
questions.append({
    "dimension": "repair_repertoire",
    "question_type": "scenario",
    "text": "Your partner tried to apologize but did it poorly — 'Sorry if that bothered you.' How do you respond?",
    "options": [
        {"id": "a", "text": "Accept the intent behind it and gently explain what a real apology would sound like", "scores": {"repair_repertoire": 5}},
        {"id": "b", "text": "Reject it — that's not a real apology and accepting it would let them off the hook", "scores": {"repair_repertoire": 2}},
        {"id": "c", "text": "Accept it and move on — at least they tried", "scores": {"repair_repertoire": 3}},
        {"id": "d", "text": "Get more upset — a bad apology is worse than no apology", "scores": {"repair_repertoire": 1}}
    ],
    "tier_role": "consistency_check",
    "trap": False,
    "consistency_group": "repair_receptivity",
    "opacity": 0.6,
    "cross_scores": [
        {"assessment": "forgiveness_profile", "dimension": "apology_processing", "weight": 0.5}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "repair", "consistency"]
})

questions.append({
    "dimension": "repair_repertoire",
    "question_type": "behavioral_recall",
    "text": "Who typically breaks the ice after a fight in your relationship?",
    "options": [
        {"id": "a", "text": "Me — almost always", "scores": {"repair_repertoire": 4}},
        {"id": "b", "text": "My partner — they're usually the first to reach out", "scores": {"repair_repertoire": 3}},
        {"id": "c", "text": "It varies — whoever realizes they were more out of line tends to go first", "scores": {"repair_repertoire": 5}},
        {"id": "d", "text": "Neither of us — we just wait it out", "scores": {"repair_repertoire": 1}}
    ],
    "tier_role": "consistency_check",
    "trap": False,
    "consistency_group": "repair_initiation",
    "opacity": 0.5,
    "cross_scores": [],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "repair", "consistency"]
})

questions.append({
    "dimension": "repair_repertoire",
    "question_type": "forced_choice",
    "text": "When it comes to repairing after conflict, which is more true?",
    "options": [
        {"id": "a", "text": "I have a varied toolkit — humor, apology, physical touch, verbal processing, taking breaks", "scores": {"repair_repertoire": 5}},
        {"id": "b", "text": "I tend to rely on one or two methods — and if those don't work, I'm stuck", "scores": {"repair_repertoire": 2}}
    ],
    "tier_role": "consistency_check",
    "trap": False,
    "consistency_group": "repair_range",
    "opacity": 0.5,
    "cross_scores": [],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "repair", "consistency"]
})

questions.append({
    "dimension": "repair_repertoire",
    "question_type": "partner_perspective",
    "text": "When your partner makes a repair attempt and you're still angry, can you at least acknowledge they're trying?",
    "options": [
        {"id": "a", "text": "Usually yes — I can say 'I appreciate you trying, I just need a minute'", "scores": {"repair_repertoire": 5}},
        {"id": "b", "text": "Sometimes — but when I'm really angry, I can't receive anything", "scores": {"repair_repertoire": 3}},
        {"id": "c", "text": "No — if I'm angry, their attempt feels manipulative or dismissive", "scores": {"repair_repertoire": 1}},
        {"id": "d", "text": "I try, but my body language probably says otherwise", "scores": {"repair_repertoire": 3}}
    ],
    "tier_role": "consistency_check",
    "trap": False,
    "consistency_group": "repair_receptivity",
    "opacity": 0.6,
    "cross_scores": [
        {"assessment": "emotional_regulation", "dimension": "emotion_during_conflict", "weight": 0.4}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "repair", "consistency"]
})

questions.append({
    "dimension": "repair_repertoire",
    "question_type": "somatic",
    "text": "When your partner reaches out to touch you after an argument — hand on your arm, a hug attempt — what does your body do?",
    "options": [
        {"id": "a", "text": "Softens — physical touch breaks through my walls faster than words", "scores": {"repair_repertoire": 5}},
        {"id": "b", "text": "Stiffens initially then relaxes — I need a second to let them in", "scores": {"repair_repertoire": 3}},
        {"id": "c", "text": "I pull away — I'm not ready for touch when I'm still upset", "scores": {"repair_repertoire": 2}},
        {"id": "d", "text": "I accept it but don't feel anything — the touch doesn't really help", "scores": {"repair_repertoire": 2}}
    ],
    "tier_role": "consistency_check",
    "trap": False,
    "consistency_group": "repair_receptivity",
    "opacity": 0.7,
    "cross_scores": [
        {"assessment": "love_languages", "dimension": "physical_touch", "weight": 0.4}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "repair", "consistency"]
})

questions.append({
    "dimension": "repair_repertoire",
    "question_type": "temporal",
    "text": "Think about your most recent three arguments. Were they all fully repaired, or are any still lingering?",
    "options": [
        {"id": "a", "text": "All fully repaired — we don't let things fester", "scores": {"repair_repertoire": 5}},
        {"id": "b", "text": "Two of three — one might still have some residual tension", "scores": {"repair_repertoire": 3}},
        {"id": "c", "text": "One at best — we have a backlog of unresolved issues", "scores": {"repair_repertoire": 1}},
        {"id": "d", "text": "I honestly don't know — we don't explicitly close out arguments", "scores": {"repair_repertoire": 2}}
    ],
    "tier_role": "consistency_check",
    "trap": False,
    "consistency_group": "repair_effectiveness",
    "opacity": 0.5,
    "cross_scores": [],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "repair", "consistency"]
})

questions.append({
    "dimension": "repair_repertoire",
    "question_type": "scenario",
    "text": "You said something hurtful to your partner in anger. The next morning, you:",
    "options": [
        {"id": "a", "text": "Bring it up directly: 'I want to talk about what I said last night. It wasn't okay.'", "scores": {"repair_repertoire": 5}},
        {"id": "b", "text": "Act extra kind and attentive — hoping actions communicate what words didn't", "scores": {"repair_repertoire": 3}},
        {"id": "c", "text": "Wait to see if they bring it up — maybe it wasn't as bad as I think", "scores": {"repair_repertoire": 2}},
        {"id": "d", "text": "Pretend it didn't happen and start the day fresh", "scores": {"repair_repertoire": 1}}
    ],
    "tier_role": "consistency_check",
    "trap": False,
    "consistency_group": "repair_initiation",
    "opacity": 0.6,
    "cross_scores": [],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "repair", "consistency"]
})

with open('/tmp/comm_q_part3.json', 'w') as f:
    json.dump(questions, f, indent=2)
print(f"Part 3: {len(questions)} repair_repertoire questions written")
