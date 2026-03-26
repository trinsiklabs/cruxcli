import json
from datetime import datetime

tickets = []

def add(slug, title, typ, pipeline, priority, deps=None):
    tickets.append({
        "slug": slug,
        "title": title,
        "type": typ,
        "pipeline": pipeline,
        "priority": priority,
        "dependencies": deps or [],
        "status": "backlog"
    })

# ============================================================
# 1. ASSESSMENT BANKS — Evidence pages, Landing pages
# ============================================================
banks = {
    # psychological
    "attachment_style": "Attachment Style",
    "act_flexibility": "ACT Psychological Flexibility",
    "cognitive_distortions": "Cognitive Distortions",
    "detachment_awareness": "Detachment / Awareness (de Mello)",
    "emotional_regulation": "Emotional Regulation Capacity",
    "shadow_integration": "Shadow Work (Jung)",
    "trauma_responses": "Trauma Response Profile (4F)",
    "triggers_profile": "Triggers Profile",
    "daddy_issues": "Daddy Issues / Father Wound",
    # personality
    "big_five": "Big Five / OCEAN Personality",
    "enneagram": "Enneagram",
    "mbti": "Myers-Briggs / MBTI",
    "disc": "DISC Profile",
    "cliftonstrengths": "CliftonStrengths",
    "love_languages": "Love Languages",
    "kolbe": "Kolbe Instinct Profile",
    "carol_tuttle": "Carol Tuttle Energy Profiling",
    "via_strengths": "VIA Character Strengths",
    # philosophical
    "stoicism": "Stoicism Assessment",
    "nietzsche": "Nietzsche Assessment",
    "existentialism": "Existentialism Assessment",
    "buddhism": "Buddhism Assessment",
    "pragmatism": "Pragmatism Assessment",
    # relationship_skill
    "communication_gottman": "Communication Skills (Gottman/NVC)",
    "boundary_capacity": "Boundary Capacity",
    "conflict_navigation": "Conflict Navigation",
    "repair_skills": "Repair Skills",
    "vulnerability_capacity": "Vulnerability Capacity",
    "age_gap_compatibility": "Age Gap Compatibility",
    # self_knowledge
    "narcissism_spectrum": "Narcissism Spectrum",
    "empathy": "Empathy (3-Dimensional)",
    "learning_strategies": "Learning Strategies",
    # clinical
    "adhd": "ADHD Reflectance",
    "autism_spectrum": "Autism Spectrum Reflectance",
    "alexithymia": "Alexithymia",
    "borderline_traits": "Borderline Traits Reflectance",
    "codependency": "Codependency",
    "dark_triad": "Dark Triad / Tetrad",
    "hsp": "Highly Sensitive Person (HSP)",
    "people_pleasing": "People-Pleasing",
    "perfectionism": "Perfectionism",
    "trauma_cptsd": "Trauma / C-PTSD",
    "anxiety_depression_screen": "Anxiety & Depression Screen",
    # custom designs
    "forgiveness_profile": "Forgiveness Profile",
    "communication_profile": "Communication Profile",
    "dashboard_light_profile": "Dashboard Light Profile",
    "relationship_expectations": "Relationship Expectations",
    "values_real_vs_aspirational": "Values: Real vs Aspirational",
    # adult
    "bdsm_dynamics": "BDSM Dynamics",
    "fetish_assessment": "Fetish Assessment",
    "kink_matching": "Kink Matching",
    "purity_test": "Purity Test",
    # life
}

# For each bank: evidence page + landing page
for bank_id, bank_name in banks.items():
    add(f"{bank_id}-evidence", f"{bank_name} -- Evidence Evaluation", "evidence", "trueassess_content", "p0", [f"bank:{bank_id}"])
    add(f"{bank_id}-landing", f"{bank_name} -- Landing Page", "landing", "trueassess_content", "p0", [f"bank:{bank_id}"])

# Additional assessments from PRODUCT_SPEC that don't have banks yet
additional_assessments = {
    "self_awareness": "Self-Awareness Gap",
    "self_worth": "Self-Worth Assessment",
    "self_respect": "Self-Respect Assessment",
    "authenticity": "Authenticity Index",
    "groupthink_tendency": "Groupthink Tendency",
    "magical_thinking": "Magical Thinking",
    "emotional_intelligence": "Emotional Intelligence (Goleman)",
    "iq_assessment": "IQ Assessment",
    "relationship_commitments": "Relationship Commitments",
    "purpose_assessment": "Purpose Assessment",
    "mindfulness_spirituality": "Mindfulness / Spirituality",
    "swot_per_axis": "SWOT Per Axis (Meta-Assessment)",
    "presuppositions_assessment": "Presuppositions Assessment",
    "pattern_recognition_profile": "Pattern Recognition Profile",
    "regulation_profile": "Regulation Profile",
    "identity_self_worth_profile": "Identity & Self-Worth Profile",
    # life assessments
    "longevity": "Longevity Assessment",
    "aging": "Aging Assessment",
    "fitness": "Fitness Assessment",
    "active_lifestyle": "Active Lifestyle Assessment",
    "skills_hobbies_interests": "Skills / Hobbies / Interests",
    "adulting_maturity": "Adulting / Maturity",
    "life_skills": "Life Skills",
    # social/political
    "traditional_feminist_spectrum": "Traditional-Feminist Spectrum (13 Axes)",
    "traditional_marxist_male": "Traditional-Marxist Male Spectrum (15 Axes)",
    "hot_crazy_matrix": "Hot/Crazy Matrix Decomposition",
    "false_accusation_risk": "False Accusation Risk Assessment",
    # appearance
    "appearance_self_rating": "Appearance Self-Rating with AI Calibration",
    # clinical extras
    "suicidality_reflectance": "Suicidality Reflectance",
}

for a_id, a_name in additional_assessments.items():
    add(f"{a_id}-evidence", f"{a_name} -- Evidence Evaluation", "evidence", "trueassess_content", "p1", [])
    add(f"{a_id}-landing", f"{a_name} -- Landing Page", "landing", "trueassess_content", "p1", [])

# Tropes and archetypes
archetypes = [
    ("cool-girl", "Cool Girl Archetype"),
    ("pick-me-girl", "Pick Me / Special Girl Archetype"),
    ("girly-girl", "Girly Girl Archetype"),
    ("nice-guy", "Nice Guy Archetype (Covert Contract)"),
    ("player-archetype", "Player Archetype"),
    ("chad-archetype", "Chad Archetype"),
    ("warrior-king-magician-lover", "Warrior / King / Magician / Lover"),
    ("alpha-beta-sigma", "Alpha / Beta / Sigma (with Critique)"),
]
for a_id, a_name in archetypes:
    add(f"{a_id}-landing", f"{a_name} -- Landing Page", "landing", "trueassess_content", "p2", [])
    add(f"{a_id}-belief-decomp", f"{a_name} -- Belief Decomposition", "belief", "trueassess_content", "p1", [])

# ============================================================
# 2. PATHWAYS — each pathway needs a content page
# ============================================================
pathways = [
    "act_flexibility", "alexithymia", "anxiety_depression_screen", "attachment_style",
    "borderline_traits", "boundary_capacity", "codependency", "cognitive_distortions",
    "communication_gottman", "conflict_navigation", "daddy_issues", "dark_triad",
    "detachment_awareness", "emotional_regulation", "groupthink_tendency",
    "magical_thinking", "narcissism_spectrum", "people_pleasing", "perfectionism",
    "shadow_integration", "trauma_responses", "triggers_profile"
]
for p in pathways:
    add(f"{p}-pathway-page", f"{p.replace('_', ' ').title()} -- Therapeutic Pathway Page", "framework", "trueassess_content", "p1", [f"pathway:{p}"])

