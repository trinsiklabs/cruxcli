import json
with open("/Users/user/personal/sb/trueassess/priv/question_bank/power_exchange_depth.json") as f:
    questions = json.load(f)
uid_counter = len(questions) + 1
def q(dim, qtype, text, options, tier_role="core", trap=False, cg=None, opacity=0.6, cross=None, tags=None):
    global uid_counter
    uid = f"pd_{uid_counter:03d}"
    uid_counter += 1
    questions.append({"uid": uid, "assessment_id": "power_exchange_depth", "dimension": dim, "question_type": qtype, "text": text, "options": options, "cross_scores": cross or [], "anti_gaming": {"opacity": opacity, "social_desirability_trap": trap, "consistency_group": cg or f"{dim}_core", "reversal": False}, "cultural_adaptability": {"universal": True, "adaptations_needed": [], "adaptation_notes": None}, "content_rating": "X", "content_categories": ["bdsm", "power_exchange"], "depth_tier": "deep", "tier_role": tier_role, "tags": tags or ["nsfw", "power_exchange", dim]})
def opts(ts):
    return [{"id": chr(97+i), "text": t, "scores": s} for i, (t, s) in enumerate(ts)]

# Fill 33 more questions across dimensions
q("lifestyle_vs_bedroom", "scenario", "Working from home while in a lifestyle D/s dynamic — the dynamic is present even during work hours:", opts([
    ("I incorporate it: morning reporting, check-ins, tasks between meetings. The dynamic doesn't pause for work", {"lifestyle_vs_bedroom": 5}),
    ("Light touches — a text protocol, awareness of the dynamic", {"lifestyle_vs_bedroom": 4}),
    ("Work time is work time — no dynamic", {"lifestyle_vs_bedroom": 2}),
    ("The dynamic never applies during professional hours", {"lifestyle_vs_bedroom": 1})
]))

q("protocol_depth", "scenario", "Meal protocols (asking permission before eating, eating only after the Dominant, serving their plate first):", opts([
    ("Are a meaningful daily ritual — even something as mundane as a meal becomes a practice of deference and care", {"protocol_depth": 5}),
    ("Are a nice addition I've enjoyed", {"protocol_depth": 4}),
    ("Are excessive", {"protocol_depth": 2}),
    ("Are weird — eating is eating", {"protocol_depth": 1})
]))

q("service_orientation_depth", "forced_choice", "Emotional service — being your Dominant's emotional support, confidante, and safe space:", opts([
    ("Is the highest form of service — being trusted with their emotional life is the deepest privilege", {"service_orientation_depth": 5}),
    ("Is important — a submissive should be a safe harbor", {"service_orientation_depth": 4}),
    ("Is part of any relationship — not specific to D/s", {"service_orientation_depth": 3}),
    ("Isn't my role — they should have a therapist for that", {"service_orientation_depth": 1})
]))

q("authority_exchange_comfort", "forced_choice", "Micro-management (Dominant controlling small details: what to wear, what to eat, when to sleep) vs. macro-management (Dominant setting broad goals and expectations):", opts([
    ("I thrive under either depending on context — sometimes micro-management is deeply grounding, sometimes macro gives me room to serve creatively", {"authority_exchange_comfort": 5}),
    ("Prefer macro — I want goals, not a checklist", {"authority_exchange_comfort": 4}),
    ("Prefer micro in scenes, macro in daily life", {"authority_exchange_comfort": 3}),
    ("Neither — I don't want to be managed", {"authority_exchange_comfort": 1})
]))

q("trust_calibration", "scenario", "Your partner accidentally triggers a trauma response during play (despite negotiation). How they handle the aftermath:", opts([
    ("Determines whether trust deepens or breaks. A good response (immediate stop, care, accountability, no defensiveness) can actually BUILD trust. A bad response (guilt-tripping, minimizing, blaming) destroys it", {"trust_calibration": 5}),
    ("Matters a lot — their response to mistakes reveals character", {"trust_calibration": 4}),
    ("Would shake my trust regardless of response", {"trust_calibration": 3}),
    ("Would end things — accidents like that shouldn't happen", {"trust_calibration": 1})
]))

q("dynamic_health", "behavioral_recall", "How do you maintain your own identity and autonomy within a D/s dynamic?", opts([
    ("Deliberately: I maintain friendships, hobbies, goals, and boundaries that exist outside the dynamic. A healthy submissive/dominant has a life beyond the relationship", {"dynamic_health": 5}),
    ("I stay connected to my own interests and people", {"dynamic_health": 4}),
    ("It can be hard — the dynamic sometimes absorbs everything", {"dynamic_health": 2}),
    ("The dynamic IS my identity now", {"dynamic_health": 1})
]), tier_role="trap", trap=True)

