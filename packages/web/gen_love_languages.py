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
        "tags": tags or ["love_languages", dim]
    }

def opts(choices):
    return [{"id": chr(97+i), "text": t, "scores": s} for i, (t, s) in enumerate(choices)]

# 100 questions: 20 per dimension
# words_of_affirmation, acts_of_service, receiving_gifts, quality_time, physical_touch
# BEHAVIORAL preferences, not self-reported

# ============================================================
# WORDS_OF_AFFIRMATION (20)
# ============================================================

questions.append(q("words_of_affirmation", "scenario",
    "Your partner did something thoughtful for you. Which response from them would make YOU feel most loved?",
    opts([
        ("A handwritten note explaining why they love you", {"words_of_affirmation": 5}),
        ("Taking over your chores so you can rest", {"acts_of_service": 5}),
        ("Sitting next to you in comfortable silence, fully present", {"quality_time": 5}),
        ("A long, warm embrace", {"physical_touch": 5})
    ]),
    tier="core", cg="woa_receive_1", opacity=0.6))

questions.append(q("words_of_affirmation", "behavioral_recall",
    "Think about the last time you felt genuinely loved. What happened?",
    opts([
        ("Someone told me exactly what I mean to them — with specific, heartfelt words", {"words_of_affirmation": 5}),
        ("Someone went out of their way to make my life easier", {"acts_of_service": 5}),
        ("Someone gave me something that showed they really know me", {"receiving_gifts": 5}),
        ("Someone gave me their undivided attention for hours", {"quality_time": 5})
    ]),
    tier="core", cg="woa_receive_1", opacity=0.65))

questions.append(q("words_of_affirmation", "partner_perspective",
    "You had a terrible day. Which partner response heals you fastest?",
    opts([
        ("'I'm so proud of how you handle hard things. You're stronger than you know.'", {"words_of_affirmation": 5}),
        ("Without a word, they draw you a bath and handle dinner", {"acts_of_service": 5}),
        ("They put their phone away, turn to you, and say 'tell me everything'", {"quality_time": 5}),
        ("They wrap their arms around you and hold you", {"physical_touch": 5})
    ]),
    tier="core", cg="woa_receive_1", opacity=0.65))

questions.append(q("words_of_affirmation", "scenario",
    "When you want to show someone you care, your instinct is to:",
    opts([
        ("Tell them — in detail — what you appreciate about them", {"words_of_affirmation": 5}),
        ("Do something practical to make their life better", {"acts_of_service": 5}),
        ("Find or make them the perfect gift", {"receiving_gifts": 5}),
        ("Reach out physically — hug, touch their arm, sit close", {"physical_touch": 5})
    ]),
    tier="core", cg="woa_express_1", opacity=0.6))

questions.append(q("words_of_affirmation", "somatic",
    "When someone you love says something specifically affirming about who you ARE (not what you did), your body:",
    opts([
        ("Fills with warmth — those words go straight to your core", {"words_of_affirmation": 5}),
        ("Feels nice but you'd rather they showed it through actions", {"acts_of_service": 3}),
        ("Feels slightly awkward — you're not great at receiving verbal praise", {"words_of_affirmation": 1}),
        ("Appreciates it but the words don't land as deeply as touch or quality time would", {"words_of_affirmation": 2})
    ]),
    tier="core", cg="woa_receive_1", opacity=0.7))

questions.append(q("words_of_affirmation", "behavioral_recall",
    "How often do you verbally express appreciation, love, or admiration to the people closest to you?",
    opts([
        ("Daily or near-daily — I'm verbally expressive with my feelings", {"words_of_affirmation": 5}),
        ("Regularly but not constantly", {"words_of_affirmation": 4}),
        ("Occasionally — I show love more through actions than words", {"words_of_affirmation": 2}),
        ("Rarely — they know how I feel without me saying it", {"words_of_affirmation": 1})
    ]),
    tier="triangulation", cg="woa_express_1", opacity=0.55))

questions.append(q("words_of_affirmation", "forced_choice",
    "Which would mean more from your partner?",
    opts([
        ("A love letter you could reread anytime", {"words_of_affirmation": 5}),
        ("Them noticing you were stressed and silently handling something on your to-do list", {"acts_of_service": 5})
    ]),
    tier="core", cg="woa_receive_1", opacity=0.7))

questions.append(q("words_of_affirmation", "scenario",
    "You cooked an elaborate dinner. Which partner response pleases you most?",
    opts([
        ("'This is incredible. You put so much thought into this. I feel so taken care of.'", {"words_of_affirmation": 5}),
        ("They insist on doing all the dishes and cleanup", {"acts_of_service": 5}),
        ("They put their phone away and make the evening entirely about being together", {"quality_time": 5}),
        ("They come up behind you, hold you, and say nothing — just closeness", {"physical_touch": 5})
    ]),
    tier="triangulation", cg="woa_receive_1", opacity=0.6))

questions.append(q("words_of_affirmation", "temporal",
    "Think about the compliment you remember most clearly from your entire life. It was:",
    opts([
        ("Someone putting into words exactly what they valued about you — it changed how you saw yourself", {"words_of_affirmation": 5}),
        ("Someone showing up for you when it mattered most — actions, not words", {"acts_of_service": 5}),
        ("A gift that showed someone truly understood you", {"receiving_gifts": 5}),
        ("A moment of physical connection that said everything without words", {"physical_touch": 5})
    ]),
    tier="triangulation", cg="woa_receive_1", opacity=0.7))

questions.append(q("words_of_affirmation", "trap",
    "Your partner is great in every way but rarely says 'I love you' or gives verbal affirmation. How much does this bother you?",
    opts([
        ("A lot — I NEED to hear it. Actions alone aren't enough.", {"words_of_affirmation": 5}),
        ("Some — I'd prefer more verbal affirmation but their actions show love", {"words_of_affirmation": 3}),
        ("Not much — I know they love me from how they treat me", {"words_of_affirmation": 1}),
        ("Not at all — words are cheap; behavior is what counts", {"words_of_affirmation": 1})
    ]),
    tier="trap", trap=True, cg="woa_receive_1", opacity=0.65))

questions.append(q("words_of_affirmation", "partner_perspective",
    "When you're proud of someone, you most naturally:",
    opts([
        ("Tell them specifically what impressed you and why", {"words_of_affirmation": 5}),
        ("Do something to celebrate them or make their day easier", {"acts_of_service": 4}),
        ("Get them something to mark the occasion", {"receiving_gifts": 4}),
        ("Give them the biggest hug or high five possible", {"physical_touch": 4})
    ]),
    tier="core", cg="woa_express_1", opacity=0.55))

