import json, random

random.seed(42)

questions = []

# Self-Worth / Identity: 120 questions across 5 dimensions (24 each)
# Dimensions: self_concept_clarity, shame_guilt, rejection_sensitivity, self_forgiveness, external_validation

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
        "tags": tags or ["self_worth", dim]
    }

def opts(choices):
    """choices: list of (text, {dim: score}) tuples"""
    return [{"id": chr(97+i), "text": t, "scores": s} for i, (t, s) in enumerate(choices)]

# ============================================================
# SELF_CONCEPT_CLARITY (24 questions)
# ============================================================

questions.append(q("self_concept_clarity", "scenario",
    "You're at a dinner party and someone asks what you're passionate about. You:",
    opts([
        ("Immediately light up talking about 2-3 things that define your life", {"self_concept_clarity": 5}),
        ("Give a polished answer you've rehearsed before", {"self_concept_clarity": 2, "external_validation": 2}),
        ("Deflect with humor because you honestly aren't sure right now", {"self_concept_clarity": 1}),
        ("List your job title and hobbies but feel like you're reading someone else's bio", {"self_concept_clarity": 1})
    ]),
    tier="core", cg="scc_identity_1", opacity=0.6))

questions.append(q("self_concept_clarity", "temporal",
    "Think about who you were 5 years ago. How much of that person still feels like 'you'?",
    opts([
        ("Almost all of it — I've grown but my core hasn't changed", {"self_concept_clarity": 5}),
        ("The important parts are the same, some things evolved", {"self_concept_clarity": 4}),
        ("I'm a completely different person and I'm proud of that", {"self_concept_clarity": 2}),
        ("I honestly can't tell what's changed and what hasn't", {"self_concept_clarity": 1})
    ]),
    tier="core", cg="scc_stability_1", opacity=0.7))

questions.append(q("self_concept_clarity", "somatic",
    "When you're alone with no plans and no one expecting anything from you, what happens in your body?",
    opts([
        ("I settle in — it feels like coming home to myself", {"self_concept_clarity": 5}),
        ("I feel okay for a while, then a restlessness kicks in", {"self_concept_clarity": 3, "external_validation": 2}),
        ("Anxiety builds quickly — I need to DO something", {"self_concept_clarity": 2, "external_validation": 3}),
        ("A strange emptiness, like I'm not sure who I am without context", {"self_concept_clarity": 1})
    ]),
    tier="core", cg="scc_alone_1", opacity=0.75))

questions.append(q("self_concept_clarity", "behavioral_recall",
    "Last time you made a major decision (job, relationship, move), how did you decide?",
    opts([
        ("I knew what I wanted — the decision was about logistics, not identity", {"self_concept_clarity": 5}),
        ("I weighed pros and cons but kept coming back to what felt right for ME", {"self_concept_clarity": 4}),
        ("I asked a lot of people what they thought I should do", {"self_concept_clarity": 2, "external_validation": 3}),
        ("I agonized because every option felt equally 'me' and 'not me'", {"self_concept_clarity": 1})
    ]),
    tier="core", cg="scc_decisions_1", opacity=0.65))

questions.append(q("self_concept_clarity", "scenario",
    "A close friend describes you to someone you've never met. When you hear their description later, you think:",
    opts([
        ("That's pretty accurate — they get me", {"self_concept_clarity": 5}),
        ("They captured one side of me but missed something important", {"self_concept_clarity": 3}),
        ("That doesn't sound like me at all", {"self_concept_clarity": 2}),
        ("I'm not sure if they're wrong or if I just don't know myself that well", {"self_concept_clarity": 1})
    ]),
    tier="triangulation", cg="scc_identity_1", opacity=0.6))

questions.append(q("self_concept_clarity", "forced_choice",
    "Which bothers you more?",
    opts([
        ("Being misunderstood by someone who matters to you", {"self_concept_clarity": 4, "rejection_sensitivity": 2}),
        ("Realizing you don't understand yourself as well as you thought", {"self_concept_clarity": 1})
    ]),
    tier="triangulation", cg="scc_stability_1", opacity=0.8))

questions.append(q("self_concept_clarity", "scenario",
    "You take one of those personality quizzes online. Your result is the OPPOSITE of what you expected. Your reaction:",
    opts([
        ("Laugh it off — I know who I am, quizzes are entertainment", {"self_concept_clarity": 5}),
        ("Feel slightly unsettled and retake it more carefully", {"self_concept_clarity": 3}),
        ("Start questioning whether you've been wrong about yourself", {"self_concept_clarity": 1}),
        ("Feel validated because you always suspected you were different than people think", {"self_concept_clarity": 2, "external_validation": 2})
    ]),
    tier="trap", trap=True, cg="scc_identity_1", opacity=0.5))

questions.append(q("self_concept_clarity", "partner_perspective",
    "Your partner says 'You've changed a lot since we first met.' You feel:",
    opts([
        ("Curious — you want to know what they've noticed", {"self_concept_clarity": 4}),
        ("Defensive — you haven't changed, they just didn't know you", {"self_concept_clarity": 2}),
        ("Anxious — change means maybe they don't love the current you", {"self_concept_clarity": 2, "rejection_sensitivity": 4}),
        ("Confused — you can't tell if you've changed or not", {"self_concept_clarity": 1})
    ]),
    tier="core", cg="scc_stability_1", opacity=0.7))

questions.append(q("self_concept_clarity", "behavioral_recall",
    "When you try on clothes, how quickly do you know what feels like 'you'?",
    opts([
        ("Instantly — I have a clear personal style", {"self_concept_clarity": 5}),
        ("Pretty quickly, I know what works", {"self_concept_clarity": 4}),
        ("It depends on my mood and who I'm dressing for", {"self_concept_clarity": 2, "external_validation": 2}),
        ("I usually just buy what looks good on the model or what's trending", {"self_concept_clarity": 1, "external_validation": 3})
    ]),
    tier="triangulation", cg="scc_identity_1", opacity=0.5))

questions.append(q("self_concept_clarity", "scenario",
    "You're starting a new job. In the first week, people form an impression of you that's very different from how you see yourself. You:",
    opts([
        ("Don't stress — they'll get to know the real you over time", {"self_concept_clarity": 5}),
        ("Actively try to correct their impression with stories and examples", {"self_concept_clarity": 3, "external_validation": 2}),
        ("Start wondering if maybe THEY see you more clearly than you see yourself", {"self_concept_clarity": 1}),
        ("Adjust your behavior to match what seems to be working", {"self_concept_clarity": 2, "external_validation": 3})
    ]),
    tier="core", cg="scc_identity_1", opacity=0.65))

questions.append(q("self_concept_clarity", "somatic",
    "When someone compliments a trait you're not sure you actually have, your body does what?",
    opts([
        ("Relaxes — nice to hear, whether or not you agree", {"self_concept_clarity": 4}),
        ("Tenses slightly — the mismatch between their view and yours creates discomfort", {"self_concept_clarity": 3}),
        ("Lights up — maybe you DO have that trait and just couldn't see it", {"self_concept_clarity": 2, "external_validation": 3}),
        ("Goes numb — you can't even evaluate the claim", {"self_concept_clarity": 1})
    ]),
    tier="triangulation", cg="scc_alone_1", opacity=0.75))

questions.append(q("self_concept_clarity", "temporal",
    "If you had to write your own obituary today, how easy would it be?",
    opts([
        ("Easy — I know what my life has been about", {"self_concept_clarity": 5}),
        ("I could do it but I'd struggle with what to emphasize", {"self_concept_clarity": 3}),
        ("Hard — I'd keep second-guessing what's actually true about me", {"self_concept_clarity": 2}),
        ("Nearly impossible — I don't have a coherent narrative of my own life", {"self_concept_clarity": 1})
    ]),
    tier="core", cg="scc_stability_1", opacity=0.7))

questions.append(q("self_concept_clarity", "forced_choice",
    "Pick the statement that resonates more:",
    opts([
        ("I contain multitudes — trying to pin myself down would be limiting", {"self_concept_clarity": 2}),
        ("I have a clear center even though I show different sides in different contexts", {"self_concept_clarity": 5})
    ]),
    tier="trap", trap=True, opacity=0.85, tags=["self_worth", "self_concept_clarity", "philosophical"]))

questions.append(q("self_concept_clarity", "scenario",
    "You've been spending time with a new group of friends who are very different from your old ones. After a month you notice you've picked up new opinions and habits. This feels:",
    opts([
        ("Natural — I'm always incorporating new things that resonate", {"self_concept_clarity": 4}),
        ("A bit alarming — am I just a chameleon?", {"self_concept_clarity": 2}),
        ("Exciting — maybe this is the REAL me finally coming out", {"self_concept_clarity": 1}),
        ("Interesting but I'll keep what fits and drop what doesn't", {"self_concept_clarity": 5})
    ]),
    tier="triangulation", cg="scc_decisions_1", opacity=0.6))

