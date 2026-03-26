import json
with open("/Users/user/personal/sb/trueassess/priv/question_bank/power_exchange_depth.json") as f:
    questions = json.load(f)
uid_counter = len(questions) + 1
def q(dim, qtype, text, options, tier_role="core", trap=False, cg=None, opacity=0.6, cross=None, tags=None):
    global uid_counter
    uid = f"pd_{uid_counter:03d}"
    uid_counter += 1
    questions.append({"uid": uid, "assessment_id": "power_exchange_depth", "dimension": dim, "question_type": qtype, "text": text, "options": options, "cross_scores": cross or [], "anti_gaming": {"opacity": opacity, "social_desirability_trap": trap, "consistency_group": cg or f"{dim}_core", "reversal": False}, "cultural_adaptability": {"universal": True, "adaptations_needed": [], "adaptation_notes": None}, "content_rating": "X", "content_categories": ["bdsm", "power_exchange"], "depth_tier": "deep", "tier_role": tier_role, "tags": tags or ["nsfw", "power_exchange", dim]})
def opts(ts):
    return [{"id": chr(97+i), "text": t, "scores": s} for i, (t, s) in enumerate(ts)]

# More lifestyle_vs_bedroom
q("lifestyle_vs_bedroom", "scenario", "Your D/s partner meets your parents. The dynamic is:", opts([
    ("Still present but invisible — I'm subtly aware of our structure even in this context. A touch, a glance, the way we orient around each other", {"lifestyle_vs_bedroom": 5}),
    ("Paused but I feel its absence — I'm aware the dynamic is temporarily muted", {"lifestyle_vs_bedroom": 4}),
    ("Completely off — family contexts and D/s don't mix at all", {"lifestyle_vs_bedroom": 2}),
    ("Not relevant — D/s is sexual and this is a family situation", {"lifestyle_vs_bedroom": 1})
]))

q("lifestyle_vs_bedroom", "forced_choice", "The phrase '24/7 D/s doesn't mean 24/7 play — it means 24/7 awareness of the power structure':", opts([
    ("Exactly right — it's about the persistent awareness of authority and service, not constant scenes", {"lifestyle_vs_bedroom": 5}),
    ("Makes sense — the distinction is important", {"lifestyle_vs_bedroom": 4}),
    ("Still sounds exhausting", {"lifestyle_vs_bedroom": 2}),
    ("It's just semantics — 24/7 anything is unsustainable", {"lifestyle_vs_bedroom": 1})
]))

q("lifestyle_vs_bedroom", "behavioral_recall", "How much of your identity is organized around your D/s role (Dominant, submissive, switch) vs. other identities (professional, parent, friend)?", opts([
    ("D/s is one of my primary identity frameworks — it shapes how I relate to people, how I understand myself, how I structure my closest relationships", {"lifestyle_vs_bedroom": 5}),
    ("Significant — it's a meaningful part of who I am beyond the bedroom", {"lifestyle_vs_bedroom": 4}),
    ("A piece — important but one of many identities", {"lifestyle_vs_bedroom": 3}),
    ("Small — it's an activity, not an identity", {"lifestyle_vs_bedroom": 1})
]))

# More protocol_depth
q("protocol_depth", "scenario", "Your Dominant introduces a new protocol requiring you to text a daily gratitude list of three things you're grateful for in the dynamic. This:", opts([
    ("Creates a beautiful daily practice of mindfulness about our dynamic — I'd do it with genuine reflection", {"protocol_depth": 5}),
    ("Sounds meaningful — a good way to stay connected", {"protocol_depth": 4}),
    ("Sounds like homework", {"protocol_depth": 2}),
    ("Is unnecessary busy-work", {"protocol_depth": 1})
]))

