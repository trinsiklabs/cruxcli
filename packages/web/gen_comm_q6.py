import json

questions = []

# ============================================================
# DIMENSION 6: DEMAND-WITHDRAW (29 questions)
# 3 core + 12 triangulation + 7 trap + 7 consistency
# ============================================================

# --- CORE (3) ---
questions.append({
    "dimension": "demand_withdraw",
    "question_type": "scenario",
    "text": "You've tried to start an important conversation with your partner three times this week. Each time, they've changed the subject or said 'not now.' What do you do the fourth time?",
    "options": [
        {"id": "a", "text": "Try harder — send a text, write a letter, corner them when they can't escape", "scores": {"demand_withdraw": 1}},
        {"id": "b", "text": "Name the pattern: 'I've tried three times this week. I need you to tell me when you CAN talk.'", "scores": {"demand_withdraw": 5}},
        {"id": "c", "text": "Give up — if they wanted to talk, they would", "scores": {"demand_withdraw": 2}},
        {"id": "d", "text": "Get increasingly frustrated and it comes out sideways — passive-aggressive comments, cold shoulder", "scores": {"demand_withdraw": 1}}
    ],
    "tier_role": "core",
    "trap": False,
    "consistency_group": "pursuer_pattern",
    "opacity": 0.6,
    "cross_scores": [
        {"assessment": "attachment_style", "dimension": "anxious_activation", "weight": 0.5}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "demand_withdraw"]
})

questions.append({
    "dimension": "demand_withdraw",
    "question_type": "behavioral_recall",
    "text": "When your partner pushes for a conversation you're not ready for, what do you actually do?",
    "options": [
        {"id": "a", "text": "Engage even though I'm not ready — it'll only get worse if I avoid it", "scores": {"demand_withdraw": 3}},
        {"id": "b", "text": "Ask for specific time: 'I need an hour to decompress, then I'm all yours'", "scores": {"demand_withdraw": 5}},
        {"id": "c", "text": "Go monosyllabic — I'm physically present but not really participating", "scores": {"demand_withdraw": 1}},
        {"id": "d", "text": "Leave the room or find an excuse to be elsewhere", "scores": {"demand_withdraw": 1}}
    ],
    "tier_role": "core",
    "trap": False,
    "consistency_group": "withdrawer_pattern",
    "opacity": 0.6,
    "cross_scores": [
        {"assessment": "attachment_style", "dimension": "avoidant_deactivation", "weight": 0.5}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "demand_withdraw"]
})

questions.append({
    "dimension": "demand_withdraw",
    "question_type": "partner_perspective",
    "text": "In your relationship, would your partner say there's a clear pursuer and a clear distancer — and if so, which are you?",
    "options": [
        {"id": "a", "text": "I'm the pursuer — I push for connection and conversation", "scores": {"demand_withdraw": 2}},
        {"id": "b", "text": "I'm the distancer — I need space and they need closeness", "scores": {"demand_withdraw": 2}},
        {"id": "c", "text": "We trade roles depending on the issue", "scores": {"demand_withdraw": 4}},
        {"id": "d", "text": "Neither — we're pretty balanced in how we approach difficult conversations", "scores": {"demand_withdraw": 5}}
    ],
    "tier_role": "core",
    "trap": False,
    "consistency_group": "role_flexibility",
    "opacity": 0.5,
    "cross_scores": [
        {"assessment": "attachment_style", "dimension": "anxious_activation", "weight": 0.3},
        {"assessment": "attachment_style", "dimension": "avoidant_deactivation", "weight": 0.3}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "demand_withdraw"]
})

# --- TRIANGULATION (12) ---
questions.append({
    "dimension": "demand_withdraw",
    "question_type": "scenario",
    "text": "Your partner goes quiet after a disagreement. You've texted them twice with no response. What's your next move?",
    "options": [
        {"id": "a", "text": "Text again — maybe they didn't see the first two", "scores": {"demand_withdraw": 1}},
        {"id": "b", "text": "Call them — I need resolution and the silence is unbearable", "scores": {"demand_withdraw": 2}},
        {"id": "c", "text": "Give space — they'll come back when they're ready, and pushing will make it worse", "scores": {"demand_withdraw": 4}},
        {"id": "d", "text": "Send one more text: 'I'm here when you're ready. Take the time you need.'", "scores": {"demand_withdraw": 5}}
    ],
    "tier_role": "triangulation",
    "trap": False,
    "consistency_group": "pursuer_pattern",
    "opacity": 0.7,
    "cross_scores": [
        {"assessment": "attachment_style", "dimension": "anxious_activation", "weight": 0.5}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "demand_withdraw"]
})

