import json

with open("/Users/user/personal/sb/trueassess/priv/question_bank/forgiveness_profile.json") as f:
    questions = json.load(f)

uid_counter = 141
def make_uid():
    global uid_counter
    uid_counter += 1
    return f"fp_{uid_counter:03d}"

# Need: 1 capacity, 1 load, 1 self_other_asymmetry, 3 stage, 2 active_hooks, 1 pattern = 9

extras = [
    {
        "uid": make_uid(), "assessment_id": "forgiveness_profile", "dimension": "capacity",
        "question_type": "scenario",
        "text": "Your best friend betrays a confidence and shares something deeply personal with others. They come to you devastated by their own behavior, saying they don't know why they did it. A year later, can you trust them with personal information again?",
        "options": [
            {"id": "a", "text": "Yes—people are complex and one terrible moment doesn't define them", "scores": {"capacity": 5}},
            {"id": "b", "text": "Partially—I'd share some things but keep the deepest things to myself", "scores": {"capacity": 3}},
            {"id": "c", "text": "No—they showed me they can't be trusted with vulnerability", "scores": {"capacity": 1}},
            {"id": "d", "text": "I'm not sure—I'd want to but I'd be hypervigilant about what I shared", "scores": {"capacity": 2}}
        ],
        "cross_scores": [], "anti_gaming": {"opacity": 0.7, "social_desirability_trap": False, "consistency_group": "cap_trust_rebuild_1", "reversal": False},
        "cultural_adaptability": {"universal": True, "adaptations_needed": [], "adaptation_notes": None},
        "content_rating": "G", "content_categories": [], "depth_tier": "deep", "tier_role": "triangulation",
        "tags": ["forgiveness_profile", "capacity", "triangulation"]
    },
    {
        "uid": make_uid(), "assessment_id": "forgiveness_profile", "dimension": "load",
        "question_type": "scenario",
        "text": "You're asked to write a gratitude list. As you write, does a 'grievance list' automatically start forming in the background?",
        "options": [
            {"id": "a", "text": "No—gratitude and grievance are separate channels for me", "scores": {"load": 5}},
            {"id": "b", "text": "Slightly—some items on the gratitude list trigger awareness of related wounds", "scores": {"load": 3}},
            {"id": "c", "text": "Yes—for every grateful thought, an ungrateful one appears", "scores": {"load": 1}},
            {"id": "d", "text": "The grievance list would be longer than the gratitude list", "scores": {"load": 1}}
        ],
        "cross_scores": [], "anti_gaming": {"opacity": 0.7, "social_desirability_trap": True, "consistency_group": "load_gratitude_1", "reversal": False},
        "cultural_adaptability": {"universal": True, "adaptations_needed": [], "adaptation_notes": None},
        "content_rating": "G", "content_categories": [], "depth_tier": "moderate", "tier_role": "trap",
        "tags": ["forgiveness_profile", "load", "trap", "awareness"]
    },
    {
        "uid": make_uid(), "assessment_id": "forgiveness_profile", "dimension": "self_other_asymmetry",
        "question_type": "scenario",
        "text": "You discover you inadvertently hurt a friend the same way someone once hurt you. Now you understand how it can happen without malice. Does this change your view of the original offense against you?",
        "options": [
            {"id": "a", "text": "Yes—experiencing the other side gives me genuine empathy and softens my resentment", "scores": {"self_other_asymmetry": 3}},
            {"id": "b", "text": "No—I hold myself to the same harsh standard I hold them to. Now I'm angry at both of us.", "scores": {"self_other_asymmetry": 2}},
            {"id": "c", "text": "I forgive myself more easily than I forgave them—I understand my own context better", "scores": {"self_other_asymmetry": 5}},
            {"id": "d", "text": "I forgive them more easily but now I can't forgive myself—I've become the thing I resented", "scores": {"self_other_asymmetry": 1}}
        ],
        "cross_scores": [], "anti_gaming": {"opacity": 0.6, "social_desirability_trap": False, "consistency_group": "soa_mirror_1", "reversal": False},
        "cultural_adaptability": {"universal": True, "adaptations_needed": [], "adaptation_notes": None},
        "content_rating": "G", "content_categories": [], "depth_tier": "deep", "tier_role": "triangulation",
        "tags": ["forgiveness_profile", "self_other_asymmetry", "triangulation"]
    },
    {
        "uid": make_uid(), "assessment_id": "forgiveness_profile", "dimension": "stage",
        "question_type": "behavioral_recall",
        "text": "When you think about your most significant unforgiveness, do you still want the person to suffer? Be honest.",
        "options": [
            {"id": "a", "text": "Yes—I want them to feel what I felt", "scores": {"stage": 2}},
            {"id": "b", "text": "Not suffer exactly, but I want them to understand the pain they caused—really understand it", "scores": {"stage": 3}},
            {"id": "c", "text": "No—I don't wish suffering on anyone, even them", "scores": {"stage": 5}},
            {"id": "d", "text": "I don't care either way—they're not part of my emotional world anymore", "scores": {"stage": 1}}
        ],
        "cross_scores": [], "anti_gaming": {"opacity": 0.4, "social_desirability_trap": True, "consistency_group": "stage_suffer_1", "reversal": False},
        "cultural_adaptability": {"universal": True, "adaptations_needed": [], "adaptation_notes": None},
        "content_rating": "G", "content_categories": [], "depth_tier": "deep", "tier_role": "trap",
        "tags": ["forgiveness_profile", "stage", "trap", "revenge"]
    },
    {
        "uid": make_uid(), "assessment_id": "forgiveness_profile", "dimension": "stage",
        "question_type": "partner_perspective",
        "text": "If your therapist used a metaphor for where you are in your forgiveness journey, it would be:",
        "options": [
            {"id": "a", "text": "'Still building the dam—holding back a flood of feeling' (denial/anger)", "scores": {"stage": 1}},
            {"id": "b", "text": "'The dam is leaking—water is coming through in controlled streams' (bargaining/grief)", "scores": {"stage": 3}},
            {"id": "c", "text": "'The dam has opened—you're in the flood but moving through it' (active grief)", "scores": {"stage": 4}},
            {"id": "d", "text": "'The water has settled into a lake—calm, deep, and navigable' (acceptance)", "scores": {"stage": 5}}
        ],
        "cross_scores": [], "anti_gaming": {"opacity": 0.6, "social_desirability_trap": False, "consistency_group": "stage_dam_1", "reversal": False},
        "cultural_adaptability": {"universal": True, "adaptations_needed": [], "adaptation_notes": None},
        "content_rating": "G", "content_categories": [], "depth_tier": "deep", "tier_role": "triangulation",
        "tags": ["forgiveness_profile", "stage", "triangulation"]
    },
    {
        "uid": make_uid(), "assessment_id": "forgiveness_profile", "dimension": "stage",
        "question_type": "forced_choice",
        "text": "Right now, regarding the person you're working to forgive, which feels most true?",
        "options": [
            {"id": "a", "text": "I'm still angry and the anger feels justified", "scores": {"stage": 2}},
            {"id": "b", "text": "I'm sad about the whole thing—the anger has given way to loss", "scores": {"stage": 4}},
            {"id": "c", "text": "I'm accepting it as part of my story without it dominating", "scores": {"stage": 5}},
            {"id": "d", "text": "I haven't really started processing—I've been avoiding it", "scores": {"stage": 1}}
        ],
        "cross_scores": [], "anti_gaming": {"opacity": 0.5, "social_desirability_trap": False, "consistency_group": "stage_current_1", "reversal": False},
        "cultural_adaptability": {"universal": True, "adaptations_needed": [], "adaptation_notes": None},
        "content_rating": "G", "content_categories": [], "depth_tier": "moderate", "tier_role": "consistency_check",
        "tags": ["forgiveness_profile", "stage", "consistency_check"]
    },
    {
        "uid": make_uid(), "assessment_id": "forgiveness_profile", "dimension": "active_hooks",
        "question_type": "partner_perspective",
        "text": "If someone monitored your emotional reactivity for a week, how many distinct 'spikes' would trace back to unresolved forgiveness issues?",
        "options": [
            {"id": "a", "text": "None—my reactivity isn't driven by unresolved past hurts", "scores": {"active_hooks": 5}},
            {"id": "b", "text": "A couple—specific situations that connect to old wounds", "scores": {"active_hooks": 3}},
            {"id": "c", "text": "Several—more of my emotional life than I'd like is driven by unresolved past", "scores": {"active_hooks": 2}},
            {"id": "d", "text": "Most of them—my default emotional state is colored by what I haven't forgiven", "scores": {"active_hooks": 1}}
        ],
        "cross_scores": [], "anti_gaming": {"opacity": 0.6, "social_desirability_trap": True, "consistency_group": "ah_spikes_1", "reversal": False},
        "cultural_adaptability": {"universal": True, "adaptations_needed": [], "adaptation_notes": None},
        "content_rating": "G", "content_categories": [], "depth_tier": "moderate", "tier_role": "trap",
        "tags": ["forgiveness_profile", "active_hooks", "trap", "frequency"]
    },
    {
        "uid": make_uid(), "assessment_id": "forgiveness_profile", "dimension": "active_hooks",
        "question_type": "temporal",
        "text": "Think about the hook that has the most impact on your daily life right now. Is it getting weaker over time, or has it plateaued?",
        "options": [
            {"id": "a", "text": "Getting weaker—I'm making progress on deactivating it", "scores": {"active_hooks": 4}},
            {"id": "b", "text": "Plateaued—it's been at the same intensity for a while", "scores": {"active_hooks": 2}},
            {"id": "c", "text": "Getting stronger—recent events have re-energized it", "scores": {"active_hooks": 1}},
            {"id": "d", "text": "I don't have a hook that meaningfully impacts my daily life", "scores": {"active_hooks": 5}}
        ],
        "cross_scores": [], "anti_gaming": {"opacity": 0.6, "social_desirability_trap": False, "consistency_group": "ah_plateau_1", "reversal": False},
        "cultural_adaptability": {"universal": True, "adaptations_needed": [], "adaptation_notes": None},
        "content_rating": "G", "content_categories": [], "depth_tier": "moderate", "tier_role": "consistency_check",
        "tags": ["forgiveness_profile", "active_hooks", "consistency_check"]
    },
    {
        "uid": make_uid(), "assessment_id": "forgiveness_profile", "dimension": "pattern",
        "question_type": "partner_perspective",
        "text": "Your closest confidant would say your forgiveness endgame is typically:",
        "options": [
            {"id": "a", "text": "'You declare it done early and then do the real work silently over months'", "scores": {"pattern": 1}},
            {"id": "b", "text": "'You take forever but when you say it's done, it's genuinely done'", "scores": {"pattern": 4}},
            {"id": "c", "text": "'You set terms and keep monitoring—forgiveness with surveillance'", "scores": {"pattern": 3}},
            {"id": "d", "text": "'You fade away from the person rather than doing the forgiveness work'", "scores": {"pattern": 2}}
        ],
        "cross_scores": [], "anti_gaming": {"opacity": 0.5, "social_desirability_trap": False, "consistency_group": "pat_endgame_1", "reversal": False},
        "cultural_adaptability": {"universal": True, "adaptations_needed": [], "adaptation_notes": None},
        "content_rating": "G", "content_categories": [], "depth_tier": "moderate", "tier_role": "consistency_check",
        "tags": ["forgiveness_profile", "pattern", "consistency_check"]
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

uids = [q["uid"] for q in questions]
dupes = [u for u in uids if uids.count(u) > 1]

print(f"Total: {len(questions)}")
print(f"Dimensions: {dim_counts}")
print(f"Types: {type_counts}")
print(f"Tiers: {tier_counts}")
print(f"SD traps: {trap_count}")
print(f"Duplicate UIDs: {set(dupes) if dupes else 'none'}")

with open("/Users/user/personal/sb/trueassess/priv/question_bank/forgiveness_profile.json", "w") as f:
    json.dump(questions, f, indent=2)

print("Updated forgiveness_profile.json")
