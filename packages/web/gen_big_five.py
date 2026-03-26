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
        "tags": tags or ["big_five", dim]
    }

def opts(choices):
    return [{"id": chr(97+i), "text": t, "scores": s} for i, (t, s) in enumerate(choices)]

# 150 questions: 30 per dimension
# OPENNESS, CONSCIENTIOUSNESS, EXTRAVERSION, AGREEABLENESS, NEUROTICISM

# ============================================================
# OPENNESS (30)
# ============================================================

questions.append(q("openness", "scenario",
    "You're browsing a bookstore and discover a section on a topic you know nothing about — ancient Persian poetry, say. You:",
    opts([
        ("Spend 30 minutes browsing — this could be fascinating", {"openness": 5}),
        ("Glance at a few titles and move on to what you came for", {"openness": 3}),
        ("Walk past — why would you read about something you have no background in?", {"openness": 1}),
        ("Buy one on impulse — the unfamiliarity IS the appeal", {"openness": 5})
    ]),
    tier="core", cg="o_curiosity_1", opacity=0.55))

questions.append(q("openness", "behavioral_recall",
    "In the last month, how many times have you voluntarily tried something completely new to you?",
    opts([
        ("Several times — I actively seek novel experiences", {"openness": 5}),
        ("Once or twice — when opportunities came up", {"openness": 3}),
        ("None that I can think of — I like what I like", {"openness": 1}),
        ("Does researching new topics online count? Because I do that constantly", {"openness": 4})
    ]),
    tier="core", cg="o_curiosity_1", opacity=0.55))

questions.append(q("openness", "scenario",
    "A friend invites you to an experimental art exhibit where the art is intentionally confusing and challenging. You:",
    opts([
        ("Go enthusiastically — art should challenge you", {"openness": 5}),
        ("Go with mild interest — might be interesting, might be pretentious", {"openness": 3}),
        ("Decline — you prefer art you can actually understand and enjoy", {"openness": 1}),
        ("Go and end up in a 2-hour conversation with a stranger about the meaning of one piece", {"openness": 5})
    ]),
    tier="triangulation", cg="o_art_1", opacity=0.5))

questions.append(q("openness", "forced_choice",
    "On vacation, you'd rather:",
    opts([
        ("Explore a city with no itinerary — see what happens", {"openness": 5}),
        ("Follow a carefully planned schedule of the top-rated attractions", {"openness": 1})
    ]),
    tier="core", cg="o_curiosity_1", opacity=0.6))

questions.append(q("openness", "temporal",
    "How have your core beliefs and worldview changed over the past decade?",
    opts([
        ("Dramatically — I've revised fundamental assumptions multiple times", {"openness": 5}),
        ("Significantly — new experiences have reshaped my perspective", {"openness": 4}),
        ("Somewhat — I've refined my views but the foundation is the same", {"openness": 3}),
        ("Very little — I figured out what I believe early and it's held up", {"openness": 1})
    ]),
    tier="core", cg="o_intellectual_1", opacity=0.7))

questions.append(q("openness", "somatic",
    "When you encounter an idea that contradicts something you've always believed, your body:",
    opts([
        ("Leans forward with excitement — 'tell me more'", {"openness": 5}),
        ("Registers mild interest — worth considering", {"openness": 3}),
        ("Tenses defensively — you need to evaluate the threat to your worldview", {"openness": 2}),
        ("Nothing — you dismiss it and move on", {"openness": 1})
    ]),
    tier="core", cg="o_intellectual_1", opacity=0.7))

questions.append(q("openness", "partner_perspective",
    "Your partner has a hobby you find deeply uninteresting. They want to share it with you. You:",
    opts([
        ("Dive in genuinely — their passion might reveal something you never expected to enjoy", {"openness": 5}),
        ("Try it once to be supportive", {"openness": 3}),
        ("Politely decline — you know what you like", {"openness": 1}),
        ("Ask them to explain what they love about it — the 'why' interests you even if the 'what' doesn't", {"openness": 4})
    ]),
    tier="triangulation", cg="o_curiosity_1", opacity=0.55))

questions.append(q("openness", "behavioral_recall",
    "When you listen to music, how adventurous are you?",
    opts([
        ("I actively seek out genres and artists I've never heard before", {"openness": 5}),
        ("I branch out sometimes when recommended something", {"openness": 3}),
        ("I mostly stick to what I know I like", {"openness": 2}),
        ("I listen to the same artists and playlists I've had for years", {"openness": 1})
    ]),
    tier="triangulation", cg="o_art_1", opacity=0.5))

questions.append(q("openness", "scenario",
    "You're at dinner with someone who holds political views very different from yours. You:",
    opts([
        ("Are genuinely curious how they arrived at their position — even if you disagree", {"openness": 5}),
        ("Engage respectfully but mostly to challenge their views", {"openness": 3}),
        ("Change the subject — no point in discussing it", {"openness": 2}),
        ("Feel physically uncomfortable — how can a reasonable person think that way?", {"openness": 1})
    ]),
    tier="core", cg="o_intellectual_1", opacity=0.65))

questions.append(q("openness", "forced_choice",
    "Which describes you better?",
    opts([
        ("I'd rather have one deep expertise than know a little about a lot of things", {"openness": 2}),
        ("I'd rather know something about everything than everything about one thing", {"openness": 5})
    ]),
    tier="core", cg="o_curiosity_1", opacity=0.7))

questions.append(q("openness", "scenario",
    "Someone offers you a free trip to a country where you don't speak the language and know nothing about the culture. You:",
    opts([
        ("Accept immediately — that's the BEST kind of travel", {"openness": 5}),
        ("Accept with some nervousness but mostly excitement", {"openness": 4}),
        ("Accept but spend weeks researching and planning first", {"openness": 3}),
        ("Decline — too many unknowns", {"openness": 1})
    ]),
    tier="triangulation", cg="o_curiosity_1", opacity=0.5))

questions.append(q("openness", "temporal",
    "How many completely different career paths or major life directions have you seriously considered?",
    opts([
        ("More than I can count — the world is full of interesting possibilities", {"openness": 5}),
        ("Three or four over my lifetime", {"openness": 3}),
        ("One or two — I've always had a pretty clear direction", {"openness": 2}),
        ("One — I decided early and stuck with it", {"openness": 1})
    ]),
    tier="consistency_check", cg="o_intellectual_1", opacity=0.6))

questions.append(q("openness", "somatic",
    "You walk into a museum you've never been to. There's a guided tour (structured) and a self-guided option (wander freely). Your body gravitates toward:",
    opts([
        ("Self-guided without question — you want to follow your own curiosity", {"openness": 5}),
        ("Self-guided but you grab a map", {"openness": 4}),
        ("The guided tour — you'll learn more with an expert", {"openness": 2}),
        ("The guided tour — wandering with no structure sounds aimless", {"openness": 1})
    ]),
    tier="triangulation", cg="o_art_1", opacity=0.5))

questions.append(q("openness", "behavioral_recall",
    "When was the last time you changed your mind about something important because of a conversation?",
    opts([
        ("Recently — good arguments can shift my thinking at any time", {"openness": 5}),
        ("Within the past year — it takes a compelling case but I'm open", {"openness": 4}),
        ("It's been a while — I'm pretty settled in my views", {"openness": 2}),
        ("I honestly can't remember — I'm not easily persuaded", {"openness": 1})
    ]),
    tier="core", cg="o_intellectual_1", opacity=0.7))

questions.append(q("openness", "scenario",
    "You have a free Saturday with no plans. You spend it:",
    opts([
        ("Exploring somewhere you've never been — a new neighborhood, a random museum, a hiking trail", {"openness": 5}),
        ("Working on a creative project that's been in your head", {"openness": 4}),
        ("Enjoying your usual routine — gym, errands, Netflix", {"openness": 2}),
        ("The same way you spend most Saturdays — your routine works", {"openness": 1})
    ]),
    tier="consistency_check", cg="o_curiosity_1", opacity=0.5))

questions.append(q("openness", "trap",
    "A friend describes you as 'traditional.' This feels:",
    opts([
        ("Wrong — you're anything but traditional", {"openness": 5}),
        ("Partially true — you value some traditions but question others", {"openness": 3}),
        ("Accurate — you appreciate tradition and stability", {"openness": 2}),
        ("Like a compliment — tradition means wisdom passed down", {"openness": 1})
    ]),
    tier="trap", trap=True, cg="o_intellectual_1", opacity=0.6))

questions.append(q("openness", "partner_perspective",
    "Your partner suggests trying an unconventional approach to something in your relationship (therapy, communication style, living arrangement). You:",
    opts([
        ("Love that they're thinking creatively — let's discuss it seriously", {"openness": 5}),
        ("Open to hearing them out", {"openness": 3}),
        ("Skeptical — the conventional approach is conventional because it works", {"openness": 2}),
        ("Uncomfortable — 'if it ain't broke, don't fix it'", {"openness": 1})
    ]),
    tier="core", cg="o_intellectual_1", opacity=0.65))

questions.append(q("openness", "behavioral_recall",
    "How diverse is your friend group in terms of backgrounds, beliefs, and lifestyles?",
    opts([
        ("Very — I'm drawn to people who are different from me", {"openness": 5}),
        ("Somewhat — there's variety but we share a core worldview", {"openness": 3}),
        ("Not very — birds of a feather", {"openness": 2}),
        ("Extremely homogeneous — I'm most comfortable with people like me", {"openness": 1})
    ]),
    tier="triangulation", cg="o_curiosity_1", opacity=0.55))

questions.append(q("openness", "scenario",
    "You discover that a belief you've held your whole life — something you'd argue for passionately — is based on a factual error. You:",
    opts([
        ("Update your belief immediately — facts matter more than comfort", {"openness": 5}),
        ("Research further to make sure, then update if confirmed", {"openness": 4}),
        ("Feel deeply unsettled and resist changing for a while", {"openness": 2}),
        ("Find reasons the new information might be wrong — your original belief felt right", {"openness": 1})
    ]),
    tier="core", cg="o_intellectual_1", opacity=0.75))

