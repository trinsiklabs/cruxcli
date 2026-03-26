import json
questions = []
uid_counter = 1
def q(dim, qtype, text, options, tier_role="core", trap=False, cg=None, opacity=0.6, cross=None, tags=None):
    global uid_counter
    uid = f"pe_{uid_counter:03d}"
    uid_counter += 1
    questions.append({"uid": uid, "assessment_id": "purity_experience", "dimension": dim, "question_type": qtype, "text": text, "options": options, "cross_scores": cross or [], "anti_gaming": {"opacity": opacity, "social_desirability_trap": trap, "consistency_group": cg or f"{dim}_core", "reversal": False}, "cultural_adaptability": {"universal": True, "adaptations_needed": [], "adaptation_notes": None}, "content_rating": "R", "content_categories": ["sexuality"], "depth_tier": "moderate", "tier_role": tier_role, "tags": tags or ["nsfw", "experience", dim]})
def opts(ts):
    return [{"id": chr(97+i), "text": t, "scores": s} for i, (t, s) in enumerate(ts)]

# RELATIONSHIP EXPERIENCE (25)
dim = "relationship_experience"
q(dim, "behavioral_recall", "How many serious romantic relationships (lasting 6+ months) have you been in?", opts([
    ("5+ — I've had a rich relationship history", {"relationship_experience": 5}),
    ("3-4", {"relationship_experience": 4}),
    ("1-2", {"relationship_experience": 3}),
    ("None", {"relationship_experience": 1})
]), cg="re_count")
q(dim, "temporal", "How old were you when you had your first serious relationship?", opts([
    ("Teens — I started dating early", {"relationship_experience": 4}),
    ("Late teens to early twenties", {"relationship_experience": 4}),
    ("Mid to late twenties", {"relationship_experience": 3}),
    ("30+ or haven't yet", {"relationship_experience": 1})
]), cg="re_temporal")
q(dim, "behavioral_recall", "Have you ever cohabited with a romantic partner?", opts([
    ("Yes, with multiple partners — I know what daily domestic partnership looks like", {"relationship_experience": 5}),
    ("Yes, with one partner", {"relationship_experience": 4}),
    ("No, but I've spent extended periods living together informally", {"relationship_experience": 3}),
    ("No", {"relationship_experience": 1})
]))
q(dim, "scenario", "A new partner asks about your relationship history. Your honest summary:", opts([
    ("Rich and varied — I've loved deeply, been hurt, grown, and have stories that taught me who I am", {"relationship_experience": 5}),
    ("A few meaningful relationships that shaped me", {"relationship_experience": 4}),
    ("Limited but significant", {"relationship_experience": 3}),
    ("Minimal — I'm early in my relationship journey", {"relationship_experience": 1})
]))
q(dim, "forced_choice", "You've experienced:", opts([
    ("Multiple relationship structures (monogamous, open, polyamorous, long-distance, D/s) and learned from each", {"relationship_experience": 5}),
    ("Two or three different relationship types", {"relationship_experience": 4}),
    ("One relationship structure", {"relationship_experience": 3}),
    ("No relationship experience to speak of", {"relationship_experience": 1})
]))
q(dim, "behavioral_recall", "Have you been through a breakup or divorce that fundamentally changed you?", opts([
    ("Yes, more than one — heartbreak has been one of my greatest teachers", {"relationship_experience": 5}),
    ("Yes, one significant one", {"relationship_experience": 4}),
    ("I've had breakups but none that transformed me", {"relationship_experience": 3}),
    ("No major breakups / no relationship experience", {"relationship_experience": 1})
]))
q(dim, "temporal", "How has your approach to relationships evolved over your lifetime?", opts([
    ("Dramatically — I've gone from naive to deeply self-aware about what I need, what I offer, and what doesn't work", {"relationship_experience": 5}),
    ("Significantly — each relationship taught me something", {"relationship_experience": 4}),
    ("Somewhat — I've learned a few things", {"relationship_experience": 3}),
    ("Not much — I'm still figuring it out", {"relationship_experience": 1})
]))
q(dim, "scenario", "The longest relationship you've been in:", opts([
    ("5+ years — I know what long-term partnership looks and feels like", {"relationship_experience": 5}),
    ("2-5 years", {"relationship_experience": 4}),
    ("6 months to 2 years", {"relationship_experience": 3}),
    ("Less than 6 months / none", {"relationship_experience": 1})
]))
q(dim, "forced_choice", "Relationship skills you've developed through experience:", opts([
    ("Conflict resolution, emotional regulation, vulnerability, communication about needs, healthy boundaries, repair after rupture", {"relationship_experience": 5}),
    ("Several key skills — communication and conflict handling", {"relationship_experience": 4}),
    ("Some — I'm getting better", {"relationship_experience": 3}),
    ("Still developing the basics", {"relationship_experience": 1})
]))
q(dim, "behavioral_recall", "Have you ever been in a relationship where you were the one who ended it because you outgrew the dynamic?", opts([
    ("Yes — recognizing incompatibility even when love remains is a painful but important skill I've used", {"relationship_experience": 5}),
    ("Yes, once", {"relationship_experience": 4}),
    ("No — my breakups were initiated by the other person", {"relationship_experience": 3}),
    ("No relationship experience", {"relationship_experience": 1})
]))

