import json

with open("/Users/user/personal/sb/trueassess/priv/question_bank/emotional_regulation.json") as f:
    questions = json.load(f)

uid_counter = 142
def make_uid():
    global uid_counter
    uid_counter += 1
    return f"er_{uid_counter:03d}"

# Need: 1 impulse_control, 1 emotional_awareness, 4 strategy_repertoire, 1 recovery_speed, 1 window_of_tolerance = 8

extras = [
    {
        "uid": make_uid(), "assessment_id": "emotional_regulation", "dimension": "impulse_control",
        "question_type": "scenario",
        "text": "You're mid-argument and your partner says something that triggers a memory of your ex doing the same thing. The urge to bring up the ex comparison is overwhelming. What do you do?",
        "options": [
            {"id": "a", "text": "I say it—the parallel is too obvious not to point out", "scores": {"impulse_control": 1}},
            {"id": "b", "text": "I catch myself mid-sentence and redirect: 'That's not fair. Let me rephrase.'", "scores": {"impulse_control": 4}},
            {"id": "c", "text": "I don't even consider saying it—past relationships stay out of current arguments", "scores": {"impulse_control": 5}},
            {"id": "d", "text": "I don't say the name but my partner can tell I'm thinking it", "scores": {"impulse_control": 3}}
        ],
        "cross_scores": [], "anti_gaming": {"opacity": 0.7, "social_desirability_trap": False, "consistency_group": "ic_ex_compare_1", "reversal": False},
        "cultural_adaptability": {"universal": True, "adaptations_needed": [], "adaptation_notes": None},
        "content_rating": "G", "content_categories": [], "depth_tier": "deep", "tier_role": "triangulation",
        "tags": ["emotional_regulation", "impulse_control", "triangulation"]
    },
    {
        "uid": make_uid(), "assessment_id": "emotional_regulation", "dimension": "emotional_awareness",
        "question_type": "temporal",
        "text": "Think about the last time you said 'I'm fine' when you weren't. How quickly did you realize you'd been dishonest with yourself?",
        "options": [
            {"id": "a", "text": "Immediately—I knew I was lying but chose to say it anyway", "scores": {"emotional_awareness": 4}},
            {"id": "b", "text": "Hours later—it dawned on me that I wasn't actually fine", "scores": {"emotional_awareness": 2}},
            {"id": "c", "text": "Someone else pointed it out—'you don't seem fine'", "scores": {"emotional_awareness": 1}},
            {"id": "d", "text": "I don't say 'I'm fine' when I'm not—I've trained myself out of that reflex", "scores": {"emotional_awareness": 5}}
        ],
        "cross_scores": [], "anti_gaming": {"opacity": 0.6, "social_desirability_trap": True, "consistency_group": "ea_fine_1", "reversal": False},
        "cultural_adaptability": {"universal": True, "adaptations_needed": [], "adaptation_notes": None},
        "content_rating": "G", "content_categories": [], "depth_tier": "moderate", "tier_role": "trap",
        "tags": ["emotional_regulation", "emotional_awareness", "trap", "self_honesty"]
    },
    {
        "uid": make_uid(), "assessment_id": "emotional_regulation", "dimension": "strategy_repertoire",
        "question_type": "scenario",
        "text": "You're feeling overwhelmed at work but can't take a break. What micro-regulation strategy do you use at your desk?",
        "options": [
            {"id": "a", "text": "Box breathing (4 counts in, 4 hold, 4 out, 4 hold) that no one around me notices", "scores": {"strategy_repertoire": 5}},
            {"id": "b", "text": "I grip my chair or press my feet into the floor for grounding", "scores": {"strategy_repertoire": 4}},
            {"id": "c", "text": "I just push through—I don't have desk-friendly regulation strategies", "scores": {"strategy_repertoire": 1}},
            {"id": "d", "text": "I open a mindless tab (social media, news) for a mental break", "scores": {"strategy_repertoire": 2}}
        ],
        "cross_scores": [], "anti_gaming": {"opacity": 0.7, "social_desirability_trap": False, "consistency_group": "sr_desk_1", "reversal": False},
        "cultural_adaptability": {"universal": True, "adaptations_needed": [], "adaptation_notes": None},
        "content_rating": "G", "content_categories": [], "depth_tier": "moderate", "tier_role": "triangulation",
        "tags": ["emotional_regulation", "strategy_repertoire", "triangulation"]
    },
    {
        "uid": make_uid(), "assessment_id": "emotional_regulation", "dimension": "strategy_repertoire",
        "question_type": "behavioral_recall",
        "text": "Do you have a 'calm down playlist,' a specific place you go, or a sensory tool (essential oil, texture, temperature) that you use specifically for emotional regulation?",
        "options": [
            {"id": "a", "text": "Yes to multiple—I've curated specific sensory tools for regulation", "scores": {"strategy_repertoire": 5}},
            {"id": "b", "text": "One or two things, but they're more accidental than intentional", "scores": {"strategy_repertoire": 3}},
            {"id": "c", "text": "No—I haven't thought to create environmental regulation tools", "scores": {"strategy_repertoire": 1}},
            {"id": "d", "text": "I have them but forget to use them when I actually need them", "scores": {"strategy_repertoire": 2}}
        ],
        "cross_scores": [], "anti_gaming": {"opacity": 0.6, "social_desirability_trap": False, "consistency_group": "sr_sensory_1", "reversal": False},
        "cultural_adaptability": {"universal": True, "adaptations_needed": [], "adaptation_notes": None},
        "content_rating": "G", "content_categories": [], "depth_tier": "moderate", "tier_role": "consistency_check",
        "tags": ["emotional_regulation", "strategy_repertoire", "consistency_check"]
    },
    {
        "uid": make_uid(), "assessment_id": "emotional_regulation", "dimension": "strategy_repertoire",
        "question_type": "partner_perspective",
        "text": "If someone watched you during a stressful week, how many distinct self-regulation behaviors would they observe?",
        "options": [
            {"id": "a", "text": "Many—exercise, meditation, calling a friend, journaling, cooking, nature walks", "scores": {"strategy_repertoire": 5}},
            {"id": "b", "text": "A couple—probably exercise and venting to someone", "scores": {"strategy_repertoire": 3}},
            {"id": "c", "text": "Mostly avoidant ones—drinking, binge-watching, sleeping more", "scores": {"strategy_repertoire": 1}},
            {"id": "d", "text": "They'd see me pushing through without visible coping strategies", "scores": {"strategy_repertoire": 1}}
        ],
        "cross_scores": [], "anti_gaming": {"opacity": 0.6, "social_desirability_trap": False, "consistency_group": None, "reversal": False},
        "cultural_adaptability": {"universal": True, "adaptations_needed": [], "adaptation_notes": None},
        "content_rating": "G", "content_categories": [], "depth_tier": "moderate", "tier_role": "triangulation",
        "tags": ["emotional_regulation", "strategy_repertoire", "triangulation"]
    },
    {
        "uid": make_uid(), "assessment_id": "emotional_regulation", "dimension": "strategy_repertoire",
        "question_type": "temporal",
        "text": "What's the most recent emotional regulation technique you learned and successfully applied?",
        "options": [
            {"id": "a", "text": "Within the past few months—I'm actively expanding my toolkit", "scores": {"strategy_repertoire": 5}},
            {"id": "b", "text": "Within the past year or two", "scores": {"strategy_repertoire": 3}},
            {"id": "c", "text": "I can't remember the last time I intentionally learned a new technique", "scores": {"strategy_repertoire": 1}},
            {"id": "d", "text": "I've learned techniques but not actually applied them successfully yet", "scores": {"strategy_repertoire": 2}}
        ],
        "cross_scores": [], "anti_gaming": {"opacity": 0.6, "social_desirability_trap": True, "consistency_group": "sr_recent_1", "reversal": False},
        "cultural_adaptability": {"universal": True, "adaptations_needed": [], "adaptation_notes": None},
        "content_rating": "G", "content_categories": [], "depth_tier": "moderate", "tier_role": "trap",
        "tags": ["emotional_regulation", "strategy_repertoire", "trap", "recency"]
    },
    {
        "uid": make_uid(), "assessment_id": "emotional_regulation", "dimension": "recovery_speed",
        "question_type": "scenario",
        "text": "You discover your partner lied to you about something small but consequential. After the initial shock and conversation, how long until trust feels approximately normal again?",
        "options": [
            {"id": "a", "text": "A day or two—it was small and they owned it", "scores": {"recovery_speed": 5}},
            {"id": "b", "text": "A week or so—trust rebuilds layer by layer", "scores": {"recovery_speed": 3}},
            {"id": "c", "text": "Months—once trust is broken, the repair is slow regardless of size", "scores": {"recovery_speed": 1}},
            {"id": "d", "text": "It never fully returns to the same level—lies leave permanent marks", "scores": {"recovery_speed": 1}}
        ],
        "cross_scores": [], "anti_gaming": {"opacity": 0.7, "social_desirability_trap": False, "consistency_group": "rs_trust_1", "reversal": False},
        "cultural_adaptability": {"universal": True, "adaptations_needed": [], "adaptation_notes": None},
        "content_rating": "G", "content_categories": [], "depth_tier": "deep", "tier_role": "triangulation",
        "tags": ["emotional_regulation", "recovery_speed", "triangulation"]
    },
    {
        "uid": make_uid(), "assessment_id": "emotional_regulation", "dimension": "window_of_tolerance",
        "question_type": "behavioral_recall",
        "text": "When you're running on fumes emotionally, how does it affect your decision-making quality?",
        "options": [
            {"id": "a", "text": "Dramatically—I make poor decisions when depleted and I know it", "scores": {"window_of_tolerance": 1}},
            {"id": "b", "text": "Noticeably—I stick to routine decisions and defer big ones", "scores": {"window_of_tolerance": 3}},
            {"id": "c", "text": "Somewhat—I'm more conservative but still capable", "scores": {"window_of_tolerance": 4}},
            {"id": "d", "text": "Minimally—my decision-making is fairly robust regardless of emotional state", "scores": {"window_of_tolerance": 5}}
        ],
        "cross_scores": [], "anti_gaming": {"opacity": 0.6, "social_desirability_trap": False, "consistency_group": "wot_decisions_1", "reversal": False},
        "cultural_adaptability": {"universal": True, "adaptations_needed": [], "adaptation_notes": None},
        "content_rating": "G", "content_categories": [], "depth_tier": "moderate", "tier_role": "consistency_check",
        "tags": ["emotional_regulation", "window_of_tolerance", "consistency_check"]
    }
]

questions.extend(extras)

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

with open("/Users/user/personal/sb/trueassess/priv/question_bank/emotional_regulation.json", "w") as f:
    json.dump(questions, f, indent=2)

print("Updated emotional_regulation.json")
