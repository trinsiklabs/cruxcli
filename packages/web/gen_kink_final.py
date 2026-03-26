import json

with open("/Users/user/personal/sb/trueassess/priv/question_bank/kink_exploration.json") as f:
    questions = json.load(f)

uid_counter = len(questions) + 1

def q(dimension, qtype, text, options, tier_role="core", trap=False, cg=None, opacity=0.6, cross=None, tags=None):
    global uid_counter
    uid = f"ke_{uid_counter:03d}"
    uid_counter += 1
    entry = {
        "uid": uid, "assessment_id": "kink_exploration", "dimension": dimension,
        "question_type": qtype, "text": text, "options": options,
        "cross_scores": cross or [],
        "anti_gaming": {"opacity": opacity, "social_desirability_trap": trap, "consistency_group": cg or f"{dimension}_core", "reversal": False},
        "cultural_adaptability": {"universal": True, "adaptations_needed": [], "adaptation_notes": None},
        "content_rating": "X", "content_categories": ["kink", "sexuality"],
        "depth_tier": "deep", "tier_role": tier_role,
        "tags": tags or ["nsfw", "kink", dimension]
    }
    questions.append(entry)

def opts(ts):
    return [{"id": chr(97+i), "text": t, "scores": s} for i, (t, s) in enumerate(ts)]

# Fill to 200 with diverse dimensions
q("kink_curiosity", "scenario", "A partner suggests visiting a sex-positive resort or cruise. You:", opts([
    ("Start packing — immersive environments accelerate exploration and I love being surrounded by openness", {"kink_curiosity": 5}),
    ("Very interested — a vacation centered on sexual exploration sounds ideal", {"kink_curiosity": 4}),
    ("Hesitant but curious", {"kink_curiosity": 3}),
    ("No — I keep my sex life private and contained", {"kink_curiosity": 1})
]))

q("experience_breadth", "behavioral_recall", "Your experience with long-distance kink (assigned tasks, remote control toys, video scenes, phone domination):", opts([
    ("Significant — I've maintained full kink dynamics across distances using creative methods", {"experience_breadth": 5}),
    ("Some — I've used remote-control toys or phone dynamics", {"experience_breadth": 4}),
    ("Minimal — sexting only", {"experience_breadth": 3}),
    ("None", {"experience_breadth": 1})
]))

q("boundary_clarity", "forced_choice", "The relationship between alcohol and your kink boundaries:", opts([
    ("Strict separation — I don't negotiate, renegotiate, or push limits under any influence. Period", {"boundary_clarity": 5}),
    ("Mostly separate — I've learned that altered states and boundary management don't mix", {"boundary_clarity": 4}),
    ("A drink loosens me up and doesn't affect my judgment", {"boundary_clarity": 2}),
    ("Alcohol has led to boundary crossings I regret", {"boundary_clarity": 1})
]))

q("communication_about_kink", "scenario", "Requesting something specific during sex — 'I want you to [specific act] while [specific position] and say [specific words].' How comfortable:", opts([
    ("Completely — specific requests get specific results, and I've learned to ask for exactly what I want", {"communication_about_kink": 5}),
    ("Fairly comfortable — I can make specific requests", {"communication_about_kink": 4}),
    ("Somewhat — I'll gesture toward what I want but not be that precise", {"communication_about_kink": 3}),
    ("Very uncomfortable — asking for something that specific feels demanding", {"communication_about_kink": 1})
]))

q("shame_vs_acceptance", "scenario", "Your parents find explicit kink content on your phone. Your internal response:", opts([
    ("Embarrassing, sure — but not shameful. My sexuality is healthy and consensual. I'd set a boundary about privacy, not apologize for content", {"shame_vs_acceptance": 5}),
    ("Mortified in the moment but able to recover — it doesn't change how I feel about myself", {"shame_vs_acceptance": 4}),
    ("Deeply ashamed — I'd want to disappear", {"shame_vs_acceptance": 2}),
    ("Devastated — this would damage my sense of self", {"shame_vs_acceptance": 1})
]))

q("safety_consciousness", "behavioral_recall", "How do you track your own physical and emotional state during a scene?", opts([
    ("Actively — I monitor my heart rate, emotional state, endorphin levels, and hydration. I know my own warning signs and respect them", {"safety_consciousness": 5}),
    ("I check in with myself periodically", {"safety_consciousness": 4}),
    ("I'm usually too in the moment to self-monitor", {"safety_consciousness": 2}),
    ("I don't — I focus on the experience, not my state", {"safety_consciousness": 1})
]))