questions.append(q("words_of_affirmation", "somatic",
    "When someone sends you a long, heartfelt text about what your friendship means to them, your body:",
    opts([
        ("Glows — you reread it twice and save it", {"words_of_affirmation": 5}),
        ("Feels touched but you'd rather hear it in person over shared time", {"quality_time": 3}),
        ("Appreciates it but feels slightly uncomfortable with the emotional directness", {"words_of_affirmation": 2}),
        ("Responds by wanting to hug them, not text back", {"physical_touch": 3})
    ]),
    tier="triangulation", cg="woa_receive_1", opacity=0.65))

questions.append(q("words_of_affirmation", "behavioral_recall",
    "In a relationship, how important is it that your partner verbally acknowledge what you do?",
    opts([
        ("Essential — if they don't say it, I start feeling invisible", {"words_of_affirmation": 5}),
        ("Important — a 'thank you' or 'I noticed' goes a long way", {"words_of_affirmation": 4}),
        ("Nice but not necessary — I don't need verbal feedback to feel valued", {"words_of_affirmation": 2}),
        ("Irrelevant — I do things because I want to, not for acknowledgment", {"words_of_affirmation": 1})
    ]),
    tier="consistency_check", cg="woa_receive_1", opacity=0.65))

questions.append(q("words_of_affirmation", "forced_choice",
    "Which absence hurts more in a relationship?",
    opts([
        ("A partner who never tells you what they appreciate about you", {"words_of_affirmation": 5}),
        ("A partner who never makes time for just the two of you", {"quality_time": 5})
    ]),
    tier="core", cg="woa_receive_1", opacity=0.75))

questions.append(q("words_of_affirmation", "scenario",
    "You're feeling insecure about yourself. What would help most?",
    opts([
        ("Your partner sitting you down and telling you specifically why you're amazing", {"words_of_affirmation": 5}),
        ("Your partner doing something that shows they rely on you", {"acts_of_service": 4}),
        ("Your partner spending the whole day focused only on you", {"quality_time": 4}),
        ("Your partner holding you close — no talking, just warmth", {"physical_touch": 5})
    ]),
    tier="triangulation", cg="woa_receive_1", opacity=0.65))

questions.append(q("words_of_affirmation", "behavioral_recall",
    "In past relationships, what did you most wish your partner did MORE of?",
    opts([
        ("Told me what they loved about me — specific, verbal appreciation", {"words_of_affirmation": 5}),
        ("Helped out without being asked — noticed what needed doing", {"acts_of_service": 5}),
        ("Surprised me with thoughtful gifts or tokens", {"receiving_gifts": 5}),
        ("Initiated physical affection — casual touches, hand-holding, closeness", {"physical_touch": 5})
    ]),
    tier="core", cg="woa_receive_1", opacity=0.7))

questions.append(q("words_of_affirmation", "partner_perspective",
    "When encouraging a friend who's struggling, you naturally:",
    opts([
        ("Use words — specific, encouraging, affirming language about who they are", {"words_of_affirmation": 5}),
        ("Take action — do something concrete to help", {"acts_of_service": 5}),
        ("Show up — dedicate time to be with them", {"quality_time": 5}),
        ("Be physically present — hug them, sit close, offer comfort through touch", {"physical_touch": 5})
    ]),
    tier="triangulation", cg="woa_express_1", opacity=0.6))

questions.append(q("words_of_affirmation", "scenario",
    "Your anniversary is coming. The gesture that would mean most from your partner is:",
    opts([
        ("A heartfelt letter recounting specific moments and why they love you", {"words_of_affirmation": 5}),
        ("Planning and executing the entire celebration so you don't lift a finger", {"acts_of_service": 5}),
        ("A carefully chosen, meaningful gift", {"receiving_gifts": 5}),
        ("An entire day of undivided togetherness — no phones, no plans", {"quality_time": 5})
    ]),
    tier="core", cg="woa_receive_1", opacity=0.6))

questions.append(q("words_of_affirmation", "trap",
    "Someone you're dating says 'I'm not great with words but I'll always show you through actions.' You think:",
    opts([
        ("That's fine — actions matter more anyway", {"words_of_affirmation": 1}),
        ("I appreciate that, but I'll probably still need some verbal affirmation", {"words_of_affirmation": 3}),
        ("That's going to be a problem — I need to hear it to feel it", {"words_of_affirmation": 5}),
        ("Let's see — if the actions are consistent, maybe words aren't essential", {"words_of_affirmation": 2})
    ]),
    tier="trap", trap=True, cg="woa_receive_1", opacity=0.65))

questions.append(q("words_of_affirmation", "behavioral_recall",
    "How naturally do you write heartfelt messages (birthday cards, thank-you notes, appreciation texts)?",
    opts([
        ("Very naturally — I love finding the right words", {"words_of_affirmation": 5}),
        ("Fairly naturally but I don't do it as often as I'd like", {"words_of_affirmation": 3}),
        ("With effort — I know it matters but words don't come easily", {"words_of_affirmation": 2}),
        ("Almost never — it feels forced", {"words_of_affirmation": 1})
    ]),
    tier="consistency_check", cg="woa_express_1", opacity=0.55))

# ============================================================
# ACTS_OF_SERVICE (20)
# ============================================================

questions.append(q("acts_of_service", "scenario",
    "You come home exhausted. Your partner has cleaned the house, done laundry, and made dinner — without asking. You feel:",
    opts([
        ("Deeply loved — this IS love in action", {"acts_of_service": 5}),
        ("Grateful but you'd rather they sat and listened about your day", {"quality_time": 4}),
        ("Touched, but a warm hug would have been enough", {"physical_touch": 3}),
        ("Appreciative — but verbal affirmation of your hard day would hit deeper", {"words_of_affirmation": 3})
    ]),
    tier="core", cg="aos_receive_1", opacity=0.6))

questions.append(q("acts_of_service", "behavioral_recall",
    "When a friend is going through a hard time, your instinct is to:",
    opts([
        ("Drop off food, help with errands, do something practical", {"acts_of_service": 5}),
        ("Send a long heartfelt message of support", {"words_of_affirmation": 5}),
        ("Spend time with them — just being there", {"quality_time": 5}),
        ("Hug them, hold their hand, physical comfort", {"physical_touch": 5})
    ]),
    tier="core", cg="aos_express_1", opacity=0.6))

questions.append(q("acts_of_service", "partner_perspective",
    "Which feels like the biggest betrayal of love?",
    opts([
        ("A partner who sees you struggling and doesn't lift a finger", {"acts_of_service": 5}),
        ("A partner who never puts their phone down when you're talking", {"quality_time": 5}),
        ("A partner who never says anything kind or affirming", {"words_of_affirmation": 5}),
        ("A partner who never initiates physical affection", {"physical_touch": 5})
    ]),
    tier="core", cg="aos_receive_1", opacity=0.7))

