import json

questions = []

# ============================================================
# DIMENSION 4: SOFT STARTUP (29 questions)
# 3 core + 12 triangulation + 7 trap + 7 consistency
# ============================================================

# --- CORE (3) ---
questions.append({
    "dimension": "soft_startup",
    "question_type": "scenario",
    "text": "Your partner has been spending a lot of time on their phone during dinner. It's been bothering you. You decide to bring it up. What comes out?",
    "options": [
        {"id": "a", "text": "'I've been feeling disconnected at dinner lately. Can we try putting phones away while we eat?'", "scores": {"soft_startup": 5}},
        {"id": "b", "text": "'You're always on your phone at dinner. It's rude.'", "scores": {"soft_startup": 1}},
        {"id": "c", "text": "'Do you think you could maybe look at your phone less at dinner?'", "scores": {"soft_startup": 3}},
        {"id": "d", "text": "I don't bring it up — I just start doing the same thing", "scores": {"soft_startup": 2, "demand_withdraw": 2}}
    ],
    "tier_role": "core",
    "trap": False,
    "consistency_group": "complaint_vs_criticism",
    "opacity": 0.6,
    "cross_scores": [
        {"assessment": "conflict_resolution", "dimension": "issue_raising", "weight": 0.5}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "startup"]
})

questions.append({
    "dimension": "soft_startup",
    "question_type": "behavioral_recall",
    "text": "Think about the last time you raised a concern with your partner. Did you lead with 'I feel...' or 'You always/never...'?",
    "options": [
        {"id": "a", "text": "I led with my feeling and a specific situation", "scores": {"soft_startup": 5}},
        {"id": "b", "text": "I probably started with 'you' and a generalization — old habit", "scores": {"soft_startup": 2}},
        {"id": "c", "text": "I started calmly but it quickly shifted into criticism as emotion took over", "scores": {"soft_startup": 3}},
        {"id": "d", "text": "I haven't raised a concern recently — I tend to let things go", "scores": {"soft_startup": 2, "demand_withdraw": 2}}
    ],
    "tier_role": "core",
    "trap": False,
    "consistency_group": "complaint_vs_criticism",
    "opacity": 0.5,
    "cross_scores": [
        {"assessment": "emotional_regulation", "dimension": "emotional_vocabulary", "weight": 0.4}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "startup"]
})

questions.append({
    "dimension": "soft_startup",
    "question_type": "partner_perspective",
    "text": "When your partner hears you start a difficult conversation, do they brace for impact or lean in to listen?",
    "options": [
        {"id": "a", "text": "They lean in — they know I'll be fair even when I'm upset", "scores": {"soft_startup": 5}},
        {"id": "b", "text": "They brace — my track record of starting gently isn't great", "scores": {"soft_startup": 2}},
        {"id": "c", "text": "It depends on the topic and my tone in the first few words", "scores": {"soft_startup": 3}},
        {"id": "d", "text": "They get defensive immediately — regardless of how I start", "scores": {"soft_startup": 3}}
    ],
    "tier_role": "core",
    "trap": False,
    "consistency_group": "startup_impact",
    "opacity": 0.6,
    "cross_scores": [
        {"assessment": "attachment_style", "dimension": "relationship_security", "weight": 0.4}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "startup"]
})

# --- TRIANGULATION (12) ---
questions.append({
    "dimension": "soft_startup",
    "question_type": "scenario",
    "text": "The house is a mess and you feel like you've been carrying the load. You want your partner to step up. What do you say?",
    "options": [
        {"id": "a", "text": "'I'm feeling overwhelmed with the housework. Can we figure out a better split?'", "scores": {"soft_startup": 5}},
        {"id": "b", "text": "'I'm the only one who ever cleans around here.'", "scores": {"soft_startup": 1}},
        {"id": "c", "text": "'Would you mind helping out more? The house is really getting to me.'", "scores": {"soft_startup": 4}},
        {"id": "d", "text": "I clean it myself in a visible, resentful way so they notice", "scores": {"soft_startup": 1}}
    ],
    "tier_role": "triangulation",
    "trap": False,
    "consistency_group": "complaint_vs_criticism",
    "opacity": 0.5,
    "cross_scores": [],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "startup"]
})

