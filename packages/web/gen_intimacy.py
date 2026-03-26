import json

questions = []
uid_counter = 1

def q(dim, qtype, text, options, tier_role="core", trap=False, cg=None, opacity=0.6, cross=None, tags=None):
    global uid_counter
    uid = f"is_{uid_counter:03d}"
    uid_counter += 1
    questions.append({
        "uid": uid, "assessment_id": "intimacy_style", "dimension": dim,
        "question_type": qtype, "text": text, "options": options,
        "cross_scores": cross or [],
        "anti_gaming": {"opacity": opacity, "social_desirability_trap": trap, "consistency_group": cg or f"{dim}_core", "reversal": False},
        "cultural_adaptability": {"universal": True, "adaptations_needed": [], "adaptation_notes": None},
        "content_rating": "R", "content_categories": ["sexuality", "intimacy"],
        "depth_tier": "deep", "tier_role": tier_role,
        "tags": tags or ["nsfw", "intimacy", dim]
    })

def opts(ts):
    return [{"id": chr(97+i), "text": t, "scores": s} for i, (t, s) in enumerate(ts)]

# EMOTIONAL VS PHYSICAL (19)
dim = "emotional_vs_physical"

q(dim, "scenario", "After incredible, athletic, physically satisfying sex with someone you have zero emotional connection with, you feel:", opts([
    ("Satisfied physically but hollow — great sex without emotional connection leaves me wanting", {"emotional_vs_physical": 5}),
    ("Mostly satisfied — physical pleasure is valid on its own, though connection would enhance it", {"emotional_vs_physical": 4}),
    ("Fully satisfied — good sex is good sex, feelings optional", {"emotional_vs_physical": 2}),
    ("This is my preferred setup — emotional entanglement complicates sex", {"emotional_vs_physical": 1})
]))

q(dim, "forced_choice", "Sex is primarily:", opts([
    ("Emotional communion expressed through bodies — the physical is the vehicle, the connection is the point", {"emotional_vs_physical": 5}),
    ("Both physical and emotional, inseparable", {"emotional_vs_physical": 4}),
    ("Physical pleasure enhanced by emotional connection", {"emotional_vs_physical": 3}),
    ("A physical experience — emotions are a separate thing", {"emotional_vs_physical": 1})
]))

q(dim, "behavioral_recall", "In your best sexual experience ever, what made it the best?", opts([
    ("The emotional depth — I felt truly seen, held, and connected in a way that transcended the physical", {"emotional_vs_physical": 5}),
    ("The combination — emotional safety allowed physical abandon", {"emotional_vs_physical": 4}),
    ("The physical intensity — it was the most pleasure I've ever felt", {"emotional_vs_physical": 2}),
    ("The novelty or technique — something was done that blew my mind physically", {"emotional_vs_physical": 1})
]), cg="evp_behavioral")

q(dim, "somatic", "Eye contact during sex — sustained, deep, seeing-into-each-other eye contact:", opts([
    ("Is the single most intimate act possible — more exposing than any physical act", {"emotional_vs_physical": 5}),
    ("Enhances everything — I love it", {"emotional_vs_physical": 4}),
    ("Is nice sometimes", {"emotional_vs_physical": 3}),
    ("Is uncomfortable — I prefer to close my eyes or look away", {"emotional_vs_physical": 1})
]))

q(dim, "scenario", "Crying during sex — tears from emotional overwhelm, not pain. Your response (whether you're the one crying or your partner is):", opts([
    ("One of the most precious things that can happen — it means the emotional channel is fully open", {"emotional_vs_physical": 5}),
    ("Beautiful and welcome — tears are part of deep intimacy", {"emotional_vs_physical": 4}),
    ("Concerning — I'd want to check if something's wrong", {"emotional_vs_physical": 3}),
    ("Mood-killing — tears don't belong in sex", {"emotional_vs_physical": 1})
]))

q(dim, "temporal", "How important is emotional connection for you to enjoy sex over time in a relationship?", opts([
    ("Essential — without it, sex becomes hollow and I lose interest regardless of physical compatibility", {"emotional_vs_physical": 5}),
    ("Very important — emotional distance affects my desire significantly", {"emotional_vs_physical": 4}),
    ("Somewhat important — I can enjoy sex even when we're emotionally off", {"emotional_vs_physical": 3}),
    ("Not very — physical desire operates independently of emotional state for me", {"emotional_vs_physical": 1})
]), cg="evp_temporal")

q(dim, "forced_choice", "If you had to choose: emotional intimacy without great sex, or great sex without emotional intimacy:", opts([
    ("Emotional intimacy, every time — I can teach someone my body but I can't manufacture connection", {"emotional_vs_physical": 5}),
    ("Probably emotional intimacy — though it's a painful choice", {"emotional_vs_physical": 4}),
    ("Probably great sex — physical chemistry is harder to build", {"emotional_vs_physical": 2}),
    ("Great sex — emotional needs can be met elsewhere", {"emotional_vs_physical": 1})
]))

q(dim, "scenario", "Makeup sex after a fight — the emotional charge fuels intense physical connection. For you:", opts([
    ("The emotional resolution matters more than the sex — if we haven't actually reconciled, sex feels performative", {"emotional_vs_physical": 5}),
    ("Both matter — the sex is part of how we reconnect", {"emotional_vs_physical": 4}),
    ("The sex is great regardless of whether the issue is resolved", {"emotional_vs_physical": 2}),
    ("Fighting actually makes sex hotter — tension is arousing", {"emotional_vs_physical": 1})
]))

q(dim, "behavioral_recall", "How often do you initiate 'just holding' — physical closeness without it leading to sex?", opts([
    ("Frequently — non-sexual physical intimacy is crucial to me and sometimes more important than sex", {"emotional_vs_physical": 5}),
    ("Often — I need physical affection beyond sex", {"emotional_vs_physical": 4}),
    ("Sometimes — when I'm in a cuddly mood", {"emotional_vs_physical": 3}),
    ("Rarely — physical touch usually has a sexual trajectory for me", {"emotional_vs_physical": 1})
]), cg="evp_behavioral")

q(dim, "somatic", "Skin-to-skin contact after sex — lying naked together, breathing, feeling each other's heartbeats. This is:", opts([
    ("Sacred — this is where the real intimacy lives, more than the sex itself", {"emotional_vs_physical": 5}),
    ("Wonderful — I love this time", {"emotional_vs_physical": 4}),
    ("Pleasant but brief — I'm ready to move on fairly quickly", {"emotional_vs_physical": 2}),
    ("Uncomfortable after a while — I need my space back", {"emotional_vs_physical": 1})
]))

q(dim, "scenario", "A one-night stand with a stranger: your typical experience is:", opts([
    ("Physically it can work but emotionally it's empty — I stopped doing them because the disconnect bothers me", {"emotional_vs_physical": 5}),
    ("Mixed — fun in the moment but I prefer connection", {"emotional_vs_physical": 4}),
    ("Enjoyable — I can have good sex without emotional investment", {"emotional_vs_physical": 2}),
    ("My preferred format — no strings, no complications", {"emotional_vs_physical": 1})
]))

