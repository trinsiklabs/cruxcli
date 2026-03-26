#!/usr/bin/env python3
"""Patch Keirsey to add 5 missing questions."""
import json, sys

# First run the generator without the assert to get partial output
sys.path.insert(0, '/tmp')

# Read existing (if any) or generate
exec_globals = {}
code = open('/tmp/gen_keirsey.py').read().replace(
    'assert len(questions) == 100',
    '# assert len(questions) == 100'
)
exec(compile(code, '/tmp/gen_keirsey.py', 'exec'), exec_globals)

with open("/Users/user/personal/sb/trueassess/priv/question_bank/keirsey_temperament.json") as f:
    questions = json.load(f)

uid_counter = len(questions) + 1

def uid():
    global uid_counter
    u = f"KEIR-{uid_counter:03d}"
    uid_counter += 1
    return u

G = "guardian"
A = "artisan"
I = "idealist"
R = "rational"

# Count per dimension
from collections import Counter
dims = Counter(q['dimension'] for q in questions)
print("Current counts:", dict(dims))

# Need to get to 100. Currently 95. Add 5 more distributed across dimensions.
# Add 2 more artisan (looks like it might be short), and others as needed

def make_q(dim, qtype, text, options, cg, tier="core"):
    return {
        "uid": uid(),
        "assessment_id": "keirsey_temperament",
        "dimension": dim,
        "question_type": qtype,
        "text": text,
        "options": options,
        "tier_role": tier,
        "anti_gaming": {"opacity": 0.6, "social_desirability_trap": False, "consistency_group": cg, "reversal": False},
        "cultural_adaptability": {"universal": True, "adaptations_needed": [], "adaptation_notes": None},
        "content_rating": "G",
        "content_categories": [],
        "depth_tier": "moderate",
        "tags": ["keirsey_temperament", dim]
    }

# Guardian extra
questions.append(make_q(G, "scenario",
    "You're choosing a vacation destination. Your primary criterion is:",
    [
        {"id": "a", "text": "Safety, reliability, and well-reviewed accommodations", "scores": {G: 5}},
        {"id": "b", "text": "Adventure potential and spontaneity — somewhere off the beaten path", "scores": {A: 4}},
        {"id": "c", "text": "Cultural richness and personal growth opportunity", "scores": {I: 4}},
        {"id": "d", "text": "Intellectual stimulation — historical sites, museums, or unique ecosystems", "scores": {R: 4}}
    ], "g_vacation_1"))

# Artisan extra
questions.append(make_q(A, "behavioral_recall",
    "When you tell stories, you tend to:",
    [
        {"id": "a", "text": "Embellish for dramatic effect — accuracy matters less than the experience", "scores": {A: 5}},
        {"id": "b", "text": "Stick to the facts and tell it accurately", "scores": {G: 4}},
        {"id": "c", "text": "Focus on the emotional and relational meaning", "scores": {I: 3}},
        {"id": "d", "text": "Include precise details and logical sequence", "scores": {R: 3}}
    ], "a_storytelling_1"))

# Idealist extra
questions.append(make_q(I, "scenario",
    "You're writing a letter to someone you care about. You focus on:",
    [
        {"id": "a", "text": "How they've grown as a person and how proud you are of their journey", "scores": {I: 5}},
        {"id": "b", "text": "Practical updates and plans for the future", "scores": {G: 4}},
        {"id": "c", "text": "Funny stories and shared adventures", "scores": {A: 3}},
        {"id": "d", "text": "Thoughtful analysis of your shared experiences", "scores": {R: 3}}
    ], "i_expression_1"))

# Rational extra
questions.append(make_q(R, "behavioral_recall",
    "When you encounter a problem in daily life (appliance breaks, software crashes), you:",
    [
        {"id": "a", "text": "Diagnose the root cause systematically before attempting any fix", "scores": {R: 5}},
        {"id": "b", "text": "Call the appropriate service professional", "scores": {G: 4}},
        {"id": "c", "text": "Try various things hands-on until something works", "scores": {A: 4}},
        {"id": "d", "text": "Ask someone you trust for help", "scores": {I: 2}}
    ], "r_troubleshoot_1"))

# One more to reach 100
questions.append(make_q(A, "somatic",
    "When you're engaged in a physical activity you're skilled at, you feel:",
    [
        {"id": "a", "text": "Total flow — mind and body unified, time disappears", "scores": {A: 5}},
        {"id": "b", "text": "Satisfaction in doing it correctly and safely", "scores": {G: 3}},
        {"id": "c", "text": "Connected to a deeper purpose through the activity", "scores": {I: 3}},
        {"id": "d", "text": "Intellectually engaged in optimizing your performance", "scores": {R: 3}}
    ], "a_flow_1"))

assert len(questions) == 100, f"Expected 100, got {len(questions)}"

with open("/Users/user/personal/sb/trueassess/priv/question_bank/keirsey_temperament.json", "w") as f:
    json.dump(questions, f, indent=2)
print(f"Patched Keirsey to {len(questions)} questions")