q("negotiation_skill", "scenario", "Your partner reveals a kink mid-negotiation that catches you completely off guard. You:", opts([
    ("Respond with curiosity, not judgment: 'I wasn't expecting that. Tell me more about what it means to you.' Then decide based on information, not reaction", {"negotiation_skill": 5}),
    ("Ask questions before reacting — I want to understand before I judge", {"negotiation_skill": 4}),
    ("React visibly but try to recover", {"negotiation_skill": 3}),
    ("My shock shows and probably hurts them", {"negotiation_skill": 1})
]))

q("aftercare_practice", "scenario", "Aftercare for a scene that went badly (emotional trigger, injury, consent gray area):", opts([
    ("Is even MORE important than usual. Additional steps: longer holding, explicit verbal processing, acknowledgment of what went wrong, a plan for repair, and potentially professional support if needed", {"aftercare_practice": 5}),
    ("Requires extra attention and conversation", {"aftercare_practice": 4}),
    ("Is the same as usual — aftercare is aftercare", {"aftercare_practice": 3}),
    ("Is awkward — I don't know how to process a bad scene", {"aftercare_practice": 1})
]))

q("lifestyle_vs_bedroom", "forced_choice", "The ideal D/s relationship for you:", opts([
    ("Is woven into the fabric of daily life — not as constant intensity but as constant awareness that we've chosen this structure and it shapes everything", {"lifestyle_vs_bedroom": 5}),
    ("Has daily elements and deeper sessions — a blend", {"lifestyle_vs_bedroom": 4}),
    ("Is primarily bedroom-based with occasional extensions", {"lifestyle_vs_bedroom": 2}),
    ("Stays firmly in the sexual realm", {"lifestyle_vs_bedroom": 1})
]), tier_role="consistency_check", cg="lvb_core")

q("protocol_depth", "forced_choice", "The ideal number of active protocols in your dynamic:", opts([
    ("Enough to create a persistent awareness of the structure — I want protocols woven through my day", {"protocol_depth": 5}),
    ("Several meaningful ones that anchor the dynamic", {"protocol_depth": 4}),
    ("A few — less is more", {"protocol_depth": 3}),
    ("None — protocols are artificial constraints", {"protocol_depth": 1})
]), tier_role="consistency_check", cg="pd_core")

q("service_orientation_depth", "forced_choice", "Your service orientation score — honestly, how central is service to your D/s identity?", opts([
    ("Defining — service IS my submission/dominance. Everything else flows from or supports the service dynamic", {"service_orientation_depth": 5}),
    ("Very important — service is a major component", {"service_orientation_depth": 4}),
    ("Moderate — service is one element among many", {"service_orientation_depth": 3}),
    ("Peripheral — service isn't central to my kink identity", {"service_orientation_depth": 1})
]), tier_role="consistency_check", cg="sod_core")

q("authority_exchange_comfort", "forced_choice", "Your honest comfort level with real authority exchange (not roleplay, not bedroom games — genuine authority over real decisions):", opts([
    ("High — I've done this, I understand the weight of it, and I find it deeply fulfilling on whichever side I'm on", {"authority_exchange_comfort": 5}),
    ("Moderate-high — I'm comfortable in specific areas", {"authority_exchange_comfort": 4}),
    ("Low-moderate — authority exchange in theory appeals but in practice I resist", {"authority_exchange_comfort": 3}),
    ("Low — real authority exchange isn't for me", {"authority_exchange_comfort": 1})
]), tier_role="consistency_check", cg="aec_core")

q("trust_calibration", "behavioral_recall", "The longest you've ever taken to fully trust a D/s partner:", opts([
    ("Months to years — and the depth of trust we eventually reached justified every moment of patient building", {"trust_calibration": 5}),
    ("Several months — it took time but was worth it", {"trust_calibration": 4}),
    ("Weeks — I'm fairly quick to trust", {"trust_calibration": 3}),
    ("Days — trust comes quickly for me", {"trust_calibration": 1})
]))