questions.append({
    "dimension": "soft_startup",
    "question_type": "forced_choice",
    "text": "When you need to raise something difficult, which is more natural for you?",
    "options": [
        {"id": "a", "text": "Start with what I'm feeling and need — make it about the situation, not their character", "scores": {"soft_startup": 5}},
        {"id": "b", "text": "Start with the problem and what they need to change — be direct about the issue", "scores": {"soft_startup": 2}}
    ],
    "tier_role": "triangulation",
    "trap": False,
    "consistency_group": "complaint_vs_criticism",
    "opacity": 0.5,
    "cross_scores": [],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "startup"]
})

questions.append({
    "dimension": "soft_startup",
    "question_type": "somatic",
    "text": "When you're about to bring up something that's been bothering you, what happens in your body in the moments before you speak?",
    "options": [
        {"id": "a", "text": "I take a breath, organize my thoughts, and feel relatively grounded", "scores": {"soft_startup": 5}},
        {"id": "b", "text": "I feel a surge of emotion — the words come out before I've filtered them", "scores": {"soft_startup": 2}},
        {"id": "c", "text": "My throat tightens — I struggle to get the words out at all", "scores": {"soft_startup": 3}},
        {"id": "d", "text": "I feel a rush of adrenaline — like I'm preparing for battle", "scores": {"soft_startup": 2}}
    ],
    "tier_role": "triangulation",
    "trap": False,
    "consistency_group": "startup_preparation",
    "opacity": 0.8,
    "cross_scores": [
        {"assessment": "emotional_regulation", "dimension": "pre_expression_awareness", "weight": 0.6}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "startup", "somatic"]
})

questions.append({
    "dimension": "soft_startup",
    "question_type": "temporal",
    "text": "Do you think about timing when you raise issues with your partner — or do you bring things up whenever they hit you?",
    "options": [
        {"id": "a", "text": "I'm deliberate about timing — I pick moments when we're both calm and present", "scores": {"soft_startup": 5}},
        {"id": "b", "text": "I try to wait for good timing but often blurt things out when I'm triggered", "scores": {"soft_startup": 3}},
        {"id": "c", "text": "I bring things up when they happen — waiting feels like suppressing", "scores": {"soft_startup": 3}},
        {"id": "d", "text": "I wait so long that by the time I bring it up, I'm already resentful", "scores": {"soft_startup": 1}}
    ],
    "tier_role": "triangulation",
    "trap": False,
    "consistency_group": "startup_preparation",
    "opacity": 0.6,
    "cross_scores": [
        {"assessment": "emotional_regulation", "dimension": "impulse_control", "weight": 0.4}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "startup", "temporal"]
})

questions.append({
    "dimension": "soft_startup",
    "question_type": "scenario",
    "text": "Your partner forgot an important date — your anniversary, a family event, etc. You feel hurt. What do you say?",
    "options": [
        {"id": "a", "text": "'It really hurt that you forgot. It makes me feel like it's not important to you.'", "scores": {"soft_startup": 5}},
        {"id": "b", "text": "'You forgot. Again. Why am I not surprised.'", "scores": {"soft_startup": 1}},
        {"id": "c", "text": "'Did you seriously forget? What is wrong with you?'", "scores": {"soft_startup": 1}},
        {"id": "d", "text": "I don't mention it — I don't want to guilt them", "scores": {"soft_startup": 2}}
    ],
    "tier_role": "triangulation",
    "trap": False,
    "consistency_group": "complaint_vs_criticism",
    "opacity": 0.6,
    "cross_scores": [
        {"assessment": "four_horsemen", "dimension": "four_horsemen", "weight": 0.4}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "startup"]
})

