import json

questions = []
uid_counter = 1

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
    """Helper: list of (id_letter, text, {dim: score}) tuples"""
    return [{"id": chr(97+i), "text": t, "scores": s} for i, (t, s) in enumerate(texts_scores)]

# ============================================================
# DOMINANCE SPECTRUM (20 questions)
# ============================================================
dim = "dominance_spectrum"

q(dim, "scenario", "Your partner tells you they want you to decide everything tonight — what you eat, what they wear, when and how you have sex. Your honest reaction:", opts([
    ("Deeply excited — this is exactly the dynamic I crave", {"dominance_spectrum": 5}),
    ("Intrigued and aroused — I'd enjoy stepping into that role", {"dominance_spectrum": 4}),
    ("Willing but unsure — I'd try it but might feel awkward", {"dominance_spectrum": 3}),
    ("Uncomfortable — I don't want that level of control over someone", {"dominance_spectrum": 1})
]))

q(dim, "behavioral_recall", "In your most recent sexual encounter, how much did you direct what happened — positions, pacing, what acts occurred?", opts([
    ("I directed almost everything — it's natural for me to lead", {"dominance_spectrum": 5}),
    ("I directed most of it, checking in along the way", {"dominance_spectrum": 4}),
    ("It was roughly equal — we flowed back and forth", {"dominance_spectrum": 3}),
    ("My partner directed most or all of it, and I preferred that", {"dominance_spectrum": 1})
]), cg="dom_behavioral")

q(dim, "forced_choice", "When you hear the word 'obey' in a sexual context, you feel:", opts([
    ("A rush of authority — I want to be the one obeyed", {"dominance_spectrum": 5}),
    ("Curious — I'd like to explore commanding someone", {"dominance_spectrum": 4}),
    ("Neutral — it depends entirely on the context", {"dominance_spectrum": 3}),
    ("Drawn to being the one who obeys", {"dominance_spectrum": 1})
]), cross=[{"dimension": "submission_spectrum", "notes": "Inverse correlation expected"}])

q(dim, "scenario", "A partner kneels before you and asks 'What would you like me to do?' You:", opts([
    ("Feel a surge of power and arousal — I have specific instructions ready", {"dominance_spectrum": 5}),
    ("Enjoy the moment and think of something I'd like", {"dominance_spectrum": 4}),
    ("Feel a bit flustered but try to play along", {"dominance_spectrum": 3}),
    ("Feel uncomfortable — I'd rather they tell me what they want", {"dominance_spectrum": 1})
]))

q(dim, "temporal", "Over the past year, how often have you fantasized about giving orders, setting rules, or controlling a partner's behavior during sex?", opts([
    ("Daily or nearly daily — it's central to my fantasy life", {"dominance_spectrum": 5}),
    ("Several times a week", {"dominance_spectrum": 4}),
    ("Occasionally — a few times a month", {"dominance_spectrum": 3}),
    ("Rarely or never", {"dominance_spectrum": 1})
]), cg="dom_temporal")

q(dim, "scenario", "You're negotiating a scene. Your partner says 'I want you to push me past where I'd normally stop — I trust you.' You:", opts([
    ("Accept with confidence — reading and pushing edges is a skill I've developed", {"dominance_spectrum": 5}),
    ("Accept carefully — I'd push gently and check in frequently", {"dominance_spectrum": 4}),
    ("Hesitate — that's a lot of responsibility", {"dominance_spectrum": 2}),
    ("Decline — I'm not comfortable holding that much power", {"dominance_spectrum": 1})
]))

q(dim, "behavioral_recall", "Think about a time you gave a direct sexual command — 'Get on your knees,' 'Don't move,' 'Come here.' How did it feel?", opts([
    ("Completely natural — commanding is my default mode", {"dominance_spectrum": 5}),
    ("Exciting and a little powerful — I liked it", {"dominance_spectrum": 4}),
    ("Forced or performative — I was playing a role", {"dominance_spectrum": 2}),
    ("I've never done this / it felt wrong when I tried", {"dominance_spectrum": 1})
]), cg="dom_behavioral")

q(dim, "somatic", "When you physically restrain a partner — holding their wrists, pinning them down — what happens in your body?", opts([
    ("Intense arousal, accelerated breathing, feeling of rightness", {"dominance_spectrum": 5}),
    ("Excitement and increased arousal", {"dominance_spectrum": 4}),
    ("Mild interest — it's fun sometimes", {"dominance_spectrum": 3}),
    ("Tension or discomfort — I'd rather not", {"dominance_spectrum": 1})
]))

q(dim, "forced_choice", "If you could only have one forever: the power to command, or the freedom to surrender?", opts([
    ("Command, without hesitation", {"dominance_spectrum": 5}),
    ("Command, but I'd miss surrendering sometimes", {"dominance_spectrum": 4}),
    ("Surrender, but I'd miss commanding sometimes", {"dominance_spectrum": 2}),
    ("Surrender, without hesitation", {"dominance_spectrum": 1})
]), cross=[{"dimension": "switch_capacity", "notes": "Middle answers indicate switch tendency"}])

q(dim, "scenario", "Your partner orgasms without permission. How do you feel about the concept of orgasm control?", opts([
    ("Essential — controlling when and how they come is core to the dynamic", {"dominance_spectrum": 5}),
    ("Very appealing — I enjoy that level of authority over their pleasure", {"dominance_spectrum": 4}),
    ("Interesting to try but not essential", {"dominance_spectrum": 3}),
    ("Uninterested — I want them to come whenever they want", {"dominance_spectrum": 1})
]))

q(dim, "temporal", "In your relationships, how consistently do you take the lead in initiating sex and deciding what happens?", opts([
    ("Almost always — it's expected and desired by both of us", {"dominance_spectrum": 5}),
    ("Most of the time", {"dominance_spectrum": 4}),
    ("About half the time", {"dominance_spectrum": 3}),
    ("Rarely — I prefer to follow my partner's lead", {"dominance_spectrum": 1})
]), cg="dom_temporal")

q(dim, "scenario", "You discover your partner has been secretly touching themselves despite a rule you set. You:", opts([
    ("Feel genuinely disrespected — rules exist for a reason, and there will be consequences", {"dominance_spectrum": 5}),
    ("Address it firmly — this is a teaching moment in the dynamic", {"dominance_spectrum": 4}),
    ("Talk about it — maybe the rule needs adjusting", {"dominance_spectrum": 3}),
    ("Shrug it off — it's their body", {"dominance_spectrum": 1})
]), cross=[{"dimension": "protocol_orientation", "notes": "High protocol Doms treat rule violations seriously"}])

q(dim, "somatic", "Imagine a partner whispering 'Yes, Sir' (or 'Yes, Ma'am' / 'Yes, Daddy') after you give an instruction. What do you feel physically?", opts([
    ("A deep, visceral satisfaction — like something clicking into place", {"dominance_spectrum": 5}),
    ("A definite arousal spike — I like hearing deference", {"dominance_spectrum": 4}),
    ("Mild pleasure — it's nice", {"dominance_spectrum": 3}),
    ("Nothing special, or mild discomfort", {"dominance_spectrum": 1})
]))

q(dim, "behavioral_recall", "When you've set boundaries or rules for a partner outside the bedroom (texting protocols, dress codes, behavior expectations), how did you feel about maintaining and enforcing them?", opts([
    ("Energized — the ongoing authority is the best part", {"dominance_spectrum": 5, "protocol_orientation": 4}),
    ("Enjoyed it but found the maintenance effort real work", {"dominance_spectrum": 4}),
    ("Mixed — it felt like too much responsibility sometimes", {"dominance_spectrum": 2}),
    ("I've never done this and wouldn't want to", {"dominance_spectrum": 1})
]), tags=["nsfw", "bdsm", "dominance_spectrum", "lifestyle"])

q(dim, "forced_choice", "A partner begs — genuinely begs — for you to let them come. This makes you feel:", opts([
    ("Powerful and deeply aroused — their desperation feeds something in me", {"dominance_spectrum": 5, "sadism": 3}),
    ("Turned on — I enjoy the control", {"dominance_spectrum": 4}),
    ("Conflicted — I want to give them what they want", {"dominance_spectrum": 2}),
    ("Uncomfortable — I'd let them immediately", {"dominance_spectrum": 1})
]))

q(dim, "scenario", "You're at a social event with your partner who is your submissive. They look to you before ordering food, before accepting a drink, before sitting down. This level of deference in public:", opts([
    ("Is exactly what I want — it's a beautiful expression of our dynamic", {"dominance_spectrum": 5, "protocol_orientation": 5}),
    ("Feels good but I'd keep it more subtle in public", {"dominance_spectrum": 4}),
    ("Is too much for me — bedroom only", {"dominance_spectrum": 2}),
    ("Would embarrass or bother me", {"dominance_spectrum": 1})
]))

q(dim, "scenario", "You're training a new submissive partner. The process of teaching them your preferences, correcting their behavior, and watching them grow into your dynamic makes you feel:", opts([
    ("Deeply fulfilled — training is one of the most rewarding parts of D/s", {"dominance_spectrum": 5, "service_orientation": 4}),
    ("Excited — watching someone learn to serve well is satisfying", {"dominance_spectrum": 4}),
    ("Patient but neutral — it's a means to an end", {"dominance_spectrum": 3}),
    ("Burdened — I'd rather have an experienced partner who already knows what to do", {"dominance_spectrum": 2})
]))

q(dim, "forced_choice", "Your deepest truth about power in relationships:", opts([
    ("I am most alive when I hold authority and my partner yields to it", {"dominance_spectrum": 5}),
    ("I enjoy leading and having a willing partner who follows", {"dominance_spectrum": 4}),
    ("I like variety — sometimes leading, sometimes not", {"dominance_spectrum": 3}),
    ("I feel most at peace when someone else holds the reins", {"dominance_spectrum": 1})
]), tier_role="consistency_check", cg="dom_core")

q(dim, "scenario", "During sex, you hold your partner by the throat — not squeezing dangerously, but asserting physical control. This is:", opts([
    ("One of my signature moves — physical dominance is instinctive for me", {"dominance_spectrum": 5}),
    ("Something I enjoy and do with consent", {"dominance_spectrum": 4}),
    ("Something I've tried and felt neutral about", {"dominance_spectrum": 3}),
    ("Not for me — I don't want to physically dominate someone", {"dominance_spectrum": 1})
]), tags=["nsfw", "bdsm", "dominance_spectrum", "physical"])

q(dim, "temporal", "How important is it to you that a partner uses a title (Sir, Daddy, Master, Ma'am, Mistress) when addressing you during a scene or in your dynamic?", opts([
    ("Non-negotiable — the title reflects the power structure", {"dominance_spectrum": 5, "protocol_orientation": 5}),
    ("Very important — it deepens the experience", {"dominance_spectrum": 4}),
    ("Nice but optional", {"dominance_spectrum": 3}),
    ("Unnecessary or uncomfortable for me", {"dominance_spectrum": 1})
]))

# ============================================================
# SUBMISSION SPECTRUM (20 questions)
# ============================================================
dim = "submission_spectrum"

q(dim, "scenario", "Your partner tells you: 'Tonight you do exactly what I say. You don't get to choose.' Your honest first reaction:", opts([
    ("Deep relief and arousal — this is what I've been craving", {"submission_spectrum": 5}),
    ("Excited — I want to see where this goes", {"submission_spectrum": 4}),
    ("Cautiously interested — depends on the partner", {"submission_spectrum": 3}),
    ("Resistant — I don't want to give up control", {"submission_spectrum": 1})
]))

q(dim, "behavioral_recall", "When a partner has given you a direct sexual instruction — 'Bend over,' 'Open your mouth,' 'Spread your legs' — how did your body respond?", opts([
    ("Immediate, intense arousal — the command itself turned me on", {"submission_spectrum": 5}),
    ("Arousal and a pleasurable feeling of being directed", {"submission_spectrum": 4}),
    ("Willingness but no particular charge from the command itself", {"submission_spectrum": 3}),
    ("Resistance or irritation — don't tell me what to do", {"submission_spectrum": 1})
]), cg="sub_behavioral")

