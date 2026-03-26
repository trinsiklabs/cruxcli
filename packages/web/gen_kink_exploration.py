import json

questions = []
uid_counter = 1

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

# ============================================================
# KINK CURIOSITY (28 questions)
# ============================================================
dim = "kink_curiosity"

q(dim, "scenario", "You stumble across a kink you've never heard of before. Your first reaction:", opts([
    ("Immediate fascination — I want to research it, understand it, and consider whether it might be for me", {"kink_curiosity": 5}),
    ("Curious — I'll look into it and see if it resonates", {"kink_curiosity": 4}),
    ("Mild interest — I might read one article", {"kink_curiosity": 3}),
    ("Indifference or discomfort — I know what I like and I'm not looking for more", {"kink_curiosity": 1})
]))

q(dim, "behavioral_recall", "In the past year, how many new sexual activities, kinks, or dynamics have you actively researched or tried?", opts([
    ("5+ — I'm constantly exploring and adding to my repertoire", {"kink_curiosity": 5}),
    ("3-4 — I make a point of trying new things", {"kink_curiosity": 4}),
    ("1-2 — when something catches my attention", {"kink_curiosity": 3}),
    ("None — I'm satisfied with what I already know and do", {"kink_curiosity": 1})
]), cg="curiosity_behavioral")

q(dim, "forced_choice", "A partner says 'I've never told anyone this fantasy.' You feel:", opts([
    ("Honored and immediately intrigued — sharing taboo desires is the deepest intimacy", {"kink_curiosity": 5}),
    ("Curious and open — I want to hear it", {"kink_curiosity": 4}),
    ("Nervous but willing to listen", {"kink_curiosity": 3}),
    ("Anxious — what if it's something I can't handle?", {"kink_curiosity": 1})
]))

q(dim, "temporal", "How has your interest in exploring new kinks changed over time?", opts([
    ("It's grown — the more I explore, the more I want to explore", {"kink_curiosity": 5}),
    ("Stayed consistently high", {"kink_curiosity": 4}),
    ("Peaked early and settled into preferences", {"kink_curiosity": 3}),
    ("Decreased — I'm less experimental than I used to be", {"kink_curiosity": 1})
]), cg="curiosity_temporal")

q(dim, "scenario", "A friend invites you to a kink education workshop on a topic you've never tried (e.g., needle play, fire play, rope). You:", opts([
    ("Go without hesitation — learning about edge activities is thrilling even if I don't try them", {"kink_curiosity": 5}),
    ("Seriously consider it — I love learning even about things outside my comfort zone", {"kink_curiosity": 4}),
    ("Decline but ask them to tell you about it later", {"kink_curiosity": 3}),
    ("Decline — why learn about something I won't do?", {"kink_curiosity": 1})
]))

q(dim, "behavioral_recall", "How many kink-related books, podcasts, or educational resources have you consumed?", opts([
    ("Extensively — I've read multiple books, follow podcasts, attend workshops", {"kink_curiosity": 5}),
    ("Several — I've sought out education in areas that interest me", {"kink_curiosity": 4}),
    ("A few — mostly online articles or one book", {"kink_curiosity": 3}),
    ("None", {"kink_curiosity": 1})
]), cg="curiosity_behavioral")

q(dim, "forced_choice", "Your 'kink bucket list' (things you want to try but haven't yet) is:", opts([
    ("Long and constantly growing — every exploration opens new doors", {"kink_curiosity": 5}),
    ("Has several items — specific things I want to explore", {"kink_curiosity": 4}),
    ("Short — maybe one or two things", {"kink_curiosity": 3}),
    ("Empty — I've tried what I want to try or don't maintain one", {"kink_curiosity": 1})
]))

q(dim, "scenario", "You see a viral tweet dismissing a particular kink as 'weird' or 'sick.' Your reaction:", opts([
    ("Frustration at the closed-mindedness — almost everything consenting adults do has psychological validity", {"kink_curiosity": 5}),
    ("Mild annoyance — different strokes for different folks", {"kink_curiosity": 4}),
    ("Depends on the kink — some things ARE weird", {"kink_curiosity": 2}),
    ("Agreement — some things should stay taboo", {"kink_curiosity": 1})
]), cross=[{"dimension": "shame_vs_acceptance", "notes": "Defensiveness about kink correlates with acceptance"}])

q(dim, "somatic", "When you encounter a new kink concept and imagine yourself trying it, your body:", opts([
    ("Responds with curious arousal — even the imagining activates something", {"kink_curiosity": 5}),
    ("Perks up with interest", {"kink_curiosity": 4}),
    ("Stays neutral until I know more", {"kink_curiosity": 3}),
    ("Tenses or recoils", {"kink_curiosity": 1})
]))

q(dim, "forced_choice", "If you had to choose: a partner who shares ALL your current kinks but refuses to try anything new, vs. a partner who shares FEW current kinks but is endlessly curious and open:", opts([
    ("The curious one — compatibility can be built if the appetite for exploration matches", {"kink_curiosity": 5}),
    ("Probably the curious one — growth together matters", {"kink_curiosity": 4}),
    ("The compatible one — why gamble on potential?", {"kink_curiosity": 2}),
    ("Compatibility now — I know what I want", {"kink_curiosity": 1})
]))

q(dim, "scenario", "A dating profile says 'kinky and always learning.' This makes you feel:", opts([
    ("Immediate interest — that phrase tells me they're my kind of explorer", {"kink_curiosity": 5}),
    ("Positive — openness is attractive", {"kink_curiosity": 4}),
    ("Neutral — I'd need more details", {"kink_curiosity": 3}),
    ("Wary — 'always learning' might mean they don't know what they want yet", {"kink_curiosity": 1})
]))

q(dim, "temporal", "At what age did you first actively seek out information about kink (beyond vanilla sex education)?", opts([
    ("Early teens — I was googling things before I had any experience", {"kink_curiosity": 5}),
    ("Late teens to early twenties", {"kink_curiosity": 4}),
    ("Mid-twenties or later", {"kink_curiosity": 3}),
    ("I've never specifically sought it out", {"kink_curiosity": 1})
]), cg="curiosity_temporal")

q(dim, "behavioral_recall", "Have you ever attended a kink convention, munch, workshop, or community event?", opts([
    ("Multiple times — community engagement is part of how I grow", {"kink_curiosity": 5}),
    ("Once or twice — I enjoyed the exposure", {"kink_curiosity": 4}),
    ("No but I've considered it", {"kink_curiosity": 3}),
    ("No and I wouldn't", {"kink_curiosity": 1})
]), cg="curiosity_behavioral")

q(dim, "forced_choice", "The phrase 'your kink is not my kink but your kink is okay' (YKINMKBYKIOK):", opts([
    ("Is a core value — I genuinely believe all consensual expression deserves respect", {"kink_curiosity": 5}),
    ("Makes sense to me intellectually and emotionally", {"kink_curiosity": 4}),
    ("Is easy to say but hard to live — some kinks test my acceptance", {"kink_curiosity": 3}),
    ("Has limits — some kinks are objectively wrong even with consent", {"kink_curiosity": 1})
]), cross=[{"dimension": "shame_vs_acceptance", "notes": "Strong YKINMK alignment correlates with low shame"}])

# ============================================================
# EXPERIENCE BREADTH (28 questions)
# ============================================================
dim = "experience_breadth"

