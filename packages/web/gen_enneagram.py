import json

questions = []
uid_counter = 1

# Enneagram: 150 questions across type_1 through type_9
# ~17 questions per type (153 total, trim to 150)

type_descriptions = {
    "type_1": {"name": "Reformer", "core": "perfectionism, integrity, responsibility", "fear": "being corrupt/defective", "desire": "to be good/right"},
    "type_2": {"name": "Helper", "core": "generosity, people-pleasing, possessiveness", "fear": "being unwanted", "desire": "to be loved"},
    "type_3": {"name": "Achiever", "core": "ambition, image-consciousness, efficiency", "fear": "being worthless", "desire": "to be valuable"},
    "type_4": {"name": "Individualist", "core": "sensitivity, expressiveness, self-absorption", "fear": "having no identity", "desire": "to be unique"},
    "type_5": {"name": "Investigator", "core": "perception, isolation, knowledge-hoarding", "fear": "being useless/incompetent", "desire": "to be capable"},
    "type_6": {"name": "Loyalist", "core": "loyalty, anxiety, suspicion", "fear": "being without support", "desire": "to have security"},
    "type_7": {"name": "Enthusiast", "core": "spontaneity, versatility, scattered focus", "fear": "being deprived/in pain", "desire": "to be satisfied"},
    "type_8": {"name": "Challenger", "core": "self-confidence, willfulness, confrontation", "fear": "being controlled", "desire": "to protect self"},
    "type_9": {"name": "Peacemaker", "core": "receptivity, complacency, conflict-avoidance", "fear": "loss/fragmentation", "desire": "inner peace"},
}

