import json

questions = []

def q(dim, qtype, text, options, tier="core", trap=False, cg=None, opacity=0.7, cross=None, tags=None):
    return {
        "dimension": dim,
        "question_type": qtype,
        "text": text,
        "options": options,
        "tier_role": tier,
        "trap": trap,
        "consistency_group": cg,
        "opacity": opacity,
        "cross_scores": cross or [],
        "universal": True,
        "adaptations_needed": [],
        "tags": tags or ["boundary_style", dim]
    }

def opts(choices):
    return [{"id": chr(97+i), "text": t, "scores": s} for i, (t, s) in enumerate(choices)]

# POROUS (25), RIGID (25), FLEXIBLE (25), ENFORCEMENT (25)

# ============================================================
# POROUS (25)
# ============================================================

questions.append(q("porous", "scenario",
    "A coworker vents about their terrible day for 45 minutes. You had plans to leave on time today. You:",
    opts([
        ("Listen as long as they need — their pain matters more than your schedule", {"porous": 5}),
        ("Listen for a bit, then gently redirect: 'I need to head out but let's talk tomorrow'", {"porous": 2, "flexible": 4}),
        ("Cut them off politely after 10 minutes — you have a life", {"porous": 1, "rigid": 3}),
        ("Stay, cancel your plans, and feel resentful about it later", {"porous": 5, "enforcement": 1})
    ]),
    tier="core", cg="por_absorb_1", opacity=0.6))

questions.append(q("porous", "somatic",
    "After spending time with someone who's going through a hard time, you notice:",
    opts([
        ("You feel energized from helping — connecting with people in pain is meaningful", {"porous": 3}),
        ("You feel emotionally drained, like you absorbed their mood", {"porous": 5}),
        ("You feel fine — their struggle is theirs, you were just present", {"porous": 1, "flexible": 4}),
        ("You feel nothing — you kept enough distance to stay unaffected", {"porous": 1, "rigid": 4})
    ]),
    tier="core", cg="por_absorb_1", opacity=0.7))

questions.append(q("porous", "behavioral_recall",
    "How often do you agree to things you don't want to do because saying no feels impossible?",
    opts([
        ("Rarely — I'm pretty good at declining", {"porous": 1}),
        ("Sometimes, but only for important people", {"porous": 3}),
        ("Regularly — I'm the person who can't say no", {"porous": 5}),
        ("I don't even register what I want until after I've already said yes", {"porous": 5})
    ]),
    tier="core", cg="por_saying_no_1", opacity=0.6))

questions.append(q("porous", "partner_perspective",
    "Your partner is in a bad mood. Within an hour, you're also in a bad mood — even though nothing happened to YOU. How familiar is this?",
    opts([
        ("Very familiar — I'm a sponge for other people's emotions", {"porous": 5}),
        ("It happens sometimes with people I'm really close to", {"porous": 3}),
        ("Rarely — I can be empathetic without catching their emotions", {"porous": 1, "flexible": 4}),
        ("Never — I don't let other people's moods affect me", {"porous": 1, "rigid": 3})
    ]),
    tier="core", cg="por_absorb_1", opacity=0.65))

questions.append(q("porous", "scenario",
    "Someone you're dating asks to borrow a significant amount of money after only a few weeks together. You:",
    opts([
        ("Lend it without hesitation — they clearly need it and you want to help", {"porous": 5}),
        ("Feel uncomfortable but lend it because saying no might push them away", {"porous": 5, "enforcement": 1}),
        ("Decline kindly but feel guilty about it for days", {"porous": 4}),
        ("Decline — it's too soon and too much, and you're not apologetic about it", {"porous": 1, "flexible": 4})
    ]),
    tier="core", cg="por_saying_no_1", opacity=0.65))

questions.append(q("porous", "forced_choice",
    "Someone crosses a line with you. Which happens first?",
    opts([
        ("You wonder what you did to make them cross the line", {"porous": 5}),
        ("You recognize the boundary violation and address it", {"porous": 1, "flexible": 5, "enforcement": 4})
    ]),
    tier="core", cg="por_absorb_1", opacity=0.8))

questions.append(q("porous", "temporal",
    "Think about the last three requests people made of you. How many did you genuinely WANT to say yes to?",
    opts([
        ("All three — I'm pretty selective about my commitments", {"porous": 1}),
        ("Two out of three — one was a stretch but manageable", {"porous": 2}),
        ("Maybe one — but I said yes to all three", {"porous": 4}),
        ("None — but I said yes to all of them anyway", {"porous": 5})
    ]),
    tier="triangulation", cg="por_saying_no_1", opacity=0.6))

questions.append(q("porous", "scenario",
    "A family member keeps making comments about your weight/career/relationship choices. You:",
    opts([
        ("Set a clear boundary: 'I'm not going to discuss that with you'", {"porous": 1, "flexible": 4, "enforcement": 4}),
        ("Try to redirect the conversation but never directly address it", {"porous": 3}),
        ("Absorb the comments, go home, and feel terrible", {"porous": 5}),
        ("Cut off contact entirely — the only way to stop it", {"porous": 1, "rigid": 5})
    ]),
    tier="triangulation", cg="por_absorb_1", opacity=0.6))

questions.append(q("porous", "somatic",
    "When someone asks you for a favor and you want to say no, what does your body do?",
    opts([
        ("Nothing unusual — 'no' is just a word", {"porous": 1}),
        ("Slight tension but you push through and decline if you need to", {"porous": 2}),
        ("Throat tightens, stomach drops — the word 'no' physically can't come out", {"porous": 5}),
        ("Immediate guilt in your chest before you've even opened your mouth", {"porous": 4})
    ]),
    tier="core", cg="por_saying_no_1", opacity=0.75))

questions.append(q("porous", "behavioral_recall",
    "How much of your emotional bandwidth on an average day is spent on OTHER people's problems?",
    opts([
        ("Very little — I'm supportive but I don't carry their burdens", {"porous": 1}),
        ("Some, but I refill my own tank too", {"porous": 2, "flexible": 3}),
        ("Most of it — I'm the unofficial therapist for my circle", {"porous": 4}),
        ("Almost all of it — I genuinely don't know what my own emotional life looks like without their problems in it", {"porous": 5})
    ]),
    tier="triangulation", cg="por_absorb_1", opacity=0.65))

questions.append(q("porous", "partner_perspective",
    "Your partner says 'You give too much to other people and there's nothing left for us.' You feel:",
    opts([
        ("Defensive — helping people is who I am", {"porous": 4}),
        ("Guilty — they're probably right, but you don't know how to stop", {"porous": 5}),
        ("Surprised — you hadn't noticed the imbalance", {"porous": 3}),
        ("Validated — you've been feeling stretched thin too", {"porous": 4, "flexible": 2})
    ]),
    tier="triangulation", cg="por_saying_no_1", opacity=0.65))

