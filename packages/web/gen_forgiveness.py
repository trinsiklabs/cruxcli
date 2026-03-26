import json

assessment_id = "forgiveness_profile"
questions = []
uid_counter = 0

def make_uid():
    global uid_counter
    uid_counter += 1
    return f"fp_{uid_counter:03d}"

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
# CAPACITY (25 questions) — trait-level forgiveness capacity
# ============================================================

questions.append(make_q("capacity", "scenario",
    "A close friend reveals they've been gossiping about your personal struggles to mutual friends. They apologize sincerely when confronted. Six months later, where are you?",
    opts([
        ("We're fine—I forgave them fully. People make mistakes and the apology was genuine", {"capacity": 5}),
        ("We're friendly but there's a boundary now—I forgave but I'm more careful about what I share", {"capacity": 3}),
        ("I still feel a flicker of resentment when I see them, even though I said I forgave them", {"capacity": 2}),
        ("The friendship ended—that kind of betrayal can't be undone by words", {"capacity": 1}),
    ]),
    "core", False, "cap_core_1", 0.7, depth="light"))

questions.append(make_q("capacity", "somatic",
    "When you think about someone who wronged you years ago—not a major trauma, just a meaningful betrayal—what does your body do?",
    opts([
        ("Nothing—the emotional charge has fully dissipated", {"capacity": 5}),
        ("A slight tightening somewhere—a ghost of the original hurt", {"capacity": 3}),
        ("Heat, tension, quickened heart—the body remembers even if I 'forgave'", {"capacity": 2}),
        ("I feel sick or angry like it happened yesterday", {"capacity": 1}),
    ]),
    "triangulation", False, "cap_somatic_1", 0.7, depth="deep"))

questions.append(make_q("capacity", "partner_perspective",
    "If your closest friends rated your ability to let go of grievances, they'd say:",
    opts([
        ("You're exceptionally forgiving—sometimes too much so", {"capacity": 5}),
        ("You forgive most things but have a line that once crossed, there's no coming back", {"capacity": 3}),
        ("You hold grudges longer than you realize", {"capacity": 2}),
        ("You never fully let anything go—you file it away for future reference", {"capacity": 1}),
    ]),
    "consistency_check", False, "cap_friends_1", 0.6))

questions.append(make_q("capacity", "temporal",
    "Think about the person who hurt you most. Has your level of forgiveness toward them changed over the past 5 years?",
    opts([
        ("Yes—I've moved from anger to understanding to something close to peace", {"capacity": 5}),
        ("Somewhat—the intensity has faded but I wouldn't say I've forgiven them", {"capacity": 3}),
        ("No—the hurt is as fresh as it was", {"capacity": 1}),
        ("I go back and forth—some days I've forgiven them, other days I haven't", {"capacity": 2}),
    ]),
    "triangulation", False, "cap_most_hurt_1", 0.8, depth="deep"))

questions.append(make_q("capacity", "behavioral_recall",
    "How many people are you currently not speaking to because of something they did?",
    opts([
        ("None—I'm on speaking terms with everyone in my life", {"capacity": 5}),
        ("One—there's a specific situation I haven't been able to get past", {"capacity": 3}),
        ("Two or three—I've had to cut people out to protect myself", {"capacity": 2}),
        ("Several—I've accumulated estrangements over the years", {"capacity": 1}),
    ]),
    "trap", True, "cap_estranged_1", 0.5,
    tags=[assessment_id, "capacity", "trap", "behavioral"]))

questions.append(make_q("capacity", "forced_choice",
    "Which statement resonates more: 'Forgiveness is a gift you give yourself' or 'Forgiveness without accountability is just enablement'?",
    opts([
        ("Forgiveness is a gift you give yourself", {"capacity": 5}),
        ("Forgiveness without accountability is just enablement", {"capacity": 2}),
    ]),
    "triangulation", False, "cap_philosophy_1", 0.5))

questions.append(make_q("capacity", "scenario",
    "A sibling who said terrible things about you at a family gathering later apologizes, blaming stress. This isn't the first time. Do you forgive?",
    opts([
        ("Yes—family relationships require persistent forgiveness", {"capacity": 5}),
        ("I accept the apology but I'm keeping a mental tally—there's a limit", {"capacity": 3}),
        ("Not really—the pattern tells me the apology is about their guilt, not my pain", {"capacity": 2}),
        ("I've already distanced myself from this person—repeated harm isn't forgivable through repeated apologies", {"capacity": 1}),
    ]),
    "consistency_check", False, "cap_pattern_1", 0.7))

questions.append(make_q("capacity", "somatic",
    "When someone who hurt you asks for forgiveness and you say 'I forgive you,' does your body agree with your words?",
    opts([
        ("Yes—I feel a genuine release, like setting down something heavy", {"capacity": 5}),
        ("Mostly—there's some residual tension but the intent is genuine", {"capacity": 4}),
        ("No—my body stays guarded even when my words are generous", {"capacity": 2}),
        ("I've learned not to say it until I mean it, so if I say it, I mean it", {"capacity": 4}),
    ]),
    "triangulation", False, "cap_body_words_1", 0.7, depth="deep"))

questions.append(make_q("capacity", "temporal",
    "Is there a type of transgression that you simply cannot forgive, regardless of context or apology?",
    opts([
        ("No—I believe any transgression can be forgiven given enough time and genuine change", {"capacity": 5}),
        ("One or two things—infidelity, abuse, or betrayal of a child", {"capacity": 3}),
        ("Several—I have firm moral lines and crossing them ends things permanently", {"capacity": 2}),
        ("Many things—I have high standards and low tolerance for being wronged", {"capacity": 1}),
    ]),
    "trap", True, "cap_unforgivable_1", 0.4,
    tags=[assessment_id, "capacity", "trap", "absolutism"]))

questions.append(make_q("capacity", "behavioral_recall",
    "Think about the last time you forgave someone. Did the forgiveness come with conditions?",
    opts([
        ("No conditions—forgiveness was freely given", {"capacity": 5}),
        ("Implicit conditions—I forgave but certain behaviors would re-open the wound", {"capacity": 3}),
        ("Explicit conditions—I told them what needed to change for the forgiveness to hold", {"capacity": 3}),
        ("I'm not sure I've fully forgiven anyone recently—I've more just moved on", {"capacity": 2}),
    ]),
    "consistency_check", False, "cap_conditions_1", 0.6))

questions.append(make_q("capacity", "partner_perspective",
    "Your romantic partner (current or most recent) would say your forgiveness is:",
    opts([
        ("Deep and genuine—when I forgive, they feel it completely", {"capacity": 5}),
        ("Surface-level—I say I forgive but they can tell I'm still holding something", {"capacity": 2}),
        ("Slow but real—it takes me a while but once I forgive, I mean it", {"capacity": 4}),
        ("Conditional—they always feel like they're on probation after a mistake", {"capacity": 2}),
    ]),
    "trap", True, "cap_partner_says_1", 0.4,
    tags=[assessment_id, "capacity", "trap", "relational"]))

questions.append(make_q("capacity", "scenario",
    "A coworker accidentally deletes your work. No malice, just carelessness. They're devastated. How quickly do you genuinely forgive?",
    opts([
        ("Immediately—accidents happen and their guilt is punishment enough", {"capacity": 5}),
        ("By the end of the day—I need to process the frustration but it doesn't take long", {"capacity": 4}),
        ("A few days—I say 'it's fine' but I'm irritated every time I have to redo the work", {"capacity": 2}),
        ("I hold it against them—carelessness IS the problem", {"capacity": 1}),
    ]),
    "triangulation", False, "cap_accident_1", 0.7))

questions.append(make_q("capacity", "forced_choice",
    "Someone who betrayed your trust 10 years ago has genuinely transformed as a person. They reach out. Do you:",
    opts([
        ("Welcome the reconnection—people change and holding grudges serves no one", {"capacity": 5}),
        ("Respond cautiously—I'm open but will need to see the change demonstrated", {"capacity": 3}),
        ("Decline—the damage was done and re-opening that door serves them, not me", {"capacity": 1}),
        ("Respond but make it clear the past is acknowledged, not erased", {"capacity": 3}),
    ]),
    "triangulation", False, "cap_transformation_1", 0.7))

questions.append(make_q("capacity", "behavioral_recall",
    "Do you keep a mental ledger of wrongs people have done to you?",
    opts([
        ("No—I genuinely don't track grievances", {"capacity": 5}),
        ("Not deliberately, but certain things surface during arguments: 'Remember when you...'", {"capacity": 2}),
        ("Yes—I remember everything, even if I've officially forgiven it", {"capacity": 1}),
        ("I used to but I've been actively working to let go of that habit", {"capacity": 3}),
    ]),
    "trap", True, "cap_ledger_1", 0.3,
    tags=[assessment_id, "capacity", "trap", "record_keeping"]))

questions.append(make_q("capacity", "somatic",
    "When you hear a song, visit a place, or encounter a smell associated with someone who hurt you, what does your body do?",
    opts([
        ("A bittersweet wave—I can hold both the good memory and the hurt without either dominating", {"capacity": 5}),
        ("A jolt of negative emotion that passes quickly", {"capacity": 3}),
        ("My body floods with the original anger or hurt as if no time has passed", {"capacity": 1}),
        ("I avoid those triggers entirely—I've restructured my life around not encountering them", {"capacity": 1}),
    ]),
    "consistency_check", False, "cap_trigger_1", 0.7, depth="deep"))

questions.append(make_q("capacity", "scenario",
    "Your parent did something in your childhood that you now understand caused real harm, though they likely didn't intend it. Where are you with forgiving them?",
    opts([
        ("I've forgiven them fully—understanding their limitations allowed genuine compassion", {"capacity": 5}),
        ("I understand but haven't fully forgiven—understanding doesn't erase impact", {"capacity": 3}),
        ("I'm angry—intention doesn't matter when the damage is real", {"capacity": 2}),
        ("I haven't thought about it enough to know where I stand", {"capacity": 2}),
    ]),
    "triangulation", False, "cap_parent_1", 0.8, depth="deep"))

questions.append(make_q("capacity", "temporal",
    "When you think about all the people who have wronged you throughout your life, does the total weight feel manageable or crushing?",
    opts([
        ("Manageable—I've genuinely let most of it go", {"capacity": 5}),
        ("Manageable because I've cut those people out, not because I've forgiven them", {"capacity": 2}),
        ("Heavier than I'd like to admit", {"capacity": 2}),
        ("I don't really track an aggregate—I deal with each situation individually", {"capacity": 4}),
    ]),
    "trap", True, "cap_total_weight_1", 0.4,
    tags=[assessment_id, "capacity", "trap", "accumulated"]))

