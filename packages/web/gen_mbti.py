#!/usr/bin/env python3
"""Generate 150 MBTI-style cognitive dimension questions."""
import json

questions = []
uid_counter = 1

def uid():
    global uid_counter
    u = f"MBTI-{uid_counter:03d}"
    uid_counter += 1
    return u

def q(dimension, qtype, text, options, tier="core", opacity=0.6, sd_trap=False, cg=None, reversal=False, universal=True, adaptations=[], adapt_notes=None, rating="G", categories=[], depth="moderate", tags=None):
    if tags is None:
        tags = ["mbti_style", dimension]
    return {
        "uid": uid(),
        "assessment_id": "mbti_style",
        "dimension": dimension,
        "question_type": qtype,
        "text": text,
        "options": options,
        "tier_role": tier,
        "anti_gaming": {
            "opacity": opacity,
            "social_desirability_trap": sd_trap,
            "consistency_group": cg or f"{dimension[:3]}_{uid_counter}",
            "reversal": reversal
        },
        "cultural_adaptability": {
            "universal": universal,
            "adaptations_needed": adaptations,
            "adaptation_notes": adapt_notes
        },
        "content_rating": rating,
        "content_categories": categories,
        "depth_tier": depth,
        "tags": tags
    }

def opts(dim, scores_list):
    """Create options with scores. scores_list = [(id, text, {dim: score}), ...]"""
    return [{"id": s[0], "text": s[1], "scores": s[2]} for s in scores_list]

# ============================================================
# EXTRAVERSION / INTROVERSION (25 questions)
# ============================================================
d = "extraversion_introversion"

questions.append(q(d, "scenario",
    "You have an unexpected free Saturday with no obligations. Your first instinct is to:",
    opts(d, [
        ("a", "Call friends to see who wants to hang out", {d: 5}),
        ("b", "Check if there are any events happening nearby", {d: 4}),
        ("c", "Enjoy the quiet — read, tinker, or just think", {d: 1}),
        ("d", "Do something solo outside — a hike or coffee shop visit", {d: 2})
    ]), cg="ei_energy_1"))

questions.append(q(d, "behavioral_recall",
    "After a full day of back-to-back meetings or social events, you typically feel:",
    opts(d, [
        ("a", "Energized and still wanting to connect with people", {d: 5}),
        ("b", "Fine but ready for some downtime", {d: 3}),
        ("c", "Completely drained — you need hours alone to recover", {d: 1}),
        ("d", "Mixed — stimulated mentally but physically tired", {d: 2})
    ]), cg="ei_energy_1"))

questions.append(q(d, "scenario",
    "At a party where you know only the host, you:",
    opts(d, [
        ("a", "Introduce yourself to several groups throughout the night", {d: 5}),
        ("b", "Find one interesting person and have a deep conversation", {d: 2}),
        ("c", "Stay near the host and let introductions happen naturally", {d: 3}),
        ("d", "Find a quiet corner and observe before deciding whether to engage", {d: 1})
    ]), cg="ei_social_1"))

questions.append(q(d, "forced_choice",
    "Which statement resonates more with how you actually operate?",
    opts(d, [
        ("a", "I think best when I can talk things through with others", {d: 5}),
        ("b", "I think best when I have uninterrupted time alone", {d: 1})
    ]), cg="ei_processing_1"))

questions.append(q(d, "behavioral_recall",
    "When you have a problem to solve at work, your first move is usually to:",
    opts(d, [
        ("a", "Bounce ideas off a colleague immediately", {d: 5}),
        ("b", "Think it through alone, then share your solution", {d: 1}),
        ("c", "Research independently, then discuss to refine", {d: 2}),
        ("d", "Call a quick meeting to brainstorm", {d: 4})
    ]), cg="ei_processing_1"))

questions.append(q(d, "scenario",
    "You're working on a creative project. The environment that helps you most is:",
    opts(d, [
        ("a", "A busy coffee shop with ambient noise and people around", {d: 4}),
        ("b", "A quiet room with the door closed", {d: 1}),
        ("c", "A co-working space where you can chat or focus as needed", {d: 3}),
        ("d", "Collaborating live with others on a whiteboard", {d: 5})
    ]), cg="ei_environment_1"))

questions.append(q(d, "temporal",
    "Over the past year, how has your social appetite changed?",
    opts(d, [
        ("a", "I've been craving more social connection than ever", {d: 5}),
        ("b", "About the same — I know my social sweet spot", {d: 3}),
        ("c", "I've been pulling back and needing more solitude", {d: 1}),
        ("d", "It fluctuates a lot depending on what's happening in my life", {d: 3})
    ]), cg="ei_temporal_1"))

questions.append(q(d, "scenario",
    "Your phone rings with an unknown number. You:",
    opts(d, [
        ("a", "Answer it — could be interesting or important", {d: 5}),
        ("b", "Let it go to voicemail and check later", {d: 1}),
        ("c", "Answer but feel slightly annoyed at the interruption", {d: 2}),
        ("d", "Google the number first, then decide", {d: 2})
    ]), cg="ei_spontaneous_1"))

questions.append(q(d, "somatic",
    "When you're in a crowded, noisy environment for an extended period, your body tends to:",
    opts(d, [
        ("a", "Feel alive — your energy rises with the stimulation", {d: 5}),
        ("b", "Feel neutral — you can tune it out", {d: 3}),
        ("c", "Feel tension building — headache, tight shoulders, restlessness", {d: 1}),
        ("d", "Feel initial excitement that fades into fatigue", {d: 2})
    ]), cg="ei_somatic_1"))

questions.append(q(d, "behavioral_recall",
    "How many close friends do you actively maintain contact with?",
    opts(d, [
        ("a", "10+ — I have a wide circle I stay connected to", {d: 5}),
        ("b", "5-9 — a solid group", {d: 4}),
        ("c", "2-4 — a few deep relationships", {d: 2}),
        ("d", "0-1 — I prefer very few but very deep bonds", {d: 1})
    ]), cg="ei_social_2"))

questions.append(q(d, "scenario",
    "A colleague suggests an impromptu lunch with a group you don't know well. You:",
    opts(d, [
        ("a", "Jump at it — great way to expand your network", {d: 5}),
        ("b", "Go along but feel a bit uncomfortable", {d: 3}),
        ("c", "Politely decline and eat at your desk", {d: 1}),
        ("d", "Go if a friend is also going, skip if you'd be alone with strangers", {d: 2})
    ]), cg="ei_spontaneous_1"))

questions.append(q(d, "forced_choice",
    "If you had to choose one for a week-long vacation:",
    opts(d, [
        ("a", "A group adventure tour with 12 strangers", {d: 5}),
        ("b", "A solo cabin retreat in the mountains", {d: 1})
    ]), cg="ei_energy_2"))

questions.append(q(d, "scenario",
    "You've just finished a major project. To celebrate, you'd prefer to:",
    opts(d, [
        ("a", "Throw a party or go out with a big group", {d: 5}),
        ("b", "Have a quiet dinner with your partner or closest friend", {d: 2}),
        ("c", "Spend the evening alone doing something you love", {d: 1}),
        ("d", "Go to a restaurant with a small group of friends", {d: 3})
    ]), cg="ei_energy_2"))

questions.append(q(d, "behavioral_recall",
    "When learning a new skill, you prefer:",
    opts(d, [
        ("a", "A group class with interaction and shared learning", {d: 5}),
        ("b", "A one-on-one mentor or tutor", {d: 3}),
        ("c", "Online tutorials you can do at your own pace alone", {d: 1}),
        ("d", "A workshop with some group and some solo practice", {d: 3})
    ]), cg="ei_learning_1"))

questions.append(q(d, "scenario",
    "You're waiting for a friend at a restaurant and they're 20 minutes late. You:",
    opts(d, [
        ("a", "Strike up a conversation with the bartender or nearby diners", {d: 5}),
        ("b", "Scroll your phone contentedly — alone time is fine", {d: 1}),
        ("c", "Text another friend to chat while waiting", {d: 4}),
        ("d", "People-watch and enjoy the atmosphere", {d: 2})
    ]), cg="ei_spontaneous_2"))

# Trap question - looks like it measures E/I but actually checks honesty
questions.append(q(d, "scenario",
    "You're at a networking event for your career. Honestly, how do you feel inside?",
    opts(d, [
        ("a", "Genuinely excited — this is where opportunities happen", {d: 5}),
        ("b", "Somewhat anxious but pushing through because it's useful", {d: 2}),
        ("c", "Dreading every minute but you know you should be here", {d: 1}),
        ("d", "Completely at ease — you love meeting new professionals", {d: 5})
    ]), tier="trap", opacity=0.4, sd_trap=True, cg="ei_trap_1"))

questions.append(q(d, "somatic",
    "After spending an entire day alone, your body and mind typically feel:",
    opts(d, [
        ("a", "Restless — you need human contact", {d: 5}),
        ("b", "Recharged and peaceful", {d: 1}),
        ("c", "Fine but ready for some interaction tomorrow", {d: 3}),
        ("d", "Slightly lonely but still comfortable", {d: 2})
    ]), cg="ei_somatic_1", reversal=True))

