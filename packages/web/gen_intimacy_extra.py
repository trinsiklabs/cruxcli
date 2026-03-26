import json

with open("/Users/user/personal/sb/trueassess/priv/question_bank/intimacy_style.json") as f:
    questions = json.load(f)

uid_counter = len(questions) + 1

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

# Additional emotional_vs_physical
q("emotional_vs_physical", "behavioral_recall", "How much does knowing a partner's inner world (their fears, dreams, wounds) enhance your sexual experience with them?", opts([
    ("Enormously — the more I know someone's soul, the more every touch means. Deep knowledge IS foreplay", {"emotional_vs_physical": 5}),
    ("Significantly — emotional knowledge enriches physical intimacy", {"emotional_vs_physical": 4}),
    ("Somewhat — it's nice but doesn't change the physical experience much", {"emotional_vs_physical": 3}),
    ("Not much — I can have great sex without knowing their inner world", {"emotional_vs_physical": 1})
]))

# More vulnerability questions
q("vulnerability_in_sex", "scenario", "Sharing a fantasy you've never told anyone — something deeply personal that reveals your inner landscape. In a sexual context, sharing this:", opts([
    ("Is the ultimate intimacy — being known in my desires is more naked than any physical act", {"vulnerability_in_sex": 5}),
    ("Is scary but worth it with the right person", {"vulnerability_in_sex": 4}),
    ("Is too risky — some fantasies are mine alone", {"vulnerability_in_sex": 2}),
    ("Is unnecessary — fantasies don't need to be shared", {"vulnerability_in_sex": 1})
]))

q("vulnerability_in_sex", "behavioral_recall", "How often do you let a partner see you struggle sexually (difficulty with arousal, delayed orgasm, performance anxiety)?", opts([
    ("When it happens, I name it: 'I'm having trouble getting there tonight.' Hiding struggle creates more shame than sharing it", {"vulnerability_in_sex": 5}),
    ("Usually — I try to be honest about what's happening", {"vulnerability_in_sex": 4}),
    ("I hide it — I don't want them to feel responsible", {"vulnerability_in_sex": 2}),
    ("Always — I perform even when I'm struggling", {"vulnerability_in_sex": 1})
]))

# More aftercare
q("aftercare_needs", "scenario", "You had casual sex with someone new. The encounter was fun but your aftercare needs weren't met (they left quickly). You:", opts([
    ("Feel the gap strongly and make a note: next time, negotiate aftercare BEFORE play, even with casual partners", {"aftercare_needs": 5}),
    ("Feel somewhat off but manage with self-care", {"aftercare_needs": 4}),
    ("It was casual — aftercare wasn't expected", {"aftercare_needs": 2}),
    ("No impact — casual sex doesn't require aftercare", {"aftercare_needs": 1})
]))

q("aftercare_needs", "behavioral_recall", "How specific are your aftercare preferences?", opts([
    ("Very — I know I need X minutes of holding, specific words, water, a blanket, and then quiet time. I've mapped this precisely", {"aftercare_needs": 5}),
    ("Fairly specific — I know the general categories of what I need", {"aftercare_needs": 4}),
    ("Vague — I know I want closeness but haven't mapped specifics", {"aftercare_needs": 3}),
    ("I don't have specific aftercare preferences", {"aftercare_needs": 1})
]))

# More attachment
q("attachment_in_sex", "forced_choice", "Sex without kissing:", opts([
    ("Feels disconnected — kissing is how I maintain the emotional thread during physical intimacy", {"attachment_in_sex": 5}),
    ("Is possible but less connecting", {"attachment_in_sex": 4}),
    ("Is fine — kissing is nice but not necessary", {"attachment_in_sex": 3}),
    ("Is preferred sometimes — kissing is too intimate for casual sex", {"attachment_in_sex": 1})
]))

q("attachment_in_sex", "temporal", "How does sexual frequency correlate with your sense of relationship security?", opts([
    ("Directly — when sex declines, my attachment anxiety spikes. Regular sex IS my security signal", {"attachment_in_sex": 5}),
    ("Somewhat — I feel more secure when our sex life is active", {"attachment_in_sex": 4}),
    ("Loosely — sex is nice but my security comes from other things", {"attachment_in_sex": 3}),
    ("Not at all — relationship security is about trust and communication, not sex frequency", {"attachment_in_sex": 1})
]))

