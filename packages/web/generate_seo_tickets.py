#!/usr/bin/env python3
"""Generate SEO landing page tickets for every content page in the knowledge web."""

import json
import re
from datetime import datetime, timezone

# Load all backlog tickets
with open('/Users/user/personal/sb/trueassess/priv/data/content_backlog.json') as f:
    backlog = json.load(f)

by_type = {}
for t in backlog['tickets']:
    tp = t['type']
    if tp not in by_type:
        by_type[tp] = []
    by_type[tp].append(t)

tickets = []
search_term_count = 0

def slug(s):
    """Convert string to URL slug."""
    return re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')

def add_ticket(ticket_slug, title, target_page, search_terms, intent, priority, category=None):
    global search_term_count
    search_term_count += len(search_terms)
    t = {
        "slug": ticket_slug,
        "title": title,
        "type": "landing",
        "target_page": target_page,
        "search_terms": search_terms,
        "search_intent": intent,
        "priority": priority,
        "pipeline": "trueassess_content"
    }
    if category:
        t["category"] = category
    tickets.append(t)


# ============================================================
# EVIDENCE PAGES (81) - ~5 landing pages each
# ============================================================

# Human-readable names for evidence page slugs
evidence_names = {
    "attachment_style": "Attachment Style",
    "act_flexibility": "ACT Psychological Flexibility",
    "cognitive_distortions": "Cognitive Distortions",
    "detachment_awareness": "Detachment / de Mello Awareness",
    "emotional_regulation": "Emotional Regulation",
    "shadow_integration": "Shadow Work",
    "trauma_responses": "Trauma Responses (4F Model)",
    "triggers_profile": "Triggers Profile",
    "daddy_issues": "Daddy Issues / Father Wound",
    "big_five": "Big Five / OCEAN Personality",
    "enneagram": "Enneagram",
    "mbti": "MBTI / Myers-Briggs",
    "disc": "DISC Profile",
    "cliftonstrengths": "CliftonStrengths",
    "love_languages": "Love Languages",
    "kolbe": "Kolbe Instinct Profile",
    "carol_tuttle": "Carol Tuttle Energy Profiling",
    "via_strengths": "VIA Character Strengths",
    "stoicism": "Stoicism Assessment",
    "nietzsche": "Nietzsche Assessment",
    "existentialism": "Existentialism Assessment",
    "buddhism": "Buddhism Assessment",
    "pragmatism": "Pragmatism Assessment",
    "communication_gottman": "Gottman Communication Skills",
    "boundary_capacity": "Boundary Capacity",
    "conflict_navigation": "Conflict Navigation",
    "repair_skills": "Repair Skills",
    "vulnerability_capacity": "Vulnerability Capacity",
    "age_gap_compatibility": "Age Gap Compatibility",
    "narcissism_spectrum": "Narcissism Spectrum",
    "empathy": "Empathy",
    "learning_strategies": "Learning Strategies",
    "adhd": "ADHD",
    "autism_spectrum": "Autism Spectrum",
    "alexithymia": "Alexithymia",
    "borderline_traits": "Borderline Traits",
    "codependency": "Codependency",
    "dark_triad": "Dark Triad",
    "hsp": "Highly Sensitive Person (HSP)",
    "people_pleasing": "People Pleasing",
    "perfectionism": "Perfectionism",
    "trauma_cptsd": "Trauma / C-PTSD",
    "anxiety_depression_screen": "Anxiety and Depression",
    "forgiveness_profile": "Forgiveness",
    "communication_profile": "Communication Style",
    "dashboard_light_profile": "Dashboard Light Profile",
    "relationship_expectations": "Relationship Expectations",
    "values_real_vs_aspirational": "Real vs Aspirational Values",
    "bdsm_dynamics": "BDSM Dynamics",
    "fetish_assessment": "Fetish Assessment",
    "kink_matching": "Kink Matching",
    "purity_test": "Purity Test",
    "self_awareness": "Self-Awareness",
    "self_worth": "Self-Worth",
    "self_respect": "Self-Respect",
    "authenticity": "Authenticity",
    "groupthink_tendency": "Groupthink Tendency",
    "magical_thinking": "Magical Thinking",
    "emotional_intelligence": "Emotional Intelligence",
    "iq_assessment": "IQ Assessment",
    "relationship_commitments": "Relationship Commitments",
    "purpose_assessment": "Purpose / Life Purpose",
    "mindfulness_spirituality": "Mindfulness and Spirituality",
    "swot_per_axis": "Personal SWOT Analysis",
    "presuppositions_assessment": "Presuppositions",
    "pattern_recognition_profile": "Pattern Recognition",
    "regulation_profile": "Regulation Profile",
    "identity_self_worth_profile": "Identity and Self-Worth",
    "longevity": "Longevity",
    "aging": "Aging",
    "fitness": "Fitness",
    "active_lifestyle": "Active Lifestyle",
    "skills_hobbies_interests": "Skills, Hobbies and Interests",
    "adulting_maturity": "Adulting / Maturity",
    "life_skills": "Life Skills",
    "traditional_feminist_spectrum": "Traditional-Feminist Spectrum",
    "traditional_marxist_male": "Traditional-Marxist Male Spectrum",
    "hot_crazy_matrix": "Hot Crazy Matrix",
    "false_accusation_risk": "False Accusation Risk",
    "appearance_self_rating": "Appearance Self-Rating",
    "suicidality_reflectance": "Suicidality Assessment",
}

for item in by_type.get('evidence', []):
    ev_slug = item['slug'].replace('-evidence', '')
    name = evidence_names.get(ev_slug, item['title'].replace(' -- Evidence Evaluation', ''))
    target = item['slug']

    name_lower = name.lower()

    # Template 1: "Is [X] reliable?"
    add_ticket(
        f"seo-is-{slug(name)}-reliable",
        f"Is {name} Reliable? What the Research Actually Says",
        target,
        [f"is {name_lower} reliable", f"{name_lower} reliability", f"is {name_lower} accurate", f"{name_lower} accuracy research"],
        "informational", "p1", "evidence-reliability"
    )

    # Template 2: "Scientific evidence for [X]"
    add_ticket(
        f"seo-{slug(name)}-scientific-evidence",
        f"{name}: What Does the Science Actually Say?",
        target,
        [f"{name_lower} scientific evidence", f"{name_lower} research studies", f"{name_lower} peer reviewed", f"is {name_lower} backed by science"],
        "informational", "p1", "evidence-science"
    )

    # Template 3: "[X] validity"
    add_ticket(
        f"seo-{slug(name)}-validity",
        f"{name} Validity and Reliability: A Complete Review",
        target,
        [f"{name_lower} validity", f"{name_lower} test-retest reliability", f"{name_lower} psychometric properties", f"{name_lower} construct validity"],
        "informational", "p2", "evidence-validity"
    )

    # Template 4: "[X] criticism"
    add_ticket(
        f"seo-{slug(name)}-criticism",
        f"{name} Criticism: Legitimate Concerns and What They Mean",
        target,
        [f"{name_lower} criticism", f"{name_lower} problems", f"{name_lower} debunked", f"why {name_lower} is wrong", f"{name_lower} flaws"],
        "informational", "p2", "evidence-criticism"
    )

    # Template 5: "How accurate is [X]?"
    add_ticket(
        f"seo-how-accurate-{slug(name)}",
        f"How Accurate Is {name}? An Honest Assessment",
        target,
        [f"how accurate is {name_lower}", f"{name_lower} accuracy rate", f"can you trust {name_lower}", f"{name_lower} false results"],
        "informational", "p1", "evidence-accuracy"
    )


# ============================================================
# FRAMEWORK PAGES (175) - ~4 landing pages each
# ============================================================

# Parse framework names from titles
for item in by_type.get('framework', []):
    fw_slug = item['slug']
    title = item['title']
    target = fw_slug

    # Extract clean framework name
    if ' -- ' in title:
        name = title.split(' -- ')[0].strip()
    else:
        name = title

    # Remove parenthetical abbreviations for search terms but keep for display
    name_clean = re.sub(r'\s*\([^)]*\)\s*', ' ', name).strip()
    name_lower = name_clean.lower()

    # Extract abbreviation if present
    abbrev = None
    abbrev_match = re.search(r'\(([A-Z]{2,})\)', title)
    if abbrev_match:
        abbrev = abbrev_match.group(1)

    # Is this a pathway page or deep framework page?
    is_pathway = 'pathway' in fw_slug

    # Template 1: "What is [X]?"
    terms = [f"what is {name_lower}", f"{name_lower} explained", f"{name_lower} definition"]
    if abbrev:
        terms.extend([f"what is {abbrev.lower()}", f"{abbrev.lower()} therapy", f"{abbrev.lower()} explained"])
    add_ticket(
        f"seo-what-is-{slug(name_clean)}",
        f"What Is {name}? A Clear Explanation",
        target, terms, "informational", "p1", "framework-definition"
    )

    # Template 2: "Does [X] work?"
    terms2 = [f"does {name_lower} work", f"{name_lower} effectiveness", f"is {name_lower} effective", f"{name_lower} success rate"]
    if abbrev:
        terms2.append(f"does {abbrev.lower()} work")
    add_ticket(
        f"seo-does-{slug(name_clean)}-work",
        f"Does {name} Actually Work? Evidence Review",
        target, terms2, "informational", "p1", "framework-effectiveness"
    )

    # Template 3: "[X] exercises/techniques"
    terms3 = [f"{name_lower} exercises", f"{name_lower} techniques", f"{name_lower} activities", f"how to practice {name_lower}"]
    if abbrev:
        terms3.append(f"{abbrev.lower()} exercises")
    add_ticket(
        f"seo-{slug(name_clean)}-exercises",
        f"{name} Exercises and Techniques You Can Try Today",
        target, terms3, "informational", "p1", "framework-exercises"
    )

    # Template 4: "[X] for [condition]" (relationships, anxiety, trauma, depression)
    if not is_pathway:
        for condition in ["relationships", "anxiety", "trauma", "depression"]:
            terms4 = [f"{name_lower} for {condition}", f"can {name_lower} help with {condition}"]
            if abbrev:
                terms4.append(f"{abbrev.lower()} for {condition}")
            add_ticket(
                f"seo-{slug(name_clean)}-for-{condition}",
                f"{name} for {condition.title()}: How It Helps and What to Expect",
                target, terms4, "informational", "p2", "framework-application"
            )