q(dim, "behavioral_recall", "How many distinct kink categories have you personally experienced (e.g., impact play, bondage, role play, exhibitionism, pet play, electrical, wax, etc.)?", opts([
    ("10+ — I've explored widely across many categories", {"experience_breadth": 5}),
    ("6-9 — a solid range of experiences", {"experience_breadth": 4}),
    ("3-5 — a few areas explored", {"experience_breadth": 3}),
    ("0-2 — very limited or no kink experience", {"experience_breadth": 1})
]), cg="breadth_behavioral")

q(dim, "temporal", "Your kink experience has been built over:", opts([
    ("Many years and many partners — each relationship expanded my range", {"experience_breadth": 5}),
    ("Several years with intentional exploration", {"experience_breadth": 4}),
    ("A few key experiences that opened doors", {"experience_breadth": 3}),
    ("I'm at the beginning of exploration or haven't started", {"experience_breadth": 1})
]), cg="breadth_temporal")

q(dim, "scenario", "At a play party, you see equipment you've never used: a St. Andrew's cross, a spanking bench, a fuck machine, suspension rigging. You:", opts([
    ("Want to try each one — new equipment is new sensation and I'm here for all of it", {"experience_breadth": 5, "kink_curiosity": 4}),
    ("Gravitate toward one or two that intrigue me most", {"experience_breadth": 4}),
    ("Observe others using them before considering", {"experience_breadth": 3}),
    ("Stick to what I know — unfamiliar equipment is intimidating", {"experience_breadth": 1})
]))

q(dim, "forced_choice", "Which better describes your kink journey?", opts([
    ("Wide and varied — I've sampled extensively and can speak knowledgeably about many kinks", {"experience_breadth": 5}),
    ("Moderately broad — I've explored several areas seriously", {"experience_breadth": 4}),
    ("Deep but narrow — I went deep into one or two kinks", {"experience_breadth": 3}),
    ("Mostly vanilla with occasional exploration", {"experience_breadth": 1})
]))

q(dim, "behavioral_recall", "Have you experimented with: role play (age play, pet play, teacher/student), exhibitionism/voyeurism, or group dynamics?", opts([
    ("Two or more of these — and actively enjoy at least one", {"experience_breadth": 5}),
    ("One of these — tried it and have an opinion", {"experience_breadth": 4}),
    ("Thought about it but haven't tried", {"experience_breadth": 3}),
    ("None — these don't interest me", {"experience_breadth": 1})
]), cg="breadth_behavioral")

q(dim, "scenario", "A new partner has a kink you've never encountered — something very specific and unusual (e.g., balloon popping, latex, feet, food play). You:", opts([
    ("Research it thoroughly and try it with genuine enthusiasm — every partner teaches me something new", {"experience_breadth": 5, "kink_curiosity": 5}),
    ("Try it with an open mind — their passion might be contagious", {"experience_breadth": 4}),
    ("Ask questions but probably don't participate", {"experience_breadth": 2}),
    ("Decline — I'm not adding random kinks to my life", {"experience_breadth": 1})
]))

q(dim, "temporal", "How would you describe the trajectory of your kink exploration over the past five years?", opts([
    ("Rapidly expanding — each year I try more new things than the last", {"experience_breadth": 5}),
    ("Steady growth — consistently adding new experiences", {"experience_breadth": 4}),
    ("Plateau — I found what I like and mostly stick to it", {"experience_breadth": 3}),
    ("Contracting — I've narrowed down to fewer activities over time", {"experience_breadth": 1})
]), cg="breadth_temporal")

q(dim, "forced_choice", "Your experience with different types of play (check all that apply conceptually): impact, bondage, sensation, role play, exhibitionism, D/s protocol, edge play, group play. How many have you actually done?", opts([
    ("6-8 — I've tried most of the major categories", {"experience_breadth": 5}),
    ("4-5 — a solid spread", {"experience_breadth": 4}),
    ("2-3 — focused exploration", {"experience_breadth": 3}),
    ("0-1 — very early in my journey", {"experience_breadth": 1})
]))

q(dim, "behavioral_recall", "Have you ever organized or hosted a kink event, scene, or play date that involved multiple participants?", opts([
    ("Yes, multiple times — I enjoy creating spaces for exploration", {"experience_breadth": 5}),
    ("Once or twice — it was a significant experience", {"experience_breadth": 4}),
    ("No, but I've participated in group dynamics", {"experience_breadth": 3}),
    ("No — my kink life is exclusively private and partnered", {"experience_breadth": 1})
]), cg="breadth_behavioral")

q(dim, "scenario", "If you had to write a 'kink resume' listing every type of play you've done, it would be:", opts([
    ("Impressively comprehensive — I've built diverse experience deliberately", {"experience_breadth": 5}),
    ("Respectable — several categories with real depth in some", {"experience_breadth": 4}),
    ("Short but meaningful — quality over quantity", {"experience_breadth": 3}),
    ("Sparse or non-existent", {"experience_breadth": 1})
]))

# ============================================================
# BOUNDARY CLARITY (28 questions)
# ============================================================
dim = "boundary_clarity"

q(dim, "scenario", "Before a scene with a new partner, your negotiation typically:", opts([
    ("Covers hard limits, soft limits, desires, safewords, aftercare needs, and medical considerations — in detail", {"boundary_clarity": 5}),
    ("Covers the major points — limits, safewords, general interests", {"boundary_clarity": 4}),
    ("Is a brief conversation — 'What are you into? Any hard limits?'", {"boundary_clarity": 3}),
    ("Happens organically as we go — formal negotiation kills the mood", {"boundary_clarity": 1})
]))

q(dim, "behavioral_recall", "How quickly and clearly can you articulate your hard limits (things you absolutely will not do)?", opts([
    ("Instantly — I have a clear, well-considered list that I can recite", {"boundary_clarity": 5}),
    ("Fairly quickly — I know my major limits, might need to think about edge cases", {"boundary_clarity": 4}),
    ("With some difficulty — I haven't fully mapped my limits", {"boundary_clarity": 3}),
    ("I'm not sure what my hard limits are — I haven't thought about it much", {"boundary_clarity": 1})
]), cg="boundary_behavioral")

q(dim, "scenario", "Mid-scene, something happens that hits a boundary you didn't know you had. You:", opts([
    ("Immediately communicate — 'Yellow' or 'I need to pause' — and then process what just came up", {"boundary_clarity": 5}),
    ("Signal to slow down and figure out what I'm feeling", {"boundary_clarity": 4}),
    ("Freeze — I'm not sure what to do with unexpected boundary discoveries", {"boundary_clarity": 2}),
    ("Push through — I don't want to ruin the moment", {"boundary_clarity": 1})
]), tier_role="trap", trap=True)

q(dim, "forced_choice", "The difference between a 'hard limit' and a 'soft limit' is:", opts([
    ("Crystal clear to me — hard limits are non-negotiable; soft limits are boundaries I might push under specific conditions with the right partner", {"boundary_clarity": 5}),
    ("Clear enough — hard limits don't change, soft limits are flexible", {"boundary_clarity": 4}),
    ("Somewhat blurry — most of my limits feel situational", {"boundary_clarity": 3}),
    ("I don't categorize limits — everything is negotiable or nothing is", {"boundary_clarity": 1})
]))

q(dim, "temporal", "How has your understanding of your own boundaries evolved over time?", opts([
    ("Dramatically — I've done deep self-work to understand not just what my limits are but WHY", {"boundary_clarity": 5}),
    ("Significantly — experience has taught me where my lines are", {"boundary_clarity": 4}),
    ("Somewhat — I'm still discovering things", {"boundary_clarity": 3}),
    ("Not much — I don't think about boundaries in a structured way", {"boundary_clarity": 1})
]), cg="boundary_temporal")