questions.append(q(d, "forced_choice",
    "When making a decision, you're more likely to:",
    opts(d, [
        ("a", "Talk it out with multiple people to hear perspectives", {d: 5}),
        ("b", "Journal or think it through privately before mentioning it", {d: 1})
    ]), cg="ei_processing_2"))

questions.append(q(d, "temporal",
    "Think about the last time you felt truly in your element. Were you:",
    opts(d, [
        ("a", "Leading or energizing a group", {d: 5}),
        ("b", "Deep in focused solo work", {d: 1}),
        ("c", "Having an intimate conversation with someone close", {d: 2}),
        ("d", "Performing or presenting to an audience", {d: 5})
    ]), cg="ei_temporal_2"))

questions.append(q(d, "scenario",
    "A new neighbor moves in next door. Your natural response is to:",
    opts(d, [
        ("a", "Go over and introduce yourself within the first day", {d: 5}),
        ("b", "Wave if you see them but wait for a natural moment", {d: 3}),
        ("c", "Hope they're quiet and keep to themselves", {d: 1}),
        ("d", "Bring over cookies or a welcome note", {d: 4})
    ]), cg="ei_social_2"))

questions.append(q(d, "behavioral_recall",
    "In group conversations, you typically:",
    opts(d, [
        ("a", "Jump in frequently — you process by talking", {d: 5}),
        ("b", "Listen mostly, then make one or two considered points", {d: 1}),
        ("c", "Contribute regularly but aren't the loudest voice", {d: 3}),
        ("d", "Dominate the conversation without realizing it", {d: 5})
    ]), cg="ei_social_3"))

questions.append(q(d, "scenario",
    "Your ideal work setup would be:",
    opts(d, [
        ("a", "Open floor plan with constant collaboration", {d: 5}),
        ("b", "Private office with a closed door", {d: 1}),
        ("c", "Hybrid — some collaborative spaces, some quiet zones", {d: 3}),
        ("d", "Remote work from home", {d: 1})
    ]), cg="ei_environment_1"))

# Consistency check
questions.append(q(d, "forced_choice",
    "Which drains you faster?",
    opts(d, [
        ("a", "Being alone with nothing to do for hours", {d: 5}),
        ("b", "Being in constant social interaction for hours", {d: 1})
    ]), tier="consistency_check", cg="ei_energy_1"))

questions.append(q(d, "scenario",
    "You discover a fascinating new interest. Your first instinct is to:",
    opts(d, [
        ("a", "Find a community or group that shares this interest", {d: 5}),
        ("b", "Dive deep into it alone — books, videos, experiments", {d: 1}),
        ("c", "Tell your closest friend about it enthusiastically", {d: 3}),
        ("d", "Search for a class or workshop to learn with others", {d: 4})
    ]), cg="ei_learning_1"))

questions.append(q(d, "behavioral_recall",
    "When you're feeling stressed or overwhelmed, you tend to:",
    opts(d, [
        ("a", "Seek out friends or family to talk it through", {d: 5}),
        ("b", "Withdraw and process alone until you feel better", {d: 1}),
        ("c", "Distract yourself with activity — going out, staying busy", {d: 4}),
        ("d", "Alternate between reaching out and needing space", {d: 3})
    ]), cg="ei_coping_1"))

# ============================================================
# SENSING / INTUITION (25 questions)
# ============================================================
d = "sensing_intuition"

questions.append(q(d, "scenario",
    "You walk into a room you've never been in before. You first notice:",
    opts(d, [
        ("a", "Specific details — the color of the walls, the furniture layout, the temperature", {d: 1}),
        ("b", "The overall vibe or atmosphere of the space", {d: 5}),
        ("c", "Practical things — where the exits are, if there's seating", {d: 1}),
        ("d", "What the space could be used for — possibilities and potential", {d: 5})
    ]), cg="sn_perception_1"))

questions.append(q(d, "forced_choice",
    "When someone asks you to describe your weekend, you're more likely to:",
    opts(d, [
        ("a", "Give a chronological account of what you did", {d: 1}),
        ("b", "Describe the overall theme or feeling of the weekend", {d: 5})
    ]), cg="sn_communication_1"))

questions.append(q(d, "behavioral_recall",
    "When reading instructions for assembling something, you typically:",
    opts(d, [
        ("a", "Follow them step by step, in order", {d: 1}),
        ("b", "Glance at the picture and figure it out as you go", {d: 5}),
        ("c", "Read all instructions first, then work from memory", {d: 4}),
        ("d", "Read each step carefully and check your work against it", {d: 1})
    ]), cg="sn_approach_1"))

questions.append(q(d, "scenario",
    "A friend tells you about a business idea. Your first response is usually to:",
    opts(d, [
        ("a", "Ask practical questions: cost, timeline, market size", {d: 1}),
        ("b", "Get excited about the vision and brainstorm possibilities", {d: 5}),
        ("c", "Think about similar businesses that have succeeded or failed", {d: 2}),
        ("d", "Imagine how it could evolve into something even bigger", {d: 5})
    ]), cg="sn_response_1"))

questions.append(q(d, "temporal",
    "When you think about your future, your thoughts tend to be:",
    opts(d, [
        ("a", "Concrete plans with specific timelines and milestones", {d: 1}),
        ("b", "A vivid but somewhat abstract vision of where you're heading", {d: 5}),
        ("c", "Focused on the next few months — future planning happens step by step", {d: 1}),
        ("d", "Grand sweeping ideas that may or may not be realistic", {d: 5})
    ]), cg="sn_temporal_1"))

questions.append(q(d, "behavioral_recall",
    "In conversations, people have told you that you:",
    opts(d, [
        ("a", "Are very detail-oriented and remember specifics others miss", {d: 1}),
        ("b", "Make unexpected connections between unrelated topics", {d: 5}),
        ("c", "Are practical and grounded in your thinking", {d: 1}),
        ("d", "Sometimes get lost in abstract tangents", {d: 5})
    ]), cg="sn_feedback_1"))

questions.append(q(d, "scenario",
    "You're choosing a vacation. You'd prefer:",
    opts(d, [
        ("a", "A well-reviewed resort with reliable amenities you can research thoroughly", {d: 1}),
        ("b", "An off-the-beaten-path destination that sparks your imagination", {d: 5}),
        ("c", "A return trip to somewhere you loved — you know what to expect", {d: 1}),
        ("d", "Somewhere completely new that offers a different perspective on life", {d: 5})
    ]), cg="sn_choice_1"))

questions.append(q(d, "forced_choice",
    "Which frustrates you more?",
    opts(d, [
        ("a", "Vague instructions that leave out important details", {d: 1}),
        ("b", "Overly rigid rules that leave no room for creative interpretation", {d: 5})
    ]), cg="sn_frustration_1"))

questions.append(q(d, "somatic",
    "When you have a sudden insight or idea, you physically feel:",
    opts(d, [
        ("a", "Nothing particular — ideas are just thoughts", {d: 1}),
        ("b", "A rush of energy or excitement, almost a physical buzz", {d: 5}),
        ("c", "Calm satisfaction if the idea is practical and useful", {d: 2}),
        ("d", "An urgent need to capture it before it fades", {d: 5})
    ]), cg="sn_somatic_1"))

questions.append(q(d, "scenario",
    "You're cooking dinner. You tend to:",
    opts(d, [
        ("a", "Follow a recipe precisely, measuring ingredients carefully", {d: 1}),
        ("b", "Use a recipe as loose inspiration and improvise freely", {d: 5}),
        ("c", "Cook a tried-and-true dish you've made many times", {d: 1}),
        ("d", "Experiment with flavor combinations that interest you", {d: 5})
    ]), cg="sn_approach_2"))

questions.append(q(d, "behavioral_recall",
    "When telling a story, you tend to:",
    opts(d, [
        ("a", "Include lots of specific details — names, dates, what people wore", {d: 1}),
        ("b", "Focus on the meaning or lesson of the story", {d: 5}),
        ("c", "Tell it in sequence — what happened first, then next", {d: 1}),
        ("d", "Jump around to the most interesting parts, sometimes losing the thread", {d: 5})
    ]), cg="sn_communication_1"))

questions.append(q(d, "scenario",
    "A new policy is announced at work. Your first thought is:",
    opts(d, [
        ("a", "How will this affect my daily routine and tasks?", {d: 1}),
        ("b", "What's the bigger picture behind this change?", {d: 5}),
        ("c", "What are the specific rules and how do I comply?", {d: 1}),
        ("d", "How could this reshape the organization over time?", {d: 5})
    ]), cg="sn_response_2"))

questions.append(q(d, "forced_choice",
    "You'd rather be known as someone who is:",
    opts(d, [
        ("a", "Reliable, thorough, and precise", {d: 1}),
        ("b", "Visionary, creative, and original", {d: 5})
    ]), cg="sn_identity_1"))

