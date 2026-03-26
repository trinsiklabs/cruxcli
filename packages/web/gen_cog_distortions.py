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
        "tags": tags or ["cognitive_distortions", dim]
    }

def opts(choices):
    return [{"id": chr(97+i), "text": t, "scores": s} for i, (t, s) in enumerate(choices)]

# 200 questions across 17 dimensions (~12 each)
# High scores = MORE of the distortion

# ============================================================
# ALL_OR_NOTHING (12)
# ============================================================

questions.append(q("all_or_nothing", "scenario",
    "You've been eating healthy for two weeks. At a party, you eat three slices of pizza. The next morning you think:",
    opts([
        ("Back on track today — one meal doesn't erase two weeks", {"all_or_nothing": 1}),
        ("Not ideal but not a disaster — pizza happens", {"all_or_nothing": 2}),
        ("I already blew it — might as well enjoy the rest of the weekend and restart Monday", {"all_or_nothing": 5}),
        ("I'm clearly not disciplined enough for this — why even try?", {"all_or_nothing": 5})
    ]),
    tier="core", cg="aon_perfection_1", opacity=0.55))

questions.append(q("all_or_nothing", "behavioral_recall",
    "When you start a new habit or project, how often do you quit entirely after one setback?",
    opts([
        ("Rarely — setbacks are part of the process", {"all_or_nothing": 1}),
        ("Sometimes — depends on how bad the setback is", {"all_or_nothing": 2}),
        ("Often — if I can't do it perfectly, I'd rather not do it at all", {"all_or_nothing": 5}),
        ("Almost always — one failure means the whole thing is ruined", {"all_or_nothing": 5})
    ]),
    tier="core", cg="aon_perfection_1", opacity=0.65))

questions.append(q("all_or_nothing", "partner_perspective",
    "Your partner makes a mistake that hurts you. Your thinking shifts to:",
    opts([
        ("They're human — this one thing doesn't define them", {"all_or_nothing": 1}),
        ("This is concerning but let's see the full picture", {"all_or_nothing": 2}),
        ("They're clearly not who I thought they were — everything is different now", {"all_or_nothing": 5}),
        ("If they could do THIS, what else are they capable of?", {"all_or_nothing": 4})
    ]),
    tier="core", cg="aon_relationships_1", opacity=0.7))

questions.append(q("all_or_nothing", "forced_choice",
    "Which is closer to how you think?",
    opts([
        ("Most things exist on a spectrum — success, failure, good, bad", {"all_or_nothing": 1}),
        ("Either something worked or it didn't — gray areas are just excuses", {"all_or_nothing": 5})
    ]),
    tier="core", cg="aon_perfection_1", opacity=0.8))

questions.append(q("all_or_nothing", "scenario",
    "You get 95% on an exam but missed one question you knew the answer to. You focus on:",
    opts([
        ("The 95% — that's excellent", {"all_or_nothing": 1}),
        ("Mostly the success, but the missed question nags a bit", {"all_or_nothing": 2}),
        ("The one you missed — you KNEW it and still got it wrong", {"all_or_nothing": 4}),
        ("The exam is ruined — 95% isn't 100%", {"all_or_nothing": 5})
    ]),
    tier="triangulation", cg="aon_perfection_1", opacity=0.55))

questions.append(q("all_or_nothing", "temporal",
    "When you describe a day, how often do you categorize it as entirely 'good' or entirely 'bad'?",
    opts([
        ("Rarely — most days are a mix", {"all_or_nothing": 1}),
        ("Sometimes — some days really are all good or all bad", {"all_or_nothing": 2}),
        ("Often — my day gets labeled based on one significant event", {"all_or_nothing": 4}),
        ("Almost always — one bad thing makes it a bad day", {"all_or_nothing": 5})
    ]),
    tier="consistency_check", cg="aon_perfection_1", opacity=0.6))

questions.append(q("all_or_nothing", "scenario",
    "You try a new skill and you're mediocre at it on day one. Your thought is:",
    opts([
        ("Obviously — everyone starts somewhere", {"all_or_nothing": 1}),
        ("I'll get better with practice", {"all_or_nothing": 1}),
        ("I'm either naturally good at things or I'm not — this clearly isn't for me", {"all_or_nothing": 5}),
        ("If I can't be great at it, there's no point continuing", {"all_or_nothing": 5})
    ]),
    tier="triangulation", cg="aon_perfection_1", opacity=0.6))

questions.append(q("all_or_nothing", "somatic",
    "When something in your life goes from 'great' to 'just okay,' your body:",
    opts([
        ("Barely registers the shift — 'okay' is still fine", {"all_or_nothing": 1}),
        ("Feels mild disappointment that passes quickly", {"all_or_nothing": 2}),
        ("Reacts as if it went from great to terrible — the middle doesn't exist", {"all_or_nothing": 5}),
        ("Crashes — you can't find motivation for something that's merely 'okay'", {"all_or_nothing": 5})
    ]),
    tier="core", cg="aon_perfection_1", opacity=0.7))

questions.append(q("all_or_nothing", "behavioral_recall",
    "How do you categorize people in your life — as entirely trustworthy or entirely untrustworthy?",
    opts([
        ("I don't — everyone is complex, trust is contextual", {"all_or_nothing": 1}),
        ("I lean toward trusting most people with appropriate caution", {"all_or_nothing": 2}),
        ("Once someone breaks my trust, they move from 'trusted' to 'can't trust' permanently", {"all_or_nothing": 4}),
        ("People are either with me or against me — there's no middle ground", {"all_or_nothing": 5})
    ]),
    tier="triangulation", cg="aon_relationships_1", opacity=0.7))

questions.append(q("all_or_nothing", "trap",
    "A friend says 'You're so extreme — it's either the best thing ever or the worst thing ever with you.' You think:",
    opts([
        ("They have a point — I do think in extremes", {"all_or_nothing": 4}),
        ("That's not quite right but I see why they'd say it", {"all_or_nothing": 3}),
        ("They're wrong — I'm perfectly nuanced", {"all_or_nothing": 2}),
        ("Of course — because things usually ARE either great or terrible", {"all_or_nothing": 5})
    ]),
    tier="trap", trap=True, cg="aon_perfection_1", opacity=0.6))

questions.append(q("all_or_nothing", "partner_perspective",
    "Your partner has a flaw you can't ignore. Does it color EVERYTHING about them?",
    opts([
        ("No — people are packages. The flaw exists alongside genuine strengths", {"all_or_nothing": 1}),
        ("It doesn't define them but it does sometimes overshadow things", {"all_or_nothing": 3}),
        ("Yes — once I see a serious flaw, I can't unsee it and it taints everything", {"all_or_nothing": 5}),
        ("I go back and forth — some days they're perfect, some days the flaw is all I see", {"all_or_nothing": 4})
    ]),
    tier="core", cg="aon_relationships_1", opacity=0.7))

questions.append(q("all_or_nothing", "scenario",
    "You applied for a promotion and didn't get it. Your conclusion:",
    opts([
        ("Not this time — I'll learn from the feedback and try again", {"all_or_nothing": 1}),
        ("Disappointing, but there will be other opportunities", {"all_or_nothing": 2}),
        ("I'm obviously not good enough and never will be", {"all_or_nothing": 5}),
        ("This company doesn't value me — time to burn it all down and start over", {"all_or_nothing": 5})
    ]),
    tier="core", cg="aon_perfection_1", opacity=0.65))

# ============================================================
# CATASTROPHIZING (12)
# ============================================================

questions.append(q("catastrophizing", "scenario",
    "You feel a new pain in your body that you haven't noticed before. Your first thought is:",
    opts([
        ("Probably slept wrong or overdid it at the gym", {"catastrophizing": 1}),
        ("I'll keep an eye on it — if it persists, I'll see a doctor", {"catastrophizing": 2}),
        ("What if it's something serious? I should Google the symptoms", {"catastrophizing": 4}),
        ("This could be cancer. Or a blood clot. I need to go to the ER.", {"catastrophizing": 5})
    ]),
    tier="core", cg="cat_health_1", opacity=0.6))

questions.append(q("catastrophizing", "behavioral_recall",
    "When something goes wrong, how quickly does your mind jump to the absolute worst-case scenario?",
    opts([
        ("Almost never — I stay grounded in what's likely", {"catastrophizing": 1}),
        ("Occasionally — in genuinely ambiguous or high-stakes situations", {"catastrophizing": 2}),
        ("Regularly — worst case is usually my first stop", {"catastrophizing": 4}),
        ("Instantly — my brain defaults to catastrophe before I can stop it", {"catastrophizing": 5})
    ]),
    tier="core", cg="cat_general_1", opacity=0.7))

questions.append(q("catastrophizing", "partner_perspective",
    "Your partner is 30 minutes late and isn't answering their phone. By minute 20, you're thinking:",
    opts([
        ("Traffic or a dead phone — they'll show up", {"catastrophizing": 1}),
        ("Mildly concerned but mostly annoyed", {"catastrophizing": 2}),
        ("Something might have happened — checking the news for accidents", {"catastrophizing": 4}),
        ("They're dead. Or cheating. Something terrible has happened.", {"catastrophizing": 5})
    ]),
    tier="core", cg="cat_general_1", opacity=0.6))

questions.append(q("catastrophizing", "somatic",
    "When you hear unexpected news (your boss wants a meeting, a friend says 'we need to talk'), your body:",
    opts([
        ("Stays calm — could be anything", {"catastrophizing": 1}),
        ("Brief spike of alertness, then levels out", {"catastrophizing": 2}),
        ("Floods with adrenaline — this is going to be terrible", {"catastrophizing": 4}),
        ("Full panic — you've already imagined the worst before they speak", {"catastrophizing": 5})
    ]),
    tier="core", cg="cat_general_1", opacity=0.7))

questions.append(q("catastrophizing", "scenario",
    "You notice your partner has been texting more than usual and seems secretive about their phone. You:",
    opts([
        ("Don't think much of it — could be a surprise, could be nothing", {"catastrophizing": 1}),
        ("Feel curious but don't jump to conclusions", {"catastrophizing": 2}),
        ("Start building a narrative: they're cheating, the relationship is over", {"catastrophizing": 5}),
        ("Can't sleep, can't eat — the uncertainty feels like proof of the worst", {"catastrophizing": 5})
    ]),
    tier="triangulation", cg="cat_general_1", opacity=0.65))

questions.append(q("catastrophizing", "forced_choice",
    "When facing uncertainty, your mind tends to:",
    opts([
        ("Consider the most likely outcome and plan for it", {"catastrophizing": 1}),
        ("Jump to the worst possible outcome and plan for THAT", {"catastrophizing": 5})
    ]),
    tier="consistency_check", cg="cat_general_1", opacity=0.8))

questions.append(q("catastrophizing", "temporal",
    "Think about the last 5 things you catastrophized about. How many actually turned out as bad as you feared?",
    opts([
        ("None or one — my fears are almost always worse than reality", {"catastrophizing": 4}),
        ("Maybe two — sometimes bad things do happen", {"catastrophizing": 3}),
        ("I don't catastrophize enough to have 5 examples", {"catastrophizing": 1}),
        ("All of them — because I have good reason to expect the worst", {"catastrophizing": 5})
    ]),
    tier="trap", trap=True, cg="cat_general_1", opacity=0.65))

questions.append(q("catastrophizing", "behavioral_recall",
    "How often do you use phrases like 'this is the worst thing ever' or 'everything is ruined'?",
    opts([
        ("Rarely or never — those phrases feel dramatically disproportionate", {"catastrophizing": 1}),
        ("In jest — I'm dramatic for humor, not because I believe it", {"catastrophizing": 2}),
        ("More than I'd like to admit — my language matches my catastrophic thoughts", {"catastrophizing": 4}),
        ("Regularly — because it often FEELS like the worst thing ever", {"catastrophizing": 5})
    ]),
    tier="triangulation", cg="cat_general_1", opacity=0.55))

questions.append(q("catastrophizing", "scenario",
    "You make a mistake at work that your boss notices. Your thought spiral goes to:",
    opts([
        ("I need to fix this and learn from it", {"catastrophizing": 1}),
        ("Embarrassing, but manageable", {"catastrophizing": 2}),
        ("My boss is going to lose trust in me. This will affect my review. I might get put on a PIP.", {"catastrophizing": 4}),
        ("I'm going to get fired. I'll lose my income. I'll lose my apartment. My life is over.", {"catastrophizing": 5})
    ]),
    tier="core", cg="cat_general_1", opacity=0.6))

questions.append(q("catastrophizing", "somatic",
    "When a small problem arises (flat tire, minor conflict, unexpected expense), your stress response is:",
    opts([
        ("Proportional — this is annoying, not life-threatening", {"catastrophizing": 1}),
        ("Slightly elevated but manageable", {"catastrophizing": 2}),
        ("Way out of proportion — your body reacts like it's a crisis", {"catastrophizing": 4}),
        ("Full emergency mode — heart racing, can't think straight, doom", {"catastrophizing": 5})
    ]),
    tier="triangulation", cg="cat_health_1", opacity=0.65))

questions.append(q("catastrophizing", "partner_perspective",
    "People close to you would say your reaction to bad news is:",
    opts([
        ("Measured — you take things in stride", {"catastrophizing": 1}),
        ("Slightly anxious but you cope well", {"catastrophizing": 2}),
        ("Intense — you tend to see things as worse than they are", {"catastrophizing": 4}),
        ("Extreme — every problem becomes a catastrophe", {"catastrophizing": 5})
    ]),
    tier="consistency_check", cg="cat_general_1", opacity=0.65))

questions.append(q("catastrophizing", "scenario",
    "Your flight is delayed by 3 hours. Your brain:",
    opts([
        ("Adjusts plans, finds a coffee shop, settles in", {"catastrophizing": 1}),
        ("Mildly annoyed, checks for rebooking options", {"catastrophizing": 2}),
        ("Starts cascading: I'll miss my connection, the whole trip is ruined, what about the hotel...", {"catastrophizing": 4}),
        ("Complete meltdown — everything is falling apart and nothing will be salvageable", {"catastrophizing": 5})
    ]),
    tier="triangulation", cg="cat_general_1", opacity=0.5))

