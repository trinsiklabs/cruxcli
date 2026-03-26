# BUILD_PLAN_009: CruxCLI Website

**Created:** 2026-03-26
**Last Updated:** 2026-03-26
**Status:** NOT STARTED
**Goal:** Build the CruxCLI marketing website following CruxDev WEBSITE_PLANNING.md methodology (Phases 0-12). Marketing pages + comparison pages alongside existing Starlight docs.

**Rule:** Follow CruxDev WEBSITE_PLANNING.md sequentially.
**Rule:** All competitor claims verified per COMPETITORS_PATTERN.md (5-pass research, counter-research mandatory).
**Rule:** Two consecutive clean passes = convergence.

## Document Alignment

- CruxDev `docs/WEBSITE_PLANNING.md` — website methodology (Phases 0-12)
- CruxDev `docs/WEBSITE_ENGINES.md` — engine selection matrix
- CruxDev `docs/COMPETITORS_PATTERN.md` — comparison page standards (Section 6)
- `docs/COMPETITORS.md` — competitor data, feature matrix, moat inventory
- `docs/STRATEGY.md` — market positioning, differentiation
- `docs/PRD.md` — product features, target users
- `ROADMAP.md` — priorities and progress

---

## Phase 0: Pre-Build Setup

**Purpose:** Collect product identity and select website engine per WEBSITE_PLANNING.md §0.

### 0.1 Product Identity

- **Go-to-market name:** CruxCLI
- **Project name:** cruxcli (packages/web in monorepo)
- **Tagline:** "The provider-agnostic AI coding agent with intelligence built in"
- **Domain:** cruxvibe.io (confirmed in CruxDev site footer)

### 0.2 Logo

- Logo files at `packages/identity/mark.svg`, `mark-light.svg`, `mark-512x512.png`
- Favicon: generate from mark.svg

### 0.3 Engine Selection

- **Engine:** Astro (already in use via packages/web with Starlight for docs)
- **Rationale:** Matches CruxDev site (Astro 6 + Tailwind 4), zero JS by default, static generation, Starlight for docs alongside marketing pages
- **Decision:** Keep Starlight at `/docs` subpath, add Tailwind marketing pages at root

### Checklist — Phase 0

- [ ] 0.1 Confirm product identity (name, tagline, domain)
- [ ] 0.2 Verify logo files exist and are usable
- [ ] 0.3 Confirm engine selection (Astro + Tailwind, keep Starlight at /docs)

---

## Phase 1: Discovery & Research

**Purpose:** Understand who the site is for, what it must accomplish, and what exists. Per WEBSITE_PLANNING.md §1.

### 1.1 Stakeholder Discovery

- **Business goal:** Drive adoption of CruxCLI as the provider-agnostic alternative to Claude Code/OpenCode
- **Constraints:** Open source project, no budget for paid tools, solo team
- **Success metrics:** GitHub stars, npm installs, organic traffic, AI citation
- **Content owner:** Bryan (trinsiklabs)

### 1.2 User Research

- **Primary persona:** Senior developer who wants an AI coding agent they control (provider choice, self-hostable, open source)
- **Secondary persona:** Team lead evaluating terminal AI agents for their org
- **Tertiary persona:** Developer migrating from Claude Code/OpenCode wanting more features
- **JTBD:** "I need an AI coding agent that works with my preferred model provider and doesn't lock me in"

### 1.3 Competitive Site Analysis

Use existing `docs/COMPETITORS.md` data. Audit competitor websites:
- opencode.ai — how they position, what pages they have
- claude.ai/claude-code — Anthropic's positioning
- github.com/google-gemini/gemini-cli — Google's approach
- github.com/openai/codex — OpenAI's approach

### 1.4 Requirements

- **Functional:** Static marketing site, no auth/forms needed initially
- **Content:** Homepage, features, comparison pages (4), roadmap, docs (existing)
- **Technical:** Lighthouse ≥90 all metrics, Core Web Vitals green, <500KB initial load
- **Legal:** MIT license, privacy policy (minimal — no tracking initially)

### Checklist — Phase 1

- [ ] 1.1 Document stakeholder goals and constraints
- [ ] 1.2 Define user personas and JTBD
- [ ] 1.3 Audit 4 competitor websites (navigation, content, conversion strategy, SEO)
- [ ] 1.4 Document functional/content/technical/legal requirements

---

## Phase 2: Strategy & Goals

**Purpose:** Define site strategy, conversion goals, success metrics. Per WEBSITE_PLANNING.md §2.

### 2.1 Site Strategy Statement

CruxCLI's website is a developer-focused marketing site for senior developers evaluating AI coding agents. It helps them understand why CruxCLI's provider-agnostic, intelligence-first approach is different from single-vendor tools, and drives them to install and try it. The project benefits through GitHub stars, npm installs, and community growth.