questions.append(q("porous", "scenario",
    "Someone shares a deeply personal secret with you. You notice yourself feeling obligated to share one back, even though you don't want to. You:",
    opts([
        ("Share something equally personal — fairness requires it", {"porous": 5}),
        ("Feel the pressure but resist it — you share on your own timeline", {"porous": 2, "flexible": 4}),
        ("Share something minor to satisfy the social contract without going deep", {"porous": 3}),
        ("Don't feel any pressure — their sharing is their choice, not an obligation for you", {"porous": 1})
    ]),
    tier="core", cg="por_absorb_1", opacity=0.65))

questions.append(q("porous", "forced_choice",
    "Which sounds more like you?",
    opts([
        ("I feel responsible for other people's emotional states", {"porous": 5}),
        ("I care about others but their feelings are their responsibility", {"porous": 1, "flexible": 4})
    ]),
    tier="consistency_check", cg="por_absorb_1", opacity=0.85))

questions.append(q("porous", "scenario",
    "A friend is in crisis at 2 AM. You have work early tomorrow and you've already helped them through three crises this month. You:",
    opts([
        ("Answer immediately — they need you, sleep can wait", {"porous": 5}),
        ("Text back: 'I care about you. I can't tonight. Let's talk first thing tomorrow.'", {"porous": 1, "flexible": 5, "enforcement": 4}),
        ("Answer but resent it, and never mention the resentment", {"porous": 5, "enforcement": 1}),
        ("Don't answer, then feel guilty for hours and can't sleep anyway", {"porous": 4})
    ]),
    tier="core", cg="por_saying_no_1", opacity=0.7))

questions.append(q("porous", "temporal",
    "Over the past year, how many times have you abandoned your own plans to accommodate someone else's?",
    opts([
        ("Once or twice — for genuine emergencies", {"porous": 1}),
        ("A handful of times — sometimes flexibility is warranted", {"porous": 2, "flexible": 3}),
        ("Too many to count — my plans are always the ones that get sacrificed", {"porous": 5}),
        ("I stopped making firm plans because they always get overridden", {"porous": 5})
    ]),
    tier="consistency_check", cg="por_saying_no_1", opacity=0.6))

questions.append(q("porous", "trap",
    "People describe you as 'the nicest person they know.' This makes you feel:",
    opts([
        ("Good — being kind is genuinely important to you", {"porous": 3}),
        ("Uncomfortable — you wonder if 'nice' means 'pushover'", {"porous": 4}),
        ("Trapped — you can't stop being 'nice' without losing the relationship", {"porous": 5}),
        ("Indifferent — your value isn't measured by how nice you are", {"porous": 1})
    ]),
    tier="trap", trap=True, cg="por_absorb_1", opacity=0.6))

questions.append(q("porous", "somatic",
    "You walk into a room where two people have been arguing. Even though it has nothing to do with you, your body:",
    opts([
        ("Picks up the tension immediately — your chest tightens", {"porous": 5}),
        ("Notices the atmosphere but you don't internalize it", {"porous": 2}),
        ("Feels nothing unusual — their conflict, their energy", {"porous": 1}),
        ("Immediately wants to fix it — you start mediating before anyone asks", {"porous": 5})
    ]),
    tier="triangulation", cg="por_absorb_1", opacity=0.7))

questions.append(q("porous", "behavioral_recall",
    "When someone tells you their opinion on a topic you had a different view on, how often does your position shift to match theirs?",
    opts([
        ("Almost never — I'm open to new info but I hold my ground", {"porous": 1}),
        ("Sometimes, if they make a compelling argument", {"porous": 2}),
        ("Frequently — especially if they feel strongly about it", {"porous": 4}),
        ("Almost always — I end up mirroring whoever I'm talking to", {"porous": 5})
    ]),
    tier="core", cg="por_absorb_1", opacity=0.6))

questions.append(q("porous", "scenario",
    "You're at a restaurant with friends. You wanted Italian but everyone wants sushi. You:",
    opts([
        ("Say 'I was hoping for Italian — can we do sushi next time?'", {"porous": 1, "flexible": 4}),
        ("Go with sushi happily — it's about the company, not the food", {"porous": 2}),
        ("Go with sushi but feel a small pang that your preference doesn't matter", {"porous": 4}),
        ("Go with sushi and pretend you wanted it too", {"porous": 5})
    ]),
    tier="triangulation", cg="por_saying_no_1", opacity=0.5))

questions.append(q("porous", "partner_perspective",
    "Your ex contacts you needing emotional support. You're in a new relationship. You:",
    opts([
        ("Help them without hesitation — they're hurting and you can help", {"porous": 5}),
        ("Check with your current partner, then offer limited support", {"porous": 2, "flexible": 4}),
        ("Decline — that chapter is closed", {"porous": 1, "rigid": 3}),
        ("Help them, hide it from your current partner, and feel conflicted", {"porous": 5, "enforcement": 1})
    ]),
    tier="core", cg="por_absorb_1", opacity=0.65))

questions.append(q("porous", "temporal",
    "Looking back at relationships (any kind) that ended badly, what pattern do you see?",
    opts([
        ("I gave too much and they took too much", {"porous": 5}),
        ("I held people at arm's length and they gave up", {"porous": 1, "rigid": 5}),
        ("A mix — different relationships, different patterns", {"porous": 2, "flexible": 3}),
        ("I drew clear lines and left when they were crossed", {"porous": 1, "enforcement": 5})
    ]),
    tier="consistency_check", cg="por_absorb_1", opacity=0.7))

questions.append(q("porous", "forced_choice",
    "Which sentence hits closer to home?",
    opts([
        ("I lose myself in other people's needs", {"porous": 5}),
        ("I protect myself at the expense of connection", {"porous": 1, "rigid": 5})
    ]),
    tier="core", cg="por_absorb_1", opacity=0.85))

questions.append(q("porous", "scenario",
    "You've just started seeing someone new. They want to spend every evening together. You:",
    opts([
        ("Love it — finally someone who wants you as much as you want them", {"porous": 4}),
        ("Enjoy it but start to miss your solo time after a few days", {"porous": 2, "flexible": 4}),
        ("Go along with it even though it's too much too fast", {"porous": 5}),
        ("Set a pace you're comfortable with from the start", {"porous": 1, "flexible": 5})
    ]),
    tier="triangulation", cg="por_saying_no_1", opacity=0.6))

questions.append(q("porous", "behavioral_recall",
    "When you have a strong emotional reaction to something someone did, how often do you question whether your reaction is valid before expressing it?",
    opts([
        ("Rarely — if I feel it, it's valid", {"porous": 1}),
        ("Sometimes — I check my assumptions but trust my feelings", {"porous": 2, "flexible": 4}),
        ("Often — I convince myself I'm overreacting before I ever speak up", {"porous": 4}),
        ("Almost always — their version of events must be more accurate than my feelings", {"porous": 5})
    ]),
    tier="core", cg="por_absorb_1", opacity=0.7))

questions.append(q("porous", "somatic",
    "When you finally set a boundary with someone, your body:",
    opts([
        ("Feels relief — like exhaling for the first time in hours", {"porous": 2, "enforcement": 4}),
        ("Feels empowered but shaky — new territory", {"porous": 3, "enforcement": 3}),
        ("Floods with guilt and dread — you're already planning to take it back", {"porous": 5, "enforcement": 1}),
        ("Feels nothing — you set boundaries all the time, it's not emotional", {"porous": 1, "rigid": 3})
    ]),
    tier="triangulation", cg="por_saying_no_1", opacity=0.7))

