import json

assessment_id = "emotional_regulation"
questions = []
uid_counter = 0

def make_uid():
    global uid_counter
    uid_counter += 1
    return f"er_{uid_counter:03d}"

def make_q(dim, qtype, text, options, tier_role, trap, cgroup, opacity, cross_scores=None, tags=None, depth="moderate", reversal=False, adaptations=None):
    return {
        "uid": make_uid(),
        "assessment_id": assessment_id,
        "dimension": dim,
        "question_type": qtype,
        "text": text,
        "options": options,
        "cross_scores": cross_scores or [],
        "anti_gaming": {
            "opacity": opacity,
            "social_desirability_trap": trap,
            "consistency_group": cgroup,
            "reversal": reversal
        },
        "cultural_adaptability": {
            "universal": True if not adaptations else False,
            "adaptations_needed": adaptations or [],
            "adaptation_notes": None
        },
        "content_rating": "G",
        "content_categories": [],
        "depth_tier": depth,
        "tier_role": tier_role,
        "tags": tags or [assessment_id, dim, tier_role]
    }

def opts(scores_list):
    letters = "abcde"
    return [{"id": letters[i], "text": t, "scores": s} for i, (t, s) in enumerate(scores_list)]

# ============================================================
# DISTRESS TOLERANCE (25 questions)
# ============================================================

questions.append(make_q("distress_tolerance", "scenario",
    "You get a text from your partner that says 'We need to talk when I get home.' You won't see them for 6 hours. What happens in those 6 hours?",
    opts([
        ("I ruminate constantly—texting them back 'about what?', checking my phone obsessively, unable to focus on anything else", {"distress_tolerance": 1}),
        ("Uncomfortable but functional—I feel anxious but can mostly continue my day with periodic dread spikes", {"distress_tolerance": 3}),
        ("I note the anxiety, label it as uncertainty, and redirect my attention—whatever it is can wait 6 hours", {"distress_tolerance": 5}),
        ("I assume the worst, and by the time they get home I've already built a case for whatever I think is coming", {"distress_tolerance": 1, "impulse_control": 1}),
    ]),
    "core", False, "dt_core_1", 0.7, depth="light"))

questions.append(make_q("distress_tolerance", "somatic",
    "When you're sitting with an emotion you can't fix or change—say, grief about something permanent—where does your body want to go?",
    opts([
        ("Fetal position—curl up, make myself small, shut out the world", {"distress_tolerance": 2}),
        ("Movement—I need to walk, clean, exercise, DO something", {"distress_tolerance": 2, "strategy_repertoire": 2}),
        ("I can sit still with it, feeling the weight without needing to escape", {"distress_tolerance": 5}),
        ("To my phone, a drink, food—something that numbs the edge", {"distress_tolerance": 1, "impulse_control": 1}),
    ]),
    "triangulation", False, "dt_somatic_1", 0.7, depth="deep"))

questions.append(make_q("distress_tolerance", "partner_perspective",
    "Your closest person would say that when you're upset, you:",
    opts([
        ("Need to resolve it NOW—can't rest until it's fixed or discussed", {"distress_tolerance": 2, "impulse_control": 2}),
        ("Go quiet and process internally for a while before talking", {"distress_tolerance": 4}),
        ("Cycle between trying to fix it and needing comfort", {"distress_tolerance": 3, "strategy_repertoire": 2}),
        ("Can name what you're feeling and sit with it without spiraling", {"distress_tolerance": 5, "emotional_awareness": 4}),
    ]),
    "consistency_check", False, "dt_partner_1", 0.6))

questions.append(make_q("distress_tolerance", "temporal",
    "Think about the most emotionally painful period of your life. What got you through it day to day?",
    opts([
        ("Distraction—keeping so busy I didn't have time to feel", {"distress_tolerance": 2, "strategy_repertoire": 2}),
        ("Support from others—I couldn't have done it alone", {"distress_tolerance": 3, "strategy_repertoire": 3}),
        ("Just... enduring. Waking up, getting through the day, going back to bed.", {"distress_tolerance": 4}),
        ("I had a breakdown and couldn't function for a significant period", {"distress_tolerance": 1}),
    ]),
    "triangulation", False, "dt_temporal_1", 0.8, depth="deep"))

questions.append(make_q("distress_tolerance", "behavioral_recall",
    "In the past month, how many times have you done something you later regretted because an emotion felt unbearable?",
    opts([
        ("Several times—angry texts, impulsive purchases, eating/drinking to cope", {"distress_tolerance": 1, "impulse_control": 1}),
        ("Once or twice, and I caught the pattern quickly", {"distress_tolerance": 3}),
        ("None that I can recall", {"distress_tolerance": 5}),
        ("I regret things I DIDN'T do—I shut down instead of acting", {"distress_tolerance": 2, "window_of_tolerance": 2}),
    ]),
    "trap", True, "dt_regret_1", 0.5,
    tags=[assessment_id, "distress_tolerance", "trap", "behavioral"]))

questions.append(make_q("distress_tolerance", "forced_choice",
    "You're stuck in an airport for 8 hours with no internet and bad news playing on every screen. You feel dread building. Which is closer to your response?",
    opts([
        ("I find a quiet corner and sit with it—discomfort won't kill me", {"distress_tolerance": 5}),
        ("I desperately look for any distraction—a book, a stranger to talk to, anything", {"distress_tolerance": 2}),
    ]),
    "triangulation", False, "dt_airport_1", 0.6))

questions.append(make_q("distress_tolerance", "scenario",
    "Your best friend is going through something terrible and all they need is for you to listen. But their pain is triggering your own unresolved stuff. Can you stay present?",
    opts([
        ("Yes—I can hold space for them even when it activates my own pain", {"distress_tolerance": 5}),
        ("For a while, but eventually I either redirect to advice-giving or need to excuse myself", {"distress_tolerance": 3}),
        ("I struggle—I end up making it about me without meaning to", {"distress_tolerance": 2, "emotional_awareness": 2}),
        ("I avoid these situations by gently suggesting they talk to a professional", {"distress_tolerance": 2}),
    ]),
    "trap", True, "dt_presence_1", 0.5,
    tags=[assessment_id, "distress_tolerance", "trap", "empathy"]))

questions.append(make_q("distress_tolerance", "somatic",
    "When anxiety peaks—like the night before a big presentation or medical result—what does your body do at 2am?",
    opts([
        ("Full activation: racing heart, churning stomach, can't lie still", {"distress_tolerance": 1, "window_of_tolerance": 1}),
        ("I feel the anxiety but can breathe through it and eventually doze", {"distress_tolerance": 4, "strategy_repertoire": 3}),
        ("I get up and do something productive—might as well use the energy", {"distress_tolerance": 2, "impulse_control": 2}),
        ("I don't really experience this—I sleep fine even when stressed", {"distress_tolerance": 5, "window_of_tolerance": 5}),
    ]),
    "consistency_check", False, "dt_2am_1", 0.7, depth="deep"))

questions.append(make_q("distress_tolerance", "behavioral_recall",
    "When you're in physical pain (bad headache, back pain, toothache), how does it affect your emotional state?",
    opts([
        ("I become irritable and snap at people—pain erodes my emotional reserves", {"distress_tolerance": 2, "window_of_tolerance": 2}),
        ("I get quiet and withdraw—I can handle the pain but can't also handle people", {"distress_tolerance": 3}),
        ("Minimal impact—physical pain and emotional regulation are separate for me", {"distress_tolerance": 5}),
        ("I catastrophize—the pain feels like it will never end and I can't cope", {"distress_tolerance": 1}),
    ]),
    "triangulation", False, "dt_pain_1", 0.7))

questions.append(make_q("distress_tolerance", "temporal",
    "Has your ability to sit with discomfort improved, stayed the same, or gotten worse over the past 5 years?",
    opts([
        ("Improved significantly—through therapy, practice, or life experience", {"distress_tolerance": 4, "strategy_repertoire": 4}),
        ("About the same—I've always been fairly resilient", {"distress_tolerance": 3}),
        ("Gotten worse—life has worn me down and I have less capacity", {"distress_tolerance": 2, "recovery_speed": 2}),
        ("It fluctuates—some periods I'm solid, others I'm paper-thin", {"distress_tolerance": 3, "window_of_tolerance": 2}),
    ]),
    "triangulation", False, "dt_trajectory_1", 0.7))

questions.append(make_q("distress_tolerance", "scenario",
    "You find out a close friend has been talking about you behind your back. You feel a rush of hurt and betrayal. What's your FIRST action?",
    opts([
        ("Call them immediately and confront the situation", {"distress_tolerance": 2, "impulse_control": 1}),
        ("Feel the hurt, let it wash through me, and decide what to do in a day or two", {"distress_tolerance": 5, "impulse_control": 5}),
        ("Vent to another friend to process the feeling before deciding", {"distress_tolerance": 3, "strategy_repertoire": 3}),
        ("Cut them off without a conversation—I know how I feel and I don't need to discuss it", {"distress_tolerance": 2, "impulse_control": 2}),
    ]),
    "trap", True, "dt_betrayal_1", 0.5,
    tags=[assessment_id, "distress_tolerance", "trap", "impulsivity"]))

questions.append(make_q("distress_tolerance", "partner_perspective",
    "How would a therapist who knows you well describe your relationship with emotional pain?",
    opts([
        ("'They avoid it at almost any cost—numbing, distraction, denial'", {"distress_tolerance": 1}),
        ("'They can tolerate it but burn a lot of energy doing so'", {"distress_tolerance": 3}),
        ("'They've developed a healthy capacity to be present with difficult emotions'", {"distress_tolerance": 5}),
        ("'They intellectualize pain rather than feeling it—high functioning but disconnected'", {"distress_tolerance": 2, "emotional_awareness": 1}),
    ]),
    "consistency_check", False, "dt_therapist_1", 0.5, depth="deep"))

questions.append(make_q("distress_tolerance", "scenario",
    "You've been laid off and have 3 months of savings. It's day one. How's your emotional state by bedtime?",
    opts([
        ("Panicked—already spiraling about worst-case scenarios", {"distress_tolerance": 1, "window_of_tolerance": 1}),
        ("Shaky but coping—I made a plan and that helped, but the fear is close to the surface", {"distress_tolerance": 3}),
        ("Surprisingly calm—the initial shock wore off and I'm in pragmatic mode", {"distress_tolerance": 4}),
        ("Numb—I can tell I haven't fully processed it yet", {"distress_tolerance": 2, "emotional_awareness": 2}),
    ]),
    "triangulation", False, "dt_layoff_1", 0.7))

questions.append(make_q("distress_tolerance", "forced_choice",
    "Which statement is more true for you: 'I can handle feeling bad' or 'I need to fix feeling bad'?",
    opts([
        ("'I can handle feeling bad'—emotions are temporary weather", {"distress_tolerance": 5}),
        ("'I need to fix feeling bad'—sitting in it feels pointless and dangerous", {"distress_tolerance": 1}),
    ]),
    "core", False, "dt_core_2", 0.5, depth="light"))

questions.append(make_q("distress_tolerance", "behavioral_recall",
    "The last time you cried, what happened next?",
    opts([
        ("I let it run its course and felt better afterward—crying is release", {"distress_tolerance": 5}),
        ("I tried to stop as quickly as possible—crying feels like losing control", {"distress_tolerance": 2}),
        ("I can't remember the last time I cried", {"distress_tolerance": 2, "emotional_awareness": 1}),
        ("It triggered a spiral—one emotion cascaded into many", {"distress_tolerance": 2, "window_of_tolerance": 1}),
    ]),
    "trap", True, "dt_crying_1", 0.4,
    tags=[assessment_id, "distress_tolerance", "trap", "vulnerability"]))