q(dim, "scenario", "A partner pushes past a stated soft limit without renegotiating first. You:", opts([
    ("Stop everything — violating negotiated boundaries is a consent violation regardless of severity", {"boundary_clarity": 5}),
    ("Use a safeword and address it immediately — this needs discussion", {"boundary_clarity": 4}),
    ("Feel uncomfortable but let it go — they were close to the limit anyway", {"boundary_clarity": 2}),
    ("Don't notice in the moment — I wasn't tracking limits that carefully", {"boundary_clarity": 1})
]), tier_role="trap", trap=True, tags=["nsfw", "kink", "boundary_clarity", "consent"])

q(dim, "behavioral_recall", "Have you ever had a post-scene debrief where you discussed what worked, what didn't, and what you'd change?", opts([
    ("Regularly — debriefs are as important as the scene itself", {"boundary_clarity": 5}),
    ("Sometimes — especially after intense or new experiences", {"boundary_clarity": 4}),
    ("Rarely — it feels awkward to dissect the experience", {"boundary_clarity": 3}),
    ("Never — sex doesn't need a performance review", {"boundary_clarity": 1})
]))

q(dim, "forced_choice", "Your boundaries exist primarily to:", opts([
    ("Create a framework where deeper exploration is POSSIBLE — limits enable freedom", {"boundary_clarity": 5}),
    ("Keep me safe while allowing growth", {"boundary_clarity": 4}),
    ("Prevent bad experiences", {"boundary_clarity": 3}),
    ("I don't think about them proactively", {"boundary_clarity": 1})
]))

q(dim, "scenario", "A potential partner doesn't want to discuss limits before playing — 'Let's just see where things go.' You:", opts([
    ("Hard no — negotiation is non-negotiable, and their resistance is a red flag", {"boundary_clarity": 5}),
    ("Insist on at least a basic conversation — I need safewords established at minimum", {"boundary_clarity": 4}),
    ("Go with it but stay cautious", {"boundary_clarity": 2}),
    ("Agree — spontaneity is part of the thrill", {"boundary_clarity": 1})
]), tier_role="trap", trap=True)

q(dim, "somatic", "When you use a safeword, your body afterwards feels:", opts([
    ("Relief and self-respect — using my safeword IS the system working correctly", {"boundary_clarity": 5}),
    ("A mix of relief and disappointment — glad I spoke up, wish I didn't need to", {"boundary_clarity": 4}),
    ("Guilty — like I failed or ruined the scene", {"boundary_clarity": 2}),
    ("I've never used a safeword / don't have one", {"boundary_clarity": 1})
]))

q(dim, "scenario", "You realize that something you used to enjoy now triggers you differently (trauma, life changes, etc.). You:", opts([
    ("Update my limits immediately, inform current partners, and do the emotional work to understand the shift", {"boundary_clarity": 5}),
    ("Remove it from my 'yes' list and tell my partner", {"boundary_clarity": 4}),
    ("Avoid the situation but don't formally address it", {"boundary_clarity": 2}),
    ("Try to push through — it used to be fine, I should be able to handle it", {"boundary_clarity": 1})
]))

q(dim, "forced_choice", "A kink negotiation checklist (a long list of activities you rate as Yes/No/Maybe):", opts([
    ("Is a tool I use enthusiastically — it surfaces things I might not have thought to discuss", {"boundary_clarity": 5}),
    ("Is useful — I've filled one out before", {"boundary_clarity": 4}),
    ("Is overkill — a conversation covers it", {"boundary_clarity": 3}),
    ("Is a buzzkill — it turns sex into a contract", {"boundary_clarity": 1})
]))

q(dim, "behavioral_recall", "Can you articulate WHY each of your hard limits is a hard limit (not just what they are, but the reason)?", opts([
    ("Yes — I've done the introspection to understand the root of each boundary", {"boundary_clarity": 5}),
    ("Mostly — some are gut feelings I haven't fully analyzed", {"boundary_clarity": 4}),
    ("A few — some limits are just 'no' without a clear reason", {"boundary_clarity": 3}),
    ("I haven't thought about reasons — they just are what they are", {"boundary_clarity": 1})
]), cg="boundary_behavioral")

q(dim, "temporal", "How often do your limits change?", opts([
    ("They evolve deliberately — as I grow, some soft limits become yes's, and occasionally new limits emerge, all through conscious process", {"boundary_clarity": 5}),
    ("Occasionally — new experiences shift my comfort zone", {"boundary_clarity": 4}),
    ("Rarely — I set them and they stay", {"boundary_clarity": 3}),
    ("I don't track them closely enough to know", {"boundary_clarity": 1})
]), cg="boundary_temporal")

# ============================================================
# COMMUNICATION ABOUT KINK (28 questions)
# ============================================================
dim = "communication_about_kink"

q(dim, "scenario", "Telling a new partner about a kink that feels vulnerable — something society might judge. You:", opts([
    ("Share directly with confidence — vulnerability about desires is strength, and their reaction tells me everything I need to know", {"communication_about_kink": 5}),
    ("Share, though my heart pounds — I've learned that the right person responds well", {"communication_about_kink": 4}),
    ("Hint around it and see how they react before being direct", {"communication_about_kink": 3}),
    ("Keep it to myself — some things are too risky to share", {"communication_about_kink": 1})
]))

q(dim, "behavioral_recall", "In your current or most recent relationship, how openly do you discuss sexual desires, fantasies, and kinks?", opts([
    ("Completely — no fantasy is off limits for discussion, even if it's off limits for action", {"communication_about_kink": 5}),
    ("Very openly — we talk about most things", {"communication_about_kink": 4}),
    ("Somewhat — the basics are covered but deep fantasies stay private", {"communication_about_kink": 3}),
    ("Minimally — sex is something we do, not something we talk about in detail", {"communication_about_kink": 1})
]), cg="comm_behavioral")

q(dim, "forced_choice", "After sex or a scene, you're more likely to:", opts([
    ("Debrief thoroughly — what was hot, what landed, what to do differently, how we both feel", {"communication_about_kink": 5}),
    ("Share highlights — 'that thing you did was incredible'", {"communication_about_kink": 4}),
    ("Cuddle and bask without much talking", {"communication_about_kink": 3}),
    ("Roll over and move on — the experience speaks for itself", {"communication_about_kink": 1})
]))

q(dim, "scenario", "Your partner does something during sex that you don't enjoy. How do you handle it?", opts([
    ("Address it directly but kindly — 'I noticed you did X; it doesn't work for me because Y. I'd love Z instead.'", {"communication_about_kink": 5}),
    ("Mention it later — redirect in the moment, explain after", {"communication_about_kink": 4}),
    ("Redirect physically without discussing it", {"communication_about_kink": 2}),
    ("Say nothing — I don't want to make them feel bad", {"communication_about_kink": 1})
]))

q(dim, "temporal", "How comfortable have you become talking about sex and kink over your lifetime?", opts([
    ("Very — I've worked hard to become articulate about desire, and I can discuss almost anything without shame", {"communication_about_kink": 5}),
    ("Significantly more comfortable than when I started", {"communication_about_kink": 4}),
    ("Somewhat more comfortable — still working on it", {"communication_about_kink": 3}),
    ("Still very uncomfortable — sex is easier to do than to discuss", {"communication_about_kink": 1})
]), cg="comm_temporal")

q(dim, "scenario", "You want to introduce a new kink into an established relationship. Your approach:", opts([
    ("Bring it up directly: 'I've been thinking about trying X. Here's what appeals to me about it. What do you think?'", {"communication_about_kink": 5}),
    ("Send an article or video and say 'This is interesting — would you be open to discussing it?'", {"communication_about_kink": 4}),
    ("Drop hints and hope they pick up on the interest", {"communication_about_kink": 2}),
    ("Keep it as a private fantasy — too risky to bring up", {"communication_about_kink": 1})
]))

