import json
with open("/Users/user/personal/sb/trueassess/priv/question_bank/purity_experience.json") as f:
    questions = json.load(f)
uid_counter = len(questions) + 1
def q(dim, qtype, text, options, tier_role="core", trap=False, cg=None, opacity=0.6, cross=None, tags=None):
    global uid_counter
    uid = f"pe_{uid_counter:03d}"
    uid_counter += 1
    questions.append({"uid": uid, "assessment_id": "purity_experience", "dimension": dim, "question_type": qtype, "text": text, "options": options, "cross_scores": cross or [], "anti_gaming": {"opacity": opacity, "social_desirability_trap": trap, "consistency_group": cg or f"{dim}_core", "reversal": False}, "cultural_adaptability": {"universal": True, "adaptations_needed": [], "adaptation_notes": None}, "content_rating": "R", "content_categories": ["sexuality"], "depth_tier": "moderate", "tier_role": tier_role, "tags": tags or ["nsfw", "experience", dim]})
def opts(ts):
    return [{"id": chr(97+i), "text": t, "scores": s} for i, (t, s) in enumerate(ts)]

# More relationship_experience
q("relationship_experience", "behavioral_recall", "Have you been in a non-monogamous relationship (open, poly, swinging)?", opts([
    ("Yes, multiple — I've navigated the complexity of non-monogamy", {"relationship_experience": 5}),
    ("Yes, at least one", {"relationship_experience": 4}),
    ("No but open to it", {"relationship_experience": 3}),
    ("No and not interested", {"relationship_experience": 1})
]))
q("relationship_experience", "scenario", "Have you ever been the 'other person' in an affair or cheating situation?", opts([
    ("Yes — and it taught me complex lessons about boundaries, desire, and ethics", {"relationship_experience": 5}),
    ("Yes, once — complicated feelings", {"relationship_experience": 4}),
    ("No", {"relationship_experience": 2}),
    ("I'd never be part of that", {"relationship_experience": 1})
]))
q("relationship_experience", "forced_choice", "Long-distance relationship experience:", opts([
    ("Extensive — I've maintained deep connection across distance for extended periods", {"relationship_experience": 5}),
    ("Yes — at least one significant LDR", {"relationship_experience": 4}),
    ("Brief periods of distance in otherwise local relationships", {"relationship_experience": 3}),
    ("None", {"relationship_experience": 1})
]))
q("relationship_experience", "behavioral_recall", "Have you been engaged or married?", opts([
    ("Yes, more than once — I've experienced deep committed partnership in multiple forms", {"relationship_experience": 5}),
    ("Yes, once", {"relationship_experience": 4}),
    ("No but I've had relationships of equivalent depth", {"relationship_experience": 3}),
    ("No", {"relationship_experience": 1})
]))
q("relationship_experience", "forced_choice", "Relationship patterns — have you identified your own repeating patterns in relationships?", opts([
    ("Yes — I can articulate my attachment patterns, selection biases, and habitual dynamics. Self-awareness was hard-won", {"relationship_experience": 5}),
    ("Some — I see a few recurring themes", {"relationship_experience": 4}),
    ("Vaguely — I sense patterns but haven't articulated them", {"relationship_experience": 3}),
    ("Not enough experience to identify patterns", {"relationship_experience": 1})
]))
q("relationship_experience", "temporal", "The relationship you learned the most from:", opts([
    ("Was probably the hardest — the ones that challenged me most taught me the most about who I am and what I need", {"relationship_experience": 5}),
    ("Taught me significant lessons", {"relationship_experience": 4}),
    ("Taught me a few things", {"relationship_experience": 3}),
    ("I haven't had a particularly instructive relationship", {"relationship_experience": 1})
]))
q("relationship_experience", "scenario", "Have you supported a partner through a crisis (job loss, health issue, family death, addiction)?", opts([
    ("Yes, multiple times — being present for a partner's worst moments is where relationships are forged", {"relationship_experience": 5}),
    ("Yes, at least once", {"relationship_experience": 4}),
    ("In minor ways", {"relationship_experience": 3}),
    ("No", {"relationship_experience": 1})
]))

