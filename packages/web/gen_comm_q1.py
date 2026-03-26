import json

questions = []

# ============================================================
# DIMENSION 1: FOUR HORSEMEN (29 questions)
# 3 core + 12 triangulation + 7 trap + 7 consistency
# ============================================================

# --- CORE (3) ---
questions.append({
    "dimension": "four_horsemen",
    "question_type": "scenario",
    "text": "Your partner forgot to pick up groceries you asked for. You walk into the kitchen and see empty counters. What's your first internal reaction?",
    "options": [
        {"id": "a", "text": "Annoyance at the specific situation — they forgot this one thing", "scores": {"four_horsemen": 4}},
        {"id": "b", "text": "A flash of 'they never follow through on anything'", "scores": {"four_horsemen": 2}},
        {"id": "c", "text": "Wondering if something came up that derailed their day", "scores": {"four_horsemen": 5}},
        {"id": "d", "text": "A sigh and the thought 'why do I even bother asking'", "scores": {"four_horsemen": 1}}
    ],
    "tier_role": "core",
    "trap": False,
    "consistency_group": "criticism_pattern",
    "opacity": 0.8,
    "cross_scores": [
        {"assessment": "cognitive_distortions", "dimension": "overgeneralization", "weight": 0.5}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "criticism"]
})

questions.append({
    "dimension": "four_horsemen",
    "question_type": "behavioral_recall",
    "text": "Think about the last argument that got heated. When your partner said something that stung, what did your body do?",
    "options": [
        {"id": "a", "text": "I crossed my arms and went quiet — just waited for it to be over", "scores": {"four_horsemen": 2}},
        {"id": "b", "text": "I fired back immediately with my own point", "scores": {"four_horsemen": 2}},
        {"id": "c", "text": "I felt my jaw clench but tried to stay in the conversation", "scores": {"four_horsemen": 4}},
        {"id": "d", "text": "I physically left the room or turned away", "scores": {"four_horsemen": 1}}
    ],
    "tier_role": "core",
    "trap": False,
    "consistency_group": "stonewalling_pattern",
    "opacity": 0.7,
    "cross_scores": [
        {"assessment": "emotional_regulation", "dimension": "flooding_response", "weight": 0.6}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "stonewalling"]
})

questions.append({
    "dimension": "four_horsemen",
    "question_type": "partner_perspective",
    "text": "If your partner described how you act when you're frustrated with them, which would they most likely say?",
    "options": [
        {"id": "a", "text": "I make a specific complaint about what happened", "scores": {"four_horsemen": 4}},
        {"id": "b", "text": "I bring up a list of other times they've done similar things", "scores": {"four_horsemen": 2}},
        {"id": "c", "text": "I get sarcastic or dismissive in my tone", "scores": {"four_horsemen": 1}},
        {"id": "d", "text": "I shut down and become unreachable for a while", "scores": {"four_horsemen": 2}}
    ],
    "tier_role": "core",
    "trap": False,
    "consistency_group": "contempt_pattern",
    "opacity": 0.6,
    "cross_scores": [
        {"assessment": "conflict_resolution", "dimension": "escalation_tendency", "weight": 0.5}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "contempt"]
})

# --- TRIANGULATION (12) ---
questions.append({
    "dimension": "four_horsemen",
    "question_type": "scenario",
    "text": "You're telling your partner about a problem at work and they interrupt with advice. You feel unheard. What comes out of your mouth?",
    "options": [
        {"id": "a", "text": "'Can you just listen for a minute before jumping to solutions?'", "scores": {"four_horsemen": 4, "soft_startup": 4}},
        {"id": "b", "text": "'You always do this — you never actually listen to me'", "scores": {"four_horsemen": 1}},
        {"id": "c", "text": "Nothing — I just stop talking about it", "scores": {"four_horsemen": 2}},
        {"id": "d", "text": "'Wow, thanks for the TED talk. Really helpful.'", "scores": {"four_horsemen": 1}}
    ],
    "tier_role": "triangulation",
    "trap": False,
    "consistency_group": "criticism_pattern",
    "opacity": 0.7,
    "cross_scores": [
        {"assessment": "attachment_style", "dimension": "protest_behavior", "weight": 0.3}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "criticism", "contempt"]
})