# ============================================================
# RIGID (25)
# ============================================================

questions.append(q("rigid", "scenario",
    "A close friend asks if they can stay at your place for a week while their apartment is being repaired. You:",
    opts([
        ("Say yes immediately — that's what friends are for", {"rigid": 1, "porous": 3}),
        ("Say yes but set clear expectations about space and timing", {"rigid": 2, "flexible": 5}),
        ("Feel uncomfortable but agree reluctantly", {"rigid": 4}),
        ("Decline — your space is your space", {"rigid": 5})
    ]),
    tier="core", cg="rig_walls_1", opacity=0.6))

questions.append(q("rigid", "somatic",
    "Someone you don't know well tries to hug you as a greeting. Your body:",
    opts([
        ("Hugs back warmly — human connection is great", {"rigid": 1}),
        ("Accepts it but feels slightly stiff", {"rigid": 3}),
        ("Recoils — you step back before they can make contact", {"rigid": 5}),
        ("Hugs back but makes a mental note to avoid this person's greetings in the future", {"rigid": 4})
    ]),
    tier="core", cg="rig_physical_1", opacity=0.65))

questions.append(q("rigid", "behavioral_recall",
    "How many people in your life know what you're actually going through emotionally right now?",
    opts([
        ("Several — I'm an open book with people I trust", {"rigid": 1}),
        ("Two or three close people", {"rigid": 2, "flexible": 4}),
        ("One person, maybe", {"rigid": 4}),
        ("Nobody — I handle my own stuff", {"rigid": 5})
    ]),
    tier="core", cg="rig_vulnerability_1", opacity=0.65))

questions.append(q("rigid", "partner_perspective",
    "Your partner wants to have a deep emotional conversation about the state of your relationship. You:",
    opts([
        ("Welcome it — these conversations strengthen the bond", {"rigid": 1, "flexible": 4}),
        ("Engage but notice yourself wanting to keep it brief and solution-focused", {"rigid": 3}),
        ("Feel cornered — you need to escape this conversation", {"rigid": 5}),
        ("Deflect with humor or redirect to a lighter topic", {"rigid": 4})
    ]),
    tier="core", cg="rig_vulnerability_1", opacity=0.7))

questions.append(q("rigid", "scenario",
    "Someone at work shares personal struggles in a team meeting — tears and everything. You:",
    opts([
        ("Feel compassion and offer support afterward", {"rigid": 1}),
        ("Feel uncomfortable but recognize their courage", {"rigid": 3}),
        ("Think it's wildly inappropriate — work isn't therapy", {"rigid": 5}),
        ("Shut down — other people's emotions in professional settings are overwhelming", {"rigid": 4})
    ]),
    tier="triangulation", cg="rig_walls_1", opacity=0.6))

questions.append(q("rigid", "forced_choice",
    "When someone gets too close emotionally, your instinct is:",
    opts([
        ("To let them in deeper — closeness is the point of relationships", {"rigid": 1}),
        ("To create distance — space is how I stay safe", {"rigid": 5})
    ]),
    tier="core", cg="rig_vulnerability_1", opacity=0.85))

questions.append(q("rigid", "temporal",
    "Think about the last time you cried in front of someone. How long ago was it?",
    opts([
        ("Recently — I'm comfortable being vulnerable with people I trust", {"rigid": 1}),
        ("Within the past year, in a particularly intense moment", {"rigid": 2}),
        ("Years ago — I don't do that anymore", {"rigid": 4}),
        ("I genuinely cannot remember the last time — or it's never happened", {"rigid": 5})
    ]),
    tier="triangulation", cg="rig_vulnerability_1", opacity=0.65))

questions.append(q("rigid", "somatic",
    "When a conversation starts getting emotionally deep, your body:",
    opts([
        ("Settles in — depth is where real connection happens", {"rigid": 1}),
        ("Stays engaged but you notice slight tension", {"rigid": 3}),
        ("Activates — you start planning your exit or topic change", {"rigid": 5}),
        ("Goes cold — like someone flipped a switch and your feelings turned off", {"rigid": 5})
    ]),
    tier="core", cg="rig_vulnerability_1", opacity=0.75))

questions.append(q("rigid", "behavioral_recall",
    "How often do people describe you as 'hard to read' or 'mysterious'?",
    opts([
        ("Never — people say I'm an open book", {"rigid": 1}),
        ("Occasionally — I'm selective about what I share", {"rigid": 3}),
        ("Often — people say they can never tell what I'm thinking", {"rigid": 4}),
        ("Constantly — and I prefer it that way", {"rigid": 5})
    ]),
    tier="triangulation", cg="rig_walls_1", opacity=0.55))

questions.append(q("rigid", "scenario",
    "A new romantic partner says 'I feel like you have walls up and I can't get through them.' You:",
    opts([
        ("Take it seriously and actively work on opening up", {"rigid": 2}),
        ("Acknowledge it but explain that you open up slowly", {"rigid": 3}),
        ("Feel attacked — your boundaries aren't 'walls', they're protection", {"rigid": 5}),
        ("End the relationship — if they can't handle your pace, they're not right for you", {"rigid": 5})
    ]),
    tier="core", cg="rig_walls_1", opacity=0.7))

questions.append(q("rigid", "partner_perspective",
    "Your partner wants to combine finances. Your reaction:",
    opts([
        ("Sure — we're a team", {"rigid": 1}),
        ("Open to it with some structure — separate accounts plus a joint one", {"rigid": 2, "flexible": 4}),
        ("Hesitant — my money is mine, your money is yours", {"rigid": 4}),
        ("Absolutely not — financial independence is non-negotiable", {"rigid": 5})
    ]),
    tier="triangulation", cg="rig_walls_1", opacity=0.6))

questions.append(q("rigid", "forced_choice",
    "Which feels more dangerous?",
    opts([
        ("Letting someone see your weaknesses", {"rigid": 5}),
        ("Keeping everyone at a distance and ending up alone", {"rigid": 1})
    ]),
    tier="core", cg="rig_vulnerability_1", opacity=0.85))

questions.append(q("rigid", "scenario",
    "You've been going through something hard. Multiple people offer help. You:",
    opts([
        ("Accept gratefully — support makes hard things easier", {"rigid": 1}),
        ("Accept from one or two trusted people, decline the rest", {"rigid": 3, "flexible": 3}),
        ("Decline everyone — you'll handle it yourself", {"rigid": 5}),
        ("Accept performatively but don't actually let anyone help with the real problem", {"rigid": 5})
    ]),
    tier="core", cg="rig_walls_1", opacity=0.65))

questions.append(q("rigid", "temporal",
    "As relationships get closer, do you notice yourself creating distance — picking fights, pulling back, finding flaws?",
    opts([
        ("No — closeness is what I want and I move toward it", {"rigid": 1}),
        ("Occasionally — I notice the urge but usually override it", {"rigid": 2}),
        ("Yes — there's a pattern and I'm aware of it even if I can't always stop it", {"rigid": 4}),
        ("Absolutely — every relationship has a distance I won't go past", {"rigid": 5})
    ]),
    tier="core", cg="rig_walls_1", opacity=0.75))