questions.append({
    "dimension": "soft_startup",
    "question_type": "partner_perspective",
    "text": "If your partner described how you typically start difficult conversations, would they say you lead with blame or with vulnerability?",
    "options": [
        {"id": "a", "text": "Vulnerability — I share what I'm feeling before accusing", "scores": {"soft_startup": 5}},
        {"id": "b", "text": "Blame — I tend to come in hot even when I don't mean to", "scores": {"soft_startup": 2}},
        {"id": "c", "text": "A mix — it depends on how much the issue has been festering", "scores": {"soft_startup": 3}},
        {"id": "d", "text": "They'd say I avoid difficult conversations altogether", "scores": {"soft_startup": 2}}
    ],
    "tier_role": "triangulation",
    "trap": False,
    "consistency_group": "startup_impact",
    "opacity": 0.5,
    "cross_scores": [
        {"assessment": "self_worth", "dimension": "vulnerability_tolerance", "weight": 0.4}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "startup"]
})

questions.append({
    "dimension": "soft_startup",
    "question_type": "behavioral_recall",
    "text": "Think of a recent complaint you had about your partner. Did you distinguish between the behavior you didn't like and their character?",
    "options": [
        {"id": "a", "text": "Yes — I addressed what they did, not who they are", "scores": {"soft_startup": 5}},
        {"id": "b", "text": "I tried to, but it came out as a character statement anyway", "scores": {"soft_startup": 3}},
        {"id": "c", "text": "No — I went straight for who they are as a person", "scores": {"soft_startup": 1}},
        {"id": "d", "text": "I didn't voice the complaint at all", "scores": {"soft_startup": 2}}
    ],
    "tier_role": "triangulation",
    "trap": False,
    "consistency_group": "complaint_vs_criticism",
    "opacity": 0.6,
    "cross_scores": [
        {"assessment": "cognitive_distortions", "dimension": "labeling", "weight": 0.4}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "startup"]
})

questions.append({
    "dimension": "soft_startup",
    "question_type": "scenario",
    "text": "You need to tell your partner something they won't want to hear — maybe about their family, a habit, or a decision. You:",
    "options": [
        {"id": "a", "text": "Preface with appreciation or context before delivering the hard part", "scores": {"soft_startup": 5}},
        {"id": "b", "text": "Just say it directly — beating around the bush is worse", "scores": {"soft_startup": 3}},
        {"id": "c", "text": "Hint at it and hope they pick up on what I mean", "scores": {"soft_startup": 2}},
        {"id": "d", "text": "Avoid it until it becomes unavoidable, then it comes out loaded", "scores": {"soft_startup": 1}}
    ],
    "tier_role": "triangulation",
    "trap": False,
    "consistency_group": "startup_preparation",
    "opacity": 0.7,
    "cross_scores": [],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "startup"]
})

questions.append({
    "dimension": "soft_startup",
    "question_type": "somatic",
    "text": "When your partner starts a conversation with an accusatory tone, what happens in your body — and what do you do with that feeling?",
    "options": [
        {"id": "a", "text": "I tense up but try to focus on what they're actually saying underneath the tone", "scores": {"soft_startup": 4}},
        {"id": "b", "text": "I immediately mirror their intensity — their harsh startup provokes a harsh response", "scores": {"soft_startup": 2}},
        {"id": "c", "text": "I shut down — the harsh tone makes me unable to hear the content", "scores": {"soft_startup": 2}},
        {"id": "d", "text": "I try to gently name it: 'I want to hear you, but the way you're starting is making it hard'", "scores": {"soft_startup": 5}}
    ],
    "tier_role": "triangulation",
    "trap": False,
    "consistency_group": "startup_impact",
    "opacity": 0.7,
    "cross_scores": [
        {"assessment": "emotional_regulation", "dimension": "reactivity_management", "weight": 0.5}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "startup", "somatic"]
})