questions.append(q("openness", "forced_choice",
    "Which sounds more like a good time?",
    opts([
        ("A dinner party where everyone disagrees about interesting topics", {"openness": 5}),
        ("A dinner party where everyone shares similar views and the conversation flows easily", {"openness": 1})
    ]),
    tier="triangulation", cg="o_intellectual_1", opacity=0.6))

questions.append(q("openness", "somatic",
    "You're in a situation with no rules, no structure, and no expectations — a blank canvas. Your body feels:",
    opts([
        ("Electric with possibility — this is where creativity lives", {"openness": 5}),
        ("Slightly anxious but mostly excited", {"openness": 4}),
        ("Uncomfortable — you want parameters", {"openness": 2}),
        ("Lost — you need structure to function", {"openness": 1})
    ]),
    tier="core", cg="o_art_1", opacity=0.65))

questions.append(q("openness", "temporal",
    "If you could learn about ANYTHING for the next year — no practical constraints — you'd choose:",
    opts([
        ("Something wildly different from anything you've studied before", {"openness": 5}),
        ("Something adjacent to your current expertise", {"openness": 3}),
        ("Going deeper into what you already know", {"openness": 2}),
        ("Something immediately practical and applicable", {"openness": 1})
    ]),
    tier="triangulation", cg="o_curiosity_1", opacity=0.55))

questions.append(q("openness", "scenario",
    "A coworker presents an idea that's creative but risky and unconventional. Most of the team is skeptical. You:",
    opts([
        ("Champion it — innovation requires risk and the conventional approach is boring", {"openness": 5}),
        ("Explore it — let's stress-test it before deciding", {"openness": 4}),
        ("Side with the skeptics — proven methods are proven for a reason", {"openness": 2}),
        ("Dismiss it — too far from what works", {"openness": 1})
    ]),
    tier="triangulation", cg="o_intellectual_1", opacity=0.6))

questions.append(q("openness", "behavioral_recall",
    "How often do you daydream or get lost in imaginative thought?",
    opts([
        ("Constantly — my inner world is rich and I visit it often", {"openness": 5}),
        ("Regularly — especially when I'm bored or relaxed", {"openness": 4}),
        ("Occasionally — but I prefer to stay grounded in reality", {"openness": 2}),
        ("Rarely — I'm a practical thinker, not a daydreamer", {"openness": 1})
    ]),
    tier="consistency_check", cg="o_art_1", opacity=0.6))

questions.append(q("openness", "partner_perspective",
    "When your partner says 'let's try something we've never done before this weekend,' your immediate reaction is:",
    opts([
        ("'Yes! What are you thinking?'", {"openness": 5}),
        ("'Sure, what did you have in mind?'", {"openness": 4}),
        ("'Like what? I need more information before I commit'", {"openness": 2}),
        ("'Can we just do something relaxing instead?'", {"openness": 1})
    ]),
    tier="core", cg="o_curiosity_1", opacity=0.5))

questions.append(q("openness", "somatic",
    "Walking through a neighborhood very different from your own — different culture, language, food — your body:",
    opts([
        ("Comes alive — senses engaged, curiosity humming", {"openness": 5}),
        ("Feels interested and slightly alert", {"openness": 3}),
        ("Feels on guard — this isn't your territory", {"openness": 2}),
        ("Wants to leave — unfamiliar environments are draining", {"openness": 1})
    ]),
    tier="core", cg="o_curiosity_1", opacity=0.6))

questions.append(q("openness", "trap",
    "People who have strong, unchanging convictions — you find them:",
    opts([
        ("Admirable — consistency shows character", {"openness": 1}),
        ("Interesting but potentially limited — how haven't they evolved?", {"openness": 4}),
        ("Suspicious — either they haven't been challenged or they're refusing to grow", {"openness": 5}),
        ("Normal — most people know what they believe", {"openness": 2})
    ]),
    tier="trap", trap=True, cg="o_intellectual_1", opacity=0.65))

questions.append(q("openness", "scenario",
    "You have to eat at the same restaurant for a week. You:",
    opts([
        ("Order something different every single day", {"openness": 5}),
        ("Try a few different things, settle on a favorite", {"openness": 3}),
        ("Find what you like on day one and order it every time", {"openness": 1}),
        ("Ask the server what most people DON'T order — that's what you want to try", {"openness": 5})
    ]),
    tier="consistency_check", cg="o_curiosity_1", opacity=0.4))

questions.append(q("openness", "forced_choice",
    "Which is a bigger loss?",
    opts([
        ("Living a predictable, comfortable life and missing out on extraordinary experiences", {"openness": 5}),
        ("Chasing novelty and never building deep roots or mastery in one thing", {"openness": 1})
    ]),
    tier="core", cg="o_art_1", opacity=0.75))

questions.append(q("openness", "behavioral_recall",
    "How often do you find beauty or meaning in things other people walk right past?",
    opts([
        ("All the time — the world is endlessly interesting if you pay attention", {"openness": 5}),
        ("Regularly — I notice more than most people", {"openness": 4}),
        ("Sometimes — when something catches my eye", {"openness": 2}),
        ("Rarely — I'm more focused on practical matters", {"openness": 1})
    ]),
    tier="triangulation", cg="o_art_1", opacity=0.6))

# ============================================================
# CONSCIENTIOUSNESS (30)
# ============================================================

questions.append(q("conscientiousness", "behavioral_recall",
    "Look at your desk/workspace right now. How organized is it?",
    opts([
        ("Meticulously organized — everything has a place", {"conscientiousness": 5}),
        ("Tidy enough — I can find what I need", {"conscientiousness": 4}),
        ("A bit messy but I know where things are", {"conscientiousness": 2}),
        ("I'd rather not describe it", {"conscientiousness": 1})
    ]),
    tier="core", cg="c_organization_1", opacity=0.5))

questions.append(q("conscientiousness", "scenario",
    "You have a project due in two weeks. On day one, you:",
    opts([
        ("Create a detailed plan with milestones and start immediately", {"conscientiousness": 5}),
        ("Think about the approach and start within a few days", {"conscientiousness": 4}),
        ("Know you should start but get distracted by other things", {"conscientiousness": 2}),
        ("Tell yourself you work better under pressure and wait until the last few days", {"conscientiousness": 1})
    ]),
    tier="core", cg="c_discipline_1", opacity=0.55))

questions.append(q("conscientiousness", "somatic",
    "When you have an unfinished task hanging over you, your body:",
    opts([
        ("Carries a persistent low-level tension until it's done", {"conscientiousness": 5}),
        ("Notices it occasionally but can put it aside when needed", {"conscientiousness": 3}),
        ("Barely registers it — you'll get to it when you get to it", {"conscientiousness": 1}),
        ("Feels stressed about it but not enough to actually do it", {"conscientiousness": 2})
    ]),
    tier="core", cg="c_discipline_1", opacity=0.7))

questions.append(q("conscientiousness", "forced_choice",
    "When packing for a trip, you:",
    opts([
        ("Have a packing list and check everything off", {"conscientiousness": 5}),
        ("Throw things in a bag the night before and hope for the best", {"conscientiousness": 1})
    ]),
    tier="core", cg="c_organization_1", opacity=0.55))

questions.append(q("conscientiousness", "behavioral_recall",
    "How often do you arrive late to things?",
    opts([
        ("Almost never — I'm usually 5-10 minutes early", {"conscientiousness": 5}),
        ("Rarely — when I am late, I have a genuine reason", {"conscientiousness": 4}),
        ("Sometimes — I'm not great with time but I try", {"conscientiousness": 2}),
        ("Frequently — it's a known thing about me", {"conscientiousness": 1})
    ]),
    tier="triangulation", cg="c_dependability_1", opacity=0.5))

questions.append(q("conscientiousness", "scenario",
    "You notice a small mistake in a report that probably nobody else will catch. It would take 30 minutes to fix. You:",
    opts([
        ("Fix it — if it's not right, it's not done", {"conscientiousness": 5}),
        ("Fix it, but grumble about perfectionism", {"conscientiousness": 4}),
        ("Weigh the effort vs. the risk of someone noticing — probably leave it", {"conscientiousness": 2}),
        ("Leave it — close enough is good enough", {"conscientiousness": 1})
    ]),
    tier="core", cg="c_discipline_1", opacity=0.6))

questions.append(q("conscientiousness", "partner_perspective",
    "Your partner asks you to handle something important while they're away. They come back to find:",
    opts([
        ("It's done, documented, and you've anticipated follow-up needs", {"conscientiousness": 5}),
        ("It's done, competently", {"conscientiousness": 4}),
        ("It's mostly done — you got sidetracked but the main thing is handled", {"conscientiousness": 2}),
        ("You forgot about it entirely", {"conscientiousness": 1})
    ]),
    tier="triangulation", cg="c_dependability_1", opacity=0.55))

questions.append(q("conscientiousness", "temporal",
    "Think about your New Year's resolutions or personal goals from last January. How many did you follow through on?",
    opts([
        ("Most of them — I set realistic goals and track them", {"conscientiousness": 5}),
        ("Some — I started strong and kept up the ones that mattered most", {"conscientiousness": 3}),
        ("One, maybe — the enthusiasm faded by February", {"conscientiousness": 2}),
        ("I stopped making resolutions because I never follow through", {"conscientiousness": 1})
    ]),
    tier="core", cg="c_discipline_1", opacity=0.6))