# ============================================================
# PATTERN PAGES (131) - ~5 landing pages each
# ============================================================

for item in by_type.get('pattern', []):
    pat_slug = item['slug']
    title = item['title']
    target = pat_slug

    # Extract clean pattern name
    if ' -- ' in title:
        name = title.split(' -- ')[0].strip()
    else:
        name = title

    name_clean = re.sub(r'\s*\([^)]*\)\s*', ' ', name).strip()
    name_lower = name_clean.lower()

    # Template 1: "Why do I [pattern]?" / "Am I [pattern]?"
    add_ticket(
        f"seo-am-i-{slug(name_clean)}",
        f"Am I {name_clean}? Signs, Examples, and What It Really Means",
        target,
        [f"am I {name_lower}", f"signs of {name_lower}", f"{name_lower} signs", f"how to tell if someone is {name_lower}", f"{name_lower} examples"],
        "informational", "p1", "pattern-identification"
    )

    # Template 2: "What is [pattern]?"
    add_ticket(
        f"seo-what-is-{slug(name_clean)}",
        f"What Is {name_clean}? Definition, Examples, and Why It Happens",
        target,
        [f"what is {name_lower}", f"{name_lower} meaning", f"{name_lower} definition", f"{name_lower} explained"],
        "informational", "p1", "pattern-definition"
    )

    # Template 3: "How to stop [pattern]"
    add_ticket(
        f"seo-how-to-stop-{slug(name_clean)}",
        f"How to Stop {name_clean}: Practical Steps That Actually Work",
        target,
        [f"how to stop {name_lower}", f"how to deal with {name_lower}", f"{name_lower} how to respond", f"what to do about {name_lower}"],
        "informational", "p1", "pattern-solution"
    )

    # Template 4: "[pattern] in relationships"
    add_ticket(
        f"seo-{slug(name_clean)}-in-relationships",
        f"{name_clean} in Relationships: What It Looks Like and What to Do",
        target,
        [f"{name_lower} in relationships", f"my partner does {name_lower}", f"{name_lower} relationship", f"is {name_lower} abusive"],
        "informational", "p1", "pattern-relationships"
    )

    # Template 5: "Why does my partner [pattern]?"
    add_ticket(
        f"seo-why-partner-{slug(name_clean)}",
        f"Why Does My Partner {name_clean}? Understanding the Psychology",
        target,
        [f"why does my partner {name_lower}", f"why does my husband {name_lower}", f"why does my wife {name_lower}", f"why do people {name_lower}"],
        "informational", "p1", "pattern-partner"
    )


# ============================================================
# BELIEF PAGES (753) - ~3-4 landing pages each
# ============================================================

for item in by_type.get('belief', []):
    bel_slug = item['slug']
    title = item['title']
    target = bel_slug

    # Extract belief name and category
    if ' -- ' in title:
        name = title.split(' -- ')[0].strip()
    else:
        name = title

    # Extract category from title
    cat_match = re.search(r'\((\w+)\)\s*$', title)
    belief_cat = cat_match.group(1) if cat_match else "general"

    # Clean the name
    name_clean = name.replace('Belief: ', '').strip()
    name_clean = re.sub(r'\s*\([^)]*\)\s*$', '', name_clean).strip()

    # Convert slug-style name to readable form
    readable = name_clean.replace('_', ' ').title()
    # Make it more natural
    readable_lower = name_clean.replace('_', ' ').lower()

    # For religious decomps (rg-*), use different templates
    if bel_slug.startswith('rg-'):
        rg_name = name_clean
        rg_lower = rg_name.lower()

        add_ticket(
            f"seo-{slug(rg_name)}-beliefs",
            f"{rg_name}: Core Beliefs, Hidden Assumptions, and What They Mean",
            target,
            [f"{rg_lower} beliefs", f"{rg_lower} what do they believe", f"understanding {rg_lower}"],
            "informational", "p2", "belief-religious"
        )

        add_ticket(
            f"seo-{slug(rg_name)}-psychology",
            f"The Psychology of Being {rg_name}",
            target,
            [f"{rg_lower} psychology", f"{rg_lower} identity", f"{rg_lower} experience"],
            "informational", "p2", "belief-religious-psychology"
        )

        add_ticket(
            f"seo-am-i-{slug(rg_name)}",
            f"Am I {rg_name}? Understanding Your Religious Identity",
            target,
            [f"am I {rg_lower}", f"{rg_lower} signs", f"what makes someone {rg_lower}"],
            "informational", "p2", "belief-religious-identity"
        )
        continue

    # For archetype decomps
    if bel_slug.endswith('-decomp') and not bel_slug.startswith('rg-') and not bel_slug.startswith('belief-'):
        arch_name = name_clean
        arch_lower = arch_name.lower()

        add_ticket(
            f"seo-what-is-{slug(arch_name)}",
            f"What Is the {arch_name}? Psychology Behind the Label",
            target,
            [f"what is {arch_lower}", f"{arch_lower} meaning", f"{arch_lower} psychology", f"am I a {arch_lower}"],
            "informational", "p1", "belief-archetype"
        )

        add_ticket(
            f"seo-{slug(arch_name)}-signs",
            f"{arch_name}: Signs, Examples, and the Beliefs Underneath",
            target,
            [f"{arch_lower} signs", f"{arch_lower} examples", f"{arch_lower} traits", f"{arch_lower} test"],
            "informational", "p1", "belief-archetype-signs"
        )

        add_ticket(
            f"seo-{slug(arch_name)}-beliefs",
            f"The Hidden Beliefs Behind the {arch_name}",
            target,
            [f"why am I a {arch_lower}", f"{arch_lower} beliefs", f"{arch_lower} childhood", f"how to stop being a {arch_lower}"],
            "informational", "p1", "belief-archetype-beliefs"
        )
        continue

    # Standard belief decompositions
    # Template 1: "Is [belief] true?"
    add_ticket(
        f"seo-is-{slug(readable)}-true",
        f"Is It True That {readable}? What Research and Philosophy Say",
        target,
        [f"is it true that {readable_lower}", f"is {readable_lower} true", f"{readable_lower} evidence", f"{readable_lower} research"],
        "informational", "p2", "belief-truth"
    )

    # Template 2: "Why do people believe [X]?"
    add_ticket(
        f"seo-why-believe-{slug(readable)}",
        f"Why Do People Believe {readable}? The Psychology of This Belief",
        target,
        [f"why do people believe {readable_lower}", f"{readable_lower} psychology", f"where does the belief {readable_lower} come from"],
        "informational", "p2", "belief-psychology"
    )

    # Template 3: "[belief] pros and cons"
    add_ticket(
        f"seo-{slug(readable)}-analysis",
        f"{readable}: Arguments For and Against",
        target,
        [f"{readable_lower} pros and cons", f"{readable_lower} arguments", f"arguments for and against {readable_lower}", f"{readable_lower} debate"],
        "informational", "p2", "belief-analysis"
    )


# ============================================================
# RELIGIOUS GROUP PAGES (48) - ~4-5 landing pages each
# ============================================================

religious_names = {}
for item in by_type.get('religious', []):
    rg_slug = item['slug']
    title = item['title']
    # Extract the name from the slug pattern rg-NAME-page
    name_part = rg_slug.replace('-page', '').replace('rg-', '')
    name = title.replace(' -- Landing Page', '').strip() if ' -- ' in title else title
    religious_names[rg_slug] = name

