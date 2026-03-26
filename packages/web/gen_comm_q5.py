import json

questions = []

# ============================================================
# DIMENSION 5: ACTIVE LISTENING (29 questions)
# 3 core + 12 triangulation + 7 trap + 7 consistency
# ============================================================

# --- CORE (3) ---
questions.append({
    "dimension": "active_listening",
    "question_type": "scenario",
    "text": "Your partner is telling you about a problem they're having. Halfway through, you realize you already know exactly what they should do. What happens?",
    "options": [
        {"id": "a", "text": "I let them finish, ask what they need from me, THEN offer my take if asked", "scores": {"active_listening": 5}},
        {"id": "b", "text": "I jump in with the solution — why let them suffer when the answer is obvious?", "scores": {"active_listening": 1}},
        {"id": "c", "text": "I half-listen while waiting for a natural pause to share my advice", "scores": {"active_listening": 2}},
        {"id": "d", "text": "I ask a question that helps them reach the conclusion themselves", "scores": {"active_listening": 5}}
    ],
    "tier_role": "core",
    "trap": False,
    "consistency_group": "listening_vs_fixing",
    "opacity": 0.6,
    "cross_scores": [
        {"assessment": "emotional_regulation", "dimension": "impulse_control", "weight": 0.3}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "listening"]
})

questions.append({
    "dimension": "active_listening",
    "question_type": "behavioral_recall",
    "text": "During your last serious conversation with your partner, what were you doing while they spoke?",
    "options": [
        {"id": "a", "text": "Fully focused on understanding their perspective — reflecting back what I heard", "scores": {"active_listening": 5}},
        {"id": "b", "text": "Listening, but also building my counter-argument in my head", "scores": {"active_listening": 2}},
        {"id": "c", "text": "Listening, but my mind wandered and I had to ask them to repeat parts", "scores": {"active_listening": 2}},
        {"id": "d", "text": "Listening for the specific facts I could respond to, filtering out the emotional content", "scores": {"active_listening": 2}}
    ],
    "tier_role": "core",
    "trap": False,
    "consistency_group": "listen_to_understand",
    "opacity": 0.6,
    "cross_scores": [],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "listening"]
})

questions.append({
    "dimension": "active_listening",
    "question_type": "partner_perspective",
    "text": "Would your partner say that when they talk to you, they feel truly heard — or just tolerated?",
    "options": [
        {"id": "a", "text": "Truly heard — they know I take their words seriously", "scores": {"active_listening": 5}},
        {"id": "b", "text": "Usually heard, but sometimes I get that 'are you even listening?' look", "scores": {"active_listening": 3}},
        {"id": "c", "text": "Tolerated — I think they feel I'm enduring the conversation rather than engaging", "scores": {"active_listening": 1}},
        {"id": "d", "text": "They'd say I hear the words but miss the feelings behind them", "scores": {"active_listening": 2}}
    ],
    "tier_role": "core",
    "trap": False,
    "consistency_group": "listen_to_understand",
    "opacity": 0.5,
    "cross_scores": [
        {"assessment": "attachment_style", "dimension": "availability_responsiveness", "weight": 0.5}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "listening"]
})

# --- TRIANGULATION (12) ---
questions.append({
    "dimension": "active_listening",
    "question_type": "scenario",
    "text": "Your partner says 'I had the worst day.' You respond with:",
    "options": [
        {"id": "a", "text": "'Tell me what happened' — and genuinely want to know", "scores": {"active_listening": 5}},
        {"id": "b", "text": "'Yeah, me too' — and pivot to my own bad day", "scores": {"active_listening": 1}},
        {"id": "c", "text": "'That sucks. What can I do?' — solutions-oriented", "scores": {"active_listening": 3}},
        {"id": "d", "text": "'I'm sorry, babe' — genuine sympathy but I don't probe further", "scores": {"active_listening": 3}}
    ],
    "tier_role": "triangulation",
    "trap": False,
    "consistency_group": "listening_vs_fixing",
    "opacity": 0.6,
    "cross_scores": [
        {"assessment": "communication_style", "dimension": "bid_recognition", "weight": 0.4}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "listening"]
})