questions.append(q("conscientiousness", "somatic",
    "When your environment is messy or chaotic, your body:",
    opts([
        ("Gets agitated until you organize it", {"conscientiousness": 5}),
        ("Feels slightly uncomfortable — you'll clean eventually", {"conscientiousness": 3}),
        ("Doesn't notice or care", {"conscientiousness": 1}),
        ("Feels overwhelmed but you don't know where to start", {"conscientiousness": 2})
    ]),
    tier="triangulation", cg="c_organization_1", opacity=0.6))

questions.append(q("conscientiousness", "behavioral_recall",
    "How detailed are your plans before you start something new (a trip, a project, a recipe)?",
    opts([
        ("Very — I plan extensively before acting", {"conscientiousness": 5}),
        ("Moderately — I have a framework but leave room for improvisation", {"conscientiousness": 3}),
        ("Minimal — I figure it out as I go", {"conscientiousness": 2}),
        ("What plans? I just dive in", {"conscientiousness": 1})
    ]),
    tier="core", cg="c_organization_1", opacity=0.55))

questions.append(q("conscientiousness", "scenario",
    "You commit to helping someone move next weekend. By Friday, you're exhausted and don't feel like it. You:",
    opts([
        ("Show up — you said you would", {"conscientiousness": 5}),
        ("Show up but help for less time than originally planned", {"conscientiousness": 3}),
        ("Cancel with an apologetic excuse", {"conscientiousness": 2}),
        ("Don't show up and feel bad about it", {"conscientiousness": 1})
    ]),
    tier="core", cg="c_dependability_1", opacity=0.6))

questions.append(q("conscientiousness", "forced_choice",
    "Which is more you?",
    opts([
        ("I'd rather do something right than do it fast", {"conscientiousness": 5}),
        ("I'd rather do something fast than get bogged down in perfectionism", {"conscientiousness": 2})
    ]),
    tier="consistency_check", cg="c_discipline_1", opacity=0.7))

questions.append(q("conscientiousness", "trap",
    "People describe you as 'reliable.' This feels:",
    opts([
        ("Accurate and important — reliability is a core value", {"conscientiousness": 5}),
        ("Nice but you know you're not as reliable as they think", {"conscientiousness": 2}),
        ("Boring — you'd rather be described as creative or spontaneous", {"conscientiousness": 2}),
        ("Like pressure — you hate the expectation that comes with being the 'reliable' one", {"conscientiousness": 3})
    ]),
    tier="trap", trap=True, cg="c_dependability_1", opacity=0.55))

questions.append(q("conscientiousness", "partner_perspective",
    "Your partner leaves dishes in the sink, clothes on the floor, and doesn't make the bed. Your reaction:",
    opts([
        ("It drives you crazy and you either clean it or bring it up regularly", {"conscientiousness": 5}),
        ("You notice it but it's not worth fighting about", {"conscientiousness": 3}),
        ("You genuinely don't care — life's too short to worry about dishes", {"conscientiousness": 1}),
        ("You're the one leaving the dishes — so you can't really complain", {"conscientiousness": 1})
    ]),
    tier="triangulation", cg="c_organization_1", opacity=0.45))

questions.append(q("conscientiousness", "scenario",
    "You're working on a creative project with no deadline and no boss. How consistently do you work on it?",
    opts([
        ("Daily or near-daily — I set my own schedule and stick to it", {"conscientiousness": 5}),
        ("Several times a week when motivation hits", {"conscientiousness": 3}),
        ("In bursts — I'll go weeks without touching it, then have a productive weekend", {"conscientiousness": 2}),
        ("I have a dozen started projects that never got finished", {"conscientiousness": 1})
    ]),
    tier="core", cg="c_discipline_1", opacity=0.65))

questions.append(q("conscientiousness", "behavioral_recall",
    "How many abandoned projects, half-read books, or unfinished tasks are currently in your life?",
    opts([
        ("Very few — I finish what I start", {"conscientiousness": 5}),
        ("A handful — mostly low-priority things I'll get to eventually", {"conscientiousness": 3}),
        ("More than I'd like to admit", {"conscientiousness": 2}),
        ("I'm surrounded by unfinished things and it doesn't really bother me", {"conscientiousness": 1})
    ]),
    tier="consistency_check", cg="c_discipline_1", opacity=0.55))

questions.append(q("conscientiousness", "temporal",
    "When you look back at your track record with commitments (jobs, relationships, goals), how consistent have you been?",
    opts([
        ("Very — when I commit, I follow through. My track record proves it", {"conscientiousness": 5}),
        ("Mostly — I've had a few lapses but the overall trend is reliable", {"conscientiousness": 4}),
        ("Mixed — some things I nailed, others I dropped", {"conscientiousness": 2}),
        ("Honestly, consistency is my biggest weakness", {"conscientiousness": 1})
    ]),
    tier="core", cg="c_dependability_1", opacity=0.7))

questions.append(q("conscientiousness", "somatic",
    "When you accomplish something you've been working hard on, your body:",
    opts([
        ("Settles with deep satisfaction — the payoff of sustained effort", {"conscientiousness": 5}),
        ("Feels brief pleasure before thinking about what's next", {"conscientiousness": 4}),
        ("Feels surprised — you weren't sure you'd actually finish", {"conscientiousness": 2}),
        ("Rarely gets to experience this because you usually move on before finishing", {"conscientiousness": 1})
    ]),
    tier="triangulation", cg="c_discipline_1", opacity=0.65))

questions.append(q("conscientiousness", "scenario",
    "You realize you double-booked two commitments. You:",
    opts([
        ("This wouldn't happen — I use a calendar religiously", {"conscientiousness": 5}),
        ("Immediately contact both parties, apologize, and figure out a solution", {"conscientiousness": 4}),
        ("Attend whichever is more important and send a vague excuse to the other", {"conscientiousness": 2}),
        ("Honestly, this happens to you more often than it should", {"conscientiousness": 1})
    ]),
    tier="triangulation", cg="c_organization_1", opacity=0.5))

questions.append(q("conscientiousness", "forced_choice",
    "When doing a task, you're more likely to:",
    opts([
        ("Check the instructions carefully before starting", {"conscientiousness": 5}),
        ("Figure it out as you go — instructions are suggestions", {"conscientiousness": 1})
    ]),
    tier="consistency_check", cg="c_organization_1", opacity=0.6))

questions.append(q("conscientiousness", "behavioral_recall",
    "How do you handle tedious but necessary tasks (taxes, paperwork, admin)?",
    opts([
        ("Schedule them, do them systematically, feel satisfied when they're done", {"conscientiousness": 5}),
        ("Procrastinate some but always get them done before deadlines", {"conscientiousness": 3}),
        ("Wait until the last possible moment or until penalties are imminent", {"conscientiousness": 1}),
        ("Often need someone else to remind or help you", {"conscientiousness": 1})
    ]),
    tier="core", cg="c_discipline_1", opacity=0.55))

questions.append(q("conscientiousness", "partner_perspective",
    "If your partner had to rate your follow-through on a scale of 1-10, what would they honestly say?",
    opts([
        ("9-10 — they can count on me completely", {"conscientiousness": 5}),
        ("7-8 — solid but not perfect", {"conscientiousness": 4}),
        ("5-6 — depends on the task", {"conscientiousness": 2}),
        ("Below 5 — and it's been a source of friction", {"conscientiousness": 1})
    ]),
    tier="consistency_check", cg="c_dependability_1", opacity=0.65))

questions.append(q("conscientiousness", "scenario",
    "You find a wallet on the ground with cash and an ID. No one's around. You:",
    opts([
        ("Track down the owner, return it with everything intact", {"conscientiousness": 5}),
        ("Turn it in to a nearby business or authority", {"conscientiousness": 4}),
        ("Take the cash and leave the wallet somewhere visible", {"conscientiousness": 1}),
        ("Leave it where it is — not your problem", {"conscientiousness": 1})
    ]),
    tier="core", cg="c_dependability_1", opacity=0.55, cross=[{"dimension": "agreeableness", "weight": 0.3}]))

questions.append(q("conscientiousness", "temporal",
    "Think about your health habits (exercise, sleep, diet). How structured are they?",
    opts([
        ("Very — I have routines and stick to them", {"conscientiousness": 5}),
        ("Somewhat — I try but consistency varies", {"conscientiousness": 3}),
        ("Not very — I do what I feel like day to day", {"conscientiousness": 2}),
        ("Chaotic — no routine, reactive to whatever happens", {"conscientiousness": 1})
    ]),
    tier="triangulation", cg="c_discipline_1", opacity=0.5))

questions.append(q("conscientiousness", "trap",
    "Someone calls you 'too uptight' about details. You:",
    opts([
        ("Take it as a compliment — details matter", {"conscientiousness": 5}),
        ("Consider whether they have a point", {"conscientiousness": 3}),
        ("Agree — you wish you could relax more", {"conscientiousness": 4}),
        ("Shrug — you've never been called that", {"conscientiousness": 1})
    ]),
    tier="trap", trap=True, cg="c_organization_1", opacity=0.55))

questions.append(q("conscientiousness", "somatic",
    "When you break a promise — even a small one — your body:",
    opts([
        ("Burns with guilt — your word means everything to you", {"conscientiousness": 5}),
        ("Feels a twinge of discomfort that motivates you to make it right", {"conscientiousness": 4}),
        ("Notes it but moves on — it happens", {"conscientiousness": 2}),
        ("Barely registers — promises are aspirational, not binding", {"conscientiousness": 1})
    ]),
    tier="core", cg="c_dependability_1", opacity=0.7))

questions.append(q("conscientiousness", "behavioral_recall",
    "How many systems do you have in place to keep yourself organized (calendars, lists, apps, routines)?",
    opts([
        ("Multiple integrated systems — my life runs on structure", {"conscientiousness": 5}),
        ("A few key ones that cover the basics", {"conscientiousness": 4}),
        ("I try to use them but keep falling off", {"conscientiousness": 2}),
        ("None — I rely on memory and momentum", {"conscientiousness": 1})
    ]),
    tier="consistency_check", cg="c_organization_1", opacity=0.5))

