# BUILD PLAN: Curiosity Engine UX — Universal Navigation & Discovery Layer

**Status:** NOT STARTED
**Date:** 2026-03-24
**Goal:** Build the overall navigation and discovery experience that makes the knowledge web infinitely explorable — universal search, knowledge graph visualization, side-by-side comparators, trending explorations, personal history, serendipity engine, citation trails, gap mapping, study tracking, and export/sharing. This is the UX shell AROUND the specific interactive tools (Risk Walkthrough, Group Explorer, entity-level Curiosity Engine), not those tools themselves.
**Language:** Elixir (PETAL stack). All new code in `trueassess/`.
**Methodology:** TDD/BDD. Two consecutive clean passes per convergence loop.
**Depends on:**
- BUILD_PLAN_EMPIRICAL_DATA.md (Ash resources: EmpiricalDatapoint, EmpiricalTrendline, EntityComposition, CrossEntityLink)
- BUILD_PLAN_CONFIDENCE_AND_GAPS.md (ConfidenceClassification, EvidenceGap, ProposedStudy, StudyFunding)
- BUILD_PLAN_INTERACTIVE_WALKTHROUGHS.md (RiskProfile, GroupDefinition, ExplorationEdge, ExplorationHighlight, CuriosityEngineLive — this plan wraps and extends those)

---

## Document Alignment

This plan must conform to:
- `/Users/user/personal/sb/pp/CORRELATION_VISIBILITY_STRATEGY.md` — epistemic architecture, no-causation framing, visualization techniques, legal safeguards
- `/Users/user/personal/sb/pp/BUILD_PLAN_INTERACTIVE_WALKTHROUGHS.md` — the specific interactive tools this UX layer wraps (RiskWalkthroughLive, GroupExplorerLive, CuriosityEngineLive)
- `/Users/user/personal/sb/pp/BUILD_PLAN_EMPIRICAL_DATA.md` — Ash resources for empirical data (EmpiricalDatapoint, CrossEntityLink, etc.)
- `/Users/user/personal/sb/pp/BUILD_PLAN_CONFIDENCE_AND_GAPS.md` — confidence tiers, evidence gaps, proposed studies, study funding pipeline
- `/Users/user/personal/sb/pp/CLAUDE.md` — project rules (Elixir/Rust only, TDD/BDD, CruxDev convergence)

---

## Constraints & Rules

1. **No causation claims** — inherited from Empirical Data Layer. CausationGate runs on all rendered text, all search results, all graph labels, all export output. Language: "X and Y tend to move together," never "X causes Y."
2. **Every number cited to source** — no empirical datapoint displays without source_url and source_name. Citation trail must be traceable to primary source in at most 3 clicks.
3. **Counter-examples always shown** — search results, graph nodes, comparisons — all must surface counter-evidence when available. Counter-examples are not a nice-to-have; they are a render requirement.
4. **Gaps are features, not bugs** — missing data renders visibly with "Fund This Study" CTA. Gap Map is a first-class feature.
5. **Privacy-safe everything** — no cookies, no behavioral tracking, no user-click-powered recommendations. "Trending Explorations" and "Surprise Me" are powered by data graph properties (edge weights, statistical outlier scores, highlight counts), NOT by tracking what users click.
6. **Data-driven, not engagement-optimized** — trending = most data-connected, not most clicked. Surprise = highest contrast from expected, not most addictive. This is an epistemic tool, not a feed.
7. **Elixir only** — Phoenix LiveView, Ash resources, Oban workers. No Python. No JS frameworks. Alpine.js for micro-interactions only. D3.js for knowledge graph visualization (the one JS library exception — force-directed graphs require it).
8. **TDD always** — tests before code, 100% coverage target.
9. **Phases <= 10 tasks each** — atomic, resumable, independently testable.
10. **Integrates with existing Interactive domain** — uses `Trueassess.Interactive` resources (ExplorationEdge, ExplorationHighlight, GroupDefinition, RiskProfile) and extends them. Does NOT duplicate data structures that already exist.

---

## Architecture Overview

### Before (Interactive Walkthroughs plan)

```
RiskWalkthroughLive  --->  standalone tool at /explore/risk/:slug
GroupExplorerLive    --->  standalone tool at /explore/groups
CuriosityEngineLive  --->  entity-level exploration at /explore/entity/:type/:slug

Each tool is self-contained. No unified search. No cross-tool discovery.
No graph visualization. No history. No trending. No export.
Users must know which tool to use and navigate to it manually.
```

### After (Curiosity Engine UX)

```
                         ┌─────────────────────────────────┐
                         │     Universal Search Bar         │
                         │  "depression in Japan"           │
                         │  "CBT vs DBT" -> Comparator      │
                         │  "are vegans happy" -> results    │
                         └──────────┬──────────────────────┘
                                    │
               ┌────────────────────┼────────────────────────┐
               │                    │                        │
               v                    v                        v
    ┌──────────────────┐  ┌─────────────────┐  ┌───────────────────────┐
    │ Knowledge Graph   │  │ "What If"       │  │ Exploration Hub       │
    │ Visualization     │  │ Comparator      │  │                       │
    │ (force-directed)  │  │ (side-by-side)  │  │ - Trending paths      │
    │ - zoom/filter     │  │ - any 2 entities│  │ - Surprise Me         │
    │ - click to drill  │  │ - any dimension │  │ - Gap Map             │
    │ - cluster coloring│  │ - citations     │  │ - Study Tracker       │
    └────────┬─────────┘  └────────┬────────┘  │ - Personal History    │
             │                     │            └───────────┬───────────┘
             └─────────┬───────────┘                        │
                       │                                    │
                       v                                    v
            ┌──────────────────────────────────────────────────┐
            │              Citation Trail                       │
            │  Click any number -> full chain to primary source │
            │  CrossEntityLink -> EmpiricalDatapoint -> source  │
            └──────────────────────────────────────────────────┘
                       │
                       v
            ┌──────────────────────────────────────────────────┐
            │              Export / Share                        │
            │  Image (PNG/SVG), PDF, shareable link w/ citations│
            │  Privacy-safe: encodes state, never identity      │
            └──────────────────────────────────────────────────┘

Existing tools integrate seamlessly:
  - Search "divorce risk" -> routes to RiskWalkthroughLive
  - Search "mormons vs atheists" -> routes to GroupExplorerLive with pre-selection
  - Graph node click -> routes to CuriosityEngineLive for that entity
  - Any data point click -> Citation Trail
  - Any view -> Export/Share
```

### Data Flow Example: "Are vegans happy?"

```
1. User types "are vegans happy" in Universal Search Bar
   -> SearchEngine.search("are vegans happy")
   -> Intent detection: group query (vegans) + dimension query (happiness)
   -> Returns:
      a) GroupOutcome for "vegans" on "happiness" dimension (if exists)
      b) Related entities: "vegetarians", "plant-based", "dietary identity"
      c) Related dimensions: "life satisfaction", "depression rate", "purpose"
      d) Knowledge graph neighborhood of "vegans" node
      e) Gaps: "No longitudinal vegan happiness data" with Fund This Study CTA

2. User clicks the top result (GroupOutcome: vegans + happiness)
   -> Routes to CuriosityEngineLive for entity "vegans"
   -> Highlights: "Vegans report 4.2/10 life satisfaction (Gallup subset)"
   -> Counter: "Sample size only N=312, :hypothesis tier"
   -> Suggestions: "Compare with vegetarians?", "See depression data?"

3. User clicks "Compare with vegetarians"
   -> Routes to WhatIfComparatorLive with vegans vs vegetarians pre-loaded
   -> Side-by-side: happiness, depression, life satisfaction, income, social belonging
   -> Each cell shows value + confidence badge + citation
   -> Gaps highlighted: "No vegan-specific depression data"

4. User clicks "Show on Graph"
   -> KnowledgeGraphLive renders with vegans + vegetarians highlighted
   -> Cluster: dietary identity groups (vegans, vegetarians, pescatarians, omnivores)
   -> Cross-cluster edges: "vegans" linked to "environmentalism", "animal rights"
   -> User zooms into the dietary cluster, sees all connected data

5. User clicks "Export as PDF"
   -> PDF generated with: comparison table, citations, methodology note, disclaimer
   -> Shareable link: /explore/compare/vegans/vegetarians?dims=happiness,depression
```