q("protocol_depth", "forced_choice", "Eye contact protocols (lowered eyes, no direct eye contact without permission, or mandatory eye contact when given instructions):", opts([
    ("Deeply impact my headspace — where I look reflects my inner state of surrender or authority", {"protocol_depth": 5}),
    ("Add a nice layer of formality", {"protocol_depth": 4}),
    ("Are too controlling for daily life", {"protocol_depth": 2}),
    ("Are weird", {"protocol_depth": 1})
]))

q("protocol_depth", "temporal", "When protocols have been suspended (travel, illness, visiting family), restarting them feels:", opts([
    ("Like coming home — the first protocol after a break reconnects me to the dynamic and my role instantly", {"protocol_depth": 5}),
    ("Good — I missed the structure", {"protocol_depth": 4}),
    ("Takes adjustment to get back into", {"protocol_depth": 3}),
    ("I wonder why we bother — we were fine without them", {"protocol_depth": 1})
]))

# More service_orientation_depth
q("service_orientation_depth", "scenario", "Sexual service — performing oral sex, preparing your body, maintaining grooming standards — not for your pleasure but as service to your Dominant's preferences:", opts([
    ("Is devotional — preparing my body as they prefer, being sexually available as they require, is the most intimate form of service", {"service_orientation_depth": 5}),
    ("Is arousing and connecting — their preferences shape my sexual presentation", {"service_orientation_depth": 4}),
    ("Is fine within reason", {"service_orientation_depth": 3}),
    ("My body is mine — I groom and present for myself", {"service_orientation_depth": 1})
]))

q("service_orientation_depth", "forced_choice", "The joy of service — genuine, non-transactional pleasure in making someone else's life better:", opts([
    ("Is central to my identity — I feel most myself when I'm serving someone I've chosen", {"service_orientation_depth": 5}),
    ("Is real — I genuinely enjoy service-oriented relating", {"service_orientation_depth": 4}),
    ("Is context-dependent — sometimes I enjoy it, sometimes it feels like obligation", {"service_orientation_depth": 3}),
    ("Is foreign to me — I serve when asked but it doesn't bring me joy", {"service_orientation_depth": 1})
]))

q("service_orientation_depth", "behavioral_recall", "Your most meaningful act of service in a D/s context:", opts([
    ("Was something that required sustained effort, sacrifice, or skill — and the completion of it gave me profound satisfaction", {"service_orientation_depth": 5}),
    ("Was something my partner deeply appreciated", {"service_orientation_depth": 4}),
    ("Was a sexual act they enjoyed", {"service_orientation_depth": 3}),
    ("I don't rank acts of service", {"service_orientation_depth": 1})
]))

# More authority_exchange_comfort
q("authority_exchange_comfort", "scenario", "Your Dominant tells you 'No' about something you want badly (attending an event, buying something, pursuing an opportunity). You:", opts([
    ("Accept it — their 'no' might be based on information I don't have, or it might be arbitrary, and both are within the authority I've granted them", {"authority_exchange_comfort": 5}),
    ("Express my feelings but accept the decision", {"authority_exchange_comfort": 4}),
    ("Push back — this affects my life", {"authority_exchange_comfort": 2}),
    ("Ignore the 'no' — they don't get to veto my desires", {"authority_exchange_comfort": 1})
]))

q("authority_exchange_comfort", "forced_choice", "Consensual authority exchange means:", opts([
    ("I CHOSE to give this person authority. It's not taken or assumed — it's a gift I can revoke. And within the structure we built together, their authority is real", {"authority_exchange_comfort": 5}),
    ("I've agreed to follow their lead in specific areas, with ongoing consent", {"authority_exchange_comfort": 4}),
    ("I go along with it but maintain veto power over everything", {"authority_exchange_comfort": 3}),
    ("Authority exchange is a fantasy — no one really gives up authority", {"authority_exchange_comfort": 1})
]))