questions.append(q("self_concept_clarity", "behavioral_recall",
    "When filling out forms that ask about your interests or 'describe yourself in 3 words,' you:",
    opts([
        ("Knock it out quickly — you know your go-to descriptors", {"self_concept_clarity": 5}),
        ("Spend way too long because none of the words feel exactly right", {"self_concept_clarity": 2}),
        ("Write different things every time depending on the context", {"self_concept_clarity": 2}),
        ("Leave it blank or write something generic", {"self_concept_clarity": 1})
    ]),
    tier="consistency_check", cg="scc_identity_1", opacity=0.5))

questions.append(q("self_concept_clarity", "scenario",
    "Your therapist asks you to describe your 'authentic self.' You:",
    opts([
        ("Can paint a clear picture even if it's complicated", {"self_concept_clarity": 5}),
        ("Describe who you want to be rather than who you currently are", {"self_concept_clarity": 2}),
        ("Feel frustrated because the concept feels meaningless", {"self_concept_clarity": 2}),
        ("Go blank — you've never really thought about it that way", {"self_concept_clarity": 1})
    ]),
    tier="core", cg="scc_alone_1", opacity=0.7))

questions.append(q("self_concept_clarity", "partner_perspective",
    "Different people in your life would describe you very differently. How does that feel?",
    opts([
        ("Fine — I'm the same person, they just see different facets", {"self_concept_clarity": 5}),
        ("A little uncomfortable but that's just how social life works", {"self_concept_clarity": 3}),
        ("Unsettling — which version of me is the real one?", {"self_concept_clarity": 1}),
        ("Validating — it means I'm complex and interesting", {"self_concept_clarity": 2, "external_validation": 2})
    ]),
    tier="triangulation", cg="scc_identity_1", opacity=0.65))

questions.append(q("self_concept_clarity", "temporal",
    "You look at old journal entries or social media posts from years ago. Your reaction:",
    opts([
        ("I can trace a clear thread — that's recognizably me, just younger", {"self_concept_clarity": 5}),
        ("Some posts feel like a stranger wrote them", {"self_concept_clarity": 2}),
        ("I cringe at the inconsistency — I was clearly performing for an audience", {"self_concept_clarity": 2, "external_validation": 3}),
        ("I don't keep records like that — too uncomfortable to look back", {"self_concept_clarity": 1})
    ]),
    tier="consistency_check", cg="scc_stability_1", opacity=0.6))

questions.append(q("self_concept_clarity", "somatic",
    "You're asked to give an impromptu toast at a friend's wedding. Standing up, you feel:",
    opts([
        ("Nervous but grounded — you know what you want to say about love and friendship", {"self_concept_clarity": 5}),
        ("Panicked about what THEY want to hear you say", {"self_concept_clarity": 2, "external_validation": 3}),
        ("Excited — you're naturally expressive and this is your element", {"self_concept_clarity": 4}),
        ("Frozen — without prep time you don't know which version of yourself to present", {"self_concept_clarity": 1})
    ]),
    tier="core", cg="scc_decisions_1", opacity=0.6))

questions.append(q("self_concept_clarity", "forced_choice",
    "Would you rather:",
    opts([
        ("Know exactly who you are but have others misunderstand you", {"self_concept_clarity": 5}),
        ("Be seen accurately by everyone but never be quite sure who you really are", {"self_concept_clarity": 1, "external_validation": 4})
    ]),
    tier="trap", trap=True, cg="scc_alone_1", opacity=0.85))

questions.append(q("self_concept_clarity", "scenario",
    "A personality assessment tells you something surprising about yourself that your partner agrees with but you don't see. You:",
    opts([
        ("Consider it seriously — two data points outweigh your blind spot", {"self_concept_clarity": 3}),
        ("Dismiss it — you know yourself better than any test", {"self_concept_clarity": 4}),
        ("Feel a sudden identity wobble — what else don't you know?", {"self_concept_clarity": 1}),
        ("File it away as interesting but not identity-shaking", {"self_concept_clarity": 5})
    ]),
    tier="triangulation", cg="scc_identity_1", opacity=0.7))

questions.append(q("self_concept_clarity", "behavioral_recall",
    "How often do you change your mind about what you want out of life?",
    opts([
        ("Rarely — my north star has been consistent for years", {"self_concept_clarity": 5}),
        ("The big stuff stays the same, details shift with circumstances", {"self_concept_clarity": 4}),
        ("Every few months I seem to want something completely different", {"self_concept_clarity": 2}),
        ("I've honestly never pinned down what I want — it feels too limiting", {"self_concept_clarity": 1})
    ]),
    tier="consistency_check", cg="scc_stability_1", opacity=0.6))

questions.append(q("self_concept_clarity", "scenario",
    "You overhear a stranger describe you to someone else based on a brief interaction. Their take is surprisingly insightful. You feel:",
    opts([
        ("Impressed but not shaken — they happened to read you right", {"self_concept_clarity": 5}),
        ("Exposed — how did they see that so fast?", {"self_concept_clarity": 3}),
        ("Grateful — their observation helps you understand yourself better", {"self_concept_clarity": 2, "external_validation": 3}),
        ("Skeptical — one interaction can't capture who you are", {"self_concept_clarity": 4})
    ]),
    tier="triangulation", cg="scc_alone_1", opacity=0.6))

questions.append(q("self_concept_clarity", "partner_perspective",
    "If your best friend and your parent each described your biggest flaw, would they name the same thing?",
    opts([
        ("Probably yes — my weaknesses are pretty consistent across contexts", {"self_concept_clarity": 5}),
        ("They'd name different things because I'm different around each of them", {"self_concept_clarity": 3}),
        ("I genuinely have no idea what either would say", {"self_concept_clarity": 1}),
        ("They'd both be wrong — nobody sees the real flaw", {"self_concept_clarity": 3, "shame_guilt": 2})
    ]),
    tier="core", cg="scc_identity_1", opacity=0.7))

# ============================================================
# SHAME_GUILT (24 questions)
# ============================================================

questions.append(q("shame_guilt", "scenario",
    "You snap at someone you care about over something trivial. An hour later, you're thinking:",
    opts([
        ("I need to apologize — that wasn't fair to them", {"shame_guilt": 5}),
        ("What is wrong with me? Why can't I just be a decent person?", {"shame_guilt": 1}),
        ("They probably provoked it without realizing — not entirely my fault", {"shame_guilt": 3}),
        ("I replay it obsessively, hating the version of me who did that", {"shame_guilt": 1})
    ]),
    tier="core", cg="sg_response_1", opacity=0.7,
    tags=["self_worth", "shame_guilt", "note: 5=healthy guilt, 1=toxic shame"]))

questions.append(q("shame_guilt", "somatic",
    "When you remember something you did that you regret, where do you feel it in your body?",
    opts([
        ("Chest tightness — like a weight pressing down", {"shame_guilt": 2}),
        ("Stomach drop — nausea or hollowness", {"shame_guilt": 1}),
        ("A wince, then it passes — I've processed it", {"shame_guilt": 5}),
        ("Full-body heat — I want to disappear", {"shame_guilt": 1})
    ]),
    tier="core", cg="sg_somatic_1", opacity=0.75))

questions.append(q("shame_guilt", "behavioral_recall",
    "Think of the last time you made a significant mistake at work. How long did it take you to move past it?",
    opts([
        ("I addressed it, learned from it, and moved on within a day or two", {"shame_guilt": 5}),
        ("A week or so — I kept replaying it", {"shame_guilt": 3}),
        ("Weeks to months — it became evidence in a case against myself", {"shame_guilt": 1}),
        ("I'm honestly not sure I've fully moved past it yet", {"shame_guilt": 1})
    ]),
    tier="core", cg="sg_recovery_1", opacity=0.65))

questions.append(q("shame_guilt", "forced_choice",
    "After doing something hurtful, which thought comes first?",
    opts([
        ("I did a bad thing — I need to make it right", {"shame_guilt": 5}),
        ("I AM bad — this is just more proof", {"shame_guilt": 1})
    ]),
    tier="core", cg="sg_response_1", opacity=0.9))

questions.append(q("shame_guilt", "scenario",
    "Your friend group is roasting each other playfully. Someone brings up an embarrassing thing you did years ago. Inside, you feel:",
    opts([
        ("Able to laugh at yourself — everyone has cringey moments", {"shame_guilt": 5}),
        ("A flash of heat and the urge to change the subject immediately", {"shame_guilt": 2}),
        ("Like they just confirmed what you secretly believe about yourself", {"shame_guilt": 1}),
        ("Fine on the surface but you'll think about this at 3 AM tonight", {"shame_guilt": 2})
    ]),
    tier="triangulation", cg="sg_somatic_1", opacity=0.65))