questions.append({
    "dimension": "four_horsemen",
    "question_type": "somatic",
    "text": "During a disagreement, your partner rolls their eyes at something you said. What happens in your chest and stomach in that moment?",
    "options": [
        {"id": "a", "text": "A hot flush — I want to say something cutting back", "scores": {"four_horsemen": 2}},
        {"id": "b", "text": "A sinking feeling — like what I said doesn't matter", "scores": {"four_horsemen": 3, "positive_negative_ratio": 2}},
        {"id": "c", "text": "Tightening — I brace for the argument to escalate", "scores": {"four_horsemen": 3}},
        {"id": "d", "text": "Numbness — I've seen that eye-roll so many times I barely register it", "scores": {"four_horsemen": 1}}
    ],
    "tier_role": "triangulation",
    "trap": False,
    "consistency_group": "contempt_pattern",
    "opacity": 0.8,
    "cross_scores": [
        {"assessment": "emotional_regulation", "dimension": "somatic_awareness", "weight": 0.5}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "contempt", "somatic"]
})

questions.append({
    "dimension": "four_horsemen",
    "question_type": "temporal",
    "text": "Think about disagreements over the past year. Has the way you express frustration with your partner changed?",
    "options": [
        {"id": "a", "text": "I've gotten better at naming the specific issue without attacking them", "scores": {"four_horsemen": 5}},
        {"id": "b", "text": "I've gotten quieter — I just don't bring things up anymore", "scores": {"four_horsemen": 2, "demand_withdraw": 2}},
        {"id": "c", "text": "It's gotten more intense — small things feel bigger now", "scores": {"four_horsemen": 2}},
        {"id": "d", "text": "Honestly, I don't think it's changed much either way", "scores": {"four_horsemen": 3}}
    ],
    "tier_role": "triangulation",
    "trap": False,
    "consistency_group": "criticism_evolution",
    "opacity": 0.7,
    "cross_scores": [
        {"assessment": "emotional_regulation", "dimension": "emotional_trajectory", "weight": 0.4}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "temporal"]
})

questions.append({
    "dimension": "four_horsemen",
    "question_type": "forced_choice",
    "text": "Which is closer to how you handle repeated disappointments with your partner?",
    "options": [
        {"id": "a", "text": "I address each instance specifically when it happens", "scores": {"four_horsemen": 5}},
        {"id": "b", "text": "I collect them until the pattern is undeniable, then bring up the whole list", "scores": {"four_horsemen": 2}}
    ],
    "tier_role": "triangulation",
    "trap": False,
    "consistency_group": "criticism_pattern",
    "opacity": 0.6,
    "cross_scores": [
        {"assessment": "conflict_resolution", "dimension": "timing_awareness", "weight": 0.4}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "criticism"]
})

questions.append({
    "dimension": "four_horsemen",
    "question_type": "scenario",
    "text": "Your partner makes a mistake that costs you both money — forgot to cancel a subscription, overdrew an account, etc. What's your go-to response?",
    "options": [
        {"id": "a", "text": "'That's frustrating. Let's figure out how to fix it.'", "scores": {"four_horsemen": 5}},
        {"id": "b", "text": "'How could you not have caught that? That's basic stuff.'", "scores": {"four_horsemen": 1}},
        {"id": "c", "text": "I fix it myself and bring it up later when I'm calmer", "scores": {"four_horsemen": 3}},
        {"id": "d", "text": "I don't say anything but I feel a familiar contempt", "scores": {"four_horsemen": 1}}
    ],
    "tier_role": "triangulation",
    "trap": False,
    "consistency_group": "contempt_pattern",
    "opacity": 0.6,
    "cross_scores": [
        {"assessment": "emotional_regulation", "dimension": "impulse_control", "weight": 0.3}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "contempt"]
})