questions.append({
    "dimension": "soft_startup",
    "question_type": "temporal",
    "text": "Has your ability to raise issues constructively improved over the years, or have bad habits calcified?",
    "options": [
        {"id": "a", "text": "Improved — I've learned the hard way that how I start determines how it ends", "scores": {"soft_startup": 5}},
        {"id": "b", "text": "Calcified — I know what I should do but under stress I revert to old patterns", "scores": {"soft_startup": 2}},
        {"id": "c", "text": "Mixed — better in some areas, worse in the sore spots", "scores": {"soft_startup": 3}},
        {"id": "d", "text": "I've given up trying to raise issues at all", "scores": {"soft_startup": 1}}
    ],
    "tier_role": "triangulation",
    "trap": False,
    "consistency_group": "complaint_vs_criticism",
    "opacity": 0.5,
    "cross_scores": [],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "startup", "temporal"]
})

questions.append({
    "dimension": "soft_startup",
    "question_type": "behavioral_recall",
    "text": "When you're frustrated and want to say 'You always...' or 'You never...', what do you actually do?",
    "options": [
        {"id": "a", "text": "Catch myself and rephrase: 'When X happens, I feel Y'", "scores": {"soft_startup": 5}},
        {"id": "b", "text": "Say it — in the moment, it feels true even if it's not literally accurate", "scores": {"soft_startup": 2}},
        {"id": "c", "text": "Sometimes catch it, sometimes don't — depends on how activated I am", "scores": {"soft_startup": 3}},
        {"id": "d", "text": "I don't use those words but my tone communicates the same thing", "scores": {"soft_startup": 2}}
    ],
    "tier_role": "triangulation",
    "trap": False,
    "consistency_group": "complaint_vs_criticism",
    "opacity": 0.6,
    "cross_scores": [
        {"assessment": "cognitive_distortions", "dimension": "overgeneralization", "weight": 0.5}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "startup"]
})

# --- TRAP (7) ---
questions.append({
    "dimension": "soft_startup",
    "question_type": "scenario",
    "text": "I believe in being direct and honest, even if it's uncomfortable. Sugarcoating issues is dishonest and wastes time.",
    "options": [
        {"id": "a", "text": "Strongly agree — directness is a virtue, even if it stings", "scores": {"soft_startup": 2}},
        {"id": "b", "text": "Somewhat agree — but HOW you deliver honesty matters as much as the honesty itself", "scores": {"soft_startup": 4}},
        {"id": "c", "text": "Somewhat disagree — gentleness isn't sugarcoating, it's respect", "scores": {"soft_startup": 5}},
        {"id": "d", "text": "Strongly disagree — harsh honesty is just cruelty with a badge", "scores": {"soft_startup": 5}}
    ],
    "tier_role": "trap",
    "trap": True,
    "consistency_group": "complaint_vs_criticism",
    "opacity": 0.9,
    "cross_scores": [
        {"assessment": "boundary_style", "dimension": "assertiveness_style", "weight": 0.3}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "startup", "trap"]
})

questions.append({
    "dimension": "soft_startup",
    "question_type": "partner_perspective",
    "text": "My partner is too sensitive — I have to walk on eggshells just to raise a simple issue.",
    "options": [
        {"id": "a", "text": "Strongly agree — their sensitivity makes honest communication impossible", "scores": {"soft_startup": 1}},
        {"id": "b", "text": "Somewhat agree — but maybe my delivery contributes to their reaction", "scores": {"soft_startup": 3}},
        {"id": "c", "text": "Somewhat disagree — what I call 'sensitivity' might be a response to how I approach them", "scores": {"soft_startup": 4}},
        {"id": "d", "text": "Strongly disagree — I need to examine my own approach before blaming their reaction", "scores": {"soft_startup": 5}}
    ],
    "tier_role": "trap",
    "trap": True,
    "consistency_group": "startup_impact",
    "opacity": 0.9,
    "cross_scores": [
        {"assessment": "four_horsemen", "dimension": "four_horsemen", "weight": 0.4}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "startup", "trap"]
})

