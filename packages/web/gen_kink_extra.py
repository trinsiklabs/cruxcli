import json

with open("/Users/user/personal/sb/trueassess/priv/question_bank/kink_exploration.json") as f:
    questions = json.load(f)

uid_counter = len(questions) + 1

def q(dimension, qtype, text, options, tier_role="core", trap=False, cg=None, opacity=0.6, cross=None, tags=None):
    global uid_counter
    uid = f"ke_{uid_counter:03d}"
    uid_counter += 1
    entry = {
        "uid": uid,
        "assessment_id": "kink_exploration",
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
        "content_categories": ["kink", "sexuality"],
        "depth_tier": "deep",
        "tier_role": tier_role,
        "tags": tags or ["nsfw", "kink", dimension]
    }
    questions.append(entry)

def opts(texts_scores):
    return [{"id": chr(97+i), "text": t, "scores": s} for i, (t, s) in enumerate(texts_scores)]

# More kink_curiosity
q("kink_curiosity", "scenario", "A documentary about a kink you find personally unappealing is available. You:", opts([
    ("Watch it — understanding human sexuality broadly makes me a better partner and person", {"kink_curiosity": 5}),
    ("Might watch it — I'm curious about the psychology", {"kink_curiosity": 4}),
    ("Skip it — why watch something I don't enjoy?", {"kink_curiosity": 2}),
    ("Actively avoid it — some things I don't want in my head", {"kink_curiosity": 1})
]))

q("kink_curiosity", "forced_choice", "Your approach to kink education is:", opts([
    ("Proactive and systematic — I seek out workshops, books, and experienced mentors", {"kink_curiosity": 5}),
    ("Interested — I'll read articles and watch educational content", {"kink_curiosity": 4}),
    ("Reactive — I learn when I encounter something new", {"kink_curiosity": 3}),
    ("Passive — I don't actively seek kink education", {"kink_curiosity": 1})
]))

q("kink_curiosity", "behavioral_recall", "How many different kink-related subreddits, forums, or Discord servers have you participated in?", opts([
    ("5+ — I'm active across multiple communities covering different interests", {"kink_curiosity": 5}),
    ("2-4 — a few that match my interests", {"kink_curiosity": 4}),
    ("1 — one main community", {"kink_curiosity": 3}),
    ("None", {"kink_curiosity": 1})
]))

q("kink_curiosity", "scenario", "You discover that a kink you dismissed years ago actually has a sophisticated psychological framework behind it. You:", opts([
    ("Revisit it with fresh eyes — my earlier dismissal was based on ignorance, and I'm always willing to reconsider", {"kink_curiosity": 5}),
    ("Read about the framework — I'm intellectually interested even if it's still not for me", {"kink_curiosity": 4}),
    ("Note it but don't pursue it", {"kink_curiosity": 3}),
    ("My initial reaction was correct — I don't need a framework to know what I don't like", {"kink_curiosity": 1})
]))

q("kink_curiosity", "temporal", "Your kink 'vocabulary' — the number of distinct kinks you could name, describe, and explain the appeal of:", opts([
    ("Extensive — I could give a seminar on dozens of kinks, including ones I don't practice", {"kink_curiosity": 5}),
    ("Solid — I know my way around most common and many uncommon kinks", {"kink_curiosity": 4}),
    ("Basic — I know the popular ones", {"kink_curiosity": 3}),
    ("Limited — I know a few terms", {"kink_curiosity": 1})
]))

# More experience_breadth
q("experience_breadth", "behavioral_recall", "Role play scenarios you've actually done (teacher/student, boss/employee, stranger, captor/captive, daddy/little, etc.):", opts([
    ("Multiple distinct scenarios — role play is a rich vein I've mined thoroughly", {"experience_breadth": 5}),
    ("2-3 scenarios — I enjoy role play in specific forms", {"experience_breadth": 4}),
    ("One scenario, tried once or twice", {"experience_breadth": 3}),
    ("None — role play doesn't appeal to me", {"experience_breadth": 1})
]))

q("experience_breadth", "scenario", "Impact implements you've personally experienced (hand, paddle, flogger, crop, cane, belt, strap, wooden spoon, etc.):", opts([
    ("6+ different implements — I've explored the full spectrum of impact sensation", {"experience_breadth": 5}),
    ("3-5 — a good range", {"experience_breadth": 4}),
    ("1-2 — usually just hands", {"experience_breadth": 3}),
    ("None", {"experience_breadth": 1})
]))