# More sexual_experience
q("sexual_experience", "behavioral_recall", "Kink experience (BDSM, role play, power exchange, fetish play):", opts([
    ("Extensive — kink is a well-explored part of my sexuality", {"sexual_experience": 5}),
    ("Moderate — I've tried several kink activities", {"sexual_experience": 4}),
    ("Minimal — light bondage or occasional role play", {"sexual_experience": 3}),
    ("None", {"sexual_experience": 1})
]))
q("sexual_experience", "scenario", "Have you ever made someone else orgasm using only your hands?", opts([
    ("Many times — manual skill is an art I've developed", {"sexual_experience": 5}),
    ("Yes, multiple times", {"sexual_experience": 4}),
    ("Maybe once or twice", {"sexual_experience": 3}),
    ("Not that I know of / never tried", {"sexual_experience": 1})
]))
q("sexual_experience", "forced_choice", "Your understanding of sexual anatomy (your own and others') is:", opts([
    ("Detailed — I know how bodies work, where things are, what different anatomies respond to, and how to adapt to individual differences", {"sexual_experience": 5}),
    ("Good — I know my way around", {"sexual_experience": 4}),
    ("Basic", {"sexual_experience": 3}),
    ("Minimal", {"sexual_experience": 1})
]))
q("sexual_experience", "behavioral_recall", "Have you ever taken a class, workshop, or educational session about sex (tantra, oral sex technique, communication, anatomy)?", opts([
    ("Multiple — I invest in my sexual education", {"sexual_experience": 5}),
    ("At least one", {"sexual_experience": 4}),
    ("No but I've done online research", {"sexual_experience": 3}),
    ("No", {"sexual_experience": 1})
]))
q("sexual_experience", "scenario", "Giving a partner an orgasm through oral sex:", opts([
    ("I'm confident in my technique — I've done it many times and know how to read a body's responses", {"sexual_experience": 5}),
    ("I've done it — reasonably skilled", {"sexual_experience": 4}),
    ("I've tried but I'm uncertain about my skill", {"sexual_experience": 3}),
    ("Haven't tried or haven't succeeded", {"sexual_experience": 1})
]))

# More substance_experience
q("substance_experience", "behavioral_recall", "Have you ever used a substance to enhance a specific experience (MDMA for connection, psychedelics for self-exploration, cannabis for sex)?", opts([
    ("Yes, deliberately and with intention — substance as tool, not just recreation", {"substance_experience": 5}),
    ("Yes — at least once with a specific purpose", {"substance_experience": 4}),
    ("Only recreationally — no intentional enhancement", {"substance_experience": 3}),
    ("No", {"substance_experience": 1})
]))
q("substance_experience", "scenario", "Sobriety — have you ever done a significant period of deliberate sobriety (Dry January, sober year, recovery)?", opts([
    ("Yes — and the contrast between using and not using gave me genuine perspective on my relationship with substances", {"substance_experience": 5}),
    ("Yes, a shorter period — I've taken intentional breaks", {"substance_experience": 4}),
    ("Not deliberately — I just don't use much", {"substance_experience": 3}),
    ("No", {"substance_experience": 1})
]))
q("substance_experience", "forced_choice", "Your knowledge of harm reduction (testing substances, understanding dosage, knowing drug interactions, recognizing overdose):", opts([
    ("Solid — I believe in informed use and have educated myself on safety", {"substance_experience": 5}),
    ("Basic — I know the fundamentals", {"substance_experience": 4}),
    ("Minimal", {"substance_experience": 3}),
    ("None — not relevant to my life", {"substance_experience": 1})
]))

# More social_experience
q("social_experience", "behavioral_recall", "How many different careers, jobs, or professional identities have you had?", opts([
    ("5+ — I've reinvented my professional self multiple times", {"social_experience": 5}),
    ("3-4 — significant career evolution", {"social_experience": 4}),
    ("1-2 — relatively linear career", {"social_experience": 3}),
    ("Just starting or haven't entered the workforce yet", {"social_experience": 1})
]))
q("social_experience", "scenario", "Have you ever been part of a subculture or counter-culture (kink community, art scene, underground music, activist movement)?", opts([
    ("Yes, multiple — subcultures have shaped who I am", {"social_experience": 5}),
    ("Yes, at least one", {"social_experience": 4}),
    ("Peripherally — I was adjacent to one", {"social_experience": 3}),
    ("No — I've been mainstream", {"social_experience": 1})
]))
q("social_experience", "forced_choice", "Have you ever had to 'start over' socially (new city, new school, new career, leaving a community)?", opts([
    ("Multiple times — I know how to build a social network from scratch", {"social_experience": 5}),
    ("At least once — it was challenging but formative", {"social_experience": 4}),
    ("Not really — my social network has been stable", {"social_experience": 3}),
    ("Never", {"social_experience": 1})
]))
q("social_experience", "behavioral_recall", "Have you mentored someone or been mentored?", opts([
    ("Both — I've been on both sides of mentorship and value both", {"social_experience": 5}),
    ("Yes to one", {"social_experience": 4}),
    ("Informally", {"social_experience": 3}),
    ("No", {"social_experience": 1})
]))
q("social_experience", "scenario", "Have you ever stood up for someone being bullied, harassed, or treated unfairly — even at personal cost?", opts([
    ("Yes, multiple times — intervening is a value I live by, even when it's uncomfortable", {"social_experience": 5}),
    ("Yes, at least once", {"social_experience": 4}),
    ("I've wanted to but didn't", {"social_experience": 2}),
    ("No", {"social_experience": 1})
]))
q("social_experience", "forced_choice", "Networking across diversity — how much of your social circle includes people very different from you (age, class, race, education, lifestyle)?", opts([
    ("Very diverse — I deliberately seek out relationships across difference", {"social_experience": 5}),
    ("Fairly diverse — more so than average", {"social_experience": 4}),
    ("Somewhat — a few people outside my demographic", {"social_experience": 3}),
    ("Not very — my circle is mostly people like me", {"social_experience": 1})
]))