q("partner_exploration_style", "scenario", "Creating ritual and ceremony around kink (collaring ceremonies, anniversary scenes, marking milestones with new experiences):", opts([
    ("Is something I actively do — marking our kink journey with ceremony adds meaning and memory", {"partner_exploration_style": 5}),
    ("Sounds meaningful — I'd participate", {"partner_exploration_style": 4}),
    ("A bit much — sex doesn't need ceremony", {"partner_exploration_style": 2}),
    ("Weird", {"partner_exploration_style": 1})
]))

q("kink_curiosity", "behavioral_recall", "How many different kink-related skills have you developed (rope tying, flogging technique, massage, dominance voice, etc.)?", opts([
    ("5+ — I treat kink skills like any craft and deliberately practice", {"kink_curiosity": 5}),
    ("3-4 — I've invested in learning key skills", {"kink_curiosity": 4}),
    ("1-2 — I'm competent at the basics", {"kink_curiosity": 3}),
    ("None specifically — I rely on instinct", {"kink_curiosity": 1})
]))

q("experience_breadth", "scenario", "Tantric or slow-sex practices combined with kink (extended arousal, energy work, breathing techniques during play):", opts([
    ("Experienced — combining mindfulness practices with kink creates extraordinary states", {"experience_breadth": 5}),
    ("Some experience — I've incorporated breathing or edging into play", {"experience_breadth": 4}),
    ("Curious but separate in my mind — kink and tantra seem like different worlds", {"experience_breadth": 3}),
    ("No interest in combining these", {"experience_breadth": 1})
]))

q("boundary_clarity", "somatic", "When a boundary of yours is crossed (even a small one), how quickly do you notice in your body?", opts([
    ("Immediately — I have finely tuned somatic awareness and my body signals boundaries before my mind catches up", {"boundary_clarity": 5}),
    ("Fairly quickly — I notice physical discomfort within moments", {"boundary_clarity": 4}),
    ("Slowly — sometimes I don't realize until after the scene", {"boundary_clarity": 2}),
    ("I often don't notice — I process it days or weeks later", {"boundary_clarity": 1})
]))

q("communication_about_kink", "scenario", "Negotiating a scene via text before meeting — a detailed back-and-forth about what will happen. You find this:", opts([
    ("Essential and arousing — text negotiation lets me be thorough AND builds anticipation", {"communication_about_kink": 5}),
    ("Useful and a turn-on", {"communication_about_kink": 4}),
    ("Practical but not exciting — negotiation isn't foreplay for me", {"communication_about_kink": 3}),
    ("Tedious — I'd rather figure it out in person", {"communication_about_kink": 1})
]))

q("shame_vs_acceptance", "scenario", "If society fully destigmatized kink tomorrow — it was seen as a normal part of human sexuality — how much of your behavior would change?", opts([
    ("Very little — I already live as if it's normal, because for me it is", {"shame_vs_acceptance": 5}),
    ("I'd be more open in casual conversation but my actual practices wouldn't change", {"shame_vs_acceptance": 4}),
    ("Significantly — I hide a lot that I would stop hiding", {"shame_vs_acceptance": 2}),
    ("Enormously — shame keeps me from doing most of what I want", {"shame_vs_acceptance": 1})
]))

q("safety_consciousness", "scenario", "You realize mid-scene that you're more affected than you expected (dropping, triggered, overwhelmed). You:", opts([
    ("Communicate immediately, even if it disrupts the scene — my self-awareness and self-advocacy are non-negotiable", {"safety_consciousness": 5}),
    ("Signal to slow down and check in", {"safety_consciousness": 4}),
    ("Try to push through — I'll process it later", {"safety_consciousness": 2}),
    ("Dissociate — I leave my body and check out", {"safety_consciousness": 1})
]))

q("partner_exploration_style", "scenario", "Kink anniversaries — marking the date of your first scene, collaring date, or other milestones:", opts([
    ("Important to me — I track these and celebrate them, sometimes with recreations or new experiences", {"partner_exploration_style": 5}),
    ("Nice to acknowledge", {"partner_exploration_style": 4}),
    ("I don't track kink milestones specifically", {"partner_exploration_style": 2}),
    ("Seems excessive", {"partner_exploration_style": 1})
]))