q("experience_breadth", "forced_choice", "Group sex, threesomes, or multi-partner play:", opts([
    ("Experienced and comfortable — I've navigated the complexity of multiple-person dynamics", {"experience_breadth": 5}),
    ("Some experience — I've tried it at least once", {"experience_breadth": 4}),
    ("Curious but no experience", {"experience_breadth": 3}),
    ("Not interested", {"experience_breadth": 1})
]))

q("experience_breadth", "behavioral_recall", "Anal play experience (plugs, penetration, rimming, training):", opts([
    ("Extensive — I've explored this area thoroughly and know my body's responses well", {"experience_breadth": 5}),
    ("Moderate — I've tried several things and know what I like", {"experience_breadth": 4}),
    ("Minimal — tried it once or twice", {"experience_breadth": 3}),
    ("None", {"experience_breadth": 1})
]))

q("experience_breadth", "scenario", "Your experience with different types of power exchange (casual bedroom D/s, structured scenes, lifestyle dynamic, master/slave, service-oriented, protocol-heavy):", opts([
    ("Multiple types — I understand the differences from lived experience", {"experience_breadth": 5}),
    ("2-3 types — I've experienced enough to know my preference", {"experience_breadth": 4}),
    ("One type — my experience has been narrow but meaningful", {"experience_breadth": 3}),
    ("None — power exchange is theoretical for me", {"experience_breadth": 1})
]))

q("experience_breadth", "temporal", "Different venues for kink play you've experienced (home, hotel, dungeon/playspace, outdoors, play party, club):", opts([
    ("4+ — I've played in many different environments", {"experience_breadth": 5}),
    ("2-3 — I've branched out from home", {"experience_breadth": 4}),
    ("Home only", {"experience_breadth": 3}),
    ("No kink-specific venues", {"experience_breadth": 1})
]))

q("experience_breadth", "forced_choice", "Your experience with sex toys beyond vibrators (prostate toys, fucking machines, chastity devices, electrostim, e-stim, suction devices):", opts([
    ("Extensive — I've explored a wide range of specialized toys", {"experience_breadth": 5}),
    ("Some — I own a few specialty items beyond basics", {"experience_breadth": 4}),
    ("Basic — vibrators and maybe one other thing", {"experience_breadth": 3}),
    ("None or just the basics", {"experience_breadth": 1})
]))

# More boundary_clarity
q("boundary_clarity", "scenario", "You're in sub drop (emotional crash after an intense scene) and your partner wants to have a serious conversation about the relationship. You:", opts([
    ("Say 'I'm in drop right now and I can't have this conversation. Let's schedule it for tomorrow when I'm regulated' — I know my emotional states and protect my boundaries even when vulnerable", {"boundary_clarity": 5}),
    ("Try to engage but name that I'm not in a great place", {"boundary_clarity": 4}),
    ("Have the conversation even though I know I'm compromised", {"boundary_clarity": 2}),
    ("I don't recognize sub drop when it's happening", {"boundary_clarity": 1})
]))

q("boundary_clarity", "forced_choice", "The 'frenzy' — when someone new to kink wants to try everything immediately. If this describes you:", opts([
    ("I went through it and learned to pace myself — now I advocate for measured exploration", {"boundary_clarity": 5}),
    ("I experienced it and it taught me about my boundaries the hard way", {"boundary_clarity": 4}),
    ("I'm in it right now — everything is exciting and I want more", {"boundary_clarity": 2}),
    ("I've always been measured about exploration", {"boundary_clarity": 3})
]))

q("boundary_clarity", "behavioral_recall", "Have you ever done something sexually that you didn't want to do because you felt pressured (by a partner, by expectations, by frenzy)?", opts([
    ("Yes, early on — and that experience taught me to establish and enforce clear boundaries. I won't repeat it", {"boundary_clarity": 5}),
    ("Yes — I've learned from it but it took time", {"boundary_clarity": 4}),
    ("Yes — and I'm still working on saying no", {"boundary_clarity": 2}),
    ("Regularly — I struggle to assert my boundaries", {"boundary_clarity": 1})
]), tier_role="trap", trap=True, cg="boundary_behavioral")

q("boundary_clarity", "scenario", "A hard limit for you also happens to be something your partner deeply desires. You:", opts([
    ("Hold the line firmly and without guilt — 'I understand this matters to you, AND it's a hard limit for me. That's not going to change, and I need you to respect that'", {"boundary_clarity": 5}),
    ("Maintain the limit but feel some guilt about disappointing them", {"boundary_clarity": 4}),
    ("Waver — maybe I could try it just once for them", {"boundary_clarity": 2}),
    ("Give in — their desire outweighs my discomfort", {"boundary_clarity": 1})
]))