questions.append({
    "dimension": "demand_withdraw",
    "question_type": "somatic",
    "text": "When your partner goes silent or withdraws during conflict, what does your body do?",
    "options": [
        {"id": "a", "text": "Panic — racing heart, tight chest, an urgent need to close the distance", "scores": {"demand_withdraw": 1}},
        {"id": "b", "text": "Relief — the pressure is off and I can breathe again", "scores": {"demand_withdraw": 2}},
        {"id": "c", "text": "Frustration building in my gut — like a pressure cooker without a valve", "scores": {"demand_withdraw": 2}},
        {"id": "d", "text": "I notice the anxiety but can sit with it — their silence doesn't require my action", "scores": {"demand_withdraw": 5}}
    ],
    "tier_role": "triangulation",
    "trap": False,
    "consistency_group": "pursuer_pattern",
    "opacity": 0.8,
    "cross_scores": [
        {"assessment": "attachment_style", "dimension": "anxious_activation", "weight": 0.6},
        {"assessment": "emotional_regulation", "dimension": "distress_tolerance", "weight": 0.5}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "demand_withdraw", "somatic"]
})

questions.append({
    "dimension": "demand_withdraw",
    "question_type": "temporal",
    "text": "Over the course of your relationship, has the demand-withdraw pattern (one pushes, one retreats) intensified, softened, or stayed the same?",
    "options": [
        {"id": "a", "text": "Intensified — we're more polarized than ever", "scores": {"demand_withdraw": 1}},
        {"id": "b", "text": "Softened — we've learned to meet in the middle", "scores": {"demand_withdraw": 5}},
        {"id": "c", "text": "Stayed the same — it's a fixed dynamic between us", "scores": {"demand_withdraw": 2}},
        {"id": "d", "text": "The roles have reversed — I used to pursue, now I withdraw (or vice versa)", "scores": {"demand_withdraw": 3}}
    ],
    "tier_role": "triangulation",
    "trap": False,
    "consistency_group": "role_flexibility",
    "opacity": 0.5,
    "cross_scores": [],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "demand_withdraw", "temporal"]
})

questions.append({
    "dimension": "demand_withdraw",
    "question_type": "forced_choice",
    "text": "When there's an unresolved issue between you and your partner:",
    "options": [
        {"id": "a", "text": "I can't rest until it's addressed — unresolved tension is physically uncomfortable", "scores": {"demand_withdraw": 2}},
        {"id": "b", "text": "I need time and space to process before I can productively engage", "scores": {"demand_withdraw": 3}}
    ],
    "tier_role": "triangulation",
    "trap": False,
    "consistency_group": "pursuer_pattern",
    "opacity": 0.5,
    "cross_scores": [
        {"assessment": "attachment_style", "dimension": "anxious_activation", "weight": 0.4}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "demand_withdraw"]
})

questions.append({
    "dimension": "demand_withdraw",
    "question_type": "scenario",
    "text": "Your partner says 'I need some time to think.' You interpret this as:",
    "options": [
        {"id": "a", "text": "A healthy boundary — they're regulating, not rejecting", "scores": {"demand_withdraw": 5}},
        {"id": "b", "text": "Avoidance disguised as processing — they just don't want to deal with it", "scores": {"demand_withdraw": 2}},
        {"id": "c", "text": "Rejection — if they cared, they'd want to work through it now", "scores": {"demand_withdraw": 1}},
        {"id": "d", "text": "Depends on the pattern — sometimes it's genuine, sometimes it's a delay tactic", "scores": {"demand_withdraw": 3}}
    ],
    "tier_role": "triangulation",
    "trap": False,
    "consistency_group": "withdrawer_pattern",
    "opacity": 0.7,
    "cross_scores": [
        {"assessment": "attachment_style", "dimension": "anxious_activation", "weight": 0.4}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "demand_withdraw"]
})