# ============================================================
# 3. PSYCHOLOGICAL FRAMEWORKS — 156 frameworks, each needs a page
# ============================================================
frameworks = [
    # Category 1: Evidence-Based Clinical (Strong)
    ("cbt", "Cognitive Behavioral Therapy (CBT)"),
    ("dbt", "Dialectical Behavior Therapy (DBT)"),
    ("act", "Acceptance and Commitment Therapy (ACT)"),
    ("emdr", "Eye Movement Desensitization and Reprocessing (EMDR)"),
    ("cpt", "Cognitive Processing Therapy (CPT)"),
    ("prolonged-exposure", "Prolonged Exposure Therapy (PE)"),
    ("ipt", "Interpersonal Psychotherapy (IPT)"),
    ("behavioral-activation", "Behavioral Activation (BA)"),
    ("motivational-interviewing", "Motivational Interviewing (MI)"),
    ("erp", "Exposure and Response Prevention (ERP)"),
    ("mbsr", "Mindfulness-Based Stress Reduction (MBSR)"),
    ("mbct", "Mindfulness-Based Cognitive Therapy (MBCT)"),
    ("eft-couples", "Emotionally Focused Therapy -- Couples (EFT)"),
    ("tf-cbt", "Trauma-Focused CBT (TF-CBT)"),
    ("rebt", "Rational Emotive Behavior Therapy (REBT)"),
    ("pcit", "Parent-Child Interaction Therapy (PCIT)"),
    # Category 2: Established Clinical (Moderate)
    ("schema-therapy", "Schema Therapy"),
    ("ifs", "Internal Family Systems (IFS)"),
    ("cft", "Compassion-Focused Therapy (CFT)"),
    ("metacognitive-therapy", "Metacognitive Therapy (MCT)"),
    ("gottman-method", "Gottman Method Couples Therapy"),
    ("mbt", "Mentalization-Based Treatment (MBT)"),
    ("aedp", "Accelerated Experiential Dynamic Psychotherapy (AEDP)"),
    ("cbasp", "Cognitive Behavioral Analysis System (CBASP)"),
    ("fap", "Functional Analytic Psychotherapy (FAP)"),
    ("sfbt", "Solution-Focused Brief Therapy (SFBT)"),
    ("imago-therapy", "Imago Relationship Therapy"),
    ("eft-individual", "Emotion-Focused Therapy -- Individual"),
    ("mbrp", "Mindfulness-Based Relapse Prevention (MBRP)"),
    ("coherence-therapy", "Coherence Therapy"),
    ("ibct", "Integrative Behavioral Couple Therapy (IBCT)"),
    ("art", "Accelerated Resolution Therapy (ART)"),
    ("rfcbt", "Rumination-Focused CBT (RFCBT)"),
    ("mst", "Multisystemic Therapy (MST)"),
    ("fft", "Functional Family Therapy (FFT)"),
    # Category 3: Body/Somatic
    ("somatic-experiencing", "Somatic Experiencing (SE)"),
    ("sensorimotor-psychotherapy", "Sensorimotor Psychotherapy"),
    ("hakomi", "Hakomi Method"),
    ("brainspotting", "Brainspotting"),
    ("bioenergetic-analysis", "Bioenergetic Analysis"),
    ("reichian-therapy", "Reichian Therapy / Vegetotherapy"),
    ("rolfing", "Rolfing / Structural Integration"),
    ("polyvagal-therapy", "Polyvagal-Informed Therapy"),
    ("ssp", "Safe and Sound Protocol (SSP)"),
    # Category 4: Mindfulness & Contemplative
    ("mindful-self-compassion", "Mindful Self-Compassion (MSC)"),
    ("mbre", "Mindfulness-Based Relationship Enhancement"),
    ("vipassana", "Vipassana Meditation"),
    ("zen-practice", "Zen Practice"),
    ("yoga-therapy", "Yoga Therapy"),
    # Category 5: Humanistic & Existential
    ("person-centered-therapy", "Person-Centered Therapy (Rogers)"),
    ("gestalt-therapy", "Gestalt Therapy"),
    ("existential-therapy", "Existential Therapy (Yalom)"),
    ("logotherapy", "Logotherapy (Frankl)"),
    ("meaning-centered-psychotherapy", "Meaning-Centered Psychotherapy"),
    ("focusing-therapy", "Focusing-Oriented Psychotherapy"),
    ("adlerian-therapy", "Adlerian Therapy"),
    # Category 6: Psychodynamic & Depth
    ("psychoanalysis", "Psychoanalysis (Classical Freudian)"),
    ("psychodynamic-short-term", "Psychodynamic Therapy (Modern Short-Term)"),
    ("jungian-analytical", "Jungian Analytical Psychology"),
    ("archetypal-psychology", "Archetypal Psychology (Hillman)"),
    ("object-relations", "Object Relations Therapy"),
    ("self-psychology", "Self Psychology (Kohut)"),
    ("relational-psychoanalysis", "Relational Psychoanalysis"),
    ("lacanian", "Lacanian Psychoanalysis"),
    ("depth-psychology", "Depth Psychology (Broad Tradition)"),
    # Category 7: Systems & Relational
    ("structural-family", "Structural Family Therapy"),
    ("strategic-family", "Strategic Family Therapy"),
    ("bowenian-family", "Bowenian Family Therapy"),
    ("narrative-therapy", "Narrative Therapy"),
    ("relational-cultural", "Relational-Cultural Therapy"),
    ("abft", "Attachment-Based Family Therapy (ABFT)"),
    ("ddp", "Dyadic Developmental Psychotherapy (DDP)"),
    ("efft", "Emotionally Focused Family Therapy (EFFT)"),
    # Category 8: Expressive & Creative
    ("art-therapy", "Art Therapy"),
    ("music-therapy", "Music Therapy"),
    ("drama-therapy", "Drama Therapy / Psychodrama"),
    ("dance-movement-therapy", "Dance/Movement Therapy"),
    ("sandplay-therapy", "Sandplay / Sand Tray Therapy"),
    ("expressive-arts", "Expressive Arts Therapy (Integrated)"),
    ("bibliotherapy", "Bibliotherapy"),
    ("writing-journaling", "Writing / Journaling Therapy"),
    ("play-therapy", "Play Therapy"),
    # Category 9: Self-Development & Coaching
    ("nvc", "Nonviolent Communication (NVC)"),
    ("boundaries-framework", "Boundaries Framework (Cloud/Townsend)"),
    ("enneagram-framework", "Enneagram Framework"),
    ("spiral-dynamics", "Spiral Dynamics"),
    ("integral-theory", "Integral Theory / AQAL"),
    ("co-active-coaching", "Co-Active Coaching Model"),
    ("grow-model", "GROW Model"),
    ("ontological-coaching", "Ontological Coaching"),
    ("nlp", "Neuro-Linguistic Programming (NLP)"),
    ("self-determination-theory", "Self-Determination Theory (SDT)"),
    ("maslows-hierarchy", "Maslow's Hierarchy of Needs"),
    ("stages-of-change", "Transtheoretical Model / Stages of Change"),
    ("positive-psychology", "Positive Psychology (Seligman)"),
    ("well-being-therapy", "Well-Being Therapy (WBT)"),
    ("broaden-and-build", "Broaden-and-Build Theory"),
    # Category 10: Philosophical & Spiritual
    ("stoicism-applied", "Stoicism (Applied)"),
    ("buddhism-applied", "Buddhism (Applied Psychological Principles)"),
    ("de-mello-framework", "Anthony de Mello's Framework"),
    ("tolle-framework", "Eckhart Tolle's Framework"),
    ("taoism-applied", "Taoism / Daoism (Applied)"),
    ("sufism-applied", "Sufism (Applied Psychological Principles)"),
    ("kabbalah-applied", "Kabbalah (Applied)"),
    ("christian-contemplative", "Christian Contemplative Practice"),
    ("existentialism-applied", "Existentialism (Applied)"),
    ("philosophical-counseling", "Philosophical Counseling"),
    ("hindu-vedantic", "Hindu/Vedantic Psychology (Applied)"),
    # Category 11: Neuroscience-Based
    ("neurofeedback", "Neurofeedback (EEG Biofeedback)"),
    ("tms", "Transcranial Magnetic Stimulation (TMS)"),
    ("ketamine-therapy", "Ketamine-Assisted Psychotherapy"),
    ("psychedelic-therapy", "Psychedelic-Assisted Therapy (PAT)"),
    ("biofeedback", "Biofeedback"),
    ("hrv-training", "Heart Rate Variability (HRV) Training"),
    ("ipnb", "Interpersonal Neurobiology (IPNB)"),
    # Category 12: Emerging & Integrative
    ("psychosynthesis", "Psychosynthesis"),
    ("process-work", "Process-Oriented Psychology"),
    ("holotropic-breathwork", "Holotropic Breathwork"),
    ("ego-state-therapy", "Ego State Therapy"),
    ("transactional-analysis", "Transactional Analysis (TA)"),
    ("reality-therapy", "Reality Therapy / Choice Theory"),
    ("constructivist-therapy", "Constructivist Therapy (Kelly)"),
    ("morita-therapy", "Morita Therapy"),
    ("naikan-therapy", "Naikan Therapy"),
    ("constructive-living", "Constructive Living"),
    ("ert", "Emotion Regulation Therapy (ERT)"),
    ("unified-protocol", "Unified Protocol (Barlow)"),
    # Category 13: Alternative & Energy-Based
    ("eft-tapping", "Emotional Freedom Techniques (EFT/Tapping)"),
    ("tft", "Thought Field Therapy (TFT)"),
    ("tat", "Tapas Acupressure Technique"),
    ("reiki-therapy", "Reiki (Therapeutic)"),
    ("primal-therapy", "Primal Therapy"),
    ("rebirthing-breathwork", "Rebirthing Breathwork"),
    ("crystal-therapy", "Crystal Therapy"),
    ("hypnotherapy", "Hypnotherapy / Clinical Hypnosis"),
    ("animal-assisted", "Animal-Assisted Therapy"),
    ("ecotherapy", "Ecotherapy / Nature-Based Therapy"),
    ("wilderness-therapy", "Wilderness Therapy"),
    ("equine-therapy", "Equine-Assisted Psychotherapy"),
    ("flotation-therapy", "Flotation Therapy (REST)"),
    # Additional frameworks
    ("feminist-therapy", "Feminist Therapy"),
    ("multicultural-therapy", "Multicultural Counseling and Therapy"),
    ("mb-eat", "Mindfulness-Based Eating Awareness Training"),
    ("positive-psychotherapy", "Positive Psychotherapy (PPT)"),
    ("control-mastery", "Control-Mastery Theory"),
    ("abbt", "Acceptance-Based Behavioral Therapy"),
    ("dbt-skills-standalone", "DBT Skills Training (Standalone)"),
    ("resilience-framework", "The Resilience Framework"),
    ("ei-framework", "Emotional Intelligence Framework"),
    ("attachment-theory", "Attachment Theory (Bowlby/Ainsworth)"),
    ("polarity-therapy", "Polarity Therapy"),
    ("alexander-technique", "Alexander Technique"),
    ("feldenkrais", "Feldenkrais Method"),
]