questions.append(make_q("capacity", "partner_perspective",
    "Would people describe you as someone who gives second chances?",
    opts([
        ("Absolutely—sometimes to a fault", {"capacity": 5}),
        ("For most things, yes—but not for everything", {"capacity": 3}),
        ("Selectively—I give second chances to people who've earned my trust", {"capacity": 3}),
        ("Rarely—I believe people show you who they are the first time", {"capacity": 1}),
    ]),
    "consistency_check", False, "cap_second_chance_1", 0.6))

questions.append(make_q("capacity", "behavioral_recall",
    "In the past year, has unforgiveness toward someone cost you sleep?",
    opts([
        ("Yes—I've lain awake replaying what they did", {"capacity": 1}),
        ("Once or twice, briefly", {"capacity": 3}),
        ("No—I don't let grievances into my sleep", {"capacity": 5}),
        ("Not sleep specifically, but it's occupied my mind during the day", {"capacity": 2}),
    ]),
    "triangulation", False, "cap_sleep_1", 0.6))

questions.append(make_q("capacity", "forced_choice",
    "Do you believe forgiveness requires the other person to apologize first?",
    opts([
        ("No—forgiveness is an internal process that doesn't depend on their behavior", {"capacity": 5}),
        ("It helps but isn't required—I can forgive without an apology", {"capacity": 4}),
        ("I need at least acknowledgment—forgiving someone who doesn't think they did anything wrong feels impossible", {"capacity": 2}),
        ("Yes—without an apology, what I'm doing is just 'acceptance,' not forgiveness", {"capacity": 2}),
    ]),
    "core", False, "cap_core_2", 0.5, depth="light"))

questions.append(make_q("capacity", "scenario",
    "You discover that a friend defended you behind your back against someone who was criticizing you. This is the same friend who hurt you last year. Does this change your unforgiveness?",
    opts([
        ("Yes—it softens the remaining resentment and shows me who they really are", {"capacity": 5}),
        ("It helps but one good act doesn't erase the original harm", {"capacity": 3}),
        ("It confuses me—now I don't know how to categorize this person", {"capacity": 2}),
        ("No—a good act doesn't retroactively make the bad one okay", {"capacity": 1}),
    ]),
    "triangulation", False, "cap_redemption_1", 0.7))

questions.append(make_q("capacity", "somatic",
    "When you choose to forgive someone, is there a physical sensation of release?",
    opts([
        ("Yes—it's distinct: something loosens in my chest or belly", {"capacity": 5}),
        ("Sometimes—if the forgiveness is genuine and deep", {"capacity": 4}),
        ("No—forgiveness is a cognitive decision for me, not a felt experience", {"capacity": 3}),
        ("I don't think I've experienced a genuine moment of full forgiveness to answer this", {"capacity": 1}),
    ]),
    "consistency_check", False, "cap_release_1", 0.7, depth="deep"))

questions.append(make_q("capacity", "temporal",
    "Has there been a forgiveness that surprised you—where you forgave something you never thought you could?",
    opts([
        ("Yes—and it taught me my capacity for forgiveness is larger than I thought", {"capacity": 5}),
        ("Yes—but it took years and specific circumstances to get there", {"capacity": 3}),
        ("No—my boundaries around the unforgivable have held firm", {"capacity": 2}),
        ("I'm still waiting to see if that's possible for me", {"capacity": 2}),
    ]),
    "triangulation", False, "cap_surprise_1", 0.7))

questions.append(make_q("capacity", "behavioral_recall",
    "When you hear stories of extraordinary forgiveness (parents forgiving their child's murderer, etc.), what is your honest reaction?",
    opts([
        ("Awe and aspiration—I hope I could find that depth of grace", {"capacity": 5}),
        ("Respect but skepticism—I wonder if it's genuine or performative", {"capacity": 3}),
        ("Discomfort—forgiving the unforgivable feels like betraying the victim", {"capacity": 2}),
        ("Admiration but certainty that I could never do that", {"capacity": 1}),
    ]),
    "trap", True, "cap_extraordinary_1", 0.5,
    tags=[assessment_id, "capacity", "trap", "aspiration_vs_reality"]))

# ============================================================
# LOAD (25 questions) — current unforgiveness load
# ============================================================

questions.append(make_q("load", "scenario",
    "If you sat down right now and listed every person you haven't fully forgiven, how long would the list be?",
    opts([
        ("Zero or one—I'm relatively clear of unforgiveness", {"load": 5}),
        ("Two to three—a manageable number of unresolved situations", {"load": 3}),
        ("Four to seven—more than I'd like to admit", {"load": 2}),
        ("Eight or more—I'm carrying a lot of unresolved hurt", {"load": 1}),
    ]),
    "core", False, "load_core_1", 0.5, depth="light"))

questions.append(make_q("load", "somatic",
    "Right now, without thinking too hard about it—does your body feel like it's carrying emotional weight from unresolved grievances?",
    opts([
        ("No—I feel relatively light and unencumbered", {"load": 5}),
        ("Maybe a little—there's something but it's manageable", {"load": 3}),
        ("Yes—I can feel the accumulated burden physically", {"load": 1}),
        ("I'm not sure—I've been carrying it so long I don't know what light feels like", {"load": 1}),
    ]),
    "triangulation", False, "load_body_1", 0.7, depth="deep"))

questions.append(make_q("load", "partner_perspective",
    "If someone who knows you well listed the people you're still carrying resentment toward, how accurate would their list be?",
    opts([
        ("Very—I'm open about who I'm still working through", {"load": 3}),
        ("Partially—they'd know the big ones but miss the smaller simmering ones", {"load": 2}),
        ("They'd find nothing because there's nothing to list", {"load": 5}),
        ("They'd be shocked—I keep my resentments private", {"load": 1}),
    ]),
    "consistency_check", False, "load_visibility_1", 0.6))

questions.append(make_q("load", "temporal",
    "Over the past year, has your total unforgiveness load increased, decreased, or stayed the same?",
    opts([
        ("Decreased—I've been actively processing and releasing", {"load": 5}),
        ("Stayed the same—old wounds persist and new ones don't add much", {"load": 2}),
        ("Increased—new hurts have added to existing ones", {"load": 1}),
        ("I don't track this—I deal with things as they come", {"load": 3}),
    ]),
    "triangulation", False, "load_trajectory_1", 0.6))

questions.append(make_q("load", "behavioral_recall",
    "How many times in the past week have you replayed a grievance in your mind—even briefly?",
    opts([
        ("None—my mind doesn't cycle through old hurts", {"load": 5}),
        ("Once or twice—brief flashes that I can redirect", {"load": 3}),
        ("Several times—certain grievances are on a loop", {"load": 2}),
        ("Daily or more—I can't stop my mind from going there", {"load": 1}),
    ]),
    "trap", True, "load_replay_1", 0.5,
    tags=[assessment_id, "load", "trap", "rumination"]))

questions.append(make_q("load", "forced_choice",
    "If you could press a button that would erase all resentment you carry, would you press it?",
    opts([
        ("Yes, immediately—I'd love to be free of it", {"load": 1}),
        ("Yes, but with some sadness—my resentments feel like they protect me", {"load": 2}),
        ("No—my resentments are valid and I'm not ready to let them go", {"load": 1}),
        ("There's no need—I don't carry enough resentment for it to matter", {"load": 5}),
    ]),
    "triangulation", False, "load_button_1", 0.6))

questions.append(make_q("load", "scenario",
    "You're in therapy and the therapist asks you to name everyone you still harbor resentment toward. As you start listing, do you feel:",
    opts([
        ("Not much—the list is short and I'm at peace with most of it", {"load": 5}),
        ("A growing weight—each name adds to the heaviness in my chest", {"load": 2}),
        ("Surprise—the list is longer than I expected", {"load": 2}),
        ("Overwhelm—the accumulated unforgiveness feels enormous when laid out explicitly", {"load": 1}),
    ]),
    "consistency_check", False, "load_therapy_list_1", 0.7))

questions.append(make_q("load", "somatic",
    "When you encounter someone on your unforgiveness list unexpectedly (at the store, online, in conversation), what does your body do?",
    opts([
        ("Nothing particular—I've released enough that seeing them doesn't activate me", {"load": 5}),
        ("A brief tension that passes quickly—a flicker of old feeling", {"load": 3}),
        ("Full body activation—adrenaline, tension, the urge to leave or confront", {"load": 1}),
        ("I avoid all places and contexts where I might encounter them", {"load": 1}),
    ]),
    "triangulation", False, "load_encounter_1", 0.7, depth="deep"))

questions.append(make_q("load", "temporal",
    "How many of your current resentments are from the past 12 months versus older than that?",
    opts([
        ("Mostly recent—I resolve old ones but pick up new ones", {"load": 3}),
        ("Mostly old—I'm carrying things from years or decades ago", {"load": 1}),
        ("A mix of both—old wounds and new ones", {"load": 2}),
        ("I don't have current resentments of either type", {"load": 5}),
    ]),
    "consistency_check", False, "load_age_1", 0.6))

questions.append(make_q("load", "behavioral_recall",
    "How often do you bring up past hurts during current arguments with your partner?",
    opts([
        ("Never—past issues stay in the past", {"load": 5}),
        ("Rarely—only when a current situation genuinely parallels a past one", {"load": 4}),
        ("Sometimes—old hurts surface when I'm activated by new ones", {"load": 2}),
        ("Often—my partner has said I 'keep score' or 'bring up ancient history'", {"load": 1}),
    ]),
    "trap", True, "load_arguments_1", 0.4,
    tags=[assessment_id, "load", "trap", "pattern"]))

questions.append(make_q("load", "partner_perspective",
    "Your closest friend would say the resentment you carry is:",
    opts([
        ("Minimal—you're impressively unburdened", {"load": 5}),
        ("Normal—everyone has some, yours isn't excessive", {"load": 3}),
        ("Heavy—they worry about how much you're holding", {"load": 1}),
        ("Hidden—they suspect you carry more than you show", {"load": 2}),
    ]),
    "triangulation", False, "load_friend_assess_1", 0.6))

questions.append(make_q("load", "scenario",
    "You're cleaning house and find a letter or gift from someone who betrayed you. What do you do?",
    opts([
        ("Throw it away without much emotional charge—it's just an object now", {"load": 5}),
        ("Hold it for a moment, feel something, then put it away or discard it", {"load": 3}),
        ("Get flooded with emotion—the object reopens the wound", {"load": 1}),
        ("I already got rid of everything from that person", {"load": 2}),
    ]),
    "consistency_check", False, "load_object_1", 0.7))

questions.append(make_q("load", "forced_choice",
    "If you rated your current 'resentment level' like a phone battery (0% = none, 100% = consumed by it), where are you?",
    opts([
        ("0-10%—essentially clear", {"load": 5}),
        ("11-30%—some background resentment but it's manageable", {"load": 3}),
        ("31-60%—it takes up significant mental space", {"load": 2}),
        ("61%+—resentment is a dominant theme in my inner life", {"load": 1}),
    ]),
    "triangulation", False, "load_battery_1", 0.5))