# SEXUAL EXPERIENCE (25)
dim = "sexual_experience"
q(dim, "behavioral_recall", "Total number of sexual partners in your lifetime:", opts([
    ("20+ — extensive sexual experience across many partners", {"sexual_experience": 5}),
    ("10-19", {"sexual_experience": 4}),
    ("3-9", {"sexual_experience": 3}),
    ("0-2", {"sexual_experience": 1})
]), cg="se_count")
q(dim, "temporal", "Age at first sexual experience:", opts([
    ("Early teens — earlier than most peers", {"sexual_experience": 4}),
    ("Mid to late teens — typical timing", {"sexual_experience": 3}),
    ("Early twenties", {"sexual_experience": 3}),
    ("Late twenties or later", {"sexual_experience": 1})
]), cg="se_temporal")
q(dim, "behavioral_recall", "Types of sexual encounters you've had (check what applies conceptually): one-night stands, friends with benefits, relationship sex, group sex, casual sex, long-term partnered sex:", opts([
    ("5-6 of these — I've experienced sex in many different contexts", {"sexual_experience": 5}),
    ("3-4 — a good range", {"sexual_experience": 4}),
    ("1-2 types", {"sexual_experience": 3}),
    ("Only one or none", {"sexual_experience": 1})
]))
q(dim, "scenario", "Your sexual repertoire — the range of acts, positions, and activities you're comfortable and experienced with:", opts([
    ("Extensive — I've explored widely and can navigate almost any sexual situation with confidence", {"sexual_experience": 5}),
    ("Solid — I'm experienced in the main categories and some specialties", {"sexual_experience": 4}),
    ("Moderate — I know what I like and stick to it", {"sexual_experience": 3}),
    ("Limited — I've done the basics", {"sexual_experience": 1})
]))
q(dim, "forced_choice", "Oral sex (giving and receiving) — your experience level:", opts([
    ("Very experienced — I've given and received extensively and consider it a skill I've developed", {"sexual_experience": 5}),
    ("Experienced — comfortable and practiced", {"sexual_experience": 4}),
    ("Some experience", {"sexual_experience": 3}),
    ("Minimal or none", {"sexual_experience": 1})
]))
q(dim, "behavioral_recall", "Anal sex — your experience:", opts([
    ("Experienced — I've explored this thoroughly and know my body's responses well", {"sexual_experience": 5}),
    ("Some experience — I've tried it several times", {"sexual_experience": 4}),
    ("Once or twice", {"sexual_experience": 3}),
    ("Never", {"sexual_experience": 1})
]))
q(dim, "scenario", "Sex in unusual locations (outdoors, cars, public adjacent, someone else's home, office):", opts([
    ("Multiple locations — I've had sex in many places beyond the bedroom", {"sexual_experience": 5}),
    ("A few — I've branched out from the bed", {"sexual_experience": 4}),
    ("Once or twice outside standard settings", {"sexual_experience": 3}),
    ("Bedroom only", {"sexual_experience": 1})
]))
q(dim, "forced_choice", "Have you had sex with someone of a different gender than your primary orientation?", opts([
    ("Yes — I've explored across gender lines and learned from it", {"sexual_experience": 5}),
    ("Yes, at least once", {"sexual_experience": 4}),
    ("No, but I'm open to it", {"sexual_experience": 3}),
    ("No, and I'm not interested", {"sexual_experience": 2})
]))
q(dim, "behavioral_recall", "Group sex, threesomes, or multi-partner sexual experiences:", opts([
    ("Multiple experiences — I'm comfortable navigating multi-partner dynamics", {"sexual_experience": 5}),
    ("At least one — I've tried it", {"sexual_experience": 4}),
    ("No but interested", {"sexual_experience": 3}),
    ("No and not interested", {"sexual_experience": 1})
]))
q(dim, "temporal", "How has your sexual confidence and skill evolved?", opts([
    ("Enormously — I went from uncertain to self-assured through extensive practice and communication", {"sexual_experience": 5}),
    ("Significantly — I'm much more confident than early on", {"sexual_experience": 4}),
    ("Somewhat — I've gotten better", {"sexual_experience": 3}),
    ("Still developing basic confidence", {"sexual_experience": 1})
]))
q(dim, "scenario", "Sexting, phone sex, or video sex:", opts([
    ("Extensive experience — I'm fluent in digital sexual expression", {"sexual_experience": 5}),
    ("Moderate — I've done it several times", {"sexual_experience": 4}),
    ("Once or twice", {"sexual_experience": 3}),
    ("Never", {"sexual_experience": 1})
]))
q(dim, "behavioral_recall", "Sex toy experience (vibrators, dildos, plugs, prostate toys, cock rings, etc.):", opts([
    ("Extensive collection and regular use — I know what works for my body and have invested in tools", {"sexual_experience": 5}),
    ("Several toys — I incorporate them regularly", {"sexual_experience": 4}),
    ("One or two basics", {"sexual_experience": 3}),
    ("None", {"sexual_experience": 1})
]))
q(dim, "forced_choice", "Have you ever been tested for STIs?", opts([
    ("Multiple times — I test regularly as part of responsible sexual health", {"sexual_experience": 5}),
    ("Yes, a few times", {"sexual_experience": 4}),
    ("Once", {"sexual_experience": 3}),
    ("Never", {"sexual_experience": 1})
]))
q(dim, "scenario", "Have you ever had a sexual experience that was purely about exploration — trying something just to see what it was like, with no expectation it would become a regular thing?", opts([
    ("Many times — exploratory sex is how I've built my sexual self-knowledge", {"sexual_experience": 5}),
    ("Several times", {"sexual_experience": 4}),
    ("Once or twice", {"sexual_experience": 3}),
    ("No — every sexual experience has been within a familiar framework", {"sexual_experience": 1})
]))
q(dim, "behavioral_recall", "Have you attended a sex-positive event, play party, swingers club, or similar adult venue?", opts([
    ("Multiple times — I'm comfortable in sexually charged social environments", {"sexual_experience": 5}),
    ("At least once", {"sexual_experience": 4}),
    ("No but I've considered it", {"sexual_experience": 3}),
    ("No", {"sexual_experience": 1})
]))