# More risk_experience
q("risk_experience", "behavioral_recall", "Have you ever quit something stable (job, relationship, living situation) to pursue something uncertain?", opts([
    ("Multiple times — I've jumped without a net and built wings on the way down", {"risk_experience": 5}),
    ("Yes, at least once — a significant leap", {"risk_experience": 4}),
    ("I've considered it but always chose safety", {"risk_experience": 3}),
    ("Never — stability is more important than possibility", {"risk_experience": 1})
]))
q("risk_experience", "scenario", "Have you ever confronted someone much more powerful than you (boss, authority figure, abuser)?", opts([
    ("Yes — speaking truth to power is terrifying and I've done it", {"risk_experience": 5}),
    ("Yes, at least once", {"risk_experience": 4}),
    ("No — I avoid confrontation with powerful people", {"risk_experience": 2}),
    ("No", {"risk_experience": 1})
]))
q("risk_experience", "forced_choice", "Emotional risks — being the first to say 'I love you,' confessing feelings to a friend, confronting a betrayal:", opts([
    ("I take emotional risks regularly — being the vulnerable one is a risk I've learned to take", {"risk_experience": 5}),
    ("I've taken some significant emotional risks", {"risk_experience": 4}),
    ("Rarely — emotional vulnerability feels too risky", {"risk_experience": 3}),
    ("I protect myself from emotional risk", {"risk_experience": 1})
]))
q("risk_experience", "behavioral_recall", "Have you ever been in a physical fight or physical confrontation?", opts([
    ("Yes — I've been in situations that escalated to physicality", {"risk_experience": 5}),
    ("Once or twice — minor confrontations", {"risk_experience": 4}),
    ("Never — I've always de-escalated or avoided", {"risk_experience": 2}),
    ("I actively avoid any possibility of physical confrontation", {"risk_experience": 1})
]))
q("risk_experience", "scenario", "Have you ever invested (time, money, emotion) in something most people told you was a bad idea — and did it anyway?", opts([
    ("Yes, multiple times — I trust my own judgment even when it contradicts consensus", {"risk_experience": 5}),
    ("Yes, at least once — it was important to me", {"risk_experience": 4}),
    ("I usually listen to others' warnings", {"risk_experience": 3}),
    ("I follow consensus — the crowd is usually right", {"risk_experience": 1})
]))

# More emotional_experience
q("emotional_experience", "behavioral_recall", "Have you been abandoned — genuinely left by someone you depended on?", opts([
    ("Yes — and surviving abandonment taught me I can survive anything", {"emotional_experience": 5}),
    ("Yes — a formative wound", {"emotional_experience": 4}),
    ("Not dramatically — people have left but I wasn't devastated", {"emotional_experience": 3}),
    ("No — my important people have stayed", {"emotional_experience": 1})
]))
q("emotional_experience", "scenario", "Have you ever experienced a spiritual or transcendent experience (with or without substances)?", opts([
    ("Yes, multiple — I've touched something beyond ordinary consciousness and it changed my understanding of reality", {"emotional_experience": 5}),
    ("At least once — a profound experience", {"emotional_experience": 4}),
    ("Maybe — I've had intense moments I'm not sure how to categorize", {"emotional_experience": 3}),
    ("No", {"emotional_experience": 1})
]))
q("emotional_experience", "forced_choice", "Self-knowledge — how well do you know your own patterns, triggers, strengths, and shadows?", opts([
    ("Deeply — I've done sustained self-exploration through therapy, journaling, relationships, and lived experience. I know my dark corners and my light", {"emotional_experience": 5}),
    ("Well — I have good self-awareness though blind spots remain", {"emotional_experience": 4}),
    ("Moderately — I'm learning", {"emotional_experience": 3}),
    ("Not well — I'm still a mystery to myself", {"emotional_experience": 1})
]))
q("emotional_experience", "behavioral_recall", "Have you changed a fundamental belief or value based on experience (not just intellectually, but a deep shift in worldview)?", opts([
    ("Multiple times — I've had my worldview shattered and rebuilt, and I'm more humble and nuanced for it", {"emotional_experience": 5}),
    ("At least once — a perspective-shifting experience", {"emotional_experience": 4}),
    ("Minor shifts", {"emotional_experience": 3}),
    ("My core beliefs have been consistent", {"emotional_experience": 1})
]))
q("emotional_experience", "scenario", "Loneliness — have you experienced deep, sustained loneliness (not just being alone, but feeling fundamentally disconnected)?", opts([
    ("Yes — and sitting with loneliness without running from it taught me more about myself than almost anything else", {"emotional_experience": 5}),
    ("Yes — a difficult period", {"emotional_experience": 4}),
    ("Briefly", {"emotional_experience": 3}),
    ("Not really — I've been fortunate in my connections", {"emotional_experience": 1})
]))

