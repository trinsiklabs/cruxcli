import json

questions = []

# ============================================================
# DIMENSION 2: BID RECOGNITION (29 questions)
# 3 core + 12 triangulation + 7 trap + 7 consistency
# ============================================================

# --- CORE (3) ---
questions.append({
    "dimension": "bid_recognition",
    "question_type": "scenario",
    "text": "You're scrolling your phone on the couch. Your partner walks in and says, 'You wouldn't believe what happened at work today.' What do you do?",
    "options": [
        {"id": "a", "text": "Put the phone down, turn toward them, and say 'Tell me'", "scores": {"bid_recognition": 5}},
        {"id": "b", "text": "Say 'Hmm?' while continuing to scroll, glancing up occasionally", "scores": {"bid_recognition": 2}},
        {"id": "c", "text": "Say 'One sec, let me finish this' — and actually follow up in a minute", "scores": {"bid_recognition": 3}},
        {"id": "d", "text": "Grunt acknowledgment but don't really engage", "scores": {"bid_recognition": 1}}
    ],
    "tier_role": "core",
    "trap": False,
    "consistency_group": "turning_toward",
    "opacity": 0.6,
    "cross_scores": [
        {"assessment": "attachment_style", "dimension": "availability_responsiveness", "weight": 0.5}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "bids"]
})

questions.append({
    "dimension": "bid_recognition",
    "question_type": "behavioral_recall",
    "text": "Think about yesterday evening with your partner. Can you identify a moment where they reached out for your attention or connection — even subtly?",
    "options": [
        {"id": "a", "text": "Yes — they made a comment, touched my arm, or showed me something", "scores": {"bid_recognition": 5}},
        {"id": "b", "text": "Maybe — I wasn't paying close attention to those signals", "scores": {"bid_recognition": 3}},
        {"id": "c", "text": "I don't think they did — it was a quiet evening", "scores": {"bid_recognition": 2}},
        {"id": "d", "text": "I honestly don't remember much about our interactions yesterday", "scores": {"bid_recognition": 1}}
    ],
    "tier_role": "core",
    "trap": False,
    "consistency_group": "bid_awareness",
    "opacity": 0.7,
    "cross_scores": [
        {"assessment": "emotional_regulation", "dimension": "present_moment_awareness", "weight": 0.4}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "bids"]
})

questions.append({
    "dimension": "bid_recognition",
    "question_type": "partner_perspective",
    "text": "If your partner rated how often you notice when they're trying to connect with you — not during big moments, but in everyday life — what score would they give (1-10)?",
    "options": [
        {"id": "a", "text": "8-10 — I'm pretty attuned to their bids", "scores": {"bid_recognition": 5}},
        {"id": "b", "text": "5-7 — I catch some but miss plenty", "scores": {"bid_recognition": 3}},
        {"id": "c", "text": "3-4 — they'd say I'm often in my own world", "scores": {"bid_recognition": 2}},
        {"id": "d", "text": "1-2 — they've probably given up making small bids", "scores": {"bid_recognition": 1}}
    ],
    "tier_role": "core",
    "trap": False,
    "consistency_group": "turning_toward",
    "opacity": 0.5,
    "cross_scores": [
        {"assessment": "attachment_style", "dimension": "avoidant_deactivation", "weight": -0.4}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "bids"]
})

# --- TRIANGULATION (12) ---
questions.append({
    "dimension": "bid_recognition",
    "question_type": "scenario",
    "text": "Your partner sighs heavily while reading something on their phone. You:",
    "options": [
        {"id": "a", "text": "Ask 'Everything okay?' — a sigh like that usually means something", "scores": {"bid_recognition": 5}},
        {"id": "b", "text": "Notice it but figure they'll tell me if it's important", "scores": {"bid_recognition": 3}},
        {"id": "c", "text": "Don't really register it — people sigh for lots of reasons", "scores": {"bid_recognition": 1}},
        {"id": "d", "text": "Feel a flash of anxiety — something might be wrong", "scores": {"bid_recognition": 4, "active_listening": 3}}
    ],
    "tier_role": "triangulation",
    "trap": False,
    "consistency_group": "bid_awareness",
    "opacity": 0.8,
    "cross_scores": [
        {"assessment": "attachment_style", "dimension": "anxious_activation", "weight": 0.3}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "bids"]
})