question_templates_by_type = {
    "type_1": [
        {"qt":"scenario","text":"You notice a colleague consistently cutting corners on quality standards that you believe matter. You:","opts":[
            {"id":"a","text":"Address it directly — standards exist for a reason and should be upheld","s":5},
            {"id":"b","text":"Mention it casually but don't push too hard","s":3},
            {"id":"c","text":"Let it go — everyone has their own approach","s":1},
            {"id":"d","text":"Document the pattern and raise it at the next review","s":4}
        ],"tier":"core","grp":"t1_standards_1","tags":["perfectionism","standards"]},
        {"qt":"behavioral_recall","text":"When you make a mistake at work, which response is closest to yours?","opts":[
            {"id":"a","text":"I replay the mistake repeatedly and think about how I should have done better","s":5},
            {"id":"b","text":"I feel frustrated briefly but move on fairly quickly","s":2},
            {"id":"c","text":"I note it, fix what I can, and don't dwell on it","s":1},
            {"id":"d","text":"I create a system or checklist to make sure it never happens again","s":4}
        ],"tier":"core","grp":"t1_selfcriticism_1","tags":["self-criticism","inner_critic"]},
        {"qt":"forced_choice","text":"Which statement resonates more with how you actually live?","opts":[
            {"id":"a","text":"I have a strong internal sense of right and wrong that guides most of my decisions","s":5},
            {"id":"b","text":"I adapt my moral compass based on the situation and people involved","s":1},
            {"id":"c","text":"I follow the rules that make sense and question the ones that don't","s":3},
            {"id":"d","text":"I focus more on outcomes than on whether the process was 'right'","s":1}
        ],"tier":"core","grp":"t1_morality_1","tags":["moral_compass","integrity"]},
        {"qt":"scenario","text":"A friend asks you to proofread their important email. You find twelve errors. You:","opts":[
            {"id":"a","text":"Fix all twelve — accuracy matters and they asked for help","s":5},
            {"id":"b","text":"Fix the critical ones and mention a few others gently","s":3},
            {"id":"c","text":"Fix the obvious ones and say it looks great","s":1},
            {"id":"d","text":"Rewrite sections that could be more precise while you're at it","s":4}
        ],"tier":"triangulation","grp":"t1_detail_1","tags":["attention_to_detail","helpfulness"]},
        {"qt":"somatic","text":"When you see disorder or messiness in your environment, what happens in your body?","opts":[
            {"id":"a","text":"I feel a physical tension or discomfort that doesn't ease until I tidy up","s":5},
            {"id":"b","text":"Mild irritation — I might straighten a few things","s":3},
            {"id":"c","text":"I barely notice unless it's extreme","s":1},
            {"id":"d","text":"I notice it but can choose to let it go without distress","s":2}
        ],"tier":"core","grp":"t1_order_1","tags":["order","somatic_response"]},
        {"qt":"temporal","text":"Looking back five years, which pattern best describes your relationship with self-improvement?","opts":[
            {"id":"a","text":"I've maintained a steady, sometimes exhausting drive to improve myself","s":5},
            {"id":"b","text":"I go through phases of intense self-improvement followed by relaxation","s":2},
            {"id":"c","text":"I improve when something specific motivates me, not as a constant pursuit","s":1},
            {"id":"d","text":"I've always felt there's a better version of me I should be working toward","s":5}
        ],"tier":"core","grp":"t1_improvement_1","tags":["self_improvement","temporal"]},
        {"qt":"scenario","text":"You're assembling furniture and the instructions are poorly written. You:","opts":[
            {"id":"a","text":"Follow them meticulously anyway — deviating could cause problems","s":4},
            {"id":"b","text":"Improvise based on the pictures, then feel uneasy about whether you did it right","s":5},
            {"id":"c","text":"Wing it — you'll figure it out as you go","s":1},
            {"id":"d","text":"Research the correct method online before proceeding","s":3}
        ],"tier":"triangulation","grp":"t1_correctness_1","tags":["correctness","anxiety"]},
        {"qt":"forced_choice","text":"When someone describes you, which word would you most want them to use?","opts":[
            {"id":"a","text":"Principled","s":5},
            {"id":"b","text":"Caring","s":1},
            {"id":"c","text":"Successful","s":1},
            {"id":"d","text":"Interesting","s":1}
        ],"tier":"trap","grp":"t1_identity_1","tags":["self_image","identity"]},
        {"qt":"behavioral_recall","text":"Think about the last time you were angry. What triggered it?","opts":[
            {"id":"a","text":"Someone acted irresponsibly or unethically","s":5},
            {"id":"b","text":"I wasn't appreciated for my efforts","s":1},
            {"id":"c","text":"I felt out of control of a situation","s":1},
            {"id":"d","text":"Someone was being unfair to others","s":4}
        ],"tier":"core","grp":"t1_anger_1","tags":["anger_triggers","justice"]},
        {"qt":"scenario","text":"You're at a restaurant and your order arrives wrong. The waiter seems stressed. You:","opts":[
            {"id":"a","text":"Politely but firmly send it back — you ordered what you ordered","s":5},
            {"id":"b","text":"Eat it to avoid causing a scene, but feel resentful","s":4},
            {"id":"c","text":"Eat it happily — it's fine, food is food","s":1},
            {"id":"d","text":"Mention it casually in case they want to fix it","s":2}
        ],"tier":"triangulation","grp":"t1_resentment_1","tags":["resentment","suppressed_anger"]},
        {"qt":"somatic","text":"When you're suppressing frustration with someone who isn't meeting your standards, where do you feel it?","opts":[
            {"id":"a","text":"Jaw clenching, tension in my neck and shoulders","s":5},
            {"id":"b","text":"A hot feeling in my chest","s":3},
            {"id":"c","text":"I don't really suppress it — I just say something","s":1},
            {"id":"d","text":"A tightness in my stomach that builds over time","s":4}
        ],"tier":"core","grp":"t1_suppression_1","tags":["somatic","suppressed_frustration"]},
        {"qt":"forced_choice","text":"Which inner experience is most familiar to you?","opts":[
            {"id":"a","text":"A persistent inner voice evaluating whether I'm doing things right","s":5},
            {"id":"b","text":"A pull toward connecting with and helping others","s":1},
            {"id":"c","text":"An awareness of how I'm being perceived by others","s":1},
            {"id":"d","text":"A restless desire for new experiences and stimulation","s":1}
        ],"tier":"core","grp":"t1_innercritic_1","tags":["inner_critic","self_evaluation"]},
        {"qt":"scenario","text":"A group project is going poorly because nobody follows through. You:","opts":[
            {"id":"a","text":"Take over and do it yourself to ensure it's done right","s":5},
            {"id":"b","text":"Create a detailed plan with assigned responsibilities and deadlines","s":4},
            {"id":"c","text":"Express your frustration to the group and see if that motivates change","s":3},
            {"id":"d","text":"Lower your standards for this project and focus your energy elsewhere","s":1}
        ],"tier":"triangulation","grp":"t1_control_1","tags":["control","responsibility"]},
        {"qt":"temporal","text":"How has your relationship with rules and structure changed over your life?","opts":[
            {"id":"a","text":"I've always valued them — they create fairness and order","s":5},
            {"id":"b","text":"I used to be rigid but I've learned to be more flexible","s":3},
            {"id":"c","text":"I've always been more of a rule-questioner than a rule-follower","s":1},
            {"id":"d","text":"Rules matter to me when they're just, but I'll break unjust ones","s":4}
        ],"tier":"consistency_check","grp":"t1_rules_1","tags":["rules","structure","temporal"]},
        {"qt":"behavioral_recall","text":"When you give yourself permission to relax, what typically happens?","opts":[
            {"id":"a","text":"I struggle to actually relax — my mind keeps finding things that need doing","s":5},
            {"id":"b","text":"I can relax but feel guilty about it afterward","s":4},
            {"id":"c","text":"I relax fully and enjoy it without much guilt","s":1},
            {"id":"d","text":"I relax by doing something productive in a different domain","s":3}
        ],"tier":"core","grp":"t1_relaxation_1","tags":["guilt","relaxation","productivity"]},
        {"qt":"scenario","text":"You discover that a rule at your workplace is inefficient and causes unnecessary burden. You:","opts":[
            {"id":"a","text":"Follow it while working through proper channels to change it","s":5},
            {"id":"b","text":"Ignore it quietly — bad rules don't deserve compliance","s":1},
            {"id":"c","text":"Loudly advocate for changing it immediately","s":3},
            {"id":"d","text":"Follow it resentfully while complaining to trusted colleagues","s":4}
        ],"tier":"triangulation","grp":"t1_reform_1","tags":["reform","institutional_change"]},
        {"qt":"forced_choice","text":"Which fear feels most viscerally real to you?","opts":[
            {"id":"a","text":"That I might be fundamentally flawed or corrupt without knowing it","s":5},
            {"id":"b","text":"That people don't actually need me","s":1},
            {"id":"c","text":"That I'm not as competent as I appear","s":1},
            {"id":"d","text":"That life will trap me in boredom or pain","s":1}
        ],"tier":"core","grp":"t1_fear_1","tags":["core_fear","shadow"]},
    ],
    "type_2": [
        {"qt":"scenario","text":"A friend mentions they're overwhelmed with moving to a new apartment. You:","opts":[
            {"id":"a","text":"Immediately offer to help — you know exactly what they need before they ask","s":5},
            {"id":"b","text":"Say 'let me know if you need anything' and mean it","s":3},
            {"id":"c","text":"Sympathize but wait to see if they actually ask for help","s":1},
            {"id":"d","text":"Show up with boxes and supplies without being asked","s":5}
        ],"tier":"core","grp":"t2_helping_1","tags":["helping","anticipating_needs"]},
        {"qt":"behavioral_recall","text":"When was the last time you felt hurt in a relationship? What caused it?","opts":[
            {"id":"a","text":"Someone I'd helped extensively didn't acknowledge or reciprocate my effort","s":5},
            {"id":"b","text":"I was excluded from a group or decision","s":1},
            {"id":"c","text":"Someone criticized my work or competence","s":1},
            {"id":"d","text":"I felt taken for granted after bending over backward for them","s":5}
        ],"tier":"core","grp":"t2_reciprocity_1","tags":["reciprocity","hurt","relationships"]},
        {"qt":"forced_choice","text":"Which describes your deepest relationship pattern?","opts":[
            {"id":"a","text":"I give more than I receive, and I usually notice the imbalance","s":5},
            {"id":"b","text":"I keep relationships fairly balanced through clear communication","s":1},
            {"id":"c","text":"I tend to be more independent and sometimes forget to check in","s":1},
            {"id":"d","text":"I adapt who I am based on what each person seems to need from me","s":4}
        ],"tier":"core","grp":"t2_giving_1","tags":["giving","adaptation","identity"]},
        {"qt":"somatic","text":"When someone you care about pulls away or seems cold, what do you feel physically?","opts":[
            {"id":"a","text":"A sinking feeling in my chest — almost like panic","s":5},
            {"id":"b","text":"Mild discomfort that I can reason through","s":2},
            {"id":"c","text":"Relief, actually — I need the space too","s":1},
            {"id":"d","text":"An urgent drive to reach out and fix whatever went wrong","s":4}
        ],"tier":"core","grp":"t2_rejection_1","tags":["rejection_sensitivity","somatic"]},
        {"qt":"scenario","text":"At a party, you notice someone sitting alone looking uncomfortable. You:","opts":[
            {"id":"a","text":"Go over and make them feel welcome — you can't enjoy yourself while someone is suffering","s":5},
            {"id":"b","text":"Notice them but focus on your own conversations","s":1},
            {"id":"c","text":"Point them out to the host so someone handles it","s":2},
            {"id":"d","text":"Catch their eye and smile, but let them manage their own experience","s":1}
        ],"tier":"triangulation","grp":"t2_rescuing_1","tags":["rescuing","empathy","social"]},
        {"qt":"temporal","text":"How has your need to be needed changed over the years?","opts":[
            {"id":"a","text":"It's been a constant — I feel most alive when someone relies on me","s":5},
            {"id":"b","text":"I've realized it was driving unhealthy patterns and I've pulled back","s":3},
            {"id":"c","text":"I've never felt a strong need to be needed","s":1},
            {"id":"d","text":"It's gotten stronger as I've taken on more caregiving roles","s":4}
        ],"tier":"core","grp":"t2_needed_1","tags":["need_to_be_needed","temporal"]},
        {"qt":"forced_choice","text":"Which statement is hardest for you to say authentically?","opts":[
            {"id":"a","text":"'No, I can't help with that right now'","s":5},
            {"id":"b","text":"'I was wrong about that'","s":1},
            {"id":"c","text":"'I need help'","s":4},
            {"id":"d","text":"'I don't care what you think of me'","s":3}
        ],"tier":"core","grp":"t2_boundaries_1","tags":["boundaries","saying_no"]},
        {"qt":"behavioral_recall","text":"Think about how you feel when you've spent all day helping others. You:","opts":[
            {"id":"a","text":"Feel fulfilled and energized — this is what life is about","s":5},
            {"id":"b","text":"Feel good but also secretly wish someone would take care of YOU","s":5},
            {"id":"c","text":"Feel drained and need time alone to recover","s":1},
            {"id":"d","text":"Feel productive but wonder if you neglected your own priorities","s":2}
        ],"tier":"triangulation","grp":"t2_exhaustion_1","tags":["self_neglect","caretaking"]},
        {"qt":"scenario","text":"You've been helping a colleague extensively with their project. They get a promotion partly due to your help but don't mention you. You:","opts":[
            {"id":"a","text":"Feel deeply hurt but say nothing and maybe pull back emotionally","s":5},
            {"id":"b","text":"Congratulate them genuinely — their success doesn't diminish you","s":1},
            {"id":"c","text":"Tell them directly that you feel your contribution wasn't acknowledged","s":2},
            {"id":"d","text":"Drop subtle hints about how much you helped them","s":4}
        ],"tier":"core","grp":"t2_recognition_1","tags":["recognition","covert_contracts"]},
        {"qt":"somatic","text":"When you say 'no' to someone's request for help, what happens in your body?","opts":[
            {"id":"a","text":"Guilt churns in my stomach — I feel physically uncomfortable until I change my mind","s":5},
            {"id":"b","text":"Brief discomfort that passes quickly","s":2},
            {"id":"c","text":"Nothing particular — no is just a word","s":1},
            {"id":"d","text":"Relief, actually — I'm learning to protect my energy","s":1}
        ],"tier":"core","grp":"t2_guilt_1","tags":["guilt","somatic","boundaries"]},
        {"qt":"scenario","text":"Your partner says they want to handle a difficult situation on their own without your input. You:","opts":[
            {"id":"a","text":"Respect their wish but feel anxious and slightly rejected","s":5},
            {"id":"b","text":"Support their independence wholeheartedly","s":1},
            {"id":"c","text":"Offer help 'just in case' even though they said no","s":5},
            {"id":"d","text":"Feel relieved — one less thing on your plate","s":1}
        ],"tier":"triangulation","grp":"t2_control_1","tags":["control_through_helping","autonomy"]},
        {"qt":"forced_choice","text":"Which fear feels most viscerally real to you?","opts":[
            {"id":"a","text":"That I might be fundamentally flawed or corrupt without knowing it","s":1},
            {"id":"b","text":"That people don't actually need or want me","s":5},
            {"id":"c","text":"That I'm not as competent as I appear","s":1},
            {"id":"d","text":"That I'll be abandoned or alone","s":3}
        ],"tier":"core","grp":"t2_fear_1","tags":["core_fear","shadow"]},
        {"qt":"temporal","text":"Reflecting on your closest relationships, which pattern recurs?","opts":[
            {"id":"a","text":"I become indispensable and then feel trapped by the role","s":5},
            {"id":"b","text":"I maintain healthy boundaries from the start","s":1},
            {"id":"c","text":"I let people come to me rather than pursuing closeness","s":1},
            {"id":"d","text":"I shape-shift to match what each person needs, losing track of my own wants","s":4}
        ],"tier":"core","grp":"t2_pattern_1","tags":["relationship_patterns","identity_loss"]},
        {"qt":"behavioral_recall","text":"When you do something generous, how honest are you about your motives?","opts":[
            {"id":"a","text":"Completely selfless — I genuinely don't expect anything back","s":2},
            {"id":"b","text":"Mostly selfless, but I'd be lying if I said I didn't want appreciation","s":4},
            {"id":"c","text":"I know there's often a hidden expectation but I struggle to admit it","s":5},
            {"id":"d","text":"I'm transactional and honest about it — I help people who help me","s":1}
        ],"tier":"core","grp":"t2_motives_1","tags":["self_honesty","covert_expectations"]},
        {"qt":"scenario","text":"A new acquaintance shares a vulnerability with you. You:","opts":[
            {"id":"a","text":"Feel honored and lean in — this is how real connection happens","s":5},
            {"id":"b","text":"Listen empathetically but maintain some emotional distance","s":1},
            {"id":"c","text":"Feel slightly uncomfortable with the intimacy level","s":1},
            {"id":"d","text":"Immediately share something vulnerable of your own to match their openness","s":4}
        ],"tier":"triangulation","grp":"t2_intimacy_1","tags":["intimacy","emotional_closeness"]},
        {"qt":"forced_choice","text":"When someone describes you, which word would you most want them to use?","opts":[
            {"id":"a","text":"Principled","s":1},
            {"id":"b","text":"Caring","s":5},
            {"id":"c","text":"Successful","s":1},
            {"id":"d","text":"Interesting","s":1}
        ],"tier":"trap","grp":"t2_identity_1","tags":["self_image","identity"]},
        {"qt":"scenario","text":"You realize you've been over-functioning in a friendship — doing emotional labor the other person never asked for. You:","opts":[
            {"id":"a","text":"Pull back dramatically and wait to see if they notice","s":5},
            {"id":"b","text":"Have an honest conversation about the dynamic","s":2},
            {"id":"c","text":"Continue as before — this is just who you are","s":4},
            {"id":"d","text":"Gradually redirect your energy without making it a thing","s":2}
        ],"tier":"core","grp":"t2_overfunction_1","tags":["over_functioning","withdrawal"]},
    ],
    "type_3": [
        {"qt":"scenario","text":"You're at a networking event and someone asks what you do. You:","opts":[
            {"id":"a","text":"Lead with your most impressive accomplishment or title","s":5},
            {"id":"b","text":"Give a straightforward answer without embellishment","s":1},
            {"id":"c","text":"Tailor your answer to what will impress this specific person","s":5},
            {"id":"d","text":"Deflect and ask about them instead","s":1}
        ],"tier":"core","grp":"t3_image_1","tags":["image_management","self_presentation"]},
        {"qt":"behavioral_recall","text":"When you achieve a major goal, what's your immediate internal experience?","opts":[
            {"id":"a","text":"Brief satisfaction, then immediately thinking about the next goal","s":5},
            {"id":"b","text":"Deep contentment that lasts for days or weeks","s":1},
            {"id":"c","text":"Relief that I didn't fail more than joy that I succeeded","s":3},
            {"id":"d","text":"Excitement about sharing the news with people","s":3}
        ],"tier":"core","grp":"t3_achievement_1","tags":["achievement","hedonic_treadmill"]},
        {"qt":"forced_choice","text":"Which internal experience is most familiar?","opts":[
            {"id":"a","text":"Constantly adjusting my presentation to match what each audience values","s":5},
            {"id":"b","text":"Worrying about whether I'm doing the right thing morally","s":1},
            {"id":"c","text":"Anticipating what others need from me emotionally","s":1},
            {"id":"d","text":"Feeling different from everyone around me","s":1}
        ],"tier":"core","grp":"t3_adaptation_1","tags":["chameleon","persona"]},
        {"qt":"somatic","text":"When you experience a public failure — say, a presentation that bombs — what happens in your body?","opts":[
            {"id":"a","text":"Full-body shame flush — heat, nausea, wanting to disappear","s":5},
            {"id":"b","text":"Frustration that shows up as tension but passes quickly","s":2},
            {"id":"c","text":"Not much — failure is just data about what to do differently","s":1},
            {"id":"d","text":"Immediate drive to recover — energy surges to 'fix' the perception","s":4}
        ],"tier":"core","grp":"t3_failure_1","tags":["shame","failure","somatic"]},
        {"qt":"scenario","text":"Your partner says: 'I love you for who you are, not what you accomplish.' You:","opts":[
            {"id":"a","text":"Feel warmth but also subtle discomfort — who am I without accomplishments?","s":5},
            {"id":"b","text":"Feel genuinely reassured and grounded","s":1},
            {"id":"c","text":"Intellectually appreciate it but don't quite believe it","s":4},
            {"id":"d","text":"Feel confused — accomplishments ARE who you are","s":5}
        ],"tier":"core","grp":"t3_identity_1","tags":["identity","worth_achievement"]},
        {"qt":"temporal","text":"How has your relationship with success and image changed over the years?","opts":[
            {"id":"a","text":"I've always been driven to achieve and be seen as successful","s":5},
            {"id":"b","text":"I used to chase status but now I care more about authenticity","s":2},
            {"id":"c","text":"Success never defined me — I value other things more","s":1},
            {"id":"d","text":"The drive has gotten more sophisticated — I achieve in ways that look effortless now","s":5}
        ],"tier":"core","grp":"t3_evolution_1","tags":["temporal","image_evolution"]},
        {"qt":"forced_choice","text":"Which fear feels most viscerally real to you?","opts":[
            {"id":"a","text":"That underneath my accomplishments, I'm actually worthless","s":5},
            {"id":"b","text":"That people will see through my image to something defective","s":4},
            {"id":"c","text":"That I'll be trapped in a meaningless routine","s":1},
            {"id":"d","text":"That someone will control or overpower me","s":1}
        ],"tier":"core","grp":"t3_fear_1","tags":["core_fear","shadow"]},
        {"qt":"behavioral_recall","text":"How do you typically respond to constructive criticism?","opts":[
            {"id":"a","text":"Accept it gracefully outwardly but burn with shame inwardly","s":5},
            {"id":"b","text":"Genuinely appreciate it as a growth opportunity","s":1},
            {"id":"c","text":"Evaluate whether the person is qualified to criticize me","s":4},
            {"id":"d","text":"Feel defensive but try to extract what's useful","s":2}
        ],"tier":"triangulation","grp":"t3_criticism_1","tags":["criticism","shame","image"]},
        {"qt":"scenario","text":"You're working on a team project and realize your approach isn't working. The team will know. You:","opts":[
            {"id":"a","text":"Pivot quickly and present the new direction as if it was always the plan","s":5},
            {"id":"b","text":"Openly admit the approach isn't working and collaborate on a new one","s":1},
            {"id":"c","text":"Work extra hours privately to fix it before anyone notices","s":4},
            {"id":"d","text":"Blame external factors for the setback","s":3}
        ],"tier":"core","grp":"t3_transparency_1","tags":["transparency","covering_failure"]},
        {"qt":"somatic","text":"When you have an unproductive day where you accomplished nothing visible, what do you feel?","opts":[
            {"id":"a","text":"Restless anxiety — almost like I'm wasting my life","s":5},
            {"id":"b","text":"Totally fine — rest is valuable too","s":1},
            {"id":"c","text":"Mild guilt that I could have done more","s":3},
            {"id":"d","text":"Physical discomfort, like I need to move or DO something","s":4}
        ],"tier":"core","grp":"t3_productivity_1","tags":["productivity_anxiety","somatic"]},
        {"qt":"forced_choice","text":"When someone describes you, which word would you most want them to use?","opts":[
            {"id":"a","text":"Principled","s":1},
            {"id":"b","text":"Caring","s":1},
            {"id":"c","text":"Successful","s":5},
            {"id":"d","text":"Interesting","s":1}
        ],"tier":"trap","grp":"t3_selfimage_1","tags":["self_image","identity"]},
        {"qt":"scenario","text":"At a social gathering, someone tells a more impressive version of a story you were about to share. You:","opts":[
            {"id":"a","text":"Feel competitive and either one-up them or change the subject","s":5},
            {"id":"b","text":"Enjoy their story and share yours anyway","s":1},
            {"id":"c","text":"Hold back your story — it won't land as well now by comparison","s":4},
            {"id":"d","text":"Barely notice — you weren't tracking the social dynamics that closely","s":1}
        ],"tier":"triangulation","grp":"t3_competition_1","tags":["competition","social_comparison"]},
        {"qt":"behavioral_recall","text":"How do you select which parts of your life to share on social media?","opts":[
            {"id":"a","text":"I curate carefully — my online presence should reflect my best self","s":5},
            {"id":"b","text":"I share authentically, including struggles and imperfections","s":1},
            {"id":"c","text":"I rarely post — my self-worth isn't tied to public perception","s":1},
            {"id":"d","text":"I post achievements and milestones — they're worth celebrating","s":4}
        ],"tier":"triangulation","grp":"t3_curation_1","tags":["social_media","image_curation"]},
        {"qt":"scenario","text":"Your mentor tells you that your greatest weakness is inauthenticity — that you perform roles instead of being real. You:","opts":[
            {"id":"a","text":"Feel devastated — this hits too close to home","s":5},
            {"id":"b","text":"Disagree — you ARE the roles you play","s":4},
            {"id":"c","text":"Consider it thoughtfully without strong emotional reaction","s":1},
            {"id":"d","text":"Ask for specific examples so you can 'fix' it","s":3}
        ],"tier":"core","grp":"t3_authenticity_1","tags":["authenticity","feedback"]},
        {"qt":"temporal","text":"When you imagine your ideal future, what does it center on?","opts":[
            {"id":"a","text":"Recognition and respect for my achievements in my field","s":5},
            {"id":"b","text":"Deep, authentic relationships with people who truly know me","s":1},
            {"id":"c","text":"Inner peace and freedom from the need to prove myself","s":2},
            {"id":"d","text":"Mastery of something that matters to me, regardless of recognition","s":1}
        ],"tier":"core","grp":"t3_future_1","tags":["vision","motivation"]},
        {"qt":"forced_choice","text":"Which describes your relationship with emotions?","opts":[
            {"id":"a","text":"I can turn emotions on and off strategically — they don't run me","s":5},
            {"id":"b","text":"My emotions are intense and I embrace their full range","s":1},
            {"id":"c","text":"I process emotions carefully and try to learn from them","s":1},
            {"id":"d","text":"Emotions are data — useful but not something I indulge in","s":3}
        ],"tier":"core","grp":"t3_emotions_1","tags":["emotional_suppression","efficiency"]},
        {"qt":"behavioral_recall","text":"What happens when you have no goals or projects to pursue?","opts":[
            {"id":"a","text":"I feel lost — my identity depends on having something to strive for","s":5},
            {"id":"b","text":"I enjoy the break and find fulfillment in simply being","s":1},
            {"id":"c","text":"I quickly create new goals — the emptiness is uncomfortable","s":5},
            {"id":"d","text":"I use the time for reflection and connecting with others","s":1}
        ],"tier":"core","grp":"t3_emptiness_1","tags":["identity_emptiness","goal_dependency"]},
    ],
    "type_4": [
        {"qt":"scenario","text":"You're at a gathering where everyone seems cheerful and connected. You feel:","opts":[
            {"id":"a","text":"An aching sense that something essential is missing — you don't quite belong","s":5},
            {"id":"b","text":"Happy to be included and energized by the group","s":1},
            {"id":"c","text":"Comfortable enough, though you'd prefer a deeper one-on-one conversation","s":3},
            {"id":"d","text":"Envious of how easily others seem to connect","s":4}
        ],"tier":"core","grp":"t4_belonging_1","tags":["belonging","alienation"]},
        {"qt":"behavioral_recall","text":"When you experience intense sadness or melancholy, you tend to:","opts":[
            {"id":"a","text":"Immerse yourself in it — listen to sad music, journal, create something","s":5},
            {"id":"b","text":"Try to distract yourself and move on quickly","s":1},
            {"id":"c","text":"Analyze why you feel this way and develop a plan to feel better","s":1},
            {"id":"d","text":"Share it with someone close and process it together","s":2}
        ],"tier":"core","grp":"t4_melancholy_1","tags":["melancholy","emotional_immersion"]},
        {"qt":"forced_choice","text":"Which describes your core experience of identity?","opts":[
            {"id":"a","text":"I'm fundamentally different from others — no one quite gets me","s":5},
            {"id":"b","text":"I fit in well and feel similar to people around me","s":1},
            {"id":"c","text":"I adapt myself to fit different contexts","s":1},
            {"id":"d","text":"I have a stable sense of who I am that doesn't depend on being different","s":1}
        ],"tier":"core","grp":"t4_uniqueness_1","tags":["uniqueness","identity","differentiation"]},
        {"qt":"somatic","text":"When you see someone living the life you wish you had — the creative freedom, the deep love, the authentic expression — what happens in your body?","opts":[
            {"id":"a","text":"A physical ache in my chest — longing mixed with envy","s":5},
            {"id":"b","text":"Inspiration — I feel motivated to pursue my own version","s":2},
            {"id":"c","text":"Nothing strong — everyone's path is different","s":1},
            {"id":"d","text":"Bitterness that sits in my throat — why do they get what I can't have?","s":4}
        ],"tier":"core","grp":"t4_envy_1","tags":["envy","longing","somatic"]},
        {"qt":"scenario","text":"You create something you feel is deeply personal and authentic. The reaction from others is polite but lukewarm. You:","opts":[
            {"id":"a","text":"Feel devastated — they didn't see what makes it special","s":5},
            {"id":"b","text":"Shrug it off — you made it for yourself, not for them","s":2},
            {"id":"c","text":"Decide your work must not be good enough and feel ashamed","s":3},
            {"id":"d","text":"Withdraw the work — if they can't appreciate it, they don't deserve access","s":4}
        ],"tier":"core","grp":"t4_expression_1","tags":["creative_expression","rejection"]},
        {"qt":"temporal","text":"How has your relationship with your emotions changed over the years?","opts":[
            {"id":"a","text":"My emotional intensity has always been my defining characteristic","s":5},
            {"id":"b","text":"I've learned to regulate better but still feel things very deeply","s":3},
            {"id":"c","text":"I was more emotional when younger but have become more balanced","s":1},
            {"id":"d","text":"I've always been fairly even-keeled","s":1}
        ],"tier":"core","grp":"t4_intensity_1","tags":["emotional_intensity","temporal"]},
        {"qt":"forced_choice","text":"Which fear feels most viscerally real to you?","opts":[
            {"id":"a","text":"That I have no unique identity — that I'm ordinary and forgettable","s":5},
            {"id":"b","text":"That people will see through my accomplishments to worthlessness","s":1},
            {"id":"c","text":"That I'll be abandoned by those I depend on","s":1},
            {"id":"d","text":"That I'm fundamentally flawed in ways I can't fix","s":3}
        ],"tier":"core","grp":"t4_fear_1","tags":["core_fear","identity_crisis"]},
        {"qt":"behavioral_recall","text":"How do you relate to 'ordinary' life — daily routines, mundane tasks, small talk?","opts":[
            {"id":"a","text":"I find them suffocating — I need depth, beauty, and meaning","s":5},
            {"id":"b","text":"I find comfort and grounding in routine","s":1},
            {"id":"c","text":"I tolerate them as necessary but try to minimize them","s":3},
            {"id":"d","text":"I actually enjoy the simple things and find meaning in them","s":1}
        ],"tier":"triangulation","grp":"t4_mundane_1","tags":["mundane_avoidance","meaning_seeking"]},
        {"qt":"scenario","text":"In a relationship, your partner suggests you're 'too much' emotionally. You:","opts":[
            {"id":"a","text":"Feel confirmed in your fear that you're too intense for anyone to truly love","s":5},
            {"id":"b","text":"Consider their perspective and try to modulate","s":2},
            {"id":"c","text":"Push back — your depth is a feature, not a flaw","s":4},
            {"id":"d","text":"Create emotional distance as a protective measure","s":3}
        ],"tier":"core","grp":"t4_toomuch_1","tags":["emotional_intensity","relationships"]},
        {"qt":"somatic","text":"When you feel misunderstood by someone important to you, where does it land in your body?","opts":[
            {"id":"a","text":"A hollow feeling in my chest — like something essential was missed","s":5},
            {"id":"b","text":"Frustration in my jaw and shoulders","s":2},
            {"id":"c","text":"It doesn't really register physically — I just think about it","s":1},
            {"id":"d","text":"Tears come easily — the disconnection hits me fast","s":4}
        ],"tier":"core","grp":"t4_misunderstood_1","tags":["somatic","misunderstanding"]},
        {"qt":"forced_choice","text":"When someone describes you, which word would you most want them to use?","opts":[
            {"id":"a","text":"Principled","s":1},
            {"id":"b","text":"Caring","s":1},
            {"id":"c","text":"Successful","s":1},
            {"id":"d","text":"Interesting","s":5}
        ],"tier":"trap","grp":"t4_selfimage_1","tags":["self_image","identity"]},
        {"qt":"scenario","text":"You discover that someone you admire has the exact creative vision you've been developing. You:","opts":[
            {"id":"a","text":"Feel crushed — your uniqueness was an illusion","s":5},
            {"id":"b","text":"Feel validated — great minds think alike","s":1},
            {"id":"c","text":"Feel competitive — you need to differentiate further","s":4},
            {"id":"d","text":"Reach out to collaborate — shared vision could amplify both","s":1}
        ],"tier":"triangulation","grp":"t4_originality_1","tags":["originality","uniqueness_threat"]},
        {"qt":"behavioral_recall","text":"When others share positive emotions — celebration, excitement, joy — how do you typically engage?","opts":[
            {"id":"a","text":"I join in if I feel it's authentic, but forced positivity repels me","s":5},
            {"id":"b","text":"I'm usually the one generating the positive energy","s":1},
            {"id":"c","text":"I participate but sometimes feel like I'm performing","s":3},
            {"id":"d","text":"I often feel detached from group celebration — my emotional rhythm is different","s":4}
        ],"tier":"core","grp":"t4_joy_1","tags":["joy_difficulty","emotional_rhythm"]},
        {"qt":"temporal","text":"Think about a time you pushed someone away who was getting close to you. What drove that?","opts":[
            {"id":"a","text":"They were getting too close to seeing the real me, and the real me might not be enough","s":5},
            {"id":"b","text":"I need a lot of alone time and they were overwhelming my space","s":2},
            {"id":"c","text":"I tested them to see if they'd fight to stay — and they didn't","s":5},
            {"id":"d","text":"I rarely push people away — I usually try to pull them closer","s":1}
        ],"tier":"core","grp":"t4_pushpull_1","tags":["push_pull","sabotage","testing"]},
        {"qt":"scenario","text":"You're given the opportunity to live a comfortable, stable, but utterly conventional life. No hardship, but no depth either. You:","opts":[
            {"id":"a","text":"Would rather suffer meaningfully than live comfortably without depth","s":5},
            {"id":"b","text":"Would take the comfort — stability has its own kind of beauty","s":1},
            {"id":"c","text":"Would try to find depth within the conventional structure","s":2},
            {"id":"d","text":"Reject the false dichotomy — you can have both","s":1}
        ],"tier":"core","grp":"t4_depth_vs_comfort_1","tags":["depth_seeking","suffering_meaning"]},
        {"qt":"forced_choice","text":"Which inner experience is most constant for you?","opts":[
            {"id":"a","text":"A sense of longing for something I can never quite name or reach","s":5},
            {"id":"b","text":"A drive to help and connect with others","s":1},
            {"id":"c","text":"A desire to understand how things work","s":1},
            {"id":"d","text":"An appetite for new experiences and possibilities","s":1}
        ],"tier":"core","grp":"t4_longing_1","tags":["longing","existential"]},
        {"qt":"behavioral_recall","text":"How do you use aesthetic choices (clothing, home decor, music taste) in your life?","opts":[
            {"id":"a","text":"They're essential expressions of my inner world — deeply personal and curated","s":5},
            {"id":"b","text":"I like nice things but don't invest them with deep meaning","s":1},
            {"id":"c","text":"Practically — functional and appropriate for the context","s":1},
            {"id":"d","text":"As a way to stand out and be noticed for my taste","s":3}
        ],"tier":"triangulation","grp":"t4_aesthetic_1","tags":["aesthetics","self_expression"]},
    ],
    "type_5": [
        {"qt":"scenario","text":"You arrive at a social event and realize it will be three hours of mingling with strangers. You:","opts":[
            {"id":"a","text":"Feel your energy draining already — calculate the minimum acceptable stay time","s":5},
            {"id":"b","text":"Look forward to meeting new people and hearing their stories","s":1},
            {"id":"c","text":"Find one interesting person to have a deep conversation with","s":4},
            {"id":"d","text":"Settle in comfortably — social events are enjoyable background noise","s":1}
        ],"tier":"core","grp":"t5_withdrawal_1","tags":["social_withdrawal","energy_conservation"]},
        {"qt":"behavioral_recall","text":"When someone makes an emotional demand on you — 'I need you to be more present/available' — your instinct is:","opts":[
            {"id":"a","text":"To retreat further — the demand itself is draining","s":5},
            {"id":"b","text":"To lean in and try to meet their need","s":1},
            {"id":"c","text":"To analyze what they actually need versus what they're asking for","s":4},
            {"id":"d","text":"To feel guilty and try harder","s":1}
        ],"tier":"core","grp":"t5_demands_1","tags":["emotional_demands","retreat"]},
        {"qt":"forced_choice","text":"Which describes your core relationship with knowledge?","opts":[
            {"id":"a","text":"I accumulate knowledge as a way of feeling prepared for a world that feels overwhelming","s":5},
            {"id":"b","text":"I learn what I need for practical purposes","s":1},
            {"id":"c","text":"Knowledge is interesting but connecting with people matters more","s":1},
            {"id":"d","text":"I enjoy learning broadly — it's fun, not a survival strategy","s":2}
        ],"tier":"core","grp":"t5_knowledge_1","tags":["knowledge_hoarding","competency"]},
        {"qt":"somatic","text":"When your personal space is invaded — someone drops by unannounced, or a coworker sits too close — what happens?","opts":[
            {"id":"a","text":"I feel physically constricted — like the walls are closing in","s":5},
            {"id":"b","text":"Mild annoyance that I manage easily","s":2},
            {"id":"c","text":"I welcome the company — spontaneous visits are nice","s":1},
            {"id":"d","text":"I freeze internally and wait for it to be over","s":4}
        ],"tier":"core","grp":"t5_space_1","tags":["personal_space","somatic"]},
        {"qt":"scenario","text":"You've spent the weekend deeply absorbed in a complex subject. Monday arrives with meetings and social obligations. You:","opts":[
            {"id":"a","text":"Feel dragged from a rich inner world into a shallow outer one","s":5},
            {"id":"b","text":"Shift gears easily — work is engaging in a different way","s":1},
            {"id":"c","text":"Look forward to sharing what you learned with colleagues","s":1},
            {"id":"d","text":"Resent the interruption but comply with obligations","s":4}
        ],"tier":"core","grp":"t5_innerouter_1","tags":["inner_world","obligation_resentment"]},
        {"qt":"temporal","text":"How has your need for solitude and privacy changed over the years?","opts":[
            {"id":"a","text":"It's been a constant — I've always needed significant alone time to function","s":5},
            {"id":"b","text":"I used to need more alone time but I've become more social","s":2},
            {"id":"c","text":"I've always been fairly social and comfortable with others","s":1},
            {"id":"d","text":"My need for solitude has increased as life has become more demanding","s":3}
        ],"tier":"core","grp":"t5_solitude_1","tags":["solitude","temporal"]},
        {"qt":"forced_choice","text":"Which fear feels most viscerally real to you?","opts":[
            {"id":"a","text":"That I'm incompetent — unable to master what I need to handle the world","s":5},
            {"id":"b","text":"That the world will overwhelm and deplete me","s":4},
            {"id":"c","text":"That I'll be abandoned by those I depend on","s":1},
            {"id":"d","text":"That I'll miss out on life's experiences","s":1}
        ],"tier":"core","grp":"t5_fear_1","tags":["core_fear","shadow"]},
        {"qt":"behavioral_recall","text":"In conversations, you tend to:","opts":[
            {"id":"a","text":"Observe more than participate — speak only when you have something precise to say","s":5},
            {"id":"b","text":"Engage actively — conversation is how you think","s":1},
            {"id":"c","text":"Listen intently and ask probing questions","s":3},
            {"id":"d","text":"Match the energy of whoever you're with","s":1}
        ],"tier":"triangulation","grp":"t5_communication_1","tags":["communication","observation"]},
        {"qt":"scenario","text":"A close friend asks you to explain how you're feeling about a difficult situation. You:","opts":[
            {"id":"a","text":"Struggle to articulate emotions in real-time — you need to process alone first","s":5},
            {"id":"b","text":"Share openly and appreciate the invitation to talk","s":1},
            {"id":"c","text":"Offer a measured, intellectual analysis of your situation instead","s":4},
            {"id":"d","text":"Deflect with humor or change the subject","s":3}
        ],"tier":"core","grp":"t5_emotional_access_1","tags":["emotional_detachment","processing"]},
        {"qt":"somatic","text":"When you feel overwhelmed by too many social obligations, where does it show up physically?","opts":[
            {"id":"a","text":"Complete exhaustion — like someone pulled my plug","s":5},
            {"id":"b","text":"Headache and mental fog","s":4},
            {"id":"c","text":"Restlessness — I need to move and burn off the energy","s":1},
            {"id":"d","text":"I don't really get overwhelmed by social obligations","s":1}
        ],"tier":"core","grp":"t5_depletion_1","tags":["somatic","energy_depletion"]},
        {"qt":"scenario","text":"You have expertise in a subject and someone at a dinner party is confidently wrong about it. You:","opts":[
            {"id":"a","text":"Correct them precisely — accuracy matters","s":4},
            {"id":"b","text":"Stay silent — it's not worth the social friction","s":5},
            {"id":"c","text":"Gently offer an alternative perspective","s":2},
            {"id":"d","text":"Let it go — being right isn't that important to you","s":1}
        ],"tier":"triangulation","grp":"t5_expertise_1","tags":["expertise","social_friction"]},
        {"qt":"forced_choice","text":"Which describes your ideal relationship dynamic?","opts":[
            {"id":"a","text":"Comfortable parallel existence — together but with abundant personal space","s":5},
            {"id":"b","text":"Deeply intertwined — sharing everything, always connected","s":1},
            {"id":"c","text":"Active and social — doing things together in the world","s":1},
            {"id":"d","text":"Intellectually stimulating — ideas and discussion are the bond","s":4}
        ],"tier":"core","grp":"t5_relationship_1","tags":["relationship_style","independence"]},
        {"qt":"behavioral_recall","text":"When you need to make a decision with incomplete information, you:","opts":[
            {"id":"a","text":"Delay until you've gathered enough information to feel confident","s":5},
            {"id":"b","text":"Make the best decision with what you have and adjust later","s":1},
            {"id":"c","text":"Go with your gut — overthinking leads nowhere","s":1},
            {"id":"d","text":"Create a framework to evaluate what you do know systematically","s":4}
        ],"tier":"triangulation","grp":"t5_decisions_1","tags":["decision_making","information_gathering"]},
        {"qt":"temporal","text":"Looking at your life trajectory, which resource have you been most protective of?","opts":[
            {"id":"a","text":"My time and energy — I guard them fiercely","s":5},
            {"id":"b","text":"My relationships — I invest heavily in keeping them strong","s":1},
            {"id":"c","text":"My reputation — I manage how I'm perceived","s":1},
            {"id":"d","text":"My independence — I resist anything that constrains my freedom","s":3}
        ],"tier":"core","grp":"t5_resources_1","tags":["resource_guarding","energy_protection"]},
        {"qt":"scenario","text":"You're going through a major life transition (job change, breakup, move). Your approach is:","opts":[
            {"id":"a","text":"Retreat inward to process — you need substantial alone time to reorganize","s":5},
            {"id":"b","text":"Reach out to your support network and talk through it","s":1},
            {"id":"c","text":"Research and plan meticulously — control what you can","s":4},
            {"id":"d","text":"Stay busy and active to avoid dwelling on the change","s":1}
        ],"tier":"core","grp":"t5_transition_1","tags":["transition","coping"]},
        {"qt":"forced_choice","text":"Which best captures your experience of emotions?","opts":[
            {"id":"a","text":"I experience them on a time delay — I feel things deeply but only after the moment has passed","s":5},
            {"id":"b","text":"I feel things intensely in the moment and express them freely","s":1},
            {"id":"c","text":"I experience emotions but contain them — they don't control me","s":3},
            {"id":"d","text":"I sometimes wonder if I feel things as deeply as others seem to","s":4}
        ],"tier":"core","grp":"t5_delayed_emotion_1","tags":["delayed_emotion","emotional_access"]},
        {"qt":"behavioral_recall","text":"How do you typically contribute in group settings?","opts":[
            {"id":"a","text":"I'm the one who synthesizes the discussion and offers the insight everyone missed","s":5},
            {"id":"b","text":"I energize the group and keep momentum going","s":1},
            {"id":"c","text":"I mediate and ensure everyone's voice is heard","s":1},
            {"id":"d","text":"I quietly observe and only speak if I have something essential to add","s":5}
        ],"tier":"triangulation","grp":"t5_groups_1","tags":["group_contribution","observation"]},
    ],
    "type_6": [
        {"qt":"scenario","text":"Your boss announces a major organizational change effective next week. No details yet. You:","opts":[
            {"id":"a","text":"Immediately start thinking through worst-case scenarios and how to prepare","s":5},
            {"id":"b","text":"Feel curious about what's coming — change can bring opportunity","s":1},
            {"id":"c","text":"Wait for details before reacting — no point worrying without information","s":1},
            {"id":"d","text":"Check in with trusted colleagues to get their read on what's happening","s":4}
        ],"tier":"core","grp":"t6_uncertainty_1","tags":["uncertainty","worst_case_thinking"]},
        {"qt":"behavioral_recall","text":"In relationships, which pattern do you recognize most?","opts":[
            {"id":"a","text":"Testing people's loyalty before fully trusting them","s":5},
            {"id":"b","text":"Trusting quickly and sometimes getting burned","s":1},
            {"id":"c","text":"Building trust gradually through consistent mutual experience","s":2},
            {"id":"d","text":"Being suspicious of people's motives even when evidence suggests they're trustworthy","s":5}
        ],"tier":"core","grp":"t6_trust_1","tags":["trust","loyalty_testing"]},
        {"qt":"forced_choice","text":"Which internal experience is most constant for you?","opts":[
            {"id":"a","text":"A background hum of anxiety scanning for what could go wrong","s":5},
            {"id":"b","text":"A desire for excitement and new possibilities","s":1},
            {"id":"c","text":"A focus on what needs to be accomplished today","s":1},
            {"id":"d","text":"An awareness of how others are feeling and what they need","s":1}
        ],"tier":"core","grp":"t6_anxiety_1","tags":["anxiety","vigilance"]},
        {"qt":"somatic","text":"When you don't know what's going to happen — a pending medical result, an ambiguous text from your partner — what do you feel physically?","opts":[
            {"id":"a","text":"Stomach churning, restless energy, can't stop thinking about it","s":5},
            {"id":"b","text":"Mild curiosity mixed with some nervousness","s":2},
            {"id":"c","text":"I can compartmentalize and deal with it when information arrives","s":1},
            {"id":"d","text":"My mind races through every possible scenario until I land on the worst one","s":5}
        ],"tier":"core","grp":"t6_ambiguity_1","tags":["somatic","ambiguity_intolerance"]},
        {"qt":"scenario","text":"A new friend seems almost too good — generous, attentive, says all the right things. You:","opts":[
            {"id":"a","text":"Enjoy the connection while quietly wondering what their angle is","s":5},
            {"id":"b","text":"Appreciate them at face value — some people are just kind","s":1},
            {"id":"c","text":"Appreciate them but test them before getting too close","s":4},
            {"id":"d","text":"Match their energy and dive into the friendship","s":1}
        ],"tier":"core","grp":"t6_suspicion_1","tags":["suspicion","too_good"]},
        {"qt":"temporal","text":"How has your relationship with authority figures changed over the years?","opts":[
            {"id":"a","text":"I've always had an ambivalent relationship — I seek authority guidance but question it too","s":5},
            {"id":"b","text":"I'm comfortable with authority when it's earned","s":2},
            {"id":"c","text":"I generally defer to authority — they usually know best","s":1},
            {"id":"d","text":"I tend to challenge authority instinctively — push back is my default","s":4}
        ],"tier":"core","grp":"t6_authority_1","tags":["authority","ambivalence","temporal"]},
        {"qt":"forced_choice","text":"Which fear feels most viscerally real to you?","opts":[
            {"id":"a","text":"Being without support or guidance when I need it most","s":5},
            {"id":"b","text":"Being trapped in pain or limitation with no way out","s":1},
            {"id":"c","text":"Being worthless or failing to achieve","s":1},
            {"id":"d","text":"Being controlled or overpowered by someone","s":2}
        ],"tier":"core","grp":"t6_fear_1","tags":["core_fear","security"]},
        {"qt":"behavioral_recall","text":"When you're about to make a major decision (career change, big purchase, commitment), you typically:","opts":[
            {"id":"a","text":"Agonize between options, seeking input from multiple trusted sources","s":5},
            {"id":"b","text":"Research thoroughly then commit decisively","s":2},
            {"id":"c","text":"Trust your gut and go for it","s":1},
            {"id":"d","text":"Make the decision then immediately second-guess it","s":5}
        ],"tier":"core","grp":"t6_decision_1","tags":["indecision","doubt"]},
        {"qt":"scenario","text":"You're in a group and someone makes a subtle power play — positioning themselves as the leader without being explicitly chosen. You:","opts":[
            {"id":"a","text":"Notice it immediately and feel wary — who gave them authority?","s":5},
            {"id":"b","text":"Go along with it if they seem competent","s":1},
            {"id":"c","text":"Challenge it openly — leadership should be earned or elected","s":4},
            {"id":"d","text":"Barely notice — group dynamics aren't something you track closely","s":1}
        ],"tier":"triangulation","grp":"t6_power_1","tags":["power_dynamics","vigilance"]},
        {"qt":"somatic","text":"When someone you trust does something unexpected that doesn't fit your model of them, what happens?","opts":[
            {"id":"a","text":"A spike of anxiety — my mental model of them needs urgent revision","s":5},
            {"id":"b","text":"Curiosity — people are complex and surprising","s":1},
            {"id":"c","text":"Suspicion — I start re-evaluating past interactions for signs I missed","s":5},
            {"id":"d","text":"Brief confusion that resolves when I ask them about it","s":2}
        ],"tier":"core","grp":"t6_trust_breach_1","tags":["somatic","trust","model_violation"]},
        {"qt":"scenario","text":"Your workplace announces layoffs are coming but won't say who's affected for two weeks. You:","opts":[
            {"id":"a","text":"Spend the two weeks catastrophizing and preparing for the worst","s":5},
            {"id":"b","text":"Update your resume but otherwise carry on normally","s":2},
            {"id":"c","text":"Talk to every contact you have to get inside information","s":4},
            {"id":"d","text":"Assume you'll be fine and don't worry about it","s":1}
        ],"tier":"triangulation","grp":"t6_preparation_1","tags":["preparation","catastrophizing"]},
        {"qt":"forced_choice","text":"Which describes your relationship with courage?","opts":[
            {"id":"a","text":"I feel fear intensely but act despite it — that IS my courage","s":5},
            {"id":"b","text":"I don't experience a lot of fear, so courage isn't a frequent theme","s":1},
            {"id":"c","text":"I avoid situations that require courage when I can","s":3},
            {"id":"d","text":"I'm brave when it's for others, less so for myself","s":2}
        ],"tier":"core","grp":"t6_courage_1","tags":["courage","phobic_counterphobic"]},
        {"qt":"behavioral_recall","text":"Think about your inner dialogue. Which voice is loudest?","opts":[
            {"id":"a","text":"The voice that asks 'but what if...' and generates scenarios","s":5},
            {"id":"b","text":"The voice that critiques whether I'm doing things right","s":1},
            {"id":"c","text":"The voice that plans what I want to do next","s":1},
            {"id":"d","text":"The voice that processes how I'm feeling","s":1}
        ],"tier":"core","grp":"t6_inner_dialogue_1","tags":["inner_dialogue","what_if"]},
        {"qt":"scenario","text":"A friend group starts forming an inner circle that you're not part of. You:","opts":[
            {"id":"a","text":"Feel anxious and question whether you're being excluded deliberately","s":5},
            {"id":"b","text":"Don't notice or care — you have your own social life","s":1},
            {"id":"c","text":"Seek reassurance from one trusted friend in the group","s":4},
            {"id":"d","text":"Start distancing yourself preemptively — if they don't want you, fine","s":3}
        ],"tier":"triangulation","grp":"t6_exclusion_1","tags":["exclusion_fear","group_belonging"]},
        {"qt":"temporal","text":"Looking at your history of commitments — jobs, relationships, beliefs — what's the pattern?","opts":[
            {"id":"a","text":"I commit deeply once I've thoroughly vetted, and I'm loyal to the end","s":5},
            {"id":"b","text":"I commit and then question, commit and question — it's cyclical","s":5},
            {"id":"c","text":"I avoid committing until I absolutely have to","s":3},
            {"id":"d","text":"I commit easily and move on when something better comes along","s":1}
        ],"tier":"core","grp":"t6_commitment_1","tags":["commitment","loyalty","doubt"]},
        {"qt":"forced_choice","text":"When you imagine worst-case scenarios, what's the purpose?","opts":[
            {"id":"a","text":"If I imagine it, I can prepare for it — preparation reduces danger","s":5},
            {"id":"b","text":"I don't tend to imagine worst cases","s":1},
            {"id":"c","text":"It happens involuntarily — I wish I could stop","s":4},
            {"id":"d","text":"It helps me appreciate what I have by contrast","s":1}
        ],"tier":"core","grp":"t6_worstcase_1","tags":["worst_case","preparation","anxiety"]},
        {"qt":"behavioral_recall","text":"How do you feel about being perceived as 'anxious'?","opts":[
            {"id":"a","text":"Defensive — I'm not anxious, I'm realistic and prepared","s":5},
            {"id":"b","text":"It's accurate and I've made peace with it","s":3},
            {"id":"c","text":"It doesn't apply to me","s":1},
            {"id":"d","text":"It bothers me because I know others see my worry as weakness","s":4}
        ],"tier":"consistency_check","grp":"t6_selfperception_1","tags":["self_perception","anxiety_identity"]},
    ],
    "type_7": [
        {"qt":"scenario","text":"You're stuck in a boring meeting that could have been an email. Your mind:","opts":[
            {"id":"a","text":"Has already wandered to three exciting ideas you want to explore after this","s":5},
            {"id":"b","text":"Stays focused on finding something useful in the content","s":1},
            {"id":"c","text":"Drifts to worrying about your to-do list","s":1},
            {"id":"d","text":"Plans your escape — you calculate when you can leave early","s":4}
        ],"tier":"core","grp":"t7_boredom_1","tags":["boredom_avoidance","mental_escape"]},
        {"qt":"behavioral_recall","text":"When you feel pain — emotional or physical — your instinct is:","opts":[
            {"id":"a","text":"Reframe it positively — there's always a silver lining or a lesson","s":5},
            {"id":"b","text":"Sit with it and feel it fully before processing","s":1},
            {"id":"c","text":"Distract yourself with activity, plans, or something stimulating","s":5},
            {"id":"d","text":"Analyze it to understand what's causing it","s":2}
        ],"tier":"core","grp":"t7_pain_avoidance_1","tags":["pain_avoidance","reframing"]},
        {"qt":"forced_choice","text":"Which describes your relationship with planning and future-orientation?","opts":[
            {"id":"a","text":"I'm always planning the next exciting thing — anticipation is half the fun","s":5},
            {"id":"b","text":"I plan carefully to avoid problems","s":1},
            {"id":"c","text":"I live mostly in the present moment","s":1},
            {"id":"d","text":"I plan but often change plans when something more interesting comes up","s":4}
        ],"tier":"core","grp":"t7_future_1","tags":["future_orientation","planning"]},
        {"qt":"somatic","text":"When someone wants to have a deep, heavy emotional conversation and you can't escape it, what happens in your body?","opts":[
            {"id":"a","text":"Restlessness — I feel physically trapped and my energy wants to bolt","s":5},
            {"id":"b","text":"I settle in — deep conversation is nourishing","s":1},
            {"id":"c","text":"Mild discomfort that I manage by steering the conversation toward solutions","s":4},
            {"id":"d","text":"I lean in with empathy — their pain becomes my focus","s":1}
        ],"tier":"core","grp":"t7_emotional_depth_1","tags":["emotional_avoidance","somatic"]},
        {"qt":"scenario","text":"You've committed to a year-long project. Three months in, a more exciting opportunity appears. You:","opts":[
            {"id":"a","text":"Feel the pull intensely — maybe you can do both? Or maybe the new thing is where you should be?","s":5},
            {"id":"b","text":"Stay committed — you made a promise and you'll see it through","s":1},
            {"id":"c","text":"Evaluate objectively which has better long-term potential","s":2},
            {"id":"d","text":"Start the new thing on the side — you can handle multiple projects","s":4}
        ],"tier":"core","grp":"t7_commitment_1","tags":["commitment_difficulty","shiny_object"]},
        {"qt":"temporal","text":"How has your appetite for new experiences changed over your life?","opts":[
            {"id":"a","text":"It's always been voracious — I want to try everything at least once","s":5},
            {"id":"b","text":"I used to be more adventurous but I've settled into preferences","s":2},
            {"id":"c","text":"I've always preferred depth over breadth in my experiences","s":1},
            {"id":"d","text":"The hunger for novelty has intensified as I've realized how much there is to experience","s":4}
        ],"tier":"core","grp":"t7_novelty_1","tags":["novelty_seeking","temporal"]},
        {"qt":"forced_choice","text":"Which fear feels most viscerally real to you?","opts":[
            {"id":"a","text":"Being trapped in pain, boredom, or deprivation with no way out","s":5},
            {"id":"b","text":"Being incompetent or unable to handle the world","s":1},
            {"id":"c","text":"Being alone and without support","s":1},
            {"id":"d","text":"Having no unique identity","s":1}
        ],"tier":"core","grp":"t7_fear_1","tags":["core_fear","deprivation"]},
        {"qt":"behavioral_recall","text":"When friends describe you, which pattern comes up most?","opts":[
            {"id":"a","text":"Energetic, fun, always has a plan — but hard to pin down","s":5},
            {"id":"b","text":"Reliable, steady, always there when you need them","s":1},
            {"id":"c","text":"Intense, passionate, emotionally deep","s":1},
            {"id":"d","text":"Thoughtful, reserved, insightful when they do speak","s":1}
        ],"tier":"triangulation","grp":"t7_reputation_1","tags":["social_reputation","energy"]},
        {"qt":"scenario","text":"You realize you've been avoiding a difficult feeling for weeks by staying busy. You:","opts":[
            {"id":"a","text":"Add another activity to your schedule — the strategy is working, why stop?","s":5},
            {"id":"b","text":"Force yourself to sit with the feeling — avoidance makes it worse","s":1},
            {"id":"c","text":"Acknowledge it intellectually but don't see the urgency in feeling it","s":4},
            {"id":"d","text":"Talk to someone about it — processing out loud helps","s":2}
        ],"tier":"core","grp":"t7_avoidance_1","tags":["emotional_avoidance","busy_defense"]},
        {"qt":"somatic","text":"When you have nothing planned — a completely empty weekend — what does your body do?","opts":[
            {"id":"a","text":"Agitation builds — I start planning something immediately","s":5},
            {"id":"b","text":"I feel peaceful and enjoy the open space","s":1},
            {"id":"c","text":"A mix — part of me relaxes, part panics about wasting time","s":3},
            {"id":"d","text":"I fill the space with solitary activities — reading, thinking, creating","s":1}
        ],"tier":"core","grp":"t7_emptiness_1","tags":["somatic","empty_time","FOMO"]},
        {"qt":"forced_choice","text":"Which describes your conversational style?","opts":[
            {"id":"a","text":"I jump between topics enthusiastically — making connections others don't see","s":5},
            {"id":"b","text":"I stay focused on one topic until it's thoroughly explored","s":1},
            {"id":"c","text":"I listen more than I talk and choose words carefully","s":1},
            {"id":"d","text":"I steer conversations toward fun, humor, and possibility","s":4}
        ],"tier":"triangulation","grp":"t7_conversation_1","tags":["conversational_style","associations"]},
        {"qt":"scenario","text":"A therapist tells you that your positivity is actually a defense mechanism avoiding deeper pain. You:","opts":[
            {"id":"a","text":"Intellectually agree but feel resistant to changing it — it works","s":5},
            {"id":"b","text":"Take it seriously and commit to doing the deeper work","s":2},
            {"id":"c","text":"Disagree — you're genuinely optimistic, not avoiding anything","s":4},
            {"id":"d","text":"Feel confronted and consider finding a new therapist","s":3}
        ],"tier":"core","grp":"t7_defense_1","tags":["positivity_defense","self_awareness"]},
        {"qt":"behavioral_recall","text":"How do you handle FOMO (fear of missing out)?","opts":[
            {"id":"a","text":"It's a constant companion — I hate choosing because every 'no' closes a door","s":5},
            {"id":"b","text":"I choose what matters most and let the rest go without regret","s":1},
            {"id":"c","text":"I try to fit in as many options as possible, even at the cost of quality","s":4},
            {"id":"d","text":"FOMO doesn't really apply to me — I'm content with my choices","s":1}
        ],"tier":"core","grp":"t7_fomo_1","tags":["FOMO","choice_difficulty"]},
        {"qt":"temporal","text":"Think about your completed vs abandoned projects over your life. The ratio is:","opts":[
            {"id":"a","text":"More abandoned than completed — I'm better at starting than finishing","s":5},
            {"id":"b","text":"Mostly completed — I follow through on commitments","s":1},
            {"id":"c","text":"About even — some things are worth finishing, some aren't","s":2},
            {"id":"d","text":"I don't start things unless I'm confident I'll finish them","s":1}
        ],"tier":"core","grp":"t7_completion_1","tags":["completion","follow_through"]},
        {"qt":"scenario","text":"You're in a long-term relationship. Your partner wants to deepen commitment (move in, merge finances, plan long-term). You:","opts":[
            {"id":"a","text":"Feel excitement mixed with a creeping sense of walls closing in","s":5},
            {"id":"b","text":"Embrace it — deepening commitment feels natural and good","s":1},
            {"id":"c","text":"Negotiate — yes to some things, but you need to maintain independence in others","s":3},
            {"id":"d","text":"Suggest doing something adventurous together instead of talking about logistics","s":4}
        ],"tier":"core","grp":"t7_commitment_rel_1","tags":["commitment","freedom_vs_connection"]},
        {"qt":"forced_choice","text":"What's your relationship with limitation?","opts":[
            {"id":"a","text":"I instinctively resist any form of limitation or constraint","s":5},
            {"id":"b","text":"I accept limitations as part of life and work within them","s":1},
            {"id":"c","text":"I see limitations as challenges to overcome creatively","s":3},
            {"id":"d","text":"I create structure and limitations for myself — they help me focus","s":1}
        ],"tier":"core","grp":"t7_limitation_1","tags":["limitation","freedom","constraint"]},
        {"qt":"behavioral_recall","text":"When you look at your life honestly, what's the biggest cost of your approach?","opts":[
            {"id":"a","text":"Depth — I sample widely but rarely go deep enough","s":5},
            {"id":"b","text":"Nothing — my approach works well for me","s":1},
            {"id":"c","text":"Other people's feelings — I can be unreliable when something better comes along","s":4},
            {"id":"d","text":"Unprocessed pain that eventually catches up with me","s":5}
        ],"tier":"core","grp":"t7_cost_1","tags":["shadow","honest_self_assessment"]},
    ],
    "type_8": [
        {"qt":"scenario","text":"You walk into a room and sense that someone is being manipulated or controlled by another person. You:","opts":[
            {"id":"a","text":"Intervene immediately — you can't tolerate seeing someone being dominated","s":5},
            {"id":"b","text":"Observe but stay out of it — it's not your business","s":1},
            {"id":"c","text":"Note it and address it privately with the person being manipulated","s":2},
            {"id":"d","text":"Confront the manipulator directly and forcefully","s":5}
        ],"tier":"core","grp":"t8_justice_1","tags":["justice","protection","confrontation"]},
        {"qt":"behavioral_recall","text":"When you feel vulnerable — truly exposed emotionally — your instinct is:","opts":[
            {"id":"a","text":"Cover it with strength, anger, or action — vulnerability is dangerous","s":5},
            {"id":"b","text":"Share it with someone I trust deeply","s":1},
            {"id":"c","text":"Retreat until I've processed it privately, then re-emerge strong","s":4},
            {"id":"d","text":"Express it openly — vulnerability is courageous","s":1}
        ],"tier":"core","grp":"t8_vulnerability_1","tags":["vulnerability_avoidance","armor"]},
        {"qt":"forced_choice","text":"Which describes your core experience of power?","opts":[
            {"id":"a","text":"I need to be in control — not for ego, but because I don't trust others to handle things properly","s":5},
            {"id":"b","text":"I'm comfortable with power but don't seek it","s":1},
            {"id":"c","text":"I prefer to influence from behind the scenes rather than hold overt power","s":2},
            {"id":"d","text":"Power dynamics aren't something I think about much","s":1}
        ],"tier":"core","grp":"t8_control_1","tags":["control","power","trust"]},
        {"qt":"somatic","text":"When someone betrays your trust, what happens physically?","opts":[
            {"id":"a","text":"Rage — hot, immediate, physical. My whole body wants to act","s":5},
            {"id":"b","text":"Hurt that settles into sadness","s":1},
            {"id":"c","text":"Cold calculation — I shut off emotion and plan my response","s":4},
            {"id":"d","text":"Anxiety about what this means for my security","s":1}
        ],"tier":"core","grp":"t8_betrayal_1","tags":["somatic","betrayal","rage"]},
        {"qt":"scenario","text":"You're in a meeting and a decision is being made that you strongly disagree with. No one else is speaking up. You:","opts":[
            {"id":"a","text":"Speak up forcefully — someone has to say what everyone is thinking","s":5},
            {"id":"b","text":"Raise your concern diplomatically and see if others agree","s":2},
            {"id":"c","text":"Stay quiet — maybe you're wrong, and it's not worth the conflict","s":1},
            {"id":"d","text":"Push back hard enough that the decision gets reconsidered","s":5}
        ],"tier":"core","grp":"t8_confrontation_1","tags":["confrontation","speaking_up"]},
        {"qt":"temporal","text":"How has your relationship with anger changed over the years?","opts":[
            {"id":"a","text":"Anger has always been my most accessible emotion — it comes fast and strong","s":5},
            {"id":"b","text":"I used to be angrier but I've learned to channel it better","s":3},
            {"id":"c","text":"Anger isn't a big part of my emotional landscape","s":1},
            {"id":"d","text":"I've learned to use anger strategically — it's a tool, not a loss of control","s":4}
        ],"tier":"core","grp":"t8_anger_1","tags":["anger","temporal"]},
        {"qt":"forced_choice","text":"Which fear feels most viscerally real to you?","opts":[
            {"id":"a","text":"Being controlled, manipulated, or made to submit against my will","s":5},
            {"id":"b","text":"Being incompetent or useless","s":1},
            {"id":"c","text":"Being abandoned or without support","s":1},
            {"id":"d","text":"Being ordinary and unremarkable","s":1}
        ],"tier":"core","grp":"t8_fear_1","tags":["core_fear","control"]},
        {"qt":"behavioral_recall","text":"How do people typically experience you in their first interaction?","opts":[
            {"id":"a","text":"Intimidating or intense — they feel my presence immediately","s":5},
            {"id":"b","text":"Warm and engaging — I put people at ease","s":1},
            {"id":"c","text":"Reserved and observant — they don't get much from me initially","s":1},
            {"id":"d","text":"Direct and no-nonsense — they know where they stand with me right away","s":4}
        ],"tier":"triangulation","grp":"t8_first_impression_1","tags":["first_impressions","intensity"]},
        {"qt":"scenario","text":"A close friend comes to you with a problem. They say they just want to vent, not receive advice. You:","opts":[
            {"id":"a","text":"Listen, but it takes real effort not to jump in with solutions","s":4},
            {"id":"b","text":"Listen empathetically — sometimes people just need to be heard","s":1},
            {"id":"c","text":"Tell them what they need to do to fix it anyway — that's how you show love","s":5},
            {"id":"d","text":"Ask pointed questions that lead them to their own solution","s":3}
        ],"tier":"triangulation","grp":"t8_listening_1","tags":["listening","fixing","support_style"]},
        {"qt":"somatic","text":"When you feel controlled — someone imposing rules, limitations, or 'shoulds' on you — what happens?","opts":[
            {"id":"a","text":"Immediate physical pushback — chest puffs out, jaw sets, I resist automatically","s":5},
            {"id":"b","text":"Intellectual evaluation — some rules are reasonable, some aren't","s":1},
            {"id":"c","text":"Quiet resentment that builds over time","s":3},
            {"id":"d","text":"Acceptance if the authority is legitimate","s":1}
        ],"tier":"core","grp":"t8_control_response_1","tags":["somatic","control_resistance"]},
        {"qt":"scenario","text":"You discover that someone you lead has been undermining you behind your back. You:","opts":[
            {"id":"a","text":"Confront them immediately — betrayal demands a direct response","s":5},
            {"id":"b","text":"Gather evidence carefully before acting","s":2},
            {"id":"c","text":"Try to understand their perspective and find a resolution","s":1},
            {"id":"d","text":"Remove them from your sphere of influence — cut your losses","s":4}
        ],"tier":"core","grp":"t8_betrayal_response_1","tags":["betrayal","confrontation","leadership"]},
        {"qt":"forced_choice","text":"Which describes your relationship with softness and tenderness?","opts":[
            {"id":"a","text":"I have deep tenderness but only show it to very few people in very private moments","s":5},
            {"id":"b","text":"I express tenderness freely — it's a natural part of how I connect","s":1},
            {"id":"c","text":"Tenderness feels like weakness and I avoid showing it","s":4},
            {"id":"d","text":"I'm tender with those who earn it through loyalty and strength","s":3}
        ],"tier":"core","grp":"t8_tenderness_1","tags":["tenderness","vulnerability","private_self"]},
        {"qt":"behavioral_recall","text":"Think about the people in your inner circle. What quality binds them?","opts":[
            {"id":"a","text":"Loyalty and strength — they can hold their own and don't fold under pressure","s":5},
            {"id":"b","text":"Warmth and emotional availability","s":1},
            {"id":"c","text":"Intelligence and competence","s":2},
            {"id":"d","text":"Shared interests and values","s":1}
        ],"tier":"triangulation","grp":"t8_inner_circle_1","tags":["relationships","loyalty","strength"]},
        {"qt":"scenario","text":"You realize you've hurt someone important to you through your intensity. They withdraw. You:","opts":[
            {"id":"a","text":"Feel terrible but struggle to find soft words — your apology might come out as explaining why you were right","s":5},
            {"id":"b","text":"Apologize genuinely and give them space","s":1},
            {"id":"c","text":"Pursue them — withdrawal feels like abandonment","s":3},
            {"id":"d","text":"Show remorse through actions rather than words — fix the situation","s":4}
        ],"tier":"core","grp":"t8_repair_1","tags":["repair","apology_difficulty"]},
        {"qt":"temporal","text":"What role has excess played in your life?","opts":[
            {"id":"a","text":"I do everything at full intensity — work, play, fight, love. Moderation feels like half-living","s":5},
            {"id":"b","text":"I've learned balance over the years — excess caused problems I had to reckon with","s":3},
            {"id":"c","text":"I'm naturally moderate — excess doesn't appeal to me","s":1},
            {"id":"d","text":"I go big in specific areas but maintain control overall","s":3}
        ],"tier":"core","grp":"t8_excess_1","tags":["excess","intensity","lust"]},
        {"qt":"forced_choice","text":"Which statement is truest about your leadership style?","opts":[
            {"id":"a","text":"People follow me because they sense I'll protect them and take charge in crisis","s":5},
            {"id":"b","text":"People follow me because I bring people together and build consensus","s":1},
            {"id":"c","text":"I don't seek leadership — I prefer to contribute as an individual","s":1},
            {"id":"d","text":"People follow me because I'm decisive and don't back down","s":4}
        ],"tier":"triangulation","grp":"t8_leadership_1","tags":["leadership","protection"]},
        {"qt":"behavioral_recall","text":"How do you experience injustice — not abstract injustice, but seeing someone being treated unfairly right in front of you?","opts":[
            {"id":"a","text":"Physically — my body activates, blood pressure rises, I'm ready to act","s":5},
            {"id":"b","text":"Emotionally — I feel sad for the person being wronged","s":1},
            {"id":"c","text":"Intellectually — I analyze the power dynamics at play","s":1},
            {"id":"d","text":"I feel rage and an irresistible urge to step in and make it right","s":5}
        ],"tier":"core","grp":"t8_injustice_1","tags":["injustice","somatic","protective_instinct"]},
    ],
    "type_9": [
        {"qt":"scenario","text":"Two friends are having a heated argument and both look to you for support. You:","opts":[
            {"id":"a","text":"See both sides so clearly that you genuinely can't pick one — and you try to bridge them","s":5},
            {"id":"b","text":"Side with whoever is right, even if it creates tension","s":1},
            {"id":"c","text":"Physically want to leave the room — conflict is viscerally uncomfortable","s":4},
            {"id":"d","text":"Support the person who seems most hurt","s":2}
        ],"tier":"core","grp":"t9_conflict_1","tags":["conflict_avoidance","merging"]},
        {"qt":"behavioral_recall","text":"When someone asks 'what do YOU want?' — genuinely wanting your preference — your immediate internal response is:","opts":[
            {"id":"a","text":"Blank — I honestly don't know, or I know but it feels selfish to say","s":5},
            {"id":"b","text":"I know immediately what I want and state it clearly","s":1},
            {"id":"c","text":"I default to 'whatever you want is fine' even when I do have a preference","s":5},
            {"id":"d","text":"I consider what will make them happy and match that","s":3}
        ],"tier":"core","grp":"t9_self_effacement_1","tags":["self_effacement","preferences"]},
        {"qt":"forced_choice","text":"Which internal experience is most constant for you?","opts":[
            {"id":"a","text":"A desire for peace and harmony that runs deeper than any other motivation","s":5},
            {"id":"b","text":"An anxiety about what could go wrong","s":1},
            {"id":"c","text":"A drive toward accomplishment and recognition","s":1},
            {"id":"d","text":"An awareness of what's missing or what could be better","s":1}
        ],"tier":"core","grp":"t9_peace_1","tags":["peace_seeking","harmony"]},
        {"qt":"somatic","text":"When someone directs anger specifically at you, what happens in your body?","opts":[
            {"id":"a","text":"I go numb — like a fog descends and I can't think or respond","s":5},
            {"id":"b","text":"I fire back — anger activates my own anger","s":1},
            {"id":"c","text":"Anxiety — my stomach drops and I feel scared","s":2},
            {"id":"d","text":"I absorb it — I feel their anger in my body as if it were my own","s":4}
        ],"tier":"core","grp":"t9_anger_response_1","tags":["somatic","anger_numbing"]},
        {"qt":"scenario","text":"You've been putting off a major life decision for months. Everyone around you is waiting. You:","opts":[
            {"id":"a","text":"Continue putting it off — the right answer will become clear eventually","s":5},
            {"id":"b","text":"Make the decision — indecision is worse than a wrong choice","s":1},
            {"id":"c","text":"Ask everyone what they think you should do, then feel more confused","s":3},
            {"id":"d","text":"Fill your time with small tasks so the big decision doesn't feel so pressing","s":4}
        ],"tier":"core","grp":"t9_indecision_1","tags":["procrastination","indecision"]},
        {"qt":"temporal","text":"How has your relationship with anger changed over the years?","opts":[
            {"id":"a","text":"I've always had trouble accessing anger — by the time I realize I'm angry, the moment has passed","s":5},
            {"id":"b","text":"I express anger readily when it arises","s":1},
            {"id":"c","text":"I've learned to express anger more, but it still feels deeply unnatural","s":3},
            {"id":"d","text":"My anger comes out sideways — passive resistance, stubbornness, procrastination","s":4}
        ],"tier":"core","grp":"t9_anger_1","tags":["anger_suppression","temporal"]},
        {"qt":"forced_choice","text":"Which fear feels most viscerally real to you?","opts":[
            {"id":"a","text":"Loss — of connection, of peace, of the wholeness that comes from harmony","s":5},
            {"id":"b","text":"Being controlled or dominated against my will","s":1},
            {"id":"c","text":"Being trapped in pain or deprivation","s":1},
            {"id":"d","text":"Being worthless or a failure","s":1}
        ],"tier":"core","grp":"t9_fear_1","tags":["core_fear","fragmentation"]},
        {"qt":"behavioral_recall","text":"How do you experience your own needs versus others' needs?","opts":[
            {"id":"a","text":"Others' needs feel more real and urgent than my own — mine can always wait","s":5},
            {"id":"b","text":"I balance my needs with others' fairly well","s":1},
            {"id":"c","text":"My needs come first — I can't help others if I'm depleted","s":1},
            {"id":"d","text":"I often realize my needs existed only after someone else points them out","s":4}
        ],"tier":"core","grp":"t9_needs_1","tags":["self_forgetting","needs_hierarchy"]},
        {"qt":"scenario","text":"Your partner wants to have a serious conversation about problems in the relationship. You:","opts":[
            {"id":"a","text":"Agree to talk but zone out during the hard parts — you hear their words but can't engage","s":5},
            {"id":"b","text":"Engage fully — difficult conversations strengthen relationships","s":1},
            {"id":"c","text":"Feel dread but participate, hoping to resolve things quickly","s":3},
            {"id":"d","text":"Minimize the problems — 'it's not that bad, we're fine'","s":5}
        ],"tier":"core","grp":"t9_avoidance_1","tags":["conflict_avoidance","numbing"]},
        {"qt":"somatic","text":"When you finally assert yourself strongly after a long period of going along with others, what happens?","opts":[
            {"id":"a","text":"Shaking — my body isn't used to this much activation","s":5},
            {"id":"b","text":"Empowerment — it feels right and energizing","s":1},
            {"id":"c","text":"Guilt immediately follows — I worry I was too harsh","s":4},
            {"id":"d","text":"Surprise at how much anger was stored up — it comes out bigger than expected","s":5}
        ],"tier":"core","grp":"t9_assertion_1","tags":["somatic","assertion","stored_anger"]},
        {"qt":"scenario","text":"You're choosing a restaurant for a group dinner. You have a preference but others are suggesting different places. You:","opts":[
            {"id":"a","text":"Drop your preference immediately — it's not worth the potential friction","s":5},
            {"id":"b","text":"State your preference and let the group decide","s":1},
            {"id":"c","text":"Advocate firmly for your choice — you know it's the best option","s":1},
            {"id":"d","text":"Say 'anywhere is fine with me' even though you just said you had a preference","s":5}
        ],"tier":"triangulation","grp":"t9_preference_1","tags":["preference_suppression","accommodation"]},
        {"qt":"forced_choice","text":"Which describes your relationship with productivity?","opts":[
            {"id":"a","text":"I stay busy with comfortable, familiar tasks to avoid facing bigger priorities","s":5},
            {"id":"b","text":"I'm highly productive and goal-oriented","s":1},
            {"id":"c","text":"I work in bursts of inspiration rather than steady effort","s":1},
            {"id":"d","text":"I sometimes realize I've spent hours on autopilot without accomplishing anything important","s":4}
        ],"tier":"core","grp":"t9_narcotization_1","tags":["narcotization","productive_avoidance"]},
        {"qt":"behavioral_recall","text":"How do people close to you describe your communication style?","opts":[
            {"id":"a","text":"I take forever to get to the point — I give all sides before stating mine","s":5},
            {"id":"b","text":"Direct and clear — people know where I stand","s":1},
            {"id":"c","text":"I say what I think people want to hear","s":3},
            {"id":"d","text":"I communicate easily but avoid touchy subjects","s":4}
        ],"tier":"triangulation","grp":"t9_communication_1","tags":["communication","indirectness"]},
        {"qt":"scenario","text":"You realize you've been living more according to someone else's agenda than your own for the past year. You:","opts":[
            {"id":"a","text":"Feel a familiar recognition — this is a recurring pattern you struggle to break","s":5},
            {"id":"b","text":"Immediately course-correct — your life, your priorities","s":1},
            {"id":"c","text":"Feel confused about what your own agenda even is","s":5},
            {"id":"d","text":"Accept it — supporting others IS your priority","s":3}
        ],"tier":"core","grp":"t9_merging_1","tags":["merging","lost_self"]},
        {"qt":"temporal","text":"Looking at your life, where has your energy actually gone versus where you wanted it to go?","opts":[
            {"id":"a","text":"Most of my energy went to keeping peace and accommodating others — my own goals fell aside","s":5},
            {"id":"b","text":"My energy went exactly where I directed it — toward my goals and priorities","s":1},
            {"id":"c","text":"I'm not sure what my goals were, so it's hard to say","s":4},
            {"id":"d","text":"My energy went to helping others, which IS where I wanted it to go","s":2}
        ],"tier":"core","grp":"t9_energy_1","tags":["energy_direction","self_forgetting"]},
        {"qt":"forced_choice","text":"Which best describes your experience of inner peace?","opts":[
            {"id":"a","text":"I create peace by merging with my environment and minimizing friction — it requires constant effort","s":5},
            {"id":"b","text":"I find peace through accomplishment and being productive","s":1},
            {"id":"c","text":"I find peace through solitude and inner exploration","s":1},
            {"id":"d","text":"True inner peace is rare — I experience a simulated version by staying comfortable","s":4}
        ],"tier":"core","grp":"t9_peace_nature_1","tags":["inner_peace","sloth","simulated_peace"]},
        {"qt":"behavioral_recall","text":"When you DO finally get angry, what surprises people?","opts":[
            {"id":"a","text":"The intensity — they had no idea I was capable of that much force","s":5},
            {"id":"b","text":"I get angry regularly — it doesn't surprise anyone","s":1},
            {"id":"c","text":"The stubbornness — I become an immovable wall","s":4},
            {"id":"d","text":"Nothing — I express frustration proportionally","s":1}
        ],"tier":"core","grp":"t9_anger_surprise_1","tags":["suppressed_anger","eruption"]},
    ],
}

for type_key, type_qs in question_templates_by_type.items():
    for i, q in enumerate(type_qs):
        if uid_counter > 150:
            break
        uid = f"ENN-{uid_counter:03d}"
        entry = {
            "uid": uid,
            "assessment_id": "enneagram",
            "dimension": type_key,
            "question_type": q["qt"],
            "text": q["text"],
            "options": [{"id": o["id"], "text": o["text"], "scores": {type_key: o["s"]}} for o in q["opts"]],
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
        uid_counter += 1
    if uid_counter > 150:
        break

# Ensure exactly 150
questions = questions[:150]

with open("/Users/user/personal/sb/trueassess/priv/question_bank/enneagram.json", "w") as f:
    json.dump(questions, f, indent=2)

print(f"Wrote {len(questions)} enneagram questions")