# ============================================================
# MIND_READING (12)
# ============================================================

questions.append(q("mind_reading", "scenario",
    "Your friend seems quieter than usual at lunch. You assume:",
    opts([
        ("They're tired or preoccupied — probably not about me", {"mind_reading": 1}),
        ("I'll ask if they're okay", {"mind_reading": 2}),
        ("I probably said something that upset them", {"mind_reading": 4}),
        ("They're definitely mad at me — I'm going through every recent interaction to figure out why", {"mind_reading": 5})
    ]),
    tier="core", cg="mr_social_1", opacity=0.6))

questions.append(q("mind_reading", "behavioral_recall",
    "How often do you 'know' what someone is thinking about you without them saying anything?",
    opts([
        ("I don't assume — I ask if I want to know", {"mind_reading": 1}),
        ("Occasionally I get a sense, but I check it rather than assuming", {"mind_reading": 2}),
        ("Regularly — I'm highly attuned to people's unspoken feelings about me", {"mind_reading": 4}),
        ("Constantly — I can read people like a book and they're usually thinking something negative", {"mind_reading": 5})
    ]),
    tier="core", cg="mr_social_1", opacity=0.7))

questions.append(q("mind_reading", "partner_perspective",
    "Your partner is quiet after a disagreement. Without them saying anything, you're convinced they're:",
    opts([
        ("Processing — I'll give them space and check in later", {"mind_reading": 1}),
        ("Probably upset but I don't know exactly what they're thinking", {"mind_reading": 2}),
        ("Thinking about leaving the relationship", {"mind_reading": 5}),
        ("Cataloguing everything wrong with me", {"mind_reading": 5})
    ]),
    tier="core", cg="mr_relationship_1", opacity=0.7))

questions.append(q("mind_reading", "somatic",
    "When you walk into a room and people glance at you, your body assumes:",
    opts([
        ("Normal social behavior — people look at whoever enters a room", {"mind_reading": 1}),
        ("Casual acknowledgment — no big deal", {"mind_reading": 2}),
        ("They were talking about me and now they're watching my reaction", {"mind_reading": 4}),
        ("I can FEEL their judgment — I know exactly what they're thinking", {"mind_reading": 5})
    ]),
    tier="triangulation", cg="mr_social_1", opacity=0.65))

questions.append(q("mind_reading", "forced_choice",
    "When someone gives you a neutral facial expression, you tend to read it as:",
    opts([
        ("Neutral — it doesn't contain information about their feelings toward me", {"mind_reading": 1}),
        ("Negative — they're masking disapproval or disinterest", {"mind_reading": 5})
    ]),
    tier="core", cg="mr_social_1", opacity=0.8))

questions.append(q("mind_reading", "scenario",
    "You send a text to a friend and get a one-word reply. You think:",
    opts([
        ("They're busy — no deeper meaning", {"mind_reading": 1}),
        ("Maybe they're not in a texting mood", {"mind_reading": 2}),
        ("They don't want to talk to me", {"mind_reading": 4}),
        ("I've done something wrong and the short reply is passive-aggressive", {"mind_reading": 5})
    ]),
    tier="triangulation", cg="mr_social_1", opacity=0.55))

questions.append(q("mind_reading", "behavioral_recall",
    "How often do you change your behavior based on what you ASSUME others are thinking, without actually checking?",
    opts([
        ("Rarely — I base my behavior on what people actually say", {"mind_reading": 1}),
        ("Sometimes — but I'm usually aware I'm guessing", {"mind_reading": 2}),
        ("Often — my assumptions about others' thoughts drive a lot of my behavior", {"mind_reading": 4}),
        ("Constantly — and I'm usually right (or so I tell myself)", {"mind_reading": 5})
    ]),
    tier="core", cg="mr_social_1", opacity=0.7))

questions.append(q("mind_reading", "partner_perspective",
    "Your partner says 'It's fine' in a tone you can't quite read. You:",
    opts([
        ("Take it at face value — they said it's fine", {"mind_reading": 1}),
        ("Note the tone, ask once more if they're sure, then accept their answer", {"mind_reading": 2}),
        ("Know it's NOT fine and start guessing what's actually wrong", {"mind_reading": 4}),
        ("Launch into a defensive monologue about what you think they're really upset about", {"mind_reading": 5})
    ]),
    tier="triangulation", cg="mr_relationship_1", opacity=0.6))

questions.append(q("mind_reading", "trap",
    "You pride yourself on your ability to read people. How often are your reads actually confirmed?",
    opts([
        ("I don't claim to read minds — I ask people directly", {"mind_reading": 1}),
        ("Sometimes I'm right, but I've been surprised enough to know I'm not always accurate", {"mind_reading": 2}),
        ("I'm right more often than not — my intuition is strong", {"mind_reading": 4}),
        ("Almost always — which is why I trust my reads over their words", {"mind_reading": 5})
    ]),
    tier="trap", trap=True, cg="mr_social_1", opacity=0.65))

questions.append(q("mind_reading", "scenario",
    "You present an idea at work. Your boss's face is unreadable. You conclude:",
    opts([
        ("I'll find out what they thought when they respond — no point guessing", {"mind_reading": 1}),
        ("Could go either way — I'll wait for feedback", {"mind_reading": 2}),
        ("They hated it — that expressionless face says everything", {"mind_reading": 5}),
        ("They think I'm stupid for suggesting it", {"mind_reading": 5})
    ]),
    tier="core", cg="mr_social_1", opacity=0.65))

questions.append(q("mind_reading", "somatic",
    "When you're in a conversation and there's a brief pause, your body:",
    opts([
        ("Relaxes — pauses are natural in conversation", {"mind_reading": 1}),
        ("Feels slightly uncertain but manages", {"mind_reading": 2}),
        ("Races to fill the silence because the other person must be bored or judging you", {"mind_reading": 4}),
        ("Floods with anxiety — silence means they're thinking something negative about you", {"mind_reading": 5})
    ]),
    tier="triangulation", cg="mr_social_1", opacity=0.65))

questions.append(q("mind_reading", "temporal",
    "How many relationships (any kind) have been damaged because you acted on what you ASSUMED someone was thinking, only to find out you were wrong?",
    opts([
        ("None that I can think of — I check my assumptions", {"mind_reading": 1}),
        ("Maybe one — and I learned from it", {"mind_reading": 2}),
        ("Several — it's a pattern I recognize", {"mind_reading": 4}),
        ("Many — but I still think I was probably right even if they denied it", {"mind_reading": 5})
    ]),
    tier="consistency_check", cg="mr_relationship_1", opacity=0.7))

# ============================================================
# PERSONALIZATION (12)
# ============================================================

questions.append(q("personalization", "scenario",
    "Your partner comes home in a terrible mood. Your first thought is:",
    opts([
        ("Something happened at work or on their commute", {"personalization": 1}),
        ("I hope they're okay — I'll ask what's going on", {"personalization": 2}),
        ("What did I do? Did I forget something?", {"personalization": 4}),
        ("It's because of me — everything comes back to something I did or didn't do", {"personalization": 5})
    ]),
    tier="core", cg="per_blame_1", opacity=0.6))

questions.append(q("personalization", "behavioral_recall",
    "When a group event goes badly (party, meeting, trip), how often do you feel personally responsible?",
    opts([
        ("Only if it was specifically my responsibility", {"personalization": 1}),
        ("Sometimes more than warranted — I tend to take too much ownership", {"personalization": 3}),
        ("Almost always — if I was involved, I must have contributed to the problem", {"personalization": 5}),
        ("Always — group failures are my failures, even if I didn't organize it", {"personalization": 5})
    ]),
    tier="core", cg="per_blame_1", opacity=0.65))

questions.append(q("personalization", "partner_perspective",
    "Your child does poorly in school. Your first thought is:",
    opts([
        ("Let me understand what's going on — many factors affect school performance", {"personalization": 1}),
        ("I could probably be doing more to help, but this isn't just about me", {"personalization": 3}),
        ("I've failed as a parent — this is my fault", {"personalization": 5}),
        ("If I'd been a better parent, this wouldn't be happening", {"personalization": 5})
    ]),
    tier="core", cg="per_blame_1", opacity=0.65))

questions.append(q("personalization", "somatic",
    "When someone near you is unhappy, your body automatically:",
    opts([
        ("Notices but doesn't assume responsibility", {"personalization": 1}),
        ("Feels empathy but stays centered", {"personalization": 2}),
        ("Takes it on — their unhappiness must be because of something you did", {"personalization": 5}),
        ("Knots up with guilt — you should be doing something to fix it", {"personalization": 4})
    ]),
    tier="triangulation", cg="per_blame_1", opacity=0.7))

questions.append(q("personalization", "scenario",
    "A friend stops inviting you to group hangouts. Without any conversation, you assume:",
    opts([
        ("Scheduling or logistics — maybe the group dynamic shifted", {"personalization": 1}),
        ("I should check in and see what's going on", {"personalization": 2}),
        ("I did something wrong and they don't want me around", {"personalization": 5}),
        ("I'm not interesting or fun enough for this group", {"personalization": 5})
    ]),
    tier="triangulation", cg="per_blame_1", opacity=0.6))

questions.append(q("personalization", "forced_choice",
    "When something goes wrong in a group, you tend to:",
    opts([
        ("Assess the situation objectively — sometimes it's you, often it's not", {"personalization": 1}),
        ("Assume you played a bigger role in the failure than you probably did", {"personalization": 5})
    ]),
    tier="core", cg="per_blame_1", opacity=0.8))

questions.append(q("personalization", "temporal",
    "Looking at relationships that ended in your life, what percentage do you take full responsibility for?",
    opts([
        ("A fair share — relationships are two-way streets", {"personalization": 1}),
        ("More than half — I probably could have saved most of them", {"personalization": 3}),
        ("Almost all — I was the common denominator", {"personalization": 5}),
        ("All of them — if they failed, it's because of me", {"personalization": 5})
    ]),
    tier="core", cg="per_blame_1", opacity=0.7))

questions.append(q("personalization", "behavioral_recall",
    "When your boss seems stressed, how often do you wonder if it's because of YOUR work?",
    opts([
        ("Rarely — bosses have a million things going on", {"personalization": 1}),
        ("Only if I actually did something questionable recently", {"personalization": 2}),
        ("Often — I default to assuming I'm the cause", {"personalization": 4}),
        ("Always — my first instinct is to check what I did wrong", {"personalization": 5})
    ]),
    tier="triangulation", cg="per_blame_1", opacity=0.6))

questions.append(q("personalization", "scenario",
    "A stranger on the street gives you a dirty look. You think:",
    opts([
        ("They're having a bad day — nothing to do with me", {"personalization": 1}),
        ("Weird, but who cares", {"personalization": 1}),
        ("What did I do? Am I dressed weird? Do I look offensive somehow?", {"personalization": 4}),
        ("They clearly don't like something about me specifically", {"personalization": 5})
    ]),
    tier="triangulation", cg="per_blame_1", opacity=0.5))

questions.append(q("personalization", "trap",
    "People say you 'take too much responsibility for things.' You think:",
    opts([
        ("They're right — I need to let go of what isn't mine", {"personalization": 4}),
        ("Maybe — but someone has to be responsible", {"personalization": 3}),
        ("I only take responsibility for what IS my responsibility", {"personalization": 1}),
        ("Better to take too much than too little — at least I care", {"personalization": 5})
    ]),
    tier="trap", trap=True, cg="per_blame_1", opacity=0.6))

questions.append(q("personalization", "somatic",
    "You hear that a friend is going through a tough time. Before knowing any details, your body:",
    opts([
        ("Feels concern and sympathy", {"personalization": 1}),
        ("Feels a pang of 'is this something I could have prevented?'", {"personalization": 3}),
        ("Immediately scans for ways YOU might have caused or contributed to it", {"personalization": 5}),
        ("Knots with guilt even when you logically know it has nothing to do with you", {"personalization": 5})
    ]),
    tier="core", cg="per_blame_1", opacity=0.7))

questions.append(q("personalization", "partner_perspective",
    "When rain ruins an outdoor event you planned, you feel:",
    opts([
        ("Disappointed — but weather is weather", {"personalization": 1}),
        ("Frustrated — but no one's to blame", {"personalization": 2}),
        ("Like you should have planned better — this is on you for not having a backup", {"personalization": 4}),
        ("Like a failure — you let everyone down", {"personalization": 5})
    ]),
    tier="consistency_check", cg="per_blame_1", opacity=0.5))

# ============================================================
# EMOTIONAL_REASONING (12)
# ============================================================

questions.append(q("emotional_reasoning", "scenario",
    "You feel anxious about a flight tomorrow. You're aware there's no logical reason. But the anxiety makes you think:",
    opts([
        ("I'm just anxious — flights are statistically safe, the feeling will pass", {"emotional_reasoning": 1}),
        ("I don't love flying but I know the anxiety isn't evidence of danger", {"emotional_reasoning": 2}),
        ("Something bad is going to happen — I can FEEL it", {"emotional_reasoning": 5}),
        ("Maybe I should cancel — my gut is telling me something", {"emotional_reasoning": 5})
    ]),
    tier="core", cg="er_feelings_1", opacity=0.65))

questions.append(q("emotional_reasoning", "forced_choice",
    "Which is more true for you?",
    opts([
        ("My feelings are information, not facts — they need to be checked against reality", {"emotional_reasoning": 1}),
        ("If I feel it strongly enough, it must be true", {"emotional_reasoning": 5})
    ]),
    tier="core", cg="er_feelings_1", opacity=0.85))

questions.append(q("emotional_reasoning", "behavioral_recall",
    "How often do you use 'I feel like...' as proof that something is actually true?",
    opts([
        ("Rarely — I distinguish between feelings and facts", {"emotional_reasoning": 1}),
        ("Sometimes — emotions inform my thinking but don't dictate it", {"emotional_reasoning": 2}),
        ("Often — my feelings are my strongest evidence for what's real", {"emotional_reasoning": 4}),
        ("Almost always — if I feel it, it IS true", {"emotional_reasoning": 5})
    ]),
    tier="core", cg="er_feelings_1", opacity=0.7))

