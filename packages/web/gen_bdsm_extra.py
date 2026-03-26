import json

with open("/Users/user/personal/sb/trueassess/priv/question_bank/bdsm_role.json") as f:
    questions = json.load(f)

uid_counter = 191

def q(dimension, qtype, text, options, tier_role="core", trap=False, cg=None, opacity=0.6, cross=None, tags=None):
    global uid_counter
    uid = f"br_{uid_counter:03d}"
    uid_counter += 1
    entry = {
        "uid": uid,
        "assessment_id": "bdsm_role",
        "dimension": dimension,
        "question_type": qtype,
        "text": text,
        "options": options,
        "cross_scores": cross or [],
        "anti_gaming": {
            "opacity": opacity,
            "social_desirability_trap": trap,
            "consistency_group": cg or f"{dimension}_core",
            "reversal": False
        },
        "cultural_adaptability": {"universal": True, "adaptations_needed": [], "adaptation_notes": None},
        "content_rating": "X",
        "content_categories": ["bdsm", "power_exchange"],
        "depth_tier": "deep",
        "tier_role": tier_role,
        "tags": tags or ["nsfw", "bdsm", dimension]
    }
    questions.append(entry)

def opts(texts_scores):
    return [{"id": chr(97+i), "text": t, "scores": s} for i, (t, s) in enumerate(texts_scores)]

q("dominance_spectrum", "scenario", "You catch your submissive partner masturbating without permission. The visceral feeling — separate from any protocol considerations — is:", opts([
    ("Possessive arousal — that pleasure belongs to me and they took it without asking", {"dominance_spectrum": 5, "sadism": 3}),
    ("A mix of arousal and the urge to address it — this is a teachable moment", {"dominance_spectrum": 4}),
    ("More amused than bothered — it's natural", {"dominance_spectrum": 2}),
    ("I wouldn't restrict a partner's self-pleasure", {"dominance_spectrum": 1})
]))

q("submission_spectrum", "forced_choice", "When you imagine your ideal relationship, the power balance looks like:", opts([
    ("Clearly asymmetric — I want someone who leads and I follow, in most things", {"submission_spectrum": 5}),
    ("Tilted — they lead in key areas, we're equal in others", {"submission_spectrum": 4}),
    ("Equal with occasional role play", {"submission_spectrum": 3}),
    ("Equal in all things", {"submission_spectrum": 1})
]), tier_role="triangulation")

q("sadism", "somatic", "When you dig your nails into a partner's flesh during sex and feel their body tense under you, the sensation in YOUR body is:", opts([
    ("A rush of primal power — my hands want to grip harder", {"sadism": 5}),
    ("Satisfying — feeling their response to my force", {"sadism": 4}),
    ("Neutral — I don't notice my own response much", {"sadism": 2}),
    ("Guilt — I don't want to leave marks", {"sadism": 1})
]))

q("masochism", "forced_choice", "Pain during sex serves as:", opts([
    ("A sacrament — it strips away everything false and leaves only what's real", {"masochism": 5}),
    ("An amplifier — it makes everything more intense", {"masochism": 4}),
    ("An occasional spice", {"masochism": 3}),
    ("An interruption", {"masochism": 1})
]))

q("bondage", "scenario", "Your partner puts a leash on your collar and leads you through your own home. Being led, literally, by another person:", opts([
    ("Feels natural and deeply intimate — my movement is theirs to direct", {"bondage": 5, "submission_spectrum": 4}),
    ("Is arousing — the symbolism and physical reality merge", {"bondage": 4}),
    ("Is playful — I'd laugh but enjoy it", {"bondage": 3}),
    ("Is degrading in a way I don't enjoy", {"bondage": 1})
]))

q("sensation_play", "forced_choice", "If you could enhance one sense during sex and dull another, you would:", opts([
    ("Enhance touch dramatically and dull vision — pure sensation without distraction", {"sensation_play": 5}),
    ("Enhance touch somewhat — more sensitive skin", {"sensation_play": 4}),
    ("Enhance vision — I'm more visual than tactile", {"sensation_play": 2}),
    ("Leave everything as is", {"sensation_play": 1})
]))

q("power_exchange_depth", "behavioral_recall", "How much of your identity is connected to your role in power exchange dynamics?", opts([
    ("It IS my identity — Dominant/submissive/switch is as core as my gender or orientation", {"power_exchange_depth": 5}),
    ("A significant part — it shapes how I relate to partners", {"power_exchange_depth": 4}),
    ("A piece of my sexuality — important but not central to who I am", {"power_exchange_depth": 3}),
    ("A peripheral interest — it's something I do, not something I am", {"power_exchange_depth": 1})
]), cg="ped_identity")

q("protocol_orientation", "scenario", "Your dynamic includes a 'ritual of reconnection' — a specific series of actions you perform together every evening (kneeling, a specific greeting, a check-in). Missing it because of life circumstances makes you feel:", opts([
    ("Genuinely bereft — the ritual IS our connection point and missing it creates distance", {"protocol_orientation": 5}),
    ("Disappointed but understanding — we'll make it up", {"protocol_orientation": 4}),
    ("Fine — it's just a ritual", {"protocol_orientation": 2}),
    ("Relieved — one less thing to perform", {"protocol_orientation": 1})
]))

q("service_orientation", "forced_choice", "The distinction between 'service submissive' and 'people pleaser' is:", opts([
    ("Clear to me — service submission is chosen, negotiated, and empowering; people pleasing is compulsive and draining", {"service_orientation": 5}),
    ("Something I think about — I want to make sure my service comes from strength", {"service_orientation": 4}),
    ("Blurry — I'm not sure where one ends and the other begins", {"service_orientation": 2}),
    ("Nonexistent — both are just doing what others want", {"service_orientation": 1})
]), tier_role="trap", trap=True, tags=["nsfw", "bdsm", "service_orientation", "self_awareness"])

q("switch_capacity", "forced_choice", "When people ask 'Are you dominant or submissive?' your honest answer is:", opts([
    ("Yes — both, fully, depending on partner and context", {"switch_capacity": 5}),
    ("Primarily one, but I have range", {"switch_capacity": 4}),
    ("One, clearly and consistently", {"switch_capacity": 2}),
    ("I don't think in those terms", {"switch_capacity": 1})
]))

print(f"Total questions: {len(questions)}")
with open("/Users/user/personal/sb/trueassess/priv/question_bank/bdsm_role.json", "w") as f:
    json.dump(questions, f, indent=2)
print("Written bdsm_role.json")