questions.append({
    "dimension": "active_listening",
    "question_type": "somatic",
    "text": "When your partner is speaking and you disagree strongly, what happens in your body?",
    "options": [
        {"id": "a", "text": "I feel tension building — my jaw tightens, I want to interrupt", "scores": {"active_listening": 2}},
        {"id": "b", "text": "I feel a pull to look away or disengage — it's hard to stay present with disagreement", "scores": {"active_listening": 2}},
        {"id": "c", "text": "I notice the disagreement but deliberately stay open — breathing, eye contact, patience", "scores": {"active_listening": 5}},
        {"id": "d", "text": "I go numb — I stop emotionally processing and just wait for them to finish", "scores": {"active_listening": 1}}
    ],
    "tier_role": "triangulation",
    "trap": False,
    "consistency_group": "listen_to_understand",
    "opacity": 0.8,
    "cross_scores": [
        {"assessment": "emotional_regulation", "dimension": "distress_tolerance", "weight": 0.5}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "listening", "somatic"]
})

questions.append({
    "dimension": "active_listening",
    "question_type": "temporal",
    "text": "How has the quality of your listening in your relationship changed over time?",
    "options": [
        {"id": "a", "text": "Better — I've learned to sit with their perspective before reacting", "scores": {"active_listening": 5}},
        {"id": "b", "text": "Worse — familiarity has made me tune out or assume I know what they'll say", "scores": {"active_listening": 1}},
        {"id": "c", "text": "About the same — I've always been either good or bad at this", "scores": {"active_listening": 3}},
        {"id": "d", "text": "It depends on the topic — I listen well for some things, tune out for others", "scores": {"active_listening": 3}}
    ],
    "tier_role": "triangulation",
    "trap": False,
    "consistency_group": "listen_to_understand",
    "opacity": 0.5,
    "cross_scores": [],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "listening", "temporal"]
})

questions.append({
    "dimension": "active_listening",
    "question_type": "forced_choice",
    "text": "When your partner pauses mid-sentence to gather their thoughts, you're more likely to:",
    "options": [
        {"id": "a", "text": "Wait in silence — give them space to find their words", "scores": {"active_listening": 5}},
        {"id": "b", "text": "Fill the silence — finish their sentence or prompt them along", "scores": {"active_listening": 2}}
    ],
    "tier_role": "triangulation",
    "trap": False,
    "consistency_group": "listening_patience",
    "opacity": 0.6,
    "cross_scores": [],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "listening"]
})

questions.append({
    "dimension": "active_listening",
    "question_type": "scenario",
    "text": "Your partner is explaining why something you did upset them. Halfway through, you realize they've misunderstood your intentions. What do you do?",
    "options": [
        {"id": "a", "text": "Let them finish completely. Acknowledge their experience. THEN share my intent.", "scores": {"active_listening": 5}},
        {"id": "b", "text": "Interrupt to clarify — there's no point in letting them build on a wrong assumption", "scores": {"active_listening": 2}},
        {"id": "c", "text": "Get frustrated — they're not seeing it right and it feels unfair", "scores": {"active_listening": 1}},
        {"id": "d", "text": "Wait for a pause, then gently say 'Can I share what was going through my mind?'", "scores": {"active_listening": 4}}
    ],
    "tier_role": "triangulation",
    "trap": False,
    "consistency_group": "listen_to_understand",
    "opacity": 0.7,
    "cross_scores": [
        {"assessment": "four_horsemen", "dimension": "four_horsemen", "weight": 0.3}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "listening"]
})

questions.append({
    "dimension": "active_listening",
    "question_type": "behavioral_recall",
    "text": "In conversations with your partner, how often do you reflect back what you heard before responding with your own thoughts?",
    "options": [
        {"id": "a", "text": "Regularly — 'So what I'm hearing is...' or 'You're saying that...'", "scores": {"active_listening": 5}},
        {"id": "b", "text": "Occasionally — when the stakes are high or I'm not sure I understood", "scores": {"active_listening": 3}},
        {"id": "c", "text": "Rarely — I just respond to what I think they said", "scores": {"active_listening": 2}},
        {"id": "d", "text": "Never — that would feel weird and clinical in a relationship", "scores": {"active_listening": 2}}
    ],
    "tier_role": "triangulation",
    "trap": False,
    "consistency_group": "listen_to_understand",
    "opacity": 0.5,
    "cross_scores": [],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "listening"]
})

