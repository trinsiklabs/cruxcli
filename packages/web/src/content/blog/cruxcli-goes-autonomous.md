---
title: "CruxCLI Goes Autonomous"
description: "CruxCLI now runs its own evolution cycle every 4 hours — gathering signals, converging build plans, and publishing results autonomously."
pubDate: 2026-03-28
author: "CruxCLI Team"
tags: ["autonomous", "evolution", "cruxdev", "convergence"]
category: "announcement"
---

CruxCLI is now running in autonomous self-improvement mode. Every 4 hours, the CruxDev evolution cycle scans for work — open GitHub issues, competitive gaps, unconverged build plans, content backlog — prioritizes it, and converges it to completion.

## What This Means

The priority engine ranks work by urgency: bugs first, then competitive gaps, then features. When it finds something to do, it creates a build plan, runs the convergence loop (plan → audit → fix → test → two clean passes), generates a changelog entry and an X post, and moves to the next item.

No human says "do it again." The engine handles that.

## What Got Us Here

Over the past week, CruxCLI went from a hard fork of OpenCode to a fully autonomous project:

- **13 build plans converged** — hard fork, checkpoints, VS Code extension, website, competitors, documentation, ecosystem integration, project-type modes, autonomous bootstrap
- **1,204 tests passing**, 13/13 packages typechecking
- **Website live** at [cruxcli.io](https://cruxcli.io) with comparison pages, roadmap, and SEO/GEO optimization
- **8 new Crux modes** — author, entrepreneur, podcaster, newsletter, youtuber, build-ts, build-rs, build-go
- **Competitor tracking** with 4 official competitors and feature matrix

## The Stack

- **CruxDev** convergence engine (Rust) — plans, audits, and converges
- **Crux** intelligence layer (Rust) — modes, session state, model tiers, safety gates
- **CruxCLI** terminal agent (TypeScript/Bun) — the user-facing coding agent
- **GitHub Issues** for cross-project coordination
- **Typefully** for social publishing

## What's Next

The evolution cycle will now handle:
- Closing competitive gaps (community adoption, cost visibility, image input)
- Monitoring GitHub issues and converting them to build plans
- Keeping comparison pages current against competitor releases
- Publishing build-in-public content as work converges

CruxCLI improves itself. That's the goal.