q(dim, "somatic", "When someone you trust holds you down firmly during sex — what happens in your nervous system?", opts([
    ("I melt — my whole body relaxes into the restraint, like coming home", {"submission_spectrum": 5}),
    ("I feel aroused and safe — the pressure feels good", {"submission_spectrum": 4}),
    ("It's physically fine but doesn't do much for me emotionally", {"submission_spectrum": 3}),
    ("I feel trapped and need to push back", {"submission_spectrum": 1})
]))

q(dim, "forced_choice", "The idea of wearing a collar — as a symbol that you belong to someone — makes you feel:", opts([
    ("Profoundly moved — it represents the deepest commitment I can imagine", {"submission_spectrum": 5}),
    ("Excited — I'd love that symbol of connection", {"submission_spectrum": 4}),
    ("Curious but uncertain", {"submission_spectrum": 3}),
    ("Repelled — I don't belong to anyone", {"submission_spectrum": 1})
]))

q(dim, "temporal", "Over the past year, how often have you fantasized about surrendering control — being told what to do, being used for someone's pleasure, being owned?", opts([
    ("Daily or nearly daily — it's the core of my sexual identity", {"submission_spectrum": 5}),
    ("Several times a week", {"submission_spectrum": 4}),
    ("Occasionally", {"submission_spectrum": 3}),
    ("Rarely or never", {"submission_spectrum": 1})
]), cg="sub_temporal")

q(dim, "scenario", "Your Dominant partner assigns you a task — writing lines, wearing a plug to work, following a specific morning routine. The structure of having assignments makes you feel:", opts([
    ("Grounded and connected — even mundane tasks feel meaningful because they were given", {"submission_spectrum": 5, "service_orientation": 4}),
    ("Happily obedient — I enjoy having things to do for them", {"submission_spectrum": 4}),
    ("Neutral — I'd do it but it doesn't add emotional depth", {"submission_spectrum": 2}),
    ("Annoyed — this feels controlling, not intimate", {"submission_spectrum": 1})
]))

q(dim, "behavioral_recall", "Think about a time you said 'Yes, Sir' or 'Yes, Daddy' (or equivalent) and meant it from a deep place. What was that like?", opts([
    ("One of the most intimate, vulnerable, right things I've ever felt", {"submission_spectrum": 5}),
    ("Exciting and connecting — I felt seen in my submission", {"submission_spectrum": 4}),
    ("It was fun roleplay", {"submission_spectrum": 3}),
    ("I've never said this sincerely / I wouldn't want to", {"submission_spectrum": 1})
]), cg="sub_behavioral")

q(dim, "scenario", "You're told to kneel and wait — naked, in position — until your partner is ready for you. Twenty minutes pass. You:", opts([
    ("Sink deeper into headspace — the waiting is part of the surrender", {"submission_spectrum": 5}),
    ("Stay patiently — pleasing them by obeying is its own reward", {"submission_spectrum": 4}),
    ("Get restless after a while — this is a lot to ask", {"submission_spectrum": 2}),
    ("Refuse — this is degrading", {"submission_spectrum": 1})
]))

q(dim, "somatic", "When a trusted partner calls you 'mine' — 'You're mine,' 'This body is mine' — your physical response is:", opts([
    ("Full-body shiver, arousal, a sense of being claimed at the cellular level", {"submission_spectrum": 5}),
    ("A warm rush of arousal and safety", {"submission_spectrum": 4}),
    ("Mild pleasure", {"submission_spectrum": 3}),
    ("Bristling — I'm not anyone's possession", {"submission_spectrum": 1})
]))

q(dim, "forced_choice", "Which statement resonates most with your sexual self?", opts([
    ("My deepest pleasure comes from being of use to someone I've chosen to serve", {"submission_spectrum": 5, "service_orientation": 4}),
    ("I love the freedom of letting someone else take charge", {"submission_spectrum": 4}),
    ("I enjoy a mix — sometimes leading, sometimes following", {"submission_spectrum": 3}),
    ("I need to be in control to feel safe during sex", {"submission_spectrum": 1})
]), tier_role="consistency_check", cg="sub_core")

q(dim, "scenario", "Your partner punishes you for a real rule violation — not play punishment, but genuine correction. You:", opts([
    ("Accept it gratefully — accountability is part of the dynamic I signed up for", {"submission_spectrum": 5, "power_exchange_depth": 5}),
    ("Accept it, even though it stings — I understand the purpose", {"submission_spectrum": 4}),
    ("Feel conflicted — punishment for real mistakes blurs lines I'm not sure about", {"submission_spectrum": 2}),
    ("Refuse — no one punishes me for real behavior", {"submission_spectrum": 1})
]))

q(dim, "temporal", "How long have you known that submission was part of your sexual identity (even if you didn't have the word for it)?", opts([
    ("As long as I can remember — it predates any relationship", {"submission_spectrum": 5}),
    ("Since my teens or early adulthood — it emerged with sexual awareness", {"submission_spectrum": 4}),
    ("Relatively recently — a partner or experience unlocked it", {"submission_spectrum": 3}),
    ("I don't identify as submissive", {"submission_spectrum": 1})
]), cg="sub_temporal")

q(dim, "scenario", "During sex, your partner grabs your hair firmly and directs your head where they want it. You:", opts([
    ("Go pliant immediately — being physically directed is deeply arousing", {"submission_spectrum": 5}),
    ("Enjoy the assertiveness — it's hot", {"submission_spectrum": 4}),
    ("Don't mind it but it's not a turn-on specifically", {"submission_spectrum": 3}),
    ("Pull away — I don't like being physically controlled", {"submission_spectrum": 1})
]))

q(dim, "forced_choice", "Orgasm denial — being told you cannot come until given permission. This concept:", opts([
    ("Makes me ache with want — giving up even that control is the ultimate surrender", {"submission_spectrum": 5}),
    ("Is very appealing — I like the tension and the release on their terms", {"submission_spectrum": 4}),
    ("Is interesting to try", {"submission_spectrum": 3}),
    ("Sounds frustrating and pointless", {"submission_spectrum": 1})
]))

q(dim, "scenario", "Your Dominant is having a bad day and takes a harsher tone than usual. You:", opts([
    ("Absorb it — part of my role is being a safe place for them, even when it's hard", {"submission_spectrum": 5}),
    ("Notice it and bring it up gently later — I serve, but I'm not a punching bag", {"submission_spectrum": 4}),
    ("Push back immediately — dynamic or not, you don't talk to me that way", {"submission_spectrum": 2}),
    ("Withdraw — this is why power exchange is dangerous", {"submission_spectrum": 1})
]), tier_role="trap", trap=True, tags=["nsfw", "bdsm", "submission_spectrum", "dynamic_health"])

q(dim, "behavioral_recall", "When you've been in a situation where someone genuinely dominated you — not play, but real authority — the core feeling was:", opts([
    ("Peace. Like finally being able to put something heavy down", {"submission_spectrum": 5}),
    ("Excitement and connection", {"submission_spectrum": 4}),
    ("Uncomfortable vulnerability", {"submission_spectrum": 2}),
    ("Resentment or fear", {"submission_spectrum": 1})
]), cg="sub_behavioral")

q(dim, "somatic", "When given a rule that applies to your daily life — what to wear, when to check in, how to address your partner — your body's baseline response over time is:", opts([
    ("Calmer, more centered — structure from them soothes my nervous system", {"submission_spectrum": 5}),
    ("Generally good — I like having guardrails", {"submission_spectrum": 4}),
    ("Neutral — I follow the rules but don't feel different physically", {"submission_spectrum": 3}),
    ("Constricted or tense — I feel controlled", {"submission_spectrum": 1})
]))

q(dim, "scenario", "A partner tells you: 'I want you to edge yourself for 30 minutes and then ask permission to come.' Alone at home, with no one watching. You:", opts([
    ("Do it exactly as instructed — their authority doesn't require their physical presence", {"submission_spectrum": 5}),
    ("Do it, though it's harder without them there to witness", {"submission_spectrum": 4}),
    ("Probably cut it short — they'd never know", {"submission_spectrum": 2}),
    ("Skip it — obedience requires someone to obey in front of", {"submission_spectrum": 1})
]), tier_role="consistency_check", cg="sub_integrity")

q(dim, "forced_choice", "What matters more to you in a D/s dynamic?", opts([
    ("Being truly known and held — submission as the ultimate vulnerability", {"submission_spectrum": 5}),
    ("The thrill of power exchange — the erotic charge of yielding", {"submission_spectrum": 4}),
    ("The structure — having clear roles and expectations", {"submission_spectrum": 3}),
    ("I don't value submission in relationships", {"submission_spectrum": 1})
]))

q(dim, "scenario", "You and your partner disagree about something in your dynamic. They pull rank: 'I've made my decision.' You:", opts([
    ("Yield — I chose this person's authority, and I trust their judgment even when I disagree", {"submission_spectrum": 5}),
    ("Yield for now but plan to discuss it later when we're outside the dynamic", {"submission_spectrum": 4}),
    ("Push back — even in a D/s dynamic, I have an equal voice", {"submission_spectrum": 2}),
    ("End the scene — pulling rank in a disagreement is a red flag", {"submission_spectrum": 1})
]), tier_role="trap", trap=True, tags=["nsfw", "bdsm", "submission_spectrum", "consent", "dynamic_health"])

# ============================================================
# SADISM (20 questions)
# ============================================================
dim = "sadism"

q(dim, "scenario", "You're spanking your partner and they gasp, flinch, and then push their body back toward you for more. You feel:", opts([
    ("Deeply aroused — their pain response feeds something primal in me", {"sadism": 5}),
    ("Excited — the power of causing sensation and seeing their reaction is hot", {"sadism": 4}),
    ("Fine — I can do it if they enjoy it", {"sadism": 3}),
    ("Guilty — I don't want to cause pain even if they ask for it", {"sadism": 1})
]))

q(dim, "behavioral_recall", "Think about a time you left marks on a partner — bruises, welts, bite marks, rope marks. Seeing those marks afterward made you feel:", opts([
    ("Deeply satisfied and possessive — my marks on their body", {"sadism": 5, "dominance_spectrum": 4}),
    ("Proud and turned on — evidence of our intensity", {"sadism": 4}),
    ("Neutral — marks happen sometimes", {"sadism": 3}),
    ("Worried or guilty — I didn't mean to hurt them that much", {"sadism": 1})
]), cg="sadism_behavioral")

q(dim, "somatic", "When you hear your partner cry out in pain during a scene — not a safeword, a genuine pain sound — your body's immediate reaction is:", opts([
    ("Arousal intensifies — their pain sounds are fuel", {"sadism": 5}),
    ("A rush of adrenaline and heightened focus", {"sadism": 4}),
    ("A brief check-in impulse before continuing", {"sadism": 3}),
    ("Immediate desire to stop — pain sounds trigger my empathy", {"sadism": 1})
]))

q(dim, "forced_choice", "Which is more arousing to you?", opts([
    ("Making someone cry from intensity — tears running down their face while they beg for more", {"sadism": 5}),
    ("Making someone moan and writhe from carefully applied sensation", {"sadism": 4}),
    ("Making someone feel overwhelmed with pleasure", {"sadism": 2}),
    ("Gentle, connected, sensual touch", {"sadism": 1})
]))

q(dim, "scenario", "You're using a flogger on a partner. You notice their skin is reddening, they're breathing hard, tears are starting. You haven't heard a safeword. You:", opts([
    ("Continue and escalate — I'm reading their body and they're flying, this is the art", {"sadism": 5}),
    ("Continue at this level — this is the sweet spot", {"sadism": 4}),
    ("Check in verbally before continuing", {"sadism": 3}),
    ("Stop — I can't keep going with them in this state", {"sadism": 1})
]))