### 2.2 Conversion Goals

- **Primary:** Install CruxCLI (`curl | bash` or `npm i -g`)
- **Secondary:** Star on GitHub
- **Micro:** Read docs, view comparison page, visit roadmap

### 2.3 Success Metrics

| Metric | Target | How Measured |
|--------|--------|-------------|
| Organic traffic | 1,000 visitors/month within 3 months | Plausible analytics |
| GitHub stars | 100 within 3 months of launch | GitHub API |
| Core Web Vitals | All green | PageSpeed Insights |
| AI visibility | Cited when searching "opencode alternative" or "AI coding agent" | Manual testing in Claude/ChatGPT/Perplexity |

### Checklist — Phase 2

- [ ] 2.1 Write site strategy statement
- [ ] 2.2 Define conversion goals (primary, secondary, micro)
- [ ] 2.3 Set success metrics with targets

---

## Phase 3: Content Strategy

**Purpose:** Plan all content before design. Content drives design. Per WEBSITE_PLANNING.md §3.

### 3.1 Page Inventory

| Page | Purpose | Primary Audience | Primary CTA | SEO Target |
|------|---------|-----------------|-------------|------------|
| `/` | Landing/conversion | All | Install | "ai coding agent", "terminal coding agent" |
| `/features` | Feature showcase | Evaluating devs | Install | "cruxcli features" |
| `/vs` | Comparison hub | Evaluating devs | View comparison | "cruxcli vs" |
| `/vs/opencode` | vs OpenCode | OpenCode users | Try CruxCLI | "opencode alternative" |
| `/vs/claude-code` | vs Claude Code | Claude users | Try CruxCLI | "claude code alternative" |
| `/vs/gemini-cli` | vs Gemini CLI | Gemini users | Try CruxCLI | "gemini cli alternative" |
| `/vs/codex-cli` | vs Codex CLI | OpenAI users | Try CruxCLI | "codex cli alternative" |
| `/roadmap` | Public roadmap | Contributors | Star on GitHub | "cruxcli roadmap" |
| `/docs/*` | Documentation | Users | (existing Starlight) | "cruxcli docs" |

### 3.2 Content Sources

- Homepage moats → `docs/COMPETITORS.md` moat inventory
- Feature details → `docs/PRD.md`
- Comparison data → `docs/COMPETITORS.md` feature matrix
- Roadmap → `ROADMAP.md`

### 3.3 Voice & Tone

- Technical, direct, no marketing buzzwords
- Show code, not prose
- Be honest about where competitors win (builds trust per COMPETITORS_PATTERN.md anti-patterns)
- Concrete numbers over vague claims

### Checklist — Phase 3

- [ ] 3.1 Complete page inventory with purpose, audience, CTA, SEO target
- [ ] 3.2 Map content sources to each page
- [ ] 3.3 Define voice and tone guidelines

---

## Phase 4: Information Architecture

**Purpose:** Organize content and define navigation. Per WEBSITE_PLANNING.md §4.

### 4.1 Sitemap

```
/                     Homepage (marketing)
/features             Feature showcase
/vs                   Comparison hub
/vs/opencode          CruxCLI vs OpenCode
/vs/claude-code       CruxCLI vs Claude Code
/vs/gemini-cli        CruxCLI vs Gemini CLI
/vs/codex-cli         CruxCLI vs Codex CLI
/roadmap              Public roadmap
/docs/                Starlight docs (existing)
```

### 4.2 Navigation

**Primary nav (sticky header):**
Home | Features | Compare | Roadmap | Docs | GitHub | [Get Started]

**Footer:**
Crux (runcrux.io) | CruxDev (cruxdev.dev) | CruxCLI (cruxvibe.io) | GitHub

### 4.3 URL Structure

- Lowercase, hyphens: `/vs/claude-code`, `/vs/gemini-cli`
- Docs at `/docs/` via Starlight (existing, unchanged)
- No trailing slashes on marketing pages

### Checklist — Phase 4

- [ ] 4.1 Create sitemap
- [ ] 4.2 Define primary nav and footer nav
- [ ] 4.3 Define URL structure

---

## Phase 5: SEO & AI Visibility Architecture

**Purpose:** Build discoverability into the site. Per WEBSITE_PLANNING.md §5.

### 5.1 Keyword Strategy

| Stage | Keywords |
|-------|----------|
| Awareness | "AI coding agent", "terminal coding agent", "AI pair programming" |
| Consideration | "opencode alternative", "claude code alternative", "best AI coding CLI" |
| Decision | "cruxcli install", "cruxcli getting started", "cruxcli vs opencode" |

### 5.2 Structured Data Plan

