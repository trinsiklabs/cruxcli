import json
with open("/Users/user/personal/sb/trueassess/priv/question_bank/intimacy_style.json") as f:
    questions = json.load(f)
uid_counter = len(questions) + 1
def q(dim, qtype, text, options, tier_role="core", trap=False, cg=None, opacity=0.6, cross=None, tags=None):
    global uid_counter
    uid = f"is_{uid_counter:03d}"
    uid_counter += 1
    questions.append({"uid": uid, "assessment_id": "intimacy_style", "dimension": dim, "question_type": qtype, "text": text, "options": options, "cross_scores": cross or [], "anti_gaming": {"opacity": opacity, "social_desirability_trap": trap, "consistency_group": cg or f"{dim}_core", "reversal": False}, "cultural_adaptability": {"universal": True, "adaptations_needed": [], "adaptation_notes": None}, "content_rating": "R", "content_categories": ["sexuality", "intimacy"], "depth_tier": "deep", "tier_role": tier_role, "tags": tags or ["nsfw", "intimacy", dim]})
def opts(ts):
    return [{"id": chr(97+i), "text": t, "scores": s} for i, (t, s) in enumerate(ts)]

q("emotional_vs_physical", "forced_choice", "The best sex of your life will be with:", opts([
    ("Someone who knows every corner of my soul — the body follows the heart", {"emotional_vs_physical": 5}),
    ("Someone I love deeply AND am physically compatible with", {"emotional_vs_physical": 4}),
    ("Someone with extraordinary physical chemistry — connection is overrated in sex", {"emotional_vs_physical": 2}),
    ("Someone skilled — technique matters most", {"emotional_vs_physical": 1})
]), tier_role="consistency_check", cg="evp_core")

q("vulnerability_in_sex", "scenario", "Using words during sex that feel embarrassingly earnest — 'I need you,' 'You're everything,' 'Please don't stop holding me':", opts([
    ("These are the most honest things I say — sex strips away my public persona and these words are what's underneath", {"vulnerability_in_sex": 5}),
    ("I can say them with the right person", {"vulnerability_in_sex": 4}),
    ("Way too earnest — I'd cringe hearing myself", {"vulnerability_in_sex": 2}),
    ("I'd never say these things", {"vulnerability_in_sex": 1})
]))

q("initiation_comfort", "scenario", "Waking your partner up with sexual touch:", opts([
    ("Is something I do when I want them — my desire is confident enough to wake them for it", {"initiation_comfort": 5}),
    ("I've done it and it went well", {"initiation_comfort": 4}),
    ("Feels presumptuous — what if they were sleeping well?", {"initiation_comfort": 2}),
    ("I'd never — that's intrusive", {"initiation_comfort": 1})
]))

q("communication_during", "scenario", "A partner asks 'What's your favorite thing I do in bed?' in a non-sexual moment. You:", opts([
    ("Answer immediately and specifically: 'When you do X while Y — the combination of Z makes me feel...' No hesitation", {"communication_during": 5}),
    ("Give a thoughtful answer after a moment", {"communication_during": 4}),
    ("Say something general — 'everything' or 'I love your hands'", {"communication_during": 3}),
    ("Struggle to answer — I can't articulate it", {"communication_during": 1})
]))

q("responsive_desire", "scenario", "Date night as desire infrastructure — dressing up, going out, flirting deliberately, building toward sex:", opts([
    ("Is how responsive desire works — I create the conditions and my desire responds. Date night IS foreplay", {"responsive_desire": 5}),
    ("Helps — the intention and buildup create desire", {"responsive_desire": 4}),
    ("Is nice but doesn't reliably activate desire", {"responsive_desire": 3}),
    ("Is unnecessary — I'm either in the mood or not", {"responsive_desire": 1})
]))

print(f"Total questions: {len(questions)}")
with open("/Users/user/personal/sb/trueassess/priv/question_bank/intimacy_style.json", "w") as f:
    json.dump(questions, f, indent=2)