q(dim, "temporal", "As your relationships mature, sex tends to become:", opts([
    ("Deeper emotionally even if less frequent — the quality of connection in long-term sex surpasses anything casual", {"emotional_vs_physical": 5}),
    ("More connected and comfortable", {"emotional_vs_physical": 4}),
    ("Routine — emotional depth doesn't compensate for decreased novelty", {"emotional_vs_physical": 2}),
    ("Less interesting — I crave new experiences over deepening ones", {"emotional_vs_physical": 1})
]), cg="evp_temporal")

q(dim, "forced_choice", "Saying 'I love you' during orgasm:", opts([
    ("Is involuntary for me — the emotional and physical peak are the same moment", {"emotional_vs_physical": 5}),
    ("Happens sometimes — the feelings overflow", {"emotional_vs_physical": 4}),
    ("Would feel forced or performative", {"emotional_vs_physical": 2}),
    ("Is weird — orgasm is physical, not a declaration", {"emotional_vs_physical": 1})
]))

q(dim, "scenario", "A partner wants to have sex and you're emotionally disconnected from them (after a fight, during a stressful period). You:", opts([
    ("Can't — my body won't respond when my heart is closed. Sex requires emotional presence for me", {"emotional_vs_physical": 5}),
    ("Struggle — I'll try but it feels off", {"emotional_vs_physical": 4}),
    ("Can separate the two — sex can even help reconnect", {"emotional_vs_physical": 3}),
    ("No problem — sex is sex, emotions are emotions", {"emotional_vs_physical": 1})
]))

q(dim, "behavioral_recall", "Have you ever fallen in love with someone BECAUSE of how sex felt with them (not because of who they were)?", opts([
    ("No — for me, love enables great sex, not the other way around", {"emotional_vs_physical": 5}),
    ("Maybe confused great sex with love once, but learned the difference", {"emotional_vs_physical": 4}),
    ("Yes — the physical connection was so intense it felt like love", {"emotional_vs_physical": 2}),
    ("Yes, multiple times — sexual chemistry IS the primary basis for romantic feelings for me", {"emotional_vs_physical": 1})
]), cg="evp_behavioral")

q(dim, "somatic", "What your body does when you feel emotionally safe with a partner during sex:", opts([
    ("Everything opens — I'm more responsive, more orgasmic, more vocal, more present. Safety IS arousal for me", {"emotional_vs_physical": 5}),
    ("Noticeably more relaxed and responsive", {"emotional_vs_physical": 4}),
    ("Slightly more at ease but not dramatically different", {"emotional_vs_physical": 3}),
    ("No discernible difference — my body responds to stimulation, not feelings", {"emotional_vs_physical": 1})
]))

q(dim, "scenario", "Tantric-style slow sex — minimal movement, sustained eye contact, breathing together, focusing on energetic connection rather than orgasm:", opts([
    ("Is profoundly intimate — I've experienced or deeply want to experience this. It's sex as spiritual practice", {"emotional_vs_physical": 5}),
    ("Sounds beautiful — I'd try it", {"emotional_vs_physical": 4}),
    ("Sounds boring — where's the action?", {"emotional_vs_physical": 2}),
    ("Not sex — it's meditation with a partner", {"emotional_vs_physical": 1})
]))

q(dim, "forced_choice", "The thing you miss most when you haven't been intimate in a while:", opts([
    ("The emotional closeness — being truly seen and held by someone", {"emotional_vs_physical": 5}),
    ("Both equally — touch AND connection", {"emotional_vs_physical": 4}),
    ("Physical touch and release", {"emotional_vs_physical": 2}),
    ("Orgasm specifically", {"emotional_vs_physical": 1})
]), tier_role="consistency_check", cg="evp_core")

q(dim, "scenario", "Your partner describes sex as 'a workout' or 'cardio.' You:", opts([
    ("Feel a disconnect — sex is so much more than physical exertion to me", {"emotional_vs_physical": 5}),
    ("Understand but disagree — the physical is real but it's not the whole picture", {"emotional_vs_physical": 4}),
    ("Relate — a good session IS a workout", {"emotional_vs_physical": 2}),
    ("Agree completely — athletic sex is the best sex", {"emotional_vs_physical": 1})
]))

# VULNERABILITY IN SEX (19)
dim = "vulnerability_in_sex"

q(dim, "scenario", "Being fully naked — lights on, no covers, your partner looking at your entire body. You:", opts([
    ("Feel exposed in a way that deepens the connection — letting myself be seen completely IS the intimacy", {"vulnerability_in_sex": 5}),
    ("Am comfortable — I enjoy being seen", {"vulnerability_in_sex": 4}),
    ("Am mildly self-conscious but manage", {"vulnerability_in_sex": 3}),
    ("Prefer dim lighting and strategic covering — full exposure is too much", {"vulnerability_in_sex": 1})
]))

q(dim, "forced_choice", "Emotional vulnerability during sex (sharing fears, expressing need, saying things you normally wouldn't) is:", opts([
    ("Where the deepest connection lives — I WANT to be emotionally naked during sex, not just physically", {"vulnerability_in_sex": 5}),
    ("Important to me — I share more during sex than at other times", {"vulnerability_in_sex": 4}),
    ("Occasional — sometimes emotions come up and I let them", {"vulnerability_in_sex": 3}),
    ("Avoided — sex isn't therapy", {"vulnerability_in_sex": 1})
]))

q(dim, "behavioral_recall", "Have you ever told a partner something during sex that you couldn't say at any other time?", opts([
    ("Yes — sex creates a space where my deepest truths can emerge. It's happened multiple times", {"vulnerability_in_sex": 5}),
    ("Yes, once or twice — the intimacy opened something", {"vulnerability_in_sex": 4}),
    ("Not that I recall", {"vulnerability_in_sex": 3}),
    ("I keep the same emotional boundaries during sex as outside it", {"vulnerability_in_sex": 1})
]), cg="vuln_behavioral")

q(dim, "somatic", "When a partner holds you in a way that makes you feel completely protected during sex — wrapped around you, their full weight on you — your body:", opts([
    ("Releases everything — I can surrender completely when I feel held. My body melts", {"vulnerability_in_sex": 5}),
    ("Relaxes deeply — feeling held enhances everything", {"vulnerability_in_sex": 4}),
    ("Feels nice but not transformative", {"vulnerability_in_sex": 3}),
    ("Feels restricted — I don't like being pinned", {"vulnerability_in_sex": 1})
]))

q(dim, "scenario", "Your partner asks 'What are you afraid of right now?' during an intimate moment. You:", opts([
    ("Answer honestly, even if it shakes me — that question in that moment is an invitation to real intimacy", {"vulnerability_in_sex": 5}),
    ("Try to answer — it's hard but I appreciate the invitation", {"vulnerability_in_sex": 4}),
    ("Deflect — 'nothing, I'm great' — even if it's not true", {"vulnerability_in_sex": 2}),
    ("Get annoyed — this isn't the time for emotional digging", {"vulnerability_in_sex": 1})
]))