q(dim, "forced_choice", "In terms of sexual vocabulary, you:", opts([
    ("Have precise, comfortable language for anatomy, acts, dynamics, and feelings — I can discuss anything clinical or dirty", {"communication_about_kink": 5}),
    ("Can discuss most things comfortably, though some topics still feel awkward", {"communication_about_kink": 4}),
    ("Use euphemisms for the more explicit stuff", {"communication_about_kink": 3}),
    ("Struggle with explicit language — it feels crass or exposing", {"communication_about_kink": 1})
]))

q(dim, "behavioral_recall", "Have you ever had a 'meta-conversation' about your sexual communication itself — discussing how you discuss sex?", opts([
    ("Yes — communication about communication is how you level up", {"communication_about_kink": 5}),
    ("Once or twice — usually when something went wrong", {"communication_about_kink": 4}),
    ("No — that feels recursive and unnecessary", {"communication_about_kink": 2}),
    ("No — we barely discuss sex, let alone how we discuss it", {"communication_about_kink": 1})
]), cg="comm_behavioral")

q(dim, "scenario", "You're writing a dating profile. How explicit are you about your kink interests?", opts([
    ("Very — I name what I'm looking for because vague profiles attract vague matches", {"communication_about_kink": 5}),
    ("Clearly kinky with some specifics — enough to signal without a full inventory", {"communication_about_kink": 4}),
    ("Coded — 'open-minded' or 'adventurous'", {"communication_about_kink": 3}),
    ("No mention — kink is private and doesn't belong in a profile", {"communication_about_kink": 1})
]))

q(dim, "somatic", "When you're about to say something sexually vulnerable out loud for the first time, your body:", opts([
    ("Feels the adrenaline but I've trained myself to speak through it — vulnerability is a skill I've practiced", {"communication_about_kink": 5}),
    ("Nervous but I do it — the payoff of being known outweighs the risk", {"communication_about_kink": 4}),
    ("Tightens up significantly — I might chicken out", {"communication_about_kink": 2}),
    ("Shuts down — I cannot get these words out of my mouth", {"communication_about_kink": 1})
]))

q(dim, "forced_choice", "If a partner reacted badly to a kink disclosure (judgment, disgust, mockery), you would:", opts([
    ("Recognize it as crucial compatibility information — their reaction tells me this isn't my person, and that's okay", {"communication_about_kink": 5}),
    ("Feel hurt but ultimately glad I found out — better to know", {"communication_about_kink": 4}),
    ("Be devastated and probably never share that kink again", {"communication_about_kink": 2}),
    ("This fear is exactly why I don't share", {"communication_about_kink": 1})
]))

q(dim, "scenario", "During a scene, you need to communicate a shift — more of something, less of something, a new direction. You:", opts([
    ("Use clear, direct language even in headspace — 'Harder,' 'Not there,' 'I need a moment'", {"communication_about_kink": 5}),
    ("Use the color system — 'yellow' to slow, 'green' for more", {"communication_about_kink": 4}),
    ("Try to communicate non-verbally — body language, sounds", {"communication_about_kink": 3}),
    ("Don't communicate — I let my partner lead and take what comes", {"communication_about_kink": 1})
]))

q(dim, "temporal", "How many partners have you been able to talk to honestly about your deepest sexual desires?", opts([
    ("Most or all of my partners — I don't enter relationships where I can't be fully honest", {"communication_about_kink": 5}),
    ("Several — I've gotten better at choosing receptive partners", {"communication_about_kink": 4}),
    ("One or two — it's rare to find someone safe enough", {"communication_about_kink": 3}),
    ("None — there are fantasies no one knows about", {"communication_about_kink": 1})
]), cg="comm_temporal")

q(dim, "behavioral_recall", "Have you ever used a structured negotiation tool (want/will/won't list, BDSM checklist, written agreement)?", opts([
    ("Yes, regularly — structure supports thorough communication", {"communication_about_kink": 5}),
    ("Yes, at least once — it was helpful", {"communication_about_kink": 4}),
    ("No — verbal conversation covers it", {"communication_about_kink": 3}),
    ("No — structured negotiation is overkill for my needs", {"communication_about_kink": 1})
]), cg="comm_behavioral")

# ============================================================
# SHAME VS ACCEPTANCE (28 questions)
# ============================================================
dim = "shame_vs_acceptance"

q(dim, "scenario", "After an intense kink session that involved something taboo (humiliation, consensual non-consent, an unusual fetish), you feel:", opts([
    ("Satisfied and self-accepting — I did something I wanted with someone I trust, and that's healthy", {"shame_vs_acceptance": 5}),
    ("Good overall with maybe a brief wave of 'was that too much?' that passes quickly", {"shame_vs_acceptance": 4}),
    ("Mixed — pleasure followed by guilt or second-guessing", {"shame_vs_acceptance": 2}),
    ("Ashamed — I wish I didn't want these things", {"shame_vs_acceptance": 1})
]))

q(dim, "somatic", "When you think about your kinkiest desire — the one that feels most taboo — your body:", opts([
    ("Responds with arousal and no shame — I've fully integrated this desire as part of me", {"shame_vs_acceptance": 5}),
    ("Responds with arousal and only mild discomfort — mostly accepted", {"shame_vs_acceptance": 4}),
    ("Responds with arousal AND shame — they're tangled together", {"shame_vs_acceptance": 2}),
    ("Tenses with shame more than arousal", {"shame_vs_acceptance": 1})
]), cg="shame_somatic")

q(dim, "forced_choice", "The statement 'There's nothing wrong with what I want sexually' — you:", opts([
    ("Believe it completely and live accordingly", {"shame_vs_acceptance": 5}),
    ("Believe it intellectually, still working on feeling it fully", {"shame_vs_acceptance": 4}),
    ("Want to believe it but struggle — societal messages are strong", {"shame_vs_acceptance": 2}),
    ("Don't believe it — some desires are wrong even if they're consensual", {"shame_vs_acceptance": 1})
]))

q(dim, "temporal", "How has your relationship with sexual shame changed over your life?", opts([
    ("I've done deep work to dismantle it — shame was installed by others and I've consciously removed it", {"shame_vs_acceptance": 5}),
    ("Significantly less shame than I used to carry", {"shame_vs_acceptance": 4}),
    ("Some progress but shame still surfaces regularly", {"shame_vs_acceptance": 2}),
    ("Shame has been a constant — it hasn't meaningfully changed", {"shame_vs_acceptance": 1})
]), cg="shame_temporal")

q(dim, "scenario", "A therapist asks about your sex life. You:", opts([
    ("Share openly, including kink — a therapist who can't handle adult sexuality isn't useful to me", {"shame_vs_acceptance": 5}),
    ("Share the basics, mention kink if it's relevant", {"shame_vs_acceptance": 4}),
    ("Keep it vague — I don't trust their judgment about alternative sexuality", {"shame_vs_acceptance": 2}),
    ("Don't bring it up — they'd pathologize me", {"shame_vs_acceptance": 1})
]))

q(dim, "forced_choice", "If your friends knew the full truth about your sex life, you believe they would:", opts([
    ("Maybe be surprised but ultimately respect my choices — and if they didn't, they're not my people", {"shame_vs_acceptance": 5}),
    ("Be accepting overall, with maybe some raised eyebrows", {"shame_vs_acceptance": 4}),
    ("Be uncomfortable — I keep these worlds separate for a reason", {"shame_vs_acceptance": 2}),
    ("Judge me harshly — this must stay secret", {"shame_vs_acceptance": 1})
]))