questions.append(make_q("load", "somatic",
    "When you lie in bed at night and your mind wanders, does it go to unresolved grievances?",
    opts([
        ("No—my mind doesn't default to grievances", {"load": 5}),
        ("Occasionally—certain unresolved situations surface at night", {"load": 3}),
        ("Frequently—nighttime is when the resentment is loudest", {"load": 1}),
        ("I've learned to redirect but it tries to go there", {"load": 2}),
    ]),
    "triangulation", False, "load_nighttime_1", 0.6, depth="deep"))

questions.append(make_q("load", "behavioral_recall",
    "How many grudges have you actively released in the past year through intentional forgiveness work?",
    opts([
        ("Several—I've been deliberate about lightening my load", {"load": 4}),
        ("One or two", {"load": 3}),
        ("None—but my load hasn't grown either", {"load": 3}),
        ("None—and my load has grown", {"load": 1}),
    ]),
    "consistency_check", False, "load_released_1", 0.6))

questions.append(make_q("load", "temporal",
    "Is there someone you've been carrying resentment toward for more than 10 years?",
    opts([
        ("No—nothing that old is still active for me", {"load": 5}),
        ("One person—and I've made peace with the fact that I may never fully forgive them", {"load": 2}),
        ("Yes, several—some wounds are permanent", {"load": 1}),
        ("I had one but I've recently released it", {"load": 4}),
    ]),
    "trap", True, "load_decade_1", 0.5,
    tags=[assessment_id, "load", "trap", "longevity"]))

questions.append(make_q("load", "scenario",
    "Someone brings up the name of a person who hurt you deeply. You're in a group setting. What happens to you internally?",
    opts([
        ("Nothing much—I've processed that relationship", {"load": 5}),
        ("A flash of something—quickly managed—but noticeable", {"load": 3}),
        ("I physically stiffen or my face changes—and others might notice", {"load": 2}),
        ("I feel ambushed—the mention ruins my mood for the rest of the interaction", {"load": 1}),
    ]),
    "triangulation", False, "load_name_drop_1", 0.7))

questions.append(make_q("load", "partner_perspective",
    "Would a therapist who assessed you say that unforgiveness is a significant source of your stress or mental health burden?",
    opts([
        ("No—unforgiveness isn't a major factor in my stress", {"load": 5}),
        ("Possibly—it's one of several contributors", {"load": 3}),
        ("Probably yes—I suspect it's a bigger burden than I want to admit", {"load": 2}),
        ("Definitely—it's one of my primary emotional weights", {"load": 1}),
    ]),
    "trap", True, "load_therapist_1", 0.4,
    tags=[assessment_id, "load", "trap", "impact"]))

questions.append(make_q("load", "behavioral_recall",
    "When telling someone about your life, how often does the narrative include 'what [someone] did to me'?",
    opts([
        ("Rarely or never—my life story isn't organized around being wronged", {"load": 5}),
        ("Sometimes—certain formative events involved being hurt", {"load": 3}),
        ("Frequently—key chapters of my life are defined by what others did to me", {"load": 1}),
        ("I actively choose not to tell those stories, even though they're a big part of my experience", {"load": 2}),
    ]),
    "consistency_check", False, "load_narrative_1", 0.5))

questions.append(make_q("load", "forced_choice",
    "How much mental energy per day would you estimate you spend on unresolved resentments?",
    opts([
        ("Nearly zero—it's not a feature of my daily mental life", {"load": 5}),
        ("A few minutes—brief flares that I manage", {"load": 3}),
        ("Thirty minutes to an hour—more than I'd like", {"load": 2}),
        ("Hours—it's a constant background process", {"load": 1}),
    ]),
    "triangulation", False, "load_energy_1", 0.5))

questions.append(make_q("load", "scenario",
    "A mutual friend tries to mediate between you and someone you resent. They say the other person wants to reconcile. What's your first reaction?",
    opts([
        ("Openness—I'd welcome the chance to resolve this", {"load": 4}),
        ("Caution—I'd need more information about what 'reconcile' means to them", {"load": 3}),
        ("Resistance—I don't want that person back in my life", {"load": 1}),
        ("Anger at the mutual friend—this isn't their business and they're putting me in an uncomfortable position", {"load": 1}),
    ]),
    "triangulation", False, "load_mediation_1", 0.7))

questions.append(make_q("load", "temporal",
    "If you compared your unforgiveness load today to when it was at its worst, what percentage of the peak are you at?",
    opts([
        ("Under 10%—I've done significant forgiveness work", {"load": 5}),
        ("25-40%—lighter than my worst but still carrying things", {"load": 3}),
        ("50-75%—I'm still in the thick of it", {"load": 2}),
        ("Near peak—I'm at or close to maximum unforgiveness load", {"load": 1}),
    ]),
    "consistency_check", False, "load_peak_compare_1", 0.5))

questions.append(make_q("load", "somatic",
    "If unforgiveness had a physical location in your body, where would it be?",
    opts([
        ("Nowhere specific—I don't somaticize resentment", {"load": 5}),
        ("Chest—a tightness or heaviness I can sometimes feel", {"load": 2}),
        ("Stomach—a knot or nausea when I think about certain people", {"load": 2}),
        ("Shoulders/jaw—chronic tension that I suspect is related to what I'm carrying", {"load": 1}),
    ]),
    "triangulation", False, "load_location_1", 0.7, depth="deep"))

questions.append(make_q("load", "behavioral_recall",
    "How often do you fantasize about confronting, punishing, or gaining vindication over someone who wronged you?",
    opts([
        ("Never or almost never", {"load": 5}),
        ("Occasionally—a passing thought that I dismiss", {"load": 3}),
        ("Regularly—I have recurring revenge or confrontation fantasies", {"load": 1}),
        ("I used to frequently but I've mostly stopped", {"load": 3}),
    ]),
    "trap", True, "load_revenge_1", 0.4,
    tags=[assessment_id, "load", "trap", "revenge"]))

# ============================================================
# SELF_OTHER_ASYMMETRY (25 questions)
# ============================================================

questions.append(make_q("self_other_asymmetry", "scenario",
    "You make a significant mistake at work that affects a colleague. They make a similar mistake that affects you. How do your reactions compare?",
    opts([
        ("I'm harder on myself—I should know better, but their mistake is understandable", {"self_other_asymmetry": 2, "capacity": 3}),
        ("I'm harder on them—my mistake had reasons, theirs was careless", {"self_other_asymmetry": 4}),
        ("About the same—mistakes are mistakes regardless of who makes them", {"self_other_asymmetry": 3}),
        ("I genuinely don't know—I've never compared the two", {"self_other_asymmetry": 3}),
    ]),
    "core", False, "soa_core_1", 0.6, depth="light"))

questions.append(make_q("self_other_asymmetry", "somatic",
    "When you recall your own worst mistakes, does your body respond differently than when you recall others' worst offenses against you?",
    opts([
        ("My own mistakes trigger more shame—a sinking, hot feeling that's worse than anger at others", {"self_other_asymmetry": 2}),
        ("Others' offenses trigger more activation—my own mistakes I've processed better", {"self_other_asymmetry": 4}),
        ("The intensity is similar but the quality differs—shame vs. anger", {"self_other_asymmetry": 3}),
        ("Neither activates me much anymore", {"self_other_asymmetry": 3}),
    ]),
    "triangulation", False, "soa_body_compare_1", 0.7, depth="deep"))

questions.append(make_q("self_other_asymmetry", "partner_perspective",
    "The people closest to you would say you're hardest on:",
    opts([
        ("Yourself—you beat yourself up over mistakes way more than you hold grudges against others", {"self_other_asymmetry": 1}),
        ("Others—you forgive yourself easily but hold others to a higher standard", {"self_other_asymmetry": 5}),
        ("Both equally—you're either forgiving across the board or strict across the board", {"self_other_asymmetry": 3}),
        ("It depends—you forgive others for some things but not yourself, and vice versa", {"self_other_asymmetry": 3}),
    ]),
    "consistency_check", False, "soa_hardest_on_1", 0.5))

questions.append(make_q("self_other_asymmetry", "temporal",
    "Think about a mistake you made 5 years ago. Have you fully forgiven yourself? Now think about something someone did to you 5 years ago. Have you fully forgiven them? Compare.",
    opts([
        ("I forgave them faster than I forgave myself", {"self_other_asymmetry": 1}),
        ("I forgave myself faster than I forgave them", {"self_other_asymmetry": 5}),
        ("Both took about the same time", {"self_other_asymmetry": 3}),
        ("I haven't fully forgiven either", {"self_other_asymmetry": 3}),
    ]),
    "triangulation", False, "soa_comparison_1", 0.7))

questions.append(make_q("self_other_asymmetry", "behavioral_recall",
    "When you hurt someone and when someone hurts you—which keeps you up at night more?",
    opts([
        ("When I hurt someone—guilt is worse than grievance for me", {"self_other_asymmetry": 1}),
        ("When someone hurts me—I ruminate more on being wronged", {"self_other_asymmetry": 5}),
        ("Both equally", {"self_other_asymmetry": 3}),
        ("Neither—I sleep fine regardless", {"self_other_asymmetry": 3}),
    ]),
    "trap", True, "soa_sleep_1", 0.5,
    tags=[assessment_id, "self_other_asymmetry", "trap", "direction"]))

questions.append(make_q("self_other_asymmetry", "forced_choice",
    "Which feels more familiar: 'I can't forgive myself for what I did' or 'I can't forgive them for what they did'?",
    opts([
        ("Can't forgive myself—self-condemnation is my dominant pattern", {"self_other_asymmetry": 1}),
        ("Can't forgive them—resentment toward others is more prominent", {"self_other_asymmetry": 5}),
        ("Both feel equally familiar", {"self_other_asymmetry": 3}),
        ("Neither—I'm reasonably forgiving in both directions", {"self_other_asymmetry": 3}),
    ]),
    "core", False, "soa_core_2", 0.4, depth="light"))

questions.append(make_q("self_other_asymmetry", "scenario",
    "You lie to protect someone's feelings. Later you discover a friend lied to you to protect yours. Your reaction to their lie versus your own:",
    opts([
        ("My lie was justified; theirs feels like a betrayal", {"self_other_asymmetry": 5}),
        ("Their lie was understandable; mine keeps me up at night with guilt", {"self_other_asymmetry": 1}),
        ("Both were well-intentioned—I judge them the same", {"self_other_asymmetry": 3}),
        ("Both were wrong, but I'm more critical of my own because I know my true intentions", {"self_other_asymmetry": 2}),
    ]),
    "triangulation", False, "soa_lie_compare_1", 0.6))