for fw_id, fw_name in frameworks:
    add(f"fw-{fw_id}", f"{fw_name} -- Deep Framework Page", "framework", "knowledge_web", "p1", [])

# ============================================================
# 4. RELIGIOUS / UNCHURCHED GROUPS — 46+ groups, each needs a page + belief decomposition
# ============================================================
religious_groups = [
    ("sbnr-protestant", "SBNR with Protestant Background"),
    ("dechurched-protestant", "Dechurched Protestant"),
    ("lapsed-catholic", "Lapsed Catholic"),
    ("cafeteria-catholic", "Cafeteria Catholic"),
    ("exvangelical", "Exvangelical"),
    ("deconstructing", "Deconstructing (Still In Process)"),
    ("cultural-orthodox", "Cultural Orthodox Christian"),
    ("post-mainline-none", "Post-Mainline Protestant 'None'"),
    ("jack-mormon", "Jack Mormon"),
    ("nom-mormon", "New Order Mormon (NOM)"),
    ("post-mormon", "Post-Mormon"),
    ("exmormon-activist", "ExMormon (Activist)"),
    ("jw-pimo", "JW PIMO (Physically In, Mentally Out)"),
    ("jw-fading", "JW Fading (Quietly Leaving)"),
    ("jw-disfellowshipped", "JW Disfellowshipped"),
    ("jw-pomi", "JW POMI (Physically Out, Mentally In)"),
    ("cultural-muslim", "Cultural / Secular Muslim"),
    ("closeted-ex-muslim", "Closeted Ex-Muslim"),
    ("public-ex-muslim", "Public Ex-Muslim"),
    ("cultural-ex-muslim", "Cultural Ex-Muslim"),
    ("progressive-muslim", "Progressive / Liberal Muslim"),
    ("sufi-non-institutional", "Sufi-Leaning Non-Institutional"),
    ("secular-jew", "Secular / Culturally Jewish"),
    ("high-holiday-jew", "High Holiday / Twice-a-Year Jew"),
    ("humanistic-judaism", "Humanistic Judaism"),
    ("post-denominational-jewish", "Post-Denominational / 'Just Jewish'"),
    ("otd-ultra-orthodox", "OTD (Off The Derech) -- Ultra-Orthodox"),
    ("cultural-hindu", "Cultural / Non-Practicing Hindu"),
    ("hindu-atheist", "Hindu Atheist / Dharmic Atheist"),
    ("western-secular-buddhist", "Western Secular Buddhist"),
    ("cultural-buddhist", "Cultural Buddhist (Asian Heritage)"),
    ("cultural-sikh", "Cultural / Non-Practicing Sikh"),
    ("free-zone-scientologist", "Free Zone / Independent Scientologist"),
    ("ex-scientologist", "Ex-Scientologist"),
    ("ex-amish", "Ex-Amish"),
    ("rumspringa-non-returner", "Rumspringa Non-Returner"),
    ("purity-culture-refugee", "Purity Culture Refugee"),
    ("quiverfull-leaver", "Quiverfull / Christian Patriarchy Leaver"),
    ("ex-seventh-day-adventist", "Ex-Seventh-day Adventist"),
    ("ex-pentecostal", "Ex-Pentecostal / Ex-Charismatic"),
    ("cult-survivor-first-gen", "Cult Survivor (First Generation)"),
    ("cult-survivor-second-gen", "Cult Survivor (Second Generation / Born In)"),
    ("sbnr-cross-tradition", "Spiritual But Not Religious (Cross-Tradition)"),
    ("agnostic-theist", "Agnostic Theist"),
    ("deist", "Deist"),
    ("syncretic-practitioner", "Syncretic Practitioner"),
    ("religious-trauma-identity", "Religious Trauma Community Identity"),
    ("moralistic-therapeutic-deism", "Moralistic Therapeutic Deism"),
]