q(dim, "temporal", "How often do you fantasize about causing consensual pain — impact play, nipple torture, predicament bondage, rough sex?", opts([
    ("It's central to almost every fantasy", {"sadism": 5}),
    ("Frequently — several times a week", {"sadism": 4}),
    ("Occasionally — a few times a month", {"sadism": 3}),
    ("Rarely or never", {"sadism": 1})
]), cg="sadism_temporal")

q(dim, "scenario", "Nipple clamps have been on your partner for a while. You know that removing them will cause a sharp spike of pain. You remove them slowly while watching their face. This moment:", opts([
    ("Is one of my favorites — watching the pain wash over them while I caused it is intoxicating", {"sadism": 5}),
    ("Is satisfying — I enjoy being the source of intense sensation", {"sadism": 4}),
    ("Is practical — clamps come off, it hurts, that's how it works", {"sadism": 2}),
    ("Makes me want to apologize", {"sadism": 1})
]))

q(dim, "behavioral_recall", "Have you ever escalated intensity during a scene because your partner's pain response aroused you more?", opts([
    ("Yes, regularly — their responses guide my escalation and my arousal drives it", {"sadism": 5}),
    ("Yes, sometimes — in the heat of the moment their reactions push me to go harder", {"sadism": 4}),
    ("Maybe once or twice — and I felt uncertain about it afterward", {"sadism": 3}),
    ("No — I stick to pre-negotiated intensity levels", {"sadism": 1})
]), cg="sadism_behavioral")

q(dim, "forced_choice", "A partner who bruises easily vs. a partner who can take extreme impact without marking. Who do you prefer to play with?", opts([
    ("Bruises easily — seeing my marks on them the next day is part of the appeal", {"sadism": 5}),
    ("Either — the marks are a bonus but the sensation exchange is what matters", {"sadism": 4}),
    ("Can take extreme impact — I want to go hard without worrying about damage", {"sadism": 3}),
    ("Neither scenario is particularly appealing to me", {"sadism": 1})
]))

q(dim, "somatic", "When you bite a partner — hard enough to leave tooth marks — and they yelp, your body responds with:", opts([
    ("A wave of primal satisfaction and hunger for more", {"sadism": 5}),
    ("Arousal and a sense of possession", {"sadism": 4}),
    ("It's fun in the moment", {"sadism": 3}),
    ("Regret — I went too far", {"sadism": 1})
]))

q(dim, "scenario", "You're choosing implements for a scene. You have access to a soft flogger, a stiff leather paddle, a thin cane, and a Wartenberg wheel. You gravitate toward:", opts([
    ("The cane — precision, sting, and the most intense reaction", {"sadism": 5}),
    ("The paddle — solid thud, reliable pain, satisfying sound", {"sadism": 4}),
    ("The Wartenberg wheel — sensation without heavy pain", {"sadism": 3}),
    ("The soft flogger — I want sensation play, not pain", {"sadism": 1})
]), tags=["nsfw", "bdsm", "sadism", "impact_play"])

q(dim, "scenario", "Your partner is in predicament bondage — any position they shift to causes a different kind of discomfort. Watching them struggle and try to find relief:", opts([
    ("Is deeply arousing — the creative cruelty of the setup satisfies something in me", {"sadism": 5, "bondage": 3}),
    ("Is exciting — I enjoy the mental chess of it", {"sadism": 4}),
    ("Is interesting but I'm more focused on whether they're okay", {"sadism": 2}),
    ("Makes me uncomfortable — I'd rather tie them comfortably", {"sadism": 1})
]))

q(dim, "forced_choice", "Your partner can take more pain than anyone you've played with. This makes you feel:", opts([
    ("Challenged and thrilled — I finally have a canvas that won't limit me", {"sadism": 5}),
    ("Excited — we can explore deep territory together", {"sadism": 4}),
    ("Neutral — pain tolerance doesn't change what I enjoy", {"sadism": 3}),
    ("Relieved — at least I know I won't accidentally hurt them", {"sadism": 1})
]))

q(dim, "temporal", "When you've caused a partner to cry during a scene (from pain, intensity, or emotional overwhelm), your response in the moment was:", opts([
    ("Profound satisfaction and tenderness — bringing someone to tears through intensity is intimate", {"sadism": 5}),
    ("Arousal mixed with care — I held them through it", {"sadism": 4}),
    ("Immediate concern — I checked if they needed to stop", {"sadism": 2}),
    ("I've never caused this / would immediately stop", {"sadism": 1})
]), cg="sadism_temporal")

q(dim, "scenario", "The concept of 'consensual non-consent' (CNC) — where a partner consents in advance to a scene that simulates resistance, force, or taking — is:", opts([
    ("One of the most intense and psychologically rich forms of play I know", {"sadism": 5}),
    ("Exciting if done with extensive negotiation and trust", {"sadism": 4}),
    ("Uncomfortable but I understand it theoretically", {"sadism": 2}),
    ("A hard limit — I can't play with anything that looks like non-consent", {"sadism": 1})
]))

q(dim, "behavioral_recall", "When you've engaged in rough sex — hair pulling, slapping, choking, throwing a partner around — how much of the roughness was for YOUR enjoyment vs. theirs?", opts([
    ("Primarily mine — the roughness IS my arousal, and their enjoyment is a bonus", {"sadism": 5}),
    ("Mutual — I enjoy being rough AND knowing they enjoy receiving it", {"sadism": 4}),
    ("Mostly theirs — I do it because they like it", {"sadism": 2}),
    ("I don't engage in rough sex", {"sadism": 1})
]), cg="sadism_behavioral")

q(dim, "somatic", "Edge play — activities that carry real risk (breath play, fire play, knife play). The proximity to genuine danger makes you feel:", opts([
    ("Alive in a way nothing else does — the risk heightens everything", {"sadism": 5}),
    ("Intensely focused — risk demands skill and presence", {"sadism": 4}),
    ("Anxious but curious", {"sadism": 2}),
    ("Hard no — the risk outweighs any thrill", {"sadism": 1})
]), tags=["nsfw", "bdsm", "sadism", "edge_play"])

q(dim, "forced_choice", "Be honest: do you sometimes enjoy a partner's genuine discomfort or embarrassment, not just their performed reaction?", opts([
    ("Yes — and the genuine quality is what makes it arousing", {"sadism": 5}),
    ("Sometimes — in controlled contexts where they consented to that experience", {"sadism": 4}),
    ("I prefer knowing they're enjoying it underneath", {"sadism": 2}),
    ("No — I need them to genuinely enjoy every moment", {"sadism": 1})
]), tier_role="trap", trap=True)

q(dim, "scenario", "You're introducing a new partner to impact play. They flinch harder than expected at a moderate strike. You:", opts([
    ("Note their threshold and work just below it — building them up is part of the fun", {"sadism": 4}),
    ("Back off significantly — their limits are the ceiling", {"sadism": 3}),
    ("Feel disappointed that they can't take more", {"sadism": 5}),
    ("Stop impact play and switch to something gentler", {"sadism": 1})
]), tier_role="trap", trap=True, tags=["nsfw", "bdsm", "sadism", "consent_sensitivity"])

q(dim, "scenario", "After an intense pain scene, your partner is in a puddle — shaking, crying, clinging to you. You:", opts([
    ("Hold them fiercely and feel both tenderness and satisfaction — I brought them here", {"sadism": 5}),
    ("Shift fully into aftercare mode — gentleness replaces intensity", {"sadism": 4}),
    ("Feel worried I went too far", {"sadism": 2}),
    ("This scenario wouldn't happen because I wouldn't push this hard", {"sadism": 1})
]), cross=[{"dimension": "masochism", "notes": "Sadist aftercare reveals care beneath the edge"}])

# ============================================================
# MASOCHISM (20 questions)
# ============================================================
dim = "masochism"

q(dim, "scenario", "Your partner strikes you hard enough to leave a mark. Your immediate reaction:", opts([
    ("Deep satisfaction — the pain blooms into something warm and right", {"masochism": 5}),
    ("Arousal spike — the sting is exciting", {"masochism": 4}),
    ("Tolerable — I can take it if they want to do it", {"masochism": 3}),
    ("I want to stop — pain isn't pleasurable for me", {"masochism": 1})
]))

q(dim, "somatic", "Think about your body's response to sharp, sudden pain (a slap, a pinch, a bite) during sexual arousal. The pain:", opts([
    ("Transforms into pleasure almost immediately — my nervous system converts it", {"masochism": 5}),
    ("Heightens my arousal — pain and pleasure blend", {"masochism": 4}),
    ("Stays as pain but I tolerate it for the dynamic", {"masochism": 3}),
    ("Breaks my arousal — pain is pain", {"masochism": 1})
]), cg="maso_somatic")

q(dim, "temporal", "How often do you crave physical pain as part of sexual expression?", opts([
    ("Regularly — I feel incomplete without it, like an itch that needs scratching", {"masochism": 5}),
    ("Frequently — it enhances almost every sexual encounter", {"masochism": 4}),
    ("Sometimes — when I'm in the right headspace", {"masochism": 3}),
    ("Never — sex and pain don't mix for me", {"masochism": 1})
]), cg="maso_temporal")

q(dim, "behavioral_recall", "The hardest you've ever been hit during consensual play — how did you feel in the moment?", opts([
    ("Transcendent — like the pain cracked something open and I flew", {"masochism": 5}),
    ("Intensely present and aroused", {"masochism": 4}),
    ("I endured it and was proud of myself", {"masochism": 3}),
    ("I safeworded / wanted to stop", {"masochism": 1})
]), cg="maso_behavioral")

q(dim, "forced_choice", "You'd rather:", opts([
    ("Be beaten until you cry and then held while you come down", {"masochism": 5}),
    ("Experience a building intensity that leaves you trembling", {"masochism": 4}),
    ("Have rough sex with some pain mixed in", {"masochism": 3}),
    ("Have intense sex without any deliberate pain", {"masochism": 1})
]))

q(dim, "somatic", "Subspace — the floaty, disconnected, euphoric state that pain can produce. Your relationship with it:", opts([
    ("It's my drug — I chase it, I know how to get there, and I come back changed", {"masochism": 5}),
    ("I've experienced it and it's profound", {"masochism": 4}),
    ("I've touched the edges of it", {"masochism": 3}),
    ("I've never experienced this / don't think it's real for me", {"masochism": 1})
]))

q(dim, "scenario", "Nipple clamps are placed on you and tightened. The initial sharp pain:", opts([
    ("Makes me gasp and then settle — my breathing deepens as I absorb it", {"masochism": 5}),
    ("Hurts but in a good way — I lean into the sensation", {"masochism": 4}),
    ("Is unpleasant but I can handle it", {"masochism": 3}),
    ("Makes me want to rip them off immediately", {"masochism": 1})
]))

q(dim, "behavioral_recall", "After a scene that left marks (bruises, welts, rope burns), how did you feel looking at them the next day?", opts([
    ("Touched them tenderly, felt aroused and connected to the experience — they're souvenirs", {"masochism": 5}),
    ("Smiled — good memories", {"masochism": 4}),
    ("Neutral — marks happen", {"masochism": 3}),
    ("Distressed — I wish they weren't there", {"masochism": 1})
]), cg="maso_behavioral")

q(dim, "forced_choice", "The thing that makes pain erotic for you (if anything does):", opts([
    ("The endorphin flood — pain literally becomes pleasure in my body", {"masochism": 5}),
    ("The vulnerability — letting someone hurt me requires deep trust", {"masochism": 4}),
    ("The power dynamic — pain is proof of their authority", {"masochism": 3}),
    ("Nothing — pain isn't erotic for me", {"masochism": 1})
]))

q(dim, "scenario", "Your partner wants to try a more intense implement than you've experienced. You're nervous. You:", opts([
    ("Enthusiastically consent — nervousness is part of the thrill, and I trust them to read me", {"masochism": 5}),
    ("Agree with clear safeword review — I want to push my limits", {"masochism": 4}),
    ("Ask to work up to it very gradually", {"masochism": 3}),
    ("Decline — I don't need to push into more intense pain", {"masochism": 1})
]))