q(dim, "behavioral_recall", "Have you ever turned down a sexual experience you wanted because of shame or fear of judgment (not because of practical concerns)?", opts([
    ("Not in years — I've learned to pursue what I want without shame dictating my choices", {"shame_vs_acceptance": 5}),
    ("Rarely now — it happened more when I was younger", {"shame_vs_acceptance": 4}),
    ("Sometimes — shame still wins occasionally", {"shame_vs_acceptance": 2}),
    ("Often — shame is a major barrier in my sexual life", {"shame_vs_acceptance": 1})
]), cg="shame_behavioral")

q(dim, "scenario", "You orgasm from something that surprises even you — a particular word, a type of pain, a dynamic you didn't think turned you on. You:", opts([
    ("File it with curiosity — 'Oh, that's a thing for me. Good to know.' No judgment.", {"shame_vs_acceptance": 5}),
    ("Feel intrigued, maybe a little surprised, but accepting", {"shame_vs_acceptance": 4}),
    ("Feel confused and a bit unsettled — where did THAT come from?", {"shame_vs_acceptance": 2}),
    ("Feel disturbed — I don't want to want that", {"shame_vs_acceptance": 1})
]))

q(dim, "somatic", "The 'shame hangover' — that wave of guilt or self-disgust that can hit after orgasm, especially after taboo play. Your experience:", opts([
    ("Non-existent or extremely rare — I've worked through the shame cycle and it no longer visits", {"shame_vs_acceptance": 5}),
    ("Occasional and brief — it passes quickly because I know it's societal programming, not truth", {"shame_vs_acceptance": 4}),
    ("Regular — especially after more extreme play", {"shame_vs_acceptance": 2}),
    ("Intense and persistent — post-orgasm shame is a real problem for me", {"shame_vs_acceptance": 1})
]), cg="shame_somatic")

q(dim, "forced_choice", "Which resonates most?", opts([
    ("My sexuality — including the kinky parts — is a source of joy, connection, and self-knowledge", {"shame_vs_acceptance": 5}),
    ("My kinks are part of who I am and I'm mostly at peace with them", {"shame_vs_acceptance": 4}),
    ("I accept my kinks intellectually but emotionally there's still friction", {"shame_vs_acceptance": 2}),
    ("I wish I could be 'normal' sexually", {"shame_vs_acceptance": 1})
]), tier_role="consistency_check", cg="shame_core")

q(dim, "scenario", "A close friend confides a kink that you personally find unappealing. You:", opts([
    ("Listen without judgment and affirm their courage in sharing — their kink isn't mine but it's valid", {"shame_vs_acceptance": 5}),
    ("Feel brief surprise, then supportive", {"shame_vs_acceptance": 4}),
    ("Struggle to hide my reaction but try to be supportive", {"shame_vs_acceptance": 3}),
    ("Judge them, even if I try not to show it", {"shame_vs_acceptance": 1})
]))

q(dim, "temporal", "How many people in your non-sexual life know about your kink interests?", opts([
    ("Multiple close friends — I don't compartmentalize unless I have to", {"shame_vs_acceptance": 5}),
    ("A select few — people I trust deeply", {"shame_vs_acceptance": 4}),
    ("One or two — it's rare and carefully chosen", {"shame_vs_acceptance": 3}),
    ("No one — my vanilla life and kink life are completely separate", {"shame_vs_acceptance": 1})
]), cg="shame_temporal")

q(dim, "behavioral_recall", "Have you ever intentionally sought out resources (therapy, books, communities) specifically to work on sexual shame?", opts([
    ("Yes — deconstructing shame has been an active project in my life", {"shame_vs_acceptance": 5}),
    ("Some — I've read about it and worked on it", {"shame_vs_acceptance": 4}),
    ("I'm aware of it but haven't actively addressed it", {"shame_vs_acceptance": 3}),
    ("No — I don't frame it as 'shame work'", {"shame_vs_acceptance": 1})
]), cg="shame_behavioral")

q(dim, "scenario", "You're watching porn that matches your kink. Someone walks in. Your reaction:", opts([
    ("Calmly close the laptop — mild embarrassment but no shame spiral", {"shame_vs_acceptance": 5}),
    ("Flustered but recover quickly — it's just porn", {"shame_vs_acceptance": 4}),
    ("Panic and feel exposed — they saw what I watch", {"shame_vs_acceptance": 2}),
    ("Devastated — this is my worst nightmare", {"shame_vs_acceptance": 1})
]))

# ============================================================
# SAFETY CONSCIOUSNESS (28 questions)
# ============================================================
dim = "safety_consciousness"

q(dim, "scenario", "Before trying a new kink activity, you:", opts([
    ("Research extensively — risks, safety protocols, first-aid measures, community best practices", {"safety_consciousness": 5}),
    ("Do basic research — what could go wrong and how to mitigate it", {"safety_consciousness": 4}),
    ("Ask experienced friends for tips", {"safety_consciousness": 3}),
    ("Jump in and figure it out — overthinking ruins the experience", {"safety_consciousness": 1})
]))

q(dim, "behavioral_recall", "How many first-aid or safety skills do you have that are relevant to kink (CPR, wound care, rope safety, understanding circulation)?", opts([
    ("Multiple — I've taken classes specifically because I take play safety seriously", {"safety_consciousness": 5}),
    ("Some — I know the basics of safe practices for what I do", {"safety_consciousness": 4}),
    ("Minimal — general first aid", {"safety_consciousness": 3}),
    ("None beyond common sense", {"safety_consciousness": 1})
]), cg="safety_behavioral")

q(dim, "forced_choice", "RACK (Risk-Aware Consensual Kink) vs. SSC (Safe, Sane, Consensual) — your position:", opts([
    ("RACK — because nothing is fully 'safe,' acknowledging risk allows for informed choice. I prefer the intellectual honesty", {"safety_consciousness": 5}),
    ("SSC — a good baseline that keeps most people safe", {"safety_consciousness": 4}),
    ("I know these acronyms but don't think about frameworks formally", {"safety_consciousness": 3}),
    ("I don't know what these mean", {"safety_consciousness": 1})
]))

q(dim, "scenario", "You're at a play party and see someone doing breath play (choking) in a way that looks dangerous. You:", opts([
    ("Intervene or alert a dungeon monitor — safety violations affect the whole community", {"safety_consciousness": 5}),
    ("Express concern to someone nearby — I'm worried but don't want to overstep", {"safety_consciousness": 4}),
    ("Mind my own business — they're adults", {"safety_consciousness": 2}),
    ("I wouldn't notice — I don't know what 'dangerous' looks like in this context", {"safety_consciousness": 1})
]))

q(dim, "temporal", "How has your approach to safety in kink evolved?", opts([
    ("Dramatically — I was less careful early on and have developed rigorous practices through education and experience", {"safety_consciousness": 5}),
    ("Grown — I take safety more seriously as I've learned more", {"safety_consciousness": 4}),
    ("About the same — I've always been reasonably careful", {"safety_consciousness": 3}),
    ("Not much — safety isn't something I actively think about", {"safety_consciousness": 1})
]), cg="safety_temporal")

q(dim, "forced_choice", "Safety shears (EMT shears for cutting rope in emergencies) during any bondage scene:", opts([
    ("Non-negotiable — they're within arm's reach every single time, no exceptions", {"safety_consciousness": 5}),
    ("Usually present — I make sure they're nearby", {"safety_consciousness": 4}),
    ("I've used them but don't always have them ready", {"safety_consciousness": 3}),
    ("I've never owned a pair / don't use them", {"safety_consciousness": 1})
]))