q("authority_exchange_comfort", "somatic", "When you fully surrender to a Dominant's authority — not in a scene, but in a life decision — your body:", opts([
    ("Releases into trust — there's a physical relief in not carrying the weight of decision. Surrender isn't weakness, it's purposeful release", {"authority_exchange_comfort": 5}),
    ("Feels somewhat lighter — sharing the load helps", {"authority_exchange_comfort": 4}),
    ("Stays tense — I'm yielding but my body doesn't agree", {"authority_exchange_comfort": 2}),
    ("Fights it — my autonomic response rejects authority over my life", {"authority_exchange_comfort": 1})
]))

# More trust_calibration
q("trust_calibration", "scenario", "A Dominant says all the right things — articulate, experienced, claims deep commitment to consent. But something feels off in your gut. You:", opts([
    ("Trust my gut over their words — instinct picks up on things logic misses. I slow down or walk away, even if I can't articulate why", {"trust_calibration": 5}),
    ("Proceed with extra caution — gut feelings deserve attention", {"trust_calibration": 4}),
    ("Override my gut — they're saying the right things, I'm probably being paranoid", {"trust_calibration": 2}),
    ("Ignore feelings — focus on what they say and do", {"trust_calibration": 1})
]))

q("trust_calibration", "behavioral_recall", "How do you verify that a potential D/s partner is trustworthy beyond what they tell you?", opts([
    ("Multiple methods: community references, watching them interact with others, observing consistency between words and actions over time, testing small trust before extending larger trust", {"trust_calibration": 5}),
    ("References and observation — I ask around and watch carefully", {"trust_calibration": 4}),
    ("Extended conversation — I trust my read of people", {"trust_calibration": 3}),
    ("I take them at face value", {"trust_calibration": 1})
]))

q("trust_calibration", "forced_choice", "Trust and control in D/s:", opts([
    ("Are paradoxically linked: the deeper I trust, the more control I can surrender — AND the deeper trust IS, the less it looks like 'giving up control' and more like 'choosing to flow with someone I believe in'", {"trust_calibration": 5}),
    ("Are closely related — trust enables control exchange", {"trust_calibration": 4}),
    ("Are somewhat separate — I can submit to control without deep trust if the boundaries are clear", {"trust_calibration": 2}),
    ("Are separate — control dynamics don't require personal trust", {"trust_calibration": 1})
]))

# More dynamic_health
q("dynamic_health", "scenario", "Your D/s dynamic has become stale — same scenes, same protocols, same energy. You:", opts([
    ("Initiate a state-of-the-dynamic conversation: 'Our dynamic needs evolution. Let's talk about what we both want more of, less of, and what new territory we want to explore.' Growth or death — those are the options", {"dynamic_health": 5}),
    ("Suggest new activities or adjustments", {"dynamic_health": 4}),
    ("Accept it — this is the mature phase of the dynamic", {"dynamic_health": 2}),
    ("Lose interest — if the dynamic is stale, it's over", {"dynamic_health": 1})
]))

q("dynamic_health", "forced_choice", "Regular 'state of the dynamic' conversations — scheduled check-ins about how the D/s structure is serving both people:", opts([
    ("Non-negotiable in any serious dynamic — this is how you prevent drift, resentment, and unhealthy patterns from calcifying", {"dynamic_health": 5}),
    ("Important — I believe in periodic check-ins", {"dynamic_health": 4}),
    ("Unnecessary if things are going well", {"dynamic_health": 2}),
    ("Undermine the dynamic — too much analysis kills the energy", {"dynamic_health": 1})
]))

q("dynamic_health", "behavioral_recall", "Have you ever ended or restructured a D/s dynamic because it became unhealthy, even though you still had feelings for the person?", opts([
    ("Yes — I prioritize the health of the dynamic and my own wellbeing over the comfort of staying. Ending an unhealthy dynamic is a form of self-respect", {"dynamic_health": 5}),
    ("Yes — it was hard but necessary", {"dynamic_health": 4}),
    ("I've stayed in unhealthy dynamics longer than I should have", {"dynamic_health": 2}),
    ("I've never assessed a dynamic as 'unhealthy'", {"dynamic_health": 1})
]))

