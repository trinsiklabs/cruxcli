import json
questions = []
uid_counter = 1
def q(dim, qtype, text, options, tier_role="core", trap=False, cg=None, opacity=0.6, cross=None, tags=None):
    global uid_counter
    uid = f"pd_{uid_counter:03d}"
    uid_counter += 1
    questions.append({"uid": uid, "assessment_id": "power_exchange_depth", "dimension": dim, "question_type": qtype, "text": text, "options": options, "cross_scores": cross or [], "anti_gaming": {"opacity": opacity, "social_desirability_trap": trap, "consistency_group": cg or f"{dim}_core", "reversal": False}, "cultural_adaptability": {"universal": True, "adaptations_needed": [], "adaptation_notes": None}, "content_rating": "X", "content_categories": ["bdsm", "power_exchange"], "depth_tier": "deep", "tier_role": tier_role, "tags": tags or ["nsfw", "power_exchange", dim]})
def opts(ts):
    return [{"id": chr(97+i), "text": t, "scores": s} for i, (t, s) in enumerate(ts)]

# LIFESTYLE VS BEDROOM (19)
dim = "lifestyle_vs_bedroom"
q(dim, "scenario", "The scene ends. The lights come on. Your partner who was your Dominant five minutes ago is now asking what you want for dinner as an equal. This transition:", opts([
    ("Feels jarring and unsatisfying — I don't want the power exchange to have an off switch", {"lifestyle_vs_bedroom": 5}),
    ("Works but I prefer some continuity — lingering protocols after a scene feel good", {"lifestyle_vs_bedroom": 4}),
    ("Is exactly right — scenes are scenes, real life is real life", {"lifestyle_vs_bedroom": 2}),
    ("Is how it should be — power exchange outside the bedroom would be unhealthy", {"lifestyle_vs_bedroom": 1})
]))
q(dim, "forced_choice", "The word 'lifestyle' applied to D/s:", opts([
    ("Describes what I want — D/s isn't an activity, it's a way of structuring a relationship", {"lifestyle_vs_bedroom": 5}),
    ("Resonates — I want more than bedroom-only", {"lifestyle_vs_bedroom": 4}),
    ("Sounds extreme — I prefer power exchange in specific contexts", {"lifestyle_vs_bedroom": 2}),
    ("Is a red flag — lifestyle D/s is just control disguised as kink", {"lifestyle_vs_bedroom": 1})
]))
q(dim, "temporal", "How much of a typical day do you want to be aware of your D/s dynamic?", opts([
    ("Most or all of it — through protocols, tasks, mental awareness, or simply knowing my place in the structure", {"lifestyle_vs_bedroom": 5}),
    ("Several touchpoints — morning, check-ins, evening", {"lifestyle_vs_bedroom": 4}),
    ("Only when we're actively playing", {"lifestyle_vs_bedroom": 2}),
    ("Only in the bedroom", {"lifestyle_vs_bedroom": 1})
]), cg="lvb_temporal")
q(dim, "behavioral_recall", "In your longest D/s relationship, how far did the dynamic extend into daily life?", opts([
    ("Comprehensively — it shaped routines, decisions, communication patterns, and domestic structure", {"lifestyle_vs_bedroom": 5}),
    ("Meaningfully — daily protocols, rules, and power-aware communication", {"lifestyle_vs_bedroom": 4}),
    ("Minimally — bedroom and occasional play", {"lifestyle_vs_bedroom": 2}),
    ("Not at all outside sex", {"lifestyle_vs_bedroom": 1})
]), cg="lvb_behavioral")
q(dim, "scenario", "Grocery shopping with your Dominant/submissive partner. The power dynamic is:", opts([
    ("Still active — they defer to me on choices, or I defer to them. The dynamic doesn't pause for errands", {"lifestyle_vs_bedroom": 5}),
    ("Subtly present — we're aware of it even in mundane contexts", {"lifestyle_vs_bedroom": 4}),
    ("Paused — grocery shopping is a vanilla activity", {"lifestyle_vs_bedroom": 2}),
    ("Completely off — D/s has nothing to do with groceries", {"lifestyle_vs_bedroom": 1})
]))
q(dim, "forced_choice", "Morning rituals in a D/s context (specific greeting, kneeling, asking permission for the day's first coffee):", opts([
    ("Are what make a dynamic feel real — daily rituals are the heartbeat of lifestyle D/s", {"lifestyle_vs_bedroom": 5}),
    ("Sound appealing — a few touchpoints to start the day in dynamic", {"lifestyle_vs_bedroom": 4}),
    ("Are too much — mornings are hectic enough", {"lifestyle_vs_bedroom": 2}),
    ("Are performative — real power exchange doesn't need daily theater", {"lifestyle_vs_bedroom": 1})
]))
q(dim, "scenario", "Your Dominant makes a decision you disagree with — about a household matter, not a scene. You:", opts([
    ("Defer — I chose this authority structure and it applies to daily life, not just sex", {"lifestyle_vs_bedroom": 5}),
    ("Express my opinion, then accept their final decision", {"lifestyle_vs_bedroom": 4}),
    ("Argue as equals — D/s doesn't apply to household decisions", {"lifestyle_vs_bedroom": 2}),
    ("Insist on equal say — they're my partner, not my boss", {"lifestyle_vs_bedroom": 1})
]), tier_role="trap", trap=True)
q(dim, "temporal", "Over time in a D/s relationship, you want the lifestyle elements to:", opts([
    ("Expand — as trust deepens, the dynamic should permeate more of daily life", {"lifestyle_vs_bedroom": 5}),
    ("Gradually increase — slow integration", {"lifestyle_vs_bedroom": 4}),
    ("Stay in their lane — bedroom and designated scenes", {"lifestyle_vs_bedroom": 2}),
    ("Decrease — I want more equality as the relationship matures", {"lifestyle_vs_bedroom": 1})
]), cg="lvb_temporal")
q(dim, "somatic", "When the dynamic is 'always on' — a constant hum of awareness that you're in a power exchange even during mundane activities — your nervous system:", opts([
    ("Is calmer than without it — the structure regulates me. The 24/7 awareness IS the benefit", {"lifestyle_vs_bedroom": 5}),
    ("Mostly benefits — the continuity feels grounding", {"lifestyle_vs_bedroom": 4}),
    ("Would be stressed — I need downtime from the dynamic", {"lifestyle_vs_bedroom": 2}),
    ("Would be exhausted — constant role maintenance is unsustainable", {"lifestyle_vs_bedroom": 1})
]))