questions.append(q("conscientiousness", "scenario",
    "You're in the middle of a project and suddenly get inspired by a completely different idea. You:",
    opts([
        ("Note the idea for later and stay focused on the current project", {"conscientiousness": 5}),
        ("Take 15 minutes to explore the new idea, then refocus", {"conscientiousness": 3}),
        ("Abandon the current project — the new idea is too exciting", {"conscientiousness": 1}),
        ("Start working on both simultaneously and finish neither on time", {"conscientiousness": 1})
    ]),
    tier="triangulation", cg="c_discipline_1", opacity=0.55))

questions.append(q("conscientiousness", "forced_choice",
    "Which bugs you more?",
    opts([
        ("Someone who does sloppy work", {"conscientiousness": 5}),
        ("Someone who takes forever because they're obsessing over details", {"conscientiousness": 1})
    ]),
    tier="triangulation", cg="c_discipline_1", opacity=0.65))

# ============================================================
# EXTRAVERSION (30)
# ============================================================

questions.append(q("extraversion", "scenario",
    "After a full day of meetings and social interaction, you feel:",
    opts([
        ("Energized — people give you energy", {"extraversion": 5}),
        ("Tired but satisfied — good day", {"extraversion": 3}),
        ("Drained — you need significant alone time to recover", {"extraversion": 1}),
        ("Overstimulated — too many people for too long", {"extraversion": 1})
    ]),
    tier="core", cg="e_energy_1", opacity=0.55))

questions.append(q("extraversion", "behavioral_recall",
    "On a typical Friday night, what sounds most appealing?",
    opts([
        ("A party or bar with a big group — the more the merrier", {"extraversion": 5}),
        ("Dinner and drinks with 3-4 close friends", {"extraversion": 3}),
        ("A quiet evening with one person or alone", {"extraversion": 1}),
        ("Whatever happens — you're flexible", {"extraversion": 3})
    ]),
    tier="core", cg="e_sociability_1", opacity=0.45))

questions.append(q("extraversion", "somatic",
    "Walking into a room full of strangers at a networking event, your body:",
    opts([
        ("Lights up — fresh faces, new possibilities", {"extraversion": 5}),
        ("Feels moderately comfortable after a brief warm-up period", {"extraversion": 3}),
        ("Tenses — you need a moment to find your footing", {"extraversion": 2}),
        ("Wants to turn around and leave immediately", {"extraversion": 1})
    ]),
    tier="core", cg="e_sociability_1", opacity=0.6))

questions.append(q("extraversion", "forced_choice",
    "You recharge your batteries by:",
    opts([
        ("Being around people", {"extraversion": 5}),
        ("Being alone", {"extraversion": 1})
    ]),
    tier="core", cg="e_energy_1", opacity=0.8))

questions.append(q("extraversion", "scenario",
    "You're working from home and haven't spoken to anyone in person for three days. You feel:",
    opts([
        ("Stir-crazy — you need human interaction badly", {"extraversion": 5}),
        ("Fine but starting to miss people", {"extraversion": 3}),
        ("Perfectly content — maybe even refreshed", {"extraversion": 1}),
        ("Wish it could last longer", {"extraversion": 1})
    ]),
    tier="triangulation", cg="e_energy_1", opacity=0.6))

questions.append(q("extraversion", "behavioral_recall",
    "How often do you initiate social plans?",
    opts([
        ("Constantly — I'm the one organizing things", {"extraversion": 5}),
        ("Regularly — I like bringing people together", {"extraversion": 4}),
        ("Sometimes — I'll join if invited more often than I initiate", {"extraversion": 2}),
        ("Rarely — I wait for invitations and often say no even then", {"extraversion": 1})
    ]),
    tier="core", cg="e_sociability_1", opacity=0.5))

questions.append(q("extraversion", "partner_perspective",
    "Your partner wants to throw a big surprise party for you. Your honest reaction would be:",
    opts([
        ("Thrilled — what a gift to have everyone you love in one room", {"extraversion": 5}),
        ("Touched but mildly anxious about being the center of attention", {"extraversion": 3}),
        ("Uncomfortable — please don't do this to me", {"extraversion": 1}),
        ("Horrified — this is literally your nightmare", {"extraversion": 1})
    ]),
    tier="triangulation", cg="e_energy_1", opacity=0.55))

questions.append(q("extraversion", "temporal",
    "Looking back at your happiest memories, most of them involve:",
    opts([
        ("Groups of people — celebrations, adventures, shared experiences", {"extraversion": 5}),
        ("Close connections — deep conversations, intimate moments", {"extraversion": 3}),
        ("Solo achievements or quiet experiences in nature/solitude", {"extraversion": 1}),
        ("A mix of all of the above", {"extraversion": 3})
    ]),
    tier="core", cg="e_sociability_1", opacity=0.6))

questions.append(q("extraversion", "somatic",
    "When you're talking in a group and the conversation energy is high — everyone's engaged, laughing, building on each other — your body:",
    opts([
        ("Is fully alive — this is the best feeling in the world", {"extraversion": 5}),
        ("Feels good — you enjoy the energy", {"extraversion": 4}),
        ("Gets tired after a while — you need breaks from high energy", {"extraversion": 2}),
        ("Gets overwhelmed — too much stimulation", {"extraversion": 1})
    ]),
    tier="triangulation", cg="e_energy_1", opacity=0.6))

questions.append(q("extraversion", "scenario",
    "You're on a long flight. The person next to you starts a conversation. You:",
    opts([
        ("Engage enthusiastically — you love meeting random people", {"extraversion": 5}),
        ("Chat politely for a bit, then naturally shift back to your own thing", {"extraversion": 3}),
        ("Put in earbuds as soon as possible — planes are for being alone with your thoughts", {"extraversion": 1}),
        ("Chat if they're interesting, otherwise politely disengage", {"extraversion": 3})
    ]),
    tier="core", cg="e_sociability_1", opacity=0.5))

questions.append(q("extraversion", "behavioral_recall",
    "In group settings, how often are you the one talking?",
    opts([
        ("Most of the time — I naturally dominate conversations", {"extraversion": 5}),
        ("My fair share — I'm comfortable contributing", {"extraversion": 4}),
        ("Less than average — I listen more than I speak", {"extraversion": 2}),
        ("Rarely — I'm usually the quietest person in the room", {"extraversion": 1})
    ]),
    tier="triangulation", cg="e_assertiveness_1", opacity=0.5))

questions.append(q("extraversion", "forced_choice",
    "Which sounds more exhausting?",
    opts([
        ("Spending a whole day alone with no one to talk to", {"extraversion": 5}),
        ("Spending a whole day at a loud, crowded social event", {"extraversion": 1})
    ]),
    tier="consistency_check", cg="e_energy_1", opacity=0.65))

questions.append(q("extraversion", "scenario",
    "You're at a conference. During the break, you:",
    opts([
        ("Work the room — introduce yourself to as many people as possible", {"extraversion": 5}),
        ("Find a few interesting people and have quality conversations", {"extraversion": 3}),
        ("Find a quiet corner to check your phone and decompress", {"extraversion": 1}),
        ("Step outside for fresh air and solitude", {"extraversion": 1})
    ]),
    tier="core", cg="e_sociability_1", opacity=0.5))

questions.append(q("extraversion", "partner_perspective",
    "Your partner is much more/less social than you. How does this play out?",
    opts([
        ("I wish they wanted to go out more — I feel held back", {"extraversion": 5}),
        ("We've found a good balance through compromise", {"extraversion": 3}),
        ("I wish they wanted to stay in more — I feel dragged out", {"extraversion": 1}),
        ("We're pretty well-matched on this", {"extraversion": 3})
    ]),
    tier="triangulation", cg="e_sociability_1", opacity=0.6))

questions.append(q("extraversion", "somatic",
    "Silence in a group — a lull in conversation — makes your body:",
    opts([
        ("Uncomfortable — you rush to fill it", {"extraversion": 5}),
        ("Slightly fidgety but you can sit with it", {"extraversion": 3}),
        ("Relaxed — silence is fine", {"extraversion": 2}),
        ("Relieved — finally a break from talking", {"extraversion": 1})
    ]),
    tier="core", cg="e_assertiveness_1", opacity=0.6))

questions.append(q("extraversion", "temporal",
    "Think about periods in your life when you were most isolated (pandemic, moving to a new city, etc.). How did you handle it?",
    opts([
        ("Badly — isolation is genuinely harmful to my wellbeing", {"extraversion": 5}),
        ("It was tough but I managed by staying connected digitally", {"extraversion": 4}),
        ("Better than expected — I discovered I need less social interaction than I thought", {"extraversion": 2}),
        ("Thrived — some of my most productive, peaceful periods have been solitary", {"extraversion": 1})
    ]),
    tier="core", cg="e_energy_1", opacity=0.65))

questions.append(q("extraversion", "behavioral_recall",
    "How quickly do you share personal news (good or bad) with others?",
    opts([
        ("Immediately — I call someone as soon as it happens", {"extraversion": 5}),
        ("Fairly quickly — within hours to a close friend or two", {"extraversion": 4}),
        ("After I've processed it myself first — sometimes days", {"extraversion": 2}),
        ("Slowly or not at all — I process alone and share selectively if ever", {"extraversion": 1})
    ]),
    tier="triangulation", cg="e_assertiveness_1", opacity=0.6))

questions.append(q("extraversion", "scenario",
    "You move to a new city where you know nobody. Your approach to building a social life is:",
    opts([
        ("Aggressively social — join everything, say yes to everything, meet everyone", {"extraversion": 5}),
        ("Strategic — find 2-3 activities aligned with your interests and let connections form naturally", {"extraversion": 3}),
        ("Slow — you'll meet people eventually through work or routine, no rush", {"extraversion": 2}),
        ("Minimal — you don't need a big social circle to be happy", {"extraversion": 1})
    ]),
    tier="core", cg="e_sociability_1", opacity=0.55))