q("dynamic_health", "scenario", "Your submissive asks for a break from the dynamic — not ending it, just pausing. You:", opts([
    ("Respect it immediately: 'Of course. What do you need? How can I support you during this pause?' A dynamic should never feel like a trap", {"dynamic_health": 5}),
    ("Agree, though I feel sad about it", {"dynamic_health": 4}),
    ("Feel threatened — is this the beginning of the end?", {"dynamic_health": 2}),
    ("Refuse — you don't get to pause a dynamic unilaterally", {"dynamic_health": 1})
]), tier_role="trap", trap=True)

# More negotiation_skill
q("negotiation_skill", "scenario", "Your partner's hard limit conflicts with your deep desire (e.g., they won't do anal, and that's important to you). In negotiation, you:", opts([
    ("Accept it cleanly: 'That's your limit and I respect it completely. Let me think about whether I can be fulfilled without it, and I'll be honest with you about that.' No pressure, no guilt, clear communication", {"negotiation_skill": 5}),
    ("Accept the limit and find alternative ways to meet the underlying need", {"negotiation_skill": 4}),
    ("Accept but revisit periodically", {"negotiation_skill": 2}),
    ("Try to convince them", {"negotiation_skill": 1})
]), tier_role="trap", trap=True)

q("negotiation_skill", "forced_choice", "Negotiation as ongoing vs. one-time:", opts([
    ("Ongoing — initial negotiation sets the baseline, but every scene, every week, every month involves renegotiation as people change, grow, and discover new things", {"negotiation_skill": 5}),
    ("Mostly initial with updates — major changes get renegotiated", {"negotiation_skill": 4}),
    ("Initial negotiation covers it — updates only when something breaks", {"negotiation_skill": 2}),
    ("Once is enough — renegotiation feels like they're not happy", {"negotiation_skill": 1})
]))

q("negotiation_skill", "behavioral_recall", "How well can you articulate not just your LIMITS but your DESIRES — what you actively want, what lights you up, what you're seeking?", opts([
    ("Precisely — I can describe my desires with as much clarity as my limits. 'I want X because it makes me feel Y, and the specific version I'm craving involves Z'", {"negotiation_skill": 5}),
    ("Fairly well — I know what I want even if articulating it takes effort", {"negotiation_skill": 4}),
    ("Limits are clearer than desires — I know what I don't want better than what I do", {"negotiation_skill": 3}),
    ("I struggle with both", {"negotiation_skill": 1})
]))

# More aftercare_practice
q("aftercare_practice", "scenario", "Aftercare for a partner who dissociated during a scene:", opts([
    ("I know the signs (glazed eyes, non-responsiveness, emotional flatness) and have a protocol: ground them physically (firm touch, blanket, temperature change), name reality ('you're safe, I'm here, this is [location]'), don't rush, don't leave, debrief when they're ready", {"aftercare_practice": 5}),
    ("I'd recognize it and provide grounding — this needs special attention", {"aftercare_practice": 4}),
    ("I'd notice something was off but might not know what to do", {"aftercare_practice": 3}),
    ("I wouldn't necessarily recognize dissociation", {"aftercare_practice": 1})
]))

q("aftercare_practice", "forced_choice", "Aftercare that extends beyond the immediate post-scene period:", opts([
    ("Is essential — next-day check-in texts, 48-hour mood monitoring, scheduled debrief if the scene was intense. Aftercare isn't just the first 30 minutes", {"aftercare_practice": 5}),
    ("Is important for intense scenes — I check in the next day", {"aftercare_practice": 4}),
    ("Isn't something I've practiced — aftercare is immediate", {"aftercare_practice": 3}),
    ("Is overkill — if you need multi-day aftercare, the scene was too much", {"aftercare_practice": 1})
]))