# PROTOCOL DEPTH (19)
dim = "protocol_depth"
q(dim, "scenario", "A high-protocol household where specific body positions, speech patterns, and behavioral expectations apply at all times:", opts([
    ("Is my ideal — high protocol creates a beautiful, orderly expression of power exchange", {"protocol_depth": 5}),
    ("Appeals to me for certain contexts — not every moment, but specific times and situations", {"protocol_depth": 4}),
    ("Is too rigid — some structure is good but this is military", {"protocol_depth": 2}),
    ("Sounds suffocating", {"protocol_depth": 1})
]))
q(dim, "forced_choice", "Formal speech (titles, permission to speak, specific address forms) in a D/s dynamic:", opts([
    ("Deepens the power exchange with every word — language shapes reality and I want every word to reflect the structure", {"protocol_depth": 5}),
    ("Matters in key contexts — titles during scenes, formal greeting/farewell", {"protocol_depth": 4}),
    ("Is fun for scenes but not daily life", {"protocol_depth": 3}),
    ("Feels ridiculous — just talk normally", {"protocol_depth": 1})
]))
q(dim, "behavioral_recall", "The most protocol-heavy dynamic you've experienced. How many simultaneous rules/protocols were active?", opts([
    ("10+ covering speech, dress, posture, meals, communication, sleep, and more", {"protocol_depth": 5}),
    ("5-10 — a meaningful structure", {"protocol_depth": 4}),
    ("2-4 — a few key protocols", {"protocol_depth": 3}),
    ("0-1", {"protocol_depth": 1})
]), cg="pd_behavioral")
q(dim, "scenario", "Position training — learning specific physical positions and assuming them on command:", opts([
    ("Is deeply fulfilling — my body becoming an expression of their will through trained positions is devotional", {"protocol_depth": 5}),
    ("Is hot and I enjoy the formality", {"protocol_depth": 4}),
    ("Is fun for scenes", {"protocol_depth": 3}),
    ("Feels degrading in a bad way", {"protocol_depth": 1})
]))
q(dim, "temporal", "How quickly do you internalize new protocols (going from consciously remembering to automatically performing)?", opts([
    ("Quickly — within days a new protocol becomes natural, like muscle memory", {"protocol_depth": 5}),
    ("Within a couple weeks", {"protocol_depth": 4}),
    ("Slowly — protocols always require conscious effort", {"protocol_depth": 2}),
    ("I don't — they always feel forced", {"protocol_depth": 1})
]), cg="pd_temporal")
q(dim, "forced_choice", "Written protocol manuals (detailed documents specifying all rules, positions, expectations):", opts([
    ("Are a labor of love — creating or receiving one is deeply meaningful and practical", {"protocol_depth": 5}),
    ("Are very useful — written clarity helps", {"protocol_depth": 4}),
    ("Are overkill — verbal understanding works fine", {"protocol_depth": 2}),
    ("Are treating a relationship like a job — no manual needed", {"protocol_depth": 1})
]))
q(dim, "scenario", "A formal high-protocol dinner party where submissives serve, kneel, and follow strict behavioral rules:", opts([
    ("Is a beautiful social expression of our lifestyle — I'd attend enthusiastically", {"protocol_depth": 5}),
    ("Is exciting — I'd enjoy the formality", {"protocol_depth": 4}),
    ("Is intense — I prefer more casual kink events", {"protocol_depth": 2}),
    ("Makes me uncomfortable", {"protocol_depth": 1})
]))
q(dim, "behavioral_recall", "Have you ever broken a protocol on purpose to test whether your Dominant/submissive noticed or enforced it?", opts([
    ("Never — protocols aren't games to test, they're the fabric of the dynamic and I respect them completely", {"protocol_depth": 5}),
    ("Once, early on — I learned it matters", {"protocol_depth": 4}),
    ("Yes — I sometimes push to see if rules are real", {"protocol_depth": 2}),
    ("Protocols aren't important enough to test", {"protocol_depth": 1})
]), cg="pd_behavioral", tier_role="trap", trap=True)
q(dim, "somatic", "When you perform a protocol perfectly — a flawless greeting, a precise position, a rule followed without thought — your body:", opts([
    ("Hums with satisfaction — the precision itself is pleasurable", {"protocol_depth": 5}),
    ("Feels a small glow of accomplishment", {"protocol_depth": 4}),
    ("Feels nothing special — it's just following rules", {"protocol_depth": 2}),
    ("Feels relief that it's over", {"protocol_depth": 1})
]))