questions.append(make_q("self_other_asymmetry", "somatic",
    "When you remember something you did that hurt someone (even years ago), does your body produce shame? When you remember what someone did to you, does your body produce anger? Which is more intense?",
    opts([
        ("Shame is significantly more intense—I'm harder on myself physically", {"self_other_asymmetry": 1}),
        ("Anger is significantly more intense—other people's wrongs hit harder", {"self_other_asymmetry": 5}),
        ("They're roughly equal in intensity", {"self_other_asymmetry": 3}),
        ("Neither is very intense anymore", {"self_other_asymmetry": 3}),
    ]),
    "consistency_check", False, "soa_shame_anger_1", 0.6, depth="deep"))

questions.append(make_q("self_other_asymmetry", "temporal",
    "How long have you been carrying your oldest self-grudge versus your oldest other-grudge?",
    opts([
        ("Self-grudge is older—I've held things against myself longer than I've held things against anyone else", {"self_other_asymmetry": 1}),
        ("Other-grudge is older—I forgive myself faster than I forgive others", {"self_other_asymmetry": 5}),
        ("About the same vintage", {"self_other_asymmetry": 3}),
        ("I don't carry either for very long", {"self_other_asymmetry": 3}),
    ]),
    "triangulation", False, "soa_oldest_1", 0.7))

questions.append(make_q("self_other_asymmetry", "behavioral_recall",
    "When a friend beats themselves up over a mistake, do you say 'be easier on yourself' while secretly holding yourself to a harsher standard?",
    opts([
        ("Yes—I'm consistently more compassionate to others than to myself", {"self_other_asymmetry": 1}),
        ("No—I apply the same compassion to myself", {"self_other_asymmetry": 3}),
        ("I'm actually harder on friends—I hold everyone to high standards including myself", {"self_other_asymmetry": 4}),
        ("Depends on the mistake—some things I can forgive in others but not myself, and vice versa", {"self_other_asymmetry": 3}),
    ]),
    "trap", True, "soa_double_standard_1", 0.3,
    tags=[assessment_id, "self_other_asymmetry", "trap", "double_standard"]))

questions.append(make_q("self_other_asymmetry", "partner_perspective",
    "A therapist would describe your forgiveness asymmetry as:",
    opts([
        ("Significant self-punishment pattern—forgives others readily, punishes self endlessly", {"self_other_asymmetry": 1}),
        ("Other-blaming pattern—quick to forgive self, slow to forgive others", {"self_other_asymmetry": 5}),
        ("Relatively balanced—treats self and others with similar standards", {"self_other_asymmetry": 3}),
        ("Contextual—the asymmetry shifts depending on the domain (work vs. relationships, etc.)", {"self_other_asymmetry": 3}),
    ]),
    "consistency_check", False, "soa_therapist_1", 0.5))

questions.append(make_q("self_other_asymmetry", "scenario",
    "You and a colleague both miss the same deadline for the same reason. How does your internal dialogue differ between the two cases?",
    opts([
        ("For me: 'You're irresponsible, this is inexcusable.' For them: 'Things happen, we'll catch up.'", {"self_other_asymmetry": 1}),
        ("For them: 'They should have planned better.' For me: 'Understandable, it was a tough week.'", {"self_other_asymmetry": 5}),
        ("Same response for both—either both understanding or both critical", {"self_other_asymmetry": 3}),
        ("I'm critical of both but express compassion to them while beating myself up silently", {"self_other_asymmetry": 2}),
    ]),
    "triangulation", False, "soa_deadline_1", 0.6))

questions.append(make_q("self_other_asymmetry", "forced_choice",
    "If you could instantly release all self-criticism OR all resentment toward others (but not both), which would free up more mental energy?",
    opts([
        ("Releasing self-criticism—I carry more weight from my own failures than from others' offenses", {"self_other_asymmetry": 1}),
        ("Releasing resentment—the grudges I carry against others are the heavier burden", {"self_other_asymmetry": 5}),
        ("Hard to say—they're roughly equal", {"self_other_asymmetry": 3}),
        ("Neither is a significant burden for me", {"self_other_asymmetry": 3}),
    ]),
    "triangulation", False, "soa_release_1", 0.5))

questions.append(make_q("self_other_asymmetry", "behavioral_recall",
    "How quickly do you forgive yourself for saying something hurtful, versus how quickly you forgive someone who said something hurtful to you?",
    opts([
        ("I forgive others faster—I hold my own hurtful words against myself for much longer", {"self_other_asymmetry": 1}),
        ("I forgive myself faster—when I say something hurtful I can contextualize it, but when others do I take it personally", {"self_other_asymmetry": 5}),
        ("About the same speed for both", {"self_other_asymmetry": 3}),
        ("Slowly for both—hurtful words linger regardless of direction", {"self_other_asymmetry": 3}),
    ]),
    "consistency_check", False, "soa_hurtful_words_1", 0.6))

questions.append(make_q("self_other_asymmetry", "somatic",
    "When you've done something wrong and been called out, where does the shame live compared to where anger lives when someone wrongs you?",
    opts([
        ("Shame goes to my gut and stays longer—it's a deeper, harder feeling", {"self_other_asymmetry": 1}),
        ("Anger is hotter and sharper—being wronged activates me more than shame does", {"self_other_asymmetry": 5}),
        ("They're felt in different places but with similar intensity", {"self_other_asymmetry": 3}),
        ("I don't somaticize either strongly enough to map them", {"self_other_asymmetry": 3}),
    ]),
    "triangulation", False, "soa_shame_location_1", 0.7, depth="deep"))

questions.append(make_q("self_other_asymmetry", "temporal",
    "Over your lifetime, has your self/other forgiveness ratio changed?",
    opts([
        ("I've gotten better at forgiving myself—used to be much harder on me than others", {"self_other_asymmetry": 2}),
        ("I've gotten better at forgiving others—used to hold grudges more than self-judge", {"self_other_asymmetry": 4}),
        ("Both have improved together", {"self_other_asymmetry": 3}),
        ("Not much has changed—the asymmetry persists", {"self_other_asymmetry": 2}),
    ]),
    "triangulation", False, "soa_evolution_1", 0.7))

questions.append(make_q("self_other_asymmetry", "scenario",
    "You break a promise to a friend. They break a promise to you. How do you handle the two situations?",
    opts([
        ("I apologize profusely and beat myself up for mine. For theirs, I say 'it's fine' and genuinely mean it.", {"self_other_asymmetry": 1}),
        ("I excuse mine with context. For theirs, I'm quietly resentful.", {"self_other_asymmetry": 5}),
        ("I hold both to the same standard—either both are forgivable or neither is.", {"self_other_asymmetry": 3}),
        ("I'm disappointed in both but move on from both at the same pace.", {"self_other_asymmetry": 3}),
    ]),
    "trap", True, "soa_promise_1", 0.5,
    tags=[assessment_id, "self_other_asymmetry", "trap", "comparison"]))

questions.append(make_q("self_other_asymmetry", "partner_perspective",
    "Does your inner critic apply the same standard to you that you apply to others?",
    opts([
        ("No—my inner critic is far harsher than my outer critic", {"self_other_asymmetry": 1}),
        ("No—I'm more lenient with myself than I am with others", {"self_other_asymmetry": 5}),
        ("Yes—same standard in both directions", {"self_other_asymmetry": 3}),
        ("My inner critic varies—sometimes harsh, sometimes generous, just like with others", {"self_other_asymmetry": 3}),
    ]),
    "consistency_check", False, "soa_inner_critic_1", 0.5))

questions.append(make_q("self_other_asymmetry", "behavioral_recall",
    "When you look at your relationship history, do you tend to blame yourself or others for what went wrong?",
    opts([
        ("Mostly myself—I'm the common denominator and I know my flaws", {"self_other_asymmetry": 1}),
        ("Mostly others—I chose poorly or they failed to meet me halfway", {"self_other_asymmetry": 5}),
        ("A balanced assessment—both parties contributed to failures", {"self_other_asymmetry": 3}),
        ("It depends on the relationship—in some I was the problem, in others they were", {"self_other_asymmetry": 3}),
    ]),
    "trap", True, "soa_relationship_blame_1", 0.4,
    tags=[assessment_id, "self_other_asymmetry", "trap", "blame_direction"]))

questions.append(make_q("self_other_asymmetry", "scenario",
    "A friend confides they cheated on their partner. Six months later, you find yourself in a similar temptation. How does your moral framework handle the parallel?",
    opts([
        ("I judged my friend but find myself rationalizing when it's me—I'm more forgiving of myself in practice", {"self_other_asymmetry": 5}),
        ("I was compassionate toward my friend but would punish myself mercilessly if I did the same", {"self_other_asymmetry": 1}),
        ("Same standard—either both are forgivable or neither is", {"self_other_asymmetry": 3}),
        ("The situations are too different to compare—context changes everything", {"self_other_asymmetry": 4}),
    ]),
    "triangulation", False, "soa_cheating_1", 0.6))

questions.append(make_q("self_other_asymmetry", "forced_choice",
    "Complete this: 'When I make a mistake, I deserve ____. When others make a mistake, they deserve ____.'",
    opts([
        ("Consequences; compassion", {"self_other_asymmetry": 1}),
        ("Understanding; accountability", {"self_other_asymmetry": 5}),
        ("Grace; grace", {"self_other_asymmetry": 3}),
        ("Accountability; accountability", {"self_other_asymmetry": 3}),
    ]),
    "core", False, "soa_core_3", 0.4, depth="light"))

questions.append(make_q("self_other_asymmetry", "temporal",
    "Think about your most embarrassing moment and someone else's most egregious offense against you. Which do you think about more often?",
    opts([
        ("My embarrassment—I revisit my own failures more than others' offenses", {"self_other_asymmetry": 1}),
        ("Their offense—what they did to me is more present in my mind", {"self_other_asymmetry": 5}),
        ("About equally", {"self_other_asymmetry": 3}),
        ("Neither—I don't dwell on either", {"self_other_asymmetry": 3}),
    ]),
    "triangulation", False, "soa_frequency_1", 0.6))

questions.append(make_q("self_other_asymmetry", "behavioral_recall",
    "How do you respond when someone else forgives you easily for something you can't forgive yourself for?",
    opts([
        ("Grateful but it doesn't help—their forgiveness can't replace my own", {"self_other_asymmetry": 1}),
        ("It helps me move on—if they've forgiven me, I should forgive myself", {"self_other_asymmetry": 3}),
        ("Confused—why are they letting me off the hook?", {"self_other_asymmetry": 2}),
        ("This scenario doesn't resonate—I don't typically struggle with self-forgiveness more than other-forgiveness", {"self_other_asymmetry": 4}),
    ]),
    "consistency_check", False, "soa_others_forgive_1", 0.6))