q("dynamic_health", "forced_choice", "The role of therapy/counseling alongside a D/s dynamic:", opts([
    ("Complementary and recommended — a therapist helps me understand my patterns, process experiences, and ensure my kink choices come from health rather than pathology", {"dynamic_health": 5}),
    ("Useful — I've combined therapy with D/s to good effect", {"dynamic_health": 4}),
    ("Separate — therapy and kink don't overlap", {"dynamic_health": 3}),
    ("Unnecessary — I don't need therapy about my sex life", {"dynamic_health": 1})
]))

q("negotiation_skill", "scenario", "CNC (consensual non-consent) negotiation — the most complex negotiation in BDSM. Your approach:", opts([
    ("Multi-session negotiation: detailed scenarios, specific triggers to avoid, multiple failsafe systems beyond verbal safewords, pre-scene and post-scene psychological check-in, limits on duration, debriefing protocol, contingency for trauma responses", {"negotiation_skill": 5}),
    ("Extensive — this requires the most thorough negotiation of any activity", {"negotiation_skill": 4}),
    ("I'd need experienced guidance to negotiate this safely", {"negotiation_skill": 3}),
    ("I wouldn't know where to start", {"negotiation_skill": 1})
]))

q("aftercare_practice", "forced_choice", "Professional aftercare resources (kink-aware therapists, community support) for processing intense D/s experiences:", opts([
    ("Are a sign of maturity, not weakness — I've used or would use professional support for processing intense experiences", {"aftercare_practice": 5}),
    ("Are a good idea for very intense dynamics", {"aftercare_practice": 4}),
    ("Seem like overkill — if you need a therapist for your kink, maybe it's too much", {"aftercare_practice": 2}),
    ("Are unnecessary", {"aftercare_practice": 1})
]))

# More fillers
q("lifestyle_vs_bedroom", "scenario", "Sleep protocols (sleeping positions, asking permission to get up, maintaining physical contact throughout the night):", opts([
    ("Are intimate and connecting — even sleep reflects the dynamic", {"lifestyle_vs_bedroom": 5}),
    ("Some are sweet — sleeping touching is nice as a protocol", {"lifestyle_vs_bedroom": 4}),
    ("Are impractical — sleep is sleep", {"lifestyle_vs_bedroom": 2}),
    ("Seem controlling in a bad way", {"lifestyle_vs_bedroom": 1})
]))

q("protocol_depth", "scenario", "End-of-day reporting — telling your Dominant about your day, how you felt, what you struggled with, what you're proud of:", opts([
    ("Is one of my favorite protocols — the accountability and intimacy of daily reporting deepens the dynamic profoundly", {"protocol_depth": 5}),
    ("Is a meaningful check-in", {"protocol_depth": 4}),
    ("Is a nice idea but feels forced daily", {"protocol_depth": 3}),
    ("Is my partner acting like my therapist", {"protocol_depth": 1})
]))

q("service_orientation_depth", "scenario", "Your Dominant is ungrateful for your service — they don't acknowledge or thank you. You:", opts([
    ("Continue serving — my service isn't contingent on acknowledgment. Though I'll address the pattern if it persists, because recognition IS part of a healthy dynamic", {"service_orientation_depth": 5}),
    ("Feel hurt and bring it up — acknowledgment matters", {"service_orientation_depth": 4}),
    ("Reduce my service — why bother if it's not appreciated?", {"service_orientation_depth": 2}),
    ("Stop — service without appreciation is exploitation", {"service_orientation_depth": 1})
]))

q("authority_exchange_comfort", "scenario", "Your Dominant makes a rule that benefits THEM but has no benefit to you (and may inconvenience you). This:", opts([
    ("Is within the scope of authority exchange — not every rule needs to serve me. The exchange itself serves the dynamic", {"authority_exchange_comfort": 5}),
    ("Is acceptable if the dynamic overall is balanced", {"authority_exchange_comfort": 4}),
    ("Bothers me — rules should benefit both people", {"authority_exchange_comfort": 2}),
    ("Is selfish — rules should serve the relationship, not just one person", {"authority_exchange_comfort": 1})
]))

q("trust_calibration", "scenario", "Your Dominant asks for more authority than you've previously given. You:", opts([
    ("Evaluate carefully: what are they asking for? Have they earned it through reliability in what they already hold? Am I extending from trust or from pressure?", {"trust_calibration": 5}),
    ("Consider it seriously — growth means expanding", {"trust_calibration": 4}),
    ("Hesitate — more authority feels risky", {"trust_calibration": 3}),
    ("Resist — they already have enough", {"trust_calibration": 1})
]))