questions.append({
    "dimension": "bid_recognition",
    "question_type": "scenario",
    "text": "Your partner says 'Look at this sunset' while you're cooking dinner. What happens?",
    "options": [
        {"id": "a", "text": "I stop what I'm doing, go look, and share the moment", "scores": {"bid_recognition": 5}},
        {"id": "b", "text": "I say 'Nice!' without looking up — I'm in the middle of something", "scores": {"bid_recognition": 2}},
        {"id": "c", "text": "I glance up briefly and say 'Pretty' then go back to cooking", "scores": {"bid_recognition": 3}},
        {"id": "d", "text": "I don't hear them or it doesn't register", "scores": {"bid_recognition": 1}}
    ],
    "tier_role": "triangulation",
    "trap": False,
    "consistency_group": "turning_toward",
    "opacity": 0.6,
    "cross_scores": [],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "bids"]
})

questions.append({
    "dimension": "bid_recognition",
    "question_type": "somatic",
    "text": "When your partner reaches for your hand unexpectedly, what do you feel in your body?",
    "options": [
        {"id": "a", "text": "Warmth — I squeeze back instinctively", "scores": {"bid_recognition": 5}},
        {"id": "b", "text": "Surprise — I sometimes flinch before relaxing into it", "scores": {"bid_recognition": 3}},
        {"id": "c", "text": "Slight discomfort — I'm not always in the mood for touch", "scores": {"bid_recognition": 2}},
        {"id": "d", "text": "I don't really notice a physical reaction — it's just a hand", "scores": {"bid_recognition": 2}}
    ],
    "tier_role": "triangulation",
    "trap": False,
    "consistency_group": "physical_bids",
    "opacity": 0.7,
    "cross_scores": [
        {"assessment": "attachment_style", "dimension": "avoidant_deactivation", "weight": 0.4},
        {"assessment": "love_languages", "dimension": "physical_touch", "weight": 0.5}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "bids", "somatic"]
})

questions.append({
    "dimension": "bid_recognition",
    "question_type": "temporal",
    "text": "Over the past six months, has your partner's frequency of reaching out to you for small moments of connection changed?",
    "options": [
        {"id": "a", "text": "They reach out just as much — or more", "scores": {"bid_recognition": 4}},
        {"id": "b", "text": "They've seemed to pull back some — fewer random texts, less 'come look at this'", "scores": {"bid_recognition": 2}},
        {"id": "c", "text": "I honestly can't tell — I haven't been tracking that", "scores": {"bid_recognition": 2}},
        {"id": "d", "text": "They reach out differently now — more substantial conversations, fewer small bids", "scores": {"bid_recognition": 3}}
    ],
    "tier_role": "triangulation",
    "trap": False,
    "consistency_group": "bid_awareness",
    "opacity": 0.7,
    "cross_scores": [
        {"assessment": "attachment_style", "dimension": "relationship_security", "weight": 0.4}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "bids", "temporal"]
})

questions.append({
    "dimension": "bid_recognition",
    "question_type": "forced_choice",
    "text": "Which is more true for you?",
    "options": [
        {"id": "a", "text": "I naturally notice when my partner is reaching for connection — it's almost automatic", "scores": {"bid_recognition": 5}},
        {"id": "b", "text": "I have to consciously remind myself to look for those moments — it doesn't come naturally", "scores": {"bid_recognition": 3}}
    ],
    "tier_role": "triangulation",
    "trap": False,
    "consistency_group": "turning_toward",
    "opacity": 0.5,
    "cross_scores": [],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "bids"]
})

questions.append({
    "dimension": "bid_recognition",
    "question_type": "partner_perspective",
    "text": "Your partner sends you a funny meme or link during your workday. How do you typically respond?",
    "options": [
        {"id": "a", "text": "Respond right away with a reaction — it's a tiny moment of connection", "scores": {"bid_recognition": 5}},
        {"id": "b", "text": "React to it later when I have a break — sometimes hours later", "scores": {"bid_recognition": 3}},
        {"id": "c", "text": "Sometimes I see it but forget to respond", "scores": {"bid_recognition": 2}},
        {"id": "d", "text": "I find those kinds of messages mildly annoying during work", "scores": {"bid_recognition": 1}}
    ],
    "tier_role": "triangulation",
    "trap": False,
    "consistency_group": "turning_toward",
    "opacity": 0.6,
    "cross_scores": [
        {"assessment": "love_languages", "dimension": "quality_time", "weight": 0.3}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "bids"]
})