questions.append(q("shame_guilt", "temporal",
    "Is there something from your past that you've NEVER told anyone? The reason you haven't shared it is:",
    opts([
        ("It would genuinely hurt someone else to know", {"shame_guilt": 4}),
        ("I'm afraid people would see me differently — see the REAL me", {"shame_guilt": 1}),
        ("It's not that deep — just never came up", {"shame_guilt": 5}),
        ("I can't even fully admit it to myself yet", {"shame_guilt": 1})
    ]),
    tier="core", cg="sg_secrecy_1", opacity=0.8))

questions.append(q("shame_guilt", "partner_perspective",
    "Your partner catches you in a lie — not a big one, but clearly a lie. Your immediate internal response:",
    opts([
        ("Embarrassment at being caught, then accountability — own it and explain why", {"shame_guilt": 5}),
        ("Scramble to minimize — 'it wasn't really a LIE exactly'", {"shame_guilt": 3}),
        ("Overwhelming dread — this is the moment they see who you really are", {"shame_guilt": 1}),
        ("Anger at yourself that spirals into self-attack", {"shame_guilt": 1})
    ]),
    tier="core", cg="sg_response_1", opacity=0.7))

questions.append(q("shame_guilt", "scenario",
    "You get publicly called out for something that was genuinely your fault — a mistake everyone can see. You:",
    opts([
        ("Own it clearly: 'You're right, I messed up, here's how I'll fix it'", {"shame_guilt": 5}),
        ("Own it but want to die inside", {"shame_guilt": 2}),
        ("Get defensive first, apologize later when the heat dies down", {"shame_guilt": 3}),
        ("Start building a narrative about why it wasn't really your fault", {"shame_guilt": 2})
    ]),
    tier="triangulation", cg="sg_recovery_1", opacity=0.65))

questions.append(q("shame_guilt", "somatic",
    "Someone you respect expresses disappointment in you. In the moment, your body:",
    opts([
        ("Tightens but stays upright — you hear them out", {"shame_guilt": 4}),
        ("Wants to shrink — you feel physically smaller", {"shame_guilt": 1}),
        ("Goes hot — fight-or-flight kicks in", {"shame_guilt": 2}),
        ("Goes numb — you'll process this later (or never)", {"shame_guilt": 2})
    ]),
    tier="triangulation", cg="sg_somatic_1", opacity=0.75))

questions.append(q("shame_guilt", "behavioral_recall",
    "How many things from your past do you carry around as evidence of being fundamentally flawed?",
    opts([
        ("None — I've made mistakes but they don't define me", {"shame_guilt": 5}),
        ("One or two big ones that I've mostly worked through", {"shame_guilt": 4}),
        ("A running list that I add to whenever something goes wrong", {"shame_guilt": 1}),
        ("I try not to think about it but the list is always there in the background", {"shame_guilt": 1})
    ]),
    tier="core", cg="sg_secrecy_1", opacity=0.75))

questions.append(q("shame_guilt", "scenario",
    "You've been secretly struggling with something (addiction, debt, mental health). When you imagine telling someone, the dominant emotion is:",
    opts([
        ("Relief — getting it out would feel freeing", {"shame_guilt": 4}),
        ("Fear of judgment — they'll think less of you forever", {"shame_guilt": 1}),
        ("Practical concern — will they help or make it worse?", {"shame_guilt": 5}),
        ("Certainty that they'll leave", {"shame_guilt": 1, "rejection_sensitivity": 4})
    ]),
    tier="core", cg="sg_secrecy_1", opacity=0.75))

questions.append(q("shame_guilt", "forced_choice",
    "Which statement is closer to your experience?",
    opts([
        ("My mistakes are things I DID — separate from who I AM", {"shame_guilt": 5}),
        ("My mistakes reveal who I am at my core", {"shame_guilt": 1})
    ]),
    tier="consistency_check", cg="sg_response_1", opacity=0.9))

questions.append(q("shame_guilt", "temporal",
    "Think about a time you were forgiven for something significant. How completely did you accept the forgiveness?",
    opts([
        ("Fully — if they forgave me, I could release it", {"shame_guilt": 5}),
        ("Mostly, but part of me felt I didn't deserve it", {"shame_guilt": 3}),
        ("Not at all — I still punish myself for it regardless", {"shame_guilt": 1}),
        ("I accepted their forgiveness but used it as motivation to never mess up again (and still haven't forgiven myself)", {"shame_guilt": 2})
    ]),
    tier="triangulation", cg="sg_recovery_1", opacity=0.7))

questions.append(q("shame_guilt", "trap",
    "A friend confesses something terrible they did. You notice your first instinct is:",
    opts([
        ("Empathy — everyone makes mistakes", {"shame_guilt": 4}),
        ("Curiosity about what led to it", {"shame_guilt": 5}),
        ("Internal comparison — at least I'd never do THAT", {"shame_guilt": 2}),
        ("Relating — thinking 'if they knew what I've done...'", {"shame_guilt": 1})
    ]),
    tier="trap", trap=True, cg="sg_secrecy_1", opacity=0.6))

questions.append(q("shame_guilt", "scenario",
    "You realize you've been wrong about something you argued passionately about in public. You:",
    opts([
        ("Post a correction or bring it up next time — being right matters less than being honest", {"shame_guilt": 5}),
        ("Quietly change your position without drawing attention to it", {"shame_guilt": 3}),
        ("Feel physically ill about the public wrongness", {"shame_guilt": 1}),
        ("Double down — admitting you were wrong feels like admitting you're stupid", {"shame_guilt": 1})
    ]),
    tier="core", cg="sg_response_1", opacity=0.65))

questions.append(q("shame_guilt", "partner_perspective",
    "Your partner gently points out that you apologize too much — for things that aren't even your fault. You feel:",
    opts([
        ("Surprised — you hadn't noticed", {"shame_guilt": 3}),
        ("Seen — they're right, and that pattern probably means something", {"shame_guilt": 3}),
        ("Defensive — being considerate isn't a flaw", {"shame_guilt": 2}),
        ("Ashamed of being ashamed — even your coping mechanisms are wrong", {"shame_guilt": 1})
    ]),
    tier="trap", trap=True, cg="sg_somatic_1", opacity=0.7))

questions.append(q("shame_guilt", "behavioral_recall",
    "When you apologize, how often do you over-apologize — saying sorry multiple times, over-explaining, or bringing it up again days later?",
    opts([
        ("Rarely — I apologize once sincerely and move on", {"shame_guilt": 5}),
        ("Sometimes — depends on how bad I feel about it", {"shame_guilt": 3}),
        ("Often — one apology never feels like enough", {"shame_guilt": 2}),
        ("Almost always — and then I apologize for over-apologizing", {"shame_guilt": 1})
    ]),
    tier="consistency_check", cg="sg_recovery_1", opacity=0.6))

questions.append(q("shame_guilt", "scenario",
    "You win an award or public recognition. Someone congratulates you. Your inner voice says:",
    opts([
        ("'I worked hard for this, I deserve it'", {"shame_guilt": 5}),
        ("'If they only knew the full picture...'", {"shame_guilt": 2}),
        ("'This is nice but I got lucky'", {"shame_guilt": 3}),
        ("'They'll find out I'm a fraud eventually'", {"shame_guilt": 1})
    ]),
    tier="triangulation", cg="sg_secrecy_1", opacity=0.65))

questions.append(q("shame_guilt", "somatic",
    "You're going through old photos and find one from a period of your life you're not proud of. Your body:",
    opts([
        ("Feels a pang but you can look at it with compassion for past-you", {"shame_guilt": 5}),
        ("Recoils — you flip past it quickly", {"shame_guilt": 2}),
        ("Freezes — the shame is as fresh as the day the photo was taken", {"shame_guilt": 1}),
        ("Nothing — you've dissociated from that version of yourself entirely", {"shame_guilt": 1})
    ]),
    tier="core", cg="sg_somatic_1", opacity=0.75))

questions.append(q("shame_guilt", "temporal",
    "If you could permanently erase one memory of something you did from everyone's mind (including your own), would you?",
    opts([
        ("No — everything I've done made me who I am", {"shame_guilt": 5}),
        ("Tempting, but no — I need to remember to stay accountable", {"shame_guilt": 4}),
        ("From their minds yes, from mine no — I don't want them to think of me that way", {"shame_guilt": 2}),
        ("Absolutely — in a heartbeat", {"shame_guilt": 1})
    ]),
    tier="trap", trap=True, cg="sg_secrecy_1", opacity=0.8))

questions.append(q("shame_guilt", "scenario",
    "You discover that someone you wronged years ago has spoken positively about you to mutual friends. They seem to have moved on completely. You feel:",
    opts([
        ("Relieved and grateful — maybe it wasn't as devastating as you thought", {"shame_guilt": 4}),
        ("Suspicious — they must not remember what you did", {"shame_guilt": 2}),
        ("Worse — their kindness makes your guilt sharper by contrast", {"shame_guilt": 1}),
        ("Freed — their moving on gives you permission to release it too", {"shame_guilt": 5})
    ]),
    tier="triangulation", cg="sg_recovery_1", opacity=0.7))