questions.append({
    "dimension": "active_listening",
    "question_type": "partner_perspective",
    "text": "When your partner says 'You're not listening,' what's actually happening?",
    "options": [
        {"id": "a", "text": "I was listening to the words but not the emotion — they felt unheard", "scores": {"active_listening": 3}},
        {"id": "b", "text": "I was distracted — phone, TV, or my own thoughts", "scores": {"active_listening": 2}},
        {"id": "c", "text": "I was listening but my body language didn't show it", "scores": {"active_listening": 3}},
        {"id": "d", "text": "This rarely happens — they usually feel heard by me", "scores": {"active_listening": 5}}
    ],
    "tier_role": "triangulation",
    "trap": False,
    "consistency_group": "listening_patience",
    "opacity": 0.6,
    "cross_scores": [],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "listening"]
})

questions.append({
    "dimension": "active_listening",
    "question_type": "scenario",
    "text": "Your partner starts telling you something and then says 'never mind, it's not important.' What do you do?",
    "options": [
        {"id": "a", "text": "'It seemed important. I'd like to hear it if you want to share.'", "scores": {"active_listening": 5, "bid_recognition": 5}},
        {"id": "b", "text": "Let it go — if it's important, they'll bring it up again", "scores": {"active_listening": 2}},
        {"id": "c", "text": "'Okay' — and move on without much thought", "scores": {"active_listening": 1}},
        {"id": "d", "text": "Feel guilty but don't follow up — I worry about being pushy", "scores": {"active_listening": 3}}
    ],
    "tier_role": "triangulation",
    "trap": False,
    "consistency_group": "listening_vs_fixing",
    "opacity": 0.7,
    "cross_scores": [
        {"assessment": "communication_style", "dimension": "bid_recognition", "weight": 0.5}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "listening"]
})

questions.append({
    "dimension": "active_listening",
    "question_type": "somatic",
    "text": "When you're genuinely listening to your partner — not just waiting to talk — what does that feel like in your body?",
    "options": [
        {"id": "a", "text": "Stillness and openness — like my whole body is oriented toward them", "scores": {"active_listening": 5}},
        {"id": "b", "text": "Effort — it takes deliberate energy to stay focused", "scores": {"active_listening": 3}},
        {"id": "c", "text": "I'm not sure — I don't notice a distinct physical state when I'm listening", "scores": {"active_listening": 2}},
        {"id": "d", "text": "Restlessness — I have thoughts that want to come out", "scores": {"active_listening": 2}}
    ],
    "tier_role": "triangulation",
    "trap": False,
    "consistency_group": "listen_to_understand",
    "opacity": 0.8,
    "cross_scores": [
        {"assessment": "emotional_regulation", "dimension": "present_moment_awareness", "weight": 0.4}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "listening", "somatic"]
})

questions.append({
    "dimension": "active_listening",
    "question_type": "temporal",
    "text": "Think about how conversations with your partner typically flow. How often does 'but' appear early in your responses?",
    "options": [
        {"id": "a", "text": "Often — 'I hear you, BUT...' is a habit I recognize", "scores": {"active_listening": 2}},
        {"id": "b", "text": "Sometimes — I try to start with 'and' instead of 'but' but it's a work in progress", "scores": {"active_listening": 3}},
        {"id": "c", "text": "Rarely — I've learned that 'but' erases everything before it", "scores": {"active_listening": 5}},
        {"id": "d", "text": "I don't track my language that closely", "scores": {"active_listening": 2}}
    ],
    "tier_role": "triangulation",
    "trap": False,
    "consistency_group": "listen_to_understand",
    "opacity": 0.6,
    "cross_scores": [],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "listening", "temporal"]
})

questions.append({
    "dimension": "active_listening",
    "question_type": "behavioral_recall",
    "text": "When your partner shares something emotionally difficult, what kind of questions do you ask?",
    "options": [
        {"id": "a", "text": "Deepening questions — 'What was that like for you?' 'How did that make you feel?'", "scores": {"active_listening": 5}},
        {"id": "b", "text": "Clarifying questions — 'When did this happen? Who was there?'", "scores": {"active_listening": 3}},
        {"id": "c", "text": "Solution questions — 'Have you tried X? What about Y?'", "scores": {"active_listening": 2}},
        {"id": "d", "text": "I mostly don't ask questions — I offer comfort or just listen silently", "scores": {"active_listening": 3}}
    ],
    "tier_role": "triangulation",
    "trap": False,
    "consistency_group": "listening_vs_fixing",
    "opacity": 0.6,
    "cross_scores": [],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "listening"]
})