questions.append(q("extraversion", "forced_choice",
    "In a meeting, you're more likely to:",
    opts([
        ("Think out loud — talking IS how you process ideas", {"extraversion": 5}),
        ("Think silently and speak only when you've formulated your point", {"extraversion": 1})
    ]),
    tier="core", cg="e_assertiveness_1", opacity=0.7))

questions.append(q("extraversion", "trap",
    "Some people describe you as 'quiet' or 'reserved.' How accurate is that?",
    opts([
        ("Not at all — nobody has ever said that about me", {"extraversion": 5}),
        ("Maybe in certain contexts, but I'm talkative once I'm comfortable", {"extraversion": 3}),
        ("Fairly accurate — I choose my words and moments carefully", {"extraversion": 2}),
        ("Very accurate — and I don't see it as a flaw", {"extraversion": 1})
    ]),
    tier="trap", trap=True, cg="e_assertiveness_1", opacity=0.55))

questions.append(q("extraversion", "somatic",
    "Think about the last time you were the center of attention (giving a presentation, being celebrated, telling a story to a group). Your body was:",
    opts([
        ("Buzzing with excitement — you love the spotlight", {"extraversion": 5}),
        ("Nervous but you rose to the occasion", {"extraversion": 3}),
        ("Deeply uncomfortable but you powered through", {"extraversion": 2}),
        ("So stressed you avoid these situations whenever possible", {"extraversion": 1})
    ]),
    tier="triangulation", cg="e_assertiveness_1", opacity=0.6))

questions.append(q("extraversion", "behavioral_recall",
    "How many close friends do you actively maintain?",
    opts([
        ("Many — I have a wide circle of people I'm genuinely close to", {"extraversion": 5}),
        ("Several — quality over quantity but still a healthy number", {"extraversion": 3}),
        ("A few — I invest deeply in a small number of people", {"extraversion": 2}),
        ("One or two — or none, honestly", {"extraversion": 1})
    ]),
    tier="consistency_check", cg="e_sociability_1", opacity=0.5))

questions.append(q("extraversion", "scenario",
    "A friend is throwing a party and asks you to co-host. You:",
    opts([
        ("Jump at the chance — you'll handle music, introductions, and energy", {"extraversion": 5}),
        ("Agree happily — you enjoy the role of making people comfortable", {"extraversion": 4}),
        ("Agree reluctantly — you'll help but you'd rather be a guest", {"extraversion": 2}),
        ("Decline — that sounds like a special kind of hell", {"extraversion": 1})
    ]),
    tier="triangulation", cg="e_sociability_1", opacity=0.5))

questions.append(q("extraversion", "partner_perspective",
    "When you need to solve a problem, you prefer to:",
    opts([
        ("Talk it through with someone — conversation helps you think", {"extraversion": 5}),
        ("Brainstorm with one trusted person", {"extraversion": 3}),
        ("Write it out or think it through alone first, then maybe discuss", {"extraversion": 2}),
        ("Process entirely alone — other people's input confuses your thinking", {"extraversion": 1})
    ]),
    tier="core", cg="e_energy_1", opacity=0.65))

questions.append(q("extraversion", "temporal",
    "As you've gotten older, have you become more or less social?",
    opts([
        ("More — I've learned how much I need people", {"extraversion": 5}),
        ("About the same — my social needs are consistent", {"extraversion": 3}),
        ("Less — I've become more selective and need more alone time", {"extraversion": 2}),
        ("Much less — I've realized I was forcing social behavior that wasn't natural for me", {"extraversion": 1})
    ]),
    tier="consistency_check", cg="e_sociability_1", opacity=0.6))

questions.append(q("extraversion", "scenario",
    "You're waiting in a long line. The person ahead of you starts chatting. You:",
    opts([
        ("Welcome it — lines are boring, people are interesting", {"extraversion": 5}),
        ("Chat casually — it's a pleasant way to pass the time", {"extraversion": 4}),
        ("Respond politely but don't encourage more conversation", {"extraversion": 2}),
        ("Give one-word answers and hope they get the hint", {"extraversion": 1})
    ]),
    tier="triangulation", cg="e_sociability_1", opacity=0.45))

questions.append(q("extraversion", "behavioral_recall",
    "When you have exciting news, how many people do you tell within the first 24 hours?",
    opts([
        ("Everyone — you broadcast it widely", {"extraversion": 5}),
        ("A handful of close people plus a social media post", {"extraversion": 4}),
        ("One or two key people", {"extraversion": 2}),
        ("You sit with it privately for a while before telling anyone", {"extraversion": 1})
    ]),
    tier="consistency_check", cg="e_assertiveness_1", opacity=0.5))

questions.append(q("extraversion", "forced_choice",
    "After a vacation, you feel more rested when you've:",
    opts([
        ("Met interesting people, explored busy places, and had social adventures", {"extraversion": 5}),
        ("Had long stretches of unstructured solitude in a beautiful place", {"extraversion": 1})
    ]),
    tier="core", cg="e_energy_1", opacity=0.65))

questions.append(q("extraversion", "somatic",
    "When your phone rings unexpectedly, your body:",
    opts([
        ("Picks up with curiosity — who is it?", {"extraversion": 4}),
        ("Checks the caller ID, answers if it's someone you want to talk to", {"extraversion": 3}),
        ("Feels a flash of annoyance — let it go to voicemail", {"extraversion": 2}),
        ("Tenses with dread — please no", {"extraversion": 1})
    ]),
    tier="triangulation", cg="e_energy_1", opacity=0.5))

# ============================================================
# AGREEABLENESS (30)
# ============================================================

questions.append(q("agreeableness", "scenario",
    "A coworker takes credit for your idea in a meeting. You:",
    opts([
        ("Let it go — the idea getting traction matters more than who said it", {"agreeableness": 5}),
        ("Mention it privately to the coworker later — not confrontationally, just clarifying", {"agreeableness": 4}),
        ("Speak up in the meeting: 'Actually, I suggested that earlier. Let me expand on it.'", {"agreeableness": 2}),
        ("Call them out publicly — that's intellectually dishonest", {"agreeableness": 1})
    ]),
    tier="core", cg="a_compliance_1", opacity=0.6))

questions.append(q("agreeableness", "behavioral_recall",
    "When someone cuts you off in traffic, your typical response is:",
    opts([
        ("They probably didn't see me — no big deal", {"agreeableness": 5}),
        ("A flash of irritation that fades quickly", {"agreeableness": 4}),
        ("Horn honk and a choice word or gesture", {"agreeableness": 2}),
        ("Road rage — it ruins your mood for the next 20 minutes", {"agreeableness": 1})
    ]),
    tier="core", cg="a_hostility_1", opacity=0.5))

questions.append(q("agreeableness", "somatic",
    "When someone near you is visibly upset (crying on the bus, stressed at work), your body:",
    opts([
        ("Moves toward them — you want to help or at least acknowledge their pain", {"agreeableness": 5}),
        ("Feels compassion but you give them space unless they signal they want help", {"agreeableness": 4}),
        ("Feels uncomfortable and looks away — their emotions are theirs", {"agreeableness": 2}),
        ("Feels nothing — you don't get emotional about strangers", {"agreeableness": 1})
    ]),
    tier="core", cg="a_altruism_1", opacity=0.6))

questions.append(q("agreeableness", "forced_choice",
    "In a negotiation, you naturally tend to:",
    opts([
        ("Find the win-win — everyone should leave feeling good", {"agreeableness": 5}),
        ("Maximize your outcome — that's literally the point of negotiation", {"agreeableness": 1})
    ]),
    tier="core", cg="a_compliance_1", opacity=0.7))

questions.append(q("agreeableness", "partner_perspective",
    "Your partner has a habit that mildly annoys you but doesn't actually affect anything important. You:",
    opts([
        ("Never mention it — it's their quirk and you love them for who they are", {"agreeableness": 5}),
        ("Joke about it affectionately", {"agreeableness": 4}),
        ("Bring it up because small annoyances become big ones over time", {"agreeableness": 2}),
        ("Bring it up directly — why tolerate something that bothers you?", {"agreeableness": 1})
    ]),
    tier="triangulation", cg="a_compliance_1", opacity=0.55))

questions.append(q("agreeableness", "scenario",
    "You find out a friend has been talking about you behind your back — nothing terrible, just mild gossip. You:",
    opts([
        ("Let it go — everyone gossips sometimes, no real harm done", {"agreeableness": 5}),
        ("Mention it casually: 'I heard you were talking about me — what's up?'", {"agreeableness": 3}),
        ("Confront them: 'If you have something to say about me, say it to my face'", {"agreeableness": 1}),
        ("Cut them off — you don't tolerate disloyalty", {"agreeableness": 1})
    ]),
    tier="core", cg="a_trust_1", opacity=0.6))

questions.append(q("agreeableness", "behavioral_recall",
    "How often do you volunteer your time or resources to help someone with no expectation of return?",
    opts([
        ("Frequently — helping others is core to who I am", {"agreeableness": 5}),
        ("Regularly — when the need is genuine and I have capacity", {"agreeableness": 4}),
        ("Occasionally — when it's convenient", {"agreeableness": 2}),
        ("Rarely — my time and resources are for me and mine", {"agreeableness": 1})
    ]),
    tier="core", cg="a_altruism_1", opacity=0.6))

questions.append(q("agreeableness", "somatic",
    "When you witness an argument between two people you know, your body:",
    opts([
        ("Jumps in to mediate — conflict between people you care about is physical discomfort", {"agreeableness": 5}),
        ("Feels tense but you let them work it out unless asked", {"agreeableness": 3}),
        ("Observes with interest — conflict reveals truth", {"agreeableness": 2}),
        ("Enjoys it a little — drama is entertaining", {"agreeableness": 1})
    ]),
    tier="triangulation", cg="a_hostility_1", opacity=0.6))

