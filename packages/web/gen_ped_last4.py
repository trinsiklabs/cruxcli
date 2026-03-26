import json
with open("/Users/user/personal/sb/trueassess/priv/question_bank/power_exchange_depth.json") as f:
    questions = json.load(f)
uid_counter = len(questions) + 1
def q(dim, qtype, text, options, **kw):
    global uid_counter
    uid = f"pd_{uid_counter:03d}"
    uid_counter += 1
    questions.append({"uid": uid, "assessment_id": "power_exchange_depth", "dimension": dim, "question_type": qtype, "text": text, "options": options, "cross_scores": kw.get("cross", []), "anti_gaming": {"opacity": 0.6, "social_desirability_trap": kw.get("trap", False), "consistency_group": kw.get("cg", f"{dim}_core"), "reversal": False}, "cultural_adaptability": {"universal": True, "adaptations_needed": [], "adaptation_notes": None}, "content_rating": "X", "content_categories": ["bdsm", "power_exchange"], "depth_tier": "deep", "tier_role": kw.get("tier_role", "core"), "tags": ["nsfw", "power_exchange", dim]})
def opts(ts):
    return [{"id": chr(97+i), "text": t, "scores": s} for i, (t, s) in enumerate(ts)]

q("lifestyle_vs_bedroom", "forced_choice", "D/s in front of children (for parents in lifestyle dynamics):", opts([
    ("Age-appropriate expressions exist: modeling respect, courtesy, and clear leadership without sexual content. Children see healthy relationship structure, not kink", {"lifestyle_vs_bedroom": 5}),
    ("Needs to be invisible to children — no protocols around kids", {"lifestyle_vs_bedroom": 4}),
    ("Lifestyle D/s and parenting are incompatible", {"lifestyle_vs_bedroom": 2}),
    ("Not relevant to my situation / haven't thought about it", {"lifestyle_vs_bedroom": 1})
]))

q("negotiation_skill", "forced_choice", "The most underrated negotiation topic:", opts([
    ("Aftercare and drop management — everyone negotiates the scene, few negotiate the aftermath with equal care", {"negotiation_skill": 5}),
    ("Emotional limits — not just physical ones", {"negotiation_skill": 4}),
    ("Communication during scenes", {"negotiation_skill": 3}),
    ("I wouldn't know what's underrated", {"negotiation_skill": 1})
]))

q("aftercare_practice", "scenario", "Aftercare kits for both top and bottom — prepared bags with comfort items specific to each person:", opts([
    ("Of course — mine contains specific items I've identified over years of knowing my own needs. I also prepare for my partner's", {"aftercare_practice": 5}),
    ("I have basic supplies ready", {"aftercare_practice": 4}),
    ("Not a formal kit but I keep things nearby", {"aftercare_practice": 3}),
    ("No prepared kit", {"aftercare_practice": 1})
]))

q("dynamic_health", "scenario", "D/s compatibility assessment — before committing to a dynamic, thoroughly evaluating alignment on all dimensions:", opts([
    ("Essential — compatibility on depth, style, communication, aftercare, and growth trajectory matters as much as chemistry. I assess deliberately before committing", {"dynamic_health": 5}),
    ("Important — I evaluate key compatibility factors", {"dynamic_health": 4}),
    ("Chemistry first, compatibility second", {"dynamic_health": 3}),
    ("Just see if it works — analysis paralysis kills dynamics", {"dynamic_health": 1})
]))

print(f"Total questions: {len(questions)}")
with open("/Users/user/personal/sb/trueassess/priv/question_bank/power_exchange_depth.json", "w") as f:
    json.dump(questions, f, indent=2)