questions.append(q("shame_guilt", "forced_choice",
    "Which feels more true?",
    opts([
        ("I sometimes do bad things — like everyone", {"shame_guilt": 5}),
        ("There's something fundamentally wrong with me that I manage to hide most of the time", {"shame_guilt": 1})
    ]),
    tier="consistency_check", cg="sg_response_1", opacity=0.9))

questions.append(q("shame_guilt", "behavioral_recall",
    "When you feel guilty about something, what's your go-to move?",
    opts([
        ("Address it directly with the person involved", {"shame_guilt": 5}),
        ("Do something nice for them without explaining why", {"shame_guilt": 3}),
        ("Withdraw and hope it blows over", {"shame_guilt": 2}),
        ("Punish yourself — restrict something you enjoy, overwork, negative self-talk", {"shame_guilt": 1})
    ]),
    tier="core", cg="sg_recovery_1", opacity=0.7))

questions.append(q("shame_guilt", "partner_perspective",
    "If your partner said 'I need to tell you something I'm ashamed of,' your gut response would be:",
    opts([
        ("Lean in — 'I'm here, whatever it is'", {"shame_guilt": 4}),
        ("Brace for impact — this is going to change how you see them", {"shame_guilt": 2}),
        ("Relief — 'good, they're human too, now we're even'", {"shame_guilt": 2}),
        ("Fear — if they show you their worst, you might have to show yours", {"shame_guilt": 1})
    ]),
    tier="trap", trap=True, cg="sg_secrecy_1", opacity=0.7))

# ============================================================
# REJECTION_SENSITIVITY (24 questions)
# ============================================================

questions.append(q("rejection_sensitivity", "scenario",
    "You text a close friend and they don't respond for 24 hours. Your brain's first explanation is:",
    opts([
        ("They're busy — I'll hear from them when they're free", {"rejection_sensitivity": 5}),
        ("Maybe they didn't see it — phones are weird", {"rejection_sensitivity": 4}),
        ("I probably said something that bothered them last time we talked", {"rejection_sensitivity": 2}),
        ("They're pulling away from the friendship — this is how it starts", {"rejection_sensitivity": 1})
    ]),
    tier="core", cg="rs_interpretation_1", opacity=0.6))

questions.append(q("rejection_sensitivity", "somatic",
    "You're at a social gathering and notice two people glancing at you then whispering. Your body:",
    opts([
        ("Doesn't register it — people look around at parties", {"rejection_sensitivity": 5}),
        ("Notes it but your attention moves on quickly", {"rejection_sensitivity": 4}),
        ("Tightens — you start monitoring whether others are doing it too", {"rejection_sensitivity": 2}),
        ("Full alert — your face gets hot, you want to leave", {"rejection_sensitivity": 1})
    ]),
    tier="core", cg="rs_social_1", opacity=0.65))

questions.append(q("rejection_sensitivity", "behavioral_recall",
    "Think about the last time you asked someone for something and they said no. How long did the sting last?",
    opts([
        ("What sting? They said no, I moved on", {"rejection_sensitivity": 5}),
        ("A brief moment of disappointment, gone within minutes", {"rejection_sensitivity": 4}),
        ("I thought about it on and off for the rest of the day", {"rejection_sensitivity": 2}),
        ("Days — and it made me less likely to ask for things", {"rejection_sensitivity": 1})
    ]),
    tier="core", cg="rs_recovery_1", opacity=0.6))

questions.append(q("rejection_sensitivity", "partner_perspective",
    "Your partner seems distracted and less affectionate than usual for a few days. No explanation given. You:",
    opts([
        ("Give them space — everyone has off days or weeks", {"rejection_sensitivity": 5}),
        ("Ask once if everything's okay, then let it be", {"rejection_sensitivity": 4}),
        ("Start reviewing your recent behavior for what you might have done wrong", {"rejection_sensitivity": 2}),
        ("Spiral — assume they're losing interest and start preparing for the end", {"rejection_sensitivity": 1})
    ]),
    tier="core", cg="rs_interpretation_1", opacity=0.7))

questions.append(q("rejection_sensitivity", "scenario",
    "You suggest a restaurant for dinner with friends. Everyone agrees on a different place instead. You feel:",
    opts([
        ("Fine — it's just a restaurant", {"rejection_sensitivity": 5}),
        ("Mildly annoyed but you go with the flow", {"rejection_sensitivity": 4}),
        ("A small pang — like your taste or judgment was rejected", {"rejection_sensitivity": 2}),
        ("Stung — you probably shouldn't have suggested anything", {"rejection_sensitivity": 1})
    ]),
    tier="triangulation", cg="rs_social_1", opacity=0.5))

questions.append(q("rejection_sensitivity", "forced_choice",
    "You'd rather:",
    opts([
        ("Be told 'no' directly to a request", {"rejection_sensitivity": 4}),
        ("Have someone make an excuse so you don't have to feel rejected", {"rejection_sensitivity": 1})
    ]),
    tier="core", cg="rs_recovery_1", opacity=0.7))

questions.append(q("rejection_sensitivity", "scenario",
    "You post something personal on social media — a photo, an opinion, a creative work. It gets very little engagement. You:",
    opts([
        ("Don't check engagement — you posted it because you wanted to", {"rejection_sensitivity": 5}),
        ("Notice but shrug it off — algorithms are random", {"rejection_sensitivity": 4}),
        ("Feel exposed and consider deleting it", {"rejection_sensitivity": 2}),
        ("Take it as a clear message that people don't care about what you have to say", {"rejection_sensitivity": 1})
    ]),
    tier="core", cg="rs_social_1", opacity=0.6, cross=[{"dimension": "external_validation", "weight": 0.4}]))

questions.append(q("rejection_sensitivity", "temporal",
    "How often do you replay social interactions looking for signs that someone was put off by you?",
    opts([
        ("Almost never — interactions are what they are", {"rejection_sensitivity": 5}),
        ("Only if something clearly awkward happened", {"rejection_sensitivity": 4}),
        ("Regularly — especially with people I want to impress", {"rejection_sensitivity": 2}),
        ("After almost every meaningful interaction", {"rejection_sensitivity": 1})
    ]),
    tier="triangulation", cg="rs_interpretation_1", opacity=0.7))

questions.append(q("rejection_sensitivity", "somatic",
    "You're about to ask someone out (romantically or even just for coffee as friends). Your body is:",
    opts([
        ("Excited — reaching out to people is energizing", {"rejection_sensitivity": 5}),
        ("A little nervous but you push through easily", {"rejection_sensitivity": 4}),
        ("Tight with dread — the possibility of 'no' feels physically threatening", {"rejection_sensitivity": 2}),
        ("You don't ask — you wait for them to initiate so you never have to risk it", {"rejection_sensitivity": 1})
    ]),
    tier="core", cg="rs_social_1", opacity=0.7))

questions.append(q("rejection_sensitivity", "behavioral_recall",
    "When someone cancels plans with you, what's your typical first thought?",
    opts([
        ("Cool, free evening — what should I do instead?", {"rejection_sensitivity": 5}),
        ("Disappointed but I understand — things come up", {"rejection_sensitivity": 4}),
        ("I bet they got a better offer", {"rejection_sensitivity": 2}),
        ("They don't actually want to spend time with me — they were just being polite", {"rejection_sensitivity": 1})
    ]),
    tier="consistency_check", cg="rs_interpretation_1", opacity=0.55))

questions.append(q("rejection_sensitivity", "scenario",
    "You're in a group conversation and make a joke that nobody laughs at. You:",
    opts([
        ("Move on — not every joke lands", {"rejection_sensitivity": 5}),
        ("Feel a flash of embarrassment but recover quickly", {"rejection_sensitivity": 4}),
        ("Replay it for hours wondering what's wrong with your sense of humor", {"rejection_sensitivity": 2}),
        ("Go quiet for the rest of the conversation", {"rejection_sensitivity": 1})
    ]),
    tier="triangulation", cg="rs_social_1", opacity=0.55))

questions.append(q("rejection_sensitivity", "partner_perspective",
    "Your partner makes a small critical comment about something you did around the house. Inside you feel:",
    opts([
        ("Fine — I'll adjust if it matters to them", {"rejection_sensitivity": 5}),
        ("Slightly stung but you know it's not personal", {"rejection_sensitivity": 4}),
        ("Like they're saying you're not good enough — this isn't about dishes", {"rejection_sensitivity": 2}),
        ("Devastated — and angry at yourself for being devastated over something so small", {"rejection_sensitivity": 1})
    ]),
    tier="core", cg="rs_recovery_1", opacity=0.7))