q("attachment_in_sex", "scenario", "A partner you're very attached to withdraws sexually for a period (stress, illness, medication). Your attachment system:", opts([
    ("Goes into overdrive — I feel rejected, panicky, and need constant reassurance that the relationship is okay", {"attachment_in_sex": 5}),
    ("Activates — I feel less secure and need to talk about it", {"attachment_in_sex": 4}),
    ("Stays relatively stable — I trust the relationship beyond sex", {"attachment_in_sex": 3}),
    ("Unaffected — their sexual withdrawal doesn't impact my sense of the relationship", {"attachment_in_sex": 1})
]))

q("attachment_in_sex", "behavioral_recall", "Oxytocin bonding: after sex, how long do you feel a heightened sense of closeness to your partner?", opts([
    ("Hours to days — the bonding effect lingers significantly", {"attachment_in_sex": 5}),
    ("A few hours", {"attachment_in_sex": 4}),
    ("An hour or so", {"attachment_in_sex": 3}),
    ("It fades almost immediately", {"attachment_in_sex": 1})
]))

# More initiation comfort
q("initiation_comfort", "scenario", "Initiating sex in a non-standard way (sending a suggestive text, leaving a toy on the bed, writing a note describing what you want):", opts([
    ("Is creative and I use multiple methods — I'm not limited to one initiation style", {"initiation_comfort": 5}),
    ("Is something I've tried and enjoyed", {"initiation_comfort": 4}),
    ("Feels too deliberate — I prefer in-the-moment initiation", {"initiation_comfort": 3}),
    ("Haven't tried — indirect initiation feels too vulnerable", {"initiation_comfort": 1})
]))

q("initiation_comfort", "forced_choice", "In a relationship where both people wait for the other to initiate, you:", opts([
    ("Recognize the pattern and break it: 'I notice we're both waiting. I'm going to commit to initiating more, and here's what that'll look like'", {"initiation_comfort": 5}),
    ("Eventually initiate, though it takes me longer than I'd like", {"initiation_comfort": 4}),
    ("Wait longer and longer", {"initiation_comfort": 2}),
    ("Accept a sexless pattern — neither of us wants it enough to go first", {"initiation_comfort": 1})
]))

q("initiation_comfort", "behavioral_recall", "Your comfort initiating specific sexual acts (oral sex, anal play, a particular kink) vs. initiating sex in general:", opts([
    ("I'm equally comfortable with both — if I want something, I ask for it", {"initiation_comfort": 5}),
    ("Initiating sex is easier than requesting specific acts", {"initiation_comfort": 4}),
    ("Both are difficult", {"initiation_comfort": 2}),
    ("I wait for my partner to suggest specific acts", {"initiation_comfort": 1})
]))

# More communication during
q("communication_during", "scenario", "Feedback loops during sex — continually adjusting based on partner's responses, asking for guidance, giving updates:", opts([
    ("Are how good sex works — sex is a real-time collaborative conversation, not a performance", {"communication_during": 5}),
    ("Are important — I check in and adjust", {"communication_during": 4}),
    ("Happen sometimes", {"communication_during": 3}),
    ("Are overthinking it — sex should be instinctive", {"communication_during": 1})
]))

q("communication_during", "behavioral_recall", "Can you articulate in the moment what specific touch, pressure, speed, or angle works best for you?", opts([
    ("Yes — I know my body well enough to give precise, helpful instructions in real-time", {"communication_during": 5}),
    ("Mostly — I can guide toward what works", {"communication_during": 4}),
    ("Sometimes — when I'm in my head enough to think about it", {"communication_during": 3}),
    ("No — I can't translate sensation into words quickly enough", {"communication_during": 1})
]))

q("communication_during", "scenario", "Laughing during sex (something awkward happens, a body makes a funny sound, you bump heads):", opts([
    ("Is wonderful — laughter during sex means we're present, connected, and not performing. It's one of my favorite things", {"communication_during": 5}),
    ("Is natural — we're human, funny things happen", {"communication_during": 4}),
    ("Is momentarily mood-breaking but recoverable", {"communication_during": 3}),
    ("Is mortifying — sex should be smooth and sexy", {"communication_during": 1})
]))

# More responsive desire
q("responsive_desire", "scenario", "Creating conditions for your desire (setting, timing, mental state) vs. waiting for desire to appear spontaneously:", opts([
    ("I actively create conditions — I know what activates my desire (reading erotica, a bath, a particular type of touch) and I set those up deliberately", {"responsive_desire": 5}),
    ("I sometimes set conditions — it helps", {"responsive_desire": 4}),
    ("I wait — desire should come naturally or not at all", {"responsive_desire": 2}),
    ("My desire is spontaneous and doesn't need setup", {"responsive_desire": 1})
]))