questions.append({
    "dimension": "four_horsemen",
    "question_type": "partner_perspective",
    "text": "If asked anonymously, would your partner say you respect them during arguments?",
    "options": [
        {"id": "a", "text": "Yes — even when I'm angry, I keep it about the issue", "scores": {"four_horsemen": 5}},
        {"id": "b", "text": "Mostly, but I have a sharp tongue when I'm hurt", "scores": {"four_horsemen": 3}},
        {"id": "c", "text": "Probably not — I know I can be dismissive or cutting", "scores": {"four_horsemen": 2}},
        {"id": "d", "text": "They'd say I don't engage enough to be disrespectful — I just leave", "scores": {"four_horsemen": 2}}
    ],
    "tier_role": "triangulation",
    "trap": False,
    "consistency_group": "contempt_pattern",
    "opacity": 0.5,
    "cross_scores": [
        {"assessment": "self_worth", "dimension": "relational_self_worth", "weight": 0.3}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "contempt"]
})

questions.append({
    "dimension": "four_horsemen",
    "question_type": "behavioral_recall",
    "text": "Last time your partner criticized something you did, what was your immediate response?",
    "options": [
        {"id": "a", "text": "I explained why I did it that way — they didn't have the full picture", "scores": {"four_horsemen": 2}},
        {"id": "b", "text": "I pointed out something they do that's just as bad or worse", "scores": {"four_horsemen": 1}},
        {"id": "c", "text": "I considered whether they had a point before responding", "scores": {"four_horsemen": 5}},
        {"id": "d", "text": "I apologized quickly to end the conflict", "scores": {"four_horsemen": 3, "repair_repertoire": 2}}
    ],
    "tier_role": "triangulation",
    "trap": False,
    "consistency_group": "defensiveness_pattern",
    "opacity": 0.6,
    "cross_scores": [
        {"assessment": "conflict_resolution", "dimension": "accountability", "weight": 0.5}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "defensiveness"]
})

questions.append({
    "dimension": "four_horsemen",
    "question_type": "scenario",
    "text": "You're both tired after a long day. Your partner brings up an issue with how you handled something with the kids/family/friends. You feel ambushed. What do you do?",
    "options": [
        {"id": "a", "text": "Say 'I hear you, but can we talk about this tomorrow when we're both fresher?'", "scores": {"four_horsemen": 4, "repair_repertoire": 4}},
        {"id": "b", "text": "Immediately defend my decision — I had good reasons", "scores": {"four_horsemen": 2}},
        {"id": "c", "text": "Go stone-faced and monosyllabic until they drop it", "scores": {"four_horsemen": 1}},
        {"id": "d", "text": "Match their energy — 'Oh, we're doing this NOW? Fine, let's talk about what YOU did last week'", "scores": {"four_horsemen": 1}}
    ],
    "tier_role": "triangulation",
    "trap": False,
    "consistency_group": "stonewalling_pattern",
    "opacity": 0.7,
    "cross_scores": [
        {"assessment": "emotional_regulation", "dimension": "fatigue_reactivity", "weight": 0.4}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "stonewalling", "defensiveness"]
})

questions.append({
    "dimension": "four_horsemen",
    "question_type": "somatic",
    "text": "When an argument with your partner is clearly going nowhere, what happens to your heart rate and breathing?",
    "options": [
        {"id": "a", "text": "My heart is pounding — I can feel it in my ears", "scores": {"four_horsemen": 2}},
        {"id": "b", "text": "I notice I'm holding my breath or breathing shallow", "scores": {"four_horsemen": 3}},
        {"id": "c", "text": "I feel eerily calm — like I've detached from the situation", "scores": {"four_horsemen": 2}},
        {"id": "d", "text": "I can usually feel myself getting activated and try to slow down", "scores": {"four_horsemen": 4}}
    ],
    "tier_role": "triangulation",
    "trap": False,
    "consistency_group": "stonewalling_pattern",
    "opacity": 0.8,
    "cross_scores": [
        {"assessment": "emotional_regulation", "dimension": "physiological_awareness", "weight": 0.7}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "stonewalling", "somatic"]
})