questions.append(q(d, "temporal",
    "When remembering a meaningful experience, what comes to mind first?",
    opts(d, [
        ("a", "Vivid sensory details — sights, sounds, smells, textures", {d: 1}),
        ("b", "The emotional meaning and how it changed your perspective", {d: 5}),
        ("c", "The sequence of events as they happened", {d: 1}),
        ("d", "Symbolic or metaphorical significance of the experience", {d: 5})
    ]), cg="sn_memory_1"))

questions.append(q(d, "scenario",
    "You're shopping for a car. You prioritize:",
    opts(d, [
        ("a", "Specs, safety ratings, fuel economy, and resale value", {d: 1}),
        ("b", "How driving it makes you feel and what it represents", {d: 5}),
        ("c", "Practical features: cargo space, reliability, maintenance cost", {d: 1}),
        ("d", "Design innovation and the brand's vision", {d: 5})
    ]), cg="sn_choice_2"))

questions.append(q(d, "behavioral_recall",
    "At work, you're most valued for:",
    opts(d, [
        ("a", "Catching errors and ensuring accuracy", {d: 1}),
        ("b", "Generating innovative ideas and strategies", {d: 5}),
        ("c", "Delivering consistent, dependable results", {d: 1}),
        ("d", "Seeing patterns and possibilities others miss", {d: 5})
    ]), cg="sn_feedback_1"))

questions.append(q(d, "scenario",
    "When learning something new, you prefer:",
    opts(d, [
        ("a", "Hands-on practice with concrete examples", {d: 1}),
        ("b", "Understanding the underlying theory and principles first", {d: 5}),
        ("c", "Step-by-step demonstrations you can replicate", {d: 1}),
        ("d", "Exploring the subject freely and making your own connections", {d: 5})
    ]), cg="sn_learning_1"))

# Trap
questions.append(q(d, "scenario",
    "You notice a pattern in your company's sales data that no one else has seen. You:",
    opts(d, [
        ("a", "Document the specific numbers and present the data clearly", {d: 2}),
        ("b", "Develop a theory about what's causing the pattern and present the big picture", {d: 4}),
        ("c", "Wait to see if the pattern holds before saying anything", {d: 2}),
        ("d", "Immediately share your insight — this could change everything", {d: 4})
    ]), tier="trap", opacity=0.4, sd_trap=True, cg="sn_trap_1"))

questions.append(q(d, "forced_choice",
    "Which type of book appeals to you more?",
    opts(d, [
        ("a", "A practical how-to guide with actionable steps", {d: 1}),
        ("b", "A thought-provoking exploration of ideas and possibilities", {d: 5})
    ]), cg="sn_preference_1"))

questions.append(q(d, "somatic",
    "When you're in a routine that works well, you feel:",
    opts(d, [
        ("a", "Comfortable and grounded — this is how things should work", {d: 1}),
        ("b", "Slightly restless — even good routines start to feel confining", {d: 5}),
        ("c", "Secure and productive — predictability is efficient", {d: 1}),
        ("d", "Fine for now but already thinking about what's next", {d: 4})
    ]), cg="sn_routine_1"))

questions.append(q(d, "scenario",
    "You're asked to give a presentation. Your approach is to:",
    opts(d, [
        ("a", "Build it around concrete facts, data, and specific examples", {d: 1}),
        ("b", "Start with the big idea and use stories and metaphors to illustrate", {d: 5}),
        ("c", "Create a clear, logical outline with supporting evidence", {d: 2}),
        ("d", "Wing it based on your deep understanding of the topic", {d: 4})
    ]), cg="sn_approach_3"))

questions.append(q(d, "behavioral_recall",
    "When you disagree with someone, it's usually because:",
    opts(d, [
        ("a", "They're ignoring relevant facts or practical considerations", {d: 1}),
        ("b", "They're too narrowly focused and missing the bigger picture", {d: 5}),
        ("c", "Their plan has specific flaws you can identify", {d: 1}),
        ("d", "They're being too literal and not seeing the deeper meaning", {d: 5})
    ]), cg="sn_conflict_1"))

# Consistency check
questions.append(q(d, "forced_choice",
    "In your daily life, you rely more on:",
    opts(d, [
        ("a", "What you can see, hear, touch, and verify directly", {d: 1}),
        ("b", "Hunches, gut feelings, and intuitive leaps", {d: 5})
    ]), tier="consistency_check", cg="sn_perception_1"))

questions.append(q(d, "scenario",
    "A friend asks for directions to your house. You'd most naturally:",
    opts(d, [
        ("a", "Give precise turn-by-turn directions with street names and landmarks", {d: 1}),
        ("b", "Describe the general area and trust they'll find it", {d: 5}),
        ("c", "Send a pin on a map app", {d: 2}),
        ("d", "Say something like 'head toward the lake and you'll feel when you're close'", {d: 5})
    ]), cg="sn_communication_2"))

questions.append(q(d, "temporal",
    "When you look at your life trajectory, you see:",
    opts(d, [
        ("a", "A series of concrete steps and practical decisions that built on each other", {d: 1}),
        ("b", "An evolving narrative shaped by insights, themes, and turning points", {d: 5}),
        ("c", "A steady progression through logical stages", {d: 2}),
        ("d", "A winding path that makes sense only in retrospect", {d: 5})
    ]), cg="sn_temporal_2"))

# ============================================================
# THINKING / FEELING (25 questions)
# ============================================================
d = "thinking_feeling"

questions.append(q(d, "scenario",
    "A close friend asks for feedback on a project they're clearly proud of, but you see significant flaws. You:",
    opts(d, [
        ("a", "Give honest, direct feedback — they need to hear it to improve", {d: 1}),
        ("b", "Start with genuine praise, then gently mention one or two concerns", {d: 4}),
        ("c", "Focus entirely on what's good — their feelings matter more than critique right now", {d: 5}),
        ("d", "Ask questions that guide them to discover the issues themselves", {d: 3})
    ]), cg="tf_feedback_1"))

questions.append(q(d, "forced_choice",
    "When making a major life decision, you give more weight to:",
    opts(d, [
        ("a", "Logic, analysis, and objective criteria", {d: 1}),
        ("b", "How it will affect you and the people you care about emotionally", {d: 5})
    ]), cg="tf_decision_1"))

questions.append(q(d, "behavioral_recall",
    "In workplace disagreements, you're known for:",
    opts(d, [
        ("a", "Cutting through the noise to find the logical solution", {d: 1}),
        ("b", "Finding compromises that keep everyone feeling heard", {d: 5}),
        ("c", "Presenting data and evidence to support your position", {d: 1}),
        ("d", "Reading the room and addressing underlying emotional dynamics", {d: 5})
    ]), cg="tf_conflict_1"))

questions.append(q(d, "scenario",
    "Two qualified candidates are up for a promotion. One has better metrics; the other has been struggling with personal issues and a promotion would be life-changing. You'd advocate for:",
    opts(d, [
        ("a", "The one with better metrics — merit should decide", {d: 1}),
        ("b", "The one who needs it more — the human factor matters", {d: 5}),
        ("c", "The one with better metrics, but push for support for the other", {d: 2}),
        ("d", "Whichever decision you could more easily explain to both parties", {d: 3})
    ]), cg="tf_values_1"))

questions.append(q(d, "somatic",
    "When you witness an injustice — say, someone being publicly humiliated — your gut reaction is:",
    opts(d, [
        ("a", "Analysis: what's the context, who's right, what should happen", {d: 1}),
        ("b", "A strong emotional response — anger, sadness, or the urge to intervene", {d: 5}),
        ("c", "Detached assessment of the situation before deciding how to respond", {d: 1}),
        ("d", "Empathic distress — you feel what the humiliated person is feeling", {d: 5})
    ]), cg="tf_somatic_1"))

questions.append(q(d, "behavioral_recall",
    "People close to you would say you are:",
    opts(d, [
        ("a", "Fair-minded and objective, even when it's uncomfortable", {d: 1}),
        ("b", "Warm, empathetic, and attuned to others' needs", {d: 5}),
        ("c", "Logical and hard to argue with", {d: 1}),
        ("d", "The person everyone goes to when they need emotional support", {d: 5})
    ]), cg="tf_feedback_2"))

questions.append(q(d, "scenario",
    "You need to deliver bad news to your team. Your approach is to:",
    opts(d, [
        ("a", "Be direct and clear — they deserve the truth without sugarcoating", {d: 1}),
        ("b", "Frame it carefully, considering how each person will receive it emotionally", {d: 5}),
        ("c", "Present the facts and the logical next steps", {d: 1}),
        ("d", "Acknowledge the emotional impact first, then share the information", {d: 5})
    ]), cg="tf_communication_1"))

questions.append(q(d, "forced_choice",
    "Which compliment would mean more to you?",
    opts(d, [
        ("a", "\"Your analysis was brilliant — completely airtight logic\"", {d: 1}),
        ("b", "\"You made everyone feel included and valued\"", {d: 5})
    ]), cg="tf_identity_1"))