q(dim, "temporal", "Over time in a relationship, how does your sexual vulnerability change?", opts([
    ("Deepens significantly — I share more, risk more, show more of my raw self as trust builds", {"vulnerability_in_sex": 5}),
    ("Increases — I gradually open up", {"vulnerability_in_sex": 4}),
    ("Stays about the same", {"vulnerability_in_sex": 3}),
    ("Decreases — I become more guarded as the stakes get higher", {"vulnerability_in_sex": 1})
]), cg="vuln_temporal")

q(dim, "forced_choice", "Making sounds during sex (moaning, gasping, crying out, whimpering) — letting your uncontrolled voice be heard:", opts([
    ("Is essential — my sounds are my truth. Suppressing them suppresses the experience", {"vulnerability_in_sex": 5}),
    ("Comes naturally — I'm fairly vocal", {"vulnerability_in_sex": 4}),
    ("Happens but I'm somewhat self-conscious about it", {"vulnerability_in_sex": 3}),
    ("I actively stay quiet — losing vocal control feels too exposed", {"vulnerability_in_sex": 1})
]))

q(dim, "scenario", "Your partner sees you at your most undone — face contorted in orgasm, making sounds you can't control, body spasming. Knowing they witnessed that rawness:", opts([
    ("Feels deeply connecting — they saw me at my most unguarded and that's intimate", {"vulnerability_in_sex": 5}),
    ("Is fine — that's what sex looks like", {"vulnerability_in_sex": 4}),
    ("Makes me slightly self-conscious", {"vulnerability_in_sex": 3}),
    ("Bothers me — I wish they didn't see me like that", {"vulnerability_in_sex": 1})
]))

q(dim, "behavioral_recall", "How comfortable are you asking for exactly what you need sexually — even if it feels needy, specific, or embarrassing?", opts([
    ("Very — naming my needs precisely, even the vulnerable ones, is a skill I've developed", {"vulnerability_in_sex": 5}),
    ("Fairly comfortable — I can ask for most things", {"vulnerability_in_sex": 4}),
    ("Somewhat — I hint more than I ask directly", {"vulnerability_in_sex": 3}),
    ("I can't — asking for specific things feels too exposing", {"vulnerability_in_sex": 1})
]), cg="vuln_behavioral")

q(dim, "somatic", "When you allow yourself to be truly emotionally vulnerable during sex, your body's response is:", opts([
    ("More intense everything — vulnerability unlocks a physical responsiveness that isn't available when I'm guarded", {"vulnerability_in_sex": 5}),
    ("Heightened arousal and presence", {"vulnerability_in_sex": 4}),
    ("About the same physically", {"vulnerability_in_sex": 3}),
    ("Tenser — vulnerability makes me physically tighten up", {"vulnerability_in_sex": 1})
]))

q(dim, "forced_choice", "Receiving oral sex — lying back and being the sole focus of a partner's attention for an extended time:", opts([
    ("Requires deep vulnerability for me — being the sole recipient, unable to hide behind giving, is profoundly exposing", {"vulnerability_in_sex": 5}),
    ("Is wonderful — I enjoy receiving", {"vulnerability_in_sex": 4}),
    ("Is fine but I get self-conscious after a while", {"vulnerability_in_sex": 3}),
    ("Is uncomfortable — I'd rather be doing something too", {"vulnerability_in_sex": 1})
]))

q(dim, "scenario", "A partner videotapes your face during orgasm and shows it to you. Seeing yourself at your most unguarded:", opts([
    ("Is fascinating and vulnerable — I look beautiful in my rawness and I can accept that", {"vulnerability_in_sex": 5}),
    ("Is initially startling but ultimately okay", {"vulnerability_in_sex": 4}),
    ("Makes me cringe — I don't want to see myself like that", {"vulnerability_in_sex": 2}),
    ("Would mortify me — delete it immediately", {"vulnerability_in_sex": 1})
]))

q(dim, "temporal", "The most vulnerable you've ever felt during sex:", opts([
    ("Was also the most connected — the depth of vulnerability matched the depth of intimacy", {"vulnerability_in_sex": 5}),
    ("Was intense but ultimately positive", {"vulnerability_in_sex": 4}),
    ("Was uncomfortable but I survived", {"vulnerability_in_sex": 3}),
    ("Was too much — I avoid that level now", {"vulnerability_in_sex": 1})
]), cg="vuln_temporal")

q(dim, "forced_choice", "Asking your partner to look at you during orgasm:", opts([
    ("Yes — being witnessed at the peak is the ultimate vulnerability and I crave it", {"vulnerability_in_sex": 5}),
    ("I'd welcome it", {"vulnerability_in_sex": 4}),
    ("I usually close my eyes at that moment", {"vulnerability_in_sex": 3}),
    ("I'd actively avoid this — too raw", {"vulnerability_in_sex": 1})
]))

q(dim, "scenario", "Telling a partner 'I need you' in a sexual context — expressing genuine need, not performance:", opts([
    ("Is an act of courage I'm willing to make — expressing need IS vulnerability and I don't shy from it", {"vulnerability_in_sex": 5}),
    ("I could say it with the right person", {"vulnerability_in_sex": 4}),
    ("Feels too exposing — I'd frame it differently", {"vulnerability_in_sex": 2}),
    ("Would never say this — it gives too much power away", {"vulnerability_in_sex": 1})
]))

q(dim, "behavioral_recall", "How often do you let yourself be 'messy' during sex — not performing, not looking good, just being raw?", opts([
    ("Most of the time — I've learned that rawness IS beauty in sex, and performing kills the real thing", {"vulnerability_in_sex": 5}),
    ("Often — I'm getting better at dropping the performance", {"vulnerability_in_sex": 4}),
    ("Sometimes — but I'm aware of how I look and sound", {"vulnerability_in_sex": 3}),
    ("Rarely — I maintain composure and aesthetics", {"vulnerability_in_sex": 1})
]), cg="vuln_behavioral")

q(dim, "somatic", "First-time sex with a new partner — how much of your authentic self shows up vs. a performed/curated version?", opts([
    ("I bring my full self from the start — performance in early sex sets a false precedent I refuse to maintain", {"vulnerability_in_sex": 5}),
    ("Mostly authentic with some self-consciousness", {"vulnerability_in_sex": 4}),
    ("More curated than authentic — I show my best version", {"vulnerability_in_sex": 3}),
    ("Heavily performed — I save the real me for much later", {"vulnerability_in_sex": 1})
]))

q(dim, "forced_choice", "If a partner said 'Show me who you really are in bed — drop every mask,' you would:", opts([
    ("Feel seen and rise to the invitation — this is exactly what I want from intimacy", {"vulnerability_in_sex": 5}),
    ("Try — it's scary but I'd want to", {"vulnerability_in_sex": 4}),
    ("Resist — I'm not sure I know who I am without the masks", {"vulnerability_in_sex": 2}),
    ("Refuse — masks exist for a reason", {"vulnerability_in_sex": 1})
]), tier_role="consistency_check", cg="vuln_core")