questions.append(q("acts_of_service", "scenario",
    "Your partner is sick. You show love by:",
    opts([
        ("Making soup, getting medicine, handling everything so they can rest", {"acts_of_service": 5}),
        ("Sitting by their bed, keeping them company", {"quality_time": 4}),
        ("Telling them they'll get through this and you're here for them", {"words_of_affirmation": 4}),
        ("Lying next to them, rubbing their back, physical comfort", {"physical_touch": 5})
    ]),
    tier="core", cg="aos_express_1", opacity=0.55))

questions.append(q("acts_of_service", "somatic",
    "When someone does something practical to make your life easier without being asked, your body:",
    opts([
        ("Floods with love — they SAW what you needed and acted", {"acts_of_service": 5}),
        ("Feels grateful — nice gesture", {"acts_of_service": 3}),
        ("Feels slightly uncomfortable — you don't like people doing things for you", {"acts_of_service": 1}),
        ("Barely registers — you'd rather have had their time or words", {"acts_of_service": 1})
    ]),
    tier="core", cg="aos_receive_1", opacity=0.7))

questions.append(q("acts_of_service", "forced_choice",
    "Which says 'I love you' more?",
    opts([
        ("Your partner handles something stressful on your behalf", {"acts_of_service": 5}),
        ("Your partner brings you a surprise gift showing they were thinking of you", {"receiving_gifts": 5})
    ]),
    tier="core", cg="aos_receive_1", opacity=0.7))

questions.append(q("acts_of_service", "behavioral_recall",
    "Think about how you typically show love. The top behavior is:",
    opts([
        ("Doing things — fixing, running errands, handling logistics", {"acts_of_service": 5}),
        ("Saying what I feel — compliments, affirmations, 'I love you'", {"words_of_affirmation": 5}),
        ("Being present — canceling plans to be with them, undivided attention", {"quality_time": 5}),
        ("Physical closeness — touching, holding, sitting close", {"physical_touch": 5})
    ]),
    tier="core", cg="aos_express_1", opacity=0.6))

questions.append(q("acts_of_service", "scenario",
    "You're overwhelmed with work. Your partner's most helpful response:",
    opts([
        ("They take over household responsibilities without being asked", {"acts_of_service": 5}),
        ("They sit next to you while you work — just companionship", {"quality_time": 4}),
        ("They leave an encouraging note on your desk", {"words_of_affirmation": 4}),
        ("They rub your shoulders and pull you into an embrace", {"physical_touch": 4})
    ]),
    tier="triangulation", cg="aos_receive_1", opacity=0.6))

questions.append(q("acts_of_service", "temporal",
    "Think about a time someone did something incredibly helpful without being asked. How did it rank among loving gestures?",
    opts([
        ("Top tier — unprompted service is THE way I feel loved", {"acts_of_service": 5}),
        ("High — but other gestures have been equally impactful", {"acts_of_service": 3}),
        ("Moderate — I appreciated it but it didn't feel like LOVE specifically", {"acts_of_service": 2}),
        ("Lower than you'd think — grateful but not necessarily loved", {"acts_of_service": 1})
    ]),
    tier="triangulation", cg="aos_receive_1", opacity=0.7))

questions.append(q("acts_of_service", "partner_perspective",
    "Your love language is most obvious when your partner ISN'T doing it. Which absence makes you feel unloved?",
    opts([
        ("When they never help — even when they can see you're drowning", {"acts_of_service": 5}),
        ("When they never say anything affirming", {"words_of_affirmation": 5}),
        ("When they never make time for just the two of you", {"quality_time": 5}),
        ("When they never touch you", {"physical_touch": 5})
    ]),
    tier="consistency_check", cg="aos_receive_1", opacity=0.7))

questions.append(q("acts_of_service", "trap",
    "Your partner says 'I love you' all the time but never helps around the house when you're overwhelmed. You feel:",
    opts([
        ("Frustrated — words without action feel empty", {"acts_of_service": 5}),
        ("Loved — they say it, and that's what matters", {"words_of_affirmation": 4}),
        ("Mixed — both matter but I wish they'd show up more", {"acts_of_service": 3}),
        ("Fine — I don't expect help, I handle things myself", {"acts_of_service": 1})
    ]),
    tier="trap", trap=True, cg="aos_receive_1", opacity=0.6))

questions.append(q("acts_of_service", "forced_choice",
    "You can only have one: a partner who constantly tells you they love you, or one who quietly handles things that stress you out?",
    opts([
        ("The one who handles things — actions speak louder", {"acts_of_service": 5}),
        ("The one who tells me — I need the words", {"words_of_affirmation": 5})
    ]),
    tier="core", cg="aos_receive_1", opacity=0.8))

questions.append(q("acts_of_service", "behavioral_recall",
    "When you love someone, how often do you find yourself doing tasks on their behalf?",
    opts([
        ("Constantly — it's my primary way of showing love", {"acts_of_service": 5}),
        ("Often — I enjoy making their life easier", {"acts_of_service": 4}),
        ("Sometimes — when I notice a need", {"acts_of_service": 2}),
        ("Rarely — I show love in other ways", {"acts_of_service": 1})
    ]),
    tier="consistency_check", cg="aos_express_1", opacity=0.6))

questions.append(q("acts_of_service", "scenario",
    "Your birthday. The gesture that hits deepest:",
    opts([
        ("Your partner planned everything — every detail handled, you just show up", {"acts_of_service": 5}),
        ("A birthday card with a message that makes you cry", {"words_of_affirmation": 5}),
        ("A gift they clearly spent months thinking about", {"receiving_gifts": 5}),
        ("They cleared the whole day — just the two of you, phone off", {"quality_time": 5})
    ]),
    tier="core", cg="aos_receive_1", opacity=0.6))

questions.append(q("acts_of_service", "partner_perspective",
    "When your partner is stressed, your automatic response is to:",
    opts([
        ("Take things off their plate — reduce their burden", {"acts_of_service": 5}),
        ("Tell them they're doing amazing and you believe in them", {"words_of_affirmation": 4}),
        ("Clear your schedule to be available", {"quality_time": 4}),
        ("Physical comfort — hold them, create physical ease", {"physical_touch": 4})
    ]),
    tier="triangulation", cg="aos_express_1", opacity=0.6))

questions.append(q("acts_of_service", "somatic",
    "When you ask your partner for help and they enthusiastically jump in, your body:",
    opts([
        ("Relaxes completely — this is partnership. THIS is love.", {"acts_of_service": 5}),
        ("Feels relief — practical help is nice", {"acts_of_service": 3}),
        ("Feels slightly guilty for asking", {"acts_of_service": 2}),
        ("Doesn't change much — help is fine but not what fills your love tank", {"acts_of_service": 1})
    ]),
    tier="triangulation", cg="aos_receive_1", opacity=0.65))