q(dim, "scenario", "A new partner wants to try breath play (choking, suffocation). You:", opts([
    ("Discuss it seriously — acknowledge it's inherently high-risk, review anatomy, agree on signals, decide together if the risk is acceptable", {"safety_consciousness": 5}),
    ("Proceed with caution — light restriction only, constant monitoring", {"safety_consciousness": 4}),
    ("Go for it — choking during sex is common enough", {"safety_consciousness": 2}),
    ("Say yes without much discussion — they asked, so they've done it before", {"safety_consciousness": 1})
]), tier_role="trap", trap=True, tags=["nsfw", "kink", "safety_consciousness", "risk"])

q(dim, "behavioral_recall", "Do you have a 'scene bag' or safety kit that includes things like safety shears, first-aid supplies, water, blankets, and aftercare items?", opts([
    ("Yes — comprehensive and maintained", {"safety_consciousness": 5}),
    ("Yes — basic supplies", {"safety_consciousness": 4}),
    ("Not a formal kit but I think about having supplies nearby", {"safety_consciousness": 3}),
    ("No", {"safety_consciousness": 1})
]), cg="safety_behavioral")

q(dim, "scenario", "Someone you're attracted to at a play party approaches and wants to scene right now — no prior negotiation, no getting to know each other first. You:", opts([
    ("Decline the immediate scene — I need at least a conversation about limits, health, and signals first", {"safety_consciousness": 5}),
    ("Slow them down — 'Let's talk for a bit first'", {"safety_consciousness": 4}),
    ("Agree to something light — we can negotiate as we go", {"safety_consciousness": 2}),
    ("Go for it — spontaneity is exciting", {"safety_consciousness": 1})
]))

q(dim, "forced_choice", "STI testing and sexual health in the context of kink:", opts([
    ("I maintain regular testing, know my status, discuss it before new partners, and consider it part of ethical play", {"safety_consciousness": 5}),
    ("I test regularly and disclose", {"safety_consciousness": 4}),
    ("I test occasionally", {"safety_consciousness": 3}),
    ("I don't test regularly", {"safety_consciousness": 1})
]))

q(dim, "scenario", "During a scene, you notice numbness or discoloration in a restrained limb. You:", opts([
    ("Stop immediately and address it — circulation issues can cause nerve damage and this is a medical concern, not a mood concern", {"safety_consciousness": 5}),
    ("Alert my partner right away — this needs immediate attention", {"safety_consciousness": 4}),
    ("Mention it but continue if it's mild", {"safety_consciousness": 2}),
    ("I wouldn't know what to look for", {"safety_consciousness": 1})
]))

q(dim, "behavioral_recall", "Have you ever had a scene go wrong (injury, panic, emotional distress)? If so, how did you handle the aftermath?", opts([
    ("Yes — and I did a thorough debrief, identified what went wrong, and changed protocols to prevent recurrence", {"safety_consciousness": 5}),
    ("Yes — we discussed it and adjusted", {"safety_consciousness": 4}),
    ("Yes — it shook me but I didn't formally change anything", {"safety_consciousness": 2}),
    ("No / I wouldn't know how to handle it", {"safety_consciousness": 1})
]), cg="safety_behavioral")

q(dim, "forced_choice", "Consent verification during a scene — checking in when your partner can't easily safeword (gagged, in deep subspace):", opts([
    ("I use non-verbal systems (held objects, hand squeezes, check-in protocols) and monitor constantly", {"safety_consciousness": 5}),
    ("I check in regularly with yes/no questions", {"safety_consciousness": 4}),
    ("I rely on reading body language", {"safety_consciousness": 3}),
    ("If they agreed to the scene beforehand, that covers it", {"safety_consciousness": 1})
]))

q(dim, "temporal", "How many safety workshops, classes, or educational sessions about safe kink practices have you attended?", opts([
    ("Multiple — safety education is ongoing for me", {"safety_consciousness": 5}),
    ("A few — I've sought out education when available", {"safety_consciousness": 4}),
    ("One or none — I learn from experience and online resources", {"safety_consciousness": 3}),
    ("None — I don't seek out safety-specific education", {"safety_consciousness": 1})
]), cg="safety_temporal")

# ============================================================
# PARTNER EXPLORATION STYLE (32 questions)
# ============================================================
dim = "partner_exploration_style"

q(dim, "scenario", "You and a partner are discussing trying something new. Your approach:", opts([
    ("Collaborative deep-dive: research together, discuss what excites and concerns each of us, design the experience jointly", {"partner_exploration_style": 5}),
    ("I take the lead in planning and present it: 'Here's what I've learned, here's how we could try it'", {"partner_exploration_style": 4}),
    ("Let them lead — I'm more of a 'follower into new territory' type", {"partner_exploration_style": 3}),
    ("One of us suggests, the other agrees or disagrees, and we just do it or don't", {"partner_exploration_style": 1})
]))

q(dim, "forced_choice", "When introducing a partner to a kink they've never tried, you:", opts([
    ("Create a gentle on-ramp: education first, demo or description, clear consent check, easy first experience, thorough debrief", {"partner_exploration_style": 5}),
    ("Describe what I want to do, check their reaction, start gently", {"partner_exploration_style": 4}),
    ("Suggest it and see if they're game", {"partner_exploration_style": 3}),
    ("Just introduce it during play and gauge their response", {"partner_exploration_style": 1})
]))

q(dim, "behavioral_recall", "How do you typically discover new kinks in the context of a relationship?", opts([
    ("Through ongoing dialogue — we regularly check in about desires, fantasies, and things we want to try", {"partner_exploration_style": 5}),
    ("Through sharing porn, erotica, or articles that spark interest", {"partner_exploration_style": 4}),
    ("Accidentally — something happens during sex and we discover we both like it", {"partner_exploration_style": 3}),
    ("We don't actively discover new things — we do what we know", {"partner_exploration_style": 1})
]), cg="partner_behavioral")

q(dim, "scenario", "A partner tries something you suggested and doesn't enjoy it. You:", opts([
    ("Thank them for trying, process their experience, adjust expectations, and find what DOES work — the exploration itself was valuable", {"partner_exploration_style": 5}),
    ("Accept it gracefully — not everything works for everyone", {"partner_exploration_style": 4}),
    ("Feel disappointed but move on", {"partner_exploration_style": 3}),
    ("Feel rejected — they didn't even try to like it", {"partner_exploration_style": 1})
]))

q(dim, "forced_choice", "The ideal pace for introducing new kinks into a relationship:", opts([
    ("Steady and intentional — something new every few weeks, with debrief time between", {"partner_exploration_style": 5}),
    ("As the mood strikes — when something appeals, we try it", {"partner_exploration_style": 4}),
    ("Slowly — one new thing every few months", {"partner_exploration_style": 3}),
    ("If it ain't broke, don't fix it — why add complexity?", {"partner_exploration_style": 1})
]))

q(dim, "scenario", "You've discovered a kink your long-term partner has zero interest in. You:", opts([
    ("Accept it, find other outlets if appropriate (solo play, fantasy, community engagement), and don't pressure them", {"partner_exploration_style": 5}),
    ("Respect their limit while keeping the conversation open — people change", {"partner_exploration_style": 4}),
    ("Keep bringing it up hoping they'll come around", {"partner_exploration_style": 2}),
    ("Resent them for not being willing to try", {"partner_exploration_style": 1})
]), tier_role="trap", trap=True, tags=["nsfw", "kink", "partner_exploration_style", "consent"])