questions.append(make_q("distress_tolerance", "somatic",
    "When you feel the urge to cry in a public or professional setting, what does your body do?",
    opts([
        ("I clench everything—jaw, fists, core—physically fighting the emotion back", {"distress_tolerance": 2}),
        ("I excuse myself calmly and find a private space", {"distress_tolerance": 4, "strategy_repertoire": 3}),
        ("I let a few tears fall without shame—emotions happen", {"distress_tolerance": 5}),
        ("I dissociate slightly—the emotion feels far away suddenly", {"distress_tolerance": 2, "window_of_tolerance": 1}),
    ]),
    "triangulation", False, "dt_public_cry_1", 0.7, depth="deep"))

questions.append(make_q("distress_tolerance", "temporal",
    "After a major loss (breakup, death, job loss), how long before you could function at 80% capacity again?",
    opts([
        ("Days—I process fast and get back to functioning", {"distress_tolerance": 4, "recovery_speed": 4}),
        ("Weeks—it takes time but I'm resilient", {"distress_tolerance": 3, "recovery_speed": 3}),
        ("Months—major losses knock me off my foundation", {"distress_tolerance": 2, "recovery_speed": 2}),
        ("I'm not sure I ever fully recovered from the last big one", {"distress_tolerance": 1, "recovery_speed": 1}),
    ]),
    "triangulation", False, "dt_recovery_1", 0.7,
    cross_scores=[{"assessment": "emotional_regulation", "dimension": "recovery_speed", "weight": 0.7}]))

questions.append(make_q("distress_tolerance", "scenario",
    "A friend shares devastating news about their health diagnosis. You're sitting across from them at a restaurant. What do you notice in yourself?",
    opts([
        ("My eyes well up and I reach for their hand—I can hold their pain and mine simultaneously", {"distress_tolerance": 5, "emotional_awareness": 4}),
        ("I go into fix-it mode—researching treatment options on my phone, suggesting doctors", {"distress_tolerance": 2, "impulse_control": 2}),
        ("I feel overwhelmed and struggle to say the right thing—their pain is activating mine", {"distress_tolerance": 2}),
        ("I stay composed and supportive on the outside, but I'll fall apart later when I'm alone", {"distress_tolerance": 3}),
    ]),
    "consistency_check", False, "dt_friend_diagnosis_1", 0.7))

questions.append(make_q("distress_tolerance", "behavioral_recall",
    "How often do you use the phrase 'I can't deal with this right now'?",
    opts([
        ("Daily or almost daily—my plate is always too full for new problems", {"distress_tolerance": 1}),
        ("Weekly—some weeks are harder than others", {"distress_tolerance": 2}),
        ("Rarely—I can usually deal with whatever comes", {"distress_tolerance": 4}),
        ("I say it sometimes but it's usually a boundary, not a capacity issue", {"distress_tolerance": 4, "strategy_repertoire": 3}),
    ]),
    "trap", True, "dt_cantdeal_1", 0.5,
    tags=[assessment_id, "distress_tolerance", "trap", "frequency"]))

questions.append(make_q("distress_tolerance", "partner_perspective",
    "A coworker who's seen you under pressure would describe you as:",
    opts([
        ("'Unflappable—you'd never know they were stressed'", {"distress_tolerance": 4}),
        ("'Steady but human—you can tell it affects them but they keep going'", {"distress_tolerance": 4}),
        ("'Reactive—stress comes out sideways in irritability or withdrawal'", {"distress_tolerance": 2}),
        ("'Hard to read—I genuinely don't know how they handle it internally'", {"distress_tolerance": 3, "emotional_awareness": 2}),
    ]),
    "triangulation", False, None, 0.6))

questions.append(make_q("distress_tolerance", "scenario",
    "You're waiting for biopsy results. The doctor's office said they'd call by Friday. It's now Monday. How have you spent the weekend?",
    opts([
        ("Calling the office repeatedly, googling symptoms, barely sleeping", {"distress_tolerance": 1}),
        ("Anxious but managed—I stayed busy and leaned on people for support", {"distress_tolerance": 3, "strategy_repertoire": 3}),
        ("Surprisingly okay—whatever the result, it already is what it is", {"distress_tolerance": 5}),
        ("Numb—I've shut down emotionally as a protective measure", {"distress_tolerance": 2}),
    ]),
    "consistency_check", False, "dt_biopsy_1", 0.7))

questions.append(make_q("distress_tolerance", "forced_choice",
    "Imagine you're told: 'This emotional pain will last exactly 30 more days, then it will lift completely.' Does knowing the timeline help?",
    opts([
        ("Enormously—it's the uncertainty that makes distress unbearable, not the pain itself", {"distress_tolerance": 2}),
        ("Somewhat—knowing there's an end helps but 30 days still feels long", {"distress_tolerance": 3}),
        ("Not much—I can endure pain whether or not I know when it ends", {"distress_tolerance": 5}),
        ("It would make it worse—I'd be counting every day", {"distress_tolerance": 1}),
    ]),
    "triangulation", False, "dt_timeline_1", 0.7))

questions.append(make_q("distress_tolerance", "somatic",
    "Rate the physical sensation: when something goes badly wrong and you can't fix it, does your body feel more like a clenched fist or a deflated balloon?",
    opts([
        ("Clenched fist—tension, activation, fighting against reality", {"distress_tolerance": 2, "window_of_tolerance": 2}),
        ("Deflated balloon—energy drains out and I feel hollow", {"distress_tolerance": 2}),
        ("Neither—more like gentle discomfort that I can hold without it defining my physical state", {"distress_tolerance": 5}),
        ("Both, cycling—first the clench, then the collapse", {"distress_tolerance": 2, "recovery_speed": 2}),
    ]),
    "consistency_check", False, "dt_body_metaphor_1", 0.7, depth="deep"))

questions.append(make_q("distress_tolerance", "behavioral_recall",
    "Think about the last time you were stuck in traffic that was going to make you late to something important. What was your internal experience?",
    opts([
        ("Rage, frustration, horn-honking, cursing—completely disproportionate to the situation", {"distress_tolerance": 1, "impulse_control": 1}),
        ("Frustrated but I called ahead, adjusted expectations, and accepted it", {"distress_tolerance": 4}),
        ("Surprisingly zen—I can't control traffic, so why waste energy being upset?", {"distress_tolerance": 5}),
        ("Anxiety spiraling—imagining all the consequences of being late", {"distress_tolerance": 2}),
    ]),
    "triangulation", False, "dt_traffic_1", 0.7))

questions.append(make_q("distress_tolerance", "temporal",
    "Is there an emotion you've been carrying for years that you haven't fully processed?",
    opts([
        ("Yes—and I know exactly what it is", {"distress_tolerance": 3, "emotional_awareness": 4}),
        ("Probably—I suspect there's something I've been avoiding", {"distress_tolerance": 2, "emotional_awareness": 2}),
        ("No—I process things as they come", {"distress_tolerance": 4}),
        ("Several—I've accumulated unprocessed emotional weight over time", {"distress_tolerance": 2}),
    ]),
    "trap", True, "dt_carrying_1", 0.4,
    tags=[assessment_id, "distress_tolerance", "trap", "depth"]))

# ============================================================
# IMPULSE CONTROL (25 questions)
# ============================================================

questions.append(make_q("impulse_control", "scenario",
    "You're furious at your partner. You have a devastating comeback that would end the argument instantly but cause real damage. The words are right there. What do you do?",
    opts([
        ("I say it—in the moment, winning the argument feels more important than the damage", {"impulse_control": 1}),
        ("I bite it back but it takes enormous effort and I'm visibly straining", {"impulse_control": 3}),
        ("The words don't even form—I've trained myself not to weaponize vulnerability", {"impulse_control": 5}),
        ("I say something close to it but softer—a version that makes my point without the cruelty", {"impulse_control": 3}),
    ]),
    "core", False, "ic_core_1", 0.6, depth="light"))

questions.append(make_q("impulse_control", "somatic",
    "When you feel the urge to say something you know you shouldn't, where in your body do you feel the brake trying to engage?",
    opts([
        ("My throat—like the words are physically stuck", {"impulse_control": 3}),
        ("My chest—a tightening that says 'stop'", {"impulse_control": 3}),
        ("Nowhere—the words are out before any brake engages", {"impulse_control": 1}),
        ("My whole body pauses—there's a full-system 'wait' that kicks in", {"impulse_control": 5}),
    ]),
    "triangulation", False, "ic_somatic_1", 0.7, depth="deep"))

questions.append(make_q("impulse_control", "partner_perspective",
    "If your partner rated 'thinks before speaking when upset' on a 1-10 scale, what would they give you?",
    opts([
        ("2-3—they've told me I shoot from the hip emotionally", {"impulse_control": 1}),
        ("4-5—I try but my filter fails under strong emotion", {"impulse_control": 3}),
        ("6-7—I'm generally measured even when upset", {"impulse_control": 4}),
        ("8-10—I'm known for being deliberate with my words", {"impulse_control": 5}),
    ]),
    "consistency_check", False, "ic_partner_1", 0.5))

questions.append(make_q("impulse_control", "temporal",
    "Think about the last time you said something hurtful in anger. How long between the trigger and the words?",
    opts([
        ("Milliseconds—it was reactive, not chosen", {"impulse_control": 1}),
        ("A few seconds—I felt the impulse, tried to stop, and failed", {"impulse_control": 2}),
        ("I don't think I've said something hurtful in anger recently", {"impulse_control": 5}),
        ("The words came out measured but the intent was still to wound—it was controlled cruelty, not impulsive", {"impulse_control": 3}),
    ]),
    "trap", True, "ic_timing_1", 0.4,
    tags=[assessment_id, "impulse_control", "trap", "honesty"]))

questions.append(make_q("impulse_control", "behavioral_recall",
    "In the past month, how many impulse purchases have you made that you later questioned?",
    opts([
        ("Several—retail therapy is real and I practice it", {"impulse_control": 1}),
        ("One or two—mostly small things", {"impulse_control": 3}),
        ("None—I research everything before buying", {"impulse_control": 5}),
        ("I don't track this closely enough to say", {"impulse_control": 3, "emotional_awareness": 2}),
    ]),
    "triangulation", False, "ic_purchases_1", 0.6))

questions.append(make_q("impulse_control", "forced_choice",
    "You've decided to stop drinking for a month. Day 3: a friend opens a bottle of really good wine. Do you:",
    opts([
        ("Have one glass—one won't hurt and it's really good wine", {"impulse_control": 2}),
        ("Decline—a commitment is a commitment regardless of the temptation", {"impulse_control": 5}),
    ]),
    "triangulation", False, "ic_wine_1", 0.7))

questions.append(make_q("impulse_control", "scenario",
    "You see your ex's new Instagram post with their new partner looking happy. You feel a surge of emotion. Your thumb hovers over the message button. What happens?",
    opts([
        ("I type something and send it before I fully think it through", {"impulse_control": 1}),
        ("I type something, stare at it for a minute, then delete it", {"impulse_control": 3}),
        ("I put the phone down and go do something else", {"impulse_control": 5}),
        ("I don't follow my ex, so this scenario doesn't apply", {"impulse_control": 4}),
    ]),
    "trap", True, "ic_ex_1", 0.5,
    tags=[assessment_id, "impulse_control", "trap", "digital"]))

questions.append(make_q("impulse_control", "somatic",
    "When you successfully stop yourself from a reaction you know you'd regret, what does restraint feel like physically?",
    opts([
        ("Like holding a sneeze—uncomfortable pressure that needs release", {"impulse_control": 3}),
        ("Like a muscle engaging—effortful but manageable", {"impulse_control": 4}),
        ("I barely notice—restraint is automatic at this point", {"impulse_control": 5}),
        ("I don't successfully stop myself often enough to describe it", {"impulse_control": 1}),
    ]),
    "consistency_check", False, "ic_restraint_feel_1", 0.7, depth="deep"))