questions.append(q(d, "temporal",
    "When you look back on past decisions you regret, they tend to be times when:",
    opts(d, [
        ("a", "You let emotions override clear thinking", {d: 1}),
        ("b", "You prioritized logic over people's feelings", {d: 5}),
        ("c", "You didn't gather enough information", {d: 2}),
        ("d", "You weren't empathetic enough to someone who needed you", {d: 5})
    ]), cg="tf_temporal_1"))

questions.append(q(d, "scenario",
    "A family member makes a financial decision you think is foolish. You:",
    opts(d, [
        ("a", "Tell them clearly why you think it's a bad decision", {d: 1}),
        ("b", "Express concern for how this might affect them, without criticizing the decision directly", {d: 5}),
        ("c", "Present alternative options with a rational comparison", {d: 1}),
        ("d", "Support their autonomy — it's their decision even if you disagree", {d: 4})
    ]), cg="tf_approach_1"))

questions.append(q(d, "behavioral_recall",
    "In a debate or argument, you're more focused on:",
    opts(d, [
        ("a", "Being correct and logically consistent", {d: 1}),
        ("b", "Maintaining the relationship and finding harmony", {d: 5}),
        ("c", "Finding the objective truth regardless of feelings", {d: 1}),
        ("d", "Making sure no one feels attacked or dismissed", {d: 5})
    ]), cg="tf_conflict_1"))

questions.append(q(d, "scenario",
    "You're writing a performance review for a struggling employee. You emphasize:",
    opts(d, [
        ("a", "Specific areas needing improvement with measurable targets", {d: 1}),
        ("b", "Their strengths and potential, with gentle guidance on growth areas", {d: 5}),
        ("c", "An honest assessment — anything less is unfair to them", {d: 1}),
        ("d", "How you can support them in getting where they need to be", {d: 4})
    ]), cg="tf_communication_2"))

questions.append(q(d, "forced_choice",
    "Which is worse in a leader?",
    opts(d, [
        ("a", "Being too soft and letting poor performance slide", {d: 1}),
        ("b", "Being too harsh and damaging team morale", {d: 5})
    ]), cg="tf_values_2"))

questions.append(q(d, "somatic",
    "When you have to make a tough decision that affects others, you physically feel:",
    opts(d, [
        ("a", "Clear-headed and focused — tough decisions require clear thinking", {d: 1}),
        ("b", "A weight in your chest or stomach — the emotional impact is real", {d: 5}),
        ("c", "Mild stress but it resolves once you've analyzed the options", {d: 2}),
        ("d", "Deep discomfort that lingers even after the decision is made", {d: 5})
    ]), cg="tf_somatic_2"))

questions.append(q(d, "scenario",
    "A movie's plot has a logical inconsistency that no one else notices. You:",
    opts(d, [
        ("a", "Point it out — it bothers you and you can't un-see it", {d: 1}),
        ("b", "Don't care — you're watching for the emotional journey", {d: 5}),
        ("c", "Notice it but enjoy the movie anyway", {d: 3}),
        ("d", "Find it mildly annoying but let it go", {d: 3})
    ]), cg="tf_perception_1"))

questions.append(q(d, "behavioral_recall",
    "When a friend is going through a hard time, they come to you because:",
    opts(d, [
        ("a", "You'll help them think through the problem clearly", {d: 1}),
        ("b", "You'll listen and validate their feelings", {d: 5}),
        ("c", "You'll give practical advice and a plan of action", {d: 1}),
        ("d", "You'll sit with them in the difficulty without trying to fix it", {d: 5})
    ]), cg="tf_support_1"))

# Trap
questions.append(q(d, "scenario",
    "You find out a colleague received a higher raise than you despite similar performance. Your honest reaction is:",
    opts(d, [
        ("a", "Analyze why — is there a logical explanation or is this unfair?", {d: 2}),
        ("b", "Feel hurt but try to be happy for them", {d: 4}),
        ("c", "Doesn't bother you as long as your compensation is fair", {d: 1}),
        ("d", "Feel a strong emotional response that takes time to process", {d: 5})
    ]), tier="trap", opacity=0.4, sd_trap=True, cg="tf_trap_1"))

questions.append(q(d, "forced_choice",
    "You trust more:",
    opts(d, [
        ("a", "Data, evidence, and logical reasoning", {d: 1}),
        ("b", "Your gut feeling about people and situations", {d: 5})
    ]), cg="tf_decision_2"))

questions.append(q(d, "scenario",
    "Your team needs to lay off one person. The decision criteria should be:",
    opts(d, [
        ("a", "Performance metrics and business need — objectivity is fairest", {d: 1}),
        ("b", "The whole picture — performance but also life circumstances and impact", {d: 5}),
        ("c", "Strictly by the numbers — anything else introduces bias", {d: 1}),
        ("d", "Whatever causes the least human suffering", {d: 5})
    ]), cg="tf_values_1"))

questions.append(q(d, "temporal",
    "Over time, your conflict style has evolved toward:",
    opts(d, [
        ("a", "Being more direct and less willing to compromise on truth", {d: 1}),
        ("b", "Being more empathetic and focused on understanding others", {d: 5}),
        ("c", "Being more strategic about when to push and when to yield", {d: 2}),
        ("d", "Being more attuned to the emotional undercurrents in conflicts", {d: 5})
    ]), cg="tf_temporal_2"))

questions.append(q(d, "behavioral_recall",
    "When you watch the news, you're drawn to stories that:",
    opts(d, [
        ("a", "Present clear analysis of complex issues", {d: 1}),
        ("b", "Highlight human impact and personal stories", {d: 5}),
        ("c", "Provide data and facts you can evaluate", {d: 1}),
        ("d", "Move you emotionally and inspire action", {d: 5})
    ]), cg="tf_perception_2"))

questions.append(q(d, "scenario",
    "You discover your partner made a decision without consulting you. Your first reaction focuses on:",
    opts(d, [
        ("a", "The logic of the decision itself — was it the right call?", {d: 1}),
        ("b", "The emotional breach — why didn't they include you?", {d: 5}),
        ("c", "Evaluating the outcome objectively before responding", {d: 1}),
        ("d", "How this makes you feel about the trust in your relationship", {d: 5})
    ]), cg="tf_approach_2"))

# Consistency
questions.append(q(d, "forced_choice",
    "In the end, the best decisions are made with:",
    opts(d, [
        ("a", "A clear head, not a bleeding heart", {d: 1}),
        ("b", "Compassion and awareness of how people will be affected", {d: 5})
    ]), tier="consistency_check", cg="tf_decision_1"))

questions.append(q(d, "scenario",
    "You're editing a friend's cover letter. You prioritize:",
    opts(d, [
        ("a", "Accuracy, clarity, and logical structure", {d: 1}),
        ("b", "Capturing their personality and making the reader feel connected", {d: 5}),
        ("c", "Fixing grammar and ensuring professional tone", {d: 2}),
        ("d", "Making it authentic and emotionally compelling", {d: 5})
    ]), cg="tf_approach_3"))

questions.append(q(d, "behavioral_recall",
    "When giving gifts, you tend to choose based on:",
    opts(d, [
        ("a", "What's practical and useful for the person", {d: 1}),
        ("b", "What will make them feel most loved and understood", {d: 5}),
        ("c", "Research into what's the best value or highest quality", {d: 1}),
        ("d", "An emotional connection — something that shows you truly know them", {d: 5})
    ]), cg="tf_support_2"))

# ============================================================
# JUDGING / PERCEIVING (25 questions)
# ============================================================
d = "judging_perceiving"

questions.append(q(d, "scenario",
    "You have a two-week vacation coming up. Your approach to planning is:",
    opts(d, [
        ("a", "Detailed itinerary with reservations, timelines, and backup plans", {d: 1}),
        ("b", "Book the flights and figure out the rest when you get there", {d: 5}),
        ("c", "A loose outline with a few key activities planned", {d: 3}),
        ("d", "No plan — spontaneity is the point of vacation", {d: 5})
    ]), cg="jp_planning_1"))

questions.append(q(d, "behavioral_recall",
    "Your workspace typically looks:",
    opts(d, [
        ("a", "Organized with everything in its place", {d: 1}),
        ("b", "Creatively chaotic — you know where everything is", {d: 5}),
        ("c", "Clean on the surface, drawers are another story", {d: 3}),
        ("d", "It varies — sometimes tidy, sometimes a mess", {d: 4})
    ]), cg="jp_environment_1"))

questions.append(q(d, "forced_choice",
    "Which sounds more like your natural tendency?",
    opts(d, [
        ("a", "I feel satisfied when I make a decision and move forward", {d: 1}),
        ("b", "I feel energized when I keep my options open", {d: 5})
    ]), cg="jp_closure_1"))

questions.append(q(d, "scenario",
    "A deadline is two weeks away. You:",
    opts(d, [
        ("a", "Break it into milestones and start immediately", {d: 1}),
        ("b", "Think about it periodically and do most of the work in the last few days", {d: 5}),
        ("c", "Create a plan but don't stress if you deviate from it", {d: 3}),
        ("d", "Work in bursts of inspiration whenever they hit", {d: 5})
    ]), cg="jp_deadline_1"))