q("aftercare_practice", "behavioral_recall", "Have you ever provided aftercare to someone who wasn't your play partner (a friend at a party who had a hard scene with someone else)?", opts([
    ("Yes — community care is part of being a responsible kink community member. I'll blanket-and-water anyone who needs it", {"aftercare_practice": 5}),
    ("Yes — I've stepped in when someone needed support", {"aftercare_practice": 4}),
    ("No — aftercare is between play partners", {"aftercare_practice": 3}),
    ("No — not my responsibility", {"aftercare_practice": 1})
]))

q("aftercare_practice", "scenario", "Aftercare journaling — writing about your experience after a scene:", opts([
    ("Is part of my practice — processing scenes through writing helps me understand my reactions, identify patterns, and communicate with my partner", {"aftercare_practice": 5}),
    ("I've done it and found it valuable", {"aftercare_practice": 4}),
    ("Interesting idea but I haven't tried it", {"aftercare_practice": 3}),
    ("Overthinking it — scenes don't need written analysis", {"aftercare_practice": 1})
]))

# Cross-dimensional consistency checks
q("lifestyle_vs_bedroom", "scenario", "D/s during conflict — when you and your partner are fighting, the power dynamic:", opts([
    ("Provides a framework for resolution — the structure doesn't dissolve during conflict, it helps us navigate it", {"lifestyle_vs_bedroom": 5}),
    ("May pause temporarily but resumes once the conflict is resolved", {"lifestyle_vs_bedroom": 4}),
    ("Dissolves — you can't maintain D/s while genuinely angry", {"lifestyle_vs_bedroom": 2}),
    ("Is part of the problem — power dynamics make conflict worse", {"lifestyle_vs_bedroom": 1})
]))

q("protocol_depth", "scenario", "Your Dominant adds a daily journaling requirement — you must write about your emotional state, your obedience, and your service each day. This:", opts([
    ("Is powerful self-awareness tool wrapped in service — writing forces reflection and gives them insight into my inner world", {"protocol_depth": 5}),
    ("Is a meaningful addition — I'd do it honestly", {"protocol_depth": 4}),
    ("Is a lot — daily feels excessive", {"protocol_depth": 2}),
    ("Is invasive — my inner world is my own", {"protocol_depth": 1})
]))

q("trust_calibration", "scenario", "You discover your Dominant discussed a private scene detail with a friend without your consent. You:", opts([
    ("Address it as a trust violation with specific consequences: 'What happened between us is confidential unless we agree otherwise. You violated that, and here's what I need to rebuild trust: [specific expectations]'", {"trust_calibration": 5}),
    ("Express displeasure and establish a confidentiality boundary going forward", {"trust_calibration": 4}),
    ("Feel hurt but let it go — they were probably just sharing", {"trust_calibration": 2}),
    ("Don't mention it — making it a big deal would be dramatic", {"trust_calibration": 1})
]))

q("dynamic_health", "scenario", "External validation of your dynamic — friends, community members, or online strangers commenting on the health/legitimacy of your D/s relationship:", opts([
    ("Matters only insofar as it prompts useful reflection. External opinions don't validate or invalidate our dynamic — the metric is: are both people growing, thriving, and genuinely consenting?", {"dynamic_health": 5}),
    ("I listen but make my own assessment", {"dynamic_health": 4}),
    ("Affects me more than I'd like to admit", {"dynamic_health": 2}),
    ("I seek validation from others about our dynamic", {"dynamic_health": 1})
]))

q("negotiation_skill", "scenario", "A potential partner uses negotiation terms you don't know (meta-consent, blanket consent, CNC framework, gradient safeword system). You:", opts([
    ("Ask for definitions without shame: 'I'm not familiar with that framework — can you explain it? I want to negotiate with full understanding.' Not knowing is fine; pretending to know is dangerous", {"negotiation_skill": 5}),
    ("Ask for clarification — I need to understand what I'm agreeing to", {"negotiation_skill": 4}),
    ("Nod along and look it up later", {"negotiation_skill": 2}),
    ("Assume I understand from context", {"negotiation_skill": 1})
]))