questions.append(q("emotional_reasoning", "scenario",
    "You feel guilty about missing a friend's event even though you had a valid reason. The guilt makes you believe:",
    opts([
        ("Nothing extra — guilt is a feeling, my reason was valid", {"emotional_reasoning": 1}),
        ("Maybe I could have tried harder — but the guilt is just guilt, not proof", {"emotional_reasoning": 2}),
        ("I AM a bad friend — the guilt proves it", {"emotional_reasoning": 5}),
        ("They probably hate me now — I can feel it", {"emotional_reasoning": 5})
    ]),
    tier="triangulation", cg="er_feelings_1", opacity=0.65))

questions.append(q("emotional_reasoning", "partner_perspective",
    "You feel unlovable today. Your partner has been loving and attentive. You believe:",
    opts([
        ("My partner loves me — my feelings today are just feelings, not reality", {"emotional_reasoning": 1}),
        ("My partner loves me but the feeling makes it hard to absorb today", {"emotional_reasoning": 2}),
        ("They can't really love the real me — the fact that I feel unlovable means I AM unlovable", {"emotional_reasoning": 5}),
        ("They're either fooling themselves or fooling me", {"emotional_reasoning": 5})
    ]),
    tier="core", cg="er_feelings_1", opacity=0.75))

questions.append(q("emotional_reasoning", "somatic",
    "When your emotions and the evidence contradict each other (you FEEL worthless but evidence shows you're competent), your body:",
    opts([
        ("Trusts the evidence — feelings are temporary, facts are facts", {"emotional_reasoning": 1}),
        ("Struggles briefly but ultimately follows the evidence", {"emotional_reasoning": 2}),
        ("Trusts the feeling — the evidence must be wrong or incomplete", {"emotional_reasoning": 5}),
        ("Can't resolve the contradiction — and the feeling always wins", {"emotional_reasoning": 5})
    ]),
    tier="core", cg="er_feelings_1", opacity=0.75))

questions.append(q("emotional_reasoning", "temporal",
    "Think about a time you felt certain something terrible was going to happen. Did it?",
    opts([
        ("Usually no — strong feelings aren't prophecy", {"emotional_reasoning": 1}),
        ("Sometimes — but more often than not, my certainty was wrong", {"emotional_reasoning": 3}),
        ("Doesn't matter — the feeling was real so my reaction was justified", {"emotional_reasoning": 5}),
        ("Yes — which proves my feelings are accurate predictors", {"emotional_reasoning": 5})
    ]),
    tier="trap", trap=True, cg="er_feelings_1", opacity=0.7))

questions.append(q("emotional_reasoning", "scenario",
    "You feel overwhelmed at work. Your actual workload is the same as last month when you felt fine. You conclude:",
    opts([
        ("Something else is affecting my capacity today — stress, sleep, personal stuff", {"emotional_reasoning": 1}),
        ("The feeling is real even if the workload hasn't changed — I need to figure out what's different", {"emotional_reasoning": 2}),
        ("The workload IS worse — the fact that I feel overwhelmed proves it", {"emotional_reasoning": 5}),
        ("I'm clearly not cut out for this job anymore", {"emotional_reasoning": 5})
    ]),
    tier="triangulation", cg="er_feelings_1", opacity=0.65))

questions.append(q("emotional_reasoning", "behavioral_recall",
    "How often do you make important decisions based primarily on how you feel in the moment?",
    opts([
        ("Rarely — I try to decide when I'm calm and have information", {"emotional_reasoning": 1}),
        ("Sometimes — but I check myself before acting on intense emotions", {"emotional_reasoning": 2}),
        ("Often — my feelings are my compass for big decisions", {"emotional_reasoning": 4}),
        ("Almost always — if it FEELS right, it IS right", {"emotional_reasoning": 5})
    ]),
    tier="consistency_check", cg="er_feelings_1", opacity=0.65))

questions.append(q("emotional_reasoning", "scenario",
    "You feel like your friend group doesn't like you despite them consistently inviting you to things. You:",
    opts([
        ("Trust the evidence — they invite me, they like me. The feeling is just insecurity talking.", {"emotional_reasoning": 1}),
        ("Acknowledge the feeling but don't act on it — invitations are data", {"emotional_reasoning": 2}),
        ("Trust the feeling — they probably invite me out of obligation", {"emotional_reasoning": 5}),
        ("Start declining invitations because the feeling of being unwanted is too painful", {"emotional_reasoning": 5})
    ]),
    tier="core", cg="er_feelings_1", opacity=0.65))

questions.append(q("emotional_reasoning", "partner_perspective",
    "When you feel jealous, you treat the jealousy as:",
    opts([
        ("An emotion to examine — what's triggering it? Is there real evidence of a threat?", {"emotional_reasoning": 1}),
        ("A signal to pay attention to, but not proof of anything", {"emotional_reasoning": 2}),
        ("Evidence that something IS wrong — jealousy means my partner is doing something suspicious", {"emotional_reasoning": 5}),
        ("Justification for controlling behavior — if I feel it, I have the right to act on it", {"emotional_reasoning": 5})
    ]),
    tier="triangulation", cg="er_feelings_1", opacity=0.7))

questions.append(q("emotional_reasoning", "forced_choice",
    "Finish this sentence: 'I feel stupid, therefore...'",
    opts([
        ("I'm having a bad day — feeling stupid doesn't make me stupid", {"emotional_reasoning": 1}),
        ("I probably AM stupid — why else would I feel this way?", {"emotional_reasoning": 5})
    ]),
    tier="consistency_check", cg="er_feelings_1", opacity=0.85))

# ============================================================
# SHOULD_STATEMENTS (12)
# ============================================================

questions.append(q("should_statements", "behavioral_recall",
    "How often do you use the words 'should,' 'must,' or 'have to' when thinking about yourself?",
    opts([
        ("Rarely — I think in terms of 'want,' 'choose,' and 'prefer'", {"should_statements": 1}),
        ("Sometimes — for genuinely important obligations", {"should_statements": 2}),
        ("Frequently — I have a long list of shoulds governing my behavior", {"should_statements": 4}),
        ("Constantly — my inner monologue is basically a list of commands", {"should_statements": 5})
    ]),
    tier="core", cg="ss_self_1", opacity=0.7))

questions.append(q("should_statements", "scenario",
    "It's Saturday and you've been productive all week. You sleep until noon. Your thought is:",
    opts([
        ("My body needed it — no judgment", {"should_statements": 1}),
        ("Lazy morning, nice treat", {"should_statements": 1}),
        ("I SHOULD have gotten up earlier — I'm wasting the day", {"should_statements": 4}),
        ("I'm disgusted with myself — a responsible person wouldn't sleep until noon", {"should_statements": 5})
    ]),
    tier="core", cg="ss_self_1", opacity=0.55))

questions.append(q("should_statements", "partner_perspective",
    "Your partner handles a situation differently than you would have. Your thought:",
    opts([
        ("Different approach, not wrong approach", {"should_statements": 1}),
        ("Interesting — I'd have done it differently but their way works too", {"should_statements": 2}),
        ("They SHOULD have done it the way I would have — that's the right way", {"should_statements": 4}),
        ("They always do things wrong — they should know better by now", {"should_statements": 5})
    ]),
    tier="core", cg="ss_others_1", opacity=0.65))

questions.append(q("should_statements", "forced_choice",
    "When you don't meet your own standards, you feel:",
    opts([
        ("Disappointed but self-compassionate — I'm human", {"should_statements": 1}),
        ("Guilty, frustrated, and angry at myself for failing to be who I SHOULD be", {"should_statements": 5})
    ]),
    tier="core", cg="ss_self_1", opacity=0.8))

questions.append(q("should_statements", "somatic",
    "When you catch yourself doing something 'unproductive' (watching TV midday, scrolling social media), your body:",
    opts([
        ("Relaxes — downtime is valuable", {"should_statements": 1}),
        ("Feels fine — you'll be productive when you're ready", {"should_statements": 2}),
        ("Tenses with guilt — you SHOULD be doing something useful", {"should_statements": 4}),
        ("Burns with shame — you're failing at basic adulting", {"should_statements": 5})
    ]),
    tier="triangulation", cg="ss_self_1", opacity=0.6))

questions.append(q("should_statements", "scenario",
    "A friend cancels plans because they're 'not feeling up to it.' Your thought:",
    opts([
        ("Totally valid — self-care is important", {"should_statements": 1}),
        ("Wish they'd told me sooner, but I understand", {"should_statements": 2}),
        ("They SHOULD honor their commitments — it's rude to cancel last minute", {"should_statements": 4}),
        ("They should feel terrible about this — a real friend would push through", {"should_statements": 5})
    ]),
    tier="core", cg="ss_others_1", opacity=0.6))

questions.append(q("should_statements", "behavioral_recall",
    "How rigid are your expectations for yourself and others?",
    opts([
        ("Flexible — I adjust expectations based on circumstances", {"should_statements": 1}),
        ("Firm but reasonable — standards matter but I'm not inflexible", {"should_statements": 2}),
        ("Quite rigid — I have clear rules about how things should be done and who people should be", {"should_statements": 4}),
        ("Extremely rigid — and I'm frustrated that the world doesn't operate the way it should", {"should_statements": 5})
    ]),
    tier="core", cg="ss_self_1", opacity=0.7))

questions.append(q("should_statements", "temporal",
    "Think about the rules you have for yourself (how you should look, behave, achieve). Where did they come from?",
    opts([
        ("I've consciously chosen values that work for me — they're mine", {"should_statements": 1}),
        ("A mix of chosen values and inherited expectations — I'm still sorting them out", {"should_statements": 3}),
        ("Mostly inherited — from parents, culture, religion — and I've never questioned them", {"should_statements": 4}),
        ("I have no idea where they came from but they RULE me", {"should_statements": 5})
    ]),
    tier="triangulation", cg="ss_self_1", opacity=0.7))

questions.append(q("should_statements", "trap",
    "Someone says 'You're too hard on yourself.' You think:",
    opts([
        ("Probably true — I could cut myself more slack", {"should_statements": 3}),
        ("If I'm not hard on myself, who will be? Standards exist for a reason.", {"should_statements": 5}),
        ("I'm exactly as hard on myself as I need to be", {"should_statements": 3}),
        ("They're right — and I should stop being so hard on myself (another should)", {"should_statements": 4})
    ]),
    tier="trap", trap=True, cg="ss_self_1", opacity=0.6))

questions.append(q("should_statements", "partner_perspective",
    "When people around you don't meet your expectations, your typical reaction is:",
    opts([
        ("Adjust expectations — people are who they are", {"should_statements": 1}),
        ("Mild frustration that passes quickly", {"should_statements": 2}),
        ("Resentment — why can't they just do what they SHOULD?", {"should_statements": 4}),
        ("Contempt — people who don't meet basic standards are failing at life", {"should_statements": 5})
    ]),
    tier="consistency_check", cg="ss_others_1", opacity=0.65))

questions.append(q("should_statements", "scenario",
    "You cry at a movie. Your inner voice says:",
    opts([
        ("That was a moving scene — I'm allowed to feel things", {"should_statements": 1}),
        ("Nothing — crying at movies is normal", {"should_statements": 1}),
        ("I shouldn't be this emotional — it's embarrassing", {"should_statements": 4}),
        ("What's wrong with me? Adults shouldn't cry at movies.", {"should_statements": 5})
    ]),
    tier="triangulation", cg="ss_self_1", opacity=0.55))

questions.append(q("should_statements", "behavioral_recall",
    "How much of your stress comes from the gap between how things ARE and how they SHOULD BE?",
    opts([
        ("Very little — I mostly deal with reality as it is", {"should_statements": 1}),
        ("Some — I have ideals but I'm realistic", {"should_statements": 2}),
        ("A lot — I'm constantly frustrated by the gap between expectation and reality", {"should_statements": 4}),
        ("Most of it — if the world would just be the way it SHOULD be, I'd be fine", {"should_statements": 5})
    ]),
    tier="core", cg="ss_self_1", opacity=0.7))

# ============================================================
# LABELING (11)
# ============================================================

questions.append(q("labeling", "scenario",
    "You make a mistake on a project. Your self-talk sounds like:",
    opts([
        ("'I made a mistake — let me fix it'", {"labeling": 1}),
        ("'That was careless of me — I'll be more careful'", {"labeling": 2}),
        ("'I'm an idiot'", {"labeling": 4}),
        ("'I'm a failure — this is just who I am'", {"labeling": 5})
    ]),
    tier="core", cg="lab_self_1", opacity=0.6))

questions.append(q("labeling", "behavioral_recall",
    "When you do something you're not proud of, how quickly does 'I did a bad thing' become 'I am a bad person'?",
    opts([
        ("It doesn't — my actions and my identity are separate", {"labeling": 1}),
        ("Rarely — only in extreme situations", {"labeling": 2}),
        ("Quickly — the jump from behavior to identity happens fast", {"labeling": 4}),
        ("Instantly — there's no gap between what I do and who I am", {"labeling": 5})
    ]),
    tier="core", cg="lab_self_1", opacity=0.75))

questions.append(q("labeling", "partner_perspective",
    "When your partner makes a mistake, how quickly do you label them? (e.g., 'You're so irresponsible' vs. 'That was irresponsible')",
    opts([
        ("I comment on the behavior, not the person", {"labeling": 1}),
        ("I usually stay behavior-focused but slip sometimes when frustrated", {"labeling": 2}),
        ("I often go straight to 'you ARE [label]' in my head, even if I don't say it", {"labeling": 4}),
        ("They have labels in my mind — lazy, careless, selfish — and events confirm them", {"labeling": 5})
    ]),
    tier="core", cg="lab_others_1", opacity=0.7))

questions.append(q("labeling", "forced_choice",
    "When someone cuts you off in traffic, you think:",
    opts([
        ("'That was dangerous driving'", {"labeling": 1}),
        ("'What a jerk/idiot'", {"labeling": 5})
    ]),
    tier="triangulation", cg="lab_others_1", opacity=0.6))

