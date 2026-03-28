# BUILD_PLAN_015: Community Launch & Adoption

**Created:** 2026-03-28
**Status:** NOT STARTED
**Goal:** Close the must-close community/adoption gap. Get CruxCLI from 0 stars to first 100 through strategic launch on developer platforms.

**Constraint:** No paid advertising. Organic only.
**Rule:** Two consecutive clean passes = convergence.

## Document Alignment

- `docs/COMPETITORS.md` — community/adoption is must-close gap
- `docs/STRATEGY.md` — growth strategy
- CruxDev `docs/SEO_AND_GEO_REFERENCE.md` — brand mentions, backlink strategy
- CruxDev `docs/GROWTH_STRATEGY.md` — growth playbook

---

## Phase 1: Launch Readiness

**Purpose:** Verify everything is polished for first impressions.

### Checklist — Phase 1

- [ ] 1.1 README.md has compelling hero section with install command
- [ ] 1.2 Website (cruxcli.io) loads fast, all pages work, blog has content
- [ ] 1.3 GitHub Release v0.2.0 published with all platform binaries
- [ ] 1.4 `curl | bash` installer works
- [ ] 1.5 VS Code extension ready (or clearly marked as coming soon)
- [ ] 1.6 llms.txt and llms-full.txt published for AI visibility

---

## Phase 2: Platform Launches

**Purpose:** Submit to developer platforms where terminal agent users congregate.

### Checklist — Phase 2

- [ ] 2.1 Hacker News Show HN post — "CruxCLI: Provider-agnostic AI coding agent with convergence"
- [ ] 2.2 Reddit r/programming post
- [ ] 2.3 Reddit r/commandline post
- [ ] 2.4 Dev.to article: "Why I forked OpenCode and what CruxCLI does differently"
- [ ] 2.5 Product Hunt launch
- [ ] 2.6 X/Twitter announcement thread via Typefully

---

## Phase 3: Content Seeding

**Purpose:** Create content that appears when developers search for AI coding agents.

### Checklist — Phase 3

- [ ] 3.1 Blog post: "CruxCLI vs OpenCode — what's different and why"
- [ ] 3.2 Blog post: "How CruxDev convergence engine works"
- [ ] 3.3 Blog post: "Provider-agnostic AI coding: why it matters"
- [ ] 3.4 Ensure all comparison pages (/vs/*) have correct Schema.org FAQPage markup

---

## Phase 4: Community Infrastructure

**Purpose:** Set up channels for ongoing community engagement.

### Checklist — Phase 4

- [ ] 4.1 GitHub Discussions enabled on trinsiklabs/cruxcli
- [ ] 4.2 Issue templates (bug report, feature request) created
- [ ] 4.3 Contributing guide polished
- [ ] 4.4 First-timers-only issues labeled for new contributors

---

## Post-Execution Convergence Checklist

- [ ] Documentation convergence
- [ ] Website convergence: deploy any new blog posts
- [ ] Inbox check: check_inbox()

---

## Test Commands

```bash
curl -sI https://cruxcli.io | head -3
gh release view v0.2.0 --repo trinsiklabs/cruxcli
```

## Convergence Criteria

- GitHub Release published with binaries
- Show HN posted
- 3+ blog posts published
- GitHub Discussions enabled
- All comparison pages have Schema.org markup
- Two consecutive clean audit passes