q("aftercare_practice", "forced_choice", "Self-aftercare vs. partner aftercare:", opts([
    ("Both are critical skills. I know how to receive care AND how to give it to myself when a partner isn't available. Self-aftercare is self-advocacy, not settling", {"aftercare_practice": 5}),
    ("Both matter — I prefer partner aftercare but can self-soothe", {"aftercare_practice": 4}),
    ("I rely on partner aftercare primarily", {"aftercare_practice": 3}),
    ("I don't need either — I'm fine after scenes", {"aftercare_practice": 1})
]))

# Extra cross-cutting
q("lifestyle_vs_bedroom", "somatic", "Wearing a subtle symbol of your dynamic in public (a locking bracelet, a specific necklace, a ring) — the physical reminder on your body:", opts([
    ("Grounds me in the dynamic all day — I touch it and feel connected to my role and my partner", {"lifestyle_vs_bedroom": 5}),
    ("Is a nice reminder", {"lifestyle_vs_bedroom": 4}),
    ("Is jewelry — I don't imbue it with D/s meaning", {"lifestyle_vs_bedroom": 2}),
    ("I don't wear symbols of my dynamic", {"lifestyle_vs_bedroom": 1})
]))

q("service_orientation_depth", "scenario", "Service burnout — when you've been serving so intensely that you're depleted. In a healthy dynamic:", opts([
    ("You name it: 'I need to recharge. My service quality suffers when I'm empty.' And a good Dominant responds by adjusting expectations and caring for you", {"service_orientation_depth": 5, "dynamic_health": 5}),
    ("You ask for reduced expectations temporarily", {"service_orientation_depth": 4}),
    ("You push through — service is the commitment", {"service_orientation_depth": 2}),
    ("Burnout means the dynamic is asking too much", {"service_orientation_depth": 1})
]), tier_role="trap", trap=True)

q("authority_exchange_comfort", "scenario", "Your Dominant's judgment call turns out to be wrong — a decision they made with authority leads to a bad outcome. You:", opts([
    ("Don't use it against them: 'We learn from this. I don't regret yielding — your authority doesn't require infallibility, it requires good faith.' This IS the test of real authority exchange", {"authority_exchange_comfort": 5}),
    ("Discuss what happened without blame — we both learn", {"authority_exchange_comfort": 4}),
    ("Feel vindicated: 'I knew that was a bad call' — and reconsider the authority exchange", {"authority_exchange_comfort": 2}),
    ("Withdraw authority: 'This proves you can't be trusted with decisions about my life'", {"authority_exchange_comfort": 1})
]))

q("trust_calibration", "temporal", "Over the arc of a D/s relationship, trust should:", opts([
    ("Deepen continuously through repeated cycles of vulnerability, reliability, and repair. Each cycle builds on the last. Trust isn't binary — it's a growing asset", {"trust_calibration": 5}),
    ("Grow steadily as positive experiences accumulate", {"trust_calibration": 4}),
    ("Reach a plateau — after a while, trust levels stabilize", {"trust_calibration": 3}),
    ("Be established early and maintained — it shouldn't need constant building", {"trust_calibration": 1})
]))

q("negotiation_skill", "forced_choice", "Your top negotiation principle:", opts([
    ("Enthusiastic clarity — I want both parties to understand exactly what they're agreeing to, with no ambiguity, no assumptions, and no unspoken expectations. Anything less is a foundation of sand", {"negotiation_skill": 5}),
    ("Thoroughness — cover all the important bases", {"negotiation_skill": 4}),
    ("Flexibility — negotiate broadly and adjust as you go", {"negotiation_skill": 3}),
    ("Efficiency — don't over-negotiate", {"negotiation_skill": 1})
]), tier_role="consistency_check", cg="ns_core")