# SUBSTANCE EXPERIENCE (25)
dim = "substance_experience"
q(dim, "behavioral_recall", "Alcohol: your experience level:", opts([
    ("Extensive — I've explored many types of alcohol, been drunk many times, know my limits well", {"substance_experience": 5}),
    ("Moderate — I drink socially and have been drunk a fair number of times", {"substance_experience": 4}),
    ("Light — I drink occasionally", {"substance_experience": 3}),
    ("None or minimal — I rarely or never drink", {"substance_experience": 1})
]), cg="sub_alcohol")
q(dim, "behavioral_recall", "Cannabis: your experience:", opts([
    ("Regular or extensive past use — I know the landscape of strains, effects, and my personal relationship with it", {"substance_experience": 5}),
    ("Moderate — I've used it many times", {"substance_experience": 4}),
    ("A few times", {"substance_experience": 3}),
    ("Never", {"substance_experience": 1})
]))
q(dim, "behavioral_recall", "Psychedelics (mushrooms, LSD, MDMA, ayahuasca, etc.): your experience:", opts([
    ("Multiple experiences with multiple substances — psychedelics have been part of my personal development", {"substance_experience": 5}),
    ("A few experiences — at least one meaningful psychedelic journey", {"substance_experience": 4}),
    ("Once", {"substance_experience": 3}),
    ("Never", {"substance_experience": 1})
]))
q(dim, "forced_choice", "Your overall substance exploration:", opts([
    ("Broad — I've tried many categories (stimulants, depressants, psychedelics, empathogens) and have a nuanced understanding of altered states", {"substance_experience": 5}),
    ("Moderate — alcohol, cannabis, and maybe one or two others", {"substance_experience": 4}),
    ("Limited to alcohol and possibly cannabis", {"substance_experience": 3}),
    ("Minimal to none", {"substance_experience": 1})
]))
q(dim, "temporal", "Your relationship with substances has:", opts([
    ("Evolved — I've gone through phases of more and less use, learned my limits, possibly struggled and recovered", {"substance_experience": 5}),
    ("Matured — I'm more intentional now than when younger", {"substance_experience": 4}),
    ("Stayed relatively consistent", {"substance_experience": 3}),
    ("Never been significant", {"substance_experience": 1})
]), cg="sub_temporal")
q(dim, "behavioral_recall", "Have you ever used substances in combination (cross-fading, candyflipping, etc.)?", opts([
    ("Yes, multiple combinations — I understand how substances interact", {"substance_experience": 5}),
    ("Yes, at least once (e.g., drinking while high)", {"substance_experience": 4}),
    ("No", {"substance_experience": 2}),
    ("I don't use substances", {"substance_experience": 1})
]))
q(dim, "scenario", "The most altered state of consciousness you've experienced (from any substance):", opts([
    ("Profound — ego dissolution, mystical experience, or reality-altering perception shift", {"substance_experience": 5}),
    ("Significant — very drunk, very high, or a strong psychedelic experience", {"substance_experience": 4}),
    ("Moderate — tipsy or mildly high", {"substance_experience": 3}),
    ("Minimal or none", {"substance_experience": 1})
]))
q(dim, "behavioral_recall", "Have you ever had a negative substance experience (bad trip, alcohol poisoning, addiction scare)?", opts([
    ("Yes — and I learned from it about my limits and relationship with substances", {"substance_experience": 5}),
    ("Yes — a scary experience that changed my approach", {"substance_experience": 4}),
    ("No — my substance use has been uneventful", {"substance_experience": 3}),
    ("N/A — minimal or no use", {"substance_experience": 1})
]))
q(dim, "forced_choice", "Substance use during sex:", opts([
    ("I've combined substances with sex deliberately and understand how different substances affect the sexual experience", {"substance_experience": 5}),
    ("I've had sex while intoxicated multiple times", {"substance_experience": 4}),
    ("Once or twice while drinking", {"substance_experience": 3}),
    ("Never — I keep substances and sex separate", {"substance_experience": 1})
]))
q(dim, "temporal", "Have you ever gone through a period of problematic substance use and come out the other side?", opts([
    ("Yes — and the experience gave me deep understanding of my own patterns and limits", {"substance_experience": 5}),
    ("Possibly — there were times I used more than I should have", {"substance_experience": 4}),
    ("No — my use has always been controlled", {"substance_experience": 3}),
    ("N/A", {"substance_experience": 1})
]))