questions.append(q("acts_of_service", "temporal",
    "Looking back at your relationship history, what's the pattern in how YOU express love?",
    opts([
        ("I do things — fix, build, organize, handle. My love is in my labor.", {"acts_of_service": 5}),
        ("I say things — compliments, affirmations, 'I love you' constantly", {"words_of_affirmation": 5}),
        ("I give things — gifts, surprises, tokens", {"receiving_gifts": 5}),
        ("I'm there — I make time and give full attention", {"quality_time": 5})
    ]),
    tier="consistency_check", cg="aos_express_1", opacity=0.65))

questions.append(q("acts_of_service", "scenario",
    "Partner A leaves you sweet voice notes throughout the day. Partner B brings your car for service without telling you. You'd feel more loved by:",
    opts([
        ("Partner B — they saw a need and handled it. That's love.", {"acts_of_service": 5}),
        ("Partner A — those voice notes would make my whole day", {"words_of_affirmation": 5}),
        ("Hard to choose — both are meaningful", {"acts_of_service": 3, "words_of_affirmation": 3})
    ]),
    tier="triangulation", cg="aos_receive_1", opacity=0.65))

questions.append(q("acts_of_service", "forced_choice",
    "Which is a bigger deal-breaker?",
    opts([
        ("A partner who's verbally loving but never cooks, cleans, or helps", {"acts_of_service": 5}),
        ("A partner who handles everything but never says they love you", {"words_of_affirmation": 5})
    ]),
    tier="consistency_check", cg="aos_receive_1", opacity=0.8))

questions.append(q("acts_of_service", "behavioral_recall",
    "When you think 'they really love me,' it's usually because:",
    opts([
        ("They did something that made my life easier — often without being asked", {"acts_of_service": 5}),
        ("They said something that told me exactly where I stand", {"words_of_affirmation": 5}),
        ("They gave up their time to be with me", {"quality_time": 5}),
        ("They reached for me — initiated touch, closeness", {"physical_touch": 5})
    ]),
    tier="core", cg="aos_receive_1", opacity=0.7))

# ============================================================
# RECEIVING_GIFTS (20)
# ============================================================

questions.append(q("receiving_gifts", "scenario",
    "Your partner comes home with a small unexpected gift — nothing expensive, just something showing they thought of you. You feel:",
    opts([
        ("Deeply touched — the fact that they thought of you and acted on it is everything", {"receiving_gifts": 5}),
        ("Nice — but you'd rather they came home early to spend time", {"quality_time": 3}),
        ("Appreciate it but physical affection says 'I was thinking about you' louder", {"physical_touch": 3}),
        ("Grateful — but if they'd said something sweet, that would mean more", {"words_of_affirmation": 3})
    ]),
    tier="core", cg="rg_receive_1", opacity=0.6))

questions.append(q("receiving_gifts", "behavioral_recall",
    "When you see something that reminds you of someone you love, how often do you buy it?",
    opts([
        ("Almost always — gift-giving is instinctive for me", {"receiving_gifts": 5}),
        ("Often — I enjoy finding the perfect thing", {"receiving_gifts": 4}),
        ("Occasionally — if it's really perfect", {"receiving_gifts": 2}),
        ("Rarely — I show love in other ways", {"receiving_gifts": 1})
    ]),
    tier="core", cg="rg_express_1", opacity=0.55))

questions.append(q("receiving_gifts", "partner_perspective",
    "Your partner forgets a gift for your birthday — just says 'happy birthday.' How bothered are you?",
    opts([
        ("Very — a gift shows thought and effort, its absence feels like indifference", {"receiving_gifts": 5}),
        ("Somewhat — it's not the gift itself, it's what the EFFORT represents", {"receiving_gifts": 4}),
        ("A little — but if they spent the day with me, I'm fine", {"quality_time": 3}),
        ("Not at all — I don't need gifts to feel loved", {"receiving_gifts": 1})
    ]),
    tier="core", cg="rg_receive_1", opacity=0.65))

questions.append(q("receiving_gifts", "forced_choice",
    "Which would move you more from your partner?",
    opts([
        ("A thoughtfully chosen gift that shows they truly understand you", {"receiving_gifts": 5}),
        ("Clearing your entire schedule to spend an uninterrupted day together", {"quality_time": 5})
    ]),
    tier="core", cg="rg_receive_1", opacity=0.7))

questions.append(q("receiving_gifts", "somatic",
    "You open a gift and it's EXACTLY what you wanted but never said aloud. Your body:",
    opts([
        ("Overwhelmed with emotion — they SAW you and this proves it", {"receiving_gifts": 5}),
        ("Happy and surprised", {"receiving_gifts": 3}),
        ("Pleased but same feeling could come from time or words", {"receiving_gifts": 2}),
        ("Appreciative but gifts aren't what move you emotionally", {"receiving_gifts": 1})
    ]),
    tier="core", cg="rg_receive_1", opacity=0.7))

questions.append(q("receiving_gifts", "scenario",
    "It's your partner's birthday. You've been planning their gift for months. This effort feels:",
    opts([
        ("Like the most natural expression of love — THIS is how you show it", {"receiving_gifts": 5}),
        ("Fun but not your primary way of expressing love", {"receiving_gifts": 3}),
        ("Like a lot of effort — you'd rather spend energy on quality time", {"quality_time": 3}),
        ("Slightly stressful — gifts aren't your love language", {"receiving_gifts": 1})
    ]),
    tier="triangulation", cg="rg_express_1", opacity=0.6))

questions.append(q("receiving_gifts", "temporal",
    "Think about the most meaningful gift you've ever received. What made it special?",
    opts([
        ("It showed the giver truly understood me — the gift itself WAS the message", {"receiving_gifts": 5}),
        ("It came when I needed to feel remembered", {"receiving_gifts": 4}),
        ("The gesture mattered but the time together that day mattered more", {"quality_time": 4}),
        ("I can't think of a gift that had that level of emotional impact", {"receiving_gifts": 1})
    ]),
    tier="triangulation", cg="rg_receive_1", opacity=0.65))

questions.append(q("receiving_gifts", "behavioral_recall",
    "How much effort do you put into choosing gifts for others?",
    opts([
        ("Enormous — I start months in advance and the gift must be PERFECT", {"receiving_gifts": 5}),
        ("Significant — real thought goes in", {"receiving_gifts": 4}),
        ("Moderate — I try but I'm not a natural gift-giver", {"receiving_gifts": 2}),
        ("Minimal — gift cards or asking what they want", {"receiving_gifts": 1})
    ]),
    tier="consistency_check", cg="rg_express_1", opacity=0.55))

questions.append(q("receiving_gifts", "partner_perspective",
    "Your partner gives you a generic gift card for your anniversary. You feel:",
    opts([
        ("Hurt — a gift card says 'I didn't try'", {"receiving_gifts": 5}),
        ("Mildly disappointed but it's the thought that counts", {"receiving_gifts": 3}),
        ("Fine — I'd rather get something I'll actually use", {"receiving_gifts": 1}),
        ("Indifferent — the card they write inside matters more", {"words_of_affirmation": 3})
    ]),
    tier="triangulation", cg="rg_receive_1", opacity=0.55))