q("boundary_clarity", "forced_choice", "Your response to the phrase 'limits are meant to be pushed':", opts([
    ("SOFT limits can be explored with consent and care. HARD limits are non-negotiable. The phrase is only valid for the former", {"boundary_clarity": 5}),
    ("True for soft limits, false for hard limits", {"boundary_clarity": 4}),
    ("Generally true — growth happens at the edges", {"boundary_clarity": 2}),
    ("True — you don't grow without pushing past comfort", {"boundary_clarity": 1})
]))

# More communication_about_kink
q("communication_about_kink", "scenario", "Your partner's communication during sex is very different from yours — they're silent and you're vocal (or vice versa). You:", opts([
    ("Name the difference, explore what it means for each of you, and find ways to bridge it — 'Your silence reads as disengagement to me; can we talk about what's happening for you?'", {"communication_about_kink": 5}),
    ("Adapt somewhat — I learn to read their non-verbal cues", {"communication_about_kink": 4}),
    ("Accept the difference without addressing it", {"communication_about_kink": 2}),
    ("Feel disconnected but don't bring it up", {"communication_about_kink": 1})
]))

q("communication_about_kink", "behavioral_recall", "Have you ever written an explicit letter, text, or email to a partner describing in detail what you want to do to them or want done to you?", opts([
    ("Many times — written communication lets me be more precise and explicit than I might be verbally", {"communication_about_kink": 5}),
    ("A few times — it's effective foreplay and communication", {"communication_about_kink": 4}),
    ("Once or twice", {"communication_about_kink": 3}),
    ("Never — I can't write that stuff down", {"communication_about_kink": 1})
]))

q("communication_about_kink", "scenario", "Sexting and explicit digital communication in a D/s or kink context:", opts([
    ("Is a regular part of how I maintain connection and express desire — I'm fluent in digital kink communication", {"communication_about_kink": 5}),
    ("I enjoy it and participate actively", {"communication_about_kink": 4}),
    ("Occasional — it's fun but not a main channel", {"communication_about_kink": 3}),
    ("Uncomfortable — explicit texts feel too permanent and risky", {"communication_about_kink": 1})
]))

q("communication_about_kink", "forced_choice", "When your partner does something in bed you love, you:", opts([
    ("Tell them exactly what it was and why it worked — positive reinforcement is how good sex gets better", {"communication_about_kink": 5}),
    ("Make enthusiastic sounds and mention it afterward", {"communication_about_kink": 4}),
    ("Show my enjoyment non-verbally in the moment", {"communication_about_kink": 3}),
    ("Don't say anything — they should know from my reactions", {"communication_about_kink": 1})
]))

q("communication_about_kink", "temporal", "Your ability to give specific sexual feedback has:", opts([
    ("Improved dramatically — I'm now precise about what I want, what works, and what doesn't", {"communication_about_kink": 5}),
    ("Gotten better with practice", {"communication_about_kink": 4}),
    ("Stayed about the same", {"communication_about_kink": 3}),
    ("Not developed — I still struggle to give sexual feedback", {"communication_about_kink": 1})
]))

# More shame_vs_acceptance  
q("shame_vs_acceptance", "scenario", "You realize you're aroused by something that contradicts your values or politics. You:", opts([
    ("Accept the complexity — arousal and ethics operate on different channels, and mature sexuality holds both without resolving the tension", {"shame_vs_acceptance": 5}),
    ("Feel conflicted but give myself grace — desire isn't chosen", {"shame_vs_acceptance": 4}),
    ("Try to redirect the arousal to something more 'acceptable'", {"shame_vs_acceptance": 2}),
    ("Spiral into shame — how can I want this?", {"shame_vs_acceptance": 1})
]))

q("shame_vs_acceptance", "forced_choice", "Kink identity in your daily life:", opts([
    ("Is integrated — being kinky is part of who I am, not a secret I keep", {"shame_vs_acceptance": 5}),
    ("Is known by close friends — I'm selectively open", {"shame_vs_acceptance": 4}),
    ("Is carefully compartmentalized — work/family me and kink me don't mix", {"shame_vs_acceptance": 2}),
    ("Is a source of anxiety — I fear discovery constantly", {"shame_vs_acceptance": 1})
]))