# SERVICE ORIENTATION DEPTH (19)
dim = "service_orientation_depth"
q(dim, "scenario", "Your Dominant assigns you the task of managing their calendar, paying their bills, and organizing their closet. This domestic/administrative service:", opts([
    ("Is deeply fulfilling — making their life smoother through practical service is how I express devotion", {"service_orientation_depth": 5}),
    ("Is satisfying — I enjoy being useful and needed", {"service_orientation_depth": 4}),
    ("Is acceptable — I'll do it but it's chores, not kink", {"service_orientation_depth": 2}),
    ("Is not what D/s means to me — this is household labor, not power exchange", {"service_orientation_depth": 1})
]))
q(dim, "forced_choice", "The highest form of service is:", opts([
    ("Anticipatory — serving needs before they're expressed, because I've studied my Dominant so thoroughly I know what they want before they do", {"service_orientation_depth": 5}),
    ("Responsive — serving well when asked, with skill and willingness", {"service_orientation_depth": 4}),
    ("Obedient — doing what I'm told, when I'm told", {"service_orientation_depth": 3}),
    ("Service isn't central to my understanding of D/s", {"service_orientation_depth": 1})
]))
q(dim, "behavioral_recall", "How much mental energy do you devote to anticipating and meeting a partner's needs?", opts([
    ("Substantial — their comfort, pleasure, and ease are constantly in my awareness", {"service_orientation_depth": 5}),
    ("Significant — I think about how to please them often", {"service_orientation_depth": 4}),
    ("Some — when it occurs to me", {"service_orientation_depth": 3}),
    ("Minimal — I expect them to communicate their needs", {"service_orientation_depth": 1})
]), cg="sod_behavioral")
q(dim, "scenario", "Body service — bathing your Dominant, shaving their body, dressing them, painting their nails. This level of physical care:", opts([
    ("Is worship in physical form — each act of tending their body is an act of devotion", {"service_orientation_depth": 5}),
    ("Is intimate and connecting — I enjoy this kind of care", {"service_orientation_depth": 4}),
    ("Is occasionally nice", {"service_orientation_depth": 3}),
    ("Isn't my thing — I'm not their valet", {"service_orientation_depth": 1})
]))
q(dim, "somatic", "When you've served someone perfectly — anticipated a need, executed a task flawlessly, received praise — your body feels:", opts([
    ("A deep, warm satisfaction — like a circuit completing. This is what I'm FOR", {"service_orientation_depth": 5}),
    ("Pride and pleasure", {"service_orientation_depth": 4}),
    ("Fine — it's nice to be appreciated", {"service_orientation_depth": 3}),
    ("Nothing notable", {"service_orientation_depth": 1})
]))
q(dim, "temporal", "How has your relationship with service evolved?", opts([
    ("Deepened continuously — I've gone from basic obedience to sophisticated anticipatory service, and the depth continues to grow", {"service_orientation_depth": 5}),
    ("Grown — I've become more skilled and willing", {"service_orientation_depth": 4}),
    ("Stayed about the same", {"service_orientation_depth": 3}),
    ("Decreased — I've moved away from service as a focus", {"service_orientation_depth": 1})
]), cg="sod_temporal")
q(dim, "forced_choice", "Service submission vs. sexual submission:", opts([
    ("Service IS my submission — the sexual aspects flow from the service dynamic, not the other way around", {"service_orientation_depth": 5}),
    ("Both matter — service deepens the connection that makes sexual submission meaningful", {"service_orientation_depth": 4}),
    ("Sexual submission is primary — service is a nice addition", {"service_orientation_depth": 3}),
    ("They're separate — I can serve without submitting and submit without serving", {"service_orientation_depth": 1})
]))
q(dim, "scenario", "Your Dominant tells you that your service was unsatisfactory — a meal was wrong, a task was done incorrectly. You:", opts([
    ("Feel genuine remorse and immediately look for how to do better — serving well matters to me as much as it matters to them", {"service_orientation_depth": 5}),
    ("Accept the correction and try again — I want to serve well", {"service_orientation_depth": 4}),
    ("Feel stung — I tried my best", {"service_orientation_depth": 2}),
    ("Feel annoyed — do it yourself if you're that particular", {"service_orientation_depth": 1})
]))
q(dim, "behavioral_recall", "Have you studied specific skills to improve your service (cooking classes, massage training, organizational systems)?", opts([
    ("Yes — I invest in skills that make me a better servant because excellence in service is a point of pride", {"service_orientation_depth": 5}),
    ("Some — I've learned skills relevant to my dynamic", {"service_orientation_depth": 4}),
    ("Not specifically — I use what I already know", {"service_orientation_depth": 3}),
    ("No — service skills aren't something I cultivate", {"service_orientation_depth": 1})
]), cg="sod_behavioral")