questions.append(q("labeling", "scenario",
    "You forget an important date (anniversary, friend's birthday). Your self-talk:",
    opts([
        ("'I forgot — let me make it right'", {"labeling": 1}),
        ("'I should have set a reminder — my bad'", {"labeling": 2}),
        ("'I'm terrible — I'm the WORST partner/friend'", {"labeling": 5}),
        ("'This is just who I am — unreliable, thoughtless'", {"labeling": 5})
    ]),
    tier="triangulation", cg="lab_self_1", opacity=0.6))

questions.append(q("labeling", "somatic",
    "When you fail at something, does the label ('loser,' 'failure,' 'fraud') attach to you physically — like you can feel it in your body?",
    opts([
        ("No — I might be disappointed but I don't take on labels", {"labeling": 1}),
        ("Briefly — a flash of self-labeling that I can dismiss", {"labeling": 2}),
        ("Yes — the label settles in and colors my whole sense of self", {"labeling": 4}),
        ("Yes — it becomes my identity until something good happens to shake it", {"labeling": 5})
    ]),
    tier="core", cg="lab_self_1", opacity=0.75))

questions.append(q("labeling", "temporal",
    "How many fixed labels do you carry about yourself? (e.g., 'I'm lazy,' 'I'm not creative,' 'I'm bad with money')",
    opts([
        ("None — I describe myself in terms of behaviors and tendencies, not labels", {"labeling": 1}),
        ("A few — but I know they're oversimplifications", {"labeling": 2}),
        ("Several — and they feel pretty accurate", {"labeling": 4}),
        ("Many — they're basically my identity", {"labeling": 5})
    ]),
    tier="core", cg="lab_self_1", opacity=0.7))

questions.append(q("labeling", "behavioral_recall",
    "How often do you describe other people using absolute labels ('she's toxic,' 'he's a narcissist,' 'they're useless')?",
    opts([
        ("Rarely — people are complex, labels are reductive", {"labeling": 1}),
        ("Sometimes — when patterns are really clear", {"labeling": 2}),
        ("Often — it helps me understand people", {"labeling": 4}),
        ("Constantly — most people fit neatly into categories", {"labeling": 5})
    ]),
    tier="triangulation", cg="lab_others_1", opacity=0.6))

questions.append(q("labeling", "trap",
    "You pride yourself on being a good judge of character — you can label someone accurately within minutes. How well does this serve you?",
    opts([
        ("I don't do this — snap judgments are usually wrong", {"labeling": 1}),
        ("I form initial impressions but hold them loosely", {"labeling": 2}),
        ("Well — I'm usually right about people", {"labeling": 4}),
        ("Perfectly — and when someone proves my label right, it confirms my skill at reading people", {"labeling": 5})
    ]),
    tier="trap", trap=True, cg="lab_others_1", opacity=0.65))

questions.append(q("labeling", "partner_perspective",
    "In arguments, do you find yourself saying 'you always...' or 'you never...' or 'you're so [label]'?",
    opts([
        ("Rarely — I try to stick to specific situations", {"labeling": 1}),
        ("Sometimes — especially when frustrated", {"labeling": 3}),
        ("Often — those phrases come out automatically", {"labeling": 4}),
        ("Every argument — because those labels are TRUE", {"labeling": 5})
    ]),
    tier="consistency_check", cg="lab_others_1", opacity=0.6))

questions.append(q("labeling", "scenario",
    "Someone you labeled as 'selfish' does something genuinely generous. You think:",
    opts([
        ("Maybe I was wrong — people are more complex than my labels", {"labeling": 1}),
        ("Interesting — let me update my view of them", {"labeling": 2}),
        ("It's an exception — they're still fundamentally selfish", {"labeling": 4}),
        ("They must have an ulterior motive — selfish people don't do generous things for real", {"labeling": 5})
    ]),
    tier="triangulation", cg="lab_others_1", opacity=0.65))

# ============================================================
# MAGNIFICATION (11)
# ============================================================

questions.append(q("magnification", "scenario",
    "You get feedback on a project: 9 positives and 1 negative. Where does your attention go?",
    opts([
        ("The overall picture — mostly positive, with one area to improve", {"magnification": 1}),
        ("Mostly the positives, with a note to address the negative", {"magnification": 2}),
        ("Straight to the negative — what did they say was wrong?", {"magnification": 4}),
        ("The negative ONLY — the 9 positives must have been generic", {"magnification": 5})
    ]),
    tier="core", cg="mag_negative_1", opacity=0.6))

questions.append(q("magnification", "behavioral_recall",
    "When you compare yourself to others, do you magnify their strengths and your weaknesses?",
    opts([
        ("No — I can see both accurately", {"magnification": 1}),
        ("Occasionally — social media doesn't help", {"magnification": 2}),
        ("Regularly — other people's highlight reels look like everyday life, mine looks like bloopers", {"magnification": 4}),
        ("Always — everyone is better than me at everything that matters", {"magnification": 5})
    ]),
    tier="core", cg="mag_comparison_1", opacity=0.65))

questions.append(q("magnification", "partner_perspective",
    "Your partner has a small flaw. In your mind, how big is it?",
    opts([
        ("Proportional — a small flaw in a complex person", {"magnification": 1}),
        ("It stands out sometimes but I keep perspective", {"magnification": 2}),
        ("It's bigger than it should be in my mind — it overshadows their good qualities", {"magnification": 4}),
        ("It's all I can see some days", {"magnification": 5})
    ]),
    tier="triangulation", cg="mag_negative_1", opacity=0.65))

questions.append(q("magnification", "forced_choice",
    "When something good and something bad happen on the same day, which gets bigger in your mind?",
    opts([
        ("They stay proportional — I can hold both", {"magnification": 1}),
        ("The bad thing grows and the good thing shrinks", {"magnification": 5})
    ]),
    tier="core", cg="mag_negative_1", opacity=0.8))

questions.append(q("magnification", "somatic",
    "When you make a mistake in front of others, the embarrassment feels:",
    opts([
        ("Proportional to the actual mistake — minor error, minor discomfort", {"magnification": 1}),
        ("A bit amplified but manageable", {"magnification": 2}),
        ("Enormous — like everyone noticed and it was catastrophic", {"magnification": 4}),
        ("Like the defining moment of the day/week — it eclipses everything else", {"magnification": 5})
    ]),
    tier="core", cg="mag_negative_1", opacity=0.65))

questions.append(q("magnification", "scenario",
    "You give a presentation. 50 people loved it, 2 people left early. You replay in your mind:",
    opts([
        ("The 50 who stayed — great reception", {"magnification": 1}),
        ("Mostly positive, but curious why 2 left", {"magnification": 2}),
        ("The 2 who left — what went wrong?", {"magnification": 4}),
        ("Only the 2 who left — the presentation was clearly a failure", {"magnification": 5})
    ]),
    tier="triangulation", cg="mag_negative_1", opacity=0.55))

questions.append(q("magnification", "temporal",
    "Looking back at your accomplishments, do they seem as big in retrospect as they were in the moment?",
    opts([
        ("Yes — I can recognize and hold onto my achievements", {"magnification": 1}),
        ("They shrink a little but I know they were real", {"magnification": 2}),
        ("They shrink a lot — my failures stay vivid while my successes fade", {"magnification": 4}),
        ("My achievements feel like flukes while my failures feel like the truth", {"magnification": 5})
    ]),
    tier="core", cg="mag_comparison_1", opacity=0.7))

questions.append(q("magnification", "behavioral_recall",
    "When someone compliments you and someone criticizes you on the same day, which sticks?",
    opts([
        ("Both — I can hold positive and negative feedback equally", {"magnification": 1}),
        ("The compliment sticks more — I'm in a good headspace", {"magnification": 1}),
        ("The criticism — it's louder, stickier, more real", {"magnification": 4}),
        ("Only the criticism — compliments slide off, criticism embeds", {"magnification": 5})
    ]),
    tier="consistency_check", cg="mag_negative_1", opacity=0.65))

questions.append(q("magnification", "trap",
    "Your tendency to focus on negatives is something you see as:",
    opts([
        ("A cognitive bias I work to counteract", {"magnification": 2}),
        ("Realism — bad things DO matter more than good things", {"magnification": 5}),
        ("I don't have this tendency — I see things pretty clearly", {"magnification": 1}),
        ("Self-protective — if I focus on what's wrong, I can fix it", {"magnification": 4})
    ]),
    tier="trap", trap=True, cg="mag_negative_1", opacity=0.65))

questions.append(q("magnification", "scenario",
    "You look in the mirror. You notice one thing you don't like about your appearance. How much of the mirror does it fill?",
    opts([
        ("Its actual size — one thing among many", {"magnification": 1}),
        ("Slightly bigger than it should but I can zoom out", {"magnification": 2}),
        ("Most of what I see — the flaw dominates", {"magnification": 4}),
        ("Everything — I can't see anything else", {"magnification": 5})
    ]),
    tier="triangulation", cg="mag_comparison_1", opacity=0.6))

questions.append(q("magnification", "partner_perspective",
    "When your partner praises something you did, does the praise feel as real as their criticism would?",
    opts([
        ("Yes — I accept positive feedback as readily as negative", {"magnification": 1}),
        ("Almost — praise is slightly harder to absorb", {"magnification": 2}),
        ("No — criticism feels true while praise feels like politeness", {"magnification": 4}),
        ("Praise bounces off, criticism penetrates — they're not even in the same category", {"magnification": 5})
    ]),
    tier="core", cg="mag_comparison_1", opacity=0.7))

# ============================================================
# FORTUNE_TELLING (11)
# ============================================================

questions.append(q("fortune_telling", "scenario",
    "You have a job interview tomorrow. Without any information, you predict:",
    opts([
        ("I'll give it my best and see what happens", {"fortune_telling": 1}),
        ("I have a decent shot — I'll prepare and hope for the best", {"fortune_telling": 2}),
        ("I'm probably not going to get it — why get my hopes up?", {"fortune_telling": 4}),
        ("There's no point going — they'll pick someone else, they always do", {"fortune_telling": 5})
    ]),
    tier="core", cg="ft_prediction_1", opacity=0.6))

questions.append(q("fortune_telling", "behavioral_recall",
    "How often do you predict negative outcomes before events happen — and then treat your prediction as certain?",
    opts([
        ("Rarely — I try not to prejudge outcomes", {"fortune_telling": 1}),
        ("Sometimes — but I hold predictions loosely", {"fortune_telling": 2}),
        ("Often — and the prediction colors the entire experience", {"fortune_telling": 4}),
        ("Constantly — and I'm already preparing for the fallout of things that haven't happened yet", {"fortune_telling": 5})
    ]),
    tier="core", cg="ft_prediction_1", opacity=0.7))

questions.append(q("fortune_telling", "partner_perspective",
    "Your partner suggests trying couples counseling. You immediately think:",
    opts([
        ("This could really help us — I'm open to it", {"fortune_telling": 1}),
        ("Worth a try — nothing to lose", {"fortune_telling": 2}),
        ("It won't work — I already know how this will go", {"fortune_telling": 4}),
        ("We're doomed — the fact that we need counseling means it's already too late", {"fortune_telling": 5})
    ]),
    tier="triangulation", cg="ft_prediction_1", opacity=0.65))

questions.append(q("fortune_telling", "forced_choice",
    "Before trying something new, you tend to:",
    opts([
        ("Be optimistic or neutral — new things are possibilities", {"fortune_telling": 1}),
        ("Pre-decide it will fail — at least you won't be disappointed", {"fortune_telling": 5})
    ]),
    tier="core", cg="ft_prediction_1", opacity=0.8))

questions.append(q("fortune_telling", "scenario",
    "You sent an important email and haven't heard back in 48 hours. You think:",
    opts([
        ("People are busy — I'll follow up if I don't hear by next week", {"fortune_telling": 1}),
        ("Probably in their queue — give it time", {"fortune_telling": 2}),
        ("They're not going to respond — they've already decided no", {"fortune_telling": 4}),
        ("It's over — they probably read it and laughed", {"fortune_telling": 5})
    ]),
    tier="triangulation", cg="ft_prediction_1", opacity=0.55))

questions.append(q("fortune_telling", "somatic",
    "When you think about an upcoming event you're nervous about, your body:",
    opts([
        ("Feels anticipation — normal pre-event energy", {"fortune_telling": 1}),
        ("Feels nervous but manageable", {"fortune_telling": 2}),
        ("Feels dread — as if the bad outcome has already happened", {"fortune_telling": 4}),
        ("Is already processing grief for a failure that hasn't occurred", {"fortune_telling": 5})
    ]),
    tier="core", cg="ft_prediction_1", opacity=0.7))

questions.append(q("fortune_telling", "behavioral_recall",
    "How many things have you not tried because you 'already knew' how they'd turn out?",
    opts([
        ("Very few — I give most things a chance", {"fortune_telling": 1}),
        ("A handful — when the odds were genuinely bad", {"fortune_telling": 2}),
        ("More than I should — my predictions have limited my life", {"fortune_telling": 4}),
        ("Countless — negative predictions have stopped me from trying most new things", {"fortune_telling": 5})
    ]),
    tier="core", cg="ft_prediction_1", opacity=0.7))

questions.append(q("fortune_telling", "temporal",
    "Think about 3 predictions you made about bad outcomes. How many were accurate?",
    opts([
        ("Fewer than I expected — my predictions are often wrong", {"fortune_telling": 3}),
        ("Maybe one — things usually turn out better than I predict", {"fortune_telling": 2}),
        ("I don't make many negative predictions to begin with", {"fortune_telling": 1}),
        ("Most of them — which proves my predictions are reliable", {"fortune_telling": 5})
    ]),
    tier="trap", trap=True, cg="ft_prediction_1", opacity=0.65))

questions.append(q("fortune_telling", "scenario",
    "A relationship starts going really well. Your thought is:",
    opts([
        ("This is great — let me enjoy it", {"fortune_telling": 1}),
        ("Cautiously optimistic — too early to predict anything", {"fortune_telling": 2}),
        ("It'll end badly — they all do", {"fortune_telling": 4}),
        ("I'm already bracing for the inevitable disappointment", {"fortune_telling": 5})
    ]),
    tier="triangulation", cg="ft_prediction_1", opacity=0.65))