questions.append(q("rigid", "behavioral_recall",
    "When you're in physical pain (sick, injured), how willing are you to let someone take care of you?",
    opts([
        ("Very willing — it's nice to be cared for", {"rigid": 1}),
        ("Willing if they offer, but I won't ask", {"rigid": 3}),
        ("Uncomfortable — I'd rather suffer alone than feel dependent", {"rigid": 5}),
        ("Impossible — I'll insist I'm fine while clearly not fine", {"rigid": 5})
    ]),
    tier="triangulation", cg="rig_vulnerability_1", opacity=0.6))

questions.append(q("rigid", "somatic",
    "When someone says 'I love you' for the first time (friend or partner), your body:",
    opts([
        ("Warms up — you say it back easily if you feel it", {"rigid": 1}),
        ("Feels pleased but you might deflect with humor before reciprocating", {"rigid": 3}),
        ("Freezes — the intimacy is overwhelming even if the feeling is mutual", {"rigid": 5}),
        ("Panics — you want to run", {"rigid": 5})
    ]),
    tier="triangulation", cg="rig_physical_1", opacity=0.75))

questions.append(q("rigid", "trap",
    "People who share everything about themselves on social media or in conversation — you find them:",
    opts([
        ("Authentic and brave", {"rigid": 1}),
        ("Sometimes oversharing, sometimes refreshing — depends on context", {"rigid": 2}),
        ("Attention-seeking and uncomfortable to be around", {"rigid": 4}),
        ("Fascinating because you could never do that", {"rigid": 3})
    ]),
    tier="trap", trap=True, cg="rig_walls_1", opacity=0.55))

questions.append(q("rigid", "scenario",
    "A therapist suggests that your independence might actually be a defense mechanism. You:",
    opts([
        ("Consider it seriously — you've wondered the same thing", {"rigid": 3}),
        ("Disagree respectfully — independence IS who you are", {"rigid": 5}),
        ("Get angry — they're pathologizing your strength", {"rigid": 5}),
        ("Already know this and are working on it", {"rigid": 2})
    ]),
    tier="trap", trap=True, cg="rig_vulnerability_1", opacity=0.7))

questions.append(q("rigid", "partner_perspective",
    "Your partner asks 'What are you afraid of?' You:",
    opts([
        ("Answer honestly — you know your fears and can share them", {"rigid": 1}),
        ("Share a surface-level fear (heights, spiders) but not the real one", {"rigid": 4}),
        ("Say 'nothing' and change the subject", {"rigid": 5}),
        ("Give a thoughtful answer but leave out the most vulnerable part", {"rigid": 3})
    ]),
    tier="core", cg="rig_vulnerability_1", opacity=0.7))

questions.append(q("rigid", "behavioral_recall",
    "How many relationships (romantic or friendship) have you ended because they were 'getting too close' or 'too intense'?",
    opts([
        ("None — closeness is the goal", {"rigid": 1}),
        ("One or two — unusual circumstances", {"rigid": 2}),
        ("Several — I see the pattern", {"rigid": 4}),
        ("Enough that people have commented on it", {"rigid": 5})
    ]),
    tier="consistency_check", cg="rig_walls_1", opacity=0.7))

questions.append(q("rigid", "scenario",
    "You're having a wonderful time on a date. The person across from you starts sharing something deeply vulnerable. You notice yourself:",
    opts([
        ("Leaning in — vulnerability creates intimacy", {"rigid": 1}),
        ("Listening carefully and matching their openness with your own", {"rigid": 1, "flexible": 4}),
        ("Getting uncomfortable and wondering if it's too much too soon", {"rigid": 4}),
        ("Thinking about how to end the evening", {"rigid": 5})
    ]),
    tier="triangulation", cg="rig_walls_1", opacity=0.65))

questions.append(q("rigid", "temporal",
    "Over the years, has your circle of people you're close to gotten bigger or smaller?",
    opts([
        ("Bigger — I keep building meaningful connections", {"rigid": 1}),
        ("About the same — I maintain a few deep connections", {"rigid": 2}),
        ("Smaller — I've been pruning, and each pruning feels like a relief", {"rigid": 4}),
        ("Minimal — I'm down to one or two people and that's plenty", {"rigid": 5})
    ]),
    tier="consistency_check", cg="rig_walls_1", opacity=0.6))

questions.append(q("rigid", "forced_choice",
    "If you had to choose one for the rest of your life:",
    opts([
        ("Deep, messy, emotionally entangled relationships", {"rigid": 1}),
        ("Peaceful, independent solitude with minimal obligations to others", {"rigid": 5})
    ]),
    tier="core", cg="rig_vulnerability_1", opacity=0.85))

questions.append(q("rigid", "somatic",
    "When someone you barely know asks a personal question, your body:",
    opts([
        ("Doesn't react — you answer or redirect casually", {"rigid": 2}),
        ("Tightens — none of their business", {"rigid": 4}),
        ("Walls up instantly — like a portcullis dropping", {"rigid": 5}),
        ("Engages — you enjoy connecting with new people at depth", {"rigid": 1})
    ]),
    tier="triangulation", cg="rig_physical_1", opacity=0.7))

questions.append(q("rigid", "scenario",
    "You've been deeply hurt by someone you let in. Your takeaway lesson is:",
    opts([
        ("Some people aren't safe, but that doesn't mean no one is — keep your heart open", {"rigid": 1}),
        ("I need to be more careful about who I trust, but trust is still worth it", {"rigid": 2, "flexible": 4}),
        ("I was stupid to let my guard down — lesson learned", {"rigid": 5}),
        ("Never again — the walls go up and they're staying up", {"rigid": 5})
    ]),
    tier="core", cg="rig_walls_1", opacity=0.7))

# ============================================================
# FLEXIBLE (25)
# ============================================================

questions.append(q("flexible", "scenario",
    "A friend asks to borrow something valuable to you. You:",
    opts([
        ("Lend it without conditions — trust until proven otherwise", {"flexible": 3, "porous": 4}),
        ("Lend it with clear return expectations: 'Sure, just have it back by Friday'", {"flexible": 5}),
        ("Say no — you don't lend valuable things", {"flexible": 2, "rigid": 4}),
        ("Say yes but worry about it until it's returned", {"flexible": 2, "porous": 3})
    ]),
    tier="core", cg="flex_adapt_1", opacity=0.6))

questions.append(q("flexible", "behavioral_recall",
    "When you set a boundary and the other person pushes back, what happens?",
    opts([
        ("I hold the boundary and explain my reasoning once — after that, it stands", {"flexible": 5, "enforcement": 5}),
        ("I cave — the conflict isn't worth it", {"flexible": 1, "porous": 5, "enforcement": 1}),
        ("I become more rigid — any pushback makes me dig in harder", {"flexible": 2, "rigid": 4}),
        ("I listen to their perspective and adjust IF their point is valid — otherwise I hold", {"flexible": 5})
    ]),
    tier="core", cg="flex_adapt_1", opacity=0.7))