# AUTHORITY EXCHANGE COMFORT (19)
dim = "authority_exchange_comfort"
q(dim, "scenario", "Your Dominant makes a decision about something that directly affects you — without consulting you first. Your reaction:", opts([
    ("Trust — they have my interests in mind and I've given them this authority. Consultation is their choice, not my right", {"authority_exchange_comfort": 5}),
    ("Acceptance, though I'd appreciate being informed", {"authority_exchange_comfort": 4}),
    ("Discomfort — I should have been consulted", {"authority_exchange_comfort": 2}),
    ("Anger — no one makes decisions about my life without my input", {"authority_exchange_comfort": 1})
]))
q(dim, "forced_choice", "The phrase 'Because I said so' from a Dominant:", opts([
    ("Is sufficient — in a D/s dynamic, their authority doesn't always require justification", {"authority_exchange_comfort": 5}),
    ("Is acceptable sometimes — I trust them but appreciate reasons when available", {"authority_exchange_comfort": 4}),
    ("Bothers me — even in D/s, I deserve explanations", {"authority_exchange_comfort": 2}),
    ("Is a red flag — authoritarian without reasoning is just controlling", {"authority_exchange_comfort": 1})
]), tier_role="trap", trap=True)
q(dim, "behavioral_recall", "Areas of your life where you've genuinely ceded authority to a partner (finances, diet, social schedule, wardrobe):", opts([
    ("Multiple significant areas — the authority exchange extends wherever it's been negotiated", {"authority_exchange_comfort": 5}),
    ("One or two areas — targeted authority exchange", {"authority_exchange_comfort": 4}),
    ("None in daily life — authority exchange stays sexual/scene-based", {"authority_exchange_comfort": 2}),
    ("None — I don't cede authority to partners", {"authority_exchange_comfort": 1})
]), cg="aec_behavioral")
q(dim, "somatic", "When you submit to an authority decision you disagree with, your body:", opts([
    ("Settles after an initial resistance — the yielding itself becomes the practice. Obedience isn't always comfortable, but the trust it demonstrates IS", {"authority_exchange_comfort": 5}),
    ("Tenses initially then accepts", {"authority_exchange_comfort": 4}),
    ("Stays tense — I comply but my body doesn't agree", {"authority_exchange_comfort": 2}),
    ("Fights it — I can't force compliance when I disagree", {"authority_exchange_comfort": 1})
]))
q(dim, "scenario", "Your Dominant assigns you a task with no explanation for why. You:", opts([
    ("Do it without question — if I need to understand every 'why,' I haven't truly surrendered authority", {"authority_exchange_comfort": 5}),
    ("Do it, though I'm curious about the reason", {"authority_exchange_comfort": 4}),
    ("Ask why before deciding whether to comply", {"authority_exchange_comfort": 2}),
    ("Refuse tasks without clear reasoning", {"authority_exchange_comfort": 1})
]))
q(dim, "temporal", "How has your comfort with yielding authority evolved?", opts([
    ("Deepened significantly — as I've built trust with the right Dominant, yielding feels more natural and freeing with each passing month", {"authority_exchange_comfort": 5}),
    ("Grown — experience has taught me that yielding can be healthy", {"authority_exchange_comfort": 4}),
    ("Stayed cautious — I yield carefully and in limited areas", {"authority_exchange_comfort": 3}),
    ("Decreased — experience has made me more protective of my autonomy", {"authority_exchange_comfort": 1})
]), cg="aec_temporal")

# TRUST CALIBRATION (19)
dim = "trust_calibration"
q(dim, "scenario", "A new potential D/s partner asks for immediate total power exchange. You:", opts([
    ("Decline — trust is earned incrementally and anyone who asks for total authority before it's been built doesn't understand what they're asking for", {"trust_calibration": 5}),
    ("Proceed very slowly — building trust takes time", {"trust_calibration": 4}),
    ("Jump in — instant chemistry means instant trust", {"trust_calibration": 2}),
    ("Give it — they seem confident enough", {"trust_calibration": 1})
]), tier_role="trap", trap=True)
q(dim, "forced_choice", "Trust in D/s is built through:", opts([
    ("Consistent action over time — a Dominant earns authority by demonstrating competence, care, and follow-through repeatedly", {"trust_calibration": 5}),
    ("A combination of communication, consistency, and chemistry", {"trust_calibration": 4}),
    ("Strong initial connection and good negotiation", {"trust_calibration": 3}),
    ("Gut feeling — I know when I trust someone", {"trust_calibration": 1})
]))
q(dim, "behavioral_recall", "How long did it take in your most significant D/s dynamic before you felt comfortable with deep authority exchange?", opts([
    ("Months — we built incrementally, adding layers of trust and authority as each was proven reliable", {"trust_calibration": 5}),
    ("Weeks to a couple months — trust built relatively quickly", {"trust_calibration": 4}),
    ("Days to weeks — the connection was strong from the start", {"trust_calibration": 2}),
    ("Immediately — deep trust was instant", {"trust_calibration": 1})
]), cg="tc_behavioral")
q(dim, "scenario", "Your Dominant does something that erodes your trust (forgets a limit, discloses private information, uses authority carelessly). You:", opts([
    ("Address it immediately, specifically, and with clear expectations: 'This violated my trust because X. For me to re-extend this authority, I need Y.' Trust can be rebuilt, but pretending nothing happened guarantees it won't be", {"trust_calibration": 5}),
    ("Bring it up — it needs discussion and repair", {"trust_calibration": 4}),
    ("Feel hurt but hope it doesn't happen again", {"trust_calibration": 2}),
    ("Pull back without explaining why — trust once broken is done", {"trust_calibration": 1})
]))
q(dim, "temporal", "Your trust calibration — the rate at which you extend, build, and sometimes withdraw trust — is:", opts([
    ("Deliberate and earned — I extend trust in measured increments matched to demonstrated reliability. Fast trust is naive trust", {"trust_calibration": 5}),
    ("Careful — I take my time but do extend it", {"trust_calibration": 4}),
    ("Intuitive — I trust my gut about people", {"trust_calibration": 3}),
    ("Either all-in or all-out — I don't do gradual", {"trust_calibration": 1})
]), cg="tc_temporal")
q(dim, "forced_choice", "The single most important quality in a Dominant (or submissive):", opts([
    ("Trustworthiness — without reliable trust, no depth of exchange is possible regardless of chemistry or skill", {"trust_calibration": 5}),
    ("Communication — trust is built through honest conversation", {"trust_calibration": 4}),
    ("Chemistry — you can't negotiate attraction", {"trust_calibration": 2}),
    ("Skill — a competent partner makes everything better", {"trust_calibration": 1})
]))