for item in by_type.get('religious', []):
    rg_slug = item['slug']
    name = religious_names[rg_slug]
    target = rg_slug
    name_lower = name.lower()

    # Determine the religious background for targeted search terms
    bg = ""
    if 'mormon' in name_lower or 'lds' in name_lower:
        bg = "mormon"
    elif 'jw' in name_lower or "jehovah" in name_lower:
        bg = "jehovah's witness"
    elif 'catholic' in name_lower:
        bg = "catholic"
    elif 'muslim' in name_lower or 'islam' in name_lower:
        bg = "muslim"
    elif 'jewish' in name_lower or 'judaism' in name_lower or 'orthodox' in name_lower:
        bg = "jewish"
    elif 'hindu' in name_lower:
        bg = "hindu"
    elif 'buddhist' in name_lower or 'buddhism' in name_lower:
        bg = "buddhist"
    elif 'sikh' in name_lower:
        bg = "sikh"
    elif 'scientolog' in name_lower:
        bg = "scientology"
    elif 'amish' in name_lower:
        bg = "amish"
    elif 'evangelical' in name_lower or 'exvangelical' in name_lower:
        bg = "evangelical"
    elif 'pentecostal' in name_lower:
        bg = "pentecostal"
    elif 'adventist' in name_lower:
        bg = "seventh-day adventist"
    elif 'purity' in name_lower:
        bg = "purity culture"
    elif 'quiverfull' in name_lower:
        bg = "quiverfull"
    elif 'cult' in name_lower:
        bg = "cult"
    elif 'protestant' in name_lower:
        bg = "protestant"
    elif 'deconstructing' in name_lower:
        bg = "christianity"
    elif 'sbnr' in name_lower:
        bg = "religion"
    elif 'deist' in name_lower:
        bg = "organized religion"
    elif 'sufi' in name_lower:
        bg = "islam"
    elif 'religious trauma' in name_lower:
        bg = "religion"
    elif 'moralistic' in name_lower:
        bg = "christianity"
    elif 'agnostic' in name_lower:
        bg = "religion"
    elif 'syncretic' in name_lower:
        bg = "religion"
    else:
        bg = "religion"

    # Template 1: "Leaving [religion]"
    add_ticket(
        f"seo-leaving-{slug(name)}",
        f"Leaving {bg.title()}: The {name} Experience",
        target,
        [f"leaving {bg}", f"how to leave {bg}", f"left {bg} now what", f"life after {bg}"],
        "informational", "p1", "religious-leaving"
    )

    # Template 2: "Ex-[religion] support"
    add_ticket(
        f"seo-ex-{slug(bg)}-support-{slug(name)}",
        f"Ex-{bg.title()} Support: Finding Your Way After {bg.title()}",
        target,
        [f"ex {bg} support", f"ex {bg} community", f"ex {bg} groups", f"ex {bg} recovery"],
        "informational", "p1", "religious-support"
    )

    # Template 3: "Religious trauma [religion]"
    add_ticket(
        f"seo-religious-trauma-{slug(name)}",
        f"Religious Trauma from {bg.title()}: Healing What You Didn't Choose",
        target,
        [f"religious trauma {bg}", f"{bg} trauma recovery", f"{bg} spiritual abuse", f"healing from {bg}"],
        "informational", "p1", "religious-trauma"
    )

    # Template 4: "[group] beliefs explained"
    add_ticket(
        f"seo-{slug(name)}-beliefs-explained",
        f"{name}: Beliefs, Experience, and What It Means",
        target,
        [f"{name_lower}", f"{name_lower} meaning", f"{name_lower} experience", f"what is {name_lower}"],
        "informational", "p2", "religious-explanation"
    )

    # Template 5: "Am I [still religious / losing faith]?"
    add_ticket(
        f"seo-losing-faith-{slug(name)}",
        f"Am I Losing My Faith? The {name} Journey",
        target,
        [f"losing my {bg} faith", f"doubting {bg}", f"questioning {bg}", f"am I still {bg}"],
        "informational", "p2", "religious-doubt"
    )


# ============================================================
# POLITICAL PAGES (73) - ~4 landing pages each
# ============================================================

for item in by_type.get('political', []):
    pol_slug = item['slug']
    title = item['title']
    target = pol_slug

    if pol_slug.startswith('pol-'):
        # Political system pages
        # Determine the system name
        if '-impl-' in pol_slug:
            # Implementation page: e.g. pol-communism-impl-soviet-union
            parts = pol_slug.split('-impl-')
            system = parts[0].replace('pol-', '').replace('-', ' ').title()
            impl = parts[1].replace('-', ' ').title()
            name = f"{system} in {impl}"
            name_lower = name.lower()

            add_ticket(
                f"seo-{slug(name)}-explained",
                f"{name}: What Actually Happened",
                target,
                [f"{name_lower}", f"{impl.lower()} {system.lower()}", f"was {impl.lower()} {system.lower()}", f"{impl.lower()} economy history"],
                "informational", "p2", "political-implementation"
            )

            add_ticket(
                f"seo-{slug(name)}-lessons",
                f"Lessons from {name}: What Went Right and Wrong",
                target,
                [f"{name_lower} pros and cons", f"what went wrong in {impl.lower()}", f"{impl.lower()} economic system", f"did {system.lower()} work in {impl.lower()}"],
                "informational", "p2", "political-lessons"
            )
        elif '-decomp' in pol_slug:
            # Decomposition page
            system = pol_slug.replace('pol-', '').replace('-decomp', '').replace('-', ' ').title()
            system_lower = system.lower()

            add_ticket(
                f"seo-what-is-{slug(system)}",
                f"What Is {system}? Definition, Beliefs, and Hidden Assumptions",
                target,
                [f"what is {system_lower}", f"{system_lower} definition", f"{system_lower} explained simply", f"{system_lower} for beginners"],
                "informational", "p1", "political-definition"
            )

            add_ticket(
                f"seo-{slug(system)}-pros-cons",
                f"{system}: Honest Pros and Cons",
                target,
                [f"{system_lower} pros and cons", f"is {system_lower} good or bad", f"{system_lower} advantages disadvantages", f"arguments for and against {system_lower}"],
                "informational", "p1", "political-analysis"
            )

            add_ticket(
                f"seo-{slug(system)}-beliefs",
                f"The Hidden Beliefs Behind {system}",
                target,
                [f"{system_lower} beliefs", f"why do people support {system_lower}", f"{system_lower} ideology", f"{system_lower} assumptions"],
                "informational", "p2", "political-beliefs"
            )
        elif '-assessment' in pol_slug:
            system = pol_slug.replace('pol-', '').replace('-assessment', '').replace('-', ' ').title()
            system_lower = system.lower()

            add_ticket(
                f"seo-am-i-{slug(system)}",
                f"Am I a {system.rstrip('ism').rstrip('i')}ist? Understanding Your Political Beliefs",
                target,
                [f"am I a {system_lower.rstrip('ism')}ist", f"{system_lower} test", f"{system_lower} quiz", f"do I believe in {system_lower}"],
                "informational", "p2", "political-identity"
            )

            add_ticket(
                f"seo-{slug(system)}-vs-alternatives",
                f"{system} Compared: How It Stacks Up Against Other Systems",
                target,
                [f"{system_lower} vs capitalism", f"{system_lower} vs socialism", f"{system_lower} compared", f"best political system"],
                "informational", "p2", "political-comparison"
            )

    elif pol_slug.startswith('controversy-'):
        # Controversy pages
        topic = pol_slug.replace('controversy-', '').replace('-', ' ').title()
        topic_lower = topic.lower()

        add_ticket(
            f"seo-{slug(topic)}-both-sides",
            f"{topic}: Both Sides Honestly Presented",
            target,
            [f"{topic_lower} both sides", f"{topic_lower} arguments", f"{topic_lower} pros and cons", f"{topic_lower} debate"],
            "informational", "p1", "controversy-analysis"
        )

        add_ticket(
            f"seo-{slug(topic)}-explained",
            f"{topic} Explained: What's Actually Being Debated",
            target,
            [f"{topic_lower} explained", f"what is the {topic_lower} debate", f"{topic_lower} issue", f"{topic_lower} controversy"],
            "informational", "p1", "controversy-explanation"
        )

        add_ticket(
            f"seo-{slug(topic)}-beliefs",
            f"The Hidden Beliefs Behind Your Position on {topic}",
            target,
            [f"{topic_lower} beliefs", f"why do people disagree about {topic_lower}", f"{topic_lower} psychology"],
            "informational", "p2", "controversy-beliefs"
        )

        add_ticket(
            f"seo-{slug(topic)}-what-research-says",
            f"What Does Research Actually Say About {topic}?",
            target,
            [f"{topic_lower} research", f"{topic_lower} evidence", f"{topic_lower} facts", f"{topic_lower} statistics"],
            "informational", "p2", "controversy-research"
        )


# ============================================================
# CRISIS PAGES (33) - ~6 landing pages each
# ============================================================

for item in by_type.get('crisis', []):
    cr_slug = item['slug']
    title = item['title']
    target = cr_slug

    if cr_slug.startswith('trauma-'):
        # Trauma pages
        trauma_type = cr_slug.replace('trauma-', '').replace('-', ' ').title()
        trauma_lower = trauma_type.lower()

        add_ticket(
            f"seo-{slug(trauma_type)}-signs",
            f"Signs of {trauma_type}: How to Know If This Affected You",
            target,
            [f"{trauma_lower} signs", f"symptoms of {trauma_lower}", f"effects of {trauma_lower}", f"did I experience {trauma_lower}"],
            "informational", "p1", "crisis-trauma-signs"
        )

        add_ticket(
            f"seo-{slug(trauma_type)}-recovery",
            f"{trauma_type} Recovery: How to Heal",
            target,
            [f"{trauma_lower} recovery", f"healing from {trauma_lower}", f"{trauma_lower} therapy", f"how to recover from {trauma_lower}"],
            "informational", "p1", "crisis-trauma-recovery"
        )

        add_ticket(
            f"seo-{slug(trauma_type)}-in-adults",
            f"{trauma_type}: How It Shows Up in Adult Life",
            target,
            [f"{trauma_lower} effects on adults", f"{trauma_lower} adult symptoms", f"how {trauma_lower} affects relationships", f"{trauma_lower} long term effects"],
            "informational", "p1", "crisis-trauma-adult"
        )

        add_ticket(
            f"seo-{slug(trauma_type)}-test",
            f"Do I Have {trauma_type}? Understanding Your Experience",
            target,
            [f"do I have {trauma_lower}", f"{trauma_lower} test", f"{trauma_lower} assessment", f"was my childhood {trauma_lower}"],
            "informational", "p1", "crisis-trauma-assessment"
        )

        add_ticket(
            f"seo-{slug(trauma_type)}-help-near-me",
            f"{trauma_type}: Finding Help and Support",
            target,
            [f"{trauma_lower} help", f"{trauma_lower} help near me", f"{trauma_lower} therapist", f"{trauma_lower} support groups"],
            "transactional", "p1", "crisis-trauma-help"
        )

        add_ticket(
            f"seo-{slug(trauma_type)}-what-to-do",
            f"What to Do If You Experienced {trauma_type}",
            target,
            [f"{trauma_lower} what to do", f"I experienced {trauma_lower}", f"{trauma_lower} first steps", f"{trauma_lower} where to start"],
            "informational", "p1", "crisis-trauma-action"
        )

    elif cr_slug.startswith('crisis-'):
        # Active crisis pages - these are the most important
        crisis_phrase = cr_slug.replace('crisis-', '').replace('-', ' ')

        # These target the exact phrases people search in crisis
        add_ticket(
            f"seo-{cr_slug}",
            f"{title}",
            target,
            [crisis_phrase, f"feeling like {crisis_phrase}", f"{crisis_phrase} help"],
            "informational", "p0", "crisis-active"
        )

        add_ticket(
            f"seo-{cr_slug}-what-to-do",
            f"If You're Feeling '{crisis_phrase.title()}' — Read This First",
            target,
            [f"{crisis_phrase} what to do", f"help {crisis_phrase}", f"{crisis_phrase} right now"],
            "informational", "p0", "crisis-immediate"
        )

        add_ticket(
            f"seo-{cr_slug}-hotline",
            f"Crisis Help: {crisis_phrase.title()} — Resources and Hotlines",
            target,
            [f"crisis hotline", f"suicide hotline", f"crisis help number", f"988 suicide hotline"],
            "transactional", "p0", "crisis-hotline"
        )

        add_ticket(
            f"seo-{cr_slug}-not-alone",
            f"You're Not Alone: Understanding the Feeling of '{crisis_phrase.title()}'",
            target,
            [f"feeling {crisis_phrase}", f"why do I feel like {crisis_phrase}", f"is it normal to feel {crisis_phrase}"],
            "informational", "p0", "crisis-validation"
        )