questions.append(q(d, "behavioral_recall",
    "When it comes to daily routines, you:",
    opts(d, [
        ("a", "Thrive on consistent routines — they make you productive", {d: 1}),
        ("b", "Find routines stifling and prefer each day to unfold differently", {d: 5}),
        ("c", "Have some routines but break them easily", {d: 3}),
        ("d", "Wish you had more routine but can't seem to stick to one", {d: 4})
    ]), cg="jp_routine_1"))

questions.append(q(d, "scenario",
    "You're at the grocery store. You:",
    opts(d, [
        ("a", "Have a list organized by aisle and stick to it", {d: 1}),
        ("b", "Browse and buy whatever looks good in the moment", {d: 5}),
        ("c", "Have a mental list of essentials but impulse-buy some extras", {d: 3}),
        ("d", "Forget the list at home but remember most of what you need", {d: 4})
    ]), cg="jp_planning_2"))

questions.append(q(d, "forced_choice",
    "Which statement is more true for you?",
    opts(d, [
        ("a", "I prefer to decide quickly and commit", {d: 1}),
        ("b", "I prefer to gather more information before deciding", {d: 5})
    ]), cg="jp_closure_1"))

questions.append(q(d, "somatic",
    "When plans change unexpectedly, your body's response is:",
    opts(d, [
        ("a", "Tension and frustration — you had a plan for a reason", {d: 1}),
        ("b", "A spark of excitement — new possibilities!", {d: 5}),
        ("c", "Brief annoyance that quickly fades", {d: 2}),
        ("d", "Relief — the old plan felt constraining anyway", {d: 5})
    ]), cg="jp_somatic_1"))

questions.append(q(d, "behavioral_recall",
    "How do you handle your email inbox?",
    opts(d, [
        ("a", "Process and organize daily — inbox zero or close to it", {d: 1}),
        ("b", "Thousands of unread — you search when you need something", {d: 5}),
        ("c", "Read important ones promptly, let others pile up", {d: 3}),
        ("d", "It goes through cycles of organization and chaos", {d: 4})
    ]), cg="jp_organization_1"))

questions.append(q(d, "scenario",
    "You're working on a report and discover interesting tangential information. You:",
    opts(d, [
        ("a", "Note it for later and stay focused on the current task", {d: 1}),
        ("b", "Follow the rabbit hole — this could be valuable", {d: 5}),
        ("c", "Quickly assess if it's relevant, then decide", {d: 2}),
        ("d", "Get absorbed in it for an hour before remembering the report", {d: 5})
    ]), cg="jp_focus_1"))

questions.append(q(d, "temporal",
    "Looking at your life, major decisions have typically been:",
    opts(d, [
        ("a", "Planned and deliberate — you researched and prepared", {d: 1}),
        ("b", "Spontaneous — you jumped when it felt right", {d: 5}),
        ("c", "A mix — some planned, some serendipitous", {d: 3}),
        ("d", "Delayed until circumstances forced a choice", {d: 4})
    ]), cg="jp_temporal_1"))

questions.append(q(d, "forced_choice",
    "Your closet is more likely to be:",
    opts(d, [
        ("a", "Sorted by type, color, or season", {d: 1}),
        ("b", "A general area where clean clothes end up", {d: 5})
    ]), cg="jp_organization_2"))

questions.append(q(d, "scenario",
    "A friend proposes a road trip starting tomorrow. You:",
    opts(d, [
        ("a", "Check your calendar — you probably can't rearrange on such short notice", {d: 1}),
        ("b", "Say yes immediately — life is short", {d: 5}),
        ("c", "Ask for a few hours to figure out logistics", {d: 2}),
        ("d", "Love the idea and start throwing things in a bag", {d: 5})
    ]), cg="jp_spontaneous_1"))

questions.append(q(d, "behavioral_recall",
    "When starting a new project, you:",
    opts(d, [
        ("a", "Create a detailed plan with milestones before doing any work", {d: 1}),
        ("b", "Dive in and figure out the structure as you go", {d: 5}),
        ("c", "Outline the key phases loosely, then start", {d: 3}),
        ("d", "Procrastinate on planning because you'd rather just do it", {d: 5})
    ]), cg="jp_approach_1"))

questions.append(q(d, "scenario",
    "You have three tasks to complete today. You:",
    opts(d, [
        ("a", "Prioritize them and work through in order", {d: 1}),
        ("b", "Work on whichever one you feel drawn to at the moment", {d: 5}),
        ("c", "Do the hardest one first to get it out of the way", {d: 1}),
        ("d", "Switch between them based on energy and interest", {d: 4})
    ]), cg="jp_approach_2"))

# Trap
questions.append(q(d, "behavioral_recall",
    "Be completely honest: how often do you meet deadlines?",
    opts(d, [
        ("a", "Always — missing a deadline is nearly unthinkable", {d: 1}),
        ("b", "Usually, but I sometimes need extensions", {d: 3}),
        ("c", "I often finish just in time or slightly late", {d: 4}),
        ("d", "Deadlines are guidelines — the work is done when it's done", {d: 5})
    ]), tier="trap", opacity=0.3, sd_trap=True, cg="jp_trap_1"))

questions.append(q(d, "somatic",
    "When you have nothing planned for a day, you feel:",
    opts(d, [
        ("a", "Uncomfortable — unstructured time feels wasted", {d: 1}),
        ("b", "Free and energized — the day is full of potential", {d: 5}),
        ("c", "A mild urge to create some structure or a to-do list", {d: 2}),
        ("d", "Delighted — your best days are unplanned ones", {d: 5})
    ]), cg="jp_somatic_2"))

questions.append(q(d, "forced_choice",
    "Which is more stressful?",
    opts(d, [
        ("a", "Having too many unknowns and no clear plan", {d: 1}),
        ("b", "Having every minute scheduled with no flexibility", {d: 5})
    ]), cg="jp_closure_2"))

questions.append(q(d, "behavioral_recall",
    "Your approach to packing for a trip is:",
    opts(d, [
        ("a", "A checklist started days in advance, packed the night before", {d: 1}),
        ("b", "Throw things in a bag an hour before leaving", {d: 5}),
        ("c", "Mental checklist, pack the night before", {d: 2}),
        ("d", "You always forget something — packing is not your strength", {d: 5})
    ]), cg="jp_planning_3"))

questions.append(q(d, "scenario",
    "You're choosing a restaurant for dinner. You:",
    opts(d, [
        ("a", "Already have a reservation at a researched spot", {d: 1}),
        ("b", "Walk around the neighborhood and see what catches your eye", {d: 5}),
        ("c", "Check reviews on your phone and pick the best option", {d: 2}),
        ("d", "Ask the group what they're in the mood for and decide together", {d: 3})
    ]), cg="jp_spontaneous_2"))

questions.append(q(d, "temporal",
    "Over the years, your relationship with deadlines has:",
    opts(d, [
        ("a", "Always been strong — you plan ahead and deliver early", {d: 1}),
        ("b", "Always been loose — you work best under last-minute pressure", {d: 5}),
        ("c", "Improved — you've learned to plan better over time", {d: 2}),
        ("d", "Stayed the same — you're consistent regardless", {d: 3})
    ]), cg="jp_temporal_2"))

# Consistency
questions.append(q(d, "forced_choice",
    "Honestly, surprises are:",
    opts(d, [
        ("a", "Generally unwelcome — I prefer to know what's coming", {d: 1}),
        ("b", "Generally exciting — I love the unexpected", {d: 5})
    ]), tier="consistency_check", cg="jp_closure_2"))

questions.append(q(d, "scenario",
    "Your partner suggests changing dinner plans at the last minute. You:",
    opts(d, [
        ("a", "Feel a twinge of frustration — you'd already mentally committed", {d: 1}),
        ("b", "Easily adapt — flexibility is a strength", {d: 5}),
        ("c", "Go along but quietly feel your plans were disrespected", {d: 1}),
        ("d", "Feel energized by the change — the new plan might be better", {d: 5})
    ]), cg="jp_flexibility_1"))

questions.append(q(d, "behavioral_recall",
    "How would you describe your relationship with to-do lists?",
    opts(d, [
        ("a", "Essential — I use them daily and check things off religiously", {d: 1}),
        ("b", "I make them sometimes but rarely follow them", {d: 4}),
        ("c", "I keep one but it's more of a brain dump than a strict plan", {d: 3}),
        ("d", "To-do lists feel constraining — I prefer to go with the flow", {d: 5})
    ]), cg="jp_organization_3"))

questions.append(q(d, "scenario",
    "You're packing for a move to a new apartment. Your approach is:",
    opts(d, [
        ("a", "Labeled boxes, room-by-room, weeks in advance", {d: 1}),
        ("b", "Throw everything in boxes the day before", {d: 5}),
        ("c", "Start organized, devolve into chaos by the end", {d: 3}),
        ("d", "Pack as you go over a few weeks, no real system", {d: 4})
    ]), cg="jp_planning_4"))

# ============================================================
# COGNITIVE FUNCTIONS - DOMINANT (25 questions)
# ============================================================
d = "cognitive_functions_dominant"