---

## Phase Ordering & Dependencies

```
Phase 1: Search Infrastructure (Ash resources, indexing, intent detection)
    |
    v
Phase 2: Universal Search LiveView (search bar, results, routing)
    |
    v
Phase 3: Knowledge Graph Data Layer (graph serialization, clustering, filtering)
    |
    v
Phase 4: Knowledge Graph LiveView (D3.js force-directed, zoom, filter, click)
    |
    v
Phase 5: "What If" Comparator (Ash resources, query layer, LiveView)
    |
    v
Phase 6: Exploration Hub — Trending, Surprise Me, Personal History
    |
    v
Phase 7: Citation Trail + Gap Map
    |
    v
Phase 8: Study Impact Tracker
    |
    v
Phase 9: Export / Share System
    |
    v
Phase 10: E2E Tests, Integration, Documentation & Convergence
```

---

## Phase 1: Search Infrastructure

**Purpose:** Build the search index, intent detection, and result ranking system that powers the Universal Search Bar. This is the foundation — every other feature routes through search.

**Files:**
- `test/trueassess/exploration/search_index_test.exs`
- `test/trueassess/exploration/intent_detector_test.exs`
- `test/trueassess/exploration/result_ranker_test.exs`
- `test/trueassess/exploration/resources/search_entry_test.exs`
- `lib/trueassess/exploration.ex` (Ash domain)
- `lib/trueassess/exploration/resources/search_entry.ex`
- `lib/trueassess/exploration/search_index.ex`
- `lib/trueassess/exploration/intent_detector.ex`
- `lib/trueassess/exploration/result_ranker.ex`
- Migration file for search_entries table

**Tasks (10):**

- [ ] Write tests for `SearchEntry` Ash resource: CRUD, validations (required: entity_type, entity_id, title, searchable_text, entry_type). `entity_type`: :group, :risk_profile, :outcome_dimension, :entity, :empirical_datapoint, :evidence_gap, :proposed_study. `entry_type`: :entity, :datapoint, :comparison, :gap, :study. `searchable_text`: concatenated text for full-text search (title + description + tags + aliases). `tags`: list of strings. `data_richness_score`: float 0.0-1.0 (how much data exists for this entity — more data = higher ranking). Identity: entity_type + entity_id unique.
- [ ] Write tests for `SearchIndex.build_from_entities/0`: scans all GroupDefinitions, RiskProfiles, OutcomeDimensions, entities with EmpiricalDatapoints, EvidenceGaps, and ProposedStudies. Creates or updates SearchEntry records for each. Computes `data_richness_score` as: (number of datapoints for this entity) / (max datapoints for any entity of same type). Idempotent.
- [ ] Write tests for `SearchIndex.build_from_entities/0` edge cases: entity with zero datapoints gets score 0.0, entity with aliases (GroupDefinition.search_terms) gets those terms in searchable_text, entity that was deleted gets its SearchEntry removed.
- [ ] Write tests for `IntentDetector.detect/1`: given a search query string, returns `%{intent, entities, dimensions, modifiers}`. Intents: `:entity_lookup` ("depression"), `:comparison` ("CBT vs DBT", "mormons vs atheists"), `:question` ("are vegans happy", "does meditation help"), `:risk_query` ("divorce risk"), `:group_query` ("mormons happiness"), `:gap_query` ("what's missing on vegans"), `:open_exploration` (everything else). Test: "depression in Japan" -> `%{intent: :entity_lookup, entities: ["japan"], dimensions: ["depression"]}`. "CBT vs DBT" -> `%{intent: :comparison, entities: ["cbt", "dbt"]}`. "are vegans happy" -> `%{intent: :question, entities: ["vegans"], dimensions: ["happiness"]}`.
- [ ] Write tests for `IntentDetector.detect/1` with modifiers: "divorce risk for atheists" -> `%{intent: :risk_query, entities: ["atheists"], modifiers: ["divorce"]}`. "trending" -> `%{intent: :open_exploration, modifiers: ["trending"]}`. "surprise me" -> `%{intent: :open_exploration, modifiers: ["surprise"]}`. Empty string -> `%{intent: :open_exploration}`.
- [ ] Implement `Trueassess.Exploration` Ash domain module, `SearchEntry` resource, and migration — GREEN all resource tests.
- [ ] Implement `SearchIndex.build_from_entities/0` — GREEN. Uses Postgres full-text search (tsvector/tsquery) via the searchable_text column. Add GIN index on searchable_text.
- [ ] Implement `IntentDetector.detect/1` — GREEN. Uses pattern matching on common query shapes (X vs Y, "are X happy", "X in Y", "X risk for Y"). Falls back to `:open_exploration` for unrecognized patterns. No LLM dependency — pure pattern matching + keyword extraction.
- [ ] Write tests for `ResultRanker.rank/2`: given a list of SearchEntry matches and the detected intent, returns ranked results. Ranking factors: (a) text relevance score from Postgres full-text search, (b) data_richness_score (entities with more data rank higher), (c) intent boost (if intent is :comparison and result is a pair, boost it; if intent is :risk_query and result is a RiskProfile, boost it), (d) confidence boost (entities with more :irrefutable datapoints rank higher). Verify: empty results -> [], single result -> [that result], 50 results ranked correctly.
- [ ] Implement `ResultRanker.rank/2` — GREEN. Write Oban worker `RebuildSearchIndex` that calls `SearchIndex.build_from_entities/0`. Scheduled daily. GREEN worker test.

**Key Design Decision: Postgres Full-Text Search, Not Elasticsearch**

For the current data scale (thousands of entities, not millions), Postgres tsvector/tsquery with GIN indexes provides sufficient search performance without adding an external service dependency. If scale demands it later, the SearchEntry resource provides a clean abstraction boundary for swapping in Elasticsearch or Meilisearch — the SearchIndex module is the only thing that touches the search implementation.

---

## Phase 2: Universal Search LiveView

**Purpose:** The search bar that sits at the top of every /explore page. Type anything, get instant results with intent-aware routing.

**Files:**
- `test/trueassess_web/live/explore_live_test.exs`
- `test/trueassess_web/live/components/search_bar_component_test.exs`
- `test/trueassess_web/live/components/search_result_card_component_test.exs`
- `lib/trueassess_web/live/explore_live.ex`
- `lib/trueassess_web/components/search_bar_component.ex`
- `lib/trueassess_web/components/search_result_card_component.ex`
- `lib/trueassess_web/components/intent_hint_component.ex`

**Tasks (10):**