# --- TRAP (7) ---
questions.append({
    "dimension": "active_listening",
    "question_type": "scenario",
    "text": "I'm a good listener — people always come to me for advice because they know I'll give them a straight answer.",
    "options": [
        {"id": "a", "text": "Exactly — good listening means providing wise counsel", "scores": {"active_listening": 2}},
        {"id": "b", "text": "Partly — but good listening is more about understanding than advising", "scores": {"active_listening": 4}},
        {"id": "c", "text": "Being sought for advice isn't the same as being a good listener — it might mean I'm a good fixer", "scores": {"active_listening": 5}},
        {"id": "d", "text": "I give advice because I care, not because I'm trying to fix", "scores": {"active_listening": 2}}
    ],
    "tier_role": "trap",
    "trap": True,
    "consistency_group": "listening_vs_fixing",
    "opacity": 0.9,
    "cross_scores": [],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "listening", "trap"]
})

questions.append({
    "dimension": "active_listening",
    "question_type": "partner_perspective",
    "text": "I listen carefully to my partner, even when I think they're wrong. But I also owe them my honest perspective.",
    "options": [
        {"id": "a", "text": "Absolutely — listening and then sharing honest feedback is the respectful approach", "scores": {"active_listening": 3}},
        {"id": "b", "text": "True, but I need to make sure they feel fully heard before I share my view", "scores": {"active_listening": 5}},
        {"id": "c", "text": "Sometimes 'sharing my honest perspective' is code for dismissing theirs", "scores": {"active_listening": 4}},
        {"id": "d", "text": "I owe them my presence more than my opinion", "scores": {"active_listening": 4}}
    ],
    "tier_role": "trap",
    "trap": True,
    "consistency_group": "listening_vs_fixing",
    "opacity": 0.9,
    "cross_scores": [],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "listening", "trap"]
})

questions.append({
    "dimension": "active_listening",
    "question_type": "forced_choice",
    "text": "I always try to see my partner's side of things — I'm empathetic to a fault.",
    "options": [
        {"id": "a", "text": "Strongly agree — I often lose myself in their perspective", "scores": {"active_listening": 3, "soft_startup": 2}},
        {"id": "b", "text": "Somewhat agree — I'm good at this but it's genuine, not performative", "scores": {"active_listening": 4}},
        {"id": "c", "text": "Somewhat disagree — I try but my own views usually dominate", "scores": {"active_listening": 3}},
        {"id": "d", "text": "Strongly disagree — empathy isn't my strongest suit", "scores": {"active_listening": 2}}
    ],
    "tier_role": "trap",
    "trap": True,
    "consistency_group": "listen_to_understand",
    "opacity": 0.9,
    "cross_scores": [
        {"assessment": "boundary_style", "dimension": "self_abandonment", "weight": 0.5}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "listening", "trap"]
})

questions.append({
    "dimension": "active_listening",
    "question_type": "scenario",
    "text": "My partner sometimes takes forever to get to the point. I'm patient, but eventually I need to move the conversation along.",
    "options": [
        {"id": "a", "text": "Agreed — being efficient with communication respects both our time", "scores": {"active_listening": 2}},
        {"id": "b", "text": "I feel this way but I'm learning that their 'rambling' IS the point — they're processing out loud", "scores": {"active_listening": 5}},
        {"id": "c", "text": "I try to be patient but I catch myself finishing their sentences", "scores": {"active_listening": 3}},
        {"id": "d", "text": "Everyone has a different communication pace — mine isn't more valid than theirs", "scores": {"active_listening": 4}}
    ],
    "tier_role": "trap",
    "trap": True,
    "consistency_group": "listening_patience",
    "opacity": 0.9,
    "cross_scores": [],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "listening", "trap"]
})