questions.append(q("agreeableness", "forced_choice",
    "When someone wrongs you, your instinct is to:",
    opts([
        ("Understand why they did it — there's probably a reason", {"agreeableness": 5}),
        ("Hold them accountable — reasons don't excuse behavior", {"agreeableness": 1})
    ]),
    tier="core", cg="a_trust_1", opacity=0.75))

questions.append(q("agreeableness", "scenario",
    "A homeless person asks you for money on the street. You:",
    opts([
        ("Give something every time — they need it more than you", {"agreeableness": 5}),
        ("Sometimes give, depending on the situation", {"agreeableness": 3}),
        ("Rarely give — you donate to organizations instead", {"agreeableness": 2}),
        ("Never give — most of them aren't actually homeless", {"agreeableness": 1})
    ]),
    tier="triangulation", cg="a_altruism_1", opacity=0.5))

questions.append(q("agreeableness", "temporal",
    "How many grudges are you currently holding?",
    opts([
        ("None — I don't hold grudges, life's too short", {"agreeableness": 5}),
        ("Maybe one, and I'm working on releasing it", {"agreeableness": 4}),
        ("A few — some things are hard to forgive", {"agreeableness": 2}),
        ("Several — cross me and I don't forget", {"agreeableness": 1})
    ]),
    tier="core", cg="a_hostility_1", opacity=0.65))

questions.append(q("agreeableness", "partner_perspective",
    "In an argument with your partner, you tend to:",
    opts([
        ("Prioritize the relationship over winning — being right matters less than being connected", {"agreeableness": 5}),
        ("Seek compromise — you hear their side and share yours", {"agreeableness": 4}),
        ("Argue your point thoroughly — if you're right, they need to understand why", {"agreeableness": 2}),
        ("Go for the jugular — if we're fighting, I'm winning", {"agreeableness": 1})
    ]),
    tier="core", cg="a_compliance_1", opacity=0.65))

questions.append(q("agreeableness", "behavioral_recall",
    "How suspicious are you of strangers' motives?",
    opts([
        ("Not at all — I assume good intentions until proven otherwise", {"agreeableness": 5}),
        ("Slightly cautious but generally trusting", {"agreeableness": 4}),
        ("Moderately suspicious — people usually want something", {"agreeableness": 2}),
        ("Very — everyone has an angle", {"agreeableness": 1})
    ]),
    tier="core", cg="a_trust_1", opacity=0.6))

questions.append(q("agreeableness", "scenario",
    "You're in a group making a decision. Everyone else agrees on an option you think is clearly wrong. You:",
    opts([
        ("Go along with it — harmony is more important than being right about this", {"agreeableness": 5}),
        ("Voice your concern once, then go along if nobody agrees", {"agreeableness": 3}),
        ("Push your position — someone needs to be the voice of reason", {"agreeableness": 2}),
        ("Argue until either they come around or you've made your opposition clear", {"agreeableness": 1})
    ]),
    tier="triangulation", cg="a_compliance_1", opacity=0.6))

questions.append(q("agreeableness", "trap",
    "Some people would say you're 'too nice.' Your honest reaction:",
    opts([
        ("Probably fair — I give people too many chances", {"agreeableness": 5}),
        ("Nice isn't weakness — but I see why they'd say it", {"agreeableness": 4}),
        ("Nobody has ever said that about me", {"agreeableness": 1}),
        ("I used to be — not anymore", {"agreeableness": 2})
    ]),
    tier="trap", trap=True, cg="a_trust_1", opacity=0.55))

questions.append(q("agreeableness", "somatic",
    "When you have to deliver criticism or bad news to someone, your body:",
    opts([
        ("Aches — hurting someone's feelings hurts you physically", {"agreeableness": 5}),
        ("Feels uncomfortable but you manage", {"agreeableness": 3}),
        ("Feels nothing unusual — it's a necessary part of life", {"agreeableness": 2}),
        ("Feels fine — if they can't handle truth, that's their problem", {"agreeableness": 1})
    ]),
    tier="core", cg="a_altruism_1", opacity=0.7))

questions.append(q("agreeableness", "forced_choice",
    "Which matters more in a friendship?",
    opts([
        ("Loyalty and emotional support", {"agreeableness": 5}),
        ("Honesty and intellectual challenge", {"agreeableness": 2})
    ]),
    tier="triangulation", cg="a_trust_1", opacity=0.65))

questions.append(q("agreeableness", "behavioral_recall",
    "When someone asks for your honest opinion and you know they won't like the truth, you:",
    opts([
        ("Soften it significantly — their feelings matter more than raw truth", {"agreeableness": 5}),
        ("Tell the truth gently but completely", {"agreeableness": 4}),
        ("Tell the truth directly — they asked for honest, they get honest", {"agreeableness": 2}),
        ("Tell the truth bluntly — sugarcoating is dishonest", {"agreeableness": 1})
    ]),
    tier="core", cg="a_modesty_1", opacity=0.6))

questions.append(q("agreeableness", "scenario",
    "You receive exceptional service at a restaurant. Your server clearly went above and beyond. You:",
    opts([
        ("Leave a huge tip AND speak to the manager to praise them", {"agreeableness": 5}),
        ("Leave a generous tip and thank them warmly", {"agreeableness": 4}),
        ("Leave a standard good tip — that's what tips are for", {"agreeableness": 2}),
        ("Leave what's appropriate — exceptional is their job", {"agreeableness": 1})
    ]),
    tier="triangulation", cg="a_altruism_1", opacity=0.5))

questions.append(q("agreeableness", "temporal",
    "Think about how you handle competitive situations (games, sports, work promotions). You:",
    opts([
        ("Compete but make sure everyone has fun — the experience matters more than winning", {"agreeableness": 5}),
        ("Compete fairly and can genuinely congratulate the winner if it's not you", {"agreeableness": 4}),
        ("Compete to win — that's what competition means", {"agreeableness": 2}),
        ("Compete ruthlessly — second place is first loser", {"agreeableness": 1})
    ]),
    tier="core", cg="a_hostility_1", opacity=0.55))

questions.append(q("agreeableness", "partner_perspective",
    "Your partner tells you they don't like one of your friends. You:",
    opts([
        ("Take it seriously and reconsider the friendship", {"agreeableness": 5}),
        ("Acknowledge their feelings but keep the friendship unless there's a real issue", {"agreeableness": 3}),
        ("Tell them that's their problem — you choose your own friends", {"agreeableness": 1}),
        ("Try to get them to see the good in your friend", {"agreeableness": 4})
    ]),
    tier="triangulation", cg="a_compliance_1", opacity=0.6))

questions.append(q("agreeableness", "behavioral_recall",
    "How comfortable are you saying 'I disagree' directly to someone's face?",
    opts([
        ("Very uncomfortable — I usually find a way to avoid direct disagreement", {"agreeableness": 5}),
        ("Mildly uncomfortable but I do it when it matters", {"agreeableness": 3}),
        ("Fine — disagreement is how ideas get tested", {"agreeableness": 2}),
        ("Easy — I enjoy intellectual sparring", {"agreeableness": 1})
    ]),
    tier="core", cg="a_compliance_1", opacity=0.65))

questions.append(q("agreeableness", "scenario",
    "Someone you barely know needs a ride to the airport at 5 AM. Nobody else is available. You:",
    opts([
        ("Do it without hesitation — they need help", {"agreeableness": 5}),
        ("Do it but you're not thrilled about it", {"agreeableness": 3}),
        ("Suggest they call an Uber — you barely know them", {"agreeableness": 2}),
        ("No — that's a massive inconvenience for an acquaintance", {"agreeableness": 1})
    ]),
    tier="triangulation", cg="a_altruism_1", opacity=0.55))

questions.append(q("agreeableness", "somatic",
    "When someone is rude to a service worker in front of you (waiter, cashier), your body:",
    opts([
        ("Surges with the urge to intervene or say something supportive to the worker", {"agreeableness": 5}),
        ("Feels uncomfortable — you make eye contact with the worker to show solidarity", {"agreeableness": 4}),
        ("Notes it but doesn't react — not your business", {"agreeableness": 2}),
        ("Doesn't notice or care", {"agreeableness": 1})
    ]),
    tier="core", cg="a_altruism_1", opacity=0.6))

questions.append(q("agreeableness", "forced_choice",
    "When someone lies to you, your dominant emotion is:",
    opts([
        ("Hurt — how could they do that to the trust between you?", {"agreeableness": 5}),
        ("Anger — that's disrespectful and they need to know it", {"agreeableness": 1})
    ]),
    tier="consistency_check", cg="a_trust_1", opacity=0.75))

questions.append(q("agreeableness", "trap",
    "An elderly neighbor needs help with yard work regularly. They can't pay you. You:",
    opts([
        ("Help consistently — being a good neighbor is its own reward", {"agreeableness": 5}),
        ("Help when you can — you're busy but you try", {"agreeableness": 3}),
        ("Help once and suggest they hire someone", {"agreeableness": 2}),
        ("This isn't your responsibility — they should make arrangements", {"agreeableness": 1})
    ]),
    tier="trap", trap=True, cg="a_altruism_1", opacity=0.5))

questions.append(q("agreeableness", "temporal",
    "Over the years, has your default level of trust in people gone up or down?",
    opts([
        ("Up — most people prove trustworthy in my experience", {"agreeableness": 5}),
        ("Stayed about the same — cautiously trusting", {"agreeableness": 3}),
        ("Down — experience has taught me to be careful", {"agreeableness": 2}),
        ("Way down — people have shown me who they really are too many times", {"agreeableness": 1})
    ]),
    tier="consistency_check", cg="a_trust_1", opacity=0.65))