q("dynamic_health", "forced_choice", "The ultimate measure of a healthy D/s dynamic:", opts([
    ("Both people are more self-aware, more emotionally regulated, more connected, and more authentically themselves within the dynamic than they would be without it", {"dynamic_health": 5}),
    ("Both people are satisfied and growing", {"dynamic_health": 4}),
    ("The sexual energy remains strong", {"dynamic_health": 3}),
    ("It lasts a long time", {"dynamic_health": 1})
]), tier_role="consistency_check", cg="dh_core")

# Final fillers
q("lifestyle_vs_bedroom", "temporal", "How long could you sustain a D/s dynamic that was bedroom-only with no lifestyle elements?", opts([
    ("Not long — I'd feel the absence and push for more integration or eventually lose interest", {"lifestyle_vs_bedroom": 5}),
    ("A while — but I'd want to add lifestyle elements over time", {"lifestyle_vs_bedroom": 4}),
    ("Indefinitely — bedroom D/s is satisfying for me", {"lifestyle_vs_bedroom": 2}),
    ("It's my preferred format — lifestyle would be too much", {"lifestyle_vs_bedroom": 1})
]))

q("protocol_depth", "behavioral_recall", "The most meaningful protocol in your D/s experience:", opts([
    ("Had symbolic and practical significance — it shaped my behavior AND reminded me of my role with every performance", {"protocol_depth": 5}),
    ("Was meaningful in context", {"protocol_depth": 4}),
    ("Was a useful routine", {"protocol_depth": 3}),
    ("I can't identify a particularly meaningful protocol", {"protocol_depth": 1})
]))

q("service_orientation_depth", "temporal", "If you couldn't serve your Dominant for an extended period (separation, illness), you would feel:", opts([
    ("Genuinely bereft — service is how I connect, and without it I feel untethered from my role and my partner", {"service_orientation_depth": 5}),
    ("Disconnected — I'd miss the service", {"service_orientation_depth": 4}),
    ("Fine — service is nice but I'm not dependent on it", {"service_orientation_depth": 2}),
    ("Relieved — a break from service obligations", {"service_orientation_depth": 1})
]))

q("authority_exchange_comfort", "temporal", "The deepest authority exchange you've ever experienced:", opts([
    ("Required months or years of trust-building and remains one of the most profound relationship experiences of my life", {"authority_exchange_comfort": 5}),
    ("Took time to build and was very meaningful", {"authority_exchange_comfort": 4}),
    ("Was intense but context-specific", {"authority_exchange_comfort": 3}),
    ("I haven't experienced deep authority exchange", {"authority_exchange_comfort": 1})
]))

q("trust_calibration", "forced_choice", "Trust and vulnerability in D/s:", opts([
    ("Are the actual kink — the toys, the scenes, the protocols are just vehicles for the profound vulnerability that trust-based power exchange enables", {"trust_calibration": 5}),
    ("Are the foundation everything else is built on", {"trust_calibration": 4}),
    ("Matter but aren't the main draw", {"trust_calibration": 3}),
    ("Are separate from the erotic elements", {"trust_calibration": 1})
]), tier_role="consistency_check", cg="tc_core")

q("aftercare_practice", "temporal", "How have your aftercare practices evolved?", opts([
    ("From basic to sophisticated — I now understand neurochemistry, emotional processing, delayed effects, and the needs of BOTH roles. My aftercare practice is informed and intentional", {"aftercare_practice": 5}),
    ("Significantly — I'm much more attentive and skilled than I used to be", {"aftercare_practice": 4}),
    ("Somewhat — I've gotten better", {"aftercare_practice": 3}),
    ("Not much — aftercare has always been informal for me", {"aftercare_practice": 1})
]))

print(f"Total questions: {len(questions)}")
with open("/Users/user/personal/sb/trueassess/priv/question_bank/power_exchange_depth.json", "w") as f:
    json.dump(questions, f, indent=2)
print("Written power_exchange_depth.json")