questions.append({
    "dimension": "soft_startup",
    "question_type": "forced_choice",
    "text": "If I've asked nicely three times and nothing changes, I'm justified in being more forceful the fourth time.",
    "options": [
        {"id": "a", "text": "Absolutely — they had their chances", "scores": {"soft_startup": 2}},
        {"id": "b", "text": "Understandable, but escalation usually backfires — maybe the approach itself needs changing", "scores": {"soft_startup": 4}},
        {"id": "c", "text": "No — the principle of soft startup applies every time, not just the first three", "scores": {"soft_startup": 5}},
        {"id": "d", "text": "Maybe — but I should first ask why it hasn't changed rather than getting louder", "scores": {"soft_startup": 4}}
    ],
    "tier_role": "trap",
    "trap": True,
    "consistency_group": "complaint_vs_criticism",
    "opacity": 0.9,
    "cross_scores": [
        {"assessment": "conflict_resolution", "dimension": "escalation_tendency", "weight": 0.4}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "startup", "trap"]
})

questions.append({
    "dimension": "soft_startup",
    "question_type": "scenario",
    "text": "I express my needs clearly and assertively. If my partner gets upset, that's their issue to manage — I can't control their reaction.",
    "options": [
        {"id": "a", "text": "Exactly — I'm responsible for my message, not their feelings about it", "scores": {"soft_startup": 2}},
        {"id": "b", "text": "Partly true — but I am responsible for choosing delivery that doesn't unnecessarily wound", "scores": {"soft_startup": 4}},
        {"id": "c", "text": "This sounds like a way to avoid accountability for harsh communication", "scores": {"soft_startup": 5}},
        {"id": "d", "text": "I try not to think about their reaction too much — otherwise I'd never bring anything up", "scores": {"soft_startup": 2}}
    ],
    "tier_role": "trap",
    "trap": True,
    "consistency_group": "startup_impact",
    "opacity": 0.9,
    "cross_scores": [
        {"assessment": "boundary_style", "dimension": "empathic_consideration", "weight": 0.4}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "startup", "trap"]
})

questions.append({
    "dimension": "soft_startup",
    "question_type": "behavioral_recall",
    "text": "When I start a conversation about a problem, I make sure to include positive context — 'I love how we X, but I'm struggling with Y.'",
    "options": [
        {"id": "a", "text": "Always — framing matters and softens the landing", "scores": {"soft_startup": 4}},
        {"id": "b", "text": "Sometimes — but it can feel manipulative or like a 'compliment sandwich'", "scores": {"soft_startup": 3}},
        {"id": "c", "text": "Rarely — I get straight to the point", "scores": {"soft_startup": 2}},
        {"id": "d", "text": "I've tried this and my partner sees through it — they brace for the 'but'", "scores": {"soft_startup": 3}}
    ],
    "tier_role": "trap",
    "trap": True,
    "consistency_group": "startup_preparation",
    "opacity": 0.8,
    "cross_scores": [],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "startup", "trap"]
})

questions.append({
    "dimension": "soft_startup",
    "question_type": "partner_perspective",
    "text": "I've noticed that when I bring up issues calmly, my partner still gets defensive. So why bother being gentle?",
    "options": [
        {"id": "a", "text": "Good point — if gentle doesn't work, might as well be direct", "scores": {"soft_startup": 1}},
        {"id": "b", "text": "Their defensiveness might be a pattern worth exploring separately — but that doesn't mean abandoning soft startup", "scores": {"soft_startup": 5}},
        {"id": "c", "text": "Maybe what I think is 'calm' still has an edge they're reacting to", "scores": {"soft_startup": 4}},
        {"id": "d", "text": "It's discouraging, but the research says gentle startup still leads to better outcomes over time", "scores": {"soft_startup": 4}}
    ],
    "tier_role": "trap",
    "trap": True,
    "consistency_group": "startup_impact",
    "opacity": 0.8,
    "cross_scores": [
        {"assessment": "four_horsemen", "dimension": "four_horsemen", "weight": 0.3}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "startup", "trap"]
})