- [ ] Write LiveView tests for `ExploreLive` mount: `GET /explore` renders the Universal Search Bar prominently centered, with placeholder text cycling through example queries ("depression in Japan", "CBT vs DBT", "are vegans happy", "divorce risk for atheists"). Below the search bar: Trending Explorations (placeholder for Phase 6), "Surprise Me" button (placeholder for Phase 6), recent explorations (placeholder for Phase 6).
- [ ] Write LiveView tests for search-as-you-type: typing in the search bar triggers `handle_event("search", %{"query" => ...})` with debounce (300ms). Results render below the search bar as cards. Each card shows: title, entity_type badge, data_richness indicator (filled dots), snippet of matching text. Verify: empty query -> no results, "japan" -> results containing Japan, "CBT vs DBT" -> comparison intent detected.
- [ ] Write LiveView tests for intent-aware routing: when user selects a result, routing depends on intent + result type. Entity result -> `/explore/entity/:type/:slug` (CuriosityEngineLive). Comparison result -> `/explore/compare/:slug1/:slug2` (WhatIfComparatorLive, Phase 5). Risk profile result -> `/explore/risk/:slug` (RiskWalkthroughLive). Group result with dimension -> `/explore/groups` with pre-selection. Verify each routing path.
- [ ] Write LiveView tests for `IntentHintComponent`: as user types, a subtle hint appears below the search bar indicating detected intent. "CBT vs DBT" -> "Comparison mode: we'll show these side by side". "are vegans happy" -> "Looking for: vegans + happiness data". "divorce risk" -> "Risk explorer: walk through factors step by step". Verify hints render correctly and update on keystroke.
- [ ] Write LiveView tests for keyboard navigation: arrow keys move through results, Enter selects the highlighted result, Escape clears the search. Tab moves to first result. Verify accessibility: results have proper ARIA roles, search input has ARIA label.
- [ ] Write LiveView tests for "no results" state: searching for something with no matches shows: "No data found for [query]" + "This might be a gap in our knowledge web" + link to Gap Map (Phase 7) + "Suggest this topic" CTA that creates a lightweight suggestion (stored for editorial review).
- [ ] Implement `SearchBarComponent` — function component with phx-debounce, live search event emission, cycling placeholder text (Alpine.js for placeholder animation only). GREEN.
- [ ] Implement `SearchResultCardComponent` — function component rendering one search result with type badge, richness dots, text snippet with query terms highlighted. `IntentHintComponent` — renders intent detection feedback. GREEN component tests.
- [ ] Implement `ExploreLive` — full LiveView. Mount loads no results (search-first UX). `handle_event("search", ...)` calls `SearchIndex`, `IntentDetector`, and `ResultRanker` in sequence. `handle_event("select_result", ...)` routes based on intent. Uses `handle_params` for URL-driven state (`/explore?q=depression+in+japan`). GREEN all LiveView tests.
- [ ] Add routes: `live "/explore", ExploreLive` as the main exploration entry point. Add `SearchBarComponent` as an includable component in the shared layout (appears on all `/explore/*` pages as a sticky header bar). Verify route + layout integration.

**LiveView Socket Assigns:**

```elixir
%{
  query: string,
  intent: %{intent: atom, entities: [string], dimensions: [string], modifiers: [string]} | nil,
  results: [%SearchEntry{}],
  selected_index: integer,        # keyboard navigation
  loading: boolean,
  show_hints: boolean,
  placeholder_index: integer      # cycling placeholder text
}
```

---

## Phase 3: Knowledge Graph Data Layer

**Purpose:** Build the data serialization, clustering, and filtering modules that prepare graph data for the frontend visualization. The graph is built from ExplorationEdge records (from Interactive Walkthroughs Phase 7) plus CrossEntityLinks (from Empirical Data Layer).

**Files:**
- `test/trueassess/exploration/graph_serializer_test.exs`
- `test/trueassess/exploration/graph_clusterer_test.exs`
- `test/trueassess/exploration/graph_filter_test.exs`
- `lib/trueassess/exploration/graph_serializer.ex`
- `lib/trueassess/exploration/graph_clusterer.ex`
- `lib/trueassess/exploration/graph_filter.ex`

**Tasks (10):**

- [ ] Write tests for `GraphSerializer.to_json/1`: given a list of entities (nodes) and ExplorationEdge records (edges), returns a JSON-serializable map `%{nodes: [...], edges: [...], metadata: %{}}`. Each node: `%{id, type, label, data_richness, highlight_count, group}`. Each edge: `%{source, target, weight, edge_type, context}`. Verify: empty graph -> empty nodes/edges, graph with 1 node -> 1 node 0 edges, graph with 100 nodes and 500 edges -> correct counts and all fields populated.
- [ ] Write tests for `GraphSerializer.to_json/1` with filtering: accepts options `%{min_weight: float, edge_types: [atom], entity_types: [atom], max_nodes: integer}`. `min_weight: 0.5` filters out weak edges. `edge_types: [:empirical_link]` shows only empirical connections. `entity_types: [:group, :country]` shows only those node types. `max_nodes: 50` returns the 50 most-connected nodes. Verify each filter independently and in combination.
- [ ] Write tests for `GraphClusterer.detect_clusters/1`: given a graph (nodes + edges), returns cluster assignments `%{node_id => cluster_id}`. Uses Louvain community detection algorithm. Verify: disconnected components -> separate clusters, clique -> one cluster, two cliques connected by single edge -> two clusters.
- [ ] Write tests for `GraphClusterer.label_clusters/2`: given cluster assignments and the underlying nodes, generates human-readable cluster labels based on the most common entity_type and tags within each cluster. E.g., cluster containing "mormons", "catholics", "evangelicals" -> label "Religious Groups". Verify labels are generated for all clusters.
- [ ] Write tests for `GraphFilter.neighborhood/3`: given entity_type, entity_id, and depth (1, 2, or 3), returns all nodes within N hops. Depth 1 = direct neighbors. Depth 2 = neighbors of neighbors. Depth 3 = max depth (prevent explosion). Verify: isolated node -> just itself, node with 5 neighbors at depth 1 -> 6 nodes, depth 2 with branching -> correct expansion.
- [ ] Write tests for `GraphFilter.subgraph_for_query/2`: given a search query (from IntentDetector output), returns the relevant subgraph. For `:entity_lookup` -> neighborhood(entity, 2). For `:comparison` -> union of neighborhoods of both entities. For `:question` -> neighborhood of entity filtered to dimension-relevant edges. Verify each intent produces a reasonable subgraph.
- [ ] Implement `GraphSerializer.to_json/1` with all filtering options — GREEN.
- [ ] Implement `GraphClusterer.detect_clusters/1` and `label_clusters/2` — GREEN. Louvain algorithm implemented as pure Elixir (no external dependency). The algorithm iterates: (a) assign each node to its own community, (b) for each node, try moving it to each neighbor's community, keep the move that maximizes modularity, (c) repeat until no moves improve modularity.
- [ ] Implement `GraphFilter.neighborhood/3` and `subgraph_for_query/2` — GREEN.
- [ ] Write integration test: given seeded data (from Interactive Walkthroughs Phase 3 seed loaders), `GraphSerializer.to_json/1` produces valid JSON for the full graph. `GraphClusterer.detect_clusters/1` produces at least 2 clusters. `GraphFilter.neighborhood/3` for "mormons" returns at least 3 nodes. Verify data flows correctly from Ash resources through serialization.

**Key Design Decision: Louvain in Elixir, Not a Graph Database**