questions.append({
    "dimension": "demand_withdraw",
    "question_type": "behavioral_recall",
    "text": "Think about the last time you wanted to talk and your partner didn't. How long did you wait before bringing it up again?",
    "options": [
        {"id": "a", "text": "Not long — within the hour, I was back with another approach", "scores": {"demand_withdraw": 2}},
        {"id": "b", "text": "I gave them the space they asked for and circled back at an agreed time", "scores": {"demand_withdraw": 5}},
        {"id": "c", "text": "I never brought it up again — the moment passed", "scores": {"demand_withdraw": 2}},
        {"id": "d", "text": "I brought it up when I couldn't hold it anymore, regardless of their readiness", "scores": {"demand_withdraw": 1}}
    ],
    "tier_role": "triangulation",
    "trap": False,
    "consistency_group": "pursuer_pattern",
    "opacity": 0.6,
    "cross_scores": [],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "demand_withdraw"]
})

questions.append({
    "dimension": "demand_withdraw",
    "question_type": "partner_perspective",
    "text": "Would your partner describe you as someone who chases them down during conflict, or someone who disappears?",
    "options": [
        {"id": "a", "text": "Chases — I follow them from room to room if I have to", "scores": {"demand_withdraw": 1}},
        {"id": "b", "text": "Disappears — I need solitude to process conflict", "scores": {"demand_withdraw": 2}},
        {"id": "c", "text": "Neither extreme — I give space but stay available", "scores": {"demand_withdraw": 5}},
        {"id": "d", "text": "It alternates — sometimes I pursue, sometimes I withdraw", "scores": {"demand_withdraw": 4}}
    ],
    "tier_role": "triangulation",
    "trap": False,
    "consistency_group": "role_flexibility",
    "opacity": 0.5,
    "cross_scores": [],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "demand_withdraw"]
})

questions.append({
    "dimension": "demand_withdraw",
    "question_type": "somatic",
    "text": "When you're the one being pursued — your partner keeps pressing for a conversation — what does your body want to do?",
    "options": [
        {"id": "a", "text": "Flee — I want to physically leave the space", "scores": {"demand_withdraw": 1}},
        {"id": "b", "text": "Freeze — I go blank and can't form words", "scores": {"demand_withdraw": 1}},
        {"id": "c", "text": "Stay but struggle — I'm physically present but it takes effort", "scores": {"demand_withdraw": 3}},
        {"id": "d", "text": "Engage — their persistence shows it matters, so I try to meet them", "scores": {"demand_withdraw": 5}}
    ],
    "tier_role": "triangulation",
    "trap": False,
    "consistency_group": "withdrawer_pattern",
    "opacity": 0.8,
    "cross_scores": [
        {"assessment": "emotional_regulation", "dimension": "flooding_response", "weight": 0.5}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "demand_withdraw", "somatic"]
})

questions.append({
    "dimension": "demand_withdraw",
    "question_type": "scenario",
    "text": "You and your partner have a recurring unresolved issue. Every time it comes up, the same dance happens: one pursues, one retreats. How do you break the cycle?",
    "options": [
        {"id": "a", "text": "Name the pattern out loud: 'We're doing the thing again. How do we approach this differently?'", "scores": {"demand_withdraw": 5}},
        {"id": "b", "text": "Push harder — eventually they'll have to engage", "scores": {"demand_withdraw": 1}},
        {"id": "c", "text": "Stop bringing it up — it's clear we can't resolve this", "scores": {"demand_withdraw": 2}},
        {"id": "d", "text": "Suggest professional help — we can't break this on our own", "scores": {"demand_withdraw": 4}}
    ],
    "tier_role": "triangulation",
    "trap": False,
    "consistency_group": "role_flexibility",
    "opacity": 0.6,
    "cross_scores": [
        {"assessment": "conflict_resolution", "dimension": "pattern_recognition", "weight": 0.5}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "demand_withdraw"]
})