questions.append(q("rejection_sensitivity", "forced_choice",
    "Which scenario is harder for you?",
    opts([
        ("Someone openly disagreeing with your opinion in a meeting", {"rejection_sensitivity": 2}),
        ("Someone being perfectly pleasant but you can't tell if they genuinely like you", {"rejection_sensitivity": 1})
    ]),
    tier="trap", trap=True, cg="rs_interpretation_1", opacity=0.8))

questions.append(q("rejection_sensitivity", "temporal",
    "Think about a time someone rejected you clearly (turned down a date, fired you, excluded you). How much does it still affect your behavior today?",
    opts([
        ("It doesn't — I processed it and moved on", {"rejection_sensitivity": 5}),
        ("I learned from it in a healthy way — adjusted some things", {"rejection_sensitivity": 4}),
        ("I can still feel the sting if I think about it, but I don't think about it often", {"rejection_sensitivity": 3}),
        ("It fundamentally changed how I approach similar situations — I'm much more guarded now", {"rejection_sensitivity": 1})
    ]),
    tier="core", cg="rs_recovery_1", opacity=0.7))

questions.append(q("rejection_sensitivity", "scenario",
    "You're at a work meeting. Your boss asks for volunteers for a high-visibility project. You want to do it but:",
    opts([
        ("You raise your hand immediately — this is your kind of thing", {"rejection_sensitivity": 5}),
        ("You volunteer, heart racing a little, but you go for it", {"rejection_sensitivity": 4}),
        ("You wait to see if anyone else volunteers first — if they do, you stay quiet", {"rejection_sensitivity": 2}),
        ("You stay silent because the pain of being passed over would be worse than not trying", {"rejection_sensitivity": 1})
    ]),
    tier="triangulation", cg="rs_social_1", opacity=0.65))

questions.append(q("rejection_sensitivity", "somatic",
    "When you see an acquaintance in public and they don't acknowledge you, your body:",
    opts([
        ("Nothing happens — they probably didn't see you", {"rejection_sensitivity": 5}),
        ("A quick flash of 'huh' and then you forget about it", {"rejection_sensitivity": 4}),
        ("Tenses — were you just intentionally ignored?", {"rejection_sensitivity": 2}),
        ("Burns with the certainty that they saw you and chose to pretend they didn't", {"rejection_sensitivity": 1})
    ]),
    tier="consistency_check", cg="rs_social_1", opacity=0.6))

questions.append(q("rejection_sensitivity", "behavioral_recall",
    "How often do you soften requests or opinions with qualifiers like 'this might be stupid but...' or 'you can totally say no...'?",
    opts([
        ("Rarely — I say what I think directly", {"rejection_sensitivity": 5}),
        ("Sometimes, when the stakes feel high", {"rejection_sensitivity": 3}),
        ("Often — I'm cushioning against potential rejection", {"rejection_sensitivity": 2}),
        ("Almost always — I need to give people an easy out so the rejection hurts less", {"rejection_sensitivity": 1})
    ]),
    tier="core", cg="rs_interpretation_1", opacity=0.6))

questions.append(q("rejection_sensitivity", "scenario",
    "You send a work email with an idea to your team. Nobody responds or acknowledges it. Three days later someone else suggests basically the same thing and gets praise. You:",
    opts([
        ("Speak up — 'I actually suggested that on Tuesday, happy to collaborate'", {"rejection_sensitivity": 5}),
        ("Feel frustrated but say nothing — it's just work politics", {"rejection_sensitivity": 3}),
        ("Take it as confirmation that your contributions don't matter", {"rejection_sensitivity": 1}),
        ("Wonder if your version was worse somehow and that's why it was ignored", {"rejection_sensitivity": 2})
    ]),
    tier="triangulation", cg="rs_recovery_1", opacity=0.65))

questions.append(q("rejection_sensitivity", "partner_perspective",
    "Your partner goes out with friends and posts photos looking like they're having an amazing time — way more fun than they seem to have with you. You:",
    opts([
        ("Happy for them — different relationships bring out different energy", {"rejection_sensitivity": 5}),
        ("A small twinge of jealousy but mostly glad they're having fun", {"rejection_sensitivity": 4}),
        ("Start questioning whether they're happier without you", {"rejection_sensitivity": 2}),
        ("Feel actively hurt — if they can light up like that, why don't they with you?", {"rejection_sensitivity": 1})
    ]),
    tier="core", cg="rs_interpretation_1", opacity=0.7))

questions.append(q("rejection_sensitivity", "trap",
    "A new colleague at work seems to click with everyone immediately except you. Your interactions are fine but unremarkable. You:",
    opts([
        ("Don't notice or care — not everyone clicks", {"rejection_sensitivity": 5}),
        ("Notice but figure it'll develop naturally over time", {"rejection_sensitivity": 4}),
        ("Start trying harder to be likeable around them", {"rejection_sensitivity": 2, "external_validation": 3}),
        ("Preemptively decide you don't like them either — get ahead of the rejection", {"rejection_sensitivity": 1})
    ]),
    tier="trap", trap=True, cg="rs_social_1", opacity=0.6))

questions.append(q("rejection_sensitivity", "forced_choice",
    "Honestly — do you sometimes avoid getting close to people because then they can't reject the real you?",
    opts([
        ("No — I let people in and accept the risk", {"rejection_sensitivity": 5}),
        ("Occasionally, with certain types of people", {"rejection_sensitivity": 3}),
        ("More often than I'd like to admit", {"rejection_sensitivity": 2}),
        ("That's basically my social strategy", {"rejection_sensitivity": 1})
    ]),
    tier="core", cg="rs_recovery_1", opacity=0.8))

questions.append(q("rejection_sensitivity", "behavioral_recall",
    "When entering a room full of people you don't know well, how much mental energy goes to monitoring whether people seem glad to see you?",
    opts([
        ("Zero — I focus on finding someone interesting to talk to", {"rejection_sensitivity": 5}),
        ("A little — normal social awareness", {"rejection_sensitivity": 4}),
        ("A lot — I'm constantly scanning for disinterest or discomfort", {"rejection_sensitivity": 2}),
        ("Almost all of it — my attention is entirely on how I'm being received", {"rejection_sensitivity": 1})
    ]),
    tier="triangulation", cg="rs_social_1", opacity=0.65))

questions.append(q("rejection_sensitivity", "scenario",
    "You overhear your name mentioned in a conversation you're not part of. Your immediate assumption is:",
    opts([
        ("Neutral curiosity — could be anything", {"rejection_sensitivity": 5}),
        ("Probably something positive or benign", {"rejection_sensitivity": 4}),
        ("A spike of anxiety — they're saying something negative", {"rejection_sensitivity": 2}),
        ("Certainty that it's criticism — and you strain to hear the details", {"rejection_sensitivity": 1})
    ]),
    tier="consistency_check", cg="rs_interpretation_1", opacity=0.6))

questions.append(q("rejection_sensitivity", "temporal",
    "Looking back at your relationship history, how much has fear of rejection shaped who you've dated or befriended?",
    opts([
        ("Not much — I pursue connections with people I'm genuinely drawn to", {"rejection_sensitivity": 5}),
        ("Some — I've avoided reaching out to people I thought were 'out of my league'", {"rejection_sensitivity": 3}),
        ("A lot — I tend to choose people who I'm confident won't reject me", {"rejection_sensitivity": 2}),
        ("Entirely — I only get close to people who clearly want me first", {"rejection_sensitivity": 1})
    ]),
    tier="core", cg="rs_recovery_1", opacity=0.75))

# ============================================================
# SELF_FORGIVENESS (24 questions)
# ============================================================

questions.append(q("self_forgiveness", "scenario",
    "You said something in anger to a friend that was true but delivered cruelly. They've forgiven you. A month later, you:",
    opts([
        ("Have forgiven yourself too — the apology was sincere, the lesson was learned", {"self_forgiveness": 5}),
        ("Still feel a twinge when you think about it, but it's fading", {"self_forgiveness": 4}),
        ("Replay the moment regularly and wish you could undo it", {"self_forgiveness": 2}),
        ("Carry it as evidence of who you are under pressure — unforgivable", {"self_forgiveness": 1})
    ]),
    tier="core", cg="sf_release_1", opacity=0.7))

questions.append(q("self_forgiveness", "temporal",
    "How many things from more than 5 years ago do you still actively beat yourself up about?",
    opts([
        ("None — anything that old has been processed", {"self_forgiveness": 5}),
        ("One or two, but they're genuinely serious", {"self_forgiveness": 3}),
        ("Several — I have an excellent memory for my own failures", {"self_forgiveness": 2}),
        ("I've lost count — the older stuff has just piled up with the new stuff", {"self_forgiveness": 1})
    ]),
    tier="core", cg="sf_accumulation_1", opacity=0.7))