questions.append(q("receiving_gifts", "trap",
    "Some people say gifts are 'materialistic.' Your take:",
    opts([
        ("They don't understand — it's not about money, it's about THOUGHT made tangible", {"receiving_gifts": 5}),
        ("I get why people think that, but a well-chosen gift is deeply personal", {"receiving_gifts": 4}),
        ("Partially agree — gifts can be meaningful but aren't essential", {"receiving_gifts": 2}),
        ("Agree — I'd rather have time, words, or touch than objects", {"receiving_gifts": 1})
    ]),
    tier="trap", trap=True, cg="rg_receive_1", opacity=0.6))

questions.append(q("receiving_gifts", "forced_choice",
    "Which Valentine's Day gesture means more?",
    opts([
        ("A carefully chosen piece of jewelry or item you'd been eyeing", {"receiving_gifts": 5}),
        ("A night where they cook, clean, handle everything, and you relax", {"acts_of_service": 5})
    ]),
    tier="triangulation", cg="rg_receive_1", opacity=0.65))

questions.append(q("receiving_gifts", "somatic",
    "When a holiday comes and there's NO gift from your partner (not forgotten — they just 'don't do gifts'), your body:",
    opts([
        ("Aches — the absence of a gift feels like absence of care", {"receiving_gifts": 5}),
        ("Feels a pang but you can rationalize it", {"receiving_gifts": 3}),
        ("Doesn't react — gifts aren't your measure of love", {"receiving_gifts": 1}),
        ("Relief — you'd rather skip the gift exchange entirely", {"receiving_gifts": 1})
    ]),
    tier="consistency_check", cg="rg_receive_1", opacity=0.7))

questions.append(q("receiving_gifts", "scenario",
    "You see the perfect item for your best friend — it's them in object form. Slightly expensive. You:",
    opts([
        ("Buy it without hesitation — they'll LOVE it", {"receiving_gifts": 5}),
        ("Buy it if it's within budget", {"receiving_gifts": 3}),
        ("Take a photo and tell them about it", {"words_of_affirmation": 2}),
        ("Move on — you'll find another way to show you care", {"receiving_gifts": 1})
    ]),
    tier="core", cg="rg_express_1", opacity=0.55))

questions.append(q("receiving_gifts", "behavioral_recall",
    "How many gifts from loved ones do you still have from years ago?",
    opts([
        ("Many — I treasure them. Each one is a physical token of love.", {"receiving_gifts": 5}),
        ("Some — the most meaningful ones", {"receiving_gifts": 3}),
        ("A few — I'm not very sentimental about objects", {"receiving_gifts": 2}),
        ("Almost none — I'm practical about possessions", {"receiving_gifts": 1})
    ]),
    tier="triangulation", cg="rg_receive_1", opacity=0.55))

questions.append(q("receiving_gifts", "partner_perspective",
    "For 'just because' moments — random Tuesday, no occasion — you most appreciate when your partner:",
    opts([
        ("Brings you something — flowers, your favorite snack, a book", {"receiving_gifts": 5}),
        ("Writes you a sweet note or texts something heartfelt", {"words_of_affirmation": 5}),
        ("Cancels plans to spend the evening with you", {"quality_time": 5}),
        ("Reaches for your hand, pulls you close", {"physical_touch": 5})
    ]),
    tier="core", cg="rg_receive_1", opacity=0.55))

questions.append(q("receiving_gifts", "scenario",
    "You're browsing a store and imagine your partner's reaction to a specific item. This happens:",
    opts([
        ("All the time — I constantly see the world through 'would they love this?' eyes", {"receiving_gifts": 5}),
        ("Fairly often — I notice things that remind me of them", {"receiving_gifts": 3}),
        ("Occasionally — in specific stores or contexts", {"receiving_gifts": 2}),
        ("Rarely — I don't naturally think in gift terms", {"receiving_gifts": 1})
    ]),
    tier="consistency_check", cg="rg_express_1", opacity=0.55))

questions.append(q("receiving_gifts", "forced_choice",
    "A tangible symbol of love (ring, necklace, a gift you can hold) is:",
    opts([
        ("Essential — you need something physical that represents the love", {"receiving_gifts": 5}),
        ("Nice but not necessary — love lives in actions and words", {"receiving_gifts": 1})
    ]),
    tier="core", cg="rg_receive_1", opacity=0.75))

questions.append(q("receiving_gifts", "temporal",
    "How do you feel about 'experience gifts' (concert tickets, trips) vs. physical objects?",
    opts([
        ("I love experiences but a physical gift I can keep and look at daily means more", {"receiving_gifts": 5}),
        ("Experiences are better — the memory matters more than the thing", {"quality_time": 4, "receiving_gifts": 2}),
        ("Either is great — the thought behind it counts", {"receiving_gifts": 3}),
        ("Neither moves me — I'd rather have time, words, or touch", {"receiving_gifts": 1})
    ]),
    tier="triangulation", cg="rg_receive_1", opacity=0.55))

questions.append(q("receiving_gifts", "somatic",
    "When you unwrap a gift from someone you love, the anticipation feels:",
    opts([
        ("Electric — one of your favorite feelings in the world", {"receiving_gifts": 5}),
        ("Pleasant and exciting", {"receiving_gifts": 3}),
        ("Slightly anxious — you never know how to react", {"receiving_gifts": 2}),
        ("Not special — it's just an object", {"receiving_gifts": 1})
    ]),
    tier="triangulation", cg="rg_receive_1", opacity=0.55))

questions.append(q("receiving_gifts", "behavioral_recall",
    "When you receive a gift that clearly had no thought behind it, how much does it bother you?",
    opts([
        ("Deeply — a thoughtless gift feels worse than no gift at all", {"receiving_gifts": 5}),
        ("A fair amount — the lack of effort is disappointing", {"receiving_gifts": 4}),
        ("A little — I appreciate any gesture", {"receiving_gifts": 2}),
        ("Not at all — the fact they gave me anything is fine", {"receiving_gifts": 1})
    ]),
    tier="consistency_check", cg="rg_receive_1", opacity=0.6))

# ============================================================
# QUALITY_TIME (20)
# ============================================================

questions.append(q("quality_time", "scenario",
    "Your partner is physically present but constantly on their phone during dinner. You:",
    opts([
        ("Are deeply bothered — their distraction feels like rejection", {"quality_time": 5}),
        ("Are mildly annoyed but let it go", {"quality_time": 3}),
        ("Don't notice much — you're probably on your phone too", {"quality_time": 1}),
        ("Wish they'd put the phone down but it doesn't feel like a love issue", {"quality_time": 2})
    ]),
    tier="core", cg="qt_receive_1", opacity=0.6))