# ============================================================
# SKILL PAGES (38) - ~4 landing pages each
# ============================================================

skill_names = {
    "mirror-how-it-works": "How Mirror Works",
    "mirror-pattern-detection": "Pattern Detection",
    "mirror-game-film": "Game Film Review",
    "mirror-growth-axes": "Growth Axes",
    "mirror-philosophical-foundation": "Mirror's Philosophical Foundation",
    "mirror-act-axis": "ACT Growth Axis",
    "mirror-de-mello-axis": "de Mello Awareness Axis",
    "mirror-aurelius-axis": "Marcus Aurelius Stoic Axis",
    "mirror-jung-axis": "Jung Shadow Work Axis",
    "mirror-nvc-axis": "NVC Communication Axis",
    "mirror-boundaries-axis": "Boundaries Axis",
    "mirror-tolle-axis": "Eckhart Tolle Presence Axis",
    "mirror-frankl-axis": "Viktor Frankl Meaning Axis",
    "mirror-van-der-kolk-axis": "van der Kolk Trauma Axis",
    "mirror-goleman-axis": "Goleman Emotional Intelligence Axis",
    "mirror-gibson-axis": "Gibson Attachment Axis",
    "mirror-bishop-axis": "Bishop Mindfulness Axis",
    "mirror-nguyen-axis": "Nguyen Cultural Identity Axis",
    "mirror-carter-axis": "Carter Relationship Axis",
    "mirror-diagnostic-chains": "Diagnostic Chains",
    "mirror-evidence-architecture": "Evidence Architecture",
    "mirror-skill-taxonomy": "Skill Taxonomy",
    "mirror-ai-coaching-philosophy": "AI Coaching Philosophy",
    "mirror-conversation-import": "Conversation Import",
    "skill-aurelius": "Stoic Practices (Marcus Aurelius)",
    "skill-de-mello": "Awareness Practices (Anthony de Mello)",
    "skill-hayes-act": "ACT Skills (Steven Hayes)",
    "skill-jung": "Shadow Work Skills (Carl Jung)",
    "skill-gibson-attachment": "Attachment Repair Skills",
    "skill-rosenberg-nvc": "Nonviolent Communication Skills",
    "skill-cloud-boundaries": "Boundary Skills (Cloud & Townsend)",
    "skill-tolle": "Presence Practices (Eckhart Tolle)",
    "skill-bishop": "Mindfulness Skills",
    "skill-frankl": "Meaning-Making Skills (Viktor Frankl)",
    "skill-nguyen": "Cultural Identity Skills",
    "skill-carter": "Relationship Skills",
    "skill-van-der-kolk": "Trauma Recovery Skills (van der Kolk)",
    "skill-goleman": "Emotional Intelligence Skills (Goleman)",
}

for item in by_type.get('skill', []):
    sk_slug = item['slug']
    name = skill_names.get(sk_slug, item['title'])
    target = sk_slug
    name_lower = name.lower()

    if sk_slug.startswith('mirror-'):
        # Mirror feature pages
        add_ticket(
            f"seo-{slug(name)}-explained",
            f"{name}: How It Works and Why It Matters",
            target,
            [f"{name_lower}", f"truemirror {name_lower}", f"ai {name_lower}", f"relationship {name_lower}"],
            "informational", "p2", "skill-mirror"
        )

        add_ticket(
            f"seo-ai-{slug(name)}",
            f"AI-Powered {name}: A New Approach to Self-Knowledge",
            target,
            [f"ai {name_lower}", f"ai relationship coach", f"ai self-awareness tool", f"ai personality analysis"],
            "informational", "p2", "skill-mirror-ai"
        )
    else:
        # Actual skill pages
        # Extract the philosopher/skill name
        core_skill = name.split('(')[0].strip() if '(' in name else name
        core_lower = core_skill.lower()

        add_ticket(
            f"seo-how-to-{slug(core_skill)}",
            f"How to Practice {core_skill}: Exercises for Beginners",
            target,
            [f"how to practice {core_lower}", f"{core_lower} exercises", f"{core_lower} for beginners", f"{core_lower} practice"],
            "informational", "p1", "skill-howto"
        )

        add_ticket(
            f"seo-{slug(core_skill)}-daily",
            f"{core_skill}: Daily Exercises and Practices",
            target,
            [f"{core_lower} daily practice", f"{core_lower} daily exercises", f"{core_lower} routine", f"{core_lower} habits"],
            "informational", "p1", "skill-daily"
        )

        add_ticket(
            f"seo-{slug(core_skill)}-relationships",
            f"Using {core_skill} in Your Relationships",
            target,
            [f"{core_lower} in relationships", f"{core_lower} for couples", f"{core_lower} relationship skills"],
            "informational", "p2", "skill-relationships"
        )

        add_ticket(
            f"seo-{slug(core_skill)}-worksheet",
            f"{core_skill} Worksheets and Practice Guides",
            target,
            [f"{core_lower} worksheet", f"{core_lower} pdf", f"{core_lower} workbook", f"{core_lower} activities"],
            "transactional", "p2", "skill-worksheet"
        )


# ============================================================
# COMPARISON PAGES (50) - ~3 landing pages each
# ============================================================

for item in by_type.get('comparison', []):
    cmp_slug = item['slug']
    title = item['title']
    target = cmp_slug

    # Extract the two things being compared
    if ' -- ' in title:
        name = title.split(' -- ')[0].strip()
    else:
        name = title

    # Parse "X vs Y" from slug
    cmp_part = cmp_slug.replace('compare-', '')
    parts = cmp_part.split('-vs-')
    if len(parts) == 2:
        a = parts[0].replace('-', ' ').title()
        b = parts[1].replace('-', ' ').title()
    else:
        a = name
        b = ""

    a_lower = a.lower()
    b_lower = b.lower()

    # Template 1: "[A] vs [B]"
    add_ticket(
        f"seo-{cmp_slug}",
        f"{a} vs {b}: Key Differences Explained",
        target,
        [f"{a_lower} vs {b_lower}", f"{a_lower} versus {b_lower}", f"{b_lower} vs {a_lower}", f"difference between {a_lower} and {b_lower}"],
        "informational", "p1", "comparison-main"
    )

    # Template 2: "Which is better [A] or [B]?"
    add_ticket(
        f"seo-which-better-{cmp_slug.replace('compare-','')}",
        f"Which Is Better: {a} or {b}?",
        target,
        [f"which is better {a_lower} or {b_lower}", f"should I do {a_lower} or {b_lower}", f"{a_lower} or {b_lower} for me", f"is {a_lower} better than {b_lower}"],
        "informational", "p1", "comparison-which-better"
    )

    # Template 3: "Can you do both [A] and [B]?"
    add_ticket(
        f"seo-both-{cmp_slug.replace('compare-','')}",
        f"Can You Combine {a} and {b}? When Both Apply",
        target,
        [f"can you do both {a_lower} and {b_lower}", f"{a_lower} and {b_lower} together", f"combining {a_lower} and {b_lower}"],
        "informational", "p2", "comparison-combine"
    )


# ============================================================
# CROSS-CUTTING LANDING PAGES (high-value query clusters)
# ============================================================

# These are landing pages for high-volume queries that span multiple content types