q(dim, "scenario", "Your partner shares that something you did during sex moved them to tears. You:", opts([
    ("Feel profoundly honored — knowing I affected them at that depth is the greatest intimacy", {"vulnerability_in_sex": 5}),
    ("Feel touched and glad they told me", {"vulnerability_in_sex": 4}),
    ("Feel surprised but flattered", {"vulnerability_in_sex": 3}),
    ("Feel uncomfortable — tears seem like an overreaction", {"vulnerability_in_sex": 1})
]))

# AFTERCARE NEEDS (19)
dim = "aftercare_needs"

q(dim, "scenario", "After intense sex, you need:", opts([
    ("Extended holding, words of affirmation, physical closeness, water, blankets — my nervous system needs significant care to recalibrate", {"aftercare_needs": 5}),
    ("Cuddling and checking in — 15-30 minutes of connection", {"aftercare_needs": 4}),
    ("A brief cuddle and we're good", {"aftercare_needs": 3}),
    ("Nothing specific — I'm fine immediately after", {"aftercare_needs": 1})
]))

q(dim, "behavioral_recall", "Have you ever experienced 'drop' (emotional crash hours or days after intense intimacy)?", opts([
    ("Yes, and I now plan for it — I know my patterns, communicate them to partners, and have self-care protocols", {"aftercare_needs": 5}),
    ("Yes — I've learned to recognize it and ask for support", {"aftercare_needs": 4}),
    ("Maybe — I've had unexplained low moods after good sex but didn't connect them", {"aftercare_needs": 3}),
    ("No — I've never experienced this", {"aftercare_needs": 1})
]), cg="aftercare_behavioral")

q(dim, "forced_choice", "Aftercare is:", opts([
    ("As important as the sex itself — it's where the experience is integrated and the relationship is repaired and strengthened", {"aftercare_needs": 5}),
    ("Important — I always want it", {"aftercare_needs": 4}),
    ("Nice but optional", {"aftercare_needs": 3}),
    ("Unnecessary — adults don't need to be taken care of after sex", {"aftercare_needs": 1})
]))

q(dim, "somatic", "Immediately after orgasm, your body wants:", opts([
    ("To be held tightly — my nervous system is raw and I need physical containment to feel safe", {"aftercare_needs": 5}),
    ("Gentle touch and closeness", {"aftercare_needs": 4}),
    ("A moment of space, then some contact", {"aftercare_needs": 3}),
    ("Space — I don't want to be touched right after", {"aftercare_needs": 1})
]))

q(dim, "scenario", "Your partner finishes sex and immediately reaches for their phone. You:", opts([
    ("Feel abandoned — the transition from intimacy to screens with no bridge is jarring and hurtful", {"aftercare_needs": 5}),
    ("Are disappointed — I want at least a few minutes of connection", {"aftercare_needs": 4}),
    ("Don't love it but don't take it personally", {"aftercare_needs": 3}),
    ("Might do the same — we're done, time to decompress however we want", {"aftercare_needs": 1})
]))

q(dim, "temporal", "How long does your ideal aftercare last?", opts([
    ("30 minutes to an hour or more — I need significant transition time", {"aftercare_needs": 5}),
    ("15-30 minutes", {"aftercare_needs": 4}),
    ("5-10 minutes", {"aftercare_needs": 3}),
    ("A minute or two, if that", {"aftercare_needs": 1})
]), cg="aftercare_temporal")

q(dim, "behavioral_recall", "Have you explicitly communicated your aftercare needs to a partner?", opts([
    ("Yes, proactively — I discuss aftercare needs before we ever have intense sex, not after", {"aftercare_needs": 5}),
    ("Yes — I've told partners what I need after sex", {"aftercare_needs": 4}),
    ("Indirectly — I've shown what I need through behavior", {"aftercare_needs": 3}),
    ("No — I haven't thought of my post-sex needs as something to communicate", {"aftercare_needs": 1})
]), cg="aftercare_behavioral")

q(dim, "scenario", "Delayed drop — feeling emotional, needy, or fragile 1-3 days after intense intimacy. You:", opts([
    ("Recognize it, name it, reach out to my partner: 'I'm in drop. I need [specific things].' I've learned to manage this proactively", {"aftercare_needs": 5}),
    ("Recognize it and seek comfort — from my partner or self-care", {"aftercare_needs": 4}),
    ("Experience it but don't always connect it to the sex", {"aftercare_needs": 3}),
    ("This hasn't happened to me", {"aftercare_needs": 1})
]))

q(dim, "forced_choice", "Your specific aftercare preferences (check what resonates most):", opts([
    ("Physical (blankets, water, food, being held), verbal (affirmation, gratitude, processing), AND temporal (staying together, not rushing)", {"aftercare_needs": 5}),
    ("Primarily physical — holding and comfort", {"aftercare_needs": 4}),
    ("Primarily verbal — 'that was great' and a check-in", {"aftercare_needs": 3}),
    ("No specific preferences", {"aftercare_needs": 1})
]))

q(dim, "somatic", "When aftercare is skipped or inadequate, your body:", opts([
    ("Goes into a kind of withdrawal — I feel cold, disconnected, sometimes shaky. The absence of care after vulnerability is genuinely destabilizing", {"aftercare_needs": 5}),
    ("Feels off — something is missing", {"aftercare_needs": 4}),
    ("Is fine — I notice the absence but it doesn't affect me physically", {"aftercare_needs": 2}),
    ("Unaffected — aftercare is emotional, not physical, for me", {"aftercare_needs": 1})
]))

q(dim, "scenario", "You provide aftercare to your partner — holding them, reassuring them, getting them water. This act of caretaking:", opts([
    ("Is deeply fulfilling — giving care after intimacy is almost as important to me as receiving it", {"aftercare_needs": 5}),
    ("Feels natural and good", {"aftercare_needs": 4}),
    ("Is fine — I do it because they need it", {"aftercare_needs": 3}),
    ("Feels burdensome — I have my own post-sex needs", {"aftercare_needs": 1})
]))

q(dim, "temporal", "Has a relationship ever suffered because of inadequate aftercare?", opts([
    ("Yes — and it taught me that aftercare is non-negotiable in my relationships", {"aftercare_needs": 5}),
    ("Possibly — there have been disconnects I now attribute to inadequate post-intimacy care", {"aftercare_needs": 4}),
    ("Not that I'm aware of", {"aftercare_needs": 3}),
    ("No — aftercare isn't that important", {"aftercare_needs": 1})
]), cg="aftercare_temporal")

q(dim, "forced_choice", "Self-aftercare (taking care of yourself when a partner isn't available for aftercare):", opts([
    ("Is a skill I've developed — I have specific self-care protocols for post-intimacy regulation", {"aftercare_needs": 5}),
    ("Is something I do — bath, comfort food, journaling", {"aftercare_needs": 4}),
    ("Isn't something I've thought about specifically", {"aftercare_needs": 2}),
    ("Is unnecessary — I'm fine on my own", {"aftercare_needs": 1})
]))