questions.append({
    "dimension": "soft_startup",
    "question_type": "scenario",
    "text": "When I'm really upset, the 'I feel' framework goes out the window. I can't process emotions and craft careful language simultaneously.",
    "options": [
        {"id": "a", "text": "Exactly — in the heat of the moment, careful language is unrealistic", "scores": {"soft_startup": 2}},
        {"id": "b", "text": "That's why I've learned to wait until I've calmed down before starting the conversation", "scores": {"soft_startup": 5}},
        {"id": "c", "text": "True — but I'm working on building it as a habit so it becomes more automatic", "scores": {"soft_startup": 4}},
        {"id": "d", "text": "I accept this about myself and my partner has learned to filter for it", "scores": {"soft_startup": 2}}
    ],
    "tier_role": "trap",
    "trap": True,
    "consistency_group": "startup_preparation",
    "opacity": 0.8,
    "cross_scores": [
        {"assessment": "emotional_regulation", "dimension": "state_dependent_behavior", "weight": 0.5}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "startup", "trap"]
})

# --- CONSISTENCY CHECK (7) ---
questions.append({
    "dimension": "soft_startup",
    "question_type": "scenario",
    "text": "You and your partner are having a calm evening. You realize you need to mention something that's been on your mind — nothing huge but mildly sensitive. When do you do it?",
    "options": [
        {"id": "a", "text": "Now — we're both relaxed, good timing for a gentle conversation", "scores": {"soft_startup": 5}},
        {"id": "b", "text": "I table it for another time — I don't want to ruin the nice evening", "scores": {"soft_startup": 2}},
        {"id": "c", "text": "I test the waters with a related topic to see their mood first", "scores": {"soft_startup": 3}},
        {"id": "d", "text": "I blurt it out and then regret the timing", "scores": {"soft_startup": 2}}
    ],
    "tier_role": "consistency_check",
    "trap": False,
    "consistency_group": "startup_preparation",
    "opacity": 0.6,
    "cross_scores": [],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "startup", "consistency"]
})

questions.append({
    "dimension": "soft_startup",
    "question_type": "behavioral_recall",
    "text": "In your last three difficult conversations with your partner, how many did you open with a specific behavior rather than a character judgment?",
    "options": [
        {"id": "a", "text": "All three — I focused on actions, not personality", "scores": {"soft_startup": 5}},
        {"id": "b", "text": "Two of three — I mostly get this right", "scores": {"soft_startup": 4}},
        {"id": "c", "text": "One at best — I tend to make it about who they are", "scores": {"soft_startup": 2}},
        {"id": "d", "text": "I haven't had three difficult conversations recently — I avoid them", "scores": {"soft_startup": 2}}
    ],
    "tier_role": "consistency_check",
    "trap": False,
    "consistency_group": "complaint_vs_criticism",
    "opacity": 0.5,
    "cross_scores": [],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "startup", "consistency"]
})

questions.append({
    "dimension": "soft_startup",
    "question_type": "forced_choice",
    "text": "Which better describes how you typically begin a complaint?",
    "options": [
        {"id": "a", "text": "'When [specific thing] happened, I felt [emotion]. I need [specific change].'", "scores": {"soft_startup": 5}},
        {"id": "b", "text": "'Why do you always [behavior]? You never [desired behavior].'", "scores": {"soft_startup": 1}}
    ],
    "tier_role": "consistency_check",
    "trap": False,
    "consistency_group": "complaint_vs_criticism",
    "opacity": 0.4,
    "cross_scores": [],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "startup", "consistency"]
})