q("responsive_desire", "forced_choice", "The 'brakes and accelerators' model (things that inhibit vs. activate your desire):", opts([
    ("I know mine precisely — stress, body image, timing are my brakes; touch, certain words, specific contexts are my accelerators. Managing these IS managing my desire", {"responsive_desire": 5}),
    ("I have a general sense of what helps and hinders", {"responsive_desire": 4}),
    ("I haven't mapped this specifically", {"responsive_desire": 3}),
    ("My desire doesn't work this way — it's either there or not", {"responsive_desire": 1})
]))

q("responsive_desire", "behavioral_recall", "Have you ever said 'I'm not in the mood but I'm willing to see if I get there'?", opts([
    ("Regularly — this is my standard approach. Willingness ≠ desire, but willingness can LEAD to desire, and I've learned to trust that process", {"responsive_desire": 5}),
    ("Sometimes — and it usually works out", {"responsive_desire": 4}),
    ("Rarely — I only have sex when I feel active desire", {"responsive_desire": 2}),
    ("Never — if I'm not in the mood, I'm not having sex", {"responsive_desire": 1})
]))

# More spontaneous desire
q("spontaneous_desire", "scenario", "Multiple-times-a-day desire — wanting sex more than once in a day, different from marathon sex:", opts([
    ("Normal for me — I can want sex in the morning, afternoon, and evening, each time genuinely", {"spontaneous_desire": 5}),
    ("Happens sometimes — especially early in a relationship", {"spontaneous_desire": 4}),
    ("Rare — once is usually enough", {"spontaneous_desire": 3}),
    ("Very rare or never — once a day would already be a lot", {"spontaneous_desire": 1})
]))

q("spontaneous_desire", "forced_choice", "If you go several days without sexual activity or fantasy, you feel:", opts([
    ("Physically and mentally restless — unresolved sexual energy builds up and demands attention", {"spontaneous_desire": 5}),
    ("Somewhat itchy — I notice the absence", {"spontaneous_desire": 4}),
    ("Normal — a few days without sex barely registers", {"spontaneous_desire": 2}),
    ("Relieved — the break is welcome", {"spontaneous_desire": 1})
]))

q("spontaneous_desire", "behavioral_recall", "How often does your desire for sex disrupt your concentration on other things (work, hobbies, social situations)?", opts([
    ("Regularly — my sexual mind runs in the background constantly", {"spontaneous_desire": 5}),
    ("Sometimes — it intrudes on my thoughts a few times a week", {"spontaneous_desire": 4}),
    ("Rarely", {"spontaneous_desire": 3}),
    ("Almost never — sex doesn't compete with other mental activities for me", {"spontaneous_desire": 1})
]))

# Cross-cutting consistency/triangulation
q("emotional_vs_physical", "scenario", "Phone sex or sexting — intimate connection through words and imagination only, no physical contact:", opts([
    ("Can be deeply satisfying because the emotional and imaginative connection IS the sex for me", {"emotional_vs_physical": 5}),
    ("Is enjoyable — a good substitute when apart", {"emotional_vs_physical": 4}),
    ("Is okay but nothing compared to physical presence", {"emotional_vs_physical": 2}),
    ("Doesn't work — I need bodies, not words", {"emotional_vs_physical": 1})
]))

q("vulnerability_in_sex", "scenario", "Performance anxiety — worrying about whether you're good enough, lasting enough, responsive enough during sex:", opts([
    ("I've worked through this by embracing vulnerability — imperfect sex with authenticity beats perfect performance every time", {"vulnerability_in_sex": 5}),
    ("I experience it sometimes but don't let it stop me", {"vulnerability_in_sex": 4}),
    ("It significantly affects my sexual experience", {"vulnerability_in_sex": 2}),
    ("It's a constant presence that I mask with performance", {"vulnerability_in_sex": 1})
]))

q("aftercare_needs", "temporal", "How have your aftercare needs changed as you've gained more sexual experience?", opts([
    ("I've become more aware of them and more articulate about them — they haven't diminished, they've become better understood", {"aftercare_needs": 5}),
    ("I've learned what I need and ask for it more confidently", {"aftercare_needs": 4}),
    ("They've stayed about the same", {"aftercare_needs": 3}),
    ("I need less aftercare as I've become more experienced", {"aftercare_needs": 1})
]))