questions.append(make_q("impulse_control", "behavioral_recall",
    "How often do you check your phone within the first 5 minutes of waking up?",
    opts([
        ("Every single morning—it's the first thing I reach for", {"impulse_control": 2}),
        ("Most mornings, though I've tried to break the habit", {"impulse_control": 2}),
        ("Occasionally—I have a morning routine that doesn't start with screens", {"impulse_control": 4}),
        ("Rarely or never—my phone stays out of the bedroom", {"impulse_control": 5}),
    ]),
    "triangulation", False, "ic_phone_1", 0.6))

questions.append(make_q("impulse_control", "temporal",
    "Compare your impulse control now to 10 years ago. What's changed?",
    opts([
        ("Much better—I've learned the hard way that impulses have consequences", {"impulse_control": 4}),
        ("About the same—I've always been fairly impulsive/deliberate", {"impulse_control": 3}),
        ("Worse in some areas—stress has eroded my willpower", {"impulse_control": 2}),
        ("Better with big things, worse with small things (or vice versa)", {"impulse_control": 3}),
    ]),
    "triangulation", False, "ic_decade_1", 0.7))

questions.append(make_q("impulse_control", "scenario",
    "You're on a diet. A coworker brings in your absolute favorite dessert. You weren't planning to eat any. What happens?",
    opts([
        ("I eat it without much internal debate—life's too short", {"impulse_control": 1}),
        ("I have a small piece as a compromise—deprivation doesn't work for me", {"impulse_control": 3}),
        ("I decline—my commitment to the goal outweighs momentary desire", {"impulse_control": 5}),
        ("I obsess about it all day whether I eat it or not", {"impulse_control": 2, "distress_tolerance": 2}),
    ]),
    "consistency_check", False, "ic_dessert_1", 0.7))

questions.append(make_q("impulse_control", "partner_perspective",
    "Your friends plan something spontaneous. How likely are you to drop everything and join?",
    opts([
        ("Very—spontaneity is my jam, I'll figure out the consequences later", {"impulse_control": 2}),
        ("Depends—if nothing critical is being displaced, I'm in", {"impulse_control": 4}),
        ("Unlikely—I need to plan and I don't like surprises", {"impulse_control": 5}),
        ("I'll say yes and then feel stressed about what I should have been doing", {"impulse_control": 2}),
    ]),
    "trap", True, "ic_spontaneous_1", 0.5,
    tags=[assessment_id, "impulse_control", "trap", "social_framing"]))

questions.append(make_q("impulse_control", "scenario",
    "A heated political argument erupts on social media. You have a perfect reply drafted that would absolutely eviscerate the other person. Your finger is on 'post.' What do you do?",
    opts([
        ("Post it—they deserve the pushback and I nailed the argument", {"impulse_control": 1}),
        ("Save it as a draft, come back in an hour, and decide then", {"impulse_control": 4}),
        ("Delete it—nothing good comes from online arguments", {"impulse_control": 5}),
        ("Tone it down slightly and post—make the point without the brutality", {"impulse_control": 3}),
    ]),
    "triangulation", False, "ic_social_media_1", 0.6))

questions.append(make_q("impulse_control", "somatic",
    "When you resist an impulse successfully, do you feel:",
    opts([
        ("Proud—willpower is a muscle and I just flexed it", {"impulse_control": 5}),
        ("Deprived—the unfulfilled desire lingers and nags", {"impulse_control": 2}),
        ("Nothing particular—impulse control is just... default", {"impulse_control": 5}),
        ("A mix—relief at not giving in, but also mourning what I denied myself", {"impulse_control": 3}),
    ]),
    "triangulation", False, "ic_resist_feel_1", 0.7, depth="moderate"))

questions.append(make_q("impulse_control", "behavioral_recall",
    "How many half-finished projects, unread books, or abandoned hobbies do you currently have?",
    opts([
        ("More than I can count—I'm great at starting things", {"impulse_control": 2}),
        ("A few—I try to finish what I start but life gets in the way", {"impulse_control": 3}),
        ("Very few—I finish what I commit to", {"impulse_control": 5}),
        ("I don't start many things precisely because I know I might not finish them", {"impulse_control": 4}),
    ]),
    "consistency_check", False, "ic_projects_1", 0.6))

questions.append(make_q("impulse_control", "temporal",
    "Think about the worst impulsive decision you've ever made. How long between the impulse and the action?",
    opts([
        ("Seconds—it was over before my brain caught up", {"impulse_control": 1}),
        ("Minutes—I had a brief window and chose wrong", {"impulse_control": 2}),
        ("Hours or days—I talked myself into it rather than out of it", {"impulse_control": 2}),
        ("My worst decisions were deliberate, not impulsive", {"impulse_control": 4}),
    ]),
    "trap", True, "ic_worst_1", 0.4,
    tags=[assessment_id, "impulse_control", "trap", "self_knowledge"]))

questions.append(make_q("impulse_control", "forced_choice",
    "You receive unexpected money. Do you spend it or save it?",
    opts([
        ("Spend a portion and save the rest—a balanced approach", {"impulse_control": 3}),
        ("Save all of it—unexpected money isn't 'extra' money", {"impulse_control": 5}),
        ("Spend it—life's short and you've already budgeted without it", {"impulse_control": 2}),
        ("It depends on whether I have an immediate want vs. a financial goal", {"impulse_control": 4}),
    ]),
    "triangulation", False, None, 0.6))

questions.append(make_q("impulse_control", "scenario",
    "Your partner just said something that felt dismissive. The impulse to escalate is strong. You notice yourself about to match their tone. What happens next?",
    opts([
        ("I match it—if they're going to be dismissive, they get dismissive back", {"impulse_control": 1}),
        ("I pause, take a breath, and say 'That felt dismissive. Can we reset?'", {"impulse_control": 5, "emotional_awareness": 4}),
        ("I go quiet—not a healthy quiet, but a shut-down-to-avoid-explosion quiet", {"impulse_control": 3, "distress_tolerance": 2}),
        ("I name what I'm feeling internally but the words that come out are still reactive", {"impulse_control": 2, "emotional_awareness": 3}),
    ]),
    "core", False, "ic_core_2", 0.6, depth="light"))

questions.append(make_q("impulse_control", "behavioral_recall",
    "When scrolling social media, how often do you look up and realize significantly more time has passed than you intended?",
    opts([
        ("Almost every time—30 minutes disappears like nothing", {"impulse_control": 1}),
        ("Frequently—I set time limits but don't stick to them", {"impulse_control": 2}),
        ("Occasionally—but I've gotten better at catching myself", {"impulse_control": 3}),
        ("Rarely—I have strong screen-time discipline", {"impulse_control": 5}),
    ]),
    "trap", True, "ic_scrolling_1", 0.5,
    tags=[assessment_id, "impulse_control", "trap", "digital"]))

questions.append(make_q("impulse_control", "partner_perspective",
    "If someone who's seen you angry described what happens to your communication, they'd say:",
    opts([
        ("'Volume goes up, filter comes off—they say things they wouldn't normally'", {"impulse_control": 1}),
        ("'They get very controlled and precise—almost cold'", {"impulse_control": 4}),
        ("'They take a break before responding—sometimes frustratingly so'", {"impulse_control": 5}),
        ("'They try to stay measured but you can see the cracks when it's bad enough'", {"impulse_control": 3}),
    ]),
    "consistency_check", False, "ic_anger_comm_1", 0.5))

questions.append(make_q("impulse_control", "scenario",
    "You're trying to have a calm conversation but keep getting interrupted. By the fourth interruption, you:",
    opts([
        ("Raise your voice: 'Will you PLEASE let me finish?!'", {"impulse_control": 2}),
        ("Calmly say: 'I notice I keep getting interrupted. I need to finish my thought.'", {"impulse_control": 5}),
        ("Give up trying to speak and shut down", {"impulse_control": 3, "distress_tolerance": 2}),
        ("Start interrupting them back—see how they like it", {"impulse_control": 1}),
    ]),
    "triangulation", False, "ic_interrupt_1", 0.7))

questions.append(make_q("impulse_control", "somatic",
    "After you've acted on an impulse you shouldn't have, what's the physical aftereffect?",
    opts([
        ("An adrenaline crash—the energy drains and shame fills the vacuum", {"impulse_control": 2}),
        ("Heat in my face—instant regret that I can feel physically", {"impulse_control": 2}),
        ("I don't experience this often enough to know", {"impulse_control": 5}),
        ("A brief 'oh no' followed by rationalization—'it wasn't that bad'", {"impulse_control": 2}),
    ]),
    "triangulation", False, "ic_aftermath_1", 0.7, depth="deep"))

questions.append(make_q("impulse_control", "temporal",
    "Have you ever made a major life decision (moving, quitting a job, ending a relationship) in under 24 hours?",
    opts([
        ("Yes, more than once—and some turned out fine", {"impulse_control": 2}),
        ("Once—and I learned from it", {"impulse_control": 3}),
        ("No—I deliberate extensively on major decisions", {"impulse_control": 5}),
        ("Yes—and every time it was a disaster", {"impulse_control": 1}),
    ]),
    "consistency_check", False, "ic_major_decision_1", 0.6))

questions.append(make_q("impulse_control", "behavioral_recall",
    "How often do you eat when you're not hungry because you're bored, stressed, or emotional?",
    opts([
        ("Daily—food is my go-to comfort and distraction", {"impulse_control": 1}),
        ("A few times a week", {"impulse_control": 2}),
        ("Occasionally—I'm aware of the pattern and working on it", {"impulse_control": 3}),
        ("Rarely—I eat when I'm hungry and stop when I'm full", {"impulse_control": 5}),
    ]),
    "trap", True, "ic_emotional_eating_1", 0.5,
    tags=[assessment_id, "impulse_control", "trap", "consumption"]))

# ============================================================
# EMOTIONAL AWARENESS (25 questions)
# ============================================================

questions.append(make_q("emotional_awareness", "scenario",
    "Someone asks you 'How are you feeling right now?' You have to answer honestly and specifically (not 'fine' or 'good'). How easy is that?",
    opts([
        ("Very easy—I can usually name the specific emotion and what triggered it", {"emotional_awareness": 5}),
        ("Moderate—I can get to a general zone (upset, happy, stressed) but struggle with specifics", {"emotional_awareness": 3}),
        ("Hard—I often don't know what I'm feeling until much later", {"emotional_awareness": 1}),
        ("Depends on the emotion—I'm better with negative ones than positive, or vice versa", {"emotional_awareness": 3}),
    ]),
    "core", False, "ea_core_1", 0.6, depth="light"))

questions.append(make_q("emotional_awareness", "somatic",
    "Can you usually tell the difference between anxiety and excitement in your body?",
    opts([
        ("Yes—anxiety is chest/throat, excitement is chest/belly, and they feel distinctly different", {"emotional_awareness": 5}),
        ("Sometimes—the physical sensations are similar and I have to use context to distinguish", {"emotional_awareness": 3}),
        ("No—they feel identical to me physically", {"emotional_awareness": 2}),
        ("I've never thought about this distinction", {"emotional_awareness": 1}),
    ]),
    "triangulation", False, "ea_anxiety_excitement_1", 0.7, depth="deep"))

questions.append(make_q("emotional_awareness", "partner_perspective",
    "If your partner asked 'What are you feeling?' and you said 'I don't know,' how often would that be genuinely true vs. deflecting?",
    opts([
        ("Genuinely true most of the time—I really don't know", {"emotional_awareness": 1}),
        ("About 50/50—sometimes I genuinely don't know, sometimes I know but don't want to say", {"emotional_awareness": 2}),
        ("Mostly deflecting—I usually know but sharing feels vulnerable", {"emotional_awareness": 4}),
        ("I rarely say 'I don't know' about my feelings—I can usually articulate them", {"emotional_awareness": 5}),
    ]),
    "trap", True, "ea_idk_1", 0.4,
    tags=[assessment_id, "emotional_awareness", "trap", "honesty"]))

