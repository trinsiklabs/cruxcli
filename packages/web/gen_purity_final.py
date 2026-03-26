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

# 33 more questions to reach 150

q("relationship_experience", "scenario", "Have you ever maintained a friendship with an ex?", opts([
    ("Yes, multiple — I can love someone, let the romantic part go, and keep the connection. It requires maturity I've developed", {"relationship_experience": 5}),
    ("Yes, at least one — we navigated the transition", {"relationship_experience": 4}),
    ("I've tried but it didn't work", {"relationship_experience": 3}),
    ("No — clean break is the only way", {"relationship_experience": 1})
]))

q("relationship_experience", "forced_choice", "Have you initiated a difficult conversation in a relationship (about sex, needs, boundaries, dissatisfaction) and had it go well?", opts([
    ("Many times — I've developed the skill of bringing up hard topics with care and directness", {"relationship_experience": 5}),
    ("A few times — it's hard but I've gotten better", {"relationship_experience": 4}),
    ("Once or twice", {"relationship_experience": 3}),
    ("I avoid difficult conversations", {"relationship_experience": 1})
]))

q("sexual_experience", "behavioral_recall", "Have you ever had a sexual experience that was genuinely transformative — not just good but life-changing?", opts([
    ("Yes, more than one — sex has been a vehicle for some of my deepest experiences of connection, healing, and self-discovery", {"sexual_experience": 5}),
    ("Yes, once — a standout experience", {"sexual_experience": 4}),
    ("Good experiences but nothing I'd call transformative", {"sexual_experience": 3}),
    ("No", {"sexual_experience": 1})
]))

q("sexual_experience", "scenario", "Have you explored your own body solo — not just masturbation but deliberate self-exploration of what feels good, mapping your responses?", opts([
    ("Extensively — I know my body's responses in detail because I've done the work of exploring solo", {"sexual_experience": 5}),
    ("Yes — I've spent time understanding my own responses", {"sexual_experience": 4}),
    ("Basic masturbation but not deliberate exploration", {"sexual_experience": 3}),
    ("Not really", {"sexual_experience": 1})
]))

q("sexual_experience", "forced_choice", "Have you ever had to navigate a sexual health issue (STI, pregnancy scare, sexual dysfunction, pain during sex)?", opts([
    ("Yes — and handling it maturely taught me about communication, vulnerability, and the reality of having a sexual life", {"sexual_experience": 5}),
    ("Yes, at least once", {"sexual_experience": 4}),
    ("No — I've been fortunate", {"sexual_experience": 3}),
    ("No", {"sexual_experience": 1})
]))

q("substance_experience", "behavioral_recall", "Have you ever been the 'sober one' managing intoxicated friends?", opts([
    ("Many times — I know what it's like to be responsible for others' safety while they're altered", {"substance_experience": 5}),
    ("Several times", {"substance_experience": 4}),
    ("Once or twice", {"substance_experience": 3}),
    ("No", {"substance_experience": 1})
]))

q("substance_experience", "forced_choice", "Your understanding of addiction — from personal experience, observation, or study:", opts([
    ("Deep — I've either struggled with it personally, supported someone through it, or studied it enough to have genuine understanding, not just stereotypes", {"substance_experience": 5}),
    ("Significant — I've seen it up close", {"substance_experience": 4}),
    ("Basic — I understand the concept", {"substance_experience": 3}),
    ("Theoretical — no personal connection to addiction", {"substance_experience": 1})
]))

q("substance_experience", "scenario", "Have you ever declined a substance in a social situation where everyone else was partaking?", opts([
    ("Yes, comfortably — knowing when to say no and being secure in that decision is a skill", {"substance_experience": 5}),
    ("Yes, though it felt awkward", {"substance_experience": 4}),
    ("I usually go along with the group", {"substance_experience": 2}),
    ("Not applicable — I either always or never participate", {"substance_experience": 1})
]))