questions.append(q("self_forgiveness", "somatic",
    "When you're lying in bed at night and a past mistake surfaces in your mind, your body:",
    opts([
        ("Registers it briefly, then lets it go — you breathe through it", {"self_forgiveness": 5}),
        ("Tenses for a moment, then you redirect your thoughts", {"self_forgiveness": 4}),
        ("Floods with cortisol — you're suddenly wide awake reliving it", {"self_forgiveness": 2}),
        ("Curls up — you physically cringe or make a noise to stop the memory", {"self_forgiveness": 1})
    ]),
    tier="core", cg="sf_release_1", opacity=0.75))

questions.append(q("self_forgiveness", "forced_choice",
    "Which feels more true?",
    opts([
        ("Forgiving yourself is necessary for growth", {"self_forgiveness": 5}),
        ("Forgiving yourself too easily means you'll do it again", {"self_forgiveness": 1})
    ]),
    tier="core", cg="sf_philosophy_1", opacity=0.85))

questions.append(q("self_forgiveness", "behavioral_recall",
    "After a breakup where you were at fault, how do you process it?",
    opts([
        ("Grieve, reflect on what you'd do differently, then move forward", {"self_forgiveness": 5}),
        ("Carry guilt for a while but eventually let it go", {"self_forgiveness": 4}),
        ("Use it as a reason to delay your next relationship — you need to 'fix yourself first' (indefinitely)", {"self_forgiveness": 2}),
        ("Never fully recover — the guilt becomes part of your identity", {"self_forgiveness": 1})
    ]),
    tier="core", cg="sf_release_1", opacity=0.7))

questions.append(q("self_forgiveness", "scenario",
    "A therapist tells you that you need to forgive yourself. Your honest reaction is:",
    opts([
        ("Agree — you know you're too hard on yourself and want to change", {"self_forgiveness": 4}),
        ("You've already done that work — self-compassion is a practice for you", {"self_forgiveness": 5}),
        ("Skepticism — sounds like letting yourself off the hook", {"self_forgiveness": 2}),
        ("Anger — they don't understand what you did. Some things shouldn't be forgiven.", {"self_forgiveness": 1})
    ]),
    tier="triangulation", cg="sf_philosophy_1", opacity=0.75))

questions.append(q("self_forgiveness", "partner_perspective",
    "Your partner says 'You need to stop punishing yourself for that — it was years ago.' You feel:",
    opts([
        ("Heard — they're right, and their saying it helps you let go", {"self_forgiveness": 4}),
        ("Already there — you appreciate the reminder but you've mostly forgiven yourself", {"self_forgiveness": 5}),
        ("Frustrated — it's easy for them to say, they're not the one who did it", {"self_forgiveness": 2}),
        ("Undeserving of their compassion — which makes you feel worse", {"self_forgiveness": 1})
    ]),
    tier="triangulation", cg="sf_release_1", opacity=0.7))

questions.append(q("self_forgiveness", "scenario",
    "You make the same mistake twice — something you swore you'd never do again. Your self-talk sounds like:",
    opts([
        ("'Alright, clearly I need a different approach. What am I missing?'", {"self_forgiveness": 5}),
        ("'Damn it. Okay, regroup.'", {"self_forgiveness": 4}),
        ("'Of course. This is just who I am. I'll never change.'", {"self_forgiveness": 1}),
        ("'I'm disgusted with myself. I don't deserve [good thing] until I fix this.'", {"self_forgiveness": 1})
    ]),
    tier="core", cg="sf_accumulation_1", opacity=0.7))

questions.append(q("self_forgiveness", "temporal",
    "If a friend made the exact same mistake you're beating yourself up about, would you hold it against them as long as you've held it against yourself?",
    opts([
        ("No — I'd have forgiven them long ago. The double standard is obvious.", {"self_forgiveness": 2}),
        ("Probably not — I know I'm harder on myself than others", {"self_forgiveness": 3}),
        ("About the same — I hold everyone to high standards", {"self_forgiveness": 3}),
        ("I wouldn't hold it against them at all — but I'm different, I should have known better", {"self_forgiveness": 1})
    ]),
    tier="trap", trap=True, cg="sf_philosophy_1", opacity=0.75))

questions.append(q("self_forgiveness", "somatic",
    "When someone brings up a topic related to your biggest regret, even tangentially, your body:",
    opts([
        ("Stays calm — the topic is separate from your personal history with it", {"self_forgiveness": 5}),
        ("Stiffens briefly but you participate in the conversation normally", {"self_forgiveness": 4}),
        ("Goes on high alert — you manage the conversation away from dangerous territory", {"self_forgiveness": 2}),
        ("Shuts down — you can't engage without the shame flooding in", {"self_forgiveness": 1})
    ]),
    tier="triangulation", cg="sf_release_1", opacity=0.75))

questions.append(q("self_forgiveness", "behavioral_recall",
    "Do you have rules or punishments you impose on yourself as penance for past mistakes? (e.g., 'I don't deserve vacations,' 'I have to work twice as hard as everyone')",
    opts([
        ("No — that sounds unhealthy", {"self_forgiveness": 5}),
        ("Not consciously, but now that you mention it, maybe...", {"self_forgiveness": 3}),
        ("Yes, a few. They feel like the minimum I owe.", {"self_forgiveness": 2}),
        ("Yes, and I add new ones regularly", {"self_forgiveness": 1})
    ]),
    tier="core", cg="sf_accumulation_1", opacity=0.75))

questions.append(q("self_forgiveness", "forced_choice",
    "Pick the one closer to how you actually operate:",
    opts([
        ("I make a mistake, feel bad, learn, and move on", {"self_forgiveness": 5}),
        ("I make a mistake, feel bad, learn, and continue feeling bad", {"self_forgiveness": 1})
    ]),
    tier="consistency_check", cg="sf_release_1", opacity=0.9))

questions.append(q("self_forgiveness", "scenario",
    "You broke a promise to your child (or someone who depends on you). You've apologized and they've moved on. But you:",
    opts([
        ("Have forgiven yourself — kids are resilient and you're a good parent overall", {"self_forgiveness": 5}),
        ("Still feel guilty sometimes but know one broken promise isn't defining", {"self_forgiveness": 4}),
        ("Use it as proof you're failing at the most important job you have", {"self_forgiveness": 1}),
        ("Have overcompensated so much they probably wish you'd stop", {"self_forgiveness": 2})
    ]),
    tier="core", cg="sf_accumulation_1", opacity=0.7))

questions.append(q("self_forgiveness", "partner_perspective",
    "Imagine your partner made the exact mistake you can't forgive yourself for. How would you want them to handle it?",
    opts([
        ("Apologize sincerely, learn from it, and let it go — exactly what I can't do for myself", {"self_forgiveness": 2}),
        ("Take it seriously but not let it define them — which is what I'm working toward", {"self_forgiveness": 3}),
        ("I'd hold them to the same standard I hold myself — no easy forgiveness", {"self_forgiveness": 2}),
        ("I'd be compassionate with them immediately — I just can't do that for me", {"self_forgiveness": 1})
    ]),
    tier="trap", trap=True, cg="sf_philosophy_1", opacity=0.75))

questions.append(q("self_forgiveness", "temporal",
    "Imagine you're 80 years old, looking back at the thing you feel worst about now. From that perspective:",
    opts([
        ("It shrinks — a blip in a long life", {"self_forgiveness": 5}),
        ("It's still there but it's one of many chapters", {"self_forgiveness": 4}),
        ("I can see myself still carrying it at 80", {"self_forgiveness": 1}),
        ("I genuinely can't imagine a future where I've forgiven myself for it", {"self_forgiveness": 1})
    ]),
    tier="triangulation", cg="sf_release_1", opacity=0.7))

questions.append(q("self_forgiveness", "behavioral_recall",
    "How often do you engage in self-sabotage — ruining good things because part of you feels you don't deserve them?",
    opts([
        ("Never, or not that I'm aware of", {"self_forgiveness": 5}),
        ("It's happened once or twice and I caught it", {"self_forgiveness": 4}),
        ("More than I'd like — there's definitely a pattern", {"self_forgiveness": 2}),
        ("Consistently — it's the main way my self-unforgiveness shows up", {"self_forgiveness": 1})
    ]),
    tier="core", cg="sf_accumulation_1", opacity=0.7))

questions.append(q("self_forgiveness", "scenario",
    "You've been working really hard on improving a personal flaw. You slip up. Your inner voice says:",
    opts([
        ("'Setbacks happen. The trend line is still positive.'", {"self_forgiveness": 5}),
        ("'Frustrating, but I'll get back on track.'", {"self_forgiveness": 4}),
        ("'See? Nothing ever changes. Why do I even try?'", {"self_forgiveness": 1}),
        ("'I should be further along by now. What's wrong with me?'", {"self_forgiveness": 2})
    ]),
    tier="consistency_check", cg="sf_philosophy_1", opacity=0.65))