questions.append(make_q("emotional_awareness", "temporal",
    "How long after an emotional event do you typically understand what you were really feeling?",
    opts([
        ("In the moment—I'm usually aware of emotions as they happen", {"emotional_awareness": 5}),
        ("Hours—I need time to process before clarity emerges", {"emotional_awareness": 3}),
        ("Days or longer—I sometimes realize weeks later what I was actually feeling", {"emotional_awareness": 1}),
        ("It varies wildly—sometimes instant, sometimes never", {"emotional_awareness": 2}),
    ]),
    "triangulation", False, "ea_delay_1", 0.7))

questions.append(make_q("emotional_awareness", "behavioral_recall",
    "In the past week, how many distinct emotions can you remember experiencing?",
    opts([
        ("Ten or more—I notice a rich emotional landscape throughout each day", {"emotional_awareness": 5}),
        ("Five to nine—the major ones stand out", {"emotional_awareness": 4}),
        ("Two to four—I can remember the big swings", {"emotional_awareness": 2}),
        ("I couldn't name specific distinct emotions from this week", {"emotional_awareness": 1}),
    ]),
    "consistency_check", False, "ea_weekly_range_1", 0.6))

questions.append(make_q("emotional_awareness", "forced_choice",
    "Which is more comfortable for you: being asked 'What do you think about this?' or 'How does this make you feel?'",
    opts([
        ("'What do you think'—I'm much better with thoughts than feelings", {"emotional_awareness": 2}),
        ("'How does this feel'—I'm naturally tuned into my emotional state", {"emotional_awareness": 5}),
        ("Both are equally comfortable", {"emotional_awareness": 4}),
        ("Both are uncomfortable in different ways", {"emotional_awareness": 2}),
    ]),
    "triangulation", False, "ea_think_vs_feel_1", 0.5))

questions.append(make_q("emotional_awareness", "scenario",
    "You snap at your partner over something trivial—leaving a cabinet open. You immediately realize the reaction was disproportionate. Can you identify what's actually bothering you?",
    opts([
        ("Yes, quickly—I can trace the snap back to the real source (work stress, feeling unappreciated, etc.)", {"emotional_awareness": 5}),
        ("Eventually—it takes some reflection but I can usually find the real trigger", {"emotional_awareness": 3}),
        ("I know the cabinet isn't the real issue but I can't put my finger on what is", {"emotional_awareness": 2}),
        ("I didn't even realize the reaction was disproportionate until you framed it that way", {"emotional_awareness": 1}),
    ]),
    "consistency_check", False, "ea_snap_1", 0.7))

questions.append(make_q("emotional_awareness", "somatic",
    "When you're sad, how do you know? What's the signal?",
    opts([
        ("Heaviness—my chest, my eyelids, my whole body feels weighted", {"emotional_awareness": 4}),
        ("I notice tears forming or a lump in my throat", {"emotional_awareness": 4}),
        ("I don't always know I'm sad—sometimes I realize only when someone asks why I'm so quiet", {"emotional_awareness": 2}),
        ("I know because I label it cognitively—I assess the situation and determine I should feel sad", {"emotional_awareness": 2}),
    ]),
    "triangulation", False, "ea_sadness_signal_1", 0.7, depth="deep"))

questions.append(make_q("emotional_awareness", "partner_perspective",
    "Would the people closest to you say you have a 'poker face' or that your emotions are readable?",
    opts([
        ("Poker face—people can't tell what I'm feeling", {"emotional_awareness": 2}),
        ("Readable—my face and body broadcast my emotions clearly", {"emotional_awareness": 4}),
        ("Selectively readable—I can hide some emotions but others leak through", {"emotional_awareness": 3}),
        ("I'm not sure—I've never asked", {"emotional_awareness": 2}),
    ]),
    "triangulation", False, "ea_poker_face_1", 0.6))

questions.append(make_q("emotional_awareness", "behavioral_recall",
    "Do you keep a journal, and if so, how much of it is about your emotional state vs. events?",
    opts([
        ("Yes—heavily emotional; I use it specifically to process feelings", {"emotional_awareness": 5}),
        ("Yes—mostly events with some emotional commentary", {"emotional_awareness": 3}),
        ("No journal, but I process emotions through conversation or art", {"emotional_awareness": 4}),
        ("No journal and no regular emotional processing practice", {"emotional_awareness": 2}),
    ]),
    "consistency_check", False, "ea_journal_1", 0.6))

questions.append(make_q("emotional_awareness", "temporal",
    "Think about the last time you felt 'off' for a whole day but couldn't explain why. How often does this happen?",
    opts([
        ("Frequently—vague unnamed moods are common for me", {"emotional_awareness": 1}),
        ("Occasionally—and when it happens I try to investigate", {"emotional_awareness": 3}),
        ("Rarely—I can usually trace mood shifts to specific causes", {"emotional_awareness": 5}),
        ("I don't really have days where I feel 'off'—my baseline is pretty steady", {"emotional_awareness": 3}),
    ]),
    "trap", True, "ea_offday_1", 0.5,
    tags=[assessment_id, "emotional_awareness", "trap", "frequency"]))

questions.append(make_q("emotional_awareness", "scenario",
    "You're watching a movie and unexpectedly start crying. Can you identify which specific emotion was triggered?",
    opts([
        ("Yes—and I can usually connect it to something personal the scene resonated with", {"emotional_awareness": 5}),
        ("Sort of—I know I'm moved but couldn't say precisely by what", {"emotional_awareness": 3}),
        ("No—I'm surprised by the tears and don't fully understand them", {"emotional_awareness": 2}),
        ("I don't cry at movies", {"emotional_awareness": 2}),
    ]),
    "triangulation", False, "ea_movie_1", 0.7))

questions.append(make_q("emotional_awareness", "forced_choice",
    "Can you distinguish between disappointment and sadness in yourself?",
    opts([
        ("Yes—disappointment has a sharp quality tied to expectations; sadness is deeper and broader", {"emotional_awareness": 5}),
        ("Not reliably—they blend together for me", {"emotional_awareness": 2}),
    ]),
    "core", False, "ea_core_2", 0.5, depth="light"))

questions.append(make_q("emotional_awareness", "somatic",
    "Right now, without changing anything, can you describe what emotion you're currently experiencing?",
    opts([
        ("Yes—I can name it and describe its texture and intensity", {"emotional_awareness": 5}),
        ("I can get close—something like 'curious' or 'calm' or 'slightly anxious'", {"emotional_awareness": 4}),
        ("Not really—I'm just... here, answering questions", {"emotional_awareness": 2}),
        ("I'd say 'neutral' but I'm not sure if neutral counts as an emotion", {"emotional_awareness": 3}),
    ]),
    "triangulation", False, "ea_right_now_1", 0.8, depth="deep"))

questions.append(make_q("emotional_awareness", "behavioral_recall",
    "When someone asks what made you angry, how easily can you trace the chain of emotions that led to the anger?",
    opts([
        ("Very easily—anger is usually my second emotion, after hurt or fear, and I can identify the sequence", {"emotional_awareness": 5}),
        ("With some effort—I know anger is rarely the first feeling but it takes work to find what's underneath", {"emotional_awareness": 3}),
        ("I don't think of anger as having layers—I'm angry because the thing happened", {"emotional_awareness": 1}),
        ("I rarely feel angry, so this doesn't apply well", {"emotional_awareness": 3}),
    ]),
    "trap", True, "ea_anger_chain_1", 0.5,
    tags=[assessment_id, "emotional_awareness", "trap", "layers"]))

questions.append(make_q("emotional_awareness", "partner_perspective",
    "How would a therapist rate your emotional vocabulary—the number of distinct emotional words you regularly use?",
    opts([
        ("Rich—I use specific words like 'wistful,' 'resentful,' 'exhilarated,' 'ashamed'", {"emotional_awareness": 5}),
        ("Adequate—the basics (happy, sad, angry, anxious, frustrated) cover most of it", {"emotional_awareness": 3}),
        ("Limited—I tend to use 'fine,' 'stressed,' 'tired,' and 'annoyed' for most states", {"emotional_awareness": 1}),
        ("Context-dependent—richer in writing than speech", {"emotional_awareness": 3}),
    ]),
    "consistency_check", False, "ea_vocabulary_1", 0.5))

questions.append(make_q("emotional_awareness", "scenario",
    "You're at a party and suddenly want to leave. Can you identify what shifted?",
    opts([
        ("Yes—I can usually pinpoint the trigger (a conversation, a person, energy shift)", {"emotional_awareness": 5}),
        ("I know I'm socially drained but can't identify the specific tipping point", {"emotional_awareness": 3}),
        ("No—I just feel 'done' without understanding why", {"emotional_awareness": 2}),
        ("I push through regardless of what I'm feeling—leaving would be rude", {"emotional_awareness": 1}),
    ]),
    "triangulation", False, "ea_party_1", 0.7))

questions.append(make_q("emotional_awareness", "temporal",
    "Has therapy, meditation, journaling, or other practices improved your ability to name your emotions?",
    opts([
        ("Yes, dramatically—I have a before and after with emotional awareness", {"emotional_awareness": 5, "strategy_repertoire": 4}),
        ("Somewhat—it's a slow process but I'm more aware than I used to be", {"emotional_awareness": 3}),
        ("No—I haven't engaged in those practices", {"emotional_awareness": 2}),
        ("I was already pretty emotionally aware before any formal practice", {"emotional_awareness": 4}),
    ]),
    "consistency_check", False, "ea_growth_1", 0.6))

questions.append(make_q("emotional_awareness", "somatic",
    "Can you tell the difference between hunger, anxiety, and anger in your stomach?",
    opts([
        ("Yes—hunger is hollow, anxiety is fluttering, anger is churning", {"emotional_awareness": 5}),
        ("Usually—but sometimes anxiety and hunger feel similar", {"emotional_awareness": 3}),
        ("Not reliably—my stomach just feels 'bad' in various situations", {"emotional_awareness": 2}),
        ("I've never tried to distinguish between them", {"emotional_awareness": 1}),
    ]),
    "triangulation", False, "ea_stomach_1", 0.7, depth="deep"))

questions.append(make_q("emotional_awareness", "behavioral_recall",
    "When filling out these questions, how aware are you of what emotions this assessment is triggering in you?",
    opts([
        ("Very—I notice self-consciousness, curiosity, occasional discomfort, and minor resistance at certain questions", {"emotional_awareness": 5}),
        ("Somewhat—I'm aware of a general engagement but not tracking specific emotional shifts", {"emotional_awareness": 3}),
        ("Not at all—I'm just answering questions, not feeling particularly emotional about it", {"emotional_awareness": 1}),
        ("Mostly annoyance—these questions feel intrusive", {"emotional_awareness": 3}),
    ]),
    "trap", True, "ea_meta_1", 0.3,
    tags=[assessment_id, "emotional_awareness", "trap", "meta"]))

questions.append(make_q("emotional_awareness", "forced_choice",
    "Mixed emotions (feeling happy AND sad simultaneously): how natural is that experience for you?",
    opts([
        ("Completely natural—I hold multiple emotions regularly", {"emotional_awareness": 5}),
        ("Rare but recognizable when it happens", {"emotional_awareness": 3}),
        ("Confusing—I can only feel one thing at a time", {"emotional_awareness": 1}),
        ("I'm not sure I've experienced this", {"emotional_awareness": 2}),
    ]),
    "consistency_check", False, "ea_mixed_1", 0.6))

