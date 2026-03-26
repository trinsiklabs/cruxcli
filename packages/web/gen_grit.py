import json

questions = []
uid = 1

# Grit: 15 questions per dimension = 60
grit_data = {
    "perseverance_of_effort": [
        {"qt":"scenario","text":"You've been working on a project for six months and you hit a wall — nothing is working despite trying multiple approaches. You:","opts":[
            {"id":"a","text":"Keep pushing — walls are temporary and you'll break through eventually","s":5},
            {"id":"b","text":"Step back and reassess your approach before continuing","s":3},
            {"id":"c","text":"Start questioning whether this project is worth the effort","s":2},
            {"id":"d","text":"Move on to something more promising — persistence past a point is stubbornness","s":1}
        ],"tier":"core","grp":"pe_persistence_1","tags":["persistence","obstacles"]},
        {"qt":"behavioral_recall","text":"When a task is much harder than you expected, your typical response is:","opts":[
            {"id":"a","text":"Double down — difficulty makes me more determined, not less","s":5},
            {"id":"b","text":"Adjust my timeline but keep working toward the goal","s":4},
            {"id":"c","text":"Consider whether it's worth the extra effort","s":2},
            {"id":"d","text":"Look for an easier path to a similar outcome","s":1}
        ],"tier":"core","grp":"pe_difficulty_1","tags":["difficulty_response","effort"]},
        {"qt":"forced_choice","text":"Which best describes your work ethic?","opts":[
            {"id":"a","text":"I'm a grinder — I'll outwork anyone through sheer sustained effort","s":5},
            {"id":"b","text":"I work hard but I also work smart — effort alone isn't enough","s":3},
            {"id":"c","text":"I work in bursts — intense effort followed by breaks","s":2},
            {"id":"d","text":"I prefer efficiency over effort — find the shortcut, not the long road","s":1}
        ],"tier":"core","grp":"pe_work_ethic_1","tags":["work_ethic","effort"]},
        {"qt":"somatic","text":"When you're deep into a challenging task that requires sustained concentration, your body:","opts":[
            {"id":"a","text":"Enters a zone — I forget fatigue, hunger, even time, until the task is done","s":5},
            {"id":"b","text":"Reminds me to take breaks, which I take before returning to the task","s":3},
            {"id":"c","text":"Gets restless — sustained focus is physically draining for me","s":2},
            {"id":"d","text":"Sends signals to stop that I usually listen to","s":1}
        ],"tier":"core","grp":"pe_endurance_1","tags":["somatic","mental_endurance"]},
        {"qt":"scenario","text":"You're training for a physical goal (marathon, weight target, skill). Progress has stalled for three weeks. You:","opts":[
            {"id":"a","text":"Stay the course — plateaus are normal and breakthrough follows patience","s":5},
            {"id":"b","text":"Research what might be causing the plateau and adjust your approach","s":4},
            {"id":"c","text":"Get frustrated and consider lowering your goal","s":2},
            {"id":"d","text":"Take a break and come back to it later — or not at all","s":1}
        ],"tier":"core","grp":"pe_plateau_1","tags":["plateaus","persistence"]},
        {"qt":"temporal","text":"Looking at your life, how would you characterize your relationship with hard work?","opts":[
            {"id":"a","text":"Hard work has been the single most reliable factor in everything I've achieved","s":5},
            {"id":"b","text":"Hard work is important but so are strategy, timing, and luck","s":3},
            {"id":"c","text":"I've worked hard when necessary but I don't define myself by effort","s":2},
            {"id":"d","text":"I've found that working smarter matters more than working harder","s":1}
        ],"tier":"core","grp":"pe_temporal_1","tags":["temporal","effort_history"]},
        {"qt":"behavioral_recall","text":"How do you handle tedious practice required to master a skill?","opts":[
            {"id":"a","text":"I embrace it — repetition is the path to mastery and I don't shy from it","s":5},
            {"id":"b","text":"I do it because I know it's necessary, but it's not enjoyable","s":3},
            {"id":"c","text":"I struggle with it — I lose focus during repetitive practice","s":2},
            {"id":"d","text":"I look for ways to skip the tedious parts and learn through doing","s":1}
        ],"tier":"core","grp":"pe_practice_1","tags":["deliberate_practice","tedium"]},
        {"qt":"forced_choice","text":"When faced with failure, your dominant response is:","opts":[
            {"id":"a","text":"Get back up immediately — failure is fuel, not an ending","s":5},
            {"id":"b","text":"Process the disappointment, learn from it, and try again","s":4},
            {"id":"c","text":"Take time to recover — failure hits me hard before I can try again","s":2},
            {"id":"d","text":"Reevaluate whether the goal is worth pursuing","s":1}
        ],"tier":"core","grp":"pe_failure_1","tags":["failure_response","resilience"]},
        {"qt":"scenario","text":"You're the last person still working on a group assignment that others have given up on. You:","opts":[
            {"id":"a","text":"Keep going — you committed and you'll finish even if you're alone","s":5},
            {"id":"b","text":"Continue but with some resentment toward those who quit","s":3},
            {"id":"c","text":"Question whether finishing alone is a reasonable expectation","s":2},
            {"id":"d","text":"Stop — if the group abandoned it, maybe it wasn't worth finishing","s":1}
        ],"tier":"triangulation","grp":"pe_solo_1","tags":["solo_persistence","commitment"]},
        {"qt":"somatic","text":"When you've been working intensely for hours and your body is exhausted but the task isn't done, you:","opts":[
            {"id":"a","text":"Override the exhaustion — the task completion matters more than comfort","s":5},
            {"id":"b","text":"Push a bit more then stop before quality deteriorates","s":3},
            {"id":"c","text":"Stop — diminishing returns make continuing counterproductive","s":2},
            {"id":"d","text":"Listen to my body and rest — the task can wait","s":1}
        ],"tier":"core","grp":"pe_exhaustion_1","tags":["somatic","pushing_through"]},
        {"qt":"behavioral_recall","text":"In your career or education, how many times have you continued pursuing something despite others telling you it wouldn't work?","opts":[
            {"id":"a","text":"Many times — others' doubts often strengthen my resolve","s":5},
            {"id":"b","text":"A few significant times — when I believed strongly enough","s":3},
            {"id":"c","text":"Rarely — I take others' input seriously when deciding to continue","s":2},
            {"id":"d","text":"I've learned to listen when multiple people give the same advice to quit","s":1}
        ],"tier":"core","grp":"pe_defiance_1","tags":["defiance_of_doubt","conviction"]},
        {"qt":"forced_choice","text":"Which describes your approach to setbacks?","opts":[
            {"id":"a","text":"Setbacks are just speed bumps — they slow me down but never stop me","s":5},
            {"id":"b","text":"Setbacks are opportunities to learn and adjust my approach","s":4},
            {"id":"c","text":"Setbacks are discouraging and I need time to recover motivation","s":2},
            {"id":"d","text":"Setbacks sometimes signal that I should change direction entirely","s":1}
        ],"tier":"core","grp":"pe_setbacks_1","tags":["setback_response","resilience"]},
        {"qt":"scenario","text":"You're learning a new skill and you're stuck at the 'mediocre' stage — good enough to do it but far from mastery. You:","opts":[
            {"id":"a","text":"Commit to the long slog toward mastery — mediocrity is not acceptable","s":5},
            {"id":"b","text":"Continue improving but accept that mastery takes years","s":4},
            {"id":"c","text":"Settle for competence — not everything needs to be mastered","s":2},
            {"id":"d","text":"Move on to something new — the initial learning phase is what energizes you","s":1}
        ],"tier":"core","grp":"pe_mastery_1","tags":["mastery","long_game"]},
        {"qt":"temporal","text":"Think about the hardest period of sustained effort in your life. How long did you maintain it?","opts":[
            {"id":"a","text":"Years — I sustained intense effort through an extended difficult period","s":5},
            {"id":"b","text":"Months — long enough to achieve a significant goal","s":3},
            {"id":"c","text":"Weeks — I can do intense bursts but not sustained long-term effort","s":2},
            {"id":"d","text":"Days — I'm better at sprints than marathons","s":1}
        ],"tier":"core","grp":"pe_endurance_temporal_1","tags":["temporal","sustained_effort"]},
        {"qt":"behavioral_recall","text":"What's your completion rate for difficult, long-term goals you've set?","opts":[
            {"id":"a","text":"Very high — once I commit, I almost always finish","s":5},
            {"id":"b","text":"More complete than abandon, but some fall away","s":3},
            {"id":"c","text":"About even — I finish some and abandon others","s":2},
            {"id":"d","text":"Lower than I'd like — I set ambitious goals but often don't finish","s":1}
        ],"tier":"consistency_check","grp":"pe_completion_1","tags":["completion_rate","self_assessment"]},
    ],
    "consistency_of_interest": [
        {"qt":"scenario","text":"You discover an exciting new hobby that you're passionate about. Over the next two years, you:","opts":[
            {"id":"a","text":"Deepen your engagement — the passion grows as you learn more","s":5},
            {"id":"b","text":"Stay interested but your initial passion moderates to steady engagement","s":3},
            {"id":"c","text":"Go through waves of intense interest and disinterest","s":2},
            {"id":"d","text":"Move on to something newer and more exciting within months","s":1}
        ],"tier":"core","grp":"ci_hobby_1","tags":["interest_stability","passion"]},
        {"qt":"behavioral_recall","text":"How many major interests or pursuits have you maintained for more than five years?","opts":[
            {"id":"a","text":"Several — I have core interests that have defined me for years or decades","s":5},
            {"id":"b","text":"One or two that have been constant while others rotate","s":3},
            {"id":"c","text":"Few to none — my interests change regularly","s":1},
            {"id":"d","text":"I have persistent interests but I explore many new ones too","s":3}
        ],"tier":"core","grp":"ci_longterm_1","tags":["long_term_interest","consistency"]},
        {"qt":"forced_choice","text":"Which describes your pattern of engagement with projects?","opts":[
            {"id":"a","text":"I'm a finisher — I see things through to completion with sustained focus","s":5},
            {"id":"b","text":"I finish most things but some lose their appeal before completion","s":3},
            {"id":"c","text":"I'm a starter — the beginning is the most exciting part","s":1},
            {"id":"d","text":"I cycle between projects, sometimes returning to old ones with renewed energy","s":2}
        ],"tier":"core","grp":"ci_project_pattern_1","tags":["project_completion","engagement_pattern"]},
        {"qt":"somatic","text":"When you think about your current primary goal or interest, you feel:","opts":[
            {"id":"a","text":"The same deep pull you felt when you first committed — unchanged over time","s":5},
            {"id":"b","text":"Steady motivation that fluctuates but never disappears","s":3},
            {"id":"c","text":"Less enthusiasm than when you started — the novelty has worn off","s":2},
            {"id":"d","text":"Already thinking about what might be next","s":1}
        ],"tier":"core","grp":"ci_current_goal_1","tags":["somatic","current_motivation"]},
        {"qt":"scenario","text":"A new opportunity appears that's tangentially related to your long-term goal but would require shifting focus. You:","opts":[
            {"id":"a","text":"Stay the course — diluting focus is the enemy of deep achievement","s":5},
            {"id":"b","text":"Evaluate whether it genuinely advances your goal before deciding","s":3},
            {"id":"c","text":"Get excited and pivot — new opportunities are how growth happens","s":1},
            {"id":"d","text":"Try to pursue both simultaneously, knowing you'll likely drop one","s":2}
        ],"tier":"core","grp":"ci_shiny_object_1","tags":["focus","new_opportunities"]},
        {"qt":"temporal","text":"Looking at your career or educational path, how consistent has your direction been?","opts":[
            {"id":"a","text":"Very consistent — I identified my path early and have pursued it steadily","s":5},
            {"id":"b","text":"Mostly consistent with some detours that ultimately reinforced my direction","s":4},
            {"id":"c","text":"Somewhat scattered — I've tried several different directions","s":2},
            {"id":"d","text":"Highly varied — I've reinvented myself multiple times","s":1}
        ],"tier":"core","grp":"ci_career_1","tags":["temporal","career_consistency"]},
        {"qt":"forced_choice","text":"When you encounter the 'boring middle' of a pursuit — past the excitement of beginning but far from the reward of completion — you:","opts":[
            {"id":"a","text":"Lean into it — the boring middle is where real growth happens","s":5},
            {"id":"b","text":"Tolerate it with discipline and the end goal in mind","s":4},
            {"id":"c","text":"Struggle — the lack of novelty makes it hard to maintain motivation","s":2},
            {"id":"d","text":"Often abandon at this point — if it's not exciting, why continue?","s":1}
        ],"tier":"core","grp":"ci_boring_middle_1","tags":["boring_middle","sustained_interest"]},
        {"qt":"behavioral_recall","text":"Friends and family would describe your interests as:","opts":[
            {"id":"a","text":"Deep and consistent — they know exactly what you're passionate about","s":5},
            {"id":"b","text":"Stable with occasional new additions","s":3},
            {"id":"c","text":"Varied and changing — they never know what you'll be into next","s":1},
            {"id":"d","text":"Intense but short-lived — passionate about something new every few months","s":1}
        ],"tier":"triangulation","grp":"ci_others_view_1","tags":["others_perception","interest_pattern"]},
        {"qt":"scenario","text":"You've been studying or practicing something for three years and a friend excitedly tells you about a completely different field. You:","opts":[
            {"id":"a","text":"Listen politely but feel no pull — your current path has your full commitment","s":5},
            {"id":"b","text":"Find it interesting but don't seriously consider switching","s":3},
            {"id":"c","text":"Feel the familiar tug of new-interest excitement and wonder if you should explore it","s":2},
            {"id":"d","text":"Immediately start researching the new field — variety is how you learn","s":1}
        ],"tier":"core","grp":"ci_distraction_1","tags":["distraction_resistance","commitment"]},
        {"qt":"somatic","text":"When you contemplate abandoning a long-held goal for a new one, you feel:","opts":[
            {"id":"a","text":"Physical resistance — like my identity is anchored to this goal","s":5},
            {"id":"b","text":"Discomfort mixed with excitement about the new possibility","s":3},
            {"id":"c","text":"Liberation — letting go of old goals feels freeing","s":1},
            {"id":"d","text":"Guilt about 'wasted time' on the old goal","s":3}
        ],"tier":"core","grp":"ci_abandonment_1","tags":["somatic","goal_abandonment"]},
        {"qt":"forced_choice","text":"How many times have you fundamentally changed your primary life direction?","opts":[
            {"id":"a","text":"Never or once — I found my direction early and stayed with it","s":5},
            {"id":"b","text":"Two or three times — significant but not frequent changes","s":3},
            {"id":"c","text":"Several times — I've had many 'phases'","s":1},
            {"id":"d","text":"I don't have a single primary direction — I pursue multiple things simultaneously","s":1}
        ],"tier":"consistency_check","grp":"ci_direction_changes_1","tags":["direction_changes","life_path"]},
        {"qt":"behavioral_recall","text":"When you're in the middle of a long-term project and you read about someone else's exciting new venture, you:","opts":[
            {"id":"a","text":"Feel happy for them and return to your work with renewed focus","s":5},
            {"id":"b","text":"Feel a pang of FOMO but remind yourself of your own commitment","s":3},
            {"id":"c","text":"Feel envious of their excitement and question your own choice","s":2},
            {"id":"d","text":"Start researching similar ventures — maybe you should pivot","s":1}
        ],"tier":"core","grp":"ci_fomo_1","tags":["FOMO","comparison"]},
        {"qt":"temporal","text":"How quickly does your 'passion' for something new typically peak and decline?","opts":[
            {"id":"a","text":"It doesn't decline — my passions deepen over time rather than fading","s":5},
            {"id":"b","text":"Initial excitement moderates but transforms into steady engagement","s":4},
            {"id":"c","text":"Peak within weeks, plateau for months, then gradually decline","s":2},
            {"id":"d","text":"Intense peak within days or weeks, then rapid decline","s":1}
        ],"tier":"core","grp":"ci_passion_curve_1","tags":["temporal","passion_lifecycle"]},
        {"qt":"scenario","text":"You achieve a long-term goal after years of focused effort. The next day, you:","opts":[
            {"id":"a","text":"Start the next phase of the same pursuit — achievement reveals new depths","s":5},
            {"id":"b","text":"Celebrate and then begin planning what's next in the same domain","s":4},
            {"id":"c","text":"Feel lost — the goal was the motivator and now there's a void","s":2},
            {"id":"d","text":"Feel ready for something completely different — this chapter is closed","s":1}
        ],"tier":"core","grp":"ci_post_achievement_1","tags":["post_achievement","direction"]},
        {"qt":"forced_choice","text":"Your bookshelf (or reading history) reveals:","opts":[
            {"id":"a","text":"Deep expertise in a few areas — many books on the same topics","s":5},
            {"id":"b","text":"Clusters of related topics with some breadth","s":3},
            {"id":"c","text":"Wide variety — a little of everything, no strong theme","s":1},
            {"id":"d","text":"Intense phases — all books on one topic, then a completely different one","s":2}
        ],"tier":"triangulation","grp":"ci_reading_1","tags":["reading_patterns","interest_depth"]},
    ],
    "passion_stability": [
        {"qt":"scenario","text":"You wake up one morning and the thing you were passionate about yesterday feels meaningless. This happens:","opts":[
            {"id":"a","text":"Almost never — my passion is remarkably stable regardless of mood","s":5},
            {"id":"b","text":"Rarely — usually after burnout or a significant setback","s":3},
            {"id":"c","text":"Occasionally — my enthusiasm fluctuates with my mood","s":2},
            {"id":"d","text":"Frequently — I question my direction regularly","s":1}
        ],"tier":"core","grp":"ps_stability_1","tags":["passion_stability","mood_independence"]},
        {"qt":"behavioral_recall","text":"How would you describe the intensity of your passion for your primary pursuit over time?","opts":[
            {"id":"a","text":"Like a steady flame — it burns consistently, sometimes brighter, never out","s":5},
            {"id":"b","text":"Like waves — highs and lows but it always comes back","s":3},
            {"id":"c","text":"Like fireworks — spectacular initially but fading quickly","s":1},
            {"id":"d","text":"Like a controlled burn — I manage it to prevent both burnout and extinction","s":4}
        ],"tier":"core","grp":"ps_metaphor_1","tags":["passion_pattern","metaphor"]},
        {"qt":"forced_choice","text":"When external circumstances make it impossible to pursue your passion temporarily, you:","opts":[
            {"id":"a","text":"Feel lost — it's so central to who I am that its absence is disorienting","s":5},
            {"id":"b","text":"Miss it and count the days until I can return to it","s":4},
            {"id":"c","text":"Find other things to engage with — I'm adaptable","s":2},
            {"id":"d","text":"Use the break to discover new interests","s":1}
        ],"tier":"core","grp":"ps_absence_1","tags":["passion_absence","identity"]},
        {"qt":"somatic","text":"When you're engaged in your core passion, the physical experience is:","opts":[
            {"id":"a","text":"Fulfilling and energizing — it's the most natural state for my body and mind","s":5},
            {"id":"b","text":"Engaging and absorbing — I'm fully present","s":3},
            {"id":"c","text":"Variable — sometimes I'm fully in it, sometimes I'm going through the motions","s":2},
            {"id":"d","text":"Depends on the day — passion can't always override fatigue or mood","s":2}
        ],"tier":"core","grp":"ps_engagement_1","tags":["somatic","engagement_quality"]},
        {"qt":"scenario","text":"Someone you respect deeply tells you that your passion is unlikely to lead anywhere meaningful. You:","opts":[
            {"id":"a","text":"Acknowledge their perspective but feel zero wavering — this isn't about outcomes, it's who I am","s":5},
            {"id":"b","text":"Consider their input but ultimately trust your own judgment","s":4},
            {"id":"c","text":"Feel shaken and question whether they might be right","s":2},
            {"id":"d","text":"Start exploring alternatives while keeping your passion as a hobby","s":1}
        ],"tier":"core","grp":"ps_external_doubt_1","tags":["external_doubt","conviction"]},
        {"qt":"temporal","text":"How many passions have you had in your adult life that you would call 'deep and sustained'?","opts":[
            {"id":"a","text":"One or two that have been with me for decades — they're part of my identity","s":5},
            {"id":"b","text":"A few that lasted years each","s":3},
            {"id":"c","text":"Many that lasted months to a year each","s":1},
            {"id":"d","text":"I'm not sure I've ever had a passion I'd call 'deep and sustained'","s":1}
        ],"tier":"core","grp":"ps_count_1","tags":["temporal","passion_history"]},
        {"qt":"forced_choice","text":"What's the relationship between your passion and your identity?","opts":[
            {"id":"a","text":"They're inseparable — my passion IS who I am at my core","s":5},
            {"id":"b","text":"My passion is important to my identity but doesn't define it entirely","s":3},
            {"id":"c","text":"My identity is broader than any single passion","s":2},
            {"id":"d","text":"My identity shifts as my passions change","s":1}
        ],"tier":"core","grp":"ps_identity_1","tags":["identity","passion_centrality"]},
        {"qt":"behavioral_recall","text":"When you're going through a difficult personal period (depression, grief, stress), your passion:","opts":[
            {"id":"a","text":"Remains a lifeline — it sustains me through the hardest times","s":5},
            {"id":"b","text":"Takes a backseat but returns as I recover","s":3},
            {"id":"c","text":"Evaporates — I can't access passion when I'm struggling","s":1},
            {"id":"d","text":"Becomes a source of frustration because I can't engage with it the way I want","s":4}
        ],"tier":"core","grp":"ps_adversity_1","tags":["adversity","passion_resilience"]},
        {"qt":"scenario","text":"You meet someone who shares your exact passion but has achieved much more than you. You:","opts":[
            {"id":"a","text":"Feel inspired — their success confirms the path is worth pursuing","s":5},
            {"id":"b","text":"Feel a mix of inspiration and envy but stay committed","s":3},
            {"id":"c","text":"Feel discouraged — their achievement makes yours seem small","s":2},
            {"id":"d","text":"Feel curious about what else might be worth pursuing","s":1}
        ],"tier":"triangulation","grp":"ps_comparison_1","tags":["social_comparison","passion_resilience"]},
        {"qt":"somatic","text":"When you can't pursue your passion for an extended period, you experience:","opts":[
            {"id":"a","text":"A physical ache — like being separated from something essential","s":5},
            {"id":"b","text":"Restlessness and longing","s":4},
            {"id":"c","text":"Relief — sometimes a break is welcome","s":1},
            {"id":"d","text":"I fill the space with other things and don't miss it much","s":1}
        ],"tier":"core","grp":"ps_absence_somatic_1","tags":["somatic","withdrawal"]},
        {"qt":"forced_choice","text":"If you could quantify your passion level on a scale of 1-10, how stable is it month to month?","opts":[
            {"id":"a","text":"Always 8-10 — remarkably consistent regardless of circumstances","s":5},
            {"id":"b","text":"Usually 6-8 — it dips sometimes but stays in a healthy range","s":3},
            {"id":"c","text":"Highly variable — could be 2 one month and 10 the next","s":1},
            {"id":"d","text":"It's been declining gradually — what started at 9 is now at 5","s":1}
        ],"tier":"core","grp":"ps_quantified_1","tags":["stability_quantified","consistency"]},
        {"qt":"behavioral_recall","text":"How do you sustain passion through the mundane parts of your pursuit?","opts":[
            {"id":"a","text":"The mundane parts ARE part of the passion — I find meaning in every aspect","s":5},
            {"id":"b","text":"I focus on the bigger picture while tolerating the mundane parts","s":3},
            {"id":"c","text":"I struggle with the mundane parts and my passion dims during them","s":2},
            {"id":"d","text":"The mundane parts are when my passion is most at risk of dying","s":1}
        ],"tier":"core","grp":"ps_mundane_1","tags":["mundane_sustaining","passion_depth"]},
        {"qt":"temporal","text":"Five years from now, do you expect to still be pursuing your current primary passion?","opts":[
            {"id":"a","text":"Absolutely — I can't imagine my life without it","s":5},
            {"id":"b","text":"Very likely — though the specific form might evolve","s":4},
            {"id":"c","text":"Possibly — but I'm open to change","s":2},
            {"id":"d","text":"Probably not — I expect to have moved on to something new","s":1}
        ],"tier":"core","grp":"ps_future_1","tags":["temporal","future_commitment"]},
        {"qt":"scenario","text":"Your passion suddenly becomes trendy — everyone's doing it now. Does this change your relationship with it?","opts":[
            {"id":"a","text":"Not at all — my passion exists independently of what's trendy","s":5},
            {"id":"b","text":"I might feel annoyed by newcomers but my commitment doesn't change","s":4},
            {"id":"c","text":"It might re-energize me to see others sharing the passion","s":3},
            {"id":"d","text":"I might lose interest — part of the appeal was that it was uniquely mine","s":1}
        ],"tier":"triangulation","grp":"ps_trendy_1","tags":["trend_independence","intrinsic_motivation"]},
        {"qt":"forced_choice","text":"What's the primary fuel source for your passion?","opts":[
            {"id":"a","text":"Internal — it comes from something deep inside me that doesn't need external validation","s":5},
            {"id":"b","text":"Mostly internal with some external reinforcement helping","s":3},
            {"id":"c","text":"External — recognition, results, and feedback keep me going","s":1},
            {"id":"d","text":"A mix that shifts — sometimes internal drive, sometimes external motivation","s":2}
        ],"tier":"core","grp":"ps_fuel_1","tags":["intrinsic_motivation","fuel_source"]},
    ],
    "resilience_to_setbacks": [
        {"qt":"scenario","text":"You've just experienced a major professional failure — a project you led publicly collapsed. You:","opts":[
            {"id":"a","text":"Process the disappointment rapidly and start planning your comeback within days","s":5},
            {"id":"b","text":"Take time to grieve and learn from it before trying again","s":3},
            {"id":"c","text":"Feel devastated and need significant time before you can face the domain again","s":2},
            {"id":"d","text":"Question whether this field is right for you","s":1}
        ],"tier":"core","grp":"rs_major_failure_1","tags":["major_failure","recovery_speed"]},
        {"qt":"behavioral_recall","text":"After your worst life setback, how long did it take you to start moving forward again?","opts":[
            {"id":"a","text":"Days to weeks — I bounce back quickly even from devastating blows","s":5},
            {"id":"b","text":"Weeks to months — I took the time I needed but didn't stay down","s":3},
            {"id":"c","text":"Months to a year — major setbacks hit me very hard","s":2},
            {"id":"d","text":"I'm still recovering from my worst setback","s":1}
        ],"tier":"core","grp":"rs_recovery_time_1","tags":["recovery_time","worst_setback"]},
        {"qt":"forced_choice","text":"Which describes your internal narrative after failure?","opts":[
            {"id":"a","text":"'This is data. What did I learn and what's the next move?'","s":5},
            {"id":"b","text":"'This hurts, but it's not the end of the story'","s":4},
            {"id":"c","text":"'Maybe I'm not cut out for this'","s":1},
            {"id":"d","text":"'Why does this keep happening to me?'","s":1}
        ],"tier":"core","grp":"rs_narrative_1","tags":["internal_narrative","failure_interpretation"]},
        {"qt":"somatic","text":"When you experience a setback, your body's stress response:","opts":[
            {"id":"a","text":"Activates briefly then normalizes — I metabolize stress quickly","s":5},
            {"id":"b","text":"Activates and takes some time to settle — hours to a day","s":3},
            {"id":"c","text":"Stays activated for extended periods — I carry the stress in my body for days or weeks","s":2},
            {"id":"d","text":"Can be debilitating — setbacks trigger full stress responses that impair functioning","s":1}
        ],"tier":"core","grp":"rs_stress_response_1","tags":["somatic","stress_recovery"]},
        {"qt":"scenario","text":"You apply for your dream position and receive a rejection. Within a week, a similar position opens up. You:","opts":[
            {"id":"a","text":"Apply immediately with an improved application — last rejection was a learning opportunity","s":5},
            {"id":"b","text":"Apply but with some lingering self-doubt from the rejection","s":3},
            {"id":"c","text":"Hesitate — the recent rejection has dented your confidence","s":2},
            {"id":"d","text":"Don't apply — the rejection means you're probably not qualified","s":1}
        ],"tier":"core","grp":"rs_repeated_attempt_1","tags":["repeated_attempts","confidence"]},
        {"qt":"temporal","text":"How has your resilience to setbacks changed over the years?","opts":[
            {"id":"a","text":"Strengthened — each setback has made me more resilient and quicker to recover","s":5},
            {"id":"b","text":"About the same — I handle setbacks consistently","s":3},
            {"id":"c","text":"Weakened — accumulating setbacks have made each one harder to handle","s":1},
            {"id":"d","text":"Variable — some setbacks I handle well, others still devastate me","s":2}
        ],"tier":"core","grp":"rs_temporal_1","tags":["temporal","resilience_development"]},
        {"qt":"forced_choice","text":"How many failures can you sustain before questioning your fundamental path?","opts":[
            {"id":"a","text":"Nearly unlimited — failure is information, not a verdict on my direction","s":5},
            {"id":"b","text":"Many — it takes a consistent pattern of failure to make me reconsider","s":4},
            {"id":"c","text":"A few — repeated failure in the same area signals I should change course","s":2},
            {"id":"d","text":"One or two major failures are enough to make me question everything","s":1}
        ],"tier":"core","grp":"rs_threshold_1","tags":["failure_threshold","persistence"]},
        {"qt":"behavioral_recall","text":"When you think about your failures, the dominant emotion is:","opts":[
            {"id":"a","text":"Gratitude — they taught me things success couldn't have","s":5},
            {"id":"b","text":"Acceptance — they happened and I've moved forward","s":3},
            {"id":"c","text":"Regret — I wish I had done things differently","s":2},
            {"id":"d","text":"Shame — they reflect something fundamentally wrong with me","s":1}
        ],"tier":"core","grp":"rs_emotion_1","tags":["failure_emotion","relationship_with_failure"]},
        {"qt":"scenario","text":"A mentor you admire tells you that your recent setback should make you reconsider your entire approach. You:","opts":[
            {"id":"a","text":"Consider their perspective but trust your own assessment of the situation","s":5},
            {"id":"b","text":"Take their advice seriously and make adjustments to your approach","s":3},
            {"id":"c","text":"Feel shaken and potentially change your entire direction based on their input","s":1},
            {"id":"d","text":"Seek additional perspectives before making any changes","s":3}
        ],"tier":"triangulation","grp":"rs_external_input_1","tags":["external_input","self_trust"]},
        {"qt":"somatic","text":"The morning after a significant setback, you wake up feeling:","opts":[
            {"id":"a","text":"Ready to fight — setbacks activate my determination","s":5},
            {"id":"b","text":"Sore but functional — I can face the day even if I'm not at my best","s":3},
            {"id":"c","text":"Heavy — the weight of the setback is still sitting on my chest","s":2},
            {"id":"d","text":"Unable to get out of bed — setbacks can be physically immobilizing for me","s":1}
        ],"tier":"core","grp":"rs_morning_after_1","tags":["somatic","recovery"]},
        {"qt":"forced_choice","text":"Which metaphor best describes your response to setbacks?","opts":[
            {"id":"a","text":"A rubber ball — I bounce back to the same height every time","s":5},
            {"id":"b","text":"A spring — I compress under pressure but return to shape","s":4},
            {"id":"c","text":"Clay — setbacks reshape me permanently","s":2},
            {"id":"d","text":"Glass — I crack under impact and the cracks are permanent","s":1}
        ],"tier":"core","grp":"rs_metaphor_1","tags":["metaphor","resilience_style"]},
        {"qt":"behavioral_recall","text":"After a setback, how quickly do you start taking action toward recovery?","opts":[
            {"id":"a","text":"Almost immediately — action is my natural response to adversity","s":5},
            {"id":"b","text":"Within a few days — after brief processing","s":3},
            {"id":"c","text":"It varies — sometimes quickly, sometimes I get stuck","s":2},
            {"id":"d","text":"Slowly — I tend to ruminate before I can act","s":1}
        ],"tier":"core","grp":"rs_action_speed_1","tags":["action_speed","recovery_behavior"]},
        {"qt":"scenario","text":"You fail at the same thing three times in a row. Different approaches, same result. You:","opts":[
            {"id":"a","text":"Try a fourth time with a radically different approach — the pattern is information, not a verdict","s":5},
            {"id":"b","text":"Seek outside help or a different perspective before trying again","s":3},
            {"id":"c","text":"Accept that this particular thing may not be achievable for you","s":2},
            {"id":"d","text":"Give up — three failures in the same domain is a clear message","s":1}
        ],"tier":"core","grp":"rs_repeated_failure_1","tags":["repeated_failure","persistence"]},
        {"qt":"temporal","text":"What's the most important thing you've learned from failure?","opts":[
            {"id":"a","text":"That failure is essential to growth — I would choose the failures I've had because of what they taught me","s":5},
            {"id":"b","text":"That failure hurts but doesn't define you — recovery is always possible","s":4},
            {"id":"c","text":"That some failures contain genuine signals to change direction","s":2},
            {"id":"d","text":"That I should avoid failure by being more careful and risk-averse","s":1}
        ],"tier":"consistency_check","grp":"rs_lesson_1","tags":["temporal","failure_wisdom"]},
        {"qt":"forced_choice","text":"If someone described you in terms of resilience, they would say:","opts":[
            {"id":"a","text":"'Nothing keeps them down — they're relentless'","s":5},
            {"id":"b","text":"'They handle adversity well — they bend but don't break'","s":4},
            {"id":"c","text":"'They take setbacks hard but eventually come back'","s":2},
            {"id":"d","text":"'They're cautious because past setbacks have made them risk-averse'","s":1}
        ],"tier":"core","grp":"rs_others_view_1","tags":["others_perception","resilience_reputation"]},
    ],
}

for dim, qs in grit_data.items():
    for q in qs:
        entry = {
            "uid": f"GRT-{uid:03d}",
            "assessment_id": "grit",
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

with open("/Users/user/personal/sb/trueassess/priv/question_bank/grit.json", "w") as f:
    json.dump(questions, f, indent=2)

print(f"Wrote {len(questions)} Grit questions")