for rg_id, rg_name in religious_groups:
    add(f"rg-{rg_id}-page", f"{rg_name} -- Belief Profile Page", "religious", "trueassess_content", "p1", [])
    add(f"rg-{rg_id}-decomp", f"{rg_name} -- Belief Decomposition", "belief", "trueassess_content", "p1", [f"rg-{rg_id}-page"])

# ============================================================
# 5. PATTERN ENCYCLOPEDIA — 175+ named patterns
# ============================================================
# Top 20 priority patterns from project_pattern_encyclopedia.md
priority_patterns = [
    ("scorekeeping", "Scorekeeping"),
    ("contempt", "Contempt (Gottman)"),
    ("stonewalling", "Stonewalling"),
    ("gaslighting", "Gaslighting"),
    ("blame-shifting", "Blame-Shifting"),
    ("defensiveness", "Defensiveness"),
    ("criticism-vs-complaint", "Criticism vs Complaint"),
    ("passive-aggression", "Passive-Aggression"),
    ("giving-to-get", "Giving to Get"),
    ("growing-to-get", "Growing to Get"),
    ("cake-eating", "Cake-Eating"),
    ("tone-policing", "Tone Policing"),
    ("projection", "Projection"),
    ("minimizing", "Minimizing"),
    ("love-bombing", "Love Bombing"),
    ("darvo", "DARVO"),
    ("triangulation", "Triangulation"),
    ("emotional-reasoning", "Emotional Reasoning"),
    ("pursue-withdraw-cycle", "Pursue-Withdraw Cycle"),
    ("agree-then-backtrack", "Agree-Then-Backtrack Pattern"),
]

# Extended pattern list (common relationship anti-patterns)
extended_patterns = [
    ("silent-treatment", "Silent Treatment"),
    ("weaponized-incompetence", "Weaponized Incompetence"),
    ("moving-goalposts", "Moving the Goalposts"),
    ("sea-lioning", "Sea-Lioning"),
    ("catastrophizing", "Catastrophizing"),
    ("all-or-nothing", "All-or-Nothing Thinking"),
    ("overgeneralization", "Overgeneralization"),
    ("mind-reading", "Mind Reading"),
    ("fortune-telling", "Fortune Telling"),
    ("should-statements", "Should Statements"),
    ("labeling", "Labeling"),
    ("personalization", "Personalization"),
    ("mental-filtering", "Mental Filtering"),
    ("disqualifying-positive", "Disqualifying the Positive"),
    ("magnification-minimization", "Magnification / Minimization"),
    ("emotional-blackmail", "Emotional Blackmail"),
    ("guilting", "Guilting"),
    ("parentification", "Parentification"),
    ("enmeshment", "Enmeshment"),
    ("codependent-rescuing", "Codependent Rescuing"),
    ("walking-on-eggshells", "Walking on Eggshells"),
    ("intermittent-reinforcement", "Intermittent Reinforcement"),
    ("idealize-devalue-discard", "Idealize-Devalue-Discard Cycle"),
    ("splitting-black-white", "Splitting (Black-and-White Thinking)"),
    ("trauma-bonding", "Trauma Bonding"),
    ("financial-abuse", "Financial Abuse"),
    ("isolation-tactics", "Isolation Tactics"),
    ("double-bind", "Double Bind"),
    ("scapegoating", "Scapegoating"),
    ("golden-child-dynamic", "Golden Child Dynamic"),
    ("emotional-incest", "Emotional Incest / Covert Incest"),
    ("people-pleasing-pattern", "People-Pleasing as Pattern"),
    ("conflict-avoidance", "Conflict Avoidance"),
    ("fawning", "Fawning (Trauma Response)"),
    ("hypervigilance", "Hypervigilance"),
    ("dissociation-pattern", "Dissociation Pattern"),
    ("demand-comply", "Demand-Comply Pattern"),
    ("attack-defend", "Attack-Defend Pattern"),
    ("withdraw-withdraw", "Withdraw-Withdraw Pattern"),
    ("flooding-pattern", "Flooding Pattern"),
    ("negative-sentiment-override", "Negative Sentiment Override"),
    ("betrayal-trauma", "Betrayal Trauma Pattern"),
    ("coercive-control", "Coercive Control"),
    ("flying-monkeys", "Flying Monkeys"),
    ("hoovering", "Hoovering"),
    ("grey-rocking-response", "Grey Rocking (Response Pattern)"),
    ("fomo-relationship", "FOMO in Relationships"),
    ("comparison-trap", "Comparison Trap"),
    ("sunk-cost-fallacy-relationship", "Sunk Cost Fallacy in Relationships"),
    ("reactivity-pattern", "Reactivity Pattern"),
    ("over-functioning-under-functioning", "Over-Functioning / Under-Functioning"),
    ("anxious-avoidant-trap", "Anxious-Avoidant Trap"),
    ("protest-behavior", "Protest Behavior"),
    ("deactivating-strategies", "Deactivating Strategies"),
    ("phantom-ex", "Phantom Ex"),
    ("grass-is-greener", "Grass Is Greener Syndrome"),
    ("white-knighting", "White Knighting"),
    ("savior-complex", "Savior Complex"),
    ("martyr-complex", "Martyr Complex"),
    ("victim-mentality", "Victim Mentality"),
    ("boundary-violation-dismissal", "Boundary Violation Dismissal"),
]

for p_id, p_name in priority_patterns:
    add(f"pattern-{p_id}", f"{p_name} -- Pattern Encyclopedia Page", "pattern", "knowledge_web", "p0", [])

for p_id, p_name in extended_patterns:
    add(f"pattern-{p_id}", f"{p_name} -- Pattern Encyclopedia Page", "pattern", "knowledge_web", "p1", [])

# ============================================================
# 6. GOTTMAN PATTERN PAGES (specific from project_gottman_pattern_pages.md)
# ============================================================
gottman_patterns = [
    ("gottman-bids-attention", "Bids for Attention -- Turning Toward/Away/Against"),
    ("gottman-flooding-dpa", "Flooding / Diffuse Physiological Arousal"),
    ("gottman-5-1-ratio", "The 5:1 Positive-to-Negative Ratio"),
    ("gottman-repair-attempts", "Repair Attempts -- The #1 Predictor"),
    ("gottman-gridlocked-conflicts", "Gridlocked (Perpetual) Conflicts"),
    ("gottman-four-horsemen-cascade", "The Four Horsemen Cascade"),
]
for g_id, g_name in gottman_patterns:
    add(g_id, f"{g_name} -- Deep Pattern Page", "pattern", "knowledge_web", "p0", [])