# DYNAMIC HEALTH (19)
dim = "dynamic_health"
q(dim, "scenario", "You notice your D/s dynamic is creating anxiety instead of security. You:", opts([
    ("Address it immediately: 'The dynamic is supposed to enhance our lives, not diminish them. Something has shifted and we need to recalibrate'", {"dynamic_health": 5}),
    ("Bring it up — this needs attention", {"dynamic_health": 4}),
    ("Wait and see — maybe it's temporary", {"dynamic_health": 2}),
    ("Endure it — this is what I signed up for", {"dynamic_health": 1})
]), tier_role="trap", trap=True)
q(dim, "forced_choice", "A healthy D/s dynamic should:", opts([
    ("Make both people MORE functional, MORE secure, and MORE connected than they would be without it. If it's not enhancing life, something is wrong", {"dynamic_health": 5}),
    ("Bring more satisfaction than stress to both people", {"dynamic_health": 4}),
    ("Be exciting and sexually fulfilling", {"dynamic_health": 3}),
    ("Be whatever the people in it decide it is", {"dynamic_health": 1})
]))
q(dim, "behavioral_recall", "How often do you and your D/s partner step outside the dynamic to check in about the dynamic itself?", opts([
    ("Regularly — scheduled 'out of dynamic' conversations about how the structure is working for both of us", {"dynamic_health": 5}),
    ("When needed — we can pause the dynamic for real talk", {"dynamic_health": 4}),
    ("Rarely — the dynamic is the dynamic", {"dynamic_health": 2}),
    ("Never — stepping outside the dynamic undermines it", {"dynamic_health": 1})
]), cg="dh_behavioral")
q(dim, "scenario", "You realize that the power exchange in your dynamic has become one-sided in a way that's draining you (too much giving, not enough receiving). You:", opts([
    ("Name it: 'I need to renegotiate. The balance has shifted in a way that isn't sustainable.' D/s should sustain, not deplete", {"dynamic_health": 5}),
    ("Bring it up — balance matters", {"dynamic_health": 4}),
    ("Absorb it — serving means accepting the hard parts", {"dynamic_health": 2}),
    ("Leave — if a dynamic isn't working, it's over", {"dynamic_health": 1})
]))
q(dim, "forced_choice", "The difference between D/s and abuse is:", opts([
    ("Clear and non-negotiable: informed consent, mutual benefit, the ability to leave, ongoing negotiation, and the sub/bottom's wellbeing being a primary concern of the Dom/top", {"dynamic_health": 5}),
    ("Consent and communication — if both people choose and can leave, it's D/s", {"dynamic_health": 4}),
    ("Mostly about consent — though the line can be blurry", {"dynamic_health": 3}),
    ("Hard to define — it's subjective", {"dynamic_health": 1})
]))
q(dim, "temporal", "In long-term D/s relationships, the dynamic typically needs:", opts([
    ("Regular maintenance — scheduled check-ins, renegotiation, evolution. A dynamic that never adapts will atrophy or become harmful", {"dynamic_health": 5}),
    ("Periodic adjustment — course corrections as life changes", {"dynamic_health": 4}),
    ("Minimal maintenance — set it and forget it", {"dynamic_health": 2}),
    ("No maintenance — the initial negotiation covers everything", {"dynamic_health": 1})
]), cg="dh_temporal")
q(dim, "scenario", "Your submissive is using the dynamic to avoid dealing with their mental health issues (using structure to mask anxiety, using punishment to process guilt, etc.). You:", opts([
    ("Pause the dynamic and address it: 'I think our structure is being used as a coping mechanism instead of dealing with the underlying issue. That's not sustainable or healthy. Let's talk about what's really going on'", {"dynamic_health": 5}),
    ("Bring it up gently — they may not see it themselves", {"dynamic_health": 4}),
    ("Continue — if it's helping them cope, what's the harm?", {"dynamic_health": 2}),
    ("Not my problem — they're an adult", {"dynamic_health": 1})
]), tier_role="trap", trap=True)