questions.append(make_q("emotional_awareness", "scenario",
    "Your child or someone close asks you: 'Why do you seem upset?' but you hadn't realized you were. How do you respond internally?",
    opts([
        ("I check in with myself and often discover they're right—I was carrying an emotion I hadn't noticed", {"emotional_awareness": 2}),
        ("I know what I'm feeling and they're misreading my expression—I'm not upset", {"emotional_awareness": 4}),
        ("Their observation helps me realize I've been suppressing something", {"emotional_awareness": 3}),
        ("I feel defensive—I don't like being read by others", {"emotional_awareness": 2}),
    ]),
    "trap", True, "ea_read_1", 0.4,
    tags=[assessment_id, "emotional_awareness", "trap", "blind_spots"]))

questions.append(make_q("emotional_awareness", "partner_perspective",
    "When you describe an emotional experience to someone, do you tend to describe what happened (narrative) or what you felt (emotional content)?",
    opts([
        ("Mostly narrative—'this happened, then this, then this'", {"emotional_awareness": 2}),
        ("Both—I weave the story with how I felt at each point", {"emotional_awareness": 5}),
        ("Mostly emotional—I focus on the feeling states and may skip details", {"emotional_awareness": 4}),
        ("I tend to analyze rather than narrate or emote—why things happened matters more than the story or the feeling", {"emotional_awareness": 2}),
    ]),
    "triangulation", False, "ea_storytelling_1", 0.6))

questions.append(make_q("emotional_awareness", "behavioral_recall",
    "How quickly can you tell whether physical symptoms (headache, fatigue, stomach ache) have an emotional cause?",
    opts([
        ("Almost immediately—I've mapped my body's emotional signals well", {"emotional_awareness": 5}),
        ("Eventually—after ruling out physical causes, I consider emotional ones", {"emotional_awareness": 3}),
        ("Rarely—I default to physical explanations", {"emotional_awareness": 1}),
        ("I'm learning this connection but it's not automatic yet", {"emotional_awareness": 3}),
    ]),
    "triangulation", False, "ea_psychosomatic_1", 0.7))

# ============================================================
# STRATEGY REPERTOIRE (25 questions)
# ============================================================

questions.append(make_q("strategy_repertoire", "scenario",
    "You just got devastating news and you're alone at home. Walk me through what you do in the first hour.",
    opts([
        ("I have a toolkit: I might breathe, call someone, journal, go outside—I know what works for me", {"strategy_repertoire": 5}),
        ("I'd call one specific person—that's my main strategy for hard things", {"strategy_repertoire": 2}),
        ("Honestly? I'd pour a drink, or eat, or scroll—my coping is mostly numbing", {"strategy_repertoire": 1}),
        ("I'd try to distract myself until the intensity passes, then deal with it", {"strategy_repertoire": 2, "distress_tolerance": 2}),
    ]),
    "core", False, "sr_core_1", 0.6, depth="light"))

questions.append(make_q("strategy_repertoire", "somatic",
    "When you notice your heart rate spiking in a stressful moment, do you have a go-to physical intervention?",
    opts([
        ("Yes—box breathing, cold water on wrists, grounding through feet, or similar", {"strategy_repertoire": 5}),
        ("I know about breathing techniques but rarely remember to use them in the moment", {"strategy_repertoire": 2}),
        ("Not really—I just wait for it to pass", {"strategy_repertoire": 1}),
        ("I exercise afterward—that's my reset", {"strategy_repertoire": 3}),
    ]),
    "triangulation", False, "sr_physical_1", 0.7, depth="deep"))

questions.append(make_q("strategy_repertoire", "partner_perspective",
    "If someone asked your partner 'how does [you] cope with stress?', how many different strategies could they name?",
    opts([
        ("Five or more—I have a visible, varied toolkit", {"strategy_repertoire": 5}),
        ("Two or three—exercise, talking to someone, maybe music or a show", {"strategy_repertoire": 3}),
        ("One—they'd say I get quiet/drink/overwork/one specific thing", {"strategy_repertoire": 1}),
        ("They might struggle to name any—I internalize everything", {"strategy_repertoire": 1}),
    ]),
    "consistency_check", False, "sr_partner_1", 0.6))

questions.append(make_q("strategy_repertoire", "temporal",
    "Compare your emotional regulation toolkit now to five years ago. Has it grown?",
    opts([
        ("Significantly—therapy, books, practice have all added tools", {"strategy_repertoire": 5}),
        ("Somewhat—I've picked up a few things", {"strategy_repertoire": 3}),
        ("Not really—I still rely on the same few things", {"strategy_repertoire": 2}),
        ("It's actually shrunk—strategies that used to work don't anymore", {"strategy_repertoire": 1}),
    ]),
    "triangulation", False, "sr_growth_1", 0.7))

questions.append(make_q("strategy_repertoire", "behavioral_recall",
    "In the past month, how many DIFFERENT strategies have you used to manage difficult emotions? (Exercise, talking to someone, breathing, journaling, meditation, creative expression, etc.)",
    opts([
        ("Five or more different strategies", {"strategy_repertoire": 5}),
        ("Three to four", {"strategy_repertoire": 4}),
        ("One to two", {"strategy_repertoire": 2}),
        ("I mainly just push through or wait it out", {"strategy_repertoire": 1}),
    ]),
    "trap", True, "sr_count_1", 0.5,
    tags=[assessment_id, "strategy_repertoire", "trap", "self_report"]))

questions.append(make_q("strategy_repertoire", "forced_choice",
    "When a strategy isn't working (say, deep breathing isn't calming you down), what do you do?",
    opts([
        ("Switch to something else—I have backup strategies", {"strategy_repertoire": 5}),
        ("Try harder at the same thing—eventually it should work", {"strategy_repertoire": 2}),
        ("Give up on regulating and just ride the emotion out", {"strategy_repertoire": 2, "distress_tolerance": 3}),
        ("I only have one strategy so if that fails, I'm stuck", {"strategy_repertoire": 1}),
    ]),
    "triangulation", False, "sr_flexibility_1", 0.6))

questions.append(make_q("strategy_repertoire", "scenario",
    "Your usual coping mechanisms are all unavailable: can't exercise (injured), can't talk to your person (traveling), can't journal (no privacy). What do you do?",
    opts([
        ("I have other options: meditation, grounding exercises, cold exposure, creative work, cooking", {"strategy_repertoire": 5}),
        ("I'd manage but it would be much harder without my main tools", {"strategy_repertoire": 3}),
        ("I'd probably default to unhealthy coping—eating, drinking, scrolling", {"strategy_repertoire": 1}),
        ("I'd feel trapped and the lack of my tools would make the distress worse", {"strategy_repertoire": 1, "distress_tolerance": 2}),
    ]),
    "consistency_check", False, "sr_unavailable_1", 0.7))

questions.append(make_q("strategy_repertoire", "somatic",
    "Do you have a physical reset button—a specific body-based practice that reliably shifts your emotional state?",
    opts([
        ("Yes—and it's evidence-based: cold shower, specific breathing pattern, yoga pose, etc.", {"strategy_repertoire": 5}),
        ("Sort of—exercise generally helps but I don't have a targeted technique", {"strategy_repertoire": 3}),
        ("Not a physical one—I regulate more through thinking or talking", {"strategy_repertoire": 3}),
        ("No—I don't have a reliable way to shift my emotional state through my body", {"strategy_repertoire": 1}),
    ]),
    "triangulation", False, "sr_reset_1", 0.7, depth="deep"))

questions.append(make_q("strategy_repertoire", "behavioral_recall",
    "Can you name a time when you successfully down-regulated a strong emotion using a specific technique in the moment?",
    opts([
        ("Yes—multiple recent examples with different techniques", {"strategy_repertoire": 5}),
        ("Yes—one or two examples, usually the same technique", {"strategy_repertoire": 3}),
        ("I think so, but I'm not sure what technique I actually used—it might have been luck", {"strategy_repertoire": 2}),
        ("No—strong emotions run their course for me regardless of what I try", {"strategy_repertoire": 1}),
    ]),
    "trap", True, "sr_specific_1", 0.5,
    tags=[assessment_id, "strategy_repertoire", "trap", "specificity"]))

questions.append(make_q("strategy_repertoire", "partner_perspective",
    "A mental health professional assessing your coping skills would say:",
    opts([
        ("'Robust and diversified—they have cognitive, somatic, social, and creative strategies'", {"strategy_repertoire": 5}),
        ("'Adequate but narrow—they rely heavily on one or two approaches'", {"strategy_repertoire": 2}),
        ("'Mostly avoidant—distraction and numbing dominate their toolkit'", {"strategy_repertoire": 1}),
        ("'Growing—they're actively learning new strategies but haven't integrated them all yet'", {"strategy_repertoire": 3}),
    ]),
    "consistency_check", False, "sr_professional_1", 0.5))

questions.append(make_q("strategy_repertoire", "temporal",
    "When you learned a new coping strategy (from a therapist, book, video), did you actually use it regularly?",
    opts([
        ("Yes—I actively practice and integrate new tools", {"strategy_repertoire": 5}),
        ("For a while, then I forgot about it and went back to old patterns", {"strategy_repertoire": 2}),
        ("I know a lot of techniques intellectually but don't actually use them", {"strategy_repertoire": 2}),
        ("I haven't tried to learn new coping strategies", {"strategy_repertoire": 1}),
    ]),
    "trap", True, "sr_integration_1", 0.4,
    tags=[assessment_id, "strategy_repertoire", "trap", "knowledge_vs_practice"]))

questions.append(make_q("strategy_repertoire", "scenario",
    "You're about to give a major presentation and your anxiety is through the roof. What's in your pre-game toolkit?",
    opts([
        ("Breathing exercises, power posing, visualization, a specific playlist, and a grounding mantra", {"strategy_repertoire": 5}),
        ("I pace, review my notes obsessively, and hope for the best", {"strategy_repertoire": 2}),
        ("I tell myself 'it'll be fine' and push through the anxiety", {"strategy_repertoire": 1}),
        ("I have a couple of things that help—maybe breathing and a pep talk from a friend", {"strategy_repertoire": 3}),
    ]),
    "triangulation", False, "sr_presentation_1", 0.7))

questions.append(make_q("strategy_repertoire", "forced_choice",
    "Do you have different strategies for different emotions (one for anger, another for sadness, another for anxiety)?",
    opts([
        ("Yes—I've learned that different emotions respond to different interventions", {"strategy_repertoire": 5}),
        ("Not explicitly—I use the same general approach for most emotions", {"strategy_repertoire": 2}),
    ]),
    "core", False, "sr_core_2", 0.5, depth="light"))

questions.append(make_q("strategy_repertoire", "somatic",
    "Do you know what vagal toning is, and if so, have you practiced it?",
    opts([
        ("Yes, and I practice regularly—humming, cold exposure, specific breathing, etc.", {"strategy_repertoire": 5}),
        ("I've heard of it but haven't integrated it into my practice", {"strategy_repertoire": 3}),
        ("No—what is that?", {"strategy_repertoire": 1}),
        ("I do things that probably tone the vagus nerve but I don't frame it that way", {"strategy_repertoire": 3}),
    ]),
    "triangulation", False, "sr_vagal_1", 0.7, depth="deep"))

questions.append(make_q("strategy_repertoire", "behavioral_recall",
    "Think about the last time you helped someone else regulate their emotions. What tools did you offer them?",
    opts([
        ("Several—breathing together, offering to listen, suggesting a walk, validating their feelings, reframing the situation", {"strategy_repertoire": 5}),
        ("Mostly listening and comforting—'it'll be okay' type support", {"strategy_repertoire": 2}),
        ("I gave them space—I'm not great at helping others regulate", {"strategy_repertoire": 2}),
        ("Advice—I told them what I thought they should do about the situation", {"strategy_repertoire": 1}),
    ]),
    "consistency_check", False, "sr_helping_1", 0.6))