# Cross-cutting / consistency
q("relationship_experience", "forced_choice", "Your overall relationship experience level:", opts([
    ("Rich and deep — I've loved, lost, learned, and grown through many types of partnership", {"relationship_experience": 5}),
    ("Solid — meaningful experience that's taught me a lot", {"relationship_experience": 4}),
    ("Growing — each experience adds to my understanding", {"relationship_experience": 3}),
    ("Early — I'm just beginning to accumulate relationship wisdom", {"relationship_experience": 1})
]), tier_role="consistency_check", cg="re_core")

q("sexual_experience", "forced_choice", "Your overall sexual experience level:", opts([
    ("Extensive — I've explored widely, with many partners, in many contexts, and have deep self-knowledge about my sexuality", {"sexual_experience": 5}),
    ("Solid — experienced and confident in my sexuality", {"sexual_experience": 4}),
    ("Moderate — some experience, still exploring", {"sexual_experience": 3}),
    ("Early — still building foundational experience", {"sexual_experience": 1})
]), tier_role="consistency_check", cg="se_core")

q("substance_experience", "forced_choice", "Your overall substance experience level:", opts([
    ("Broad and informed — I've explored many altered states and have a nuanced, experienced perspective on substances", {"substance_experience": 5}),
    ("Moderate — familiar with the common ones and have clear preferences", {"substance_experience": 4}),
    ("Light — mainly alcohol with maybe some cannabis", {"substance_experience": 3}),
    ("Minimal — substances have not been part of my life experience", {"substance_experience": 1})
]), tier_role="consistency_check", cg="sub_core")

q("social_experience", "forced_choice", "Your overall social experience breadth:", opts([
    ("Wide — I've navigated many worlds, built and rebuilt social networks, and am comfortable in diverse environments", {"social_experience": 5}),
    ("Broad — I've had varied social experiences", {"social_experience": 4}),
    ("Moderate — a few meaningful social contexts", {"social_experience": 3}),
    ("Narrow — I've operated in limited social environments", {"social_experience": 1})
]), tier_role="consistency_check", cg="soc_core")

q("risk_experience", "forced_choice", "Your overall risk experience:", opts([
    ("Extensive — I've taken physical, financial, emotional, and social risks that shaped who I am", {"risk_experience": 5}),
    ("Moderate — I've taken meaningful risks in several domains", {"risk_experience": 4}),
    ("Some — a few notable risks", {"risk_experience": 3}),
    ("Minimal — I've lived cautiously", {"risk_experience": 1})
]), tier_role="consistency_check", cg="risk_core")

q("emotional_experience", "forced_choice", "Your overall emotional experience depth:", opts([
    ("Profound — I've felt the full range of human emotion at extreme intensity and emerged with deep self-knowledge and empathy", {"emotional_experience": 5}),
    ("Deep — I've experienced significant joy and pain", {"emotional_experience": 4}),
    ("Moderate — a normal range of emotional experience", {"emotional_experience": 3}),
    ("Shallow — I haven't experienced extreme emotions or done deep emotional processing", {"emotional_experience": 1})
]), tier_role="consistency_check", cg="emo_core")

# Additional cross-dimensional
q("relationship_experience", "scenario", "Have you ever been in a relationship with significant age gap, cultural difference, or power imbalance? What did it teach you?", opts([
    ("Yes — navigating difference in intimate relationships taught me things I couldn't learn otherwise", {"relationship_experience": 5}),
    ("Yes — it was instructive", {"relationship_experience": 4}),
    ("No — my partners have been similar to me", {"relationship_experience": 3}),
    ("No", {"relationship_experience": 1})
]))