questions.append({
    "dimension": "bid_recognition",
    "question_type": "behavioral_recall",
    "text": "Think about the last time your partner started telling you a story about their day. What did your body language communicate?",
    "options": [
        {"id": "a", "text": "I faced them, made eye contact, and engaged actively", "scores": {"bid_recognition": 5}},
        {"id": "b", "text": "I was half-present — looking at them sometimes but also doing something else", "scores": {"bid_recognition": 2}},
        {"id": "c", "text": "I was physically present but mentally somewhere else", "scores": {"bid_recognition": 1}},
        {"id": "d", "text": "I turned toward them but got distracted partway through", "scores": {"bid_recognition": 3}}
    ],
    "tier_role": "triangulation",
    "trap": False,
    "consistency_group": "turning_toward",
    "opacity": 0.6,
    "cross_scores": [
        {"assessment": "communication_style", "dimension": "active_listening", "weight": 0.5}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "bids"]
})

questions.append({
    "dimension": "bid_recognition",
    "question_type": "scenario",
    "text": "You come home and your partner has cleaned the entire kitchen. This is unusual. What do you think?",
    "options": [
        {"id": "a", "text": "They're doing something nice — I should acknowledge and appreciate it", "scores": {"bid_recognition": 5, "positive_negative_ratio": 5}},
        {"id": "b", "text": "They must want something from me", "scores": {"bid_recognition": 2}},
        {"id": "c", "text": "That's great — but I don't make a big deal of it", "scores": {"bid_recognition": 3}},
        {"id": "d", "text": "I notice but don't think much of it — someone had to clean", "scores": {"bid_recognition": 2}}
    ],
    "tier_role": "triangulation",
    "trap": False,
    "consistency_group": "bid_awareness",
    "opacity": 0.7,
    "cross_scores": [
        {"assessment": "attachment_style", "dimension": "trust_capacity", "weight": 0.3}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "bids"]
})

questions.append({
    "dimension": "bid_recognition",
    "question_type": "somatic",
    "text": "Your partner walks into the room while you're deeply focused on something. Before they even speak, what happens in your body?",
    "options": [
        {"id": "a", "text": "I feel a brief warmth or lift — their presence registers positively", "scores": {"bid_recognition": 5}},
        {"id": "b", "text": "I feel a twinge of irritation — my focus is being interrupted", "scores": {"bid_recognition": 2}},
        {"id": "c", "text": "I don't really feel anything — I'm absorbed in what I'm doing", "scores": {"bid_recognition": 1}},
        {"id": "d", "text": "I feel a mix — glad to see them but protective of my concentration", "scores": {"bid_recognition": 3}}
    ],
    "tier_role": "triangulation",
    "trap": False,
    "consistency_group": "physical_bids",
    "opacity": 0.8,
    "cross_scores": [
        {"assessment": "attachment_style", "dimension": "avoidant_deactivation", "weight": 0.4}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "bids", "somatic"]
})

questions.append({
    "dimension": "bid_recognition",
    "question_type": "temporal",
    "text": "When you first started dating your partner, how quickly did you respond to their texts compared to now?",
    "options": [
        {"id": "a", "text": "Faster then, but I still respond pretty quickly now — it just matters to me", "scores": {"bid_recognition": 4}},
        {"id": "b", "text": "Way faster then — now it can be hours because we're settled", "scores": {"bid_recognition": 3}},
        {"id": "c", "text": "About the same — I'm consistent in how I communicate", "scores": {"bid_recognition": 4}},
        {"id": "d", "text": "I barely respond to non-essential texts now — we're past that phase", "scores": {"bid_recognition": 1}}
    ],
    "tier_role": "triangulation",
    "trap": False,
    "consistency_group": "turning_toward",
    "opacity": 0.6,
    "cross_scores": [],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "bids", "temporal"]
})