questions.append(q("quality_time", "behavioral_recall",
    "When you want to feel connected, what do you suggest?",
    opts([
        ("'Let's hang out — no agenda, no phones, just us'", {"quality_time": 5}),
        ("'I want to tell you something' — a deep conversation", {"words_of_affirmation": 4}),
        ("You move closer physically — sit next to them, touch their hand", {"physical_touch": 5}),
        ("You do something for them — make coffee, handle a task", {"acts_of_service": 4})
    ]),
    tier="core", cg="qt_express_1", opacity=0.6))

questions.append(q("quality_time", "somatic",
    "When you haven't had uninterrupted time with your partner for a while, your body:",
    opts([
        ("Feels disconnected and anxious — like the relationship is slipping", {"quality_time": 5}),
        ("A bit lonely but manageable", {"quality_time": 3}),
        ("Fine — you'll catch up when you can", {"quality_time": 1}),
        ("Missing them, but a text or call fills the gap", {"words_of_affirmation": 3})
    ]),
    tier="core", cg="qt_receive_1", opacity=0.7))

questions.append(q("quality_time", "forced_choice",
    "Which is more important?",
    opts([
        ("Your partner being fully present when together — even if it's less time", {"quality_time": 5}),
        ("Your partner helping you with things — even if distracted while doing it", {"acts_of_service": 5})
    ]),
    tier="core", cg="qt_receive_1", opacity=0.75))

questions.append(q("quality_time", "partner_perspective",
    "A perfect evening with your partner looks like:",
    opts([
        ("Hours of talking, cooking together, or just being in the same room undistracted", {"quality_time": 5}),
        ("Them taking care of everything while you relax", {"acts_of_service": 4}),
        ("Exchanging heartfelt words about your relationship", {"words_of_affirmation": 4}),
        ("Physical intimacy — closeness, touching, sex", {"physical_touch": 5})
    ]),
    tier="core", cg="qt_receive_1", opacity=0.55))

questions.append(q("quality_time", "scenario",
    "Your partner surprises you with concert tickets vs. clears their entire Saturday for whatever you want. You prefer:",
    opts([
        ("The Saturday — their TIME is the gift", {"quality_time": 5}),
        ("The concert — the thought and the experience matter", {"receiving_gifts": 4}),
        ("Depends on the concert vs. what we'd do Saturday", {"quality_time": 3})
    ]),
    tier="triangulation", cg="qt_receive_1", opacity=0.6))

questions.append(q("quality_time", "behavioral_recall",
    "When you think about people you feel closest to, what do you DO with them?",
    opts([
        ("Spend long stretches together — quality of presence matters most", {"quality_time": 5}),
        ("Talk openly — deep conversation is our glue", {"words_of_affirmation": 4}),
        ("Physical activities or being physically close", {"physical_touch": 3}),
        ("Take care of each other — mutual service", {"acts_of_service": 4})
    ]),
    tier="triangulation", cg="qt_express_1", opacity=0.6))

questions.append(q("quality_time", "somatic",
    "When someone gives you their undivided attention — eye contact, active listening, phone away — your body:",
    opts([
        ("Opens up — this is when you feel most loved and most yourself", {"quality_time": 5}),
        ("Feels seen — it's nice", {"quality_time": 3}),
        ("Feels slightly pressured — intense focus can be overwhelming", {"quality_time": 1}),
        ("Doesn't react differently than if they were multitasking", {"quality_time": 1})
    ]),
    tier="core", cg="qt_receive_1", opacity=0.7))

questions.append(q("quality_time", "forced_choice",
    "Your partner can spend 2 hours fully present or 4 hours while also working. You choose:",
    opts([
        ("2 hours fully present — quality over quantity every time", {"quality_time": 5}),
        ("4 hours — even divided attention is still togetherness", {"quality_time": 2})
    ]),
    tier="consistency_check", cg="qt_receive_1", opacity=0.75))

questions.append(q("quality_time", "temporal",
    "Think about your happiest relationship moments. The common thread is:",
    opts([
        ("Shared TIME — road trips, lazy mornings, evenings talking for hours", {"quality_time": 5}),
        ("Shared WORDS — deep conversations, love letters", {"words_of_affirmation": 5}),
        ("Shared ACTIONS — building things together, mutual care", {"acts_of_service": 4}),
        ("Shared TOUCH — physical closeness, intimacy", {"physical_touch": 5})
    ]),
    tier="core", cg="qt_receive_1", opacity=0.65))

questions.append(q("quality_time", "scenario",
    "Long-distance relationship: what would be hardest?",
    opts([
        ("Not spending daily time together — the distance itself", {"quality_time": 5}),
        ("Not being able to touch them", {"physical_touch": 5}),
        ("Not hearing their voice say loving things as often", {"words_of_affirmation": 4}),
        ("Not being able to do things for each other in person", {"acts_of_service": 4})
    ]),
    tier="triangulation", cg="qt_receive_1", opacity=0.65))

questions.append(q("quality_time", "behavioral_recall",
    "When a friend cancels plans you were looking forward to, how disappointing is it?",
    opts([
        ("Deeply — I was counting on that time together", {"quality_time": 5}),
        ("Bummed but I'll find something else", {"quality_time": 3}),
        ("Mild — I'll text them instead", {"quality_time": 1}),
        ("Honestly, sometimes cancelled plans is a gift", {"quality_time": 1})
    ]),
    tier="triangulation", cg="qt_receive_1", opacity=0.5))

questions.append(q("quality_time", "partner_perspective",
    "The relationship behavior you find MOST disrespectful is:",
    opts([
        ("Consistently choosing work, friends, or phone over time with you", {"quality_time": 5}),
        ("Failing to acknowledge or affirm you verbally", {"words_of_affirmation": 5}),
        ("Never helping when you clearly need it", {"acts_of_service": 5}),
        ("Flinching from or avoiding your touch", {"physical_touch": 5})
    ]),
    tier="core", cg="qt_receive_1", opacity=0.7))

questions.append(q("quality_time", "trap",
    "Your partner works long hours. They compensate with expensive gifts. You feel:",
    opts([
        ("Like gifts can't replace presence — I'd rather have the time", {"quality_time": 5, "receiving_gifts": 1}),
        ("Appreciated — the gifts show they're thinking of me", {"receiving_gifts": 4}),
        ("Mixed — I want both", {"quality_time": 3, "receiving_gifts": 3}),
        ("Fine — I value my independence and enjoy the gifts", {"quality_time": 1})
    ]),
    tier="trap", trap=True, cg="qt_receive_1", opacity=0.6))

questions.append(q("quality_time", "forced_choice",
    "Which is a stronger expression of love?",
    opts([
        ("Canceling something important to be with you when you need them", {"quality_time": 5}),
        ("Staying up late to handle something stressful so you don't have to", {"acts_of_service": 5})
    ]),
    tier="triangulation", cg="qt_receive_1", opacity=0.7))