questions.append(q("flexible", "partner_perspective",
    "Your partner's family has different traditions/values than yours. When they visit, you:",
    opts([
        ("Adapt cheerfully — different strokes for different folks", {"flexible": 5}),
        ("Accommodate some things but hold firm on what matters to you", {"flexible": 5}),
        ("Absorb everything and suppress your discomfort", {"flexible": 2, "porous": 5}),
        ("Refuse to change anything — your house, your rules", {"flexible": 1, "rigid": 5})
    ]),
    tier="core", cg="flex_relationship_1", opacity=0.6))

questions.append(q("flexible", "scenario",
    "You have a firm 'no phones at dinner' rule. Your partner's parent is in the hospital. Your partner keeps checking their phone. You:",
    opts([
        ("Obviously make an exception — context matters", {"flexible": 5}),
        ("Feel annoyed but say nothing", {"flexible": 2, "rigid": 3}),
        ("Point out the rule — they could check after dinner", {"flexible": 1, "rigid": 5}),
        ("Throw the rule out entirely — it was too rigid anyway", {"flexible": 3, "porous": 3})
    ]),
    tier="core", cg="flex_adapt_1", opacity=0.55))

questions.append(q("flexible", "forced_choice",
    "A healthy boundary is:",
    opts([
        ("A clear line that never moves", {"flexible": 2, "rigid": 4}),
        ("A clear line that adjusts based on context and relationship", {"flexible": 5})
    ]),
    tier="core", cg="flex_adapt_1", opacity=0.85))

questions.append(q("flexible", "somatic",
    "When you're in a situation that requires you to be both open AND protected — like a first date or job interview — your body:",
    opts([
        ("Finds a comfortable middle — alert but relaxed", {"flexible": 5}),
        ("Defaults to open and hopes for the best", {"flexible": 2, "porous": 4}),
        ("Defaults to guarded and you'll open up only if it feels safe", {"flexible": 3, "rigid": 3}),
        ("Can't find a middle — oscillates between oversharing and shutting down", {"flexible": 1})
    ]),
    tier="core", cg="flex_adapt_1", opacity=0.7))

questions.append(q("flexible", "temporal",
    "Think about a relationship where the boundary expectations changed over time (e.g., you grew closer and shared more, or grew apart and needed more space). How naturally did you adjust?",
    opts([
        ("Smoothly — I read the shifting dynamics and adapted", {"flexible": 5}),
        ("With some effort but I got there", {"flexible": 4}),
        ("Badly — I couldn't let go of how things used to be", {"flexible": 2, "rigid": 3}),
        ("I gave away everything the moment they asked for more", {"flexible": 1, "porous": 5})
    ]),
    tier="triangulation", cg="flex_relationship_1", opacity=0.7))

questions.append(q("flexible", "scenario",
    "You're a manager. A usually-reliable employee asks for special accommodation that goes against company policy. You:",
    opts([
        ("Follow policy — rules exist for a reason", {"flexible": 2, "rigid": 4}),
        ("Grant the exception with clear parameters: 'This time, because X, but going forward Y'", {"flexible": 5}),
        ("Grant it immediately without conditions — they're a good employee", {"flexible": 2, "porous": 3}),
        ("Agonize because you can't decide what's right", {"flexible": 2})
    ]),
    tier="triangulation", cg="flex_adapt_1", opacity=0.6))

questions.append(q("flexible", "behavioral_recall",
    "How do you handle the different boundary expectations of different relationships? (e.g., what you share with your best friend vs. your boss vs. your parent)",
    opts([
        ("Naturally — I have a clear sense of what's appropriate where", {"flexible": 5}),
        ("Mostly well, with occasional missteps", {"flexible": 4}),
        ("I'm the same with everyone — take it or leave it", {"flexible": 2, "rigid": 4}),
        ("I overadapt — I become a different person in every context and lose track of myself", {"flexible": 1, "porous": 5})
    ]),
    tier="core", cg="flex_relationship_1", opacity=0.65))

questions.append(q("flexible", "partner_perspective",
    "Your partner wants more alone time than you do. How do you handle the mismatch?",
    opts([
        ("Discuss it openly and find a balance you both can live with", {"flexible": 5}),
        ("Give them all the space they want, even if it hurts you", {"flexible": 2, "porous": 4}),
        ("Insist on the same amount of together time — compromise means meeting in the middle", {"flexible": 2, "rigid": 3}),
        ("Take it personally and start questioning the relationship", {"flexible": 1})
    ]),
    tier="triangulation", cg="flex_relationship_1", opacity=0.65))

questions.append(q("flexible", "scenario",
    "Your roommate starts working from home and the shared space dynamics shift. You:",
    opts([
        ("Have a proactive conversation about new shared-space expectations", {"flexible": 5}),
        ("Adapt silently and hope they notice you making accommodations", {"flexible": 2, "porous": 3}),
        ("Get increasingly irritated that the old rules aren't being followed", {"flexible": 1, "rigid": 4}),
        ("Move out — the dynamic has changed too much", {"flexible": 1, "rigid": 4})
    ]),
    tier="core", cg="flex_adapt_1", opacity=0.6))

questions.append(q("flexible", "forced_choice",
    "Which better describes how you operate?",
    opts([
        ("I have clear personal rules that I apply consistently across all situations", {"flexible": 2, "rigid": 4}),
        ("I have clear values that I express differently depending on the context", {"flexible": 5})
    ]),
    tier="consistency_check", cg="flex_adapt_1", opacity=0.85))

questions.append(q("flexible", "somatic",
    "When someone needs more from you than you expected to give today, your body:",
    opts([
        ("Checks in: 'Do I have the capacity right now? If yes, give it. If not, say so.'", {"flexible": 5}),
        ("Gives it automatically without checking — their need overrides your limit", {"flexible": 1, "porous": 5}),
        ("Locks up — unanticipated demands feel like violations", {"flexible": 1, "rigid": 5}),
        ("Feels annoyed but you figure it out — adapting is a skill you've practiced", {"flexible": 4})
    ]),
    tier="triangulation", cg="flex_adapt_1", opacity=0.7))

questions.append(q("flexible", "temporal",
    "How has your approach to boundaries changed since your twenties (or early adulthood)?",
    opts([
        ("I was too open then, too closed now — haven't found the sweet spot", {"flexible": 2}),
        ("I've gradually developed clearer, more adaptive boundaries", {"flexible": 5}),
        ("I was flexible then and I'm still flexible now — it's consistent", {"flexible": 4}),
        ("I swung from one extreme (no boundaries) to the other (walls everywhere)", {"flexible": 1})
    ]),
    tier="triangulation", cg="flex_relationship_1", opacity=0.65))

questions.append(q("flexible", "behavioral_recall",
    "When a close friend does something that bothers you, how do you typically handle it?",
    opts([
        ("Bring it up directly but kindly — 'hey, when you did X, it bothered me because Y'", {"flexible": 5}),
        ("Let it go if it's small, bring it up if it's a pattern", {"flexible": 5}),
        ("Never bring it up — confrontation isn't worth it", {"flexible": 1, "porous": 3}),
        ("Bring it up aggressively, or cut them off without explaining", {"flexible": 1, "rigid": 4})
    ]),
    tier="core", cg="flex_relationship_1", opacity=0.6))