At current scale (hundreds to low thousands of entities), Louvain community detection runs in milliseconds in pure Elixir. The graph data lives in Postgres via ExplorationEdge records and is loaded into memory for computation. If scale demands it, Neo4j or a dedicated graph database can be introduced behind the same API boundary. The GraphSerializer module is the abstraction layer.

---

## Phase 4: Knowledge Graph LiveView

**Purpose:** Interactive force-directed graph visualization using D3.js (via LiveView hooks) with zoom, filter, click-to-drill, and cluster coloring.

**Files:**
- `test/trueassess_web/live/knowledge_graph_live_test.exs`
- `test/trueassess_web/live/components/graph_controls_component_test.exs`
- `lib/trueassess_web/live/knowledge_graph_live.ex`
- `lib/trueassess_web/components/graph_controls_component.ex`
- `assets/js/hooks/knowledge_graph_hook.js`
- `assets/js/knowledge_graph/force_layout.js`
- `assets/js/knowledge_graph/interactions.js`
- `assets/js/knowledge_graph/renderer.js`

**Tasks (10):**

- [ ] Write LiveView tests for `KnowledgeGraphLive` mount: `GET /explore/graph` loads the full graph (or a filtered subset if params present). Socket assigns include: `graph_data` (JSON from GraphSerializer), `clusters` (from GraphClusterer), `filters` (current filter state), `selected_node` (nil initially). Verify mount succeeds and graph_data is non-empty with seeded data.
- [ ] Write LiveView tests for filter controls: changing `min_weight` slider triggers `handle_event("filter", %{"min_weight" => "0.7"})`. Graph data re-serialized with new filter. Changing entity_type checkboxes filters node types. Changing edge_type checkboxes filters edge types. Verify socket assigns update correctly after each filter change.
- [ ] Write LiveView tests for node selection: clicking a node (via JS hook pushEvent) triggers `handle_event("select_node", %{"id" => id, "type" => type})`. Selected node's details render in a sidebar panel: entity name, type, data_richness, key metrics, ExplorationHighlights, and a "Explore This" button that routes to CuriosityEngineLive. Verify sidebar renders with correct data.
- [ ] Write LiveView tests for search-to-graph integration: navigating to `/explore/graph?entity=mormons&depth=2` pre-filters the graph to show the neighborhood of "mormons" at depth 2, with "mormons" centered and highlighted. Verify `handle_params` processes the entity + depth params correctly.
- [ ] Write LiveView tests for cluster coloring: clusters detected by GraphClusterer are assigned colors. The graph data includes `group` field on each node corresponding to cluster_id. The JS hook uses group for color assignment. Verify cluster labels render in a legend panel. Verify clicking a cluster label highlights all nodes in that cluster.
- [ ] Write `GraphControlsComponent` — function component rendering: min_weight slider (0.0-1.0), entity_type checkboxes, edge_type checkboxes, depth selector (1/2/3 for neighborhood views), cluster toggle (show/hide cluster coloring), "Reset" button. GREEN component tests.
- [ ] Write `knowledge_graph_hook.js` — LiveView hook that: (a) receives graph_data JSON from server via `handleEvent`, (b) initializes D3 force-directed layout with SVG rendering, (c) handles zoom/pan via D3.zoom, (d) handles node click -> pushEvent to server, (e) handles node hover -> tooltip with name + type + data_richness, (f) handles semantic zoom (zoom in = show labels, zoom out = show cluster structure). Uses `force_layout.js`, `interactions.js`, `renderer.js` as sub-modules.
- [ ] Write `force_layout.js` — D3 force simulation configuration: charge force (repulsion between nodes), link force (attraction along edges, strength proportional to weight), center force, collision force. Node size proportional to data_richness. Edge thickness proportional to weight. Edge color by edge_type. Write `renderer.js` — SVG rendering: nodes as circles with type-specific colors, edges as lines with arrowheads for directed relationships, labels on zoom-in, cluster background hulls. Write `interactions.js` — zoom, pan, node drag, click, hover.
- [ ] Implement `KnowledgeGraphLive` — full LiveView. Mount loads graph via `GraphSerializer.to_json/1` with filters from params. `handle_event("filter", ...)` re-serializes graph. `handle_event("select_node", ...)` loads node details. `handle_params` for URL-driven state. Pushes graph_data to JS hook via `push_event`. GREEN all LiveView tests (server-side only — JS hook tested manually + with Wallaby if available).
- [ ] Add route: `live "/explore/graph", KnowledgeGraphLive`. Add "Show on Graph" link from CuriosityEngineLive, GroupExplorerLive, and RiskWalkthroughLive that routes to `/explore/graph?entity=:slug&depth=2`. Verify route integration.

**LiveView Socket Assigns:**

```elixir
%{
  graph_data: map(),              # JSON-serializable graph for JS hook
  clusters: %{node_id => cluster_id},
  cluster_labels: %{cluster_id => string},
  filters: %{
    min_weight: float,
    entity_types: [atom],
    edge_types: [atom],
    max_nodes: integer
  },
  selected_node: %{type: atom, id: string, name: string, metrics: [...], highlights: [...]} | nil,
  focus_entity: %{type: atom, id: string} | nil,  # for neighborhood views
  focus_depth: integer,
  show_clusters: boolean
}
```

**JS Architecture Note:**

D3.js is the single JavaScript dependency. The force_layout.js, interactions.js, and renderer.js modules are vanilla JS (no framework). They communicate with LiveView exclusively through the hook interface: `this.handleEvent("graph_data", callback)` to receive data, `this.pushEvent("select_node", payload)` to send clicks back. All state lives on the server in socket assigns. The JS layer is a pure rendering layer with no application state.

---

## Phase 5: "What If" Comparator

**Purpose:** Side-by-side comparison of any two entities on any dimension. The "What If" Comparator is the tool users reach when they want to directly compare: "What if I'm Mormon vs Atheist? What if I do CBT vs DBT? What if I live in Japan vs the US?"

**Files:**
- `test/trueassess/exploration/comparator_test.exs`
- `test/trueassess_web/live/comparator_live_test.exs`
- `test/trueassess_web/live/components/comparison_column_component_test.exs`
- `test/trueassess_web/live/components/dimension_row_component_test.exs`
- `lib/trueassess/exploration/comparator.ex`
- `lib/trueassess_web/live/comparator_live.ex`
- `lib/trueassess_web/components/comparison_column_component.ex`
- `lib/trueassess_web/components/dimension_row_component.ex`
- `lib/trueassess_web/components/delta_indicator_component.ex`

**Tasks (10):**