questions.append({
    "dimension": "demand_withdraw",
    "question_type": "temporal",
    "text": "After a fight, how long can you tolerate silence from your partner before you feel compelled to act?",
    "options": [
        {"id": "a", "text": "Minutes — I need resolution immediately", "scores": {"demand_withdraw": 1}},
        {"id": "b", "text": "Hours — I can give some space but the anxiety builds", "scores": {"demand_withdraw": 3}},
        {"id": "c", "text": "Days — I actually prefer extended cool-down periods", "scores": {"demand_withdraw": 2}},
        {"id": "d", "text": "I don't feel compelled to act — I trust that we'll reconnect when we're both ready", "scores": {"demand_withdraw": 5}}
    ],
    "tier_role": "triangulation",
    "trap": False,
    "consistency_group": "pursuer_pattern",
    "opacity": 0.6,
    "cross_scores": [
        {"assessment": "attachment_style", "dimension": "anxious_activation", "weight": 0.5}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "demand_withdraw", "temporal"]
})

questions.append({
    "dimension": "demand_withdraw",
    "question_type": "behavioral_recall",
    "text": "When you withdraw from a conversation, is it a deliberate choice to regulate, or an automatic shutdown you can't control?",
    "options": [
        {"id": "a", "text": "Deliberate — I know when I need space and I communicate it", "scores": {"demand_withdraw": 5}},
        {"id": "b", "text": "Automatic — I just go numb and can't engage even if I want to", "scores": {"demand_withdraw": 2}},
        {"id": "c", "text": "A mix — sometimes strategic, sometimes involuntary", "scores": {"demand_withdraw": 3}},
        {"id": "d", "text": "I don't withdraw — I stay in every conversation to the end", "scores": {"demand_withdraw": 3}}
    ],
    "tier_role": "triangulation",
    "trap": False,
    "consistency_group": "withdrawer_pattern",
    "opacity": 0.6,
    "cross_scores": [
        {"assessment": "emotional_regulation", "dimension": "flooding_response", "weight": 0.5}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "demand_withdraw"]
})

# --- TRAP (7) ---
questions.append({
    "dimension": "demand_withdraw",
    "question_type": "scenario",
    "text": "I just want us to communicate. If my partner would just TALK to me instead of shutting down, everything would be fine.",
    "options": [
        {"id": "a", "text": "Exactly — the problem is their withdrawal, not my approach", "scores": {"demand_withdraw": 1}},
        {"id": "b", "text": "I feel this way, but I'm starting to see that my pursuing might be part of what makes them shut down", "scores": {"demand_withdraw": 4}},
        {"id": "c", "text": "The demand-withdraw cycle is co-created — both roles fuel the other", "scores": {"demand_withdraw": 5}},
        {"id": "d", "text": "They'd feel safer talking if I created more space and less pressure", "scores": {"demand_withdraw": 5}}
    ],
    "tier_role": "trap",
    "trap": True,
    "consistency_group": "pursuer_pattern",
    "opacity": 0.9,
    "cross_scores": [
        {"assessment": "attachment_style", "dimension": "anxious_activation", "weight": 0.5}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "demand_withdraw", "trap"]
})

questions.append({
    "dimension": "demand_withdraw",
    "question_type": "forced_choice",
    "text": "I give my partner plenty of space. If anything, I'm too accommodating of their need for distance.",
    "options": [
        {"id": "a", "text": "Strongly agree — I'm patient and non-demanding", "scores": {"demand_withdraw": 2}},
        {"id": "b", "text": "Somewhat agree — but 'giving space' might actually be my own avoidance in disguise", "scores": {"demand_withdraw": 4}},
        {"id": "c", "text": "Somewhat disagree — I think I could give more space than I do", "scores": {"demand_withdraw": 3}},
        {"id": "d", "text": "Strongly disagree — I know I tend to pursue", "scores": {"demand_withdraw": 3}}
    ],
    "tier_role": "trap",
    "trap": True,
    "consistency_group": "withdrawer_pattern",
    "opacity": 0.9,
    "cross_scores": [
        {"assessment": "attachment_style", "dimension": "avoidant_deactivation", "weight": 0.5}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "demand_withdraw", "trap"]
})

