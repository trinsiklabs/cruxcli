import json

questions = []
uid = 1

dims = ["dominance", "influence", "steadiness", "conscientiousness"]

# 25 questions per dimension = 100 total
disc_questions = {
    "dominance": [
        {"qt":"scenario","text":"Your team is stuck on a decision that's been going back and forth for a week. You:","opts":[
            {"id":"a","text":"Take charge and make the call — someone has to","s":{"dominance":5}},
            {"id":"b","text":"Facilitate a discussion to build consensus","s":{"dominance":1,"influence":3}},
            {"id":"c","text":"Wait patiently — the right answer will emerge","s":{"dominance":1,"steadiness":3}},
            {"id":"d","text":"Analyze the options more thoroughly before deciding","s":{"dominance":1,"conscientiousness":3}}
        ],"tier":"core","grp":"d_decisiveness_1","tags":["decision_making","leadership"]},
        {"qt":"behavioral_recall","text":"When facing a challenge that others say is impossible, you typically:","opts":[
            {"id":"a","text":"Get energized — impossible challenges bring out your best","s":{"dominance":5}},
            {"id":"b","text":"Rally others to tackle it as a team","s":{"dominance":2,"influence":3}},
            {"id":"c","text":"Assess whether it's worth the risk before committing","s":{"dominance":2,"conscientiousness":3}},
            {"id":"d","text":"Prefer to work on achievable goals rather than moon shots","s":{"dominance":1,"steadiness":3}}
        ],"tier":"core","grp":"d_challenge_1","tags":["challenge","motivation"]},
        {"qt":"forced_choice","text":"In a negotiation, you tend to:","opts":[
            {"id":"a","text":"Push hard for what you want — you're comfortable with tension","s":{"dominance":5}},
            {"id":"b","text":"Find a win-win that keeps the relationship strong","s":{"dominance":1,"influence":4}},
            {"id":"c","text":"Concede on points that aren't critical to avoid conflict","s":{"dominance":1,"steadiness":3}},
            {"id":"d","text":"Come prepared with data that supports your position","s":{"dominance":2,"conscientiousness":4}}
        ],"tier":"core","grp":"d_negotiation_1","tags":["negotiation","conflict"]},
        {"qt":"scenario","text":"A subordinate questions your decision in front of the whole team. You:","opts":[
            {"id":"a","text":"Welcome the challenge — you respect people who push back","s":{"dominance":5}},
            {"id":"b","text":"Feel annoyed but address it calmly to maintain authority","s":{"dominance":4}},
            {"id":"c","text":"Feel uncomfortable and try to defuse the tension","s":{"dominance":1,"steadiness":3}},
            {"id":"d","text":"Ask them to provide data supporting their alternative","s":{"dominance":2,"conscientiousness":3}}
        ],"tier":"core","grp":"d_authority_1","tags":["authority","pushback"]},
        {"qt":"somatic","text":"When you're in competition — sports, business, games — what happens in your body?","opts":[
            {"id":"a","text":"Adrenaline surge — I become sharper, faster, more alive","s":{"dominance":5}},
            {"id":"b","text":"Excitement about the social aspect more than the winning","s":{"dominance":1,"influence":4}},
            {"id":"c","text":"Tension — I'd rather cooperate than compete","s":{"dominance":1,"steadiness":3}},
            {"id":"d","text":"Focus — I methodically work my strategy","s":{"dominance":2,"conscientiousness":3}}
        ],"tier":"core","grp":"d_competition_1","tags":["competition","somatic"]},
        {"qt":"temporal","text":"How has your approach to conflict changed over the years?","opts":[
            {"id":"a","text":"I've always been direct — conflict doesn't scare me","s":{"dominance":5}},
            {"id":"b","text":"I've learned to channel my directness more strategically","s":{"dominance":4}},
            {"id":"c","text":"I avoid it more now — I've seen the damage it can cause","s":{"dominance":1,"steadiness":3}},
            {"id":"d","text":"I address conflict when the facts clearly support my position","s":{"dominance":2,"conscientiousness":3}}
        ],"tier":"triangulation","grp":"d_conflict_1","tags":["conflict","temporal"]},
        {"qt":"forced_choice","text":"Which workplace environment energizes you most?","opts":[
            {"id":"a","text":"Fast-paced, high-stakes, results-driven","s":{"dominance":5}},
            {"id":"b","text":"Collaborative, social, team-oriented","s":{"dominance":1,"influence":4}},
            {"id":"c","text":"Stable, predictable, supportive","s":{"dominance":1,"steadiness":4}},
            {"id":"d","text":"Structured, quality-focused, detail-oriented","s":{"dominance":1,"conscientiousness":4}}
        ],"tier":"core","grp":"d_environment_1","tags":["work_environment","motivation"]},
        {"qt":"scenario","text":"You're given a project with an aggressive deadline and limited resources. You:","opts":[
            {"id":"a","text":"Thrive — constraints force creativity and decisive action","s":{"dominance":5}},
            {"id":"b","text":"Motivate the team and delegate effectively","s":{"dominance":3,"influence":3}},
            {"id":"c","text":"Feel stressed but work steadily toward the deadline","s":{"dominance":1,"steadiness":3}},
            {"id":"d","text":"Push back on the deadline if the quality will suffer","s":{"dominance":2,"conscientiousness":4}}
        ],"tier":"triangulation","grp":"d_pressure_1","tags":["pressure","deadlines"]},
        {"qt":"behavioral_recall","text":"When you receive feedback that you're 'too aggressive' or 'intimidating,' you:","opts":[
            {"id":"a","text":"Shrug — getting results requires intensity","s":{"dominance":5}},
            {"id":"b","text":"Adjust your approach to maintain relationships","s":{"dominance":2,"influence":3}},
            {"id":"c","text":"Feel genuinely bad — you never want to make others uncomfortable","s":{"dominance":1,"steadiness":3}},
            {"id":"d","text":"Consider whether the feedback is valid based on specific examples","s":{"dominance":2,"conscientiousness":3}}
        ],"tier":"core","grp":"d_feedback_1","tags":["feedback","self_awareness"]},
        {"qt":"scenario","text":"Two paths to a goal: one is risky but fast, the other is safe but slow. You:","opts":[
            {"id":"a","text":"Fast path — speed and boldness usually win","s":{"dominance":5}},
            {"id":"b","text":"Whichever path gets the team most excited","s":{"dominance":1,"influence":3}},
            {"id":"c","text":"Safe path — why risk what you already have?","s":{"dominance":1,"steadiness":4}},
            {"id":"d","text":"Analyze both paths thoroughly before committing","s":{"dominance":1,"conscientiousness":4}}
        ],"tier":"core","grp":"d_risk_1","tags":["risk_taking","decision_making"]},
        {"qt":"forced_choice","text":"Your natural response to obstacles is:","opts":[
            {"id":"a","text":"Push through them — obstacles are meant to be overcome","s":{"dominance":5}},
            {"id":"b","text":"Find creative workarounds with help from others","s":{"dominance":2,"influence":3}},
            {"id":"c","text":"Wait for the obstacle to resolve itself if possible","s":{"dominance":1,"steadiness":3}},
            {"id":"d","text":"Study the obstacle until you find the optimal solution","s":{"dominance":1,"conscientiousness":4}}
        ],"tier":"core","grp":"d_obstacles_1","tags":["obstacle_response","persistence"]},
        {"qt":"behavioral_recall","text":"In group settings, you naturally tend to:","opts":[
            {"id":"a","text":"Lead — you gravitate toward the front of the room","s":{"dominance":5}},
            {"id":"b","text":"Energize — you keep the mood positive and people engaged","s":{"dominance":1,"influence":5}},
            {"id":"c","text":"Support — you make sure everyone feels heard and included","s":{"dominance":1,"steadiness":4}},
            {"id":"d","text":"Observe — you analyze what's happening before contributing","s":{"dominance":1,"conscientiousness":3}}
        ],"tier":"core","grp":"d_group_role_1","tags":["group_dynamics","natural_role"]},
        {"qt":"scenario","text":"Your manager gives you a directive you disagree with. You:","opts":[
            {"id":"a","text":"Push back immediately — respect goes both ways","s":{"dominance":5}},
            {"id":"b","text":"Express your concern diplomatically and suggest alternatives","s":{"dominance":3,"influence":2}},
            {"id":"c","text":"Follow the directive to maintain harmony, even if you disagree","s":{"dominance":1,"steadiness":4}},
            {"id":"d","text":"Follow it if logically sound; question it with data if not","s":{"dominance":2,"conscientiousness":4}}
        ],"tier":"triangulation","grp":"d_authority_2","tags":["authority","disagreement"]},
        {"qt":"somatic","text":"When you accomplish a major goal, what's the dominant physical feeling?","opts":[
            {"id":"a","text":"Triumph — a surge of power and readiness for the next challenge","s":{"dominance":5}},
            {"id":"b","text":"Joy — you want to celebrate with everyone involved","s":{"dominance":1,"influence":4}},
            {"id":"c","text":"Relief and contentment — glad it's done","s":{"dominance":1,"steadiness":4}},
            {"id":"d","text":"Satisfaction — you executed the plan correctly","s":{"dominance":1,"conscientiousness":4}}
        ],"tier":"triangulation","grp":"d_achievement_1","tags":["achievement","somatic"]},
        {"qt":"forced_choice","text":"What motivates you most at work?","opts":[
            {"id":"a","text":"Results, impact, and winning","s":{"dominance":5}},
            {"id":"b","text":"Recognition, relationships, and influence","s":{"dominance":1,"influence":5}},
            {"id":"c","text":"Stability, teamwork, and helping others succeed","s":{"dominance":1,"steadiness":5}},
            {"id":"d","text":"Accuracy, expertise, and doing things right","s":{"dominance":1,"conscientiousness":5}}
        ],"tier":"core","grp":"d_motivation_1","tags":["motivation","values"]},
        {"qt":"scenario","text":"During a crisis, your instinct is to:","opts":[
            {"id":"a","text":"Take command — crises need decisive leaders, not committees","s":{"dominance":5}},
            {"id":"b","text":"Communicate clearly and keep people calm","s":{"dominance":2,"influence":4}},
            {"id":"c","text":"Stay steady and handle what's in front of you","s":{"dominance":1,"steadiness":4}},
            {"id":"d","text":"Gather information before taking any action","s":{"dominance":1,"conscientiousness":4}}
        ],"tier":"core","grp":"d_crisis_1","tags":["crisis","leadership"]},
        {"qt":"behavioral_recall","text":"How do you handle being told 'no'?","opts":[
            {"id":"a","text":"It's a starting point for negotiation, not a final answer","s":{"dominance":5}},
            {"id":"b","text":"I try to understand why and find a path to 'yes'","s":{"dominance":2,"influence":3}},
            {"id":"c","text":"I accept it gracefully even if I'm disappointed","s":{"dominance":1,"steadiness":4}},
            {"id":"d","text":"I accept it if the reasoning is sound; challenge it if not","s":{"dominance":3,"conscientiousness":3}}
        ],"tier":"triangulation","grp":"d_rejection_1","tags":["rejection","persistence"]},
        {"qt":"temporal","text":"How would you describe your career trajectory?","opts":[
            {"id":"a","text":"Aggressive upward — I seek positions of greater authority and impact","s":{"dominance":5}},
            {"id":"b","text":"People-focused — I've gravitated toward roles where I influence and inspire","s":{"dominance":1,"influence":4}},
            {"id":"c","text":"Steady growth — I value loyalty and long-term commitment to organizations","s":{"dominance":1,"steadiness":4}},
            {"id":"d","text":"Expertise-driven — I've deepened my knowledge in my field","s":{"dominance":1,"conscientiousness":4}}
        ],"tier":"core","grp":"d_career_1","tags":["career","temporal"]},
        {"qt":"scenario","text":"A colleague takes credit for your idea in a meeting. You:","opts":[
            {"id":"a","text":"Call it out right there — you won't let someone take what's yours","s":{"dominance":5}},
            {"id":"b","text":"Address it privately after the meeting with humor","s":{"dominance":2,"influence":3}},
            {"id":"c","text":"Let it go — it's not worth the confrontation","s":{"dominance":1,"steadiness":3}},
            {"id":"d","text":"Document the timeline of the idea for future reference","s":{"dominance":2,"conscientiousness":3}}
        ],"tier":"core","grp":"d_credit_1","tags":["credit","confrontation"]},
        {"qt":"forced_choice","text":"Your communication style is best described as:","opts":[
            {"id":"a","text":"Direct, bottom-line, no fluff","s":{"dominance":5}},
            {"id":"b","text":"Enthusiastic, persuasive, storytelling","s":{"dominance":1,"influence":5}},
            {"id":"c","text":"Warm, patient, good listener","s":{"dominance":1,"steadiness":5}},
            {"id":"d","text":"Precise, factual, thorough","s":{"dominance":1,"conscientiousness":5}}
        ],"tier":"core","grp":"d_communication_1","tags":["communication_style"]},
        {"qt":"behavioral_recall","text":"When making decisions, you rely most on:","opts":[
            {"id":"a","text":"Gut instinct and confidence — overthinking kills momentum","s":{"dominance":5}},
            {"id":"b","text":"Input from people you trust and respect","s":{"dominance":1,"influence":3}},
            {"id":"c","text":"What's been proven to work before","s":{"dominance":1,"steadiness":4}},
            {"id":"d","text":"Data, research, and careful analysis","s":{"dominance":1,"conscientiousness":5}}
        ],"tier":"triangulation","grp":"d_decision_style_1","tags":["decision_making","instinct"]},
        {"qt":"scenario","text":"You're asked to slow down and follow a detailed process that feels unnecessary. You:","opts":[
            {"id":"a","text":"Push to skip it — bureaucracy kills results","s":{"dominance":5}},
            {"id":"b","text":"Follow it but make it more fun and engaging for the team","s":{"dominance":1,"influence":3}},
            {"id":"c","text":"Follow it without complaint — processes exist for a reason","s":{"dominance":1,"steadiness":4}},
            {"id":"d","text":"Follow it meticulously — the process ensures quality","s":{"dominance":1,"conscientiousness":5}}
        ],"tier":"core","grp":"d_process_1","tags":["process","impatience"]},
        {"qt":"somatic","text":"When everything is running smoothly and there's nothing to fix or conquer, you feel:","opts":[
            {"id":"a","text":"Restless — I need a new challenge or I'll create one","s":{"dominance":5}},
            {"id":"b","text":"Happy — time to connect with people and enjoy the moment","s":{"dominance":1,"influence":4}},
            {"id":"c","text":"Content — this is the goal, enjoy it","s":{"dominance":1,"steadiness":5}},
            {"id":"d","text":"Watchful — smooth operations need monitoring to stay smooth","s":{"dominance":1,"conscientiousness":3}}
        ],"tier":"core","grp":"d_restlessness_1","tags":["restlessness","somatic"]},
        {"qt":"forced_choice","text":"Under stress, you tend to become:","opts":[
            {"id":"a","text":"More aggressive and controlling — I double down","s":{"dominance":5}},
            {"id":"b","text":"More disorganized and emotional — I lose focus","s":{"dominance":1,"influence":3}},
            {"id":"c","text":"More indecisive and passive — I freeze","s":{"dominance":1,"steadiness":2}},
            {"id":"d","text":"More critical and withdrawn — I overanalyze","s":{"dominance":1,"conscientiousness":3}}
        ],"tier":"core","grp":"d_stress_1","tags":["stress_response"]},
        {"qt":"behavioral_recall","text":"What's your relationship with patience?","opts":[
            {"id":"a","text":"Low — I want results now and waiting feels like losing","s":{"dominance":5}},
            {"id":"b","text":"Variable — patient with people, impatient with tasks","s":{"dominance":2,"influence":3}},
            {"id":"c","text":"High — good things take time and I'm comfortable waiting","s":{"dominance":1,"steadiness":5}},
            {"id":"d","text":"Depends — patient with complex problems, impatient with carelessness","s":{"dominance":2,"conscientiousness":3}}
        ],"tier":"triangulation","grp":"d_patience_1","tags":["patience","temperament"]},
    ],
    "influence": [
        {"qt":"scenario","text":"You arrive at a party where you know almost nobody. You:","opts":[
            {"id":"a","text":"Introduce yourself to everyone — this is exciting","s":{"influence":5}},
            {"id":"b","text":"Find the most important person in the room and introduce yourself","s":{"influence":2,"dominance":4}},
            {"id":"c","text":"Find someone who looks friendly and start a conversation","s":{"influence":3,"steadiness":2}},
            {"id":"d","text":"Observe the room before approaching anyone","s":{"influence":1,"conscientiousness":3}}
        ],"tier":"core","grp":"i_social_1","tags":["social_approach","networking"]},
        {"qt":"behavioral_recall","text":"When presenting an idea, you focus most on:","opts":[
            {"id":"a","text":"Enthusiasm and vision — getting people excited about the possibility","s":{"influence":5}},
            {"id":"b","text":"The bottom line — what it will achieve and why now","s":{"influence":1,"dominance":4}},
            {"id":"c","text":"How it benefits the team and maintains harmony","s":{"influence":2,"steadiness":3}},
            {"id":"d","text":"The evidence and logic supporting the idea","s":{"influence":1,"conscientiousness":4}}
        ],"tier":"core","grp":"i_persuasion_1","tags":["persuasion","presentation"]},
        {"qt":"forced_choice","text":"Your greatest fear in social situations is:","opts":[
            {"id":"a","text":"Being ignored or invisible","s":{"influence":5}},
            {"id":"b","text":"Losing control or looking weak","s":{"influence":1,"dominance":4}},
            {"id":"c","text":"Causing conflict or tension","s":{"influence":1,"steadiness":4}},
            {"id":"d","text":"Saying something factually incorrect","s":{"influence":1,"conscientiousness":4}}
        ],"tier":"core","grp":"i_fear_1","tags":["social_fear","rejection"]},
        {"qt":"scenario","text":"A friend is going through a tough time. Your instinct is to:","opts":[
            {"id":"a","text":"Cheer them up — positivity and fun are the best medicine","s":{"influence":5}},
            {"id":"b","text":"Give them practical advice to fix the situation","s":{"influence":1,"dominance":3}},
            {"id":"c","text":"Simply be present — listen and provide steady support","s":{"influence":1,"steadiness":5}},
            {"id":"d","text":"Help them think through the problem logically","s":{"influence":1,"conscientiousness":3}}
        ],"tier":"core","grp":"i_support_1","tags":["support_style","friendship"]},
        {"qt":"somatic","text":"When you're the center of attention — presenting, performing, storytelling — your body feels:","opts":[
            {"id":"a","text":"Alive and energized — this is my element","s":{"influence":5}},
            {"id":"b","text":"Powerful — I command the room","s":{"influence":2,"dominance":4}},
            {"id":"c","text":"Uncomfortable — I'd rather blend in","s":{"influence":1,"steadiness":3}},
            {"id":"d","text":"Focused on delivering accurate content, not on the attention itself","s":{"influence":1,"conscientiousness":3}}
        ],"tier":"core","grp":"i_attention_1","tags":["attention","somatic"]},
        {"qt":"temporal","text":"How has your need for social connection changed over the years?","opts":[
            {"id":"a","text":"I've always been a social butterfly — people are my energy source","s":{"influence":5}},
            {"id":"b","text":"I've learned to channel my social energy more strategically","s":{"influence":3,"dominance":2}},
            {"id":"c","text":"I've deepened fewer relationships rather than expanding my network","s":{"influence":2,"steadiness":3}},
            {"id":"d","text":"I've always preferred meaningful one-on-one conversations over socializing","s":{"influence":1,"conscientiousness":2}}
        ],"tier":"core","grp":"i_social_need_1","tags":["social_need","temporal"]},
        {"qt":"scenario","text":"You need to deliver bad news to your team. You:","opts":[
            {"id":"a","text":"Frame it positively — focus on the opportunity within the challenge","s":{"influence":5}},
            {"id":"b","text":"State it directly and pivot to the action plan","s":{"influence":1,"dominance":5}},
            {"id":"c","text":"Deliver it gently, acknowledging the impact on everyone","s":{"influence":2,"steadiness":4}},
            {"id":"d","text":"Present the facts and context so they understand why","s":{"influence":1,"conscientiousness":4}}
        ],"tier":"triangulation","grp":"i_bad_news_1","tags":["communication","bad_news"]},
        {"qt":"forced_choice","text":"In collaborative work, your biggest strength is:","opts":[
            {"id":"a","text":"Generating enthusiasm and keeping momentum","s":{"influence":5}},
            {"id":"b","text":"Driving toward results and accountability","s":{"influence":1,"dominance":4}},
            {"id":"c","text":"Maintaining harmony and ensuring everyone contributes","s":{"influence":1,"steadiness":4}},
            {"id":"d","text":"Ensuring quality and catching errors","s":{"influence":1,"conscientiousness":4}}
        ],"tier":"core","grp":"i_strength_1","tags":["collaboration","strengths"]},
        {"qt":"behavioral_recall","text":"When a conversation gets boring, you:","opts":[
            {"id":"a","text":"Redirect to something more exciting — you can't tolerate dull conversation","s":{"influence":5}},
            {"id":"b","text":"Cut it short and move on to something productive","s":{"influence":1,"dominance":4}},
            {"id":"c","text":"Stay engaged politely even if you're bored","s":{"influence":1,"steadiness":4}},
            {"id":"d","text":"Try to deepen it — surface-level bores you, not the topic itself","s":{"influence":1,"conscientiousness":3}}
        ],"tier":"triangulation","grp":"i_boredom_1","tags":["boredom","conversation"]},
        {"qt":"scenario","text":"You have an idea that's unconventional and risky. To get buy-in you:","opts":[
            {"id":"a","text":"Pitch it with passion and charisma — make them feel the vision","s":{"influence":5}},
            {"id":"b","text":"Present it as a fait accompli — just start doing it","s":{"influence":1,"dominance":4}},
            {"id":"c","text":"Run it by trusted allies first for a reality check","s":{"influence":2,"steadiness":3}},
            {"id":"d","text":"Build an airtight case with evidence and projections","s":{"influence":1,"conscientiousness":5}}
        ],"tier":"core","grp":"i_influence_1","tags":["influence_tactics","persuasion"]},
        {"qt":"somatic","text":"When you're excluded from a social event you expected to attend, you feel:","opts":[
            {"id":"a","text":"Stung — social exclusion is physically painful for you","s":{"influence":5}},
            {"id":"b","text":"Annoyed — their loss","s":{"influence":1,"dominance":3}},
            {"id":"c","text":"Disappointed but understanding — you can't attend everything","s":{"influence":2,"steadiness":3}},
            {"id":"d","text":"Unbothered — you'd rather spend the time productively","s":{"influence":1,"conscientiousness":2}}
        ],"tier":"core","grp":"i_exclusion_1","tags":["exclusion","somatic"]},
        {"qt":"forced_choice","text":"Which describes your relationship with details?","opts":[
            {"id":"a","text":"Big picture all the way — details bore me and I delegate them","s":{"influence":5}},
            {"id":"b","text":"I focus on the details that drive results","s":{"influence":1,"dominance":3}},
            {"id":"c","text":"I'm detail-oriented when it comes to people's needs","s":{"influence":2,"steadiness":3}},
            {"id":"d","text":"Details are where the truth lives — I thrive in them","s":{"influence":1,"conscientiousness":5}}
        ],"tier":"core","grp":"i_details_1","tags":["detail_orientation","big_picture"]},
        {"qt":"behavioral_recall","text":"After a social event, you typically feel:","opts":[
            {"id":"a","text":"Energized — being with people charges my batteries","s":{"influence":5}},
            {"id":"b","text":"Satisfied if I made valuable connections","s":{"influence":2,"dominance":3}},
            {"id":"c","text":"Drained but glad I went","s":{"influence":1,"steadiness":2}},
            {"id":"d","text":"Ready for quiet time to recharge","s":{"influence":1,"conscientiousness":2}}
        ],"tier":"triangulation","grp":"i_energy_1","tags":["social_energy","introversion_extraversion"]},
        {"qt":"scenario","text":"You make a mistake that affects the team. You:","opts":[
            {"id":"a","text":"Address it with humor and a positive spin — keep morale up","s":{"influence":5}},
            {"id":"b","text":"Own it quickly, fix it, and move on","s":{"influence":1,"dominance":4}},
            {"id":"c","text":"Apologize sincerely and make sure everyone feels okay","s":{"influence":2,"steadiness":4}},
            {"id":"d","text":"Analyze what went wrong to prevent recurrence","s":{"influence":1,"conscientiousness":5}}
        ],"tier":"core","grp":"i_mistake_1","tags":["accountability","mistakes"]},
        {"qt":"temporal","text":"When you look back at your relationships, what pattern do you see?","opts":[
            {"id":"a","text":"Wide network — I collect people and maintain many connections","s":{"influence":5}},
            {"id":"b","text":"Strategic network — I invest in relationships that advance my goals","s":{"influence":2,"dominance":3}},
            {"id":"c","text":"Deep loyalty — fewer friends but lifetime commitment to each","s":{"influence":1,"steadiness":5}},
            {"id":"d","text":"Selective — I respect competence and shared intellectual interests","s":{"influence":1,"conscientiousness":3}}
        ],"tier":"core","grp":"i_relationship_pattern_1","tags":["relationship_patterns","temporal"]},
        {"qt":"forced_choice","text":"When you disagree with someone, your approach is:","opts":[
            {"id":"a","text":"Charm them to your side — make them feel like it was their idea","s":{"influence":5}},
            {"id":"b","text":"State your position firmly and let them decide","s":{"influence":1,"dominance":5}},
            {"id":"c","text":"Avoid the disagreement if possible — it's usually not worth it","s":{"influence":1,"steadiness":4}},
            {"id":"d","text":"Present a logical argument with supporting evidence","s":{"influence":1,"conscientiousness":4}}
        ],"tier":"core","grp":"i_disagreement_1","tags":["disagreement","persuasion_style"]},
        {"qt":"behavioral_recall","text":"How do you typically process difficult emotions?","opts":[
            {"id":"a","text":"Talk about them with friends — processing is social for me","s":{"influence":5}},
            {"id":"b","text":"Channel them into action — doing something productive","s":{"influence":1,"dominance":3}},
            {"id":"c","text":"Give myself time and space — I process slowly and privately","s":{"influence":1,"steadiness":4}},
            {"id":"d","text":"Journal, analyze, or think through them systematically","s":{"influence":1,"conscientiousness":3}}
        ],"tier":"triangulation","grp":"i_processing_1","tags":["emotional_processing","social"]},
        {"qt":"scenario","text":"You're organizing a team project. Your focus is on:","opts":[
            {"id":"a","text":"Making it exciting — themes, celebrations, creative approaches","s":{"influence":5}},
            {"id":"b","text":"Clear goals, accountability, and deadlines","s":{"influence":1,"dominance":5}},
            {"id":"c","text":"Making sure everyone has a role they're comfortable with","s":{"influence":1,"steadiness":4}},
            {"id":"d","text":"Creating a detailed project plan with milestones","s":{"influence":1,"conscientiousness":5}}
        ],"tier":"core","grp":"i_organizing_1","tags":["project_management","style"]},
        {"qt":"somatic","text":"When you haven't had social interaction for more than a day, you feel:","opts":[
            {"id":"a","text":"Antsy and energy-deprived — I need people to feel alive","s":{"influence":5}},
            {"id":"b","text":"Fine — I have plenty to do on my own","s":{"influence":1,"dominance":2}},
            {"id":"c","text":"Content — alone time is restorative","s":{"influence":1,"steadiness":3}},
            {"id":"d","text":"Productive — no interruptions means focused work","s":{"influence":1,"conscientiousness":4}}
        ],"tier":"core","grp":"i_isolation_1","tags":["social_need","somatic"]},
        {"qt":"forced_choice","text":"Under stress, you tend to become:","opts":[
            {"id":"a","text":"More scattered, talkative, and emotionally reactive","s":{"influence":5}},
            {"id":"b","text":"More aggressive, controlling, and impatient","s":{"influence":1,"dominance":5}},
            {"id":"c","text":"More withdrawn, passive, and conflict-avoidant","s":{"influence":1,"steadiness":3}},
            {"id":"d","text":"More critical, perfectionist, and isolated","s":{"influence":1,"conscientiousness":4}}
        ],"tier":"core","grp":"i_stress_response_1","tags":["stress_behavior"]},
        {"qt":"behavioral_recall","text":"What's the biggest compliment someone could give you?","opts":[
            {"id":"a","text":"'You make everyone feel welcome and energized'","s":{"influence":5}},
            {"id":"b","text":"'You get things done no matter what'","s":{"influence":1,"dominance":5}},
            {"id":"c","text":"'You're always there when I need you'","s":{"influence":1,"steadiness":5}},
            {"id":"d","text":"'Your work is impeccable'","s":{"influence":1,"conscientiousness":5}}
        ],"tier":"trap","grp":"i_compliment_1","tags":["values","identity"]},
        {"qt":"scenario","text":"You're working on a tedious but important task. After 20 minutes, you:","opts":[
            {"id":"a","text":"Find someone to do it with — everything is better social","s":{"influence":5}},
            {"id":"b","text":"Power through it — done is better than fun","s":{"influence":1,"dominance":3}},
            {"id":"c","text":"Continue patiently — it has to get done","s":{"influence":1,"steadiness":5}},
            {"id":"d","text":"Stay focused — the precision matters","s":{"influence":1,"conscientiousness":4}}
        ],"tier":"triangulation","grp":"i_tedium_1","tags":["tedium","focus"]},
        {"qt":"temporal","text":"How has your communication style evolved?","opts":[
            {"id":"a","text":"I've always been expressive and verbal — talking IS thinking for me","s":{"influence":5}},
            {"id":"b","text":"I've become more concise and strategic with my words","s":{"influence":2,"dominance":3}},
            {"id":"c","text":"I've become a better listener over the years","s":{"influence":2,"steadiness":3}},
            {"id":"d","text":"I've always been precise and measured in how I communicate","s":{"influence":1,"conscientiousness":4}}
        ],"tier":"consistency_check","grp":"i_comm_evolution_1","tags":["communication","temporal"]},
        {"qt":"forced_choice","text":"Your approach to planning a vacation is:","opts":[
            {"id":"a","text":"Spontaneous and social — who's coming? Let's figure it out as we go!","s":{"influence":5}},
            {"id":"b","text":"Adventure-focused — challenging activities, new experiences","s":{"influence":2,"dominance":3}},
            {"id":"c","text":"Relaxation-focused — familiar comforts, no surprises","s":{"influence":1,"steadiness":5}},
            {"id":"d","text":"Thoroughly researched — optimized itinerary, best restaurants","s":{"influence":1,"conscientiousness":5}}
        ],"tier":"triangulation","grp":"i_vacation_1","tags":["vacation_style","spontaneity"]},
    ],
    "steadiness": [
        {"qt":"scenario","text":"Your company announces a major reorganization. New team, new manager, new responsibilities. You:","opts":[
            {"id":"a","text":"Feel anxious — you had a good rhythm and now it's disrupted","s":{"steadiness":5}},
            {"id":"b","text":"See opportunity — change means new possibilities","s":{"steadiness":1,"dominance":3}},
            {"id":"c","text":"Focus on the social aspect — who will your new teammates be?","s":{"steadiness":2,"influence":3}},
            {"id":"d","text":"Evaluate the change logically — is this an improvement?","s":{"steadiness":2,"conscientiousness":3}}
        ],"tier":"core","grp":"s_change_1","tags":["change_resistance","stability"]},
        {"qt":"behavioral_recall","text":"How do you handle it when multiple people need you at the same time?","opts":[
            {"id":"a","text":"Calmly work through each request in order — everyone gets their turn","s":{"steadiness":5}},
            {"id":"b","text":"Prioritize by impact and handle the most important first","s":{"steadiness":1,"dominance":4}},
            {"id":"c","text":"Try to be everywhere at once — you hate letting anyone down","s":{"steadiness":3,"influence":3}},
            {"id":"d","text":"Create a system to manage the requests efficiently","s":{"steadiness":2,"conscientiousness":4}}
        ],"tier":"core","grp":"s_multitask_1","tags":["patience","reliability"]},
        {"qt":"forced_choice","text":"Which best describes your pace of work?","opts":[
            {"id":"a","text":"Slow and steady — I'm consistent and reliable, day in and day out","s":{"steadiness":5}},
            {"id":"b","text":"Fast and intense — I sprint through work with high energy","s":{"steadiness":1,"dominance":4}},
            {"id":"c","text":"Variable — my pace depends on who I'm working with","s":{"steadiness":2,"influence":3}},
            {"id":"d","text":"Methodical — I work at whatever pace ensures accuracy","s":{"steadiness":2,"conscientiousness":4}}
        ],"tier":"core","grp":"s_pace_1","tags":["work_pace","consistency"]},
        {"qt":"scenario","text":"A coworker is visibly upset after receiving harsh feedback. You:","opts":[
            {"id":"a","text":"Go to them quietly and offer support — no one should sit with that alone","s":{"steadiness":5}},
            {"id":"b","text":"Tell them to use the feedback to get better — toughen up","s":{"steadiness":1,"dominance":3}},
            {"id":"c","text":"Organize the team to show solidarity and boost morale","s":{"steadiness":2,"influence":4}},
            {"id":"d","text":"Help them objectively evaluate what in the feedback was valid","s":{"steadiness":1,"conscientiousness":3}}
        ],"tier":"core","grp":"s_empathy_1","tags":["empathy","support"]},
        {"qt":"somatic","text":"When your daily routine gets disrupted unexpectedly, what do you feel?","opts":[
            {"id":"a","text":"Unsettled — my body craves the predictability of routine","s":{"steadiness":5}},
            {"id":"b","text":"Energized — disruption is stimulating","s":{"steadiness":1,"dominance":3}},
            {"id":"c","text":"Adaptable — I roll with whatever comes","s":{"steadiness":2,"influence":2}},
            {"id":"d","text":"Irritated if the disruption was avoidable","s":{"steadiness":2,"conscientiousness":3}}
        ],"tier":"core","grp":"s_routine_1","tags":["routine","somatic"]},
        {"qt":"temporal","text":"How has your need for stability changed over the years?","opts":[
            {"id":"a","text":"I've always valued stability — it's the foundation everything else is built on","s":{"steadiness":5}},
            {"id":"b","text":"I used to need more stability but I've become more comfortable with change","s":{"steadiness":3}},
            {"id":"c","text":"I've always preferred excitement and variety over stability","s":{"steadiness":1,"influence":3}},
            {"id":"d","text":"Stability matters for some things, but I also need intellectual challenge","s":{"steadiness":2,"conscientiousness":3}}
        ],"tier":"core","grp":"s_stability_need_1","tags":["stability","temporal"]},
        {"qt":"forced_choice","text":"In team conflicts, you naturally:","opts":[
            {"id":"a","text":"Mediate — helping both sides find common ground","s":{"steadiness":5}},
            {"id":"b","text":"Take a side and argue for it","s":{"steadiness":1,"dominance":4}},
            {"id":"c","text":"Use humor to defuse the tension","s":{"steadiness":2,"influence":3}},
            {"id":"d","text":"Present the facts and let logic resolve it","s":{"steadiness":1,"conscientiousness":4}}
        ],"tier":"core","grp":"s_mediation_1","tags":["mediation","conflict"]},
        {"qt":"scenario","text":"You've been in your role for three years and a recruiter offers an exciting opportunity elsewhere. You:","opts":[
            {"id":"a","text":"Feel torn — leaving feels disloyal even if the new role is better","s":{"steadiness":5}},
            {"id":"b","text":"Jump at it if it offers more authority or impact","s":{"steadiness":1,"dominance":4}},
            {"id":"c","text":"Get excited about the new people and possibilities","s":{"steadiness":1,"influence":4}},
            {"id":"d","text":"Compare the two roles systematically across multiple criteria","s":{"steadiness":2,"conscientiousness":4}}
        ],"tier":"core","grp":"s_loyalty_1","tags":["loyalty","change"]},
        {"qt":"behavioral_recall","text":"How do you show love and care for the important people in your life?","opts":[
            {"id":"a","text":"Consistent, reliable presence — I show up, day after day, no matter what","s":{"steadiness":5}},
            {"id":"b","text":"Taking charge of problems and fixing things for them","s":{"steadiness":1,"dominance":3}},
            {"id":"c","text":"Words of affirmation, quality time, and shared experiences","s":{"steadiness":2,"influence":4}},
            {"id":"d","text":"Thoughtful gestures that show I've paid attention to their needs","s":{"steadiness":3,"conscientiousness":3}}
        ],"tier":"triangulation","grp":"s_caregiving_1","tags":["love","caregiving"]},
        {"qt":"somatic","text":"When you witness injustice or unfairness, your body's first response is:","opts":[
            {"id":"a","text":"Discomfort — but I tend to process it internally rather than act immediately","s":{"steadiness":5}},
            {"id":"b","text":"Rage — I'm ready to act","s":{"steadiness":1,"dominance":5}},
            {"id":"c","text":"Empathy for the person affected — I feel their pain","s":{"steadiness":3,"influence":2}},
            {"id":"d","text":"Assessment — I need to understand the full situation before responding","s":{"steadiness":2,"conscientiousness":3}}
        ],"tier":"triangulation","grp":"s_injustice_1","tags":["injustice","somatic"]},
        {"qt":"scenario","text":"Your team is moving much faster than you're comfortable with on a project. You:","opts":[
            {"id":"a","text":"Voice concern gently — rushing leads to mistakes","s":{"steadiness":5}},
            {"id":"b","text":"Keep up — speed is competitive advantage","s":{"steadiness":1,"dominance":3}},
            {"id":"c","text":"Match the energy — teamwork means going at the group's pace","s":{"steadiness":2,"influence":3}},
            {"id":"d","text":"Insist on quality checkpoints even if it slows things down","s":{"steadiness":3,"conscientiousness":5}}
        ],"tier":"core","grp":"s_pace_comfort_1","tags":["pace","quality"]},
        {"qt":"forced_choice","text":"Which describes your reaction to being asked to multitask?","opts":[
            {"id":"a","text":"Stressful — I do my best work focusing on one thing at a time","s":{"steadiness":5}},
            {"id":"b","text":"Energizing — I like having multiple balls in the air","s":{"steadiness":1,"dominance":3}},
            {"id":"c","text":"Fun if it involves working with different people","s":{"steadiness":1,"influence":3}},
            {"id":"d","text":"Uncomfortable — multitasking compromises quality","s":{"steadiness":3,"conscientiousness":4}}
        ],"tier":"core","grp":"s_multitask_2","tags":["multitasking","focus"]},
        {"qt":"behavioral_recall","text":"When a close friend or family member makes a decision you disagree with, you:","opts":[
            {"id":"a","text":"Support them anyway — relationships matter more than being right","s":{"steadiness":5}},
            {"id":"b","text":"Tell them directly what you think, even if they don't want to hear it","s":{"steadiness":1,"dominance":4}},
            {"id":"c","text":"Express concern gently but ultimately respect their autonomy","s":{"steadiness":4,"influence":1}},
            {"id":"d","text":"Present the logical case for why their decision is problematic","s":{"steadiness":1,"conscientiousness":4}}
        ],"tier":"core","grp":"s_support_1","tags":["support","disagreement"]},
        {"qt":"scenario","text":"You've developed an efficient system for handling your work. A new manager wants to change it. You:","opts":[
            {"id":"a","text":"Feel resistant — your system works and change introduces unnecessary risk","s":{"steadiness":5}},
            {"id":"b","text":"Adapt quickly — if the boss wants it, make it happen","s":{"steadiness":1,"dominance":2}},
            {"id":"c","text":"Approach the change with curiosity — maybe it's better","s":{"steadiness":1,"influence":2}},
            {"id":"d","text":"Evaluate the new system against the old one on measurable criteria","s":{"steadiness":2,"conscientiousness":5}}
        ],"tier":"core","grp":"s_change_resistance_1","tags":["change_resistance","systems"]},
        {"qt":"somatic","text":"When everything in your life is stable — same routine, same people, same environment — your body feels:","opts":[
            {"id":"a","text":"Deeply comfortable — stability is where I thrive","s":{"steadiness":5}},
            {"id":"b","text":"Restless — I need something to shake things up","s":{"steadiness":1,"dominance":3}},
            {"id":"c","text":"Content but socially hungry — I need my routines AND my people","s":{"steadiness":3,"influence":3}},
            {"id":"d","text":"Focused and productive — consistency enables my best work","s":{"steadiness":3,"conscientiousness":3}}
        ],"tier":"core","grp":"s_comfort_1","tags":["somatic","stability"]},
        {"qt":"forced_choice","text":"What's most difficult for you?","opts":[
            {"id":"a","text":"Saying no to someone who needs my help","s":{"steadiness":5}},
            {"id":"b","text":"Accepting that I can't control the outcome","s":{"steadiness":1,"dominance":5}},
            {"id":"c","text":"Being alone with nothing social planned","s":{"steadiness":1,"influence":4}},
            {"id":"d","text":"Submitting work that isn't perfect","s":{"steadiness":1,"conscientiousness":5}}
        ],"tier":"core","grp":"s_difficulty_1","tags":["difficulty","self_awareness"]},
        {"qt":"behavioral_recall","text":"How do you handle it when someone breaks a promise to you?","opts":[
            {"id":"a","text":"I'm deeply hurt but may not say anything to avoid conflict","s":{"steadiness":5}},
            {"id":"b","text":"I confront them directly — accountability matters","s":{"steadiness":1,"dominance":5}},
            {"id":"c","text":"I express my disappointment and give them a chance to explain","s":{"steadiness":3,"influence":2}},
            {"id":"d","text":"I note it and adjust my expectations for the future","s":{"steadiness":2,"conscientiousness":3}}
        ],"tier":"core","grp":"s_promises_1","tags":["promises","hurt"]},
        {"qt":"scenario","text":"You're at a team brainstorm. Ideas are flying. You:","opts":[
            {"id":"a","text":"Listen, synthesize, and offer grounded perspective when the energy settles","s":{"steadiness":5}},
            {"id":"b","text":"Drive the direction — too many ideas without focus is waste","s":{"steadiness":1,"dominance":4}},
            {"id":"c","text":"Contribute enthusiastically — creative energy is contagious","s":{"steadiness":1,"influence":5}},
            {"id":"d","text":"Evaluate each idea against criteria before supporting any","s":{"steadiness":1,"conscientiousness":4}}
        ],"tier":"triangulation","grp":"s_brainstorm_1","tags":["brainstorming","contribution"]},
        {"qt":"temporal","text":"What role have you played most consistently in your friendships?","opts":[
            {"id":"a","text":"The rock — the one everyone leans on, the steady presence","s":{"steadiness":5}},
            {"id":"b","text":"The leader — the one who decides what the group does","s":{"steadiness":1,"dominance":4}},
            {"id":"c","text":"The connector — the one who brings the group together","s":{"steadiness":1,"influence":5}},
            {"id":"d","text":"The advisor — the one people come to for thoughtful guidance","s":{"steadiness":2,"conscientiousness":3}}
        ],"tier":"core","grp":"s_friendship_role_1","tags":["friendship","role"]},
        {"qt":"forced_choice","text":"Under stress, you tend to become:","opts":[
            {"id":"a","text":"Withdrawn, passive, and stuck — I can't decide or act","s":{"steadiness":5}},
            {"id":"b","text":"Aggressive, controlling, and demanding","s":{"steadiness":1,"dominance":5}},
            {"id":"c","text":"Scattered, emotional, and seeking reassurance","s":{"steadiness":1,"influence":4}},
            {"id":"d","text":"Critical, perfectionist, and harsh on myself","s":{"steadiness":1,"conscientiousness":4}}
        ],"tier":"core","grp":"s_stress_1","tags":["stress_response"]},
        {"qt":"behavioral_recall","text":"Your approach to learning new skills is:","opts":[
            {"id":"a","text":"Gradual and thorough — I master each step before moving on","s":{"steadiness":5}},
            {"id":"b","text":"Jump in and figure it out — trial and error","s":{"steadiness":1,"dominance":3}},
            {"id":"c","text":"Best in a group — I learn well from and with others","s":{"steadiness":2,"influence":3}},
            {"id":"d","text":"Systematic — I study the theory before practicing","s":{"steadiness":2,"conscientiousness":5}}
        ],"tier":"triangulation","grp":"s_learning_1","tags":["learning_style"]},
        {"qt":"scenario","text":"Someone you manage is consistently underperforming. You:","opts":[
            {"id":"a","text":"Give them more time and support — maybe they're going through something","s":{"steadiness":5}},
            {"id":"b","text":"Set clear expectations with consequences if they don't improve","s":{"steadiness":1,"dominance":5}},
            {"id":"c","text":"Talk to them to understand what's going on and motivate them","s":{"steadiness":2,"influence":3}},
            {"id":"d","text":"Document the performance issues carefully before taking action","s":{"steadiness":2,"conscientiousness":4}}
        ],"tier":"core","grp":"s_management_1","tags":["management","patience"]},
        {"qt":"somatic","text":"When you finally express frustration after holding it in for too long, it feels:","opts":[
            {"id":"a","text":"Overwhelming — it comes out bigger than I expected and I regret it","s":{"steadiness":5}},
            {"id":"b","text":"Satisfying — finally saying what needed to be said","s":{"steadiness":1,"dominance":4}},
            {"id":"c","text":"Scary — I worry I've damaged the relationship","s":{"steadiness":4,"influence":1}},
            {"id":"d","text":"Measured — even when frustrated, I express it logically","s":{"steadiness":1,"conscientiousness":3}}
        ],"tier":"core","grp":"s_frustration_1","tags":["somatic","suppressed_frustration"]},
        {"qt":"forced_choice","text":"What would you miss most if it disappeared from your life?","opts":[
            {"id":"a","text":"My daily routines and the comfort they bring","s":{"steadiness":5}},
            {"id":"b","text":"The feeling of winning and achieving goals","s":{"steadiness":1,"dominance":4}},
            {"id":"c","text":"My social connections and the energy of being with people","s":{"steadiness":1,"influence":5}},
            {"id":"d","text":"The satisfaction of solving complex problems","s":{"steadiness":1,"conscientiousness":4}}
        ],"tier":"consistency_check","grp":"s_values_1","tags":["values","what_matters"]},
    ],
    "conscientiousness": [
        {"qt":"scenario","text":"You've finished a report and it's due in one hour. You've reviewed it twice. You:","opts":[
            {"id":"a","text":"Review it a third time — there might be an error you missed","s":{"conscientiousness":5}},
            {"id":"b","text":"Submit it — good enough is good enough, move to the next thing","s":{"conscientiousness":1,"dominance":3}},
            {"id":"c","text":"Ask a colleague to review it — fresh eyes catch things","s":{"conscientiousness":3,"influence":2}},
            {"id":"d","text":"Submit it confidently — you trust your process","s":{"conscientiousness":3,"steadiness":2}}
        ],"tier":"core","grp":"c_perfectionism_1","tags":["perfectionism","quality"]},
        {"qt":"behavioral_recall","text":"When someone presents you with data or a claim, your instinct is to:","opts":[
            {"id":"a","text":"Verify it — check the source, look for methodology, find the caveats","s":{"conscientiousness":5}},
            {"id":"b","text":"Accept it if it aligns with your experience","s":{"conscientiousness":1,"dominance":2}},
            {"id":"c","text":"Accept it if the person is trustworthy","s":{"conscientiousness":1,"influence":2}},
            {"id":"d","text":"Take it at face value unless something feels off","s":{"conscientiousness":1,"steadiness":3}}
        ],"tier":"core","grp":"c_verification_1","tags":["verification","critical_thinking"]},
        {"qt":"forced_choice","text":"Which describes your ideal work environment?","opts":[
            {"id":"a","text":"Clear standards, defined processes, and emphasis on getting it right","s":{"conscientiousness":5}},
            {"id":"b","text":"Results-focused — I don't care about process as long as we win","s":{"conscientiousness":1,"dominance":5}},
            {"id":"c","text":"Creative, flexible, and collaborative","s":{"conscientiousness":1,"influence":4}},
            {"id":"d","text":"Calm, supportive, and predictable","s":{"conscientiousness":2,"steadiness":4}}
        ],"tier":"core","grp":"c_environment_1","tags":["work_environment","standards"]},
        {"qt":"scenario","text":"A colleague submits work with several errors that you have to fix. You:","opts":[
            {"id":"a","text":"Fix the errors but also document them so the colleague can learn","s":{"conscientiousness":5}},
            {"id":"b","text":"Fix them quickly and move on — no point dwelling on it","s":{"conscientiousness":2,"dominance":3}},
            {"id":"c","text":"Fix them and have a gentle conversation about expectations","s":{"conscientiousness":3,"steadiness":3}},
            {"id":"d","text":"Fix them and tell the colleague directly that this isn't acceptable","s":{"conscientiousness":3,"dominance":3}}
        ],"tier":"core","grp":"c_standards_1","tags":["standards","quality_control"]},
        {"qt":"somatic","text":"When you submit work that you know isn't your best quality, you feel:","opts":[
            {"id":"a","text":"Physical discomfort — almost like handing in a test you didn't study for","s":{"conscientiousness":5}},
            {"id":"b","text":"Fine — done is better than perfect","s":{"conscientiousness":1,"dominance":3}},
            {"id":"c","text":"Okay as long as the team is happy with it","s":{"conscientiousness":1,"influence":2}},
            {"id":"d","text":"Slightly uneasy but able to let it go","s":{"conscientiousness":3,"steadiness":2}}
        ],"tier":"core","grp":"c_quality_1","tags":["somatic","quality_anxiety"]},
        {"qt":"temporal","text":"How has your attention to detail changed over the years?","opts":[
            {"id":"a","text":"I've always been meticulous — details matter to me inherently","s":{"conscientiousness":5}},
            {"id":"b","text":"I've learned to focus on details that matter and ignore the rest","s":{"conscientiousness":3,"dominance":2}},
            {"id":"c","text":"I've never been particularly detail-oriented","s":{"conscientiousness":1,"influence":2}},
            {"id":"d","text":"My detail orientation has increased as stakes have gotten higher","s":{"conscientiousness":4}}
        ],"tier":"core","grp":"c_detail_1","tags":["attention_to_detail","temporal"]},
        {"qt":"forced_choice","text":"When rules don't make sense to you, you:","opts":[
            {"id":"a","text":"Follow them anyway — rules exist for reasons you might not see","s":{"conscientiousness":5}},
            {"id":"b","text":"Break them if they're in the way of results","s":{"conscientiousness":1,"dominance":5}},
            {"id":"c","text":"Bend them creatively — the spirit matters more than the letter","s":{"conscientiousness":1,"influence":3}},
            {"id":"d","text":"Follow them but feel uncomfortable about it","s":{"conscientiousness":4,"steadiness":2}}
        ],"tier":"core","grp":"c_rules_1","tags":["rules","compliance"]},
        {"qt":"scenario","text":"You're writing an important email. A friend texts asking if you want to grab lunch. You:","opts":[
            {"id":"a","text":"Finish the email first — you can't leave tasks half-done","s":{"conscientiousness":5}},
            {"id":"b","text":"Send the email as-is and head to lunch — you can refine it later","s":{"conscientiousness":1,"dominance":2}},
            {"id":"c","text":"Reply to the friend and finish the email at lunch","s":{"conscientiousness":1,"influence":3}},
            {"id":"d","text":"Take a break — the email can wait 30 minutes","s":{"conscientiousness":2,"steadiness":3}}
        ],"tier":"triangulation","grp":"c_completion_1","tags":["completion","task_switching"]},
        {"qt":"behavioral_recall","text":"How organized is your physical workspace?","opts":[
            {"id":"a","text":"Meticulously organized — everything has a place and everything is in its place","s":{"conscientiousness":5}},
            {"id":"b","text":"Functional chaos — I know where everything is even if it looks messy","s":{"conscientiousness":1,"dominance":2}},
            {"id":"c","text":"It varies — sometimes organized, sometimes a disaster","s":{"conscientiousness":2,"influence":2}},
            {"id":"d","text":"Tidy enough — I keep things generally clean without being obsessive","s":{"conscientiousness":3,"steadiness":3}}
        ],"tier":"core","grp":"c_organization_1","tags":["organization","workspace"]},
        {"qt":"somatic","text":"When someone makes a factual error in a presentation, even if it's minor, you feel:","opts":[
            {"id":"a","text":"A physical flinch — errors are almost painful to witness","s":{"conscientiousness":5}},
            {"id":"b","text":"Nothing unless the error affects the outcome","s":{"conscientiousness":1,"dominance":3}},
            {"id":"c","text":"Empathy for the presenter — everyone makes mistakes","s":{"conscientiousness":1,"steadiness":3}},
            {"id":"d","text":"Mild discomfort that passes quickly","s":{"conscientiousness":3}}
        ],"tier":"core","grp":"c_errors_1","tags":["somatic","error_sensitivity"]},
        {"qt":"scenario","text":"You're asked to give your honest opinion on a project plan. You notice fifteen issues. You:","opts":[
            {"id":"a","text":"List all fifteen — thoroughness matters more than popularity","s":{"conscientiousness":5}},
            {"id":"b","text":"Highlight the top three deal-breakers and move on","s":{"conscientiousness":2,"dominance":4}},
            {"id":"c","text":"Mention a few positives first, then the key issues diplomatically","s":{"conscientiousness":2,"influence":3}},
            {"id":"d","text":"Focus on the biggest issues to avoid overwhelming the team","s":{"conscientiousness":3,"steadiness":2}}
        ],"tier":"core","grp":"c_thoroughness_1","tags":["thoroughness","feedback"]},
        {"qt":"forced_choice","text":"Your approach to deadlines is:","opts":[
            {"id":"a","text":"I finish well before the deadline — last-minute work isn't my best","s":{"conscientiousness":5}},
            {"id":"b","text":"I hit deadlines but don't stress about being early","s":{"conscientiousness":2,"dominance":2}},
            {"id":"c","text":"I sometimes cut it close because I got sidetracked","s":{"conscientiousness":1,"influence":2}},
            {"id":"d","text":"I finish on time, consistently, without drama","s":{"conscientiousness":3,"steadiness":4}}
        ],"tier":"core","grp":"c_deadlines_1","tags":["deadlines","time_management"]},
        {"qt":"behavioral_recall","text":"When learning something new, you prefer:","opts":[
            {"id":"a","text":"Structured courses with clear progression and assessments","s":{"conscientiousness":5}},
            {"id":"b","text":"Hands-on experience — learn by doing","s":{"conscientiousness":1,"dominance":3}},
            {"id":"c","text":"Group learning — discussion and collaboration","s":{"conscientiousness":1,"influence":4}},
            {"id":"d","text":"Self-paced learning at your own comfortable speed","s":{"conscientiousness":2,"steadiness":4}}
        ],"tier":"triangulation","grp":"c_learning_1","tags":["learning_style","structure"]},
        {"qt":"scenario","text":"You discover an error in a report that was published last week. Nobody has noticed. You:","opts":[
            {"id":"a","text":"Correct it immediately and issue an updated version","s":{"conscientiousness":5}},
            {"id":"b","text":"Fix it quietly — no need to draw attention to it","s":{"conscientiousness":3,"dominance":2}},
            {"id":"c","text":"Let it go — it's not a major error and publishing a correction would be awkward","s":{"conscientiousness":1,"influence":2}},
            {"id":"d","text":"Note it for next time but don't reissue — it would cause unnecessary disruption","s":{"conscientiousness":2,"steadiness":3}}
        ],"tier":"core","grp":"c_integrity_1","tags":["integrity","error_correction"]},
        {"qt":"somatic","text":"When you have a long, unstructured day with no deadlines or commitments, you feel:","opts":[
            {"id":"a","text":"Uneasy — I create structure even when none is required","s":{"conscientiousness":5}},
            {"id":"b","text":"Free — time to pursue whatever catches my attention","s":{"conscientiousness":1,"influence":3}},
            {"id":"c","text":"Relaxed — I can recharge without pressure","s":{"conscientiousness":1,"steadiness":4}},
            {"id":"d","text":"Productive — I use the time for deep, focused work","s":{"conscientiousness":4}}
        ],"tier":"core","grp":"c_structure_1","tags":["somatic","structure_need"]},
        {"qt":"forced_choice","text":"What's your biggest professional fear?","opts":[
            {"id":"a","text":"Producing work that contains errors or is below standard","s":{"conscientiousness":5}},
            {"id":"b","text":"Missing an opportunity because I moved too slowly","s":{"conscientiousness":1,"dominance":4}},
            {"id":"c","text":"Being disliked by my colleagues","s":{"conscientiousness":1,"influence":4}},
            {"id":"d","text":"Losing my job security or stable routine","s":{"conscientiousness":1,"steadiness":4}}
        ],"tier":"core","grp":"c_fear_1","tags":["fear","professional"]},
        {"qt":"behavioral_recall","text":"How do you prepare for important meetings or presentations?","opts":[
            {"id":"a","text":"Extensively — I prepare for every possible question and scenario","s":{"conscientiousness":5}},
            {"id":"b","text":"Minimally — I trust my ability to think on my feet","s":{"conscientiousness":1,"dominance":3}},
            {"id":"c","text":"Focus on the audience — how to engage and connect with them","s":{"conscientiousness":1,"influence":4}},
            {"id":"d","text":"Enough to feel confident but not so much that I over-prepare","s":{"conscientiousness":3,"steadiness":2}}
        ],"tier":"triangulation","grp":"c_preparation_1","tags":["preparation","thoroughness"]},
        {"qt":"scenario","text":"Two approaches to a problem: one is fast and approximately right, the other is slow and precisely right. You:","opts":[
            {"id":"a","text":"Slow and precise — accuracy is non-negotiable","s":{"conscientiousness":5}},
            {"id":"b","text":"Fast and approximate — iterate based on feedback","s":{"conscientiousness":1,"dominance":4}},
            {"id":"c","text":"Depends on who it affects — precision matters more for some audiences","s":{"conscientiousness":2,"influence":2}},
            {"id":"d","text":"Fast first, then refine — get something out and improve it","s":{"conscientiousness":2,"steadiness":1}}
        ],"tier":"core","grp":"c_precision_1","tags":["precision","speed_accuracy"]},
        {"qt":"temporal","text":"How has your relationship with mistakes changed?","opts":[
            {"id":"a","text":"I've always taken them seriously — mistakes represent a failure of process","s":{"conscientiousness":5}},
            {"id":"b","text":"I view them as learning opportunities and move on quickly","s":{"conscientiousness":1,"dominance":3}},
            {"id":"c","text":"I used to be more perfectionist but I've learned to be gentler with myself","s":{"conscientiousness":3}},
            {"id":"d","text":"Mistakes are just part of life — I don't overweight them","s":{"conscientiousness":1,"steadiness":3}}
        ],"tier":"consistency_check","grp":"c_mistakes_1","tags":["mistakes","temporal"]},
        {"qt":"forced_choice","text":"Under stress, you tend to become:","opts":[
            {"id":"a","text":"More perfectionist and critical — of myself and others","s":{"conscientiousness":5}},
            {"id":"b","text":"More aggressive and impatient","s":{"conscientiousness":1,"dominance":5}},
            {"id":"c","text":"More disorganized and scattered","s":{"conscientiousness":1,"influence":3}},
            {"id":"d","text":"More withdrawn and passive","s":{"conscientiousness":1,"steadiness":3}}
        ],"tier":"core","grp":"c_stress_1","tags":["stress_response"]},
        {"qt":"behavioral_recall","text":"How do you feel about 'good enough'?","opts":[
            {"id":"a","text":"It's a phrase I have to force myself to accept — my instinct is always 'better'","s":{"conscientiousness":5}},
            {"id":"b","text":"It's a pragmatic reality — perfect is the enemy of done","s":{"conscientiousness":1,"dominance":3}},
            {"id":"c","text":"Depends on the context — some things need to be perfect, some don't","s":{"conscientiousness":3}},
            {"id":"d","text":"Good enough is genuinely fine for most things","s":{"conscientiousness":1,"steadiness":3}}
        ],"tier":"core","grp":"c_good_enough_1","tags":["perfectionism","pragmatism"]},
        {"qt":"scenario","text":"You notice your team is about to implement a solution that works but isn't optimal. The deadline is tight. You:","opts":[
            {"id":"a","text":"Flag the suboptimal approach and propose the correct one, even if it means missing the deadline","s":{"conscientiousness":5}},
            {"id":"b","text":"Ship it — optimize later if needed","s":{"conscientiousness":1,"dominance":4}},
            {"id":"c","text":"Go with the team's energy — they're motivated and it works","s":{"conscientiousness":1,"influence":2}},
            {"id":"d","text":"Implement it but document the technical debt for future improvement","s":{"conscientiousness":4,"steadiness":2}}
        ],"tier":"core","grp":"c_optimization_1","tags":["optimization","pragmatism"]},
        {"qt":"somatic","text":"When you complete a project that meets every requirement and exceeds expectations, you feel:","opts":[
            {"id":"a","text":"Deep satisfaction — this is what I live for","s":{"conscientiousness":5}},
            {"id":"b","text":"Ready for the next challenge — achievement feels like a starting line","s":{"conscientiousness":1,"dominance":4}},
            {"id":"c","text":"Proud and want to celebrate with the team","s":{"conscientiousness":1,"influence":3}},
            {"id":"d","text":"Relieved and peaceful — glad it's done well","s":{"conscientiousness":3,"steadiness":3}}
        ],"tier":"triangulation","grp":"c_completion_satisfaction_1","tags":["somatic","satisfaction"]},
        {"qt":"forced_choice","text":"Your personal filing system (digital or physical) is:","opts":[
            {"id":"a","text":"Highly organized with consistent naming conventions and folder structure","s":{"conscientiousness":5}},
            {"id":"b","text":"Functional but not pretty — I find what I need when I need it","s":{"conscientiousness":2,"dominance":2}},
            {"id":"c","text":"Honestly a mess — I rely on search and memory","s":{"conscientiousness":1,"influence":2}},
            {"id":"d","text":"Neat and tidy but simple — not overthought","s":{"conscientiousness":3,"steadiness":3}}
        ],"tier":"triangulation","grp":"c_filing_1","tags":["organization","systems"]},
    ],
}

for dim, qs in disc_questions.items():
    for q in qs:
        entry = {
            "uid": f"DISC-{uid:03d}",
            "assessment_id": "disc_style",
            "dimension": dim,
            "question_type": q["qt"],
            "text": q["text"],
            "options": [{"id":o["id"],"text":o["text"],"scores":o["s"]} for o in q["opts"]],
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

with open("/Users/user/personal/sb/trueassess/priv/question_bank/disc_style.json", "w") as f:
    json.dump(questions, f, indent=2)

print(f"Wrote {len(questions)} DISC questions")