questions.append({
    "dimension": "bid_recognition",
    "question_type": "behavioral_recall",
    "text": "Your partner recently said something like 'I had a really weird dream last night' or 'I saw the strangest thing today.' What did you do?",
    "options": [
        {"id": "a", "text": "Leaned in with genuine curiosity — 'Oh yeah? Tell me'", "scores": {"bid_recognition": 5}},
        {"id": "b", "text": "Half-engaged — 'Huh, that's weird' and moved on", "scores": {"bid_recognition": 2}},
        {"id": "c", "text": "I don't remember them saying something like that recently", "scores": {"bid_recognition": 1}},
        {"id": "d", "text": "I asked a follow-up question but was doing something else at the same time", "scores": {"bid_recognition": 3}}
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

# --- TRAP (7) ---
questions.append({
    "dimension": "bid_recognition",
    "question_type": "scenario",
    "text": "I don't need my partner to constantly reach out to me — we're secure enough that we don't need to perform connection.",
    "options": [
        {"id": "a", "text": "Strongly agree — secure relationships don't require constant bidding", "scores": {"bid_recognition": 2}},
        {"id": "b", "text": "Somewhat agree — but even secure couples need regular small connections", "scores": {"bid_recognition": 4}},
        {"id": "c", "text": "Somewhat disagree — those small moments ARE the relationship", "scores": {"bid_recognition": 5}},
        {"id": "d", "text": "Strongly disagree — everyone needs bids for connection", "scores": {"bid_recognition": 5}}
    ],
    "tier_role": "trap",
    "trap": True,
    "consistency_group": "turning_toward",
    "opacity": 0.9,
    "cross_scores": [
        {"assessment": "attachment_style", "dimension": "avoidant_deactivation", "weight": 0.5}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "bids", "trap"]
})

questions.append({
    "dimension": "bid_recognition",
    "question_type": "partner_perspective",
    "text": "My partner and I have a deep connection, so we don't need a lot of small talk or daily check-ins to stay close.",
    "options": [
        {"id": "a", "text": "Exactly — our bond goes beyond daily minutiae", "scores": {"bid_recognition": 1}},
        {"id": "b", "text": "Mostly true — but I try to stay engaged in the small stuff too", "scores": {"bid_recognition": 3}},
        {"id": "c", "text": "I used to think this, but I've learned the small stuff IS the bond", "scores": {"bid_recognition": 5}},
        {"id": "d", "text": "Not true — we need those daily connections to stay close", "scores": {"bid_recognition": 5}}
    ],
    "tier_role": "trap",
    "trap": True,
    "consistency_group": "bid_awareness",
    "opacity": 0.9,
    "cross_scores": [
        {"assessment": "attachment_style", "dimension": "avoidant_deactivation", "weight": 0.6}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "bids", "trap"]
})

questions.append({
    "dimension": "bid_recognition",
    "question_type": "forced_choice",
    "text": "I show my partner I care through actions and providing, not through constantly responding to every little thing they say.",
    "options": [
        {"id": "a", "text": "Strongly agree — actions matter more than verbal responsiveness", "scores": {"bid_recognition": 2}},
        {"id": "b", "text": "Somewhat agree — but I know responsiveness matters to them", "scores": {"bid_recognition": 3}},
        {"id": "c", "text": "Somewhat disagree — responding to the small things IS an action", "scores": {"bid_recognition": 4}},
        {"id": "d", "text": "Strongly disagree — being responsive is one of the most important things", "scores": {"bid_recognition": 5}}
    ],
    "tier_role": "trap",
    "trap": True,
    "consistency_group": "turning_toward",
    "opacity": 0.9,
    "cross_scores": [
        {"assessment": "love_languages", "dimension": "acts_of_service", "weight": 0.3}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "bids", "trap"]
})

questions.append({
    "dimension": "bid_recognition",
    "question_type": "scenario",
    "text": "Your partner starts talking about something you have zero interest in — a work colleague's drama, a hobby you don't share. What do you do?",
    "options": [
        {"id": "a", "text": "Listen anyway — they're excited and that matters more than the topic", "scores": {"bid_recognition": 5}},
        {"id": "b", "text": "Listen for a bit then gently redirect to something we both care about", "scores": {"bid_recognition": 3}},
        {"id": "c", "text": "Zone out politely — I can't fake interest I don't have", "scores": {"bid_recognition": 2}},
        {"id": "d", "text": "Tell them honestly that I'm not the right audience for this one", "scores": {"bid_recognition": 2}}
    ],
    "tier_role": "trap",
    "trap": True,
    "consistency_group": "turning_toward",
    "opacity": 0.8,
    "cross_scores": [
        {"assessment": "communication_style", "dimension": "active_listening", "weight": 0.5}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "bids", "trap"]
})

questions.append({
    "dimension": "bid_recognition",
    "question_type": "behavioral_recall",
    "text": "I give my partner plenty of quality time, so missing a few small moments here and there doesn't really matter.",
    "options": [
        {"id": "a", "text": "True — quality over quantity", "scores": {"bid_recognition": 2}},
        {"id": "b", "text": "Mostly true — the big moments carry more weight", "scores": {"bid_recognition": 2}},
        {"id": "c", "text": "I'm starting to realize the small moments accumulate", "scores": {"bid_recognition": 4}},
        {"id": "d", "text": "Not true — the small moments ARE the quality time", "scores": {"bid_recognition": 5}}
    ],
    "tier_role": "trap",
    "trap": True,
    "consistency_group": "bid_awareness",
    "opacity": 0.9,
    "cross_scores": [
        {"assessment": "love_languages", "dimension": "quality_time", "weight": 0.4}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "bids", "trap"]
})

questions.append({
    "dimension": "bid_recognition",
    "question_type": "scenario",
    "text": "When your partner tries to show you something on their phone, you often think:",
    "options": [
        {"id": "a", "text": "'I love that they want to share things with me' — and I engage", "scores": {"bid_recognition": 5}},
        {"id": "b", "text": "'Another video/meme/article' — but I look anyway because it matters to them", "scores": {"bid_recognition": 4}},
        {"id": "c", "text": "'I wish they'd just describe it instead of making me watch'", "scores": {"bid_recognition": 2}},
        {"id": "d", "text": "I try to be interested but I know my lack of enthusiasm shows", "scores": {"bid_recognition": 3}}
    ],
    "tier_role": "trap",
    "trap": True,
    "consistency_group": "turning_toward",
    "opacity": 0.8,
    "cross_scores": [],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "bids", "trap"]
})

questions.append({
    "dimension": "bid_recognition",
    "question_type": "partner_perspective",
    "text": "My partner knows I love them, even if I'm not always immediately responsive to every bid for attention.",
    "options": [
        {"id": "a", "text": "Absolutely — love isn't measured in response time", "scores": {"bid_recognition": 2}},
        {"id": "b", "text": "I think so — but I sometimes wonder if my non-responsiveness hurts them", "scores": {"bid_recognition": 3}},
        {"id": "c", "text": "They probably wish I was more responsive even if they don't say it", "scores": {"bid_recognition": 4}},
        {"id": "d", "text": "I've learned that responsiveness IS how they measure love", "scores": {"bid_recognition": 5}}
    ],
    "tier_role": "trap",
    "trap": True,
    "consistency_group": "bid_awareness",
    "opacity": 0.9,
    "cross_scores": [
        {"assessment": "love_languages", "dimension": "quality_time", "weight": 0.4}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "bids", "trap"]
})

# --- CONSISTENCY CHECK (7) ---
questions.append({
    "dimension": "bid_recognition",
    "question_type": "scenario",
    "text": "You're watching a show together and your partner makes a comment about one of the characters. You:",
    "options": [
        {"id": "a", "text": "Pause the show and discuss — they're inviting me into a shared experience", "scores": {"bid_recognition": 5}},
        {"id": "b", "text": "Respond briefly without pausing — don't want to lose the plot", "scores": {"bid_recognition": 3}},
        {"id": "c", "text": "Say 'shh' or 'wait' — I want to hear the dialogue", "scores": {"bid_recognition": 1}},
        {"id": "d", "text": "Acknowledge what they said but keep watching — we can discuss after", "scores": {"bid_recognition": 3}}
    ],
    "tier_role": "consistency_check",
    "trap": False,
    "consistency_group": "turning_toward",
    "opacity": 0.6,
    "cross_scores": [],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "bids", "consistency"]
})

questions.append({
    "dimension": "bid_recognition",
    "question_type": "behavioral_recall",
    "text": "How many times today did your partner try to connect with you in a small way (text, touch, comment, look)?",
    "options": [
        {"id": "a", "text": "Several times — I can name specific instances", "scores": {"bid_recognition": 5}},
        {"id": "b", "text": "A couple of times, I think", "scores": {"bid_recognition": 3}},
        {"id": "c", "text": "I'm not sure — I wasn't counting", "scores": {"bid_recognition": 2}},
        {"id": "d", "text": "We haven't interacted much today", "scores": {"bid_recognition": 2}}
    ],
    "tier_role": "consistency_check",
    "trap": False,
    "consistency_group": "bid_awareness",
    "opacity": 0.6,
    "cross_scores": [],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "bids", "consistency"]
})