questions.append(make_q("self_other_asymmetry", "somatic",
    "Self-compassion practice: when you place your hand on your heart and say 'I forgive myself,' versus saying 'I forgive you' to someone who hurt you—which feels more genuine?",
    opts([
        ("Forgiving others feels natural; self-forgiveness feels performative or hollow", {"self_other_asymmetry": 1}),
        ("Self-forgiveness feels natural; forgiving others is where I get stuck", {"self_other_asymmetry": 5}),
        ("Both feel equally genuine (or equally difficult)", {"self_other_asymmetry": 3}),
        ("I haven't tried this kind of practice", {"self_other_asymmetry": 3}),
    ]),
    "triangulation", False, "soa_practice_1", 0.7, depth="deep"))

# ============================================================
# STAGE (25 questions) — where in the forgiveness process
# ============================================================

questions.append(make_q("stage", "scenario",
    "Think about your most active unforgiveness right now. When you think about what happened, what's the dominant feeling?",
    opts([
        ("Denial—'it wasn't that bad' or 'I should be over this by now'", {"stage": 1}),
        ("Anger—'how could they do this to me'", {"stage": 2}),
        ("Bargaining—'if only they'd apologize properly' or 'if only I could understand why'", {"stage": 3}),
        ("Grief—sadness about what was lost, without the heat of anger", {"stage": 4}),
    ]),
    "core", False, "stage_core_1", 0.6, depth="light"))

questions.append(make_q("stage", "somatic",
    "When the person who hurt you comes to mind, is the physical sensation more like fire (anger stage) or water (grief stage)?",
    opts([
        ("Fire—heat, tension, energy, the urge to act", {"stage": 2}),
        ("Water—tears, heaviness, sadness, the urge to withdraw", {"stage": 4}),
        ("Ice—numbness, detachment, nothing much", {"stage": 1}),
        ("Something calmer—warmth without heat, acceptance forming", {"stage": 5}),
    ]),
    "triangulation", False, "stage_element_1", 0.7, depth="deep"))

questions.append(make_q("stage", "partner_perspective",
    "If a therapist watched you discuss the person who hurt you most, they'd say you're in the stage of:",
    opts([
        ("Still minimizing or avoiding—you haven't fully acknowledged the impact", {"stage": 1}),
        ("Righteous anger—you know what they did and you're angry about it", {"stage": 2}),
        ("Negotiating with the pain—trying to find conditions under which you could forgive", {"stage": 3}),
        ("Mourning—you're grieving the relationship or the trust that was lost", {"stage": 4}),
    ]),
    "consistency_check", False, "stage_therapist_1", 0.5))

questions.append(make_q("stage", "temporal",
    "Has the quality of your unforgiveness changed over time, even if the amount hasn't? (e.g., hot anger cooling to cold resentment, or numbness warming to sadness)",
    opts([
        ("Yes—it's evolved through distinct phases", {"stage": 4}),
        ("Not really—it's been stuck at the same temperature", {"stage": 2}),
        ("It fluctuates—I cycle through stages rather than progressing", {"stage": 2}),
        ("It's mostly resolved—I'm in the final stages of release", {"stage": 5}),
    ]),
    "triangulation", False, "stage_evolution_1", 0.7))

questions.append(make_q("stage", "behavioral_recall",
    "When you talk about the person who hurt you, do you tell the story with heat (anger stage), with tears (grief stage), or with detachment (either early denial or late acceptance)?",
    opts([
        ("With heat—the anger is still alive in the telling", {"stage": 2}),
        ("With tears—the sadness surfaces when I tell it", {"stage": 4}),
        ("With detachment—either I haven't engaged with it or I've come through the other side", {"stage": 1}),
        ("With complexity—I can hold multiple feelings and tell a nuanced story", {"stage": 5}),
    ]),
    "consistency_check", False, "stage_telling_1", 0.6))

questions.append(make_q("stage", "forced_choice",
    "When you imagine the person who wronged you being happy and successful, do you feel:",
    opts([
        ("Anger or injustice—they don't deserve happiness after what they did", {"stage": 2}),
        ("Indifference or genuine gladness—their life is their life", {"stage": 5}),
        ("A complex mix—I wish them well in theory but it stings in practice", {"stage": 3}),
        ("Nothing—I don't think about them enough to have feelings about their happiness", {"stage": 1}),
    ]),
    "trap", True, "stage_success_1", 0.4,
    tags=[assessment_id, "stage", "trap", "goodwill"]))

questions.append(make_q("stage", "scenario",
    "The person who hurt you writes you a genuine, thorough apology letter. They take full responsibility and don't make excuses. What happens inside you?",
    opts([
        ("It wouldn't matter—words can't undo what they did", {"stage": 2}),
        ("It would help enormously—I've been waiting for acknowledgment", {"stage": 3}),
        ("I'd feel the grief more intensely—the apology would unlock the sadness I've been protecting with anger", {"stage": 3}),
        ("I'd feel peace—this is the final piece I needed to fully release it", {"stage": 5}),
    ]),
    "triangulation", False, "stage_apology_1", 0.7))

questions.append(make_q("stage", "somatic",
    "Is the physical sensation around your unforgiveness getting lighter over time, staying the same, or getting heavier?",
    opts([
        ("Getting lighter—I can feel myself moving through it", {"stage": 4}),
        ("Staying the same—it's been at this level for a while", {"stage": 2}),
        ("Getting heavier—as more time passes without resolution, it compounds", {"stage": 2}),
        ("It's already very light—I'm near the end of this process", {"stage": 5}),
    ]),
    "triangulation", False, "stage_trajectory_1", 0.7, depth="deep"))

questions.append(make_q("stage", "temporal",
    "Think about a forgiveness process you completed in the past. Can you identify the stage you're in with your current most active unforgiveness?",
    opts([
        ("Yes—I recognize the denial phase because I went through it before", {"stage": 1}),
        ("Yes—I'm in the anger phase and I know grief comes next", {"stage": 2}),
        ("Yes—I'm bargaining/negotiating and I know I need to let go of conditions", {"stage": 3}),
        ("Yes—I'm grieving and I know acceptance is close", {"stage": 4}),
    ]),
    "consistency_check", False, "stage_self_awareness_1", 0.6))

questions.append(make_q("stage", "behavioral_recall",
    "Do you find yourself asking 'why' about what they did? ('Why did they do this to me?' 'Why wasn't I enough?')",
    opts([
        ("Constantly—the 'why' is the loudest question", {"stage": 3}),
        ("Sometimes—but less than I used to", {"stage": 4}),
        ("I've moved past 'why'—I may never understand and that's okay", {"stage": 5}),
        ("I don't ask 'why'—I know exactly why and it doesn't require understanding, it requires anger", {"stage": 2}),
    ]),
    "triangulation", False, "stage_why_1", 0.6))

questions.append(make_q("stage", "partner_perspective",
    "A close friend who's watched you go through this unforgiveness process would say you're:",
    opts([
        ("Stuck—you've been in the same place for too long", {"stage": 2}),
        ("Moving—slowly but perceptibly working through it", {"stage": 3}),
        ("Almost through—they can see the light returning to your eyes", {"stage": 5}),
        ("In denial—you say you're fine but your behavior says otherwise", {"stage": 1}),
    ]),
    "trap", True, "stage_friend_assess_1", 0.5,
    tags=[assessment_id, "stage", "trap", "outside_view"]))

questions.append(make_q("stage", "scenario",
    "You dream about the person who hurt you. In the dream, what's the emotional tone?",
    opts([
        ("Angry or violent—I'm fighting them or they're hurting me again", {"stage": 2}),
        ("Negotiating—we're talking, trying to work something out", {"stage": 3}),
        ("Sad—I'm mourning what we had or what could have been", {"stage": 4}),
        ("Neutral or even warm—the old charge has dissipated", {"stage": 5}),
    ]),
    "triangulation", False, "stage_dream_1", 0.7, depth="deep"))

questions.append(make_q("stage", "forced_choice",
    "Which of these sentences could you say about the person who hurt you and genuinely mean it?",
    opts([
        ("'I hope they suffer the way I did'", {"stage": 2}),
        ("'I hope they learn from what they did'", {"stage": 3}),
        ("'I hope they find peace, even though they broke mine'", {"stage": 5}),
        ("'I don't think about what I hope for them at all'", {"stage": 1}),
    ]),
    "core", False, "stage_core_2", 0.4, depth="light"))

questions.append(make_q("stage", "somatic",
    "When you practice intentional compassion toward the person who hurt you (whether genuinely felt or aspirational), does your body resist or allow it?",
    opts([
        ("Strong resistance—my body rejects compassion for them", {"stage": 2}),
        ("Some resistance but it's softening—I can hold a moment of compassion before the walls go back up", {"stage": 3}),
        ("My body allows it—compassion feels authentic even though what they did was wrong", {"stage": 5}),
        ("I haven't tried—compassion toward them isn't something I've considered", {"stage": 1}),
    ]),
    "consistency_check", False, "stage_compassion_1", 0.7, depth="deep"))

questions.append(make_q("stage", "temporal",
    "If you mapped your forgiveness journey on a timeline, what percentage of the total process do you think you've completed?",
    opts([
        ("Under 25%—I'm still early in this", {"stage": 1}),
        ("25-50%—I've engaged with it but I'm far from done", {"stage": 2}),
        ("50-75%—more than halfway through", {"stage": 3}),
        ("Over 75%—I can see the end even if I'm not there yet", {"stage": 4}),
    ]),
    "triangulation", False, "stage_percentage_1", 0.5))

questions.append(make_q("stage", "behavioral_recall",
    "Can you talk about what happened without your voice changing (getting tighter, louder, quieter, or shaky)?",
    opts([
        ("No—my voice always betrays the emotion still present", {"stage": 2}),
        ("Mostly—with occasional breaks in composure", {"stage": 3}),
        ("Yes—I can tell the story with a steady voice now", {"stage": 5}),
        ("I avoid talking about it, so I don't know", {"stage": 1}),
    ]),
    "triangulation", False, "stage_voice_1", 0.6))

questions.append(make_q("stage", "scenario",
    "You unexpectedly see a photo of the person who hurt you looking happy with new people in their life. Immediate reaction?",
    opts([
        ("'They don't deserve happiness'—flash of anger", {"stage": 2}),
        ("'If only things had been different'—pang of what-if", {"stage": 3}),
        ("Sadness—for what was, not anger about what happened", {"stage": 4}),
        ("Something approaching genuine gladness—I want them to be well", {"stage": 5}),
    ]),
    "consistency_check", False, "stage_photo_1", 0.7))