q(dim, "somatic", "When you're being bitten hard on the neck or shoulder during sex, your body:", opts([
    ("Arches into it — I want them to bite harder", {"masochism": 5}),
    ("Tenses then releases — the pain-pleasure cycle", {"masochism": 4}),
    ("Flinches but I don't pull away", {"masochism": 3}),
    ("Pulls away reflexively", {"masochism": 1})
]))

q(dim, "temporal", "How has your relationship with pain evolved over your sexual life?", opts([
    ("I've steadily wanted more — my thresholds have increased and I keep seeking deeper intensity", {"masochism": 5}),
    ("I've gotten more comfortable with it and enjoy it more than I used to", {"masochism": 4}),
    ("It's stayed about the same", {"masochism": 3}),
    ("I've become less tolerant of it / never wanted it", {"masochism": 1})
]), cg="maso_temporal")

q(dim, "scenario", "Wax play — hot wax dripped on your chest, stomach, thighs. The unpredictable drops of heat:", opts([
    ("Send me into a beautiful alertness — each drop is a gift of sensation", {"masochism": 5}),
    ("Are exciting — the anticipation and the sting are fun", {"masochism": 4}),
    ("Are tolerable — I can do it for my partner", {"masochism": 3}),
    ("Sound awful — I don't want to be burned", {"masochism": 1})
]))

q(dim, "forced_choice", "If you could never experience pain during sex again, you would feel:", opts([
    ("Genuinely bereft — something essential would be missing from my sexual life", {"masochism": 5}),
    ("Disappointed — it's an important part of what I enjoy", {"masochism": 4}),
    ("Mildly disappointed — there are other things I enjoy more", {"masochism": 3}),
    ("Relieved or indifferent", {"masochism": 1})
]), tier_role="consistency_check", cg="maso_core")

q(dim, "behavioral_recall", "Have you ever asked a partner to hurt you more than they were comfortable with?", opts([
    ("Yes — and convincing them was part of the journey", {"masochism": 5}),
    ("Yes — I've asked for escalation beyond their comfort zone", {"masochism": 4}),
    ("No — I take what's offered", {"masochism": 3}),
    ("No — I've never needed to because I don't want that much", {"masochism": 1})
]), cg="maso_behavioral")

q(dim, "scenario", "Punishment — not play punishment, but real consequence for breaking a rule. Receiving a punishment that genuinely hurts:", opts([
    ("Fulfills something deep — the pain is cleansing, like the slate is truly wiped clean", {"masochism": 5, "submission_spectrum": 4}),
    ("Is hard but meaningful — I value the accountability", {"masochism": 4}),
    ("Is something I'd tolerate but wouldn't seek", {"masochism": 2}),
    ("Is unacceptable — punishment shouldn't involve real pain", {"masochism": 1})
]))

q(dim, "somatic", "During extended impact play (20+ minutes), your body enters a state where:", opts([
    ("Pain becomes irrelevant — I'm floating, my body is processing everything as euphoria", {"masochism": 5}),
    ("I'm deeply relaxed despite the intensity — endorphins are flowing", {"masochism": 4}),
    ("I'm counting strikes and hoping it ends soon", {"masochism": 2}),
    ("I would have stopped long before 20 minutes", {"masochism": 1})
]))

q(dim, "scenario", "A partner scratches deep lines down your back during sex. The sharp, burning sensation:", opts([
    ("Is electric — I moan and press closer, wanting them to mark me deeper", {"masochism": 5}),
    ("Adds a layer of intensity to the sex", {"masochism": 4}),
    ("Is startling but I recover", {"masochism": 3}),
    ("Is a mood-killer", {"masochism": 1})
]))

q(dim, "forced_choice", "Your deepest truth about pain:", opts([
    ("Pain is a pathway to transcendence — it strips me bare and leaves me pure", {"masochism": 5}),
    ("Pain is a spice — it heightens everything around it", {"masochism": 4}),
    ("Pain is tolerable if the context is right", {"masochism": 3}),
    ("Pain is just pain — I avoid it", {"masochism": 1})
]), tier_role="consistency_check", cg="maso_core")

q(dim, "scenario", "You're wearing a butt plug that's slightly larger than comfortable. The stretch and ache during a meeting/dinner/mundane activity makes you feel:", opts([
    ("Secretly alive — the hidden discomfort connects me to my partner and my body", {"masochism": 5, "submission_spectrum": 3}),
    ("Distracted but in a good way", {"masochism": 4}),
    ("Uncomfortable — I'd rather save it for the bedroom", {"masochism": 2}),
    ("Ridiculous — why would I do this", {"masochism": 1})
]))

# ============================================================
# BONDAGE (20 questions)
# ============================================================
dim = "bondage"

q(dim, "scenario", "Your partner ties your wrists above your head with rope, takes their time with the knots, and then stands back to look at you. You feel:", opts([
    ("Profoundly exposed and aroused — being bound and displayed is intoxicating", {"bondage": 5, "submission_spectrum": 3}),
    ("Excited — the restriction adds a layer of intensity", {"bondage": 4}),
    ("Okay with it — I'm game to try things", {"bondage": 3}),
    ("Anxious — I need to be able to move", {"bondage": 1})
]))

q(dim, "behavioral_recall", "How much experience do you have with rope bondage, cuffs, restraints, or other forms of physical restriction during sex?", opts([
    ("Extensive — I own multiple types of restraints and use them regularly", {"bondage": 5}),
    ("Moderate — I've used restraints in several relationships", {"bondage": 4}),
    ("Minimal — I've tried scarves or handcuffs once or twice", {"bondage": 3}),
    ("None — and I'm not drawn to it", {"bondage": 1})
]), cg="bondage_exp")

q(dim, "somatic", "The feeling of rope being wrapped around your body — not tight, but the texture and pressure of being slowly bound. Your body's response:", opts([
    ("Deep relaxation — each wrap quiets my mind and drops me into my body", {"bondage": 5}),
    ("Heightened arousal — the anticipation of being restrained builds", {"bondage": 4}),
    ("Neutral — it's rope", {"bondage": 2}),
    ("Claustrophobic — I feel trapped before it's even tight", {"bondage": 1})
]))

q(dim, "forced_choice", "Which appeals to you most?", opts([
    ("Full-body rope harness — elaborate, beautiful, restrictive, taking an hour to tie", {"bondage": 5}),
    ("Wrists and ankles secured to the bed — functional restriction, quick to set up", {"bondage": 4}),
    ("Hands held above your head by a partner — no equipment needed", {"bondage": 3}),
    ("No physical restriction — I want full freedom of movement", {"bondage": 1})
]))

q(dim, "scenario", "You come across shibari (Japanese rope bondage) art — images of bodies suspended in intricate rope patterns. Your reaction:", opts([
    ("Deep aesthetic and erotic appreciation — this is one of the most beautiful art forms I know", {"bondage": 5}),
    ("Intrigued and aroused — I'd love to experience that", {"bondage": 4}),
    ("Aesthetically interesting but not arousing", {"bondage": 3}),
    ("It looks dangerous or uncomfortable", {"bondage": 1})
]))

q(dim, "temporal", "How often do you think about or want to incorporate bondage into your sexual experiences?", opts([
    ("Almost always — restraint is a core part of my ideal sex life", {"bondage": 5}),
    ("Frequently — most sessions benefit from some form of bondage", {"bondage": 4}),
    ("Sometimes — it's a nice addition occasionally", {"bondage": 3}),
    ("Rarely or never", {"bondage": 1})
]), cg="bondage_temporal")

q(dim, "scenario", "Your partner blindfolds you, ties your hands behind your back, and then leaves the room. You can't see, can't move, and don't know when they'll return. You feel:", opts([
    ("Completely alive — the sensory deprivation and helplessness heighten everything", {"bondage": 5}),
    ("Nervous but excited — the vulnerability is part of the appeal", {"bondage": 4}),
    ("Very anxious — I need some sensory input", {"bondage": 2}),
    ("Panicked — this is too much", {"bondage": 1})
]))

q(dim, "somatic", "When you test your bonds and realize you truly cannot move — the restraints are secure — your body:", opts([
    ("Settles and surrenders — the inability to escape IS the point", {"bondage": 5}),
    ("Surges with arousal at the helplessness", {"bondage": 4}),
    ("Accepts it calmly", {"bondage": 3}),
    ("Fights harder — I need to know I can get free", {"bondage": 1})
]))

q(dim, "behavioral_recall", "On the tying/rigging side: have you practiced tying, learned knots, studied rope techniques?", opts([
    ("Yes — I've invested significant time in learning to rig safely and beautifully", {"bondage": 5}),
    ("Some — I know the basics and a few patterns", {"bondage": 4}),
    ("I've looked into it a little", {"bondage": 3}),
    ("No — I haven't pursued the technical side", {"bondage": 1})
]), cg="bondage_exp", tags=["nsfw", "bdsm", "bondage", "rigger"])

q(dim, "forced_choice", "Bondage is primarily about:", opts([
    ("The art of restriction — the helplessness, the aesthetics, the trust it requires", {"bondage": 5}),
    ("Enhancing power exchange — making the control physical", {"bondage": 4}),
    ("Novelty — something different to spice things up", {"bondage": 2}),
    ("Something I don't relate to", {"bondage": 1})
]))

q(dim, "scenario", "Suspension bondage — being lifted off the ground entirely in rope. The idea:", opts([
    ("Is a goal I'm actively working toward or have experienced — the ultimate expression of trust and art", {"bondage": 5}),
    ("Is thrilling and I'd try it with the right rigger", {"bondage": 4}),
    ("Is too extreme for me", {"bondage": 2}),
    ("Is terrifying", {"bondage": 1})
]))

q(dim, "scenario", "Your partner slowly wraps rope around your chest in a karada (body harness). It takes 30 minutes. The process itself — not the sex that follows — is:", opts([
    ("One of the most intimate experiences possible — the meditative care, the vulnerability, the art on my body", {"bondage": 5}),
    ("Foreplay of the highest order", {"bondage": 4}),
    ("Pleasant but I'm really waiting for what comes next", {"bondage": 3}),
    ("Boring — can we get to the point?", {"bondage": 1})
]))

q(dim, "temporal", "If you were in a relationship where bondage was never part of sex, how would you feel over time?", opts([
    ("A significant piece of my sexuality would be unfulfilled", {"bondage": 5}),
    ("I'd miss it and request it regularly", {"bondage": 4}),
    ("Mildly disappointed but fine", {"bondage": 3}),
    ("Unaffected", {"bondage": 1})
]), tier_role="consistency_check", cg="bondage_temporal")

q(dim, "scenario", "You discover your partner has a collection of high-quality rope, leather cuffs, a spreader bar, and a bondage bench. Your reaction:", opts([
    ("Thrilled — I want to try everything immediately", {"bondage": 5}),
    ("Very interested — I'd love to explore their collection together", {"bondage": 4}),
    ("Surprised but open-minded", {"bondage": 3}),
    ("Intimidated or turned off", {"bondage": 1})
]))

q(dim, "somatic", "Wearing restraints in daily life — a locked collar, cuffs under clothing, a rope harness beneath your shirt. The constant physical reminder:", opts([
    ("Keeps me in a beautiful state of awareness and connection to my dynamic all day", {"bondage": 5, "submission_spectrum": 3}),
    ("Is exciting as occasional play", {"bondage": 4}),
    ("Sounds uncomfortable for daily wear", {"bondage": 2}),
    ("Has no appeal", {"bondage": 1})
]))

q(dim, "forced_choice", "Your preferred level of restriction:", opts([
    ("Total immobilization — mummification, vacuum beds, full body rope — the more helpless the better", {"bondage": 5}),
    ("Significant but targeted — wrists, ankles, maybe a chest harness", {"bondage": 4}),
    ("Light — hands held or loosely tied", {"bondage": 3}),
    ("None", {"bondage": 1})
]))

q(dim, "scenario", "During bondage, the rope slips and you have a moment where you could free yourself. You:", opts([
    ("Don't even consider it — being bound is a choice, and I'm choosing to stay", {"bondage": 5, "submission_spectrum": 4}),
    ("Stay put and mention the slip so it can be fixed", {"bondage": 4}),
    ("Free myself — the illusion is broken", {"bondage": 2}),
    ("Feel relieved I can get out", {"bondage": 1})
]))