# ============================================================
# 7. TRAUMA LIFECYCLE PAGES
# ============================================================
traumas = [
    ("childhood-emotional-neglect", "Childhood Emotional Neglect"),
    ("childhood-physical-abuse", "Childhood Physical Abuse"),
    ("childhood-sexual-abuse", "Childhood Sexual Abuse"),
    ("emotional-parentification", "Emotional Parentification"),
    ("instrumental-parentification", "Instrumental Parentification"),
    ("narcissistic-parent", "Narcissistic Parent(s)"),
    ("alcoholic-addicted-parent", "Alcoholic / Addicted Parent(s)"),
    ("divorce-family-dissolution", "Divorce / Family Dissolution"),
    ("abandonment-physical", "Abandonment (Physical)"),
    ("abandonment-emotional", "Abandonment (Emotional)"),
    ("enmeshment-boundaryless-family", "Enmeshment / Boundary-less Family"),
    ("conditional-love", "Conditional Love"),
    ("perfectionism-demanding-environment", "Perfectionism-Demanding Environment"),
    ("bullying-peer-sibling-parental", "Bullying (Peer, Sibling, or Parental)"),
    ("medical-trauma-childhood", "Medical Trauma in Childhood"),
    ("poverty-financial-instability", "Poverty / Financial Instability"),
    ("chaotic-unpredictable-environment", "Chaotic / Unpredictable Environment"),
    ("loss-parent-sibling-childhood", "Loss of Parent or Sibling in Childhood"),
    ("religious-trauma", "Religious Trauma"),
    ("cultural-racial-trauma", "Cultural / Racial Trauma"),
    ("immigration-displacement-trauma", "Immigration / Displacement Trauma"),
]
for t_id, t_name in traumas:
    add(f"trauma-{t_id}", f"{t_name} -- Trauma Lifecycle Page", "crisis", "knowledge_web", "p0", [])

# ============================================================
# 8. SUICIDALITY / CRISIS PAGES
# ============================================================
crisis_queries = [
    ("i-want-to-die", "I Want to Die"),
    ("is-life-worth-living", "Is Life Worth Living"),
    ("should-i-kill-myself", "Should I Kill Myself"),
    ("i-cant-take-it-anymore", "I Can't Take It Anymore"),
    ("no-one-would-miss-me", "No One Would Miss Me"),
    ("permanent-solution-temporary-problems", "Permanent Solution to Temporary Problems"),
    ("i-have-nothing-to-live-for", "I Have Nothing to Live For"),
    ("why-shouldnt-i-kill-myself", "Why Shouldn't I Kill Myself"),
    ("im-a-burden", "I'm a Burden to Everyone"),
    ("world-better-without-me", "The World Would Be Better Without Me"),
    ("how-to-stop-wanting-to-die", "How to Stop Wanting to Die"),
    ("dont-want-to-die-want-pain-to-stop", "I Don't Want to Die, I Just Want the Pain to Stop"),
]
for c_id, c_name in crisis_queries:
    add(f"crisis-{c_id}", f"{c_name} -- Crisis Response Page", "crisis", "knowledge_web", "p0", [])

# ============================================================
# 9. DSM CONDITION PAGES
# ============================================================
dsm_conditions = [
    # Neurodevelopmental
    ("dsm-adhd", "ADHD -- Relationship Impact"),
    ("dsm-asd", "Autism Spectrum Disorder -- Relationship Impact"),
    ("dsm-learning-disorders", "Learning Disorders -- Relationship Impact"),
    ("dsm-intellectual-disability", "Intellectual Disability -- Relationship Impact"),
    ("dsm-communication-disorders", "Communication Disorders -- Relationship Impact"),
    ("dsm-motor-disorders", "Motor Disorders -- Relationship Impact"),
    ("dsm-tic-disorders", "Tic Disorders -- Relationship Impact"),
    # Schizophrenia spectrum
    ("dsm-schizophrenia", "Schizophrenia -- Relationship Impact"),
    ("dsm-schizoaffective", "Schizoaffective Disorder -- Relationship Impact"),
    ("dsm-schizophreniform", "Schizophreniform -- Relationship Impact"),
    ("dsm-delusional", "Delusional Disorder -- Relationship Impact"),
    ("dsm-brief-psychotic", "Brief Psychotic Disorder -- Relationship Impact"),
    # Bipolar
    ("dsm-bipolar-i", "Bipolar I -- Relationship Impact"),
    ("dsm-bipolar-ii", "Bipolar II -- Relationship Impact"),
    ("dsm-cyclothymic", "Cyclothymic Disorder -- Relationship Impact"),
    # Depressive
    ("dsm-mdd", "Major Depressive Disorder -- Relationship Impact"),
    ("dsm-persistent-depressive", "Persistent Depressive Disorder -- Relationship Impact"),
    ("dsm-pmdd", "PMDD -- Relationship Impact"),
    ("dsm-disruptive-mood", "Disruptive Mood Dysregulation -- Relationship Impact"),
    # Anxiety
    ("dsm-gad", "Generalized Anxiety Disorder -- Relationship Impact"),
    ("dsm-social-anxiety", "Social Anxiety -- Relationship Impact"),
    ("dsm-specific-phobias", "Specific Phobias -- Relationship Impact"),
    ("dsm-panic", "Panic Disorder -- Relationship Impact"),
    ("dsm-agoraphobia", "Agoraphobia -- Relationship Impact"),
    ("dsm-separation-anxiety", "Separation Anxiety -- Relationship Impact"),
    ("dsm-selective-mutism", "Selective Mutism -- Relationship Impact"),
    # OCD and related
    ("dsm-ocd", "OCD -- Relationship Impact"),
    ("dsm-rocd", "ROCD (Relationship OCD) -- Relationship Impact"),
    ("dsm-body-dysmorphic", "Body Dysmorphic Disorder -- Relationship Impact"),
    ("dsm-hoarding", "Hoarding Disorder -- Relationship Impact"),
    ("dsm-trichotillomania", "Trichotillomania -- Relationship Impact"),
    ("dsm-excoriation", "Excoriation Disorder -- Relationship Impact"),
    # Trauma and stressor
    ("dsm-ptsd", "PTSD -- Relationship Impact"),
    ("dsm-cptsd", "C-PTSD -- Relationship Impact"),
    ("dsm-acute-stress", "Acute Stress Disorder -- Relationship Impact"),
    ("dsm-adjustment", "Adjustment Disorders -- Relationship Impact"),
    ("dsm-prolonged-grief", "Prolonged Grief -- Relationship Impact"),
    ("dsm-rad", "Reactive Attachment Disorder -- Relationship Impact"),
    ("dsm-dsed", "Disinhibited Social Engagement Disorder -- Relationship Impact"),
    # Dissociative
    ("dsm-did", "DID -- Relationship Impact"),
    ("dsm-dissociative-amnesia", "Dissociative Amnesia -- Relationship Impact"),
    ("dsm-depersonalization", "Depersonalization/Derealization -- Relationship Impact"),
    # Somatic
    ("dsm-somatic-symptom", "Somatic Symptom Disorder -- Relationship Impact"),
    ("dsm-illness-anxiety", "Illness Anxiety Disorder -- Relationship Impact"),
    ("dsm-conversion", "Conversion Disorder -- Relationship Impact"),
    ("dsm-factitious", "Factitious Disorder -- Relationship Impact"),
    # Eating
    ("dsm-anorexia", "Anorexia Nervosa -- Relationship Impact"),
    ("dsm-bulimia", "Bulimia Nervosa -- Relationship Impact"),
    ("dsm-binge-eating", "Binge Eating Disorder -- Relationship Impact"),
    ("dsm-arfid", "ARFID -- Relationship Impact"),
    # Sleep-wake
    ("dsm-insomnia", "Insomnia -- Relationship Impact"),
    ("dsm-narcolepsy", "Narcolepsy -- Relationship Impact"),
    ("dsm-sleep-apnea", "Sleep Apnea -- Relationship Impact"),
    # Sexual dysfunctions
    ("dsm-erectile", "Erectile Dysfunction -- Relationship Impact"),
    ("dsm-female-arousal", "Female Arousal Disorder -- Relationship Impact"),
    ("dsm-delayed-ejaculation", "Delayed Ejaculation -- Relationship Impact"),
    ("dsm-early-ejaculation", "Early Ejaculation -- Relationship Impact"),
    ("dsm-genito-pelvic-pain", "Genito-Pelvic Pain -- Relationship Impact"),
    # Gender dysphoria
    ("dsm-gender-dysphoria", "Gender Dysphoria -- Relationship Impact"),
    # Impulse control
    ("dsm-odd", "ODD -- Relationship Impact"),
    ("dsm-conduct-disorder", "Conduct Disorder -- Relationship Impact"),
    ("dsm-ied", "Intermittent Explosive Disorder -- Relationship Impact"),
    # Substance
    ("dsm-alcohol-use", "Alcohol Use Disorder -- Relationship Impact"),
    ("dsm-cannabis-use", "Cannabis Use Disorder -- Relationship Impact"),
    ("dsm-opioid-use", "Opioid Use Disorder -- Relationship Impact"),
    ("dsm-stimulant-use", "Stimulant Use Disorder -- Relationship Impact"),
    # Neurocognitive
    ("dsm-alzheimers", "Alzheimer's Disease -- Relationship Impact"),
    ("dsm-tbi", "Traumatic Brain Injury -- Relationship Impact"),
    # Personality disorders
    ("dsm-paranoid-pd", "Paranoid Personality Disorder -- Relationship Impact"),
    ("dsm-schizoid-pd", "Schizoid Personality Disorder -- Relationship Impact"),
    ("dsm-schizotypal-pd", "Schizotypal Personality Disorder -- Relationship Impact"),
    ("dsm-antisocial-pd", "Antisocial Personality Disorder -- Relationship Impact"),
    ("dsm-borderline-pd", "Borderline Personality Disorder -- Relationship Impact"),
    ("dsm-histrionic-pd", "Histrionic Personality Disorder -- Relationship Impact"),
    ("dsm-narcissistic-pd", "Narcissistic Personality Disorder -- Relationship Impact"),
    ("dsm-avoidant-pd", "Avoidant Personality Disorder -- Relationship Impact"),
    ("dsm-dependent-pd", "Dependent Personality Disorder -- Relationship Impact"),
    ("dsm-ocpd", "OCPD -- Relationship Impact"),
]
for d_id, d_name in dsm_conditions:
    add(d_id, f"{d_name} -- DSM Condition Page", "landing", "knowledge_web", "p1", [])

