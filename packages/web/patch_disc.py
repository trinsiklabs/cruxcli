#!/usr/bin/env python3
"""Patch DISC to add 3 missing questions."""
import json

with open("/Users/user/personal/sb/trueassess/priv/question_bank/disc_style.json") as f:
    questions = json.load(f)

uid_counter = len(questions) + 1

def uid():
    global uid_counter
    u = f"DISC-{uid_counter:03d}"
    uid_counter += 1
    return u

D = "dominance"
I = "influence"
S = "steadiness"
C = "conscientiousness"

# Add 1 more influence question
questions.append({
    "uid": uid(),
    "assessment_id": "disc_style",
    "dimension": I,
    "question_type": "temporal",
    "text": "Your ability to read a room and adjust your energy accordingly has been:",
    "options": [
        {"id": "a", "text": "A lifelong strength — you're a natural social barometer", "scores": {I: 5}},
        {"id": "b", "text": "Developing — you're getting better with experience", "scores": {I: 3}},
        {"id": "c", "text": "Not something you think about — you are who you are", "scores": {I: 1, S: 2}},
        {"id": "d", "text": "Strong in formal settings, less so in casual ones", "scores": {I: 3, C: 2}}
    ],
    "tier_role": "core",
    "anti_gaming": {"opacity": 0.6, "social_desirability_trap": False, "consistency_group": "i_awareness_1", "reversal": False},
    "cultural_adaptability": {"universal": True, "adaptations_needed": [], "adaptation_notes": None},
    "content_rating": "G",
    "content_categories": [],
    "depth_tier": "moderate",
    "tags": ["disc_style", I]
})

# Add 1 more steadiness question
questions.append({
    "uid": uid(),
    "assessment_id": "disc_style",
    "dimension": S,
    "question_type": "behavioral_recall",
    "text": "When you find a process, tool, or system that works well, you:",
    "options": [
        {"id": "a", "text": "Stick with it for years — why change what works?", "scores": {S: 5}},
        {"id": "b", "text": "Use it until something clearly better comes along", "scores": {S: 3}},
        {"id": "c", "text": "Are always looking for the next upgrade or improvement", "scores": {S: 1, D: 3}},
        {"id": "d", "text": "Research alternatives regularly to make sure you have the best option", "scores": {S: 1, C: 4}}
    ],
    "tier_role": "core",
    "anti_gaming": {"opacity": 0.6, "social_desirability_trap": False, "consistency_group": "s_consistency_1", "reversal": False},
    "cultural_adaptability": {"universal": True, "adaptations_needed": [], "adaptation_notes": None},
    "content_rating": "G",
    "content_categories": [],
    "depth_tier": "moderate",
    "tags": ["disc_style", S]
})

# Add 1 more conscientiousness question
questions.append({
    "uid": uid(),
    "assessment_id": "disc_style",
    "dimension": C,
    "question_type": "scenario",
    "text": "You're asked to make a quick decision without having all the data you'd prefer. You:",
    "options": [
        {"id": "a", "text": "Make the call with available info — perfect is the enemy of good", "scores": {C: 1, D: 4}},
        {"id": "b", "text": "Ask for more time — you need to research before deciding", "scores": {C: 5}},
        {"id": "c", "text": "Make a provisional decision and refine as data comes in", "scores": {C: 3}},
        {"id": "d", "text": "Poll the group for their instincts", "scores": {C: 1, I: 3}}
    ],
    "tier_role": "core",
    "anti_gaming": {"opacity": 0.6, "social_desirability_trap": False, "consistency_group": "c_data_1", "reversal": False},
    "cultural_adaptability": {"universal": True, "adaptations_needed": [], "adaptation_notes": None},
    "content_rating": "G",
    "content_categories": [],
    "depth_tier": "moderate",
    "tags": ["disc_style", C]
})

assert len(questions) == 100, f"Expected 100, got {len(questions)}"

with open("/Users/user/personal/sb/trueassess/priv/question_bank/disc_style.json", "w") as f:
    json.dump(questions, f, indent=2)
print(f"Patched DISC to {len(questions)} questions")