questions.append(q("fortune_telling", "partner_perspective",
    "When making plans for the future (trips, goals, milestones), how confident are you that they'll actually happen?",
    opts([
        ("Reasonably confident — most plans work out in some form", {"fortune_telling": 1}),
        ("Somewhat — I plan but hold plans loosely", {"fortune_telling": 2}),
        ("Low confidence — something will probably go wrong", {"fortune_telling": 4}),
        ("I avoid planning because plans always fall apart", {"fortune_telling": 5})
    ]),
    tier="consistency_check", cg="ft_prediction_1", opacity=0.65))

questions.append(q("fortune_telling", "forced_choice",
    "Your approach to hope is:",
    opts([
        ("I hope for the best and prepare for challenges — that's realistic optimism", {"fortune_telling": 1}),
        ("I expect the worst so I'm pleasantly surprised if it goes well — that's self-protection", {"fortune_telling": 5})
    ]),
    tier="core", cg="ft_prediction_1", opacity=0.8))

# ============================================================
# OVERGENERALIZATION (12)
# ============================================================

questions.append(q("overgeneralization", "scenario",
    "You go on a bad first date. Your conclusion:",
    opts([
        ("Not a match — next", {"overgeneralization": 1}),
        ("That was rough, but first dates are always a gamble", {"overgeneralization": 2}),
        ("Dating is terrible — it's always like this", {"overgeneralization": 4}),
        ("I'll never find someone — this is proof that I'm undateable", {"overgeneralization": 5})
    ]),
    tier="core", cg="og_pattern_1", opacity=0.6))

questions.append(q("overgeneralization", "behavioral_recall",
    "How often do you use the words 'always' or 'never' when describing what happens to you?",
    opts([
        ("Rarely — those words are almost never accurate", {"overgeneralization": 1}),
        ("Sometimes — for emphasis, but I know it's an exaggeration", {"overgeneralization": 2}),
        ("Often — because things really DO always go wrong / never work out", {"overgeneralization": 4}),
        ("Constantly — my life is a pattern of things never working", {"overgeneralization": 5})
    ]),
    tier="core", cg="og_pattern_1", opacity=0.65))

questions.append(q("overgeneralization", "scenario",
    "You got rejected from one job application. Your thought process:",
    opts([
        ("This one didn't work — on to the next", {"overgeneralization": 1}),
        ("Disappointing, but the right fit is still out there", {"overgeneralization": 2}),
        ("Nobody wants to hire me", {"overgeneralization": 4}),
        ("I'll never get a good job — this always happens", {"overgeneralization": 5})
    ]),
    tier="triangulation", cg="og_pattern_1", opacity=0.55))

questions.append(q("overgeneralization", "forced_choice",
    "One bad experience in a new activity means:",
    opts([
        ("That activity didn't go well this time — might be different next time", {"overgeneralization": 1}),
        ("I'm not good at that activity and never will be", {"overgeneralization": 5})
    ]),
    tier="core", cg="og_pattern_1", opacity=0.8))

questions.append(q("overgeneralization", "partner_perspective",
    "Your partner disappoints you once. You catch yourself thinking:",
    opts([
        ("That was disappointing — let's address this specific thing", {"overgeneralization": 1}),
        ("This stings, but it's one event in a larger relationship", {"overgeneralization": 2}),
        ("They ALWAYS let me down", {"overgeneralization": 4}),
        ("This is what people do — everyone always disappoints you eventually", {"overgeneralization": 5})
    ]),
    tier="core", cg="og_pattern_1", opacity=0.65))

questions.append(q("overgeneralization", "somatic",
    "When one thing goes wrong, does your body react as if EVERYTHING is going wrong?",
    opts([
        ("No — one problem stays one problem", {"overgeneralization": 1}),
        ("Occasionally — stress can make things feel bigger", {"overgeneralization": 2}),
        ("Often — one domino falling feels like the whole row", {"overgeneralization": 4}),
        ("Always — a single failure proves that everything is falling apart", {"overgeneralization": 5})
    ]),
    tier="triangulation", cg="og_pattern_1", opacity=0.7))

questions.append(q("overgeneralization", "temporal",
    "Think about the last time something went wrong. How broad was the conclusion you drew?",
    opts([
        ("Narrow — I addressed the specific issue", {"overgeneralization": 1}),
        ("Somewhat broader than warranted — but I caught it", {"overgeneralization": 2}),
        ("Way too broad — one failure became a statement about my entire life/ability/worth", {"overgeneralization": 5}),
        ("Total — it confirmed everything I already believe about how things go for me", {"overgeneralization": 5})
    ]),
    tier="core", cg="og_pattern_1", opacity=0.65))

questions.append(q("overgeneralization", "behavioral_recall",
    "How many 'I always' or 'I never' beliefs do you hold about yourself? (e.g., 'I always screw things up,' 'I never get what I want')",
    opts([
        ("None — those statements are too absolute to be true", {"overgeneralization": 1}),
        ("One or two — and I know they're exaggerations", {"overgeneralization": 2}),
        ("Several — and they feel pretty accurate", {"overgeneralization": 4}),
        ("Many — they're basically the soundtrack of my life", {"overgeneralization": 5})
    ]),
    tier="consistency_check", cg="og_pattern_1", opacity=0.65))

questions.append(q("overgeneralization", "scenario",
    "Your new neighbor is unfriendly. Your thought:",
    opts([
        ("Some people are private — nothing personal", {"overgeneralization": 1}),
        ("Not ideal but I'll give them time", {"overgeneralization": 2}),
        ("People in this neighborhood are cold", {"overgeneralization": 4}),
        ("Nobody ever likes me — even neighbors", {"overgeneralization": 5})
    ]),
    tier="triangulation", cg="og_pattern_1", opacity=0.5))

questions.append(q("overgeneralization", "trap",
    "You notice that bad things seem to happen to you more than to other people. A friend says 'that's not actually true — you just remember the bad things more.' You think:",
    opts([
        ("They might be right — I do focus on negative experiences", {"overgeneralization": 2}),
        ("They have a point but some patterns ARE real", {"overgeneralization": 3}),
        ("They're wrong — my life genuinely has more bad luck than most", {"overgeneralization": 5}),
        ("They don't understand — I've seen the pattern, it's undeniable", {"overgeneralization": 5})
    ]),
    tier="trap", trap=True, cg="og_pattern_1", opacity=0.65))

questions.append(q("overgeneralization", "partner_perspective",
    "After one awkward social situation, you conclude:",
    opts([
        ("That was awkward — next one will probably be fine", {"overgeneralization": 1}),
        ("I felt off today but I'm usually fine socially", {"overgeneralization": 2}),
        ("I'm bad at social situations", {"overgeneralization": 4}),
        ("I'll never be good with people — this proves it", {"overgeneralization": 5})
    ]),
    tier="triangulation", cg="og_pattern_1", opacity=0.6))

questions.append(q("overgeneralization", "forced_choice",
    "One failure means:",
    opts([
        ("I failed at this one thing", {"overgeneralization": 1}),
        ("I'm a failure in general", {"overgeneralization": 5})
    ]),
    tier="consistency_check", cg="og_pattern_1", opacity=0.85))

# ============================================================
# REMAINING DIMENSIONS (mental_filter, disqualifying_positive, jumping_to_conclusions, blaming, fallacy_of_fairness, fallacy_of_change, heaven_reward_fallacy)
# 7 dimensions x ~12 = 84 questions, but we need only what gets us to 200 total
# Currently at: 12+12+12+12+12+12+12+11+11+11+12 = 129
# Need 71 more across 7 dimensions ≈ ~10 each
# ============================================================

# MENTAL_FILTER (10)
questions.append(q("mental_filter", "scenario",
    "You host a dinner party. Everyone has a great time except one person who seems bored. You remember:",
    opts([
        ("A wonderful evening with friends", {"mental_filter": 1}),
        ("Great night, with a minor note about the bored person", {"mental_filter": 2}),
        ("The bored person — their discomfort overshadows everything else", {"mental_filter": 4}),
        ("Only the bored person — the entire party was ruined", {"mental_filter": 5})
    ]),
    tier="core", cg="mf_negative_1", opacity=0.6))

questions.append(q("mental_filter", "behavioral_recall",
    "After a performance review that's mostly positive with one area for improvement, what do you think about most over the next week?",
    opts([
        ("The positive feedback — validation of my hard work", {"mental_filter": 1}),
        ("A balanced picture — good stuff and the area to work on", {"mental_filter": 2}),
        ("Almost exclusively the negative — it replays on loop", {"mental_filter": 5}),
        ("The negative item AND new worries it spawns about my job security", {"mental_filter": 5})
    ]),
    tier="core", cg="mf_negative_1", opacity=0.65))

questions.append(q("mental_filter", "partner_perspective",
    "Your partner takes you on a wonderful vacation but one day is rained out. Your memory of the trip:",
    opts([
        ("Mostly wonderful — the rain day was just a blip", {"mental_filter": 1}),
        ("Positive overall, with a 'too bad about that rainy day' footnote", {"mental_filter": 2}),
        ("Colored by the rain day — it's the part you keep mentioning", {"mental_filter": 4}),
        ("Dominated by the rain day — it ruined the whole trip in your memory", {"mental_filter": 5})
    ]),
    tier="triangulation", cg="mf_negative_1", opacity=0.55))

questions.append(q("mental_filter", "forced_choice",
    "At the end of a day with 10 good things and 1 bad thing, your mind settles on:",
    opts([
        ("The overall good day — the bad thing is just one data point", {"mental_filter": 1}),
        ("The one bad thing — it filters out everything else", {"mental_filter": 5})
    ]),
    tier="core", cg="mf_negative_1", opacity=0.8))

questions.append(q("mental_filter", "somatic",
    "Someone gives you feedback that's 90% praise and 10% criticism. Hours later, your body is carrying:",
    opts([
        ("A warm glow from the praise", {"mental_filter": 1}),
        ("A mix — both the praise and the criticism", {"mental_filter": 2}),
        ("Mostly the criticism — the praise has faded", {"mental_filter": 4}),
        ("Only the criticism — as if the praise never happened", {"mental_filter": 5})
    ]),
    tier="core", cg="mf_negative_1", opacity=0.7))

questions.append(q("mental_filter", "scenario",
    "You give a speech. 200 people clap, 1 person sits on their phone. You find your eyes drawn to:",
    opts([
        ("The 200 who are engaged — incredible turnout", {"mental_filter": 1}),
        ("Mostly the crowd, with occasional glances at the phone person", {"mental_filter": 2}),
        ("The phone person — why aren't they paying attention?", {"mental_filter": 4}),
        ("ONLY the phone person — they're the only real feedback", {"mental_filter": 5})
    ]),
    tier="triangulation", cg="mf_negative_1", opacity=0.55))

questions.append(q("mental_filter", "temporal",
    "Think about the past year. What comes to mind first — the highlights or the lowlights?",
    opts([
        ("Highlights — I naturally lean toward remembering good things", {"mental_filter": 1}),
        ("A mix of both in roughly accurate proportion", {"mental_filter": 2}),
        ("Lowlights first — I have to actively try to remember the good stuff", {"mental_filter": 4}),
        ("Almost exclusively lowlights — the good parts have been filtered out of memory", {"mental_filter": 5})
    ]),
    tier="consistency_check", cg="mf_negative_1", opacity=0.65))

questions.append(q("mental_filter", "behavioral_recall",
    "When you scroll through photos from an event, do you focus on the ones where you look good or the ones where you don't?",
    opts([
        ("The good ones — those are the memories I want", {"mental_filter": 1}),
        ("Both — I enjoy the good ones and cringe at the bad ones", {"mental_filter": 2}),
        ("The bad ones — I can't stop looking at them", {"mental_filter": 4}),
        ("I delete the bad ones immediately and they still haunt me", {"mental_filter": 5})
    ]),
    tier="triangulation", cg="mf_negative_1", opacity=0.5))

questions.append(q("mental_filter", "trap",
    "You see your mental focus on negatives as:",
    opts([
        ("A bias I actively work to counteract", {"mental_filter": 2}),
        ("I don't have this problem", {"mental_filter": 1}),
        ("Realistic — bad things deserve more attention because they need fixing", {"mental_filter": 4}),
        ("Protective — if I focus on threats, I can prepare for them", {"mental_filter": 5})
    ]),
    tier="trap", trap=True, cg="mf_negative_1", opacity=0.65))

questions.append(q("mental_filter", "partner_perspective",
    "Your partner does 10 kind things this week and one thoughtless thing. In your mind, the week was:",
    opts([
        ("Wonderful — they were so thoughtful", {"mental_filter": 1}),
        ("Good overall, with one thing to mention", {"mental_filter": 2}),
        ("Defined by the thoughtless thing — it overshadows the rest", {"mental_filter": 4}),
        ("Evidence that the thoughtless thing is the 'real' them", {"mental_filter": 5})
    ]),
    tier="core", cg="mf_negative_1", opacity=0.65))

# DISQUALIFYING_POSITIVE (10)
questions.append(q("disqualifying_positive", "scenario",
    "Someone gives you a genuine compliment. Your internal response:",
    opts([
        ("Accept it — 'thank you, I appreciate that'", {"disqualifying_positive": 1}),
        ("Appreciate it while being slightly awkward", {"disqualifying_positive": 2}),
        ("Dismiss it — 'they're just being nice'", {"disqualifying_positive": 4}),
        ("Argue against it — 'no, I'm really not that good at it'", {"disqualifying_positive": 5})
    ]),
    tier="core", cg="dp_deflection_1", opacity=0.55))

questions.append(q("disqualifying_positive", "behavioral_recall",
    "When you succeed at something, how often do you attribute it to luck rather than ability?",
    opts([
        ("Rarely — I can own my successes", {"disqualifying_positive": 1}),
        ("Sometimes — when the success involved some fortune", {"disqualifying_positive": 2}),
        ("Often — I got lucky, anyone could have done it", {"disqualifying_positive": 4}),
        ("Always — every success is either luck, low standards, or people being nice", {"disqualifying_positive": 5})
    ]),
    tier="core", cg="dp_deflection_1", opacity=0.65,
    tags=["cognitive_distortions", "disqualifying_positive"]))

