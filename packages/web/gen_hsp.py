import json

questions = []
uid = 1

# HSP: 20 questions per dimension = 80
hsp_data = {
    "sensory_sensitivity": [
        {"qt":"scenario","text":"You walk into a restaurant with bright fluorescent lighting, a loud TV, and a heavily scented candle. You:","opts":[
            {"id":"a","text":"Feel immediately overwhelmed — each stimulus stacks and it's physically uncomfortable","s":5},
            {"id":"b","text":"Notice the stimuli but adapt within a few minutes","s":3},
            {"id":"c","text":"Barely register it — environments don't affect you much","s":1},
            {"id":"d","text":"Focus on whichever stimulus bothers you most and try to mitigate it","s":4}
        ],"tier":"core","grp":"ss_multisensory_1","tags":["sensory_overload","environment"]},
        {"qt":"behavioral_recall","text":"How sensitive are you to fabric textures against your skin?","opts":[
            {"id":"a","text":"Very — I've rejected clothing that feels wrong, even if it looks good","s":5},
            {"id":"b","text":"Somewhat — I have preferences but most fabrics are fine","s":3},
            {"id":"c","text":"Not at all — I barely notice fabric texture","s":1},
            {"id":"d","text":"I notice textures but can tolerate most of them","s":2}
        ],"tier":"core","grp":"ss_tactile_1","tags":["tactile_sensitivity","clothing"]},
        {"qt":"somatic","text":"When someone nearby is wearing strong perfume or cologne, you:","opts":[
            {"id":"a","text":"Get a headache or nausea — strong scents are physically distressing","s":5},
            {"id":"b","text":"Notice it and find it mildly unpleasant","s":3},
            {"id":"c","text":"Don't really notice unless it's extreme","s":1},
            {"id":"d","text":"Notice it immediately and may need to move away","s":4}
        ],"tier":"core","grp":"ss_olfactory_1","tags":["somatic","smell_sensitivity"]},
        {"qt":"forced_choice","text":"How do you respond to subtle sounds — a clock ticking, a refrigerator humming, someone chewing?","opts":[
            {"id":"a","text":"They're impossible to ignore — they dominate my awareness until they stop","s":5},
            {"id":"b","text":"I notice them but can tune them out with effort","s":3},
            {"id":"c","text":"I genuinely don't notice background sounds unless they're loud","s":1},
            {"id":"d","text":"Some sounds bother me intensely while others don't register","s":4}
        ],"tier":"core","grp":"ss_auditory_1","tags":["auditory_sensitivity","misophonia"]},
        {"qt":"scenario","text":"You're trying to sleep and there's a faint light coming from under the door. You:","opts":[
            {"id":"a","text":"Can't sleep until it's completely dark — even small light sources disrupt you","s":5},
            {"id":"b","text":"Notice it but fall asleep anyway","s":3},
            {"id":"c","text":"Don't notice — you fall asleep in any conditions","s":1},
            {"id":"d","text":"Get up and block it — you know it'll bother you all night otherwise","s":4}
        ],"tier":"core","grp":"ss_light_1","tags":["light_sensitivity","sleep"]},
        {"qt":"temporal","text":"How has your sensitivity to physical environments changed over the years?","opts":[
            {"id":"a","text":"I've always been highly sensitive — it's a core part of my experience","s":5},
            {"id":"b","text":"I've become more sensitive as I've aged","s":4},
            {"id":"c","text":"I've always been fairly robust — environments don't affect me much","s":1},
            {"id":"d","text":"I've learned to manage it better but the sensitivity hasn't decreased","s":4}
        ],"tier":"core","grp":"ss_temporal_1","tags":["temporal","sensitivity_trajectory"]},
        {"qt":"behavioral_recall","text":"When you eat food, how much do you notice subtle flavors and textures?","opts":[
            {"id":"a","text":"Intensely — I detect ingredients others miss and texture is as important as taste","s":5},
            {"id":"b","text":"More than average — I enjoy food and notice details","s":3},
            {"id":"c","text":"Not particularly — food is fuel and I eat what's available","s":1},
            {"id":"d","text":"I'm very sensitive to unpleasant flavors but don't seek out complex ones","s":3}
        ],"tier":"triangulation","grp":"ss_gustatory_1","tags":["taste_sensitivity","food"]},
        {"qt":"somatic","text":"When you're in a visually cluttered environment — a messy room, a busy street, a crowded store — you:","opts":[
            {"id":"a","text":"Feel cognitive overwhelm — too much visual information makes it hard to think","s":5},
            {"id":"b","text":"Feel slightly distracted but manage fine","s":3},
            {"id":"c","text":"Feel normal — visual clutter doesn't affect my mental state","s":1},
            {"id":"d","text":"Need to look away or close my eyes periodically to reset","s":4}
        ],"tier":"core","grp":"ss_visual_1","tags":["somatic","visual_overwhelm"]},
        {"qt":"forced_choice","text":"How affected are you by temperature changes?","opts":[
            {"id":"a","text":"Very — I notice temperature shifts of a degree or two and they affect my comfort significantly","s":5},
            {"id":"b","text":"Somewhat — I have a preferred range but I'm fairly adaptable","s":3},
            {"id":"c","text":"Barely — temperature doesn't bother me much","s":1},
            {"id":"d","text":"I'm very sensitive to cold but handle heat fine (or vice versa)","s":4}
        ],"tier":"core","grp":"ss_temperature_1","tags":["temperature_sensitivity"]},
        {"qt":"scenario","text":"You've been at a concert for two hours. The music is good but the volume is high, the crowd is dense, and the lights are flashing. You:","opts":[
            {"id":"a","text":"Need to leave — the sensory intensity has become physically unbearable","s":5},
            {"id":"b","text":"Enjoy it despite some discomfort — the music makes it worth it","s":3},
            {"id":"c","text":"Love every second — this is exactly the kind of stimulation you enjoy","s":1},
            {"id":"d","text":"Take breaks — step outside periodically to recover before going back in","s":4}
        ],"tier":"core","grp":"ss_concert_1","tags":["sensory_overwhelm","coping"]},
        {"qt":"behavioral_recall","text":"How sensitive are you to pain compared to people around you?","opts":[
            {"id":"a","text":"Very — I feel pain more intensely than others seem to","s":5},
            {"id":"b","text":"About average","s":3},
            {"id":"c","text":"Less sensitive — I have a high pain tolerance","s":1},
            {"id":"d","text":"My pain threshold varies — some types of pain bother me more than others","s":3}
        ],"tier":"core","grp":"ss_pain_1","tags":["pain_sensitivity"]},
        {"qt":"somatic","text":"After spending time in a noisy, stimulating environment, your body:","opts":[
            {"id":"a","text":"Needs significant recovery time — I feel physically drained and possibly headachy","s":5},
            {"id":"b","text":"Takes a short while to recalibrate — maybe 30 minutes of quiet","s":3},
            {"id":"c","text":"Feels fine — I bounce right back","s":1},
            {"id":"d","text":"Feels wired and overstimulated — like my nervous system is buzzing","s":4}
        ],"tier":"core","grp":"ss_recovery_1","tags":["somatic","recovery_time"]},
        {"qt":"forced_choice","text":"How do you react to violent or graphic images in media?","opts":[
            {"id":"a","text":"Intensely — the images stay with me for days and cause real distress","s":5},
            {"id":"b","text":"Mildly uncomfortable — I don't seek them out but can handle exposure","s":3},
            {"id":"c","text":"Unfazed — they're just images","s":1},
            {"id":"d","text":"I physically flinch or look away — the visual impact is too strong","s":5}
        ],"tier":"core","grp":"ss_graphic_1","tags":["visual_sensitivity","media"]},
        {"qt":"scenario","text":"You're shopping and the store has music playing, employees approaching, multiple checkout beeps, and fluorescent lights. You:","opts":[
            {"id":"a","text":"Feel your anxiety rising with each additional stimulus — you need to leave soon","s":5},
            {"id":"b","text":"Notice the stimuli but shop normally","s":3},
            {"id":"c","text":"Feel comfortable — this is a normal shopping experience","s":1},
            {"id":"d","text":"Use noise-canceling headphones or shop during off-peak hours to manage it","s":4}
        ],"tier":"triangulation","grp":"ss_shopping_1","tags":["sensory_management","daily_life"]},
        {"qt":"behavioral_recall","text":"How often do environmental conditions (noise, lighting, temperature) affect your ability to concentrate?","opts":[
            {"id":"a","text":"Constantly — I need very specific conditions to focus well","s":5},
            {"id":"b","text":"Sometimes — certain conditions are more disruptive than others","s":3},
            {"id":"c","text":"Rarely — I can concentrate in almost any environment","s":1},
            {"id":"d","text":"Frequently — I've built my life around controlling my environment","s":5}
        ],"tier":"core","grp":"ss_concentration_1","tags":["concentration","environmental_impact"]},
        {"qt":"somatic","text":"How do you experience caffeine compared to others?","opts":[
            {"id":"a","text":"Very sensitively — small amounts make me jittery or anxious","s":5},
            {"id":"b","text":"Normally — I enjoy coffee without unusual reactions","s":3},
            {"id":"c","text":"I need large amounts to feel any effect","s":1},
            {"id":"d","text":"I've had to significantly limit caffeine due to sensitivity","s":5}
        ],"tier":"triangulation","grp":"ss_caffeine_1","tags":["somatic","substance_sensitivity"]},
        {"qt":"forced_choice","text":"How would you describe your startle reflex?","opts":[
            {"id":"a","text":"Extreme — I jump easily at unexpected sounds and it takes a while to calm down","s":5},
            {"id":"b","text":"Normal — unexpected sounds startle me briefly","s":3},
            {"id":"c","text":"Mild — I'm hard to startle","s":1},
            {"id":"d","text":"I startle easily but recover quickly","s":3}
        ],"tier":"core","grp":"ss_startle_1","tags":["startle_reflex","nervous_system"]},
        {"qt":"temporal","text":"How have you adapted to your sensory sensitivity over the years?","opts":[
            {"id":"a","text":"I've built extensive environmental controls — specific lighting, sound, materials in my home","s":5},
            {"id":"b","text":"I've learned some coping strategies but still get overwhelmed regularly","s":4},
            {"id":"c","text":"I haven't needed to adapt — sensory input doesn't bother me","s":1},
            {"id":"d","text":"I've found a balance between accommodation and exposure","s":3}
        ],"tier":"consistency_check","grp":"ss_adaptation_1","tags":["temporal","adaptation"]},
        {"qt":"scenario","text":"Someone brushes against you unexpectedly in a crowd. You:","opts":[
            {"id":"a","text":"Feel a jolt — unexpected physical contact is jarring and stays with you","s":5},
            {"id":"b","text":"Notice it briefly and move on","s":3},
            {"id":"c","text":"Don't really register it — it's just a crowd","s":1},
            {"id":"d","text":"Flinch and need a moment to reset your personal space boundary","s":4}
        ],"tier":"core","grp":"ss_touch_1","tags":["touch_sensitivity","personal_space"]},
        {"qt":"behavioral_recall","text":"Have you ever been told you're 'too sensitive' about physical environments?","opts":[
            {"id":"a","text":"Frequently — it's a lifelong theme in how others describe me","s":5},
            {"id":"b","text":"Occasionally — certain sensitivities have been noted","s":3},
            {"id":"c","text":"Never — people don't describe me as physically sensitive","s":1},
            {"id":"d","text":"Yes, but I've learned to advocate for my needs without apology","s":4}
        ],"tier":"consistency_check","grp":"ss_told_sensitive_1","tags":["self_perception","others_perception"]},
    ],
    "emotional_reactivity": [
        {"qt":"scenario","text":"A friend makes a casual critical comment about something you care about. You:","opts":[
            {"id":"a","text":"Feel a surge of emotion that's disproportionate to the comment — it hits deep","s":5},
            {"id":"b","text":"Feel a brief sting and move on","s":3},
            {"id":"c","text":"Don't take it personally — it's just their opinion","s":1},
            {"id":"d","text":"Feel hurt but try to understand their perspective before reacting","s":4}
        ],"tier":"core","grp":"er_criticism_1","tags":["emotional_reactivity","criticism"]},
        {"qt":"behavioral_recall","text":"When you watch a sad movie or hear a moving piece of music, how intense is your response?","opts":[
            {"id":"a","text":"Overwhelming — I may cry, feel drained, or be affected for hours","s":5},
            {"id":"b","text":"Strong — I feel it deeply in the moment but recover quickly","s":3},
            {"id":"c","text":"Mild — I appreciate it intellectually but it doesn't move me much","s":1},
            {"id":"d","text":"Unpredictable — sometimes it hits me hard, sometimes it doesn't","s":3}
        ],"tier":"core","grp":"er_media_1","tags":["emotional_response","media"]},
        {"qt":"forced_choice","text":"How quickly do you transition between emotional states?","opts":[
            {"id":"a","text":"Slowly — emotions linger and one feeling bleeds into the next activity","s":5},
            {"id":"b","text":"Moderately — I need some time but can transition within an hour or so","s":3},
            {"id":"c","text":"Quickly — I can shift emotional gears easily","s":1},
            {"id":"d","text":"It depends entirely on the intensity of the emotion","s":3}
        ],"tier":"core","grp":"er_transitions_1","tags":["emotional_persistence","transitions"]},
        {"qt":"somatic","text":"When you feel an emotion strongly, how does it manifest in your body?","opts":[
            {"id":"a","text":"Full-body — I feel emotions as physical sensations throughout my entire body","s":5},
            {"id":"b","text":"Localized — I feel emotions in specific areas (chest, stomach)","s":3},
            {"id":"c","text":"Minimal physical sensation — emotions are mental experiences for me","s":1},
            {"id":"d","text":"Intense physical sensation that can be hard to distinguish from illness","s":5}
        ],"tier":"core","grp":"er_somatic_1","tags":["somatic","emotional_embodiment"]},
        {"qt":"scenario","text":"You're having a great day when you receive mildly disappointing news (a minor plan cancellation). You:","opts":[
            {"id":"a","text":"Your whole mood shifts — the disappointment colors everything","s":5},
            {"id":"b","text":"Feel disappointed about that specific thing but your overall mood stays positive","s":2},
            {"id":"c","text":"Barely react — minor disappointments don't register emotionally","s":1},
            {"id":"d","text":"Feel a disproportionate wave of sadness that takes effort to shake","s":5}
        ],"tier":"core","grp":"er_mood_1","tags":["mood_reactivity","emotional_lability"]},
        {"qt":"temporal","text":"How has your emotional reactivity changed over the years?","opts":[
            {"id":"a","text":"It's been consistently high — I've always felt things intensely","s":5},
            {"id":"b","text":"I've developed better emotional regulation but the intensity is unchanged","s":4},
            {"id":"c","text":"I've become less reactive as I've matured","s":2},
            {"id":"d","text":"I was never particularly emotionally reactive","s":1}
        ],"tier":"core","grp":"er_temporal_1","tags":["temporal","emotional_development"]},
        {"qt":"forced_choice","text":"Other people's moods affect you:","opts":[
            {"id":"a","text":"Profoundly — I absorb others' emotions and they become mine","s":5},
            {"id":"b","text":"Noticeably — I'm influenced by the emotional atmosphere around me","s":3},
            {"id":"c","text":"Minimally — I maintain my own emotional state regardless of others","s":1},
            {"id":"d","text":"I pick up on moods easily and have to consciously separate my feelings from theirs","s":4}
        ],"tier":"core","grp":"er_contagion_1","tags":["emotional_contagion","empathy"]},
        {"qt":"scenario","text":"You overhear a stranger being cruel to their child in a store. You:","opts":[
            {"id":"a","text":"Feel physically sick — the child's pain registers in your body as if it were happening to you","s":5},
            {"id":"b","text":"Feel angry on the child's behalf and consider intervening","s":3},
            {"id":"c","text":"Notice it and disapprove but don't feel it physically","s":1},
            {"id":"d","text":"Are upset for hours afterward — you can't stop thinking about the child","s":5}
        ],"tier":"core","grp":"er_empathic_distress_1","tags":["empathic_distress","vicarious_emotion"]},
        {"qt":"behavioral_recall","text":"After a conflict with someone important to you, how long does it take to emotionally recover?","opts":[
            {"id":"a","text":"Days — conflict reverberates through my system long after it's resolved","s":5},
            {"id":"b","text":"Hours — I process it and move on the same day","s":3},
            {"id":"c","text":"Minutes — once the issue is addressed, I'm fine","s":1},
            {"id":"d","text":"It depends — small conflicts resolve quickly but significant ones can take weeks","s":3}
        ],"tier":"core","grp":"er_recovery_1","tags":["emotional_recovery","conflict"]},
        {"qt":"somatic","text":"When you're very happy, how does your body express it?","opts":[
            {"id":"a","text":"Intensely — I'm bursting with energy, may tear up with joy, feel electric","s":5},
            {"id":"b","text":"Warmth and smiling — a pleasant physical state","s":3},
            {"id":"c","text":"Subtle — I know I'm happy but it doesn't manifest strongly physically","s":1},
            {"id":"d","text":"Sometimes overwhelming — intense joy can tip into feeling overstimulated","s":5}
        ],"tier":"core","grp":"er_positive_1","tags":["somatic","positive_reactivity"]},
        {"qt":"forced_choice","text":"How easily do you cry?","opts":[
            {"id":"a","text":"Very easily — music, kindness, beauty, sadness, frustration all bring tears","s":5},
            {"id":"b","text":"Sometimes — significant emotional events bring tears","s":3},
            {"id":"c","text":"Rarely — I don't cry easily","s":1},
            {"id":"d","text":"Easily, and it sometimes surprises me how little it takes","s":4}
        ],"tier":"core","grp":"er_crying_1","tags":["crying","emotional_threshold"]},
        {"qt":"scenario","text":"You receive genuinely wonderful news. Your response is:","opts":[
            {"id":"a","text":"Explosive — tears of joy, jumping, an overwhelming wave of feeling","s":5},
            {"id":"b","text":"Strong happiness that you express and share","s":3},
            {"id":"c","text":"Quiet satisfaction — you're pleased but don't show it dramatically","s":1},
            {"id":"d","text":"So intense it's almost uncomfortable — the joy is physical and overwhelming","s":5}
        ],"tier":"triangulation","grp":"er_good_news_1","tags":["positive_reactivity","expression"]},
        {"qt":"behavioral_recall","text":"How many emotions can you identify and name at any given moment?","opts":[
            {"id":"a","text":"Many — I experience complex blends of emotions and can identify nuanced states","s":5},
            {"id":"b","text":"Several — I'm aware of my primary emotion and sometimes secondary ones","s":3},
            {"id":"c","text":"One or two — I'm either happy, sad, angry, or fine","s":1},
            {"id":"d","text":"Many, and sometimes the complexity itself is overwhelming","s":5}
        ],"tier":"core","grp":"er_granularity_1","tags":["emotional_granularity","awareness"]},
        {"qt":"temporal","text":"Has anyone ever told you that you feel things 'too much' or 'too deeply'?","opts":[
            {"id":"a","text":"Frequently — it's been said by partners, family, and friends throughout my life","s":5},
            {"id":"b","text":"Occasionally — usually during intense emotional periods","s":3},
            {"id":"c","text":"Never — people don't describe me as especially emotional","s":1},
            {"id":"d","text":"Yes, and I've spent years questioning whether they're right or my feelings are valid","s":4}
        ],"tier":"consistency_check","grp":"er_told_too_much_1","tags":["temporal","others_perception"]},
        {"qt":"somatic","text":"When you feel angry, the physical intensity is:","opts":[
            {"id":"a","text":"Overwhelming — heat, racing heart, shaking, difficulty thinking clearly","s":5},
            {"id":"b","text":"Noticeable — I feel it but I can manage it","s":3},
            {"id":"c","text":"Mild — anger doesn't produce strong physical reactions in me","s":1},
            {"id":"d","text":"Intense and fast — it spikes hard and then crashes, leaving me exhausted","s":4}
        ],"tier":"core","grp":"er_anger_physical_1","tags":["somatic","anger_intensity"]},
        {"qt":"forced_choice","text":"How does anticipation of emotional events (weddings, funerals, confrontations) affect you?","opts":[
            {"id":"a","text":"The anticipation itself is almost as emotionally intense as the event","s":5},
            {"id":"b","text":"I feel some anticipation but it's manageable","s":3},
            {"id":"c","text":"I don't feel much until the event actually happens","s":1},
            {"id":"d","text":"I pre-process emotionally so much that the actual event sometimes feels anticlimactic","s":4}
        ],"tier":"core","grp":"er_anticipation_1","tags":["anticipatory_emotion","intensity"]},
        {"qt":"scenario","text":"Someone shares a beautiful personal story of resilience and growth. You:","opts":[
            {"id":"a","text":"Are deeply moved — tears well up and you feel their experience viscerally","s":5},
            {"id":"b","text":"Feel inspired and appreciative","s":3},
            {"id":"c","text":"Find it interesting but don't feel strong emotions about it","s":1},
            {"id":"d","text":"Are so moved that you need a moment before you can respond","s":5}
        ],"tier":"triangulation","grp":"er_beauty_1","tags":["emotional_response","beauty"]},
        {"qt":"behavioral_recall","text":"After an emotional day, how do you feel the next morning?","opts":[
            {"id":"a","text":"Still processing — emotional residue carries over and colors the next day","s":5},
            {"id":"b","text":"Somewhat tired but largely reset","s":3},
            {"id":"c","text":"Completely fresh — sleep resets my emotional state","s":1},
            {"id":"d","text":"My body feels the aftermath even when my mind has moved on","s":4}
        ],"tier":"core","grp":"er_carryover_1","tags":["emotional_carryover","recovery"]},
        {"qt":"somatic","text":"When you empathize with someone's emotional pain, do you feel it in your body?","opts":[
            {"id":"a","text":"Yes — their pain creates a matching physical sensation in me","s":5},
            {"id":"b","text":"Sometimes — if the emotion is very strong or the person is close to me","s":3},
            {"id":"c","text":"No — empathy is a mental process for me, not physical","s":1},
            {"id":"d","text":"Intensely — it's sometimes hard to distinguish my feelings from theirs","s":5}
        ],"tier":"core","grp":"er_empathic_physical_1","tags":["somatic","empathic_pain"]},
        {"qt":"forced_choice","text":"Your emotional baseline throughout the day is:","opts":[
            {"id":"a","text":"Variable — I cycle through multiple emotional states naturally, with high peaks and valleys","s":5},
            {"id":"b","text":"Fairly stable with moderate responses to events","s":3},
            {"id":"c","text":"Very stable — it takes a lot to shift my emotional state","s":1},
            {"id":"d","text":"Responsive — my emotions track closely with what's happening around me","s":4}
        ],"tier":"core","grp":"er_baseline_1","tags":["emotional_baseline","variability"]},
    ],
    "depth_of_processing": [
        {"qt":"scenario","text":"Someone makes a casual remark in a meeting. Hours later, you realize it had a hidden implication. This kind of delayed insight happens to you:","opts":[
            {"id":"a","text":"Constantly — I process things on multiple levels and meaning reveals itself over time","s":5},
            {"id":"b","text":"Occasionally — certain things stick with me and I realize more later","s":3},
            {"id":"c","text":"Rarely — I take things at face value and move on","s":1},
            {"id":"d","text":"Often — and the deeper meaning sometimes keeps me up at night","s":5}
        ],"tier":"core","grp":"dp_delayed_1","tags":["delayed_processing","depth"]},
        {"qt":"behavioral_recall","text":"Before making a decision, how many angles do you typically consider?","opts":[
            {"id":"a","text":"Exhaustively many — I consider implications, second-order effects, others' perspectives, and long-term consequences","s":5},
            {"id":"b","text":"Several — I consider the main factors thoroughly","s":3},
            {"id":"c","text":"A few — I trust my initial assessment and act","s":1},
            {"id":"d","text":"So many that decision-making is often painful and slow","s":5}
        ],"tier":"core","grp":"dp_decisions_1","tags":["decision_depth","analysis"]},
        {"qt":"forced_choice","text":"When you enter a new space (room, office, home), you:","opts":[
            {"id":"a","text":"Immediately notice details others miss — the mood, the arrangement, what's off","s":5},
            {"id":"b","text":"Take in the general vibe and notable features","s":3},
            {"id":"c","text":"See the space functionally — does it serve my needs?","s":1},
            {"id":"d","text":"Notice everything simultaneously and need a moment to process the input","s":5}
        ],"tier":"core","grp":"dp_observation_1","tags":["observation","detail_processing"]},
        {"qt":"somatic","text":"When you encounter a complex problem, your mind:","opts":[
            {"id":"a","text":"Enters a state of deep absorption — I lose track of time and my body as I think","s":5},
            {"id":"b","text":"Works through it methodically until I reach a solution","s":3},
            {"id":"c","text":"Looks for the simplest viable solution and moves on","s":1},
            {"id":"d","text":"Generates multiple frameworks and perspectives simultaneously — it's almost overwhelming","s":5}
        ],"tier":"core","grp":"dp_complexity_1","tags":["somatic","deep_thinking"]},
        {"qt":"scenario","text":"You watch a movie with ambiguous symbolism. Afterward, you:","opts":[
            {"id":"a","text":"Can't stop thinking about it — layers of meaning keep unfolding for days","s":5},
            {"id":"b","text":"Discuss the themes with friends over dinner and then move on","s":3},
            {"id":"c","text":"Enjoyed it in the moment but don't analyze it further","s":1},
            {"id":"d","text":"Research the director's intentions and related works to deepen understanding","s":4}
        ],"tier":"core","grp":"dp_meaning_1","tags":["meaning_making","analysis"]},
        {"qt":"temporal","text":"How has your tendency to overthink or deeply process changed?","opts":[
            {"id":"a","text":"I've always been a deep processor — my mind naturally works in layers","s":5},
            {"id":"b","text":"I've developed deeper processing as I've gained more knowledge and experience","s":3},
            {"id":"c","text":"I've always been more of a surface processor — quick judgments, fast action","s":1},
            {"id":"d","text":"I've always processed deeply but I've learned when depth is helpful vs when it's paralyzing","s":4}
        ],"tier":"core","grp":"dp_temporal_1","tags":["temporal","processing_development"]},
        {"qt":"forced_choice","text":"When someone tells you something, how many things are you simultaneously processing?","opts":[
            {"id":"a","text":"Their words, tone, body language, context, implications, what they're not saying, and how it connects to past information","s":5},
            {"id":"b","text":"Content and emotional tone primarily","s":3},
            {"id":"c","text":"The literal content — what they're saying","s":1},
            {"id":"d","text":"Everything, which sometimes means I miss the obvious because I'm tracking the subtle","s":5}
        ],"tier":"core","grp":"dp_communication_1","tags":["communication_processing","subtlety"]},
        {"qt":"behavioral_recall","text":"How often do you have 'aha' moments where seemingly unrelated pieces of information suddenly connect?","opts":[
            {"id":"a","text":"Frequently — my mind is always making connections in the background","s":5},
            {"id":"b","text":"Occasionally — when I've been thinking about something for a while","s":3},
            {"id":"c","text":"Rarely — I process things linearly, not associatively","s":1},
            {"id":"d","text":"Often, and it can happen at unexpected moments — in the shower, while driving","s":4}
        ],"tier":"core","grp":"dp_connections_1","tags":["pattern_recognition","insight"]},
        {"qt":"scenario","text":"You meet someone new at a social event. After a 15-minute conversation, you:","opts":[
            {"id":"a","text":"Have formed a complex, nuanced impression including things they probably didn't intend to reveal","s":5},
            {"id":"b","text":"Have a general sense of whether you like them and their key interests","s":3},
            {"id":"c","text":"Remember their name and what they do — the basics","s":1},
            {"id":"d","text":"Need time alone to process everything you picked up about them","s":5}
        ],"tier":"core","grp":"dp_people_1","tags":["people_reading","impression_formation"]},
        {"qt":"somatic","text":"When you're trying to make sense of a complex situation, you notice:","opts":[
            {"id":"a","text":"Physical tension until the pieces fit — my body won't relax until I understand","s":5},
            {"id":"b","text":"Mental engagement — thinking hard but no particular physical sensation","s":3},
            {"id":"c","text":"I don't dwell on complex situations — I look for the simple explanation","s":1},
            {"id":"d","text":"A meditative-like state where I can feel my brain working through multiple threads","s":4}
        ],"tier":"core","grp":"dp_resolution_1","tags":["somatic","cognitive_tension"]},
        {"qt":"forced_choice","text":"How do you process feedback about your work?","opts":[
            {"id":"a","text":"Deeply — I consider every word, what's behind it, what they didn't say, and integrate it over days","s":5},
            {"id":"b","text":"I listen carefully, note the key points, and apply what's useful","s":3},
            {"id":"c","text":"I take the headline and move on — dwelling on feedback isn't productive","s":1},
            {"id":"d","text":"I process it in waves — first reaction, then deeper understanding, then integration","s":4}
        ],"tier":"core","grp":"dp_feedback_1","tags":["feedback_processing","depth"]},
        {"qt":"behavioral_recall","text":"When planning, how far ahead do you naturally think?","opts":[
            {"id":"a","text":"Many steps — I naturally consider cascading consequences and long-term implications","s":5},
            {"id":"b","text":"A few steps — I plan for likely outcomes","s":3},
            {"id":"c","text":"One step — I handle things as they come","s":1},
            {"id":"d","text":"I think so far ahead that present-moment decisions become complicated","s":5}
        ],"tier":"triangulation","grp":"dp_planning_1","tags":["planning_depth","foresight"]},
        {"qt":"scenario","text":"A colleague says something that could be interpreted multiple ways. You:","opts":[
            {"id":"a","text":"Consider all possible interpretations, their implications, and which is most likely given context","s":5},
            {"id":"b","text":"Consider the most obvious interpretation and ask if unclear","s":3},
            {"id":"c","text":"Take it at face value — most communication is straightforward","s":1},
            {"id":"d","text":"Get stuck cycling through interpretations, unable to settle on one","s":4}
        ],"tier":"core","grp":"dp_interpretation_1","tags":["interpretation","ambiguity_processing"]},
        {"qt":"somatic","text":"When you're about to sleep, your mind:","opts":[
            {"id":"a","text":"Continues processing the day's events, finding patterns, making connections — it takes a long time to wind down","s":5},
            {"id":"b","text":"Reviews the day briefly then quiets down","s":3},
            {"id":"c","text":"Switches off fairly easily — sleep comes quickly","s":1},
            {"id":"d","text":"Presents me with insights and connections I didn't have time to process during the day","s":4}
        ],"tier":"core","grp":"dp_sleep_1","tags":["somatic","nighttime_processing"]},
        {"qt":"forced_choice","text":"How do you experience time during deep thought or creative work?","opts":[
            {"id":"a","text":"It disappears completely — I lose hours without noticing","s":5},
            {"id":"b","text":"I can track time with some effort while thinking deeply","s":3},
            {"id":"c","text":"I'm always aware of time — I don't get that absorbed","s":1},
            {"id":"d","text":"Time distortion is so common for me that I set multiple alarms","s":5}
        ],"tier":"triangulation","grp":"dp_flow_1","tags":["flow","time_perception"]},
        {"qt":"behavioral_recall","text":"When reading a book, do you pause to think about implications and connections?","opts":[
            {"id":"a","text":"Constantly — reading is more thinking than reading for me","s":5},
            {"id":"b","text":"Sometimes — when something particularly strikes me","s":3},
            {"id":"c","text":"Rarely — I read for content and move through it","s":1},
            {"id":"d","text":"So often that books take me much longer to finish than they should","s":4}
        ],"tier":"core","grp":"dp_reading_1","tags":["reading_depth","reflection"]},
        {"qt":"scenario","text":"You notice a small detail that's inconsistent with the rest of a situation — like a person's expression not matching their words. You:","opts":[
            {"id":"a","text":"Can't let it go — the inconsistency demands explanation and you'll figure it out","s":5},
            {"id":"b","text":"Note it and keep it in mind in case more evidence appears","s":3},
            {"id":"c","text":"Might not notice, or would dismiss it as nothing","s":1},
            {"id":"d","text":"Create multiple hypotheses to explain the inconsistency and test them over time","s":5}
        ],"tier":"core","grp":"dp_inconsistency_1","tags":["pattern_detection","incongruence"]},
        {"qt":"temporal","text":"How does your depth of processing affect your energy levels?","opts":[
            {"id":"a","text":"Significantly — deep processing is exhausting and I need more rest than most people","s":5},
            {"id":"b","text":"Somewhat — intense thinking tires me but it's manageable","s":3},
            {"id":"c","text":"Not much — thinking doesn't drain me physically","s":1},
            {"id":"d","text":"I alternate between energized absorption and complete exhaustion depending on the topic","s":4}
        ],"tier":"core","grp":"dp_energy_1","tags":["temporal","processing_fatigue"]},
        {"qt":"forced_choice","text":"When you reflect on past experiences, you tend to:","opts":[
            {"id":"a","text":"Extract multiple layers of meaning — each review reveals something new","s":5},
            {"id":"b","text":"Draw practical lessons and apply them going forward","s":3},
            {"id":"c","text":"Recall the facts but don't analyze them deeply","s":1},
            {"id":"d","text":"Get absorbed in re-processing, sometimes discovering completely new understandings years later","s":5}
        ],"tier":"core","grp":"dp_reflection_1","tags":["reflection_depth","meaning_extraction"]},
        {"qt":"behavioral_recall","text":"When someone asks your opinion on a complex topic, you:","opts":[
            {"id":"a","text":"Need time — my immediate response would be too simplistic; I need to process fully","s":5},
            {"id":"b","text":"Can give a solid answer fairly quickly","s":3},
            {"id":"c","text":"Share my view immediately — I know where I stand","s":1},
            {"id":"d","text":"Start with caveats and qualifications because the topic's complexity deserves nuance","s":4}
        ],"tier":"core","grp":"dp_opinion_1","tags":["opinion_formation","nuance"]},
    ],
    "overstimulation_threshold": [
        {"qt":"scenario","text":"You've been socializing, shopping, and running errands all day. It's 3pm and a friend suggests adding one more activity. You:","opts":[
            {"id":"a","text":"Feel your body revolt — you've hit a wall and adding anything more feels impossible","s":5},
            {"id":"b","text":"Tired but could push through for something fun","s":3},
            {"id":"c","text":"Still have plenty of energy — this has been a normal day","s":1},
            {"id":"d","text":"Need to rest NOW or you'll become irritable, tearful, or physically unwell","s":5}
        ],"tier":"core","grp":"ot_capacity_1","tags":["overstimulation","capacity"]},
        {"qt":"behavioral_recall","text":"How often do you need to withdraw from social situations to recover?","opts":[
            {"id":"a","text":"After almost every social interaction — even enjoyable ones drain me","s":5},
            {"id":"b","text":"After extended or intense social situations","s":3},
            {"id":"c","text":"Rarely — social interaction energizes me","s":1},
            {"id":"d","text":"I need recovery proportional to the stimulation — quiet dinner needs less than a party","s":4}
        ],"tier":"core","grp":"ot_recovery_need_1","tags":["social_recovery","withdrawal"]},
        {"qt":"forced_choice","text":"Your ideal daily schedule includes:","opts":[
            {"id":"a","text":"Significant blocks of alone time built around limited social/stimulating activities","s":5},
            {"id":"b","text":"A balance of social time and alone time","s":3},
            {"id":"c","text":"Mostly social or active time with brief rest periods","s":1},
            {"id":"d","text":"I plan my entire day around managing my energy and stimulation levels","s":5}
        ],"tier":"core","grp":"ot_schedule_1","tags":["schedule_management","energy"]},
        {"qt":"somatic","text":"When you've exceeded your stimulation threshold, your body:","opts":[
            {"id":"a","text":"Shuts down — I get brain fog, physical exhaustion, maybe headache or nausea","s":5},
            {"id":"b","text":"Feels tired — I need rest but I'm functional","s":3},
            {"id":"c","text":"I don't really have a stimulation threshold — I can keep going","s":1},
            {"id":"d","text":"Enters a strange state — wired but exhausted, unable to rest even though I need to","s":5}
        ],"tier":"core","grp":"ot_shutdown_1","tags":["somatic","nervous_system_shutdown"]},
        {"qt":"scenario","text":"You have three social events in one weekend. By Sunday evening, you:","opts":[
            {"id":"a","text":"Are completely depleted — you need at least two days of solitude to recover","s":5},
            {"id":"b","text":"Are tired but will recover with a good night's sleep","s":3},
            {"id":"c","text":"Feel great — that was a fun weekend","s":1},
            {"id":"d","text":"Are physically ill — overstimulation manifests as actual symptoms for you","s":5}
        ],"tier":"core","grp":"ot_weekend_1","tags":["social_depletion","recovery"]},
        {"qt":"temporal","text":"How has your threshold for stimulation changed over the years?","opts":[
            {"id":"a","text":"It's always been low — I've always needed more recovery time than my peers","s":5},
            {"id":"b","text":"It's decreased — I used to handle more stimulation than I can now","s":4},
            {"id":"c","text":"It's always been high — I can handle a lot before feeling overwhelmed","s":1},
            {"id":"d","text":"I've learned to manage it better but the underlying threshold hasn't changed","s":4}
        ],"tier":"core","grp":"ot_temporal_1","tags":["temporal","threshold_change"]},
        {"qt":"forced_choice","text":"How do you feel about unexpected changes to your plans?","opts":[
            {"id":"a","text":"Very distressed — unexpected changes consume energy I'd budgeted for something else","s":5},
            {"id":"b","text":"Mildly annoyed but adaptable","s":3},
            {"id":"c","text":"Fine — flexibility is one of my strengths","s":1},
            {"id":"d","text":"Anxious because I can't recalculate my energy budget on the fly","s":5}
        ],"tier":"core","grp":"ot_unexpected_1","tags":["change_sensitivity","energy_budgeting"]},
        {"qt":"scenario","text":"You're in an open-plan office. Multiple conversations, phones ringing, people walking by. You:","opts":[
            {"id":"a","text":"Cannot function — you need noise-canceling headphones, or better yet, a private space","s":5},
            {"id":"b","text":"Find it distracting but can work through it","s":3},
            {"id":"c","text":"Thrive — the energy of a busy office helps you focus","s":1},
            {"id":"d","text":"Reach your limit within an hour or two and need to escape to a quiet space","s":4}
        ],"tier":"core","grp":"ot_office_1","tags":["open_plan","overstimulation"]},
        {"qt":"behavioral_recall","text":"How often do you cancel plans because you've run out of energy?","opts":[
            {"id":"a","text":"Frequently — protecting my energy sometimes means disappointing people","s":5},
            {"id":"b","text":"Occasionally — usually after an unusually demanding period","s":3},
            {"id":"c","text":"Rarely — I follow through on plans regardless of energy level","s":1},
            {"id":"d","text":"I've learned to schedule preventively so I don't overcommit in the first place","s":4}
        ],"tier":"core","grp":"ot_cancellation_1","tags":["plan_cancellation","energy_protection"]},
        {"qt":"somatic","text":"When you've been overstimulated and finally reach a quiet, safe space, you:","opts":[
            {"id":"a","text":"Feel like you're decompressing — physical relief floods your body, you might cry","s":5},
            {"id":"b","text":"Feel relief and relaxation setting in","s":3},
            {"id":"c","text":"Don't particularly notice a difference","s":1},
            {"id":"d","text":"Take hours to truly settle — my nervous system stays activated long after the stimulation ends","s":5}
        ],"tier":"core","grp":"ot_relief_1","tags":["somatic","decompression"]},
        {"qt":"scenario","text":"A holiday gathering involves 20+ people, children running around, music, cooking smells, and constant conversation. After two hours, you:","opts":[
            {"id":"a","text":"Are hiding in the bathroom taking deep breaths","s":5},
            {"id":"b","text":"Are ready to go but managing okay","s":3},
            {"id":"c","text":"Are having the time of your life — this is what holidays are about","s":1},
            {"id":"d","text":"Left an hour ago — you know your limits and planned your exit","s":4}
        ],"tier":"core","grp":"ot_holiday_1","tags":["family_gatherings","overstimulation"]},
        {"qt":"forced_choice","text":"How much alone time do you need daily to feel balanced?","opts":[
            {"id":"a","text":"Several hours minimum — without it I become irritable, foggy, or unwell","s":5},
            {"id":"b","text":"An hour or two is enough","s":3},
            {"id":"c","text":"Very little — I get restless being alone","s":1},
            {"id":"d","text":"My need varies but I always need some, and it's non-negotiable","s":4}
        ],"tier":"core","grp":"ot_alone_need_1","tags":["alone_time","daily_need"]},
        {"qt":"behavioral_recall","text":"How do you manage your energy during a typical work week?","opts":[
            {"id":"a","text":"Carefully — I schedule recovery time, limit social commitments, and control my environment","s":5},
            {"id":"b","text":"Somewhat — I know my limits and try to respect them","s":3},
            {"id":"c","text":"I don't need to manage energy — I have plenty","s":1},
            {"id":"d","text":"It's a constant struggle — the work week demands more stimulation than I can handle","s":5}
        ],"tier":"core","grp":"ot_work_management_1","tags":["energy_management","work"]},
        {"qt":"somatic","text":"When you're approaching overstimulation, what are the early warning signs in your body?","opts":[
            {"id":"a","text":"I have reliable signs — irritability, jaw clenching, difficulty tracking conversation, sensory sensitivity spikes","s":5},
            {"id":"b","text":"I notice fatigue and decreased patience","s":3},
            {"id":"c","text":"I don't really have early warning signs — I just keep going","s":1},
            {"id":"d","text":"My body signals clearly but I sometimes override the warnings, which I always regret","s":4}
        ],"tier":"core","grp":"ot_warning_signs_1","tags":["somatic","interoception"]},
        {"qt":"scenario","text":"Your work requires a day of back-to-back meetings (8 hours of constant social interaction). Afterward:","opts":[
            {"id":"a","text":"You're completely incapacitated — unable to cook dinner, hold a conversation, or function","s":5},
            {"id":"b","text":"You're very tired and need a quiet evening","s":3},
            {"id":"c","text":"You're tired but could still go to dinner with friends","s":1},
            {"id":"d","text":"You've learned to pace yourself during the day (breaks, quiet moments) so you're functional but drained","s":4}
        ],"tier":"core","grp":"ot_marathon_1","tags":["social_marathon","depletion"]},
        {"qt":"temporal","text":"How has your understanding of your stimulation threshold evolved?","opts":[
            {"id":"a","text":"I've spent years mapping my limits — I now have detailed knowledge of what drains me and how to recover","s":5},
            {"id":"b","text":"I've become more aware of my needs and accommodate them when possible","s":3},
            {"id":"c","text":"I haven't needed to map my limits — I don't get overstimulated","s":1},
            {"id":"d","text":"Understanding my threshold has been a journey of self-acceptance — I used to push through, now I protect","s":4}
        ],"tier":"consistency_check","grp":"ot_self_knowledge_1","tags":["temporal","self_knowledge"]},
        {"qt":"forced_choice","text":"Which best describes your experience of 'too much'?","opts":[
            {"id":"a","text":"I have a clearly defined maximum beyond which I can't function — it's not a preference, it's a limit","s":5},
            {"id":"b","text":"I have preferences for how much stimulation I enjoy but I can push through when needed","s":3},
            {"id":"c","text":"I don't experience a 'too much' threshold — more stimulation is usually better","s":1},
            {"id":"d","text":"My limit varies day to day but it's always present and must be respected","s":4}
        ],"tier":"core","grp":"ot_limit_1","tags":["limit_definition","self_awareness"]},
        {"qt":"behavioral_recall","text":"Have you ever had a 'meltdown' or 'shutdown' from overstimulation?","opts":[
            {"id":"a","text":"Yes — complete emotional or physical collapse that took days to recover from","s":5},
            {"id":"b","text":"Mild versions — I've felt overwhelmed but not to the point of collapse","s":3},
            {"id":"c","text":"Never — overstimulation isn't something I experience","s":1},
            {"id":"d","text":"Yes, and it was a turning point in understanding and managing my sensitivity","s":4}
        ],"tier":"core","grp":"ot_meltdown_1","tags":["meltdown","shutdown"]},
        {"qt":"somatic","text":"When traveling (airports, new environments, navigation, crowds), how quickly do you deplete?","opts":[
            {"id":"a","text":"Very quickly — travel is one of the most overstimulating activities I do","s":5},
            {"id":"b","text":"It's tiring but manageable with good planning","s":3},
            {"id":"c","text":"Travel energizes me — the novelty is stimulating in a good way","s":1},
            {"id":"d","text":"I enjoy travel but need much more recovery time than my travel companions","s":4}
        ],"tier":"triangulation","grp":"ot_travel_1","tags":["somatic","travel"]},
        {"qt":"forced_choice","text":"Your relationship with stimulating environments (concerts, festivals, busy cities) is:","opts":[
            {"id":"a","text":"Love the idea, can't handle the reality — my nervous system overloads","s":5},
            {"id":"b","text":"Enjoy in moderation with planned recovery time","s":3},
            {"id":"c","text":"Love them and thrive in them — the busier the better","s":1},
            {"id":"d","text":"I've grieved the loss of being able to enjoy them — my threshold has decreased over time","s":5}
        ],"tier":"core","grp":"ot_stimulating_env_1","tags":["stimulating_environments","limits"]},
    ],
}

for dim, qs in hsp_data.items():
    for q in qs:
        entry = {
            "uid": f"HSP-{uid:03d}",
            "assessment_id": "highly_sensitive",
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

with open("/Users/user/personal/sb/trueassess/priv/question_bank/highly_sensitive.json", "w") as f:
    json.dump(questions, f, indent=2)

print(f"Wrote {len(questions)} HSP questions")
