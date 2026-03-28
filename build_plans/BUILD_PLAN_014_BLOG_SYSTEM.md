# BUILD_PLAN_014: Blog System

**Created:** 2026-03-28
**Status:** NOT STARTED
**Goal:** Set up Astro blog with content collections, RSS feed, pagination, tagging, and BIP pipeline integration per CruxDev BLOG_PATTERNS.md.

**Constraint:** Follow CruxDev BLOG_PATTERNS.md, BLOG_POST_PATTERNS.md, BLOG_PAGINATION_PATTERNS.md, BLOG_TAGGING_PATTERNS.md.
**Rule:** Two consecutive clean passes = convergence.

## Document Alignment

- CruxDev `docs/BLOG_PATTERNS.md` — blog architecture patterns
- CruxDev `docs/BLOG_POST_PATTERNS.md` — post content patterns
- CruxDev `docs/BLOG_PAGINATION_PATTERNS.md` — pagination patterns
- CruxDev `docs/BLOG_TAGGING_PATTERNS.md` — tagging patterns
- `.cruxdev/growth.toml` — blog_dir config

---

## Phase 1: Content Collection + Pages

**Purpose:** Set up Astro blog content collection with schema validation, index page, and post pages.

### Checklist — Phase 1

- [ ] 1.1 Add blog collection to content.config.ts with Zod schema (title, description, pubDate, author, tags, category, draft)
- [ ] 1.2 Create /blog/index.astro — list all posts sorted by date, with category badges and tags
- [ ] 1.3 Create /blog/[...slug].astro — individual post pages with Marketing layout
- [ ] 1.4 Create first blog post (announcement)
- [ ] 1.5 Add "Blog" link to Marketing.astro nav
- [ ] 1.6 Verify build succeeds with blog pages

---

## Phase 2: RSS Feed

**Purpose:** RSS feed for blog subscribers and aggregators.

### Checklist — Phase 2

- [ ] 2.1 Install @astrojs/rss package
- [ ] 2.2 Create /blog/rss.xml.ts endpoint
- [ ] 2.3 Add RSS link tag to Marketing.astro head
- [ ] 2.4 Verify RSS validates

---

## Phase 3: BIP Pipeline Integration

**Purpose:** Connect evolution cycle blog drafts to the content collection.

### Checklist — Phase 3

- [ ] 3.1 Verify .cruxdev/evolution/posts/ drafts can be promoted to src/content/blog/
- [ ] 3.2 Add publish_drafts flow: copy from evolution/posts → content/blog with frontmatter
- [ ] 3.3 Test: converge a build plan, verify blog draft appears, promote to blog, build, deploy

---

## Post-Execution Convergence Checklist

- [ ] Documentation convergence: update docs/INVENTORY.md with blog pages
- [ ] Website convergence: deploy updated site to cruxcli.io
- [ ] Inbox check: check_inbox()

---

## Test Commands

```bash
cd packages/web && bun run build 2>&1 | grep -E "error|Complete"
```

## Convergence Criteria

- Blog index and post pages build and render
- RSS feed validates
- First post published
- Nav includes Blog link
- BIP pipeline can promote drafts to blog
- Two consecutive clean audit passes