questions.append(q(d, "scenario",
    "You're faced with a complex problem at work. Your FIRST instinctive response — before any deliberate thinking — is to:",
    opts(d, [
        ("a", "Categorize it logically and build a framework for analysis (Ti)", {d: 1, "thinking_feeling": 1}),
        ("b", "Consider how it affects people and what values are at stake (Fi)", {d: 2, "thinking_feeling": 5}),
        ("c", "Look for established best practices and proven solutions (Si)", {d: 3, "sensing_intuition": 1}),
        ("d", "See the hidden patterns and imagine novel solutions (Ni)", {d: 4, "sensing_intuition": 5})
    ]), cg="cf_dom_1", tags=["mbti_style", "cognitive_functions"]))

questions.append(q(d, "behavioral_recall",
    "When you're in your element — fully engaged and performing at your best — you're typically:",
    opts(d, [
        ("a", "Organizing the external world efficiently: plans, systems, delegation (Te)", {d: 5}),
        ("b", "Connecting with people, creating harmony, understanding group dynamics (Fe)", {d: 6}),
        ("c", "Responding to the immediate environment with skill and precision (Se)", {d: 7}),
        ("d", "Generating possibilities and connections between seemingly unrelated ideas (Ne)", {d: 8})
    ]), cg="cf_dom_2", tags=["mbti_style", "cognitive_functions"]))

questions.append(q(d, "forced_choice",
    "Which internal process feels most natural — like your default mode?",
    opts(d, [
        ("a", "Analyzing systems: understanding how things work internally, finding logical inconsistencies", {d: 1}),
        ("b", "Evaluating authenticity: checking if actions align with core values", {d: 2})
    ]), cg="cf_dom_introverted", tags=["mbti_style", "cognitive_functions"]))

questions.append(q(d, "forced_choice",
    "Which external process feels most natural?",
    opts(d, [
        ("a", "Organizing and deciding: structuring the world, making things efficient", {d: 5}),
        ("b", "Connecting and harmonizing: reading people, maintaining relationships", {d: 6})
    ]), cg="cf_dom_extraverted", tags=["mbti_style", "cognitive_functions"]))

questions.append(q(d, "scenario",
    "You're reading about a topic you find fascinating. What captivates you most?",
    opts(d, [
        ("a", "The internal logic and elegant models that explain the phenomenon (Ti)", {d: 1}),
        ("b", "What it reveals about human nature and personal meaning (Fi)", {d: 2}),
        ("c", "The concrete facts, history, and reliable evidence (Si)", {d: 3}),
        ("d", "The future implications and where this trend is heading (Ni)", {d: 4})
    ]), cg="cf_dom_3", tags=["mbti_style", "cognitive_functions"]))

questions.append(q(d, "scenario",
    "In a group discussion, your natural role tends to be:",
    opts(d, [
        ("a", "The one who organizes the conversation and drives toward decisions (Te)", {d: 5}),
        ("b", "The one who ensures everyone is heard and conflicts are resolved (Fe)", {d: 6}),
        ("c", "The one who notices what's happening right now and responds in real time (Se)", {d: 7}),
        ("d", "The one who generates ideas and explores possibilities (Ne)", {d: 8})
    ]), cg="cf_dom_4", tags=["mbti_style", "cognitive_functions"]))

questions.append(q(d, "somatic",
    "When you encounter information that contradicts something you believe, your immediate internal response is:",
    opts(d, [
        ("a", "An intellectual puzzle to solve — does this break my model? (Ti)", {d: 1}),
        ("b", "A gut check — does this feel right based on my values? (Fi)", {d: 2}),
        ("c", "Skepticism — what's the source and track record? (Si)", {d: 3}),
        ("d", "A flash of insight — what if this changes everything? (Ni)", {d: 4})
    ]), cg="cf_dom_5", tags=["mbti_style", "cognitive_functions"]))

questions.append(q(d, "behavioral_recall",
    "When making a major purchase, your process is most like:",
    opts(d, [
        ("a", "Comparing specs, reading reviews, optimizing for best value (Te)", {d: 5}),
        ("b", "Asking friends and family, considering what will please everyone (Fe)", {d: 6}),
        ("c", "Trying it in person — touching, testing, experiencing it directly (Se)", {d: 7}),
        ("d", "Exploring all possible options, even ones you hadn't considered (Ne)", {d: 8})
    ]), cg="cf_dom_6", tags=["mbti_style", "cognitive_functions"]))

questions.append(q(d, "scenario",
    "A friend comes to you with a personal dilemma. Your instinct is to:",
    opts(d, [
        ("a", "Help them think through it logically, mapping out options and consequences (Ti/Te)", {d: 1}),
        ("b", "Ask how they feel about it and help them find what resonates with their values (Fi/Fe)", {d: 2}),
        ("c", "Draw on your own similar experiences to offer practical guidance (Si/Se)", {d: 3}),
        ("d", "Help them see new perspectives and possibilities they haven't considered (Ni/Ne)", {d: 4})
    ]), cg="cf_dom_7", tags=["mbti_style", "cognitive_functions"]))

questions.append(q(d, "temporal",
    "When you think about your personal growth over the last five years, you notice you've most developed your ability to:",
    opts(d, [
        ("a", "Build systematic understanding and precise internal models (Ti)", {d: 1}),
        ("b", "Know yourself deeply and stay true to your authentic values (Fi)", {d: 2}),
        ("c", "Draw on accumulated experience to make reliable judgments (Si)", {d: 3}),
        ("d", "Foresee outcomes and trust your long-range vision (Ni)", {d: 4})
    ]), cg="cf_dom_temporal_1", tags=["mbti_style", "cognitive_functions"]))

questions.append(q(d, "forced_choice",
    "Which criticism would sting more?",
    opts(d, [
        ("a", "\"Your logic doesn't hold up\" (Ti/Te vulnerability)", {d: 1}),
        ("b", "\"You don't really care about people\" (Fi/Fe vulnerability)", {d: 2})
    ]), cg="cf_dom_vulnerability", tags=["mbti_style", "cognitive_functions"]))

questions.append(q(d, "forced_choice",
    "Which criticism would sting more?",
    opts(d, [
        ("a", "\"You're out of touch with reality\" (Si/Se vulnerability)", {d: 3}),
        ("b", "\"You have no vision or imagination\" (Ni/Ne vulnerability)", {d: 4})
    ]), cg="cf_dom_vulnerability_2", tags=["mbti_style", "cognitive_functions"]))

questions.append(q(d, "scenario",
    "You're leading a new initiative. Your first priority is:",
    opts(d, [
        ("a", "Create a clear structure, metrics, and accountability system (Te)", {d: 5}),
        ("b", "Get team buy-in and ensure everyone feels motivated (Fe)", {d: 6}),
        ("c", "Assess current resources and build on what's already working (Se/Si)", {d: 3}),
        ("d", "Brainstorm all possible approaches before committing to one (Ne)", {d: 8})
    ]), cg="cf_dom_8", tags=["mbti_style", "cognitive_functions"]))

questions.append(q(d, "behavioral_recall",
    "In conversations, you naturally tend to:",
    opts(d, [
        ("a", "Debate ideas and test logical consistency (Ti)", {d: 1}),
        ("b", "Explore what things mean personally and emotionally (Fi)", {d: 2}),
        ("c", "Reference past experiences and established knowledge (Si)", {d: 3}),
        ("d", "Make leaps and connections that surprise others (Ni/Ne)", {d: 4})
    ]), cg="cf_dom_9", tags=["mbti_style", "cognitive_functions"]))

questions.append(q(d, "scenario",
    "You're in a meeting that's going nowhere. You:",
    opts(d, [
        ("a", "Take charge: 'Here's what we need to decide and here's how' (Te)", {d: 5}),
        ("b", "Address the group dynamic: 'I sense some unspoken concerns' (Fe)", {d: 6}),
        ("c", "Ground it: 'Let's focus on what's actually happening right now' (Se)", {d: 7}),
        ("d", "Redirect: 'What if we're asking the wrong question entirely?' (Ne)", {d: 8})
    ]), cg="cf_dom_10", tags=["mbti_style", "cognitive_functions"]))

questions.append(q(d, "somatic",
    "When you use your dominant cognitive mode, you physically feel:",
    opts(d, [
        ("a", "Sharp and precise — like a well-oiled machine (T functions)", {d: 1}),
        ("b", "Warm and resonant — deeply connected to meaning (F functions)", {d: 2}),
        ("c", "Grounded and present — plugged into reality (S functions)", {d: 3}),
        ("d", "Electric and expansive — like your mind is reaching outward (N functions)", {d: 4})
    ]), cg="cf_dom_somatic", tags=["mbti_style", "cognitive_functions"]))

questions.append(q(d, "scenario",
    "You're reviewing someone's work. You instinctively focus on:",
    opts(d, [
        ("a", "Internal consistency — does the logic hold together? (Ti)", {d: 1}),
        ("b", "Authenticity — does it ring true? (Fi)", {d: 2}),
        ("c", "Accuracy — are the facts correct and the details right? (Si)", {d: 3}),
        ("d", "Vision — does it point toward something meaningful? (Ni)", {d: 4})
    ]), cg="cf_dom_11", tags=["mbti_style", "cognitive_functions"]))