questions.append(make_q("strategy_repertoire", "temporal",
    "Has a strategy that used to work for you stopped working? What did you do?",
    opts([
        ("Yes—I found alternatives because I know regulation requires an evolving toolkit", {"strategy_repertoire": 5}),
        ("Yes—and I struggled until I found a replacement", {"strategy_repertoire": 3}),
        ("Yes—and I haven't replaced it yet", {"strategy_repertoire": 1}),
        ("My strategies have been consistent and still work", {"strategy_repertoire": 3}),
    ]),
    "triangulation", False, "sr_evolved_1", 0.7))

questions.append(make_q("strategy_repertoire", "scenario",
    "You can't sleep because your mind is racing. What's your protocol?",
    opts([
        ("A multi-step approach: body scan, then breathing, then if that fails, get up and journal, then try again", {"strategy_repertoire": 5}),
        ("I put on a podcast or TV show to quiet my mind", {"strategy_repertoire": 2}),
        ("I toss and turn and eventually fall asleep from exhaustion", {"strategy_repertoire": 1}),
        ("I have one technique (counting, breathing, etc.) that sometimes works", {"strategy_repertoire": 3}),
    ]),
    "consistency_check", False, "sr_insomnia_1", 0.7))

questions.append(make_q("strategy_repertoire", "partner_perspective",
    "Would your friends say you have good advice for managing emotions, even if you don't always follow it yourself?",
    opts([
        ("Yes—I know more than I practice, unfortunately", {"strategy_repertoire": 3}),
        ("Yes—and I practice what I preach", {"strategy_repertoire": 5}),
        ("Not really—emotional management isn't my area of expertise", {"strategy_repertoire": 1}),
        ("I'm more of a 'figure it out as I go' person than an advice-giver", {"strategy_repertoire": 2}),
    ]),
    "trap", True, "sr_advice_1", 0.4,
    tags=[assessment_id, "strategy_repertoire", "trap", "knowledge_gap"]))

questions.append(make_q("strategy_repertoire", "behavioral_recall",
    "How many books, courses, or therapy sessions focused specifically on emotional regulation have you engaged with?",
    opts([
        ("Extensive—this is an area I've deliberately invested in", {"strategy_repertoire": 5}),
        ("Some—I've read a book or two or discussed it in therapy", {"strategy_repertoire": 3}),
        ("Minimal—I've absorbed things casually but never focused on it", {"strategy_repertoire": 2}),
        ("None—I regulate emotions the way I always have", {"strategy_repertoire": 1}),
    ]),
    "triangulation", False, "sr_investment_1", 0.6))

questions.append(make_q("strategy_repertoire", "forced_choice",
    "Cognitive reframing (changing how you think about a situation to change how you feel): how natural is this for you?",
    opts([
        ("Very natural—I do it almost automatically", {"strategy_repertoire": 5}),
        ("I can do it with effort but it doesn't come naturally", {"strategy_repertoire": 3}),
        ("I've heard of it but don't practice it", {"strategy_repertoire": 2}),
        ("It feels fake—changing my thoughts doesn't change my feelings", {"strategy_repertoire": 1}),
    ]),
    "triangulation", False, "sr_reframe_1", 0.6))

questions.append(make_q("strategy_repertoire", "scenario",
    "A friend is having a panic attack in front of you. What do you do?",
    opts([
        ("Guide them through grounding: '5 things you can see, 4 you can hear...' or box breathing, staying calm and present", {"strategy_repertoire": 5}),
        ("Try to comfort them verbally while feeling helpless about what specifically to do", {"strategy_repertoire": 2}),
        ("Call 911 or suggest they call their therapist", {"strategy_repertoire": 2}),
        ("Stay calm and present, talk in a low voice, and let them know they're safe", {"strategy_repertoire": 4}),
    ]),
    "consistency_check", False, "sr_panic_1", 0.7))

# ============================================================
# RECOVERY SPEED (25 questions)
# ============================================================

questions.append(make_q("recovery_speed", "scenario",
    "You have a terrible argument with your partner before work. You said things you regret. You have a 9am meeting. How functional are you?",
    opts([
        ("Completely derailed—I can barely focus and everyone can tell something's wrong", {"recovery_speed": 1}),
        ("I compartmentalize enough to function but I'm operating at 60%", {"recovery_speed": 3}),
        ("After 20-30 minutes of settling, I can engage professionally", {"recovery_speed": 4}),
        ("I can switch into work mode fairly quickly—I'll deal with the argument tonight", {"recovery_speed": 5}),
    ]),
    "core", False, "rs_core_1", 0.7, depth="light"))

questions.append(make_q("recovery_speed", "somatic",
    "After a stressful event ends (the presentation is over, the confrontation resolved), how long does the physical activation last?",
    opts([
        ("Minutes—my body calms down quickly once the stressor passes", {"recovery_speed": 5}),
        ("An hour or two—the adrenaline takes time to metabolize", {"recovery_speed": 3}),
        ("The rest of the day—I'm wired even after the event is over", {"recovery_speed": 2}),
        ("Sometimes into the next day—I struggle to come down from high-stress states", {"recovery_speed": 1}),
    ]),
    "triangulation", False, "rs_physical_1", 0.7, depth="deep"))

questions.append(make_q("recovery_speed", "partner_perspective",
    "Your partner would say that after you're upset, you:",
    opts([
        ("Bounce back within minutes—it's almost unsettling how fast you recover", {"recovery_speed": 5}),
        ("Need an hour or so but then you're back to normal", {"recovery_speed": 4}),
        ("Are affected for the rest of the day—the mood lingers", {"recovery_speed": 2}),
        ("Can carry it for days—residual irritability or sadness persists", {"recovery_speed": 1}),
    ]),
    "consistency_check", False, "rs_partner_1", 0.6))

questions.append(make_q("recovery_speed", "temporal",
    "After your last breakup (or major interpersonal loss), how long before you could enjoy a full day without intrusive thoughts about it?",
    opts([
        ("A few days to a week", {"recovery_speed": 5}),
        ("A few weeks", {"recovery_speed": 4}),
        ("Months", {"recovery_speed": 2}),
        ("It's been [time period] and I'm still not there", {"recovery_speed": 1}),
    ]),
    "triangulation", False, "rs_breakup_1", 0.7, depth="deep"))

questions.append(make_q("recovery_speed", "behavioral_recall",
    "Think about the last time someone criticized you unfairly. How many hours before the sting fully faded?",
    opts([
        ("Under an hour—I processed it and moved on", {"recovery_speed": 5}),
        ("A few hours—by bedtime it was mostly gone", {"recovery_speed": 4}),
        ("It lingered for days—I kept replaying it", {"recovery_speed": 2}),
        ("I'm not sure it ever fully faded—I can still feel it now thinking about it", {"recovery_speed": 1}),
    ]),
    "trap", True, "rs_criticism_1", 0.5,
    tags=[assessment_id, "recovery_speed", "trap", "rumination"]))

questions.append(make_q("recovery_speed", "forced_choice",
    "After receiving bad news, you're more likely to:",
    opts([
        ("Feel it intensely for a short time, then stabilize", {"recovery_speed": 5}),
        ("Feel it moderately for a long time—a slow burn rather than a quick flame", {"recovery_speed": 2}),
    ]),
    "triangulation", False, "rs_pattern_1", 0.6))

questions.append(make_q("recovery_speed", "scenario",
    "You make an embarrassing mistake at work—replied all to a personal email, forgot a client name, etc. By lunch, how are you?",
    opts([
        ("Laughing about it—everyone makes mistakes", {"recovery_speed": 5}),
        ("Still cringing but functional—it'll fade by end of day", {"recovery_speed": 4}),
        ("Replaying it obsessively and dreading seeing the people who witnessed it", {"recovery_speed": 2}),
        ("Already composing damage-control messages and unable to focus on other work", {"recovery_speed": 1}),
    ]),
    "consistency_check", False, "rs_embarrass_1", 0.7))

questions.append(make_q("recovery_speed", "somatic",
    "After crying, how quickly does your body return to baseline (no more tight throat, normal breathing, stable energy)?",
    opts([
        ("Within minutes—crying is a quick release for me", {"recovery_speed": 5}),
        ("30 minutes to an hour—I feel drained but gradually recover", {"recovery_speed": 3}),
        ("Hours—I feel physically depleted after emotional release", {"recovery_speed": 2}),
        ("I avoid crying specifically because of how long recovery takes", {"recovery_speed": 1}),
    ]),
    "triangulation", False, "rs_crying_1", 0.7, depth="deep"))

questions.append(make_q("recovery_speed", "behavioral_recall",
    "How often do you ruminate—replay upsetting events on a loop?",
    opts([
        ("Constantly—my brain is a broken record for negative events", {"recovery_speed": 1}),
        ("Often—especially at night or during idle time", {"recovery_speed": 2}),
        ("Sometimes—but I have tools to interrupt the loop", {"recovery_speed": 3, "strategy_repertoire": 3}),
        ("Rarely—once I've processed something I can let it go", {"recovery_speed": 5}),
    ]),
    "trap", True, "rs_ruminate_1", 0.5,
    tags=[assessment_id, "recovery_speed", "trap", "rumination"]))

questions.append(make_q("recovery_speed", "partner_perspective",
    "Your friends would say your emotional recovery pattern is:",
    opts([
        ("Quick but maybe too quick—they wonder if I'm actually processing or just suppressing", {"recovery_speed": 4}),
        ("Healthy—I take time to feel it and then move on", {"recovery_speed": 5}),
        ("Slow—moods linger and affect my energy for days", {"recovery_speed": 2}),
        ("Unpredictable—sometimes fast, sometimes devastatingly slow", {"recovery_speed": 2}),
    ]),
    "trap", True, "rs_speed_trap_1", 0.4,
    tags=[assessment_id, "recovery_speed", "trap", "suppression"]))

questions.append(make_q("recovery_speed", "temporal",
    "Do emotional events from years ago still have the power to ruin your day if you think about them?",
    opts([
        ("Yes—certain memories can trigger the full emotional response even years later", {"recovery_speed": 1}),
        ("Sometimes—the intensity has faded but certain triggers can bring it back", {"recovery_speed": 2}),
        ("Rarely—I can revisit painful memories without being overwhelmed", {"recovery_speed": 4}),
        ("No—the past is the past and I've fully processed those events", {"recovery_speed": 5}),
    ]),
    "consistency_check", False, "rs_old_wounds_1", 0.6))

questions.append(make_q("recovery_speed", "scenario",
    "You're rejected for a job you really wanted. It's been one week. How are you?",
    opts([
        ("Already applied to three more and barely thinking about it", {"recovery_speed": 5}),
        ("Disappointed but making progress—the sting is fading", {"recovery_speed": 4}),
        ("Still stewing—questioning my worth and replaying the interview", {"recovery_speed": 2}),
        ("Devastated—rejection hits me at the core and recovery is measured in weeks", {"recovery_speed": 1}),
    ]),
    "triangulation", False, "rs_rejection_1", 0.7))

questions.append(make_q("recovery_speed", "behavioral_recall",
    "After a poor night's sleep due to stress, how many days does it take your emotional baseline to reset?",
    opts([
        ("One good night of sleep and I'm back", {"recovery_speed": 5}),
        ("Two to three days—poor sleep compounds my emotional state", {"recovery_speed": 3}),
        ("A week or more—sleep deprivation sends me into a spiral", {"recovery_speed": 1}),
        ("I'm chronically sleep-deprived so I wouldn't know what my baseline even is", {"recovery_speed": 1}),
    ]),
    "triangulation", False, "rs_sleep_1", 0.7))