questions.append({
    "dimension": "four_horsemen",
    "question_type": "temporal",
    "text": "Compared to the first year of your relationship, how has the way you and your partner disagree changed?",
    "options": [
        {"id": "a", "text": "We're more efficient — we know each other's triggers and mostly avoid them", "scores": {"four_horsemen": 4}},
        {"id": "b", "text": "There's more edge to it now — the gloves come off faster", "scores": {"four_horsemen": 1}},
        {"id": "c", "text": "We disagree less because one of us stopped bringing things up", "scores": {"four_horsemen": 2, "demand_withdraw": 2}},
        {"id": "d", "text": "We've actually learned to fight better — it's less personal", "scores": {"four_horsemen": 5}}
    ],
    "tier_role": "triangulation",
    "trap": False,
    "consistency_group": "criticism_evolution",
    "opacity": 0.6,
    "cross_scores": [
        {"assessment": "attachment_style", "dimension": "relationship_security", "weight": 0.4}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "temporal"]
})

questions.append({
    "dimension": "four_horsemen",
    "question_type": "behavioral_recall",
    "text": "Think of a time you said something in an argument you later regretted. What category did it fall into?",
    "options": [
        {"id": "a", "text": "A character attack — I went after who they are, not what they did", "scores": {"four_horsemen": 1}},
        {"id": "b", "text": "A mocking or sarcastic comment that landed harder than I intended", "scores": {"four_horsemen": 1}},
        {"id": "c", "text": "A defensive excuse that dismissed their feelings", "scores": {"four_horsemen": 2}},
        {"id": "d", "text": "I can't recall a specific regretted statement recently", "scores": {"four_horsemen": 4}}
    ],
    "tier_role": "triangulation",
    "trap": False,
    "consistency_group": "contempt_pattern",
    "opacity": 0.5,
    "cross_scores": [
        {"assessment": "emotional_regulation", "dimension": "regret_processing", "weight": 0.4}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "contempt", "criticism"]
})

# --- TRAP (7) ---
questions.append({
    "dimension": "four_horsemen",
    "question_type": "scenario",
    "text": "When your partner does something that bothers you, you pride yourself on staying calm and not reacting. How does this usually play out?",
    "options": [
        {"id": "a", "text": "I stay composed, address it later when I've thought it through", "scores": {"four_horsemen": 4}},
        {"id": "b", "text": "I don't react at all — I've learned it's not worth the fight", "scores": {"four_horsemen": 2, "demand_withdraw": 1}},
        {"id": "c", "text": "I stay calm on the surface but they can tell I'm seething", "scores": {"four_horsemen": 2}},
        {"id": "d", "text": "I acknowledge it in the moment even if I'm not perfectly composed", "scores": {"four_horsemen": 5}}
    ],
    "tier_role": "trap",
    "trap": True,
    "consistency_group": "stonewalling_pattern",
    "opacity": 0.9,
    "cross_scores": [
        {"assessment": "emotional_regulation", "dimension": "suppression_tendency", "weight": 0.6}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "stonewalling", "trap"]
})

questions.append({
    "dimension": "four_horsemen",
    "question_type": "forced_choice",
    "text": "I hold my partner to high standards because I believe in their potential.",
    "options": [
        {"id": "a", "text": "Strongly agree — pushing them helps them grow", "scores": {"four_horsemen": 2}},
        {"id": "b", "text": "Somewhat agree — but I try to do it gently", "scores": {"four_horsemen": 3}},
        {"id": "c", "text": "Somewhat disagree — it's not my job to improve them", "scores": {"four_horsemen": 4}},
        {"id": "d", "text": "Strongly disagree — I accept them as they are", "scores": {"four_horsemen": 4}}
    ],
    "tier_role": "trap",
    "trap": True,
    "consistency_group": "criticism_pattern",
    "opacity": 0.9,
    "cross_scores": [
        {"assessment": "boundary_style", "dimension": "control_orientation", "weight": 0.5}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "criticism", "trap"]
})