questions.append(q("flexible", "scenario",
    "You have a personal rule about not lending money. Your sibling asks you for help with rent — they'll be evicted otherwise. You:",
    opts([
        ("Break your rule — this is an extraordinary circumstance for someone you love", {"flexible": 5}),
        ("Offer alternative help (finding resources, letting them stay with you) without breaking the money rule", {"flexible": 4}),
        ("Hold the rule — if you break it once, the boundary is gone forever", {"flexible": 1, "rigid": 5}),
        ("Give the money but resent it and bring it up in future arguments", {"flexible": 2, "porous": 3})
    ]),
    tier="trap", trap=True, cg="flex_adapt_1", opacity=0.7))

questions.append(q("flexible", "partner_perspective",
    "You and your partner have different ideas about appropriate boundaries with exes. You:",
    opts([
        ("Have an open conversation and find a boundary you both feel safe with", {"flexible": 5}),
        ("Default to whatever makes your partner comfortable, regardless of your feelings", {"flexible": 2, "porous": 4}),
        ("Insist on your own boundary — they can deal with it or leave", {"flexible": 1, "rigid": 5}),
        ("Avoid the conversation entirely and hope it resolves itself", {"flexible": 1})
    ]),
    tier="triangulation", cg="flex_relationship_1", opacity=0.65))

questions.append(q("flexible", "trap",
    "Someone says 'healthy relationships require compromise.' Your honest reaction:",
    opts([
        ("True — and compromise goes both ways", {"flexible": 5}),
        ("True — which is why I usually compromise first", {"flexible": 2, "porous": 4}),
        ("Depends — 'compromise' is sometimes code for 'give up what matters to you'", {"flexible": 4}),
        ("Disagree — the right person won't require you to compromise your needs", {"flexible": 1, "rigid": 4})
    ]),
    tier="trap", trap=True, cg="flex_adapt_1", opacity=0.65))

questions.append(q("flexible", "behavioral_recall",
    "How often do you reassess and adjust your boundaries as relationships evolve?",
    opts([
        ("Regularly — boundaries should grow with the relationship", {"flexible": 5}),
        ("Sometimes — when something isn't working, I'll adjust", {"flexible": 4}),
        ("Rarely — my boundaries don't change much once they're set", {"flexible": 2, "rigid": 3}),
        ("I don't have clear enough boundaries to adjust them", {"flexible": 1, "porous": 4})
    ]),
    tier="consistency_check", cg="flex_adapt_1", opacity=0.65))

questions.append(q("flexible", "scenario",
    "A colleague who you normally keep at professional distance shares that they're going through something similar to what you went through years ago. You:",
    opts([
        ("Share your experience if it might help — the usual boundary can flex for compassion", {"flexible": 5}),
        ("Express empathy but keep professional distance — boundaries exist for a reason", {"flexible": 3, "rigid": 3}),
        ("Tell them everything — you can't hold back when someone needs support", {"flexible": 2, "porous": 4}),
        ("Share thoughtfully — some personal details that are relevant, not everything", {"flexible": 5})
    ]),
    tier="core", cg="flex_relationship_1", opacity=0.6))

questions.append(q("flexible", "somatic",
    "When you successfully navigate a boundary conversation — holding your line while staying connected to the other person — your body feels:",
    opts([
        ("Accomplished and centered — this is what emotional maturity feels like", {"flexible": 5}),
        ("Relieved but exhausted — that took a lot of energy", {"flexible": 3}),
        ("You've never had this experience — you either cave or wall up", {"flexible": 1}),
        ("Slightly anxious — did you do it right? Will they be okay?", {"flexible": 3, "porous": 3})
    ]),
    tier="triangulation", cg="flex_adapt_1", opacity=0.7))

questions.append(q("flexible", "forced_choice",
    "Which describes your boundary style more accurately?",
    opts([
        ("I adapt to each situation but sometimes lose myself in the process", {"flexible": 2, "porous": 4}),
        ("I hold firm regardless of situation — consistency IS the boundary", {"flexible": 2, "rigid": 4}),
        ("I know my limits AND I can adjust them thoughtfully when circumstances warrant", {"flexible": 5}),
        ("I genuinely don't know — it changes depending on my mood", {"flexible": 1})
    ]),
    tier="consistency_check", cg="flex_adapt_1", opacity=0.8))

questions.append(q("flexible", "temporal",
    "Think of someone who handles boundaries well — firm but warm, clear but not rigid. How close is your own style to theirs?",
    opts([
        ("Very close — I've developed that balance over time", {"flexible": 5}),
        ("Getting there — I can do it in low-stakes situations but struggle under pressure", {"flexible": 3}),
        ("Not close at all — I lean too far in one direction (open or closed)", {"flexible": 1}),
        ("I can't even picture what that looks like in practice", {"flexible": 1})
    ]),
    tier="triangulation", cg="flex_relationship_1", opacity=0.65))

# ============================================================
# ENFORCEMENT (25)
# ============================================================

questions.append(q("enforcement", "scenario",
    "You told your partner that a specific behavior is a dealbreaker. They do it. You:",
    opts([
        ("Follow through — you said it was a dealbreaker and you meant it", {"enforcement": 5}),
        ("Have a serious conversation — one more chance with clear consequences", {"enforcement": 4}),
        ("Downgrade the boundary — 'well, it wasn't REALLY a dealbreaker'", {"enforcement": 2}),
        ("Pretend you didn't notice because the confrontation is scarier than the behavior", {"enforcement": 1})
    ]),
    tier="core", cg="enf_followthrough_1", opacity=0.7))

questions.append(q("enforcement", "behavioral_recall",
    "How often do the boundaries you set actually get maintained over time?",
    opts([
        ("Almost always — my word is my word", {"enforcement": 5}),
        ("Usually — with occasional slippage that I catch and correct", {"enforcement": 4}),
        ("Hit or miss — I set them with conviction but enforcement is harder", {"enforcement": 2}),
        ("Rarely — I'm great at setting boundaries and terrible at keeping them", {"enforcement": 1})
    ]),
    tier="core", cg="enf_followthrough_1", opacity=0.7))

questions.append(q("enforcement", "somatic",
    "Someone violates a boundary you've clearly communicated. The moment you realize it, your body:",
    opts([
        ("Activates with clear energy — 'this needs to be addressed'", {"enforcement": 5}),
        ("Tenses with resolve — uncomfortable but you'll handle it", {"enforcement": 4}),
        ("Floods with anxiety — confrontation is terrifying", {"enforcement": 2}),
        ("Shuts down — you freeze and do nothing", {"enforcement": 1})
    ]),
    tier="core", cg="enf_confrontation_1", opacity=0.7))