questions.append({
    "dimension": "soft_startup",
    "question_type": "partner_perspective",
    "text": "Would your partner say that your complaints focus on specific situations, or do they feel like indictments of their character?",
    "options": [
        {"id": "a", "text": "Specific situations — I'm good at separating behavior from identity", "scores": {"soft_startup": 5}},
        {"id": "b", "text": "They might feel indicted sometimes, even when I don't mean to attack their character", "scores": {"soft_startup": 3}},
        {"id": "c", "text": "Probably indictments — I know I tend to globalize", "scores": {"soft_startup": 2}},
        {"id": "d", "text": "They'd say I don't complain at all, which is its own problem", "scores": {"soft_startup": 2}}
    ],
    "tier_role": "consistency_check",
    "trap": False,
    "consistency_group": "startup_impact",
    "opacity": 0.5,
    "cross_scores": [],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "startup", "consistency"]
})

questions.append({
    "dimension": "soft_startup",
    "question_type": "somatic",
    "text": "Right before you raise an issue with your partner, do you feel more like a prosecutor building a case or a partner sharing a concern?",
    "options": [
        {"id": "a", "text": "A partner sharing a concern — I approach with openness", "scores": {"soft_startup": 5}},
        {"id": "b", "text": "A prosecutor, honestly — I often prepare evidence and examples", "scores": {"soft_startup": 2}},
        {"id": "c", "text": "It depends on the issue — some topics feel adversarial, others collaborative", "scores": {"soft_startup": 3}},
        {"id": "d", "text": "A defendant — I'm bracing for their reaction more than focused on my message", "scores": {"soft_startup": 3}}
    ],
    "tier_role": "consistency_check",
    "trap": False,
    "consistency_group": "startup_preparation",
    "opacity": 0.7,
    "cross_scores": [
        {"assessment": "conflict_resolution", "dimension": "adversarial_framing", "weight": 0.4}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "startup", "consistency"]
})

questions.append({
    "dimension": "soft_startup",
    "question_type": "temporal",
    "text": "Think about how you raised issues 5 years ago vs. now. What changed?",
    "options": [
        {"id": "a", "text": "I'm significantly better — more 'I' statements, less blame, better timing", "scores": {"soft_startup": 5}},
        {"id": "b", "text": "About the same — this is just how I communicate under stress", "scores": {"soft_startup": 2}},
        {"id": "c", "text": "I raise fewer issues now — not because I'm gentler but because I've given up on some things", "scores": {"soft_startup": 1}},
        {"id": "d", "text": "I'm more measured, but that's partly because I've learned to suppress rather than express", "scores": {"soft_startup": 2}}
    ],
    "tier_role": "consistency_check",
    "trap": False,
    "consistency_group": "complaint_vs_criticism",
    "opacity": 0.6,
    "cross_scores": [],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "startup", "consistency"]
})

questions.append({
    "dimension": "soft_startup",
    "question_type": "scenario",
    "text": "You catch yourself about to say something critical. You stop mid-sentence. What do you do next?",
    "options": [
        {"id": "a", "text": "Rephrase: 'Let me start over. What I mean is...'", "scores": {"soft_startup": 5, "repair_repertoire": 4}},
        {"id": "b", "text": "Just stop talking — I don't know how to say it any other way right now", "scores": {"soft_startup": 3}},
        {"id": "c", "text": "Push through — the sentiment was right even if the words weren't perfect", "scores": {"soft_startup": 2}},
        {"id": "d", "text": "This rarely happens — I don't catch myself mid-criticism", "scores": {"soft_startup": 1}}
    ],
    "tier_role": "consistency_check",
    "trap": False,
    "consistency_group": "startup_preparation",
    "opacity": 0.6,
    "cross_scores": [
        {"assessment": "emotional_regulation", "dimension": "real_time_correction", "weight": 0.4}
    ],
    "universal": True,
    "adaptations_needed": [],
    "tags": ["communication", "relationship", "gottman", "startup", "consistency"]
})

with open('/tmp/comm_q_part4.json', 'w') as f:
    json.dump(questions, f, indent=2)
print(f"Part 4: {len(questions)} soft_startup questions written")