q("sexual_experience", "scenario", "Have you experienced a significant sexual awakening or discovery that changed your understanding of your sexuality?", opts([
    ("Yes, more than once — my sexuality has undergone transformative discoveries", {"sexual_experience": 5}),
    ("Yes — one major discovery (kink, orientation, desire pattern)", {"sexual_experience": 4}),
    ("Gradual — no single moment but steady evolution", {"sexual_experience": 3}),
    ("My sexuality has been relatively consistent", {"sexual_experience": 1})
]))

q("substance_experience", "scenario", "Have you had a substance-assisted insight — a realization during an altered state that remained true and useful afterward?", opts([
    ("Multiple — some of my most important self-knowledge came from altered states", {"substance_experience": 5}),
    ("At least one — a meaningful experience", {"substance_experience": 4}),
    ("Maybe — hard to tell if it was insight or just being high", {"substance_experience": 3}),
    ("No / not applicable", {"substance_experience": 1})
]))

q("social_experience", "scenario", "Have you ever been an outsider — not fitting in with any obvious group — for an extended period?", opts([
    ("Yes — and being an outsider gave me perspective that insiders lack. I've made peace with not belonging", {"social_experience": 5}),
    ("Yes — it was difficult but formative", {"social_experience": 4}),
    ("Briefly — I usually find my people eventually", {"social_experience": 3}),
    ("No — I've generally fit in", {"social_experience": 1})
]))

q("risk_experience", "scenario", "Have you ever bet on yourself when everyone else doubted you — and been right?", opts([
    ("Yes — trusting my own vision against opposition has been validated multiple times", {"risk_experience": 5}),
    ("Yes, at least once — a defining moment", {"risk_experience": 4}),
    ("I tend to defer to others' judgment", {"risk_experience": 3}),
    ("I haven't been in this situation", {"risk_experience": 1})
]))

q("emotional_experience", "scenario", "Have you had a period of your life where everything fell apart at once (relationship, career, health, finances)?", opts([
    ("Yes — total collapse. And rebuilding from nothing taught me that I am more resilient than any circumstance", {"emotional_experience": 5}),
    ("A partial collapse — several things went wrong at once", {"emotional_experience": 4}),
    ("One major area at a time", {"emotional_experience": 3}),
    ("My life has been relatively stable", {"emotional_experience": 1})
]))

q("relationship_experience", "behavioral_recall", "How many different communication styles have you had to learn to accommodate in relationships?", opts([
    ("Many — each partner taught me a new way to communicate, and I'm fluent in several love languages now", {"relationship_experience": 5}),
    ("Several — I've adapted my communication style multiple times", {"relationship_experience": 4}),
    ("One or two", {"relationship_experience": 3}),
    ("I communicate the same way with everyone", {"relationship_experience": 1})
]))

q("sexual_experience", "behavioral_recall", "Have you experienced sex in the context of deep love AND in the context of no love (purely physical)? How do they compare?", opts([
    ("Both, many times — and understanding that both can be valid, good experiences that serve different needs was an important lesson", {"sexual_experience": 5}),
    ("Both — they're genuinely different experiences", {"sexual_experience": 4}),
    ("Mostly one type", {"sexual_experience": 3}),
    ("Only one type", {"sexual_experience": 1})
]))

q("risk_experience", "forced_choice", "Creative risk — have you created something (art, writing, music, project) and put it out into the world for judgment?", opts([
    ("Multiple times — creative vulnerability is its own form of courage and I've practiced it", {"risk_experience": 5}),
    ("At least once — sharing creative work is exposing", {"risk_experience": 4}),
    ("Only privately — I've created but not shared", {"risk_experience": 3}),
    ("No — I'm not the creative type or I don't share", {"risk_experience": 1})
]))

q("emotional_experience", "forced_choice", "Gratitude — genuinely felt, not performed:", opts([
    ("A daily practice — I've cultivated the capacity for deep gratitude because I've experienced enough loss to know what can be taken away", {"emotional_experience": 5}),
    ("Frequent — I regularly feel genuine thankfulness", {"emotional_experience": 4}),
    ("Occasional — when things go well", {"emotional_experience": 3}),
    ("Rare — I struggle with gratitude", {"emotional_experience": 1})
]))

print(f"Total questions: {len(questions)}")
with open("/Users/user/personal/sb/trueassess/priv/question_bank/purity_experience.json", "w") as f:
    json.dump(questions, f, indent=2)
print("Written purity_experience.json")