questions.append({
    "dimension": "four_horsemen",
    "question_type": "partner_perspective",
    "text": "My partner would say I'm the more rational one in arguments — I don't get as emotional.",
    "options": [
        {"id": "a", "text": "Yes, I keep things logical and fact-based", "scores": {"four_horsemen": 2}},
        {"id": "b", "text": "Sometimes — but being 'rational' is sometimes my way of dismissing their feelings", "scores": {"four_horsemen": 4}},
        {"id": "c", "text": "We're both emotional in different ways", "scores": {"four_horsemen": 4}},
        {"id": "d", "text": "No, I'm actually the more emotional one", "scores": {"four_horsemen": 3}}
    ],
    "tier_role": "trap",
    "trap": True,
    "consistency_group": "contempt_pattern",
    "opacity": 0.9,
    "cross_scores": [
        {"assessment": "emotional_regulation", "dimension": "intellectualization", "weight": 0.6}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "contempt", "trap"]
})

questions.append({
    "dimension": "four_horsemen",
    "question_type": "behavioral_recall",
    "text": "I rarely raise my voice during disagreements. I express displeasure in other ways.",
    "options": [
        {"id": "a", "text": "True — I use silence, tone shifts, or withdrawal instead", "scores": {"four_horsemen": 2}},
        {"id": "b", "text": "True — I genuinely keep things measured and respectful", "scores": {"four_horsemen": 5}},
        {"id": "c", "text": "Not really — I can get loud when I'm frustrated", "scores": {"four_horsemen": 3}},
        {"id": "d", "text": "True — I use humor or sarcasm to make my point", "scores": {"four_horsemen": 2}}
    ],
    "tier_role": "trap",
    "trap": True,
    "consistency_group": "contempt_pattern",
    "opacity": 0.9,
    "cross_scores": [
        {"assessment": "conflict_resolution", "dimension": "passive_aggression", "weight": 0.5}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "contempt", "trap"]
})

questions.append({
    "dimension": "four_horsemen",
    "question_type": "scenario",
    "text": "Your partner brings up the same complaint for the third time this month. You've heard it before. How do you respond?",
    "options": [
        {"id": "a", "text": "I listen again — if they keep bringing it up, it's clearly still unresolved for them", "scores": {"four_horsemen": 5, "active_listening": 5}},
        {"id": "b", "text": "I tell them we've already discussed this and I don't know what else to say", "scores": {"four_horsemen": 2}},
        {"id": "c", "text": "I feel a wave of frustration but try to find what's new in this iteration", "scores": {"four_horsemen": 4}},
        {"id": "d", "text": "I mentally check out while appearing to listen", "scores": {"four_horsemen": 1}}
    ],
    "tier_role": "trap",
    "trap": True,
    "consistency_group": "stonewalling_pattern",
    "opacity": 0.8,
    "cross_scores": [
        {"assessment": "emotional_regulation", "dimension": "patience_capacity", "weight": 0.4}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "stonewalling", "trap"]
})

questions.append({
    "dimension": "four_horsemen",
    "question_type": "scenario",
    "text": "A friend asks how arguments with your partner typically end. You say:",
    "options": [
        {"id": "a", "text": "'Usually one of us sees reason and we work it out'", "scores": {"four_horsemen": 3}},
        {"id": "b", "text": "'Honestly, they just kind of fizzle — nobody wins or resolves anything'", "scores": {"four_horsemen": 2}},
        {"id": "c", "text": "'We've gotten good at circling back and making sure both people feel heard'", "scores": {"four_horsemen": 5}},
        {"id": "d", "text": "'I usually let it go — it's not worth the drama'", "scores": {"four_horsemen": 2, "demand_withdraw": 2}}
    ],
    "tier_role": "trap",
    "trap": True,
    "consistency_group": "stonewalling_pattern",
    "opacity": 0.8,
    "cross_scores": [
        {"assessment": "conflict_resolution", "dimension": "resolution_quality", "weight": 0.5}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "stonewalling", "trap"]
})