q("shame_vs_acceptance", "behavioral_recall", "How do you feel about your body in kink contexts (nudity, exposure, being seen in vulnerable positions)?", opts([
    ("Accepting and present — my body is the vehicle for this experience and I inhabit it fully", {"shame_vs_acceptance": 5}),
    ("Mostly comfortable — some self-consciousness but it doesn't stop me", {"shame_vs_acceptance": 4}),
    ("Anxious — body shame gets louder in kink contexts", {"shame_vs_acceptance": 2}),
    ("Very uncomfortable — vulnerability amplifies every insecurity", {"shame_vs_acceptance": 1})
]))

q("shame_vs_acceptance", "scenario", "You have a kink that, if described to someone unfamiliar, sounds 'weird' or 'gross.' Your relationship with this kink:", opts([
    ("Is one of full ownership — I can explain what I enjoy and why without defensiveness or shame", {"shame_vs_acceptance": 5}),
    ("Is mostly comfortable — I accept it even if I don't broadcast it", {"shame_vs_acceptance": 4}),
    ("Is complicated — I enjoy it but hate that I enjoy it", {"shame_vs_acceptance": 2}),
    ("Is tormented — I wish I could stop wanting it", {"shame_vs_acceptance": 1})
]))

q("shame_vs_acceptance", "temporal", "The most shame you've ever felt about a sexual desire — how long ago was that, and how do you feel about it now?", opts([
    ("Years ago — and I've done the work to fully accept that desire. The shame is gone", {"shame_vs_acceptance": 5}),
    ("A while ago — I'm much better about it now but echoes remain", {"shame_vs_acceptance": 4}),
    ("Recently — I'm actively struggling with acceptance", {"shame_vs_acceptance": 2}),
    ("Right now — there are desires I'm deeply ashamed of currently", {"shame_vs_acceptance": 1})
]))

# More safety_consciousness
q("safety_consciousness", "scenario", "Rope bondage: you're about to suspend someone (or be suspended). Your safety checklist:", opts([
    ("Extensive: load-bearing points checked, backup lines in place, EMT shears accessible, circulation check protocol, hard point rated and inspected, spotter present, descent plan rehearsed", {"safety_consciousness": 5}),
    ("Covers the basics: good hardware, safety shears, monitoring", {"safety_consciousness": 4}),
    ("Minimal: the rope seems strong and my partner says they're fine", {"safety_consciousness": 2}),
    ("I wouldn't think through a formal checklist", {"safety_consciousness": 1})
]))

q("safety_consciousness", "forced_choice", "Community accountability — if someone in your kink community is known to violate consent, you:", opts([
    ("Actively support accountability processes, warn potential partners, and won't play at events that don't address consent violations", {"safety_consciousness": 5}),
    ("Avoid them and warn people I'm close to", {"safety_consciousness": 4}),
    ("Stay out of it — community drama isn't my business", {"safety_consciousness": 2}),
    ("I'm not connected to a community", {"safety_consciousness": 1})
]))

q("safety_consciousness", "behavioral_recall", "How do you vet a new play partner before engaging in kink with them?", opts([
    ("Thorough: multiple conversations, references from mutual connections, negotiation over several meetings, start with low-risk play and build", {"safety_consciousness": 5}),
    ("Significant: at least one extended conversation about experience and limits, check with mutual friends if possible", {"safety_consciousness": 4}),
    ("Basic: one conversation, establish safewords, see how it goes", {"safety_consciousness": 3}),
    ("Minimal vetting — if there's chemistry, we play", {"safety_consciousness": 1})
]))

q("safety_consciousness", "scenario", "Your partner asks to remove the safeword system for a scene — 'I want it to feel real.' You:", opts([
    ("No — safewords can be invisible (tap codes, held objects) but some consent system MUST exist. Removing safety is removing consent infrastructure", {"safety_consciousness": 5}),
    ("No — but I'll find a less obtrusive system", {"safety_consciousness": 4}),
    ("Maybe — if I know them very well and I'm confident I can read them", {"safety_consciousness": 2}),
    ("Sure — real surrender means no escape hatch", {"safety_consciousness": 1})
]), tier_role="trap", trap=True)