questions.append({
    "dimension": "demand_withdraw",
    "question_type": "partner_perspective",
    "text": "I'm not needy — I just have reasonable expectations for communication in a relationship.",
    "options": [
        {"id": "a", "text": "Absolutely — wanting to talk things through isn't neediness", "scores": {"demand_withdraw": 2}},
        {"id": "b", "text": "Mostly — but my 'reasonable' might feel like 'relentless' to my partner", "scores": {"demand_withdraw": 4}},
        {"id": "c", "text": "I should check whether my communication expectations match what's sustainable for both of us", "scores": {"demand_withdraw": 5}},
        {"id": "d", "text": "I've been told I'm intense about communication — maybe my bar is higher than average", "scores": {"demand_withdraw": 4}}
    ],
    "tier_role": "trap",
    "trap": True,
    "consistency_group": "pursuer_pattern",
    "opacity": 0.9,
    "cross_scores": [
        {"assessment": "attachment_style", "dimension": "anxious_activation", "weight": 0.4}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "demand_withdraw", "trap"]
})

questions.append({
    "dimension": "demand_withdraw",
    "question_type": "scenario",
    "text": "When my partner needs space, I respect it completely. I don't check in, I don't text, I just wait.",
    "options": [
        {"id": "a", "text": "That's healthy — respecting boundaries builds trust", "scores": {"demand_withdraw": 3}},
        {"id": "b", "text": "Mostly healthy — but complete radio silence might feel like abandonment to them", "scores": {"demand_withdraw": 4}},
        {"id": "c", "text": "A brief check-in ('I'm here when you're ready') shows both space and care", "scores": {"demand_withdraw": 5}},
        {"id": "d", "text": "I do this but honestly it's partly because I'm hurt and pulling away too", "scores": {"demand_withdraw": 2}}
    ],
    "tier_role": "trap",
    "trap": True,
    "consistency_group": "withdrawer_pattern",
    "opacity": 0.9,
    "cross_scores": [
        {"assessment": "attachment_style", "dimension": "avoidant_deactivation", "weight": 0.4}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "demand_withdraw", "trap"]
})

questions.append({
    "dimension": "demand_withdraw",
    "question_type": "behavioral_recall",
    "text": "I've been told I'm 'too much' or 'too intense' in how I pursue resolution. I disagree — I'm just invested in the relationship.",
    "options": [
        {"id": "a", "text": "Exactly — intensity shows I care", "scores": {"demand_withdraw": 1}},
        {"id": "b", "text": "I hear the feedback but struggle to modulate — the urgency feels real", "scores": {"demand_withdraw": 3}},
        {"id": "c", "text": "If multiple people have said this, there's probably something to it", "scores": {"demand_withdraw": 4}},
        {"id": "d", "text": "Investment and intensity aren't the same thing — I need to separate caring from controlling", "scores": {"demand_withdraw": 5}}
    ],
    "tier_role": "trap",
    "trap": True,
    "consistency_group": "pursuer_pattern",
    "opacity": 0.9,
    "cross_scores": [
        {"assessment": "attachment_style", "dimension": "protest_behavior", "weight": 0.5}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "demand_withdraw", "trap"]
})

questions.append({
    "dimension": "demand_withdraw",
    "question_type": "scenario",
    "text": "I don't withdraw — I just need to process things internally before I can talk about them. There's a difference.",
    "options": [
        {"id": "a", "text": "Absolutely — internal processing is legitimate and healthy", "scores": {"demand_withdraw": 3}},
        {"id": "b", "text": "True, but if my partner doesn't know when I'll be ready, my 'processing' functions like withdrawal to them", "scores": {"demand_withdraw": 5}},
        {"id": "c", "text": "I should communicate my timeline — 'I need 2 hours' is different from just going dark", "scores": {"demand_withdraw": 5}},
        {"id": "d", "text": "Sometimes what I call 'processing' is actually avoiding", "scores": {"demand_withdraw": 4}}
    ],
    "tier_role": "trap",
    "trap": True,
    "consistency_group": "withdrawer_pattern",
    "opacity": 0.9,
    "cross_scores": [
        {"assessment": "attachment_style", "dimension": "avoidant_deactivation", "weight": 0.4}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "demand_withdraw", "trap"]
})