# SOCIAL EXPERIENCE (25)
dim = "social_experience"
q(dim, "behavioral_recall", "How many close friendships (people you'd call at 3 AM) have you maintained simultaneously?", opts([
    ("5+ — I have a rich, deep social network", {"social_experience": 5}),
    ("3-4 — a solid inner circle", {"social_experience": 4}),
    ("1-2 — one or two very close people", {"social_experience": 3}),
    ("None currently", {"social_experience": 1})
]))
q(dim, "scenario", "Public speaking, performing, or being the center of attention:", opts([
    ("Comfortable — I've done it many times in various contexts", {"social_experience": 5}),
    ("I can do it — nervous but capable", {"social_experience": 4}),
    ("Very difficult for me", {"social_experience": 2}),
    ("I avoid it at all costs", {"social_experience": 1})
]))
q(dim, "behavioral_recall", "Countries or cultures you've experienced firsthand (travel, living abroad):", opts([
    ("10+ countries or extensive multicultural experience — I've been deeply shaped by exposure to different ways of living", {"social_experience": 5}),
    ("5-10 countries — meaningful travel experience", {"social_experience": 4}),
    ("2-4 countries", {"social_experience": 3}),
    ("Just my home country", {"social_experience": 1})
]))
q(dim, "forced_choice", "Your social range — can you navigate very different social environments (board rooms, dive bars, art openings, kink events, religious gatherings)?", opts([
    ("Fluently — I'm a social chameleon who's comfortable in almost any environment", {"social_experience": 5}),
    ("Mostly — I handle most social situations well", {"social_experience": 4}),
    ("In familiar environments — I struggle outside my comfort zone", {"social_experience": 3}),
    ("Limited — I'm comfortable in very few social settings", {"social_experience": 1})
]))
q(dim, "behavioral_recall", "Have you led a team, organized an event, or been responsible for a group of people?", opts([
    ("Multiple times in various contexts — leadership is familiar to me", {"social_experience": 5}),
    ("Yes, at least once in a significant way", {"social_experience": 4}),
    ("In minor ways", {"social_experience": 3}),
    ("No", {"social_experience": 1})
]))
q(dim, "scenario", "Navigating a conflict between two friends:", opts([
    ("Something I've done multiple times — I'm comfortable as a mediator and have social skills for difficult conversations", {"social_experience": 5}),
    ("I've managed it at least once", {"social_experience": 4}),
    ("I'd avoid getting involved", {"social_experience": 2}),
    ("I've never been in this position", {"social_experience": 1})
]))
q(dim, "temporal", "How many different social circles or communities have you been part of over your life?", opts([
    ("Many — I've moved through different worlds (professional, creative, spiritual, kink, academic, etc.)", {"social_experience": 5}),
    ("Several distinct groups", {"social_experience": 4}),
    ("A few", {"social_experience": 3}),
    ("One or two", {"social_experience": 1})
]))
q(dim, "behavioral_recall", "Have you ever lived alone for an extended period?", opts([
    ("Yes, and it was deeply formative — I know myself in solitude as well as in company", {"social_experience": 5}),
    ("Yes", {"social_experience": 4}),
    ("Briefly", {"social_experience": 3}),
    ("Never — always had family, roommates, or partners", {"social_experience": 1})
]))
q(dim, "forced_choice", "Networking, small talk, and social lubrication:", opts([
    ("Skills I've developed — I can connect with strangers and build rapport efficiently", {"social_experience": 5}),
    ("I'm decent — social situations don't paralyze me", {"social_experience": 4}),
    ("Difficult but improving", {"social_experience": 3}),
    ("My weakest area — I hate small talk and avoid networking", {"social_experience": 1})
]))
q(dim, "behavioral_recall", "Have you supported someone through a major crisis (death, illness, job loss, mental health emergency)?", opts([
    ("Multiple times — I'm often the person people turn to in crisis", {"social_experience": 5}),
    ("Yes, at least once — it was intense and formative", {"social_experience": 4}),
    ("In minor ways", {"social_experience": 3}),
    ("No", {"social_experience": 1})
]))