questions.append(q("disqualifying_positive", "partner_perspective",
    "Your partner says 'You're the best thing that ever happened to me.' You think:",
    opts([
        ("That's incredibly sweet — I feel the same way about them", {"disqualifying_positive": 1}),
        ("Wow — I hope I can live up to that", {"disqualifying_positive": 2}),
        ("They don't know the real me — if they did, they wouldn't say that", {"disqualifying_positive": 5}),
        ("They're delusional or settling — I'm not that special", {"disqualifying_positive": 5})
    ]),
    tier="core", cg="dp_deflection_1", opacity=0.7))

questions.append(q("disqualifying_positive", "forced_choice",
    "When evidence contradicts your negative self-view, you:",
    opts([
        ("Update your self-view — evidence matters", {"disqualifying_positive": 1}),
        ("Explain the evidence away — it must be a fluke, exception, or mistake", {"disqualifying_positive": 5})
    ]),
    tier="core", cg="dp_deflection_1", opacity=0.85))

questions.append(q("disqualifying_positive", "scenario",
    "You get promoted. Your first thought:",
    opts([
        ("I earned this — my work speaks for itself", {"disqualifying_positive": 1}),
        ("Great recognition — I'll keep proving they made the right choice", {"disqualifying_positive": 2}),
        ("They must have been desperate — or just being political", {"disqualifying_positive": 5}),
        ("Now they'll find out I'm not actually qualified", {"disqualifying_positive": 5})
    ]),
    tier="triangulation", cg="dp_deflection_1", opacity=0.6))

questions.append(q("disqualifying_positive", "somatic",
    "When you receive praise, does your body let it in?",
    opts([
        ("Yes — praise warms me and I can sit with it", {"disqualifying_positive": 1}),
        ("Mostly — with a small reflex to deflect", {"disqualifying_positive": 2}),
        ("No — it bounces off, like my body has a shield against positive information", {"disqualifying_positive": 5}),
        ("It triggers anxiety — being seen positively means people have expectations I can't meet", {"disqualifying_positive": 5})
    ]),
    tier="core", cg="dp_deflection_1", opacity=0.75))

questions.append(q("disqualifying_positive", "temporal",
    "Think about the last 5 good things that happened to you. How many do you attribute to YOUR ability vs. external factors?",
    opts([
        ("Most were earned through my effort and skill", {"disqualifying_positive": 1}),
        ("A mix — some earned, some lucky", {"disqualifying_positive": 2}),
        ("Mostly luck, timing, or other people's generosity", {"disqualifying_positive": 4}),
        ("All external — nothing good happens because of ME", {"disqualifying_positive": 5})
    ]),
    tier="triangulation", cg="dp_deflection_1", opacity=0.65))

questions.append(q("disqualifying_positive", "trap",
    "A friend says 'You always downplay your accomplishments.' You think:",
    opts([
        ("They're right — I should own my wins more", {"disqualifying_positive": 3}),
        ("I'm just being modest — that's a virtue", {"disqualifying_positive": 3}),
        ("They don't understand — my accomplishments really AREN'T that impressive", {"disqualifying_positive": 5}),
        ("I don't downplay them — I describe them accurately. Other people just inflate things.", {"disqualifying_positive": 4})
    ]),
    tier="trap", trap=True, cg="dp_deflection_1", opacity=0.6))

questions.append(q("disqualifying_positive", "behavioral_recall",
    "When someone thanks you for something you did, you typically respond with:",
    opts([
        ("'You're welcome — happy to help'", {"disqualifying_positive": 1}),
        ("'No problem' — and you mean it", {"disqualifying_positive": 2}),
        ("'Oh, it was nothing' — minimizing what you did", {"disqualifying_positive": 4}),
        ("'Anyone would have done that' — erasing your specific contribution", {"disqualifying_positive": 5})
    ]),
    tier="consistency_check", cg="dp_deflection_1", opacity=0.5))

questions.append(q("disqualifying_positive", "scenario",
    "You look at your resume or list of life accomplishments. You feel:",
    opts([
        ("Proud — I've done real things", {"disqualifying_positive": 1}),
        ("Decent about some things, less so about others", {"disqualifying_positive": 2}),
        ("Like an imposter — none of it sounds like the real me", {"disqualifying_positive": 5}),
        ("Nothing — the list feels hollow, like it describes someone else", {"disqualifying_positive": 5})
    ]),
    tier="triangulation", cg="dp_deflection_1", opacity=0.65))

# JUMPING_TO_CONCLUSIONS (10)
questions.append(q("jumping_to_conclusions", "scenario",
    "Your best friend hasn't called in a week. You conclude:",
    opts([
        ("They're busy — no deeper meaning", {"jumping_to_conclusions": 1}),
        ("I should check in — they might need something", {"jumping_to_conclusions": 2}),
        ("They're pulling away — something has changed", {"jumping_to_conclusions": 4}),
        ("The friendship is over — they've moved on without me", {"jumping_to_conclusions": 5})
    ]),
    tier="core", cg="jtc_leap_1", opacity=0.6))

questions.append(q("jumping_to_conclusions", "behavioral_recall",
    "How often do you reach a firm conclusion about a situation before having all the facts?",
    opts([
        ("Rarely — I wait for information before concluding", {"jumping_to_conclusions": 1}),
        ("Sometimes — but I hold conclusions loosely until confirmed", {"jumping_to_conclusions": 2}),
        ("Often — my first conclusion becomes my only conclusion", {"jumping_to_conclusions": 4}),
        ("Constantly — I decide what something means instantly and rarely revise", {"jumping_to_conclusions": 5})
    ]),
    tier="core", cg="jtc_leap_1", opacity=0.7))

questions.append(q("jumping_to_conclusions", "partner_perspective",
    "Your partner seems distant at dinner. Without asking, you've already decided:",
    opts([
        ("Nothing — I'll ask if something's on their mind", {"jumping_to_conclusions": 1}),
        ("They might be tired — I'll see how the evening goes", {"jumping_to_conclusions": 2}),
        ("They're unhappy with ME — I'm scanning my behavior for what I did wrong", {"jumping_to_conclusions": 4}),
        ("They want to break up — this distance is the beginning of the end", {"jumping_to_conclusions": 5})
    ]),
    tier="triangulation", cg="jtc_leap_1", opacity=0.65))

questions.append(q("jumping_to_conclusions", "forced_choice",
    "When you don't have enough information, you tend to:",
    opts([
        ("Wait for more — ambiguity is uncomfortable but manageable", {"jumping_to_conclusions": 1}),
        ("Fill in the blanks with assumptions — usually negative ones", {"jumping_to_conclusions": 5})
    ]),
    tier="core", cg="jtc_leap_1", opacity=0.8))

questions.append(q("jumping_to_conclusions", "scenario",
    "You hear laughter from the next room right after you left it. You think:",
    opts([
        ("Someone told a joke — not about me", {"jumping_to_conclusions": 1}),
        ("Could be about anything — I don't connect it to myself", {"jumping_to_conclusions": 1}),
        ("They're laughing at me — at something I said or did", {"jumping_to_conclusions": 5}),
        ("I knew I shouldn't have said that thing earlier — they're definitely mocking it", {"jumping_to_conclusions": 5})
    ]),
    tier="triangulation", cg="jtc_leap_1", opacity=0.55))

questions.append(q("jumping_to_conclusions", "somatic",
    "When a situation is ambiguous (unclear text message, unexplained change in plans), your body:",
    opts([
        ("Stays calm — ambiguity is normal, I'll get clarity soon", {"jumping_to_conclusions": 1}),
        ("Feels slightly uneasy but manageable", {"jumping_to_conclusions": 2}),
        ("Jumps to a negative conclusion immediately and reacts to THAT", {"jumping_to_conclusions": 5}),
        ("Can't tolerate the uncertainty — I need to reach a conclusion RIGHT NOW even if it's wrong", {"jumping_to_conclusions": 5})
    ]),
    tier="core", cg="jtc_leap_1", opacity=0.7))

questions.append(q("jumping_to_conclusions", "temporal",
    "How many of your conclusions about people's intentions have turned out to be wrong?",
    opts([
        ("Many — I've learned to check my assumptions", {"jumping_to_conclusions": 2}),
        ("Enough that I try to withhold judgment now", {"jumping_to_conclusions": 2}),
        ("I rarely check — once I've concluded, I act on it", {"jumping_to_conclusions": 4}),
        ("They're almost never wrong — I have strong instincts", {"jumping_to_conclusions": 5})
    ]),
    tier="trap", trap=True, cg="jtc_leap_1", opacity=0.65))

questions.append(q("jumping_to_conclusions", "behavioral_recall",
    "When your plans change unexpectedly, how quickly do you interpret WHY — and how accurate is that interpretation?",
    opts([
        ("I ask rather than assume — interpretations without data are just stories", {"jumping_to_conclusions": 1}),
        ("I have a hypothesis but I check it", {"jumping_to_conclusions": 2}),
        ("I instantly 'know' why and act accordingly — even without confirmation", {"jumping_to_conclusions": 4}),
        ("My interpretation is gospel — I don't need confirmation because I can feel the truth", {"jumping_to_conclusions": 5})
    ]),
    tier="consistency_check", cg="jtc_leap_1", opacity=0.7))

questions.append(q("jumping_to_conclusions", "scenario",
    "A coworker walks past your desk without saying hello. You:",
    opts([
        ("Don't notice or don't care", {"jumping_to_conclusions": 1}),
        ("Wave — maybe they were distracted", {"jumping_to_conclusions": 1}),
        ("Wonder if they're upset with you", {"jumping_to_conclusions": 3}),
        ("Conclude they don't respect you and start treating them differently", {"jumping_to_conclusions": 5})
    ]),
    tier="triangulation", cg="jtc_leap_1", opacity=0.5))

questions.append(q("jumping_to_conclusions", "partner_perspective",
    "Your partner sighs. Just a sigh. You:",
    opts([
        ("Don't read into it — people sigh", {"jumping_to_conclusions": 1}),
        ("Might ask 'everything okay?' casually", {"jumping_to_conclusions": 2}),
        ("Immediately start constructing a theory about what's wrong", {"jumping_to_conclusions": 4}),
        ("Have already written the entire narrative in your head and are reacting to it", {"jumping_to_conclusions": 5})
    ]),
    tier="core", cg="jtc_leap_1", opacity=0.6))

# BLAMING (10)
questions.append(q("blaming", "scenario",
    "You're having a bad day. Who or what is responsible?",
    opts([
        ("A mix of circumstances, some my choices, some beyond my control", {"blaming": 1}),
        ("Mostly bad luck today — it'll pass", {"blaming": 2}),
        ("Other people — they made my day worse", {"blaming": 4}),
        ("The world is against me — everything and everyone is the problem", {"blaming": 5})
    ]),
    tier="core", cg="bl_external_1", opacity=0.65))

questions.append(q("blaming", "behavioral_recall",
    "When a relationship fails, your default is to assign blame to:",
    opts([
        ("Both of us — relationships are two-way", {"blaming": 1}),
        ("Mostly me (too much self-blame) or mostly them (too much other-blame)", {"blaming": 3}),
        ("Them — I gave everything and they dropped the ball", {"blaming": 4}),
        ("It's always the other person — I'm always the one who tried", {"blaming": 5})
    ]),
    tier="core", cg="bl_external_1", opacity=0.7))

questions.append(q("blaming", "partner_perspective",
    "You and your partner are arguing. You catch yourself thinking:",
    opts([
        ("We both contributed to this — let me own my part", {"blaming": 1}),
        ("This started because of their behavior, but my reaction made it worse", {"blaming": 2}),
        ("This is entirely their fault — if they hadn't done X, we wouldn't be here", {"blaming": 4}),
        ("Everything wrong in this relationship is because of them", {"blaming": 5})
    ]),
    tier="core", cg="bl_external_1", opacity=0.7))

questions.append(q("blaming", "forced_choice",
    "When things go wrong in your life, you tend to focus blame on:",
    opts([
        ("Yourself — often too harshly (self-blame)", {"blaming": 3}),
        ("Others — they're usually the reason things don't work out", {"blaming": 5}),
        ("Circumstances — life just happens sometimes", {"blaming": 1}),
        ("A realistic mix — some me, some them, some circumstances", {"blaming": 1})
    ]),
    tier="core", cg="bl_external_1", opacity=0.7))

questions.append(q("blaming", "scenario",
    "You get a parking ticket because you forgot to feed the meter. Your thought:",
    opts([
        ("My fault — I'll set reminders next time", {"blaming": 1}),
        ("Annoying, but that's how meters work", {"blaming": 2}),
        ("This city's parking enforcement is ridiculous — they're just revenue machines", {"blaming": 4}),
        ("Someone should have reminded me — or the app should have sent an alert", {"blaming": 5})
    ]),
    tier="triangulation", cg="bl_external_1", opacity=0.5))

questions.append(q("blaming", "temporal",
    "When you think about why your life isn't where you want it to be, you blame:",
    opts([
        ("My own choices and circumstances in roughly equal measure", {"blaming": 1}),
        ("Some bad breaks, but mostly I'm responsible for my own path", {"blaming": 2}),
        ("Other people — parents who didn't prepare me, partners who held me back, bosses who didn't see my potential", {"blaming": 4}),
        ("Everyone and everything except me — I'd be successful if the world wasn't stacked against me", {"blaming": 5})
    ]),
    tier="core", cg="bl_external_1", opacity=0.75))

questions.append(q("blaming", "behavioral_recall",
    "How often do you find yourself saying 'If they hadn't done X, I wouldn't have done Y'?",
    opts([
        ("Rarely — I own my reactions regardless of what triggered them", {"blaming": 1}),
        ("Sometimes — in genuinely reactive situations", {"blaming": 2}),
        ("Often — other people's behavior explains most of my negative actions", {"blaming": 4}),
        ("Constantly — my bad behavior is always someone else's fault", {"blaming": 5})
    ]),
    tier="triangulation", cg="bl_external_1", opacity=0.65))