questions.append({
    "dimension": "demand_withdraw",
    "question_type": "partner_perspective",
    "text": "Our conflicts would resolve faster if my partner just engaged when I'm ready instead of on their own timeline.",
    "options": [
        {"id": "a", "text": "True — their delay makes everything worse", "scores": {"demand_withdraw": 1}},
        {"id": "b", "text": "I feel this way, but 'my timeline' isn't automatically the right one", "scores": {"demand_withdraw": 4}},
        {"id": "c", "text": "We need to find a timeline that works for BOTH of us, not just whoever is more urgent", "scores": {"demand_withdraw": 5}},
        {"id": "d", "text": "Maybe the fact that I'm always 'ready' first says more about my anxiety than their avoidance", "scores": {"demand_withdraw": 5}}
    ],
    "tier_role": "trap",
    "trap": True,
    "consistency_group": "pursuer_pattern",
    "opacity": 0.9,
    "cross_scores": [
        {"assessment": "attachment_style", "dimension": "anxious_activation", "weight": 0.5}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "demand_withdraw", "trap"]
})

# --- CONSISTENCY CHECK (7) ---
questions.append({
    "dimension": "demand_withdraw",
    "question_type": "scenario",
    "text": "After an argument, you send your partner a long text explaining your feelings. They respond with 'Ok.' What do you do?",
    "options": [
        {"id": "a", "text": "Send another long text — they clearly didn't get it", "scores": {"demand_withdraw": 1}},
        {"id": "b", "text": "Accept the 'Ok' for now and trust we'll talk more later", "scores": {"demand_withdraw": 4}},
        {"id": "c", "text": "Feel devastated — I poured my heart out and got one word back", "scores": {"demand_withdraw": 2}},
        {"id": "d", "text": "Ask: 'Is Ok all you want to say, or do you need more time before we dig in?'", "scores": {"demand_withdraw": 5}}
    ],
    "tier_role": "consistency_check",
    "trap": False,
    "consistency_group": "pursuer_pattern",
    "opacity": 0.6,
    "cross_scores": [],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "demand_withdraw", "consistency"]
})

questions.append({
    "dimension": "demand_withdraw",
    "question_type": "behavioral_recall",
    "text": "When you need space during conflict, how do you communicate that to your partner?",
    "options": [
        {"id": "a", "text": "Clearly: 'I need X amount of time, and then I want to come back to this'", "scores": {"demand_withdraw": 5}},
        {"id": "b", "text": "Nonverbally: I just get quiet, leave, or start doing something else", "scores": {"demand_withdraw": 1}},
        {"id": "c", "text": "With frustration: 'Just leave me alone!' — which doesn't land well", "scores": {"demand_withdraw": 2}},
        {"id": "d", "text": "I don't usually need space — I prefer to push through to resolution", "scores": {"demand_withdraw": 3}}
    ],
    "tier_role": "consistency_check",
    "trap": False,
    "consistency_group": "withdrawer_pattern",
    "opacity": 0.5,
    "cross_scores": [],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "demand_withdraw", "consistency"]
})

questions.append({
    "dimension": "demand_withdraw",
    "question_type": "forced_choice",
    "text": "In your relationship, unresolved conflict tends to:",
    "options": [
        {"id": "a", "text": "Get discussed to death because one of us won't let it rest until it's resolved", "scores": {"demand_withdraw": 2}},
        {"id": "b", "text": "Get buried because one or both of us avoid circling back to it", "scores": {"demand_withdraw": 2}}
    ],
    "tier_role": "consistency_check",
    "trap": False,
    "consistency_group": "role_flexibility",
    "opacity": 0.5,
    "cross_scores": [],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "demand_withdraw", "consistency"]
})