questions.append(make_q("stage", "forced_choice",
    "If the person who hurt you died tomorrow, would your predominant feeling be:",
    opts([
        ("'Good'—they deserved consequences", {"stage": 2}),
        ("Complicated—anger mixed with regret that closure is now impossible", {"stage": 3}),
        ("Grief—I've already mourned the relationship but death adds finality", {"stage": 4}),
        ("Sadness for a life lost, regardless of what they did to me", {"stage": 5}),
    ]),
    "trap", True, "stage_death_1", 0.4,
    tags=[assessment_id, "stage", "trap", "mortality"]))

questions.append(make_q("stage", "behavioral_recall",
    "Have you tried to forgive this person before? If so, did it stick?",
    opts([
        ("I've never tried—I'm not there yet", {"stage": 1}),
        ("I've tried and it didn't stick—the anger came back", {"stage": 2}),
        ("I've tried and it partially stuck—some days are better than others", {"stage": 3}),
        ("Yes—this time it's real and lasting", {"stage": 5}),
    ]),
    "triangulation", False, "stage_previous_attempts_1", 0.6))

questions.append(make_q("stage", "partner_perspective",
    "If you're honest with yourself, the primary reason you haven't fully forgiven is:",
    opts([
        ("I haven't admitted to myself how much it hurt (denial)", {"stage": 1}),
        ("The anger protects me from the grief underneath (anger as defense)", {"stage": 2}),
        ("I'm waiting for something—an apology, understanding, justice (bargaining)", {"stage": 3}),
        ("I'm in the grief and it's just... taking time (grief in process)", {"stage": 4}),
    ]),
    "trap", True, "stage_honest_reason_1", 0.3,
    tags=[assessment_id, "stage", "trap", "self_knowledge"]))

questions.append(make_q("stage", "somatic",
    "When you imagine fully releasing this unforgiveness—completely letting go—does your body feel:",
    opts([
        ("Terror—the anger is armor and without it I'm exposed", {"stage": 2}),
        ("Yearning—I desperately want to get there but don't know how", {"stage": 3}),
        ("Warmth—I can almost taste the freedom", {"stage": 4}),
        ("I already feel mostly released—the last wisps are dissolving", {"stage": 5}),
    ]),
    "consistency_check", False, "stage_imagine_release_1", 0.7, depth="deep"))

questions.append(make_q("stage", "temporal",
    "When did you last feel a genuine shift in your forgiveness process—a moment where something softened or changed?",
    opts([
        ("Recently—within the past few weeks", {"stage": 4}),
        ("Months ago—I've plateaued since then", {"stage": 3}),
        ("I can't remember a shift—it's been static", {"stage": 2}),
        ("Just now, answering these questions, something is shifting", {"stage": 3}),
    ]),
    "triangulation", False, "stage_last_shift_1", 0.7))

# ============================================================
# ACTIVE_HOOKS (25 questions) — unresolved items that are live
# ============================================================

questions.append(make_q("active_hooks", "scenario",
    "You're at a dinner party and someone tells a story that closely parallels your betrayal experience. What happens?",
    opts([
        ("I listen with interest—their story is separate from mine", {"active_hooks": 5}),
        ("I feel a flicker of activation but manage it—my situation brushes against their story", {"active_hooks": 3}),
        ("I get hijacked—suddenly I'm reliving my own experience and can barely focus on them", {"active_hooks": 1}),
        ("I excuse myself—I can't be in this conversation without getting triggered", {"active_hooks": 1}),
    ]),
    "core", False, "ah_core_1", 0.7, depth="light"))

questions.append(make_q("active_hooks", "somatic",
    "How many 'trigger zones' do you currently have—specific topics, names, places, or situations that can hijack your emotional state?",
    opts([
        ("None—I'm not aware of active triggers", {"active_hooks": 5}),
        ("One or two—specific and manageable", {"active_hooks": 3}),
        ("Several—I navigate around multiple triggers regularly", {"active_hooks": 2}),
        ("Many—it feels like landmines everywhere", {"active_hooks": 1}),
    ]),
    "triangulation", False, "ah_zones_1", 0.6, depth="moderate"))

questions.append(make_q("active_hooks", "partner_perspective",
    "Your partner or close friend would say the number of 'things you can't talk about without getting activated' is:",
    opts([
        ("Zero or one—you're pretty even-keeled", {"active_hooks": 5}),
        ("A few—they know to avoid certain topics", {"active_hooks": 2}),
        ("Many—there's a long list of conversational landmines", {"active_hooks": 1}),
        ("Unknown—you keep your triggers so private they might not know about most of them", {"active_hooks": 2}),
    ]),
    "consistency_check", False, "ah_partner_1", 0.5))

questions.append(make_q("active_hooks", "temporal",
    "In the past month, how many times has something innocuous (a song, a street, a phrase) pulled you back to an unresolved hurt?",
    opts([
        ("Not once—I move through the world without much triggering", {"active_hooks": 5}),
        ("A few times—momentary pulls that I can redirect from", {"active_hooks": 3}),
        ("Weekly or more—the hooks are frequent and disruptive", {"active_hooks": 1}),
        ("I've restructured my life to avoid the triggers, so the count is low but the avoidance is high", {"active_hooks": 1}),
    ]),
    "trap", True, "ah_frequency_1", 0.5,
    tags=[assessment_id, "active_hooks", "trap", "avoidance"]))

questions.append(make_q("active_hooks", "behavioral_recall",
    "How many people, if they walked into the room right now, would cause an immediate emotional reaction in you related to unforgiveness?",
    opts([
        ("Nobody—I'm at peace with everyone who might show up", {"active_hooks": 5}),
        ("One person—there's one person who still gets to me", {"active_hooks": 3}),
        ("Two or three—a small group of unresolved relationships", {"active_hooks": 2}),
        ("More than three—there are several people I'm actively avoiding or dreading", {"active_hooks": 1}),
    ]),
    "triangulation", False, "ah_room_1", 0.6))

questions.append(make_q("active_hooks", "forced_choice",
    "If you could remove ONE active hook—one piece of unforgiveness that still affects your daily life—which describes it?",
    opts([
        ("A family member who hurt me in a way that still shapes how I interact with family", {"active_hooks": 2}),
        ("A romantic partner (current or ex) where the wound is still live", {"active_hooks": 2}),
        ("A professional betrayal that affects how I trust at work", {"active_hooks": 2}),
        ("I don't have an active hook that meaningfully affects my daily life", {"active_hooks": 5}),
    ]),
    "triangulation", False, "ah_remove_one_1", 0.6))

questions.append(make_q("active_hooks", "scenario",
    "You're scrolling social media and see the person who betrayed you tagged in a mutual friend's post. Do you:",
    opts([
        ("Keep scrolling—it doesn't register emotionally", {"active_hooks": 5}),
        ("Pause, feel a brief pang, then continue scrolling", {"active_hooks": 3}),
        ("Click their profile and spend time looking at their life—the hook pulls you in", {"active_hooks": 1}),
        ("Feel your mood shift for the next hour—the encounter derails you", {"active_hooks": 1}),
    ]),
    "consistency_check", False, "ah_social_media_1", 0.7))

questions.append(make_q("active_hooks", "somatic",
    "Your active hooks—when they activate, how intense is the physical response on a 1-10 scale?",
    opts([
        ("1-2—barely registers physically anymore", {"active_hooks": 5}),
        ("3-4—noticeable but manageable", {"active_hooks": 3}),
        ("5-7—significant physical activation that takes time to settle", {"active_hooks": 2}),
        ("8-10—full body response like it's happening right now", {"active_hooks": 1}),
    ]),
    "triangulation", False, "ah_intensity_1", 0.5, depth="deep"))

questions.append(make_q("active_hooks", "temporal",
    "What's the oldest active hook you're still carrying? One that can still be triggered and produce a strong emotional response?",
    opts([
        ("I don't have one—my oldest hurts are fully resolved", {"active_hooks": 5}),
        ("From the past few years—relatively recent", {"active_hooks": 3}),
        ("From 5-10 years ago—a stubborn one", {"active_hooks": 2}),
        ("From childhood or adolescence—decades old and still live", {"active_hooks": 1}),
    ]),
    "trap", True, "ah_oldest_1", 0.5,
    tags=[assessment_id, "active_hooks", "trap", "longevity"]))

questions.append(make_q("active_hooks", "behavioral_recall",
    "How much of your decision-making is currently influenced by active hooks? (e.g., not trusting certain types of people, avoiding certain situations, choosing differently because of past hurt)",
    opts([
        ("Very little—my decisions aren't shaped by unresolved wounds", {"active_hooks": 5}),
        ("Somewhat—I'm aware of a few areas where old hurts influence my choices", {"active_hooks": 3}),
        ("Significantly—active hooks affect how I approach relationships, work, or both", {"active_hooks": 2}),
        ("Pervasively—I can trace many of my current behaviors back to unresolved pain", {"active_hooks": 1}),
    ]),
    "consistency_check", False, "ah_decisions_1", 0.6))

questions.append(make_q("active_hooks", "partner_perspective",
    "Would a therapist say your active hooks are interfering with your current relationships?",
    opts([
        ("No—my current relationships are relatively uncontaminated by past hurts", {"active_hooks": 5}),
        ("Slightly—there are a few areas of hypervigilance or sensitivity that trace back to old wounds", {"active_hooks": 3}),
        ("Yes—active hooks are creating patterns in my current relationships (trust issues, hypervigilance, withdrawal)", {"active_hooks": 1}),
        ("I haven't explored this with a therapist so I'm not sure", {"active_hooks": 3}),
    ]),
    "triangulation", False, "ah_relationships_1", 0.6))

questions.append(make_q("active_hooks", "scenario",
    "You meet someone new who reminds you of a person who betrayed you—similar mannerisms, communication style, even looks a bit like them. How does this affect your ability to engage with the new person?",
    opts([
        ("Not at all—people are individuals and I don't project old wounds onto new people", {"active_hooks": 5}),
        ("I notice the similarity but can override the association", {"active_hooks": 3}),
        ("I'm immediately guarded—the resemblance activates protective patterns", {"active_hooks": 2}),
        ("I avoid them—the association is too strong to override", {"active_hooks": 1}),
    ]),
    "trap", True, "ah_resemblance_1", 0.5,
    tags=[assessment_id, "active_hooks", "trap", "projection"]))

questions.append(make_q("active_hooks", "forced_choice",
    "On a typical day, how much mental bandwidth do your active hooks consume?",
    opts([
        ("Less than 5%—they're background noise at most", {"active_hooks": 5}),
        ("5-15%—a noticeable portion of my mental life", {"active_hooks": 3}),
        ("15-30%—a significant share of my daily attention", {"active_hooks": 2}),
        ("Over 30%—unforgiveness is a dominant theme in my thinking", {"active_hooks": 1}),
    ]),
    "core", False, "ah_core_2", 0.5, depth="light"))