questions.append(q("agreeableness", "behavioral_recall",
    "How important is modesty to you — downplaying your achievements rather than drawing attention to them?",
    opts([
        ("Very — bragging makes me deeply uncomfortable", {"agreeableness": 5}),
        ("Somewhat — I'll share achievements but I don't lead with them", {"agreeableness": 4}),
        ("Not very — if I did something impressive, I'll mention it", {"agreeableness": 2}),
        ("Not at all — own your wins", {"agreeableness": 1})
    ]),
    tier="triangulation", cg="a_modesty_1", opacity=0.55))

questions.append(q("agreeableness", "scenario",
    "A friend introduces you to someone and privately warns you 'they can be difficult.' Your approach is:",
    opts([
        ("Give them a clean slate — everyone deserves to be judged on their own behavior with you", {"agreeableness": 5}),
        ("Keep the warning in mind but remain open", {"agreeableness": 4}),
        ("Be cautious from the start — your friend's warning means something", {"agreeableness": 2}),
        ("Avoid the person — why sign up for difficult?", {"agreeableness": 1})
    ]),
    tier="core", cg="a_trust_1", opacity=0.6))

# ============================================================
# NEUROTICISM (30)
# ============================================================

questions.append(q("neuroticism", "scenario",
    "You wake up to an unexpected email from your boss with the subject line 'We need to talk.' Your first thought is:",
    opts([
        ("Must be about that project — let me read it", {"neuroticism": 1}),
        ("Hmm, could be anything — I'll check", {"neuroticism": 2}),
        ("My stomach drops — what did I do wrong?", {"neuroticism": 4}),
        ("Full panic before I even open it — I'm getting fired", {"neuroticism": 5})
    ]),
    tier="core", cg="n_anxiety_1", opacity=0.6))

questions.append(q("neuroticism", "somatic",
    "On an average day with no particular stress, your baseline body state is:",
    opts([
        ("Relaxed and at ease", {"neuroticism": 1}),
        ("Calm with occasional flickers of tension", {"neuroticism": 2}),
        ("Low-level anxiety humming in the background", {"neuroticism": 4}),
        ("Tense, keyed up, waiting for something to go wrong", {"neuroticism": 5})
    ]),
    tier="core", cg="n_anxiety_1", opacity=0.75))

questions.append(q("neuroticism", "behavioral_recall",
    "How often do you catastrophize — imagine the worst possible outcome of a situation?",
    opts([
        ("Almost never — I'm realistic about risk", {"neuroticism": 1}),
        ("Occasionally, when stakes are high", {"neuroticism": 2}),
        ("Regularly — my mind goes to worst case before I can stop it", {"neuroticism": 4}),
        ("My brain's default mode is catastrophe — I have to actively fight it", {"neuroticism": 5})
    ]),
    tier="core", cg="n_anxiety_1", opacity=0.7))

questions.append(q("neuroticism", "forced_choice",
    "When you hear an ambulance siren while a family member is out, you:",
    opts([
        ("Don't connect it to your family member at all", {"neuroticism": 1}),
        ("Think of them for a split second, then dismiss it", {"neuroticism": 2}),
        ("Feel a spike of worry and check your phone", {"neuroticism": 4}),
        ("Can't rest until you've confirmed they're safe", {"neuroticism": 5})
    ]),
    tier="triangulation", cg="n_anxiety_1", opacity=0.65))

questions.append(q("neuroticism", "scenario",
    "You're having a perfectly normal day when a wave of sadness hits you for no apparent reason. You:",
    opts([
        ("That doesn't happen to me", {"neuroticism": 1}),
        ("Notice it, sit with it briefly, and it passes", {"neuroticism": 2}),
        ("It derails my afternoon — I try to figure out what's wrong", {"neuroticism": 4}),
        ("It happens regularly and sometimes spirals into a bad day or week", {"neuroticism": 5})
    ]),
    tier="core", cg="n_depression_1", opacity=0.7))

questions.append(q("neuroticism", "temporal",
    "How stable is your mood on a day-to-day basis?",
    opts([
        ("Very stable — I'm pretty even-keeled", {"neuroticism": 1}),
        ("Mostly stable with occasional dips", {"neuroticism": 2}),
        ("Variable — my mood shifts significantly based on what happens (or doesn't happen) each day", {"neuroticism": 4}),
        ("Volatile — I can go from fine to terrible in the space of a few hours", {"neuroticism": 5})
    ]),
    tier="core", cg="n_depression_1", opacity=0.7))

questions.append(q("neuroticism", "partner_perspective",
    "Your partner would describe your emotional baseline as:",
    opts([
        ("Calm, stable, even-tempered", {"neuroticism": 1}),
        ("Generally steady with occasional stress", {"neuroticism": 2}),
        ("Anxious or moody more often than not", {"neuroticism": 4}),
        ("Frequently overwhelmed or reactive", {"neuroticism": 5})
    ]),
    tier="triangulation", cg="n_anxiety_1", opacity=0.65))

questions.append(q("neuroticism", "somatic",
    "When you're stressed, where does it show up in your body FIRST?",
    opts([
        ("It doesn't have a consistent physical manifestation", {"neuroticism": 1}),
        ("Mild tension — shoulders, jaw — that I can release with awareness", {"neuroticism": 2}),
        ("Stomach issues, headaches, or chest tightness that I can't always shake", {"neuroticism": 4}),
        ("Full-body: can't sleep, can't eat, muscle tension, digestive problems — all of it", {"neuroticism": 5})
    ]),
    tier="core", cg="n_vulnerability_1", opacity=0.7))

questions.append(q("neuroticism", "behavioral_recall",
    "How much of your mental energy on an average day goes to worrying about things that might go wrong?",
    opts([
        ("Very little — I deal with problems when they arise", {"neuroticism": 1}),
        ("Some — normal prudent thinking about risks", {"neuroticism": 2}),
        ("A lot — I'm frequently running 'what if' scenarios", {"neuroticism": 4}),
        ("Most of it — worry is my brain's default activity", {"neuroticism": 5})
    ]),
    tier="core", cg="n_anxiety_1", opacity=0.7))

questions.append(q("neuroticism", "scenario",
    "Something mildly embarrassing happens to you in public (trip on the sidewalk, spill a drink). You:",
    opts([
        ("Laugh it off immediately — everyone trips", {"neuroticism": 1}),
        ("Feel brief embarrassment, move on within minutes", {"neuroticism": 2}),
        ("Cringe and replay it in your mind for the rest of the day", {"neuroticism": 4}),
        ("It ruins your day and you'll think about it again tonight in bed", {"neuroticism": 5})
    ]),
    tier="triangulation", cg="n_self_consciousness_1", opacity=0.55))

questions.append(q("neuroticism", "forced_choice",
    "Your emotional life is more like:",
    opts([
        ("A lake — generally still with occasional ripples", {"neuroticism": 1}),
        ("An ocean — powerful tides, regular storms, deep currents", {"neuroticism": 5})
    ]),
    tier="core", cg="n_depression_1", opacity=0.75))

questions.append(q("neuroticism", "temporal",
    "How often have you been through periods where you felt hopeless or like things would never get better?",
    opts([
        ("Never or very rarely", {"neuroticism": 1}),
        ("Once or twice during major life events", {"neuroticism": 2}),
        ("Several times — it's a recurring pattern", {"neuroticism": 4}),
        ("I'm in one right now, or was recently", {"neuroticism": 5})
    ]),
    tier="core", cg="n_depression_1", opacity=0.75))

questions.append(q("neuroticism", "partner_perspective",
    "When your partner does something that could be interpreted two ways (innocent or hurtful), you tend to assume:",
    opts([
        ("Innocent — I default to good intent", {"neuroticism": 1}),
        ("Innocent, but I'll ask if it happens again", {"neuroticism": 2}),
        ("Hurtful — and I need reassurance it wasn't", {"neuroticism": 4}),
        ("Hurtful — and I react to that interpretation before checking", {"neuroticism": 5})
    ]),
    tier="triangulation", cg="n_hostility_1", opacity=0.65))

questions.append(q("neuroticism", "scenario",
    "You have a medical test scheduled. You're waiting for results. During the waiting period, you:",
    opts([
        ("Go about your life normally — worrying won't change the results", {"neuroticism": 1}),
        ("Think about it occasionally but manage the anxiety", {"neuroticism": 2}),
        ("Can barely focus on anything else — you're googling symptoms", {"neuroticism": 4}),
        ("Are convinced it's the worst-case scenario and are already planning for it", {"neuroticism": 5})
    ]),
    tier="core", cg="n_anxiety_1", opacity=0.65))

questions.append(q("neuroticism", "somatic",
    "When something minor goes wrong (burnt toast, minor traffic, small scheduling conflict), your body's response is:",
    opts([
        ("Proportional — minor inconvenience, minor reaction", {"neuroticism": 1}),
        ("Slightly elevated — a flash of frustration that fades quickly", {"neuroticism": 2}),
        ("Disproportionate — your body reacts as if something major happened", {"neuroticism": 4}),
        ("Full stress response — minor things can trigger the same reaction as major ones", {"neuroticism": 5})
    ]),
    tier="core", cg="n_vulnerability_1", opacity=0.7))

questions.append(q("neuroticism", "behavioral_recall",
    "How often do you lose sleep because of worry?",
    opts([
        ("Almost never — I sleep well regardless of what's happening", {"neuroticism": 1}),
        ("Occasionally — during genuinely stressful periods", {"neuroticism": 2}),
        ("Regularly — racing thoughts keep me awake at least weekly", {"neuroticism": 4}),
        ("Most nights — my mind won't shut off", {"neuroticism": 5})
    ]),
    tier="triangulation", cg="n_anxiety_1", opacity=0.7))