questions.append({
    "dimension": "bid_recognition",
    "question_type": "forced_choice",
    "text": "When your partner shares random thoughts throughout the day, it's:",
    "options": [
        {"id": "a", "text": "A sign they feel safe sharing their inner world with me — I cherish it", "scores": {"bid_recognition": 5}},
        {"id": "b", "text": "Nice but sometimes overwhelming — I don't always have the bandwidth", "scores": {"bid_recognition": 3}}
    ],
    "tier_role": "consistency_check",
    "trap": False,
    "consistency_group": "turning_toward",
    "opacity": 0.5,
    "cross_scores": [],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "bids", "consistency"]
})

questions.append({
    "dimension": "bid_recognition",
    "question_type": "somatic",
    "text": "When you realize you missed a bid from your partner — they tried to share something and you didn't engage — what do you feel?",
    "options": [
        {"id": "a", "text": "A pang of guilt — I try to circle back", "scores": {"bid_recognition": 4}},
        {"id": "b", "text": "Not much — it was just a moment, not a big deal", "scores": {"bid_recognition": 2}},
        {"id": "c", "text": "I usually don't even realize I missed it until later, if at all", "scores": {"bid_recognition": 1}},
        {"id": "d", "text": "Some regret, but I often don't know how to re-open the moment", "scores": {"bid_recognition": 3}}
    ],
    "tier_role": "consistency_check",
    "trap": False,
    "consistency_group": "bid_awareness",
    "opacity": 0.7,
    "cross_scores": [],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "bids", "consistency"]
})