# RISK EXPERIENCE (25)
dim = "risk_experience"
q(dim, "behavioral_recall", "Have you ever done something physically dangerous on purpose (extreme sports, high-risk activities, dangerous travel)?", opts([
    ("Multiple times — I seek out adrenaline and have a varied history of physical risk-taking", {"risk_experience": 5}),
    ("A few notable times", {"risk_experience": 4}),
    ("Once or twice — minor risk-taking", {"risk_experience": 3}),
    ("Never — I avoid physical risk", {"risk_experience": 1})
]))
q(dim, "scenario", "Breaking rules — have you ever deliberately broken a law, rule, or social norm?", opts([
    ("Many times and in many ways — from minor to significant. Rules are guidelines I evaluate, not absolutes I follow", {"risk_experience": 5}),
    ("Several times — I've pushed boundaries when it seemed worth it", {"risk_experience": 4}),
    ("Occasionally — minor infractions", {"risk_experience": 3}),
    ("Rarely or never — I follow rules", {"risk_experience": 1})
]))
q(dim, "behavioral_recall", "Financial risks you've taken (investments, starting a business, quitting a job without another lined up, large purchases):", opts([
    ("Multiple significant financial risks — some paid off, some didn't, all taught me something", {"risk_experience": 5}),
    ("A few notable ones", {"risk_experience": 4}),
    ("Minor risks only", {"risk_experience": 3}),
    ("I avoid financial risk", {"risk_experience": 1})
]))
q(dim, "forced_choice", "Your relationship with risk in general:", opts([
    ("Comfortable and calculated — I assess risk deliberately and accept it when the reward justifies it", {"risk_experience": 5}),
    ("Moderate — I take some risks when they feel worth it", {"risk_experience": 4}),
    ("Cautious — I prefer known outcomes", {"risk_experience": 3}),
    ("Risk-averse — I minimize risk wherever possible", {"risk_experience": 1})
]))
q(dim, "behavioral_recall", "Have you ever moved to a new city knowing no one?", opts([
    ("Yes, more than once — starting fresh in unknown places is something I've done and learned from", {"risk_experience": 5}),
    ("Once — a major life event", {"risk_experience": 4}),
    ("No but I've considered it", {"risk_experience": 3}),
    ("No — I stay where my roots are", {"risk_experience": 1})
]))
q(dim, "scenario", "The biggest risk you've ever taken:", opts([
    ("Was genuinely life-altering — it could have gone very wrong and required real courage", {"risk_experience": 5}),
    ("Was significant — a meaningful gamble", {"risk_experience": 4}),
    ("Was moderate — risky but recoverable", {"risk_experience": 3}),
    ("I can't identify a notably risky decision", {"risk_experience": 1})
]))
q(dim, "temporal", "How has your appetite for risk changed over time?", opts([
    ("I've become more calibrated — I take smarter risks now, not fewer. Experience taught me which risks are worth taking", {"risk_experience": 5}),
    ("Somewhat decreased — I'm more careful but still take risks", {"risk_experience": 4}),
    ("Significantly decreased — I was wilder when young", {"risk_experience": 3}),
    ("Always been risk-averse", {"risk_experience": 1})
]))
q(dim, "behavioral_recall", "Have you ever done something sexually risky (unprotected sex, public sex, sex with someone inappropriate, infidelity)?", opts([
    ("More than a few times — and I've learned about my own risk tolerance from each", {"risk_experience": 5}),
    ("A few times — some I regret, some I don't", {"risk_experience": 4}),
    ("Once or twice", {"risk_experience": 3}),
    ("Never — I'm careful in sexual contexts", {"risk_experience": 1})
]))
q(dim, "forced_choice", "Have you ever had a 'close call' — a situation where things almost went very wrong?", opts([
    ("Multiple — and surviving close calls has given me both resilience and respect for risk", {"risk_experience": 5}),
    ("At least one memorable one", {"risk_experience": 4}),
    ("Nothing that dramatic", {"risk_experience": 3}),
    ("I've lived a careful life", {"risk_experience": 1})
]))
q(dim, "behavioral_recall", "Have you ever been arrested, detained, or had a serious confrontation with authority?", opts([
    ("Yes — and the experience taught me things about systems, power, and myself", {"risk_experience": 5}),
    ("A minor brush — nothing serious", {"risk_experience": 4}),
    ("No", {"risk_experience": 2}),
    ("I go out of my way to avoid any authority confrontation", {"risk_experience": 1})
]))

