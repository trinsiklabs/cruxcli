import json
import random

random.seed(42)

assessment_id = "conflict_resolution"
dimensions = ["competing", "collaborating", "compromising", "avoiding", "accommodating"]

# 120 questions total, 24 per dimension
# Distribution: ~30% scenario (36), ~15% somatic (18), ~15% partner_perspective (18), ~15% temporal (18), ~15% behavioral_recall (18), ~10% forced_choice (12)
# Tier: ~8% core (10), ~40% triangulation (48), ~27% trap (32), ~25% consistency_check (30)

questions = []
uid_counter = 0

def make_uid():
    global uid_counter
    uid_counter += 1
    return f"cr_{uid_counter:03d}"

def make_q(dim, qtype, text, options, tier_role, trap, cgroup, opacity, cross_scores=None, tags=None, depth="moderate", reversal=False, adaptations=None):
    q = {
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
    return q

def opts(scores_list):
    """scores_list: list of (text, {dim: score}) tuples"""
    letters = "abcde"
    return [{"id": letters[i], "text": t, "scores": s} for i, (t, s) in enumerate(scores_list)]

# ============================================================
# COMPETING (24 questions)
# ============================================================

questions.append(make_q("competing", "scenario",
    "Your team is debating which vendor to choose. You've done extensive research and are confident in your pick. A colleague pushes hard for a different option with what you consider weaker reasoning. What do you do?",
    opts([
        ("Present your data forcefully and make the case that their analysis is incomplete", {"competing": 5, "collaborating": 1}),
        ("Suggest combining elements of both proposals into a hybrid solution", {"compromising": 4, "collaborating": 3}),
        ("Ask to hear their full reasoning before responding, then work through the comparison together", {"collaborating": 5, "competing": 1}),
        ("Let them take the lead since it's not worth the friction", {"accommodating": 4, "avoiding": 2}),
    ]),
    "triangulation", False, "competing_assert_1", 0.7, tags=["conflict_resolution", "competing", "work", "triangulation"]))

questions.append(make_q("competing", "somatic",
    "When someone contradicts your position in a meeting, what happens in your body first?",
    opts([
        ("My jaw tightens and I lean forward—I'm already formulating my rebuttal", {"competing": 5}),
        ("I feel a flutter of anxiety in my chest and want to smooth things over", {"accommodating": 4, "avoiding": 2}),
        ("I notice curiosity—my head tilts and I want to understand their angle", {"collaborating": 4}),
        ("I feel nothing particular—disagreements are just information", {"avoiding": 3, "compromising": 2}),
    ]),
    "triangulation", False, "competing_somatic_1", 0.8, depth="deep"))

questions.append(make_q("competing", "partner_perspective",
    "If your closest friend described how you handle disagreements, which would they most likely say?",
    opts([
        ("'They always have a strong opinion and aren't shy about defending it'", {"competing": 5}),
        ("'They're the peacemaker—they hate when people fight'", {"accommodating": 4, "avoiding": 2}),
        ("'They want everyone's input before deciding anything'", {"collaborating": 4}),
        ("'They pick their battles—some things they'll fight for, most they let go'", {"compromising": 3, "avoiding": 2}),
    ]),
    "consistency_check", False, "competing_partner_1", 0.6))

questions.append(make_q("competing", "temporal",
    "Think back to the last time you 'won' an argument with someone close to you. How did you feel two hours later?",
    opts([
        ("Satisfied—I was right and it was important to establish that", {"competing": 5}),
        ("Slightly guilty—I wonder if I was too aggressive", {"competing": 3, "accommodating": 2}),
        ("Hollow—winning didn't feel as good as I expected", {"collaborating": 3, "avoiding": 2}),
        ("I don't really 'win' arguments—I either find middle ground or drop it", {"compromising": 3, "avoiding": 3}),
    ]),
    "triangulation", False, "competing_temporal_1", 0.7, depth="deep"))

questions.append(make_q("competing", "behavioral_recall",
    "In the past month, how many times have you interrupted someone mid-sentence during a disagreement?",
    opts([
        ("Multiple times—when I see a flaw in their logic I can't wait", {"competing": 5}),
        ("Once or twice, and I caught myself and apologized", {"competing": 3, "collaborating": 2}),
        ("I don't think I have—I tend to wait them out", {"avoiding": 3, "accommodating": 2}),
        ("I can't recall specific instances but I know it happens sometimes", {"competing": 2, "compromising": 2}),
    ]),
    "trap", True, "competing_interrupt_1", 0.5,
    tags=["conflict_resolution", "competing", "trap", "social_desirability"]))

questions.append(make_q("competing", "forced_choice",
    "You must choose: Would you rather be respected for your convictions or liked for your flexibility?",
    opts([
        ("Respected for my convictions", {"competing": 5, "collaborating": 1}),
        ("Liked for my flexibility", {"accommodating": 4, "compromising": 2}),
    ]),
    "core", False, "competing_core_1", 0.4, depth="light"))

questions.append(make_q("competing", "scenario",
    "Your landlord raises rent by 20% with 30 days notice. You believe this exceeds legal limits. What's your first move?",
    opts([
        ("Research the law, draft a formal letter citing specific statutes, and demand they rescind", {"competing": 5}),
        ("Call the landlord to discuss it and try to negotiate a smaller increase", {"compromising": 4, "collaborating": 2}),
        ("Talk to neighbors to see if everyone got the same increase and organize a group response", {"collaborating": 4, "competing": 2}),
        ("Start looking for a new place—fighting with your landlord never ends well", {"avoiding": 5}),
    ]),
    "triangulation", False, "competing_assert_2", 0.8))

questions.append(make_q("competing", "scenario",
    "A coworker takes credit for an idea you shared in a private conversation. In the next meeting, the boss praises them for it. What do you do?",
    opts([
        ("Speak up immediately: 'Actually, I mentioned that idea to [coworker] last week—glad it got traction'", {"competing": 5}),
        ("Say nothing in the meeting but confront the coworker privately afterward", {"competing": 3, "avoiding": 2}),
        ("Let it go this time but make sure to share ideas in public channels going forward", {"avoiding": 3, "compromising": 2}),
        ("Mention it casually to the boss later in a 1:1, framing it as building on the idea together", {"collaborating": 3, "competing": 2}),
    ]),
    "trap", True, "competing_credit_1", 0.6,
    tags=["conflict_resolution", "competing", "trap", "work"]))

questions.append(make_q("competing", "somatic",
    "You're about to push back on your manager's decision. What do you notice in your body?",
    opts([
        ("Energy and alertness—like I'm gearing up for a performance", {"competing": 4}),
        ("Tension in my shoulders and a knot in my stomach", {"avoiding": 3, "accommodating": 2}),
        ("Calm focus—I've prepared my points and feel grounded", {"collaborating": 3, "competing": 2}),
        ("Honestly, a little excited—I enjoy the challenge", {"competing": 5}),
    ]),
    "consistency_check", False, "competing_somatic_1", 0.7, depth="deep"))

questions.append(make_q("competing", "behavioral_recall",
    "Think about the last disagreement where you backed down. Why did you?",
    opts([
        ("I realized I was wrong—the other person had better evidence", {"collaborating": 4}),
        ("I was tired of fighting and the issue wasn't worth the energy", {"avoiding": 4, "compromising": 2}),
        ("The other person was getting emotional and I didn't want to escalate", {"accommodating": 3, "avoiding": 2}),
        ("I honestly can't remember the last time I fully backed down", {"competing": 5}),
    ]),
    "triangulation", False, "competing_backdown_1", 0.7))

questions.append(make_q("competing", "temporal",
    "When a conflict with a friend resolves in your favor, how long does the satisfaction last?",
    opts([
        ("It stays with me—being right matters to me", {"competing": 5}),
        ("A few minutes, then I start worrying about the relationship", {"accommodating": 3, "competing": 2}),
        ("I don't really keep score—once it's resolved I move on", {"compromising": 3, "collaborating": 2}),
        ("I usually feel worse after 'winning' than I expected to", {"collaborating": 3, "avoiding": 2}),
    ]),
    "consistency_check", False, "competing_temporal_1", 0.7))

questions.append(make_q("competing", "partner_perspective",
    "If your romantic partner (or closest person) rated your stubbornness on a scale, where would they put you?",
    opts([
        ("Off the charts—they've literally said I'm the most stubborn person they know", {"competing": 5}),
        ("Above average—I can be immovable on things that matter to me", {"competing": 4}),
        ("Middle of the road—I have my moments but I'm reasonable", {"compromising": 3}),
        ("Low—I'm usually the one who gives in to keep the peace", {"accommodating": 4, "avoiding": 2}),
    ]),
    "trap", True, "competing_stubborn_1", 0.4,
    tags=["conflict_resolution", "competing", "trap", "relationship"]))

questions.append(make_q("competing", "scenario",
    "You're playing a board game with friends. You notice another player made an illegal move that benefits them. No one else caught it. What do you do?",
    opts([
        ("Call it out immediately—rules are rules", {"competing": 4}),
        ("Let it slide—it's just a game", {"accommodating": 3, "avoiding": 3}),
        ("Mention it casually: 'Hey, I think that move might not be legal—want to check?'", {"collaborating": 3, "compromising": 2}),
        ("Keep quiet but make a mental note for next time", {"avoiding": 4}),
    ]),
    "triangulation", False, None, 0.8))

questions.append(make_q("competing", "forced_choice",
    "In a negotiation, would you rather get 80% of what you want while the other side is unhappy, or 60% while both sides feel okay?",
    opts([
        ("80%—that's why you negotiate", {"competing": 5}),
        ("60%—a deal both sides can live with lasts longer", {"compromising": 4, "collaborating": 2}),
    ]),
    "core", False, "competing_core_2", 0.5, depth="light"))

questions.append(make_q("competing", "scenario",
    "Your sibling wants to sell your deceased parent's house immediately. You want to keep it for sentimental reasons. Neither of you can buy the other out. What do you do?",
    opts([
        ("Make the strongest possible case for keeping it and try to find creative financing", {"competing": 4, "collaborating": 2}),
        ("Propose renting it out as a compromise so neither of you fully loses", {"compromising": 5}),
        ("Listen to their reasoning first and try to understand what's driving the urgency", {"collaborating": 4}),
        ("Agree to sell—family harmony matters more than a building", {"accommodating": 5}),
    ]),
    "triangulation", False, "competing_family_1", 0.8))

questions.append(make_q("competing", "trap",
    "How important is it to you that people see you as someone who stands up for themselves?",
    opts([
        ("Very important—self-advocacy is a core value", {"competing": 4}),
        ("Somewhat important but not at the expense of relationships", {"compromising": 3, "accommodating": 2}),
        ("Not particularly—I'd rather be seen as fair and considerate", {"accommodating": 3, "collaborating": 2}),
        ("I don't think about how others perceive my conflict style", {"avoiding": 3}),
    ]),
    "trap", True, "competing_image_1", 0.3,
    tags=["conflict_resolution", "competing", "trap", "self_image"]))

# FIX: question_type should be valid
questions[-1]["question_type"] = "behavioral_recall"

questions.append(make_q("competing", "scenario",
    "You overhear a colleague giving incorrect information to a client. The colleague is senior to you. What do you do?",
    opts([
        ("Correct them on the spot—accuracy matters more than hierarchy", {"competing": 5}),
        ("Send a follow-up message to the client with the correct info, CC'ing the colleague", {"competing": 3, "collaborating": 2}),
        ("Pull the colleague aside afterward and mention what you heard", {"collaborating": 3, "avoiding": 2}),
        ("Say nothing—it's their client relationship to manage", {"avoiding": 4, "accommodating": 2}),
    ]),
    "triangulation", False, "competing_hierarchy_1", 0.7,
    tags=["conflict_resolution", "competing", "triangulation", "work"]))

questions.append(make_q("competing", "somatic",
    "Someone cuts in front of you in a long line. What's your immediate physical response?",
    opts([
        ("Heat in my face, shoulders square—I'm about to say something", {"competing": 5}),
        ("A sigh and eye-roll—annoying but not worth a confrontation", {"avoiding": 3, "compromising": 2}),
        ("I tap them on the shoulder politely and point out the line", {"competing": 3, "collaborating": 2}),
        ("I barely notice—I'm usually on my phone anyway", {"avoiding": 4}),
    ]),
    "consistency_check", False, "competing_line_1", 0.6))

questions.append(make_q("competing", "behavioral_recall",
    "In the last year, how many times have you sent a strongly worded email or text that you later wished you could take back?",
    opts([
        ("More than five—I'm passionate and it comes through in writing", {"competing": 5}),
        ("Two or three times", {"competing": 3}),
        ("Once, maybe—I usually draft and then soften before sending", {"compromising": 3, "collaborating": 2}),
        ("Never—I'm very careful with written communication", {"avoiding": 3, "accommodating": 2}),
    ]),
    "trap", True, "competing_email_1", 0.5,
    tags=["conflict_resolution", "competing", "trap", "behavioral"]))

questions.append(make_q("competing", "temporal",
    "Think of someone you've had recurring disagreements with over the past year. Has your approach to them changed?",
    opts([
        ("No—I've been consistent because my position is right", {"competing": 5}),
        ("Yes—I've learned which battles to fight with this person", {"compromising": 4, "avoiding": 2}),
        ("Yes—we've found better ways to communicate our differences", {"collaborating": 5}),
        ("I've mostly stopped engaging—it's not worth it", {"avoiding": 4, "accommodating": 2}),
    ]),
    "triangulation", False, "competing_recurring_1", 0.7))

questions.append(make_q("competing", "partner_perspective",
    "After a heated argument with you, your partner says: 'You always have to be right.' How accurate is that?",
    opts([
        ("Honestly? Probably pretty accurate—being wrong is hard for me", {"competing": 5}),
        ("It's unfair—I only push hard when the evidence supports me", {"competing": 4}),
        ("There's some truth to it, and I'm working on it", {"competing": 3, "collaborating": 2}),
        ("Not accurate—I give in more than they realize", {"accommodating": 3, "compromising": 2}),
    ]),
    "consistency_check", False, "competing_partner_1", 0.5))

questions.append(make_q("competing", "forced_choice",
    "A friend asks for honest feedback on their business idea. You think it's terrible. Do you:",
    opts([
        ("Tell them directly—real friends don't let friends waste money on bad ideas", {"competing": 4}),
        ("Highlight the strengths first, then gently raise concerns", {"collaborating": 3, "accommodating": 2}),
        ("Ask probing questions and let them discover the weaknesses themselves", {"collaborating": 4}),
        ("Keep concerns vague—it's their money and their dream", {"accommodating": 4, "avoiding": 2}),
    ]),
    "triangulation", False, None, 0.7))

questions.append(make_q("competing", "scenario",
    "You're renovating your home. The contractor wants to do something a cheaper way that you believe will cause problems in 5 years. They insist their way is fine. What do you do?",
    opts([
        ("Hold firm—it's your house and your money. You want it done your way.", {"competing": 5}),
        ("Get a second opinion and bring the evidence to the contractor", {"collaborating": 4, "competing": 2}),
        ("Compromise—do it their way for some parts, your way for others", {"compromising": 4}),
        ("Trust the professional—they do this every day and you don't", {"accommodating": 4}),
    ]),
    "triangulation", False, "competing_assert_3", 0.8))

questions.append(make_q("competing", "behavioral_recall",
    "When was the last time you let someone else's bad idea proceed without objecting, even though you knew it would fail?",
    opts([
        ("I can't remember—I always speak up when I see a problem", {"competing": 5}),
        ("Recently—sometimes people need to learn from their own mistakes", {"avoiding": 3, "accommodating": 2}),
        ("It happens when the stakes are low and fighting it isn't worth the political cost", {"compromising": 4, "avoiding": 2}),
        ("Last week—I'm trying to be less controlling", {"accommodating": 3, "collaborating": 2}),
    ]),
    "trap", True, None, 0.5,
    tags=["conflict_resolution", "competing", "trap", "control"]))

# ============================================================
# COLLABORATING (24 questions)
# ============================================================

questions.append(make_q("collaborating", "scenario",
    "Two team members come to you with conflicting approaches to a project. Both have valid points. How do you handle it?",
    opts([
        ("Facilitate a meeting where both present their full cases, then synthesize the best elements", {"collaborating": 5}),
        ("Pick the stronger approach and move forward—analysis paralysis helps no one", {"competing": 4}),
        ("Suggest they each give a little and meet in the middle", {"compromising": 4}),
        ("Let them work it out between themselves—it's not your call", {"avoiding": 4}),
    ]),
    "core", False, "collab_core_1", 0.6, depth="light"))

questions.append(make_q("collaborating", "somatic",
    "When you're in a brainstorming session and someone builds on your idea in an unexpected direction, what do you feel?",
    opts([
        ("Energized—the creative exchange is exciting", {"collaborating": 5}),
        ("Protective—they're changing my idea without permission", {"competing": 4}),
        ("Relieved—someone else is carrying the creative load", {"avoiding": 3, "accommodating": 2}),
        ("Indifferent—an idea is an idea, doesn't matter whose", {"compromising": 2, "avoiding": 2}),
    ]),
    "triangulation", False, "collab_somatic_1", 0.7, depth="deep"))

questions.append(make_q("collaborating", "partner_perspective",
    "When making a big household decision (where to live, major purchase), how would your partner describe your process?",
    opts([
        ("'We talk it to death—every angle, every option, every feeling. It takes forever but we both feel good about the result'", {"collaborating": 5}),
        ("'They usually know what they want and advocate strongly for it'", {"competing": 4}),
        ("'They ask what I want and go with that'", {"accommodating": 4}),
        ("'We each give a little and find something we can both live with'", {"compromising": 4}),
    ]),
    "consistency_check", False, "collab_partner_1", 0.6))

questions.append(make_q("collaborating", "temporal",
    "Think about a major decision you made with someone else in the last year. How long did the process take compared to what felt efficient?",
    opts([
        ("It took longer than necessary but the outcome was better for the extra time", {"collaborating": 5}),
        ("About right—we found the sweet spot between thorough and efficient", {"collaborating": 3, "compromising": 2}),
        ("Too long—I had to drag the other person through the process", {"competing": 3, "collaborating": 2}),
        ("Quick—one of us made the call and the other went along", {"competing": 3, "accommodating": 3}),
    ]),
    "triangulation", False, "collab_temporal_1", 0.7))

questions.append(make_q("collaborating", "behavioral_recall",
    "In your last significant disagreement, did you ask the other person to explain their perspective before sharing yours?",
    opts([
        ("Yes—I always try to understand their view first", {"collaborating": 5}),
        ("I tried but ended up sharing mine first because I felt strongly", {"competing": 3, "collaborating": 2}),
        ("No—we were both talking past each other honestly", {"competing": 3, "compromising": 2}),
        ("I mostly listened and agreed with their view", {"accommodating": 4}),
    ]),
    "trap", True, "collab_listen_1", 0.4,
    tags=["conflict_resolution", "collaborating", "trap", "social_desirability"]))

questions.append(make_q("collaborating", "forced_choice",
    "A decision needs to be made today. You and your colleague disagree. Would you rather:",
    opts([
        ("Spend two more hours hashing it out until you reach a genuine consensus", {"collaborating": 5}),
        ("Flip a coin and commit fully to whichever option wins", {"avoiding": 2, "compromising": 3}),
        ("Make the call yourself since time is running out", {"competing": 5}),
        ("Go with their preference since you trust them", {"accommodating": 4}),
    ]),
    "triangulation", False, "collab_time_1", 0.6))

questions.append(make_q("collaborating", "scenario",
    "Your partner wants to go to the mountains for vacation. You want the beach. You have one week of PTO left. What do you do?",
    opts([
        ("Research destinations that offer both—a beach town near mountains", {"collaborating": 5}),
        ("Split the week: half mountains, half beach", {"compromising": 5}),
        ("Make your case for the beach with enthusiasm and data", {"competing": 4}),
        ("Tell them the mountains are fine—you just want to spend time together", {"accommodating": 5}),
    ]),
    "consistency_check", False, "collab_vacation_1", 0.7))

questions.append(make_q("collaborating", "scenario",
    "Your teenage child wants a later curfew. You're concerned about safety. How do you approach this?",
    opts([
        ("Sit down together, hear their reasoning, share your concerns, and co-create a plan with check-in texts and a trial period", {"collaborating": 5}),
        ("Hold the line—the curfew exists for a reason and you're the parent", {"competing": 5}),
        ("Extend it by 30 minutes as a compromise", {"compromising": 4}),
        ("Let them have the later curfew—they need to learn from experience", {"accommodating": 4, "avoiding": 2}),
    ]),
    "triangulation", False, "collab_parent_1", 0.7,
    adaptations=["JP", "KR", "CN"]))

questions.append(make_q("collaborating", "somatic",
    "During a heated discussion where you're trying to understand someone who disagrees with you, what happens to your breathing?",
    opts([
        ("It stays steady—I'm focused on listening and understanding", {"collaborating": 4}),
        ("It quickens—I'm preparing my counterarguments", {"competing": 4}),
        ("It gets shallow—conflict makes me anxious", {"avoiding": 4}),
        ("I don't notice—I'm too focused on the content", {"compromising": 2, "competing": 2}),
    ]),
    "triangulation", False, "collab_somatic_2", 0.8, depth="deep"))

questions.append(make_q("collaborating", "behavioral_recall",
    "Think of the last time you changed your mind during a disagreement. What caused it?",
    opts([
        ("The other person presented evidence I hadn't considered", {"collaborating": 5}),
        ("I was tired of arguing and it wasn't worth the fight", {"avoiding": 4, "compromising": 2}),
        ("They got upset and I didn't want to hurt them", {"accommodating": 4}),
        ("I honestly can't remember the last time I changed my mind during an argument", {"competing": 5}),
    ]),
    "trap", True, "collab_mindchange_1", 0.5,
    tags=["conflict_resolution", "collaborating", "trap", "flexibility"]))

questions.append(make_q("collaborating", "temporal",
    "How has your approach to disagreements with your closest person changed over the past 5 years?",
    opts([
        ("We've developed shared language and processes for working through things", {"collaborating": 5}),
        ("I've learned which issues to fight for and which to let go", {"compromising": 3, "avoiding": 2}),
        ("Not much—I've always been direct about what I want", {"competing": 4}),
        ("I've become better at reading what they need and adapting", {"accommodating": 4}),
    ]),
    "consistency_check", False, "collab_evolution_1", 0.7))

questions.append(make_q("collaborating", "partner_perspective",
    "Your best friend describes how you handle group decisions (where to eat, what to do on a weekend). What do they say?",
    opts([
        ("'They want everyone to weigh in and find something everyone's excited about—even if it takes an hour'", {"collaborating": 5}),
        ("'They usually have a strong opinion and lobby for it'", {"competing": 4}),
        ("'They suggest splitting the difference or going somewhere neutral'", {"compromising": 4}),
        ("'They go with the flow—they're happy with whatever'", {"accommodating": 4, "avoiding": 2}),
    ]),
    "triangulation", False, "collab_group_1", 0.6))

questions.append(make_q("collaborating", "scenario",
    "You and a neighbor share a fence that needs replacing. You want cedar, they want vinyl. The cost difference is significant. How do you handle it?",
    opts([
        ("Research both options together, get joint quotes, and find a solution that addresses both your needs (maybe cedar on your side, vinyl on theirs)", {"collaborating": 5}),
        ("Offer to pay the difference for cedar since it's your preference", {"accommodating": 3, "collaborating": 2}),
        ("Insist on cedar—you'll be looking at this fence for 20 years", {"competing": 4}),
        ("Go with vinyl to avoid a neighborly dispute", {"accommodating": 4, "avoiding": 2}),
    ]),
    "triangulation", False, None, 0.8))

questions.append(make_q("collaborating", "forced_choice",
    "When solving a problem with someone, do you naturally focus more on understanding their constraints or presenting your solution?",
    opts([
        ("Understanding their constraints first—solutions emerge from shared understanding", {"collaborating": 5}),
        ("Presenting my solution—I usually come prepared with one", {"competing": 4}),
        ("It depends on how much time we have", {"compromising": 3}),
        ("I usually let them lead and support their direction", {"accommodating": 4}),
    ]),
    "core", False, "collab_core_2", 0.5, depth="light"))

questions.append(make_q("collaborating", "trap",
    "How often do your collaborative discussions actually result in a genuinely new solution that neither person started with?",
    opts([
        ("Almost always—that's the whole point of collaborating", {"collaborating": 4}),
        ("Sometimes, but often one person's original idea wins with minor modifications", {"competing": 3, "collaborating": 2}),
        ("Rarely—usually we compromise rather than truly synthesize", {"compromising": 4}),
        ("I'm not sure I could tell the difference between genuine synthesis and one person caving gracefully", {"avoiding": 2, "accommodating": 2, "competing": 2}),
    ]),
    "trap", True, "collab_honesty_1", 0.3,
    tags=["conflict_resolution", "collaborating", "trap", "self_honesty"]))

# Fix question_type
questions[-1]["question_type"] = "behavioral_recall"

questions.append(make_q("collaborating", "scenario",
    "A project deadline is approaching and your approach isn't working. A junior colleague suggests a radically different method. What's your honest first reaction?",
    opts([
        ("Interest—if their method could work, ego shouldn't matter", {"collaborating": 5}),
        ("Skepticism—I have more experience and my approach should work with more time", {"competing": 4}),
        ("Relief—someone else has an idea and the pressure is off me", {"avoiding": 3, "accommodating": 2}),
        ("Let's try a hybrid—some of my approach, some of theirs", {"compromising": 4}),
    ]),
    "trap", True, "collab_ego_1", 0.4,
    tags=["conflict_resolution", "collaborating", "trap", "ego"]))

questions.append(make_q("collaborating", "somatic",
    "When you and someone reach a genuine 'we both got what we needed' resolution, what do you feel physically?",
    opts([
        ("A warm sense of connection—like something real happened between us", {"collaborating": 5}),
        ("Relief that the conflict is over", {"avoiding": 3, "accommodating": 2}),
        ("Satisfaction that I got what I needed from the exchange", {"competing": 3}),
        ("Nothing special—it's just how things should work", {"compromising": 2}),
    ]),
    "consistency_check", False, "collab_somatic_3", 0.7, depth="deep"))

questions.append(make_q("collaborating", "temporal",
    "When someone you disagreed with turns out to be right, how long does it take you to fully acknowledge it?",
    opts([
        ("Immediately—I have no problem saying 'you were right'", {"collaborating": 5}),
        ("A day or two—I need to process it before admitting it", {"competing": 3}),
        ("I acknowledge it internally but may not say it out loud", {"competing": 4, "avoiding": 2}),
        ("I don't think of disagreements in terms of right/wrong", {"compromising": 3, "collaborating": 2}),
    ]),
    "trap", True, None, 0.4,
    tags=["conflict_resolution", "collaborating", "trap", "humility"]))

questions.append(make_q("collaborating", "behavioral_recall",
    "In your most recent group project or team effort, did you actively solicit dissenting opinions?",
    opts([
        ("Yes—I specifically asked 'what could go wrong' and 'who disagrees'", {"collaborating": 5}),
        ("I was open to hearing them but didn't specifically seek them out", {"collaborating": 3, "compromising": 2}),
        ("Not really—we were aligned and I didn't want to create problems", {"avoiding": 3, "accommodating": 2}),
        ("I shared my vision clearly and the team got on board", {"competing": 4}),
    ]),
    "trap", True, "collab_dissent_1", 0.4,
    tags=["conflict_resolution", "collaborating", "trap", "leadership"]))

questions.append(make_q("collaborating", "partner_perspective",
    "If a colleague described your email style during a disagreement, which sounds most like you?",
    opts([
        ("Long, thoughtful emails exploring multiple angles with questions at the end", {"collaborating": 5}),
        ("Short, direct emails stating your position clearly", {"competing": 4}),
        ("Diplomatic emails that acknowledge their view while gently steering toward yours", {"compromising": 3, "competing": 2}),
        ("You'd rather have the conversation in person than over email", {"collaborating": 3, "avoiding": 2}),
    ]),
    "consistency_check", False, None, 0.7))

questions.append(make_q("collaborating", "scenario",
    "Your book club can't agree on the next book. Three factions, three different genres. You're facilitating. What do you do?",
    opts([
        ("Have each faction pitch their book, discuss what each person is craving from the reading experience, find a book that satisfies the underlying needs", {"collaborating": 5}),
        ("Rotate—each faction picks one of the next three books", {"compromising": 5}),
        ("Vote—majority rules", {"competing": 3}),
        ("Read whatever—you're there for the company, not the book", {"accommodating": 4}),
    ]),
    "triangulation", False, None, 0.7))

questions.append(make_q("collaborating", "behavioral_recall",
    "How often do you ask 'what am I missing?' during a disagreement?",
    opts([
        ("Almost every time—it's a genuine question, not a rhetorical one", {"collaborating": 5}),
        ("Sometimes, when I'm stuck and need new input", {"collaborating": 3, "compromising": 2}),
        ("Rarely—I usually have a clear picture of the situation", {"competing": 4}),
        ("I ask it but mostly as a politeness—I usually think I have it right", {"competing": 4, "collaborating": 1}),
    ]),
    "trap", True, "collab_missing_1", 0.3,
    tags=["conflict_resolution", "collaborating", "trap", "metacognition"]))

questions.append(make_q("collaborating", "forced_choice",
    "A 90-minute meeting has produced no consensus. You have 10 minutes left. Do you:",
    opts([
        ("Push for 30 more minutes—we're close and rushing will waste the 90 minutes already invested", {"collaborating": 4}),
        ("Propose a vote and commit to the majority's choice", {"compromising": 3, "competing": 2}),
        ("Make a decision yourself and take accountability for it", {"competing": 5}),
        ("Table it—fresh eyes next week might help", {"avoiding": 3, "collaborating": 2}),
    ]),
    "triangulation", False, "collab_time_2", 0.6))

# ============================================================
# COMPROMISING (24 questions)
# ============================================================

questions.append(make_q("compromising", "scenario",
    "You're splitting household chores with a roommate. You hate dishes; they hate vacuuming. But the dishes take twice as long. How do you divide things?",
    opts([
        ("Each person does what they hate less, and the dishes person gets fewer total chores to balance time", {"collaborating": 5}),
        ("Alternate everything weekly so it's perfectly equal", {"compromising": 5}),
        ("You do dishes if they do vacuuming plus one other thing—exact time parity matters", {"competing": 3, "compromising": 2}),
        ("You'll do whichever they don't want—it's not worth fighting about chores", {"accommodating": 4}),
    ]),
    "triangulation", False, "comp_fairness_1", 0.7))

questions.append(make_q("compromising", "somatic",
    "When you accept a compromise that gives you 50% of what you wanted, how does your body respond?",
    opts([
        ("A slight sense of loss—like leaving money on the table", {"competing": 3, "compromising": 2}),
        ("Relief—the conflict is resolved and both sides gave something", {"compromising": 4, "avoiding": 2}),
        ("Nothing strong—this is just how negotiations work", {"compromising": 5}),
        ("Resentment building slowly—I should have pushed harder", {"competing": 5}),
    ]),
    "triangulation", False, "comp_somatic_1", 0.7, depth="deep"))

questions.append(make_q("compromising", "partner_perspective",
    "How would your partner describe your approach to choosing a restaurant together?",
    opts([
        ("'We each suggest two places and pick one from the combined list'", {"compromising": 5}),
        ("'They always know exactly where they want to go'", {"competing": 4}),
        ("'They ask me what I'm in the mood for and work from there'", {"collaborating": 4}),
        ("'They tell me to pick—they're happy anywhere'", {"accommodating": 4}),
    ]),
    "consistency_check", False, "comp_restaurant_1", 0.6))

questions.append(make_q("compromising", "temporal",
    "Think about a compromise you made at work in the last 6 months. In hindsight, do you wish you had pushed harder for your original position?",
    opts([
        ("Yes—the compromise watered down the outcome", {"competing": 4}),
        ("No—the compromise was fair and reasonable", {"compromising": 5}),
        ("I wish we had explored more creative options beyond splitting the difference", {"collaborating": 4}),
        ("I barely remember—I move on quickly from these things", {"avoiding": 3, "accommodating": 2}),
    ]),
    "triangulation", False, "comp_hindsight_1", 0.7))

questions.append(make_q("compromising", "behavioral_recall",
    "How quickly do you typically offer a compromise when a disagreement starts?",
    opts([
        ("Almost immediately—why waste time posturing when we can find the middle?", {"compromising": 5}),
        ("Only after I've made my full case first", {"competing": 4}),
        ("After we've both shared our perspectives and explored options", {"collaborating": 4}),
        ("I don't usually offer compromises—I either agree or disengage", {"avoiding": 3, "accommodating": 3}),
    ]),
    "core", False, "comp_core_1", 0.6, depth="light"))

questions.append(make_q("compromising", "forced_choice",
    "You have two job offers. One pays 20% more but has a toxic culture. The other is less money but great people. A friend says 'negotiate the good job up.' Do you:",
    opts([
        ("Negotiate aggressively—you deserve both good culture and good pay", {"competing": 4}),
        ("Ask for a modest raise—meet them in the middle", {"compromising": 5}),
        ("Take the good culture job as-is—money isn't everything", {"accommodating": 3, "collaborating": 2}),
        ("Go back to the high-paying job and see if the culture concerns are addressable", {"collaborating": 4}),
    ]),
    "triangulation", False, None, 0.7))

questions.append(make_q("compromising", "scenario",
    "You and your spouse disagree on how much to spend on Christmas gifts for the kids. You want to spend $200 per child, they want $100. What happens?",
    opts([
        ("You land on $150—splitting the difference feels fair", {"compromising": 5}),
        ("You discuss what each child actually needs and wants, and let that drive the budget", {"collaborating": 5}),
        ("You make the case for $200 with examples of what you'd buy", {"competing": 4}),
        ("You agree to $100—your spouse is more financially cautious and that's probably wise", {"accommodating": 4}),
    ]),
    "consistency_check", False, "comp_money_1", 0.7))

questions.append(make_q("compromising", "somatic",
    "When someone proposes splitting something exactly 50/50, what's your gut reaction?",
    opts([
        ("Fair—that's the obvious starting point", {"compromising": 5}),
        ("Depends on what we're splitting—equal isn't always equitable", {"collaborating": 4}),
        ("I'd rather get more than 50%, honestly", {"competing": 4}),
        ("I'd give them more to avoid seeming petty", {"accommodating": 4}),
    ]),
    "triangulation", False, "comp_5050_1", 0.6, depth="moderate"))

questions.append(make_q("compromising", "partner_perspective",
    "A colleague describes you in a negotiation. Which do they say?",
    opts([
        ("'They're the first to say, let's find a middle ground'", {"compromising": 5}),
        ("'They come in with a strong opening position and don't budge much'", {"competing": 5}),
        ("'They spend a lot of time understanding what everyone needs'", {"collaborating": 4}),
        ("'They tend to go along with whoever has the strongest opinion'", {"accommodating": 4}),
    ]),
    "triangulation", False, "comp_colleague_1", 0.6))

questions.append(make_q("compromising", "behavioral_recall",
    "When splitting a bill with friends, how do you handle it if you ordered less?",
    opts([
        ("I suggest we split evenly—it's not worth nickel-and-diming", {"compromising": 4, "accommodating": 2}),
        ("I mention it and suggest we pay for what we ordered", {"competing": 3, "collaborating": 2}),
        ("I pay the even split but feel slightly annoyed", {"accommodating": 3, "avoiding": 2}),
        ("I offer to Venmo the difference or pick up the next one", {"compromising": 4, "collaborating": 2}),
    ]),
    "trap", True, "comp_bill_1", 0.5,
    tags=["conflict_resolution", "compromising", "trap", "money"]))

questions.append(make_q("compromising", "temporal",
    "Over your lifetime, has your tendency to compromise increased or decreased?",
    opts([
        ("Increased—I've learned that getting something is better than getting nothing", {"compromising": 5}),
        ("Decreased—I've learned that compromising too quickly leaves value on the table", {"competing": 4}),
        ("It's shifted—I now pick when to compromise more strategically", {"collaborating": 3, "compromising": 2}),
        ("It's about the same—I've always been pretty moderate", {"compromising": 4}),
    ]),
    "consistency_check", False, "comp_lifetime_1", 0.7))

questions.append(make_q("compromising", "scenario",
    "You're co-planning a party. Your co-planner wants an elaborate theme party. You want a casual gathering. What do you do?",
    opts([
        ("Suggest a light theme that's fun but doesn't require costumes or elaborate decoration", {"compromising": 5}),
        ("Go all in on the theme—their enthusiasm is contagious", {"accommodating": 4}),
        ("Push for casual—theme parties stress people out", {"competing": 4}),
        ("Propose two events: a themed dinner party and a casual barbecue", {"collaborating": 4}),
    ]),
    "triangulation", False, None, 0.7))

questions.append(make_q("compromising", "forced_choice",
    "Complete this sentence: 'A good compromise is one where...'",
    opts([
        ("Both sides feel slightly dissatisfied—that means it was truly balanced", {"compromising": 5}),
        ("Both sides feel they got what mattered most", {"collaborating": 5}),
        ("The better argument won, even if the other side gave something up", {"competing": 4}),
        ("The relationship was preserved regardless of the outcome", {"accommodating": 4}),
    ]),
    "core", False, "comp_core_2", 0.5, depth="light"))

questions.append(make_q("compromising", "scenario",
    "Your department needs to cut 10% of the budget. You can cut equally across all teams, or cut deeply from one underperforming area. What's your instinct?",
    opts([
        ("Equal cuts—shared pain is fairer even if suboptimal", {"compromising": 5}),
        ("Cut the underperformer—why punish good teams for a struggling one", {"competing": 4}),
        ("Analyze each team's needs and craft targeted cuts based on impact", {"collaborating": 5}),
        ("Ask each team leader to propose their own cuts—let them own it", {"avoiding": 3, "collaborating": 2}),
    ]),
    "triangulation", False, "comp_budget_1", 0.7))

questions.append(make_q("compromising", "somatic",
    "When a negotiation stalls and neither side will move, what happens in your body?",
    opts([
        ("Restlessness—I want to propose a split just to get unstuck", {"compromising": 5}),
        ("Determination—I dig in harder", {"competing": 5}),
        ("Anxiety—the tension is uncomfortable", {"avoiding": 4, "accommodating": 2}),
        ("Curiosity—there must be something we're both missing", {"collaborating": 4}),
    ]),
    "triangulation", False, "comp_stall_1", 0.7, depth="deep"))

questions.append(make_q("compromising", "behavioral_recall",
    "In your last salary negotiation, did you accept the first counteroffer?",
    opts([
        ("Yes—it was close enough to what I wanted", {"compromising": 4, "accommodating": 2}),
        ("No—I countered again and we met somewhere between", {"compromising": 3, "competing": 2}),
        ("No—I held firm on my number and they eventually met it", {"competing": 5}),
        ("I didn't negotiate—I accepted the initial offer", {"accommodating": 4, "avoiding": 3}),
    ]),
    "trap", True, "comp_salary_1", 0.5,
    tags=["conflict_resolution", "compromising", "trap", "money"]))

questions.append(make_q("compromising", "partner_perspective",
    "Your teenager accuses you of 'always taking the easy middle.' Are they right?",
    opts([
        ("Probably—I value fairness and the middle usually feels fair", {"compromising": 5}),
        ("No—I fight hard for what's important, I just don't need to win everything", {"compromising": 3, "competing": 2}),
        ("Maybe—but the middle is where real life happens", {"compromising": 4}),
        ("They're wrong—I usually give them what they want", {"accommodating": 4}),
    ]),
    "consistency_check", False, "comp_teen_1", 0.5))

questions.append(make_q("compromising", "temporal",
    "Think of a compromise you made 5+ years ago that you're still not fully okay with. What does that tell you?",
    opts([
        ("That I should have fought harder—I compromised on something that mattered too much", {"competing": 4}),
        ("That compromise sometimes means nobody wins, and that's not always okay", {"collaborating": 4}),
        ("I can't think of one—I make peace with compromises pretty quickly", {"compromising": 5, "avoiding": 2}),
        ("That I need to be more selective about when I compromise", {"compromising": 3, "competing": 2}),
    ]),
    "trap", True, "comp_regret_1", 0.6,
    tags=["conflict_resolution", "compromising", "trap", "depth"]))

questions.append(make_q("compromising", "scenario",
    "Two friends are fighting and both come to you for support. You see valid points on both sides. What do you do?",
    opts([
        ("Help each see the other's perspective and suggest they meet halfway", {"compromising": 4, "collaborating": 2}),
        ("Tell each of them honestly where you think they're right and wrong", {"competing": 3, "collaborating": 3}),
        ("Facilitate a conversation between them", {"collaborating": 5}),
        ("Stay out of it—you don't want to pick sides", {"avoiding": 5}),
    ]),
    "triangulation", False, None, 0.7))

questions.append(make_q("compromising", "behavioral_recall",
    "When you're shopping with someone who likes a different item than you, how do you typically resolve it?",
    opts([
        ("We each get what we want—why compromise on personal taste?", {"competing": 3, "avoiding": 2}),
        ("We find something we both like well enough", {"compromising": 5}),
        ("I go with what they want—I'm less particular", {"accommodating": 4}),
        ("We discuss what we each like about our choices and look for something that combines those features", {"collaborating": 4}),
    ]),
    "consistency_check", False, None, 0.7))

questions.append(make_q("compromising", "forced_choice",
    "Your company is choosing between two software platforms. Neither is perfect. Do you advocate for:",
    opts([
        ("The one that's 'good enough' on both sides—perfect is the enemy of good", {"compromising": 5}),
        ("The one that's excellent in the most critical area, even if it's weak elsewhere", {"competing": 4}),
        ("A deeper analysis of both before deciding—maybe there's a third option", {"collaborating": 4}),
        ("Whatever the team prefers—you can adapt to either", {"accommodating": 4}),
    ]),
    "triangulation", False, None, 0.6))

questions.append(make_q("compromising", "scenario",
    "You're merging two teams with different work cultures. One is formal and structured, the other casual and flexible. As the new manager, what's your approach?",
    opts([
        ("Create hybrid norms—structured meetings but flexible work hours", {"compromising": 5}),
        ("Let both cultures coexist—people can work their own way", {"avoiding": 3, "accommodating": 3}),
        ("Set the standard based on what produces better results", {"competing": 4}),
        ("Facilitate a series of conversations where both teams co-create the new culture", {"collaborating": 5}),
    ]),
    "triangulation", False, "comp_culture_1", 0.7))

questions.append(make_q("compromising", "trap",
    "Be honest: when you compromise quickly, is it more about efficiency or about avoiding the discomfort of prolonged conflict?",
    opts([
        ("Efficiency—I genuinely value speed over perfection", {"compromising": 4}),
        ("Avoiding discomfort—I hate the tension of unresolved disagreement", {"avoiding": 4, "accommodating": 2}),
        ("Both, honestly", {"compromising": 3, "avoiding": 2}),
        ("Neither—I compromise when it's the right call, not as a reflex", {"collaborating": 3, "competing": 2}),
    ]),
    "trap", True, "comp_motive_1", 0.3,
    tags=["conflict_resolution", "compromising", "trap", "self_honesty"]))

# Fix question_type
questions[-1]["question_type"] = "behavioral_recall"

questions.append(make_q("compromising", "somatic",
    "When you propose 'let's meet in the middle' and the other person says 'no, I want all of it,' what do you feel?",
    opts([
        ("Irritation—I made a fair offer and they're being unreasonable", {"competing": 3, "compromising": 2}),
        ("Respect—at least they know what they want", {"competing": 2, "collaborating": 2}),
        ("Anxiety—now what?", {"avoiding": 4}),
        ("I move to a different approach—clearly compromise isn't going to work here", {"collaborating": 3, "compromising": 2}),
    ]),
    "consistency_check", False, "comp_rejected_1", 0.7, depth="deep"))

# ============================================================
# AVOIDING (24 questions)
# ============================================================

questions.append(make_q("avoiding", "scenario",
    "Your partner brings up a topic that always leads to an argument. They seem calm and genuine this time. What do you do?",
    opts([
        ("Change the subject smoothly—nothing good comes from this conversation", {"avoiding": 5}),
        ("Engage cautiously—maybe this time will be different", {"collaborating": 3, "avoiding": 2}),
        ("Listen but keep your opinions to yourself", {"accommodating": 3, "avoiding": 3}),
        ("Address it directly—if they're bringing it up, it clearly matters to them", {"collaborating": 4, "competing": 2}),
    ]),
    "core", False, "avoid_core_1", 0.6, depth="light"))

questions.append(make_q("avoiding", "somatic",
    "When you realize a conversation is about to become a conflict, what does your body do?",
    opts([
        ("I feel the urge to physically leave—get a glass of water, check my phone, go to the bathroom", {"avoiding": 5}),
        ("My heart rate increases and I feel energized to engage", {"competing": 5}),
        ("I feel heavy—like I want to just absorb whatever they say so it ends faster", {"accommodating": 4}),
        ("I take a breath and try to center myself for what's coming", {"collaborating": 4}),
    ]),
    "triangulation", False, "avoid_somatic_1", 0.7, depth="deep"))

questions.append(make_q("avoiding", "partner_perspective",
    "Your partner would say that when they try to discuss a problem, you most often:",
    opts([
        ("Shut down—go quiet, leave the room, or say 'I don't want to talk about this'", {"avoiding": 5}),
        ("Engage but get defensive quickly", {"competing": 4}),
        ("Listen and validate but don't share your own feelings", {"accommodating": 4}),
        ("Ask questions and try to understand before responding", {"collaborating": 4}),
    ]),
    "consistency_check", False, "avoid_partner_1", 0.5))

questions.append(make_q("avoiding", "temporal",
    "Is there a difficult conversation you've been putting off for more than a month?",
    opts([
        ("Yes—several, actually", {"avoiding": 5}),
        ("One, maybe—but I have a plan for when to address it", {"avoiding": 2, "compromising": 2}),
        ("No—I handle things as they come up", {"competing": 3, "collaborating": 3}),
        ("I'm not sure—I might be avoiding something I haven't even admitted to myself", {"avoiding": 4}),
    ]),
    "trap", True, "avoid_delay_1", 0.4,
    tags=["conflict_resolution", "avoiding", "trap", "awareness"]))

questions.append(make_q("avoiding", "behavioral_recall",
    "Think about the last time you saw a text or email that you knew would require a difficult response. How long before you replied?",
    opts([
        ("Within the hour—putting it off makes it worse", {"competing": 3, "collaborating": 3}),
        ("Same day, but I needed time to think", {"compromising": 3, "avoiding": 2}),
        ("The next day or later—I needed distance", {"avoiding": 4}),
        ("I'm not sure I ever replied to it", {"avoiding": 5}),
    ]),
    "triangulation", False, "avoid_reply_1", 0.6))

questions.append(make_q("avoiding", "forced_choice",
    "You notice tension between two friends at a dinner you're hosting. Do you:",
    opts([
        ("Ignore it and hope they work it out—it's not your business", {"avoiding": 5}),
        ("Subtly separate them by rearranging seating or conversation groups", {"avoiding": 4, "accommodating": 2}),
        ("Address it privately with one of them later", {"collaborating": 3, "avoiding": 2}),
        ("Say something in the moment: 'Hey, everything okay between you two?'", {"competing": 3, "collaborating": 3}),
    ]),
    "triangulation", False, "avoid_dinner_1", 0.7))

questions.append(make_q("avoiding", "scenario",
    "Your manager gives you feedback that you think is unfair and based on incomplete information. What do you do?",
    opts([
        ("Thank them for the feedback and say nothing more", {"avoiding": 4, "accommodating": 3}),
        ("Politely push back in the moment with specific examples", {"competing": 4, "collaborating": 2}),
        ("Ask for a follow-up meeting once you've had time to gather your thoughts", {"collaborating": 3, "avoiding": 2}),
        ("Nod, then vent to a colleague about how unfair it was", {"avoiding": 5}),
    ]),
    "trap", True, "avoid_feedback_1", 0.5,
    tags=["conflict_resolution", "avoiding", "trap", "work"]))

questions.append(make_q("avoiding", "somatic",
    "When someone asks 'can we talk?' what's your immediate physical response?",
    opts([
        ("Stomach drops—nothing good ever follows those words", {"avoiding": 5}),
        ("Slight adrenaline—I brace for whatever it is", {"competing": 2, "avoiding": 2}),
        ("Curiosity—I wonder what's on their mind", {"collaborating": 4}),
        ("Calm—I'm used to these conversations", {"compromising": 2, "competing": 2}),
    ]),
    "triangulation", False, "avoid_somatic_2", 0.7, depth="deep"))

questions.append(make_q("avoiding", "partner_perspective",
    "If your friends had to choose one word for how you handle conflict, what would it be?",
    opts([
        ("Diplomatic", {"compromising": 4}),
        ("Direct", {"competing": 4}),
        ("Easygoing", {"avoiding": 3, "accommodating": 3}),
        ("Thoughtful", {"collaborating": 4}),
    ]),
    "consistency_check", False, "avoid_oneword_1", 0.6))

questions.append(make_q("avoiding", "temporal",
    "Think of a conflict you avoided that eventually resolved on its own. How often does that actually happen?",
    opts([
        ("More often than people think—time really does heal some things", {"avoiding": 4}),
        ("Sometimes, but only for small things—the big stuff festers", {"avoiding": 3, "compromising": 2}),
        ("Rarely—avoidance usually makes things worse", {"collaborating": 3, "competing": 2}),
        ("I can't think of a good example—my avoidance usually backfires", {"avoiding": 2, "collaborating": 3}),
    ]),
    "trap", True, "avoid_resolve_1", 0.5,
    tags=["conflict_resolution", "avoiding", "trap", "rationalization"]))

questions.append(make_q("avoiding", "behavioral_recall",
    "In the past week, how many times did you think 'I should say something' but didn't?",
    opts([
        ("Multiple times—I constantly bite my tongue", {"avoiding": 5, "accommodating": 2}),
        ("Once or twice, on small things", {"avoiding": 3}),
        ("I can't think of a time—I generally speak my mind", {"competing": 4}),
        ("It happened but I addressed it later in a calmer moment", {"collaborating": 3, "compromising": 2}),
    ]),
    "triangulation", False, "avoid_bite_tongue_1", 0.6))

questions.append(make_q("avoiding", "scenario",
    "You overhear your name in a conversation that sounds critical. The speakers don't know you heard. What do you do?",
    opts([
        ("Pretend you didn't hear it and process it alone", {"avoiding": 5}),
        ("Walk over and say 'I couldn't help but hear my name—what's up?'", {"competing": 4, "collaborating": 2}),
        ("Bring it up later with one of them privately", {"collaborating": 3, "avoiding": 2}),
        ("Let it go—people talk, and their opinion of you isn't your business", {"avoiding": 4, "accommodating": 2}),
    ]),
    "consistency_check", False, "avoid_overheard_1", 0.7))

questions.append(make_q("avoiding", "forced_choice",
    "Which statement resonates most with you?",
    opts([
        ("'If you ignore a problem long enough, it usually goes away'", {"avoiding": 5}),
        ("'The only way out is through'", {"competing": 3, "collaborating": 3}),
        ("'Pick your battles wisely'", {"compromising": 4, "avoiding": 2}),
        ("'An ounce of prevention is worth a pound of cure'", {"collaborating": 4}),
    ]),
    "core", False, "avoid_core_2", 0.5, depth="light"))

questions.append(make_q("avoiding", "scenario",
    "A family member makes a political comment at dinner that you deeply disagree with. What's your move?",
    opts([
        ("Excuse yourself to get more food or help in the kitchen", {"avoiding": 5}),
        ("Change the subject to something lighter", {"avoiding": 4, "accommodating": 2}),
        ("Engage respectfully—family should be able to discuss differences", {"collaborating": 4}),
        ("State your position clearly—staying silent feels like endorsement", {"competing": 4}),
    ]),
    "triangulation", False, "avoid_family_1", 0.7,
    adaptations=["US"]))

questions.append(make_q("avoiding", "somatic",
    "After you've successfully avoided a conflict, do you feel:",
    opts([
        ("Relief—like I dodged a bullet", {"avoiding": 5}),
        ("Guilt—I should have said something", {"avoiding": 3, "collaborating": 2}),
        ("Nothing—it was a non-event", {"avoiding": 4}),
        ("A slight sense of cowardice that I push away", {"avoiding": 4, "competing": 2}),
    ]),
    "trap", True, "avoid_aftermath_1", 0.4,
    tags=["conflict_resolution", "avoiding", "trap", "self_awareness"]))

questions.append(make_q("avoiding", "behavioral_recall",
    "How often do you use humor to deflect when a conversation gets too serious?",
    opts([
        ("Frequently—humor is my default defense mechanism", {"avoiding": 5}),
        ("Sometimes, but I can switch to serious mode when needed", {"avoiding": 3, "compromising": 2}),
        ("Rarely—I prefer to stay with the seriousness", {"collaborating": 3, "competing": 2}),
        ("I use humor to lighten the mood, not to avoid—there's a difference", {"compromising": 3, "collaborating": 2}),
    ]),
    "triangulation", False, "avoid_humor_1", 0.6))

questions.append(make_q("avoiding", "temporal",
    "How many unresolved conflicts do you currently have simmering in your life?",
    opts([
        ("None that I'm aware of—I deal with things", {"competing": 3, "collaborating": 3}),
        ("One or two, but they're manageable", {"compromising": 3, "avoiding": 2}),
        ("Several—they're background noise I've learned to live with", {"avoiding": 5}),
        ("I'm honestly not sure—I might be in denial about some", {"avoiding": 4}),
    ]),
    "trap", True, "avoid_simmering_1", 0.4,
    tags=["conflict_resolution", "avoiding", "trap", "load"]))

questions.append(make_q("avoiding", "partner_perspective",
    "Has a partner or close friend ever said something like 'I wish you'd fight with me instead of going silent'?",
    opts([
        ("Yes—multiple people have said some version of this", {"avoiding": 5}),
        ("Once, and it was a wake-up call", {"avoiding": 3, "collaborating": 2}),
        ("No—I'm not the silent type in conflict", {"competing": 3, "collaborating": 2}),
        ("They've said they wish I'd fight LESS, not more", {"competing": 4}),
    ]),
    "consistency_check", False, "avoid_silent_1", 0.5))

questions.append(make_q("avoiding", "scenario",
    "You receive a performance review that's mostly positive but contains one criticism you strongly disagree with. Do you:",
    opts([
        ("Sign it and move on—one bad point in an otherwise good review isn't worth fighting", {"avoiding": 4, "accommodating": 2}),
        ("Add written comments addressing the specific criticism before signing", {"competing": 3, "collaborating": 3}),
        ("Request a follow-up meeting to discuss the one point you disagree with", {"collaborating": 4, "competing": 2}),
        ("Refuse to sign until the criticism is removed or modified", {"competing": 5}),
    ]),
    "triangulation", False, "avoid_review_1", 0.7))

questions.append(make_q("avoiding", "behavioral_recall",
    "When a friend cancels plans at the last minute for the third time, do you say anything?",
    opts([
        ("No—I figure they have their reasons", {"avoiding": 4, "accommodating": 3}),
        ("I might send a passive-aggressive 'lol ok no worries' but not address it directly", {"avoiding": 4}),
        ("Yes—I tell them it's becoming a pattern and it bothers me", {"competing": 3, "collaborating": 3}),
        ("I stop making plans with them rather than having the conversation", {"avoiding": 5}),
    ]),
    "trap", True, "avoid_passive_1", 0.4,
    tags=["conflict_resolution", "avoiding", "trap", "friendship"]))

questions.append(make_q("avoiding", "forced_choice",
    "Would you rather have a painful conversation now or a peaceful month followed by the same conversation later?",
    opts([
        ("Painful conversation now—ripping off the bandaid", {"competing": 3, "collaborating": 3}),
        ("Peaceful month—I'll take the temporary peace", {"avoiding": 5}),
    ]),
    "consistency_check", False, "avoid_timing_1", 0.5))

questions.append(make_q("avoiding", "scenario",
    "You and a friend have grown apart but they still text you daily. The friendship feels draining. What do you do?",
    opts([
        ("Gradually reduce response frequency and hope they get the hint", {"avoiding": 5}),
        ("Have an honest conversation about where the friendship stands", {"collaborating": 4, "competing": 2}),
        ("Continue responding but invest less emotionally—maintain the surface friendship", {"avoiding": 4, "accommodating": 2}),
        ("Set a boundary: 'I love you but I can't be as available as I used to be'", {"collaborating": 3, "competing": 3}),
    ]),
    "triangulation", False, "avoid_drift_1", 0.7))

questions.append(make_q("avoiding", "temporal",
    "Think about the pattern of your closest relationships. How many ended because something went unspoken too long?",
    opts([
        ("More than I'd like to admit", {"avoiding": 5}),
        ("One or two—those taught me to speak up sooner", {"avoiding": 2, "collaborating": 3}),
        ("None—my relationships end for other reasons", {"competing": 2, "collaborating": 2}),
        ("I'm in one right now where something important isn't being said", {"avoiding": 4}),
    ]),
    "trap", True, "avoid_pattern_1", 0.4,
    tags=["conflict_resolution", "avoiding", "trap", "relationship_pattern"]))

questions.append(make_q("avoiding", "somatic",
    "When you know you need to have a difficult conversation tomorrow, how does it affect your sleep?",
    opts([
        ("I lie awake rehearsing and dreading it", {"avoiding": 5}),
        ("Mild unease but I can still sleep", {"avoiding": 3, "compromising": 2}),
        ("I sleep fine—I've prepared and I'm ready", {"competing": 3, "collaborating": 3}),
        ("I often decide by morning that it's not worth bringing up after all", {"avoiding": 5}),
    ]),
    "consistency_check", False, "avoid_sleep_1", 0.7, depth="deep"))

# ============================================================
# ACCOMMODATING (24 questions)
# ============================================================

questions.append(make_q("accommodating", "scenario",
    "Your team votes to take the project in a direction you believe is a mistake. Your objection was heard but outvoted. What do you do next?",
    opts([
        ("Commit fully to the team's direction—you had your say and the group decided", {"accommodating": 5}),
        ("Commit publicly but continue gathering evidence for your position in case it's needed", {"competing": 3, "collaborating": 2}),
        ("Ask to document your objection formally, then commit to the team direction", {"collaborating": 3, "competing": 2}),
        ("Propose a checkpoint: 'Let's try it for two weeks and reassess'", {"compromising": 4, "collaborating": 2}),
    ]),
    "triangulation", False, "accom_team_1", 0.7))

questions.append(make_q("accommodating", "somatic",
    "When someone you care about expresses disappointment in your decision, what happens in your body?",
    opts([
        ("A sinking feeling—their disappointment physically hurts me", {"accommodating": 5}),
        ("A brief pang but I stand by my decision", {"competing": 3, "collaborating": 2}),
        ("Nothing strong—their feelings about my decisions are their responsibility", {"competing": 4}),
        ("Tension—I start second-guessing and want to fix it immediately", {"accommodating": 4, "avoiding": 2}),
    ]),
    "triangulation", False, "accom_somatic_1", 0.7, depth="deep"))

questions.append(make_q("accommodating", "partner_perspective",
    "If your partner rated 'how often do they put your needs ahead of their own,' what score would they give?",
    opts([
        ("Very high—they'd probably say I do it too much", {"accommodating": 5}),
        ("Moderate—I'm good at balancing both our needs", {"collaborating": 3, "compromising": 3}),
        ("Low—I'm pretty firm about my own needs and they know it", {"competing": 4}),
        ("They might not know—I do it quietly without making it obvious", {"accommodating": 4, "avoiding": 2}),
    ]),
    "consistency_check", False, "accom_partner_1", 0.5))

questions.append(make_q("accommodating", "temporal",
    "Think about the last time you said yes when you wanted to say no. How long ago was it?",
    opts([
        ("Today or yesterday", {"accommodating": 5}),
        ("This week", {"accommodating": 4}),
        ("I genuinely can't remember a recent example", {"competing": 3, "collaborating": 2}),
        ("It happens but I've been getting better at saying no", {"accommodating": 2, "collaborating": 3}),
    ]),
    "trap", True, "accom_yesno_1", 0.4,
    tags=["conflict_resolution", "accommodating", "trap", "boundaries"]))

questions.append(make_q("accommodating", "behavioral_recall",
    "When a waiter brings you the wrong order, what do you do?",
    opts([
        ("Eat it—it's fine, and I don't want to make a fuss", {"accommodating": 5}),
        ("Politely flag it and ask for what I ordered", {"collaborating": 3, "competing": 2}),
        ("Eat it but feel annoyed the whole time", {"accommodating": 3, "avoiding": 3}),
        ("Send it back immediately—I'm paying for what I ordered", {"competing": 4}),
    ]),
    "core", False, "accom_core_1", 0.5, depth="light"))

questions.append(make_q("accommodating", "forced_choice",
    "Your friend wants to watch a movie you've already seen and didn't like. You were looking forward to something else. Do you:",
    opts([
        ("Watch their choice—their enthusiasm matters more than your preference", {"accommodating": 5}),
        ("Suggest your pick and explain why, but go with theirs if they insist", {"compromising": 3, "competing": 2}),
        ("Propose something neither of you has seen", {"collaborating": 4}),
        ("Push for your choice—you already sat through theirs (metaphorically)", {"competing": 4}),
    ]),
    "triangulation", False, "accom_movie_1", 0.7))

questions.append(make_q("accommodating", "scenario",
    "Your sister plans the family vacation every year and always picks what she wants. This year you finally want input. But she's already booked something. What do you do?",
    opts([
        ("Go along with it—she planned it and it would be ungrateful to complain", {"accommodating": 5}),
        ("Express your disappointment and ask to have input next year", {"collaborating": 3, "accommodating": 2}),
        ("Tell her you're not going unless your preferences are considered", {"competing": 5}),
        ("Suggest modifying part of the trip to include something you want", {"compromising": 4}),
    ]),
    "triangulation", False, "accom_family_1", 0.7))

questions.append(make_q("accommodating", "somatic",
    "When you give in during an argument to preserve the relationship, what does your body feel afterward?",
    opts([
        ("Relief—the conflict is over and the relationship is intact", {"accommodating": 4, "avoiding": 2}),
        ("A dull ache—like I abandoned myself", {"accommodating": 4}),
        ("Nothing—giving in on small things doesn't bother me", {"compromising": 3, "accommodating": 2}),
        ("I rarely give in, so I don't have a strong reference point", {"competing": 4}),
    ]),
    "trap", True, "accom_body_after_1", 0.4,
    tags=["conflict_resolution", "accommodating", "trap", "self_abandonment"]))

questions.append(make_q("accommodating", "partner_perspective",
    "Your coworkers would say that in team meetings, you:",
    opts([
        ("Agree with the consensus even when you initially had a different idea", {"accommodating": 5}),
        ("Push back when you disagree, respectfully but firmly", {"competing": 3, "collaborating": 3}),
        ("Facilitate everyone getting heard before sharing your own view", {"collaborating": 4}),
        ("Suggest practical middle-ground solutions", {"compromising": 4}),
    ]),
    "consistency_check", False, "accom_meeting_1", 0.6))

questions.append(make_q("accommodating", "temporal",
    "Over the past year, has anyone told you that you give in too easily?",
    opts([
        ("Yes—a partner, friend, or therapist has pointed this out", {"accommodating": 5}),
        ("Not directly, but I've felt it about myself", {"accommodating": 4}),
        ("No—people generally see me as fair but firm", {"compromising": 3, "competing": 2}),
        ("The opposite—people wish I'd give in more", {"competing": 5}),
    ]),
    "trap", True, "accom_feedback_1", 0.5,
    tags=["conflict_resolution", "accommodating", "trap", "external_feedback"]))

questions.append(make_q("accommodating", "behavioral_recall",
    "In the past month, have you apologized for something that wasn't your fault?",
    opts([
        ("Multiple times—I apologize reflexively", {"accommodating": 5}),
        ("Once or twice, to smooth things over", {"accommodating": 3, "avoiding": 2}),
        ("No—I only apologize when I've actually done something wrong", {"competing": 3, "collaborating": 2}),
        ("I apologize for my part even when the other person was more at fault—it takes two", {"accommodating": 4, "collaborating": 2}),
    ]),
    "triangulation", False, "accom_apologize_1", 0.5))

questions.append(make_q("accommodating", "scenario",
    "Your friend group wants to go to an expensive restaurant. You're on a tight budget but don't want to be the one who changes the plan. What do you do?",
    opts([
        ("Go and just order carefully—you'll figure out the budget later", {"accommodating": 5}),
        ("Suggest a less expensive alternative that's still nice", {"compromising": 4, "collaborating": 2}),
        ("Be honest about your budget and ask if there's flexibility", {"collaborating": 3, "competing": 2}),
        ("Make an excuse not to go rather than bring up money", {"avoiding": 5}),
    ]),
    "triangulation", False, "accom_budget_1", 0.6))

questions.append(make_q("accommodating", "forced_choice",
    "Complete this sentence: 'Relationships work best when...'",
    opts([
        ("Someone is willing to yield for the sake of harmony", {"accommodating": 5}),
        ("Both people communicate honestly even when it's uncomfortable", {"collaborating": 5}),
        ("Both people know when to push and when to bend", {"compromising": 4}),
        ("Everyone knows what they want and advocates for it", {"competing": 4}),
    ]),
    "core", False, "accom_core_2", 0.5, depth="light"))

questions.append(make_q("accommodating", "scenario",
    "You're in a rideshare and the driver takes a route you know is slower. Do you say something?",
    opts([
        ("No—they're the driver and maybe they know something about traffic I don't", {"accommodating": 4, "avoiding": 2}),
        ("I mention it casually: 'Hey, I usually take [route]—any reason for this one?'", {"collaborating": 3, "competing": 2}),
        ("Yes—'Can you switch to [route]? It's faster.'", {"competing": 4}),
        ("I pull up the map and quietly seethe but say nothing", {"avoiding": 4, "accommodating": 2}),
    ]),
    "triangulation", False, None, 0.7))

questions.append(make_q("accommodating", "somatic",
    "When you agree to do something you don't want to do, where does the discomfort live in your body?",
    opts([
        ("My chest—a constriction or heaviness", {"accommodating": 5}),
        ("My gut—a gnawing sense of self-betrayal", {"accommodating": 5}),
        ("My jaw—I clench it while smiling", {"accommodating": 4, "avoiding": 2}),
        ("Nowhere specific—if I agreed, I'm at peace with it", {"compromising": 3, "collaborating": 2}),
    ]),
    "consistency_check", False, "accom_somatic_body_1", 0.6, depth="deep"))

questions.append(make_q("accommodating", "behavioral_recall",
    "How often do you volunteer to do tasks at work that no one else wants?",
    opts([
        ("Almost always—someone has to do it and I don't mind", {"accommodating": 5}),
        ("Sometimes, but I've started being more selective", {"accommodating": 3, "collaborating": 2}),
        ("Rarely—I'm careful about taking on work that isn't mine", {"competing": 3}),
        ("Only when it's genuinely important and no one else can", {"collaborating": 3, "compromising": 2}),
    ]),
    "triangulation", False, "accom_volunteer_1", 0.6))

questions.append(make_q("accommodating", "temporal",
    "Think about a pattern in your relationships: do the people closest to you tend to have strong personalities?",
    opts([
        ("Yes—I seem to gravitate toward people who know what they want", {"accommodating": 4}),
        ("Mixed—some do, some don't", {"compromising": 3}),
        ("No—I'm usually the one with the strong personality", {"competing": 4}),
        ("I hadn't thought about it but... yes, actually", {"accommodating": 5}),
    ]),
    "trap", True, "accom_pattern_1", 0.4,
    tags=["conflict_resolution", "accommodating", "trap", "pattern"]))

questions.append(make_q("accommodating", "partner_perspective",
    "Someone who has hurt you describes you as 'so understanding.' How does that land?",
    opts([
        ("It feels good—being understanding is a strength", {"accommodating": 4}),
        ("It stings—'understanding' might mean 'easy to take advantage of'", {"accommodating": 4, "competing": 2}),
        ("Neutral—I am understanding, but I also have limits", {"collaborating": 3, "compromising": 2}),
        ("Irritated—I'd rather be described as 'fair' than 'understanding'", {"competing": 3, "collaborating": 2}),
    ]),
    "trap", True, "accom_understanding_1", 0.4,
    tags=["conflict_resolution", "accommodating", "trap", "identity"]))

questions.append(make_q("accommodating", "scenario",
    "Your boss assigns you work that should go to your colleague, who is underperforming. Do you:",
    opts([
        ("Do it without complaint—it needs to get done and you're capable", {"accommodating": 5}),
        ("Do it but have a private conversation with your boss about workload fairness", {"collaborating": 3, "competing": 3}),
        ("Suggest the work be split between you and the colleague as a development opportunity for them", {"collaborating": 4, "compromising": 2}),
        ("Decline and explain that it's not in your role—the colleague needs to step up", {"competing": 5}),
    ]),
    "consistency_check", False, "accom_workload_1", 0.7))

questions.append(make_q("accommodating", "behavioral_recall",
    "When was the last time you stood firm on something your partner or close friend wanted you to give in on?",
    opts([
        ("I can't remember a specific time—I usually find a way to make them happy", {"accommodating": 5}),
        ("Recently—I've been working on holding my ground more", {"accommodating": 2, "collaborating": 3}),
        ("It happens regularly—I know what matters to me", {"competing": 4}),
        ("Last week, but I felt terrible about it afterward", {"accommodating": 4, "competing": 2}),
    ]),
    "triangulation", False, "accom_standfirm_1", 0.6))

questions.append(make_q("accommodating", "forced_choice",
    "If you could only keep one, would you rather have respect or harmony?",
    opts([
        ("Harmony—life is too short for constant conflict", {"accommodating": 5}),
        ("Respect—without it, harmony is just compliance", {"competing": 5}),
    ]),
    "consistency_check", False, "accom_respect_1", 0.4, depth="light"))

questions.append(make_q("accommodating", "temporal",
    "Looking back at your most important relationships, do you see a pattern of losing yourself to keep the peace?",
    opts([
        ("Yes—it's something I'm actively working on", {"accommodating": 5}),
        ("In the past, yes. I've gotten better.", {"accommodating": 3, "collaborating": 2}),
        ("No—I've always maintained my sense of self in relationships", {"competing": 3, "collaborating": 2}),
        ("I'm not sure—maybe I don't see it because I'm still in it", {"accommodating": 4, "avoiding": 2}),
    ]),
    "trap", True, "accom_loseself_1", 0.3,
    tags=["conflict_resolution", "accommodating", "trap", "self_awareness"]))

questions.append(make_q("accommodating", "scenario",
    "A friend asks you to help them move on the only free Saturday you've had in weeks. You were planning to rest. What do you say?",
    opts([
        ("'Of course!'—they need help and you can rest another time", {"accommodating": 5}),
        ("'I can help for a few hours in the morning but need the afternoon'", {"compromising": 4}),
        ("'I can't this Saturday but I'm free next weekend if that works'", {"collaborating": 3, "competing": 2}),
        ("'I'm sorry, I really need this day for myself'", {"competing": 4}),
    ]),
    "triangulation", False, "accom_saturday_1", 0.7))

questions.append(make_q("accommodating", "somatic",
    "When someone thanks you for accommodating them, and you know you sacrificed something important to do so, what do you feel?",
    opts([
        ("Warm—their gratitude makes the sacrifice worth it", {"accommodating": 5}),
        ("Resentful underneath the smile—they should know what it cost you", {"accommodating": 3, "competing": 2}),
        ("Nothing special—I chose to do it, so there's nothing to feel conflicted about", {"collaborating": 3, "compromising": 2}),
        ("A mix of good and bad—appreciated but also a little used", {"accommodating": 4}),
    ]),
    "consistency_check", False, "accom_thanks_1", 0.5, depth="deep"))

# Validate counts
dim_counts = {}
type_counts = {}
tier_counts = {}
for q in questions:
    dim_counts[q["dimension"]] = dim_counts.get(q["dimension"], 0) + 1
    type_counts[q["question_type"]] = type_counts.get(q["question_type"], 0) + 1
    tier_counts[q["tier_role"]] = tier_counts.get(q["tier_role"], 0) + 1

print(f"Total: {len(questions)}")
print(f"Dimensions: {dim_counts}")
print(f"Types: {type_counts}")
print(f"Tiers: {tier_counts}")

with open("/Users/user/personal/sb/trueassess/priv/question_bank/conflict_resolution.json", "w") as f:
    json.dump(questions, f, indent=2)

print("Written to conflict_resolution.json")