q("social_experience", "scenario", "Have you navigated a betrayal by a friend (not romantic partner)?", opts([
    ("Yes — friendship betrayals taught me as much about trust and forgiveness as romantic ones", {"social_experience": 5}),
    ("Yes — a painful experience", {"social_experience": 4}),
    ("Minor falling-outs but nothing dramatic", {"social_experience": 3}),
    ("No significant friendship conflicts", {"social_experience": 1})
]))

q("social_experience", "behavioral_recall", "Have you ever been part of a team that achieved something extraordinary?", opts([
    ("Yes — collective achievement is one of the most powerful human experiences I've had", {"social_experience": 5}),
    ("Yes — at least one notable team success", {"social_experience": 4}),
    ("Modest team successes", {"social_experience": 3}),
    ("No — I work alone or in unremarkable teams", {"social_experience": 1})
]))

q("social_experience", "forced_choice", "Your experience with power dynamics in non-sexual contexts (workplace hierarchy, social groups, family dynamics):", opts([
    ("Extensive — I've navigated complex power structures and understand how authority, influence, and social dynamics work", {"social_experience": 5}),
    ("Significant — I've been in various positions of power and subordination", {"social_experience": 4}),
    ("Some — I've experienced normal hierarchies", {"social_experience": 3}),
    ("Limited — I've avoided or been sheltered from power dynamics", {"social_experience": 1})
]))

q("risk_experience", "scenario", "Have you ever taken a reputational risk — done something publicly that could have cost you social standing or professional credibility?", opts([
    ("Yes, deliberately — I've chosen authenticity over safety multiple times", {"risk_experience": 5}),
    ("At least once — it was nerve-wracking", {"risk_experience": 4}),
    ("I've thought about it but always played it safe", {"risk_experience": 3}),
    ("My reputation is too important to risk", {"risk_experience": 1})
]))

q("risk_experience", "forced_choice", "Have you traveled to a country or region that most people would consider dangerous or risky?", opts([
    ("Yes, multiple — I've gone where comfort ends and real experience begins", {"risk_experience": 5}),
    ("At least once — outside the tourist trail", {"risk_experience": 4}),
    ("I travel but stick to safe destinations", {"risk_experience": 3}),
    ("I don't travel to risky places", {"risk_experience": 1})
]))

q("risk_experience", "behavioral_recall", "Have you ever walked away from financial security (inheritance, stable job, guaranteed path) to pursue something meaningful but uncertain?", opts([
    ("Yes — I've traded security for meaning more than once", {"risk_experience": 5}),
    ("Yes, once — a pivotal choice", {"risk_experience": 4}),
    ("I've considered it but chose security", {"risk_experience": 3}),
    ("Security is non-negotiable for me", {"risk_experience": 1})
]))

q("emotional_experience", "scenario", "Have you experienced a 'dark night of the soul' — a period of existential crisis, loss of meaning, or spiritual/psychological dissolution?", opts([
    ("Yes — and what emerged on the other side was a more authentic, grounded version of myself", {"emotional_experience": 5}),
    ("Yes — a period of deep questioning", {"emotional_experience": 4}),
    ("Moments of doubt but nothing sustained", {"emotional_experience": 3}),
    ("No — my sense of meaning has been stable", {"emotional_experience": 1})
]))

q("emotional_experience", "behavioral_recall", "How many significant 'identity crises' have you navigated (questioning who you are, what you want, what you believe)?", opts([
    ("Multiple — each one stripped me to the foundation and I rebuilt stronger", {"emotional_experience": 5}),
    ("One or two major ones", {"emotional_experience": 4}),
    ("Minor questioning", {"emotional_experience": 3}),
    ("I've never questioned my identity significantly", {"emotional_experience": 1})
]))

q("emotional_experience", "forced_choice", "Shame — deep, personal shame (not just embarrassment):", opts([
    ("I've experienced it intensely and done the work to process it — shame is now a signal I investigate, not a state I live in", {"emotional_experience": 5}),
    ("I've felt it and am learning to work with it", {"emotional_experience": 4}),
    ("Occasionally but not intensely", {"emotional_experience": 3}),
    ("I don't experience much shame", {"emotional_experience": 1})
]))