q(dim, "temporal", "How much time do you invest in understanding a PARTNER'S kinks (vs. just your own)?", opts([
    ("Equal to my own — understanding their desires, reading about their kinks, learning to provide what they need", {"partner_exploration_style": 5}),
    ("Significant — I want to be a good play partner for their interests too", {"partner_exploration_style": 4}),
    ("Some — I'll try what they want but don't study it", {"partner_exploration_style": 3}),
    ("Minimal — they can explore their kinks, I'll explore mine", {"partner_exploration_style": 1})
]), cg="partner_temporal")

q(dim, "behavioral_recall", "In past relationships, have you successfully introduced a partner to a kink they now love that they had never considered before?", opts([
    ("Multiple times — I take pride in being a good guide into new experiences", {"partner_exploration_style": 5}),
    ("At least once — it was rewarding", {"partner_exploration_style": 4}),
    ("I don't think so", {"partner_exploration_style": 2}),
    ("I've never tried to introduce a partner to something new", {"partner_exploration_style": 1})
]), cg="partner_behavioral")

q(dim, "forced_choice", "After trying something new, the most important thing is:", opts([
    ("Thorough processing — what worked, what didn't, how we each felt, what we'd change", {"partner_exploration_style": 5}),
    ("A quick check-in — did you like it? Want to do it again?", {"partner_exploration_style": 4}),
    ("Whether it was hot or not — the body knows", {"partner_exploration_style": 3}),
    ("Moving on — analysis ruins spontaneity", {"partner_exploration_style": 1})
]))

q(dim, "scenario", "Your partner's kink interests are very different from yours — their top kinks are your 'meh' and vice versa. You:", opts([
    ("See this as an opportunity — learning to enjoy something for your partner's sake, and teaching them yours, is intimate and growth-producing", {"partner_exploration_style": 5}),
    ("Work to find overlap and compromise on the rest", {"partner_exploration_style": 4}),
    ("Focus on the areas where you do overlap", {"partner_exploration_style": 3}),
    ("Consider it a fundamental incompatibility", {"partner_exploration_style": 1})
]))

q(dim, "temporal", "In your longest relationship, how did your shared kink life evolve over time?", opts([
    ("Continuously — we never stopped exploring, adding, refining. The kink grew as the trust grew", {"partner_exploration_style": 5}),
    ("Expanded for a while, then settled into favorites", {"partner_exploration_style": 4}),
    ("Started strong and gradually decreased", {"partner_exploration_style": 2}),
    ("Stayed mostly the same throughout", {"partner_exploration_style": 1})
]), cg="partner_temporal")

q(dim, "forced_choice", "A partner who has never explored kink but is curious and willing vs. a partner who is highly experienced but set in their ways. You prefer:", opts([
    ("The curious beginner — building something together from scratch is deeply intimate", {"partner_exploration_style": 5}),
    ("Slight lean toward the beginner — enthusiasm and openness matter more than skill", {"partner_exploration_style": 4}),
    ("The experienced one — I want a partner who knows what they're doing", {"partner_exploration_style": 3}),
    ("Either — compatibility is more about chemistry than experience level", {"partner_exploration_style": 2})
]))

# Now cross-cutting questions mixing multiple dimensions

q("kink_curiosity", "scenario", "FetLife, Reddit kink communities, Feeld, or other kink-focused platforms. Your engagement:", opts([
    ("Active — I post, discuss, learn, and connect. These communities are vital to my growth", {"kink_curiosity": 5, "communication_about_kink": 4}),
    ("I read and lurk regularly", {"kink_curiosity": 4}),
    ("Occasional browsing", {"kink_curiosity": 3}),
    ("No presence — I don't engage with kink communities online", {"kink_curiosity": 1})
]))

q("experience_breadth", "forced_choice", "Pet play (puppy, kitten, pony, etc.) — your experience and reaction:", opts([
    ("Experienced and enjoy it — the psychology of pet space is rich and unique", {"experience_breadth": 5}),
    ("Tried it or deeply curious — the role play aspect intrigues me", {"experience_breadth": 4}),
    ("Not my thing but I don't judge", {"experience_breadth": 3}),
    ("Confusing — I don't understand the appeal", {"experience_breadth": 1})
]))

q("boundary_clarity", "scenario", "A partner wants to try consensual non-consent (CNC). Your negotiation for this specific activity:", opts([
    ("Would be the most thorough of any scene — specific triggers, multiple check-in systems, detailed aftercare plan, days of discussion beforehand", {"boundary_clarity": 5, "safety_consciousness": 5}),
    ("Would require extensive conversation and very clear boundaries", {"boundary_clarity": 4}),
    ("Would make me uncomfortable to even negotiate — the topic is too loaded", {"boundary_clarity": 2}),
    ("Wouldn't need special negotiation — rough play is rough play", {"boundary_clarity": 1})
]))

q("communication_about_kink", "scenario", "You and your partner keep a shared 'desire list' — a running document where either of you can add fantasies, kinks you want to try, or things you've seen and found hot. This:", opts([
    ("Is exactly how I'd want to manage ongoing exploration — living documentation of desire", {"communication_about_kink": 5, "partner_exploration_style": 5}),
    ("Is a great idea — I'd participate enthusiastically", {"communication_about_kink": 4}),
    ("Is interesting but might feel like homework", {"communication_about_kink": 3}),
    ("Is over-engineering sex", {"communication_about_kink": 1})
]))

q("shame_vs_acceptance", "scenario", "You discover that a kink you enjoy has problematic cultural associations (e.g., race play, age play, CNC). You:", opts([
    ("Sit with the complexity — I can enjoy something in a consensual context while being aware of its broader implications. The two coexist", {"shame_vs_acceptance": 5}),
    ("Feel conflicted but continue — context matters and my play space is my own", {"shame_vs_acceptance": 4}),
    ("Stop engaging — the associations are too troubling", {"shame_vs_acceptance": 2}),
    ("Feel deep shame that I ever enjoyed it", {"shame_vs_acceptance": 1})
]))

q("safety_consciousness", "scenario", "You're topping someone for the first time and they have a medical condition (asthma, heart condition, diabetes). You:", opts([
    ("Get full medical details, research contraindications for planned activities, have emergency protocols in place, possibly consult with kink-aware medical professionals", {"safety_consciousness": 5}),
    ("Ask thorough questions and adjust the scene plan accordingly", {"safety_consciousness": 4}),
    ("Note it and keep things lighter than usual", {"safety_consciousness": 3}),
    ("They know their body — they'll speak up if something's wrong", {"safety_consciousness": 1})
]))

q("partner_exploration_style", "scenario", "Your partner comes home excited about a workshop they attended on a kink you've never heard of. You:", opts([
    ("Match their energy — sit down, listen to everything, ask questions, and start brainstorming how to incorporate it", {"partner_exploration_style": 5, "kink_curiosity": 4}),
    ("Listen with interest and openness", {"partner_exploration_style": 4}),
    ("Listen politely but don't feel the same excitement", {"partner_exploration_style": 2}),
    ("Feel threatened — why are they learning about new kinks without me?", {"partner_exploration_style": 1})
]))

q("kink_curiosity", "forced_choice", "Your reaction to the concept of 'kink as therapy' — using BDSM dynamics to process trauma, build trust, or explore emotional patterns:", opts([
    ("Deeply resonant — I've experienced the therapeutic power of kink firsthand", {"kink_curiosity": 5}),
    ("Interesting and plausible — I can see how structured power exchange could be healing", {"kink_curiosity": 4}),
    ("Skeptical but open — seems like it could be rationalization", {"kink_curiosity": 3}),
    ("Pseudoscientific — kink is play, not therapy", {"kink_curiosity": 1})
]))