# ============================================================
# 10. NEURODIVERGENT CLINICAL PAGES (Mirror-specific)
# ============================================================
neuro_pages = [
    ("mirror-autism", "Mirror and Autism Spectrum Users"),
    ("mirror-adhd", "Mirror and ADHD Users"),
    ("mirror-bipolar", "Mirror and Bipolar Users"),
    ("mirror-anxiety", "Mirror and Anxiety Disorder Users"),
    ("mirror-depression", "Mirror and Depression Users"),
    ("mirror-ptsd-cptsd", "Mirror and PTSD/C-PTSD Users"),
    ("mirror-bpd", "Mirror and BPD Users"),
    ("mirror-ocd-rocd", "Mirror and OCD/ROCD Users"),
    ("mirror-schizophrenia", "Mirror and Schizophrenia Spectrum Users"),
    ("mirror-neurodivergent-overview", "Mirror and Neurodivergent Users -- Overview"),
]
for n_id, n_name in neuro_pages:
    add(n_id, f"{n_name}", "landing", "knowledge_web", "p1", [])

# ============================================================
# 11. POLITICAL ENCYCLOPEDIA
# ============================================================
political_systems = [
    ("communism", "Communism"),
    ("capitalism", "Capitalism"),
    ("socialism-democratic", "Democratic Socialism"),
    ("fascism", "Fascism"),
    ("libertarianism", "Libertarianism"),
    ("theocracy", "Theocracy"),
    ("monarchy", "Monarchy"),
    ("direct-democracy", "Direct Democracy"),
    ("authoritarianism", "Authoritarianism"),
    ("anarchism", "Anarchism"),
    ("social-democracy", "Social Democracy (Nordic Model)"),
    ("neoliberalism", "Neoliberalism"),
    ("populism", "Populism"),
    ("nationalism", "Nationalism"),
]

# Each system gets: decomposition page + honest assessment + per-implementation pages
implementations = {
    "communism": ["soviet-union", "maoist-china", "khmer-rouge", "cuba", "venezuela", "vietnam", "north-korea", "yugoslavia"],
    "capitalism": ["us-capitalism", "uk-capitalism", "singapore", "chile-pinochet", "gilded-age", "post-2008"],
    "fascism": ["nazi-germany", "mussolini-italy", "franco-spain", "imperial-japan"],
    "theocracy": ["iran", "saudi-arabia", "taliban-afghanistan", "calvins-geneva"],
    "socialism-democratic": ["nordic-model", "post-war-uk", "european-social-democracies"],
}

for sys_id, sys_name in political_systems:
    add(f"pol-{sys_id}-decomp", f"{sys_name} -- Belief Decomposition", "political", "levnation_content", "p1", [])
    add(f"pol-{sys_id}-assessment", f"{sys_name} -- Honest Assessment", "political", "levnation_content", "p1", [f"pol-{sys_id}-decomp"])
    if sys_id in implementations:
        for impl in implementations[sys_id]:
            add(f"pol-{sys_id}-impl-{impl}", f"{sys_name} -- {impl.replace('-', ' ').title()} Implementation", "political", "levnation_content", "p2", [f"pol-{sys_id}-decomp"])