q("safety_consciousness", "forced_choice", "Aftercare — structured post-scene care (blankets, water, holding, checking in, debriefing):", opts([
    ("Non-negotiable and planned in advance — aftercare is part of the scene, not optional. I also plan for subdrop/topdrop that might come days later", {"safety_consciousness": 5}),
    ("Important — I always do aftercare though it may not be formally planned", {"safety_consciousness": 4}),
    ("Sometimes — depends on the intensity", {"safety_consciousness": 3}),
    ("Rarely — we're adults, not children who need coddling after sex", {"safety_consciousness": 1})
]))

q("safety_consciousness", "temporal", "Have you ever called a safeword or had a partner call one? What happened?", opts([
    ("Yes — and it was handled well: immediate stop, care, debrief, no guilt or shame. The system worked exactly as intended", {"safety_consciousness": 5}),
    ("Yes — it was handled but with some awkwardness", {"safety_consciousness": 4}),
    ("Yes — it was handled badly (guilt, dismissal, resentment)", {"safety_consciousness": 2}),
    ("No — I've never needed to / I don't use safewords", {"safety_consciousness": 1})
]))

# More partner_exploration_style
q("partner_exploration_style", "scenario", "Your partner says 'I want to explore but I don't know what I want.' You:", opts([
    ("Create a structured exploration process — questionnaires, educational content together, low-stakes experiments, regular check-ins about what resonated", {"partner_exploration_style": 5}),
    ("Suggest some things and see what catches their interest", {"partner_exploration_style": 4}),
    ("Wait for them to figure out what they want", {"partner_exploration_style": 2}),
    ("Not sure how to help — they need to know what they want first", {"partner_exploration_style": 1})
]))

q("partner_exploration_style", "forced_choice", "The best kink education for a new partner is:", opts([
    ("Experiential learning with extensive support: try a little, debrief a lot, adjust, try more", {"partner_exploration_style": 5}),
    ("Reading and research first, then careful practice", {"partner_exploration_style": 4}),
    ("Jump in and learn by doing", {"partner_exploration_style": 3}),
    ("They should educate themselves before playing with me", {"partner_exploration_style": 1})
]))

q("partner_exploration_style", "behavioral_recall", "How do you respond when a partner's kink skills are underdeveloped (clumsy with rope, unsure with impact, poor pacing)?", opts([
    ("With patience and specific, encouraging feedback — 'That was good, and if you adjust the angle slightly...' I enjoy teaching", {"partner_exploration_style": 5}),
    ("Gently redirect — show them what works better", {"partner_exploration_style": 4}),
    ("Tolerate it and hope they improve", {"partner_exploration_style": 2}),
    ("Get frustrated — why play at something you're not skilled in?", {"partner_exploration_style": 1})
]))

q("partner_exploration_style", "scenario", "You and your partner have been doing the same types of play for a year. You:", opts([
    ("Proactively introduce variation — 'What if we tried the same dynamic but with different implements/location/intensity?'", {"partner_exploration_style": 5}),
    ("Suggest something new when the mood strikes", {"partner_exploration_style": 4}),
    ("Am content with what works", {"partner_exploration_style": 3}),
    ("Haven't noticed the repetition", {"partner_exploration_style": 1})
]))

q("partner_exploration_style", "forced_choice", "When a scene doesn't go as planned (equipment failure, emotional trigger, physical limit hit), you:", opts([
    ("Treat it as data — what did we learn? How do we adjust? Failed scenes teach more than perfect ones", {"partner_exploration_style": 5}),
    ("Debrief and move on — it happens", {"partner_exploration_style": 4}),
    ("Feel discouraged", {"partner_exploration_style": 2}),
    ("Avoid trying that thing again", {"partner_exploration_style": 1})
]))

# Cross-cutting triangulation
q("kink_curiosity", "scenario", "Your 'Didn't Know That Was a Thing' reaction over the years — the number of times you've discovered a kink you never imagined:", opts([
    ("Happens regularly and I love it — the vastness of human sexuality is endlessly surprising", {"kink_curiosity": 5}),
    ("Has happened many times — each discovery is interesting", {"kink_curiosity": 4}),
    ("A few times — mostly early in my exploration", {"kink_curiosity": 3}),
    ("Rarely — I feel like I've heard it all", {"kink_curiosity": 2})
]))

q("experience_breadth", "scenario", "Sensory deprivation (blindfolds, hoods, earplugs, sensory deprivation tanks) as kink:", opts([
    ("Experienced and find it profound — removing senses rewires the entire experience", {"experience_breadth": 5}),
    ("Have tried at least blindfolds and enjoyed the effect", {"experience_breadth": 4}),
    ("Haven't tried but intrigued", {"experience_breadth": 3}),
    ("Sounds claustrophobic", {"experience_breadth": 1})
]))