questions.append(make_q("recovery_speed", "forced_choice",
    "Which metaphor better describes your emotional recovery?",
    opts([
        ("A rubber band—I stretch and snap back to shape", {"recovery_speed": 5}),
        ("A bruise—it takes time to heal and you can see it while it does", {"recovery_speed": 2}),
    ]),
    "core", False, "rs_core_2", 0.5, depth="light"))

questions.append(make_q("recovery_speed", "somatic",
    "When you wake up the morning after an emotional day, what's your body's state?",
    opts([
        ("Reset—sleep clears the emotional residue for me", {"recovery_speed": 5}),
        ("Heavy—I can feel yesterday's emotions in my body before I'm fully conscious", {"recovery_speed": 2}),
        ("Depends on whether I resolved anything before bed or just collapsed", {"recovery_speed": 3}),
        ("I don't sleep well after emotional days so the exhaustion compounds", {"recovery_speed": 1}),
    ]),
    "consistency_check", False, "rs_morning_after_1", 0.7, depth="deep"))

questions.append(make_q("recovery_speed", "scenario",
    "You witness a car accident (no one seriously hurt). How long before the adrenaline and distress dissipate?",
    opts([
        ("Minutes—once I know everyone's okay, I can move on", {"recovery_speed": 5}),
        ("An hour or so—the shock takes time to wear off", {"recovery_speed": 4}),
        ("Most of the day—I keep replaying it and checking news for updates", {"recovery_speed": 2}),
        ("Days—secondary trauma lingers for me", {"recovery_speed": 1}),
    ]),
    "triangulation", False, "rs_accident_1", 0.7))

questions.append(make_q("recovery_speed", "partner_perspective",
    "If your therapist tracked your emotional recovery time over several months, they'd see:",
    opts([
        ("Consistent and fast—I have reliable recovery patterns", {"recovery_speed": 5}),
        ("Getting faster—I'm actively improving", {"recovery_speed": 4}),
        ("Highly variable—some things I recover from quickly, others take forever", {"recovery_speed": 2}),
        ("Generally slow—I need more recovery time than average", {"recovery_speed": 2}),
    ]),
    "triangulation", False, "rs_therapist_1", 0.6))

questions.append(make_q("recovery_speed", "temporal",
    "Think of the last time you were really angry. How long until you could discuss the issue calmly?",
    opts([
        ("Under an hour", {"recovery_speed": 5}),
        ("A few hours—I needed to cool down but could talk same day", {"recovery_speed": 4}),
        ("The next day—I need to sleep on anger before I can be reasonable", {"recovery_speed": 3}),
        ("Multiple days—anger is one of my stickiest emotions", {"recovery_speed": 1}),
    ]),
    "consistency_check", False, "rs_anger_recovery_1", 0.6))

questions.append(make_q("recovery_speed", "behavioral_recall",
    "How many times in the past month have you woken up still feeling an emotion from the previous day?",
    opts([
        ("Almost never—sleep is a reliable reset for me", {"recovery_speed": 5}),
        ("A few times—usually after particularly intense events", {"recovery_speed": 3}),
        ("Frequently—my emotions carry over between days regularly", {"recovery_speed": 1}),
        ("I'm not sure—I don't track this", {"recovery_speed": 3}),
    ]),
    "triangulation", False, "rs_carryover_1", 0.6))

questions.append(make_q("recovery_speed", "trap",
    "People who recover quickly from emotional events sometimes do so by suppressing rather than processing. Which is more true of you?",
    opts([
        ("I genuinely process quickly—I feel it fully and then it lifts", {"recovery_speed": 5}),
        ("I might be suppressing some things and calling it 'recovery'", {"recovery_speed": 2}),
        ("I process slowly but thoroughly—slow recovery is genuine recovery", {"recovery_speed": 3}),
        ("I honestly can't tell the difference between processing and suppressing", {"recovery_speed": 2, "emotional_awareness": 1}),
    ]),
    "trap", True, "rs_suppress_1", 0.3,
    tags=[assessment_id, "recovery_speed", "trap", "self_honesty"]))

# Fix question_type
questions[-1]["question_type"] = "behavioral_recall"

questions.append(make_q("recovery_speed", "scenario",
    "Your team loses a big contract. Everyone else seems to move on by Wednesday. You're still upset on Friday. Is that a problem?",
    opts([
        ("Yes—I should be able to bounce back faster from professional setbacks", {"recovery_speed": 2}),
        ("No—different people process at different speeds and mine is valid", {"recovery_speed": 3}),
        ("This wouldn't happen to me—I'd be over it by Tuesday", {"recovery_speed": 5}),
        ("It depends on how much I invested in that contract emotionally", {"recovery_speed": 3}),
    ]),
    "triangulation", False, "rs_contract_1", 0.7))

questions.append(make_q("recovery_speed", "somatic",
    "After a period of sustained stress (weeks, not hours), how long does your body take to recalibrate when the stressor lifts?",
    opts([
        ("A day or two—once it's over, I bounce back quickly", {"recovery_speed": 5}),
        ("A week or so—my body holds tension even after my mind has let go", {"recovery_speed": 3}),
        ("Weeks or longer—I often get sick after stressful periods as my body crashes", {"recovery_speed": 1}),
        ("I'm never not stressed, so I can't answer this hypothetically", {"recovery_speed": 1}),
    ]),
    "consistency_check", False, "rs_sustained_1", 0.7, depth="deep"))

questions.append(make_q("recovery_speed", "forced_choice",
    "Would you rather feel intense pain that resolves quickly or mild pain that lasts for months?",
    opts([
        ("Intense and quick—I recover fast so I'd rather get it over with", {"recovery_speed": 5}),
        ("Mild and long—I don't handle intensity well even if it's brief", {"recovery_speed": 2, "distress_tolerance": 2}),
    ]),
    "triangulation", False, "rs_intensity_duration_1", 0.6))

questions.append(make_q("recovery_speed", "behavioral_recall",
    "Think of a significant emotional event from this past week. Rate its current emotional charge on a scale.",
    opts([
        ("Already faded to near-zero—I've processed and moved on", {"recovery_speed": 5}),
        ("Still present but muted—maybe 30% of original intensity", {"recovery_speed": 3}),
        ("Still fairly charged—I haven't fully processed it", {"recovery_speed": 2}),
        ("Nothing significant happened this week, emotionally", {"recovery_speed": 4}),
    ]),
    "consistency_check", False, "rs_this_week_1", 0.6))

# ============================================================
# WINDOW OF TOLERANCE (25 questions)
# ============================================================

questions.append(make_q("window_of_tolerance", "scenario",
    "You're having a normal day when three stressful things happen within an hour: a work deadline moves up, your car makes a weird noise, and your partner texts something passive-aggressive. How do you respond?",
    opts([
        ("I can hold all three without losing functionality—stressful but manageable", {"window_of_tolerance": 5}),
        ("Two I could handle, but the third one tips me over—I snap or shut down", {"window_of_tolerance": 2}),
        ("I'm overwhelmed immediately—the compounding effect is exponential, not additive", {"window_of_tolerance": 1}),
        ("I triage: handle the most urgent, shelve the rest, and deal with them in order", {"window_of_tolerance": 4, "strategy_repertoire": 3}),
    ]),
    "core", False, "wot_core_1", 0.7, depth="light"))

questions.append(make_q("window_of_tolerance", "somatic",
    "When multiple stressors pile up, does your body go into overdrive (hyperarousal) or shut down (hypoarousal)?",
    opts([
        ("Overdrive—racing thoughts, can't sit still, anxiety through the roof", {"window_of_tolerance": 2}),
        ("Shut down—I go numb, foggy, and want to sleep", {"window_of_tolerance": 1}),
        ("I alternate between the two, sometimes within the same day", {"window_of_tolerance": 1}),
        ("Neither—I stay in a manageable middle zone even under compound stress", {"window_of_tolerance": 5}),
    ]),
    "triangulation", False, "wot_arousal_1", 0.7, depth="deep"))

questions.append(make_q("window_of_tolerance", "partner_perspective",
    "Your partner would say your capacity for handling 'life noise' (minor daily stressors) is:",
    opts([
        ("Very high—I can absorb a lot of daily friction without it affecting me", {"window_of_tolerance": 5}),
        ("Moderate—normal amounts are fine but add one unexpected thing and I'm maxed out", {"window_of_tolerance": 3}),
        ("Low—even routine stressors can overwhelm me", {"window_of_tolerance": 1}),
        ("Variable—depends on my baseline that day (sleep, nutrition, mood)", {"window_of_tolerance": 3}),
    ]),
    "consistency_check", False, "wot_partner_1", 0.6))

questions.append(make_q("window_of_tolerance", "temporal",
    "Has your capacity for handling stress (the range of arousal you can function within) expanded or contracted over the past few years?",
    opts([
        ("Expanded—I can handle more than I used to", {"window_of_tolerance": 5}),
        ("Contracted—burnout, trauma, or life circumstances have narrowed it", {"window_of_tolerance": 1}),
        ("About the same", {"window_of_tolerance": 3}),
        ("I'm not sure—I've adapted but I might just be dissociating more", {"window_of_tolerance": 2, "emotional_awareness": 2}),
    ]),
    "trap", True, "wot_trajectory_1", 0.5,
    tags=[assessment_id, "window_of_tolerance", "trap", "self_assessment"]))

questions.append(make_q("window_of_tolerance", "behavioral_recall",
    "How many times in the past month have you felt 'I'm at capacity—one more thing will break me'?",
    opts([
        ("Never or almost never—I have bandwidth to spare", {"window_of_tolerance": 5}),
        ("A few times—during peak stress periods", {"window_of_tolerance": 3}),
        ("Weekly or more—I run close to the edge regularly", {"window_of_tolerance": 2}),
        ("That's my default state—I'm always at capacity", {"window_of_tolerance": 1}),
    ]),
    "triangulation", False, "wot_capacity_1", 0.6))

questions.append(make_q("window_of_tolerance", "forced_choice",
    "When you hit emotional overload, do you more often 'blow up' (yelling, crying, panic) or 'shut down' (going numb, dissociating, sleeping)?",
    opts([
        ("Blow up—I go over the top when overwhelmed", {"window_of_tolerance": 2}),
        ("Shut down—I go under and become unreachable", {"window_of_tolerance": 2}),
        ("Both—depends on the type of stressor", {"window_of_tolerance": 2}),
        ("Neither happens often—I rarely reach the point of overload", {"window_of_tolerance": 5}),
    ]),
    "triangulation", False, "wot_direction_1", 0.6))

questions.append(make_q("window_of_tolerance", "scenario",
    "You're working from home. Your kids are loud, your inbox is full, a repair person is knocking on the door, and your boss just scheduled an impromptu meeting. What happens to your ability to think clearly?",
    opts([
        ("It stays intact—I can context-switch and handle simultaneous demands", {"window_of_tolerance": 5}),
        ("It degrades gradually—each new demand makes the others harder", {"window_of_tolerance": 3}),
        ("It collapses—I freeze, can't prioritize, and feel paralyzed", {"window_of_tolerance": 1}),
        ("I snap at someone (probably the kids)—my regulation fails under compound pressure", {"window_of_tolerance": 2, "impulse_control": 2}),
    ]),
    "consistency_check", False, "wot_wfh_1", 0.7))

questions.append(make_q("window_of_tolerance", "somatic",
    "What physical signs tell you that you're approaching the edge of your window of tolerance?",
    opts([
        ("I know my signals well: jaw clenching, shallow breathing, specific tension patterns", {"window_of_tolerance": 4, "emotional_awareness": 5}),
        ("I recognize it after the fact—'oh, I was clenching my jaw all day'", {"window_of_tolerance": 3, "emotional_awareness": 2}),
        ("I don't notice until I've already crossed the line into overwhelm", {"window_of_tolerance": 2, "emotional_awareness": 1}),
        ("My body gives me very early warnings that I've learned to heed", {"window_of_tolerance": 5, "emotional_awareness": 5}),
    ]),
    "triangulation", False, "wot_signals_1", 0.7, depth="deep"))