q(dim, "scenario", "Your partner wants to try self-bondage (tying themselves up alone). Your reaction as someone who ties:", opts([
    ("Teach them proper safety protocols — I understand the drive and want them to be safe", {"bondage": 5}),
    ("Concerned about safety but curious", {"bondage": 3}),
    ("Confused — why not wait for a partner?", {"bondage": 2}),
    ("Not applicable — I'm not the tying type", {"bondage": 1})
]), tags=["nsfw", "bdsm", "bondage", "safety"])

q(dim, "behavioral_recall", "The longest you've ever been restrained in a single session:", opts([
    ("Hours — extended bondage is meditative and I settle into it deeply", {"bondage": 5}),
    ("An hour or so — significant but not extreme", {"bondage": 4}),
    ("20-30 minutes", {"bondage": 3}),
    ("A few minutes / never", {"bondage": 1})
]), cg="bondage_exp")

q(dim, "forced_choice", "Bondage photography: if a partner wanted to photograph you bound, your response:", opts([
    ("Enthusiastically yes — the documentation of rope on my body is beautiful", {"bondage": 5}),
    ("Yes, for private use only", {"bondage": 4}),
    ("Uncertain — it feels vulnerable", {"bondage": 2}),
    ("No — I wouldn't want evidence of this", {"bondage": 1})
]))

# ============================================================
# SENSATION PLAY (20 questions)
# ============================================================
dim = "sensation_play"

q(dim, "scenario", "Blindfolded, you feel an ice cube tracing down your sternum followed immediately by hot wax on your inner thigh. The contrast:", opts([
    ("Is exquisite — playing with sensation is one of my deepest pleasures", {"sensation_play": 5}),
    ("Intensely arousing — the unpredictability is thrilling", {"sensation_play": 4}),
    ("Interesting but intense", {"sensation_play": 3}),
    ("Overwhelming — I prefer consistent, predictable touch", {"sensation_play": 1})
]))

q(dim, "somatic", "How sensitive is your body to texture, temperature, and pressure during arousal?", opts([
    ("Extraordinarily — when aroused, a feather and a knife feel like entirely different universes on my skin", {"sensation_play": 5}),
    ("Very — I notice and respond to subtle differences in touch", {"sensation_play": 4}),
    ("Moderately — I have preferences but I'm not hypersensitive", {"sensation_play": 3}),
    ("Not very — sensation is sensation, it all blends together", {"sensation_play": 1})
]), cg="sensation_somatic")

q(dim, "forced_choice", "Which would you choose for an evening of play?", opts([
    ("A full sensory deprivation and overload scene — blindfold, furs, ice, wax, pinwheels, feathers", {"sensation_play": 5}),
    ("Temperature play with ice and warm massage oil", {"sensation_play": 4}),
    ("A mix of firm and gentle touch", {"sensation_play": 3}),
    ("Straightforward physical sex without accessories", {"sensation_play": 1})
]))

q(dim, "scenario", "A Wartenberg wheel (spiked metal pinwheel) is rolled slowly along your inner thigh. The prickling, almost-pain sensation:", opts([
    ("Sends electricity through my entire nervous system — I crave more", {"sensation_play": 5}),
    ("Is thrilling — the border between pleasure and pain is where I live", {"sensation_play": 4}),
    ("Is unusual but I can appreciate it", {"sensation_play": 3}),
    ("Is unpleasant — that's just scratchy", {"sensation_play": 1})
]))

q(dim, "temporal", "How often do you incorporate non-standard sensations (temperature, texture, electrical, vibration) into your sexual play?", opts([
    ("Almost every time — vanilla touch alone isn't enough for me", {"sensation_play": 5}),
    ("Frequently — I have a collection of sensation toys", {"sensation_play": 4}),
    ("Occasionally — as a special treat", {"sensation_play": 3}),
    ("Rarely or never", {"sensation_play": 1})
]), cg="sensation_temporal")

q(dim, "behavioral_recall", "What's the most unusual sensation you've incorporated into sex, and how did you feel about it?", opts([
    ("Something most people would find extreme (electrical play, fire, needles) — and I found it transformative", {"sensation_play": 5}),
    ("Creative use of household items or specialty toys — very enjoyable", {"sensation_play": 4}),
    ("Ice or food — it was fun", {"sensation_play": 3}),
    ("I stick to hands, mouths, and standard toys", {"sensation_play": 1})
]))

q(dim, "scenario", "Electrostimulation — a violet wand crackling across your skin, leaving trails of prickling electricity. This:", opts([
    ("Is incredible — the unique sensation of electricity is in a class by itself", {"sensation_play": 5}),
    ("Is something I'd eagerly try or have enjoyed", {"sensation_play": 4}),
    ("Sounds scary but intriguing", {"sensation_play": 3}),
    ("Is a hard no — electricity and bodies don't mix", {"sensation_play": 1})
]))

q(dim, "somatic", "When a partner alternates between feather-light touch and firm pressure on your skin, your body:", opts([
    ("Becomes a live wire — the contrast makes every nerve ending sing", {"sensation_play": 5}),
    ("Responds strongly — I love the variety", {"sensation_play": 4}),
    ("Notices the difference but isn't dramatically affected", {"sensation_play": 3}),
    ("Prefers consistent touch — the switching is distracting", {"sensation_play": 1})
]))

q(dim, "forced_choice", "Sensory deprivation (blindfold + earplugs or headphones) to heighten remaining senses during play:", opts([
    ("Yes, always — removing senses makes remaining ones explosively sensitive", {"sensation_play": 5}),
    ("Love blindfolds — full deprivation is intense but amazing", {"sensation_play": 4}),
    ("Blindfolds are fun occasionally", {"sensation_play": 3}),
    ("I need all my senses — deprivation makes me anxious", {"sensation_play": 1})
]))

q(dim, "scenario", "Your partner traces a pattern on your inner thigh with an ice cube, then immediately breathes warm air over the cold trail. You:", opts([
    ("Moan involuntarily — this kind of deliberate sensation craft is art", {"sensation_play": 5}),
    ("Shiver with pleasure — the temperature contrast is wonderful", {"sensation_play": 4}),
    ("Find it pleasant enough", {"sensation_play": 3}),
    ("Squirm away — just touch me normally", {"sensation_play": 1})
]))

q(dim, "temporal", "If a partner was skilled in sensation play techniques, how much of your sexual time would you want dedicated to non-genital, non-penetrative sensation exploration?", opts([
    ("As much as half or more — the whole body is an erogenous zone when sensation is done right", {"sensation_play": 5}),
    ("A significant portion — extended sensation play as foreplay", {"sensation_play": 4}),
    ("A little — as warm-up before the main event", {"sensation_play": 3}),
    ("Very little — I want to get to the point", {"sensation_play": 1})
]), cg="sensation_temporal")

q(dim, "scenario", "Knife play — a blade (sharp or dull) drawn across skin. The psychological and physical edge of this:", opts([
    ("Is one of the most intense sensation experiences available — the mind amplifies everything", {"sensation_play": 5, "sadism": 3}),
    ("Intrigues me — the psychological element adds layers", {"sensation_play": 4}),
    ("Scares me but I understand the appeal intellectually", {"sensation_play": 2}),
    ("Is beyond what I'd consider", {"sensation_play": 1})
]))

q(dim, "behavioral_recall", "How do you respond to sensation that hovers on the boundary between pleasure and pain — a firm pinch, nails on skin, teeth on a nipple?", opts([
    ("I live on that boundary — it's where sensation is most vivid", {"sensation_play": 5}),
    ("I lean into it — the ambiguity is exciting", {"sensation_play": 4}),
    ("I can handle it but prefer clear pleasure", {"sensation_play": 3}),
    ("I pull away — I want only pleasant sensation", {"sensation_play": 1})
]))

q(dim, "forced_choice", "Fire play — an alcohol-soaked wand ignited and swept across skin, creating a brief flash of heat without burns. This:", opts([
    ("Is breathtaking — the primal fear plus the actual sensation is unmatched", {"sensation_play": 5}),
    ("Is something I'd try with a skilled practitioner", {"sensation_play": 4}),
    ("Is too risky for me", {"sensation_play": 2}),
    ("Is absolutely not something I'd do", {"sensation_play": 1})
]))

q(dim, "somatic", "During arousal, a partner runs different textures across your body — silk, leather, fur, metal chain. Your body's ability to distinguish and respond to each:", opts([
    ("Is heightened dramatically — each texture creates a completely different sensation landscape", {"sensation_play": 5}),
    ("Is strong — I notice and enjoy the variety", {"sensation_play": 4}),
    ("Is moderate — some textures are nicer than others", {"sensation_play": 3}),
    ("Is limited — they all feel roughly the same when I'm turned on", {"sensation_play": 1})
]), cg="sensation_somatic")

q(dim, "scenario", "Cupping — heated glass cups creating suction on your back or chest. The pulling, warming sensation:", opts([
    ("Is divine — the deep tissue sensation is unlike anything else", {"sensation_play": 5}),
    ("Is interesting — I'd incorporate it into play", {"sensation_play": 4}),
    ("Is more wellness than sex for me", {"sensation_play": 2}),
    ("Has no appeal", {"sensation_play": 1})
]))

q(dim, "forced_choice", "If you had to rank what matters most in a sexual encounter:", opts([
    ("Variety and intensity of sensation — the body being played like an instrument", {"sensation_play": 5}),
    ("Emotional connection expressed through varied, attentive touch", {"sensation_play": 4}),
    ("Passion and chemistry", {"sensation_play": 3}),
    ("Orgasm and physical release", {"sensation_play": 1})
]))

q(dim, "behavioral_recall", "Have you ever spent money on specialty sensation toys (pinwheels, electrical devices, temperature play tools)?", opts([
    ("Yes, significantly — my collection is curated", {"sensation_play": 5}),
    ("Some — I have a few specialty items", {"sensation_play": 4}),
    ("I've used household items creatively", {"sensation_play": 3}),
    ("No", {"sensation_play": 1})
]), cg="sensation_temporal")

q(dim, "scenario", "Sound as sensation — your partner whispers commands directly into your ear while simultaneously using a vibrator at an unpredictable rhythm. The layering of auditory and physical stimulation:", opts([
    ("Creates a symphony — multi-sensory input is how my body reaches its peak states", {"sensation_play": 5}),
    ("Is very effective — combining senses amplifies everything", {"sensation_play": 4}),
    ("Is nice but I could take or leave the layering", {"sensation_play": 3}),
    ("Is overstimulating — one thing at a time", {"sensation_play": 1})
]))

q(dim, "forced_choice", "Your pain and sensation thresholds after orgasm:", opts([
    ("Drop dramatically — post-orgasm my body is hypersensitive and I can barely be touched", {"sensation_play": 5}),
    ("Shift noticeably — I'm more sensitive after", {"sensation_play": 4}),
    ("Change slightly", {"sensation_play": 3}),
    ("Stay about the same", {"sensation_play": 1})
]))

# ============================================================
# POWER EXCHANGE DEPTH (20 questions)
# ============================================================
dim = "power_exchange_depth"

q(dim, "scenario", "A 24/7 power exchange dynamic — where the authority structure doesn't turn off when the scene ends. This concept:", opts([
    ("Is what I'm built for — bedroom-only dynamics feel incomplete", {"power_exchange_depth": 5}),
    ("Deeply appeals to me, though I know it requires exceptional communication", {"power_exchange_depth": 4}),
    ("Is interesting in theory but too much for me in practice", {"power_exchange_depth": 2}),
    ("Sounds unhealthy — power exchange should stay in the bedroom", {"power_exchange_depth": 1})
]))