questions.append({
    "dimension": "active_listening",
    "question_type": "behavioral_recall",
    "text": "When my partner tells me about a problem, I know the best thing I can do is help them solve it.",
    "options": [
        {"id": "a", "text": "Yes — that's what a supportive partner does", "scores": {"active_listening": 1}},
        {"id": "b", "text": "Sometimes — but only after I've asked if they want solutions or just support", "scores": {"active_listening": 5}},
        {"id": "c", "text": "I've learned the hard way that they usually want to be heard first, not fixed", "scores": {"active_listening": 5}},
        {"id": "d", "text": "I try to balance listening and solving", "scores": {"active_listening": 3}}
    ],
    "tier_role": "trap",
    "trap": True,
    "consistency_group": "listening_vs_fixing",
    "opacity": 0.9,
    "cross_scores": [],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "listening", "trap"]
})

questions.append({
    "dimension": "active_listening",
    "question_type": "partner_perspective",
    "text": "I have a good memory for conversations — I can recall exactly what my partner said in past arguments.",
    "options": [
        {"id": "a", "text": "True — and I use this to ensure consistency and accountability", "scores": {"active_listening": 2}},
        {"id": "b", "text": "True — but I've learned that bringing up past quotes can feel weaponized", "scores": {"active_listening": 4}},
        {"id": "c", "text": "Somewhat — but memory is selective and I might remember differently than they do", "scores": {"active_listening": 4}},
        {"id": "d", "text": "Not really — I focus more on the present conversation", "scores": {"active_listening": 3}}
    ],
    "tier_role": "trap",
    "trap": True,
    "consistency_group": "listen_to_understand",
    "opacity": 0.9,
    "cross_scores": [
        {"assessment": "conflict_resolution", "dimension": "score_keeping", "weight": 0.5}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "listening", "trap"]
})

questions.append({
    "dimension": "active_listening",
    "question_type": "scenario",
    "text": "When my partner expresses a feeling I think is irrational, I gently help them see a more balanced perspective.",
    "options": [
        {"id": "a", "text": "Yes — feelings should be grounded in reality", "scores": {"active_listening": 1}},
        {"id": "b", "text": "Sometimes — but I validate the feeling first before offering perspective", "scores": {"active_listening": 4}},
        {"id": "c", "text": "I've learned that correcting someone's feelings is invalidating, not helpful", "scores": {"active_listening": 5}},
        {"id": "d", "text": "I try not to, but my face probably gives away my skepticism", "scores": {"active_listening": 2}}
    ],
    "tier_role": "trap",
    "trap": True,
    "consistency_group": "listen_to_understand",
    "opacity": 0.9,
    "cross_scores": [
        {"assessment": "emotional_regulation", "dimension": "emotional_validation", "weight": 0.5}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "listening", "trap"]
})

# --- CONSISTENCY CHECK (7) ---
questions.append({
    "dimension": "active_listening",
    "question_type": "scenario",
    "text": "Your partner finishes telling you about something that happened. Before you respond, do you check that you understood correctly?",
    "options": [
        {"id": "a", "text": "Yes — I paraphrase or ask 'Did I get that right?'", "scores": {"active_listening": 5}},
        {"id": "b", "text": "Sometimes, but usually I'm confident I understood", "scores": {"active_listening": 3}},
        {"id": "c", "text": "No — I just respond based on what I think they said", "scores": {"active_listening": 2}},
        {"id": "d", "text": "Only when the topic is complicated or high-stakes", "scores": {"active_listening": 3}}
    ],
    "tier_role": "consistency_check",
    "trap": False,
    "consistency_group": "listen_to_understand",
    "opacity": 0.5,
    "cross_scores": [],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "listening", "consistency"]
})

questions.append({
    "dimension": "active_listening",
    "question_type": "behavioral_recall",
    "text": "In your last conversation with your partner, did you ask any follow-up questions based on what they shared?",
    "options": [
        {"id": "a", "text": "Yes — multiple questions that showed I was genuinely curious about their experience", "scores": {"active_listening": 5}},
        {"id": "b", "text": "One or two — enough to be polite", "scores": {"active_listening": 3}},
        {"id": "c", "text": "No — I responded with my own thoughts or experience", "scores": {"active_listening": 2}},
        {"id": "d", "text": "I don't remember the conversation well enough to say", "scores": {"active_listening": 1}}
    ],
    "tier_role": "consistency_check",
    "trap": False,
    "consistency_group": "listen_to_understand",
    "opacity": 0.5,
    "cross_scores": [],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "listening", "consistency"]
})