# NEGOTIATION SKILL (19)
dim = "negotiation_skill"
q(dim, "scenario", "Scene negotiation with a new partner. Your approach:", opts([
    ("Systematic: discuss experience levels, hard/soft limits for both sides, desires, safewords, check-in protocols, aftercare needs, any medical/psychological considerations — all before anything physical happens", {"negotiation_skill": 5}),
    ("Thorough: limits, safewords, major interests, aftercare", {"negotiation_skill": 4}),
    ("Basic: 'What are you into? Any hard limits?'", {"negotiation_skill": 3}),
    ("Minimal: 'Let's just see how it goes'", {"negotiation_skill": 1})
]))
q(dim, "forced_choice", "Negotiation should happen:", opts([
    ("Before play (establishing boundaries), during play (check-ins), AND after play (debriefs) — it's a continuous process, not a one-time conversation", {"negotiation_skill": 5}),
    ("Primarily before, with check-ins during", {"negotiation_skill": 4}),
    ("Once before playing — then it's established", {"negotiation_skill": 3}),
    ("Organically — formal negotiation kills spontaneity", {"negotiation_skill": 1})
]))
q(dim, "behavioral_recall", "How confident are you in your ability to negotiate a complex scene that involves multiple types of play, risk management, and emotional processing?", opts([
    ("Very — I can design and negotiate sophisticated scenes that account for physical safety, emotional risk, and interpersonal dynamics", {"negotiation_skill": 5}),
    ("Fairly — I can handle most negotiations competently", {"negotiation_skill": 4}),
    ("Somewhat — for simpler scenes", {"negotiation_skill": 3}),
    ("Not confident — I'm still learning", {"negotiation_skill": 1})
]), cg="ns_behavioral")
q(dim, "scenario", "Mid-scene, the energy shifts and you want to do something not pre-negotiated. You:", opts([
    ("Pause the action: 'I'd like to introduce X. Is that on your yes list? If not, let's talk about it before I proceed.' Real-time negotiation IS possible without killing the mood", {"negotiation_skill": 5}),
    ("Ask permission: 'Can I try something new?'", {"negotiation_skill": 4}),
    ("Proceed cautiously and watch their reaction", {"negotiation_skill": 2}),
    ("Do it — we negotiated the general territory", {"negotiation_skill": 1})
]))
q(dim, "forced_choice", "The skill of negotiation in D/s:", opts([
    ("Is itself an erotic act — thorough negotiation builds anticipation, reveals desires, and demonstrates care. It's foreplay with purpose", {"negotiation_skill": 5}),
    ("Is necessary and can be enjoyable", {"negotiation_skill": 4}),
    ("Is necessary but clinical — get it done and get to the fun part", {"negotiation_skill": 3}),
    ("Is a buzzkill — the less negotiation, the more spontaneous", {"negotiation_skill": 1})
]))
q(dim, "temporal", "How have your negotiation skills improved over time?", opts([
    ("Dramatically — I now negotiate with a sophistication that accounts for psychological, physical, and relational dimensions. Early negotiations were naive by comparison", {"negotiation_skill": 5}),
    ("Significantly — experience has made me much more thorough", {"negotiation_skill": 4}),
    ("Somewhat — I've gotten better", {"negotiation_skill": 3}),
    ("Not much", {"negotiation_skill": 1})
]), cg="ns_temporal")

# AFTERCARE PRACTICE (17)
dim = "aftercare_practice"
q(dim, "scenario", "After an intense scene, your aftercare protocol:", opts([
    ("Is planned in advance and customized: physical care (blankets, water, food), emotional care (words of affirmation, processing), temporal care (staying together, not rushing). I also plan for delayed drop", {"aftercare_practice": 5}),
    ("Covers the basics well — holding, hydration, check-in", {"aftercare_practice": 4}),
    ("Is brief — a quick cuddle and we're good", {"aftercare_practice": 3}),
    ("Isn't formalized — we just do whatever feels right", {"aftercare_practice": 1})
]))
q(dim, "forced_choice", "Top drop (emotional crash experienced by the dominant/top partner) is:", opts([
    ("Real, important, and something I actively plan for — the person causing pain or holding authority also needs care after", {"aftercare_practice": 5}),
    ("Something I'm aware of — I check in with tops/Doms after", {"aftercare_practice": 4}),
    ("I've heard of it but haven't experienced or planned for it", {"aftercare_practice": 3}),
    ("Not something I believe in — the top doesn't need aftercare", {"aftercare_practice": 1})
]))
q(dim, "behavioral_recall", "How specific are your aftercare plans/discussions?", opts([
    ("Very — I know exactly what I need (type of touch, specific words, how long, what foods/drinks), AND I ask partners the same level of detail", {"aftercare_practice": 5}),
    ("Fairly — I communicate the basics", {"aftercare_practice": 4}),
    ("General — 'let's cuddle after'", {"aftercare_practice": 3}),
    ("No specific plans", {"aftercare_practice": 1})
]), cg="ap_behavioral")
q(dim, "temporal", "Sub drop / top drop days later — how do you manage it?", opts([
    ("Proactive: pre-arranged check-in texts, self-care protocols, partner awareness. I plan for the possibility before the scene happens", {"aftercare_practice": 5}),
    ("I recognize it and reach out for support when it happens", {"aftercare_practice": 4}),
    ("I know it happens but don't specifically prepare", {"aftercare_practice": 3}),
    ("Delayed effects haven't been an issue for me", {"aftercare_practice": 1})
]), cg="ap_temporal")
q(dim, "scenario", "Your partner says 'I don't need aftercare.' You:", opts([
    ("Respect their self-knowledge AND stay observant — some people genuinely need less, but I'll still check in because drop can surprise even experienced players", {"aftercare_practice": 5}),
    ("Accept it but remain attentive", {"aftercare_practice": 4}),
    ("Take them at their word completely", {"aftercare_practice": 3}),
    ("Agree — aftercare is optional", {"aftercare_practice": 1})
]))
q(dim, "forced_choice", "Aftercare supplies (blanket, water, snacks, favorite comfort item) prepared BEFORE the scene:", opts([
    ("Always — preparation IS care. Having everything ready shows forethought and respect for the vulnerability ahead", {"aftercare_practice": 5}),
    ("Usually — I think about it beforehand", {"aftercare_practice": 4}),
    ("Sometimes — if I remember", {"aftercare_practice": 3}),
    ("Never — we figure it out after", {"aftercare_practice": 1})
]))