q("relationship_experience", "scenario", "Have you ever chosen to stay in a difficult relationship and worked through the hard parts rather than leaving?", opts([
    ("Yes — and the decision to stay and repair, rather than leave, taught me things about love that leaving can't teach", {"relationship_experience": 5}),
    ("Yes — it was the harder path but the right one", {"relationship_experience": 4}),
    ("I tend to leave when things get hard", {"relationship_experience": 3}),
    ("I haven't been in a relationship difficult enough to test this", {"relationship_experience": 1})
]))

q("sexual_experience", "forced_choice", "Have you experienced desire that surprised you — wanted someone or something you 'shouldn't' want?", opts([
    ("Yes — and allowing myself to have complex, sometimes contradictory desires without shame is a mark of my sexual maturity", {"sexual_experience": 5}),
    ("Yes — it was confusing but ultimately growth-producing", {"sexual_experience": 4}),
    ("Maybe — I've had unexpected attractions", {"sexual_experience": 3}),
    ("My desires have been predictable", {"sexual_experience": 1})
]))

q("substance_experience", "temporal", "If you could relive your substance experiences knowing what you know now:", opts([
    ("I'd make some different choices but I don't regret the exploration — even the painful parts taught me something real", {"substance_experience": 5}),
    ("I'd be somewhat more careful but keep most experiences", {"substance_experience": 4}),
    ("I'd avoid the harmful ones", {"substance_experience": 3}),
    ("I'd avoid substances entirely / I already have", {"substance_experience": 1})
]))

q("social_experience", "scenario", "Have you ever completely changed your social circle — left one group of friends for another?", opts([
    ("Yes, multiple times — I've outgrown communities and had the courage to leave", {"social_experience": 5}),
    ("At least once — a significant social transition", {"social_experience": 4}),
    ("Gradually drifted from people but no dramatic change", {"social_experience": 3}),
    ("My social circle has been stable throughout my life", {"social_experience": 1})
]))

q("risk_experience", "scenario", "Have you ever trusted your gut over expert advice — and been vindicated?", opts([
    ("Yes — intuition backed by experience has proven more reliable than others' opinions in key moments of my life", {"risk_experience": 5}),
    ("At least once — an important trust-your-gut moment", {"risk_experience": 4}),
    ("I usually defer to expert advice", {"risk_experience": 3}),
    ("I always follow expert advice", {"risk_experience": 1})
]))

q("emotional_experience", "scenario", "Have you experienced genuine awe — in nature, in art, in a human connection — that stopped you in your tracks?", opts([
    ("Many times — I cultivate awe as a practice because I've learned that it recalibrates my entire perspective", {"emotional_experience": 5}),
    ("Several times — profound moments of smallness and beauty", {"emotional_experience": 4}),
    ("Once or twice", {"emotional_experience": 3}),
    ("Not really — I'm not easily awed", {"emotional_experience": 1})
]))

# Final cross-dimensional triangulation
q("relationship_experience", "scenario", "Looking at ALL your experience — relationships, sex, substances, social life, risk-taking, emotions — what has it made you?", opts([
    ("Deeply experienced and fundamentally shaped by what I've lived through — I carry my history as wisdom, not just memories", {"relationship_experience": 5, "emotional_experience": 5}),
    ("Experienced and growing — my history informs who I'm becoming", {"relationship_experience": 4, "emotional_experience": 4}),
    ("Building — I'm accumulating meaningful experience", {"relationship_experience": 3, "emotional_experience": 3}),
    ("Early — my story is still in its opening chapters", {"relationship_experience": 2, "emotional_experience": 2})
]), tier_role="triangulation")

q("sexual_experience", "forced_choice", "If you could give your younger self one piece of sexual wisdom from everything you've learned:", opts([
    ("Multiple things — I have hard-won wisdom about desire, boundaries, communication, and self-acceptance that only experience could teach", {"sexual_experience": 5}),
    ("A few key lessons — I know what I wish I'd known earlier", {"sexual_experience": 4}),
    ("One or two things — I'm still learning most of it", {"sexual_experience": 3}),
    ("I don't have enough experience to advise anyone, including my younger self", {"sexual_experience": 1})
]))