cross_cutting = [
    # "Am I..." queries
    {"slug": "seo-am-i-toxic", "title": "Am I Toxic? An Honest Self-Assessment", "target": "pattern-gaslighting", "terms": ["am I toxic", "am I a toxic person", "toxic traits test", "am I the problem in my relationship", "signs you're the toxic one"], "intent": "informational", "priority": "p0", "cat": "self-assessment"},
    {"slug": "seo-am-i-narcissist", "title": "Am I a Narcissist? How to Tell the Difference Between Confidence and Narcissism", "target": "narcissism_spectrum-evidence", "terms": ["am I a narcissist", "narcissist test", "narcissistic traits", "am I narcissistic or just confident", "covert narcissist test"], "intent": "informational", "priority": "p0", "cat": "self-assessment"},
    {"slug": "seo-am-i-codependent", "title": "Am I Codependent? Signs, Causes, and What to Do", "target": "codependency-evidence", "terms": ["am I codependent", "codependency test", "codependent traits", "signs of codependency", "codependency quiz"], "intent": "informational", "priority": "p0", "cat": "self-assessment"},
    {"slug": "seo-am-i-emotionally-unavailable", "title": "Am I Emotionally Unavailable? What That Actually Means", "target": "attachment_style-evidence", "terms": ["am I emotionally unavailable", "emotionally unavailable test", "signs of being emotionally unavailable", "why am I emotionally unavailable"], "intent": "informational", "priority": "p0", "cat": "self-assessment"},
    {"slug": "seo-am-i-in-abusive-relationship", "title": "Am I in an Abusive Relationship? The Signs Most People Miss", "target": "pattern-coercive-control", "terms": ["am I in an abusive relationship", "signs of emotional abuse", "is my relationship abusive", "emotional abuse test", "am I being abused"], "intent": "informational", "priority": "p0", "cat": "self-assessment"},
    {"slug": "seo-am-i-depressed-or-lazy", "title": "Am I Depressed or Just Lazy? How to Tell the Difference", "target": "anxiety_depression_screen-evidence", "terms": ["am I depressed or lazy", "depression vs laziness", "how to tell if you're depressed", "am I depressed test"], "intent": "informational", "priority": "p0", "cat": "self-assessment"},
    {"slug": "seo-am-i-trauma-bonded", "title": "Am I Trauma Bonded? Understanding Why You Can't Leave", "target": "pattern-trauma-bonding", "terms": ["am I trauma bonded", "trauma bonding test", "signs of trauma bonding", "why can't I leave", "trauma bond quiz"], "intent": "informational", "priority": "p0", "cat": "self-assessment"},
    {"slug": "seo-am-i-anxiously-attached", "title": "Am I Anxiously Attached? Signs and What to Do About It", "target": "attachment_style-evidence", "terms": ["am I anxiously attached", "anxious attachment test", "anxious attachment signs", "anxious attachment style quiz"], "intent": "informational", "priority": "p0", "cat": "self-assessment"},
    {"slug": "seo-am-i-avoidant", "title": "Am I Avoidant? Understanding Avoidant Attachment", "target": "attachment_style-evidence", "terms": ["am I avoidant", "avoidant attachment test", "dismissive avoidant signs", "fearful avoidant test", "avoidant attachment quiz"], "intent": "informational", "priority": "p0", "cat": "self-assessment"},
    {"slug": "seo-am-i-people-pleaser", "title": "Am I a People Pleaser? The Hidden Cost of Always Being Nice", "target": "people_pleasing-evidence", "terms": ["am I a people pleaser", "people pleasing test", "signs of people pleasing", "why am I a people pleaser"], "intent": "informational", "priority": "p0", "cat": "self-assessment"},
    {"slug": "seo-am-i-gaslighting", "title": "Am I Being Gaslighted? Or Am I Gaslighting Someone?", "target": "pattern-gaslighting", "terms": ["am I being gaslighted", "am I gaslighting", "gaslighting test", "signs of gaslighting", "gaslighting examples"], "intent": "informational", "priority": "p0", "cat": "self-assessment"},
    {"slug": "seo-am-i-borderline", "title": "Do I Have BPD? Understanding Borderline Traits", "target": "borderline_traits-evidence", "terms": ["do I have bpd", "borderline personality test", "bpd signs", "bpd quiz", "am I borderline"], "intent": "informational", "priority": "p0", "cat": "self-assessment"},
    {"slug": "seo-am-i-hsp", "title": "Am I a Highly Sensitive Person? HSP Signs and What It Means", "target": "hsp-evidence", "terms": ["am I a highly sensitive person", "hsp test", "highly sensitive person quiz", "hsp signs", "am I too sensitive"], "intent": "informational", "priority": "p0", "cat": "self-assessment"},
    {"slug": "seo-am-i-autistic", "title": "Am I Autistic? Understanding Autism in Adults", "target": "autism_spectrum-evidence", "terms": ["am I autistic", "autism test adults", "signs of autism in adults", "undiagnosed autism", "late diagnosis autism"], "intent": "informational", "priority": "p0", "cat": "self-assessment"},
    {"slug": "seo-do-i-have-adhd", "title": "Do I Have ADHD? Adult ADHD Signs Most People Miss", "target": "adhd-evidence", "terms": ["do I have adhd", "adhd test adults", "adult adhd signs", "adhd quiz", "undiagnosed adhd"], "intent": "informational", "priority": "p0", "cat": "self-assessment"},

    # "Why do I..." queries
    {"slug": "seo-why-do-i-push-people-away", "title": "Why Do I Push People Away? The Psychology Behind It", "target": "pattern-deactivating-strategies", "terms": ["why do I push people away", "pushing people away psychology", "why do I sabotage relationships", "fear of intimacy"], "intent": "informational", "priority": "p0", "cat": "why-do-i"},
    {"slug": "seo-why-do-i-pick-unavailable-partners", "title": "Why Do I Always Pick Emotionally Unavailable Partners?", "target": "attachment_style-evidence", "terms": ["why do I pick emotionally unavailable partners", "attracted to unavailable people", "why do I choose the wrong person", "picking bad partners"], "intent": "informational", "priority": "p0", "cat": "why-do-i"},
    {"slug": "seo-why-do-i-shut-down-in-arguments", "title": "Why Do I Shut Down During Arguments? Understanding Stonewalling and Flooding", "target": "pattern-stonewalling", "terms": ["why do I shut down during arguments", "shutting down emotionally", "stonewalling why", "I freeze during conflict"], "intent": "informational", "priority": "p0", "cat": "why-do-i"},
    {"slug": "seo-why-cant-i-set-boundaries", "title": "Why Can't I Set Boundaries? The Real Reasons and How to Start", "target": "boundary_capacity-evidence", "terms": ["why can't I set boundaries", "trouble setting boundaries", "afraid to set boundaries", "boundaries feel mean"], "intent": "informational", "priority": "p0", "cat": "why-do-i"},
    {"slug": "seo-why-do-i-feel-empty", "title": "Why Do I Feel Empty Inside? What That Emptiness Actually Means", "target": "pattern-dissociation-pattern", "terms": ["why do I feel empty", "feeling empty inside", "emotional emptiness", "I feel nothing"], "intent": "informational", "priority": "p0", "cat": "why-do-i"},
    {"slug": "seo-why-do-i-stay-in-bad-relationships", "title": "Why Do I Stay in Bad Relationships? The Psychology of Staying", "target": "pattern-sunk-cost-fallacy-relationship", "terms": ["why do I stay in bad relationships", "why can't I leave my relationship", "stuck in bad relationship", "why do I put up with bad treatment"], "intent": "informational", "priority": "p0", "cat": "why-do-i"},
    {"slug": "seo-why-do-i-attract-narcissists", "title": "Why Do I Keep Attracting Narcissists? Breaking the Pattern", "target": "narcissism_spectrum-evidence", "terms": ["why do I attract narcissists", "attracting narcissists pattern", "narcissist magnet", "keep dating narcissists"], "intent": "informational", "priority": "p0", "cat": "why-do-i"},
    {"slug": "seo-why-am-i-so-angry", "title": "Why Am I So Angry? Understanding Your Anger", "target": "emotional_regulation-evidence", "terms": ["why am I so angry", "anger issues", "always angry", "anger management", "why am I angry all the time"], "intent": "informational", "priority": "p0", "cat": "why-do-i"},
    {"slug": "seo-why-am-i-so-anxious", "title": "Why Am I So Anxious? Understanding Anxiety Beyond the Label", "target": "anxiety_depression_screen-evidence", "terms": ["why am I so anxious", "constant anxiety", "anxiety for no reason", "always anxious", "generalized anxiety"], "intent": "informational", "priority": "p0", "cat": "why-do-i"},
    {"slug": "seo-why-do-i-overthink", "title": "Why Do I Overthink Everything? The Pattern Behind Rumination", "target": "pattern-catastrophizing", "terms": ["why do I overthink everything", "overthinking", "how to stop overthinking", "rumination", "racing thoughts"], "intent": "informational", "priority": "p0", "cat": "why-do-i"},
    {"slug": "seo-why-do-i-self-sabotage", "title": "Why Do I Self-Sabotage? Understanding the Pattern", "target": "pattern-protest-behavior", "terms": ["why do I self sabotage", "self sabotage psychology", "self destructive behavior", "why do I ruin good things"], "intent": "informational", "priority": "p0", "cat": "why-do-i"},
    {"slug": "seo-why-cant-i-trust-anyone", "title": "Why Can't I Trust Anyone? Rebuilding After Betrayal", "target": "pattern-betrayal-trauma", "terms": ["why can't I trust anyone", "trust issues", "can't trust my partner", "how to trust again", "trust issues after cheating"], "intent": "informational", "priority": "p0", "cat": "why-do-i"},
    {"slug": "seo-why-do-i-need-constant-reassurance", "title": "Why Do I Need Constant Reassurance? The Anxious Attachment Connection", "target": "pattern-protest-behavior", "terms": ["why do I need constant reassurance", "needing reassurance in relationships", "reassurance seeking", "insecure in relationship"], "intent": "informational", "priority": "p0", "cat": "why-do-i"},
    {"slug": "seo-why-am-i-so-sensitive", "title": "Why Am I So Sensitive? Is It a Problem or a Strength?", "target": "hsp-evidence", "terms": ["why am I so sensitive", "too sensitive", "crying easily", "emotional sensitivity", "is being sensitive bad"], "intent": "informational", "priority": "p0", "cat": "why-do-i"},
    {"slug": "seo-why-do-i-feel-like-burden", "title": "Why Do I Feel Like a Burden? Understanding This Painful Belief", "target": "self_worth-evidence", "terms": ["why do I feel like a burden", "feeling like a burden", "I'm a burden to everyone", "burden on others"], "intent": "informational", "priority": "p0", "cat": "why-do-i"},

    # "How to..." queries
    {"slug": "seo-how-to-heal-from-childhood-trauma", "title": "How to Heal from Childhood Trauma: A Practical Guide", "target": "trauma_cptsd-evidence", "terms": ["how to heal from childhood trauma", "childhood trauma recovery", "healing childhood wounds", "adult children of trauma"], "intent": "informational", "priority": "p0", "cat": "how-to"},
    {"slug": "seo-how-to-set-boundaries", "title": "How to Set Boundaries (When You've Never Had Them)", "target": "boundary_capacity-evidence", "terms": ["how to set boundaries", "setting boundaries examples", "boundary setting scripts", "how to say no"], "intent": "informational", "priority": "p0", "cat": "how-to"},
    {"slug": "seo-how-to-stop-being-codependent", "title": "How to Stop Being Codependent: Breaking the Pattern", "target": "codependency-evidence", "terms": ["how to stop being codependent", "overcoming codependency", "codependency recovery", "breaking codependency"], "intent": "informational", "priority": "p0", "cat": "how-to"},
    {"slug": "seo-how-to-communicate-better", "title": "How to Communicate Better in Your Relationship", "target": "communication_gottman-evidence", "terms": ["how to communicate better in relationships", "relationship communication", "communication skills for couples", "how to talk to your partner"], "intent": "informational", "priority": "p0", "cat": "how-to"},
    {"slug": "seo-how-to-regulate-emotions", "title": "How to Regulate Your Emotions (Without Suppressing Them)", "target": "emotional_regulation-evidence", "terms": ["how to regulate emotions", "emotional regulation techniques", "emotion regulation strategies", "how to control emotions"], "intent": "informational", "priority": "p0", "cat": "how-to"},
    {"slug": "seo-how-to-stop-people-pleasing", "title": "How to Stop People Pleasing: Reclaiming Your Authenticity", "target": "people_pleasing-evidence", "terms": ["how to stop people pleasing", "overcoming people pleasing", "stop being a people pleaser", "people pleasing recovery"], "intent": "informational", "priority": "p0", "cat": "how-to"},
    {"slug": "seo-how-to-leave-narcissist", "title": "How to Leave a Narcissist: A Safety-First Guide", "target": "narcissism_spectrum-evidence", "terms": ["how to leave a narcissist", "leaving narcissistic relationship", "how to leave abusive relationship", "escape narcissist"], "intent": "informational", "priority": "p0", "cat": "how-to"},
    {"slug": "seo-how-to-forgive", "title": "How to Forgive (When Part of You Doesn't Want To)", "target": "forgiveness_profile-evidence", "terms": ["how to forgive someone", "forgiveness process", "how to let go of resentment", "struggling to forgive"], "intent": "informational", "priority": "p0", "cat": "how-to"},
    {"slug": "seo-how-to-rebuild-trust", "title": "How to Rebuild Trust After Betrayal", "target": "repair_skills-evidence", "terms": ["how to rebuild trust", "rebuilding trust after cheating", "trust repair", "can trust be rebuilt"], "intent": "informational", "priority": "p0", "cat": "how-to"},
    {"slug": "seo-how-to-stop-overthinking", "title": "How to Stop Overthinking: Practical Techniques That Work", "target": "pattern-catastrophizing", "terms": ["how to stop overthinking", "overthinking cure", "stop ruminating", "racing thoughts how to stop"], "intent": "informational", "priority": "p0", "cat": "how-to"},
    {"slug": "seo-how-to-find-therapist", "title": "How to Find a Therapist: Which Type Is Right for You?", "target": "fw-cbt", "terms": ["how to find a therapist", "types of therapy", "which therapy is best for me", "therapist near me", "how to choose a therapist"], "intent": "transactional", "priority": "p0", "cat": "how-to"},
    {"slug": "seo-how-to-be-vulnerable", "title": "How to Be Vulnerable Without Getting Destroyed", "target": "vulnerability_capacity-evidence", "terms": ["how to be vulnerable", "vulnerability in relationships", "afraid to be vulnerable", "opening up to partner"], "intent": "informational", "priority": "p0", "cat": "how-to"},
    {"slug": "seo-how-to-stop-being-triggered", "title": "How to Stop Being Triggered: Understanding and Managing Your Reactions", "target": "triggers_profile-evidence", "terms": ["how to stop being triggered", "emotional triggers", "triggered meaning", "why do I get triggered easily"], "intent": "informational", "priority": "p0", "cat": "how-to"},
    {"slug": "seo-how-to-break-trauma-bond", "title": "How to Break a Trauma Bond: Step by Step", "target": "pattern-trauma-bonding", "terms": ["how to break trauma bond", "breaking trauma bond", "trauma bond recovery", "stages of breaking trauma bond"], "intent": "informational", "priority": "p0", "cat": "how-to"},
    {"slug": "seo-how-to-deal-with-gaslighting", "title": "How to Deal with Gaslighting: Protecting Your Reality", "target": "pattern-gaslighting", "terms": ["how to deal with gaslighting", "gaslighting response", "being gaslit what to do", "responding to gaslighter"], "intent": "informational", "priority": "p0", "cat": "how-to"},
    {"slug": "seo-how-to-stop-being-a-perfectionist", "title": "How to Stop Being a Perfectionist (Without Becoming Lazy)", "target": "perfectionism-evidence", "terms": ["how to stop being a perfectionist", "overcoming perfectionism", "perfectionism recovery", "letting go of perfectionism"], "intent": "informational", "priority": "p0", "cat": "how-to"},
    {"slug": "seo-how-to-do-shadow-work", "title": "How to Do Shadow Work: A Beginner's Guide", "target": "shadow_integration-evidence", "terms": ["how to do shadow work", "shadow work exercises", "shadow work for beginners", "shadow work journal prompts", "shadow work explained"], "intent": "informational", "priority": "p0", "cat": "how-to"},
    {"slug": "seo-how-to-build-self-worth", "title": "How to Build Self-Worth (When You've Never Had It)", "target": "self_worth-evidence", "terms": ["how to build self worth", "building self esteem", "low self worth", "how to value yourself", "self worth exercises"], "intent": "informational", "priority": "p0", "cat": "how-to"},
    {"slug": "seo-how-to-stop-fawning", "title": "How to Stop Fawning: Breaking the People-Pleasing Trauma Response", "target": "pattern-fawning", "terms": ["how to stop fawning", "fawn trauma response", "fawning response", "fawn response examples"], "intent": "informational", "priority": "p0", "cat": "how-to"},
    {"slug": "seo-how-to-reparent-yourself", "title": "How to Reparent Yourself: Healing the Inner Child", "target": "trauma_cptsd-evidence", "terms": ["how to reparent yourself", "reparenting exercises", "inner child healing", "reparenting yourself", "inner child work"], "intent": "informational", "priority": "p0", "cat": "how-to"},

    # "My partner..." queries
    {"slug": "seo-my-partner-stonewalls-me", "title": "My Partner Stonewalls Me: What's Happening and What to Do", "target": "pattern-stonewalling", "terms": ["my partner stonewalls me", "partner shuts down during arguments", "husband stonewalls", "wife stonewalls", "partner won't talk about problems"], "intent": "informational", "priority": "p0", "cat": "my-partner"},
    {"slug": "seo-my-partner-is-narcissist", "title": "Is My Partner a Narcissist? How to Tell (And What to Do)", "target": "narcissism_spectrum-evidence", "terms": ["is my partner a narcissist", "narcissistic partner signs", "married to a narcissist", "dating a narcissist", "narcissistic husband signs"], "intent": "informational", "priority": "p0", "cat": "my-partner"},
    {"slug": "seo-my-partner-gaslights-me", "title": "My Partner Gaslights Me: Recognizing and Responding", "target": "pattern-gaslighting", "terms": ["my partner gaslights me", "partner denies reality", "am I being gaslit by my partner", "gaslighting in marriage"], "intent": "informational", "priority": "p0", "cat": "my-partner"},
    {"slug": "seo-my-partner-wont-communicate", "title": "My Partner Won't Communicate: Why and What Actually Helps", "target": "communication_gottman-evidence", "terms": ["my partner won't communicate", "partner won't talk about feelings", "husband won't communicate", "wife won't talk to me"], "intent": "informational", "priority": "p0", "cat": "my-partner"},
    {"slug": "seo-my-partner-is-avoidant", "title": "My Partner Is Avoidant: Understanding and Navigating the Dynamic", "target": "pattern-anxious-avoidant-trap", "terms": ["my partner is avoidant", "dating avoidant person", "avoidant partner what to do", "married to avoidant"], "intent": "informational", "priority": "p0", "cat": "my-partner"},
    {"slug": "seo-my-partner-love-bombs-then-withdraws", "title": "My Partner Love Bombs Then Withdraws: The Hot-Cold Cycle", "target": "pattern-hot-cold-pattern", "terms": ["partner love bombs then withdraws", "hot and cold relationship", "partner hot and cold", "inconsistent partner"], "intent": "informational", "priority": "p0", "cat": "my-partner"},
    {"slug": "seo-my-partner-blames-me-for-everything", "title": "My Partner Blames Me for Everything: Is It Me or Them?", "target": "pattern-blame-shifting", "terms": ["partner blames me for everything", "always my fault in relationship", "blame shifting partner", "everything is my fault"], "intent": "informational", "priority": "p0", "cat": "my-partner"},
    {"slug": "seo-my-partner-cheated", "title": "My Partner Cheated: What to Do Next", "target": "pattern-betrayal-trauma", "terms": ["my partner cheated", "what to do after cheating", "partner had an affair", "should I stay after cheating", "infidelity recovery"], "intent": "informational", "priority": "p0", "cat": "my-partner"},
    {"slug": "seo-my-partner-threatens-to-leave", "title": "My Partner Threatens to Leave During Arguments: Understanding Emotional Blackmail", "target": "pattern-emotional-blackmail", "terms": ["partner threatens to leave", "partner threatens breakup during arguments", "emotional blackmail relationship", "using breakup as threat"], "intent": "informational", "priority": "p0", "cat": "my-partner"},
    {"slug": "seo-my-partner-gives-silent-treatment", "title": "My Partner Gives Me the Silent Treatment: What It Means and What to Do", "target": "pattern-silent-treatment", "terms": ["partner gives silent treatment", "silent treatment in relationships", "husband silent treatment", "wife won't talk to me"], "intent": "informational", "priority": "p0", "cat": "my-partner"},

    # "After..." queries
    {"slug": "seo-after-narcissistic-abuse", "title": "After Narcissistic Abuse: What Recovery Actually Looks Like", "target": "narcissism_spectrum-evidence", "terms": ["after narcissistic abuse", "narcissistic abuse recovery", "healing from narcissistic abuse", "narcissistic abuse survivor"], "intent": "informational", "priority": "p0", "cat": "after"},
    {"slug": "seo-after-breakup", "title": "After a Breakup: What's Actually Happening in Your Brain", "target": "attachment_style-evidence", "terms": ["after breakup", "breakup recovery", "getting over a breakup", "heartbreak", "how long to get over breakup"], "intent": "informational", "priority": "p0", "cat": "after"},
    {"slug": "seo-after-divorce", "title": "After Divorce: Rebuilding When Everything Falls Apart", "target": "trauma-divorce-family-dissolution", "terms": ["after divorce", "life after divorce", "rebuilding after divorce", "divorce recovery", "starting over after divorce"], "intent": "informational", "priority": "p0", "cat": "after"},
    {"slug": "seo-after-infidelity", "title": "After Infidelity: Can a Relationship Survive?", "target": "pattern-betrayal-trauma", "terms": ["after infidelity", "relationship after cheating", "can marriage survive infidelity", "recovering from affair", "trust after cheating"], "intent": "informational", "priority": "p0", "cat": "after"},

    # "Is it normal to..." queries
    {"slug": "seo-is-it-normal-to-fight", "title": "Is It Normal to Fight in a Relationship? What Healthy Conflict Looks Like", "target": "conflict_navigation-evidence", "terms": ["is it normal to fight in a relationship", "how much fighting is normal", "healthy vs unhealthy fighting", "couples fighting"], "intent": "informational", "priority": "p1", "cat": "normal"},
    {"slug": "seo-is-it-normal-to-feel-nothing", "title": "Is It Normal to Feel Nothing? Understanding Emotional Numbness", "target": "alexithymia-evidence", "terms": ["is it normal to feel nothing", "emotional numbness", "I feel nothing", "can't feel emotions", "alexithymia"], "intent": "informational", "priority": "p1", "cat": "normal"},
    {"slug": "seo-is-it-normal-to-doubt-relationship", "title": "Is It Normal to Doubt Your Relationship? When Doubts Are Healthy vs Concerning", "target": "relationship_expectations-evidence", "terms": ["is it normal to doubt your relationship", "relationship doubt", "questioning my relationship", "not sure about relationship"], "intent": "informational", "priority": "p1", "cat": "normal"},

    # Therapy-shopping queries
    {"slug": "seo-best-therapy-for-trauma", "title": "Best Therapy for Trauma: Comparing EMDR, CPT, PE, and More", "target": "compare-emdr-vs-cpt", "terms": ["best therapy for trauma", "trauma therapy types", "emdr vs talk therapy for trauma", "most effective trauma therapy"], "intent": "informational", "priority": "p0", "cat": "therapy-shopping"},
    {"slug": "seo-best-therapy-for-anxiety", "title": "Best Therapy for Anxiety: Which Approach Actually Works?", "target": "compare-cbt-vs-act", "terms": ["best therapy for anxiety", "therapy for anxiety", "cbt for anxiety", "act for anxiety", "most effective anxiety treatment"], "intent": "informational", "priority": "p0", "cat": "therapy-shopping"},
    {"slug": "seo-best-therapy-for-depression", "title": "Best Therapy for Depression: Evidence-Based Options", "target": "compare-cbt-vs-act", "terms": ["best therapy for depression", "therapy for depression", "most effective depression treatment", "cbt for depression"], "intent": "informational", "priority": "p0", "cat": "therapy-shopping"},
    {"slug": "seo-best-therapy-for-couples", "title": "Best Couples Therapy: Comparing Gottman, EFT, and Others", "target": "compare-eft-vs-gottman", "terms": ["best couples therapy", "marriage counseling types", "couples therapy approaches", "gottman vs eft"], "intent": "informational", "priority": "p0", "cat": "therapy-shopping"},
    {"slug": "seo-best-therapy-for-attachment", "title": "Best Therapy for Attachment Issues: What Actually Helps", "target": "attachment_style-evidence", "terms": ["therapy for attachment issues", "attachment therapy adults", "healing attachment style", "can attachment style change"], "intent": "informational", "priority": "p0", "cat": "therapy-shopping"},
    {"slug": "seo-best-therapy-for-narcissistic-abuse", "title": "Best Therapy After Narcissistic Abuse: What Survivors Need", "target": "narcissism_spectrum-evidence", "terms": ["therapy for narcissistic abuse", "therapist for narcissistic abuse", "emdr for narcissistic abuse", "healing from narcissistic abuse therapy"], "intent": "informational", "priority": "p0", "cat": "therapy-shopping"},

    # Personality test queries
    {"slug": "seo-personality-test-accurate", "title": "Which Personality Tests Are Actually Accurate? A Scientific Ranking", "target": "big_five-evidence", "terms": ["which personality test is most accurate", "best personality test", "accurate personality test", "scientific personality test", "personality test that actually works"], "intent": "informational", "priority": "p0", "cat": "personality-test"},
    {"slug": "seo-mbti-vs-big-five-accuracy", "title": "MBTI vs Big Five: Which One Should You Actually Trust?", "target": "compare-mbti-vs-big-five", "terms": ["mbti vs big five", "is mbti or big five better", "mbti accuracy vs big five", "personality test comparison"], "intent": "informational", "priority": "p0", "cat": "personality-test"},
    {"slug": "seo-is-mbti-real", "title": "Is MBTI Real? What the Science Actually Says", "target": "mbti-evidence", "terms": ["is mbti real", "is mbti pseudoscience", "mbti scientific validity", "mbti evidence", "is myers briggs accurate"], "intent": "informational", "priority": "p0", "cat": "personality-test"},
    {"slug": "seo-is-enneagram-real", "title": "Is the Enneagram Real? Science, Spirituality, and What's Valid", "target": "enneagram-evidence", "terms": ["is enneagram real", "enneagram scientific basis", "enneagram evidence", "is enneagram accurate", "enneagram criticism"], "intent": "informational", "priority": "p0", "cat": "personality-test"},
    {"slug": "seo-are-love-languages-real", "title": "Are Love Languages Real? What Research Says About Chapman's Theory", "target": "love_languages-evidence", "terms": ["are love languages real", "love languages evidence", "love languages criticism", "love languages scientific", "do love languages work"], "intent": "informational", "priority": "p0", "cat": "personality-test"},

    # Relationship type queries
    {"slug": "seo-anxious-avoidant-relationship", "title": "Anxious-Avoidant Relationship: The Trap and How to Escape It", "target": "pattern-anxious-avoidant-trap", "terms": ["anxious avoidant relationship", "anxious avoidant trap", "anxious attachment avoidant partner", "anxious avoidant dynamic"], "intent": "informational", "priority": "p0", "cat": "relationship-type"},
    {"slug": "seo-codependent-relationship-signs", "title": "Codependent Relationship: Signs, Causes, and Breaking Free", "target": "codependency-evidence", "terms": ["codependent relationship signs", "codependency in relationships", "am I in a codependent relationship", "codependent vs healthy relationship"], "intent": "informational", "priority": "p0", "cat": "relationship-type"},
    {"slug": "seo-toxic-relationship-signs", "title": "Toxic Relationship Signs: 15 Red Flags You Should Never Ignore", "target": "pattern-coercive-control", "terms": ["toxic relationship signs", "red flags in a relationship", "unhealthy relationship signs", "toxic partner signs"], "intent": "informational", "priority": "p0", "cat": "relationship-type"},
    {"slug": "seo-emotionally-abusive-relationship", "title": "Emotionally Abusive Relationship: Signs Most People Dismiss", "target": "pattern-coercive-control", "terms": ["emotionally abusive relationship", "emotional abuse signs", "verbal abuse signs", "psychological abuse in relationships"], "intent": "informational", "priority": "p0", "cat": "relationship-type"},
    {"slug": "seo-trauma-bond-vs-love", "title": "Trauma Bond vs Love: How to Tell the Difference", "target": "pattern-trauma-bonding", "terms": ["trauma bond vs love", "is it love or trauma bond", "difference between love and trauma bonding", "how to tell if its a trauma bond"], "intent": "informational", "priority": "p0", "cat": "relationship-type"},

    # Childhood / family queries
    {"slug": "seo-emotionally-absent-parent", "title": "Emotionally Absent Parent: How It Shapes You as an Adult", "target": "trauma-childhood-emotional-neglect", "terms": ["emotionally absent parent", "emotionally unavailable parent", "emotional neglect childhood", "parent who wasn't there emotionally"], "intent": "informational", "priority": "p0", "cat": "childhood"},
    {"slug": "seo-narcissistic-mother", "title": "Narcissistic Mother: Signs, Effects, and How to Heal", "target": "trauma-narcissistic-parent", "terms": ["narcissistic mother", "narcissistic mother signs", "raised by narcissistic mother", "narcissistic mom effects"], "intent": "informational", "priority": "p0", "cat": "childhood"},
    {"slug": "seo-narcissistic-father", "title": "Narcissistic Father: How It Shapes Daughters and Sons", "target": "trauma-narcissistic-parent", "terms": ["narcissistic father", "narcissistic father signs", "raised by narcissistic father", "narcissistic dad effects on daughter"], "intent": "informational", "priority": "p0", "cat": "childhood"},
    {"slug": "seo-daddy-issues-meaning", "title": "What Are Daddy Issues Actually? Beyond the Dismissive Label", "target": "daddy_issues-evidence", "terms": ["daddy issues meaning", "what are daddy issues", "daddy issues psychology", "father wound", "daddy issues signs"], "intent": "informational", "priority": "p0", "cat": "childhood"},
    {"slug": "seo-emotional-neglect-childhood", "title": "Childhood Emotional Neglect: The Invisible Wound", "target": "trauma-childhood-emotional-neglect", "terms": ["childhood emotional neglect", "CEN", "emotional neglect signs", "was I emotionally neglected", "running on empty"], "intent": "informational", "priority": "p0", "cat": "childhood"},
    {"slug": "seo-parentified-child", "title": "Were You the Parentified Child? What It Means and What It Cost You", "target": "pattern-parentification", "terms": ["parentified child", "parentification", "child taking care of parent", "I raised my siblings", "emotional parentification"], "intent": "informational", "priority": "p0", "cat": "childhood"},

    # Identity / meaning queries
    {"slug": "seo-who-am-i-really", "title": "Who Am I Really? Going Beyond Labels to Actual Self-Knowledge", "target": "self_awareness-evidence", "terms": ["who am I really", "self discovery", "finding myself", "identity crisis", "I don't know who I am"], "intent": "informational", "priority": "p1", "cat": "identity"},
    {"slug": "seo-what-is-my-purpose", "title": "What Is My Purpose? Moving Beyond the Question to Living the Answer", "target": "purpose_assessment-evidence", "terms": ["what is my purpose", "finding purpose in life", "life purpose", "why am I here", "how to find purpose"], "intent": "informational", "priority": "p1", "cat": "identity"},
    {"slug": "seo-what-are-my-values", "title": "What Are My Real Values? (Not the Ones You Think You Should Have)", "target": "values_real_vs_aspirational-evidence", "terms": ["what are my values", "personal values list", "core values", "how to find your values", "values assessment"], "intent": "informational", "priority": "p1", "cat": "identity"},

    # Religious deconstruction queries
    {"slug": "seo-losing-my-faith", "title": "Losing My Faith: What's Happening and Why It Feels Like Death", "target": "rg-deconstructing-page", "terms": ["losing my faith", "losing faith in god", "faith crisis", "questioning my religion", "doubt in faith"], "intent": "informational", "priority": "p0", "cat": "religious-crisis"},
    {"slug": "seo-religious-trauma-syndrome", "title": "Religious Trauma Syndrome: Is It Real and Do You Have It?", "target": "rg-religious-trauma-identity-page", "terms": ["religious trauma syndrome", "religious trauma", "spiritual abuse", "church hurt", "religious ptsd"], "intent": "informational", "priority": "p0", "cat": "religious-crisis"},
    {"slug": "seo-deconstruction-faith", "title": "Deconstructing Your Faith: What It Is and What Comes After", "target": "rg-deconstructing-page", "terms": ["deconstruction faith", "deconstructing christianity", "faith deconstruction", "what is deconstruction", "exvangelical"], "intent": "informational", "priority": "p0", "cat": "religious-crisis"},
    {"slug": "seo-purity-culture-damage", "title": "Purity Culture Damage: Healing from Shame That Was Taught", "target": "rg-purity-culture-refugee-page", "terms": ["purity culture damage", "purity culture trauma", "purity culture recovery", "true love waits damage", "sexual shame religion"], "intent": "informational", "priority": "p0", "cat": "religious-crisis"},
    {"slug": "seo-leaving-mormonism", "title": "Leaving Mormonism: A Guide for Those Who Can't Un-Know What They Know", "target": "rg-post-mormon-page", "terms": ["leaving mormonism", "leaving the lds church", "mormon faith crisis", "exmormon", "leaving lds"], "intent": "informational", "priority": "p0", "cat": "religious-crisis"},
    {"slug": "seo-leaving-jehovah-witnesses", "title": "Leaving Jehovah's Witnesses: What No One Tells You", "target": "rg-jw-fading-page", "terms": ["leaving jehovah's witnesses", "leaving jw", "exjw", "disfellowshipped recovery", "fading from jw"], "intent": "informational", "priority": "p0", "cat": "religious-crisis"},

    # Assessment queries
    {"slug": "seo-free-personality-assessment", "title": "Free Personality Assessment: Scientifically-Grounded Self-Discovery", "target": "big_five-evidence", "terms": ["free personality assessment", "free personality test", "free big five test", "personality quiz", "online personality test"], "intent": "transactional", "priority": "p0", "cat": "assessment"},
    {"slug": "seo-attachment-style-quiz", "title": "Attachment Style Quiz: Find Your Pattern in 5 Minutes", "target": "attachment_style-evidence", "terms": ["attachment style quiz", "attachment style test", "what is my attachment style", "attachment quiz free", "anxious avoidant test"], "intent": "transactional", "priority": "p0", "cat": "assessment"},
    {"slug": "seo-trauma-test", "title": "Do I Have Trauma? A Self-Assessment That Goes Beyond ACE Scores", "target": "trauma_cptsd-evidence", "terms": ["trauma test", "do I have trauma", "trauma assessment", "ACE score test", "childhood trauma test"], "intent": "transactional", "priority": "p0", "cat": "assessment"},
    {"slug": "seo-emotional-intelligence-test", "title": "Emotional Intelligence Test: How Emotionally Intelligent Are You Really?", "target": "emotional_intelligence-evidence", "terms": ["emotional intelligence test", "eq test", "emotional intelligence quiz", "how emotionally intelligent am I"], "intent": "transactional", "priority": "p0", "cat": "assessment"},
    {"slug": "seo-narcissism-test", "title": "Narcissism Test: Am I a Narcissist or Just Confident?", "target": "narcissism_spectrum-evidence", "terms": ["narcissism test", "am I a narcissist quiz", "narcissistic personality test", "covert narcissist test"], "intent": "transactional", "priority": "p0", "cat": "assessment"},
    {"slug": "seo-codependency-test", "title": "Codependency Test: Are You Codependent?", "target": "codependency-evidence", "terms": ["codependency test", "am I codependent quiz", "codependency assessment", "codependency quiz free"], "intent": "transactional", "priority": "p0", "cat": "assessment"},
    {"slug": "seo-cognitive-distortion-test", "title": "Cognitive Distortion Test: Which Thinking Traps Catch You?", "target": "cognitive_distortions-evidence", "terms": ["cognitive distortion test", "thinking errors quiz", "cognitive distortion quiz", "what cognitive distortions do I have"], "intent": "transactional", "priority": "p0", "cat": "assessment"},
    {"slug": "seo-relationship-health-check", "title": "Relationship Health Check: How Healthy Is Your Relationship?", "target": "relationship_expectations-evidence", "terms": ["relationship health check", "is my relationship healthy", "relationship assessment", "relationship quiz", "healthy relationship test"], "intent": "transactional", "priority": "p0", "cat": "assessment"},
]