| Page Type | Schema.org |
|-----------|-----------|
| Homepage | `SoftwareApplication` + `Organization` |
| Features | `SoftwareApplication` with features list |
| Comparison | `FAQPage` ("How does CruxCLI compare to X?") |
| Roadmap | `ItemList` |

### 5.3 AI Visibility

- Create `/llms.txt` and `/llms-full.txt`
- Answer-first content: lead paragraphs answer the question in 40-80 words
- Concrete numbers: test count, provider count, mode count, binary size
- Brand consistency: "CruxCLI" (not "Crux CLI" or "cruxcli")

### 5.4 Technical SEO

- Unique `<title>` (50-60 chars) and `<meta description>` (150-160 chars) per page
- Open Graph + Twitter Card tags
- XML sitemap (auto-generated)
- Canonical URLs on every page
- Allow all AI crawlers (GPTBot, ClaudeBot, Google-Extended)

### Checklist — Phase 5

- [ ] 5.1 Define keyword strategy (awareness, consideration, decision)
- [ ] 5.2 Plan structured data per page type
- [ ] 5.3 Create llms.txt and llms-full.txt
- [ ] 5.4 Define technical SEO requirements

---

## Phase 6: Design System

**Purpose:** Match CruxDev's design system for ecosystem brand cohesion. Per WEBSITE_PLANNING.md §7.

### 6.1 Design Tokens (from CruxDev)

| Token | Value | Usage |
|-------|-------|-------|
| dev-950 | #09090b | Page background |
| dev-900 | #18181b | Card backgrounds |
| dev-800 | #27272a | Border dark |
| dev-700 | #3f3f46 | Borders |
| dev-600 | #52525b | Muted borders |
| dev-500 | #71717a | Muted text |
| dev-400 | #a1a1aa | Body text |
| dev-300 | #d4d4d8 | Emphasis text |
| accent | #8b5cf6 | CTAs, highlights |
| accent-hover | #7c3aed | Hover state |

### 6.2 Typography

- System font stack (matches CruxDev — no custom fonts, fast loading)
- Body: 16px, dev-400
- Headings: white, bold, tight tracking

### 6.3 Components Needed

- Marketing layout (nav, footer, SEO meta)
- Hero section
- Trust bar (metrics grid)
- Feature cards
- Comparison table
- Problem/solution comparison cards
- CTA sections

### Checklist — Phase 6

- [ ] 6.1 Create `src/styles/marketing.css` with CruxDev color tokens
- [ ] 6.2 Create `src/layouts/Marketing.astro` (sticky nav, footer, SEO meta, Schema.org)
- [ ] 6.3 Create reusable components (Hero, TrustBar, FeatureCard, ComparisonTable, CTA)

---

## Phase 7: Technical Architecture

**Purpose:** Define tech stack and performance budgets. Per WEBSITE_PLANNING.md §8.

### 7.1 Tech Stack

| Component | Choice |
|-----------|--------|
| Framework | Astro 5.x (existing in packages/web) |
| Styling | Tailwind CSS 4.x (via @tailwindcss/vite) |
| Docs | Starlight (existing, at /docs) |
| Output | Static (Cloudflare adapter for docs SSR if needed) |
| Analytics | Plausible (privacy-respecting, no cookie consent needed) |

### 7.2 Performance Budget

| Metric | Target |
|--------|--------|
| LCP | < 2.5s |
| INP | < 200ms |
| CLS | < 0.1 |
| TTFB | < 800ms |
| Total page weight | < 500KB |
| JavaScript | < 200KB compressed |

### Checklist — Phase 7

- [ ] 7.1 Add Tailwind to packages/web dependencies
- [ ] 7.2 Update astro.config.mjs with Tailwind vite plugin
- [ ] 7.3 Verify Starlight docs still work at /docs
- [ ] 7.4 `npm run build` succeeds with marketing + docs pages

---

## Phase 8: Development

**Purpose:** Build all pages with real content. No lorem ipsum. Per WEBSITE_PLANNING.md §9.

### 8.1 Homepage

- [ ] 8.1.1 Hero: tagline, description, dual CTAs (Install + GitHub)
- [ ] 8.1.2 Trust bar: test count (1204), typecheck (13/13), providers (75+), modes (24)
- [ ] 8.1.3 Problem/solution: "Without CruxCLI" vs "With CruxCLI" comparison cards
- [ ] 8.1.4 Moat showcase: 6 unique advantages from COMPETITORS.md
- [ ] 8.1.5 How it works: Install → Configure → Launch → Build
- [ ] 8.1.6 Provider mentions: OpenRouter, Anthropic, OpenAI, Google, Ollama
- [ ] 8.1.7 Final CTA

### 8.2 Features Page