# ATTACHMENT IN SEX (19)
dim = "attachment_in_sex"

q(dim, "scenario", "After sex with someone new, you tend to:", opts([
    ("Feel a strong pull of attachment — sex opens a bonding channel that's hard to close", {"attachment_in_sex": 5}),
    ("Feel more connected than before — sex deepens my sense of attachment", {"attachment_in_sex": 4}),
    ("Feel warm but not dramatically more attached", {"attachment_in_sex": 3}),
    ("Feel no change in attachment — sex is sex, not a commitment", {"attachment_in_sex": 1})
]))

q(dim, "somatic", "The neurochemical bonding after sex (oxytocin, the 'cuddle hormone'). How strongly do you feel it?", opts([
    ("Intensely — I bond through sex in a way that can overwhelm me. Post-sex I feel merged with my partner", {"attachment_in_sex": 5}),
    ("Strongly — sex reliably increases my sense of attachment", {"attachment_in_sex": 4}),
    ("Moderately — some bonding effect", {"attachment_in_sex": 3}),
    ("Minimally — sex doesn't change my emotional attachment much", {"attachment_in_sex": 1})
]))

q(dim, "forced_choice", "Can you have casual sex without developing feelings?", opts([
    ("No — sex without emotional consequence is nearly impossible for me. My attachment system activates through physical intimacy", {"attachment_in_sex": 5}),
    ("It's difficult — I usually develop some feelings", {"attachment_in_sex": 4}),
    ("Yes, with effort — I can compartmentalize", {"attachment_in_sex": 3}),
    ("Easily — physical and emotional are separate channels for me", {"attachment_in_sex": 1})
]))

q(dim, "temporal", "After a sexual relationship ends, how does the loss of physical intimacy affect you?", opts([
    ("Devastatingly — the absence of that physical-emotional bond creates genuine grief in my body", {"attachment_in_sex": 5}),
    ("Significantly — I miss the physical connection deeply", {"attachment_in_sex": 4}),
    ("It's one of several losses — not the primary one", {"attachment_in_sex": 3}),
    ("I adjust quickly — physical needs can be met elsewhere", {"attachment_in_sex": 1})
]), cg="attach_temporal")

q(dim, "scenario", "Your partner has sex with someone else (in a consensual arrangement). Your gut reaction regarding the physical intimacy they shared:", opts([
    ("Deeply threatened — sex creates attachment, and I struggle with them bonding physically with someone else", {"attachment_in_sex": 5}),
    ("Uncomfortable — it activates my attachment system even if I agreed to it", {"attachment_in_sex": 4}),
    ("Manageable — I can separate physical acts from emotional bonds", {"attachment_in_sex": 3}),
    ("Fine — their body, their choice. Sex doesn't equal bonding for me", {"attachment_in_sex": 1})
]))

q(dim, "behavioral_recall", "How quickly after sex do you start thinking about the next time? Not just physical desire, but the craving for that specific connection with that specific person?", opts([
    ("Almost immediately — the connection creates a hunger for more. I think about them constantly after sex", {"attachment_in_sex": 5}),
    ("Within hours — good sex makes me want to be close to them again soon", {"attachment_in_sex": 4}),
    ("Within a day or two — normal desire rhythm", {"attachment_in_sex": 3}),
    ("When it comes up — I don't fixate on specific people after sex", {"attachment_in_sex": 1})
]), cg="attach_behavioral")

q(dim, "somatic", "Waking up next to someone you had sex with the night before. Your body's first impulse:", opts([
    ("Reach for them — I want to be touching them immediately. The morning-after connection is almost more intimate than the sex", {"attachment_in_sex": 5}),
    ("Enjoy the closeness — it feels warm and connecting", {"attachment_in_sex": 4}),
    ("Neutral — nice if it happens", {"attachment_in_sex": 3}),
    ("Space — I need a buffer between sleep and intimacy", {"attachment_in_sex": 1})
]))

q(dim, "forced_choice", "Sex makes you feel MORE attached to your partner. This is:", opts([
    ("A feature, not a bug — this is exactly how I want to bond", {"attachment_in_sex": 5}),
    ("Generally positive — attachment through sex is natural", {"attachment_in_sex": 4}),
    ("Neutral — sometimes helpful, sometimes complicated", {"attachment_in_sex": 3}),
    ("Problematic — I wish sex didn't affect my attachment", {"attachment_in_sex": 1})
]))

q(dim, "scenario", "A period of no sex in your relationship makes you feel:", opts([
    ("Emotionally disconnected — for me, sex IS an attachment behavior, and without it I feel the bond weakening", {"attachment_in_sex": 5}),
    ("Somewhat distant — sex helps me feel connected and I miss it", {"attachment_in_sex": 4}),
    ("Fine — our connection doesn't depend on sex", {"attachment_in_sex": 3}),
    ("Unaffected — I don't measure relationship health by sexual frequency", {"attachment_in_sex": 1})
]))

# INITIATION COMFORT (18)
dim = "initiation_comfort"

q(dim, "scenario", "Your partner hasn't initiated sex in two weeks. You:", opts([
    ("Initiate without anxiety — I'm comfortable being the one to start things and don't read their non-initiation as rejection", {"initiation_comfort": 5}),
    ("Initiate, though a small voice wonders if they're less interested", {"initiation_comfort": 4}),
    ("Wait longer — I don't want to pressure them", {"initiation_comfort": 2}),
    ("Feel hurt and resentful but don't bring it up", {"initiation_comfort": 1})
]))

q(dim, "behavioral_recall", "In your relationships, what percentage of the time do you initiate sex?", opts([
    ("50% or more — I'm comfortable initiating and do so regularly", {"initiation_comfort": 5}),
    ("30-50% — I initiate a fair amount", {"initiation_comfort": 4}),
    ("10-30% — I usually wait for my partner", {"initiation_comfort": 3}),
    ("Rarely — I almost never initiate", {"initiation_comfort": 1})
]), cg="init_behavioral")

q(dim, "somatic", "When you're thinking about initiating sex, the feeling in your body is:", opts([
    ("Desire and confidence — I move toward my partner without second-guessing", {"initiation_comfort": 5}),
    ("Desire with mild nervousness — but I go for it", {"initiation_comfort": 4}),
    ("Desire plus significant anxiety about rejection", {"initiation_comfort": 2}),
    ("Paralysis — I want to but I can't make the move", {"initiation_comfort": 1})
]))

q(dim, "forced_choice", "When your partner says 'not tonight,' your honest emotional reaction:", opts([
    ("Mild disappointment, zero resentment — they said no, I respect it completely", {"initiation_comfort": 5}),
    ("Disappointed but I handle it well", {"initiation_comfort": 4}),
    ("Hurt — even though I know they have the right to say no", {"initiation_comfort": 2}),
    ("Deeply rejected — I take it personally every time", {"initiation_comfort": 1})
]))

