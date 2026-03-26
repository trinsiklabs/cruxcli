import json

questions = []
uid = 1

# Keirsey: 25 questions per dimension = 100
keirsey_data = {
    "guardian": [
        {"qt":"scenario","text":"Your community faces a budget crisis. The committee asks for volunteers to help organize and manage resources. You:","opts":[
            {"id":"a","text":"Step up immediately — organizing and stewarding resources is second nature to you","s":{"guardian":5}},
            {"id":"b","text":"Offer to help with the creative problem-solving aspect","s":{"guardian":1,"artisan":3}},
            {"id":"c","text":"Volunteer to advocate for the most vulnerable members","s":{"guardian":2,"idealist":3}},
            {"id":"d","text":"Analyze the budget data to find optimal solutions before committing","s":{"guardian":1,"rational":4}}
        ],"tier":"core","grp":"gu_responsibility_1","tags":["responsibility","stewardship"]},
        {"qt":"behavioral_recall","text":"In your daily life, how important are routines and traditions?","opts":[
            {"id":"a","text":"Essential — they provide structure, meaning, and stability to my life","s":{"guardian":5}},
            {"id":"b","text":"Boring — I prefer spontaneity and flexibility","s":{"guardian":1,"artisan":4}},
            {"id":"c","text":"Meaningful when they connect people and express values","s":{"guardian":2,"idealist":3}},
            {"id":"d","text":"Useful when efficient, but I'll modify them if a better system exists","s":{"guardian":2,"rational":3}}
        ],"tier":"core","grp":"gu_tradition_1","tags":["tradition","routine"]},
        {"qt":"forced_choice","text":"Which describes your core motivation at work?","opts":[
            {"id":"a","text":"Being dependable, maintaining standards, and ensuring things run smoothly","s":{"guardian":5}},
            {"id":"b","text":"Making an impact right now through skillful action","s":{"guardian":1,"artisan":4}},
            {"id":"c","text":"Helping people grow and finding deeper meaning in the work","s":{"guardian":1,"idealist":4}},
            {"id":"d","text":"Solving complex problems and building better systems","s":{"guardian":1,"rational":4}}
        ],"tier":"core","grp":"gu_motivation_1","tags":["motivation","dependability"]},
        {"qt":"somatic","text":"When established rules or norms are being violated around you, you feel:","opts":[
            {"id":"a","text":"Physically uncomfortable — disorder and norm-violation create real tension in my body","s":{"guardian":5}},
            {"id":"b","text":"Excited — rules are made to be broken when they don't work","s":{"guardian":1,"artisan":3}},
            {"id":"c","text":"Concerned about how the violation affects the people involved","s":{"guardian":2,"idealist":3}},
            {"id":"d","text":"Analytical — which norms are being violated and why?","s":{"guardian":1,"rational":3}}
        ],"tier":"core","grp":"gu_norms_1","tags":["somatic","norms","order"]},
        {"qt":"scenario","text":"A new employee joins your team and seems lost. You:","opts":[
            {"id":"a","text":"Take them under your wing — proper onboarding and mentoring ensure they succeed","s":{"guardian":5}},
            {"id":"b","text":"Show them the ropes through hands-on experience","s":{"guardian":2,"artisan":3}},
            {"id":"c","text":"Connect with them personally and make them feel welcome and valued","s":{"guardian":2,"idealist":4}},
            {"id":"d","text":"Point them to the resources and documentation they need to get up to speed","s":{"guardian":2,"rational":3}}
        ],"tier":"core","grp":"gu_mentoring_1","tags":["mentoring","onboarding"]},
        {"qt":"temporal","text":"How has your relationship with duty and obligation changed over the years?","opts":[
            {"id":"a","text":"Duty has always been a core value — I fulfill my obligations because it's right","s":{"guardian":5}},
            {"id":"b","text":"I've learned to balance duty with personal freedom and spontaneity","s":{"guardian":2,"artisan":2}},
            {"id":"c","text":"I feel duty most strongly toward people I care about, not institutions","s":{"guardian":2,"idealist":3}},
            {"id":"d","text":"I fulfill obligations that are logically justified, not ones based on tradition alone","s":{"guardian":1,"rational":4}}
        ],"tier":"core","grp":"gu_duty_1","tags":["duty","obligation","temporal"]},
        {"qt":"forced_choice","text":"Which social role feels most natural to you?","opts":[
            {"id":"a","text":"The protector and provider — ensuring security and stability for those who depend on me","s":{"guardian":5}},
            {"id":"b","text":"The performer and problem-solver — handling whatever comes up in the moment","s":{"guardian":1,"artisan":4}},
            {"id":"c","text":"The counselor and advocate — helping people become their best selves","s":{"guardian":1,"idealist":4}},
            {"id":"d","text":"The strategist and architect — designing systems and solving complex problems","s":{"guardian":1,"rational":4}}
        ],"tier":"core","grp":"gu_role_1","tags":["social_role","identity"]},
        {"qt":"scenario","text":"Your organization is considering a radical change to its operating model. You:","opts":[
            {"id":"a","text":"Advocate caution — what works shouldn't be thrown away for unproven ideas","s":{"guardian":5}},
            {"id":"b","text":"Get excited — anything beats the boring status quo","s":{"guardian":1,"artisan":4}},
            {"id":"c","text":"Evaluate how the change will affect people's wellbeing and morale","s":{"guardian":2,"idealist":3}},
            {"id":"d","text":"Analyze the proposal rigorously — is it actually better, or just different?","s":{"guardian":2,"rational":4}}
        ],"tier":"core","grp":"gu_change_1","tags":["change_response","conservatism"]},
        {"qt":"behavioral_recall","text":"How do you feel about saving, planning ahead, and preparing for the future?","opts":[
            {"id":"a","text":"It's fundamental — responsible people prepare for what's ahead","s":{"guardian":5}},
            {"id":"b","text":"I live in the moment — the future takes care of itself","s":{"guardian":1,"artisan":4}},
            {"id":"c","text":"I plan for the future but prioritize present-moment meaning and connection","s":{"guardian":2,"idealist":3}},
            {"id":"d","text":"I plan strategically for likely scenarios rather than anxiously for everything","s":{"guardian":2,"rational":4}}
        ],"tier":"core","grp":"gu_preparation_1","tags":["preparation","future_orientation"]},
        {"qt":"somatic","text":"When you've completed all your responsibilities for the day — everything is done, everyone is cared for — you feel:","opts":[
            {"id":"a","text":"Deep satisfaction — this is the reward for doing things right","s":{"guardian":5}},
            {"id":"b","text":"Antsy — now what? I need stimulation","s":{"guardian":1,"artisan":3}},
            {"id":"c","text":"Peaceful — but also wondering if there's someone I forgot to check on","s":{"guardian":3,"idealist":2}},
            {"id":"d","text":"Accomplished — now I can pursue intellectual interests","s":{"guardian":1,"rational":3}}
        ],"tier":"core","grp":"gu_completion_1","tags":["somatic","duty_fulfilled"]},
        {"qt":"forced_choice","text":"When making decisions, you most value:","opts":[
            {"id":"a","text":"What's proven to work — experience and precedent are the best guides","s":{"guardian":5}},
            {"id":"b","text":"What feels right in the moment — trust your instincts","s":{"guardian":1,"artisan":4}},
            {"id":"c","text":"What aligns with your values and benefits the people involved","s":{"guardian":2,"idealist":3}},
            {"id":"d","text":"What's logically optimal — follow the best reasoning","s":{"guardian":1,"rational":4}}
        ],"tier":"core","grp":"gu_decision_1","tags":["decision_making","experience"]},
        {"qt":"scenario","text":"A younger family member is making choices you disagree with. You:","opts":[
            {"id":"a","text":"Share your concerns clearly — experience has taught you lessons they need to hear","s":{"guardian":5}},
            {"id":"b","text":"Let them learn from their own mistakes — that's how you grow","s":{"guardian":1,"artisan":3}},
            {"id":"c","text":"Gently explore their feelings and values behind the choices","s":{"guardian":1,"idealist":4}},
            {"id":"d","text":"Present a logical case for why their choices might be suboptimal","s":{"guardian":1,"rational":4}}
        ],"tier":"triangulation","grp":"gu_guidance_1","tags":["guidance","family"]},
        {"qt":"behavioral_recall","text":"How important is it to you that people 'do the right thing'?","opts":[
            {"id":"a","text":"Extremely — moral and social obligations are the foundation of a functioning society","s":{"guardian":5}},
            {"id":"b","text":"Context matters — 'right' isn't always clear-cut and people should have freedom","s":{"guardian":1,"artisan":2}},
            {"id":"c","text":"Very important, but compassion should temper judgment about what's 'right'","s":{"guardian":2,"idealist":4}},
            {"id":"d","text":"Important, but 'right' should be determined by logic and evidence, not convention","s":{"guardian":1,"rational":4}}
        ],"tier":"core","grp":"gu_morality_1","tags":["morality","social_norms"]},
        {"qt":"temporal","text":"What gives you the deepest sense of belonging?","opts":[
            {"id":"a","text":"Being part of established institutions — family, community, organizations with history","s":{"guardian":5}},
            {"id":"b","text":"Being part of an action-oriented group that tackles challenges together","s":{"guardian":1,"artisan":3}},
            {"id":"c","text":"Deep personal connections with people who share your values","s":{"guardian":1,"idealist":5}},
            {"id":"d","text":"Being among competent people working on interesting problems","s":{"guardian":1,"rational":4}}
        ],"tier":"core","grp":"gu_belonging_1","tags":["belonging","institutional_identity"]},
        {"qt":"forced_choice","text":"Your approach to leadership is:","opts":[
            {"id":"a","text":"Steady, reliable, and focused on maintaining standards and protecting what works","s":{"guardian":5}},
            {"id":"b","text":"Adaptive, action-oriented, and focused on seizing opportunities","s":{"guardian":1,"artisan":4}},
            {"id":"c","text":"Inspiring, empathetic, and focused on people's growth and potential","s":{"guardian":1,"idealist":4}},
            {"id":"d","text":"Strategic, analytical, and focused on efficiency and innovation","s":{"guardian":1,"rational":4}}
        ],"tier":"core","grp":"gu_leadership_1","tags":["leadership_style"]},
        {"qt":"scenario","text":"A crisis hits your family/team. Everyone is panicking. You:","opts":[
            {"id":"a","text":"Become the rock — establish order, assign tasks, ensure everyone is safe","s":{"guardian":5}},
            {"id":"b","text":"Leap into action — handle the most urgent problem first","s":{"guardian":2,"artisan":4}},
            {"id":"c","text":"Focus on calming people down emotionally before addressing the practical crisis","s":{"guardian":1,"idealist":4}},
            {"id":"d","text":"Analyze the situation rapidly and deploy the most logical response","s":{"guardian":1,"rational":4}}
        ],"tier":"core","grp":"gu_crisis_1","tags":["crisis_response","stability"]},
        {"qt":"behavioral_recall","text":"How do you feel about waste — wasted money, time, food, or resources?","opts":[
            {"id":"a","text":"It bothers me deeply — waste is irresponsible and shows poor stewardship","s":{"guardian":5}},
            {"id":"b","text":"I don't think about it much — life's too short to optimize everything","s":{"guardian":1,"artisan":3}},
            {"id":"c","text":"I care about waste that harms people or the environment","s":{"guardian":2,"idealist":2}},
            {"id":"d","text":"Waste of intellectual potential bothers me more than material waste","s":{"guardian":1,"rational":3}}
        ],"tier":"triangulation","grp":"gu_waste_1","tags":["waste","stewardship"]},
        {"qt":"somatic","text":"When your home is clean, organized, and everything is in order, you feel:","opts":[
            {"id":"a","text":"Deeply calm — external order creates internal peace","s":{"guardian":5}},
            {"id":"b","text":"Restless — too much order feels sterile","s":{"guardian":1,"artisan":3}},
            {"id":"c","text":"Content if it also feels warm and welcoming","s":{"guardian":2,"idealist":2}},
            {"id":"d","text":"Efficient — now I can focus on what matters","s":{"guardian":2,"rational":3}}
        ],"tier":"core","grp":"gu_order_1","tags":["somatic","order","environment"]},
        {"qt":"forced_choice","text":"What's your relationship with authority and hierarchy?","opts":[
            {"id":"a","text":"I respect legitimate authority and believe hierarchies create necessary order","s":{"guardian":5}},
            {"id":"b","text":"I chafe under authority and prefer flat, flexible structures","s":{"guardian":1,"artisan":4}},
            {"id":"c","text":"Authority is only legitimate when it serves the wellbeing of those under it","s":{"guardian":1,"idealist":4}},
            {"id":"d","text":"Authority should be based on competence, not position or seniority","s":{"guardian":1,"rational":5}}
        ],"tier":"core","grp":"gu_authority_1","tags":["authority","hierarchy"]},
        {"qt":"scenario","text":"You inherit your grandmother's recipe box filled with handwritten cards from generations of your family. You:","opts":[
            {"id":"a","text":"Treasure it — this is a tangible connection to your lineage and you'll preserve every card","s":{"guardian":5}},
            {"id":"b","text":"Appreciate the sentiment but you cook by feel anyway","s":{"guardian":1,"artisan":3}},
            {"id":"c","text":"Feel deep emotion — each card represents a person and their love","s":{"guardian":2,"idealist":4}},
            {"id":"d","text":"Interesting historically — you might digitize them for archival purposes","s":{"guardian":1,"rational":2}}
        ],"tier":"triangulation","grp":"gu_heritage_1","tags":["heritage","family_tradition"]},
        {"qt":"behavioral_recall","text":"How do you feel about your role as a provider or caretaker?","opts":[
            {"id":"a","text":"It's central to who I am — providing for and protecting others gives me purpose","s":{"guardian":5}},
            {"id":"b","text":"I care for people in my own way but I don't define myself by it","s":{"guardian":1,"artisan":2}},
            {"id":"c","text":"Caregiving is important but it should be mutual, not one-directional","s":{"guardian":2,"idealist":3}},
            {"id":"d","text":"I contribute through competence rather than caregiving per se","s":{"guardian":1,"rational":3}}
        ],"tier":"core","grp":"gu_provider_1","tags":["provider","caretaker"]},
        {"qt":"forced_choice","text":"Which concern is most fundamental to you?","opts":[
            {"id":"a","text":"Security — for myself, my family, and my community","s":{"guardian":5}},
            {"id":"b","text":"Freedom — to act, explore, and experience life fully","s":{"guardian":1,"artisan":5}},
            {"id":"c","text":"Meaning — to find purpose and help others find theirs","s":{"guardian":1,"idealist":5}},
            {"id":"d","text":"Knowledge — to understand how things work and use that understanding","s":{"guardian":1,"rational":5}}
        ],"tier":"core","grp":"gu_core_concern_1","tags":["core_concern","security"]},
        {"qt":"scenario","text":"Society is debating whether to change a longstanding tradition that some find outdated. You:","opts":[
            {"id":"a","text":"Advocate for preserving it — traditions carry wisdom even when it's not immediately obvious","s":{"guardian":5}},
            {"id":"b","text":"Shrug — traditions are just habits, change them if they don't work","s":{"guardian":1,"artisan":3}},
            {"id":"c","text":"Evaluate it based on whether it harms or helps people, not on its age","s":{"guardian":1,"idealist":4}},
            {"id":"d","text":"Analyze whether the tradition serves a functional purpose before deciding","s":{"guardian":2,"rational":4}}
        ],"tier":"core","grp":"gu_tradition_debate_1","tags":["tradition","social_debate"]},
        {"qt":"temporal","text":"What kind of legacy do you want to leave?","opts":[
            {"id":"a","text":"That I was reliable, responsible, and built something lasting for those who come after","s":{"guardian":5}},
            {"id":"b","text":"That I lived fully, seized every moment, and had incredible experiences","s":{"guardian":1,"artisan":4}},
            {"id":"c","text":"That I made a positive difference in people's lives and inspired growth","s":{"guardian":1,"idealist":5}},
            {"id":"d","text":"That I contributed knowledge, solved important problems, or built elegant systems","s":{"guardian":1,"rational":4}}
        ],"tier":"core","grp":"gu_legacy_1","tags":["legacy","temporal"]},
        {"qt":"behavioral_recall","text":"When someone asks you for help with a practical task (moving, taxes, repairs), you:","opts":[
            {"id":"a","text":"Show up prepared with tools and a plan — concrete help is how I show love","s":{"guardian":5}},
            {"id":"b","text":"Help with what you can, improvising as you go","s":{"guardian":2,"artisan":3}},
            {"id":"c","text":"Help willingly but you're more comfortable with emotional than practical support","s":{"guardian":1,"idealist":3}},
            {"id":"d","text":"Help by optimizing their approach — you may redesign their filing system while you're at it","s":{"guardian":2,"rational":3}}
        ],"tier":"triangulation","grp":"gu_practical_help_1","tags":["practical_help","service"]},
    ],
    "artisan": [
        {"qt":"scenario","text":"An unexpected free day opens up with no obligations. You:","opts":[
            {"id":"a","text":"Feel a thrill of possibility — you'll follow whatever catches your attention","s":{"artisan":5}},
            {"id":"b","text":"Use it productively — there are always tasks to catch up on","s":{"artisan":1,"guardian":4}},
            {"id":"c","text":"Spend it connecting deeply with someone important to you","s":{"artisan":1,"idealist":4}},
            {"id":"d","text":"Dive into a project or intellectual pursuit you've been wanting to explore","s":{"artisan":1,"rational":3}}
        ],"tier":"core","grp":"ar_spontaneity_1","tags":["spontaneity","freedom"]},
        {"qt":"behavioral_recall","text":"How do you learn best?","opts":[
            {"id":"a","text":"By doing — hands-on experience teaches me more than any book or lecture","s":{"artisan":5}},
            {"id":"b","text":"Through structured instruction with clear steps and expectations","s":{"artisan":1,"guardian":4}},
            {"id":"c","text":"Through discussion and understanding how concepts relate to people's experiences","s":{"artisan":1,"idealist":3}},
            {"id":"d","text":"Through theory and principles — understanding 'why' before 'how'","s":{"artisan":1,"rational":4}}
        ],"tier":"core","grp":"ar_learning_1","tags":["learning_style","experiential"]},
        {"qt":"forced_choice","text":"Which describes your relationship with rules?","opts":[
            {"id":"a","text":"Rules are suggestions — I follow the ones that make sense in the moment","s":{"artisan":5}},
            {"id":"b","text":"Rules create order — I follow them because they serve the community","s":{"artisan":1,"guardian":5}},
            {"id":"c","text":"Rules matter when they protect people — otherwise they should be flexible","s":{"artisan":1,"idealist":3}},
            {"id":"d","text":"Rules should be logical — I follow rational rules and question arbitrary ones","s":{"artisan":1,"rational":4}}
        ],"tier":"core","grp":"ar_rules_1","tags":["rules","flexibility"]},
        {"qt":"somatic","text":"When you're doing something physical that requires skill — sports, crafts, cooking — you feel:","opts":[
            {"id":"a","text":"Completely alive — my body and mind merge in the action","s":{"artisan":5}},
            {"id":"b","text":"Satisfied when I do it correctly and the result meets standards","s":{"artisan":1,"guardian":3}},
            {"id":"c","text":"Connected to the experience and the people sharing it","s":{"artisan":2,"idealist":3}},
            {"id":"d","text":"Interested in the technique and the principles behind the skill","s":{"artisan":1,"rational":3}}
        ],"tier":"core","grp":"ar_physical_1","tags":["somatic","physical_engagement"]},
        {"qt":"scenario","text":"Plans change at the last minute — your carefully planned evening is now completely open. You:","opts":[
            {"id":"a","text":"Love it — last-minute changes mean new possibilities","s":{"artisan":5}},
            {"id":"b","text":"Feel annoyed — you had a plan and now it's disrupted","s":{"artisan":1,"guardian":4}},
            {"id":"c","text":"Feel fine as long as the people you were seeing are okay","s":{"artisan":1,"idealist":3}},
            {"id":"d","text":"Re-plan — optimize the newly available time","s":{"artisan":1,"rational":3}}
        ],"tier":"core","grp":"ar_adaptability_1","tags":["adaptability","change"]},
        {"qt":"temporal","text":"How has your appetite for excitement and novelty changed?","opts":[
            {"id":"a","text":"I've always been a thrill-seeker — variety and excitement are essential","s":{"artisan":5}},
            {"id":"b","text":"I used to be more adventurous but I've come to value stability","s":{"artisan":2,"guardian":3}},
            {"id":"c","text":"I've always preferred meaningful experiences over exciting ones","s":{"artisan":1,"idealist":3}},
            {"id":"d","text":"I seek intellectual excitement more than physical or social novelty","s":{"artisan":1,"rational":3}}
        ],"tier":"core","grp":"ar_excitement_1","tags":["temporal","novelty_seeking"]},
        {"qt":"forced_choice","text":"In a work context, you're most energized by:","opts":[
            {"id":"a","text":"Variety, urgency, and hands-on problem-solving","s":{"artisan":5}},
            {"id":"b","text":"Clear processes, predictability, and maintaining quality","s":{"artisan":1,"guardian":4}},
            {"id":"c","text":"Meaningful work that helps people and aligns with your values","s":{"artisan":1,"idealist":4}},
            {"id":"d","text":"Complex challenges that require creative strategic thinking","s":{"artisan":1,"rational":4}}
        ],"tier":"core","grp":"ar_work_energy_1","tags":["work_motivation","variety"]},
        {"qt":"scenario","text":"You're at a social gathering that's becoming dull. You:","opts":[
            {"id":"a","text":"Stir things up — suggest a game, tell a provocative story, or propose an adventure","s":{"artisan":5}},
            {"id":"b","text":"Stay and make polite conversation — you committed to being here","s":{"artisan":1,"guardian":3}},
            {"id":"c","text":"Find someone to have a deep, meaningful conversation with","s":{"artisan":1,"idealist":4}},
            {"id":"d","text":"Find the most intellectually interesting person and engage them","s":{"artisan":1,"rational":3}}
        ],"tier":"core","grp":"ar_boredom_social_1","tags":["boredom","social_energy"]},
        {"qt":"behavioral_recall","text":"How do you approach risk?","opts":[
            {"id":"a","text":"Embrace it — risk is what makes life interesting and I trust my ability to handle whatever comes","s":{"artisan":5}},
            {"id":"b","text":"Minimize it — responsible people don't take unnecessary risks","s":{"artisan":1,"guardian":5}},
            {"id":"c","text":"Evaluate it based on impact on relationships and people I care about","s":{"artisan":1,"idealist":3}},
            {"id":"d","text":"Calculate it — risk is acceptable when the expected value is positive","s":{"artisan":1,"rational":4}}
        ],"tier":"core","grp":"ar_risk_1","tags":["risk_appetite","boldness"]},
        {"qt":"somatic","text":"When you're confined — stuck in a meeting, waiting in line, trapped by routine — you feel:","opts":[
            {"id":"a","text":"Physically restless — my body needs movement, action, and freedom","s":{"artisan":5}},
            {"id":"b","text":"Patient — waiting is part of life","s":{"artisan":1,"guardian":4}},
            {"id":"c","text":"Fine if I'm with someone I can connect with","s":{"artisan":1,"idealist":3}},
            {"id":"d","text":"I retreat into my mind — I can think anywhere","s":{"artisan":1,"rational":4}}
        ],"tier":"core","grp":"ar_confinement_1","tags":["somatic","restlessness"]},
        {"qt":"forced_choice","text":"How do you make decisions in the moment?","opts":[
            {"id":"a","text":"Instinctively — I read the situation and act before I consciously analyze","s":{"artisan":5}},
            {"id":"b","text":"Based on what I know works — experience is the best guide","s":{"artisan":1,"guardian":4}},
            {"id":"c","text":"Based on how the decision will affect the people involved","s":{"artisan":1,"idealist":3}},
            {"id":"d","text":"I rarely decide without analysis — even in the moment, I run quick calculations","s":{"artisan":1,"rational":4}}
        ],"tier":"core","grp":"ar_instinct_1","tags":["instinct","snap_decisions"]},
        {"qt":"scenario","text":"You're offered two vacations: a carefully planned cultural tour or an open-ended road trip with no itinerary. You choose:","opts":[
            {"id":"a","text":"Road trip — the whole point is discovering what you find along the way","s":{"artisan":5}},
            {"id":"b","text":"Cultural tour — the planning ensures you see everything important","s":{"artisan":1,"guardian":4}},
            {"id":"c","text":"Whichever option involves the people most important to you","s":{"artisan":1,"idealist":3}},
            {"id":"d","text":"Cultural tour — but self-planned with optimized logistics","s":{"artisan":1,"rational":3}}
        ],"tier":"triangulation","grp":"ar_vacation_1","tags":["vacation","spontaneity"]},
        {"qt":"behavioral_recall","text":"How do you feel about long-term planning?","opts":[
            {"id":"a","text":"Resistant — plans beyond next week feel like cages","s":{"artisan":5}},
            {"id":"b","text":"Essential — planning ahead is responsible and wise","s":{"artisan":1,"guardian":5}},
            {"id":"c","text":"I plan around my values and relationships, not around tasks","s":{"artisan":1,"idealist":3}},
            {"id":"d","text":"I love strategic planning — building models of the future is engaging","s":{"artisan":1,"rational":4}}
        ],"tier":"core","grp":"ar_planning_1","tags":["planning_resistance","present_focus"]},
        {"qt":"somatic","text":"When you successfully improvise your way through a challenging situation, you feel:","opts":[
            {"id":"a","text":"Exhilarated — nothing beats the rush of pulling something off in the moment","s":{"artisan":5}},
            {"id":"b","text":"Relieved — but you'd have preferred to be prepared","s":{"artisan":1,"guardian":3}},
            {"id":"c","text":"Grateful — especially if it helped someone in need","s":{"artisan":1,"idealist":3}},
            {"id":"d","text":"Satisfied — but also thinking about how to systematize the solution","s":{"artisan":1,"rational":3}}
        ],"tier":"core","grp":"ar_improvisation_1","tags":["somatic","improvisation"]},
        {"qt":"forced_choice","text":"Your communication style is most like:","opts":[
            {"id":"a","text":"Quick, concrete, and action-oriented — get to the point and do something","s":{"artisan":5}},
            {"id":"b","text":"Thorough, sequential, and detailed — context matters","s":{"artisan":1,"guardian":4}},
            {"id":"c","text":"Warm, expressive, and focused on connection","s":{"artisan":1,"idealist":4}},
            {"id":"d","text":"Precise, conceptual, and focused on accuracy","s":{"artisan":1,"rational":4}}
        ],"tier":"core","grp":"ar_communication_1","tags":["communication_style"]},
        {"qt":"scenario","text":"You're given a tool (software, instrument, machine) with a thick instruction manual. You:","opts":[
            {"id":"a","text":"Start playing with it — you learn by experimenting, not reading","s":{"artisan":5}},
            {"id":"b","text":"Read the manual first — it was written for a reason","s":{"artisan":1,"guardian":4}},
            {"id":"c","text":"Ask someone who's used it before to show you","s":{"artisan":2,"idealist":2}},
            {"id":"d","text":"Skim the manual for key concepts then experiment systematically","s":{"artisan":1,"rational":4}}
        ],"tier":"triangulation","grp":"ar_learning_tools_1","tags":["learning_approach","hands_on"]},
        {"qt":"temporal","text":"What kind of work history characterizes your career?","opts":[
            {"id":"a","text":"Varied — different jobs, industries, or roles reflecting my need for variety","s":{"artisan":5}},
            {"id":"b","text":"Stable — progressive advancement in a consistent field","s":{"artisan":1,"guardian":5}},
            {"id":"c","text":"Purpose-driven — each role connected to helping others or pursuing meaning","s":{"artisan":1,"idealist":4}},
            {"id":"d","text":"Expertise-focused — deepening in areas of intellectual interest","s":{"artisan":1,"rational":4}}
        ],"tier":"core","grp":"ar_career_1","tags":["temporal","career_variety"]},
        {"qt":"behavioral_recall","text":"In arguments or debates, you tend to:","opts":[
            {"id":"a","text":"Go for the jugular — quick wit and tactical strikes","s":{"artisan":5}},
            {"id":"b","text":"Appeal to precedent and established facts","s":{"artisan":1,"guardian":3}},
            {"id":"c","text":"Appeal to values, empathy, and the human impact","s":{"artisan":1,"idealist":4}},
            {"id":"d","text":"Build a logical case systematically and dismantle the opposing argument","s":{"artisan":1,"rational":5}}
        ],"tier":"triangulation","grp":"ar_debate_1","tags":["debate_style","tactics"]},
        {"qt":"forced_choice","text":"Your ideal lifestyle includes:","opts":[
            {"id":"a","text":"Maximum freedom, variety, and opportunities for excitement","s":{"artisan":5}},
            {"id":"b","text":"Stability, community, and the comfort of established patterns","s":{"artisan":1,"guardian":5}},
            {"id":"c","text":"Deep relationships, meaningful work, and personal growth","s":{"artisan":1,"idealist":5}},
            {"id":"d","text":"Intellectual stimulation, autonomy, and opportunities to master complex skills","s":{"artisan":1,"rational":5}}
        ],"tier":"core","grp":"ar_ideal_life_1","tags":["ideal_lifestyle","freedom"]},
        {"qt":"scenario","text":"You've been doing the same job for two years. It's stable and pays well. You:","opts":[
            {"id":"a","text":"Feel like you're dying inside — you need change, challenge, or you'll leave","s":{"artisan":5}},
            {"id":"b","text":"Feel grateful for the stability — this is what responsible adulting looks like","s":{"artisan":1,"guardian":5}},
            {"id":"c","text":"Feel satisfied if the work is meaningful and relationships are good","s":{"artisan":1,"idealist":3}},
            {"id":"d","text":"Feel fine if you're still learning, frustrated if you've stopped growing","s":{"artisan":1,"rational":3}}
        ],"tier":"core","grp":"ar_stagnation_1","tags":["stagnation","restlessness"]},
        {"qt":"somatic","text":"When everything in your life is predictable and safe, you feel:","opts":[
            {"id":"a","text":"Suffocated — I need uncertainty and excitement to feel alive","s":{"artisan":5}},
            {"id":"b","text":"Secure — this is the goal","s":{"artisan":1,"guardian":5}},
            {"id":"c","text":"Grounded, as long as my relationships are fulfilling","s":{"artisan":1,"idealist":3}},
            {"id":"d","text":"Bored — predictability without intellectual challenge is stagnation","s":{"artisan":2,"rational":3}}
        ],"tier":"core","grp":"ar_predictability_1","tags":["somatic","predictability"]},
        {"qt":"behavioral_recall","text":"How do you handle multiple simultaneous demands?","opts":[
            {"id":"a","text":"Thrive — juggling multiple things at once keeps me sharp and engaged","s":{"artisan":5}},
            {"id":"b","text":"Prioritize and handle them sequentially — one thing at a time","s":{"artisan":1,"guardian":4}},
            {"id":"c","text":"Get stressed if the demands pull me away from the people who need me","s":{"artisan":1,"idealist":2}},
            {"id":"d","text":"Create a system to triage and manage them efficiently","s":{"artisan":1,"rational":4}}
        ],"tier":"triangulation","grp":"ar_multitask_1","tags":["multitasking","energy"]},
        {"qt":"forced_choice","text":"Which word resonates most deeply with how you want to live?","opts":[
            {"id":"a","text":"Freedom","s":{"artisan":5}},
            {"id":"b","text":"Responsibility","s":{"artisan":1,"guardian":5}},
            {"id":"c","text":"Authenticity","s":{"artisan":1,"idealist":5}},
            {"id":"d","text":"Competence","s":{"artisan":1,"rational":5}}
        ],"tier":"trap","grp":"ar_word_1","tags":["core_value","word_association"]},
        {"qt":"scenario","text":"You're watching a friend struggle with a task you could easily do for them. You:","opts":[
            {"id":"a","text":"Jump in and show them — demonstration beats explanation","s":{"artisan":5}},
            {"id":"b","text":"Walk them through the proper steps methodically","s":{"artisan":1,"guardian":3}},
            {"id":"c","text":"Ask if they want help — respect their autonomy","s":{"artisan":1,"idealist":3}},
            {"id":"d","text":"Explain the underlying principle so they can figure it out themselves","s":{"artisan":1,"rational":4}}
        ],"tier":"triangulation","grp":"ar_helping_style_1","tags":["helping_style","action"]},
    ],
    "idealist": [
        {"qt":"scenario","text":"You're choosing between two jobs: one pays more, the other aligns more closely with your values and sense of purpose. You:","opts":[
            {"id":"a","text":"Choose meaning without hesitation — money can't replace purpose","s":{"idealist":5}},
            {"id":"b","text":"Choose the higher pay — you can find meaning outside of work","s":{"idealist":1,"guardian":3}},
            {"id":"c","text":"Choose whichever is more exciting and varied","s":{"idealist":1,"artisan":3}},
            {"id":"d","text":"Analyze both options across multiple criteria including growth potential","s":{"idealist":1,"rational":4}}
        ],"tier":"core","grp":"id_meaning_1","tags":["meaning","values_alignment"]},
        {"qt":"behavioral_recall","text":"How central is personal growth to your life?","opts":[
            {"id":"a","text":"It's the primary organizing principle — I'm always working on becoming a better person","s":{"idealist":5}},
            {"id":"b","text":"It matters but so does maintaining stability and meeting obligations","s":{"idealist":2,"guardian":3}},
            {"id":"c","text":"Growth happens through experience and action, not introspection","s":{"idealist":1,"artisan":3}},
            {"id":"d","text":"Intellectual growth matters more to me than personal/emotional growth","s":{"idealist":1,"rational":4}}
        ],"tier":"core","grp":"id_growth_1","tags":["personal_growth","self_development"]},
        {"qt":"forced_choice","text":"In relationships, what do you value most?","opts":[
            {"id":"a","text":"Deep emotional authenticity — knowing and being truly known","s":{"idealist":5}},
            {"id":"b","text":"Reliability and commitment — being there through thick and thin","s":{"idealist":1,"guardian":4}},
            {"id":"c","text":"Fun, excitement, and shared adventures","s":{"idealist":1,"artisan":3}},
            {"id":"d","text":"Intellectual stimulation and mutual respect for competence","s":{"idealist":1,"rational":4}}
        ],"tier":"core","grp":"id_relationships_1","tags":["relationship_values","authenticity"]},
        {"qt":"somatic","text":"When you witness injustice, especially toward someone vulnerable, you feel:","opts":[
            {"id":"a","text":"A deep ache — injustice toward others is physically painful to me","s":{"idealist":5}},
            {"id":"b","text":"Frustration that the rules aren't being followed","s":{"idealist":1,"guardian":3}},
            {"id":"c","text":"Anger that drives immediate action","s":{"idealist":1,"artisan":3}},
            {"id":"d","text":"Analysis of the systemic causes and how to fix them","s":{"idealist":1,"rational":3}}
        ],"tier":"core","grp":"id_injustice_1","tags":["somatic","injustice","empathy"]},
        {"qt":"scenario","text":"A friend asks for your advice about a relationship problem. You:","opts":[
            {"id":"a","text":"Listen deeply, reflect their feelings back, and help them discover their own truth","s":{"idealist":5}},
            {"id":"b","text":"Give practical advice based on what's worked for you","s":{"idealist":1,"guardian":3}},
            {"id":"c","text":"Share your honest opinion directly — they asked, so you'll tell them","s":{"idealist":1,"artisan":3}},
            {"id":"d","text":"Help them analyze the situation logically to find the optimal decision","s":{"idealist":1,"rational":3}}
        ],"tier":"core","grp":"id_counseling_1","tags":["counseling","empathy"]},
        {"qt":"temporal","text":"How has your idealism changed over the years?","opts":[
            {"id":"a","text":"It's deepened — experience has shown me that meaning and purpose are what matter most","s":{"idealist":5}},
            {"id":"b","text":"I've become more practical — idealism needs to be grounded in reality","s":{"idealist":2,"guardian":3}},
            {"id":"c","text":"I've always been more practical than idealistic","s":{"idealist":1,"artisan":2}},
            {"id":"d","text":"My idealism has become more strategic — I apply it where it can make the biggest impact","s":{"idealist":3,"rational":2}}
        ],"tier":"core","grp":"id_idealism_1","tags":["idealism","temporal"]},
        {"qt":"forced_choice","text":"Which inner conflict is most familiar?","opts":[
            {"id":"a","text":"The gap between how the world is and how it should be — and feeling responsible for closing it","s":{"idealist":5}},
            {"id":"b","text":"Balancing personal desires with family and community obligations","s":{"idealist":1,"guardian":4}},
            {"id":"c","text":"Wanting freedom and novelty while needing stability and connection","s":{"idealist":1,"artisan":3}},
            {"id":"d","text":"Wanting to master everything while having limited time and energy","s":{"idealist":1,"rational":3}}
        ],"tier":"core","grp":"id_conflict_1","tags":["inner_conflict","idealism"]},
        {"qt":"scenario","text":"You discover that an organization you admired has been engaging in unethical practices. You:","opts":[
            {"id":"a","text":"Feel deeply betrayed — you gave them your trust and they violated your values","s":{"idealist":5}},
            {"id":"b","text":"Feel disappointed but not surprised — organizations are run by imperfect people","s":{"idealist":1,"guardian":2}},
            {"id":"c","text":"Don't dwell on it — find a better organization or move on","s":{"idealist":1,"artisan":2}},
            {"id":"d","text":"Analyze why the unethical practices emerged and what systemic changes are needed","s":{"idealist":2,"rational":3}}
        ],"tier":"core","grp":"id_betrayal_1","tags":["institutional_betrayal","values"]},
        {"qt":"behavioral_recall","text":"How important is it that your work has a positive impact on the world?","opts":[
            {"id":"a","text":"Essential — I can't sustain motivation for work that doesn't serve a larger good","s":{"idealist":5}},
            {"id":"b","text":"Important but secondary to providing for myself and my family","s":{"idealist":2,"guardian":3}},
            {"id":"c","text":"Nice but not required — I work for the experience and the paycheck","s":{"idealist":1,"artisan":3}},
            {"id":"d","text":"I define 'impact' broadly — creating excellent work IS a positive impact","s":{"idealist":1,"rational":3}}
        ],"tier":"core","grp":"id_impact_1","tags":["impact","purpose"]},
        {"qt":"somatic","text":"When you have a deep, authentic conversation with someone — real connection, real vulnerability — you feel:","opts":[
            {"id":"a","text":"Alive — this is what life is actually for","s":{"idealist":5}},
            {"id":"b","text":"Grateful but slightly uncomfortable — vulnerability is risky","s":{"idealist":2,"guardian":2}},
            {"id":"c","text":"Enjoyable but heavy — I prefer lighter interactions","s":{"idealist":1,"artisan":3}},
            {"id":"d","text":"Intellectually stimulating — deep conversation reveals how people think","s":{"idealist":2,"rational":3}}
        ],"tier":"core","grp":"id_connection_1","tags":["somatic","authentic_connection"]},
        {"qt":"forced_choice","text":"Your greatest strength in relationships is:","opts":[
            {"id":"a","text":"Seeing and drawing out the best in people — even potential they don't see themselves","s":{"idealist":5}},
            {"id":"b","text":"Being dependable and loyal — people know they can count on me","s":{"idealist":1,"guardian":5}},
            {"id":"c","text":"Being fun, spontaneous, and exciting to be around","s":{"idealist":1,"artisan":4}},
            {"id":"d","text":"Being honest, fair, and intellectually stimulating","s":{"idealist":1,"rational":3}}
        ],"tier":"core","grp":"id_strength_1","tags":["relationship_strength","potential_seeing"]},
        {"qt":"scenario","text":"You're in a leadership position and must make a decision that benefits the organization but harms a few individuals. You:","opts":[
            {"id":"a","text":"Agonize — the impact on those individuals weighs on you more than the organizational benefit","s":{"idealist":5}},
            {"id":"b","text":"Make the tough call — leadership requires difficult decisions for the greater good","s":{"idealist":1,"guardian":3}},
            {"id":"c","text":"Act decisively — dwelling helps nobody","s":{"idealist":1,"artisan":2}},
            {"id":"d","text":"Look for a third option that achieves the organizational goal without harming individuals","s":{"idealist":4,"rational":2}}
        ],"tier":"core","grp":"id_leadership_dilemma_1","tags":["leadership","ethical_dilemma"]},
        {"qt":"behavioral_recall","text":"How do you handle it when reality fails to match your ideals?","opts":[
            {"id":"a","text":"With deep disappointment that can spiral into disillusionment — the gap is painful","s":{"idealist":5}},
            {"id":"b","text":"Practically — ideals are targets, not expectations","s":{"idealist":1,"guardian":3}},
            {"id":"c","text":"By adjusting quickly — adapt to what IS, not what should be","s":{"idealist":1,"artisan":3}},
            {"id":"d","text":"By analyzing why the gap exists and engineering solutions","s":{"idealist":1,"rational":4}}
        ],"tier":"core","grp":"id_disillusionment_1","tags":["disillusionment","ideals_vs_reality"]},
        {"qt":"temporal","text":"How important is having a sense of personal mission or calling?","opts":[
            {"id":"a","text":"Central — without a sense of mission, life feels empty and purposeless","s":{"idealist":5}},
            {"id":"b","text":"Nice to have but not essential — duty and responsibility provide enough structure","s":{"idealist":1,"guardian":3}},
            {"id":"c","text":"I don't think in terms of 'mission' — I follow what excites me","s":{"idealist":1,"artisan":4}},
            {"id":"d","text":"I have intellectual goals that serve as my 'mission' but I don't frame it that way","s":{"idealist":1,"rational":3}}
        ],"tier":"core","grp":"id_mission_1","tags":["mission","calling","temporal"]},
        {"qt":"forced_choice","text":"Which would devastate you most?","opts":[
            {"id":"a","text":"Discovering that your life lacked meaning — that you never made a real difference","s":{"idealist":5}},
            {"id":"b","text":"Failing the people who depended on you","s":{"idealist":2,"guardian":4}},
            {"id":"c","text":"Looking back and realizing you played it safe and missed out on life","s":{"idealist":1,"artisan":4}},
            {"id":"d","text":"Remaining ignorant about things you could have understood","s":{"idealist":1,"rational":4}}
        ],"tier":"core","grp":"id_devastation_1","tags":["worst_fear","meaning"]},
        {"qt":"scenario","text":"You're in therapy or deep self-reflection and uncover a pattern where you sacrifice your own needs for others. You:","opts":[
            {"id":"a","text":"Recognize it as a lifelong pattern — caring for others IS my nature, but I need balance","s":{"idealist":5}},
            {"id":"b","text":"See it as fulfilling your duty — you're supposed to sacrifice for others","s":{"idealist":2,"guardian":3}},
            {"id":"c","text":"This pattern doesn't apply — you prioritize your own experience","s":{"idealist":1,"artisan":3}},
            {"id":"d","text":"Analyze it objectively and create strategies to establish boundaries","s":{"idealist":2,"rational":3}}
        ],"tier":"core","grp":"id_self_sacrifice_1","tags":["self_sacrifice","pattern_recognition"]},
        {"qt":"behavioral_recall","text":"How do you feel about conflict in relationships?","opts":[
            {"id":"a","text":"Deeply uncomfortable — I want harmony and conflict creates a rift in my sense of connection","s":{"idealist":5}},
            {"id":"b","text":"Necessary sometimes — conflict can be addressed responsibly","s":{"idealist":1,"guardian":3}},
            {"id":"c","text":"I don't mind it — say what you mean, clear the air, move on","s":{"idealist":1,"artisan":4}},
            {"id":"d","text":"I approach it analytically — what's the underlying issue and what's the solution?","s":{"idealist":1,"rational":4}}
        ],"tier":"core","grp":"id_conflict_avoidance_1","tags":["conflict","harmony"]},
        {"qt":"somatic","text":"When you see someone living below their potential, you feel:","opts":[
            {"id":"a","text":"An almost physical urge to help them see what you see in them","s":{"idealist":5}},
            {"id":"b","text":"It's their life — not my place to judge","s":{"idealist":1,"artisan":2}},
            {"id":"c","text":"Sympathy, but you respect their autonomy","s":{"idealist":3,"guardian":1}},
            {"id":"d","text":"Curiosity about what's holding them back from optimization","s":{"idealist":1,"rational":3}}
        ],"tier":"core","grp":"id_potential_1","tags":["somatic","potential_seeing"]},
        {"qt":"forced_choice","text":"Which describes your communication at its best?","opts":[
            {"id":"a","text":"Inspiring — I connect with people's hearts and help them see possibilities","s":{"idealist":5}},
            {"id":"b","text":"Clear and reliable — people know what I mean and trust what I say","s":{"idealist":1,"guardian":4}},
            {"id":"c","text":"Dynamic and persuasive — I read the room and adjust","s":{"idealist":1,"artisan":3}},
            {"id":"d","text":"Precise and insightful — I cut through confusion to the core issue","s":{"idealist":1,"rational":4}}
        ],"tier":"core","grp":"id_communication_1","tags":["communication","inspiration"]},
        {"qt":"scenario","text":"You're writing a personal mission statement. The core of it centers on:","opts":[
            {"id":"a","text":"Making a positive difference in people's lives and pursuing what's meaningful","s":{"idealist":5}},
            {"id":"b","text":"Being responsible, building something lasting, and serving my community","s":{"idealist":1,"guardian":4}},
            {"id":"c","text":"Living fully, experiencing everything, and mastering diverse skills","s":{"idealist":1,"artisan":4}},
            {"id":"d","text":"Understanding deeply, creating elegant solutions, and achieving mastery","s":{"idealist":1,"rational":4}}
        ],"tier":"core","grp":"id_mission_statement_1","tags":["mission_statement","purpose"]},
        {"qt":"temporal","text":"What do you believe about human nature at its core?","opts":[
            {"id":"a","text":"People are fundamentally good and capable of remarkable growth when supported","s":{"idealist":5}},
            {"id":"b","text":"People are a mix — they need structure and accountability to bring out their best","s":{"idealist":1,"guardian":3}},
            {"id":"c","text":"People are what they do, not what they aspire to — actions matter","s":{"idealist":1,"artisan":3}},
            {"id":"d","text":"People are rational actors who respond to incentives and logic","s":{"idealist":1,"rational":3}}
        ],"tier":"core","grp":"id_human_nature_1","tags":["human_nature","belief"]},
        {"qt":"behavioral_recall","text":"How often do you feel a deep longing for a world that doesn't yet exist?","opts":[
            {"id":"a","text":"Constantly — the vision of what could be drives everything I do","s":{"idealist":5}},
            {"id":"b","text":"Sometimes — but I focus on improving what we have","s":{"idealist":2,"guardian":2}},
            {"id":"c","text":"Rarely — I focus on the world as it is right now","s":{"idealist":1,"artisan":3}},
            {"id":"d","text":"I think about better systems but it's intellectual, not emotional","s":{"idealist":1,"rational":3}}
        ],"tier":"core","grp":"id_longing_1","tags":["longing","visionary"]},
        {"qt":"forced_choice","text":"Your approach to personal development is:","opts":[
            {"id":"a","text":"Holistic — emotional, spiritual, relational, and vocational growth are all intertwined","s":{"idealist":5}},
            {"id":"b","text":"Practical — develop skills that meet real-world needs","s":{"idealist":1,"guardian":3}},
            {"id":"c","text":"Experiential — you grow by doing, not by planning growth","s":{"idealist":1,"artisan":4}},
            {"id":"d","text":"Intellectual — expanding knowledge and capability is the primary growth axis","s":{"idealist":1,"rational":4}}
        ],"tier":"core","grp":"id_development_1","tags":["personal_development","holistic"]},
        {"qt":"scenario","text":"A close friend reveals they've been dishonest with you about something important. You:","opts":[
            {"id":"a","text":"Feel deeply wounded — authenticity and trust are sacred to you, and this violation cuts deep","s":{"idealist":5}},
            {"id":"b","text":"Feel betrayed but focus on understanding why they did it and what it means for the relationship","s":{"idealist":3,"guardian":1}},
            {"id":"c","text":"Feel angry in the moment but let it go quickly — people make mistakes","s":{"idealist":1,"artisan":3}},
            {"id":"d","text":"Evaluate what the dishonesty means about their character and whether the relationship is sustainable","s":{"idealist":1,"rational":4}}
        ],"tier":"core","grp":"id_dishonesty_1","tags":["dishonesty","trust","authenticity"]},
    ],
    "rational": [
        {"qt":"scenario","text":"You encounter a system at work that's functional but clearly suboptimal. Nobody else seems bothered by it. You:","opts":[
            {"id":"a","text":"Can't let it go — the inefficiency nags at you until you redesign it","s":{"rational":5}},
            {"id":"b","text":"Leave it alone — if it works, don't fix it","s":{"rational":1,"guardian":4}},
            {"id":"c","text":"Only care if it's causing problems for people you work with","s":{"rational":1,"idealist":3}},
            {"id":"d","text":"Fix it quickly with the minimum viable improvement","s":{"rational":2,"artisan":3}}
        ],"tier":"core","grp":"ra_optimization_1","tags":["optimization","system_thinking"]},
        {"qt":"behavioral_recall","text":"When someone presents an argument, your first instinct is:","opts":[
            {"id":"a","text":"Test its logic — look for flaws, inconsistencies, and unsupported assumptions","s":{"rational":5}},
            {"id":"b","text":"Evaluate it against established knowledge and precedent","s":{"rational":2,"guardian":3}},
            {"id":"c","text":"Consider how it makes you feel and whether it resonates with your values","s":{"rational":1,"idealist":3}},
            {"id":"d","text":"See if it matches your experience — does it ring true in practice?","s":{"rational":1,"artisan":3}}
        ],"tier":"core","grp":"ra_logic_1","tags":["logical_analysis","critical_thinking"]},
        {"qt":"forced_choice","text":"Which describes your deepest motivation?","opts":[
            {"id":"a","text":"To understand — knowledge and competence are their own rewards","s":{"rational":5}},
            {"id":"b","text":"To provide — security and stability for those who depend on me","s":{"rational":1,"guardian":4}},
            {"id":"c","text":"To experience — life is for living fully in the present","s":{"rational":1,"artisan":4}},
            {"id":"d","text":"To connect — relationships and meaning are what matter most","s":{"rational":1,"idealist":4}}
        ],"tier":"core","grp":"ra_motivation_1","tags":["motivation","knowledge"]},
        {"qt":"somatic","text":"When you finally understand something complex that has been puzzling you, the feeling is:","opts":[
            {"id":"a","text":"Profound satisfaction — like a deep intellectual hunger being fed","s":{"rational":5}},
            {"id":"b","text":"Pleased that you can now apply the knowledge practically","s":{"rational":2,"guardian":2}},
            {"id":"c","text":"Brief excitement before moving to the next interesting thing","s":{"rational":1,"artisan":3}},
            {"id":"d","text":"Eager to share the insight with others","s":{"rational":1,"idealist":3}}
        ],"tier":"core","grp":"ra_understanding_1","tags":["somatic","intellectual_satisfaction"]},
        {"qt":"scenario","text":"You're in a meeting and someone makes a claim that's emotionally compelling but logically flawed. You:","opts":[
            {"id":"a","text":"Point out the logical flaw, even if it makes you unpopular","s":{"rational":5}},
            {"id":"b","text":"Note it but don't challenge it if the group is aligned","s":{"rational":1,"guardian":2}},
            {"id":"c","text":"Challenge it with a counterexample rather than abstract logic","s":{"rational":2,"artisan":2}},
            {"id":"d","text":"Acknowledge the emotional truth while gently correcting the logic","s":{"rational":2,"idealist":2}}
        ],"tier":"core","grp":"ra_intellectual_honesty_1","tags":["intellectual_honesty","logic_vs_emotion"]},
        {"qt":"temporal","text":"How has your need for competence and mastery evolved?","opts":[
            {"id":"a","text":"It's been a constant — incompetence in myself is deeply unacceptable to me","s":{"rational":5}},
            {"id":"b","text":"I value competence but I've learned that reliability matters more than brilliance","s":{"rational":2,"guardian":3}},
            {"id":"c","text":"I seek competence in whatever I'm currently doing, but it shifts with my interests","s":{"rational":2,"artisan":2}},
            {"id":"d","text":"I've shifted from seeking competence to seeking wisdom and understanding","s":{"rational":3,"idealist":2}}
        ],"tier":"core","grp":"ra_competence_1","tags":["competence","temporal"]},
        {"qt":"forced_choice","text":"Your intellectual style is:","opts":[
            {"id":"a","text":"Systems-oriented — I see patterns, structures, and how things interconnect","s":{"rational":5}},
            {"id":"b","text":"Detail-oriented — I notice specifics and ensure accuracy","s":{"rational":2,"guardian":3}},
            {"id":"c","text":"Tactical — I think about what works right now in this specific situation","s":{"rational":1,"artisan":3}},
            {"id":"d","text":"Integrative — I connect ideas with human experience and meaning","s":{"rational":2,"idealist":3}}
        ],"tier":"core","grp":"ra_thinking_style_1","tags":["thinking_style","systems"]},
        {"qt":"scenario","text":"Someone asks you to explain why you love your partner. You:","opts":[
            {"id":"a","text":"Struggle — you know you love them but translating feelings into words isn't natural","s":{"rational":5}},
            {"id":"b","text":"List the qualities that make them a good partner — reliability, kindness, commitment","s":{"rational":1,"guardian":3}},
            {"id":"c","text":"Show rather than tell — take them on a spontaneous date instead","s":{"rational":1,"artisan":3}},
            {"id":"d","text":"Express it eloquently — articulating feelings is important to you","s":{"rational":1,"idealist":5}}
        ],"tier":"core","grp":"ra_emotional_expression_1","tags":["emotional_expression","relationships"]},
        {"qt":"behavioral_recall","text":"How do you handle incompetence in yourself?","opts":[
            {"id":"a","text":"With intense self-criticism — incompetence is my deepest shame","s":{"rational":5}},
            {"id":"b","text":"I work to improve but don't beat myself up — nobody's perfect at everything","s":{"rational":2,"guardian":2}},
            {"id":"c","text":"I focus on what I'm good at and don't worry about what I'm not","s":{"rational":1,"artisan":3}},
            {"id":"d","text":"With self-compassion — growth is a process, not a performance","s":{"rational":1,"idealist":4}}
        ],"tier":"core","grp":"ra_incompetence_1","tags":["self_criticism","competence"]},
        {"qt":"somatic","text":"When someone presents a sloppy argument with logical fallacies, you feel:","opts":[
            {"id":"a","text":"Physical discomfort — bad reasoning is almost painful to endure","s":{"rational":5}},
            {"id":"b","text":"Patience — not everyone thinks rigorously, and that's okay","s":{"rational":1,"guardian":2}},
            {"id":"c","text":"Impatient — skip the argument and just do something","s":{"rational":1,"artisan":3}},
            {"id":"d","text":"Empathy for the person even while noting the logical flaws","s":{"rational":1,"idealist":3}}
        ],"tier":"core","grp":"ra_logical_pain_1","tags":["somatic","logical_rigor"]},
        {"qt":"scenario","text":"You're designing a solution to a problem. You've found an approach that works but isn't elegant. You:","opts":[
            {"id":"a","text":"Keep working until you find the elegant solution — inelegance offends your aesthetic","s":{"rational":5}},
            {"id":"b","text":"Ship the working solution — functionality over elegance","s":{"rational":1,"guardian":3}},
            {"id":"c","text":"Ship it and iterate later if inspiration strikes","s":{"rational":1,"artisan":3}},
            {"id":"d","text":"Ask colleagues for input — collaboration might reveal the elegant path","s":{"rational":2,"idealist":2}}
        ],"tier":"core","grp":"ra_elegance_1","tags":["elegance","perfectionism"]},
        {"qt":"forced_choice","text":"In social situations, you're most likely to:","opts":[
            {"id":"a","text":"Observe the dynamics, analyze the subtext, and engage selectively","s":{"rational":5}},
            {"id":"b","text":"Fulfill your social obligations and be appropriately friendly","s":{"rational":1,"guardian":3}},
            {"id":"c","text":"Be the life of the party — social energy comes naturally","s":{"rational":1,"artisan":4}},
            {"id":"d","text":"Seek deep one-on-one conversations about things that matter","s":{"rational":1,"idealist":4}}
        ],"tier":"core","grp":"ra_social_1","tags":["social_approach","observation"]},
        {"qt":"behavioral_recall","text":"How do you feel about emotional expression in professional settings?","opts":[
            {"id":"a","text":"Uncomfortable — emotions cloud judgment and should be managed privately","s":{"rational":5}},
            {"id":"b","text":"Appropriate in moderation — being human at work is fine","s":{"rational":1,"guardian":2}},
            {"id":"c","text":"Natural — suppressing emotions is unhealthy regardless of setting","s":{"rational":1,"artisan":2}},
            {"id":"d","text":"Important — emotional authenticity builds trust and connection at work","s":{"rational":1,"idealist":4}}
        ],"tier":"core","grp":"ra_workplace_emotion_1","tags":["workplace","emotional_expression"]},
        {"qt":"temporal","text":"What kind of problems do you find most engaging?","opts":[
            {"id":"a","text":"Abstract, complex, systemic problems that require deep analysis","s":{"rational":5}},
            {"id":"b","text":"Practical problems with clear solutions that help real people","s":{"rational":1,"guardian":3}},
            {"id":"c","text":"Immediate, concrete problems that need creative solutions now","s":{"rational":1,"artisan":4}},
            {"id":"d","text":"Human problems — understanding why people behave as they do","s":{"rational":1,"idealist":4}}
        ],"tier":"core","grp":"ra_problem_type_1","tags":["problem_preference","abstraction"]},
        {"qt":"forced_choice","text":"Which describes your relationship with debate and intellectual disagreement?","opts":[
            {"id":"a","text":"I enjoy it — testing ideas through rigorous debate is how truth emerges","s":{"rational":5}},
            {"id":"b","text":"I participate when necessary but prefer consensus","s":{"rational":1,"guardian":3}},
            {"id":"c","text":"I debate to win, not to discover truth","s":{"rational":1,"artisan":3}},
            {"id":"d","text":"I avoid debate that might hurt feelings — there are gentler ways to explore ideas","s":{"rational":1,"idealist":3}}
        ],"tier":"core","grp":"ra_debate_1","tags":["debate","intellectual_combat"]},
        {"qt":"scenario","text":"You're reading about a topic you thought you understood well and discover you were fundamentally wrong. You:","opts":[
            {"id":"a","text":"Feel excited — being wrong means you're about to understand something new","s":{"rational":5}},
            {"id":"b","text":"Feel uncomfortable but update your understanding responsibly","s":{"rational":2,"guardian":2}},
            {"id":"c","text":"Shrug and move on — being wrong isn't a big deal","s":{"rational":1,"artisan":3}},
            {"id":"d","text":"Feel humbled and share the insight with others who might be similarly wrong","s":{"rational":2,"idealist":2}}
        ],"tier":"core","grp":"ra_being_wrong_1","tags":["being_wrong","intellectual_honesty"]},
        {"qt":"behavioral_recall","text":"How important is independence and autonomy in your work?","opts":[
            {"id":"a","text":"Essential — I need the freedom to pursue problems my own way without bureaucratic interference","s":{"rational":5}},
            {"id":"b","text":"Important but I work well within established structures too","s":{"rational":1,"guardian":3}},
            {"id":"c","text":"Very important — I resist anyone telling me how to do things","s":{"rational":2,"artisan":4}},
            {"id":"d","text":"I prefer collaborative work — ideas are better when developed together","s":{"rational":1,"idealist":3}}
        ],"tier":"core","grp":"ra_autonomy_1","tags":["autonomy","independence"]},
        {"qt":"somatic","text":"When you achieve mastery over a complex skill or concept, the dominant feeling is:","opts":[
            {"id":"a","text":"Quiet, deep satisfaction — competence is its own reward","s":{"rational":5}},
            {"id":"b","text":"Pride in a job well done","s":{"rational":2,"guardian":2}},
            {"id":"c","text":"Excitement about what you can now DO with the skill","s":{"rational":1,"artisan":3}},
            {"id":"d","text":"Gratitude and a desire to share what you've learned","s":{"rational":1,"idealist":3}}
        ],"tier":"core","grp":"ra_mastery_1","tags":["somatic","mastery"]},
        {"qt":"forced_choice","text":"How do you relate to imprecise language?","opts":[
            {"id":"a","text":"It frustrates me — precision in language reflects precision in thought","s":{"rational":5}},
            {"id":"b","text":"It's fine for everyday conversation — not everything needs to be precise","s":{"rational":1,"guardian":2}},
            {"id":"c","text":"I don't care about words — I care about action and impact","s":{"rational":1,"artisan":3}},
            {"id":"d","text":"Language should be more about connection than precision","s":{"rational":1,"idealist":3}}
        ],"tier":"core","grp":"ra_precision_1","tags":["precision","language"]},
        {"qt":"scenario","text":"A colleague presents you with an emotional appeal for why a project should be prioritized. The data doesn't support their position. You:","opts":[
            {"id":"a","text":"Present the data — decisions should be evidence-based, not emotion-based","s":{"rational":5}},
            {"id":"b","text":"Consider both the emotional and data perspectives — they both matter","s":{"rational":2,"guardian":2}},
            {"id":"c","text":"Go with the energy — if the team is passionate, that's worth something","s":{"rational":1,"artisan":2}},
            {"id":"d","text":"Validate their feelings while gently redirecting to what the evidence shows","s":{"rational":2,"idealist":3}}
        ],"tier":"core","grp":"ra_data_vs_emotion_1","tags":["data_driven","emotion_vs_logic"]},
        {"qt":"behavioral_recall","text":"What's your relationship with credentials and titles?","opts":[
            {"id":"a","text":"Irrelevant — competence is what matters, not what letters follow your name","s":{"rational":5}},
            {"id":"b","text":"Important — credentials signal preparation and commitment","s":{"rational":1,"guardian":4}},
            {"id":"c","text":"I judge people by what they do, not what they're certified to do","s":{"rational":2,"artisan":3}},
            {"id":"d","text":"Useful but not definitive — some of the wisest people have no formal credentials","s":{"rational":2,"idealist":2}}
        ],"tier":"triangulation","grp":"ra_credentials_1","tags":["credentials","meritocracy"]},
        {"qt":"temporal","text":"What do you spend the most mental energy on?","opts":[
            {"id":"a","text":"Understanding complex systems, solving problems, and building mental models","s":{"rational":5}},
            {"id":"b","text":"Planning, organizing, and managing responsibilities","s":{"rational":1,"guardian":4}},
            {"id":"c","text":"What's happening right now and what's coming next","s":{"rational":1,"artisan":3}},
            {"id":"d","text":"People — understanding them, helping them, connecting with them","s":{"rational":1,"idealist":4}}
        ],"tier":"core","grp":"ra_mental_energy_1","tags":["mental_energy","focus"]},
        {"qt":"forced_choice","text":"If you could be known for one quality, it would be:","opts":[
            {"id":"a","text":"Brilliant — capable of insights and solutions others can't achieve","s":{"rational":5}},
            {"id":"b","text":"Dependable — someone everyone can count on","s":{"rational":1,"guardian":5}},
            {"id":"c","text":"Bold — willing to act when others hesitate","s":{"rational":1,"artisan":4}},
            {"id":"d","text":"Compassionate — deeply caring and attuned to others","s":{"rational":1,"idealist":5}}
        ],"tier":"trap","grp":"ra_quality_1","tags":["desired_quality","identity"]},
        {"qt":"scenario","text":"You and your partner disagree about a life decision. They make an emotional case; you make a logical case. You:","opts":[
            {"id":"a","text":"Struggle to value their emotional reasoning as equivalent to your logical analysis","s":{"rational":5}},
            {"id":"b","text":"Try to find a compromise that respects both approaches","s":{"rational":2,"guardian":2}},
            {"id":"c","text":"Go with your gut — overthinking kills momentum","s":{"rational":1,"artisan":3}},
            {"id":"d","text":"Recognize that emotional and logical arguments both have valid insights","s":{"rational":2,"idealist":3}}
        ],"tier":"core","grp":"ra_relationship_logic_1","tags":["relationship","logic_vs_emotion"]},
    ],
}

for dim, qs in keirsey_data.items():
    for q in qs:
        entry = {
            "uid": f"KT-{uid:03d}",
            "assessment_id": "keirsey_temperament",
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

with open("/Users/user/personal/sb/trueassess/priv/question_bank/keirsey_temperament.json", "w") as f:
    json.dump(questions, f, indent=2)

print(f"Wrote {len(questions)} Keirsey questions")