questions.append(make_q("window_of_tolerance", "behavioral_recall",
    "When was the last time you completely lost it—screamed, sobbed uncontrollably, froze up, or had a panic episode?",
    opts([
        ("Within the past week", {"window_of_tolerance": 1}),
        ("Within the past month", {"window_of_tolerance": 2}),
        ("Within the past year", {"window_of_tolerance": 3}),
        ("I genuinely can't remember the last time", {"window_of_tolerance": 5}),
    ]),
    "trap", True, "wot_lost_it_1", 0.5,
    tags=[assessment_id, "window_of_tolerance", "trap", "frequency"]))

questions.append(make_q("window_of_tolerance", "partner_perspective",
    "Would the people around you say they have to 'tiptoe' around you on your bad days?",
    opts([
        ("Yes—when I'm maxed out, everyone knows to give me space", {"window_of_tolerance": 1}),
        ("Sometimes—I can be sensitive when I'm already stressed", {"window_of_tolerance": 2}),
        ("No—even my bad days don't dramatically affect how I interact with people", {"window_of_tolerance": 5}),
        ("I don't think so, but I might not be the best judge of that", {"window_of_tolerance": 3}),
    ]),
    "consistency_check", False, "wot_tiptoe_1", 0.5))

questions.append(make_q("window_of_tolerance", "temporal",
    "Think about your most stressful month in the past year. Did your coping capacity hold, or did it fail?",
    opts([
        ("Held—I was stressed but functional throughout", {"window_of_tolerance": 5}),
        ("Bent but didn't break—some rough patches but I recovered within that month", {"window_of_tolerance": 3}),
        ("Failed at some point—I had a significant breakdown, burnout, or health collapse", {"window_of_tolerance": 1}),
        ("I can't identify a 'most stressful' month because they're all stressful", {"window_of_tolerance": 1}),
    ]),
    "triangulation", False, "wot_worst_month_1", 0.7))

questions.append(make_q("window_of_tolerance", "scenario",
    "You're on a family road trip. The GPS fails, the kids are fighting, your partner is navigating poorly, and you're hungry. At what point do you lose your composure?",
    opts([
        ("GPS fails—I'm already irritated", {"window_of_tolerance": 1}),
        ("When the kids start fighting—the noise on top of the GPS problem is too much", {"window_of_tolerance": 2}),
        ("The partner navigating badly—now I feel alone in handling things", {"window_of_tolerance": 3}),
        ("I can hold all of it—annoying but not composure-breaking", {"window_of_tolerance": 5}),
    ]),
    "consistency_check", False, "wot_roadtrip_1", 0.7))

questions.append(make_q("window_of_tolerance", "forced_choice",
    "If your emotional regulation were a battery, how much charge does a typical day of work leave you with?",
    opts([
        ("60-80%—plenty left for personal life", {"window_of_tolerance": 5}),
        ("30-50%—I need recovery time before I can be present at home", {"window_of_tolerance": 3}),
        ("Under 20%—by evening I'm running on fumes emotionally", {"window_of_tolerance": 1}),
        ("It varies wildly by day", {"window_of_tolerance": 2}),
    ]),
    "triangulation", False, "wot_battery_1", 0.6))

questions.append(make_q("window_of_tolerance", "somatic",
    "When you're overwhelmed, does your body respond more with tension (fight-flight) or collapse (freeze-shutdown)?",
    opts([
        ("Tension—I'm wired, can't relax, muscles tight, heart racing", {"window_of_tolerance": 2}),
        ("Collapse—I feel heavy, spacey, disconnected, want to sleep", {"window_of_tolerance": 1}),
        ("I move between both in waves", {"window_of_tolerance": 2}),
        ("I don't reach overwhelm often enough to have a clear pattern", {"window_of_tolerance": 5}),
    ]),
    "triangulation", False, "wot_body_1", 0.7, depth="deep"))

questions.append(make_q("window_of_tolerance", "behavioral_recall",
    "Do you have activities that reliably expand your window of tolerance (exercise, nature, social connection, creative work)?",
    opts([
        ("Yes—and I prioritize them even when busy because I know they expand my capacity", {"window_of_tolerance": 5, "strategy_repertoire": 4}),
        ("Yes—but I only do them when I'm already struggling, not preventatively", {"window_of_tolerance": 3}),
        ("Not really—I haven't found reliable ways to expand my capacity", {"window_of_tolerance": 2}),
        ("I used to but haven't maintained those practices", {"window_of_tolerance": 2}),
    ]),
    "consistency_check", False, "wot_expand_1", 0.6))

questions.append(make_q("window_of_tolerance", "scenario",
    "You receive three pieces of difficult news in one day: a medical concern, a financial setback, and a friend conflict. Can you process all three, or do you have to triage?",
    opts([
        ("I can hold all three and give each appropriate attention over the coming days", {"window_of_tolerance": 5}),
        ("I triage—handle the most urgent, shelve the rest, and process in sequence", {"window_of_tolerance": 4}),
        ("I can deal with one, maybe two—the third goes into denial until I have capacity", {"window_of_tolerance": 2}),
        ("I'd be paralyzed—the combination would overwhelm my ability to act on any of them", {"window_of_tolerance": 1}),
    ]),
    "triangulation", False, "wot_triple_1", 0.7))

questions.append(make_q("window_of_tolerance", "partner_perspective",
    "How would someone who's seen you at your worst describe what happens when you exceed your capacity?",
    opts([
        ("'They get very quiet and withdrawn—like the lights are on but nobody's home'", {"window_of_tolerance": 2}),
        ("'They get explosive—snapping, crying, or panicking'", {"window_of_tolerance": 2}),
        ("'They get rigidly controlled—functioning but clearly white-knuckling it'", {"window_of_tolerance": 3}),
        ("'I've rarely seen them actually exceed their capacity'", {"window_of_tolerance": 5}),
    ]),
    "trap", True, "wot_worst_1", 0.4,
    tags=[assessment_id, "window_of_tolerance", "trap", "presentation"]))

questions.append(make_q("window_of_tolerance", "temporal",
    "How much does sleep quality affect your emotional bandwidth the next day?",
    opts([
        ("Massively—poor sleep shrinks my window of tolerance dramatically", {"window_of_tolerance": 2}),
        ("Noticeably—I'm more reactive after bad sleep but still functional", {"window_of_tolerance": 3}),
        ("Somewhat—it's a factor but not a dominant one", {"window_of_tolerance": 4}),
        ("Minimally—I can function well regardless of sleep quality", {"window_of_tolerance": 5}),
    ]),
    "consistency_check", False, "wot_sleep_1", 0.6))

questions.append(make_q("window_of_tolerance", "behavioral_recall",
    "Think about a normal Tuesday. How many emotionally activating events can happen before you feel overwhelmed?",
    opts([
        ("One significant or two minor ones—my baseline capacity is low", {"window_of_tolerance": 1}),
        ("Three or four moderate ones—typical daily stressors are fine", {"window_of_tolerance": 3}),
        ("Five or more—it takes a lot to overwhelm me on a normal day", {"window_of_tolerance": 5}),
        ("Depends entirely on my starting state—some Tuesdays I start already at 80% capacity", {"window_of_tolerance": 2}),
    ]),
    "triangulation", False, "wot_tuesday_1", 0.6))

questions.append(make_q("window_of_tolerance", "forced_choice",
    "When your partner is also stressed, does their stress expand into your window (making you more stressed) or do you maintain your own emotional regulation?",
    opts([
        ("Their stress infects me—we end up co-dysregulated", {"window_of_tolerance": 2}),
        ("I can usually maintain my own regulation and be a stabilizing presence", {"window_of_tolerance": 5}),
        ("It depends on how much capacity I have left that day", {"window_of_tolerance": 3}),
        ("I take on their stress and lose mine—I regulate by focusing on them", {"window_of_tolerance": 2}),
    ]),
    "trap", True, "wot_coregulation_1", 0.5,
    tags=[assessment_id, "window_of_tolerance", "trap", "codependency"]))

questions.append(make_q("window_of_tolerance", "scenario",
    "You're managing a high-stakes project with daily crises for two weeks straight. By day 10, you:",
    opts([
        ("Are still sharp—sustained pressure is something I handle well", {"window_of_tolerance": 5}),
        ("Are functional but making more mistakes—cognitive and emotional fatigue is setting in", {"window_of_tolerance": 3}),
        ("Have already had at least one breakdown or blow-up—two weeks of this is beyond my capacity", {"window_of_tolerance": 1}),
        ("Am dissociating—I'm physically present but emotionally checked out", {"window_of_tolerance": 1}),
    ]),
    "consistency_check", False, "wot_sustained_1", 0.7))

questions.append(make_q("window_of_tolerance", "somatic",
    "When you hit your absolute limit, what's the first physical sign that tells you 'this is it'?",
    opts([
        ("Tears—I start crying and can't stop", {"window_of_tolerance": 3}),
        ("Numbness—I feel disconnected from my body", {"window_of_tolerance": 1}),
        ("Shaking—my hands or body trembles", {"window_of_tolerance": 2}),
        ("I don't have a specific 'limit' signal—I maintain homeostasis under most conditions", {"window_of_tolerance": 5}),
    ]),
    "triangulation", False, "wot_limit_sign_1", 0.7, depth="deep"))

questions.append(make_q("window_of_tolerance", "behavioral_recall",
    "How much does hunger, caffeine, or blood sugar affect your emotional regulation?",
    opts([
        ("Hugely—'hangry' is a real state for me and skipping meals means emotional volatility", {"window_of_tolerance": 2}),
        ("Noticeably but manageable—I'm more irritable but still in control", {"window_of_tolerance": 3}),
        ("Slightly—physical needs affect my mood but don't override my regulation", {"window_of_tolerance": 4}),
        ("Minimally—my emotional state is fairly independent of physical conditions", {"window_of_tolerance": 5}),
    ]),
    "consistency_check", False, "wot_physiology_1", 0.6))

questions.append(make_q("window_of_tolerance", "temporal",
    "After a vacation or extended rest period, how much wider does your window of tolerance feel?",
    opts([
        ("Dramatically wider—rest is essential for my emotional capacity", {"window_of_tolerance": 3}),
        ("Somewhat wider—I notice I'm more patient and resilient", {"window_of_tolerance": 4}),
        ("Not much—my baseline doesn't change significantly with rest", {"window_of_tolerance": 4}),
        ("I can't remember the last time I had enough rest to notice a difference", {"window_of_tolerance": 1}),
    ]),
    "triangulation", False, "wot_rest_1", 0.7))

# Validate
dim_counts = {}
type_counts = {}
tier_counts = {}
trap_count = 0
for q in questions:
    dim_counts[q["dimension"]] = dim_counts.get(q["dimension"], 0) + 1
    type_counts[q["question_type"]] = type_counts.get(q["question_type"], 0) + 1
    tier_counts[q["tier_role"]] = tier_counts.get(q["tier_role"], 0) + 1
    if q["anti_gaming"]["social_desirability_trap"]:
        trap_count += 1

print(f"Total: {len(questions)}")
print(f"Dimensions: {dim_counts}")
print(f"Types: {type_counts}")
print(f"Tiers: {tier_counts}")
print(f"SD traps: {trap_count}")

with open("/Users/user/personal/sb/trueassess/priv/question_bank/emotional_regulation.json", "w") as f:
    json.dump(questions, f, indent=2)

print("Written to emotional_regulation.json")
