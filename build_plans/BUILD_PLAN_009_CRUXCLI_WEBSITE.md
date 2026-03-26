# BUILD_PLAN_009: CruxCLI Website

**Created:** 2026-03-26
**Status:** NOT STARTED
**Goal:** Build the CruxCLI marketing website with homepage, features, competitor comparison pages, and roadmap — using the existing `packages/web` Astro scaffold and matching CruxDev's design system for ecosystem consistency.

**Constraint:** Keep Starlight docs at `/docs` — marketing pages are separate Astro pages at root.
**Constraint:** Match CruxDev site design system (dark theme, dev-* color tokens, purple accent) for brand cohesion.
**Constraint:** All competitor claims verified per CruxDev COMPETITORS_PATTERN.md (5-pass research, counter-research mandatory).
**Rule:** Two consecutive clean passes = convergence.

## Document Alignment

- `docs/COMPETITORS.md` — competitor data, feature matrix, moat inventory
- `docs/STRATEGY.md` — market positioning, differentiation
- `docs/PRD.md` — product features, target users
- `ROADMAP.md` — priorities and progress
- CruxDev `docs/WEBSITE_PLANNING.md` — website methodology
- CruxDev `docs/COMPETITORS_PATTERN.md` — comparison page standards

---

## Architecture

```
packages/web/
  src/
    layouts/
      Marketing.astro         # Marketing page layout (nav, footer, SEO)
    pages/
      index.astro             # Homepage
      features.astro          # Feature showcase
      compare/
        index.astro           # Comparison hub
      vs/
        opencode.astro        # CruxCLI vs OpenCode
        claude-code.astro     # CruxCLI vs Claude Code
        gemini-cli.astro      # CruxCLI vs Gemini CLI
        codex-cli.astro       # CruxCLI vs Codex CLI
      roadmap.astro           # Public roadmap
    components/
      Hero.astro
      FeatureCard.astro
      ComparisonTable.astro
      TrustBar.astro
      CTA.astro
    styles/
      marketing.css           # Tailwind theme matching CruxDev
    content/docs/             # Starlight docs (existing, unchanged)
  astro.config.mjs            # Updated with Tailwind plugin
```

### Design System (from CruxDev)

| Token | Value | Usage |
|-------|-------|-------|
| dev-950 | #09090b | Page background |
| dev-900 | #18181b | Card backgrounds |
| dev-700 | #3f3f46 | Borders |
| dev-400 | #a1a1aa | Body text |
| dev-300 | #d4d4d8 | Emphasis text |
| accent | #8b5cf6 | CTAs, highlights |
| accent-hover | #7c3aed | Hover state |

---

## Phase 1: Foundation — Layout + Design System

**Purpose:** Set up the marketing page infrastructure alongside existing Starlight docs.

### Checklist — Phase 1

- [ ] 1.1 Add `@tailwindcss/vite` and `tailwindcss` to packages/web dependencies
- [ ] 1.2 Update `astro.config.mjs` to include Tailwind vite plugin
- [ ] 1.3 Create `src/styles/marketing.css` with CruxDev color tokens (dev-*, accent)
- [ ] 1.4 Create `src/layouts/Marketing.astro` — sticky nav, footer, SEO meta, Schema.org
- [ ] 1.5 Nav links: Home, Features, Compare, Roadmap, Docs (/docs), GitHub
- [ ] 1.6 Footer links: Crux (runcrux.io), CruxDev (cruxdev.dev), CruxCLI (cruxvibe.io), GitHub
- [ ] 1.7 Verify Starlight docs still work at /docs after Tailwind addition
- [ ] 1.8 `npm run build` succeeds with both marketing and docs pages

---

## Phase 2: Homepage

**Purpose:** The landing page — first impression, primary conversion point.

### Checklist — Phase 2

- [ ] 2.1 Hero section: tagline, description, dual CTAs (Get Started + GitHub)
- [ ] 2.2 Trust bar: test count (1204), typecheck (13/13), provider count, mode count
- [ ] 2.3 Problem/solution section: "Without CruxCLI" vs "With CruxCLI" comparison cards
- [ ] 2.4 Moat showcase: 6 unique advantages from COMPETITORS.md moat inventory
- [ ] 2.5 How it works: 4-step flow (Install → Configure → Launch → Build)
- [ ] 2.6 Provider logos or mention: OpenRouter, Anthropic, OpenAI, Google, Ollama
- [ ] 2.7 Final CTA section
- [ ] 2.8 Mobile responsive (test at 375px, 768px, 1024px)