questions.append(q("self_forgiveness", "somatic",
    "When you achieve something good, do you feel a pull to immediately remember something bad you've done — like you don't deserve to celebrate?",
    opts([
        ("No — I enjoy successes without qualification", {"self_forgiveness": 5}),
        ("Occasionally, but I can override it", {"self_forgiveness": 4}),
        ("Yes — success triggers the guilt reflex reliably", {"self_forgiveness": 2}),
        ("Always — I don't deserve good things until I've paid off the debt of my past", {"self_forgiveness": 1})
    ]),
    tier="triangulation", cg="sf_accumulation_1", opacity=0.75))

questions.append(q("self_forgiveness", "forced_choice",
    "Which terrifies you more?",
    opts([
        ("Forgiving yourself and then making the same mistake again", {"self_forgiveness": 2}),
        ("Never forgiving yourself and carrying it to your grave", {"self_forgiveness": 4})
    ]),
    tier="trap", trap=True, cg="sf_philosophy_1", opacity=0.85))

questions.append(q("self_forgiveness", "scenario",
    "Someone says 'everyone deserves a second chance.' Your honest gut reaction:",
    opts([
        ("Agree — and that includes me", {"self_forgiveness": 5}),
        ("Agree for others, but I'm on my fifth chance and that's different", {"self_forgiveness": 2}),
        ("Depends on what they did — some things don't get second chances", {"self_forgiveness": 3}),
        ("Nice sentiment but naive — some of us have used up our chances", {"self_forgiveness": 1})
    ]),
    tier="triangulation", cg="sf_philosophy_1", opacity=0.7))

questions.append(q("self_forgiveness", "behavioral_recall",
    "When something goes wrong, how quickly do you shift from 'what happened' to 'what's wrong with me'?",
    opts([
        ("I usually stay focused on what happened — it's more useful", {"self_forgiveness": 5}),
        ("I have to actively redirect from self-blame to problem-solving", {"self_forgiveness": 3}),
        ("Almost instantly — 'what happened' and 'what's wrong with me' feel like the same question", {"self_forgiveness": 1}),
        ("I skip 'what happened' entirely and go straight to 'I'm the problem'", {"self_forgiveness": 1})
    ]),
    tier="core", cg="sf_release_1", opacity=0.7))

questions.append(q("self_forgiveness", "partner_perspective",
    "If you could hear your harshest inner critic's voice coming from someone else, would you consider it abusive?",
    opts([
        ("Probably not — my inner critic is firm but fair", {"self_forgiveness": 5}),
        ("It would sound harsh but not abusive", {"self_forgiveness": 3}),
        ("Honestly, yes — I wouldn't let anyone talk to my friends that way", {"self_forgiveness": 2}),
        ("Absolutely — the things I say to myself are brutal", {"self_forgiveness": 1})
    ]),
    tier="trap", trap=True, cg="sf_accumulation_1", opacity=0.75))

questions.append(q("self_forgiveness", "scenario",
    "You discover that something you felt guilty about for years was actually a misunderstanding — you weren't at fault. Do you feel relief?",
    opts([
        ("Immense relief — you release it completely", {"self_forgiveness": 5}),
        ("Mostly relieved but frustrated you carried it so long", {"self_forgiveness": 4}),
        ("Some relief but you find a new angle to blame yourself (you should have clarified sooner)", {"self_forgiveness": 2}),
        ("Not really — the guilt has become part of you regardless of facts", {"self_forgiveness": 1})
    ]),
    tier="core", cg="sf_release_1", opacity=0.7))

questions.append(q("self_forgiveness", "temporal",
    "How does your capacity for self-forgiveness compare to 10 years ago?",
    opts([
        ("Much better — I've done real work on this", {"self_forgiveness": 5}),
        ("Somewhat better — age has softened me", {"self_forgiveness": 4}),
        ("About the same", {"self_forgiveness": 3}),
        ("Worse — the pile of things to forgive keeps growing and I'm losing ground", {"self_forgiveness": 1})
    ]),
    tier="consistency_check", cg="sf_accumulation_1", opacity=0.65))

# ============================================================
# EXTERNAL_VALIDATION (24 questions)
# ============================================================

questions.append(q("external_validation", "scenario",
    "You finish a creative project you're proud of. Nobody sees it. How satisfying is that?",
    opts([
        ("Deeply — the work itself is the reward", {"external_validation": 5}),
        ("Mostly satisfying but you'd enjoy sharing it", {"external_validation": 4}),
        ("Incomplete — if nobody sees it, does it even count?", {"external_validation": 2}),
        ("Pointless — you make things for the response, not the process", {"external_validation": 1})
    ]),
    tier="core", cg="ev_achievement_1", opacity=0.65))

questions.append(q("external_validation", "behavioral_recall",
    "When you get dressed for a regular day (not a special event), who are you dressing for?",
    opts([
        ("Myself — I wear what makes me feel good regardless of audience", {"external_validation": 5}),
        ("Mostly myself, but I'm aware of how I'll be perceived", {"external_validation": 4}),
        ("It depends entirely on who I'm going to see today", {"external_validation": 2}),
        ("I wouldn't bother looking good if no one was going to see me", {"external_validation": 1})
    ]),
    tier="core", cg="ev_daily_1", opacity=0.55))

questions.append(q("external_validation", "somatic",
    "You spend an entire day doing exactly what YOU want — your choices, your pace. At the end of the day, you feel:",
    opts([
        ("Restored and grounded — this is how all days should feel", {"external_validation": 5}),
        ("Good, but a little guilty for being 'selfish'", {"external_validation": 3}),
        ("Restless — like the day didn't count because no one witnessed it", {"external_validation": 2}),
        ("Anxious — what did people think about your absence?", {"external_validation": 1})
    ]),
    tier="core", cg="ev_daily_1", opacity=0.7))

questions.append(q("external_validation", "forced_choice",
    "Which matters more to you RIGHT NOW (not which should matter more)?",
    opts([
        ("Knowing you did a good job", {"external_validation": 5}),
        ("Being told you did a good job", {"external_validation": 1})
    ]),
    tier="core", cg="ev_achievement_1", opacity=0.85))

questions.append(q("external_validation", "scenario",
    "You take a bold professional risk. It pays off beautifully, but your boss doesn't notice or comment. You feel:",
    opts([
        ("Satisfied — the result speaks for itself", {"external_validation": 5}),
        ("Good about the outcome but disappointed by the lack of recognition", {"external_validation": 3}),
        ("Like it barely happened — without acknowledgment, the win feels hollow", {"external_validation": 1}),
        ("Motivated to make the NEXT win impossible to ignore", {"external_validation": 2})
    ]),
    tier="triangulation", cg="ev_achievement_1", opacity=0.65))

questions.append(q("external_validation", "partner_perspective",
    "Your partner compliments you. How long does the good feeling last?",
    opts([
        ("It's nice but doesn't fundamentally change my mood either way", {"external_validation": 5}),
        ("Warm glow for a while — I appreciate it", {"external_validation": 4}),
        ("It lifts me for hours — I run on compliments", {"external_validation": 2}),
        ("It's the only thing that makes me feel okay about myself", {"external_validation": 1})
    ]),
    tier="core", cg="ev_relationships_1", opacity=0.7))

questions.append(q("external_validation", "behavioral_recall",
    "How often do you check likes, comments, or reactions on things you post online?",
    opts([
        ("I rarely post, or if I do, I post and forget about it", {"external_validation": 5}),
        ("I check once or twice, then move on", {"external_validation": 4}),
        ("Multiple times in the first hour, then it tapers", {"external_validation": 2}),
        ("Compulsively until the engagement confirms I'm okay", {"external_validation": 1})
    ]),
    tier="core", cg="ev_daily_1", opacity=0.55))

questions.append(q("external_validation", "scenario",
    "You're at a party and you overhear someone praising you to another person. How much does this affect your night?",
    opts([
        ("Mildly pleasant — cool that they think well of me", {"external_validation": 4}),
        ("Doesn't change anything — I already knew where I stood", {"external_validation": 5}),
        ("Makes my whole night — I glow for hours", {"external_validation": 2}),
        ("Becomes the thing I replay most when I get home", {"external_validation": 1})
    ]),
    tier="triangulation", cg="ev_relationships_1", opacity=0.6))

questions.append(q("external_validation", "temporal",
    "Think about the last goal you achieved. Which part felt most rewarding?",
    opts([
        ("The moment I knew I'd done it — internal satisfaction", {"external_validation": 5}),
        ("Telling someone about it and seeing their reaction", {"external_validation": 2}),
        ("The process itself — the achievement was just the end point", {"external_validation": 5}),
        ("The public recognition that followed", {"external_validation": 1})
    ]),
    tier="triangulation", cg="ev_achievement_1", opacity=0.6))