questions.append(q("blaming", "trap",
    "You believe that taking responsibility for everything is:",
    opts([
        ("Important — even when it's uncomfortable, owning your part leads to growth", {"blaming": 1}),
        ("Reasonable — for the things that are actually your responsibility", {"blaming": 2}),
        ("Overrated — some things genuinely aren't your fault and saying they are is just guilt", {"blaming": 3}),
        ("Unfair — especially when other people caused the problem", {"blaming": 5})
    ]),
    tier="trap", trap=True, cg="bl_external_1", opacity=0.65))

questions.append(q("blaming", "somatic",
    "When you recognize that YOU caused a problem (not someone else), your body:",
    opts([
        ("Feels uncomfortable but you lean into accountability", {"blaming": 1}),
        ("Resists briefly then accepts — ownership is healthy", {"blaming": 2}),
        ("Deflects immediately — your body literally rejects the blame", {"blaming": 4}),
        ("Finds someone else to redirect it to before the discomfort settles", {"blaming": 5})
    ]),
    tier="core", cg="bl_external_1", opacity=0.7))

questions.append(q("blaming", "partner_perspective",
    "Your partner says 'You need to take responsibility for your part in this.' You:",
    opts([
        ("Do — they're right, even if it stings", {"blaming": 1}),
        ("Think about it and identify what you could have done differently", {"blaming": 2}),
        ("Deflect — 'what about YOUR part?'", {"blaming": 4}),
        ("Get angry — they're the one who should be apologizing, not you", {"blaming": 5})
    ]),
    tier="consistency_check", cg="bl_external_1", opacity=0.65))

# FALLACY_OF_FAIRNESS (10)
questions.append(q("fallacy_of_fairness", "scenario",
    "A coworker who does less work than you gets the same raise. You think:",
    opts([
        ("Raises aren't always perfectly calibrated — I'll advocate for myself next cycle", {"fallacy_of_fairness": 1}),
        ("Frustrating, but I don't know their full situation", {"fallacy_of_fairness": 2}),
        ("This is so unfair — I deserve more because I work harder", {"fallacy_of_fairness": 4}),
        ("The system is rigged — hard work is never rewarded fairly", {"fallacy_of_fairness": 5})
    ]),
    tier="core", cg="fof_justice_1", opacity=0.6))

questions.append(q("fallacy_of_fairness", "behavioral_recall",
    "How much of your emotional energy goes to tracking whether life is treating you fairly?",
    opts([
        ("Very little — fairness is a concept, not a guarantee", {"fallacy_of_fairness": 1}),
        ("Some — I notice unfairness but don't dwell on it", {"fallacy_of_fairness": 2}),
        ("A lot — I'm constantly measuring whether I'm getting what I deserve", {"fallacy_of_fairness": 4}),
        ("Most of it — the unfairness of life is the central fact of my existence", {"fallacy_of_fairness": 5})
    ]),
    tier="core", cg="fof_justice_1", opacity=0.7))

questions.append(q("fallacy_of_fairness", "partner_perspective",
    "You do more housework than your partner. You feel:",
    opts([
        ("Like it needs a conversation, not a score-keeping exercise", {"fallacy_of_fairness": 1}),
        ("Mildly frustrated — I'd like more balance", {"fallacy_of_fairness": 2}),
        ("Deeply resentful — it's NOT FAIR and I keep a running tally", {"fallacy_of_fairness": 5}),
        ("Like I'm being taken advantage of — they OWE me", {"fallacy_of_fairness": 5})
    ]),
    tier="core", cg="fof_justice_1", opacity=0.65))

questions.append(q("fallacy_of_fairness", "forced_choice",
    "Life being unfair makes you:",
    opts([
        ("Pragmatic — fairness isn't guaranteed so I work with what I have", {"fallacy_of_fairness": 1}),
        ("Bitter — I've been dealt a bad hand and I can't get over it", {"fallacy_of_fairness": 5})
    ]),
    tier="core", cg="fof_justice_1", opacity=0.8))

questions.append(q("fallacy_of_fairness", "scenario",
    "Someone born into wealth succeeds effortlessly while you struggle for everything. You think:",
    opts([
        ("Different starting points — I focus on my own path", {"fallacy_of_fairness": 1}),
        ("Frustrating but comparing doesn't help", {"fallacy_of_fairness": 2}),
        ("It's deeply unfair and it makes my achievements feel pointless", {"fallacy_of_fairness": 4}),
        ("Why should I even try? The game is rigged.", {"fallacy_of_fairness": 5})
    ]),
    tier="triangulation", cg="fof_justice_1", opacity=0.6))

questions.append(q("fallacy_of_fairness", "somatic",
    "When you perceive an unfairness directed at you, your body:",
    opts([
        ("Notes it and moves on — not everything is fair, that's life", {"fallacy_of_fairness": 1}),
        ("Feels a flash of indignation that passes", {"fallacy_of_fairness": 2}),
        ("Burns with resentment that can last for days", {"fallacy_of_fairness": 4}),
        ("Can't let it go — the unfairness replays and compounds with every other unfairness you've experienced", {"fallacy_of_fairness": 5})
    ]),
    tier="triangulation", cg="fof_justice_1", opacity=0.7))

questions.append(q("fallacy_of_fairness", "behavioral_recall",
    "Do you keep a mental scorecard of what you give vs. what you receive in relationships?",
    opts([
        ("No — relationships aren't transactions", {"fallacy_of_fairness": 1}),
        ("Loosely — I notice big imbalances but don't track details", {"fallacy_of_fairness": 2}),
        ("Yes — and the imbalance bothers me constantly", {"fallacy_of_fairness": 4}),
        ("Meticulously — I know exactly how much more I give than I get", {"fallacy_of_fairness": 5})
    ]),
    tier="core", cg="fof_justice_1", opacity=0.65))

questions.append(q("fallacy_of_fairness", "temporal",
    "Looking back, how much has a sense of unfairness held you back from happiness?",
    opts([
        ("Very little — I focus on what I can control", {"fallacy_of_fairness": 1}),
        ("Some — I've had moments of resentment but moved past them", {"fallacy_of_fairness": 2}),
        ("Significantly — the unfairness narrative has poisoned a lot of joy", {"fallacy_of_fairness": 4}),
        ("Enormously — I can't enjoy what I have because I'm focused on what I should have", {"fallacy_of_fairness": 5})
    ]),
    tier="consistency_check", cg="fof_justice_1", opacity=0.7))

questions.append(q("fallacy_of_fairness", "trap",
    "Someone says 'Life isn't fair — get over it.' You:",
    opts([
        ("Agree — and you have", {"fallacy_of_fairness": 1}),
        ("Know they're right but it's still hard sometimes", {"fallacy_of_fairness": 2}),
        ("Feel dismissed — easy for them to say when life HAS been fair to them", {"fallacy_of_fairness": 4}),
        ("Rage — they're invalidating your experience and that's another unfairness", {"fallacy_of_fairness": 5})
    ]),
    tier="trap", trap=True, cg="fof_justice_1", opacity=0.6))

questions.append(q("fallacy_of_fairness", "scenario",
    "You go above and beyond for a friend and they barely acknowledge it. You:",
    opts([
        ("Don't keep score — you did it because you wanted to", {"fallacy_of_fairness": 1}),
        ("Feel a twinge of disappointment but move on", {"fallacy_of_fairness": 2}),
        ("Feel intensely resentful — you DESERVE gratitude proportional to your effort", {"fallacy_of_fairness": 5}),
        ("Add it to the running list of ways life isn't fair to you specifically", {"fallacy_of_fairness": 5})
    ]),
    tier="triangulation", cg="fof_justice_1", opacity=0.6))

# FALLACY_OF_CHANGE (10)
questions.append(q("fallacy_of_change", "scenario",
    "Something about your partner really bothers you. Your strategy is:",
    opts([
        ("Communicate what I need and accept that they may or may not change", {"fallacy_of_change": 1}),
        ("Discuss it, then decide if I can live with it either way", {"fallacy_of_change": 2}),
        ("Keep pushing until they change — I know what's best for them and us", {"fallacy_of_change": 4}),
        ("My happiness depends on them changing this — and they WILL if they really love me", {"fallacy_of_change": 5})
    ]),
    tier="core", cg="foc_control_1", opacity=0.7))

questions.append(q("fallacy_of_change", "behavioral_recall",
    "How much of your happiness is contingent on other people changing their behavior?",
    opts([
        ("Very little — I'm responsible for my own happiness", {"fallacy_of_change": 1}),
        ("Some — certain people's behavior does affect my wellbeing", {"fallacy_of_change": 2}),
        ("A lot — I'd be happy if only certain people would stop doing certain things", {"fallacy_of_change": 4}),
        ("Almost all of it — other people are the primary obstacle to my happiness", {"fallacy_of_change": 5})
    ]),
    tier="core", cg="foc_control_1", opacity=0.7))

questions.append(q("fallacy_of_change", "partner_perspective",
    "Have you ever stayed in a relationship primarily because you believed you could change the other person?",
    opts([
        ("No — I accept people as they are or I leave", {"fallacy_of_change": 1}),
        ("Maybe briefly — but I realized it doesn't work", {"fallacy_of_change": 2}),
        ("Yes — and I invested years before accepting they wouldn't change", {"fallacy_of_change": 4}),
        ("I'm doing it right now", {"fallacy_of_change": 5})
    ]),
    tier="core", cg="foc_control_1", opacity=0.7))

questions.append(q("fallacy_of_change", "forced_choice",
    "If your partner/friend/family member would just change ONE thing, everything would be fine. This thought:",
    opts([
        ("Rarely crosses my mind — I don't hinge my happiness on others changing", {"fallacy_of_change": 1}),
        ("Crosses my mind constantly — I know exactly what they need to change", {"fallacy_of_change": 5})
    ]),
    tier="core", cg="foc_control_1", opacity=0.8))

questions.append(q("fallacy_of_change", "scenario",
    "You've asked your partner to change a behavior multiple times. They haven't. You:",
    opts([
        ("Accept that this is who they are and decide if you can live with it", {"fallacy_of_change": 1}),
        ("Have one more conversation, then let it go one way or another", {"fallacy_of_change": 2}),
        ("Keep bringing it up — eventually they'll get it", {"fallacy_of_change": 4}),
        ("Resort to pressure tactics (ultimatums, guilt, withdrawal) because they MUST change for this to work", {"fallacy_of_change": 5})
    ]),
    tier="triangulation", cg="foc_control_1", opacity=0.7))

questions.append(q("fallacy_of_change", "somatic",
    "When someone you love refuses to change something you've asked about repeatedly, your body:",
    opts([
        ("Accepts it — I control my reactions, not their behavior", {"fallacy_of_change": 1}),
        ("Feels frustration but ultimately respects their autonomy", {"fallacy_of_change": 2}),
        ("Fills with resentment — they're choosing not to change FOR me", {"fallacy_of_change": 4}),
        ("Rages — if they loved me, they'd change. Their refusal is proof they don't care.", {"fallacy_of_change": 5})
    ]),
    tier="core", cg="foc_control_1", opacity=0.75))

questions.append(q("fallacy_of_change", "temporal",
    "How many relationships have you lost because you couldn't stop trying to change the other person?",
    opts([
        ("None — I learned early that people are who they are", {"fallacy_of_change": 1}),
        ("One — it was a hard lesson", {"fallacy_of_change": 2}),
        ("Several — I keep thinking THIS time the person will change", {"fallacy_of_change": 4}),
        ("Most of them — and I still believe the right amount of pressure can change people", {"fallacy_of_change": 5})
    ]),
    tier="consistency_check", cg="foc_control_1", opacity=0.7))

questions.append(q("fallacy_of_change", "trap",
    "When people say 'you can't change other people,' you think:",
    opts([
        ("True — and I've stopped trying", {"fallacy_of_change": 1}),
        ("Mostly true, but healthy relationships DO involve growth", {"fallacy_of_change": 2}),
        ("That's what people say when they've given up — with enough love and effort, people CAN change", {"fallacy_of_change": 5}),
        ("I don't want to change them — I just want them to see how their behavior affects me (which is still wanting them to change)", {"fallacy_of_change": 4})
    ]),
    tier="trap", trap=True, cg="foc_control_1", opacity=0.65))

questions.append(q("fallacy_of_change", "behavioral_recall",
    "How much time do you spend thinking about what OTHER people should do differently vs. what YOU could do differently?",
    opts([
        ("Mostly focused on myself — that's where I have control", {"fallacy_of_change": 1}),
        ("A healthy balance — I see both sides", {"fallacy_of_change": 2}),
        ("Mostly focused on them — if they'd just change, things would be fine", {"fallacy_of_change": 4}),
        ("Entirely focused on them — I've done all I can; it's their turn", {"fallacy_of_change": 5})
    ]),
    tier="triangulation", cg="foc_control_1", opacity=0.65))

questions.append(q("fallacy_of_change", "scenario",
    "Your happiness would increase most by:",
    opts([
        ("Changing how I think about and respond to situations", {"fallacy_of_change": 1}),
        ("A mix of internal changes and external improvements", {"fallacy_of_change": 2}),
        ("Specific people in my life changing specific behaviors", {"fallacy_of_change": 4}),
        ("Everyone around me finally treating me the way I deserve", {"fallacy_of_change": 5})
    ]),
    tier="core", cg="foc_control_1", opacity=0.65))

# HEAVEN_REWARD_FALLACY (11)
questions.append(q("heaven_reward_fallacy", "scenario",
    "You've been working incredibly hard for months — extra hours, sacrificing personal time, going above and beyond. But nobody notices. You feel:",
    opts([
        ("Fine — I work hard because it aligns with my values, not for recognition", {"heaven_reward_fallacy": 1}),
        ("A bit disappointed, but I'll advocate for myself", {"heaven_reward_fallacy": 2}),
        ("Resentful — I DESERVE recognition and the fact that it hasn't come is deeply unfair", {"heaven_reward_fallacy": 4}),
        ("Enraged — the universe owes me for my sacrifice and the debt is accumulating", {"heaven_reward_fallacy": 5})
    ]),
    tier="core", cg="hrf_reward_1", opacity=0.65))