questions.append(q("quality_time", "behavioral_recall",
    "How important is it that your partner shares your hobbies — not because they have to, but for shared time?",
    opts([
        ("Very — shared interests create shared time which IS the relationship", {"quality_time": 5}),
        ("Somewhat — nice but not essential if we connect otherwise", {"quality_time": 3}),
        ("Not very — separate interests are fine", {"quality_time": 2}),
        ("Irrelevant — I'd rather they be their own person", {"quality_time": 1})
    ]),
    tier="consistency_check", cg="qt_receive_1", opacity=0.6))

questions.append(q("quality_time", "scenario",
    "You and your partner have 30 free minutes. You'd most like to:",
    opts([
        ("Talk about your days, really connect — phones down, eyes on each other", {"quality_time": 5}),
        ("Cuddle on the couch — no talking, just closeness", {"physical_touch": 5}),
        ("Tackle a small project together", {"acts_of_service": 3}),
        ("Exchange appreciation — 'here's what I loved about today'", {"words_of_affirmation": 4})
    ]),
    tier="triangulation", cg="qt_receive_1", opacity=0.55))

questions.append(q("quality_time", "somatic",
    "After spending uninterrupted quality time with your partner — no phones, no distractions — your body feels:",
    opts([
        ("Filled up — like your love tank is full. THIS is what you needed.", {"quality_time": 5}),
        ("Good — connected and happy", {"quality_time": 3}),
        ("Nice but not different than how touch or kind words make you feel", {"quality_time": 2}),
        ("The same — time together is fine but not the thing that fills you up", {"quality_time": 1})
    ]),
    tier="core", cg="qt_receive_1", opacity=0.7))

questions.append(q("quality_time", "partner_perspective",
    "Your partner is leaving for a week. Before they go, you most want:",
    opts([
        ("An entire evening together — just you two, unrushed", {"quality_time": 5}),
        ("A long hug, deep kiss, and physical closeness", {"physical_touch": 5}),
        ("A letter or text to read while they're gone", {"words_of_affirmation": 5}),
        ("For them to handle everything that'll need doing while away", {"acts_of_service": 4})
    ]),
    tier="core", cg="qt_receive_1", opacity=0.6))

# ============================================================
# PHYSICAL_TOUCH (20)
# ============================================================

questions.append(q("physical_touch", "somatic",
    "When your partner reaches for your hand in public, your body:",
    opts([
        ("Melts — casual physical contact is one of the greatest feelings", {"physical_touch": 5}),
        ("Feels nice — pleasant sensation", {"physical_touch": 3}),
        ("Doesn't react much — fine but not especially meaningful", {"physical_touch": 1}),
        ("Stiffens slightly — not big on PDA", {"physical_touch": 1})
    ]),
    tier="core", cg="pt_receive_1", opacity=0.6))

questions.append(q("physical_touch", "behavioral_recall",
    "How often do you initiate physical contact with people you're close to?",
    opts([
        ("Constantly — I'm always reaching for people I love", {"physical_touch": 5}),
        ("Often — touch is natural for me in close relationships", {"physical_touch": 4}),
        ("Sometimes — depends on person and mood", {"physical_touch": 2}),
        ("Rarely — I'm not naturally a toucher", {"physical_touch": 1})
    ]),
    tier="core", cg="pt_express_1", opacity=0.55))

questions.append(q("physical_touch", "scenario",
    "You're upset about something. What soothes you fastest?",
    opts([
        ("Being held — arms around you, physical safety", {"physical_touch": 5}),
        ("Hearing 'I'm here for you' — verbal reassurance", {"words_of_affirmation": 4}),
        ("Someone taking the problem off your plate", {"acts_of_service": 4}),
        ("Someone sitting with you — quiet presence", {"quality_time": 4})
    ]),
    tier="core", cg="pt_receive_1", opacity=0.6))

questions.append(q("physical_touch", "forced_choice",
    "In a relationship, which would you miss most if it disappeared?",
    opts([
        ("All casual physical affection — hugs, hand-holding, sitting close", {"physical_touch": 5}),
        ("All verbal expressions of love — compliments, 'I love you'", {"words_of_affirmation": 5})
    ]),
    tier="core", cg="pt_receive_1", opacity=0.75))

questions.append(q("physical_touch", "partner_perspective",
    "Your partner has been physically distant — sleeping far apart, not reaching for you. You feel:",
    opts([
        ("Devastated — physical distance IS emotional distance for you", {"physical_touch": 5}),
        ("Concerned — you want to ask what's wrong", {"physical_touch": 3}),
        ("A bit sad but you don't need constant physical contact", {"physical_touch": 2}),
        ("Fine — maybe they just need space", {"physical_touch": 1})
    ]),
    tier="core", cg="pt_receive_1", opacity=0.7))

questions.append(q("physical_touch", "somatic",
    "When you greet someone you love after time apart, your body's first impulse is:",
    opts([
        ("Full-body hug — long, tight, physical", {"physical_touch": 5}),
        ("Hug then a stream of 'I missed you, tell me everything'", {"physical_touch": 3, "words_of_affirmation": 3}),
        ("Excited to be together — the greeting style matters less than being together", {"quality_time": 4}),
        ("A wave or verbal greeting — not a hugger", {"physical_touch": 1})
    ]),
    tier="triangulation", cg="pt_express_1", opacity=0.55))

questions.append(q("physical_touch", "behavioral_recall",
    "Sitting next to your partner on the couch, how much of the time are you physically touching?",
    opts([
        ("Almost always — physical contact is default when we're near each other", {"physical_touch": 5}),
        ("Often — we gravitate toward each other naturally", {"physical_touch": 4}),
        ("Sometimes — depends on what we're doing", {"physical_touch": 2}),
        ("Rarely — we sit near but don't necessarily touch", {"physical_touch": 1})
    ]),
    tier="consistency_check", cg="pt_express_1", opacity=0.5))

questions.append(q("physical_touch", "scenario",
    "After a fight with your partner, what signals things are okay?",
    opts([
        ("They reach for you physically — hand on knee, embrace, coming close", {"physical_touch": 5}),
        ("They say 'I'm sorry, I love you' — verbal repair", {"words_of_affirmation": 5}),
        ("They do something kind — make you coffee, handle something", {"acts_of_service": 4}),
        ("They sit with you and give full attention — present and engaged", {"quality_time": 4})
    ]),
    tier="core", cg="pt_receive_1", opacity=0.65))

questions.append(q("physical_touch", "forced_choice",
    "Which absence creates more loneliness?",
    opts([
        ("A partner who never touches you — no hugs, handholding, casual contact", {"physical_touch": 5}),
        ("A partner who never has time for you — always busy, always distracted", {"quality_time": 5})
    ]),
    tier="triangulation", cg="pt_receive_1", opacity=0.75))