# Fill remaining with cross-cutting questions
q("lifestyle_vs_bedroom", "forced_choice", "The phrase 'this is who we are, not what we do':", opts([
    ("Perfectly describes my relationship to D/s — it's an identity, not a hobby", {"lifestyle_vs_bedroom": 5}),
    ("Resonates — it's more than play but I hold it loosely", {"lifestyle_vs_bedroom": 4}),
    ("Doesn't apply — D/s is something I do, not something I am", {"lifestyle_vs_bedroom": 2}),
    ("Sounds cultish", {"lifestyle_vs_bedroom": 1})
]), tier_role="consistency_check", cg="lvb_core")

q("protocol_depth", "scenario", "Public protocols (subtle D/s signals in vanilla settings — sitting position, ordering for your partner, holding doors in a specific way):", opts([
    ("Are delicious — maintaining the dynamic visibly but invisibly in public keeps us connected all day", {"protocol_depth": 5}),
    ("Are fun — I enjoy subtle signals in public", {"protocol_depth": 4}),
    ("Are unnecessary — save it for home", {"protocol_depth": 2}),
    ("Make me nervous — what if someone notices?", {"protocol_depth": 1})
]))

q("service_orientation_depth", "scenario", "Your Dominant is sick. You:", opts([
    ("Shift into full caretaker mode — soup, medicine, comfort, entertainment, managing their schedule. My service adapts to their need, and right now they need nursing, not kneeling", {"service_orientation_depth": 5}),
    ("Take care of them naturally — service doesn't stop for illness", {"service_orientation_depth": 4}),
    ("Pause the dynamic and just be partners", {"service_orientation_depth": 2}),
    ("I'd take care of them the way I'd take care of anyone — D/s doesn't apply here", {"service_orientation_depth": 1})
]))

q("authority_exchange_comfort", "scenario", "Your Dominant wants input on a major life decision (career change, relocation, large purchase). You:", opts([
    ("Provide my input honestly and thoroughly, then accept their final decision — that's how authority exchange works on significant matters", {"authority_exchange_comfort": 5}),
    ("Provide input with the expectation of being heard, but accept they have final say", {"authority_exchange_comfort": 4}),
    ("Expect equal decision-making power for life-changing decisions", {"authority_exchange_comfort": 2}),
    ("These decisions should be entirely mutual — D/s doesn't apply here", {"authority_exchange_comfort": 1})
]))

q("trust_calibration", "scenario", "Your Dominant suggests an edge play activity that terrifies you but you trust them completely. You:", opts([
    ("Agree after thorough negotiation — this is where trust meets growth. My terror is real and their competence is proven", {"trust_calibration": 5}),
    ("Express my fear and discuss extensively before deciding", {"trust_calibration": 4}),
    ("Decline — trust doesn't override fear for me", {"trust_calibration": 3}),
    ("The fact that it terrifies me means it's a hard no", {"trust_calibration": 1})
]))

q("dynamic_health", "scenario", "You realize you've been using your D/s role to avoid dealing with a personal issue (hiding behind dominance to avoid vulnerability, hiding behind submission to avoid responsibility). You:", opts([
    ("Acknowledge it honestly — 'I'm using our dynamic to avoid something. I need to deal with [issue] outside the structure, not through it.' D/s should enhance growth, not replace it", {"dynamic_health": 5}),
    ("Bring it up with my partner — I need accountability", {"dynamic_health": 4}),
    ("Feel uncomfortable but continue — the dynamic is working for me", {"dynamic_health": 2}),
    ("Don't see this as a problem", {"dynamic_health": 1})
]))