q("experience_breadth", "behavioral_recall", "Exhibitionism or voyeurism (play parties, watching others, being watched, public play, cam play). Your experience:", opts([
    ("Extensive and enthusiastic — the social dimension of kink adds layers", {"experience_breadth": 5}),
    ("Some experience — I've been to events or played semi-publicly", {"experience_breadth": 4}),
    ("Curious but haven't acted on it", {"experience_breadth": 3}),
    ("No interest — kink is private", {"experience_breadth": 1})
]))

q("boundary_clarity", "forced_choice", "The difference between a boundary and a preference:", opts([
    ("Clear and important — boundaries are non-negotiable lines; preferences are flexible. Treating preferences as boundaries OR boundaries as preferences causes problems", {"boundary_clarity": 5}),
    ("I understand the distinction and try to be clear about which is which", {"boundary_clarity": 4}),
    ("Somewhat blurry — most things feel like preferences until they don't", {"boundary_clarity": 3}),
    ("I don't make this distinction", {"boundary_clarity": 1})
]))

q("communication_about_kink", "forced_choice", "Talking dirty — explicit verbal communication during sex:", opts([
    ("A skill I've developed and enjoy — I can narrate, command, beg, or describe what's happening with full comfort", {"communication_about_kink": 5}),
    ("I enjoy it and am decent at it", {"communication_about_kink": 4}),
    ("I can do it but feel self-conscious", {"communication_about_kink": 3}),
    ("I prefer silence or minimal talking during sex", {"communication_about_kink": 1})
]))

q("shame_vs_acceptance", "behavioral_recall", "Have you ever deleted kink-related content (browser history, messages, photos, accounts) out of shame rather than practical privacy?", opts([
    ("Not in a long time — I maintain privacy by choice, not by shame", {"shame_vs_acceptance": 5}),
    ("Rarely now — I used to but have grown past it", {"shame_vs_acceptance": 4}),
    ("Sometimes — the shame still drives some secrecy", {"shame_vs_acceptance": 2}),
    ("Regularly — I purge anything that could expose my kink interests", {"shame_vs_acceptance": 1})
]), cg="shame_behavioral")

q("safety_consciousness", "forced_choice", "Intoxication and kink:", opts([
    ("Don't mix — altered states compromise consent, judgment, and pain perception. I play sober", {"safety_consciousness": 5}),
    ("Light social drinking is fine but I don't play intoxicated", {"safety_consciousness": 4}),
    ("A drink or two helps me relax into play", {"safety_consciousness": 2}),
    ("Substances often enhance my kink experiences", {"safety_consciousness": 1})
]))

q("partner_exploration_style", "temporal", "When starting a new relationship with kink potential, how do you map your shared kink landscape?", opts([
    ("Systematically — questionnaires, long conversations, shared checklists, graduated experiences with debriefs", {"partner_exploration_style": 5}),
    ("Extended conversations over multiple dates before playing", {"partner_exploration_style": 4}),
    ("One big talk and then learning by doing", {"partner_exploration_style": 3}),
    ("Organically — we figure it out as we go", {"partner_exploration_style": 1})
]), cg="partner_temporal")

q("kink_curiosity", "scenario", "You learn about a kink subculture that has its own community, language, events, and aesthetics (e.g., leather, rubber/latex, puppy play community). Your reaction:", opts([
    ("Fascinated — I want to understand the culture, the history, the psychology. Subcultures reveal human depth", {"kink_curiosity": 5}),
    ("Interested — I'd attend an event or read about it", {"kink_curiosity": 4}),
    ("Mildly curious but wouldn't seek it out", {"kink_curiosity": 3}),
    ("Indifferent — not my world", {"kink_curiosity": 1})
]))

q("experience_breadth", "scenario", "A partner suggests a week-long 'kink intensive' — every day trying a different type of play you've never done. You:", opts([
    ("Am ecstatic — a deliberate deep-dive into new experiences is my idea of a perfect vacation", {"experience_breadth": 5, "kink_curiosity": 5}),
    ("Very interested — though I'd want some recovery time between sessions", {"experience_breadth": 4}),
    ("Interested in maybe 2-3 days of that", {"experience_breadth": 3}),
    ("Overwhelmed — that sounds exhausting, not fun", {"experience_breadth": 1})
]))

q("boundary_clarity", "scenario", "You're playing with a new partner and they do something not discussed — nothing harmful, but not negotiated. You:", opts([
    ("Pause and address it — undiscussed activities, even harmless ones, are a negotiation violation that needs discussion", {"boundary_clarity": 5}),
    ("Note it mentally and bring it up after the scene", {"boundary_clarity": 4}),
    ("Let it go if it felt fine in the moment", {"boundary_clarity": 2}),
    ("Don't notice — I wasn't tracking what was negotiated that closely", {"boundary_clarity": 1})
]))

q("communication_about_kink", "scenario", "You and a partner have very different communication styles about sex — one of you processes verbally, the other through physical connection. You:", opts([
    ("Name the difference explicitly and build a system that honors both — 'I know you need to talk about it and I need to feel it. Let's do both'", {"communication_about_kink": 5}),
    ("Try to meet in the middle — some talking, some non-verbal processing", {"communication_about_kink": 4}),
    ("Default to whichever style is more comfortable for me", {"communication_about_kink": 2}),
    ("Don't address the mismatch directly", {"communication_about_kink": 1})
]))

q("shame_vs_acceptance", "forced_choice", "If you could take a pill that would make you vanilla — remove all kink desires and make you sexually 'normal' — would you?", opts([
    ("Absolutely not — my kinks are part of what makes me ME, and I wouldn't erase any of it", {"shame_vs_acceptance": 5}),
    ("No — even the complicated kinks have taught me something", {"shame_vs_acceptance": 4}),
    ("I'd be tempted — life would be simpler", {"shame_vs_acceptance": 2}),
    ("In a heartbeat — I'd love to just be normal", {"shame_vs_acceptance": 1})
]), tier_role="consistency_check", cg="shame_core")

q("safety_consciousness", "scenario", "You're negotiating with someone who says 'I don't have any limits.' Your response:", opts([
    ("Red flag — everyone has limits. Either they haven't done the self-work to identify them, or they're telling me what they think I want to hear. Either way, I need to slow down and dig deeper", {"safety_consciousness": 5}),
    ("Concerned — I'd probe further before playing with them", {"safety_consciousness": 4}),
    ("Take it at face value — some people are just very open", {"safety_consciousness": 2}),
    ("Exciting — carte blanche", {"safety_consciousness": 1})
]), tier_role="trap", trap=True)

q("partner_exploration_style", "forced_choice", "In a kink relationship, who typically drives the exploration of new activities?", opts([
    ("We both do equally — kink exploration is a shared project we're both invested in", {"partner_exploration_style": 5}),
    ("Mostly me — I'm the more curious one and I bring things to the table", {"partner_exploration_style": 4}),
    ("Mostly my partner — they're more adventurous and I follow their lead", {"partner_exploration_style": 3}),
    ("Neither — we do what we do without much new exploration", {"partner_exploration_style": 1})
]), cg="partner_behavioral")

print(f"Total questions: {len(questions)}")
with open("/Users/user/personal/sb/trueassess/priv/question_bank/kink_exploration.json", "w") as f:
    json.dump(questions, f, indent=2)
print("Written kink_exploration.json")
