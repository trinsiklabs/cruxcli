import json

questions = []
uid = 1

# Dark Triad + Sadism: 25 questions each = 100

dark_data = {
    "narcissism": [
        {"qt":"scenario","text":"You walk into a room and nobody acknowledges your presence. You:","opts":[
            {"id":"a","text":"Feel a flash of irritation — you deserve to be noticed","s":5},
            {"id":"b","text":"Find someone to start a conversation with — you'll make yourself known","s":3},
            {"id":"c","text":"Don't think about it — why would strangers acknowledge you?","s":1},
            {"id":"d","text":"Feel comfortable — attention isn't something you seek","s":1}
        ],"tier":"core","grp":"narc_attention_1","tags":["attention_seeking","entitlement"]},
        {"qt":"behavioral_recall","text":"When you compare yourself to most people you know, you honestly think:","opts":[
            {"id":"a","text":"I'm more talented, intelligent, or capable than most of them","s":5},
            {"id":"b","text":"I have my strengths and weaknesses, like everyone","s":1},
            {"id":"c","text":"I have unique gifts that most people don't appreciate fully","s":4},
            {"id":"d","text":"I'm pretty average and that's fine","s":1}
        ],"tier":"core","grp":"narc_grandiosity_1","tags":["grandiosity","self_assessment"]},
        {"qt":"forced_choice","text":"Which statement is most true for you?","opts":[
            {"id":"a","text":"I naturally expect special treatment because I bring special qualities","s":5},
            {"id":"b","text":"I expect to be treated the same as everyone else","s":1},
            {"id":"c","text":"I deserve recognition but rarely receive it","s":4},
            {"id":"d","text":"I'm uncomfortable when singled out for special treatment","s":1}
        ],"tier":"core","grp":"narc_entitlement_1","tags":["entitlement","special_treatment"]},
        {"qt":"somatic","text":"When someone achieves something you've been working toward, you feel:","opts":[
            {"id":"a","text":"Threatened — their success diminishes mine in some way","s":5},
            {"id":"b","text":"Envy mixed with motivation to work harder","s":3},
            {"id":"c","text":"Happy for them — their success doesn't affect mine","s":1},
            {"id":"d","text":"Competitive energy — time to step up my game","s":3}
        ],"tier":"core","grp":"narc_envy_1","tags":["envy","competition","somatic"]},
        {"qt":"scenario","text":"A group conversation shifts away from a topic you were leading. You:","opts":[
            {"id":"a","text":"Steer it back — your point wasn't finished and it was more important","s":5},
            {"id":"b","text":"Let it go — conversations flow naturally","s":1},
            {"id":"c","text":"Feel annoyed but adapt to the new topic","s":3},
            {"id":"d","text":"Find a way to make the new topic about your experiences","s":4}
        ],"tier":"core","grp":"narc_conversation_1","tags":["conversational_dominance","attention"]},
        {"qt":"temporal","text":"How has your sense of your own importance changed over the years?","opts":[
            {"id":"a","text":"I've always known I was destined for more than average","s":5},
            {"id":"b","text":"I've grown more humble as I've gained experience","s":1},
            {"id":"c","text":"I've always had a realistic self-assessment","s":1},
            {"id":"d","text":"My confidence has grown as my achievements have mounted","s":3}
        ],"tier":"core","grp":"narc_temporal_1","tags":["self_importance","temporal"]},
        {"qt":"forced_choice","text":"When you receive criticism, your first internal reaction is:","opts":[
            {"id":"a","text":"They don't understand my brilliance or vision","s":5},
            {"id":"b","text":"Defensiveness — but I try to listen objectively","s":3},
            {"id":"c","text":"Genuine consideration — they might be right","s":1},
            {"id":"d","text":"Hurt — criticism feels like a personal attack","s":4}
        ],"tier":"core","grp":"narc_criticism_1","tags":["criticism_sensitivity","defensiveness"]},
        {"qt":"scenario","text":"You're passed over for a promotion in favor of a colleague. You:","opts":[
            {"id":"a","text":"Know it's political — your qualifications obviously exceed theirs","s":5},
            {"id":"b","text":"Feel disappointed but examine what you could do differently","s":1},
            {"id":"c","text":"Question whether the decision-maker is competent enough to evaluate you","s":4},
            {"id":"d","text":"Accept it and plan your next move","s":1}
        ],"tier":"core","grp":"narc_rejection_1","tags":["rejection","self_assessment"]},
        {"qt":"behavioral_recall","text":"In your relationships, who tends to make more accommodations?","opts":[
            {"id":"a","text":"Others accommodate me more — my needs tend to take priority","s":5},
            {"id":"b","text":"It's fairly balanced — we both give and take","s":1},
            {"id":"c","text":"I accommodate others more — their needs feel more important","s":1},
            {"id":"d","text":"I expect accommodation because I bring more to the relationship","s":5}
        ],"tier":"core","grp":"narc_relationships_1","tags":["relationships","accommodation"]},
        {"qt":"somatic","text":"When you imagine yourself in five years, the most prominent feeling is:","opts":[
            {"id":"a","text":"Certainty that I'll be recognized for the exceptional person I am","s":5},
            {"id":"b","text":"Hope tempered with realistic expectations","s":1},
            {"id":"c","text":"Excitement about the authority and influence I'll have gained","s":4},
            {"id":"d","text":"Anxiety about whether things will work out","s":1}
        ],"tier":"core","grp":"narc_future_1","tags":["grandiose_fantasy","future"]},
        {"qt":"scenario","text":"At a dinner party, someone tells a story that gets big laughs. You:","opts":[
            {"id":"a","text":"Immediately think of a better story to top theirs","s":5},
            {"id":"b","text":"Enjoy their story and contribute naturally when it's your turn","s":1},
            {"id":"c","text":"Feel competitive but resist the urge to one-up them","s":3},
            {"id":"d","text":"Admire their storytelling and ask follow-up questions","s":1}
        ],"tier":"triangulation","grp":"narc_competition_social_1","tags":["social_competition","one_upping"]},
        {"qt":"forced_choice","text":"How do you feel when someone doesn't know who you are or what you've accomplished?","opts":[
            {"id":"a","text":"Surprised — I expect a certain level of recognition","s":5},
            {"id":"b","text":"Unbothered — why would strangers know me?","s":1},
            {"id":"c","text":"It's an opportunity to impress them","s":3},
            {"id":"d","text":"Slightly disappointed but I understand not everyone follows my field","s":3}
        ],"tier":"core","grp":"narc_recognition_1","tags":["recognition","fame_expectation"]},
        {"qt":"behavioral_recall","text":"How do you respond when someone outperforms you at something you consider your strength?","opts":[
            {"id":"a","text":"They must have had some advantage I didn't — it's not about raw ability","s":5},
            {"id":"b","text":"I acknowledge their skill and learn from them","s":1},
            {"id":"c","text":"I feel threatened and motivated to reclaim my position","s":4},
            {"id":"d","text":"I quietly reassess — maybe I overestimated my ability in this area","s":1}
        ],"tier":"core","grp":"narc_outperformed_1","tags":["outperformance","ego_protection"]},
        {"qt":"scenario","text":"A journalist is writing a profile about people in your industry. They don't contact you. You:","opts":[
            {"id":"a","text":"Feel offended — they missed the most important person in the field","s":5},
            {"id":"b","text":"Don't think about it — not everyone will know your work","s":1},
            {"id":"c","text":"Reach out to them proactively — they clearly need your perspective","s":4},
            {"id":"d","text":"Feel mildly disappointed but move on","s":2}
        ],"tier":"triangulation","grp":"narc_media_1","tags":["media_attention","self_importance"]},
        {"qt":"somatic","text":"When you receive excessive praise or admiration from someone, you feel:","opts":[
            {"id":"a","text":"Validated — this is the recognition I deserve and it feels right","s":5},
            {"id":"b","text":"Slightly uncomfortable — I don't need that much praise","s":1},
            {"id":"c","text":"Suspicious — what do they want?","s":2},
            {"id":"d","text":"Energized — admiration fuels me","s":5}
        ],"tier":"core","grp":"narc_praise_1","tags":["somatic","narcissistic_supply"]},
        {"qt":"forced_choice","text":"Which describes your empathy for others?","opts":[
            {"id":"a","text":"I understand others' feelings intellectually but I'm primarily focused on my own experience","s":5},
            {"id":"b","text":"I feel others' emotions deeply and naturally","s":1},
            {"id":"c","text":"I empathize when it's strategic to do so","s":4},
            {"id":"d","text":"I'm empathetic but sometimes my own needs overshadow it","s":3}
        ],"tier":"core","grp":"narc_empathy_1","tags":["empathy","self_focus"]},
        {"qt":"behavioral_recall","text":"When you tell stories, how often are you the hero of the narrative?","opts":[
            {"id":"a","text":"Almost always — my stories naturally center on my actions and insights","s":5},
            {"id":"b","text":"Sometimes — but I highlight others' roles too","s":2},
            {"id":"c","text":"Rarely — I'm more interested in what happened than in my role in it","s":1},
            {"id":"d","text":"Often — but the stories are about lessons learned, not bragging","s":3}
        ],"tier":"triangulation","grp":"narc_storytelling_1","tags":["self_centeredness","narrative"]},
        {"qt":"scenario","text":"Your partner tells you that you don't listen well and make everything about yourself. You:","opts":[
            {"id":"a","text":"Think they're being unfair — you're just passionate and expressive","s":5},
            {"id":"b","text":"Take it seriously and work on changing the pattern","s":1},
            {"id":"c","text":"Acknowledge the pattern but think they're exaggerating","s":4},
            {"id":"d","text":"Feel hurt and defensive but try to hear the feedback","s":2}
        ],"tier":"core","grp":"narc_feedback_partner_1","tags":["relationship_feedback","self_awareness"]},
        {"qt":"temporal","text":"Looking at your friendships, which pattern emerges?","opts":[
            {"id":"a","text":"People orbit me — I'm naturally the center of my social groups","s":5},
            {"id":"b","text":"I have equal, mutual friendships built on genuine connection","s":1},
            {"id":"c","text":"I surround myself with people who appreciate my qualities","s":4},
            {"id":"d","text":"I've had trouble maintaining close friendships long-term","s":2}
        ],"tier":"core","grp":"narc_friendship_1","tags":["friendship_patterns","social_dynamics"]},
        {"qt":"forced_choice","text":"Which best describes your self-image?","opts":[
            {"id":"a","text":"I'm genuinely exceptional in ways that most people aren't","s":5},
            {"id":"b","text":"I have strengths and weaknesses like everyone else","s":1},
            {"id":"c","text":"I'm exceptional in specific areas but average in others","s":2},
            {"id":"d","text":"I have untapped potential that the world hasn't recognized yet","s":4}
        ],"tier":"core","grp":"narc_selfimage_1","tags":["self_image","grandiosity"]},
        {"qt":"scenario","text":"You volunteer for a charitable cause. Someone asks why you're doing it. Honestly, the strongest motivation is:","opts":[
            {"id":"a","text":"The social recognition and how it reflects on my character","s":5},
            {"id":"b","text":"Genuine desire to help — the cause matters to me","s":1},
            {"id":"c","text":"A mix — I care AND it looks good","s":3},
            {"id":"d","text":"Networking opportunities with other high-status volunteers","s":4}
        ],"tier":"trap","grp":"narc_prosocial_1","tags":["prosocial_motivation","impression_management"]},
        {"qt":"behavioral_recall","text":"How do you handle being wrong in front of others?","opts":[
            {"id":"a","text":"Deflect, reframe, or find a way to save face — being wrong publicly is painful","s":5},
            {"id":"b","text":"Acknowledge it openly — everyone's wrong sometimes","s":1},
            {"id":"c","text":"Minimize it — 'I was close' or 'the information changed'","s":4},
            {"id":"d","text":"Feel embarrassed but admit it","s":2}
        ],"tier":"core","grp":"narc_wrong_1","tags":["being_wrong","face_saving"]},
        {"qt":"somatic","text":"When someone fails to give you the respect you feel you deserve, you feel:","opts":[
            {"id":"a","text":"Narcissistic rage — a disproportionate anger that surprises even me","s":5},
            {"id":"b","text":"Mild annoyance that passes quickly","s":2},
            {"id":"c","text":"Nothing — I don't have expectations about how others treat me","s":1},
            {"id":"d","text":"A burning resentment that I store away","s":4}
        ],"tier":"core","grp":"narc_disrespect_1","tags":["somatic","narcissistic_rage"]},
        {"qt":"forced_choice","text":"If you could choose one superpower, it would be:","opts":[
            {"id":"a","text":"The power to make everyone admire and respect you","s":5},
            {"id":"b","text":"The power to understand anyone's deepest feelings","s":1},
            {"id":"c","text":"The power to control any situation you're in","s":3},
            {"id":"d","text":"The power to know the truth about anything","s":1}
        ],"tier":"trap","grp":"narc_fantasy_1","tags":["fantasy","wish_fulfillment"]},
        {"qt":"behavioral_recall","text":"How much energy do you spend managing your image — what people think of you?","opts":[
            {"id":"a","text":"Significant energy — my reputation and image matter enormously to me","s":5},
            {"id":"b","text":"Some — I care about being respected but don't obsess over it","s":2},
            {"id":"c","text":"Very little — I am who I am and people can take it or leave it","s":1},
            {"id":"d","text":"I curate my image carefully for strategic purposes","s":4}
        ],"tier":"core","grp":"narc_image_1","tags":["image_management","reputation"]},
    ],
    "machiavellianism": [
        {"qt":"scenario","text":"You learn confidential information about a colleague that could be useful in a future negotiation. You:","opts":[
            {"id":"a","text":"File it away — information is leverage, and you never know when it'll be useful","s":5},
            {"id":"b","text":"Forget about it — using personal information as leverage is wrong","s":1},
            {"id":"c","text":"Wouldn't use it directly but might let it inform your strategy","s":3},
            {"id":"d","text":"Feel uncomfortable knowing it — you'd rather not have that kind of power over someone","s":1}
        ],"tier":"core","grp":"mach_leverage_1","tags":["information_leverage","strategy"]},
        {"qt":"behavioral_recall","text":"When you meet someone new, how much do you assess what they can offer you?","opts":[
            {"id":"a","text":"Always — I automatically evaluate people's usefulness to my goals","s":5},
            {"id":"b","text":"Sometimes — but I mostly connect based on genuine interest","s":2},
            {"id":"c","text":"Rarely — I connect with people based on who they are, not what they offer","s":1},
            {"id":"d","text":"I notice it but I also value the relationship independently","s":3}
        ],"tier":"core","grp":"mach_instrumental_1","tags":["instrumental_relationships","assessment"]},
        {"qt":"forced_choice","text":"Which statement do you most agree with?","opts":[
            {"id":"a","text":"The ends justify the means if the outcome is important enough","s":5},
            {"id":"b","text":"How you achieve something matters as much as what you achieve","s":1},
            {"id":"c","text":"You should play by the rules unless the rules are clearly unjust","s":1},
            {"id":"d","text":"Flexibility in methods is important — rigid morality leads to inefficiency","s":4}
        ],"tier":"core","grp":"mach_ends_means_1","tags":["ends_means","moral_flexibility"]},
        {"qt":"somatic","text":"When you successfully manipulate a situation to your advantage without anyone knowing, you feel:","opts":[
            {"id":"a","text":"Satisfaction — like a chess player who sees three moves ahead","s":5},
            {"id":"b","text":"Guilty — even if it worked, deception feels wrong","s":1},
            {"id":"c","text":"Smart — but with a slight edge of guilt","s":3},
            {"id":"d","text":"Nothing — manipulation isn't part of my approach","s":1}
        ],"tier":"core","grp":"mach_manipulation_feeling_1","tags":["somatic","manipulation"]},
        {"qt":"scenario","text":"A business opportunity requires you to break a promise to a friend, but the financial upside is significant. You:","opts":[
            {"id":"a","text":"Break the promise — in business, you can't let personal loyalty hold you back","s":5},
            {"id":"b","text":"Keep the promise — integrity can't be bought","s":1},
            {"id":"c","text":"Find a creative way to pursue the opportunity while minimizing the broken promise","s":3},
            {"id":"d","text":"Talk to your friend about the situation and negotiate a solution","s":1}
        ],"tier":"core","grp":"mach_loyalty_vs_gain_1","tags":["loyalty","self_interest"]},
        {"qt":"temporal","text":"How has your approach to trust changed over the years?","opts":[
            {"id":"a","text":"I've learned that trusting people is a liability — everyone has an angle","s":5},
            {"id":"b","text":"I've become more trusting as I've had more positive experiences","s":1},
            {"id":"c","text":"I trust strategically — certain people in certain contexts","s":4},
            {"id":"d","text":"My trust level has stayed consistent — I give people the benefit of the doubt","s":1}
        ],"tier":"core","grp":"mach_trust_1","tags":["trust","cynicism","temporal"]},
        {"qt":"forced_choice","text":"In organizational politics, you:","opts":[
            {"id":"a","text":"Excel — I read power dynamics naturally and position myself advantageously","s":5},
            {"id":"b","text":"Participate reluctantly — I'd rather things were straightforward","s":2},
            {"id":"c","text":"Avoid entirely — politics is distasteful","s":1},
            {"id":"d","text":"Navigate carefully — I don't start political games but I can play them","s":3}
        ],"tier":"core","grp":"mach_politics_1","tags":["organizational_politics","strategic_thinking"]},
        {"qt":"scenario","text":"You discover your manager is making a decision based on flawed data. Correcting them publicly would embarrass them. You:","opts":[
            {"id":"a","text":"Stay quiet and use the knowledge later when it's strategically advantageous","s":5},
            {"id":"b","text":"Correct them privately — they'd want to know","s":1},
            {"id":"c","text":"Bring it up in a way that doesn't embarrass them but fixes the problem","s":2},
            {"id":"d","text":"Consider how correcting vs not correcting affects your position, then decide","s":4}
        ],"tier":"core","grp":"mach_information_1","tags":["strategic_information","self_interest"]},
        {"qt":"behavioral_recall","text":"How often do you tell people what they want to hear rather than the truth?","opts":[
            {"id":"a","text":"Frequently — managing people's perceptions is essential to getting what you want","s":5},
            {"id":"b","text":"Rarely — I value honesty even when it's uncomfortable","s":1},
            {"id":"c","text":"Sometimes — social lubrication is necessary","s":3},
            {"id":"d","text":"Only when the truth would cause unnecessary harm","s":2}
        ],"tier":"core","grp":"mach_deception_1","tags":["deception","impression_management"]},
        {"qt":"somatic","text":"When you realize someone is trying to manipulate you, you feel:","opts":[
            {"id":"a","text":"Respect for their game — and I counter-maneuver","s":5},
            {"id":"b","text":"Angry — manipulation is a violation of trust","s":1},
            {"id":"c","text":"Alert — I assess their strategy and decide how to respond","s":3},
            {"id":"d","text":"Hurt — I expected better from them","s":1}
        ],"tier":"core","grp":"mach_counter_1","tags":["somatic","counter_manipulation"]},
        {"qt":"scenario","text":"You can advance your career by taking credit for someone else's idea. They'll never find out. You:","opts":[
            {"id":"a","text":"Do it without hesitation — in competitive environments, this is how it works","s":5},
            {"id":"b","text":"Never — that's theft of intellectual effort","s":1},
            {"id":"c","text":"Consider it but ultimately give credit — the risk isn't worth it","s":2},
            {"id":"d","text":"Reframe the idea as collaborative so you both benefit","s":3}
        ],"tier":"core","grp":"mach_credit_theft_1","tags":["credit_stealing","ethics"]},
        {"qt":"forced_choice","text":"Which view of human nature do you hold?","opts":[
            {"id":"a","text":"People are fundamentally self-interested — altruism is usually disguised selfishness","s":5},
            {"id":"b","text":"People are generally good and want to do right","s":1},
            {"id":"c","text":"People are complex — capable of both selfishness and genuine altruism","s":2},
            {"id":"d","text":"People are self-interested but can learn to be genuinely caring","s":2}
        ],"tier":"core","grp":"mach_human_nature_1","tags":["cynicism","worldview"]},
        {"qt":"behavioral_recall","text":"How do you prepare for important negotiations?","opts":[
            {"id":"a","text":"Research the other party's weaknesses, needs, and pressure points extensively","s":5},
            {"id":"b","text":"Focus on finding a fair outcome for both sides","s":1},
            {"id":"c","text":"Know my bottom line and BATNA, then negotiate in good faith","s":2},
            {"id":"d","text":"Prepare multiple strategies including some that exploit the other party's position","s":4}
        ],"tier":"triangulation","grp":"mach_negotiation_1","tags":["negotiation","exploitation"]},
        {"qt":"scenario","text":"A colleague confides their career plans to you in confidence. Later, your boss asks about team members' career aspirations. You:","opts":[
            {"id":"a","text":"Share what you know — information is currency and this makes you valuable to your boss","s":5},
            {"id":"b","text":"Keep the confidence — trust is more valuable than looking good to the boss","s":1},
            {"id":"c","text":"Share only what's not harmful and keep sensitive details private","s":2},
            {"id":"d","text":"Use the information obliquely without directly betraying the confidence","s":4}
        ],"tier":"core","grp":"mach_confidence_1","tags":["confidentiality","strategic_betrayal"]},
        {"qt":"temporal","text":"How has your strategic thinking about relationships evolved?","opts":[
            {"id":"a","text":"I've become more calculated — experience taught me that naivety costs too much","s":5},
            {"id":"b","text":"I've become less strategic — authentic relationships matter more than positioning","s":1},
            {"id":"c","text":"I've always been strategic — it's how I naturally process social dynamics","s":5},
            {"id":"d","text":"I balance strategic awareness with genuine connection","s":2}
        ],"tier":"core","grp":"mach_evolution_1","tags":["strategic_evolution","temporal"]},
        {"qt":"forced_choice","text":"Your approach to alliances and partnerships is:","opts":[
            {"id":"a","text":"Form them when useful, dissolve them when they no longer serve my interests","s":5},
            {"id":"b","text":"Build them on genuine mutual value and maintain them through loyalty","s":1},
            {"id":"c","text":"Keep a balance of alliances that protect my interests","s":3},
            {"id":"d","text":"Invest in a few deep partnerships rather than many shallow ones","s":1}
        ],"tier":"core","grp":"mach_alliances_1","tags":["alliances","instrumental_relationships"]},
        {"qt":"behavioral_recall","text":"How comfortable are you with deception when the stakes are high?","opts":[
            {"id":"a","text":"Very — deception is a tool, and skilled use of it is an advantage","s":5},
            {"id":"b","text":"Uncomfortable — I avoid deception even at personal cost","s":1},
            {"id":"c","text":"I can do it but it weighs on me afterward","s":2},
            {"id":"d","text":"I distinguish between strategic misdirection and harmful lying","s":3}
        ],"tier":"core","grp":"mach_deception_comfort_1","tags":["deception","comfort_level"]},
        {"qt":"scenario","text":"You realize a colleague's project is going to fail. Their failure could highlight your success by contrast. You:","opts":[
            {"id":"a","text":"Let it play out — their failure enhances your relative position","s":5},
            {"id":"b","text":"Warn them — you'd want the same from someone else","s":1},
            {"id":"c","text":"Offer limited help — enough to seem supportive without fixing the problem","s":4},
            {"id":"d","text":"Help if you can do so without significant cost to yourself","s":2}
        ],"tier":"core","grp":"mach_others_failure_1","tags":["schadenfreude","strategic_positioning"]},
        {"qt":"somatic","text":"When you execute a well-planned strategy that gives you advantage over competitors, you feel:","opts":[
            {"id":"a","text":"Intellectual pleasure — like winning a chess match against a worthy opponent","s":5},
            {"id":"b","text":"Relief that the plan worked, mixed with concern about its fairness","s":2},
            {"id":"c","text":"Satisfied if the outcome is fair for everyone involved","s":1},
            {"id":"d","text":"Powerful — this is what competence feels like","s":4}
        ],"tier":"core","grp":"mach_strategic_pleasure_1","tags":["somatic","strategic_pleasure"]},
        {"qt":"forced_choice","text":"What's your view on 'playing fair'?","opts":[
            {"id":"a","text":"Fairness is a concept the powerful use to keep the less powerful in line","s":5},
            {"id":"b","text":"Fairness is essential — society depends on it","s":1},
            {"id":"c","text":"Fairness is ideal but the real world requires pragmatic flexibility","s":3},
            {"id":"d","text":"I play fair but I don't expect others to","s":2}
        ],"tier":"core","grp":"mach_fairness_1","tags":["fairness","cynicism"]},
        {"qt":"behavioral_recall","text":"How often do you have a 'public position' that differs from your 'private position'?","opts":[
            {"id":"a","text":"Often — managing perception requires presenting different faces to different audiences","s":5},
            {"id":"b","text":"Rarely — what you see is what you get with me","s":1},
            {"id":"c","text":"Sometimes — certain truths aren't appropriate for all audiences","s":3},
            {"id":"d","text":"Never — authenticity is non-negotiable for me","s":1}
        ],"tier":"core","grp":"mach_two_faces_1","tags":["duplicity","impression_management"]},
        {"qt":"scenario","text":"A moral shortcut would save your company millions but hurts a small group of people who would never trace it back to you. You:","opts":[
            {"id":"a","text":"Take the shortcut — the numbers speak for themselves","s":5},
            {"id":"b","text":"Refuse — ethical lines exist for a reason","s":1},
            {"id":"c","text":"Weigh the specific harm against the specific benefit","s":3},
            {"id":"d","text":"Find a way to achieve the savings without the ethical compromise","s":1}
        ],"tier":"core","grp":"mach_moral_shortcut_1","tags":["moral_flexibility","utilitarian"]},
        {"qt":"forced_choice","text":"Which best describes how you view emotional appeals?","opts":[
            {"id":"a","text":"Useful tools for persuasion — emotions are levers","s":5},
            {"id":"b","text":"Genuine expressions of human connection","s":1},
            {"id":"c","text":"Sometimes manipulative, sometimes authentic — context matters","s":2},
            {"id":"d","text":"I use them when logic alone isn't enough to persuade","s":3}
        ],"tier":"core","grp":"mach_emotional_appeals_1","tags":["emotional_manipulation","persuasion"]},
        {"qt":"behavioral_recall","text":"How much long-term planning do you do regarding your social and professional positioning?","opts":[
            {"id":"a","text":"Extensively — I think years ahead about who I need to know and where I need to be","s":5},
            {"id":"b","text":"Some — I have general career goals but I don't scheme about positioning","s":2},
            {"id":"c","text":"Very little — I focus on doing good work and let positioning happen naturally","s":1},
            {"id":"d","text":"I plan strategically but I don't think of it as 'positioning' — it's just being smart","s":3}
        ],"tier":"triangulation","grp":"mach_longterm_1","tags":["strategic_planning","social_positioning"]},
        {"qt":"temporal","text":"What's the most cynical lesson you've learned about how the world works?","opts":[
            {"id":"a","text":"Trust is a resource to be spent wisely, not given freely — most people exploit it","s":5},
            {"id":"b","text":"The world is imperfect but people are generally trustworthy","s":1},
            {"id":"c","text":"Power matters more than merit in most systems","s":4},
            {"id":"d","text":"I try not to be cynical — cynicism becomes self-fulfilling","s":1}
        ],"tier":"core","grp":"mach_cynicism_1","tags":["cynicism","worldview","temporal"]},
    ],
    "psychopathy": [
        {"qt":"scenario","text":"A friend tells you they're devastated about their grandmother's death. They're crying. You:","opts":[
            {"id":"a","text":"Feel nothing internally but know the appropriate response and perform it","s":5},
            {"id":"b","text":"Feel genuine empathy and hold space for their grief","s":1},
            {"id":"c","text":"Feel mild discomfort — their emotional intensity is hard to process","s":3},
            {"id":"d","text":"Offer practical help — emotions aren't your strong suit but action is","s":2}
        ],"tier":"core","grp":"psy_empathy_deficit_1","tags":["empathy_deficit","emotional_mimicry"]},
        {"qt":"behavioral_recall","text":"When you hurt someone's feelings, your typical internal experience is:","opts":[
            {"id":"a","text":"Little to no guilt — their emotional reactions are their responsibility","s":5},
            {"id":"b","text":"Genuine remorse that motivates me to make amends","s":1},
            {"id":"c","text":"Brief guilt that fades quickly — I move on faster than most people","s":3},
            {"id":"d","text":"Guilt proportional to the harm — sometimes a lot, sometimes none","s":2}
        ],"tier":"core","grp":"psy_guilt_1","tags":["guilt_deficit","remorse"]},
        {"qt":"forced_choice","text":"Which describes your experience of boredom?","opts":[
            {"id":"a","text":"Boredom is intense and almost painful — I need stimulation constantly","s":5},
            {"id":"b","text":"Boredom is mildly uncomfortable — I manage it easily","s":2},
            {"id":"c","text":"I'm rarely bored — I can find interest in most situations","s":1},
            {"id":"d","text":"Boredom drives me to seek thrills or take risks just to feel something","s":5}
        ],"tier":"core","grp":"psy_stimulation_1","tags":["stimulation_seeking","boredom"]},
        {"qt":"somatic","text":"When you're about to do something risky that could have serious consequences, you feel:","opts":[
            {"id":"a","text":"Excited — risk makes me feel alive in a way nothing else does","s":5},
            {"id":"b","text":"Anxious — the potential consequences worry me","s":1},
            {"id":"c","text":"Calculated alertness — I've assessed the odds and I'm proceeding","s":3},
            {"id":"d","text":"A thrill that overrides any concern about consequences","s":5}
        ],"tier":"core","grp":"psy_risk_1","tags":["somatic","risk_seeking"]},
        {"qt":"scenario","text":"You're in a relationship and an attractive opportunity for infidelity arises with zero chance of being caught. You:","opts":[
            {"id":"a","text":"Act on it — if there are no consequences, the constraint is artificial","s":5},
            {"id":"b","text":"Decline — commitment means something regardless of whether you'd get caught","s":1},
            {"id":"c","text":"Seriously consider it — the temptation is real","s":3},
            {"id":"d","text":"Decline but not because of morality — because it's not worth the emotional complication","s":3}
        ],"tier":"core","grp":"psy_impulse_1","tags":["impulse_control","morality"]},
        {"qt":"temporal","text":"How has your ability to form deep emotional bonds changed?","opts":[
            {"id":"a","text":"I've never formed deep bonds easily — people are interesting but I don't attach deeply","s":5},
            {"id":"b","text":"I form deep bonds naturally and have maintained them throughout my life","s":1},
            {"id":"c","text":"I've become better at forming bonds through practice and effort","s":2},
            {"id":"d","text":"I connect intensely at first but the intensity fades quickly — I cycle through people","s":4}
        ],"tier":"core","grp":"psy_attachment_1","tags":["attachment","temporal"]},
        {"qt":"forced_choice","text":"Which describes your relationship with rules and social norms?","opts":[
            {"id":"a","text":"Rules are suggestions that I follow when convenient and ignore when not","s":5},
            {"id":"b","text":"Rules exist for good reasons and I follow them","s":1},
            {"id":"c","text":"I follow rules in public and bend them in private","s":3},
            {"id":"d","text":"I question rules but generally comply because the consequences aren't worth it","s":2}
        ],"tier":"core","grp":"psy_norms_1","tags":["rule_breaking","social_norms"]},
        {"qt":"scenario","text":"You witness a car accident where someone is clearly injured. Others are already calling 911. You:","opts":[
            {"id":"a","text":"Observe the scene with curiosity rather than distress — it's interesting more than upsetting","s":5},
            {"id":"b","text":"Feel immediate distress and rush to help if you can","s":1},
            {"id":"c","text":"Stop to help if you're needed but don't feel particularly emotional about it","s":3},
            {"id":"d","text":"Drive past — others are handling it and you have somewhere to be","s":4}
        ],"tier":"core","grp":"psy_callousness_1","tags":["callousness","empathy"]},
        {"qt":"behavioral_recall","text":"How quickly do you get bored in relationships?","opts":[
            {"id":"a","text":"Very quickly — the initial excitement fades fast and I start looking elsewhere","s":5},
            {"id":"b","text":"Slowly — deep relationships become richer over time","s":1},
            {"id":"c","text":"Moderately — I need novelty but I can maintain interest with effort","s":2},
            {"id":"d","text":"It depends on the person — some hold my interest, most don't","s":3}
        ],"tier":"core","grp":"psy_boredom_rel_1","tags":["relationship_boredom","stimulation"]},
        {"qt":"somatic","text":"When you lie, even about significant things, you typically experience:","opts":[
            {"id":"a","text":"Nothing — lying doesn't produce a physiological stress response in me","s":5},
            {"id":"b","text":"Anxiety — increased heart rate, sweating, discomfort","s":1},
            {"id":"c","text":"Mild discomfort that I control easily","s":3},
            {"id":"d","text":"A slight thrill — getting away with it is satisfying","s":4}
        ],"tier":"core","grp":"psy_lying_1","tags":["somatic","lying","stress_response"]},
        {"qt":"scenario","text":"A coworker is struggling and asks you for help on something that would take you two hours. You:","opts":[
            {"id":"a","text":"Help only if there's something in it for you — your time has value","s":5},
            {"id":"b","text":"Help willingly — helping others is part of being on a team","s":1},
            {"id":"c","text":"Help but note the favor for future leverage","s":4},
            {"id":"d","text":"Consider whether helping makes you look good before deciding","s":3}
        ],"tier":"core","grp":"psy_prosocial_1","tags":["prosocial_behavior","self_interest"]},
        {"qt":"forced_choice","text":"How would you describe your emotional life?","opts":[
            {"id":"a","text":"Shallow — I experience emotions but they're surface-level and pass quickly","s":5},
            {"id":"b","text":"Rich and varied — I feel a full range of emotions deeply","s":1},
            {"id":"c","text":"Controlled — I choose when and how to express emotions","s":3},
            {"id":"d","text":"Intense in some areas (anger, excitement) but flat in others (guilt, sadness)","s":4}
        ],"tier":"core","grp":"psy_emotional_depth_1","tags":["emotional_depth","affective_experience"]},
        {"qt":"behavioral_recall","text":"When making decisions, how much do you consider the impact on others?","opts":[
            {"id":"a","text":"Minimally — I prioritize my interests and assume others will do the same","s":5},
            {"id":"b","text":"Significantly — the impact on others is a major factor","s":1},
            {"id":"c","text":"I consider it but don't let it override what's best for me","s":3},
            {"id":"d","text":"Only when the impact on others could circle back to affect me","s":4}
        ],"tier":"core","grp":"psy_consideration_1","tags":["self_interest","impact_awareness"]},
        {"qt":"scenario","text":"You find an ATM that dispenses cash without debiting accounts. You:","opts":[
            {"id":"a","text":"Take as much as you can — this is a victimless windfall","s":5},
            {"id":"b","text":"Report it to the bank — it's not your money","s":1},
            {"id":"c","text":"Take some but not too much — moderation in all things","s":3},
            {"id":"d","text":"Walk away — it's clearly a malfunction and taking money is wrong","s":1}
        ],"tier":"triangulation","grp":"psy_opportunism_1","tags":["opportunism","moral_reasoning"]},
        {"qt":"temporal","text":"Looking back at your behavior patterns, how impulsive have you been?","opts":[
            {"id":"a","text":"Very — I act first and think later, which creates exciting but chaotic life patterns","s":5},
            {"id":"b","text":"Moderately — I'm impulsive sometimes but mostly thoughtful","s":2},
            {"id":"c","text":"Rarely impulsive — I think carefully before acting","s":1},
            {"id":"d","text":"I used to be very impulsive but I've learned to channel it","s":2}
        ],"tier":"core","grp":"psy_impulsivity_1","tags":["impulsivity","temporal"]},
        {"qt":"forced_choice","text":"Which best describes your conscience?","opts":[
            {"id":"a","text":"Quiet — I rarely feel guilt or moral discomfort about my choices","s":5},
            {"id":"b","text":"Active — guilt and moral concern guide many of my decisions","s":1},
            {"id":"c","text":"Selective — I feel guilt about some things but not others","s":3},
            {"id":"d","text":"Intellectual — I know what's right but the feeling doesn't always match","s":4}
        ],"tier":"core","grp":"psy_conscience_1","tags":["conscience","moral_emotion"]},
        {"qt":"behavioral_recall","text":"How many close friends have you maintained for more than five years?","opts":[
            {"id":"a","text":"Few to none — people cycle through my life and I don't try to hold onto them","s":5},
            {"id":"b","text":"Several — I invest in long-term friendships","s":1},
            {"id":"c","text":"A few — I'm selective but loyal to those I choose","s":2},
            {"id":"d","text":"People come and go — attachment isn't my strength","s":4}
        ],"tier":"triangulation","grp":"psy_relationships_1","tags":["relationship_stability","attachment"]},
        {"qt":"scenario","text":"You accidentally damage a parked car in an empty parking lot. No cameras, no witnesses. You:","opts":[
            {"id":"a","text":"Drive away without a second thought","s":5},
            {"id":"b","text":"Leave a note with your contact information","s":1},
            {"id":"c","text":"Drive away but feel somewhat guilty about it","s":3},
            {"id":"d","text":"Drive away — it's their insurance company's problem","s":4}
        ],"tier":"core","grp":"psy_accountability_1","tags":["accountability","conscience"]},
        {"qt":"somatic","text":"When you see someone in physical pain, you:","opts":[
            {"id":"a","text":"Feel a clinical detachment — I notice it intellectually but don't 'feel' their pain","s":5},
            {"id":"b","text":"Wince — I almost feel their pain in my own body","s":1},
            {"id":"c","text":"Feel concern and want to help reduce their suffering","s":1},
            {"id":"d","text":"Feel something brief and mild that passes immediately","s":3}
        ],"tier":"core","grp":"psy_pain_empathy_1","tags":["somatic","empathic_pain"]},
        {"qt":"forced_choice","text":"How do you view loyalty?","opts":[
            {"id":"a","text":"It's a useful expectation to create in others but I don't feel bound by it myself","s":5},
            {"id":"b","text":"It's one of the most important values — I'm deeply loyal","s":1},
            {"id":"c","text":"I'm loyal to those who prove themselves worthy of it","s":2},
            {"id":"d","text":"Loyalty is contextual — it can be renegotiated as circumstances change","s":3}
        ],"tier":"core","grp":"psy_loyalty_1","tags":["loyalty","commitment"]},
        {"qt":"behavioral_recall","text":"How often do you feel genuine fear?","opts":[
            {"id":"a","text":"Rarely — I'm not easily scared and danger doesn't produce strong fear responses","s":5},
            {"id":"b","text":"Regularly — fear is a normal emotional experience for me","s":1},
            {"id":"c","text":"Sometimes — certain specific things frighten me","s":2},
            {"id":"d","text":"I experience excitement where others feel fear — high-stakes situations energize me","s":4}
        ],"tier":"core","grp":"psy_fearlessness_1","tags":["fearlessness","arousal"]},
        {"qt":"scenario","text":"You overhear a conversation revealing that a company's stock is about to crash. You have significant holdings. Selling on inside information is illegal. You:","opts":[
            {"id":"a","text":"Sell immediately — getting caught is the only real risk, and you can manage that","s":5},
            {"id":"b","text":"Hold — insider trading is illegal and unethical","s":1},
            {"id":"c","text":"Find a way to sell that's hard to trace","s":4},
            {"id":"d","text":"Struggle with the temptation but ultimately hold","s":2}
        ],"tier":"core","grp":"psy_illegal_1","tags":["illegal_behavior","risk_assessment"]},
        {"qt":"temporal","text":"How many times have people described you as 'cold' or 'emotionally detached'?","opts":[
            {"id":"a","text":"Many times — it's a consistent theme in how people describe me","s":5},
            {"id":"b","text":"Never or rarely — people generally find me warm","s":1},
            {"id":"c","text":"A few times, usually by people who wanted more emotional engagement than I give","s":3},
            {"id":"d","text":"I've heard it but I see it as being rational, not cold","s":3}
        ],"tier":"consistency_check","grp":"psy_cold_1","tags":["coldness","temporal"]},
        {"qt":"forced_choice","text":"Which describes your approach to taking responsibility for your actions?","opts":[
            {"id":"a","text":"I accept responsibility when it's to my advantage — otherwise, I deflect or deny","s":5},
            {"id":"b","text":"I take full responsibility for my actions, even when it's costly","s":1},
            {"id":"c","text":"I take responsibility when it's clearly my fault","s":2},
            {"id":"d","text":"I reframe situations so that blame is distributed — nothing is entirely one person's fault","s":4}
        ],"tier":"core","grp":"psy_responsibility_1","tags":["responsibility","blame_deflection"]},
    ],
    "sadism": [
        {"qt":"scenario","text":"You're playing a competitive video game and your opponent is clearly frustrated and having a terrible time. You:","opts":[
            {"id":"a","text":"Enjoy their suffering — their frustration adds to your satisfaction","s":5},
            {"id":"b","text":"Feel empathy and maybe ease up","s":1},
            {"id":"c","text":"Feel nothing particular — focus on winning, not their experience","s":2},
            {"id":"d","text":"Find their frustration mildly amusing but don't seek to intensify it","s":3}
        ],"tier":"core","grp":"sad_enjoyment_1","tags":["enjoyment_of_suffering","competition"]},
        {"qt":"behavioral_recall","text":"When you see someone get their comeuppance — a bully getting beaten, an arrogant person being humbled — you feel:","opts":[
            {"id":"a","text":"Intense satisfaction that borders on glee — they deserved it","s":5},
            {"id":"b","text":"Mild satisfaction — justice was served","s":2},
            {"id":"c","text":"Mixed feelings — even deserved suffering is still suffering","s":1},
            {"id":"d","text":"Pleasure specifically from imagining what they're feeling in that moment","s":5}
        ],"tier":"core","grp":"sad_schadenfreude_1","tags":["schadenfreude","justice_satisfaction"]},
        {"qt":"forced_choice","text":"When you have power over someone (employee, student, subordinate), you:","opts":[
            {"id":"a","text":"Sometimes enjoy making them squirm — it's a perk of authority","s":5},
            {"id":"b","text":"Use power carefully and kindly — it's a responsibility","s":1},
            {"id":"c","text":"Exercise authority fairly without emotional investment either way","s":2},
            {"id":"d","text":"Find the power itself gratifying but don't deliberately cause discomfort","s":3}
        ],"tier":"core","grp":"sad_power_1","tags":["power_over_others","cruelty"]},
        {"qt":"somatic","text":"When you witness someone experiencing intense embarrassment, you feel:","opts":[
            {"id":"a","text":"A pleasurable tingle — their humiliation is physically enjoyable to me","s":5},
            {"id":"b","text":"Secondhand embarrassment — I feel it in my own body","s":1},
            {"id":"c","text":"Nothing much — embarrassment is a normal part of life","s":2},
            {"id":"d","text":"Amusement that I try to suppress because I know it's not kind","s":3}
        ],"tier":"core","grp":"sad_embarrassment_1","tags":["somatic","vicarious_enjoyment"]},
        {"qt":"scenario","text":"You're in a position to give a harsh but fair performance review. The person will be devastated. You:","opts":[
            {"id":"a","text":"Notice you're looking forward to it — delivering the blow has a certain appeal","s":5},
            {"id":"b","text":"Dread it — causing someone pain, even necessary pain, is hard for you","s":1},
            {"id":"c","text":"Approach it matter-of-factly — it's part of the job","s":2},
            {"id":"d","text":"Feel neutral about delivering it — the content is necessary regardless of their reaction","s":2}
        ],"tier":"core","grp":"sad_delivering_pain_1","tags":["delivering_pain","anticipation"]},
        {"qt":"temporal","text":"How have your reactions to violent or disturbing content (movies, news) changed?","opts":[
            {"id":"a","text":"I've always found it more fascinating than disturbing — I'm drawn to it","s":5},
            {"id":"b","text":"I've become more sensitive to it over the years","s":1},
            {"id":"c","text":"I've always been disturbed by violence and avoid it","s":1},
            {"id":"d","text":"I've become somewhat desensitized but don't seek it out","s":2}
        ],"tier":"core","grp":"sad_violence_1","tags":["violence_interest","temporal"]},
        {"qt":"forced_choice","text":"Which is closest to your honest experience of cruelty humor (jokes at someone's expense)?","opts":[
            {"id":"a","text":"I find it genuinely funnier than other kinds of humor — the target's discomfort adds to it","s":5},
            {"id":"b","text":"I don't enjoy humor that hurts others","s":1},
            {"id":"c","text":"It can be funny in the right context but I feel guilty laughing","s":2},
            {"id":"d","text":"I enjoy witty put-downs but not cruel bullying humor","s":3}
        ],"tier":"core","grp":"sad_humor_1","tags":["cruel_humor","enjoyment"]},
        {"qt":"scenario","text":"You're playing a board game and have the chance to make a move that would devastate another player's position. It's not strictly necessary for you to win. You:","opts":[
            {"id":"a","text":"Do it — watching their plans crumble is part of the fun","s":5},
            {"id":"b","text":"Avoid it if it's not necessary — no need to be cruel","s":1},
            {"id":"c","text":"Do it — it's a game and you play to win","s":2},
            {"id":"d","text":"Enjoy the moment of deciding whether to be merciful or not","s":4}
        ],"tier":"core","grp":"sad_games_1","tags":["game_cruelty","unnecessary_harm"]},
        {"qt":"behavioral_recall","text":"Have you ever said something hurtful and realized you enjoyed the impact?","opts":[
            {"id":"a","text":"Yes — the power of words to wound is something I've savored","s":5},
            {"id":"b","text":"No — I feel terrible when I hurt someone with words","s":1},
            {"id":"c","text":"Maybe once or twice in heated moments","s":2},
            {"id":"d","text":"Yes, but only toward people who hurt me first — revenge is satisfying","s":3}
        ],"tier":"core","grp":"sad_verbal_1","tags":["verbal_cruelty","enjoyment"]},
        {"qt":"somatic","text":"When you're in a confrontation and you sense the other person is afraid of you, you feel:","opts":[
            {"id":"a","text":"A rush of power — their fear is intoxicating","s":5},
            {"id":"b","text":"Uncomfortable — I never want to make someone afraid","s":1},
            {"id":"c","text":"Nothing particular — fear is a natural response to confrontation","s":2},
            {"id":"d","text":"Slight satisfaction that quickly gives way to guilt","s":3}
        ],"tier":"core","grp":"sad_fear_response_1","tags":["somatic","intimidation_enjoyment"]},
        {"qt":"scenario","text":"An insect is trapped and struggling. You:","opts":[
            {"id":"a","text":"Observe its struggle with a detached fascination","s":4},
            {"id":"b","text":"Free it — even insects deserve compassion","s":1},
            {"id":"c","text":"Ignore it — it's just an insect","s":2},
            {"id":"d","text":"Feel a slight impulse to make its situation worse before you either help or ignore it","s":5}
        ],"tier":"core","grp":"sad_creatures_1","tags":["cruelty_to_creatures","impulse"]},
        {"qt":"forced_choice","text":"Which describes your honest reaction to 'justice porn' content (bad people getting what they deserve)?","opts":[
            {"id":"a","text":"I actively seek it out — the suffering of deserving people is deeply satisfying","s":5},
            {"id":"b","text":"I find it mildly satisfying but don't seek it out","s":2},
            {"id":"c","text":"I feel uncomfortable with celebrating anyone's suffering, even if deserved","s":1},
            {"id":"d","text":"The satisfaction depends on the severity — proportional justice is satisfying, excessive isn't","s":2}
        ],"tier":"core","grp":"sad_justice_porn_1","tags":["justice_porn","proportionality"]},
        {"qt":"behavioral_recall","text":"Think about the last time you teased someone. How far did you push it?","opts":[
            {"id":"a","text":"Further than was comfortable for them — their increasing discomfort was part of the fun","s":5},
            {"id":"b","text":"I kept it light and stopped when I sensed any discomfort","s":1},
            {"id":"c","text":"I pushed until they got annoyed, then backed off","s":3},
            {"id":"d","text":"I don't really tease people — it feels mean-spirited","s":1}
        ],"tier":"core","grp":"sad_teasing_1","tags":["teasing","boundary_pushing"]},
        {"qt":"scenario","text":"You're anonymously rating restaurants online. A restaurant gave you poor service. You:","opts":[
            {"id":"a","text":"Write a devastatingly detailed negative review, enjoying the craft of the takedown","s":5},
            {"id":"b","text":"Write an honest review noting the specific issues","s":2},
            {"id":"c","text":"Don't bother — negative reviews aren't worth your time","s":1},
            {"id":"d","text":"Write a harsh review and enjoy imagining the owner reading it","s":5}
        ],"tier":"triangulation","grp":"sad_anonymous_1","tags":["anonymous_cruelty","takedowns"]},
        {"qt":"temporal","text":"Looking back at your childhood, how did you relate to aggressive play or bullying behavior?","opts":[
            {"id":"a","text":"I sometimes enjoyed making weaker kids uncomfortable — it felt powerful","s":5},
            {"id":"b","text":"I was protective of weaker kids — bullying horrified me","s":1},
            {"id":"c","text":"I was mostly a bystander — not bullying but not intervening either","s":2},
            {"id":"d","text":"I was sometimes aggressive but felt guilty about it afterward","s":2}
        ],"tier":"core","grp":"sad_childhood_1","tags":["childhood_aggression","temporal"]},
        {"qt":"somatic","text":"When you dominate someone in an argument — completely dismantle their position — you feel:","opts":[
            {"id":"a","text":"A physical high — it's one of the most satisfying feelings I know","s":5},
            {"id":"b","text":"Satisfied that the better argument won, nothing more","s":2},
            {"id":"c","text":"Uncomfortable if they seem hurt or humiliated","s":1},
            {"id":"d","text":"Powerful — their intellectual defeat is gratifying beyond the argument itself","s":4}
        ],"tier":"core","grp":"sad_domination_1","tags":["somatic","intellectual_domination"]},
        {"qt":"forced_choice","text":"How do you relate to the concept of mercy?","opts":[
            {"id":"a","text":"Mercy is weakness — people should face the full consequences of their actions","s":5},
            {"id":"b","text":"Mercy is strength — the ability to forgive is admirable","s":1},
            {"id":"c","text":"Mercy should be strategic — extend it when useful, withhold when not","s":3},
            {"id":"d","text":"I believe in mercy but I enjoy the moment before granting it — the power of deciding","s":4}
        ],"tier":"core","grp":"sad_mercy_1","tags":["mercy","punishment"]},
        {"qt":"scenario","text":"You overhear a colleague share a deeply embarrassing personal secret. You:","opts":[
            {"id":"a","text":"Store it away — knowing someone's weakness gives you a subtle thrill of power","s":5},
            {"id":"b","text":"Feel protective of their vulnerability","s":1},
            {"id":"c","text":"Note it but don't plan to use it — it's their business","s":2},
            {"id":"d","text":"Feel entertained by the gossip but wouldn't deliberately use it against them","s":3}
        ],"tier":"core","grp":"sad_secrets_1","tags":["power_over_vulnerability","secrets"]},
        {"qt":"behavioral_recall","text":"When you fire someone, end a relationship, or deliver devastating news, do you notice any positive feeling mixed in?","opts":[
            {"id":"a","text":"Yes — there's a grim satisfaction in the power and finality of it","s":5},
            {"id":"b","text":"No — it's entirely painful and I avoid it when possible","s":1},
            {"id":"c","text":"Relief, maybe — but not satisfaction","s":2},
            {"id":"d","text":"Sometimes — depending on whether they deserved it","s":3}
        ],"tier":"core","grp":"sad_termination_1","tags":["termination","mixed_feelings"]},
        {"qt":"scenario","text":"A social media figure you dislike faces a public scandal. You:","opts":[
            {"id":"a","text":"Follow every detail with glee — their downfall is entertainment","s":5},
            {"id":"b","text":"Feel some sympathy despite your dislike — public shaming is cruel","s":1},
            {"id":"c","text":"Note it briefly and move on — other people's drama isn't that interesting","s":2},
            {"id":"d","text":"Enjoy it but feel slightly guilty about enjoying it","s":3}
        ],"tier":"triangulation","grp":"sad_downfall_1","tags":["schadenfreude","public_shaming"]},
        {"qt":"forced_choice","text":"When playing competitive games, what adds the most satisfaction?","opts":[
            {"id":"a","text":"Watching my opponent struggle and fail — their misery enhances my victory","s":5},
            {"id":"b","text":"The intrinsic challenge of the game itself","s":1},
            {"id":"c","text":"Winning — regardless of my opponent's experience","s":2},
            {"id":"d","text":"A close match where I narrowly win — their competence makes my victory meaningful","s":2}
        ],"tier":"core","grp":"sad_competition_1","tags":["competitive_sadism","gaming"]},
        {"qt":"behavioral_recall","text":"Have you ever intentionally withheld something (information, help, comfort) from someone just to see them struggle?","opts":[
            {"id":"a","text":"Yes — watching them flounder when I could easily help has a certain appeal","s":5},
            {"id":"b","text":"No — if I can help, I do","s":1},
            {"id":"c","text":"Maybe once or twice, not as a pattern","s":2},
            {"id":"d","text":"I've withheld help when they needed to learn, but not for my enjoyment","s":1}
        ],"tier":"core","grp":"sad_withholding_1","tags":["withholding","deliberate_suffering"]},
        {"qt":"somatic","text":"Honestly, when you imagine having complete power over someone — where they can't resist or leave — what's the first feeling?","opts":[
            {"id":"a","text":"Excitement — total power is an intoxicating thought","s":5},
            {"id":"b","text":"Discomfort — that's a disturbing scenario to imagine","s":1},
            {"id":"c","text":"Responsibility — power should be exercised wisely","s":1},
            {"id":"d","text":"Curiosity about what I'd do with it","s":3}
        ],"tier":"core","grp":"sad_power_fantasy_1","tags":["somatic","power_fantasy"]},
        {"qt":"temporal","text":"How has your enjoyment of others' discomfort changed over time?","opts":[
            {"id":"a","text":"It's been consistent — I've always found others' distress somewhat entertaining","s":5},
            {"id":"b","text":"I've become more compassionate over time — I cringe at my younger self's callousness","s":1},
            {"id":"c","text":"I was never particularly entertained by others' suffering","s":1},
            {"id":"d","text":"I've learned to hide it better but the underlying impulse hasn't changed","s":5}
        ],"tier":"consistency_check","grp":"sad_temporal_1","tags":["temporal","consistency"]},
        {"qt":"forced_choice","text":"Which form of entertainment are you most honestly drawn to?","opts":[
            {"id":"a","text":"Conflict, violence, and power dynamics — the darker the more compelling","s":5},
            {"id":"b","text":"Stories of human connection, growth, and triumph","s":1},
            {"id":"c","text":"Comedy, adventure, and escapism","s":1},
            {"id":"d","text":"Psychological thrillers — I enjoy understanding the dark side of human nature","s":3}
        ],"tier":"triangulation","grp":"sad_entertainment_1","tags":["entertainment_preference","darkness"]},
    ],
}

for dim, qs in dark_data.items():
    for q in qs:
        entry = {
            "uid": f"DRK-{uid:03d}",
            "assessment_id": "dark_triad",
            "dimension": dim,
            "question_type": q["qt"],
            "text": q["text"],
            "options": [{"id":o["id"],"text":o["text"],"scores":{dim:o["s"]}} for o in q["opts"]],
            "tier_role": q["tier"],
            "anti_gaming": {
                "opacity": 0.6,
                "social_desirability_trap": q["tier"] == "trap",
                "consistency_group": q["grp"],
                "reversal": False
            },
            "cultural_adaptability": {
                "universal": True,
                "adaptations_needed": [],
                "adaptation_notes": None
            },
            "content_rating": "G",
            "content_categories": [],
            "depth_tier": "moderate",
            "tags": q["tags"]
        }
        questions.append(entry)
        uid += 1

with open("/Users/user/personal/sb/trueassess/priv/question_bank/dark_triad.json", "w") as f:
    json.dump(questions, f, indent=2)

print(f"Wrote {len(questions)} Dark Triad questions")
