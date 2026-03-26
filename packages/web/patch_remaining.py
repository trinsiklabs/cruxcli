#!/usr/bin/env python3
"""Patch Dark Triad and HSP to correct counts, then generate Grit."""
import json

# ============================================================
# PATCH DARK TRIAD (99 -> 100)
# ============================================================
with open("/Users/user/personal/sb/trueassess/priv/question_bank/dark_triad.json") as f:
    dt = json.load(f)

dt.append({
    "uid": "DARK-100",
    "assessment_id": "dark_triad",
    "dimension": "sadism",
    "question_type": "behavioral_recall",
    "text": "When you correct someone's mistake, you:",
    "options": [
        {"id": "a", "text": "Enjoy the moment of their realization more than helping them learn", "scores": {"sadism": 5}},
        {"id": "b", "text": "Focus on helping them understand so they don't repeat it", "scores": {"sadism": 1}},
        {"id": "c", "text": "Feel a small satisfaction in being right that has an edge to it", "scores": {"sadism": 3}},
        {"id": "d", "text": "Handle it diplomatically — corrections shouldn't be painful", "scores": {"sadism": 1}}
    ],
    "tier_role": "core",
    "anti_gaming": {"opacity": 0.6, "social_desirability_trap": False, "consistency_group": "s_correction_1", "reversal": False},
    "cultural_adaptability": {"universal": True, "adaptations_needed": [], "adaptation_notes": None},
    "content_rating": "PG",
    "content_categories": [],
    "depth_tier": "moderate",
    "tags": ["dark_triad", "sadism"]
})

assert len(dt) == 100, f"Dark Triad: expected 100, got {len(dt)}"
with open("/Users/user/personal/sb/trueassess/priv/question_bank/dark_triad.json", "w") as f:
    json.dump(dt, f, indent=2)
print(f"Dark Triad: {len(dt)} questions")

# ============================================================
# GENERATE HSP (need to fix count — run gen then patch)
# ============================================================
# Run the gen script without assert first
code = open('/tmp/gen_hsp.py').read().replace(
    'assert len(questions) == 80',
    '# assert'
)
exec(compile(code, '/tmp/gen_hsp.py', 'exec'))

with open("/Users/user/personal/sb/trueassess/priv/question_bank/highly_sensitive.json") as f:
    hsp = json.load(f)

from collections import Counter
dims = Counter(q['dimension'] for q in hsp)
print(f"HSP current: {dict(dims)}, total: {len(hsp)}")

# Need 80-74 = 6 more
uid_c = 75
def uid():
    global uid_c
    u = f"HSP-{uid_c:03d}"
    uid_c += 1
    return u

def make_hsp(dim, qtype, text, options, cg, tier="core"):
    return {
        "uid": uid(),
        "assessment_id": "highly_sensitive",
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
        "tags": ["highly_sensitive", dim]
    }

SS = "sensory_sensitivity"
ER = "emotional_reactivity"
DP = "depth_of_processing"
OT = "overstimulation_threshold"

# Add 2 more to depth_of_processing
hsp.append(make_hsp(DP, "scenario",
    "When making a major life decision, the time you spend considering options compared to others is:",
    [
        {"id": "a", "text": "Much longer — you consider angles no one else thinks of", "scores": {DP: 5}},
        {"id": "b", "text": "About the same — you weigh pros and cons normally", "scores": {DP: 1}},
        {"id": "c", "text": "Somewhat longer — you're thorough but not excessive", "scores": {DP: 3}},
        {"id": "d", "text": "So long that you sometimes miss the window for action", "scores": {DP: 5}}
    ], "dp_decisions_1"))

hsp.append(make_hsp(DP, "behavioral_recall",
    "When you meet a new person, the amount of information you process about them is:",
    [
        {"id": "a", "text": "Enormous — their body language, micro-expressions, word choices, and energy all register simultaneously", "scores": {DP: 5}},
        {"id": "b", "text": "Normal — you form a general impression", "scores": {DP: 1}},
        {"id": "c", "text": "Above average — you pick up on subtleties", "scores": {DP: 3}},
        {"id": "d", "text": "So much that you need time alone afterward to sort through it all", "scores": {DP: 5}}
    ], "dp_social_processing_1"))

# Add 2 more to overstimulation_threshold
hsp.append(make_hsp(OT, "scenario",
    "When multiple people are talking to you at once (children, colleagues, family), you:",
    [
        {"id": "a", "text": "Quickly become overwhelmed and may snap or shut down", "scores": {OT: 5}},
        {"id": "b", "text": "Handle it fine — multitasking is normal", "scores": {OT: 1}},
        {"id": "c", "text": "Manage but feel your stress level rising", "scores": {OT: 3}},
        {"id": "d", "text": "Need to stop everything and address one person at a time", "scores": {OT: 5}}
    ], "ot_multitask_2"))

hsp.append(make_hsp(OT, "behavioral_recall",
    "How much does travel (airports, hotels, new environments) drain you compared to others?",
    [
        {"id": "a", "text": "Much more — travel exhausts you in ways others don't seem to experience", "scores": {OT: 5}},
        {"id": "b", "text": "About the same — travel is tiring for everyone", "scores": {OT: 1}},
        {"id": "c", "text": "Somewhat more — you need extra recovery time after trips", "scores": {OT: 3}},
        {"id": "d", "text": "Significantly more — you plan travel carefully to minimize overstimulation", "scores": {OT: 5}}
    ], "ot_travel_1"))

# Add 1 more to sensory_sensitivity
hsp.append(make_hsp(SS, "scenario",
    "You're in a car with the radio, air conditioning, and a passenger talking simultaneously. You:",
    [
        {"id": "a", "text": "Feel your nervous system protesting — too many inputs", "scores": {SS: 5}},
        {"id": "b", "text": "Don't even notice the layered stimulation", "scores": {SS: 1}},
        {"id": "c", "text": "Turn down the radio to focus on the conversation", "scores": {SS: 3}},
        {"id": "d", "text": "Need to eliminate at least one source of input to feel comfortable", "scores": {SS: 5}}
    ], "ss_layered_1"))

# Add 1 more to emotional_reactivity
hsp.append(make_hsp(ER, "scenario",
    "You witness a random act of kindness between strangers. You:",
    [
        {"id": "a", "text": "Are moved to tears or feel a physical wave of emotion", "scores": {ER: 5}},
        {"id": "b", "text": "Smile and feel good briefly", "scores": {ER: 1}},
        {"id": "c", "text": "Feel warmth but it doesn't overwhelm you", "scores": {ER: 2}},
        {"id": "d", "text": "Are deeply affected — it restores your faith in humanity and you might think about it for days", "scores": {ER: 5}}
    ], "er_positive_2"))

assert len(hsp) == 80, f"HSP: expected 80, got {len(hsp)}"
with open("/Users/user/personal/sb/trueassess/priv/question_bank/highly_sensitive.json", "w") as f:
    json.dump(hsp, f, indent=2)
print(f"HSP: {len(hsp)} questions")