q("negotiation_skill", "scenario", "Renegotiation — changing the terms of an established dynamic. Your approach:", opts([
    ("Request a formal out-of-dynamic conversation: 'I need to discuss some changes. Can we set aside time to talk as equals about what's working and what needs to shift?' Regular renegotiation is maintenance, not failure", {"negotiation_skill": 5}),
    ("Bring it up when something specific needs addressing", {"negotiation_skill": 4}),
    ("Hint at changes and hope they're noticed", {"negotiation_skill": 2}),
    ("Avoid renegotiation — we set the terms, we stick to them", {"negotiation_skill": 1})
]))

q("aftercare_practice", "scenario", "You topped a very intense scene and are now providing aftercare. Meanwhile, you're starting to feel shaky yourself. You:", opts([
    ("Say so: 'I'm feeling drop coming on too. Can we shift to mutual care?' The myth that tops don't need care is harmful. I model vulnerability by naming my own needs", {"aftercare_practice": 5}),
    ("Finish their aftercare first, then ask for mine", {"aftercare_practice": 4}),
    ("Push through — their needs come first right now", {"aftercare_practice": 2}),
    ("Ignore my own feelings — I was the top, I don't get to be fragile", {"aftercare_practice": 1})
]))

q("lifestyle_vs_bedroom", "scenario", "Vanilla sex within a D/s relationship — sometimes just being two people having sex without any power dynamic:", opts([
    ("Feels disorienting — the absence of the dynamic makes sex feel flat for me", {"lifestyle_vs_bedroom": 5}),
    ("Is fine occasionally — variety includes turning down the D/s intensity", {"lifestyle_vs_bedroom": 4}),
    ("Is my default — D/s enhances but isn't required", {"lifestyle_vs_bedroom": 2}),
    ("Is preferred most of the time", {"lifestyle_vs_bedroom": 1})
]))

q("trust_calibration", "forced_choice", "Rebuilding trust after a violation in D/s:", opts([
    ("Is possible but requires specific work: acknowledgment, accountability, changed behavior over time, and gradual re-extension of authority that was earned back, not assumed", {"trust_calibration": 5}),
    ("Is possible with honest conversation and time", {"trust_calibration": 4}),
    ("Is very difficult — once broken, trust barely returns", {"trust_calibration": 3}),
    ("Is impossible — one strike and you're out", {"trust_calibration": 1})
]))

q("dynamic_health", "forced_choice", "Red flags in a D/s dynamic — signs that something is unhealthy:", opts([
    ("I can identify multiple: isolation from support systems, punishment for using safewords, refusing renegotiation, using authority to control beyond consent, emotional manipulation framed as dominance, shaming limits", {"dynamic_health": 5}),
    ("I know the major ones — isolation, safeword violations, refusing limits", {"dynamic_health": 4}),
    ("I'd recognize extreme cases", {"dynamic_health": 3}),
    ("I'm not sure what would constitute a red flag in D/s specifically", {"dynamic_health": 1})
]))

q("negotiation_skill", "behavioral_recall", "Have you ever walked away from a potential D/s partner because the negotiation revealed incompatibilities or red flags?", opts([
    ("Yes — the negotiation process is partly a screening tool. Incompatible limits, resistance to discussion, or concerning attitudes all show up in negotiation, and I've walked away based on what I learned", {"negotiation_skill": 5}),
    ("Yes — I've declined to play based on negotiation concerns", {"negotiation_skill": 4}),
    ("I've had concerns but played anyway", {"negotiation_skill": 2}),
    ("Negotiation hasn't revealed issues for me", {"negotiation_skill": 1})
]), cg="ns_behavioral")

q("protocol_depth", "forced_choice", "Ritual vs. routine in D/s:", opts([
    ("I know the difference: ritual has intentional meaning behind each element; routine is habit. The best D/s transforms routine into ritual through intention", {"protocol_depth": 5}),
    ("I try to keep rituals meaningful rather than mindless", {"protocol_depth": 4}),
    ("They blend together for me", {"protocol_depth": 3}),
    ("I don't differentiate — rules are rules", {"protocol_depth": 1})
]))

q("service_orientation_depth", "forced_choice", "The distinction between service submission and codependency:", opts([
    ("Is critical and I think about it regularly: service submission is CHOSEN from a place of strength and can be withdrawn; codependency is compulsive and driven by fear. My service comes from abundance, not emptiness", {"service_orientation_depth": 5}),
    ("Is important — I try to make sure my service comes from a healthy place", {"service_orientation_depth": 4}),
    ("Is blurry — I'm not always sure which drives me", {"service_orientation_depth": 2}),
    ("Is irrelevant — if it looks like service, it IS service", {"service_orientation_depth": 1})
]), tier_role="trap", trap=True)

q("authority_exchange_comfort", "forced_choice", "The scariest part of authority exchange is:", opts([
    ("For the submissive: truly surrendering, not performing surrender. For the Dominant: truly accepting responsibility, not playing at authority. Both sides require courage", {"authority_exchange_comfort": 5}),
    ("The vulnerability on both sides", {"authority_exchange_comfort": 4}),
    ("Giving up control as the submissive", {"authority_exchange_comfort": 3}),
    ("The responsibility as the Dominant", {"authority_exchange_comfort": 2})
]))

print(f"Total questions: {len(questions)}")
with open("/Users/user/personal/sb/trueassess/priv/question_bank/power_exchange_depth.json", "w") as f:
    json.dump(questions, f, indent=2)
print("Written power_exchange_depth.json")