questions.append(make_q("active_hooks", "somatic",
    "Do your active hooks have different physical signatures? (e.g., the betrayal by a friend feels different in your body than the betrayal by a parent)",
    opts([
        ("Yes—each hook has a distinct physical pattern", {"active_hooks": 2}),
        ("Somewhat—they blur together into a general 'hurt' response", {"active_hooks": 2}),
        ("I only have one active hook so there's nothing to compare", {"active_hooks": 3}),
        ("I don't have active hooks that produce physical responses", {"active_hooks": 5}),
    ]),
    "triangulation", False, "ah_signatures_1", 0.7, depth="deep"))

questions.append(make_q("active_hooks", "behavioral_recall",
    "How often do you tell the story of what someone did to you? Not to process it, but because you can't stop telling it—to new people, in new contexts?",
    opts([
        ("I don't tell it unless asked—it's processed and filed away", {"active_hooks": 5}),
        ("Occasionally—when something relevant comes up", {"active_hooks": 3}),
        ("More often than I'd like—I realize I keep bringing it up", {"active_hooks": 2}),
        ("Frequently—it's become part of my identity narrative", {"active_hooks": 1}),
    ]),
    "trap", True, "ah_retelling_1", 0.4,
    tags=[assessment_id, "active_hooks", "trap", "compulsive_retelling"]))

questions.append(make_q("active_hooks", "temporal",
    "Are your active hooks shrinking (fewer triggers, less intensity) or growing (new triggers, more sensitivity)?",
    opts([
        ("Shrinking—I'm gradually decommissioning old hooks through processing", {"active_hooks": 4}),
        ("Stable—same hooks, same intensity", {"active_hooks": 2}),
        ("Growing—new experiences keep adding to the pile", {"active_hooks": 1}),
        ("I don't have enough active hooks to assess a trend", {"active_hooks": 5}),
    ]),
    "consistency_check", False, "ah_trend_1", 0.6))

questions.append(make_q("active_hooks", "scenario",
    "You're in a couples therapy session (or a mediated conversation) and the therapist asks: 'What from your past is showing up in this current conflict?' Can you identify specific hooks?",
    opts([
        ("Yes—I can name the old wound and how it's coloring the current situation", {"active_hooks": 3}),
        ("Vaguely—I know something old is activating but I can't pinpoint it", {"active_hooks": 2}),
        ("No—I don't think my past is relevant to this current issue", {"active_hooks": 2}),
        ("This doesn't apply—my past wounds don't contaminate current conflicts", {"active_hooks": 5}),
    ]),
    "triangulation", False, "ah_therapy_1", 0.7))

questions.append(make_q("active_hooks", "partner_perspective",
    "People who've dated you or been close to you—have any of them said 'you're still not over [that person/event]'?",
    opts([
        ("Yes—it's been pointed out to me by more than one person", {"active_hooks": 1}),
        ("Once—and it was a wake-up call", {"active_hooks": 2}),
        ("No—because I don't let my active hooks show", {"active_hooks": 2}),
        ("No—because I don't have hooks that obviously affect my relationships", {"active_hooks": 5}),
    ]),
    "trap", True, "ah_pointed_out_1", 0.4,
    tags=[assessment_id, "active_hooks", "trap", "external_view"]))

questions.append(make_q("active_hooks", "behavioral_recall",
    "Do you avoid specific restaurants, streets, neighborhoods, songs, or activities because of their association with someone who hurt you?",
    opts([
        ("No—I go where I want without emotional geography dictating my choices", {"active_hooks": 5}),
        ("One or two places—but it's a mild preference, not a hard avoidance", {"active_hooks": 3}),
        ("Several—there are meaningful parts of my city or my life that I've ceded to the wound", {"active_hooks": 1}),
        ("I used to but I've reclaimed those spaces", {"active_hooks": 4}),
    ]),
    "consistency_check", False, "ah_avoidance_1", 0.6))

questions.append(make_q("active_hooks", "forced_choice",
    "If you woke up tomorrow with all your active hooks deactivated—no more triggers, no more resentment—how different would your daily life feel?",
    opts([
        ("Not very different—my hooks are minor and my daily life is largely unaffected", {"active_hooks": 5}),
        ("Somewhat different—there'd be a noticeable lightness", {"active_hooks": 3}),
        ("Very different—I'd feel like a different person", {"active_hooks": 1}),
        ("I can't even imagine what that would feel like—the hooks are too integrated into who I am", {"active_hooks": 1}),
    ]),
    "triangulation", False, "ah_deactivate_1", 0.6))

questions.append(make_q("active_hooks", "somatic",
    "When one of your hooks activates, how long does the physical response last?",
    opts([
        ("Seconds—a brief flash that dissipates quickly", {"active_hooks": 4}),
        ("Minutes—it takes some time to settle back down", {"active_hooks": 3}),
        ("An hour or more—activation lingers well past the trigger", {"active_hooks": 2}),
        ("It can last the rest of the day—once activated, the hook stays live", {"active_hooks": 1}),
    ]),
    "consistency_check", False, "ah_duration_1", 0.7, depth="deep"))

questions.append(make_q("active_hooks", "temporal",
    "Think about 5 years from now. Do you expect your current active hooks to still be active?",
    opts([
        ("No—I'm on a trajectory to resolve them", {"active_hooks": 4}),
        ("Some will, some won't—the deepest ones may persist", {"active_hooks": 3}),
        ("Probably yes—I haven't found a way to deactivate them", {"active_hooks": 1}),
        ("They're already nearly inactive—5 years from now they'll be gone", {"active_hooks": 5}),
    ]),
    "triangulation", False, "ah_future_1", 0.6))

questions.append(make_q("active_hooks", "scenario",
    "You're having a great day—genuinely happy—and someone makes an innocent reference to something connected to a past hurt. Does it:",
    opts([
        ("Barely register—my good mood buffers against triggers", {"active_hooks": 5}),
        ("Put a small dent in my mood that repairs within minutes", {"active_hooks": 3}),
        ("Significantly shift my mood—the hook overrides the good day", {"active_hooks": 1}),
        ("Ruin the day—I spiral from there", {"active_hooks": 1}),
    ]),
    "triangulation", False, "ah_good_day_1", 0.7))

# ============================================================
# PATTERN (25 questions) — how forgiveness typically proceeds
# ============================================================

questions.append(make_q("pattern", "scenario",
    "When someone hurts you and apologizes, what's your typical pattern?",
    opts([
        ("Quick forgiveness that may not be fully processed—I say 'it's fine' fast because I hate conflict", {"pattern": 1}),
        ("Slow, deliberate processing—I need time, but once I forgive, it's thorough and complete", {"pattern": 4}),
        ("Conditional forgiveness—I forgive if certain conditions are met (changes in behavior, accountability)", {"pattern": 3}),
        ("Avoidant—I don't address it directly, I just gradually distance myself", {"pattern": 2}),
    ]),
    "core", False, "pat_core_1", 0.6, depth="light"))

questions.append(make_q("pattern", "somatic",
    "When you're in the middle of forgiving someone, does it feel more like unwinding a knot (slow-thorough) or ripping off a bandaid (quick-incomplete)?",
    opts([
        ("Bandaid—I decide to forgive and move on, even if the feeling hasn't fully caught up", {"pattern": 1}),
        ("Knot—it takes time, layer by layer, until the tension is genuinely gone", {"pattern": 4}),
        ("Neither—it's more like waiting for conditions to be met before I can release", {"pattern": 3}),
        ("Neither—I don't actively forgive, I just... stop caring over time", {"pattern": 2}),
    ]),
    "triangulation", False, "pat_metaphor_1", 0.7, depth="deep"))

questions.append(make_q("pattern", "partner_perspective",
    "People who've known you through multiple conflicts would say your forgiveness pattern is:",
    opts([
        ("Fast but shallow—you say you're over it quickly but sometimes aren't", {"pattern": 1}),
        ("Slow but deep—you take your time but when you forgive, it's real", {"pattern": 4}),
        ("Transactional—forgiveness comes with expectations about future behavior", {"pattern": 3}),
        ("Avoidant—you sidestep the forgiveness conversation by distancing yourself", {"pattern": 2}),
    ]),
    "consistency_check", False, "pat_others_see_1", 0.5))

questions.append(make_q("pattern", "temporal",
    "Think about the last three times someone hurt you. Was your forgiveness process the same each time, or does it change based on circumstances?",
    opts([
        ("Same pattern every time—I have a consistent approach regardless of who or what", {"pattern": 3}),
        ("It varies based on the severity—minor stuff I forgive quickly, major stuff takes time", {"pattern": 3}),
        ("It varies based on the person—some people I forgive easily, others never", {"pattern": 3}),
        ("I don't have a recognizable pattern—each situation feels like starting from scratch", {"pattern": 2}),
    ]),
    "triangulation", False, "pat_consistency_1", 0.6))

questions.append(make_q("pattern", "behavioral_recall",
    "How many times have you said 'I forgive you' and then realized weeks or months later that you hadn't actually forgiven them?",
    opts([
        ("Multiple times—premature forgiveness is my pattern", {"pattern": 1}),
        ("Once or twice—I learned from it and now I'm more careful with the words", {"pattern": 2}),
        ("Never—I don't say it until I mean it", {"pattern": 4}),
        ("I'm not sure—I might be doing it right now without realizing", {"pattern": 1}),
    ]),
    "trap", True, "pat_premature_1", 0.4,
    tags=[assessment_id, "pattern", "trap", "premature"]))

questions.append(make_q("pattern", "forced_choice",
    "Which better describes your forgiveness completion: 'I forgive quickly but incompletely—residue remains' or 'I forgive slowly but thoroughly—when it's done, it's done'?",
    opts([
        ("Quick but incomplete—I often discover unforgiven residue later", {"pattern": 1}),
        ("Slow but thorough—the process takes time but the result is clean", {"pattern": 4}),
    ]),
    "triangulation", False, "pat_quick_vs_thorough_1", 0.5))

questions.append(make_q("pattern", "scenario",
    "A friend hurts you, apologizes, and you say you forgive them. Three months later they do something annoying (but minor). Do you notice the old wound resurface?",
    opts([
        ("Yes—the minor thing reopens the old wound, which means I hadn't fully closed it", {"pattern": 1}),
        ("A faint echo—I notice the connection but it doesn't take over", {"pattern": 3}),
        ("No—the old matter is genuinely resolved and the new annoyance is just a new annoyance", {"pattern": 4}),
        ("Yes, and I use it as evidence that they haven't really changed", {"pattern": 3}),
    ]),
    "consistency_check", False, "pat_resurface_1", 0.7))

questions.append(make_q("pattern", "somatic",
    "When you tell someone 'I forgive you' and your body doesn't agree (still tense, still guarded), do you notice the disconnect?",
    opts([
        ("Yes—and I've learned to wait until body and words align before saying it", {"pattern": 4}),
        ("Sometimes—I notice afterward that the words were ahead of the feeling", {"pattern": 2}),
        ("I don't notice—I assume if I said it, I meant it", {"pattern": 1}),
        ("I don't say 'I forgive you'—it's not language I use", {"pattern": 2}),
    ]),
    "triangulation", False, "pat_body_words_1", 0.7, depth="deep"))