---

## Phase 3: Features Page

**Purpose:** Deep showcase of CruxCLI's capabilities.

### Checklist — Phase 3

- [ ] 3.1 Feature cards for each major capability:
  - Mode→model tier mapping
  - Token budget system
  - Workspace checkpoints
  - Client/server architecture
  - LSP integration
  - Plugin API + MCP
  - Provider-agnostic (75+ models)
  - CruxDev convergence engine integration
- [ ] 3.2 Each feature: title, description, code example or diagram
- [ ] 3.3 Comparison table: CruxCLI vs generic coding agents (feature matrix subset)
- [ ] 3.4 Mobile responsive

---

## Phase 4: Comparison Pages

**Purpose:** SEO-optimized `/vs/` pages for each official competitor. Follow COMPETITORS_PATTERN.md Section 6.

### Checklist — Phase 4

- [ ] 4.1 Create `/compare` hub page listing all 4 competitors with star counts and summary
- [ ] 4.2 Create `/vs/opencode` — CruxCLI vs OpenCode (upstream fork, intelligence layer differentiator)
- [ ] 4.3 Create `/vs/claude-code` — CruxCLI vs Claude Code (open source + provider-agnostic differentiator)
- [ ] 4.4 Create `/vs/gemini-cli` — CruxCLI vs Gemini CLI (mode system + convergence differentiator)
- [ ] 4.5 Create `/vs/codex-cli` — CruxCLI vs Codex CLI (LSP + plugin API differentiator)
- [ ] 4.6 Each comparison page includes: feature table, key differences (where we win), where they win (honest), migration guide if applicable
- [ ] 4.7 SEO: title tags "[CruxCLI] vs [Competitor] — Comparison 2026", Schema.org FAQPage
- [ ] 4.8 Verify all competitor claims against COMPETITORS.md (no unverified claims)

---

## Phase 5: Roadmap Page

**Purpose:** Public roadmap showing progress and planned features.

### Checklist — Phase 5

- [ ] 5.1 Completed section: hard fork, checkpoints, VS Code extension, competitor tracking, Key migration docs
- [ ] 5.2 In progress section: Key domain migration, CruxDev integration hardening
- [ ] 5.3 Planned section: browser automation, enterprise compliance, memory pipeline
- [ ] 5.4 Non-goals section: upstream sync, building what can be integrated
- [ ] 5.5 Competitive gap closure tracker (visual progress)

---

## Phase 6: Build + Deploy

**Purpose:** Production build, deployment pipeline, verification.

### Checklist — Phase 6

- [ ] 6.1 `npm run build` produces clean output (zero warnings)
- [ ] 6.2 All pages render correctly (spot check each page)
- [ ] 6.3 All internal links resolve (no 404s)
- [ ] 6.4 All external links verified (competitor URLs, GitHub, ecosystem URLs)
- [ ] 6.5 Meta tags correct on each page (title, description, OG, canonical)
- [ ] 6.6 Schema.org structured data validates (use Google Rich Results test)
- [ ] 6.7 Mobile responsive verified (375px, 768px, 1024px)
- [ ] 6.8 Lighthouse score: Performance ≥90, Accessibility ≥90, SEO ≥90
- [ ] 6.9 Deployment pipeline configured (Cloudflare Pages or similar)
- [ ] 6.10 DNS configured for cruxvibe.io (or chosen domain)

---

## Post-Execution Convergence Checklist

- [ ] Documentation convergence: docs/INVENTORY.md updated with website pages
- [ ] Website convergence: all pages build, Lighthouse ≥90, links verified
- [ ] Deployment: site live at public URL
- [ ] Patterns update: share website patterns to CruxDev if novel
- [ ] Inbox check: check_inbox() for messages from other sessions

---

## Test Commands

```bash
cd packages/web && npm run build
# Verify all pages build without errors

# Check for broken links
grep -r 'href="/' dist/ | grep -v node_modules | while read line; do
  path=$(echo "$line" | sed 's/.*href="\([^"]*\)".*/\1/')
  [ -f "dist${path}index.html" ] || [ -f "dist${path}.html" ] || echo "BROKEN: $path"
done
```

## Convergence Criteria

- All pages build and render correctly
- All competitor claims verified
- Mobile responsive on 3 breakpoints
- Lighthouse ≥90 on all metrics
- Two consecutive clean audit passes
- Deployed and accessible at public URL