questions.append(q(d, "behavioral_recall",
    "When stressed, you tend to rely more heavily on:",
    opts(d, [
        ("a", "Over-analyzing everything to the point of paralysis (Ti grip)", {d: 1}),
        ("b", "Withdrawing into intense personal feelings (Fi grip)", {d: 2}),
        ("c", "Clinging to familiar routines or past precedents (Si grip)", {d: 3}),
        ("d", "Fixating on a single vision of how things should unfold (Ni grip)", {d: 4})
    ]), cg="cf_dom_stress", tags=["mbti_style", "cognitive_functions"]))

questions.append(q(d, "scenario",
    "You witness a heated argument between two people you respect. Your instinct is to:",
    opts(d, [
        ("a", "Evaluate which person's argument is more logically sound (Ti/Te)", {d: 1}),
        ("b", "Understand each person's feelings and try to bridge the gap (Fi/Fe)", {d: 2}),
        ("c", "Focus on the specific facts of the disagreement (Si/Se)", {d: 3}),
        ("d", "Reframe the argument by finding a higher-level perspective (Ni/Ne)", {d: 4})
    ]), cg="cf_dom_12", tags=["mbti_style", "cognitive_functions"]))

questions.append(q(d, "forced_choice",
    "When you're at your worst, you're more likely to:",
    opts(d, [
        ("a", "Become cold, dismissive, and overly critical (T shadow)", {d: 1}),
        ("b", "Become oversensitive, moody, and take everything personally (F shadow)", {d: 2})
    ]), cg="cf_dom_shadow", tags=["mbti_style", "cognitive_functions"]))

questions.append(q(d, "forced_choice",
    "When you're at your worst, you're more likely to:",
    opts(d, [
        ("a", "Become rigid, obsessive about details, and unable to adapt (S shadow)", {d: 3}),
        ("b", "Become scattered, unrealistic, and disconnected from practical reality (N shadow)", {d: 4})
    ]), cg="cf_dom_shadow_2", tags=["mbti_style", "cognitive_functions"]))

questions.append(q(d, "temporal",
    "Over your lifetime, your greatest cognitive strength has been:",
    opts(d, [
        ("a", "Building elegant systems of understanding that work reliably (Ti)", {d: 1}),
        ("b", "Understanding people at a level that surprises them (Fi/Fe)", {d: 2}),
        ("c", "Remembering and applying lessons from experience (Si)", {d: 3}),
        ("d", "Seeing what others miss — patterns, connections, futures (Ni/Ne)", {d: 4})
    ]), cg="cf_dom_lifetime", tags=["mbti_style", "cognitive_functions"]))

questions.append(q(d, "scenario",
    "You're told your approach to a project is wrong and need to start over. You:",
    opts(d, [
        ("a", "Ask for specific logical reasons — you need to understand WHY (Ti)", {d: 1}),
        ("b", "Feel personally hurt but try to understand the feedback through your values (Fi)", {d: 2}),
        ("c", "Review what you did step by step to find where it went wrong (Si)", {d: 3}),
        ("d", "Immediately start generating alternative approaches (Ne)", {d: 8})
    ]), cg="cf_dom_13", tags=["mbti_style", "cognitive_functions"]))

# Trap
questions.append(q(d, "scenario",
    "When someone describes you as 'a thinker' or 'a feeler,' you:",
    opts(d, [
        ("a", "Know exactly which one you are — it's obvious to you", {d: 1}),
        ("b", "Feel like both apply depending on the context", {d: 3}),
        ("c", "Think the distinction is too simplistic", {d: 2}),
        ("d", "Don't care about labels — you just do what works", {d: 3})
    ]), tier="trap", opacity=0.3, sd_trap=True, cg="cf_trap_1", tags=["mbti_style", "cognitive_functions"]))

questions.append(q(d, "behavioral_recall",
    "The type of learning you find most effortless is:",
    opts(d, [
        ("a", "Theoretical frameworks and abstract models (Ti/Ni)", {d: 1}),
        ("b", "Interpersonal skills and reading people (Fe/Fi)", {d: 2}),
        ("c", "Practical skills learned through hands-on practice (Se/Si)", {d: 3}),
        ("d", "Creative problem-solving and generating novel ideas (Ne)", {d: 8})
    ]), cg="cf_dom_14", tags=["mbti_style", "cognitive_functions"]))

# ============================================================
# COGNITIVE FUNCTIONS - AUXILIARY (25 questions)
# ============================================================
d = "cognitive_functions_auxiliary"

questions.append(q(d, "scenario",
    "After making a decision using your primary approach, you then typically:",
    opts(d, [
        ("a", "Double-check the logic and make sure it's internally consistent (Ti support)", {d: 1}),
        ("b", "Consider how people will be affected emotionally (Fe/Fi support)", {d: 2}),
        ("c", "Verify against past experience and established facts (Si support)", {d: 3}),
        ("d", "Explore what possibilities this decision opens up (Ne support)", {d: 4})
    ]), cg="cf_aux_1", tags=["mbti_style", "cognitive_functions"]))

questions.append(q(d, "behavioral_recall",
    "When your primary instinct leads you astray, you recover by:",
    opts(d, [
        ("a", "Stepping back to organize and create clear action steps (Te recovery)", {d: 5}),
        ("b", "Checking in with trusted people for perspective (Fe recovery)", {d: 6}),
        ("c", "Grounding yourself in what's concretely happening right now (Se recovery)", {d: 7}),
        ("d", "Brainstorming alternative interpretations and options (Ne recovery)", {d: 8})
    ]), cg="cf_aux_2", tags=["mbti_style", "cognitive_functions"]))

questions.append(q(d, "forced_choice",
    "Your secondary strength — the skill you call on to balance your dominant approach — is more:",
    opts(d, [
        ("a", "Analytical: organizing, evaluating, or systematic thinking", {d: 1}),
        ("b", "Relational: understanding people, values, and emotional dynamics", {d: 2})
    ]), cg="cf_aux_balance_1", tags=["mbti_style", "cognitive_functions"]))

questions.append(q(d, "forced_choice",
    "Your secondary strength is more:",
    opts(d, [
        ("a", "Concrete: grounded in reality, experience, and practical detail", {d: 3}),
        ("b", "Abstract: oriented toward possibilities, patterns, and future vision", {d: 4})
    ]), cg="cf_aux_balance_2", tags=["mbti_style", "cognitive_functions"]))

questions.append(q(d, "scenario",
    "You're mentoring someone younger. Beyond your main approach, you find yourself also teaching them to:",
    opts(d, [
        ("a", "Think critically and question assumptions (Ti auxiliary)", {d: 1}),
        ("b", "Stay true to their own values and feelings (Fi auxiliary)", {d: 2}),
        ("c", "Build on what they already know and what works (Si auxiliary)", {d: 3}),
        ("d", "See the long game and trust their deeper insights (Ni auxiliary)", {d: 4})
    ]), cg="cf_aux_3", tags=["mbti_style", "cognitive_functions"]))

questions.append(q(d, "behavioral_recall",
    "When your primary mode is in overdrive, you balance it by:",
    opts(d, [
        ("a", "Getting practical: making lists, creating timelines, executing (Te balance)", {d: 5}),
        ("b", "Connecting with others: talking it through, seeking harmony (Fe balance)", {d: 6}),
        ("c", "Getting physical: exercising, cooking, engaging your senses (Se balance)", {d: 7}),
        ("d", "Exploring: reading widely, brainstorming, following curiosity (Ne balance)", {d: 8})
    ]), cg="cf_aux_4", tags=["mbti_style", "cognitive_functions"]))

questions.append(q(d, "scenario",
    "You've made a strong first impression judgment about a new situation. You then:",
    opts(d, [
        ("a", "Test your judgment against logical criteria (Ti check)", {d: 1}),
        ("b", "Consult your personal value system — does this feel right? (Fi check)", {d: 2}),
        ("c", "Compare it to past experiences with similar situations (Si check)", {d: 3}),
        ("d", "Let your mind wander to see what other insights emerge (Ni/Ne check)", {d: 4})
    ]), cg="cf_aux_5", tags=["mbti_style", "cognitive_functions"]))

questions.append(q(d, "temporal",
    "As you've matured, the skill you've most needed to develop alongside your natural strength is:",
    opts(d, [
        ("a", "Being more organized, decisive, and action-oriented (Te growth)", {d: 5}),
        ("b", "Being more empathetic and attuned to social dynamics (Fe growth)", {d: 6}),
        ("c", "Being more present and engaged with the physical world (Se growth)", {d: 7}),
        ("d", "Being more open to possibilities and creative alternatives (Ne growth)", {d: 8})
    ]), cg="cf_aux_growth", tags=["mbti_style", "cognitive_functions"]))