questions.append({
    "dimension": "demand_withdraw",
    "question_type": "partner_perspective",
    "text": "Would your partner say you make them feel safe to come to you with difficult topics, or do they feel they have to pick the perfect moment?",
    "options": [
        {"id": "a", "text": "Safe — they know I'll engage without overwhelming them or shutting down", "scores": {"demand_withdraw": 5}},
        {"id": "b", "text": "They pick their moments — because my reaction varies and they're trying to minimize fallout", "scores": {"demand_withdraw": 3}},
        {"id": "c", "text": "They probably avoid certain topics altogether because of how I've responded before", "scores": {"demand_withdraw": 1}},
        {"id": "d", "text": "I'm not sure — I've never asked them this directly", "scores": {"demand_withdraw": 3}}
    ],
    "tier_role": "consistency_check",
    "trap": False,
    "consistency_group": "withdrawer_pattern",
    "opacity": 0.6,
    "cross_scores": [
        {"assessment": "attachment_style", "dimension": "relationship_security", "weight": 0.5}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "demand_withdraw", "consistency"]
})

questions.append({
    "dimension": "demand_withdraw",
    "question_type": "somatic",
    "text": "When an important conversation keeps getting postponed or avoided in your relationship, what builds in your body over the days?",
    "options": [
        {"id": "a", "text": "Anxiety — a constant low-grade tension that only resolving the issue can release", "scores": {"demand_withdraw": 2}},
        {"id": "b", "text": "Nothing particular — I'm patient and trust it'll happen when it's time", "scores": {"demand_withdraw": 4}},
        {"id": "c", "text": "Resentment — a slow burn in my chest or stomach", "scores": {"demand_withdraw": 2}},
        {"id": "d", "text": "Relief that keeps getting more uncomfortable — I know avoidance isn't solving anything", "scores": {"demand_withdraw": 3}}
    ],
    "tier_role": "consistency_check",
    "trap": False,
    "consistency_group": "pursuer_pattern",
    "opacity": 0.7,
    "cross_scores": [
        {"assessment": "emotional_regulation", "dimension": "distress_tolerance", "weight": 0.4}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "demand_withdraw", "consistency"]
})

questions.append({
    "dimension": "demand_withdraw",
    "question_type": "temporal",
    "text": "How has the balance of pursuing vs. withdrawing shifted in your relationship over time?",
    "options": [
        {"id": "a", "text": "We've found a middle ground — both of us can initiate and both can take space", "scores": {"demand_withdraw": 5}},
        {"id": "b", "text": "It's gotten more entrenched — our roles are more rigid now", "scores": {"demand_withdraw": 1}},
        {"id": "c", "text": "One of us gave up pursuing, so now there's just... silence", "scores": {"demand_withdraw": 1}},
        {"id": "d", "text": "It shifts depending on the season and stress levels", "scores": {"demand_withdraw": 3}}
    ],
    "tier_role": "consistency_check",
    "trap": False,
    "consistency_group": "role_flexibility",
    "opacity": 0.5,
    "cross_scores": [],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "demand_withdraw", "consistency"]
})

questions.append({
    "dimension": "demand_withdraw",
    "question_type": "scenario",
    "text": "Your partner says 'I feel like I can't talk to you about this.' Your immediate internal response is:",
    "options": [
        {"id": "a", "text": "'What have I done that makes them feel that way?' — genuine curiosity and concern", "scores": {"demand_withdraw": 5}},
        {"id": "b", "text": "'That's not fair — I'm always willing to talk!' — defensive", "scores": {"demand_withdraw": 2}},
        {"id": "c", "text": "'Then don't' — withdrawn", "scores": {"demand_withdraw": 1}},
        {"id": "d", "text": "'I want you to feel safe. Tell me what would make this easier.' — solution-seeking", "scores": {"demand_withdraw": 5}}
    ],
    "tier_role": "consistency_check",
    "trap": False,
    "consistency_group": "role_flexibility",
    "opacity": 0.6,
    "cross_scores": [
        {"assessment": "four_horsemen", "dimension": "four_horsemen", "weight": 0.3}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "demand_withdraw", "consistency"]
})

with open('/tmp/comm_q_part6.json', 'w') as f:
    json.dump(questions, f, indent=2)
print(f"Part 6: {len(questions)} demand_withdraw questions written")