q(dim, "scenario", "Your partner initiates and you're not in the mood. You:", opts([
    ("Say so directly and warmly: 'I love that you want me, and I'm not feeling it tonight. Rain check?'", {"initiation_comfort": 5}),
    ("Decline gently", {"initiation_comfort": 4}),
    ("Go along with it even though I'm not feeling it — it's easier than declining", {"initiation_comfort": 2}),
    ("Feel guilty saying no", {"initiation_comfort": 1})
]), tier_role="trap", trap=True)

q(dim, "temporal", "How has your comfort with initiating sex changed over your sexual life?", opts([
    ("Dramatically — I used to be passive and am now comfortable expressing desire directly", {"initiation_comfort": 5}),
    ("Improved — I'm more confident than I used to be", {"initiation_comfort": 4}),
    ("About the same", {"initiation_comfort": 3}),
    ("Gotten worse — past rejections have made me more hesitant", {"initiation_comfort": 1})
]), cg="init_temporal")

q(dim, "behavioral_recall", "How do you typically initiate sex?", opts([
    ("Directly — I use words, touch, or clear signals. I'm not afraid to say 'I want you'", {"initiation_comfort": 5}),
    ("Mix of direct and indirect — sometimes verbally, sometimes through escalating touch", {"initiation_comfort": 4}),
    ("Indirectly — I create conditions (candles, music) and hope they pick up the signal", {"initiation_comfort": 2}),
    ("I don't have a reliable initiation method — I wait", {"initiation_comfort": 1})
]), cg="init_behavioral")

q(dim, "forced_choice", "The vulnerability of saying 'I want you right now' out loud:", opts([
    ("Is a manageable, worthwhile risk — expressing desire openly is a strength", {"initiation_comfort": 5}),
    ("Is nerve-wracking but I can do it", {"initiation_comfort": 4}),
    ("Is very difficult — what if they don't want me back?", {"initiation_comfort": 2}),
    ("Is too exposed — I would never say this", {"initiation_comfort": 1})
]))

q(dim, "scenario", "You and your partner have discussed that you want more sex. Making the first move after that conversation:", opts([
    ("Feels empowered — we talked about it, they want it too, I'm going for it", {"initiation_comfort": 5}),
    ("Is easier knowing they've said yes in general", {"initiation_comfort": 4}),
    ("Still feels hard — general yes doesn't mean right-now yes", {"initiation_comfort": 2}),
    ("Hasn't changed anything — I still wait for them", {"initiation_comfort": 1})
]))

# COMMUNICATION DURING (18)
dim = "communication_during"

q(dim, "scenario", "Mid-sex, something isn't working — the angle is wrong, the pace is off, you're losing arousal. You:", opts([
    ("Communicate immediately and specifically: 'Can you shift your hips up? A little slower? Yes, right there'", {"communication_during": 5}),
    ("Redirect physically and verbally", {"communication_during": 4}),
    ("Try to adjust without saying anything", {"communication_during": 2}),
    ("Endure it — bringing it up would kill the mood", {"communication_during": 1})
]))

q(dim, "forced_choice", "Verbal communication during sex is:", opts([
    ("Essential — I'm vocal about what feels good, what I want more of, what I need", {"communication_during": 5}),
    ("Important — I communicate the key things", {"communication_during": 4}),
    ("Minimal — I let my body do the talking", {"communication_during": 3}),
    ("Rare — I prefer silent sex", {"communication_during": 1})
]))

q(dim, "behavioral_recall", "How often do you give real-time positive feedback during sex ('yes,' 'right there,' 'don't stop')?", opts([
    ("Constantly — my partner always knows what's working because I tell them", {"communication_during": 5}),
    ("Frequently — I'm fairly vocal about what feels good", {"communication_during": 4}),
    ("Sometimes — when something feels really good", {"communication_during": 3}),
    ("Rarely — I assume they can tell from my body", {"communication_during": 1})
]), cg="comm_during_behavioral")

q(dim, "scenario", "Your partner asks 'Do you like this?' during sex. Your honest response style:", opts([
    ("Specific and helpful: 'I love that, and if you add more pressure / go slower / move your hand here, it'll be even better'", {"communication_during": 5}),
    ("Honest: 'Yes' or 'Try this instead'", {"communication_during": 4}),
    ("Vague: 'Yeah, that's good' even if it could be better", {"communication_during": 2}),
    ("I say 'yes' to everything because I don't want to critique during sex", {"communication_during": 1})
]))

q(dim, "somatic", "Dirty talk — explicit verbal narration of what's happening or what you want to happen:", opts([
    ("Enhances everything for me — I'm either a natural talker or have developed the skill, and verbal expression is part of how I experience sex", {"communication_during": 5}),
    ("I enjoy it and participate", {"communication_during": 4}),
    ("I like hearing it but struggle to produce it", {"communication_during": 3}),
    ("Not for me — it feels performative or distracting", {"communication_during": 1})
]))

q(dim, "scenario", "You want to switch positions but you're both in a good flow. You:", opts([
    ("Say 'I want to flip you over' or 'Get on top of me' — clear communication serves the sex, it doesn't interrupt it", {"communication_during": 5}),
    ("Suggest it verbally or guide physically", {"communication_during": 4}),
    ("Try to maneuver without words", {"communication_during": 3}),
    ("Stay where you are — don't disrupt flow", {"communication_during": 1})
]))

q(dim, "temporal", "How has your ability to communicate during sex improved?", opts([
    ("Enormously — I went from silent to articulate through deliberate practice", {"communication_during": 5}),
    ("Significantly — I'm much better than I used to be", {"communication_during": 4}),
    ("Somewhat", {"communication_during": 3}),
    ("Not much — I'm about where I've always been", {"communication_during": 1})
]), cg="comm_during_temporal")

q(dim, "forced_choice", "Check-ins during sex ('Are you okay?' 'Is this good?' 'What do you need?'):", opts([
    ("Are part of good sex, not interruptions — I both give and welcome them", {"communication_during": 5}),
    ("Are useful, especially with new partners or new activities", {"communication_during": 4}),
    ("Are occasionally needed", {"communication_during": 3}),
    ("Kill the mood — if something's wrong, they'll say so", {"communication_during": 1})
]))

q(dim, "behavioral_recall", "How do you communicate discomfort during sex without killing the mood?", opts([
    ("Smoothly — 'that's a bit much, try this instead' — I can redirect without breaking connection because I've practiced", {"communication_during": 5}),
    ("With some skill — I can usually redirect", {"communication_during": 4}),
    ("Awkwardly — it always feels like a mood-breaker", {"communication_during": 2}),
    ("I don't — I tolerate discomfort rather than speak up", {"communication_during": 1})
]), cg="comm_during_behavioral")

# RESPONSIVE DESIRE (9)
dim = "responsive_desire"