q("boundary_clarity", "temporal", "How confident are you that you could articulate your complete yes/no/maybe list right now?", opts([
    ("Very — I maintain a mental (or physical) list that I review and update", {"boundary_clarity": 5}),
    ("Fairly — I know the major categories, might miss some edge cases", {"boundary_clarity": 4}),
    ("Partially — I know my hard no's but the rest is fuzzy", {"boundary_clarity": 3}),
    ("Not confident — I'd need to think about it for a while", {"boundary_clarity": 1})
]))

q("communication_about_kink", "scenario", "A new partner asks 'What are you into?' Your response:", opts([
    ("Detailed, specific, and comfortable: I name activities, dynamics, roles, and can describe what I enjoy about each", {"communication_about_kink": 5}),
    ("Clear but somewhat general: 'I enjoy power exchange, impact play, and bondage — happy to get more specific'", {"communication_about_kink": 4}),
    ("Vague: 'I'm pretty open-minded' or 'I like to be adventurous'", {"communication_about_kink": 2}),
    ("Deflecting: 'Oh, you know, the usual stuff'", {"communication_about_kink": 1})
]))

q("shame_vs_acceptance", "forced_choice", "Kink at the intersection of identity — being kinky is:", opts([
    ("As fundamental as my orientation — it's part of my sexual identity, not just something I do", {"shame_vs_acceptance": 5}),
    ("A significant part of who I am sexually", {"shame_vs_acceptance": 4}),
    ("An interest — important but not definitional", {"shame_vs_acceptance": 3}),
    ("A behavior — not an identity", {"shame_vs_acceptance": 1})
]))

q("safety_consciousness", "scenario", "You witness a consent violation at a play event. You:", opts([
    ("Report to event staff immediately AND check on the affected person AND document what I saw — consent violations are everyone's business", {"safety_consciousness": 5}),
    ("Report to event staff and check on the person involved", {"safety_consciousness": 4}),
    ("Mention it to someone in charge later", {"safety_consciousness": 3}),
    ("Stay out of it — I don't know the full context", {"safety_consciousness": 1})
]))

q("partner_exploration_style", "scenario", "Building a shared toy collection with a partner — choosing implements, restraints, and accessories together:", opts([
    ("Is one of my favorite relationship activities — shopping for play equipment together builds anticipation and reveals desires", {"partner_exploration_style": 5}),
    ("Is fun — I enjoy picking things out together", {"partner_exploration_style": 4}),
    ("Is fine — I'll contribute opinions", {"partner_exploration_style": 3}),
    ("Is unnecessary — I already own what I need", {"partner_exploration_style": 1})
]))

# Additional cross-dimensional
q("kink_curiosity", "forced_choice", "Kink and creativity are:", opts([
    ("Deeply linked — kink IS creative expression. Every scene is co-created art", {"kink_curiosity": 5}),
    ("Connected — good kink requires imagination", {"kink_curiosity": 4}),
    ("Separate — kink is about desire, not creativity", {"kink_curiosity": 2}),
    ("Unrelated", {"kink_curiosity": 1})
]))

q("experience_breadth", "forced_choice", "Your experience with kink across different relationship structures (monogamous, open, polyamorous, casual):", opts([
    ("Multiple structures — each taught me different things about how kink functions in relationships", {"experience_breadth": 5}),
    ("Two structures — I've experienced kink in different contexts", {"experience_breadth": 4}),
    ("One structure only", {"experience_breadth": 3}),
    ("I haven't had kink relationships", {"experience_breadth": 1})
]))

q("boundary_clarity", "scenario", "Someone tells you 'I don't have hard limits.' You think:", opts([
    ("That's a sign of insufficient self-knowledge, not impressive openness — everyone has limits, and not knowing yours means you can't communicate them", {"boundary_clarity": 5}),
    ("They probably haven't explored enough to know where their edges are", {"boundary_clarity": 4}),
    ("Some people genuinely are that open", {"boundary_clarity": 2}),
    ("Impressive — they must be very experienced", {"boundary_clarity": 1})
]), tier_role="trap", trap=True)

q("communication_about_kink", "behavioral_recall", "How comfortable are you discussing your sexual trauma history with a kink partner (if applicable)?", opts([
    ("I share relevant history before play — it's safety-critical information and I'm practiced at disclosing without oversharing", {"communication_about_kink": 5}),
    ("I share the basics — enough to keep play safe", {"communication_about_kink": 4}),
    ("I struggle to bring it up but know I should", {"communication_about_kink": 2}),
    ("I don't disclose — it's too vulnerable", {"communication_about_kink": 1})
]), tags=["nsfw", "kink", "communication_about_kink", "trauma"])