questions.append(q("enforcement", "partner_perspective",
    "Your partner keeps 'forgetting' a boundary you've set multiple times. At this point, you:",
    opts([
        ("Enforce a consequence: 'We've talked about this three times. Here's what happens now.'", {"enforcement": 5}),
        ("Have one more direct conversation — maybe you haven't been clear enough", {"enforcement": 3}),
        ("Start questioning whether the boundary is reasonable — maybe you're asking too much", {"enforcement": 2, "porous": 3}),
        ("Give up — clearly this boundary isn't going to be respected, so why bother", {"enforcement": 1})
    ]),
    tier="core", cg="enf_followthrough_1", opacity=0.7))

questions.append(q("enforcement", "scenario",
    "A family member repeatedly makes inappropriate comments at holidays despite you asking them to stop. This year, you:",
    opts([
        ("Don't attend — you've warned them and now there are consequences", {"enforcement": 5}),
        ("Attend but leave immediately if it happens again", {"enforcement": 4}),
        ("Attend, endure it, and complain about it later to someone else", {"enforcement": 1}),
        ("Don't even remember setting the boundary — you've made peace with it", {"enforcement": 1})
    ]),
    tier="triangulation", cg="enf_followthrough_1", opacity=0.65))

questions.append(q("enforcement", "forced_choice",
    "Which is harder for you?",
    opts([
        ("Setting a boundary in the first place", {"enforcement": 4}),
        ("Enforcing a boundary after someone has violated it", {"enforcement": 1})
    ]),
    tier="core", cg="enf_confrontation_1", opacity=0.8))

questions.append(q("enforcement", "temporal",
    "Think about a boundary you set with someone important. What happened over the following weeks/months?",
    opts([
        ("It held — they respected it and I maintained it", {"enforcement": 5}),
        ("It mostly held — a few tests but I reinforced it each time", {"enforcement": 4}),
        ("It eroded gradually — I kept making exceptions until it was gone", {"enforcement": 2}),
        ("It collapsed the first time they pushed back", {"enforcement": 1})
    ]),
    tier="core", cg="enf_followthrough_1", opacity=0.7))

questions.append(q("enforcement", "behavioral_recall",
    "When you need to enforce a boundary, how directly do you communicate?",
    opts([
        ("Very directly: 'You crossed a line. This is what I need to happen now.'", {"enforcement": 5}),
        ("Directly but gently: 'Hey, we talked about this — can we get back on track?'", {"enforcement": 4}),
        ("Indirectly: hint, use passive language, or get someone else to convey the message", {"enforcement": 2}),
        ("Not at all: I just distance myself without explaining why", {"enforcement": 2, "rigid": 3})
    ]),
    tier="triangulation", cg="enf_confrontation_1", opacity=0.65))

questions.append(q("enforcement", "scenario",
    "You're leading a project. A team member consistently misses deadlines despite multiple conversations. You:",
    opts([
        ("Escalate — formal consequence, reassignment, or removal from the project", {"enforcement": 5}),
        ("One final clear conversation with documented expectations and consequences", {"enforcement": 4}),
        ("Keep accommodating them because the confrontation of escalation feels worse than doing their work yourself", {"enforcement": 1}),
        ("Complain to others but take no direct action", {"enforcement": 1})
    ]),
    tier="triangulation", cg="enf_followthrough_1", opacity=0.6))

questions.append(q("enforcement", "somatic",
    "You're about to have a conversation where you need to enforce a boundary with someone you love. In the hour before, your body:",
    opts([
        ("Is focused and steady — you've thought about what to say and you're ready", {"enforcement": 5}),
        ("Has butterflies but you're committed to following through", {"enforcement": 4}),
        ("Is so anxious you're considering canceling or softening your message", {"enforcement": 2}),
        ("Is already rehearsing ways to avoid the confrontation entirely", {"enforcement": 1})
    ]),
    tier="core", cg="enf_confrontation_1", opacity=0.7))

questions.append(q("enforcement", "partner_perspective",
    "Your partner accuses you of being 'too strict' about a boundary that's important to you. You:",
    opts([
        ("Explain why it matters to you calmly and hold firm", {"enforcement": 5}),
        ("Hear them out — if they make a good point, you'll adjust; if not, you hold", {"enforcement": 4, "flexible": 4}),
        ("Start doubting yourself — maybe you ARE being unreasonable", {"enforcement": 2, "porous": 3}),
        ("Cave immediately — being called 'strict' feels like being called unloving", {"enforcement": 1})
    ]),
    tier="triangulation", cg="enf_confrontation_1", opacity=0.7))

questions.append(q("enforcement", "trap",
    "Someone you admire violates one of your boundaries. Compared to when a stranger does it, your enforcement is:",
    opts([
        ("Exactly the same — a boundary is a boundary regardless of who crosses it", {"enforcement": 5}),
        ("Slightly softer in delivery but equally firm in content", {"enforcement": 4}),
        ("Much softer — you find excuses for people you admire", {"enforcement": 2}),
        ("Nonexistent — you'd rather let them cross it than risk the relationship", {"enforcement": 1})
    ]),
    tier="trap", trap=True, cg="enf_followthrough_1", opacity=0.7))

questions.append(q("enforcement", "behavioral_recall",
    "How many times do you typically repeat a boundary before you enforce a consequence?",
    opts([
        ("Once. If I have to say it twice, there's already a consequence", {"enforcement": 5}),
        ("Twice — everyone deserves a reminder", {"enforcement": 4}),
        ("Three to five times — I give too many chances and I know it", {"enforcement": 2}),
        ("I lose count — I keep saying it and keep not doing anything about it", {"enforcement": 1})
    ]),
    tier="consistency_check", cg="enf_followthrough_1", opacity=0.65))

questions.append(q("enforcement", "scenario",
    "You told a friend that if they cancel on you one more time, you're done making plans with them. They cancel. You:",
    opts([
        ("Stop making plans with them — you said you would and you meant it", {"enforcement": 5}),
        ("Call them out: 'This is the last time. Next time I follow through. I mean it this time.'", {"enforcement": 2}),
        ("Make an excuse for them in your head and make plans again next week", {"enforcement": 1}),
        ("Distance yourself gradually rather than having the confrontation", {"enforcement": 2, "rigid": 3})
    ]),
    tier="core", cg="enf_followthrough_1", opacity=0.65))

questions.append(q("enforcement", "forced_choice",
    "Be honest: do your consequences for boundary violations tend to be:",
    opts([
        ("Clear, proportional, and consistently enforced", {"enforcement": 5}),
        ("Threatened but rarely executed", {"enforcement": 1})
    ]),
    tier="consistency_check", cg="enf_followthrough_1", opacity=0.9))

questions.append(q("enforcement", "temporal",
    "Over time, do the people in your life learn to respect your boundaries?",
    opts([
        ("Yes — because they know I enforce them", {"enforcement": 5}),
        ("Mostly — some people test more than others but eventually get it", {"enforcement": 4}),
        ("No — the same people keep crossing the same boundaries", {"enforcement": 2}),
        ("The people who don't respect my boundaries stay in my life; the respectful ones drift away", {"enforcement": 1})
    ]),
    tier="triangulation", cg="enf_followthrough_1", opacity=0.65))