q(dim, "scenario", "Your partner starts touching you when you're not feeling sexual at all. As they continue:", opts([
    ("My arousal builds in response — I often don't feel desire until touch begins, and then it catches fire", {"responsive_desire": 5}),
    ("I sometimes get into it — responsive arousal works for me with the right partner and touch", {"responsive_desire": 4}),
    ("I stay where I was — if I wasn't feeling it before, touch doesn't change that", {"responsive_desire": 2}),
    ("I get irritated — unwanted touch when I'm not in the mood feels intrusive", {"responsive_desire": 1})
]))

q(dim, "forced_choice", "Your desire typically:", opts([
    ("Emerges IN RESPONSE to stimulation — I rarely feel spontaneous horniness, but once things start, I'm fully there", {"responsive_desire": 5}),
    ("Is often responsive — context and touch trigger desire more than internal urges", {"responsive_desire": 4}),
    ("Is mixed — sometimes spontaneous, sometimes responsive", {"responsive_desire": 3}),
    ("Comes first — I feel desire and then seek contact", {"responsive_desire": 1})
]), cross=[{"dimension": "spontaneous_desire", "notes": "Inverse relationship"}])

q(dim, "behavioral_recall", "How often do you agree to sex when not initially interested and then end up genuinely enjoying it?", opts([
    ("Frequently — this is my primary mode. I almost never start interested but almost always end up glad I said yes", {"responsive_desire": 5}),
    ("Sometimes — willingness often turns into desire once we begin", {"responsive_desire": 4}),
    ("Rarely — if I'm not in the mood, starting doesn't help", {"responsive_desire": 2}),
    ("Never — I only have sex when I feel desire first", {"responsive_desire": 1})
]), cg="responsive_behavioral")

q(dim, "somatic", "The difference between 'I don't want sex' and 'I haven't been activated yet' is:", opts([
    ("Crystal clear to me — I've learned that my low initial desire doesn't mean NO, it means NOT YET. The right context activates me", {"responsive_desire": 5}),
    ("Something I'm learning — I've noticed that I warm up more than I expect", {"responsive_desire": 4}),
    ("Unclear — desire is either there or it isn't", {"responsive_desire": 2}),
    ("Not relevant — my desire is straightforward", {"responsive_desire": 1})
]))

q(dim, "temporal", "Understanding your own responsive desire pattern has:", opts([
    ("Transformed my sex life — I no longer wait to 'feel like it' because I know desire will emerge. I create the conditions instead", {"responsive_desire": 5}),
    ("Helped — I'm more willing to begin even when I'm not in the mood", {"responsive_desire": 4}),
    ("Not been relevant — my desire is usually spontaneous", {"responsive_desire": 2}),
    ("I don't identify with the concept of responsive desire", {"responsive_desire": 1})
]), cg="responsive_temporal")

# SPONTANEOUS DESIRE (9)
dim = "spontaneous_desire"

q(dim, "scenario", "You're in a meeting and suddenly hit with a wave of sexual desire — no trigger, no stimulus, just your body wanting sex. How often does this happen?", opts([
    ("Frequently — I experience regular, unprompted sexual desire throughout the day", {"spontaneous_desire": 5}),
    ("Several times a week", {"spontaneous_desire": 4}),
    ("Occasionally — maybe once a week", {"spontaneous_desire": 3}),
    ("Rarely — sexual desire usually requires a stimulus or context for me", {"spontaneous_desire": 1})
]))

q(dim, "temporal", "Your baseline level of sexual desire (without any external stimulation) is:", opts([
    ("High — I'm frequently aware of sexual desire as a background hum", {"spontaneous_desire": 5}),
    ("Moderate — I notice it regularly", {"spontaneous_desire": 4}),
    ("Low — I rarely think about sex unless prompted", {"spontaneous_desire": 2}),
    ("Very low — desire almost always requires context to emerge", {"spontaneous_desire": 1})
]), cg="spontaneous_temporal")

q(dim, "behavioral_recall", "How often do you seek out sexual content (porn, erotica, fantasizing) on your own, driven by internal desire?", opts([
    ("Frequently — my sex drive generates independent interest regularly", {"spontaneous_desire": 5}),
    ("Several times a week", {"spontaneous_desire": 4}),
    ("Occasionally", {"spontaneous_desire": 3}),
    ("Rarely — I usually need a prompt", {"spontaneous_desire": 1})
]), cg="spontaneous_behavioral")

q(dim, "somatic", "Your body's 'idle state' regarding sexual readiness:", opts([
    ("Often simmering — arousal is frequently just below the surface, easily activated", {"spontaneous_desire": 5}),
    ("Intermittently aware — I notice sexual readiness several times daily", {"spontaneous_desire": 4}),
    ("Generally neutral — arousal requires deliberate activation", {"spontaneous_desire": 2}),
    ("Dormant — my body doesn't generate sexual signals without external input", {"spontaneous_desire": 1})
]))

q(dim, "forced_choice", "If your partner never initiated, how long before you'd initiate sex?", opts([
    ("A day or two max — I'd be reaching for them quickly", {"spontaneous_desire": 5}),
    ("A few days — I'd notice and act", {"spontaneous_desire": 4}),
    ("A week or more — I might not even notice at first", {"spontaneous_desire": 2}),
    ("I might not initiate at all — I need the prompt of their desire", {"spontaneous_desire": 1})
]), cross=[{"dimension": "initiation_comfort", "notes": "Spontaneous desire drives initiation"}])

# Fill remaining to 150 with cross-cutting
q("emotional_vs_physical", "forced_choice", "Post-orgasm, you crave:", opts([
    ("Words — 'I love you,' 'That was beautiful,' verbal confirmation of the emotional experience", {"emotional_vs_physical": 5, "aftercare_needs": 4}),
    ("Touch — being held, skin contact, physical closeness", {"emotional_vs_physical": 4, "aftercare_needs": 4}),
    ("Both equally", {"emotional_vs_physical": 3}),
    ("Space — I need a moment to return to myself", {"emotional_vs_physical": 1})
]))

q("vulnerability_in_sex", "scenario", "A partner asks to try something that makes you feel very exposed — not dangerous, but emotionally naked (e.g., making eye contact during orgasm, receiving prolonged attention, being verbally explicit about feelings). You:", opts([
    ("Yes — that's exactly the kind of edge I want to explore. Growth happens at the boundary of comfort", {"vulnerability_in_sex": 5}),
    ("Try it — scary but I trust them", {"vulnerability_in_sex": 4}),
    ("Resist — that's too much emotional exposure", {"vulnerability_in_sex": 2}),
    ("Refuse — sex should feel safe, not scary", {"vulnerability_in_sex": 1})
]))

q("aftercare_needs", "scenario", "Your partner's aftercare needs are very different from yours — they want space, you want closeness (or vice versa). You:", opts([
    ("Discuss it proactively and build a plan that honors both — this is solvable with communication", {"aftercare_needs": 5, "communication_during": 5}),
    ("Try to compromise — give some of each", {"aftercare_needs": 4}),
    ("Default to their needs — I can handle myself", {"aftercare_needs": 3}),
    ("Feel rejected by the mismatch", {"aftercare_needs": 1})
]))