q("safety_consciousness", "forced_choice", "Consent under duress — a partner agreeing to something because they fear losing you, want to please you, or feel pressured:", opts([
    ("Is NOT valid consent — I actively watch for signs of compliance without enthusiasm, and I'd rather hear 'no' than receive reluctant 'yes'", {"safety_consciousness": 5}),
    ("Is something I try to be aware of — I check in about motivations", {"safety_consciousness": 4}),
    ("Is hard to detect — I trust their words", {"safety_consciousness": 3}),
    ("Isn't my responsibility — they're an adult who can say no", {"safety_consciousness": 1})
]))

q("partner_exploration_style", "forced_choice", "Kink mentorship — being a guide for someone less experienced:", opts([
    ("Is deeply rewarding — I take mentorship seriously and enjoy watching someone grow into their kink identity", {"partner_exploration_style": 5}),
    ("I've done it informally and enjoyed it", {"partner_exploration_style": 4}),
    ("Not my thing — I want partners at my level", {"partner_exploration_style": 2}),
    ("I'm the one who needs mentoring", {"partner_exploration_style": 1})
]))

# Consistency check questions
q("kink_curiosity", "forced_choice", "If a new kink emerged tomorrow that no one had ever practiced — something entirely novel — you would:", opts([
    ("Be among the first to research and potentially try it — pioneering is in my nature", {"kink_curiosity": 5}),
    ("Watch early adopters and consider trying it", {"kink_curiosity": 4}),
    ("Wait until it's well-established and reviewed", {"kink_curiosity": 3}),
    ("Ignore it — I have enough on my plate", {"kink_curiosity": 1})
]), tier_role="consistency_check", cg="curiosity_core")

q("experience_breadth", "forced_choice", "If you had to rate your overall kink experience on a scale, you'd honestly say:", opts([
    ("Expert — I've explored widely, deeply, and reflectively across many categories over many years", {"experience_breadth": 5}),
    ("Experienced — solid breadth with depth in key areas", {"experience_breadth": 4}),
    ("Intermediate — meaningful experience in a few areas", {"experience_breadth": 3}),
    ("Beginner — just starting or limited experience", {"experience_breadth": 1})
]), tier_role="consistency_check", cg="breadth_core")

q("boundary_clarity", "forced_choice", "Your relationship with the word 'no' in a sexual context:", opts([
    ("It's a complete sentence that I can say without guilt and receive without resentment — 'no' is the foundation that makes 'yes' meaningful", {"boundary_clarity": 5}),
    ("I can say it, though sometimes it's hard", {"boundary_clarity": 4}),
    ("I struggle with it — I feel guilty saying no to a partner", {"boundary_clarity": 2}),
    ("I rarely say no even when I should", {"boundary_clarity": 1})
]), tier_role="consistency_check", cg="boundary_core")

q("communication_about_kink", "forced_choice", "Your comfort level discussing kink is:", opts([
    ("Clinical precision meets dirty talk fluency — I can discuss any sexual topic in any register without shame", {"communication_about_kink": 5}),
    ("Very comfortable — most topics are easy for me", {"communication_about_kink": 4}),
    ("Moderate — some topics are easier than others", {"communication_about_kink": 3}),
    ("Low — sexual communication is one of my growth edges", {"communication_about_kink": 1})
]), tier_role="consistency_check", cg="comm_core")

q("safety_consciousness", "forced_choice", "Your personal safety philosophy for kink:", opts([
    ("Informed, prepared, and proactive — I study risks, maintain skills, carry supplies, and won't compromise on safety for the sake of spontaneity or intensity", {"safety_consciousness": 5}),
    ("Careful and aware — I take reasonable precautions", {"safety_consciousness": 4}),
    ("Common-sense — I don't do obviously dangerous things", {"safety_consciousness": 3}),
    ("Reactive — I deal with problems if they arise", {"safety_consciousness": 1})
]), tier_role="consistency_check", cg="safety_core")