questions.append(q("heaven_reward_fallacy", "behavioral_recall",
    "How strongly do you believe that sacrifice and suffering should be rewarded?",
    opts([
        ("Effort is its own reward — external payoff isn't guaranteed", {"heaven_reward_fallacy": 1}),
        ("I hope hard work pays off, but I know it doesn't always", {"heaven_reward_fallacy": 2}),
        ("Strongly — the universe SHOULD reward people who sacrifice", {"heaven_reward_fallacy": 4}),
        ("Absolutely — I keep score of my sacrifices and I'm owed a payoff", {"heaven_reward_fallacy": 5})
    ]),
    tier="core", cg="hrf_reward_1", opacity=0.7))

questions.append(q("heaven_reward_fallacy", "partner_perspective",
    "You've been extremely self-sacrificing for your partner. They don't seem to fully appreciate it. You think:",
    opts([
        ("I gave because I wanted to — not for a return", {"heaven_reward_fallacy": 1}),
        ("A little appreciation would be nice, but I'm not keeping score", {"heaven_reward_fallacy": 2}),
        ("I GAVE UP SO MUCH for them and this is what I get?", {"heaven_reward_fallacy": 4}),
        ("They owe me — my sacrifice MUST be repaid or I've been a fool", {"heaven_reward_fallacy": 5})
    ]),
    tier="core", cg="hrf_reward_1", opacity=0.7))

questions.append(q("heaven_reward_fallacy", "forced_choice",
    "Being a good person should result in:",
    opts([
        ("Internal peace — goodness is the reward itself", {"heaven_reward_fallacy": 1}),
        ("Good things happening to you — that's how the universe should work", {"heaven_reward_fallacy": 5})
    ]),
    tier="core", cg="hrf_reward_1", opacity=0.8))

questions.append(q("heaven_reward_fallacy", "scenario",
    "You always put others first. But when YOU need help, nobody's there. Your thought:",
    opts([
        ("I need to build more reciprocal relationships — and be willing to ask for help", {"heaven_reward_fallacy": 1}),
        ("Disappointing — but I can't give expecting to receive", {"heaven_reward_fallacy": 2}),
        ("This is proof that being good doesn't pay off — why do I even bother?", {"heaven_reward_fallacy": 5}),
        ("I've been cheated — I've EARNED support through my sacrifice and the world defaulted", {"heaven_reward_fallacy": 5})
    ]),
    tier="triangulation", cg="hrf_reward_1", opacity=0.65))

questions.append(q("heaven_reward_fallacy", "somatic",
    "When good things happen to someone who hasn't 'earned' them (while you've been working so hard), your body:",
    opts([
        ("Doesn't react — their fortune isn't related to my effort", {"heaven_reward_fallacy": 1}),
        ("Feels a brief twinge of 'that's not fair' that passes", {"heaven_reward_fallacy": 2}),
        ("Burns with injustice — THEY didn't sacrifice like I did", {"heaven_reward_fallacy": 4}),
        ("Is consumed by bitterness — the reward system is broken and I'm the one paying", {"heaven_reward_fallacy": 5})
    ]),
    tier="triangulation", cg="hrf_reward_1", opacity=0.7))

questions.append(q("heaven_reward_fallacy", "temporal",
    "How much resentment have you accumulated from unrewarded sacrifice?",
    opts([
        ("Very little — I don't sacrifice with the expectation of reward", {"heaven_reward_fallacy": 1}),
        ("Some — there are moments I wish my effort had been recognized", {"heaven_reward_fallacy": 2}),
        ("A lot — I carry a ledger of unreturned favors and unrecognized sacrifice", {"heaven_reward_fallacy": 4}),
        ("Enormous — it's one of the defining grievances of my life", {"heaven_reward_fallacy": 5})
    ]),
    tier="core", cg="hrf_reward_1", opacity=0.7))

questions.append(q("heaven_reward_fallacy", "behavioral_recall",
    "How often do you do things you don't want to do because you believe the sacrifice will eventually be rewarded?",
    opts([
        ("Rarely — I do things because I choose to, not for cosmic credit", {"heaven_reward_fallacy": 1}),
        ("Sometimes — delayed gratification is real, but I don't expect the universe to keep score", {"heaven_reward_fallacy": 2}),
        ("Often — I push through misery believing it'll pay off eventually", {"heaven_reward_fallacy": 4}),
        ("Constantly — I martyr myself expecting eventual reward, and I'm furious it hasn't come", {"heaven_reward_fallacy": 5})
    ]),
    tier="consistency_check", cg="hrf_reward_1", opacity=0.65))

questions.append(q("heaven_reward_fallacy", "trap",
    "A friend who parties constantly and takes no responsibility seems happier than you. You feel:",
    opts([
        ("Their happiness is their business — I live according to my values, not theirs", {"heaven_reward_fallacy": 1}),
        ("Slightly envious but I know their path wouldn't work for me", {"heaven_reward_fallacy": 2}),
        ("It's unfair — I do the RIGHT thing and I'm miserable while they're having fun", {"heaven_reward_fallacy": 5}),
        ("Proof that being responsible and self-sacrificing is for suckers", {"heaven_reward_fallacy": 5})
    ]),
    tier="trap", trap=True, cg="hrf_reward_1", opacity=0.6))

questions.append(q("heaven_reward_fallacy", "scenario",
    "You consistently put in more effort than your peers. A peer who does less gets promoted over you. You:",
    opts([
        ("Advocate for yourself — promotion requires visibility, not just effort", {"heaven_reward_fallacy": 1}),
        ("Frustrated but pragmatic — I need to make my contributions more visible", {"heaven_reward_fallacy": 2}),
        ("Devastated — hard work SHOULD be rewarded and the system failed me", {"heaven_reward_fallacy": 4}),
        ("Give up — effort is meaningless if the world doesn't reward it", {"heaven_reward_fallacy": 5})
    ]),
    tier="triangulation", cg="hrf_reward_1", opacity=0.6))

questions.append(q("heaven_reward_fallacy", "partner_perspective",
    "In relationships, how much do you expect your sacrifices to be matched or repaid?",
    opts([
        ("Not at all — I give freely without expectation", {"heaven_reward_fallacy": 1}),
        ("I hope for reciprocity but don't demand it", {"heaven_reward_fallacy": 2}),
        ("I expect equal return — anything less is exploitation", {"heaven_reward_fallacy": 4}),
        ("I track every sacrifice and expect compound interest on my generosity", {"heaven_reward_fallacy": 5})
    ]),
    tier="core", cg="hrf_reward_1", opacity=0.65))


questions.append(q("disqualifying_positive", "scenario",
    "You handled a crisis at work brilliantly. Your thought afterward:",
    opts([
        ("I'm proud of how I handled that — I'm good under pressure", {"disqualifying_positive": 1}),
        ("That went well — I'll note it as a strength", {"disqualifying_positive": 2}),
        ("Anyone would have handled it the same way — it wasn't special", {"disqualifying_positive": 4}),
        ("I got lucky — next time I'll probably freeze", {"disqualifying_positive": 5})
    ]),
    tier="triangulation", cg="dp_deflection_1", opacity=0.6))

questions.append(q("jumping_to_conclusions", "behavioral_recall",
    "When a meeting gets scheduled with no context, you immediately assume:",
    opts([
        ("It's just a meeting — I'll find out when I get there", {"jumping_to_conclusions": 1}),
        ("Could be anything — I don't speculate", {"jumping_to_conclusions": 1}),
        ("Something is wrong — meetings without context mean bad news", {"jumping_to_conclusions": 4}),
        ("I'm in trouble — I start preparing my defense before I even know the topic", {"jumping_to_conclusions": 5})
    ]),
    tier="triangulation", cg="jtc_leap_1", opacity=0.6))

questions.append(q("mental_filter", "scenario",
    "You cook a complex recipe. Everything turns out great except you slightly oversalted one dish. Your takeaway:",
    opts([
        ("Overall success — I made a great meal", {"mental_filter": 1}),
        ("Mostly great, I'll adjust the salt next time", {"mental_filter": 2}),
        ("I oversalted it — that's all I can think about", {"mental_filter": 4}),
        ("The whole meal was ruined by my mistake", {"mental_filter": 5})
    ]),
    tier="triangulation", cg="mf_negative_1", opacity=0.5))

questions.append(q("labeling", "behavioral_recall",
    "After making a social misstep, your self-talk is:",
    opts([
        ("'That was awkward — I'll do better next time'", {"labeling": 1}),
        ("'That wasn't my best moment'", {"labeling": 2}),
        ("'I'm so awkward — I'm hopeless at social situations'", {"labeling": 4}),
        ("'I'm a social disaster — this is who I am'", {"labeling": 5})
    ]),
    tier="triangulation", cg="lab_self_1", opacity=0.6))

questions.append(q("blaming", "scenario",
    "You overslept and missed an important meeting. Your first thought:",
    opts([
        ("My fault — I should have set multiple alarms", {"blaming": 1}),
        ("I dropped the ball — time to apologize and reschedule", {"blaming": 1}),
        ("My phone's alarm didn't go off — stupid technology", {"blaming": 4}),
        ("My partner should have woken me up — they knew I had the meeting", {"blaming": 5})
    ]),
    tier="triangulation", cg="bl_external_1", opacity=0.55))

questions.append(q("fallacy_of_fairness", "scenario",
    "You held the door for someone and they didn't say thank you. You:",
    opts([
        ("Don't think twice about it", {"fallacy_of_fairness": 1}),
        ("Note it briefly and move on", {"fallacy_of_fairness": 2}),
        ("Feel genuinely angry — basic courtesy is a RULE and they broke it", {"fallacy_of_fairness": 4}),
        ("It confirms that being a decent person goes unrecognized in this world", {"fallacy_of_fairness": 5})
    ]),
    tier="triangulation", cg="fof_justice_1", opacity=0.5))

questions.append(q("fallacy_of_change", "partner_perspective",
    "How often do you think 'If they REALLY loved me, they would change [behavior]'?",
    opts([
        ("Rarely — love and behavior change are separate things", {"fallacy_of_change": 1}),
        ("Occasionally — but I know that's not how love works", {"fallacy_of_change": 2}),
        ("Often — love should motivate change", {"fallacy_of_change": 4}),
        ("Constantly — their refusal to change is proof they don't love me enough", {"fallacy_of_change": 5})
    ]),
    tier="consistency_check", cg="foc_control_1", opacity=0.7))

questions.append(q("catastrophizing", "behavioral_recall",
    "When you get a notification that says 'Your bank account' — before even reading it, you think:",
    opts([
        ("Could be anything — statement, promotion, fraud alert", {"catastrophizing": 1}),
        ("Probably a statement or routine notification", {"catastrophizing": 2}),
        ("Someone drained my account — oh no", {"catastrophizing": 4}),
        ("Full panic — my money is gone, identity stolen, financial ruin", {"catastrophizing": 5})
    ]),
    tier="triangulation", cg="cat_general_1", opacity=0.55))

questions.append(q("emotional_reasoning", "scenario",
    "You feel like your marriage is falling apart, but your partner says they're happy and there's no evidence of problems. You trust:",
    opts([
        ("The evidence and my partner's words — my feeling is anxiety, not reality", {"emotional_reasoning": 1}),
        ("Mostly the evidence, but I'll stay alert", {"emotional_reasoning": 2}),
        ("My feeling — something must be wrong even if I can't prove it", {"emotional_reasoning": 4}),
        ("My feeling over everything else — the evidence is deceiving and my partner is lying", {"emotional_reasoning": 5})
    ]),
    tier="core", cg="er_feelings_1", opacity=0.7))

questions.append(q("should_statements", "behavioral_recall",
    "Count the 'shoulds' in your life. How many things do you do purely because you 'should' vs. because you want to?",
    opts([
        ("Most of what I do is chosen — my obligations are freely accepted", {"should_statements": 1}),
        ("A mix — some obligations, some genuine desires", {"should_statements": 2}),
        ("Most of my life is 'should' — I rarely do things just because I want to", {"should_statements": 4}),
        ("My entire life is a list of shoulds — I've lost track of what I actually want", {"should_statements": 5})
    ]),
    tier="consistency_check", cg="ss_self_1", opacity=0.7))

questions.append(q("fortune_telling", "behavioral_recall",
    "Before attending a social event, you've already decided:",
    opts([
        ("Nothing — I'll see how it goes", {"fortune_telling": 1}),
        ("I might be a little nervous but it'll probably be fine", {"fortune_telling": 2}),
        ("Nobody will want to talk to me — I'll end up alone in a corner", {"fortune_telling": 4}),
        ("It will be terrible — I'll embarrass myself, everyone will judge me, and I'll wish I'd stayed home", {"fortune_telling": 5})
    ]),
    tier="triangulation", cg="ft_prediction_1", opacity=0.6))

questions.append(q("personalization", "scenario",
    "The mood in your household is tense. Everyone seems on edge. You assume:",
    opts([
        ("People are dealing with their own stress — not everything is about me", {"personalization": 1}),
        ("Something external is affecting everyone — work stress, weather, whatever", {"personalization": 2}),
        ("It's probably because of something I said or did earlier", {"personalization": 4}),
        ("I've created this atmosphere — the tension is my fault, even if I can't identify how", {"personalization": 5})
    ]),
    tier="triangulation", cg="per_blame_1", opacity=0.6))


# Count and validate
assert len(questions) == 200, f"Expected 200, got {len(questions)}"

with open("/Users/user/personal/sb/trueassess/priv/question_bank/cognitive_distortions.json", "w") as f:
    json.dump(questions, f, indent=2)

print(f"Cognitive Distortions: {len(questions)} questions written")
from collections import Counter
dims = Counter(q["dimension"] for q in questions)
print("Dimensions:", dict(dims))
tiers = Counter(q["tier_role"] for q in questions)
print("Tiers:", dict(tiers))
types = Counter(q["question_type"] for q in questions)
print("Types:", dict(types))