# ============================================================
# 12. BELIEF DECOMPOSITION PAGES (945 beliefs across 6 domains)
# ============================================================
belief_domains = {
    "parenting": [
        "strict-discipline-necessary", "gentle-parenting-best", "children-seen-not-heard",
        "spare-rod-spoil-child", "children-are-resilient", "parents-know-best",
        "children-should-be-free", "helicopter-parenting-harmful", "attachment-parenting",
        "authoritative-best-style", "children-need-structure", "children-should-respect-elders",
        "participation-trophies-harmful", "screen-time-dangerous", "homeschooling-superior",
    ],
    "relationships": [
        "love-unconditional", "trust-must-be-earned", "people-can-change",
        "once-cheater-always-cheater", "opposites-attract", "love-at-first-sight",
        "soulmates-exist", "happy-wife-happy-life", "never-go-to-bed-angry",
        "relationships-take-work", "love-is-enough", "you-complete-me",
        "jealousy-means-love", "absence-makes-heart-grow-fonder",
        "love-is-patient-love-is-kind",
    ],
    "gender": [
        "men-should-be-providers", "gender-is-spectrum", "traditional-femininity-valuable",
        "toxic-masculinity-real", "men-and-women-equal", "patriarchy-exists",
        "wage-gap-myth", "biological-sex-determines-roles", "gender-roles-cultural",
        "feminism-went-too-far", "men-cant-be-feminists", "boys-will-be-boys",
        "women-more-emotional", "men-dont-cry",
    ],
    "politics": [
        "free-markets-best-outcomes", "government-should-provide-healthcare",
        "immigration-strengthens-nations", "death-penalty-justified",
        "gun-control-saves-lives", "taxes-are-theft", "democracy-best-system",
        "socialism-always-fails", "capitalism-exploitative", "meritocracy-exists",
        "systemic-racism-exists", "police-are-necessary", "universal-basic-income",
        "climate-change-human-caused", "border-security-essential",
    ],
    "religion": [
        "faith-without-evidence-virtue", "morality-requires-god",
        "organized-religion-harmful", "all-religions-lead-to-god",
        "bible-literal-word-of-god", "afterlife-exists", "prayer-works",
        "religion-source-of-wars", "science-and-religion-compatible",
        "atheism-requires-faith-too", "spiritual-not-religious-valid",
        "hell-exists", "karma-is-real", "everything-happens-for-reason",
    ],
    "health": [
        "vaccines-safe-effective", "natural-remedies-superior",
        "mental-health-as-important-as-physical", "therapy-is-for-weak",
        "antidepressants-overprescribed", "exercise-cures-depression",
        "addiction-is-disease", "addiction-is-choice", "obesity-personal-responsibility",
        "healthcare-is-a-right", "pharmaceutical-companies-corrupt",
        "alternative-medicine-valid", "mental-illness-overdiagnosed",
    ],
}

for domain, beliefs in belief_domains.items():
    for belief_slug in beliefs:
        add(f"belief-{domain}-{belief_slug}", f"Belief: {belief_slug.replace('-', ' ').title()} ({domain})", "belief", "trueassess_content", "p2", [])

# ============================================================
# 13. COMPARISON PAGES
# ============================================================
comparisons = [
    ("mbti-vs-big-five", "MBTI vs Big Five"),
    ("mbti-vs-enneagram", "MBTI vs Enneagram"),
    ("big-five-vs-disc", "Big Five vs DISC"),
    ("enneagram-vs-disc", "Enneagram vs DISC"),
    ("big-five-vs-enneagram", "Big Five vs Enneagram"),
    ("attachment-style-vs-love-languages", "Attachment Style vs Love Languages"),
    ("cliftonstrengths-vs-via", "CliftonStrengths vs VIA Character Strengths"),
    ("cbt-vs-act", "CBT vs ACT"),
    ("cbt-vs-dbt", "CBT vs DBT"),
    ("eft-vs-gottman", "EFT vs Gottman Method"),
    ("stoicism-vs-buddhism", "Stoicism vs Buddhism"),
    ("emdr-vs-cpt", "EMDR vs CPT"),
    ("ifs-vs-schema-therapy", "IFS vs Schema Therapy"),
    ("act-vs-dbt", "ACT vs DBT"),
    ("kolbe-vs-disc", "Kolbe vs DISC"),
    ("mbti-vs-cliftonstrengths", "MBTI vs CliftonStrengths"),
    ("big-five-vs-cliftonstrengths", "Big Five vs CliftonStrengths"),
    ("enneagram-vs-mbti", "Enneagram vs MBTI"),
    ("love-languages-vs-attachment", "Love Languages vs Attachment Theory"),
    ("ifs-vs-ego-state", "IFS vs Ego State Therapy"),
]
for c_id, c_name in comparisons:
    add(f"compare-{c_id}", f"{c_name} -- Comparison Page", "comparison", "trueassess_content", "p2", [])

# ============================================================
# 14. "AM I A..." PAGES
# ============================================================
am_i_pages = [
    ("am-i-narcissist", "Am I a Narcissist?"),
    ("am-i-codependent", "Am I Codependent?"),
    ("am-i-autistic", "Am I Autistic?"),
    ("am-i-introvert", "Am I an Introvert?"),
    ("am-i-empath", "Am I an Empath?"),
    ("am-i-people-pleaser", "Am I a People Pleaser?"),
    ("am-i-adhd", "Do I Have ADHD?"),
    ("am-i-depressed", "Am I Depressed?"),
    ("am-i-anxious", "Do I Have Anxiety?"),
    ("am-i-bipolar", "Am I Bipolar?"),
    ("am-i-borderline", "Do I Have BPD?"),
    ("am-i-hsp", "Am I Highly Sensitive?"),
    ("am-i-trauma-bonded", "Am I Trauma Bonded?"),
    ("am-i-in-toxic-relationship", "Am I in a Toxic Relationship?"),
    ("am-i-gaslighted", "Am I Being Gaslighted?"),
    ("am-i-emotionally-abused", "Am I Being Emotionally Abused?"),
    ("am-i-love-bombed", "Am I Being Love Bombed?"),
    ("am-i-avoidant", "Am I Avoidant?"),
    ("am-i-anxious-attachment", "Do I Have Anxious Attachment?"),
    ("am-i-insecure", "Am I Insecure?"),
    ("am-i-controlling", "Am I Controlling?"),
    ("am-i-manipulative", "Am I Manipulative?"),
    ("am-i-toxic", "Am I Toxic?"),
    ("am-i-emotionally-unavailable", "Am I Emotionally Unavailable?"),
    ("am-i-commitment-phobe", "Am I a Commitment-Phobe?"),
    ("am-i-passive-aggressive", "Am I Passive-Aggressive?"),
    ("am-i-perfectionist", "Am I a Perfectionist?"),
    ("am-i-burnout", "Am I Burned Out?"),
    ("am-i-having-midlife-crisis", "Am I Having a Midlife Crisis?"),
    ("am-i-in-cult", "Am I in a Cult?"),
]
for a_id, a_name in am_i_pages:
    add(a_id, f"{a_name} -- Self-Assessment Landing Page", "landing", "trueassess_content", "p1", [])

# ============================================================
# 15. MIRROR KNOWLEDGE WEB PAGES (growth axes, concepts)
# ============================================================
mirror_concepts = [
    ("mirror-how-it-works", "How Mirror Works -- Technical Explanation"),
    ("mirror-pattern-detection", "Pattern Detection -- How Mirror Sees Your Patterns"),
    ("mirror-game-film", "Game Film Review -- Backward-Chain Analysis"),
    ("mirror-growth-axes", "Growth Axes -- The Journey Map"),
    ("mirror-philosophical-foundation", "Philosophical Foundation -- Why This Works"),
    ("mirror-act-axis", "ACT Growth Axis -- Psychological Flexibility"),
    ("mirror-de-mello-axis", "de Mello Growth Axis -- Awareness & Detachment"),
    ("mirror-aurelius-axis", "Aurelius Growth Axis -- Stoic Resilience"),
    ("mirror-jung-axis", "Jung Growth Axis -- Shadow Integration"),
    ("mirror-nvc-axis", "NVC Growth Axis -- Compassionate Communication"),
    ("mirror-boundaries-axis", "Boundaries Growth Axis -- Healthy Limits"),
    ("mirror-tolle-axis", "Tolle Growth Axis -- Present-Moment Awareness"),
    ("mirror-frankl-axis", "Frankl Growth Axis -- Meaning & Purpose"),
    ("mirror-van-der-kolk-axis", "van der Kolk Growth Axis -- Body-Based Healing"),
    ("mirror-goleman-axis", "Goleman Growth Axis -- Emotional Intelligence"),
    ("mirror-gibson-axis", "Gibson Growth Axis -- Attachment Reprogramming"),
    ("mirror-bishop-axis", "Bishop Growth Axis -- Radical Self-Accountability"),
    ("mirror-nguyen-axis", "Nguyen Growth Axis -- Thought vs Awareness"),
    ("mirror-carter-axis", "Carter Growth Axis -- Healthy Assertiveness"),
    ("mirror-diagnostic-chains", "Diagnostic Chains -- How Mirror Traces Problems to Roots"),
    ("mirror-evidence-architecture", "Evidence Architecture -- Proof That Growth Works"),
    ("mirror-skill-taxonomy", "Relationship Skill Taxonomy -- What You'll Learn"),
    ("mirror-ai-coaching-philosophy", "AI Coaching Philosophy -- Not Therapy, Not Advice"),
    ("mirror-conversation-import", "Conversation Import -- Bring Your Real Conversations"),
]
for m_id, m_name in mirror_concepts:
    add(m_id, f"{m_name}", "skill", "knowledge_web", "p1", [])