questions.append(q(d, "scenario",
    "Your dominant approach generates an insight. To make it useful, you then:",
    opts(d, [
        ("a", "Build a logical framework to test and validate it (Ti support)", {d: 1}),
        ("b", "Check it against your deepest values — is this truly important? (Fi support)", {d: 2}),
        ("c", "Ground it in facts and historical precedent (Si support)", {d: 3}),
        ("d", "See where it leads — what else does this connect to? (Ne support)", {d: 4})
    ]), cg="cf_aux_6", tags=["mbti_style", "cognitive_functions"]))

questions.append(q(d, "behavioral_recall",
    "In team settings, your secondary contribution (beyond your main role) is usually:",
    opts(d, [
        ("a", "Bringing structure and efficiency to the group's efforts (Te)", {d: 5}),
        ("b", "Ensuring group cohesion and addressing interpersonal issues (Fe)", {d: 6}),
        ("c", "Keeping things grounded and realistic (Se/Si)", {d: 3}),
        ("d", "Generating alternatives when the group gets stuck (Ne)", {d: 8})
    ]), cg="cf_aux_7", tags=["mbti_style", "cognitive_functions"]))

questions.append(q(d, "forced_choice",
    "If your primary mode is your sword, your auxiliary mode is more like:",
    opts(d, [
        ("a", "A shield — it protects you from your blind spots through logical analysis", {d: 1}),
        ("b", "A compass — it guides you toward what truly matters to people", {d: 2})
    ]), cg="cf_aux_metaphor_1", tags=["mbti_style", "cognitive_functions"]))

questions.append(q(d, "forced_choice",
    "If your primary mode is your sword, your auxiliary mode is more like:",
    opts(d, [
        ("a", "An anchor — it keeps you grounded in reality and experience", {d: 3}),
        ("b", "Wings — it lifts you to see new perspectives and possibilities", {d: 4})
    ]), cg="cf_aux_metaphor_2", tags=["mbti_style", "cognitive_functions"]))

questions.append(q(d, "scenario",
    "You're trying to understand a new person you've met. Your secondary instinct (after your first impression) is to:",
    opts(d, [
        ("a", "Analyze their behavior patterns logically (Ti)", {d: 1}),
        ("b", "Tune into their emotional state and personal values (Fi/Fe)", {d: 2}),
        ("c", "Notice specific details about their appearance, habits, and behavior (Si/Se)", {d: 3}),
        ("d", "Speculate about their deeper motivations and future trajectory (Ni/Ne)", {d: 4})
    ]), cg="cf_aux_8", tags=["mbti_style", "cognitive_functions"]))

questions.append(q(d, "behavioral_recall",
    "The skill that took you the longest to develop but now feels natural is:",
    opts(d, [
        ("a", "Systematic thinking and logical organization (T functions)", {d: 1}),
        ("b", "Emotional awareness and interpersonal sensitivity (F functions)", {d: 2}),
        ("c", "Practical attention to detail and sensory awareness (S functions)", {d: 3}),
        ("d", "Abstract thinking and pattern recognition (N functions)", {d: 4})
    ]), cg="cf_aux_9", tags=["mbti_style", "cognitive_functions"]))

questions.append(q(d, "somatic",
    "When your secondary function activates, it feels like:",
    opts(d, [
        ("a", "Clarity — a second layer of analysis clicking into place", {d: 1}),
        ("b", "Warmth — a caring perspective that enriches your primary view", {d: 2}),
        ("c", "Grounding — coming back to earth from wherever your mind was", {d: 3}),
        ("d", "Expansion — suddenly seeing more than you did a moment ago", {d: 4})
    ]), cg="cf_aux_somatic", tags=["mbti_style", "cognitive_functions"]))

questions.append(q(d, "scenario",
    "You need to explain a complex idea to a group. After organizing your main points, you add:",
    opts(d, [
        ("a", "A logical proof or step-by-step reasoning chain (Ti support)", {d: 1}),
        ("b", "Stories and examples that connect emotionally (Fe/Fi support)", {d: 2}),
        ("c", "Concrete data, specific examples, and real-world evidence (Si/Se support)", {d: 3}),
        ("d", "Surprising connections and provocative 'what ifs' (Ne support)", {d: 4})
    ]), cg="cf_aux_10", tags=["mbti_style", "cognitive_functions"]))

questions.append(q(d, "temporal",
    "A skill that was once awkward for you but now supports you daily is:",
    opts(d, [
        ("a", "Creating efficient systems and holding yourself to standards (Te)", {d: 5}),
        ("b", "Reading social situations and responding with emotional intelligence (Fe)", {d: 6}),
        ("c", "Staying present and responsive to your physical environment (Se)", {d: 7}),
        ("d", "Keeping multiple possibilities alive without rushing to closure (Ne)", {d: 8})
    ]), cg="cf_aux_11", tags=["mbti_style", "cognitive_functions"]))

questions.append(q(d, "behavioral_recall",
    "When you make a mistake, your secondary process helps you by:",
    opts(d, [
        ("a", "Analyzing what went wrong with precise logic (Ti)", {d: 1}),
        ("b", "Reconnecting with your values and what matters (Fi)", {d: 2}),
        ("c", "Drawing on past lessons to avoid repeating the error (Si)", {d: 3}),
        ("d", "Seeing the mistake as part of a bigger pattern or journey (Ni)", {d: 4})
    ]), cg="cf_aux_12", tags=["mbti_style", "cognitive_functions"]))

questions.append(q(d, "scenario",
    "You're crafting an important email. Your first draft reflects your dominant mode. Your revision process involves:",
    opts(d, [
        ("a", "Tightening the logic and removing ambiguity (Ti/Te refinement)", {d: 1}),
        ("b", "Adjusting tone to be more empathetic or authentic (Fi/Fe refinement)", {d: 2}),
        ("c", "Adding specific details, facts, or practical next steps (Si/Se refinement)", {d: 3}),
        ("d", "Expanding to include broader implications or creative angles (Ni/Ne refinement)", {d: 4})
    ]), cg="cf_aux_13", tags=["mbti_style", "cognitive_functions"]))

questions.append(q(d, "forced_choice",
    "People who know you well would say your backup strength is:",
    opts(d, [
        ("a", "Your ability to get things done efficiently and hold people accountable", {d: 5}),
        ("b", "Your warmth and ability to make people feel valued", {d: 6})
    ]), cg="cf_aux_external", tags=["mbti_style", "cognitive_functions"]))

# Trap
questions.append(q(d, "behavioral_recall",
    "Be honest: the cognitive skill you most wish you were better at is:",
    opts(d, [
        ("a", "Cold, objective analysis without emotional interference", {d: 1}),
        ("b", "Deep empathy and emotional attunement", {d: 2}),
        ("c", "Practical, detail-oriented execution", {d: 3}),
        ("d", "Big-picture thinking and creative vision", {d: 4})
    ]), tier="trap", opacity=0.3, sd_trap=True, cg="cf_aux_trap", tags=["mbti_style", "cognitive_functions"]))

questions.append(q(d, "scenario",
    "Your best work typically happens when you combine:",
    opts(d, [
        ("a", "Vision with logical rigor (N + T)", {d: 1}),
        ("b", "Vision with empathetic understanding (N + F)", {d: 2}),
        ("c", "Practical grounding with logical analysis (S + T)", {d: 3}),
        ("d", "Practical grounding with emotional intelligence (S + F)", {d: 6})
    ]), cg="cf_aux_combo", tags=["mbti_style", "cognitive_functions"]))

questions.append(q(d, "behavioral_recall",
    "When you give advice, your secondary voice adds:",
    opts(d, [
        ("a", "Practical steps and concrete suggestions (Te/Se)", {d: 5}),
        ("b", "Emotional validation and relational wisdom (Fe/Fi)", {d: 2}),
        ("c", "Historical context and lessons learned (Si)", {d: 3}),
        ("d", "Creative alternatives they hadn't thought of (Ne)", {d: 8})
    ]), cg="cf_aux_14", tags=["mbti_style", "cognitive_functions"]))

# Consistency
questions.append(q(d, "forced_choice",
    "Your secondary mode — the one that balances your dominant — is more about:",
    opts(d, [
        ("a", "Thinking: analyzing, systematizing, evaluating truth", {d: 1}),
        ("b", "Feeling: valuing, empathizing, evaluating importance", {d: 2})
    ]), tier="consistency_check", cg="cf_aux_balance_1", tags=["mbti_style", "cognitive_functions"]))

questions.append(q(d, "forced_choice",
    "And it's more:",
    opts(d, [
        ("a", "Sensing: concrete, detailed, experience-based", {d: 3}),
        ("b", "Intuiting: abstract, pattern-based, possibility-oriented", {d: 4})
    ]), tier="consistency_check", cg="cf_aux_balance_2", tags=["mbti_style", "cognitive_functions"]))

# Verify we have 150
assert len(questions) == 150, f"Expected 150 questions, got {len(questions)}"

with open("/Users/user/personal/sb/trueassess/priv/question_bank/mbti_style.json", "w") as f:
    json.dump(questions, f, indent=2)

print(f"Written {len(questions)} MBTI-style questions")