questions.append(q("physical_touch", "temporal",
    "The most comforting moment in your relationship history was defined by:",
    opts([
        ("Physical contact — being held, touch that said everything", {"physical_touch": 5}),
        ("Words — something they said you'll never forget", {"words_of_affirmation": 5}),
        ("Action — something they did that showed pure love", {"acts_of_service": 5}),
        ("Presence — just BEING there when you needed someone", {"quality_time": 5})
    ]),
    tier="core", cg="pt_receive_1", opacity=0.65))

questions.append(q("physical_touch", "partner_perspective",
    "If your partner expressed love by rubbing your back, playing with your hair, resting their head on you throughout the day, this would feel:",
    opts([
        ("Like heaven — exactly what love should feel like", {"physical_touch": 5}),
        ("Very nice — physical affection is welcome", {"physical_touch": 4}),
        ("Pleasant but you'd prefer love through words or actions", {"physical_touch": 2}),
        ("Overwhelming — you'd need them to tone it down", {"physical_touch": 1})
    ]),
    tier="triangulation", cg="pt_receive_1", opacity=0.6))

questions.append(q("physical_touch", "behavioral_recall",
    "When you're excited or happy, what does your body want to DO?",
    opts([
        ("Grab someone — hug, high-five, squeeze, jump on them", {"physical_touch": 5}),
        ("Tell someone — call, text, blurt it out", {"words_of_affirmation": 4}),
        ("Share the moment — be with someone in the joy", {"quality_time": 3}),
        ("Channel the energy into action — do something productive", {"acts_of_service": 2})
    ]),
    tier="triangulation", cg="pt_express_1", opacity=0.55))

questions.append(q("physical_touch", "trap",
    "People who say they 'aren't touchy-feely.' You think:",
    opts([
        ("I literally cannot imagine that — touch is essential to my wellbeing", {"physical_touch": 5}),
        ("Different strokes — some people aren't wired that way", {"physical_touch": 3}),
        ("I understand — I'm not naturally touchy-feely either", {"physical_touch": 1}),
        ("Maybe they haven't been touched by the right person", {"physical_touch": 4})
    ]),
    tier="trap", trap=True, cg="pt_receive_1", opacity=0.55))

questions.append(q("physical_touch", "scenario",
    "You walk past your partner in the kitchen. Without thinking, do you:",
    opts([
        ("Touch them — hand on waist, kiss on neck, brush against them", {"physical_touch": 5}),
        ("Say something affectionate — 'hey beautiful' or 'love you'", {"words_of_affirmation": 4}),
        ("Smile and keep moving — no particular impulse to interact", {"physical_touch": 1}),
        ("Check if they need help with anything", {"acts_of_service": 3})
    ]),
    tier="core", cg="pt_express_1", opacity=0.5))

questions.append(q("physical_touch", "somatic",
    "When you haven't been physically touched by anyone for days, your body:",
    opts([
        ("Craves it — physically starved and emotionally depleted", {"physical_touch": 5}),
        ("Misses it — a dull ache of absence", {"physical_touch": 4}),
        ("Notes it but manages fine", {"physical_touch": 2}),
        ("Doesn't notice — touch isn't a need that registers as urgent", {"physical_touch": 1})
    ]),
    tier="core", cg="pt_receive_1", opacity=0.7))

questions.append(q("physical_touch", "forced_choice",
    "After a long day, which recharges you more?",
    opts([
        ("A 20-minute massage from your partner — silent, physical, intimate", {"physical_touch": 5}),
        ("A 20-minute conversation where they give complete attention", {"quality_time": 5})
    ]),
    tier="consistency_check", cg="pt_receive_1", opacity=0.7))

questions.append(q("physical_touch", "temporal",
    "In relationships that ended, did physical affection decline first or did other things go first?",
    opts([
        ("Physical affection went first — and that was the canary in the coal mine", {"physical_touch": 5}),
        ("Communication went first — we stopped talking before we stopped touching", {"words_of_affirmation": 4, "quality_time": 3}),
        ("Quality time went first — we stopped spending time together", {"quality_time": 5}),
        ("Acts of caring went first", {"acts_of_service": 4})
    ]),
    tier="triangulation", cg="pt_receive_1", opacity=0.65))

questions.append(q("physical_touch", "partner_perspective",
    "Falling asleep next to your partner, you need:",
    opts([
        ("Physical contact — touching feet, arm across them, spooning", {"physical_touch": 5}),
        ("Closeness but not necessarily touching", {"physical_touch": 3}),
        ("Your own space — you sleep better without contact", {"physical_touch": 1}),
        ("A goodnight 'I love you' matters more than position", {"words_of_affirmation": 4})
    ]),
    tier="core", cg="pt_receive_1", opacity=0.6))

questions.append(q("physical_touch", "behavioral_recall",
    "How do you comfort a crying child?",
    opts([
        ("Pick them up, hold them tight — physical comfort first", {"physical_touch": 5}),
        ("Kneel down and talk to them — verbal soothing", {"words_of_affirmation": 4}),
        ("Fix whatever made them cry — solve the problem", {"acts_of_service": 4}),
        ("Sit with them and be present until they calm down", {"quality_time": 4})
    ]),
    tier="triangulation", cg="pt_express_1", opacity=0.55))

questions.append(q("physical_touch", "scenario",
    "Your partner comes home after a terrible day. Before they speak, you:",
    opts([
        ("Open your arms — no words needed, just hold them", {"physical_touch": 5}),
        ("Say 'Tell me everything — what happened?'", {"quality_time": 4, "words_of_affirmation": 3}),
        ("Start making them dinner or drawing a bath", {"acts_of_service": 5}),
        ("Sit next to them, fully present, and wait for them to be ready", {"quality_time": 5})
    ]),
    tier="core", cg="pt_express_1", opacity=0.55))


questions.append(q("quality_time", "behavioral_recall",
    "When you look at your phone screen time and realize you spent 3 hours scrolling while sitting next to your partner, you feel:",
    opts([
        ("Guilty — that was time we could have been actually together", {"quality_time": 5}),
        ("Mildly regretful but it happens", {"quality_time": 3}),
        ("Fine — parallel screen time is still togetherness", {"quality_time": 1}),
        ("You wouldn't notice — screen time next to your partner is comfortable", {"quality_time": 1})
    ]),
    tier="triangulation", cg="qt_receive_1", opacity=0.55))


assert len(questions) == 100, f"Expected 100, got {len(questions)}"

with open("/Users/user/personal/sb/trueassess/priv/question_bank/love_languages.json", "w") as f:
    json.dump(questions, f, indent=2)

print(f"Love Languages: {len(questions)} questions written")
from collections import Counter
dims = Counter(q["dimension"] for q in questions)
print("Distribution:", dict(dims))
tiers = Counter(q["tier_role"] for q in questions)
print("Tiers:", dict(tiers))
types = Counter(q["question_type"] for q in questions)
print("Types:", dict(types))