q(dim, "behavioral_recall", "In your most significant D/s relationship, how far did the power exchange extend beyond the bedroom?", opts([
    ("Into most areas of life — finances, social decisions, daily routines, rules", {"power_exchange_depth": 5}),
    ("Into some areas — specific protocols, check-ins, and standing rules", {"power_exchange_depth": 4}),
    ("Occasionally referenced outside sex but not formally", {"power_exchange_depth": 3}),
    ("Stayed entirely in the bedroom / I haven't had a D/s relationship", {"power_exchange_depth": 1})
]), cg="ped_behavioral")

q(dim, "forced_choice", "The word 'dynamic' vs. 'play.' Which better describes what you want from power exchange?", opts([
    ("Dynamic — this is a relationship structure, not an activity", {"power_exchange_depth": 5}),
    ("Mostly dynamic with dedicated play time", {"power_exchange_depth": 4}),
    ("Mostly play with some dynamic elements", {"power_exchange_depth": 3}),
    ("Play — it's a bedroom activity", {"power_exchange_depth": 1})
]))

q(dim, "scenario", "Your partner has authority over your orgasms 24/7. You need permission to come, whether they're present or not. This level of control:", opts([
    ("Is beautiful — my body's most intimate response belongs to them", {"power_exchange_depth": 5, "submission_spectrum": 4}),
    ("Is very hot — I'd maintain that rule faithfully", {"power_exchange_depth": 4}),
    ("Is interesting for a scene but not sustainable long-term", {"power_exchange_depth": 2}),
    ("Is too invasive", {"power_exchange_depth": 1})
]))

q(dim, "temporal", "How much of your daily life would you ideally want structured by a power exchange dynamic?", opts([
    ("Most of it — I function best within an authority structure", {"power_exchange_depth": 5}),
    ("Several touchpoints throughout the day — morning routines, check-ins, rules", {"power_exchange_depth": 4}),
    ("Evenings and weekends — when we're together", {"power_exchange_depth": 3}),
    ("Only during specifically designated play time", {"power_exchange_depth": 1})
]), cg="ped_temporal")

q(dim, "scenario", "Financial control — your partner manages your discretionary spending, you ask before purchases above a certain amount. This:", opts([
    ("Is a natural extension of the authority exchange — I trust their judgment", {"power_exchange_depth": 5}),
    ("Goes too far for me — there are limits to what I'd yield", {"power_exchange_depth": 2}),
    ("Feels like a red flag for abuse disguised as kink", {"power_exchange_depth": 1}),
    ("Is something I'd consider with extensive safeguards", {"power_exchange_depth": 3})
]), tier_role="trap", trap=True, tags=["nsfw", "bdsm", "power_exchange_depth", "lifestyle", "safety"])

q(dim, "behavioral_recall", "Have you participated in a formal collaring ceremony or a similar ritual to mark the commitment of a D/s dynamic?", opts([
    ("Yes — it was one of the most meaningful rituals of my life", {"power_exchange_depth": 5}),
    ("Not yet but I deeply want to", {"power_exchange_depth": 4}),
    ("I'd be open to it", {"power_exchange_depth": 3}),
    ("No and it doesn't appeal to me", {"power_exchange_depth": 1})
]), cg="ped_behavioral")

q(dim, "forced_choice", "D/s contracts — formal written agreements outlining rules, protocols, limits, and responsibilities. Your view:", opts([
    ("Essential — they create clarity, accountability, and a reference point for the dynamic", {"power_exchange_depth": 5}),
    ("Very useful — I'd want one in a serious D/s relationship", {"power_exchange_depth": 4}),
    ("Interesting but probably overkill", {"power_exchange_depth": 2}),
    ("Unnecessary — dynamics should be organic, not legalistic", {"power_exchange_depth": 1})
]))

q(dim, "scenario", "You attend a munch (kink community social) and meet others in 24/7 dynamics. Learning about how they structure daily life with power exchange:", opts([
    ("Feels like coming home — I relate deeply and want this for myself", {"power_exchange_depth": 5}),
    ("Is fascinating and aspirational", {"power_exchange_depth": 4}),
    ("Is interesting but extreme for my taste", {"power_exchange_depth": 2}),
    ("Seems like an unhealthy co-dependency dressed up as kink", {"power_exchange_depth": 1})
]), tier_role="trap", trap=True)

q(dim, "temporal", "Over time in a power exchange relationship, do you want the exchange to deepen (more areas of control/service) or stay stable?", opts([
    ("Deepen — a dynamic that stays static feels stagnant to me", {"power_exchange_depth": 5}),
    ("Gradually deepen as trust grows", {"power_exchange_depth": 4}),
    ("Stay stable — find a level and maintain it", {"power_exchange_depth": 3}),
    ("I'd want to pull back over time as the relationship matures", {"power_exchange_depth": 1})
]), cg="ped_temporal")

q(dim, "scenario", "Your Dominant restructures your morning routine — specific wake time, exercise, grooming standards, a text when you're ready. Following this structure:", opts([
    ("Grounds my entire day — I perform better with their framework around me", {"power_exchange_depth": 5, "service_orientation": 3}),
    ("Feels caring and connecting — I enjoy the structure", {"power_exchange_depth": 4}),
    ("Is a bit much for mornings", {"power_exchange_depth": 2}),
    ("Is controlling in a bad way", {"power_exchange_depth": 1})
]))

q(dim, "forced_choice", "The core of what you want from power exchange:", opts([
    ("A complete relationship structure — authority, service, care, and accountability woven into everything", {"power_exchange_depth": 5}),
    ("A deep dynamic that enriches the relationship beyond just sex", {"power_exchange_depth": 4}),
    ("Hot sex with defined roles", {"power_exchange_depth": 3}),
    ("Occasional role play", {"power_exchange_depth": 1})
]), tier_role="consistency_check", cg="ped_core")

q(dim, "scenario", "Master/slave vs. Dominant/submissive. Do you know the difference, and which resonates more?", opts([
    ("Yes — M/s resonates. The depth of surrender and authority in M/s is what I seek", {"power_exchange_depth": 5}),
    ("Yes — D/s resonates. Deep but with more negotiated flexibility", {"power_exchange_depth": 4}),
    ("Vaguely — I think of them as roughly the same", {"power_exchange_depth": 2}),
    ("Neither — these labels don't apply to me", {"power_exchange_depth": 1})
]))

q(dim, "behavioral_recall", "How much have you studied, read about, or participated in the broader BDSM/kink community?", opts([
    ("Extensively — workshops, books, munches, classes, mentors — this is my community", {"power_exchange_depth": 5}),
    ("Significantly — I've read books and attended events", {"power_exchange_depth": 4}),
    ("Some — primarily online research", {"power_exchange_depth": 3}),
    ("Minimally", {"power_exchange_depth": 1})
]), cg="ped_behavioral")

q(dim, "scenario", "A respected community member offers to mentor you in your D/s journey. You:", opts([
    ("Accept eagerly — mentorship and knowledge transmission are valued traditions in this lifestyle", {"power_exchange_depth": 5}),
    ("Accept with interest — guidance from experienced people is valuable", {"power_exchange_depth": 4}),
    ("Consider it but feel uncomfortable — my sex life is private", {"power_exchange_depth": 2}),
    ("Decline — I don't need guidance in this area", {"power_exchange_depth": 1})
]))

q(dim, "forced_choice", "Safewords — how do you think about them?", opts([
    ("Essential foundation that makes deep power exchange possible — they enable the illusion of absolute control", {"power_exchange_depth": 5}),
    ("Non-negotiable safety tool that I always establish", {"power_exchange_depth": 4}),
    ("Important for intense scenes", {"power_exchange_depth": 3}),
    ("I've never needed one / don't do scenes intense enough to require one", {"power_exchange_depth": 1})
]))

q(dim, "scenario", "Your non-kinky friend finds out about your dynamic and says 'That sounds abusive.' You:", opts([
    ("Calmly explain the difference between consensual power exchange and abuse — I'm secure in my choices", {"power_exchange_depth": 5}),
    ("Feel a pang but know the difference — consent and communication make it healthy", {"power_exchange_depth": 4}),
    ("Wonder if they have a point", {"power_exchange_depth": 2}),
    ("Feel ashamed", {"power_exchange_depth": 1})
]))

q(dim, "temporal", "How consistently do you maintain power exchange protocols (titles, rules, rituals) even when stressed, sick, or going through a difficult time?", opts([
    ("The protocols are the scaffolding that gets us through hard times — we lean into them more, not less", {"power_exchange_depth": 5}),
    ("We maintain core elements and release less essential ones", {"power_exchange_depth": 4}),
    ("We pause the dynamic during hard times", {"power_exchange_depth": 2}),
    ("Hard times show why power exchange can't be a full-time thing", {"power_exchange_depth": 1})
]), cg="ped_temporal")

q(dim, "forced_choice", "Vulnerability in power exchange — the person who holds more vulnerability is:", opts([
    ("Both equally — the Dominant's vulnerability in holding authority matches the submissive's in yielding it", {"power_exchange_depth": 5}),
    ("The submissive — they're the one giving up control", {"power_exchange_depth": 3}),
    ("The Dominant — they carry the weight of responsibility", {"power_exchange_depth": 3}),
    ("Neither — it's just sex with roles", {"power_exchange_depth": 1})
]))

# ============================================================
# PROTOCOL ORIENTATION (20 questions)
# ============================================================
dim = "protocol_orientation"

q(dim, "scenario", "Your Dominant establishes a set of daily protocols: specific morning greeting, kneeling when they come home, asking permission before eating. This level of structure:", opts([
    ("Is my ideal — protocols create the container for the dynamic to live in", {"protocol_orientation": 5}),
    ("Appeals to me — I enjoy having rituals that maintain the dynamic", {"protocol_orientation": 4}),
    ("Is too much structure for daily life", {"protocol_orientation": 2}),
    ("Sounds like playing house — real relationships don't need scripts", {"protocol_orientation": 1})
]))

q(dim, "forced_choice", "High protocol (formal, many rules, structured) vs. low protocol (casual, organic, fluid). You prefer:", opts([
    ("High protocol — the formality deepens the power exchange", {"protocol_orientation": 5}),
    ("Medium-high — clear structure with room for personality", {"protocol_orientation": 4}),
    ("Medium-low — a few guidelines but mostly organic", {"protocol_orientation": 3}),
    ("Low protocol — rules kill the chemistry", {"protocol_orientation": 1})
]))

q(dim, "behavioral_recall", "In past relationships or dynamics, how many standing rules or protocols have you maintained simultaneously?", opts([
    ("10+ — they covered speech, behavior, dress, routines, communication", {"protocol_orientation": 5}),
    ("5-10 — a meaningful structure of rules", {"protocol_orientation": 4}),
    ("2-4 — a few key ones", {"protocol_orientation": 3}),
    ("0-1 — rules aren't my thing", {"protocol_orientation": 1})
]), cg="protocol_behavioral")

q(dim, "scenario", "Position training — learning specific positions (present, kneel, display) and being expected to assume them on command. This:", opts([
    ("Is deeply fulfilling — my body in their chosen position is an act of worship", {"protocol_orientation": 5, "submission_spectrum": 4}),
    ("Is sexy — having trained positions adds formality I enjoy", {"protocol_orientation": 4}),
    ("Is fun for scenes", {"protocol_orientation": 3}),
    ("Feels silly or dehumanizing", {"protocol_orientation": 1})
]))

q(dim, "temporal", "How quickly do protocols and rituals start feeling like 'just how we do things' vs. feeling performative?", opts([
    ("Within days — I internalize structure quickly and it becomes natural", {"protocol_orientation": 5}),
    ("Within a few weeks — it takes practice but becomes routine", {"protocol_orientation": 4}),
    ("Slowly — protocols always feel somewhat performative to me", {"protocol_orientation": 2}),
    ("They never stop feeling forced", {"protocol_orientation": 1})
]), cg="protocol_temporal")

q(dim, "forced_choice", "Speech protocols — using titles, speaking in third person, asking permission to speak. You:", opts([
    ("Love them — language shapes reality, and formal speech keeps me in headspace", {"protocol_orientation": 5}),
    ("Enjoy titles at minimum — 'Sir,' 'Daddy,' etc. matter to me", {"protocol_orientation": 4}),
    ("Can do it in scenes but not consistently", {"protocol_orientation": 3}),
    ("Find modified speech patterns degrading or ridiculous", {"protocol_orientation": 1})
]))