# EMOTIONAL EXPERIENCE (25)
dim = "emotional_experience"
q(dim, "behavioral_recall", "Have you experienced the death of someone close to you?", opts([
    ("Multiple significant losses — grief has been a profound teacher", {"emotional_experience": 5}),
    ("One or two — it changed me", {"emotional_experience": 4}),
    ("Extended family or acquaintances", {"emotional_experience": 3}),
    ("No significant losses", {"emotional_experience": 1})
]))
q(dim, "forced_choice", "Your emotional range — how many different emotional states can you name and describe that you've personally experienced?", opts([
    ("Extensive — I have a sophisticated emotional vocabulary because I've felt deeply across the full spectrum", {"emotional_experience": 5}),
    ("Broad — I've experienced most major emotions intensely", {"emotional_experience": 4}),
    ("Moderate — I've felt the basics strongly", {"emotional_experience": 3}),
    ("Limited — I don't experience intense emotions often", {"emotional_experience": 1})
]))
q(dim, "behavioral_recall", "Have you been through a mental health crisis (depression, anxiety disorder, panic attacks, suicidal ideation)?", opts([
    ("Yes — and coming through it gave me depth, empathy, and self-knowledge I couldn't have gained any other way", {"emotional_experience": 5}),
    ("Yes — it was a difficult period", {"emotional_experience": 4}),
    ("Mild struggles — nothing clinical", {"emotional_experience": 3}),
    ("No significant mental health challenges", {"emotional_experience": 1})
]))
q(dim, "scenario", "Have you ever been so in love it felt like you'd die if they left?", opts([
    ("Yes — and I survived, and the capacity to love that intensely is something I value about myself", {"emotional_experience": 5}),
    ("Yes — overwhelming love is part of my history", {"emotional_experience": 4}),
    ("Strong feelings but not that level of intensity", {"emotional_experience": 3}),
    ("No — I've never been consumed by love", {"emotional_experience": 1})
]))
q(dim, "temporal", "How has your emotional maturity evolved?", opts([
    ("Profoundly — I went from reactive to reflective, from avoiding feelings to sitting with them, through deliberate work and hard experience", {"emotional_experience": 5}),
    ("Significantly — I handle emotions much better now", {"emotional_experience": 4}),
    ("Somewhat — still growing", {"emotional_experience": 3}),
    ("I'm still pretty reactive", {"emotional_experience": 1})
]))
q(dim, "behavioral_recall", "Have you done therapy or counseling?", opts([
    ("Extensively — therapy has been transformative and I've done multiple types (talk, CBT, EMDR, somatic, etc.)", {"emotional_experience": 5}),
    ("Yes, for a meaningful period", {"emotional_experience": 4}),
    ("Briefly", {"emotional_experience": 3}),
    ("No", {"emotional_experience": 1})
]))
q(dim, "forced_choice", "Have you ever experienced betrayal — a deep breach of trust by someone you loved?", opts([
    ("Yes — and processing it is one of the hardest, most character-building experiences I've had", {"emotional_experience": 5}),
    ("Yes — it's left lasting marks", {"emotional_experience": 4}),
    ("Minor betrayals — nothing devastating", {"emotional_experience": 3}),
    ("No — I've been fortunate in who I've trusted", {"emotional_experience": 1})
]))
q(dim, "behavioral_recall", "Have you ever forgiven someone for something you thought was unforgivable?", opts([
    ("Yes — and the process of forgiveness taught me more about myself than the original wound did", {"emotional_experience": 5}),
    ("Yes, with difficulty", {"emotional_experience": 4}),
    ("I've forgiven small things", {"emotional_experience": 3}),
    ("No — some things are unforgivable", {"emotional_experience": 1})
]))
q(dim, "scenario", "The deepest emotional pain you've experienced:", opts([
    ("Was soul-crushing and I thought I might not survive — but I did, and I'm more resilient and empathetic because of it", {"emotional_experience": 5}),
    ("Was very intense — a formative period of suffering", {"emotional_experience": 4}),
    ("Was significant but manageable", {"emotional_experience": 3}),
    ("I've been relatively sheltered from deep emotional pain", {"emotional_experience": 1})
]))
q(dim, "temporal", "Have you cared for someone who was ill, dying, or struggling with addiction?", opts([
    ("Yes — caregiving has been one of the most challenging and deepening experiences of my life", {"emotional_experience": 5}),
    ("Yes, to some extent", {"emotional_experience": 4}),
    ("Peripherally — I've supported someone going through it but wasn't the primary caregiver", {"emotional_experience": 3}),
    ("No", {"emotional_experience": 1})
]))
q(dim, "forced_choice", "Joy — have you experienced moments of pure, transcendent joy?", opts([
    ("Yes, many — joy is as much part of my emotional repertoire as pain. I've felt it intensely enough to know it's real", {"emotional_experience": 5}),
    ("Yes, a few — peak moments I remember clearly", {"emotional_experience": 4}),
    ("Contentment, sure — but transcendent joy seems like an exaggeration", {"emotional_experience": 3}),
    ("Rarely — I'm not sure I've felt what you're describing", {"emotional_experience": 1})
]))
q(dim, "behavioral_recall", "Have you ever written about your emotions in a sustained way (journaling, poetry, letters, blogs)?", opts([
    ("Extensively — writing has been a primary tool for processing my emotional life", {"emotional_experience": 5}),
    ("Yes — periodic journaling or writing", {"emotional_experience": 4}),
    ("Occasionally", {"emotional_experience": 3}),
    ("No — I don't process emotions through writing", {"emotional_experience": 1})
]))
q(dim, "scenario", "Empathy — can you feel what other people are feeling, even when they haven't told you?", opts([
    ("Intensely — I'm highly empathic, sometimes to my own detriment. Other people's emotions register in my body", {"emotional_experience": 5}),
    ("Fairly strongly — I pick up on emotional states", {"emotional_experience": 4}),
    ("Sometimes — when it's obvious", {"emotional_experience": 3}),
    ("Not really — I need people to tell me how they feel", {"emotional_experience": 1})
]))
q(dim, "forced_choice", "Emotional resilience — your ability to recover from setbacks:", opts([
    ("Battle-tested — I've been knocked down hard and gotten back up enough times to know I can survive almost anything", {"emotional_experience": 5}),
    ("Strong — I recover from most things", {"emotional_experience": 4}),
    ("Moderate — some things take me a long time to recover from", {"emotional_experience": 3}),
    ("Low — I struggle with recovery", {"emotional_experience": 1})
]))
q(dim, "behavioral_recall", "Have you experienced a major life transition that required rebuilding your identity (career change, divorce, coming out, leaving a religion, immigration)?", opts([
    ("Multiple — reinventing myself has been a recurring theme", {"emotional_experience": 5}),
    ("One major reinvention", {"emotional_experience": 4}),
    ("Minor transitions", {"emotional_experience": 3}),
    ("My identity has been relatively stable", {"emotional_experience": 1})
]))

print(f"Total questions: {len(questions)}")
with open("/Users/user/personal/sb/trueassess/priv/question_bank/purity_experience.json", "w") as f:
    json.dump(questions, f, indent=2)
print("Written purity_experience.json")