questions.append(q("neuroticism", "scenario",
    "You make a social faux pas at a dinner party — say something awkward or misread the room. Later that night:",
    opts([
        ("You've already forgotten about it", {"neuroticism": 1}),
        ("You think about it once, cringe, and move on", {"neuroticism": 2}),
        ("You replay it multiple times, constructing better things you could have said", {"neuroticism": 4}),
        ("It haunts you for days and makes you dread the next social gathering", {"neuroticism": 5})
    ]),
    tier="triangulation", cg="n_self_consciousness_1", opacity=0.55))

questions.append(q("neuroticism", "forced_choice",
    "When facing a challenge, your default emotional state is:",
    opts([
        ("Calm determination — let's figure this out", {"neuroticism": 1}),
        ("Anxiety-driven urgency — I need to fix this before it gets worse", {"neuroticism": 5})
    ]),
    tier="consistency_check", cg="n_anxiety_1", opacity=0.75))

questions.append(q("neuroticism", "temporal",
    "How resilient are you after a setback (job loss, breakup, failure)?",
    opts([
        ("Very — I bounce back quickly and learn from it", {"neuroticism": 1}),
        ("Moderately — it takes time but I get there", {"neuroticism": 2}),
        ("Slowly — setbacks send me into extended periods of distress", {"neuroticism": 4}),
        ("Barely — each setback feels like it permanently damages me", {"neuroticism": 5})
    ]),
    tier="core", cg="n_vulnerability_1", opacity=0.7))

questions.append(q("neuroticism", "partner_perspective",
    "If your partner forgets something you told them was important to you, your response is:",
    opts([
        ("Remind them calmly — people forget things", {"neuroticism": 1}),
        ("Feel a bit hurt but address it matter-of-factly", {"neuroticism": 2}),
        ("Take it as a sign they don't value you — emotionally shut down or blow up", {"neuroticism": 4}),
        ("It triggers a cascade of 'they don't care about me' thoughts that ruins the whole day", {"neuroticism": 5})
    ]),
    tier="triangulation", cg="n_hostility_1", opacity=0.65))

questions.append(q("neuroticism", "somatic",
    "When you're angry, how quickly can you calm yourself down?",
    opts([
        ("Quickly — I feel the anger, then choose my response", {"neuroticism": 1}),
        ("Within minutes — I need a brief cooldown period", {"neuroticism": 2}),
        ("Slowly — anger lingers and colors my interactions for hours", {"neuroticism": 4}),
        ("I can't — anger takes over and I say or do things I regret", {"neuroticism": 5})
    ]),
    tier="core", cg="n_hostility_1", opacity=0.7))

questions.append(q("neuroticism", "behavioral_recall",
    "How often do you feel overwhelmed by your own emotions — like they're bigger than you can handle?",
    opts([
        ("Rarely or never", {"neuroticism": 1}),
        ("In extreme circumstances only", {"neuroticism": 2}),
        ("Regularly — emotional overwhelm is a recurring experience", {"neuroticism": 4}),
        ("Frequently — I feel at the mercy of my emotions", {"neuroticism": 5})
    ]),
    tier="core", cg="n_vulnerability_1", opacity=0.75))

questions.append(q("neuroticism", "trap",
    "You've been called 'sensitive' before. Your reaction:",
    opts([
        ("Incorrect — I'm actually pretty thick-skinned", {"neuroticism": 1}),
        ("Maybe — but I see it as emotional awareness, not weakness", {"neuroticism": 2}),
        ("Accurate — and it causes me real problems", {"neuroticism": 4}),
        ("Deeply accurate — I feel everything too much and I can't turn it off", {"neuroticism": 5})
    ]),
    tier="trap", trap=True, cg="n_vulnerability_1", opacity=0.6))

questions.append(q("neuroticism", "scenario",
    "Multiple stressful things happen in the same week (car trouble, work deadline, argument with friend). You:",
    opts([
        ("Handle them one at a time — stressors are just problems to solve", {"neuroticism": 1}),
        ("Feel stressed but manage — you prioritize and cope", {"neuroticism": 2}),
        ("Feel overwhelmed — the accumulation tips you into crisis mode", {"neuroticism": 4}),
        ("Shut down completely — too much at once paralyzes you", {"neuroticism": 5})
    ]),
    tier="core", cg="n_vulnerability_1", opacity=0.65))

questions.append(q("neuroticism", "temporal",
    "How much does your self-esteem fluctuate based on daily events?",
    opts([
        ("Very little — my sense of self is stable regardless of what happens", {"neuroticism": 1}),
        ("Slightly — a bad day is just a bad day, not an identity crisis", {"neuroticism": 2}),
        ("Significantly — good day = I'm great, bad day = I'm worthless", {"neuroticism": 4}),
        ("Dramatically — my self-worth is almost entirely determined by what happened today", {"neuroticism": 5})
    ]),
    tier="triangulation", cg="n_self_consciousness_1", opacity=0.7))

questions.append(q("neuroticism", "partner_perspective",
    "When things are going well in your life, do you enjoy it or do you feel anxious that it can't last?",
    opts([
        ("I enjoy it fully — good times are meant to be savored", {"neuroticism": 1}),
        ("Mostly enjoy it with an occasional 'too good to be true' thought", {"neuroticism": 2}),
        ("I'm constantly bracing for the other shoe to drop", {"neuroticism": 4}),
        ("I almost can't enjoy good times because the anticipation of losing them is so strong", {"neuroticism": 5})
    ]),
    tier="core", cg="n_anxiety_1", opacity=0.7))

questions.append(q("neuroticism", "forced_choice",
    "Which describes your relationship with uncertainty?",
    opts([
        ("I'm comfortable not knowing — uncertainty is just part of life", {"neuroticism": 1}),
        ("Uncertainty is my greatest source of distress — I need to know what's going to happen", {"neuroticism": 5})
    ]),
    tier="core", cg="n_anxiety_1", opacity=0.8))

questions.append(q("neuroticism", "behavioral_recall",
    "When you're in a bad mood, how much does it affect the people around you?",
    opts([
        ("Minimally — I can manage my mood without inflicting it on others", {"neuroticism": 1}),
        ("Somewhat — I might be quieter or less patient", {"neuroticism": 2}),
        ("Significantly — my mood fills the room whether I want it to or not", {"neuroticism": 4}),
        ("Dramatically — when I'm upset, everyone knows it and everyone suffers", {"neuroticism": 5})
    ]),
    tier="consistency_check", cg="n_hostility_1", opacity=0.65))

questions.append(q("neuroticism", "scenario",
    "You just completed something you should feel proud of. Instead, you feel:",
    opts([
        ("Proud and satisfied — I earned this", {"neuroticism": 1}),
        ("Good, with a quick thought about what's next", {"neuroticism": 2}),
        ("Relief more than pride — like you barely escaped failure", {"neuroticism": 4}),
        ("Nothing — or worse, a vague emptiness. Achievement doesn't fix the underlying unease", {"neuroticism": 5})
    ]),
    tier="trap", trap=True, cg="n_depression_1", opacity=0.7))


questions.append(q("conscientiousness", "scenario",
    "You promised yourself you'd exercise today. It's 8 PM, you're tired, and the couch is calling. You:",
    opts([
        ("Exercise — a promise to yourself is still a promise", {"conscientiousness": 5}),
        ("Do a shorter version — some effort counts", {"conscientiousness": 3}),
        ("Skip it — tomorrow is another day", {"conscientiousness": 1}),
        ("Didn't have a specific plan to begin with, so there's nothing to skip", {"conscientiousness": 1})
    ]),
    tier="triangulation", cg="c_discipline_1", opacity=0.55))

questions.append(q("extraversion", "behavioral_recall",
    "When you have a problem to solve, do you think better by talking it out or thinking it through silently?",
    opts([
        ("Talking — I literally need to hear myself think", {"extraversion": 5}),
        ("A mix — I start alone but benefit from bouncing ideas off someone", {"extraversion": 3}),
        ("Silently — I need to formulate my thoughts before sharing", {"extraversion": 2}),
        ("Always alone — external input disrupts my process", {"extraversion": 1})
    ]),
    tier="consistency_check", cg="e_energy_1", opacity=0.6))

questions.append(q("agreeableness", "scenario",
    "You witness someone cheating in a game or competition that doesn't affect you personally. You:",
    opts([
        ("Say nothing — not your business", {"agreeableness": 3}),
        ("Feel uncomfortable but stay quiet", {"agreeableness": 4}),
        ("Speak up — fairness matters even when you're not involved", {"agreeableness": 2}),
        ("Call it out loudly — cheating is unacceptable", {"agreeableness": 1})
    ]),
    tier="triangulation", cg="a_compliance_1", opacity=0.55))

questions.append(q("neuroticism", "behavioral_recall",
    "How often do you check things multiple times (locked the door, turned off the stove, sent the email correctly)?",
    opts([
        ("Rarely — I trust myself and move on", {"neuroticism": 1}),
        ("Occasionally — for important things", {"neuroticism": 2}),
        ("Frequently — I don't trust my own memory or attention", {"neuroticism": 4}),
        ("Compulsively — checking things is a significant time drain", {"neuroticism": 5})
    ]),
    tier="triangulation", cg="n_anxiety_1", opacity=0.6))


assert len(questions) == 150, f"Expected 150, got {len(questions)}"

with open("/Users/user/personal/sb/trueassess/priv/question_bank/big_five.json", "w") as f:
    json.dump(questions, f, indent=2)

print(f"Big Five: {len(questions)} questions written")
from collections import Counter
dims = Counter(q["dimension"] for q in questions)
print("Distribution:", dict(dims))
tiers = Counter(q["tier_role"] for q in questions)
print("Tiers:", dict(tiers))
types = Counter(q["question_type"] for q in questions)
print("Types:", dict(types))