q(dim, "scenario", "You forget a protocol — you sit before being given permission. Your partner corrects you. Your response:", opts([
    ("Genuine remorse and gratitude for the correction — maintaining protocol matters", {"protocol_orientation": 5}),
    ("Apologize and correct myself — mistakes happen but I take it seriously", {"protocol_orientation": 4}),
    ("Shrug it off — it's not a big deal", {"protocol_orientation": 2}),
    ("Feel annoyed — correcting small things is controlling", {"protocol_orientation": 1})
]))

q(dim, "behavioral_recall", "Have you ever created a protocol manual, rule book, or formal structure document for a D/s relationship?", opts([
    ("Yes — and maintaining it was an ongoing, rewarding project", {"protocol_orientation": 5}),
    ("Yes — at least a written list of rules and expectations", {"protocol_orientation": 4}),
    ("Verbal agreements only", {"protocol_orientation": 3}),
    ("No — nothing formal", {"protocol_orientation": 1})
]), cg="protocol_behavioral")

q(dim, "scenario", "At a formal BDSM event (high protocol), submissives kneel beside their Dominants, speak when spoken to, and serve food and drink. This environment:", opts([
    ("Is magnificent — high protocol events are where I feel most at home", {"protocol_orientation": 5}),
    ("Is exciting and aspirational", {"protocol_orientation": 4}),
    ("Is interesting to observe but too intense to participate in", {"protocol_orientation": 2}),
    ("Makes me uncomfortable — it looks like oppression", {"protocol_orientation": 1})
]))

q(dim, "forced_choice", "The purpose of protocol in D/s is primarily:", opts([
    ("To create a living structure where power exchange breathes in every interaction", {"protocol_orientation": 5}),
    ("To maintain awareness of the dynamic throughout the day", {"protocol_orientation": 4}),
    ("To add formality to scenes and play", {"protocol_orientation": 3}),
    ("Unnecessary — power exchange doesn't need rules", {"protocol_orientation": 1})
]), tier_role="consistency_check", cg="protocol_core")

# ============================================================
# SERVICE ORIENTATION (20 questions)
# ============================================================
dim = "service_orientation"

q(dim, "scenario", "Your Dominant comes home exhausted. Without being asked, you draw a bath, prepare their drink, lay out comfortable clothes, and kneel to remove their shoes. This feels:", opts([
    ("Like my purpose — anticipatory service is how I show love and devotion", {"service_orientation": 5}),
    ("Deeply satisfying — caring for them in this way connects us", {"service_orientation": 4}),
    ("Nice to do sometimes but not a regular thing", {"service_orientation": 3}),
    ("Degrading — I'm not a servant", {"service_orientation": 1})
]))

q(dim, "behavioral_recall", "How naturally does service (not just sexual service — domestic, emotional, practical service) come to you in a relationship?", opts([
    ("It's my primary love language — I find deep fulfillment in making their life better", {"service_orientation": 5}),
    ("Very naturally — I enjoy taking care of a partner", {"service_orientation": 4}),
    ("Moderately — I do my share but it's not what drives me", {"service_orientation": 3}),
    ("Not naturally — I believe in equal distribution, not service", {"service_orientation": 1})
]), cg="service_behavioral")

q(dim, "forced_choice", "The idea of being a 'service submissive' — where your role centers on making your Dominant's life smoother, better, more comfortable:", opts([
    ("Is my identity — service is the vehicle through which I express my submission", {"service_orientation": 5}),
    ("Strongly appeals to me", {"service_orientation": 4}),
    ("Appeals somewhat — mixed with other forms of submission", {"service_orientation": 3}),
    ("Doesn't resonate — submission for me isn't about service", {"service_orientation": 1})
]))

q(dim, "scenario", "Your Dominant asks you to learn to cook their favorite meal perfectly, to iron their shirts exactly the way they like, to memorize how they take their coffee. The precision required:", opts([
    ("Excites me — learning their preferences in detail is an act of devotion", {"service_orientation": 5}),
    ("Is rewarding — I enjoy mastering skills for their benefit", {"service_orientation": 4}),
    ("Is a lot — I'd try but resent the perfectionism", {"service_orientation": 2}),
    ("Is unreasonable — make your own coffee", {"service_orientation": 1})
]))

q(dim, "somatic", "When you've served someone well — completed a task to their satisfaction, anticipated a need — what does your body feel?", opts([
    ("A warm glow of completion — like a circuit closing, a deep rightness", {"service_orientation": 5}),
    ("Pride and pleasure — satisfaction at a job well done", {"service_orientation": 4}),
    ("Normal — it's nice but not a physical sensation", {"service_orientation": 2}),
    ("Nothing notable", {"service_orientation": 1})
]), cg="service_somatic")

q(dim, "temporal", "In a relationship, how much of your mental energy goes toward thinking about what your partner needs, wants, or would enjoy?", opts([
    ("A significant portion — their needs are always running in my background processes", {"service_orientation": 5}),
    ("Frequently — I think about how to please them often", {"service_orientation": 4}),
    ("Sometimes — when it occurs to me", {"service_orientation": 3}),
    ("Rarely — I expect them to communicate their needs directly", {"service_orientation": 1})
]), cg="service_temporal")

q(dim, "scenario", "Sexual service — performing oral sex because your partner wants it, regardless of your current desire, purely because serving their pleasure is your role. This framing:", opts([
    ("Is how I think about sex in a dynamic — my pleasure comes through their pleasure", {"service_orientation": 5, "submission_spectrum": 4}),
    ("Is very appealing — I enjoy being used for their pleasure", {"service_orientation": 4}),
    ("Is okay sometimes but I need my pleasure prioritized too", {"service_orientation": 2}),
    ("Is unacceptable — mutual desire matters every time", {"service_orientation": 1})
]))

q(dim, "forced_choice", "Domestic service (cleaning, cooking, organizing) as part of a D/s dynamic vs. as shared household responsibility:", opts([
    ("Transforms mundane tasks into acts of devotion — context is everything", {"service_orientation": 5}),
    ("Adds meaning to things I'd do anyway", {"service_orientation": 4}),
    ("Doesn't change how the tasks feel — chores are chores", {"service_orientation": 2}),
    ("Making household chores part of a power dynamic is problematic", {"service_orientation": 1})
]))

q(dim, "behavioral_recall", "Have you ever been told you're 'too giving,' 'too accommodating,' or that you neglect your own needs for a partner's?", opts([
    ("Yes — and in a D/s context, that giving nature finally has a healthy structure", {"service_orientation": 5}),
    ("Yes — I do tend to prioritize others", {"service_orientation": 4}),
    ("Occasionally", {"service_orientation": 3}),
    ("No — I maintain strong boundaries around my own needs", {"service_orientation": 1})
]), tier_role="trap", trap=True, tags=["nsfw", "bdsm", "service_orientation", "codependency_screen"])

q(dim, "scenario", "Your partner is entertaining friends. They expect you to serve drinks, prepare food, and ensure everyone is comfortable — as an expression of your dynamic. This:", opts([
    ("Would make me proud — serving well reflects on both of us", {"service_orientation": 5}),
    ("Is fun — I enjoy being the attentive one", {"service_orientation": 4}),
    ("Is fine at home but awkward in front of others", {"service_orientation": 2}),
    ("Is embarrassing — I'm not staff", {"service_orientation": 1})
]))

q(dim, "forced_choice", "If your Dominant told you your service was the single thing they valued most about your dynamic — more than sex, more than pain play — you would feel:", opts([
    ("Deeply validated — service IS my submission", {"service_orientation": 5}),
    ("Very pleased — that's a meaningful compliment", {"service_orientation": 4}),
    ("Somewhat disappointed — I want to be valued for more than service", {"service_orientation": 3}),
    ("Confused — why would service be valued above connection?", {"service_orientation": 1})
]), tier_role="consistency_check", cg="service_core")

q(dim, "scenario", "You're assigned a weekly task that serves no practical purpose — it exists solely as an act of obedience (e.g., writing lines, completing a specific ritual). You:", opts([
    ("Find meaning in the purposelessness — obedience itself is the point", {"service_orientation": 5, "submission_spectrum": 4}),
    ("Do it — if it matters to them, it matters to me", {"service_orientation": 4}),
    ("Feel frustrated — I want my service to be useful", {"service_orientation": 2}),
    ("Refuse — pointless tasks are disrespectful of my time", {"service_orientation": 1})
]))

# ============================================================
# SWITCH CAPACITY (20 questions)
# ============================================================
dim = "switch_capacity"

q(dim, "scenario", "During sex, your partner who usually submits to you suddenly takes charge — pins you down, gives you instructions, takes control. You:", opts([
    ("Melt — I love switching, and their dominance is as hot as their submission", {"switch_capacity": 5}),
    ("Enjoy it — the novelty and role reversal is exciting", {"switch_capacity": 4}),
    ("Feel disoriented — this isn't our dynamic", {"switch_capacity": 2}),
    ("Resist — I don't want to be dominated", {"switch_capacity": 1})
]))

q(dim, "behavioral_recall", "How often do you switch roles (top/bottom, D/s, giving/receiving pain) within a single relationship?", opts([
    ("Regularly — switching is core to my identity, not an exception", {"switch_capacity": 5}),
    ("Sometimes — I have a primary orientation but enjoy switching occasionally", {"switch_capacity": 4}),
    ("Rarely — once or twice with the right partner", {"switch_capacity": 3}),
    ("Never — my role is fixed", {"switch_capacity": 1})
]), cg="switch_behavioral")

q(dim, "forced_choice", "When you hear 'switch,' you think:", opts([
    ("That's me — I contain both energies fully, not as a compromise but as completeness", {"switch_capacity": 5}),
    ("I'm primarily one orientation but switching is in my range", {"switch_capacity": 4}),
    ("Sounds confusing — pick a lane", {"switch_capacity": 2}),
    ("Not me — I'm firmly on one side", {"switch_capacity": 1})
]))

q(dim, "scenario", "You're at a play party. An attractive person you've played with before asks you to top them tonight — you normally bottom. You:", opts([
    ("Shift gears naturally — my dominant side activates as easily as my submissive side", {"switch_capacity": 5}),
    ("Consider it — with the right energy I could do it", {"switch_capacity": 4}),
    ("Decline — I'd be performing, not feeling it", {"switch_capacity": 2}),
    ("Decline firmly — that's not who I am", {"switch_capacity": 1})
]))

q(dim, "somatic", "Can you access dominant energy AND submissive energy authentically — not performing one while being the other?", opts([
    ("Yes — they're both genuinely me, just different modes", {"switch_capacity": 5}),
    ("Mostly — one feels slightly more natural but both are real", {"switch_capacity": 4}),
    ("One feels authentic, the other feels like acting", {"switch_capacity": 2}),
    ("Only one is real — the other is foreign", {"switch_capacity": 1})
]), cg="switch_somatic")

q(dim, "temporal", "Over time, has your dominant/submissive orientation shifted, or has it been stable?", opts([
    ("It shifts — sometimes I'm deeply dominant for months, then submissive. Both states are equally me", {"switch_capacity": 5}),
    ("Mostly stable with occasional shifts based on partner or mood", {"switch_capacity": 4}),
    ("Deepened in one direction over time", {"switch_capacity": 2}),
    ("Always been the same", {"switch_capacity": 1})
]), cg="switch_temporal")

q(dim, "scenario", "With Partner A you're dominant. With Partner B you're submissive. Both are authentic and deeply fulfilling. This:", opts([
    ("Is my ideal — different partners bring out different aspects of my full self", {"switch_capacity": 5}),
    ("Is appealing — I can see how that would work", {"switch_capacity": 4}),
    ("Sounds unstable — how can you be both?", {"switch_capacity": 2}),
    ("Doesn't resonate — I'm the same in every dynamic", {"switch_capacity": 1})
]))