q("kink_curiosity", "forced_choice", "If you could safely observe any kink activity being practiced by experienced practitioners (purely for education, not participation), you would:", opts([
    ("Choose something I know nothing about — maximum learning potential", {"kink_curiosity": 5}),
    ("Choose something I'm curious about but haven't tried", {"kink_curiosity": 4}),
    ("Choose something I already enjoy — to see how others do it", {"kink_curiosity": 3}),
    ("Decline — observation feels voyeuristic", {"kink_curiosity": 1})
]))

q("experience_breadth", "forced_choice", "Fetish-specific experience (latex, leather, feet, lingerie, uniforms, masks):", opts([
    ("Multiple fetish experiences — I've explored several material/aesthetic kinks", {"experience_breadth": 5}),
    ("One or two — I have a specific fetish I've explored", {"experience_breadth": 4}),
    ("Lingerie/aesthetics only — nothing I'd call a fetish", {"experience_breadth": 3}),
    ("None", {"experience_breadth": 1})
]))

q("boundary_clarity", "forced_choice", "Limit renegotiation — changing a limit after you've set it:", opts([
    ("Is a healthy process when done deliberately, outside of a scene, with full emotional clarity — limits should evolve, not be impulsive", {"boundary_clarity": 5}),
    ("Should happen after reflection, not in the heat of the moment", {"boundary_clarity": 4}),
    ("Is fine whenever — people change their minds", {"boundary_clarity": 2}),
    ("Limits shouldn't change — consistency matters", {"boundary_clarity": 1})
]))

q("communication_about_kink", "temporal", "How has your kink vocabulary expanded over time?", opts([
    ("Enormously — I now have precise language for dynamics, acts, emotional states, and physical sensations that I couldn't name years ago", {"communication_about_kink": 5}),
    ("Significantly — I can discuss most things clearly", {"communication_about_kink": 4}),
    ("Somewhat — I know more terms than I used to", {"communication_about_kink": 3}),
    ("Not much — I still struggle with terminology", {"communication_about_kink": 1})
]))

q("shame_vs_acceptance", "forced_choice", "The word 'pervert' applied to you makes you feel:", opts([
    ("Amused or even proud — I've reclaimed it. Yes, my sexuality is outside the mainstream, and that's fine", {"shame_vs_acceptance": 5}),
    ("Neutral — it's just a word", {"shame_vs_acceptance": 4}),
    ("Uncomfortable — even as a joke", {"shame_vs_acceptance": 2}),
    ("Hurt — it confirms my worst self-assessment", {"shame_vs_acceptance": 1})
]))

q("safety_consciousness", "temporal", "How often do you review and update your own safety practices and knowledge?", opts([
    ("Regularly — safety education is ongoing. I re-read, attend refresher workshops, and stay current", {"safety_consciousness": 5}),
    ("Occasionally — when something prompts me to review", {"safety_consciousness": 4}),
    ("Rarely — I established practices and stick to them", {"safety_consciousness": 3}),
    ("Never — I learned enough early on", {"safety_consciousness": 1})
]))

q("partner_exploration_style", "behavioral_recall", "In your most successful kink partnership, how was exploration managed?", opts([
    ("As an ongoing co-creative project — we regularly discussed desires, planned new experiences, debriefed thoroughly, and built on each experience", {"partner_exploration_style": 5}),
    ("One of us brought ideas and the other was enthusiastic — it worked well", {"partner_exploration_style": 4}),
    ("Organically — we naturally fell into new things without much planning", {"partner_exploration_style": 3}),
    ("We found what worked and repeated it — not much exploration", {"partner_exploration_style": 1})
]))

q("kink_curiosity", "scenario", "Kink-adjacent practices (tantra, somatic therapy, breathwork, ecstatic dance) — your level of interest:", opts([
    ("High — I see these as part of the same exploration of embodied experience", {"kink_curiosity": 5}),
    ("Curious — there's obvious overlap", {"kink_curiosity": 4}),
    ("Separate interests — I don't connect them to kink", {"kink_curiosity": 2}),
    ("No interest in any of these", {"kink_curiosity": 1})
]))

q("experience_breadth", "scenario", "BDSM photography or art creation — being part of creating kink-themed visual art:", opts([
    ("Experienced and enthusiastic — I've modeled, photographed, or created kink art", {"experience_breadth": 5}),
    ("Have done it once or would love to", {"experience_breadth": 4}),
    ("Interesting concept but too exposed", {"experience_breadth": 3}),
    ("No", {"experience_breadth": 1})
]))

print(f"Total questions: {len(questions)}")
with open("/Users/user/personal/sb/trueassess/priv/question_bank/kink_exploration.json", "w") as f:
    json.dump(questions, f, indent=2)
print("Written kink_exploration.json")
