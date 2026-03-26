import json

questions = []
uid = 1

dims = ["honesty_humility", "emotionality", "extraversion", "agreeableness", "conscientiousness", "openness"]
# 20 questions per dimension = 120

hexaco_data = {
    "honesty_humility": [
        {"qt":"scenario","text":"You accidentally receive a package meant for your neighbor that contains an expensive item. They're on vacation for a month. You:","opts":[
            {"id":"a","text":"Keep it safe and deliver it when they return — it's not yours","s":5},
            {"id":"b","text":"Use it carefully and return it before they get back","s":2},
            {"id":"c","text":"Keep it — their mistake, your gain","s":1},
            {"id":"d","text":"Contact the shipping company to arrange proper delivery","s":4}
        ],"tier":"core","grp":"hh_integrity_1","tags":["integrity","honesty"]},
        {"qt":"behavioral_recall","text":"When you've achieved something impressive, you tend to:","opts":[
            {"id":"a","text":"Mention it only if directly relevant to the conversation","s":5},
            {"id":"b","text":"Share it with close friends who would be genuinely interested","s":3},
            {"id":"c","text":"Find ways to bring it up — you're proud and want people to know","s":1},
            {"id":"d","text":"Downplay it — drawing attention to achievements feels uncomfortable","s":5}
        ],"tier":"core","grp":"hh_modesty_1","tags":["modesty","self-promotion"]},
        {"qt":"forced_choice","text":"Which statement most accurately describes you?","opts":[
            {"id":"a","text":"I treat people the same regardless of their status or what they can do for me","s":5},
            {"id":"b","text":"I naturally pay more attention to people who can help my career","s":1},
            {"id":"c","text":"I try to treat everyone equally but I'm more attentive to influential people","s":2},
            {"id":"d","text":"I focus on people I genuinely connect with, regardless of status","s":4}
        ],"tier":"core","grp":"hh_fairness_1","tags":["fairness","status"]},
        {"qt":"scenario","text":"You're in a salary negotiation and you know the company has a tight budget. Your honest assessment is that you're worth 10% more. You:","opts":[
            {"id":"a","text":"Ask for 10% — that's fair and honest","s":5},
            {"id":"b","text":"Ask for 20% knowing you'll negotiate down to 10%","s":2},
            {"id":"c","text":"Ask for as much as you can possibly get","s":1},
            {"id":"d","text":"Accept what they offer to avoid seeming greedy","s":3}
        ],"tier":"core","grp":"hh_greed_1","tags":["greed_avoidance","fairness"]},
        {"qt":"somatic","text":"When you witness someone blatantly lying to get ahead, you feel:","opts":[
            {"id":"a","text":"Visceral disgust — dishonesty physically repels me","s":5},
            {"id":"b","text":"Annoyance but understanding — everyone's playing the game","s":2},
            {"id":"c","text":"Admiration if they're skilled at it","s":1},
            {"id":"d","text":"Sadness that this is how things work","s":3}
        ],"tier":"core","grp":"hh_sincerity_1","tags":["sincerity","somatic"]},
        {"qt":"temporal","text":"How has your relationship with material wealth and luxury changed?","opts":[
            {"id":"a","text":"I've never been driven by material things — enough is enough","s":5},
            {"id":"b","text":"I used to want more but I've found contentment with less","s":3},
            {"id":"c","text":"I enjoy luxury and I'm not ashamed of wanting nice things","s":1},
            {"id":"d","text":"I appreciate quality but don't need excess","s":4}
        ],"tier":"core","grp":"hh_materialism_1","tags":["materialism","temporal"]},
        {"qt":"forced_choice","text":"When flattery is clearly being used to manipulate you, you:","opts":[
            {"id":"a","text":"See through it immediately and feel insulted they thought it would work","s":5},
            {"id":"b","text":"Enjoy the flattery even knowing it's strategic","s":1},
            {"id":"c","text":"Recognize it but don't mind — everyone uses social lubrication","s":2},
            {"id":"d","text":"Feel uncomfortable and distance yourself from the person","s":4}
        ],"tier":"triangulation","grp":"hh_flattery_1","tags":["flattery","manipulation_awareness"]},
        {"qt":"scenario","text":"You find a wallet with $500 and a driver's license. You:","opts":[
            {"id":"a","text":"Return the wallet with all the money — the thought of keeping it doesn't even occur to you","s":5},
            {"id":"b","text":"Return the wallet but keep some cash as a 'finder's fee'","s":2},
            {"id":"c","text":"Keep the cash and mail the wallet anonymously","s":1},
            {"id":"d","text":"Return everything and refuse any reward offered","s":5}
        ],"tier":"core","grp":"hh_honesty_2","tags":["honesty","integrity"]},
        {"qt":"behavioral_recall","text":"How do you typically behave when you have power or authority over others?","opts":[
            {"id":"a","text":"I'm careful not to exploit it — I treat people as I would without the power differential","s":5},
            {"id":"b","text":"I use it strategically to get things done efficiently","s":2},
            {"id":"c","text":"I enjoy the perks and influence that come with authority","s":1},
            {"id":"d","text":"I'm uncomfortable with power and try to flatten hierarchies","s":4}
        ],"tier":"core","grp":"hh_power_1","tags":["power","humility"]},
        {"qt":"forced_choice","text":"Which describes your approach to social status?","opts":[
            {"id":"a","text":"I'm genuinely uninterested in status symbols or social climbing","s":5},
            {"id":"b","text":"I work hard to advance my social position","s":1},
            {"id":"c","text":"I don't chase status but I appreciate it when I have it","s":2},
            {"id":"d","text":"I actively reject status markers — they feel pretentious","s":4}
        ],"tier":"core","grp":"hh_status_1","tags":["status","social_climbing"]},
        {"qt":"scenario","text":"A close friend asks your honest opinion about their new business idea, which you think is deeply flawed. You:","opts":[
            {"id":"a","text":"Give them your honest assessment, even though it might hurt","s":5},
            {"id":"b","text":"Emphasize the positives while subtly hinting at problems","s":2},
            {"id":"c","text":"Tell them it's great — why crush their enthusiasm?","s":1},
            {"id":"d","text":"Ask probing questions that help them discover the flaws themselves","s":4}
        ],"tier":"core","grp":"hh_candor_1","tags":["candor","honesty_in_relationships"]},
        {"qt":"behavioral_recall","text":"When you receive more credit than you deserve for something, you:","opts":[
            {"id":"a","text":"Correct the record and acknowledge others' contributions","s":5},
            {"id":"b","text":"Accept it gracefully — these things balance out over time","s":2},
            {"id":"c","text":"Enjoy it — credit is valuable capital","s":1},
            {"id":"d","text":"Feel uncomfortable but struggle to correct it publicly","s":3}
        ],"tier":"core","grp":"hh_credit_1","tags":["credit","modesty"]},
        {"qt":"somatic","text":"When you bend the truth even slightly — a white lie, an exaggeration — you feel:","opts":[
            {"id":"a","text":"Immediate discomfort — even small dishonesty bothers me physically","s":5},
            {"id":"b","text":"Nothing if it serves a good purpose","s":1},
            {"id":"c","text":"Mild guilt that fades quickly","s":3},
            {"id":"d","text":"It depends on who I'm lying to and why","s":2}
        ],"tier":"core","grp":"hh_lying_1","tags":["somatic","honesty"]},
        {"qt":"scenario","text":"You're on a committee selecting a vendor. Your friend's company is one of the options but isn't the best choice. You:","opts":[
            {"id":"a","text":"Vote for the best option regardless — integrity demands it","s":5},
            {"id":"b","text":"Advocate subtly for your friend while appearing objective","s":1},
            {"id":"c","text":"Recuse yourself from the decision due to the conflict of interest","s":5},
            {"id":"d","text":"Try to find legitimate reasons to choose your friend's company","s":2}
        ],"tier":"core","grp":"hh_conflict_of_interest_1","tags":["conflict_of_interest","integrity"]},
        {"qt":"forced_choice","text":"What's your relationship with rules and loopholes?","opts":[
            {"id":"a","text":"I follow the spirit of rules, not just the letter — loopholes feel dishonest","s":5},
            {"id":"b","text":"If a loophole exists, it's fair game — that's how the system works","s":1},
            {"id":"c","text":"I follow rules but I'm aware of loopholes just in case","s":2},
            {"id":"d","text":"I follow rules strictly and wish others would too","s":4}
        ],"tier":"core","grp":"hh_rules_1","tags":["rules","loopholes","spirit_vs_letter"]},
        {"qt":"temporal","text":"Looking back at your life, how consistent have you been in your principles?","opts":[
            {"id":"a","text":"Very — my core principles haven't wavered even when it cost me","s":5},
            {"id":"b","text":"Mostly — I've compromised when the stakes were high enough","s":3},
            {"id":"c","text":"Flexible — principles are guidelines, not absolutes","s":1},
            {"id":"d","text":"I've become more principled as I've aged and seen the cost of compromise","s":4}
        ],"tier":"consistency_check","grp":"hh_principles_1","tags":["principles","temporal"]},
        {"qt":"behavioral_recall","text":"How do you handle situations where being honest would clearly disadvantage you?","opts":[
            {"id":"a","text":"I'm honest anyway — short-term disadvantage beats long-term integrity loss","s":5},
            {"id":"b","text":"I weigh the cost and sometimes shade the truth if the stakes are high","s":2},
            {"id":"c","text":"I protect my interests first — honesty is a luxury in competitive situations","s":1},
            {"id":"d","text":"I find a way to be truthful without volunteering information that hurts me","s":3}
        ],"tier":"core","grp":"hh_costly_honesty_1","tags":["costly_honesty","integrity"]},
        {"qt":"scenario","text":"A cashier gives you too much change — $20 extra. You:","opts":[
            {"id":"a","text":"Return it immediately without hesitation","s":5},
            {"id":"b","text":"Notice it later and feel too awkward to go back","s":3},
            {"id":"c","text":"Keep it — the store won't miss it","s":1},
            {"id":"d","text":"Return it, but only because you'd want someone to do the same for you","s":4}
        ],"tier":"triangulation","grp":"hh_honesty_3","tags":["honesty","everyday_integrity"]},
        {"qt":"forced_choice","text":"When comparing yourself to others in terms of entitlement, you:","opts":[
            {"id":"a","text":"Don't feel entitled to special treatment — I should earn what I get","s":5},
            {"id":"b","text":"Know my worth and expect to be treated accordingly","s":2},
            {"id":"c","text":"Believe I deserve the best and pursue it unapologetically","s":1},
            {"id":"d","text":"Sometimes feel I deserve more but keep it to myself","s":3}
        ],"tier":"core","grp":"hh_entitlement_1","tags":["entitlement","humility"]},
        {"qt":"behavioral_recall","text":"How do you react when someone you look up to turns out to have ethical failings?","opts":[
            {"id":"a","text":"Deeply disappointed — character matters more than capability","s":5},
            {"id":"b","text":"Separate their work from their character — both can be true","s":2},
            {"id":"c","text":"It doesn't change my opinion of their work — everyone has flaws","s":1},
            {"id":"d","text":"Reassess my relationship with them entirely","s":4}
        ],"tier":"triangulation","grp":"hh_ethical_1","tags":["ethics","character_assessment"]},
    ],
    "emotionality": [
        {"qt":"scenario","text":"You're watching a movie and a character loses a loved one. You:","opts":[
            {"id":"a","text":"Feel tears welling up — fictional or not, loss resonates deeply with you","s":5},
            {"id":"b","text":"Feel moved but maintain composure","s":3},
            {"id":"c","text":"Appreciate the storytelling but don't feel it emotionally","s":1},
            {"id":"d","text":"Get fully absorbed and might cry openly","s":5}
        ],"tier":"core","grp":"em_sensitivity_1","tags":["emotional_sensitivity","empathy"]},
        {"qt":"behavioral_recall","text":"When facing a stressful situation (job interview, medical test), you tend to:","opts":[
            {"id":"a","text":"Experience significant anxiety that's hard to control","s":5},
            {"id":"b","text":"Feel nervous but manage it well","s":3},
            {"id":"c","text":"Stay remarkably calm — stress doesn't affect me much","s":1},
            {"id":"d","text":"Seek reassurance from someone close to me","s":4}
        ],"tier":"core","grp":"em_anxiety_1","tags":["anxiety","stress"]},
        {"qt":"forced_choice","text":"In close relationships, you tend to:","opts":[
            {"id":"a","text":"Need frequent emotional reassurance and closeness","s":5},
            {"id":"b","text":"Balance closeness with independence comfortably","s":2},
            {"id":"c","text":"Value independence and feel smothered by too much emotional demand","s":1},
            {"id":"d","text":"Provide emotional support more than you seek it","s":3}
        ],"tier":"core","grp":"em_dependence_1","tags":["emotional_dependence","attachment"]},
        {"qt":"somatic","text":"When someone you care about is in distress, what happens in your body?","opts":[
            {"id":"a","text":"I feel their pain almost physically — it's like it's happening to me","s":5},
            {"id":"b","text":"I feel concerned and want to help, but I maintain emotional boundaries","s":2},
            {"id":"c","text":"I stay calm and focused on practical solutions","s":1},
            {"id":"d","text":"My heart rate increases and I feel an urgent need to do something","s":4}
        ],"tier":"core","grp":"em_empathy_1","tags":["somatic","empathic_response"]},
        {"qt":"scenario","text":"You receive unexpected criticism from someone whose opinion matters to you. You:","opts":[
            {"id":"a","text":"Feel devastated — it occupies your mind for days","s":5},
            {"id":"b","text":"Feel hurt initially but recover within hours","s":3},
            {"id":"c","text":"Evaluate the criticism objectively and move on","s":1},
            {"id":"d","text":"Feel deeply hurt but try to learn from it","s":4}
        ],"tier":"core","grp":"em_sensitivity_2","tags":["sensitivity","criticism"]},
        {"qt":"temporal","text":"How has your emotional sensitivity changed over the years?","opts":[
            {"id":"a","text":"I've always been highly sensitive — it's a core part of who I am","s":5},
            {"id":"b","text":"I've become more emotionally resilient with experience","s":2},
            {"id":"c","text":"I was always fairly thick-skinned","s":1},
            {"id":"d","text":"I've become more sensitive as I've allowed myself to be more open","s":4}
        ],"tier":"core","grp":"em_temporal_1","tags":["sensitivity","temporal"]},
        {"qt":"forced_choice","text":"When you're going through a difficult time, you prefer to:","opts":[
            {"id":"a","text":"Talk about my feelings extensively with people I trust","s":5},
            {"id":"b","text":"Process it internally and share only when I've sorted it out","s":1},
            {"id":"c","text":"Distract myself with activity and not dwell on it","s":1},
            {"id":"d","text":"Seek physical comfort — hugs, presence, being held","s":5}
        ],"tier":"core","grp":"em_coping_1","tags":["coping","emotional_processing"]},
        {"qt":"scenario","text":"A stranger on the bus is crying quietly. You:","opts":[
            {"id":"a","text":"Feel a strong pull to comfort them — their pain moves you","s":5},
            {"id":"b","text":"Respect their privacy but feel compassion","s":3},
            {"id":"c","text":"Barely notice — you're absorbed in your own thoughts","s":1},
            {"id":"d","text":"Offer a tissue or a kind word if it feels appropriate","s":4}
        ],"tier":"triangulation","grp":"em_stranger_empathy_1","tags":["empathy","strangers"]},
        {"qt":"behavioral_recall","text":"How often do you cry?","opts":[
            {"id":"a","text":"Regularly — movies, music, beautiful moments, sad news all move me to tears","s":5},
            {"id":"b","text":"Occasionally — at funerals or truly significant moments","s":3},
            {"id":"c","text":"Rarely — I can't remember the last time","s":1},
            {"id":"d","text":"More than I'd expect — it catches me off guard","s":4}
        ],"tier":"core","grp":"em_crying_1","tags":["crying","emotional_expression"]},
        {"qt":"somatic","text":"When you're anticipating a potential loss (a friend moving away, a pet aging), you feel:","opts":[
            {"id":"a","text":"Pre-emptive grief — I feel the loss before it happens","s":5},
            {"id":"b","text":"Sadness that I acknowledge and process","s":3},
            {"id":"c","text":"I try not to think about it until it happens","s":1},
            {"id":"d","text":"A physical heaviness in my chest that's hard to shake","s":5}
        ],"tier":"core","grp":"em_anticipatory_1","tags":["somatic","anticipatory_grief"]},
        {"qt":"scenario","text":"You're home alone on a stormy night and you hear an unexpected noise. You:","opts":[
            {"id":"a","text":"Feel genuine fear — your imagination runs to worst-case scenarios","s":5},
            {"id":"b","text":"Feel a brief startle and then investigate calmly","s":2},
            {"id":"c","text":"Barely react — it's probably nothing","s":1},
            {"id":"d","text":"Feel scared and wish someone else were home with you","s":5}
        ],"tier":"core","grp":"em_fearfulness_1","tags":["fearfulness","safety"]},
        {"qt":"forced_choice","text":"How would you describe your emotional range?","opts":[
            {"id":"a","text":"Wide and intense — I experience highs and lows vividly","s":5},
            {"id":"b","text":"Moderate — I feel things but stay within a comfortable range","s":2},
            {"id":"c","text":"Narrow — I'm fairly even-keeled regardless of circumstances","s":1},
            {"id":"d","text":"Deep — I feel things profoundly but don't always show it","s":4}
        ],"tier":"core","grp":"em_range_1","tags":["emotional_range","intensity"]},
        {"qt":"behavioral_recall","text":"When you need to make a decision, how much does emotion influence you?","opts":[
            {"id":"a","text":"Significantly — my feelings are important data that guide my choices","s":5},
            {"id":"b","text":"I consider emotions but logic ultimately drives the decision","s":2},
            {"id":"c","text":"I try to keep emotion out of decisions entirely","s":1},
            {"id":"d","text":"Emotion and logic both play equal roles","s":3}
        ],"tier":"triangulation","grp":"em_decision_1","tags":["emotional_decision_making"]},
        {"qt":"scenario","text":"A friend shares that they've been diagnosed with a serious illness. Your immediate response is:","opts":[
            {"id":"a","text":"Tears — you feel their fear and pain viscerally","s":5},
            {"id":"b","text":"Deep concern and immediate practical support — what do they need?","s":2},
            {"id":"c","text":"Reassurance — statistics are in their favor, stay positive","s":1},
            {"id":"d","text":"Listening with your full attention and holding space for their emotions","s":4}
        ],"tier":"core","grp":"em_empathic_response_1","tags":["empathy","crisis_response"]},
        {"qt":"temporal","text":"Looking back, how has your ability to handle emotional pain changed?","opts":[
            {"id":"a","text":"I still feel things as intensely as ever — maybe more so","s":5},
            {"id":"b","text":"I've built better coping mechanisms but the pain is just as real","s":4},
            {"id":"c","text":"I've become more detached — self-protection through distance","s":1},
            {"id":"d","text":"I've developed emotional resilience — pain is temporary and I know that now","s":2}
        ],"tier":"consistency_check","grp":"em_pain_1","tags":["emotional_pain","temporal"]},
        {"qt":"somatic","text":"When you feel emotionally overwhelmed, where does it manifest in your body?","opts":[
            {"id":"a","text":"Everywhere — tight chest, watery eyes, shaky hands, heavy limbs","s":5},
            {"id":"b","text":"Mostly in my chest and throat","s":4},
            {"id":"c","text":"I don't really feel emotions in my body","s":1},
            {"id":"d","text":"Stomach and head — nausea and headaches","s":3}
        ],"tier":"core","grp":"em_somatic_1","tags":["somatic","overwhelm"]},
        {"qt":"forced_choice","text":"Which describes your need for emotional closeness in relationships?","opts":[
            {"id":"a","text":"Very high — I need deep emotional intimacy to feel secure","s":5},
            {"id":"b","text":"Moderate — I like closeness but also value my independence","s":2},
            {"id":"c","text":"Low — too much emotional closeness feels claustrophobic","s":1},
            {"id":"d","text":"It varies by relationship — some I want close, others I keep at arm's length","s":3}
        ],"tier":"core","grp":"em_closeness_1","tags":["emotional_closeness","attachment"]},
        {"qt":"behavioral_recall","text":"How easily do you pick up on others' emotional states?","opts":[
            {"id":"a","text":"Instantly — I read rooms and feel shifts in energy before anything is said","s":5},
            {"id":"b","text":"Usually — I notice when someone is off but I might miss subtleties","s":3},
            {"id":"c","text":"Only when it's obvious — I'm not naturally tuned into emotional cues","s":1},
            {"id":"d","text":"Very well, but I sometimes absorb others' emotions and need to decompress","s":5}
        ],"tier":"core","grp":"em_emotional_radar_1","tags":["emotional_intelligence","perception"]},
        {"qt":"scenario","text":"You're about to give a presentation to 200 people. Minutes before, you feel:","opts":[
            {"id":"a","text":"Intense anxiety — sweating, heart racing, stomach churning","s":5},
            {"id":"b","text":"Normal nervousness that sharpens your performance","s":3},
            {"id":"c","text":"Calm and ready — this doesn't faze you","s":1},
            {"id":"d","text":"Excited and anxious in equal measure","s":3}
        ],"tier":"triangulation","grp":"em_performance_anxiety_1","tags":["anxiety","performance"]},
        {"qt":"forced_choice","text":"When you haven't heard from a close friend in a while, you:","opts":[
            {"id":"a","text":"Worry something is wrong — your mind goes to negative possibilities","s":5},
            {"id":"b","text":"Reach out casually to check in","s":3},
            {"id":"c","text":"Don't think about it — people have their own lives","s":1},
            {"id":"d","text":"Feel a pang of worry but trust the relationship is fine","s":3}
        ],"tier":"core","grp":"em_worry_1","tags":["worry","attachment"]},
    ],
    "extraversion": [
        {"qt":"scenario","text":"You have a completely free Saturday. Your ideal day involves:","opts":[
            {"id":"a","text":"Calling friends, making plans, being around people all day","s":5},
            {"id":"b","text":"A mix — brunch with friends, afternoon alone, evening out","s":3},
            {"id":"c","text":"A quiet day at home — reading, hobbies, recharging alone","s":1},
            {"id":"d","text":"An adventure — exploring somewhere new, preferably with company","s":4}
        ],"tier":"core","grp":"ex_sociability_1","tags":["sociability","energy_source"]},
        {"qt":"behavioral_recall","text":"At work, you're most productive when:","opts":[
            {"id":"a","text":"I'm around others — the energy of a busy environment helps me focus","s":5},
            {"id":"b","text":"I alternate between collaboration and solo work","s":3},
            {"id":"c","text":"I'm alone with minimal interruptions","s":1},
            {"id":"d","text":"I'm in a small group working closely together","s":4}
        ],"tier":"core","grp":"ex_work_style_1","tags":["work_style","environment"]},
        {"qt":"forced_choice","text":"In social situations, you tend to:","opts":[
            {"id":"a","text":"Seek the spotlight — I enjoy leading conversations and being noticed","s":5},
            {"id":"b","text":"Participate actively but don't need to be the center","s":3},
            {"id":"c","text":"Stay on the periphery and engage only when approached","s":1},
            {"id":"d","text":"Seek deep one-on-one conversations rather than group interaction","s":2}
        ],"tier":"core","grp":"ex_social_boldness_1","tags":["social_boldness","attention"]},
        {"qt":"somatic","text":"After spending several hours at a lively social event, you feel:","opts":[
            {"id":"a","text":"Energized and wanting more — this is fuel for me","s":5},
            {"id":"b","text":"Pleasantly tired — it was fun but I'm ready to wind down","s":3},
            {"id":"c","text":"Completely drained — I need at least a day to recover","s":1},
            {"id":"d","text":"Happy but ready for quiet — my social battery is full","s":2}
        ],"tier":"core","grp":"ex_energy_1","tags":["somatic","social_energy"]},
        {"qt":"scenario","text":"You're at a conference and the evening networking event is optional. You:","opts":[
            {"id":"a","text":"Attend enthusiastically — networking events are where real connections happen","s":5},
            {"id":"b","text":"Go for an hour to make a few connections then leave","s":3},
            {"id":"c","text":"Skip it — you're socially exhausted from the day's sessions","s":1},
            {"id":"d","text":"Find one or two interesting people for a quiet dinner instead","s":2}
        ],"tier":"core","grp":"ex_networking_1","tags":["networking","social_initiative"]},
        {"qt":"temporal","text":"How has your social energy changed over the years?","opts":[
            {"id":"a","text":"I've always been highly social — people are my primary energy source","s":5},
            {"id":"b","text":"I've become slightly less social but still enjoy people","s":3},
            {"id":"c","text":"I've always preferred solitude and small groups","s":1},
            {"id":"d","text":"I've learned to manage my social energy better but the need hasn't changed","s":4}
        ],"tier":"core","grp":"ex_temporal_1","tags":["social_energy","temporal"]},
        {"qt":"forced_choice","text":"Which describes your self-esteem?","opts":[
            {"id":"a","text":"High — I feel confident in most situations and believe in my abilities","s":5},
            {"id":"b","text":"Moderate — I have confidence in some areas and doubt in others","s":3},
            {"id":"c","text":"Variable — my self-esteem depends heavily on context and feedback","s":2},
            {"id":"d","text":"Quiet confidence — I don't need external validation but I know my worth","s":4}
        ],"tier":"core","grp":"ex_self_esteem_1","tags":["self_esteem","confidence"]},
        {"qt":"scenario","text":"You're waiting for a bus and the only other person at the stop seems approachable. You:","opts":[
            {"id":"a","text":"Strike up a conversation — meeting new people is always interesting","s":5},
            {"id":"b","text":"Smile and say hello but don't push for conversation","s":3},
            {"id":"c","text":"Put in headphones — you prefer your own company","s":1},
            {"id":"d","text":"Wait to see if they initiate — you'll engage if they do","s":2}
        ],"tier":"triangulation","grp":"ex_initiation_1","tags":["social_initiation","strangers"]},
        {"qt":"behavioral_recall","text":"When you're excited about something, you tend to:","opts":[
            {"id":"a","text":"Tell everyone — my enthusiasm is contagious and I can't contain it","s":5},
            {"id":"b","text":"Share with a few close people who'd appreciate it","s":3},
            {"id":"c","text":"Savor it internally — I don't need to externalize my excitement","s":1},
            {"id":"d","text":"Express it physically — jumping, laughing, high energy","s":5}
        ],"tier":"core","grp":"ex_expression_1","tags":["emotional_expression","enthusiasm"]},
        {"qt":"somatic","text":"When you've been alone for an extended period (a full weekend), you feel:","opts":[
            {"id":"a","text":"Starved for interaction — I start reaching out to anyone available","s":5},
            {"id":"b","text":"Ready to see people but not desperate","s":3},
            {"id":"c","text":"Recharged and content — I could keep going","s":1},
            {"id":"d","text":"A mix — refreshed but starting to want company","s":3}
        ],"tier":"core","grp":"ex_solitude_1","tags":["somatic","solitude_tolerance"]},
        {"qt":"forced_choice","text":"In group decision-making, you tend to:","opts":[
            {"id":"a","text":"Voice your opinion early and confidently — I shape the direction","s":5},
            {"id":"b","text":"Share thoughts when asked but don't dominate","s":3},
            {"id":"c","text":"Listen and process before contributing — my best input comes later","s":1},
            {"id":"d","text":"Build on others' ideas to create consensus","s":3}
        ],"tier":"triangulation","grp":"ex_assertiveness_1","tags":["assertiveness","group_participation"]},
        {"qt":"scenario","text":"A friend invites you to a party where you'll know nobody except them. You:","opts":[
            {"id":"a","text":"Excited — meeting new people is one of your favorite things","s":5},
            {"id":"b","text":"Go willingly but stay close to your friend at first","s":3},
            {"id":"c","text":"Dread it but go out of obligation","s":1},
            {"id":"d","text":"Suggest a smaller gathering instead","s":1}
        ],"tier":"core","grp":"ex_new_people_1","tags":["new_people","social_comfort"]},
        {"qt":"behavioral_recall","text":"How do you typically handle silence in a conversation?","opts":[
            {"id":"a","text":"Fill it — silence is uncomfortable and I always have something to say","s":5},
            {"id":"b","text":"Let it sit briefly then bridge to a new topic","s":3},
            {"id":"c","text":"Enjoy it — comfortable silence is a sign of a good relationship","s":1},
            {"id":"d","text":"Depends on who I'm with — some silences are fine, others feel awkward","s":3}
        ],"tier":"triangulation","grp":"ex_silence_1","tags":["silence","conversation"]},
        {"qt":"temporal","text":"How has your confidence in social situations changed?","opts":[
            {"id":"a","text":"I've always been socially confident — it's natural for me","s":5},
            {"id":"b","text":"I've grown more confident through experience","s":3},
            {"id":"c","text":"Social situations still make me uncomfortable despite experience","s":1},
            {"id":"d","text":"I've become more selectively social — confident in chosen settings","s":3}
        ],"tier":"consistency_check","grp":"ex_confidence_1","tags":["social_confidence","temporal"]},
        {"qt":"somatic","text":"When you walk into a room full of people you need to impress, you feel:","opts":[
            {"id":"a","text":"A surge of energy — I'm in my element","s":5},
            {"id":"b","text":"Normal alertness — I can handle this","s":3},
            {"id":"c","text":"Anxiety that manifests as a racing heart and dry mouth","s":1},
            {"id":"d","text":"Focused determination — time to perform","s":3}
        ],"tier":"core","grp":"ex_social_pressure_1","tags":["somatic","social_pressure"]},
        {"qt":"forced_choice","text":"Which statement best describes your communication preference?","opts":[
            {"id":"a","text":"I think out loud — talking IS my processing method","s":5},
            {"id":"b","text":"I balance talking and thinking — both have their place","s":3},
            {"id":"c","text":"I process internally first and speak only when I've formed a clear thought","s":1},
            {"id":"d","text":"I prefer written communication over verbal","s":1}
        ],"tier":"core","grp":"ex_communication_1","tags":["communication_preference"]},
        {"qt":"scenario","text":"You're leading a meeting and a quiet team member hasn't spoken. You:","opts":[
            {"id":"a","text":"Draw them in enthusiastically — their input matters","s":5},
            {"id":"b","text":"Create space for them but don't put them on the spot","s":3},
            {"id":"c","text":"Respect their silence — not everyone needs to speak in meetings","s":1},
            {"id":"d","text":"Check in with them privately after the meeting","s":2}
        ],"tier":"triangulation","grp":"ex_leadership_social_1","tags":["leadership","inclusion"]},
        {"qt":"behavioral_recall","text":"Your phone rings and it's an unknown number. You:","opts":[
            {"id":"a","text":"Answer it — could be something interesting","s":5},
            {"id":"b","text":"Let it go to voicemail and call back if needed","s":2},
            {"id":"c","text":"Never answer unknown numbers — text me instead","s":1},
            {"id":"d","text":"Answer depending on my mood and what I'm doing","s":3}
        ],"tier":"triangulation","grp":"ex_openness_to_contact_1","tags":["social_openness","phone_behavior"]},
        {"qt":"forced_choice","text":"How do you feel about small talk?","opts":[
            {"id":"a","text":"I enjoy it — it's the gateway to deeper connection","s":5},
            {"id":"b","text":"It's a necessary social skill that I use competently","s":3},
            {"id":"c","text":"I find it exhausting and meaningless — get to the real conversation","s":1},
            {"id":"d","text":"It depends on the person — some people make it enjoyable","s":3}
        ],"tier":"core","grp":"ex_smalltalk_1","tags":["small_talk","social_skills"]},
        {"qt":"scenario","text":"You're given the choice between a solo office and a collaborative open workspace. You choose:","opts":[
            {"id":"a","text":"Open workspace without hesitation — I need the energy of people around me","s":5},
            {"id":"b","text":"Open workspace but with access to a quiet room when needed","s":3},
            {"id":"c","text":"Solo office — no question, I need my own space","s":1},
            {"id":"d","text":"Solo office with an open door policy — on my terms","s":2}
        ],"tier":"core","grp":"ex_workspace_1","tags":["workspace","environment_preference"]},
    ],
    "agreeableness": [
        {"qt":"scenario","text":"Someone cuts in line right in front of you. You:","opts":[
            {"id":"a","text":"Let it go — it's not worth getting upset about","s":5},
            {"id":"b","text":"Politely point out the line","s":3},
            {"id":"c","text":"Call them out firmly — line-cutting is disrespectful","s":1},
            {"id":"d","text":"Feel irritated but say nothing to avoid confrontation","s":4}
        ],"tier":"core","grp":"ag_patience_1","tags":["patience","conflict_avoidance"]},
        {"qt":"behavioral_recall","text":"When you disagree with someone's opinion in a group setting, you typically:","opts":[
            {"id":"a","text":"Find common ground first, then gently introduce your perspective","s":5},
            {"id":"b","text":"Respectfully state your disagreement with clear reasoning","s":3},
            {"id":"c","text":"Challenge their position directly — weak ideas need to be confronted","s":1},
            {"id":"d","text":"Stay quiet unless directly asked — the disagreement isn't worth the friction","s":4}
        ],"tier":"core","grp":"ag_gentleness_1","tags":["gentleness","disagreement"]},
        {"qt":"forced_choice","text":"Which best describes your approach to judging others?","opts":[
            {"id":"a","text":"I give people the benefit of the doubt — everyone has reasons for their behavior","s":5},
            {"id":"b","text":"I try to be fair but I form opinions based on evidence","s":3},
            {"id":"c","text":"I'm quick to assess people and I'm usually right","s":1},
            {"id":"d","text":"I withhold judgment until I know someone well","s":4}
        ],"tier":"core","grp":"ag_judgment_1","tags":["judgment","benefit_of_doubt"]},
        {"qt":"somatic","text":"When someone is angry at you, even if you think they're wrong, you:","opts":[
            {"id":"a","text":"Feel compelled to smooth things over — their anger is physically distressing to me","s":5},
            {"id":"b","text":"Stay calm and try to understand their perspective","s":3},
            {"id":"c","text":"Match their energy — if they want a fight, I won't back down","s":1},
            {"id":"d","text":"Feel anxious but hold my ground quietly","s":3}
        ],"tier":"core","grp":"ag_anger_response_1","tags":["somatic","conflict_response"]},
        {"qt":"scenario","text":"A colleague consistently takes credit for team efforts. Others are annoyed but nobody speaks up. You:","opts":[
            {"id":"a","text":"Try to see their perspective — maybe they don't realize they're doing it","s":5},
            {"id":"b","text":"Address it calmly and constructively in private","s":3},
            {"id":"c","text":"Confront them publicly the next time it happens","s":1},
            {"id":"d","text":"Sympathize with colleagues but avoid direct confrontation","s":4}
        ],"tier":"core","grp":"ag_confrontation_1","tags":["confrontation","understanding"]},
        {"qt":"temporal","text":"How has your willingness to compromise changed over the years?","opts":[
            {"id":"a","text":"I've always been a natural compromiser — harmony matters more than winning","s":5},
            {"id":"b","text":"I've learned when to compromise and when to stand firm","s":3},
            {"id":"c","text":"I've become less willing to compromise — I know what I want","s":1},
            {"id":"d","text":"I still compromise too easily and I know it","s":4}
        ],"tier":"core","grp":"ag_compromise_1","tags":["compromise","temporal"]},
        {"qt":"forced_choice","text":"How do you handle it when someone insults you?","opts":[
            {"id":"a","text":"I genuinely try to understand what prompted it and respond with compassion","s":5},
            {"id":"b","text":"I address it calmly but make it clear the behavior is unacceptable","s":3},
            {"id":"c","text":"I fire back — disrespect earns disrespect","s":1},
            {"id":"d","text":"I disengage — it says more about them than me","s":4}
        ],"tier":"core","grp":"ag_insults_1","tags":["insults","response_style"]},
        {"qt":"scenario","text":"You're mediating a dispute between two friends. One is clearly more in the wrong. You:","opts":[
            {"id":"a","text":"Help both see the other's perspective without assigning blame","s":5},
            {"id":"b","text":"Gently point out where each person could do better","s":3},
            {"id":"c","text":"Tell the person who's wrong that they're wrong — honestly helps more than coddling","s":1},
            {"id":"d","text":"Focus on feelings rather than facts — both need to feel heard","s":4}
        ],"tier":"core","grp":"ag_mediation_1","tags":["mediation","fairness"]},
        {"qt":"behavioral_recall","text":"When you're frustrated with someone's behavior, you tend to:","opts":[
            {"id":"a","text":"Assume good intentions and give them space to improve","s":5},
            {"id":"b","text":"Express your frustration constructively","s":3},
            {"id":"c","text":"Let them know exactly how their behavior is affecting things","s":1},
            {"id":"d","text":"Suppress the frustration to keep the peace","s":4}
        ],"tier":"core","grp":"ag_frustration_1","tags":["frustration","expression"]},
        {"qt":"somatic","text":"When you witness a heated argument between others, you feel:","opts":[
            {"id":"a","text":"Physically uncomfortable — tension in my body until it's resolved","s":5},
            {"id":"b","text":"Engaged — I want to help find a resolution","s":3},
            {"id":"c","text":"Nothing strong — conflict is a normal part of life","s":1},
            {"id":"d","text":"Anxious and wanting to leave the room","s":4}
        ],"tier":"core","grp":"ag_witness_conflict_1","tags":["somatic","conflict_sensitivity"]},
        {"qt":"forced_choice","text":"Your natural assumption about strangers' intentions is:","opts":[
            {"id":"a","text":"Positive — most people are fundamentally good and well-meaning","s":5},
            {"id":"b","text":"Neutral — I assess each person individually","s":3},
            {"id":"c","text":"Guarded — I trust people only after they've earned it","s":1},
            {"id":"d","text":"Optimistic but watchful — I hope for the best while staying alert","s":4}
        ],"tier":"core","grp":"ag_trust_1","tags":["trust","default_assumption"]},
        {"qt":"scenario","text":"You strongly believe a friend is making a terrible life decision. They haven't asked for advice. You:","opts":[
            {"id":"a","text":"Respect their autonomy — it's their life to live","s":5},
            {"id":"b","text":"Share your concern gently, once, and let it go","s":3},
            {"id":"c","text":"Tell them directly and persistently — real friends don't let friends fail","s":1},
            {"id":"d","text":"Find a way to subtly introduce information that might change their mind","s":3}
        ],"tier":"triangulation","grp":"ag_unsolicited_advice_1","tags":["unsolicited_advice","respect"]},
        {"qt":"behavioral_recall","text":"After an argument, even when you were right, you tend to:","opts":[
            {"id":"a","text":"Reach out first to repair — being right matters less than the relationship","s":5},
            {"id":"b","text":"Wait a cooling period then reconnect normally","s":3},
            {"id":"c","text":"Wait for them to come to you — you were right, after all","s":1},
            {"id":"d","text":"Feel bad about the argument regardless of who was right","s":4}
        ],"tier":"core","grp":"ag_repair_1","tags":["repair","reconciliation"]},
        {"qt":"temporal","text":"How has your tolerance for difficult people changed?","opts":[
            {"id":"a","text":"I've always had high tolerance — every person has something to offer","s":5},
            {"id":"b","text":"I've become more selective about who gets my energy","s":2},
            {"id":"c","text":"I have less patience for difficult people now — life is too short","s":1},
            {"id":"d","text":"I still give too many chances — I need to set better boundaries","s":4}
        ],"tier":"consistency_check","grp":"ag_tolerance_1","tags":["tolerance","temporal"]},
        {"qt":"forced_choice","text":"When someone apologizes for hurting you, you:","opts":[
            {"id":"a","text":"Forgive immediately and genuinely — holding grudges hurts me more than them","s":5},
            {"id":"b","text":"Accept the apology but need time to rebuild trust","s":3},
            {"id":"c","text":"Evaluate whether the apology is genuine before responding","s":1},
            {"id":"d","text":"Forgive quickly to restore harmony, even if I'm still hurt inside","s":4}
        ],"tier":"core","grp":"ag_forgiveness_1","tags":["forgiveness","grudges"]},
        {"qt":"scenario","text":"In a team meeting, everyone is excited about a plan that you think has problems, but the enthusiasm is high. You:","opts":[
            {"id":"a","text":"Go along with the energy — you don't want to be the buzzkill","s":5},
            {"id":"b","text":"Raise your concerns diplomatically without dampening enthusiasm","s":3},
            {"id":"c","text":"Point out the flaws clearly — enthusiasm doesn't excuse poor planning","s":1},
            {"id":"d","text":"Stay quiet in the meeting but share concerns privately with the lead","s":4}
        ],"tier":"triangulation","grp":"ag_groupthink_1","tags":["groupthink","dissent"]},
        {"qt":"behavioral_recall","text":"How do you handle passive-aggressive behavior from others?","opts":[
            {"id":"a","text":"Respond with kindness — maybe they're going through something difficult","s":5},
            {"id":"b","text":"Address it directly but calmly — passive aggression needs to be named","s":3},
            {"id":"c","text":"Match it or escalate — games deserve game-level responses","s":1},
            {"id":"d","text":"Ignore it and hope it stops","s":4}
        ],"tier":"core","grp":"ag_passive_aggression_1","tags":["passive_aggression","response"]},
        {"qt":"somatic","text":"When you hold back your true opinion to keep the peace, you feel:","opts":[
            {"id":"a","text":"Comfortable — preserving harmony IS my true preference","s":5},
            {"id":"b","text":"Slightly frustrated but it passes quickly","s":3},
            {"id":"c","text":"Resentful — I should have spoken my mind","s":1},
            {"id":"d","text":"A familiar tightness — I do this often and I know the cost","s":3}
        ],"tier":"core","grp":"ag_self_suppression_1","tags":["somatic","self_suppression"]},
        {"qt":"forced_choice","text":"Which describes your relationship with anger?","opts":[
            {"id":"a","text":"Anger is rare for me — I genuinely don't get angry easily","s":5},
            {"id":"b","text":"I feel anger but express it constructively","s":3},
            {"id":"c","text":"Anger is a frequent and useful emotion for me","s":1},
            {"id":"d","text":"I suppress anger to the point where others don't know I'm upset","s":4}
        ],"tier":"core","grp":"ag_anger_1","tags":["anger","temperament"]},
        {"qt":"scenario","text":"Your neighbor plays loud music late at night regularly. You:","opts":[
            {"id":"a","text":"Wait, hoping they'll realize on their own — confrontation feels extreme","s":5},
            {"id":"b","text":"Leave a polite note or mention it casually next time you see them","s":3},
            {"id":"c","text":"Knock on their door and tell them firmly to turn it down","s":1},
            {"id":"d","text":"Buy earplugs — it's easier to adapt than to confront","s":4}
        ],"tier":"triangulation","grp":"ag_neighbor_1","tags":["confrontation","avoidance"]},
    ],
    "conscientiousness": [
        {"qt":"scenario","text":"You promised to help a friend move this Saturday. A much more exciting invitation comes up for the same day. You:","opts":[
            {"id":"a","text":"Keep your promise without hesitation — your word is your bond","s":5},
            {"id":"b","text":"See if you can do both — help move in the morning, event in the evening","s":3},
            {"id":"c","text":"Apologize to your friend and go to the better event — life's short","s":1},
            {"id":"d","text":"Keep your promise but feel resentful about missing the event","s":4}
        ],"tier":"core","grp":"co_diligence_1","tags":["commitment","diligence"]},
        {"qt":"behavioral_recall","text":"How disciplined are you with long-term goals?","opts":[
            {"id":"a","text":"Very — I set goals and work toward them daily with consistent effort","s":5},
            {"id":"b","text":"Moderate — I make progress but with some starts and stops","s":3},
            {"id":"c","text":"Low — I set goals but rarely follow through long-term","s":1},
            {"id":"d","text":"Depends on the goal — I'm disciplined about things that excite me","s":2}
        ],"tier":"core","grp":"co_discipline_1","tags":["discipline","long_term_goals"]},
        {"qt":"forced_choice","text":"Your approach to deadlines is:","opts":[
            {"id":"a","text":"I finish well before the deadline — I hate last-minute pressure","s":5},
            {"id":"b","text":"I meet deadlines consistently but don't aim to be early","s":3},
            {"id":"c","text":"I work best under deadline pressure — I often finish just in time","s":1},
            {"id":"d","text":"I set my own earlier deadline to build in buffer time","s":5}
        ],"tier":"core","grp":"co_deadlines_1","tags":["deadlines","time_management"]},
        {"qt":"somatic","text":"When your space is disorganized, you feel:","opts":[
            {"id":"a","text":"Physically uncomfortable — I can't function until I tidy up","s":5},
            {"id":"b","text":"Mild irritation — I'll get to it when I can","s":3},
            {"id":"c","text":"Fine — organized chaos works for me","s":1},
            {"id":"d","text":"Anxious — clutter creates mental noise","s":4}
        ],"tier":"core","grp":"co_organization_1","tags":["somatic","organization"]},
        {"qt":"scenario","text":"You're working on a task and realize you could take a shortcut that would save two hours but might introduce a small risk of error. You:","opts":[
            {"id":"a","text":"Do it the thorough way — shortcuts are how mistakes happen","s":5},
            {"id":"b","text":"Take the shortcut if the risk is truly small","s":2},
            {"id":"c","text":"Always take the shortcut — efficiency over perfection","s":1},
            {"id":"d","text":"Evaluate the risk precisely before deciding","s":4}
        ],"tier":"core","grp":"co_thoroughness_1","tags":["thoroughness","shortcuts"]},
        {"qt":"temporal","text":"How has your level of self-discipline changed over the years?","opts":[
            {"id":"a","text":"I've always been highly disciplined — it's a core trait","s":5},
            {"id":"b","text":"I've become more disciplined through practice and maturity","s":3},
            {"id":"c","text":"I'm still working on it — discipline doesn't come naturally to me","s":1},
            {"id":"d","text":"My discipline is strong in certain areas but weak in others","s":2}
        ],"tier":"core","grp":"co_temporal_1","tags":["discipline","temporal"]},
        {"qt":"forced_choice","text":"When planning a project, you:","opts":[
            {"id":"a","text":"Create a detailed plan with milestones, timelines, and contingencies","s":5},
            {"id":"b","text":"Create a loose framework and fill in details as you go","s":3},
            {"id":"c","text":"Start working and figure it out along the way","s":1},
            {"id":"d","text":"Plan the critical path carefully and leave room for adaptation","s":4}
        ],"tier":"core","grp":"co_planning_1","tags":["planning","organization"]},
        {"qt":"behavioral_recall","text":"How often do you procrastinate on important tasks?","opts":[
            {"id":"a","text":"Almost never — I tackle important tasks first","s":5},
            {"id":"b","text":"Sometimes — but I always get them done on time","s":3},
            {"id":"c","text":"Often — I tend to put off what's difficult or boring","s":1},
            {"id":"d","text":"I procrastinate on certain types of tasks but not others","s":2}
        ],"tier":"core","grp":"co_procrastination_1","tags":["procrastination","task_management"]},
        {"qt":"scenario","text":"You notice a small error in a document that's already been approved and distributed. Nobody else noticed. You:","opts":[
            {"id":"a","text":"Correct it and redistribute — errors shouldn't stand just because they're unnoticed","s":5},
            {"id":"b","text":"Make a note to correct it in the next version","s":3},
            {"id":"c","text":"Leave it — it's minor and fixing it would be more trouble than it's worth","s":1},
            {"id":"d","text":"Fix it quietly without drawing attention to the error","s":4}
        ],"tier":"core","grp":"co_error_correction_1","tags":["error_correction","standards"]},
        {"qt":"somatic","text":"When a project you're responsible for has loose ends, even minor ones, you feel:","opts":[
            {"id":"a","text":"Nagging discomfort until every loose end is tied up","s":5},
            {"id":"b","text":"Aware of them but able to move on","s":3},
            {"id":"c","text":"Unbothered — some loose ends are just part of life","s":1},
            {"id":"d","text":"Compelled to document them even if I can't fix them right now","s":4}
        ],"tier":"core","grp":"co_completion_1","tags":["somatic","completion"]},
        {"qt":"forced_choice","text":"How do you feel about making decisions impulsively?","opts":[
            {"id":"a","text":"Uncomfortable — I need to think things through before committing","s":5},
            {"id":"b","text":"Sometimes it's necessary — not every decision needs deep analysis","s":3},
            {"id":"c","text":"I'm naturally impulsive and it usually works out","s":1},
            {"id":"d","text":"I'm impulsive with low-stakes decisions but methodical with important ones","s":3}
        ],"tier":"core","grp":"co_impulsivity_1","tags":["impulsivity","deliberation"]},
        {"qt":"behavioral_recall","text":"How consistent is your daily routine?","opts":[
            {"id":"a","text":"Very — I follow similar patterns every day and it helps me be productive","s":5},
            {"id":"b","text":"Somewhat — I have habits but I'm flexible","s":3},
            {"id":"c","text":"Low consistency — my days look very different from each other","s":1},
            {"id":"d","text":"I have routines for work but not for personal life","s":2}
        ],"tier":"triangulation","grp":"co_routine_1","tags":["routine","consistency"]},
        {"qt":"scenario","text":"You're working late to finish a presentation. It's already good but not perfect. You could make it great with another two hours. You:","opts":[
            {"id":"a","text":"Stay and make it great — your name is on it","s":5},
            {"id":"b","text":"Submit it — good is sufficient and sleep matters","s":2},
            {"id":"c","text":"Call it done — diminishing returns on extra effort","s":1},
            {"id":"d","text":"Identify the highest-impact improvements and do only those","s":4}
        ],"tier":"core","grp":"co_perfectionism_1","tags":["perfectionism","work_ethic"]},
        {"qt":"temporal","text":"How has your relationship with organization and planning evolved?","opts":[
            {"id":"a","text":"I've always been organized — it's how my mind naturally works","s":5},
            {"id":"b","text":"I've developed organizational skills out of necessity","s":3},
            {"id":"c","text":"I've accepted that I'm not naturally organized and work around it","s":1},
            {"id":"d","text":"I've found the minimum level of organization that keeps me functional","s":2}
        ],"tier":"consistency_check","grp":"co_organization_temporal_1","tags":["organization","temporal"]},
        {"qt":"forced_choice","text":"When you make a commitment, you:","opts":[
            {"id":"a","text":"Follow through reliably — breaking a commitment causes me genuine distress","s":5},
            {"id":"b","text":"Intend to follow through but sometimes life gets in the way","s":3},
            {"id":"c","text":"Keep commitments loosely — plans change and that's okay","s":1},
            {"id":"d","text":"Take commitments very seriously which makes me careful about what I commit to","s":5}
        ],"tier":"core","grp":"co_commitment_1","tags":["commitment","reliability"]},
        {"qt":"behavioral_recall","text":"How do you handle it when a task is tedious but necessary?","opts":[
            {"id":"a","text":"I do it with the same care as interesting tasks — it needs to be done right","s":5},
            {"id":"b","text":"I do it but with less enthusiasm","s":3},
            {"id":"c","text":"I delegate it or find a way to avoid it if possible","s":1},
            {"id":"d","text":"I break it into small pieces and reward myself for completing each one","s":3}
        ],"tier":"triangulation","grp":"co_tedium_1","tags":["tedium","diligence"]},
        {"qt":"somatic","text":"When you check something off your to-do list, you feel:","opts":[
            {"id":"a","text":"Genuine satisfaction — completion gives me a physical sense of accomplishment","s":5},
            {"id":"b","text":"Ready to move on — the next task awaits","s":3},
            {"id":"c","text":"Not much — I don't use to-do lists consistently","s":1},
            {"id":"d","text":"Relief, especially if it was overdue","s":3}
        ],"tier":"triangulation","grp":"co_completion_reward_1","tags":["somatic","task_completion"]},
        {"qt":"scenario","text":"Your team cuts corners to meet a deadline. The result is acceptable but below your personal standards. You:","opts":[
            {"id":"a","text":"Feel deeply uncomfortable and want to fix it even after it's shipped","s":5},
            {"id":"b","text":"Accept it — deadlines require trade-offs","s":2},
            {"id":"c","text":"Don't sweat it — done is done","s":1},
            {"id":"d","text":"Document what was compromised so it can be improved next time","s":4}
        ],"tier":"core","grp":"co_standards_vs_deadlines_1","tags":["standards","pragmatism"]},
        {"qt":"forced_choice","text":"Your morning routine is:","opts":[
            {"id":"a","text":"Highly structured — the same sequence every day, optimized for productivity","s":5},
            {"id":"b","text":"Generally consistent with some flexibility","s":3},
            {"id":"c","text":"Chaotic — every morning is different and I'm often rushing","s":1},
            {"id":"d","text":"I have a routine but I don't beat myself up if I deviate","s":3}
        ],"tier":"triangulation","grp":"co_morning_1","tags":["routine","structure"]},
        {"qt":"behavioral_recall","text":"When assigned a task with vague instructions, you:","opts":[
            {"id":"a","text":"Clarify every detail before starting — I need clear parameters","s":5},
            {"id":"b","text":"Start working and ask questions as they arise","s":3},
            {"id":"c","text":"Wing it and show them what I came up with","s":1},
            {"id":"d","text":"Create my own structure and standards, then validate with the requester","s":4}
        ],"tier":"core","grp":"co_ambiguity_1","tags":["ambiguity","structure_seeking"]},
    ],
    "openness": [
        {"qt":"scenario","text":"You discover a philosophy that directly contradicts your current worldview but has compelling arguments. You:","opts":[
            {"id":"a","text":"Spend weeks exploring it — intellectual challenge is thrilling","s":5},
            {"id":"b","text":"Read the main arguments and integrate what's useful","s":3},
            {"id":"c","text":"Dismiss it — your worldview is well-tested","s":1},
            {"id":"d","text":"Discuss it with others to test the ideas against different perspectives","s":4}
        ],"tier":"core","grp":"op_intellectual_curiosity_1","tags":["intellectual_curiosity","openness_to_ideas"]},
        {"qt":"behavioral_recall","text":"When you encounter art that's deliberately abstract or unconventional, you:","opts":[
            {"id":"a","text":"Feel deeply engaged — abstract art speaks to something beyond words","s":5},
            {"id":"b","text":"Appreciate the craft even if it doesn't move me emotionally","s":3},
            {"id":"c","text":"Feel nothing — if I can't understand it, it's not for me","s":1},
            {"id":"d","text":"Try to understand what the artist was attempting","s":4}
        ],"tier":"core","grp":"op_aesthetic_1","tags":["aesthetics","abstract_art"]},
        {"qt":"forced_choice","text":"Which describes your relationship with imagination?","opts":[
            {"id":"a","text":"My inner world of ideas and fantasies is richer than physical reality","s":5},
            {"id":"b","text":"I have a good imagination but I'm primarily practical","s":3},
            {"id":"c","text":"I'm grounded in reality — daydreaming feels unproductive","s":1},
            {"id":"d","text":"I use imagination strategically — for problem-solving and creativity","s":4}
        ],"tier":"core","grp":"op_imagination_1","tags":["imagination","creativity"]},
        {"qt":"somatic","text":"When you encounter a genuinely new idea that shifts your perspective, you feel:","opts":[
            {"id":"a","text":"Physical excitement — a buzz of energy, elevated mood, restless enthusiasm","s":5},
            {"id":"b","text":"Intellectual interest that motivates further exploration","s":3},
            {"id":"c","text":"Skepticism — most 'new' ideas are recycled","s":1},
            {"id":"d","text":"A calm deep satisfaction — like a puzzle piece clicking into place","s":4}
        ],"tier":"core","grp":"op_new_ideas_1","tags":["somatic","new_ideas"]},
        {"qt":"scenario","text":"You're offered a chance to spend three months in a country with a culture completely unlike your own. You:","opts":[
            {"id":"a","text":"Say yes immediately — immersion in difference is how you grow","s":5},
            {"id":"b","text":"Seriously consider it but weigh the practical challenges","s":3},
            {"id":"c","text":"Decline — three months away from your comfort zone is too long","s":1},
            {"id":"d","text":"Jump at it, but plan carefully to get the most from the experience","s":4}
        ],"tier":"core","grp":"op_experience_1","tags":["openness_to_experience","culture"]},
        {"qt":"temporal","text":"How has your curiosity changed over the years?","opts":[
            {"id":"a","text":"It's only grown — the more I learn, the more I want to know","s":5},
            {"id":"b","text":"It's stayed about the same — I've always been moderately curious","s":3},
            {"id":"c","text":"It's narrowed — I know what interests me and focus there","s":1},
            {"id":"d","text":"I've become more curious about some things and less about others","s":3}
        ],"tier":"core","grp":"op_curiosity_1","tags":["curiosity","temporal"]},
        {"qt":"forced_choice","text":"In conversations, you're most drawn to:","opts":[
            {"id":"a","text":"Abstract ideas — philosophy, hypotheticals, 'what if' scenarios","s":5},
            {"id":"b","text":"A mix of abstract and practical topics","s":3},
            {"id":"c","text":"Concrete, practical topics — things that directly affect daily life","s":1},
            {"id":"d","text":"Deep discussions about meaning, purpose, and values","s":4}
        ],"tier":"core","grp":"op_conversation_1","tags":["conversation_preference","abstraction"]},
        {"qt":"behavioral_recall","text":"How often do you challenge your own beliefs and assumptions?","opts":[
            {"id":"a","text":"Constantly — I actively seek out perspectives that challenge mine","s":5},
            {"id":"b","text":"Occasionally — when evidence contradicts what I believe","s":3},
            {"id":"c","text":"Rarely — my beliefs are well-formed and I trust them","s":1},
            {"id":"d","text":"Regularly — I consider it a discipline to question my own thinking","s":5}
        ],"tier":"core","grp":"op_self_challenge_1","tags":["self_challenge","critical_thinking"]},
        {"qt":"scenario","text":"A friend suggests trying an unusual cuisine from a culture you know nothing about. The menu is in a foreign language. You:","opts":[
            {"id":"a","text":"Love it — point at random items on the menu and see what arrives","s":5},
            {"id":"b","text":"Research the cuisine quickly and order something you think you'll like","s":3},
            {"id":"c","text":"Suggest going somewhere familiar instead","s":1},
            {"id":"d","text":"Ask the server to recommend their most authentic dish","s":4}
        ],"tier":"triangulation","grp":"op_novelty_1","tags":["novelty","openness_to_experience"]},
        {"qt":"somatic","text":"When you're deeply absorbed in creative or intellectual work, you feel:","opts":[
            {"id":"a","text":"Alive in a way that nothing else replicates — time disappears, the world drops away","s":5},
            {"id":"b","text":"Focused and productive","s":3},
            {"id":"c","text":"I don't often experience deep creative absorption","s":1},
            {"id":"d","text":"A deep satisfaction that lingers even after I stop","s":4}
        ],"tier":"core","grp":"op_flow_1","tags":["somatic","creative_absorption"]},
        {"qt":"forced_choice","text":"Which describes your approach to tradition?","opts":[
            {"id":"a","text":"Traditions should be questioned — many exist only because of inertia","s":5},
            {"id":"b","text":"I value traditions but am open to modifying them when they no longer serve","s":3},
            {"id":"c","text":"Traditions provide stability and meaning — I follow them faithfully","s":1},
            {"id":"d","text":"I create my own traditions rather than following inherited ones","s":4}
        ],"tier":"core","grp":"op_tradition_1","tags":["tradition","unconventionality"]},
        {"qt":"behavioral_recall","text":"How many genuinely different topics or skills have you explored in the last year?","opts":[
            {"id":"a","text":"Many — I'm always picking up new interests and going down rabbit holes","s":5},
            {"id":"b","text":"A few — I balance new explorations with ongoing commitments","s":3},
            {"id":"c","text":"One or two — I prefer to deepen existing skills rather than add new ones","s":1},
            {"id":"d","text":"Several, but they're all connected to a broader theme I'm exploring","s":4}
        ],"tier":"triangulation","grp":"op_breadth_1","tags":["breadth_of_interest","exploration"]},
        {"qt":"scenario","text":"You read an article proposing that a deeply held belief of yours might be wrong. The evidence is strong. You:","opts":[
            {"id":"a","text":"Feel excited — this is an opportunity to update your understanding","s":5},
            {"id":"b","text":"Read critically and integrate what's valid","s":3},
            {"id":"c","text":"Look for flaws in the argument to defend your existing belief","s":1},
            {"id":"d","text":"Sit with the discomfort and let the new perspective settle before deciding","s":4}
        ],"tier":"core","grp":"op_belief_change_1","tags":["belief_revision","intellectual_flexibility"]},
        {"qt":"somatic","text":"When you enter a museum or gallery, you feel:","opts":[
            {"id":"a","text":"Anticipation and openness — each piece is a world to enter","s":5},
            {"id":"b","text":"Appreciative but selective — some things move me, most don't","s":3},
            {"id":"c","text":"Bored unless there's something specific I'm interested in","s":1},
            {"id":"d","text":"Contemplative — art slows my mind down in a good way","s":4}
        ],"tier":"triangulation","grp":"op_art_1","tags":["somatic","art_appreciation"]},
        {"qt":"forced_choice","text":"When solving a problem, you prefer:","opts":[
            {"id":"a","text":"Novel, creative approaches — the unconventional solution often works best","s":5},
            {"id":"b","text":"A blend of proven methods and creative thinking","s":3},
            {"id":"c","text":"Tried-and-true methods — why reinvent the wheel?","s":1},
            {"id":"d","text":"Understanding the underlying principles so I can derive the right approach","s":4}
        ],"tier":"core","grp":"op_problem_solving_1","tags":["problem_solving","creativity"]},
        {"qt":"behavioral_recall","text":"How do you feel about ambiguity and uncertainty?","opts":[
            {"id":"a","text":"Comfortable — ambiguity means possibility and I can sit with not-knowing","s":5},
            {"id":"b","text":"Manageable — I prefer clarity but can tolerate ambiguity","s":3},
            {"id":"c","text":"Uncomfortable — I need clear answers and defined paths","s":1},
            {"id":"d","text":"I find it intellectually stimulating even when it's emotionally uncomfortable","s":4}
        ],"tier":"core","grp":"op_ambiguity_1","tags":["ambiguity_tolerance","uncertainty"]},
        {"qt":"temporal","text":"How has your taste in music, art, or entertainment evolved?","opts":[
            {"id":"a","text":"Constantly expanding — I seek out increasingly diverse and challenging material","s":5},
            {"id":"b","text":"Broadened somewhat but I return to favorites","s":3},
            {"id":"c","text":"Settled into clear preferences — I know what I like","s":1},
            {"id":"d","text":"Deepened in specific areas rather than broadened across many","s":3}
        ],"tier":"consistency_check","grp":"op_taste_1","tags":["taste_evolution","temporal"]},
        {"qt":"scenario","text":"You're given a creative project with no constraints — total freedom in approach, medium, and content. You feel:","opts":[
            {"id":"a","text":"Thrilled — unlimited possibility is the best starting point","s":5},
            {"id":"b","text":"Excited but slightly anxious — some constraints help me focus","s":3},
            {"id":"c","text":"Overwhelmed — I work better with clear guidelines","s":1},
            {"id":"d","text":"Energized to create my own constraints that align with my vision","s":4}
        ],"tier":"core","grp":"op_freedom_1","tags":["creative_freedom","constraints"]},
        {"qt":"forced_choice","text":"Which describes your inner life?","opts":[
            {"id":"a","text":"Rich and vivid — I have a constant stream of ideas, images, and associations","s":5},
            {"id":"b","text":"Active but organized — I think purposefully","s":3},
            {"id":"c","text":"Practical — my thoughts are mostly about what needs to be done","s":1},
            {"id":"d","text":"Deep — I think about a few things with great intensity","s":4}
        ],"tier":"core","grp":"op_inner_life_1","tags":["inner_life","imagination"]},
        {"qt":"behavioral_recall","text":"When someone holds a view that's completely opposite to yours, you:","opts":[
            {"id":"a","text":"Get genuinely curious about how they arrived at that view","s":5},
            {"id":"b","text":"Engage in respectful debate to test both positions","s":3},
            {"id":"c","text":"Conclude they're wrong and move on","s":1},
            {"id":"d","text":"Try to understand their perspective even if I ultimately disagree","s":4}
        ],"tier":"core","grp":"op_opposing_views_1","tags":["perspective_taking","intellectual_curiosity"]},
    ],
}

for dim, qs in hexaco_data.items():
    for q in qs:
        entry = {
            "uid": f"HEX-{uid:03d}",
            "assessment_id": "hexaco",
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

with open("/Users/user/personal/sb/trueassess/priv/question_bank/hexaco.json", "w") as f:
    json.dump(questions, f, indent=2)

print(f"Wrote {len(questions)} HEXACO questions")