questions.append({
    "dimension": "bid_recognition",
    "question_type": "partner_perspective",
    "text": "When your partner tries to initiate physical affection (not sexual — just a hug, leaning against you, etc.), how do you usually respond?",
    "options": [
        {"id": "a", "text": "I reciprocate naturally — it feels good to be close", "scores": {"bid_recognition": 5}},
        {"id": "b", "text": "I accept it but don't always initiate back", "scores": {"bid_recognition": 3}},
        {"id": "c", "text": "Sometimes I stiffen or pull away without meaning to", "scores": {"bid_recognition": 2}},
        {"id": "d", "text": "It depends entirely on my mood", "scores": {"bid_recognition": 3}}
    ],
    "tier_role": "consistency_check",
    "trap": False,
    "consistency_group": "physical_bids",
    "opacity": 0.6,
    "cross_scores": [
        {"assessment": "attachment_style", "dimension": "avoidant_deactivation", "weight": 0.4}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "bids", "consistency"]
})

questions.append({
    "dimension": "bid_recognition",
    "question_type": "temporal",
    "text": "Has your ability to notice your partner's bids for connection improved, stayed the same, or declined over the course of your relationship?",
    "options": [
        {"id": "a", "text": "Improved — I've gotten better at reading their signals", "scores": {"bid_recognition": 5}},
        {"id": "b", "text": "Stayed the same — I was always tuned in (or not)", "scores": {"bid_recognition": 3}},
        {"id": "c", "text": "Declined — I've gotten more absorbed in my own world over time", "scores": {"bid_recognition": 2}},
        {"id": "d", "text": "I honestly don't know what a 'bid for connection' is in practical terms", "scores": {"bid_recognition": 1}}
    ],
    "tier_role": "consistency_check",
    "trap": False,
    "consistency_group": "bid_awareness",
    "opacity": 0.5,
    "cross_scores": [],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "bids", "consistency"]
})

questions.append({
    "dimension": "bid_recognition",
    "question_type": "scenario",
    "text": "You're at a social gathering and your partner catches your eye from across the room and smiles. You:",
    "options": [
        {"id": "a", "text": "Smile back warmly — a shared moment in a crowd", "scores": {"bid_recognition": 5}},
        {"id": "b", "text": "Nod and go back to my conversation", "scores": {"bid_recognition": 3}},
        {"id": "c", "text": "Don't notice — I'm engaged with the people around me", "scores": {"bid_recognition": 1}},
        {"id": "d", "text": "Find an excuse to go over to them", "scores": {"bid_recognition": 5}}
    ],
    "tier_role": "consistency_check",
    "trap": False,
    "consistency_group": "turning_toward",
    "opacity": 0.6,
    "cross_scores": [
        {"assessment": "attachment_style", "dimension": "secure_base", "weight": 0.3}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "bids", "consistency"]
})

with open('/tmp/comm_q_part2.json', 'w') as f:
    json.dump(questions, f, indent=2)
print(f"Part 2: {len(questions)} bid_recognition questions written")