- [ ] Write tests for `Comparator.compare/2`: given two entity identifiers `{type, slug}`, returns `%{entity_a: %{...}, entity_b: %{...}, dimensions: [%{slug, name, value_a, value_b, delta, confidence_a, confidence_b, source_a, source_b, higher_is_better}], shared_connections: [...], unique_to_a: [...], unique_to_b: [...]}`. Dimensions include ALL OutcomeDimensions + all EmpiricalDatapoint metric_names that both entities have data for. `delta`: absolute difference with direction arrow. Verify: two entities with overlapping data -> populated dimensions, two entities with no overlap -> empty dimensions with gap indicators, same entity compared to itself -> all deltas zero.
- [ ] Write tests for `Comparator.compare/2` with dimension filtering: accepts optional `dimensions: [slug]` to compare only specific dimensions. Accepts `include_gaps: boolean` (default true) to show/hide dimensions where one entity has data and the other doesn't. Verify filtering works correctly.
- [ ] Write tests for `Comparator.find_comparables/1`: given one entity `{type, slug}`, returns a ranked list of suggested comparison targets. Ranking: (a) same entity_type (group vs group, country vs country), (b) high data overlap (both have data on many shared dimensions), (c) high contrast (entities with very different values are more interesting comparisons). Returns top 10 suggestions with a `comparison_interest_score`.
- [ ] Write tests for `Comparator.compare/2` counter-evidence integration: for each dimension where entity_a and entity_b differ significantly (delta > 1 standard deviation), include `confounders` and `counter_evidence` from the underlying GroupOutcome or EmpiricalDatapoint. Verify: counter-evidence populated for high-contrast dimensions, absent for similar-value dimensions.
- [ ] Write LiveView tests for `ComparatorLive` mount: `GET /explore/compare` shows two entity picker inputs (search-as-you-type, reusing SearchBarComponent logic). `GET /explore/compare/:slug_a/:slug_b` pre-loads the comparison. Verify: empty state shows pickers, pre-loaded state shows comparison table.
- [ ] Write LiveView tests for comparison interaction: selecting entity A triggers suggestions for entity B (from `find_comparables/1`). Selecting entity B triggers comparison. Dimensions render as rows with values side by side, delta indicators, confidence badges, and citations. Clicking a dimension row expands it to show: confounders, counter-evidence, methodology notes, data sources. Verify expand/collapse works.
- [ ] Write LiveView tests for "Swap" and "Add Third": "Swap" button reverses A and B (cosmetic — same data, different column order). "Add Third" allows a third entity for three-way comparison (table expands to three columns). Maximum 5 entities. Verify swapping and adding work.
- [ ] Implement `Comparator` module — `compare/2`, `find_comparables/1` — GREEN.
- [ ] Implement `ComparisonColumnComponent` (one entity's data column), `DimensionRowComponent` (one row in the comparison table with expand/collapse), `DeltaIndicatorComponent` (visual delta with arrow + magnitude + color coding: green = entity_a higher on positive dimension, red = entity_a higher on negative dimension). GREEN component tests.
- [ ] Implement `ComparatorLive` — full LiveView. Mount with picker or pre-loaded state. `handle_event("search_entity", ...)` for entity selection. `handle_event("select_entity", ...)` triggers comparison. `handle_event("expand_dimension", ...)` for drill-down. `handle_event("swap", ...)` and `handle_event("add_entity", ...)` for multi-entity comparison. URL state: `/explore/compare/:slug_a/:slug_b?dims=happiness,depression`. GREEN all LiveView tests. Add route: `live "/explore/compare", ComparatorLive` and `live "/explore/compare/:slug_a/:slug_b", ComparatorLive`.

**LiveView Socket Assigns:**

```elixir
%{
  entity_a: %{type: atom, id: string, name: string} | nil,
  entity_b: %{type: atom, id: string, name: string} | nil,
  additional_entities: [%{type: atom, id: string, name: string}],
  comparison: %{dimensions: [...], shared_connections: [...]} | nil,
  suggestions: [%{entity: %{type, id, name}, interest_score: float}],
  expanded_dimensions: MapSet.t(),
  dimension_filter: [string] | nil,       # nil = show all
  search_query_a: string,
  search_query_b: string,
  search_results_a: [%SearchEntry{}],
  search_results_b: [%SearchEntry{}]
}
```

---

## Phase 6: Exploration Hub — Trending, Surprise Me, Personal History

**Purpose:** The discovery features that make the knowledge web self-propelling. Trending explorations show what's data-richest (NOT most-clicked). Surprise Me surfaces high-contrast data. Personal History lets users track their exploration trails.

**Files:**
- `test/trueassess/exploration/trending_test.exs`
- `test/trueassess/exploration/surprise_engine_test.exs`
- `test/trueassess/exploration/resources/exploration_session_test.exs`
- `test/trueassess/exploration/resources/saved_exploration_test.exs`
- `test/trueassess_web/live/components/trending_panel_component_test.exs`
- `test/trueassess_web/live/components/surprise_card_component_test.exs`
- `test/trueassess_web/live/components/history_panel_component_test.exs`
- `lib/trueassess/exploration/trending.ex`
- `lib/trueassess/exploration/surprise_engine.ex`
- `lib/trueassess/exploration/resources/exploration_session.ex`
- `lib/trueassess/exploration/resources/saved_exploration.ex`
- `lib/trueassess_web/components/trending_panel_component.ex`
- `lib/trueassess_web/components/surprise_card_component.ex`
- `lib/trueassess_web/components/history_panel_component.ex`
- Migration file for exploration_sessions and saved_explorations tables

**Tasks (10):**

- [ ] Write tests for `Trending.top_explorations/1`: returns the top N most data-connected entities. Ranking is based ONLY on data properties, NOT user behavior: (a) data_richness_score (from SearchEntry), (b) number of ExplorationEdge connections, (c) number of ExplorationHighlights, (d) recency of data updates (freshly updated entities get a boost). This is a "trending in the knowledge web" metric — entities where the most data converges. Verify: returns N results, sorted by composite score, no user tracking involved.
- [ ] Write tests for `Trending.top_explorations/1` with freshness: entities whose underlying EmpiricalDatapoints were updated in the last 7 days get a 2x boost. Entities with new ExplorationHighlights in the last 7 days get a 1.5x boost. Verify freshness boost changes ordering.
- [ ] Write tests for `SurpriseEngine.generate/0`: returns a single high-contrast data point. Selection criteria: (a) draw from ExplorationHighlights of type :statistical_outlier or :paradox, (b) prioritize highlights with higher contrast (further from expected value), (c) never return the same highlight twice in a row (maintains a small rotation set). Returns `%{highlight: %ExplorationHighlight{}, framing: string, counter: string}` where `framing` is a one-sentence description and `counter` is the counter-evidence.
- [ ] Write tests for `SurpriseEngine.generate/0` assumption-challenging behavior: the "Surprise Me" feature's entire purpose is to challenge assumptions. Test that: highlights of type :paradox are preferred 2:1 over :statistical_outlier, the framing text does NOT use causal language (CausationGate check), the counter-evidence is always present. Verify with multiple calls that variety is maintained (no repeats within 10 calls).
- [ ] Write tests for `ExplorationSession` Ash resource: CRUD, validations (required: session_token, started_at). `session_token`: a random UUID stored in browser localStorage via Alpine.js (NOT a cookie — no tracking). `trail`: list of `%{entity_type, entity_id, timestamp}` representing the user's exploration path. `saved_comparisons`: list of `%{entity_a, entity_b, dimensions}`. `bookmarks`: list of `%{entity_type, entity_id, note}`. Optional `user_id` for authenticated users (links to OneList account if they choose to save permanently). Queries: `by_token/1`, `recent_for_user/1`.
- [ ] Write tests for `SavedExploration` Ash resource: CRUD, validations (required: exploration_session_id, title, exploration_type, state_json). `exploration_type`: :trail, :comparison, :graph_view, :search_results. `state_json`: the full state needed to reconstruct the view (entity slugs, filter settings, dimension selections — same data that goes in shareable URLs but stored server-side for authenticated users). Queries: `for_session/1`, `for_user/1`, `recent/1`.
- [ ] Implement `ExplorationSession` and `SavedExploration` Ash resources, register in `Trueassess.Exploration` domain, write migration — GREEN.
- [ ] Implement `Trending.top_explorations/1` and `SurpriseEngine.generate/0` — GREEN.
- [ ] Implement `TrendingPanelComponent` (renders top 5-10 trending entities with name, type badge, data_richness indicator, and "why it's trending" snippet), `SurpriseCardComponent` (renders one surprise highlight with framing, counter-evidence, and "Explore This" link), `HistoryPanelComponent` (renders the current session's trail as a clickable list, with "Save Trail" and "Clear" buttons). GREEN component tests.
- [ ] Integrate into `ExploreLive`: the /explore landing page now renders TrendingPanelComponent, SurpriseCardComponent (with "Surprise Me" button that calls `SurpriseEngine.generate/0` via handle_event), and HistoryPanelComponent (populated from ExplorationSession). Update `ExploreLive` tests to verify all three panels render. Session tracking: on first mount, if no session_token in params, push a `set_session_token` event to the JS hook that stores a UUID in localStorage and sends it back. Subsequent mounts include the token. GREEN.

**Privacy Architecture:**

The ExplorationSession uses a random UUID stored in browser localStorage — not a cookie, not a server-set identifier. The server never knows who the user is unless they explicitly log in and choose to save their exploration permanently. The session_token is ephemeral — clearing localStorage clears the session. No behavioral data is ever used for recommendations. The "Trending" and "Surprise Me" features are entirely data-property-driven.

---

## Phase 7: Citation Trail + Gap Map

**Purpose:** Two complementary features. Citation Trail: click any number anywhere in the system and see the full chain back to primary source. Gap Map: visual overview of where data exists and where it doesn't across the entire knowledge web.

**Files:**
- `test/trueassess/exploration/citation_trail_test.exs`
- `test/trueassess/exploration/gap_map_test.exs`
- `test/trueassess_web/live/citation_trail_live_test.exs`
- `test/trueassess_web/live/gap_map_live_test.exs`
- `test/trueassess_web/live/components/citation_chain_component_test.exs`
- `test/trueassess_web/live/components/gap_grid_component_test.exs`
- `lib/trueassess/exploration/citation_trail.ex`
- `lib/trueassess/exploration/gap_map.ex`
- `lib/trueassess_web/live/citation_trail_live.ex`
- `lib/trueassess_web/live/gap_map_live.ex`
- `lib/trueassess_web/components/citation_chain_component.ex`
- `lib/trueassess_web/components/gap_grid_component.ex`

**Tasks (10):**

- [ ] Write tests for `CitationTrail.trace/2`: given an entity_type and entity_id (or a specific EmpiricalDatapoint ID), returns the full citation chain: `[%{level: :displayed_value, value: "69.4%", context: "Mormon happiness"}, %{level: :datapoint, source_name: "Gallup-Healthways 2012", source_url: "...", sample_size: 666000, methodology: "..."}, %{level: :primary_source, title: "Gallup-Healthways Well-Being Index", url: "...", publisher: "Gallup", year: 2012, study_type: "national_survey"}]`. The chain always terminates at the primary source. Verify: chain has at least 2 levels, every level has a non-nil source, primary source has a URL.
- [ ] Write tests for `CitationTrail.trace/2` with derived data: for values computed from multiple sources (e.g., a trendline aggregated from 5 datapoints), the chain branches: level 2 shows all contributing datapoints, each with its own primary source. Returns a tree structure, not a linear chain. Verify branching works correctly.
- [ ] Write tests for `GapMap.generate/1`: given optional filters (entity_types, metric_categories), returns a matrix `%{rows: [entity_slugs], columns: [metric_names], cells: %{entity_slug => %{metric_name => :has_data | :gap | :stale}}}`. `:has_data` = at least one EmpiricalDatapoint exists and is within recency threshold. `:gap` = no data at all. `:stale` = data exists but is older than the recency threshold (default 5 years). Verify: matrix dimensions correct, cells correctly classified, filters work.
- [ ] Write tests for `GapMap.generate/1` with confidence overlay: each `:has_data` cell also includes the confidence tier of the best-available datapoint (from ConfidenceClassification). This allows the gap map to show not just "data exists" but "data exists at what quality." Verify: confidence tiers populated for cells with data, nil for gaps.
- [ ] Write tests for `GapMap.gap_summary/0`: returns aggregate statistics: `%{total_cells: N, has_data: N, gaps: N, stale: N, coverage_percent: float, most_gapped_entities: [...], most_gapped_metrics: [...], proposed_studies_for_gaps: N}`. Verify: numbers are consistent (has_data + gaps + stale = total_cells), most_gapped lists are sorted correctly.
- [ ] Write LiveView tests for `CitationTrailLive`: `GET /explore/citation/:type/:id` renders the citation chain for that entity/datapoint. Chain renders as a vertical flow: displayed value at top, each level below with expandable details. Clicking a source URL opens in new tab. If chain branches (multiple sources), branches render as an expandable tree. Verify rendering for linear and branching chains.
- [ ] Write LiveView tests for `GapMapLive`: `GET /explore/gaps` renders the gap matrix as a colored grid. Rows = entities (scrollable), columns = metrics (scrollable). Cell colors: green = has_data + irrefutable, light green = has_data + strong_signal, yellow = has_data + hypothesis, orange = stale, red = gap. Clicking a gap cell shows: entity name, metric name, "Fund This Study" CTA linking to relevant ProposedStudy if it exists, or a "Suggest Study" CTA otherwise. Filter controls for entity_type and metric_category. Verify rendering and interaction.
- [ ] Implement `CitationTrail.trace/2` and `GapMap.generate/1` + `gap_summary/0` — GREEN.
- [ ] Implement `CitationChainComponent` (renders one citation chain as a vertical flow with expandable levels), `GapGridComponent` (renders the matrix with color-coded cells, scrollable in both axes, cell click handler). GREEN component tests.
- [ ] Implement `CitationTrailLive` and `GapMapLive` — GREEN all LiveView tests. Add routes: `live "/explore/citation/:type/:id", CitationTrailLive` and `live "/explore/gaps", GapMapLive`. Add "View Citation" links to every data value displayed in ComparatorLive, GroupExplorerLive, RiskWalkthroughLive, and CuriosityEngineLive (clicking any number routes to CitationTrailLive). Add "Gap Map" link in ExploreLive and in navigation. Verify integration.

---

## Phase 8: Study Impact Tracker

**Purpose:** Track the lifecycle of research gaps: from detection to proposed study design to funding to completed results to re-integration into the knowledge web. This makes the gap-to-knowledge pipeline visible and participatory.

**Files:**
- `test/trueassess/exploration/study_tracker_test.exs`
- `test/trueassess_web/live/study_tracker_live_test.exs`
- `test/trueassess_web/live/components/study_card_component_test.exs`
- `test/trueassess_web/live/components/study_timeline_component_test.exs`
- `lib/trueassess/exploration/study_tracker.ex`
- `lib/trueassess_web/live/study_tracker_live.ex`
- `lib/trueassess_web/components/study_card_component.ex`
- `lib/trueassess_web/components/study_timeline_component.ex`

**Tasks (10):**

- [ ] Write tests for `StudyTracker.list_studies/1`: given optional filters (status, entity_type, metric_category), returns all ProposedStudy records with enriched metadata: `%{study: %ProposedStudy{}, gap: %EvidenceGap{}, funding: %StudyFunding{} | nil, impact_preview: string, related_entities: [...]}`. `impact_preview`: a pre-computed description of what would change in the knowledge web if this study were completed (e.g., "Would fill 3 gap cells for 'vegans', upgrade 'vegan happiness' from :hypothesis to :strong_signal"). Verify: returns all studies matching filters, impact_preview is non-empty.
- [ ] Write tests for `StudyTracker.compute_impact_preview/1`: given a ProposedStudy, traces which EvidenceGaps it would fill, which SearchEntry data_richness_scores would increase, which GapMap cells would turn from red to green. Returns a structured impact report. Verify: study that fills 1 gap -> impact mentions 1 gap, study that fills 5 gaps across 3 entities -> impact mentions all.
- [ ] Write tests for `StudyTracker.lifecycle_events/1`: given a ProposedStudy ID, returns the ordered timeline of events: `[%{event: :gap_detected, date: ..., details: ...}, %{event: :study_designed, date: ..., details: ...}, %{event: :funding_received, date: ..., amount: ..., source: ...}, %{event: :study_started, date: ...}, %{event: :results_published, date: ..., source_url: ...}, %{event: :integrated, date: ..., datapoints_added: N}]`. Not all events exist for every study — most are in early stages. Verify timeline is chronologically ordered and events reflect actual state.
- [ ] Write tests for `StudyTracker.web_impact/1`: given a completed study (status = :completed), returns the concrete changes it made to the knowledge web: new EmpiricalDatapoints added, confidence tiers upgraded, gap cells filled, new ExplorationEdges created. This is the "receipt" — proof that funding this study changed something. Verify for a study that added 3 datapoints and filled 2 gaps.
- [ ] Write LiveView tests for `StudyTrackerLive` mount: `GET /explore/studies` renders three tabs: "Funded" (studies with StudyFunding), "In Progress" (studies with status :in_progress), "Completed" (studies with results integrated). Each tab shows StudyCardComponents. A summary header shows: total studies, total funded, total gaps filled, total datapoints added.
- [ ] Write LiveView tests for study card interaction: clicking a StudyCard expands it to show: the full study design (methodology, sample_size, estimated_cost), the EvidenceGap it addresses, the impact_preview, the timeline (StudyTimelineComponent), and if completed, the web_impact showing what changed. Verify expand/collapse and all sections render.
- [ ] Write LiveView tests for "Fund This Study" flow: clicking "Fund This Study" on a study card (or on a GapMap gap cell) shows: study title, estimated cost, impact preview, and a link to the funding platform (external — not built here, just linked). The link encodes the study ID and gap ID for tracking. Verify link generation.
- [ ] Implement `StudyTracker` module — `list_studies/1`, `compute_impact_preview/1`, `lifecycle_events/1`, `web_impact/1` — GREEN.
- [ ] Implement `StudyCardComponent` (renders one study with status badge, gap context, impact preview, expand/collapse), `StudyTimelineComponent` (vertical timeline of lifecycle events with icons per event type). GREEN component tests.
- [ ] Implement `StudyTrackerLive` — full LiveView with tabs, filtering, card expansion. GREEN all LiveView tests. Add route: `live "/explore/studies", StudyTrackerLive`. Add "Track This Study" links from GapMapLive (gap cells with associated ProposedStudy link to the study tracker). Verify integration.

---

## Phase 9: Export / Share System

**Purpose:** Export any view in the system as PNG/SVG image, PDF with full citations, or shareable link that reconstructs the exact view. All exports are privacy-safe (encode state, never identity).

**Files:**
- `test/trueassess/exploration/export_test.exs`
- `test/trueassess/exploration/share_link_test.exs`
- `test/trueassess_web/live/components/export_menu_component_test.exs`
- `lib/trueassess/exploration/export.ex`
- `lib/trueassess/exploration/share_link.ex`
- `lib/trueassess_web/components/export_menu_component.ex`
- `assets/js/hooks/export_hook.js`

**Tasks (10):**

- [ ] Write tests for `ShareLink.encode/2`: given a view type (:comparison, :graph, :risk_walkthrough, :group_explorer, :citation_trail, :gap_map, :study_tracker, :curiosity_trail) and the view's state (entity slugs, filter settings, dimension selections, trail), generates a URL-safe encoded string. Format: `/explore/shared/:encoded_state`. State is compressed (Base64 of zlib-compressed JSON). Verify: round-trip encode -> decode recovers original state, no PII in encoded string, URL length < 2000 chars for typical states, URL length < 8000 chars for maximum states (17 risk factors + all selections).
- [ ] Write tests for `ShareLink.decode/1`: given an encoded string, returns the original view type + state. Handles: valid encoding, corrupted encoding (returns error), encoding from older schema version (graceful degradation — ignore unknown fields). Verify error handling.
- [ ] Write tests for `Export.to_pdf/2`: given a view type and state, generates a PDF binary. PDF includes: the visualization (as rendered table/chart), full citation list, methodology notes, disclaimer, date generated, and the shareable link. Uses a PDF generation library (e.g., Chromic PDF for headless Chrome rendering or a pure-Elixir solution). Verify: PDF is non-empty, contains expected text (entity names, citations, disclaimer).
- [ ] Write tests for `Export.to_image/2`: given a view type and state, generates a PNG or SVG. For table-based views (comparison, gap map): server-side rendered SVG. For graph views: triggers client-side SVG export via JS hook (the D3 graph is client-rendered). Verify: image is non-empty, SVG contains expected elements.
- [ ] Write tests for `Export.citation_block/1`: given a view state, extracts ALL citations referenced in that view and formats them as a bibliography. Format: numbered list, each entry with: author/org, title, year, URL, accessed date. Verify: no duplicate citations, all sources from the view are included, sorted alphabetically by author.
- [ ] Implement `ShareLink.encode/2` and `ShareLink.decode/1` — GREEN. Encoding: JSON.encode -> :zlib.compress -> Base64.url_encode64. Decoding: reverse. Version field in JSON for schema evolution.
- [ ] Implement `Export.to_pdf/2`, `Export.to_image/2`, `Export.citation_block/1` — GREEN. PDF generation via Chromic PDF (renders a hidden LiveView of the export content, captures as PDF). Image generation: SVG for server-renderable views, JS hook pushEvent for client-rendered views (graph).
- [ ] Implement `ExportMenuComponent` — function component rendering a dropdown menu with options: "Copy Link" (copies shareable URL to clipboard via JS), "Download as PDF" (triggers server-side PDF generation + download), "Download as Image" (PNG for tables, SVG for graphs), "Export Citations" (downloads bibliography as .txt). GREEN component tests.
- [ ] Write `export_hook.js` — LiveView hook that handles: clipboard copy (navigator.clipboard.writeText), SVG export from D3 graph (serializes SVG element), download triggering (creates blob URL + programmatic click). Communicates with server via pushEvent for PDF/citation generation.
- [ ] Integrate `ExportMenuComponent` into ALL exploration LiveViews: ExploreLive (for search results), KnowledgeGraphLive (graph export), ComparatorLive (comparison export), CuriosityEngineLive (trail export), CitationTrailLive (citation chain export), GapMapLive (gap map export), StudyTrackerLive (study report export). Each LiveView implements `handle_event("export", %{"format" => format})` that calls the appropriate Export function. Verify integration in all LiveViews. Add route: `live "/explore/shared/:encoded", SharedViewLive` that decodes the state and redirects to the appropriate tool with the encoded state applied. GREEN.

---

## Phase 10: E2E Tests, Integration, Documentation & Convergence

**Purpose:** End-to-end tests verifying complete user flows across the entire Curiosity Engine UX, integration verification between all components, documentation, and final convergence.

**Files:**
- `test/trueassess/exploration/e2e/search_to_graph_flow_test.exs`
- `test/trueassess/exploration/e2e/search_to_comparison_flow_test.exs`
- `test/trueassess/exploration/e2e/full_exploration_flow_test.exs`
- `test/trueassess/exploration/e2e/export_share_flow_test.exs`
- `test/trueassess/exploration/e2e/gap_to_study_flow_test.exs`
- `test/trueassess/exploration/e2e/cross_tool_integration_test.exs`

**Tasks (10):**

- [ ] Write E2E test: `search_to_graph_flow_test` — Seed data -> mount ExploreLive -> search "mormons" -> select entity result -> verify routes to CuriosityEngineLive -> click "Show on Graph" -> verify routes to KnowledgeGraphLive with mormons centered -> apply filter (min_weight 0.5) -> verify graph updates -> click a neighboring node -> verify routes to CuriosityEngineLive for that entity. Full flow, no mocks.
- [ ] Write E2E test: `search_to_comparison_flow_test` — Seed data -> mount ExploreLive -> search "mormons vs atheists" -> verify intent detected as :comparison -> select comparison result -> verify routes to ComparatorLive with both pre-loaded -> verify comparison table renders with all shared dimensions -> expand a dimension -> verify confounders and counter-evidence show -> swap entities -> verify table updates -> export as shareable link -> load link -> verify same state reconstructed.
- [ ] Write E2E test: `full_exploration_flow_test` — Seed data -> mount ExploreLive -> click "Surprise Me" -> verify a highlight renders -> click "Explore This" -> verify routes to CuriosityEngineLive -> follow 3 suggestions (building a trail) -> click "Show on Graph" -> verify graph centered on current entity with trail visible -> go back to /explore -> verify "Your Recent Explorations" shows the trail -> click "Save Trail" -> verify SavedExploration created.
- [ ] Write E2E test: `export_share_flow_test` — Generate shareable links for: comparison (2 entities, 5 dimensions), graph view (filtered to entity neighborhood), curiosity trail (5-entity trail), gap map (filtered to :mental_health metrics). Verify all links < 2000 chars, decode correctly, and reconstruct the original view. Generate PDFs for comparison and gap map views. Verify PDFs contain citations and disclaimers.
- [ ] Write E2E test: `gap_to_study_flow_test` — Seed data including EvidenceGaps and ProposedStudies -> mount GapMapLive -> find a red (gap) cell -> click it -> verify gap details render with "Fund This Study" CTA -> click CTA -> verify routes to StudyTrackerLive with the relevant study highlighted -> verify study card shows impact preview -> verify timeline shows gap_detected and study_designed events.
- [ ] Write E2E test: `cross_tool_integration_test` — Verify all cross-tool navigation paths work: (a) search -> comparison, (b) search -> entity -> graph, (c) graph node click -> entity, (d) entity "Compare with..." -> comparator, (e) any value click -> citation trail, (f) any gap indicator -> gap map, (g) gap map gap -> study tracker, (h) study tracker study -> entities affected. Every path tested with seeded data.
- [ ] Write integration test: all ExportMenuComponents render correctly in all LiveViews. All export formats produce non-empty output. All shareable links round-trip. Citation blocks contain all referenced sources. CausationGate passes on ALL exported text (PDFs, citation blocks, share link preview text).
- [ ] Write documentation: Add exploration features section describing: Universal Search (how intent detection works, what you can search for), Knowledge Graph (what nodes and edges represent, how clusters are detected), Comparator (how to compare any two entities, what dimensions are available), Trending (data-driven, not engagement-driven — explain the algorithm), Surprise Me (assumption-challenging design), Gap Map (how to read it, what the colors mean), Study Tracker (the gap-to-knowledge lifecycle), Export/Share (privacy guarantees, what's encoded). Update CORRELATION_VISIBILITY_STRATEGY.md with implementation notes referencing actual modules.
- [ ] Run full test suite across all exploration modules. Verify >= 95% coverage on `lib/trueassess/exploration/` and all new LiveView files. Fix any coverage gaps. Verify no CausationGate failures in any rendered text.
- [ ] Final convergence verification: (a) Universal Search returns results for all seeded entities, (b) Knowledge Graph renders with all ExplorationEdges, clusters detected and labeled, (c) Comparator works for any entity pair in the seed data, (d) Trending returns non-empty results, (e) Surprise Me returns a highlight that passes CausationGate, (f) Citation Trail traces to primary source for all displayed values, (g) Gap Map renders with correct coverage for seeded data, (h) Study Tracker shows all ProposedStudies with impact previews, (i) Export produces valid PDF/SVG/PNG for all view types, (j) Share links round-trip for all view types, (k) All cross-tool navigation paths work, (l) No causal language in any rendered text.

---

## Convergence Criteria

This plan is converged when TWO consecutive independent clean passes confirm:

1. **Search infrastructure complete** — SearchEntry indexed, IntentDetector detects all intent types, ResultRanker produces ordered results, Postgres full-text search returns relevant matches.
2. **Universal Search LiveView works** — search-as-you-type with debounce, intent hints display, results render with type badges and richness indicators, intent-aware routing works for all paths (entity, comparison, risk, group, gap).
3. **Knowledge Graph renders correctly** — GraphSerializer produces valid JSON, GraphClusterer detects communities, D3 force-directed layout initializes and responds to zoom/pan/click, cluster coloring works, node selection shows details sidebar, search-to-graph routing works.
4. **Comparator works for any entity pair** — side-by-side comparison renders all shared dimensions, delta indicators show direction and magnitude, counter-evidence and confounders display on expand, find_comparables suggests relevant alternatives, up to 5 entities supported.
5. **Exploration Hub features functional** — Trending returns data-driven results (no user tracking), Surprise Me returns high-contrast highlights that pass CausationGate, Personal History tracks exploration sessions via localStorage token (no cookies), saved explorations persist for authenticated users.
6. **Citation Trail traces to primary source** — every displayed value in the system is traceable to its primary source in at most 3 levels, branching chains handled for aggregated values, CitationTrailLive renders the chain interactively.
7. **Gap Map visualizes coverage** — matrix renders with correct color coding (green/light green/yellow/orange/red), filtering by entity_type and metric_category works, gap cells link to ProposedStudies, gap_summary statistics are accurate.
8. **Study Tracker shows lifecycle** — all ProposedStudies listed with impact previews, timeline renders lifecycle events, completed studies show web_impact (what changed), "Fund This Study" CTAs present on gaps.
9. **Export/Share works for all views** — shareable links round-trip for all view types, PDFs contain visualizations + citations + disclaimers, images export correctly (SVG for tables, SVG/PNG for graphs), citation blocks include all referenced sources.
10. **No causal language anywhere** — CausationGate passes on: all search result snippets, all graph labels, all comparison text, all export output, all citation trail descriptions, all gap map tooltips, all study tracker descriptions.
11. **No user tracking** — verified that Trending uses data properties only, Surprise Me uses highlight scores only, no cookies set, no behavioral data collected, ExplorationSession uses localStorage UUID only.
12. **Privacy-safe sharing** — all shareable links encode view state only (entity slugs, filters, selections), never user identity or session data. URL inspection confirms no PII.
13. **Cross-tool navigation works** — all paths between search, graph, comparator, entity explorer, citation trail, gap map, and study tracker are tested and functional.
14. **Test coverage >= 95%** on all new files in `lib/trueassess/exploration/` and `lib/trueassess_web/live/` (Curiosity Engine files only).
15. **Documentation complete** — all features documented with methodology notes and privacy guarantees.