questions.append(q("enforcement", "somatic",
    "After you successfully enforce a boundary — you say what needs to be said and hold your ground — your body feels:",
    opts([
        ("Strong and grounded — this is self-respect in action", {"enforcement": 5}),
        ("Shaky but proud — it was hard but you did it", {"enforcement": 4}),
        ("Guilty and anxious — maybe you were too harsh", {"enforcement": 2}),
        ("You can't recall ever doing this successfully", {"enforcement": 1})
    ]),
    tier="triangulation", cg="enf_confrontation_1", opacity=0.7))

questions.append(q("enforcement", "scenario",
    "You've been assertive and clear about a boundary. The other person responds with tears and 'I can't believe you'd do this to me.' You:",
    opts([
        ("Hold firm: 'I understand you're upset, and this boundary still stands'", {"enforcement": 5}),
        ("Comfort them briefly but don't retract the boundary", {"enforcement": 4}),
        ("Feel terrible and start negotiating — 'okay, what if we compromise...'", {"enforcement": 2}),
        ("Completely retract: 'I'm sorry, forget I said anything'", {"enforcement": 1})
    ]),
    tier="core", cg="enf_confrontation_1", opacity=0.7))

questions.append(q("enforcement", "partner_perspective",
    "Think about the person closest to you. If asked, would they say your boundaries are consistently enforced?",
    opts([
        ("Yes — they know my lines and they know I hold them", {"enforcement": 5}),
        ("Mostly — I'm consistent about the important ones", {"enforcement": 4}),
        ("Probably not — they'd say I set them but don't follow through", {"enforcement": 2}),
        ("They'd say 'what boundaries?'", {"enforcement": 1})
    ]),
    tier="consistency_check", cg="enf_followthrough_1", opacity=0.65))

questions.append(q("enforcement", "behavioral_recall",
    "When someone guilts you for enforcing a boundary, how effective is the guilt at getting you to cave?",
    opts([
        ("Not effective — guilt trips are a manipulation tactic and I recognize them", {"enforcement": 5}),
        ("Mildly effective — I feel the guilt but usually hold firm", {"enforcement": 4}),
        ("Quite effective — guilt is my kryptonite", {"enforcement": 2}),
        ("Devastatingly effective — I can't maintain a boundary against guilt", {"enforcement": 1})
    ]),
    tier="core", cg="enf_confrontation_1", opacity=0.7))

questions.append(q("enforcement", "trap",
    "A well-meaning friend says 'You should be more flexible' about a boundary you hold firmly. You:",
    opts([
        ("Consider it — maybe they see something you don't", {"enforcement": 3, "flexible": 4}),
        ("Thank them but hold your position — you've thought about this", {"enforcement": 5}),
        ("Immediately doubt yourself — are your standards too high?", {"enforcement": 2}),
        ("Feel defensive and double down, even if they might have a point", {"enforcement": 3, "rigid": 4})
    ]),
    tier="trap", trap=True, cg="enf_confrontation_1", opacity=0.6))

questions.append(q("enforcement", "scenario",
    "You set a boundary at work about not answering emails after 7 PM. Your boss starts sending urgent emails at 9 PM. You:",
    opts([
        ("Don't respond until morning — the boundary applies to everyone", {"enforcement": 5}),
        ("Respond to genuinely urgent ones only, address the pattern with your boss the next day", {"enforcement": 4, "flexible": 4}),
        ("Respond to everything because you can't enforce boundaries with authority figures", {"enforcement": 1}),
        ("Respond but feel resentful, and never raise the issue directly", {"enforcement": 1})
    ]),
    tier="triangulation", cg="enf_followthrough_1", opacity=0.65))

questions.append(q("enforcement", "temporal",
    "How has your boundary enforcement changed over the years?",
    opts([
        ("I've gotten steadily better — practice makes it easier", {"enforcement": 5}),
        ("It comes and goes — I enforce well in some life chapters and poorly in others", {"enforcement": 3}),
        ("I was better at it years ago and I've gotten worse", {"enforcement": 2}),
        ("I've never been good at it — setting boundaries is easy, keeping them is where I fail", {"enforcement": 1})
    ]),
    tier="triangulation", cg="enf_followthrough_1", opacity=0.65))

questions.append(q("enforcement", "forced_choice",
    "What's the REAL reason boundaries collapse — for you specifically?",
    opts([
        ("They don't — I maintain them", {"enforcement": 5}),
        ("I'm afraid of conflict", {"enforcement": 2}),
        ("I'm afraid of being alone", {"enforcement": 1}),
        ("I'm afraid of being seen as mean or unreasonable", {"enforcement": 2})
    ]),
    tier="trap", trap=True, cg="enf_confrontation_1", opacity=0.8))


questions.append(q("flexible", "scenario",
    "Your best friend and your partner don't get along. Managing time between them, you:",
    opts([
        ("See them separately and don't force it — you can love people who don't love each other", {"flexible": 5}),
        ("Constantly try to get them in the same room hoping they'll click", {"flexible": 2, "porous": 3}),
        ("Choose one over the other — you can't handle the tension", {"flexible": 1, "rigid": 3}),
        ("Have honest conversations with both about your needs — transparent even if it's uncomfortable", {"flexible": 5})
    ]),
    tier="triangulation", cg="flex_relationship_1", opacity=0.6))

questions.append(q("flexible", "behavioral_recall",
    "When life circumstances change dramatically (new job, new city, new relationship), how well do your boundaries adapt?",
    opts([
        ("Smoothly — I recalibrate for the new context while keeping my core values", {"flexible": 5}),
        ("With a lag — I cling to old patterns for a while before adjusting", {"flexible": 3}),
        ("Badly — I either throw all boundaries out the window or cling to rigid ones that no longer fit", {"flexible": 1}),
        ("I don't notice my boundaries changing until someone points out I've either overextended or shut down", {"flexible": 2})
    ]),
    tier="consistency_check", cg="flex_adapt_1", opacity=0.65))

questions.append(q("enforcement", "scenario",
    "You catch someone lying to you about something that matters. Your response:",
    opts([
        ("Confront them directly and clearly state the consequence if trust isn't rebuilt", {"enforcement": 5}),
        ("Address it but give them a chance to explain — enforcement depends on their response", {"enforcement": 4, "flexible": 4}),
        ("Mention it indirectly and hope they get the message", {"enforcement": 2}),
        ("Say nothing but distance yourself silently — confrontation is too hard", {"enforcement": 1, "rigid": 3})
    ]),
    tier="core", cg="enf_confrontation_1", opacity=0.7))


assert len(questions) == 100, f"Expected 100, got {len(questions)}"

with open("/Users/user/personal/sb/trueassess/priv/question_bank/boundary_style.json", "w") as f:
    json.dump(questions, f, indent=2)

print(f"Boundary style: {len(questions)} questions written")
from collections import Counter
dims = Counter(q["dimension"] for q in questions)
print("Distribution:", dict(dims))
tiers = Counter(q["tier_role"] for q in questions)
print("Tiers:", dict(tiers))
types = Counter(q["question_type"] for q in questions)
print("Types:", dict(types))

# Fix: need 2 more flexible, 1 more enforcement (was short)
# Remove the assert and re-add

# Already have questions list from above, just need to append
# But since we errored, let me re-run the whole thing with the additions