- [ ] 8.2.1 Feature cards: mode→model tiers, token budgets, checkpoints, client/server, LSP, plugins/MCP, provider-agnostic, CruxDev integration
- [ ] 8.2.2 Each feature: title, description, code example or config snippet
- [ ] 8.2.3 Comparison table: CruxCLI vs generic agents (feature matrix subset)

### 8.3 Comparison Pages

- [ ] 8.3.1 `/vs` hub: list all 4 competitors with stars, summary, link
- [ ] 8.3.2 `/vs/opencode`: feature table, where we win (intelligence layer), where they win (community), honest
- [ ] 8.3.3 `/vs/claude-code`: feature table, where we win (open source, provider-agnostic), where they win (first-party model access)
- [ ] 8.3.4 `/vs/gemini-cli`: feature table, where we win (modes, convergence), where they win (free tier)
- [ ] 8.3.5 `/vs/codex-cli`: feature table, where we win (LSP, plugins), where they win (Rust performance)
- [ ] 8.3.6 SEO: title "[CruxCLI] vs [Competitor] — Features & Comparison 2026", FAQPage schema
- [ ] 8.3.7 Verify all claims against COMPETITORS.md

### 8.4 Roadmap Page

- [ ] 8.4.1 Completed: hard fork, checkpoints, VS Code, competitors, Key migration docs
- [ ] 8.4.2 In progress: Key migration, CruxDev integration
- [ ] 8.4.3 Planned: browser automation, enterprise compliance, memory pipeline
- [ ] 8.4.4 Non-goals: upstream sync, building what can be integrated

### 8.5 SEO Assets

- [ ] 8.5.1 Create `/llms.txt`
- [ ] 8.5.2 Create `/llms-full.txt`
- [ ] 8.5.3 XML sitemap auto-generated
- [ ] 8.5.4 robots.txt allowing all crawlers

---

## Phase 9: Pre-Launch QA

**Purpose:** Full QA checklist per WEBSITE_PLANNING.md §10.

### Checklist — Phase 9

- [ ] 9.1 All internal links work (zero 404s)
- [ ] 9.2 All external links verified (competitor URLs, GitHub, ecosystem URLs)
- [ ] 9.3 All pages render correctly at 375px, 768px, 1024px
- [ ] 9.4 Chrome, Firefox, Safari tested
- [ ] 9.5 Meta tags correct on each page (title, description, OG, canonical)
- [ ] 9.6 Schema.org validates (Rich Results Test)
- [ ] 9.7 Core Web Vitals green (mobile + desktop)
- [ ] 9.8 Lighthouse: Performance ≥90, Accessibility ≥90, SEO ≥90
- [ ] 9.9 No placeholder text (all real content)
- [ ] 9.10 Favicon present
- [ ] 9.11 llms.txt accessible
- [ ] 9.12 Keyboard navigation works (all interactive elements reachable)

---

## Phase 10: Launch

**Purpose:** Deploy and verify. Per WEBSITE_PLANNING.md §11.

### Checklist — Phase 10

- [ ] 10.1 Deploy to Cloudflare Pages (or chosen host)
- [ ] 10.2 DNS configured for cruxvibe.io
- [ ] 10.3 SSL valid
- [ ] 10.4 Submit sitemap to Google Search Console
- [ ] 10.5 Verify indexing (all pages crawlable)
- [ ] 10.6 Analytics tracking verified (Plausible)
- [ ] 10.7 Social sharing verified (OG images, descriptions)
- [ ] 10.8 Monitor error logs first 48 hours

---

## Post-Execution Convergence Checklist

- [ ] Documentation convergence: docs/INVENTORY.md updated with website pages
- [ ] Website convergence: all pages build, Lighthouse ≥90, links verified
- [ ] Deployment: site live at cruxvibe.io
- [ ] Patterns update: share website patterns to CruxDev if novel
- [ ] Inbox check: check_inbox() for messages from other sessions
- [ ] Comparison page regeneration: verify generate_comparison_page() integration works

---

## Test Commands

```bash
cd packages/web && npm run build
# Verify all pages build without errors

# Check for broken internal links
grep -r 'href="/' dist/ | grep -v node_modules | while read line; do
  path=$(echo "$line" | sed 's/.*href="\([^"]*\)".*/\1/')
  [ -f "dist${path}index.html" ] || [ -f "dist${path}.html" ] || echo "BROKEN: $path"
done
```

## Convergence Criteria

- All pages build and render correctly
- All competitor claims verified per 5-pass research methodology
- Mobile responsive on 3 breakpoints
- Core Web Vitals green, Lighthouse ≥90 on all metrics
- llms.txt published
- Two consecutive clean audit passes
- Deployed and accessible at cruxvibe.io