questions.append({
    "dimension": "active_listening",
    "question_type": "forced_choice",
    "text": "Be honest: when your partner is talking, are you more often listening to understand, or listening to respond?",
    "options": [
        {"id": "a", "text": "Listening to understand — I genuinely want to know their world", "scores": {"active_listening": 5}},
        {"id": "b", "text": "Listening to respond — I'm usually formulating my reply while they speak", "scores": {"active_listening": 2}}
    ],
    "tier_role": "consistency_check",
    "trap": False,
    "consistency_group": "listen_to_understand",
    "opacity": 0.4,
    "cross_scores": [],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "listening", "consistency"]
})

questions.append({
    "dimension": "active_listening",
    "question_type": "partner_perspective",
    "text": "If your partner could change one thing about how you communicate, would 'listen more' be on the list?",
    "options": [
        {"id": "a", "text": "Probably not — listening is one of my strengths", "scores": {"active_listening": 5}},
        {"id": "b", "text": "Maybe — not my worst trait but there's room for improvement", "scores": {"active_listening": 3}},
        {"id": "c", "text": "Likely yes — they've said as much before", "scores": {"active_listening": 2}},
        {"id": "d", "text": "Definitely — it's one of our biggest friction points", "scores": {"active_listening": 1}}
    ],
    "tier_role": "consistency_check",
    "trap": False,
    "consistency_group": "listen_to_understand",
    "opacity": 0.5,
    "cross_scores": [],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "listening", "consistency"]
})

questions.append({
    "dimension": "active_listening",
    "question_type": "somatic",
    "text": "When your partner says something that surprises you — a feeling you didn't expect or a perspective you hadn't considered — what does your body do?",
    "options": [
        {"id": "a", "text": "I lean in — surprise creates curiosity, not defensiveness", "scores": {"active_listening": 5}},
        {"id": "b", "text": "I lean back — I need a second to process the unexpected", "scores": {"active_listening": 3}},
        {"id": "c", "text": "I feel a flash of defensiveness — like I should have already known this", "scores": {"active_listening": 2}},
        {"id": "d", "text": "I don't notice a physical reaction — I process surprises cognitively", "scores": {"active_listening": 3}}
    ],
    "tier_role": "consistency_check",
    "trap": False,
    "consistency_group": "listening_patience",
    "opacity": 0.7,
    "cross_scores": [],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "listening", "consistency"]
})

questions.append({
    "dimension": "active_listening",
    "question_type": "temporal",
    "text": "Does your partner share less with you now than they used to? If so, why do you think that is?",
    "options": [
        {"id": "a", "text": "They share the same or more — our communication has deepened", "scores": {"active_listening": 5}},
        {"id": "b", "text": "Somewhat less — but I think that's natural as relationships mature", "scores": {"active_listening": 3}},
        {"id": "c", "text": "Noticeably less — and it might be because they don't feel heard when they do", "scores": {"active_listening": 1}},
        {"id": "d", "text": "Less, but it's because they've become more independent, not because I'm a bad listener", "scores": {"active_listening": 3}}
    ],
    "tier_role": "consistency_check",
    "trap": False,
    "consistency_group": "listen_to_understand",
    "opacity": 0.6,
    "cross_scores": [
        {"assessment": "attachment_style", "dimension": "relationship_security", "weight": 0.4}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "listening", "consistency"]
})

questions.append({
    "dimension": "active_listening",
    "question_type": "scenario",
    "text": "Your partner is telling you a story you've heard before. What do you do?",
    "options": [
        {"id": "a", "text": "Listen again — they're sharing it for a reason, and I might hear something new", "scores": {"active_listening": 5}},
        {"id": "b", "text": "Gently mention I've heard it before but invite them to tell me if there's something new about it", "scores": {"active_listening": 4}},
        {"id": "c", "text": "Say 'You've told me this one' — saves us both time", "scores": {"active_listening": 2}},
        {"id": "d", "text": "Zone out while appearing to listen — no point in interrupting", "scores": {"active_listening": 1}}
    ],
    "tier_role": "consistency_check",
    "trap": False,
    "consistency_group": "listening_patience",
    "opacity": 0.6,
    "cross_scores": [],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "listening", "consistency"]
})

with open('/tmp/comm_q_part5.json', 'w') as f:
    json.dump(questions, f, indent=2)
print(f"Part 5: {len(questions)} active_listening questions written")
