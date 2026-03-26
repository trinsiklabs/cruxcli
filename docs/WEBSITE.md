# CruxDev Website

**Last Updated:** 2026-03-26
**URL:** https://cruxdev.dev
**Repository:** /Users/user/personal/cruxdev-dev
**Status:** Live (single-page landing)

## Overview

The CruxDev website is the public marketing site for the CruxDev autonomous convergence engine. It is a separate project from the CruxCLI monorepo, located at `/Users/user/personal/cruxdev-dev`.

Note: This is the CruxDev site, not a CruxCLI site. CruxCLI does not have its own website yet (packages/web exists as a framework but is not deployed).

## Tech Stack

| Component | Technology |
|-----------|-----------|
| Framework | Astro 6.x |
| Styling | Tailwind CSS 4.x (via @tailwindcss/vite plugin) |
| Language | TypeScript |
| Build | `astro build` → `dist/` |
| Dev server | `astro dev` → localhost:4321 |
| Node | >= 22.12.0 |

## Site Structure

```
cruxdev-dev/
  src/
    layouts/Base.astro      # Base HTML layout (nav, footer, SEO meta)
    pages/index.astro       # Landing page (single page)
    styles/global.css       # Tailwind theme (dev-* color palette, accent purple)
  public/
    favicon.svg
  astro.config.mjs          # Astro + Tailwind config
  package.json
  dist/                     # Build output
```

## Pages

Currently a single-page site:

### Landing Page (index.astro)
- **Hero**: Tagline "The convergence engine for AI coding", CTA buttons (Get Started, Read Methodology)
- **Trust bar**: 543 tests, 100% coverage, 18 MCP tools, 2 clean passes
- **Problem section**: "One clean pass isn't enough" — side-by-side comparison (without/with CruxDev)
- **How it works**: 4-step flow (Plan → Audit → Fix & Test → Converge)
- **Safety gates**: Max rounds, timeout, 3-failure rollback, net-negative detection
- **Model tiers**: Table showing task → tier → example model routing
- **Final CTA**: "Stop saying do it again"

### Planned Pages (not yet built)
- `/methodology` — full CruxDev methodology
- `/engine` — engine architecture and API
- `/docs` — documentation hub
- `/docs/quickstart` — getting started guide
- `/blog` — blog/changelog

## Design System

### Color Palette

| Token | Value | Usage |
|-------|-------|-------|
| dev-950 | #09090b | Background |
| dev-900 | #18181b | Card backgrounds |
| dev-800 | #27272a | Borders dark |
| dev-700 | #3f3f46 | Borders |
| dev-600 | #52525b | Muted borders |
| dev-500 | #71717a | Muted text |
| dev-400 | #a1a1aa | Body text |
| dev-300 | #d4d4d8 | Emphasis text |
| accent | #8b5cf6 | Purple accent (CTAs, highlights) |
| accent-hover | #7c3aed | Purple accent hover |

### Typography
- System font stack (no custom fonts)
- Headings: white, bold
- Body: dev-400 (zinc-400 equivalent)
- Accent: purple-500

### Layout
- Max width: 6xl (1152px) for content sections
- Responsive: mobile-first, breakpoints at sm/md/lg
- Sticky nav with backdrop blur

## SEO

- Canonical URLs set per page
- Open Graph meta tags (type, url, title, description)
- Twitter card: summary_large_image
- Schema.org: SoftwareApplication structured data
- Title format: "CruxDev — Autonomous Convergence for AI Coding" (home) / "[Page] | CruxDev" (subpages)

## Navigation

Header nav links:
- Methodology → /methodology
- Engine → /engine
- Docs → /docs
- Blog → /blog
- GitHub → https://github.com/splntrb/cruxdev

Footer links:
- Crux → https://runcrux.io
- CruxCLI → https://cruxvibe.io
- GitHub → https://github.com/splntrb/cruxdev

## Ecosystem URLs

| Product | Domain |
|---------|--------|
| CruxDev | cruxdev.dev |
| Crux | runcrux.io |
| CruxCLI | cruxvibe.io |

## Development

```bash
cd /Users/user/personal/cruxdev-dev
npm install
npm run dev      # localhost:4321
npm run build    # builds to dist/
npm run preview  # preview production build
```

## Deployment

Not yet documented — the site builds to `dist/` but the hosting/deployment pipeline is not configured.

## Known Gaps

- Only landing page exists — methodology, engine, docs, blog pages are linked but not built
- No analytics configured
- No deployment pipeline
- Trust bar numbers (543 tests, 18 tools) need to be kept current
- CruxCLI link in footer points to cruxvibe.io (may need updating)
- No comparison pages per COMPETITORS_PATTERN.md