# ============================================================
# 16. CITY PAGES (levciti) — seed the top 50 cities
# ============================================================
top_cities = [
    "new-york", "los-angeles", "chicago", "houston", "phoenix",
    "philadelphia", "san-antonio", "san-diego", "dallas", "san-jose",
    "austin", "jacksonville", "san-francisco", "columbus", "charlotte",
    "indianapolis", "seattle", "denver", "washington-dc", "nashville",
    "oklahoma-city", "el-paso", "boston", "portland", "las-vegas",
    "memphis", "louisville", "baltimore", "milwaukee", "albuquerque",
    "tucson", "fresno", "sacramento", "mesa", "kansas-city",
    "atlanta", "omaha", "colorado-springs", "raleigh", "long-beach",
    "virginia-beach", "miami", "oakland", "minneapolis", "tulsa",
    "tampa", "arlington", "new-orleans", "cleveland", "detroit",
]
for city in top_cities:
    add(f"city-{city}", f"{city.replace('-', ' ').title()} -- City Page", "landing", "levciti_content", "p2", [])

# ============================================================
# 17. CONTROVERSY CLASSES (levnation)
# ============================================================
controversy_classes = [
    ("immigration-policy", "Immigration Policy"),
    ("gun-control-rights", "Gun Control / Gun Rights"),
    ("abortion-rights", "Abortion Rights"),
    ("healthcare-system", "Healthcare System"),
    ("education-policy", "Education Policy"),
    ("climate-policy", "Climate Policy"),
    ("policing-criminal-justice", "Policing / Criminal Justice Reform"),
    ("taxation-wealth-inequality", "Taxation / Wealth Inequality"),
    ("free-speech-censorship", "Free Speech / Censorship"),
    ("religious-freedom-secularism", "Religious Freedom / Secularism"),
    ("gender-identity-policy", "Gender Identity Policy"),
    ("drug-policy", "Drug Policy / Legalization"),
    ("housing-homelessness", "Housing / Homelessness"),
    ("trade-tariffs", "Trade / Tariffs"),
    ("foreign-policy-military", "Foreign Policy / Military"),
    ("technology-privacy", "Technology / Privacy"),
    ("election-integrity", "Election Integrity / Voting Rights"),
    ("ai-regulation", "AI Regulation"),
    ("labor-rights-unions", "Labor Rights / Unions"),
    ("environmental-regulation", "Environmental Regulation"),
]
for cc_id, cc_name in controversy_classes:
    add(f"controversy-{cc_id}", f"{cc_name} -- Controversy Class Template", "political", "levnation_content", "p2", [])

# ============================================================
# 18. B2B INDUSTRY VERTICAL LANDING PAGES
# ============================================================
industries = [
    "law-firms", "medical-practices", "dental-practices", "startups",
    "engineering-teams", "sales-teams", "executive-teams", "boards-of-directors",
    "nonprofits", "accounting-firms", "consulting-firms", "real-estate-teams",
    "financial-advisors", "agencies", "construction", "restaurants",
    "healthcare-teams", "retail-management", "church-staff", "family-businesses",
    "franchises", "venture-capital", "pe-portfolio", "professional-services",
]
for ind in industries:
    add(f"b2b-{ind}", f"{ind.replace('-', ' ').title()} -- B2B Landing Page", "landing", "trueassess_content", "p2", [])

# ============================================================
# 19. CORE 15 SKILL FRAMEWORK DEEP PAGES
# ============================================================
core_frameworks = [
    ("skill-aurelius", "Marcus Aurelius / Stoicism -- Skill Framework Deep Page"),
    ("skill-de-mello", "Anthony de Mello -- Skill Framework Deep Page"),
    ("skill-hayes-act", "Steven Hayes / ACT -- Skill Framework Deep Page"),
    ("skill-jung", "Carl Jung / Shadow Work -- Skill Framework Deep Page"),
    ("skill-gibson-attachment", "Thais Gibson / Attachment -- Skill Framework Deep Page"),
    ("skill-rosenberg-nvc", "Marshall Rosenberg / NVC -- Skill Framework Deep Page"),
    ("skill-cloud-boundaries", "Henry Cloud / Boundaries -- Skill Framework Deep Page"),
    ("skill-tolle", "Eckhart Tolle / Power of Now -- Skill Framework Deep Page"),
    ("skill-bishop", "Gary John Bishop / Radical Accountability -- Skill Framework Deep Page"),
    ("skill-frankl", "Viktor Frankl / Meaning -- Skill Framework Deep Page"),
    ("skill-nguyen", "Joseph Nguyen / Thought vs Awareness -- Skill Framework Deep Page"),
    ("skill-carter", "Dr. Les Carter / Healthy Assertiveness -- Skill Framework Deep Page"),
    ("skill-van-der-kolk", "Bessel van der Kolk / Body-Based Healing -- Skill Framework Deep Page"),
    ("skill-goleman", "Daniel Goleman / Emotional Intelligence -- Skill Framework Deep Page"),
]
for sf_id, sf_name in core_frameworks:
    add(sf_id, sf_name, "skill", "knowledge_web", "p0", [])

# ============================================================
# BUILD SUMMARY
# ============================================================
by_type = {}
by_pipeline = {}
by_priority = {}
for t in tickets:
    by_type[t["type"]] = by_type.get(t["type"], 0) + 1
    by_pipeline[t["pipeline"]] = by_pipeline.get(t["pipeline"], 0) + 1
    by_priority[t["priority"]] = by_priority.get(t["priority"], 0) + 1

output = {
    "generated_at": datetime.utcnow().isoformat() + "Z",
    "total_tickets": len(tickets),
    "tickets": tickets,
    "summary": {
        "by_type": dict(sorted(by_type.items())),
        "by_pipeline": dict(sorted(by_pipeline.items())),
        "by_priority": dict(sorted(by_priority.items())),
    }
}

with open("/Users/user/personal/sb/trueassess/priv/data/content_backlog.json", "w") as f:
    json.dump(output, f, indent=2)

print(f"Total tickets: {len(tickets)}")
print(f"\nBy type: {json.dumps(by_type, indent=2)}")
print(f"\nBy pipeline: {json.dumps(by_pipeline, indent=2)}")
print(f"\nBy priority: {json.dumps(by_priority, indent=2)}")