q("dynamic_health", "scenario", "Burnout from the Dominant/top role — feeling exhausted by the responsibility of holding authority, making decisions, managing the dynamic:", opts([
    ("Is real and should be named and addressed: 'I need to lighten the load right now.' The myth that Dominants are inexhaustible is harmful", {"dynamic_health": 5}),
    ("Should be communicated and accommodated", {"dynamic_health": 4}),
    ("Is a sign maybe you shouldn't be Dominant", {"dynamic_health": 2}),
    ("Isn't real — if you can't handle the responsibility, don't take it", {"dynamic_health": 1})
]))

q("negotiation_skill", "behavioral_recall", "The negotiation skill you're most proud of developing:", opts([
    ("The ability to create space for honest, shame-free disclosure — I can make people feel safe enough to tell me their real desires, limits, and fears", {"negotiation_skill": 5}),
    ("Thoroughness — I don't miss important topics", {"negotiation_skill": 4}),
    ("I'm still developing my negotiation skills", {"negotiation_skill": 3}),
    ("I don't think about negotiation as a 'skill'", {"negotiation_skill": 1})
]))

q("aftercare_practice", "scenario", "You discover a new partner has never experienced structured aftercare before. You:", opts([
    ("Educate them: 'Aftercare is as important as the scene itself. Here's what I need, and I want to learn what you need. Let's build an aftercare plan before we play'", {"aftercare_practice": 5}),
    ("Model good aftercare and explain its importance", {"aftercare_practice": 4}),
    ("Do what I normally do and hope they follow", {"aftercare_practice": 3}),
    ("Let them figure out their own needs", {"aftercare_practice": 1})
]))

q("lifestyle_vs_bedroom", "scenario", "The concept of a D/s household (where the entire domestic structure reflects the power exchange — assigned roles, designated spaces, visual symbols):", opts([
    ("Is aspirational or my current reality — living in a space that reflects the dynamic makes it tangible and permanent", {"lifestyle_vs_bedroom": 5}),
    ("Appeals to me — some domestic reflection of the dynamic would be nice", {"lifestyle_vs_bedroom": 4}),
    ("Is too much — a normal home where we sometimes play kinky", {"lifestyle_vs_bedroom": 2}),
    ("Sounds like a commune", {"lifestyle_vs_bedroom": 1})
]))

q("protocol_depth", "forced_choice", "Punishment protocols (formal punishment for rule violations, with specific implements, positions, and severity):", opts([
    ("Are an essential part of maintaining a disciplined dynamic — punishment isn't just play, it's accountability", {"protocol_depth": 5}),
    ("Work in some dynamics — real punishment requires real trust", {"protocol_depth": 4}),
    ("Should be fun punishment only — play, not real correction", {"protocol_depth": 3}),
    ("Are problematic — adults don't punish each other", {"protocol_depth": 1})
]))

q("service_orientation_depth", "temporal", "The evolution of your service skills over time:", opts([
    ("From basic compliance to sophisticated anticipatory service — I've trained in skills, studied my partner's preferences, and developed an intuition for their needs that took years to build", {"service_orientation_depth": 5}),
    ("Improved significantly with practice and feedback", {"service_orientation_depth": 4}),
    ("Somewhat better", {"service_orientation_depth": 3}),
    ("About the same", {"service_orientation_depth": 1})
]))

q("trust_calibration", "forced_choice", "The relationship between trust and surrender:", opts([
    ("They're inseparable — surrender without trust is just compliance. Real surrender requires trusting that the person holding you won't drop you", {"trust_calibration": 5}),
    ("Trust enables surrender — they're closely linked", {"trust_calibration": 4}),
    ("You can surrender without trust if the boundaries are clear enough", {"trust_calibration": 2}),
    ("Surrender doesn't require trust — it requires negotiation", {"trust_calibration": 1})
]))

q("dynamic_health", "temporal", "Looking back at your D/s journey, the most important lesson about healthy power exchange:", opts([
    ("The dynamic exists to serve the people in it, not the other way around. The moment the structure becomes more important than the humans, it's gone wrong", {"dynamic_health": 5}),
    ("Communication is everything — without it, even good dynamics fail", {"dynamic_health": 4}),
    ("Find the right person — the dynamic is only as good as the people in it", {"dynamic_health": 3}),
    ("I'm still learning", {"dynamic_health": 2})
]))

print(f"Total questions: {len(questions)}")
with open("/Users/user/personal/sb/trueassess/priv/question_bank/power_exchange_depth.json", "w") as f:
    json.dump(questions, f, indent=2)
print("Written power_exchange_depth.json")