q("attachment_in_sex", "scenario", "A partner with a different attachment style in sex (e.g., they don't bond through sex the way you do). You:", opts([
    ("Name the difference: 'Sex creates deep bonding for me and I know it doesn't work that way for you. Let's talk about how we each feel connected'", {"attachment_in_sex": 5}),
    ("Notice the difference and try to adapt", {"attachment_in_sex": 4}),
    ("Feel confused by the mismatch", {"attachment_in_sex": 3}),
    ("It doesn't matter — sex is sex", {"attachment_in_sex": 1})
]))

q("initiation_comfort", "scenario", "Initiating after a dry spell — it's been weeks and the longer it goes, the harder it feels to break the pattern:", opts([
    ("I name the elephant: 'We haven't been intimate in a while and I miss it. Can we talk about what's going on?' Direct address breaks the cycle", {"initiation_comfort": 5}),
    ("I push through the discomfort and initiate physically", {"initiation_comfort": 4}),
    ("I wait for external circumstances to create an opening", {"initiation_comfort": 2}),
    ("The dry spell becomes self-perpetuating — neither of us breaks it", {"initiation_comfort": 1})
]))

q("communication_during", "scenario", "You've had an orgasm and your partner hasn't. Communicating about this:", opts([
    ("Is natural: 'Your turn — what do you need? Show me / tell me'", {"communication_during": 5}),
    ("I check in: 'Do you want me to keep going?'", {"communication_during": 4}),
    ("I continue without checking in — assumed they want more", {"communication_during": 3}),
    ("I hope they're satisfied and don't ask", {"communication_during": 1})
]))

q("responsive_desire", "scenario", "Reading erotica, watching porn, or engaging in fantasy as a way to activate desire (not just satisfy it):", opts([
    ("Is a deliberate tool I use — I know that my desire system responds to input, so I provide input when I want to activate it", {"responsive_desire": 5}),
    ("Works for me sometimes", {"responsive_desire": 4}),
    ("I use these when I'm already aroused, not to get aroused", {"responsive_desire": 2}),
    ("These don't affect my desire level", {"responsive_desire": 1})
]))

q("spontaneous_desire", "temporal", "How has your baseline desire level changed with age?", opts([
    ("Still high — my desire hasn't significantly diminished", {"spontaneous_desire": 5}),
    ("Somewhat lower but still present regularly", {"spontaneous_desire": 4}),
    ("Noticeably lower — desire is less frequent and less urgent", {"spontaneous_desire": 2}),
    ("Significantly lower — I rarely feel spontaneous desire anymore", {"spontaneous_desire": 1})
]))

# Final cross-cutting
q("emotional_vs_physical", "forced_choice", "Kissing deeply for 10 minutes without it leading to sex vs. 10 minutes of sex without kissing:", opts([
    ("Kissing — prolonged intimate kissing without an agenda is more connecting than agenda-driven sex", {"emotional_vs_physical": 5}),
    ("Kissing slightly edges it out", {"emotional_vs_physical": 4}),
    ("Sex", {"emotional_vs_physical": 2}),
    ("Definitely sex — kissing alone isn't enough", {"emotional_vs_physical": 1})
]))

q("vulnerability_in_sex", "forced_choice", "Your 'sexual shame' — things about your body, desires, or responses that you hide from partners:", opts([
    ("Minimal to none — I've done the work to accept and reveal myself fully", {"vulnerability_in_sex": 5}),
    ("A few things I'm still working on sharing", {"vulnerability_in_sex": 4}),
    ("Significant — there's a lot I don't show", {"vulnerability_in_sex": 2}),
    ("Pervasive — I hide most of my authentic sexual self", {"vulnerability_in_sex": 1})
]))

q("aftercare_needs", "scenario", "Morning-after check-in — texting or talking about last night's sex. You:", opts([
    ("Always do this — the check-in extends the aftercare and maintains connection", {"aftercare_needs": 5}),
    ("Usually — a quick 'last night was wonderful' text", {"aftercare_needs": 4}),
    ("Sometimes", {"aftercare_needs": 3}),
    ("Rarely — what happened last night stays last night", {"aftercare_needs": 1})
]))

q("attachment_in_sex", "forced_choice", "The phrase 'making love' vs. 'having sex' vs. 'fucking':", opts([
    ("Each describes a genuinely different experience, and 'making love' is the one that feeds my attachment needs most deeply", {"attachment_in_sex": 5}),
    ("I use different terms for different moods but they're all sex", {"attachment_in_sex": 4}),
    ("I prefer 'sex' or 'fucking' — 'making love' is too sentimental", {"attachment_in_sex": 2}),
    ("They're all the same thing with different labels", {"attachment_in_sex": 1})
]))