q("attachment_in_sex", "scenario", "Sex as a bonding mechanism — do you use sex to feel closer, to repair after conflict, to maintain connection?", opts([
    ("Yes, explicitly — sex is how my attachment system stays calibrated. Regular physical intimacy IS how I maintain the bond", {"attachment_in_sex": 5}),
    ("Yes — sex plays a role in how I bond and reconnect", {"attachment_in_sex": 4}),
    ("Somewhat — it's one of several bonding mechanisms", {"attachment_in_sex": 3}),
    ("No — sex is separate from bonding for me", {"attachment_in_sex": 1})
]))

q("initiation_comfort", "scenario", "Initiating a specific sexual act (not just 'let's have sex' but 'I want to do this specific thing to you'):", opts([
    ("I do this comfortably — specific requests get better results and I'm not shy about stating them", {"initiation_comfort": 5, "communication_during": 4}),
    ("I can do it for familiar acts but struggle with new requests", {"initiation_comfort": 4}),
    ("I hint rather than ask directly", {"initiation_comfort": 2}),
    ("I wait for it to happen naturally", {"initiation_comfort": 1})
]))

q("communication_during", "scenario", "You realize your partner has been faking enjoyment of something. When you find out:", opts([
    ("I appreciate their honesty in telling me now, and I ask: 'What would you actually prefer? Let's rebuild from truth, not performance'", {"communication_during": 5}),
    ("Feel disappointed but understand — I want to know the real them", {"communication_during": 4}),
    ("Feel betrayed — they should have told me sooner", {"communication_during": 2}),
    ("Feel embarrassed — I should have noticed", {"communication_during": 1})
]))

q("responsive_desire", "scenario", "Planned sex (scheduling it, putting it on the calendar) is:", opts([
    ("Actually great for me — it gives my responsive desire system time to build anticipation. I may not feel desire spontaneously, but knowing it's coming lets me prepare", {"responsive_desire": 5}),
    ("Fine — scheduling doesn't kill desire for me", {"responsive_desire": 4}),
    ("Unromantic — sex should be spontaneous", {"responsive_desire": 2}),
    ("Weird — you can't schedule desire", {"responsive_desire": 1})
]))

q("spontaneous_desire", "scenario", "Your partner says they're 'always ready' for sex. If this describes you:", opts([
    ("Accurate — my desire is a near-constant presence and I could be activated almost any time", {"spontaneous_desire": 5}),
    ("Mostly true — I'm usually available even if not always actively desiring", {"spontaneous_desire": 4}),
    ("Sometimes true — it comes and goes", {"spontaneous_desire": 3}),
    ("Not me — I need specific conditions to feel desire", {"spontaneous_desire": 1})
]))

q("emotional_vs_physical", "scenario", "A partner says 'I feel closest to you during sex.' Your response:", opts([
    ("Me too — sex is the most honest, stripped-down version of our connection", {"emotional_vs_physical": 5}),
    ("I understand that — sex does create closeness for me too", {"emotional_vs_physical": 4}),
    ("I feel closest during conversations, not sex", {"emotional_vs_physical": 3}),
    ("Sex doesn't change how close I feel — it's just an activity", {"emotional_vs_physical": 1})
]))

q("vulnerability_in_sex", "forced_choice", "The most vulnerable sexual act is:", opts([
    ("Receiving — letting someone give to me without reciprocating, being the sole focus, accepting pleasure I didn't earn", {"vulnerability_in_sex": 5}),
    ("Asking for what I want — naming desire out loud", {"vulnerability_in_sex": 4}),
    ("Being fully naked and seen", {"vulnerability_in_sex": 3}),
    ("Nothing about sex feels particularly vulnerable to me", {"vulnerability_in_sex": 1})
]))

q("aftercare_needs", "forced_choice", "If your aftercare needs aren't met, the long-term effect on the relationship is:", opts([
    ("Significant — I'll start to dread sex because I associate it with feeling abandoned afterward", {"aftercare_needs": 5}),
    ("Noticeable — I'll bring it up and try to fix it", {"aftercare_needs": 4}),
    ("Minimal — I can self-soothe", {"aftercare_needs": 3}),
    ("None — aftercare isn't that important to me", {"aftercare_needs": 1})
]), tier_role="consistency_check", cg="aftercare_core")

q("attachment_in_sex", "forced_choice", "Your attachment style in relationships (anxious, secure, avoidant) shows up during sex as:", opts([
    ("Very visible — my attachment patterns are amplified by the vulnerability of sex", {"attachment_in_sex": 5}),
    ("Somewhat visible — sex activates my attachment system", {"attachment_in_sex": 4}),
    ("Mildly — sex is somewhat separate from my attachment patterns", {"attachment_in_sex": 3}),
    ("Not visible — sex doesn't activate my attachment system", {"attachment_in_sex": 1})
]))

q("initiation_comfort", "forced_choice", "Rejection resilience — after being turned down for sex, how long until you initiate again?", opts([
    ("Same day or next day — one 'no' doesn't change my willingness to express desire", {"initiation_comfort": 5}),
    ("A couple of days — I bounce back", {"initiation_comfort": 4}),
    ("A week or more — rejection stings and I need time", {"initiation_comfort": 2}),
    ("I may not initiate again — I wait for them to come to me", {"initiation_comfort": 1})
]), cg="init_temporal")

q("communication_during", "forced_choice", "Nonverbal communication during sex (moving a partner's hand, adjusting position, using sounds) vs. verbal:", opts([
    ("I use both fluently — nonverbal for quick adjustments, verbal for desires and affirmation", {"communication_during": 5}),
    ("Mostly nonverbal with some verbal", {"communication_during": 4}),
    ("Mostly nonverbal — talking feels interrupting", {"communication_during": 3}),
    ("Minimal communication of either type", {"communication_during": 1})
]))

q("responsive_desire", "forced_choice", "Understanding your own desire type (spontaneous vs. responsive) has:", opts([
    ("Been transformative — I no longer pathologize my responsive pattern or think something is wrong with me", {"responsive_desire": 5}),
    ("Been helpful — it explains patterns I couldn't before", {"responsive_desire": 4}),
    ("Been mildly interesting", {"responsive_desire": 3}),
    ("Not been relevant — my desire doesn't need a label", {"responsive_desire": 1})
]))

q("spontaneous_desire", "forced_choice", "Masturbation frequency as a measure of spontaneous desire:", opts([
    ("I masturbate regularly driven by internal desire, not just habit — my body generates sexual energy that needs an outlet", {"spontaneous_desire": 5}),
    ("I masturbate a few times a week — fairly driven by desire", {"spontaneous_desire": 4}),
    ("Occasionally — when the mood strikes", {"spontaneous_desire": 3}),
    ("Rarely — I don't often feel the urge independently", {"spontaneous_desire": 1})
]), cg="spontaneous_behavioral")

print(f"Total questions: {len(questions)}")
with open("/Users/user/personal/sb/trueassess/priv/question_bank/intimacy_style.json", "w") as f:
    json.dump(questions, f, indent=2)
print("Written intimacy_style.json")