q(dim, "forced_choice", "The biggest challenge of being a switch (if you are one):", opts([
    ("Finding partners who value and can receive BOTH sides equally", {"switch_capacity": 5}),
    ("Being taken seriously — people assume you're undecided", {"switch_capacity": 4}),
    ("I'm not really a switch — I have a clear preference", {"switch_capacity": 2}),
    ("This doesn't apply to me", {"switch_capacity": 1})
]))

q(dim, "scenario", "In a single scene, you start by dominating your partner, then they flip you and take over. The transition itself:", opts([
    ("Is one of the most electric moments possible — the power reversal IS the kink", {"switch_capacity": 5}),
    ("Is exciting when it happens organically", {"switch_capacity": 4}),
    ("Is jarring — I'd rather commit to one role per scene", {"switch_capacity": 2}),
    ("Wouldn't happen — I maintain my role", {"switch_capacity": 1})
]))

q(dim, "behavioral_recall", "Have you ever been surprised by a dominant urge while in a submissive headspace, or vice versa?", opts([
    ("Frequently — my orientation is fluid and responsive to the energy in the room", {"switch_capacity": 5}),
    ("A few times — it caught me off guard but felt natural", {"switch_capacity": 4}),
    ("Once or twice — it felt like an anomaly", {"switch_capacity": 3}),
    ("Never — my headspace is consistent", {"switch_capacity": 1})
]), cg="switch_behavioral")

# Total so far: 20+20+20+20+20+20+20+20+10+10 = ~200

# Fill remaining to get to 200 total with mixed dimensions for triangulation and consistency

# Additional cross-cutting / triangulation questions
q("dominance_spectrum", "forced_choice", "When choosing porn or erotica, you're drawn to content where:", opts([
    ("Someone is clearly in command — giving orders, using, directing", {"dominance_spectrum": 5}),
    ("There's a visible power dynamic but it shifts back and forth", {"switch_capacity": 4}),
    ("Someone is surrendering — being used, following instructions, serving", {"submission_spectrum": 5}),
    ("It's equal and reciprocal — no power dynamic", {"dominance_spectrum": 1, "submission_spectrum": 1})
]), tier_role="triangulation", tags=["nsfw", "bdsm", "triangulation"])

q("sadism", "scenario", "Your partner asks you to humiliate them — call them degrading names, make them beg, treat them as less than. You:", opts([
    ("Excel at this — psychological edge play is as arousing to me as physical", {"sadism": 5, "dominance_spectrum": 4}),
    ("Can do it with enthusiastic consent and clear boundaries", {"sadism": 4}),
    ("Struggle — even with consent, degradation feels wrong", {"sadism": 2}),
    ("Refuse — I won't treat someone that way", {"sadism": 1})
]))

q("masochism", "scenario", "Humiliation — being called degrading names, being made to beg, being treated as less than. Your response:", opts([
    ("Can send me into deep subspace — psychological pain is as potent as physical for me", {"masochism": 5, "submission_spectrum": 4}),
    ("Is exciting with the right person in the right context", {"masochism": 4}),
    ("Is a hard limit — pain yes, degradation no", {"masochism": 2}),
    ("Is off the table entirely", {"masochism": 1})
]))

q("bondage", "forced_choice", "Predicament bondage (tied so that any movement causes a consequence — pulling a nipple clamp, tightening a rope) vs. comfortable bondage (restrained but not in pain):", opts([
    ("Predicament — the mental and physical challenge is the point", {"bondage": 5, "masochism": 4}),
    ("Either, depending on mood — both have their place", {"bondage": 4}),
    ("Comfortable — I want restriction without discomfort", {"bondage": 3}),
    ("Neither", {"bondage": 1})
]))

q("sensation_play", "scenario", "Your partner uses a tens unit (electrical muscle stimulation) on your inner thighs during oral sex. The combination of electric pulses and sexual stimulation:", opts([
    ("Is transcendent — layered, multi-source sensation is my ideal", {"sensation_play": 5}),
    ("Is very exciting — the addition of electricity heightens everything", {"sensation_play": 4}),
    ("Is distracting — I'd rather focus on one thing", {"sensation_play": 2}),
    ("Is unwelcome — keep electricity away from sex", {"sensation_play": 1})
]))

q("power_exchange_depth", "scenario", "Your partner introduces 'protocols for travel' — specific rules for how you behave in hotels, airports, restaurants while traveling together. This:", opts([
    ("Thrills me — the dynamic traveling with us means it's real, not just a bedroom game", {"power_exchange_depth": 5, "protocol_orientation": 4}),
    ("Is exciting — maintaining the dynamic outside our usual context deepens it", {"power_exchange_depth": 4}),
    ("Is impractical — travel is stressful enough", {"power_exchange_depth": 2}),
    ("Is controlling — vacation should be relaxation, not performance", {"power_exchange_depth": 1})
]))

q("protocol_orientation", "scenario", "Formal address — your partner requires you to use 'Sir/Ma'am/Daddy/Mistress' in all private communication, including texts. This:", opts([
    ("Is natural — the title reminds me of our dynamic with every message", {"protocol_orientation": 5}),
    ("Is hot in person but feels performative in texts", {"protocol_orientation": 3}),
    ("Is too much for daily communication", {"protocol_orientation": 2}),
    ("Is ridiculous in text form", {"protocol_orientation": 1})
]))

q("service_orientation", "scenario", "You're sick. Your Dominant suspends all protocols and takes care of YOU — brings you soup, cancels your tasks, nurtures you. This makes you feel:", opts([
    ("Deeply loved AND slightly bereft — I miss serving even when I'm sick", {"service_orientation": 5}),
    ("Cared for and grateful — the dynamic flexes when it needs to", {"service_orientation": 4}),
    ("Relieved — finally a break from the structure", {"service_orientation": 2}),
    ("This is how it should always be — mutual, not one-directional", {"service_orientation": 1})
]), tier_role="trap", trap=True, tags=["nsfw", "bdsm", "service_orientation", "dynamic_health"])

q("switch_capacity", "scenario", "A partner says: 'I need you to dominate me tonight. I can't be strong right now.' You normally submit to them. You:", opts([
    ("Step into the role seamlessly — I can be their strength when they need it", {"switch_capacity": 5}),
    ("Do my best — it's not my natural mode but I care about them", {"switch_capacity": 3}),
    ("Feel lost — I don't know how to be dominant", {"switch_capacity": 2}),
    ("Say no — that's not who I am in this relationship", {"switch_capacity": 1})
]))

q("dominance_spectrum", "scenario", "You're in a group dynamic (triad, polycule) where you're the dominant over multiple submissives. Managing multiple people's needs, rules, and dynamics:", opts([
    ("Is where I shine — leading a household or group dynamic is my calling", {"dominance_spectrum": 5, "power_exchange_depth": 5}),
    ("Is appealing but demanding — I could manage two, maybe three", {"dominance_spectrum": 4}),
    ("Is overwhelming — one dynamic is enough", {"dominance_spectrum": 3}),
    ("Has no appeal", {"dominance_spectrum": 1})
]))

q("submission_spectrum", "scenario", "You're one of multiple submissives to the same Dominant. The idea of having a 'sister/brother submissive' and your place in a hierarchy:", opts([
    ("Is appealing — I thrive in structured systems and sharing service", {"submission_spectrum": 5, "service_orientation": 4}),
    ("Is interesting — I'd consider it with the right people", {"submission_spectrum": 4}),
    ("Triggers jealousy — I want to be the only one", {"submission_spectrum": 2}),
    ("Is unappealing — one-to-one dynamics only", {"submission_spectrum": 1})
]))

q("sadism", "forced_choice", "Aftercare following an intense scene — you were the one causing the pain. Your aftercare needs:", opts([
    ("Are real — I need to decompress from the intensity of holding someone's pain just as they need to come down from receiving it", {"sadism": 5}),
    ("Exist but are smaller — I mainly focus on my partner's needs", {"sadism": 4}),
    ("Are minimal — I don't process causing pain the same way they process receiving it", {"sadism": 2}),
    ("Don't apply — I don't cause pain", {"sadism": 1})
]), tags=["nsfw", "bdsm", "sadism", "aftercare"])

q("masochism", "scenario", "You discover that a specific type of pain (e.g., impact on your thighs, nipple torture, caning) reliably triggers orgasm for you. This:", opts([
    ("Doesn't surprise me — my body has always wired pain and pleasure together", {"masochism": 5}),
    ("Is an exciting discovery — pain-gasm is a gift", {"masochism": 4}),
    ("Would be surprising but welcome", {"masochism": 3}),
    ("Seems unlikely for me — pain and orgasm don't connect", {"masochism": 1})
]))

q("bondage", "scenario", "Self-bondage (tying yourself up, with safety measures, for solo play). Your response:", opts([
    ("I've done it or would — the sensation and restriction is valuable even alone", {"bondage": 5}),
    ("Intriguing but safety concerns give me pause", {"bondage": 3}),
    ("Pointless — bondage requires a partner for the power exchange element", {"bondage": 2}),
    ("No interest", {"bondage": 1})
]))

q("sensation_play", "somatic", "How does your body respond to unexpected touch during high arousal — a sudden pinch, scratch, or temperature change you didn't anticipate?", opts([
    ("Intensifies everything — surprise sensation when I'm aroused is electric", {"sensation_play": 5}),
    ("A sharp but pleasurable jolt", {"sensation_play": 4}),
    ("Startling — takes me out of the moment briefly", {"sensation_play": 2}),
    ("Unpleasant — I need predictable touch when aroused", {"sensation_play": 1})
]))

q("power_exchange_depth", "forced_choice", "Total power exchange (TPE) — where theoretically nothing is off-limits and the Dominant has authority over all aspects of life. Your view:", opts([
    ("Is the deepest form of trust and intimacy humans can achieve", {"power_exchange_depth": 5}),
    ("Is an ideal to approach asymptotically — full TPE is theoretical but striving toward it matters", {"power_exchange_depth": 4}),
    ("Goes too far — some areas of life should never be under someone else's control", {"power_exchange_depth": 2}),
    ("Is inherently abusive regardless of consent", {"power_exchange_depth": 1})
]), tier_role="trap", trap=True)

q("protocol_orientation", "behavioral_recall", "When protocols are removed or paused (e.g., during vanilla time, visiting family), do you feel:", opts([
    ("Unmoored — without the structure, I feel disconnected from my partner and my role", {"protocol_orientation": 5}),
    ("Slightly adrift — I miss the touchpoints", {"protocol_orientation": 4}),
    ("Relieved — vanilla time is a break I enjoy", {"protocol_orientation": 2}),
    ("Normal — protocols don't affect my baseline state", {"protocol_orientation": 1})
]), cg="protocol_temporal")

q("service_orientation", "scenario", "Your Dominant gives you a task that's genuinely unpleasant — scrubbing a bathroom floor on your hands and knees while they watch. The combination of menial labor and being observed:", opts([
    ("Is deeply submissive — the mundanity is the point, my willingness to do anything is the offering", {"service_orientation": 5, "submission_spectrum": 4}),
    ("Is arousing in context — the power dynamic transforms the task", {"service_orientation": 4}),
    ("Is humiliating in a bad way", {"service_orientation": 1}),
    ("Is just... cleaning a bathroom. I'd rather do it without being watched", {"service_orientation": 2})
]))

q("switch_capacity", "temporal", "In your fantasy life, what percentage of the time are you dominant vs. submissive?", opts([
    ("It genuinely splits close to 50/50", {"switch_capacity": 5}),
    ("Maybe 70/30 one way — I have a lean but both are present", {"switch_capacity": 4}),
    ("90/10 — one side dominates but the other exists", {"switch_capacity": 3}),
    ("100/0 — I only fantasize from one role", {"switch_capacity": 1})
]), cg="switch_temporal")

print(f"Total questions: {len(questions)}")
with open("/Users/user/personal/sb/trueassess/priv/question_bank/bdsm_role.json", "w") as f:
    json.dump(questions, f, indent=2)
print("Written bdsm_role.json")