q("partner_exploration_style", "forced_choice", "Your ideal kink partner is someone who:", opts([
    ("Matches my energy for exploration — curious, communicative, willing to try things, and invested in building our shared kink life together", {"partner_exploration_style": 5}),
    ("Is open and willing even if not as proactive as I am", {"partner_exploration_style": 4}),
    ("Has their own established kinks that happen to overlap with mine", {"partner_exploration_style": 3}),
    ("Just does what I want without needing to 'explore'", {"partner_exploration_style": 1})
]), tier_role="consistency_check", cg="partner_core")

# Additional fillers to hit 200
q("kink_curiosity", "scenario", "Edge play — activities that push against the boundary of safety (breath play, knife play, consensual non-consent). Your intellectual interest:", opts([
    ("High — even if I don't practice all of them, understanding why people seek the edge fascinates me", {"kink_curiosity": 5}),
    ("Moderate — I'm interested in some edge activities", {"kink_curiosity": 4}),
    ("Low — I respect it but don't need to understand it", {"kink_curiosity": 2}),
    ("None — edge play scares me", {"kink_curiosity": 1})
]))

q("experience_breadth", "behavioral_recall", "Chastity play (orgasm denial devices, key holding) — your experience:", opts([
    ("Experienced — I understand the psychological and physical dimensions from lived practice", {"experience_breadth": 5}),
    ("Tried it or actively interested", {"experience_breadth": 4}),
    ("Curious but no experience", {"experience_breadth": 3}),
    ("No interest", {"experience_breadth": 1})
]))

q("boundary_clarity", "scenario", "A partner pushes a soft limit during a scene — something you said was 'maybe.' In the moment it feels wrong. You:", opts([
    ("Safeword without hesitation — 'maybe' means 'only with explicit in-the-moment consent,' which wasn't given", {"boundary_clarity": 5}),
    ("Use yellow to pause and discuss", {"boundary_clarity": 4}),
    ("Endure it — I did say maybe", {"boundary_clarity": 2}),
    ("Freeze and can't communicate", {"boundary_clarity": 1})
]))

q("communication_about_kink", "scenario", "You realize you've been faking enjoyment of something your partner thinks you love. You:", opts([
    ("Come clean — 'I need to be honest: I've been performing enjoyment of X. Here's what's actually going on for me.' Hard conversation, necessary honesty", {"communication_about_kink": 5}),
    ("Gradually redirect away from it while looking for the right moment to be honest", {"communication_about_kink": 3}),
    ("Keep faking — it's too late to change the narrative", {"communication_about_kink": 1}),
    ("Hint that your interest has changed", {"communication_about_kink": 2})
]))

q("shame_vs_acceptance", "scenario", "A new study suggests that a kink you enjoy may be correlated with childhood experiences. Your response:", opts([
    ("'So what?' — the origin of a desire doesn't determine its healthiness. Lots of healthy adult behaviors have childhood roots. What matters is how it functions now", {"shame_vs_acceptance": 5}),
    ("Reflect on it without spiraling — interesting information that doesn't change my relationship with the kink", {"shame_vs_acceptance": 4}),
    ("Feel unsettled — does this mean something is wrong with me?", {"shame_vs_acceptance": 2}),
    ("Panic — this confirms my worst fears about why I want this", {"shame_vs_acceptance": 1})
]))

q("safety_consciousness", "scenario", "You're playing with a partner who goes non-verbal (deep subspace, trance state). They can't use their safeword. You:", opts([
    ("Switch to physical check-ins (hand squeezes), monitor vitals (breathing, skin color, responsiveness), and reduce intensity. If I can't get a clear check-in response, I stop", {"safety_consciousness": 5}),
    ("Check in with yes/no questions and pause if they can't respond", {"safety_consciousness": 4}),
    ("Continue but watch them carefully", {"safety_consciousness": 2}),
    ("Continue — they'd snap out of it if something was wrong", {"safety_consciousness": 1})
]))

q("partner_exploration_style", "scenario", "Your partner wants to attend a kink event together for the first time. Your preparation:", opts([
    ("Research the event, discuss expectations and boundaries, plan what we're open to and not, establish reconnection rituals, debrief extensively afterward", {"partner_exploration_style": 5}),
    ("Talk through expectations and set some ground rules", {"partner_exploration_style": 4}),
    ("Show up and see how it goes", {"partner_exploration_style": 2}),
    ("I wouldn't attend a kink event", {"partner_exploration_style": 1})
]))

print(f"Total questions: {len(questions)}")
with open("/Users/user/personal/sb/trueassess/priv/question_bank/kink_exploration.json", "w") as f:
    json.dump(questions, f, indent=2)
print("Written kink_exploration.json")