questions.append({
    "dimension": "four_horsemen",
    "question_type": "partner_perspective",
    "text": "When I correct my partner, it's because I genuinely want to help them avoid mistakes.",
    "options": [
        {"id": "a", "text": "Absolutely — it comes from caring, not criticism", "scores": {"four_horsemen": 2}},
        {"id": "b", "text": "I think so, but they might experience it as criticism even when I don't mean it that way", "scores": {"four_horsemen": 4}},
        {"id": "c", "text": "Sometimes it's genuinely helpful, sometimes I'm just frustrated", "scores": {"four_horsemen": 3}},
        {"id": "d", "text": "I've realized I correct them more than I should", "scores": {"four_horsemen": 4}}
    ],
    "tier_role": "trap",
    "trap": True,
    "consistency_group": "criticism_pattern",
    "opacity": 0.9,
    "cross_scores": [
        {"assessment": "boundary_style", "dimension": "control_orientation", "weight": 0.5}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "criticism", "trap"]
})

# --- CONSISTENCY CHECK (7) ---
questions.append({
    "dimension": "four_horsemen",
    "question_type": "scenario",
    "text": "Your partner leaves dishes in the sink again. What thought crosses your mind?",
    "options": [
        {"id": "a", "text": "'They left dishes in the sink' — specific, factual", "scores": {"four_horsemen": 5}},
        {"id": "b", "text": "'They're so inconsiderate' — about their character", "scores": {"four_horsemen": 1}},
        {"id": "c", "text": "'Here we go again' — a weary pattern recognition", "scores": {"four_horsemen": 2}},
        {"id": "d", "text": "'I'll just do it myself' — resigned acceptance", "scores": {"four_horsemen": 2}}
    ],
    "tier_role": "consistency_check",
    "trap": False,
    "consistency_group": "criticism_pattern",
    "opacity": 0.6,
    "cross_scores": [],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "criticism", "consistency"]
})

questions.append({
    "dimension": "four_horsemen",
    "question_type": "behavioral_recall",
    "text": "In your last conflict, did you use the word 'always' or 'never' when describing your partner's behavior?",
    "options": [
        {"id": "a", "text": "Yes, probably — it felt true in the moment", "scores": {"four_horsemen": 2}},
        {"id": "b", "text": "No, I'm careful about absolute language", "scores": {"four_horsemen": 5}},
        {"id": "c", "text": "I don't remember, but it wouldn't surprise me", "scores": {"four_horsemen": 3}},
        {"id": "d", "text": "I didn't say much at all during that conflict", "scores": {"four_horsemen": 2}}
    ],
    "tier_role": "consistency_check",
    "trap": False,
    "consistency_group": "criticism_pattern",
    "opacity": 0.5,
    "cross_scores": [
        {"assessment": "cognitive_distortions", "dimension": "overgeneralization", "weight": 0.6}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "criticism", "consistency"]
})

questions.append({
    "dimension": "four_horsemen",
    "question_type": "forced_choice",
    "text": "During conflict, which are you more likely to do?",
    "options": [
        {"id": "a", "text": "Attack — criticism, sarcasm, or pointing out their flaws", "scores": {"four_horsemen": 1}},
        {"id": "b", "text": "Withdraw — go quiet, leave, or shut down emotionally", "scores": {"four_horsemen": 2}}
    ],
    "tier_role": "consistency_check",
    "trap": False,
    "consistency_group": "stonewalling_pattern",
    "opacity": 0.4,
    "cross_scores": [
        {"assessment": "conflict_resolution", "dimension": "conflict_style", "weight": 0.5}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "consistency"]
})