for cc in cross_cutting:
    add_ticket(cc["slug"], cc["title"], cc["target"], cc["terms"], cc["intent"], cc["priority"], cc.get("cat", "cross-cutting"))


# ============================================================
# EXISTING LANDING PAGE SEARCH TERM MAPPING
# (Map search terms to the 301 existing landing pages)
# ============================================================
# These don't create NEW tickets but we track them in the summary
existing_mapped_terms = 0
for item in by_type.get('landing', []):
    existing_mapped_terms += 3  # at minimum 3 terms per existing page


# ============================================================
# GENERATE OUTPUT
# ============================================================

# Deduplicate by slug
seen = set()
unique_tickets = []
for t in tickets:
    if t['slug'] not in seen:
        seen.add(t['slug'])
        unique_tickets.append(t)

# Count by target type
by_target_type = {}
for t in unique_tickets:
    target = t['target_page']
    # Determine the type of the target page
    target_type = "cross-cutting"
    for tp_name, tp_items in by_type.items():
        for tp_item in tp_items:
            if tp_item['slug'] == target:
                target_type = tp_name
                break
    if target_type not in by_target_type:
        by_target_type[target_type] = 0
    by_target_type[target_type] += 1

output = {
    "generated_at": datetime.now(timezone.utc).isoformat(),
    "total_landing_tickets": len(unique_tickets),
    "tickets": unique_tickets,
    "summary": {
        "by_target_type": by_target_type,
        "total_search_terms_mapped": search_term_count,
        "existing_landing_pages_with_terms": existing_mapped_terms,
        "new_landing_pages_generated": len(unique_tickets),
        "methodology": "Generated search terms for every content page type: evidence (5 per page), framework (4-8 per page), pattern (5 per page), belief (3 per page), religious (5 per page), political (2-4 per page), crisis (4-6 per page), skill (2-4 per page), comparison (3 per page), plus ~130 high-value cross-cutting landing pages for common queries"
    }
}

with open('/Users/user/personal/sb/trueassess/priv/data/seo_landing_tickets.json', 'w') as f:
    json.dump(output, f, indent=2)

print(f"Total unique landing tickets: {len(unique_tickets)}")
print(f"Total search terms mapped: {search_term_count}")
print(f"By target type: {json.dumps(by_target_type, indent=2)}")