questions.append(make_q("pattern", "temporal",
    "Look at your pattern over multiple forgivings: are you getting faster, slower, or staying the same at completing the forgiveness process?",
    opts([
        ("Faster—I've developed skills and self-awareness that speed the process", {"pattern": 4}),
        ("Slower—as I understand what genuine forgiveness requires, I've stopped rushing", {"pattern": 4}),
        ("Same speed—my pattern hasn't changed much", {"pattern": 2}),
        ("More avoidant—I now avoid situations that would require forgiveness rather than processing faster", {"pattern": 2}),
    ]),
    "triangulation", False, "pat_trajectory_1", 0.6))

questions.append(make_q("pattern", "behavioral_recall",
    "When you forgive, do you need to tell the other person, or is it a purely internal process?",
    opts([
        ("I need to tell them—forgiveness isn't complete without the relational component", {"pattern": 3}),
        ("It's internal—I can fully forgive without them ever knowing", {"pattern": 4}),
        ("I usually tell them because I want them to know the conditions (what would break the forgiveness)", {"pattern": 3}),
        ("I don't formally 'forgive'—I just gradually stop being upset", {"pattern": 2}),
    ]),
    "consistency_check", False, "pat_telling_1", 0.6))

questions.append(make_q("pattern", "partner_perspective",
    "An ex would say your forgiveness pattern in relationships is:",
    opts([
        ("'You forgive fast but keep a mental file—and that file gets opened in future arguments'", {"pattern": 1}),
        ("'You process deeply and when you truly forgive, the issue is dead and buried'", {"pattern": 4}),
        ("'You set conditions and monitor whether they're met—forgiveness on parole'", {"pattern": 3}),
        ("'You don't really forgive—you just emotionally relocate. One day you're in, next day you're gone.'", {"pattern": 2}),
    ]),
    "trap", True, "pat_ex_says_1", 0.4,
    tags=[assessment_id, "pattern", "trap", "relational_pattern"]))

questions.append(make_q("pattern", "scenario",
    "You've forgiven your partner for something serious. A year later you're in a bad argument and the old offense pops into your mind. What do you do with it?",
    opts([
        ("I bring it up—clearly I haven't actually forgiven it if it's still coming back", {"pattern": 1}),
        ("I notice it, recognize it as a sign I have more work to do, and don't use it as a weapon", {"pattern": 4}),
        ("I use it strategically—if it's relevant to the current pattern, it should be discussed", {"pattern": 3}),
        ("I suppress it—I said I forgave and I'm sticking to that, even if my feelings disagree", {"pattern": 1}),
    ]),
    "triangulation", False, "pat_recurrence_1", 0.6))

questions.append(make_q("pattern", "forced_choice",
    "Your natural forgiveness style is best described as:",
    opts([
        ("Quick and generous—but sometimes superficial", {"pattern": 1}),
        ("Slow and thorough—but sometimes exhausting", {"pattern": 4}),
        ("Conditional and structured—but sometimes feels transactional", {"pattern": 3}),
        ("Avoidant and gradual—but sometimes means things never truly resolve", {"pattern": 2}),
    ]),
    "core", False, "pat_core_2", 0.4, depth="light"))

questions.append(make_q("pattern", "somatic",
    "After you complete your forgiveness process (however long it takes), does your body register a clear 'done' signal?",
    opts([
        ("Yes—there's a distinct physical shift when genuine forgiveness lands", {"pattern": 4}),
        ("Sort of—it's more of a gradual fading than a clear moment", {"pattern": 3}),
        ("No—I never quite know if I'm done or just taking a break from the processing", {"pattern": 1}),
        ("I don't process at the body level—forgiveness is a mental/verbal act for me", {"pattern": 2}),
    ]),
    "triangulation", False, "pat_done_signal_1", 0.7, depth="deep"))

questions.append(make_q("pattern", "behavioral_recall",
    "When you forgive conditionally ('I forgive you but you need to X'), what happens when the condition isn't met?",
    opts([
        ("The forgiveness retracts—I was clear about the terms", {"pattern": 3}),
        ("I forgive anyway—the condition was more about hope than requirement", {"pattern": 1}),
        ("I feel justified in my resentment returning—they had their chance", {"pattern": 3}),
        ("I don't attach conditions to forgiveness—it's either given or it isn't", {"pattern": 4}),
    ]),
    "consistency_check", False, "pat_conditions_1", 0.6))

questions.append(make_q("pattern", "temporal",
    "Your fastest complete forgiveness ever took how long? Your slowest (that did eventually complete) took how long?",
    opts([
        ("Fastest: minutes to hours. Slowest: weeks. —I'm a quick forgiver overall", {"pattern": 1}),
        ("Fastest: days. Slowest: years. —I have a wide range depending on severity", {"pattern": 3}),
        ("Fastest: weeks. Slowest: still in progress. —I don't rush any of it", {"pattern": 4}),
        ("I'm not sure any forgiveness I've done was truly 'complete'", {"pattern": 1}),
    ]),
    "trap", True, "pat_range_1", 0.5,
    tags=[assessment_id, "pattern", "trap", "self_assessment"]))

questions.append(make_q("pattern", "scenario",
    "Someone wrongs you and immediately, genuinely apologizes—tears, accountability, the whole thing. Do you forgive faster because of the quality of the apology?",
    opts([
        ("Yes—a good apology dramatically accelerates my forgiveness process", {"pattern": 3}),
        ("It helps but my processing still takes time regardless", {"pattern": 4}),
        ("I'm suspicious of dramatic apologies—they feel performative", {"pattern": 3}),
        ("I'd say 'I forgive you' immediately to end the emotional scene, even if I'm not there yet", {"pattern": 1}),
    ]),
    "triangulation", False, "pat_apology_speed_1", 0.6))

questions.append(make_q("pattern", "partner_perspective",
    "If someone mapped all your forgiveness events on a chart, the pattern they'd see is:",
    opts([
        ("Fast declarations followed by slow actual processing—surface speed hides depth work", {"pattern": 1}),
        ("A consistent, deliberate arc—same process every time, reliable and thorough", {"pattern": 4}),
        ("Contingency-based—the arc shape depends on what the other person does next", {"pattern": 3}),
        ("Flat—minimal processing visible, most forgiveness is internal or absent", {"pattern": 2}),
    ]),
    "consistency_check", False, "pat_chart_1", 0.5))

questions.append(make_q("pattern", "behavioral_recall",
    "Has anyone ever told you that your forgiveness felt performative or incomplete to them?",
    opts([
        ("Yes—they could tell I wasn't really over it even though I said I was", {"pattern": 1}),
        ("No—when I forgive, people feel it as genuine", {"pattern": 4}),
        ("Not in those words, but they've mentioned that I 'bring things up again' that were supposedly resolved", {"pattern": 1}),
        ("No one's commented on it—my forgiveness is mostly private", {"pattern": 2}),
    ]),
    "trap", True, "pat_performative_1", 0.4,
    tags=[assessment_id, "pattern", "trap", "authenticity"]))

questions.append(make_q("pattern", "forced_choice",
    "If you had to choose between 'forgive immediately and risk it being incomplete' or 'withhold forgiveness until you're certain it's genuine,' which is your default?",
    opts([
        ("Forgive immediately—I'd rather err on the side of grace even if I have to do cleanup later", {"pattern": 1}),
        ("Withhold until certain—premature forgiveness is worse than delayed forgiveness", {"pattern": 4}),
    ]),
    "triangulation", False, "pat_default_1", 0.5))

questions.append(make_q("pattern", "somatic",
    "During the period between being hurt and reaching genuine forgiveness, where is the discomfort most concentrated?",
    opts([
        ("Everywhere briefly—I don't hold it long enough for it to localize", {"pattern": 1}),
        ("In a specific place that gradually releases as forgiveness deepens—I can feel the layers unwinding", {"pattern": 4}),
        ("In my head—I'm negotiating, analyzing, deciding, more than feeling", {"pattern": 3}),
        ("I go numb to it—I don't feel the discomfort during avoidance, it surfaces later", {"pattern": 2}),
    ]),
    "triangulation", False, "pat_discomfort_1", 0.7, depth="deep"))

questions.append(make_q("pattern", "temporal",
    "Have you ever gone back and truly forgiven someone you thought you'd already forgiven? A second round of deeper processing?",
    opts([
        ("Yes—I realized my first 'forgiveness' was surface-level and I needed to go deeper", {"pattern": 1}),
        ("Yes—and the second round was where the real healing happened", {"pattern": 4}),
        ("No—my forgiveness process may be slow but I don't need to redo it", {"pattern": 4}),
        ("No—I'm not sure I've ever completed a first round of genuine forgiveness, let alone a second", {"pattern": 1}),
    ]),
    "consistency_check", False, "pat_second_round_1", 0.7))

questions.append(make_q("pattern", "scenario",
    "Two people wrong you in the same week: one is a close friend (deep betrayal), the other is a stranger (rude behavior). How does your forgiveness process differ?",
    opts([
        ("Stranger: instant forgiveness. Friend: same speed, I'm a quick forgiver across the board.", {"pattern": 1}),
        ("Stranger: instant. Friend: months of processing—depth of relationship determines depth of process", {"pattern": 4}),
        ("Both take time proportional to the harm, regardless of who did it", {"pattern": 4}),
        ("Stranger: irritation that fades. Friend: the forgiveness depends on what they do next (apologize, explain, change).", {"pattern": 3}),
    ]),
    "triangulation", False, "pat_stranger_vs_friend_1", 0.7))

questions.append(make_q("pattern", "behavioral_recall",
    "What's your relationship between forgiveness and trust? Once you forgive, do you also re-trust?",
    opts([
        ("Yes—forgiveness and trust are the same act for me", {"pattern": 1}),
        ("Forgiveness comes first; trust is rebuilt separately and slowly", {"pattern": 4}),
        ("Trust is rebuilt conditionally—based on observed behavior changes", {"pattern": 3}),
        ("I can forgive without ever re-trusting—they're completely separate", {"pattern": 4}),
    ]),
    "core", False, "pat_core_3", 0.6, depth="light"))

# Final validation
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

# Check UIDs unique
uids = [q["uid"] for q in questions]
dupes = [u for u in uids if uids.count(u) > 1]
print(f"Duplicate UIDs: {set(dupes) if dupes else 'none'}")

with open("/Users/user/personal/sb/trueassess/priv/question_bank/forgiveness_profile.json", "w") as f:
    json.dump(questions, f, indent=2)

print("Written to forgiveness_profile.json")