questions.append({
    "dimension": "four_horsemen",
    "question_type": "partner_perspective",
    "text": "Would your partner say that you treat them with contempt — even subtly — during arguments?",
    "options": [
        {"id": "a", "text": "No — heated, maybe, but not contemptuous", "scores": {"four_horsemen": 4}},
        {"id": "b", "text": "They might — my tone can get dismissive even when my words are fine", "scores": {"four_horsemen": 3}},
        {"id": "c", "text": "Probably yes — I know I can be condescending", "scores": {"four_horsemen": 2}},
        {"id": "d", "text": "I honestly don't know how they experience my tone", "scores": {"four_horsemen": 3}}
    ],
    "tier_role": "consistency_check",
    "trap": False,
    "consistency_group": "contempt_pattern",
    "opacity": 0.5,
    "cross_scores": [],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "contempt", "consistency"]
})

questions.append({
    "dimension": "four_horsemen",
    "question_type": "somatic",
    "text": "When your partner starts a conversation with 'We need to talk,' what's the first thing your body does?",
    "options": [
        {"id": "a", "text": "My stomach drops — I brace for an attack", "scores": {"four_horsemen": 2}},
        {"id": "b", "text": "I feel alert but open — could be anything", "scores": {"four_horsemen": 5}},
        {"id": "c", "text": "I mentally start building my defense before they even say what it's about", "scores": {"four_horsemen": 2}},
        {"id": "d", "text": "I feel an urge to preemptively end the conversation or change the subject", "scores": {"four_horsemen": 1}}
    ],
    "tier_role": "consistency_check",
    "trap": False,
    "consistency_group": "defensiveness_pattern",
    "opacity": 0.7,
    "cross_scores": [
        {"assessment": "attachment_style", "dimension": "anxious_activation", "weight": 0.5}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "defensiveness", "consistency"]
})

questions.append({
    "dimension": "four_horsemen",
    "question_type": "temporal",
    "text": "Over the course of your relationship, has your respect for your partner during disagreements increased or decreased?",
    "options": [
        {"id": "a", "text": "Increased — we've built mutual respect over time", "scores": {"four_horsemen": 5}},
        {"id": "b", "text": "Decreased — frustration has eroded some of the respect", "scores": {"four_horsemen": 1}},
        {"id": "c", "text": "It fluctuates depending on the topic", "scores": {"four_horsemen": 3}},
        {"id": "d", "text": "Stayed about the same", "scores": {"four_horsemen": 3}}
    ],
    "tier_role": "consistency_check",
    "trap": False,
    "consistency_group": "contempt_pattern",
    "opacity": 0.5,
    "cross_scores": [
        {"assessment": "attachment_style", "dimension": "relationship_security", "weight": 0.4}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "contempt", "consistency"]
})

questions.append({
    "dimension": "four_horsemen",
    "question_type": "scenario",
    "text": "Your partner accuses you of something you didn't do. Your reaction:",
    "options": [
        {"id": "a", "text": "Explain calmly that they have the facts wrong and ask what made them think that", "scores": {"four_horsemen": 5}},
        {"id": "b", "text": "Get indignant — 'I can't believe you'd even think that about me'", "scores": {"four_horsemen": 2}},
        {"id": "c", "text": "Turn it around — 'Oh really? What about when YOU did X?'", "scores": {"four_horsemen": 1}},
        {"id": "d", "text": "Shut down — if they've already decided, what's the point of defending myself", "scores": {"four_horsemen": 1}}
    ],
    "tier_role": "consistency_check",
    "trap": False,
    "consistency_group": "defensiveness_pattern",
    "opacity": 0.6,
    "cross_scores": [],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "defensiveness", "consistency"]
})

with open('/tmp/comm_q_part1.json', 'w') as f:
    json.dump(questions, f, indent=2)
print(f"Part 1: {len(questions)} four_horsemen questions written")