questions.append(q("external_validation", "forced_choice",
    "Would you rather:",
    opts([
        ("Do meaningful work that nobody ever knows about", {"external_validation": 5}),
        ("Get credit for work that wasn't actually yours", {"external_validation": 1})
    ]),
    tier="trap", trap=True, cg="ev_achievement_1", opacity=0.8))

questions.append(q("external_validation", "somatic",
    "When you accomplish something and there's nobody around to tell, your body:",
    opts([
        ("Still feels the satisfaction — you might even pump your fist", {"external_validation": 5}),
        ("Feels good but reaches for the phone to share it", {"external_validation": 3}),
        ("Deflates slightly — the moment needs a witness to feel real", {"external_validation": 2}),
        ("Feels almost nothing — unwitnessed achievements don't register emotionally", {"external_validation": 1})
    ]),
    tier="core", cg="ev_achievement_1", opacity=0.7))

questions.append(q("external_validation", "scenario",
    "You go on a vacation and decide not to post anything on social media about it. By day 3:",
    opts([
        ("You're fully present — not posting hasn't crossed your mind since day 1", {"external_validation": 5}),
        ("You've enjoyed the freedom from performing your life", {"external_validation": 4}),
        ("You've taken photos 'for later' with a growing urge to share", {"external_validation": 2}),
        ("You feel like the vacation barely counts if nobody knows about it", {"external_validation": 1})
    ]),
    tier="triangulation", cg="ev_daily_1", opacity=0.55))

questions.append(q("external_validation", "behavioral_recall",
    "When making decisions about your appearance, career, or lifestyle, how much weight does 'what will people think' carry?",
    opts([
        ("Very little — I live on my own terms", {"external_validation": 5}),
        ("It's one factor among many", {"external_validation": 4}),
        ("It's usually the loudest voice in the room", {"external_validation": 2}),
        ("It's basically the deciding factor", {"external_validation": 1})
    ]),
    tier="consistency_check", cg="ev_daily_1", opacity=0.65))

questions.append(q("external_validation", "partner_perspective",
    "How would you feel if your partner loved you deeply but never expressed it verbally — just through actions?",
    opts([
        ("Perfectly loved — actions speak louder", {"external_validation": 5}),
        ("Mostly fine but I'd miss hearing it sometimes", {"external_validation": 4}),
        ("Insecure — I need to hear it to believe it", {"external_validation": 2}),
        ("Devastated — without the words, I'd always wonder if it was real", {"external_validation": 1})
    ]),
    tier="core", cg="ev_relationships_1", opacity=0.7))

questions.append(q("external_validation", "scenario",
    "You hold a controversial opinion that you've thought through carefully. Everyone in the room disagrees. You:",
    opts([
        ("Hold your ground — you've done the work and you're comfortable being the minority", {"external_validation": 5}),
        ("Present your case but acknowledge their points — open to being wrong", {"external_validation": 5}),
        ("Start doubting yourself — that many people can't all be wrong", {"external_validation": 2}),
        ("Quickly agree with the group — being the outsider isn't worth it", {"external_validation": 1})
    ]),
    tier="core", cg="ev_social_1", opacity=0.65))

questions.append(q("external_validation", "temporal",
    "If all social media disappeared tomorrow and nobody could see what you were doing with your life, what would change?",
    opts([
        ("Nothing meaningful — my life isn't performed for an audience", {"external_validation": 5}),
        ("I'd miss sharing but my behavior wouldn't change", {"external_validation": 4}),
        ("I'd feel untethered — a lot of what I do is partially for the perception of it", {"external_validation": 2}),
        ("I'd honestly struggle to feel motivated — external eyes drive a lot of my behavior", {"external_validation": 1})
    ]),
    tier="triangulation", cg="ev_daily_1", opacity=0.65))

questions.append(q("external_validation", "somatic",
    "When someone you admire criticizes your work (constructively), your body:",
    opts([
        ("Takes it in like fuel — criticism from smart people is valuable", {"external_validation": 5}),
        ("Stiffens initially but you lean into the feedback", {"external_validation": 4}),
        ("Crumbles — their opinion feels like a verdict on your worth", {"external_validation": 1}),
        ("Shuts down — you smile and nod but inside you're devastated", {"external_validation": 1})
    ]),
    tier="core", cg="ev_achievement_1", opacity=0.7))

questions.append(q("external_validation", "behavioral_recall",
    "How often do you do things primarily because they'll look good to others rather than because you genuinely want to?",
    opts([
        ("Rarely — I've gotten good at separating my wants from others' expectations", {"external_validation": 5}),
        ("Sometimes — social pressure is real but I'm aware of it", {"external_validation": 3}),
        ("Frequently — I'm honestly not sure where their expectations end and my desires begin", {"external_validation": 2}),
        ("Almost always — my life is largely built around what impresses people", {"external_validation": 1})
    ]),
    tier="consistency_check", cg="ev_social_1", opacity=0.7))

questions.append(q("external_validation", "scenario",
    "You write a heartfelt email to someone. They respond with 'thanks.' That's it. You feel:",
    opts([
        ("Fine — not everyone reciprocates depth and that's okay", {"external_validation": 5}),
        ("A little let down but you don't take it personally", {"external_validation": 4}),
        ("Foolish for being vulnerable — you exposed yourself for nothing", {"external_validation": 2}),
        ("Crushed — and you'll never be that open with them again", {"external_validation": 1, "rejection_sensitivity": 3})
    ]),
    tier="triangulation", cg="ev_relationships_1", opacity=0.65))

questions.append(q("external_validation", "forced_choice",
    "Finish this sentence honestly: 'I feel most like myself when...'",
    opts([
        ("I'm alone doing something I love", {"external_validation": 5}),
        ("I'm with people who see and appreciate me", {"external_validation": 2}),
        ("I've just accomplished something impressive", {"external_validation": 3}),
        ("Someone I respect tells me they're proud of me", {"external_validation": 1})
    ]),
    tier="core", cg="ev_social_1", opacity=0.75))

questions.append(q("external_validation", "partner_perspective",
    "If your partner stopped complimenting you entirely — still loving, still present, just no verbal affirmation — how long before it affected your self-image?",
    opts([
        ("It wouldn't — my self-image doesn't depend on their words", {"external_validation": 5}),
        ("Eventually I'd miss it, but I'd be fine", {"external_validation": 4}),
        ("Within a few weeks I'd start feeling insecure", {"external_validation": 2}),
        ("Within days — their affirmation is the main thing holding my self-image together", {"external_validation": 1})
    ]),
    tier="consistency_check", cg="ev_relationships_1", opacity=0.7))

questions.append(q("external_validation", "trap",
    "When you help someone, how important is it that they know it was you?",
    opts([
        ("Not important — the help is what matters", {"external_validation": 5}),
        ("Not important but I'd appreciate a thank you", {"external_validation": 4}),
        ("Pretty important — I want credit for good deeds", {"external_validation": 2}),
        ("If they don't know, I feel like I wasted my time", {"external_validation": 1})
    ]),
    tier="trap", trap=True, cg="ev_social_1", opacity=0.6))

questions.append(q("external_validation", "temporal",
    "When did you last do something difficult purely because you thought it was right, with no chance of anyone knowing?",
    opts([
        ("Recently — it happens regularly because I'm guided by internal values", {"external_validation": 5}),
        ("A while ago — but I know I would if the situation came up", {"external_validation": 4}),
        ("I honestly can't remember a time", {"external_validation": 2}),
        ("That's not how motivation works for me — visibility drives my behavior", {"external_validation": 1})
    ]),
    tier="triangulation", cg="ev_social_1", opacity=0.7))

questions.append(q("external_validation", "scenario",
    "You're at a crossroads: one path is prestigious and everyone will be impressed, the other is humble but deeply aligned with what you actually want. You:",
    opts([
        ("Take the aligned path without much deliberation", {"external_validation": 5}),
        ("Take the aligned path but feel some grief about the prestige", {"external_validation": 4}),
        ("Agonize because the prestige path feels SO good to imagine telling people about", {"external_validation": 2}),
        ("Take the prestigious path — if you're honest, the external perception IS what you want", {"external_validation": 1})
    ]),
    tier="core", cg="ev_achievement_1", opacity=0.7))

assert len(questions) == 120, f"Expected 120, got {len(questions)}"

with open("/Users/user/personal/sb/trueassess/priv/question_bank/self_worth.json", "w") as f:
    json.dump(questions, f, indent=2)

print(f"Self-worth: {len(questions)} questions written")

# Verify dimension distribution
from collections import Counter
dims = Counter(q["dimension"] for q in questions)
print("Distribution:", dict(dims))
tiers = Counter(q["tier_role"] for q in questions)
print("Tiers:", dict(tiers))
types = Counter(q["question_type"] for q in questions)
print("Types:", dict(types))