q("initiation_comfort", "forced_choice", "Seduction — the art of building desire in a partner through deliberate signals, touch, words:", opts([
    ("Is a skill I enjoy exercising — I can create desire in a partner through intentional seduction", {"initiation_comfort": 5}),
    ("Is fun when I'm in the mood for it", {"initiation_comfort": 4}),
    ("Feels performative — I prefer desire to emerge naturally", {"initiation_comfort": 3}),
    ("Is beyond my comfort zone — I don't know how to seduce", {"initiation_comfort": 1})
]))

q("communication_during", "scenario", "Your partner does something unexpected during sex — a new move, position, or sensation. You:", opts([
    ("Immediately respond with feedback: 'Oh — that's new. Keep going / hold on, not quite right / what are you doing? I like it'", {"communication_during": 5}),
    ("React naturally and discuss it later if needed", {"communication_during": 4}),
    ("Go with it without comment", {"communication_during": 3}),
    ("Freeze — unexpected things throw me off", {"communication_during": 1})
]))

q("responsive_desire", "temporal", "Your understanding of your own desire pattern has:", opts([
    ("Liberated me — once I understood that my desire is responsive, not broken, I stopped pathologizing myself and started working WITH my pattern", {"responsive_desire": 5}),
    ("Helped me make sense of past confusion about my desire", {"responsive_desire": 4}),
    ("Not been particularly relevant", {"responsive_desire": 3}),
    ("I don't think about desire patterns", {"responsive_desire": 1})
]))

q("spontaneous_desire", "scenario", "A new relationship: your desire in the first three months is:", opts([
    ("Through the roof — new relationship energy supercharges my already-high baseline desire", {"spontaneous_desire": 5}),
    ("Very high — NRE boosts things significantly", {"spontaneous_desire": 4}),
    ("Higher than normal but not dramatically", {"spontaneous_desire": 3}),
    ("Not that different from my baseline — NRE doesn't affect me much", {"spontaneous_desire": 1})
]))

# Final fillers
q("emotional_vs_physical", "scenario", "A partner who is emotionally available but physically unskilled vs. physically talented but emotionally guarded:", opts([
    ("Emotionally available, hands down — I can teach skills, I can't teach openness", {"emotional_vs_physical": 5}),
    ("Probably emotionally available — skills develop, walls don't always come down", {"emotional_vs_physical": 4}),
    ("Physically talented — physical chemistry is harder to teach", {"emotional_vs_physical": 2}),
    ("Physically talented — skills matter more than feelings", {"emotional_vs_physical": 1})
]))

q("vulnerability_in_sex", "temporal", "Your willingness to be sexually vulnerable has been shaped by:", opts([
    ("Deliberate practice — I've intentionally pushed my comfort zone, done therapy, and chosen partners who can hold my vulnerability", {"vulnerability_in_sex": 5}),
    ("Good experiences — safe partners taught me it's okay to be open", {"vulnerability_in_sex": 4}),
    ("A mix of good and bad — some partners earned vulnerability, others punished it", {"vulnerability_in_sex": 3}),
    ("Bad experiences — I've learned to protect myself", {"vulnerability_in_sex": 1})
]))

q("aftercare_needs", "forced_choice", "Aftercare for the person who topped/dominated:", opts([
    ("Is just as real and important — 'top drop' is a genuine phenomenon and both parties need care", {"aftercare_needs": 5}),
    ("Is something I'm aware of — the giver needs care too", {"aftercare_needs": 4}),
    ("Hadn't occurred to me — I assumed aftercare was for the receiver", {"aftercare_needs": 2}),
    ("Isn't a thing — the person in charge doesn't need aftercare", {"aftercare_needs": 1})
]))

q("attachment_in_sex", "scenario", "Friends with benefits — ongoing sexual relationship without romantic attachment:", opts([
    ("Is nearly impossible for me — sex creates attachment whether I want it to or not", {"attachment_in_sex": 5}),
    ("Is difficult — feelings tend to develop", {"attachment_in_sex": 4}),
    ("Is achievable with clear boundaries", {"attachment_in_sex": 3}),
    ("Works great — I can keep sex and feelings separate", {"attachment_in_sex": 1})
]))

print(f"Total questions: {len(questions)}")
with open("/Users/user/personal/sb/trueassess/priv/question_bank/intimacy_style.json", "w") as f:
    json.dump(questions, f, indent=2)
print("Written intimacy_style.json")