q("risk_experience", "temporal", "Your overall life trajectory has been:", opts([
    ("Unconventional — I've taken paths most people wouldn't, and the sum of those risks created a life that's uniquely mine", {"risk_experience": 5}),
    ("Somewhat unconventional — I've diverged from the norm in meaningful ways", {"risk_experience": 4}),
    ("Mostly conventional with a few notable exceptions", {"risk_experience": 3}),
    ("Conventional — I've followed expected paths", {"risk_experience": 1})
]))

q("social_experience", "forced_choice", "People who know you from different contexts (work, family, friends, kink, hobbies) would describe:", opts([
    ("Different aspects of the same authentic person — I'm consistent in character even if context changes my expression", {"social_experience": 5}),
    ("Slightly different versions — I adapt but remain recognizable", {"social_experience": 4}),
    ("Quite different people — I compartmentalize heavily", {"social_experience": 3}),
    ("Similar descriptions — I'm the same everywhere", {"social_experience": 2})
]))

q("substance_experience", "forced_choice", "Overall, substances in your life have been:", opts([
    ("A significant category of experience that taught me about altered states, my own psychology, and the border between use and abuse", {"substance_experience": 5}),
    ("A meaningful part of my experience — some good, some cautionary", {"substance_experience": 4}),
    ("A minor category — present but not significant", {"substance_experience": 3}),
    ("Virtually absent from my life experience", {"substance_experience": 1})
]))

q("emotional_experience", "temporal", "The person you are now vs. the person you were 10 years ago:", opts([
    ("Almost unrecognizable — I've been transformed by experience into someone deeper, wiser, and more compassionate", {"emotional_experience": 5}),
    ("Significantly evolved — growth has been real and visible", {"emotional_experience": 4}),
    ("Somewhat changed — matured in predictable ways", {"emotional_experience": 3}),
    ("Mostly the same — I'm consistent over time", {"emotional_experience": 1})
]))

q("relationship_experience", "behavioral_recall", "Have you ever loved someone you knew was wrong for you — and had to choose between heart and head?", opts([
    ("Yes — and living through that contradiction taught me that love and compatibility are different things, and both matter", {"relationship_experience": 5}),
    ("Yes — a painful but instructive experience", {"relationship_experience": 4}),
    ("Mildly — I've been attracted to wrong people but didn't fall deeply", {"relationship_experience": 3}),
    ("No — my attractions align with my judgment", {"relationship_experience": 1})
]))

q("sexual_experience", "scenario", "Have you experienced sexual healing — using sex, intimacy, or kink to process trauma, build trust, or reclaim your body?", opts([
    ("Yes — sexual healing is real and I've experienced it. Connection and vulnerability in a sexual context can repair what was broken", {"sexual_experience": 5}),
    ("Possibly — I've had sexual experiences that felt healing", {"sexual_experience": 4}),
    ("No — sex and healing are separate domains for me", {"sexual_experience": 3}),
    ("No", {"sexual_experience": 1})
]))

q("risk_experience", "forced_choice", "Looking back at all the risks you've taken, you feel:", opts([
    ("Grateful — even the risks that went badly taught me something essential. I'd rather have lived boldly than safely", {"risk_experience": 5}),
    ("Mostly positive — the wins outweigh the losses", {"risk_experience": 4}),
    ("Mixed — some risks I regret", {"risk_experience": 3}),
    ("Cautious — I wish I'd taken fewer risks", {"risk_experience": 1})
]))

q("emotional_experience", "forced_choice", "If emotional experience were a currency, you'd say you are:", opts([
    ("Wealthy — I've paid in pain and been rewarded with depth, empathy, resilience, and self-knowledge", {"emotional_experience": 5}),
    ("Comfortable — I have meaningful emotional capital", {"emotional_experience": 4}),
    ("Moderate — building my reserves", {"emotional_experience": 3}),
    ("Early — my emotional experience account is still young", {"emotional_experience": 1})
]))

print(f"Total questions: {len(questions)}")
with open("/Users/user/personal/sb/trueassess/priv/question_bank/purity_experience.json", "w") as f:
    json.dump(questions, f, indent=2)
print("Written purity_experience.json")
