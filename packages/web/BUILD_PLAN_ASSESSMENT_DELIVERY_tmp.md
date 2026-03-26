# BUILD PLAN: Assessment Delivery Pipeline

**Goal:** Build the complete user-facing assessment delivery pipeline — the P0 launch blocker. Without this pipeline, users cannot take assessments. The pipeline orchestrates session management, adaptive question delivery, real-time gaming detection, scoring, result persistence, therapeutic pathway generation, and five quality gates.

**Priority:** P0 — LAUNCH BLOCKER
**Stack:** Elixir / Phoenix / Ash / Oban / LiveView
**Convergence Criteria:** Two consecutive clean audit passes across all phases
**TDD Mandate:** Every task writes tests BEFORE implementation. Test file always listed first.

---

## Document Alignment

These existing documents and code artifacts contain decisions this plan must conform to:

- `/Users/user/personal/sb/trueassess/lib/trueassess/assessments.ex` — Ash domain definition; new resources must register here
- `/Users/user/personal/sb/trueassess/lib/trueassess/assessments/` — All existing pure-functional modules (DynamicSelector, GamingDetector, ScoringEngine, ConsistencyAnalyzer, CertaintyIndicator, SupersetOptimizer, QuestionBank, Question, BankImporter, QuestionGenerator, Validators) — integrate, do not rewrite
- `/Users/user/personal/sb/trueassess/lib/trueassess/assessments/resources/` — Existing Ash resources (AssessmentType, AuditResult, TherapeuticPathway, BrokenBelief, CounterBelief, SkillMapping) — extend, do not break
- `/Users/user/personal/sb/trueassess/lib/trueassess_web/router.ex` — Existing routes; new routes must not collide
- `/Users/user/personal/sb/trueassess/lib/trueassess/pipeline/chain.ex` — Worker chain graph; new workers must register
- `/Users/user/personal/sb/pp/PIPELINES_AND_GATES_GAP_ANALYSIS.md` section 2.1 — The gap analysis that defines what this pipeline must deliver
- `/Users/user/personal/sb/pp/self_assessment_app/banks/` — 54 bank JSON files defining the assessment data model
- `/Users/user/personal/sb/pp/CLAUDE.md` — Project rules: Elixir/Rust only, TDD mandatory, CruxDev convergence

---

## Existing Modules (DO NOT REWRITE — integrate these)

| Module | Location | What It Does | Status |
|--------|----------|-------------|--------|
| `DynamicSelector` | `lib/trueassess/assessments/dynamic_selector.ex` | Selects initial + followup questions by tier | Complete, pure functional |
| `GamingDetector` | `lib/trueassess/assessments/gaming_detector.ex` | Detects social desirability, all-agree, perfect profile | Complete, pure functional |
| `ScoringEngine` | `lib/trueassess/assessments/scoring_engine.ex` | Multi-axis scoring with confidence levels | Complete, pure functional |
| `ConsistencyAnalyzer` | `lib/trueassess/assessments/consistency_analyzer.ex` | Detects inconsistencies across consistency groups | Complete, pure functional |
| `CertaintyIndicator` | `lib/trueassess/assessments/certainty_indicator.ex` | Real-time certainty % (drops on gaming) | Complete, pure functional |
| `SupersetOptimizer` | `lib/trueassess/assessments/superset_optimizer.ex` | Minimizes questions across multi-assessment sessions | Complete, pure functional |
| `QuestionBank` | `lib/trueassess/assessments/question_bank.ex` | In-memory question collection with filtering | Complete, pure functional |
| `Question` | `lib/trueassess/assessments/question.ex` | Question struct with validation | Complete, pure functional |
| `BankImporter` | `lib/trueassess/assessments/bank_importer.ex` | Imports Python bank JSON into Elixir structs | Complete |
| `AssessmentType` | `lib/trueassess/assessments/resources/assessment_type.ex` | Ash resource for assessment metadata | Complete |
| `TherapeuticPathway` | `lib/trueassess/assessments/resources/therapeutic_pathway.ex` | Ash resource for pathways | Complete |
| `BrokenBelief` | `lib/trueassess/assessments/resources/broken_belief.ex` | Ash resource for broken beliefs | Complete |
| `CounterBelief` | `lib/trueassess/assessments/resources/counter_belief.ex` | Ash resource for counter-beliefs | Complete |
| `SkillMapping` | `lib/trueassess/assessments/resources/skill_mapping.ex` | Ash resource for skills | Complete |

## What Does NOT Exist (this plan builds it)

- [ ] **AssessmentSession** — Ash resource tracking a user's in-progress or completed assessment session
- [ ] **SessionResponse** — Ash resource storing individual answers within a session
- [ ] **SessionResult** — Ash resource storing computed scores and results
- [ ] **SessionGateCheck** — Ash resource recording per-session quality gate outcomes
- [ ] **AssessmentDelivery** — Orchestrator module connecting all pure-functional modules
- [ ] **Quality Gates** — Session integrity, gaming detection, score validity, result rendering, pathway completeness
- [ ] **LiveView UI** — The actual assessment-taking experience
- [ ] **API endpoints** — JSON API for headless/mobile assessment delivery

---

## PHASE 1: Ash Resources for Session State (8 tasks)

Foundation layer. Every piece of runtime state must be persisted in PostgreSQL via Ash before any orchestration logic exists.

### Task 1.1: AssessmentSession Resource

**Tests:**
- `test/trueassess/assessments/assessment_session_test.exs`

**Implementation:**
- `lib/trueassess/assessments/resources/assessment_session.ex`
- Migration: `priv/repo/migrations/XXXX_create_assessment_sessions.exs`

**Work Items:**
- [ ] Write test: create session with required fields (user_id, bank_id, tier, status)
- [ ] Write test: session status transitions (started -> in_progress -> gaming_check -> scoring -> completed / abandoned)
- [ ] Write test: session cannot be created without valid bank_id referencing AssessmentType
- [ ] Write test: read actions — by_user, by_status, active_for_user (max 1 active per bank per user)
- [ ] Write test: session metadata stored as JSONB (content_rating_filter, selected_assessments for superset)
- [ ] Write test: timestamps — started_at, completed_at, abandoned_at
- [ ] Write test: session expiry — sessions older than 24h auto-marked abandoned
- [ ] Implement AssessmentSession Ash resource passing all tests
- [ ] Write and run migration
- [ ] Register resource in `Trueassess.Assessments` domain

### Task 1.2: SessionResponse Resource

**Tests:**
- `test/trueassess/assessments/session_response_test.exs`

**Implementation:**
- `lib/trueassess/assessments/resources/session_response.ex`
- Migration: `priv/repo/migrations/XXXX_create_session_responses.exs`

**Work Items:**
- [ ] Write test: create response with required fields (session_id, question_uid, selected_option_id, raw_scores)
- [ ] Write test: response belongs_to AssessmentSession
- [ ] Write test: response stores timing data (time_to_answer_ms) for speed anomaly detection
- [ ] Write test: response stores sequence_number (order answered, not order displayed)
- [ ] Write test: prevent duplicate responses for same question_uid within a session
- [ ] Write test: read action — by_session (ordered by sequence_number)
- [ ] Write test: response immutability — no update action (answers cannot be changed)
- [ ] Implement SessionResponse Ash resource passing all tests
- [ ] Write and run migration
- [ ] Register resource in domain

### Task 1.3: SessionResult Resource

**Tests:**
- `test/trueassess/assessments/session_result_test.exs`

**Implementation:**
- `lib/trueassess/assessments/resources/session_result.ex`
- Migration: `priv/repo/migrations/XXXX_create_session_results.exs`

**Work Items:**
- [ ] Write test: create result with required fields (session_id, dimension_scores as JSONB map)
- [ ] Write test: result stores gaming_assessment as JSONB (patterns, severity, narrative)
- [ ] Write test: result stores certainty as JSONB (confidence level, percentage, target_reached)
- [ ] Write test: result stores badge_eligible boolean
- [ ] Write test: result stores compatibility_readiness as JSONB map
- [ ] Write test: result belongs_to AssessmentSession (1:1)
- [ ] Write test: result stores pathway_id (nullable — populated after pathway generation)
- [ ] Write test: result stores tier (:light, :moderate, :deep)
- [ ] Implement SessionResult Ash resource passing all tests
- [ ] Write and run migration, register in domain

### Task 1.4: SessionGateCheck Resource

**Tests:**
- `test/trueassess/assessments/session_gate_check_test.exs`

**Implementation:**
- `lib/trueassess/assessments/resources/session_gate_check.ex`
- Migration: `priv/repo/migrations/XXXX_create_session_gate_checks.exs`

**Work Items:**
- [ ] Write test: create gate check with fields (session_id, gate_name, passed, findings as JSONB)
- [ ] Write test: gate_name constrained to [:session_integrity, :gaming_detection, :score_validity, :result_rendering, :pathway_completeness]
- [ ] Write test: gate check records severity (:pass, :warn, :fail, :block)
- [ ] Write test: read actions — by_session, failed_for_session, all_passed?(session_id)
- [ ] Write test: gate checks are append-only (no updates — re-run creates new record)
- [ ] Write test: timestamps for gate execution timing
- [ ] Implement SessionGateCheck Ash resource passing all tests
- [ ] Write and run migration, register in domain

### Task 1.5: Update Assessments Domain Registration

**Tests:**
- `test/trueassess/assessments/domain_test.exs`

**Implementation:**
- `lib/trueassess/assessments.ex` (modify existing)

**Work Items:**
- [ ] Write test: all four new resources are accessible through the Assessments domain
- [ ] Write test: Ash.Resource.Info.domain/1 returns Trueassess.Assessments for each new resource
- [ ] Update `resources do` block in assessments.ex to include AssessmentSession, SessionResponse, SessionResult, SessionGateCheck
- [ ] Verify compilation with no warnings

### Task 1.6: Database Seeds for Test Assessments

**Tests:**
- `test/trueassess/assessments/seeds_test.exs`

**Implementation:**
- `lib/trueassess/assessments/seeds.ex`

**Work Items:**
- [ ] Write test: seed function imports at least 3 bank JSON files into AssessmentType records
- [ ] Write test: seed function loads questions from bank JSON into QuestionBank structs
- [ ] Write test: seed function creates TherapeuticPathway stubs for each imported bank
- [ ] Write test: seed is idempotent (running twice doesn't create duplicates)
- [ ] Write test: seed returns summary map with counts
- [ ] Implement Seeds module using BankImporter + Ash creates
- [ ] Create seed data for: attachment_style, big_five, codependency (3 representative banks)

### Task 1.7: Assessment Session Lifecycle Queries

**Tests:**
- `test/trueassess/assessments/session_queries_test.exs`

**Implementation:**
- `lib/trueassess/assessments/session_queries.ex`

**Work Items:**
- [ ] Write test: get_active_session(user_id, bank_id) returns in-progress session or nil
- [ ] Write test: get_session_with_responses(session_id) loads session + all responses
- [ ] Write test: get_session_with_result(session_id) loads session + result + gate checks
- [ ] Write test: count_responses(session_id) returns current answer count
- [ ] Write test: session_progress(session_id) returns {answered, total_expected, percentage}
- [ ] Write test: abandon_stale_sessions() marks old sessions as abandoned
- [ ] Implement SessionQueries module with Ash queries and calculations

### Task 1.8: Schema Validation & Integrity Constraints

**Tests:**
- `test/trueassess/assessments/schema_integrity_test.exs`

**Implementation:**
- Update migrations with database-level constraints

**Work Items:**
- [ ] Write test: session cannot reference non-existent user_id (FK constraint)
- [ ] Write test: response cannot reference non-existent session_id (FK constraint)
- [ ] Write test: result cannot reference non-existent session_id (FK constraint)
- [ ] Write test: unique constraint on (session_id, question_uid) in responses
- [ ] Write test: unique constraint on session_id in results (1:1)
- [ ] Write test: check constraint on session status values
- [ ] Write test: check constraint on gate_name values
- [ ] Add database-level constraints to migrations

---

## PHASE 2: Assessment Delivery Orchestrator (9 tasks)

The brain. This module connects all pure-functional modules into a stateful pipeline. It is the ONLY module that coordinates DynamicSelector, GamingDetector, ScoringEngine, ConsistencyAnalyzer, CertaintyIndicator, and SupersetOptimizer.

### Task 2.1: Session Initialization

**Tests:**
- `test/trueassess/assessments/delivery/session_init_test.exs`

**Implementation:**
- `lib/trueassess/assessments/delivery.ex`

**Work Items:**
- [ ] Write test: start_session(user_id, bank_id, tier) creates AssessmentSession + returns initial questions
- [ ] Write test: start_session loads bank JSON via BankImporter, creates QuestionBank in memory
- [ ] Write test: start_session calls DynamicSelector.select_initial(bank, tier) for question list
- [ ] Write test: start_session with content_rating_filter applies QuestionBank.filter_safe_for_user
- [ ] Write test: start_session rejects if user already has active session for this bank
- [ ] Write test: start_session rejects if AssessmentType.gate_status is :blocked
- [ ] Write test: start_session stores question_order (UIDs in delivery sequence) in session metadata
- [ ] Implement Delivery.start_session/3 and Delivery.start_session/4 (with opts)
- [ ] Write test: start_superset_session(user_id, bank_ids, tier) uses SupersetOptimizer
- [ ] Implement Delivery.start_superset_session/3

### Task 2.2: Answer Submission

**Tests:**
- `test/trueassess/assessments/delivery/answer_submission_test.exs`

**Implementation:**
- `lib/trueassess/assessments/delivery.ex` (extend)

**Work Items:**
- [ ] Write test: submit_answer(session_id, question_uid, option_id, timing_ms) creates SessionResponse
- [ ] Write test: submit_answer validates question_uid is in the session's question list
- [ ] Write test: submit_answer validates option_id is valid for the question
- [ ] Write test: submit_answer rejects if question already answered
- [ ] Write test: submit_answer rejects if session status is not :in_progress
- [ ] Write test: submit_answer computes raw_scores from question.options scoring matrix
- [ ] Write test: submit_answer increments sequence_number correctly
- [ ] Write test: submit_answer returns updated certainty (calls CertaintyIndicator.compute)
- [ ] Implement Delivery.submit_answer/4
- [ ] Write test: submit_answer returns next_question or :assessment_complete

### Task 2.3: Adaptive Question Selection (Mid-Session)

**Tests:**
- `test/trueassess/assessments/delivery/adaptive_selection_test.exs`

**Implementation:**
- `lib/trueassess/assessments/delivery.ex` (extend)

**Work Items:**
- [ ] Write test: after N answers, run ConsistencyAnalyzer on current responses
- [ ] Write test: if inconsistencies found, call DynamicSelector.select_followup for additional questions
- [ ] Write test: followup questions are appended to session's question list
- [ ] Write test: after gaming detection triggers, additional trap questions injected
- [ ] Write test: question injection is transparent to user (no visible "we caught you" signal)
- [ ] Write test: adaptive selection respects content_rating_filter
- [ ] Write test: maximum question cap prevents infinite injection (e.g., 2x initial count)
- [ ] Implement Delivery.check_and_adapt/1 (called internally after each submit_answer)

### Task 2.4: Real-Time Certainty Updates

**Tests:**
- `test/trueassess/assessments/delivery/certainty_test.exs`

**Implementation:**
- `lib/trueassess/assessments/delivery.ex` (extend)

**Work Items:**
- [ ] Write test: get_certainty(session_id) computes live certainty from current responses
- [ ] Write test: certainty drops when gaming_detected flips to true
- [ ] Write test: certainty reflects inconsistency count from ConsistencyAnalyzer
- [ ] Write test: certainty uses logarithmic growth (matches CertaintyIndicator formula)
- [ ] Write test: certainty result includes confidence label (:hypothesis/:strong_signal/:irrefutable)
- [ ] Write test: certainty result includes target_reached boolean
- [ ] Implement Delivery.get_certainty/1

### Task 2.5: Gaming Detection Integration

**Tests:**
- `test/trueassess/assessments/delivery/gaming_integration_test.exs`

**Implementation:**
- `lib/trueassess/assessments/delivery.ex` (extend)

**Work Items:**
- [ ] Write test: run_gaming_check(session_id) calls GamingDetector.detect with formatted responses
- [ ] Write test: gaming check formats SessionResponse records into GamingDetector.response() type
- [ ] Write test: gaming check includes timing data for speed anomaly detection
- [ ] Write test: gaming_detected: true triggers session status change to :gaming_check
- [ ] Write test: gaming severity :high blocks scoring without human review
- [ ] Write test: gaming severity :low/:moderate adds warning to results but allows scoring
- [ ] Write test: gaming check is idempotent (running twice returns same result for same data)
- [ ] Implement Delivery.run_gaming_check/1

### Task 2.6: Scoring Integration

**Tests:**
- `test/trueassess/assessments/delivery/scoring_integration_test.exs`

**Implementation:**
- `lib/trueassess/assessments/delivery.ex` (extend)

**Work Items:**
- [ ] Write test: compute_scores(session_id) calls ScoringEngine.score with formatted responses
- [ ] Write test: scoring formats SessionResponse records into ScoringEngine.response() type
- [ ] Write test: scoring creates SessionResult with dimension_scores, gaming_assessment, certainty
- [ ] Write test: scoring stores badge_eligible and compatibility_readiness
- [ ] Write test: scoring rejects if session status is not :in_progress or :gaming_check
- [ ] Write test: scoring transitions session status to :scoring then :completed
- [ ] Write test: scoring with gaming severity :high returns {:error, :gaming_blocked}
- [ ] Implement Delivery.compute_scores/1

### Task 2.7: Pathway Linkage

**Tests:**
- `test/trueassess/assessments/delivery/pathway_linkage_test.exs`

**Implementation:**
- `lib/trueassess/assessments/delivery.ex` (extend)
- `lib/trueassess/assessments/pathway_matcher.ex`

**Work Items:**
- [ ] Write test: link_pathway(session_id) finds TherapeuticPathway for the session's bank_id
- [ ] Write test: link_pathway evaluates dysfunction_threshold against session scores
- [ ] Write test: link_pathway returns relevant broken_beliefs based on score thresholds
- [ ] Write test: link_pathway returns counter_beliefs for each triggered broken_belief
- [ ] Write test: link_pathway returns skill_mappings for triggered beliefs
- [ ] Write test: link_pathway stores pathway_id on SessionResult
- [ ] Write test: link_pathway handles no-pathway case gracefully (not all assessments have pathways)
- [ ] Write test: link_pathway handles crisis_flag (scores exceeding crisis_threshold return crisis data)
- [ ] Implement PathwayMatcher module
- [ ] Implement Delivery.link_pathway/1

### Task 2.8: Full Session Orchestration (End-to-End)

**Tests:**
- `test/trueassess/assessments/delivery/full_session_test.exs`

**Implementation:**
- `lib/trueassess/assessments/delivery.ex` (extend)

**Work Items:**
- [ ] Write test: complete happy path — start -> answer all -> score -> link pathway -> result
- [ ] Write test: complete path with gaming detection — start -> answer -> gaming flagged -> extra questions -> score
- [ ] Write test: complete path with inconsistency — start -> answer -> inconsistency -> followup -> score
- [ ] Write test: abandoned path — start -> some answers -> abandon -> session marked abandoned
- [ ] Write test: superset path — start multi-assessment -> optimized questions -> per-assessment scores
- [ ] Write test: session resume — start -> answer some -> resume later -> continue from last answer
- [ ] Write test: session state is fully reconstructable from database (no in-memory-only state)
- [ ] Implement Delivery.abandon_session/1 and Delivery.resume_session/1

### Task 2.9: Delivery Context (In-Memory Session Cache)

**Tests:**
- `test/trueassess/assessments/delivery/context_test.exs`

**Implementation:**
- `lib/trueassess/assessments/delivery/context.ex`

**Work Items:**
- [ ] Write test: DeliveryContext struct holds session_id, question_bank, question_order, current_index
- [ ] Write test: build_context(session_id) loads from DB and reconstructs full state
- [ ] Write test: context is rebuildable from DB state alone (crash recovery)
- [ ] Write test: context caches QuestionBank to avoid re-parsing JSON per answer
- [ ] Write test: context tracks which questions have been answered without DB round-trip
- [ ] Write test: context is invalidated when adaptive selection adds new questions
- [ ] Implement DeliveryContext struct and build/rebuild functions

---

## PHASE 3: Quality Gates (7 tasks)

Five gates that MUST pass before results are shown to a user. Each gate is independently testable and produces a SessionGateCheck record.

### Task 3.1: Session Integrity Gate

**Tests:**
- `test/trueassess/assessments/gates/session_integrity_test.exs`

**Implementation:**
- `lib/trueassess/assessments/gates/session_integrity.ex`

**Work Items:**
- [ ] Write test: passes when all questions answered in sequence with valid option IDs
- [ ] Write test: fails when response count doesn't match expected question count
- [ ] Write test: fails when any response has an invalid option_id for its question
- [ ] Write test: fails when duplicate question_uids found in responses
- [ ] Write test: warns when timing anomalies detected (all answers < 2 seconds)
- [ ] Write test: fails when session was tampered (response created outside delivery flow)
- [ ] Write test: records SessionGateCheck with findings
- [ ] Implement SessionIntegrity gate module

### Task 3.2: Gaming Detection Gate

**Tests:**
- `test/trueassess/assessments/gates/gaming_detection_test.exs`

**Implementation:**
- `lib/trueassess/assessments/gates/gaming_detection.ex`

**Work Items:**
- [ ] Write test: passes when gaming_severity is :none
- [ ] Write test: warns when gaming_severity is :low
- [ ] Write test: warns when gaming_severity is :moderate (results shown with caveat)
- [ ] Write test: blocks when gaming_severity is :high (results NOT shown)
- [ ] Write test: gate uses GamingDetector result already stored in SessionResult
- [ ] Write test: gate narrative included in findings
- [ ] Write test: records SessionGateCheck with severity and patterns list
- [ ] Implement GamingDetection gate module

### Task 3.3: Score Validity Gate

**Tests:**
- `test/trueassess/assessments/gates/score_validity_test.exs`

**Implementation:**
- `lib/trueassess/assessments/gates/score_validity.ex`

**Work Items:**
- [ ] Write test: passes when all dimension scores within expected range for the bank's axes
- [ ] Write test: fails when any dimension score is outside axis range (e.g., score 15 on [-10, 10] axis)
- [ ] Write test: warns when all dimensions cluster at extremes (suggests low discrimination)
- [ ] Write test: fails when dimension count in result doesn't match bank's axis count
- [ ] Write test: warns when confidence is :hypothesis on critical assessments
- [ ] Write test: passes with partial dimensions when superset session (some assessments may not reach all dims)
- [ ] Write test: records SessionGateCheck with per-dimension validity
- [ ] Implement ScoreValidity gate module

### Task 3.4: Result Rendering Gate

**Tests:**
- `test/trueassess/assessments/gates/result_rendering_test.exs`

**Implementation:**
- `lib/trueassess/assessments/gates/result_rendering.ex`

**Work Items:**
- [ ] Write test: passes when all dimension_scores have numeric values (no nil, no NaN)
- [ ] Write test: fails when any dimension label is missing from bank axes definition
- [ ] Write test: fails when gaming_assessment field is nil (must always be populated)
- [ ] Write test: fails when certainty field is nil
- [ ] Write test: warns when percentile data is all nil (population data not yet available)
- [ ] Write test: passes when all required fields for chart rendering are present
- [ ] Write test: records SessionGateCheck with list of missing/broken fields
- [ ] Implement ResultRendering gate module

### Task 3.5: Pathway Completeness Gate

**Tests:**
- `test/trueassess/assessments/gates/pathway_completeness_test.exs`

**Implementation:**
- `lib/trueassess/assessments/gates/pathway_completeness.ex`

**Work Items:**
- [ ] Write test: passes when pathway_id is set and TherapeuticPathway exists with status :complete
- [ ] Write test: warns when pathway exists but status is :incomplete
- [ ] Write test: passes with :no_pathway_needed when assessment is entertainment/taste category
- [ ] Write test: fails when dysfunction detected but no pathway linked
- [ ] Write test: warns when pathway has zero broken_beliefs
- [ ] Write test: warns when broken_beliefs exist but zero counter_beliefs linked
- [ ] Write test: records SessionGateCheck with pathway coverage metrics
- [ ] Implement PathwayCompleteness gate module

### Task 3.6: Gate Runner (Orchestrates All Gates)

**Tests:**
- `test/trueassess/assessments/gates/gate_runner_test.exs`

**Implementation:**
- `lib/trueassess/assessments/gates/gate_runner.ex`

**Work Items:**
- [ ] Write test: run_all_gates(session_id) executes all 5 gates in order
- [ ] Write test: returns aggregate result (:all_passed, :passed_with_warnings, :blocked)
- [ ] Write test: short-circuits on :block severity (skips remaining gates)
- [ ] Write test: collects all warnings even when some gates pass
- [ ] Write test: stores all gate check results to DB
- [ ] Write test: idempotent — running twice produces same result, creates new gate check records
- [ ] Write test: returns structured summary with per-gate results
- [ ] Implement GateRunner module

### Task 3.7: Gate Integration with Delivery

**Tests:**
- `test/trueassess/assessments/delivery/gate_integration_test.exs`

**Implementation:**
- `lib/trueassess/assessments/delivery.ex` (extend)

**Work Items:**
- [ ] Write test: compute_scores automatically triggers gate_runner after scoring
- [ ] Write test: if gates blocked, session status set to :gate_blocked instead of :completed
- [ ] Write test: if gates passed_with_warnings, session completes but warnings stored
- [ ] Write test: get_results(session_id) returns nil if gates haven't passed
- [ ] Write test: get_results(session_id) returns full result with gate summary when passed
- [ ] Write test: blocked sessions can be manually reviewed and unblocked
- [ ] Implement gate integration in Delivery.compute_scores and Delivery.get_results

---

## PHASE 4: LiveView Assessment UI (10 tasks)

The user-facing experience. A Phoenix LiveView that guides users through assessment selection, question answering, and result viewing.

### Task 4.1: Assessment Catalog LiveView

**Tests:**
- `test/trueassess_web/live/assessment_catalog_live_test.exs`

**Implementation:**
- `lib/trueassess_web/live/assessment_catalog_live.ex`
- Update `lib/trueassess_web/router.ex`

**Work Items:**
- [ ] Write test: renders list of available assessments from AssessmentType (gate_status: :open)
- [ ] Write test: displays bank_name, category, framework_source, estimated time
- [ ] Write test: filters by category
- [ ] Write test: shows tier selector (Light / Moderate / Deep) with explanation
- [ ] Write test: "Start Assessment" button navigates to session LiveView
- [ ] Write test: shows "In Progress" badge if user has active session
- [ ] Write test: hides age-gated assessments for non-verified users
- [ ] Implement AssessmentCatalogLive
- [ ] Add route: `live "/assessments", AssessmentCatalogLive`
- [ ] Add route: `live "/assessments/:bank_id", AssessmentSessionLive`

### Task 4.2: Assessment Session LiveView — Shell

**Tests:**
- `test/trueassess_web/live/assessment_session_live_test.exs`

**Implementation:**
- `lib/trueassess_web/live/assessment_session_live.ex`

**Work Items:**
- [ ] Write test: mount initializes session via Delivery.start_session or Delivery.resume_session
- [ ] Write test: renders first question with options
- [ ] Write test: displays certainty indicator bar
- [ ] Write test: displays progress bar (answered / total)
- [ ] Write test: handles session not found gracefully (redirect to catalog)
- [ ] Write test: handles bank not available (gate_status: :blocked) gracefully
- [ ] Implement AssessmentSessionLive mount and initial render

### Task 4.3: Question Rendering Component

**Tests:**
- `test/trueassess_web/live/components/question_component_test.exs`

**Implementation:**
- `lib/trueassess_web/live/components/question_component.ex`

**Work Items:**
- [ ] Write test: renders scenario question with radio options
- [ ] Write test: renders forced_choice question with button options
- [ ] Write test: renders intensity_scale question with slider
- [ ] Write test: renders behavioral_recall question with text area + options
- [ ] Write test: renders ranked_preference with drag-and-drop ordering
- [ ] Write test: highlights selected option
- [ ] Write test: disables interaction after answer submitted
- [ ] Write test: shows question text without revealing dimension (opacity)
- [ ] Implement QuestionComponent with all question type renderers

### Task 4.4: Answer Submission Flow

**Tests:**
- `test/trueassess_web/live/assessment_session_answer_test.exs`

**Implementation:**
- `lib/trueassess_web/live/assessment_session_live.ex` (extend)

**Work Items:**
- [ ] Write test: selecting option and clicking "Next" calls Delivery.submit_answer
- [ ] Write test: after submit, next question renders with transition
- [ ] Write test: certainty bar updates after each answer
- [ ] Write test: progress bar updates after each answer
- [ ] Write test: timing tracked (time between question display and answer submit)
- [ ] Write test: "Previous" button is NOT available (no going back — integrity gate)
- [ ] Write test: network error during submit shows retry option
- [ ] Implement handle_event("submit_answer", ...) and question progression

### Task 4.5: Certainty Indicator Component

**Tests:**
- `test/trueassess_web/live/components/certainty_indicator_test.exs`

**Implementation:**
- `lib/trueassess_web/live/components/certainty_indicator.ex`

**Work Items:**
- [ ] Write test: renders percentage as animated bar
- [ ] Write test: color changes by confidence level (red/yellow/green)
- [ ] Write test: shows label (Hypothesis / Strong Signal / Irrefutable)
- [ ] Write test: bar drops visibly when gaming detected (key UX feature)
- [ ] Write test: tooltip explains what certainty means
- [ ] Write test: updates in real-time via LiveView assigns
- [ ] Implement CertaintyIndicator component with Tailwind styling

### Task 4.6: Assessment Completion & Scoring Trigger

**Tests:**
- `test/trueassess_web/live/assessment_session_complete_test.exs`

**Implementation:**
- `lib/trueassess_web/live/assessment_session_live.ex` (extend)

**Work Items:**
- [ ] Write test: after last question, show "Computing your results..." loading state
- [ ] Write test: triggers Delivery.compute_scores asynchronously
- [ ] Write test: on scoring complete, redirects to results page
- [ ] Write test: on gate blocked, shows explanation and next steps
- [ ] Write test: on gaming blocked, shows "results may not be accurate" explanation
- [ ] Write test: handles scoring timeout gracefully
- [ ] Implement completion flow with async scoring

### Task 4.7: Results Display LiveView

**Tests:**
- `test/trueassess_web/live/assessment_results_live_test.exs`

**Implementation:**
- `lib/trueassess_web/live/assessment_results_live.ex`
- Update `lib/trueassess_web/router.ex`

**Work Items:**
- [ ] Write test: renders dimension scores as chart data (JSON for JS charting)
- [ ] Write test: renders confidence level per dimension
- [ ] Write test: renders gaming assessment narrative (if any patterns detected)
- [ ] Write test: renders badge eligibility status
- [ ] Write test: renders compatibility readiness per dimension
- [ ] Write test: shows gate check summary (all passed / warnings)
- [ ] Write test: renders tier label
- [ ] Write test: "View Growth Path" button links to pathway page
- [ ] Implement AssessmentResultsLive
- [ ] Add route: `live "/assessments/:bank_id/results/:session_id", AssessmentResultsLive`

### Task 4.8: Therapeutic Pathway Display

**Tests:**
- `test/trueassess_web/live/pathway_live_test.exs`

**Implementation:**
- `lib/trueassess_web/live/pathway_live.ex`
- Update `lib/trueassess_web/router.ex`

**Work Items:**
- [ ] Write test: renders dysfunction description
- [ ] Write test: renders broken beliefs with origin and pattern_it_drives
- [ ] Write test: renders counter-beliefs with evidence and citations
- [ ] Write test: renders skill mappings with difficulty and micro-practices
- [ ] Write test: renders crisis resources if crisis_flag triggered
- [ ] Write test: links to knowledge_web pages
- [ ] Write test: handles pathway not found gracefully
- [ ] Implement PathwayLive
- [ ] Add route: `live "/pathway/:pathway_id", PathwayLive`
- [ ] Add route: `live "/assessments/:bank_id/results/:session_id/pathway", PathwayLive` (contextual)

### Task 4.9: Session Management (Abandon / Resume)

**Tests:**
- `test/trueassess_web/live/assessment_session_management_test.exs`

**Implementation:**
- `lib/trueassess_web/live/assessment_session_live.ex` (extend)

**Work Items:**
- [ ] Write test: "Save & Exit" button calls Delivery.abandon_session (preserves progress)
- [ ] Write test: returning to assessment with active session triggers resume flow
- [ ] Write test: resume shows "Continue where you left off?" confirmation
- [ ] Write test: resume restores question_order and advances to next unanswered question
- [ ] Write test: "Start Over" option abandons old session and creates new one
- [ ] Write test: session expiry warning shown when session is > 20 hours old
- [ ] Implement session management UI flows

### Task 4.10: Mobile-Responsive Layout

**Tests:**
- `test/trueassess_web/live/assessment_responsive_test.exs`

**Implementation:**
- `lib/trueassess_web/live/components/assessment_layout.ex`
- CSS/Tailwind in `assets/css/`

**Work Items:**
- [ ] Write test: question component renders correctly at mobile viewport (< 640px)
- [ ] Write test: certainty indicator stacks below question on mobile
- [ ] Write test: option buttons are full-width on mobile
- [ ] Write test: results chart is scrollable on mobile
- [ ] Write test: pathway display is readable on mobile
- [ ] Implement responsive Tailwind classes for all assessment components

---

## PHASE 5: JSON API Layer (6 tasks)

For headless clients, mobile apps, and third-party integrations. Mirrors the LiveView functionality as a REST API.

### Task 5.1: API Authentication Plug

**Tests:**
- `test/trueassess_web/plugs/api_auth_test.exs`

**Implementation:**
- `lib/trueassess_web/plugs/api_auth.ex`
- Update `lib/trueassess_web/router.ex`

**Work Items:**
- [ ] Write test: requests without token return 401
- [ ] Write test: requests with valid Bearer token pass through with user_id in conn.assigns
- [ ] Write test: requests with expired token return 401
- [ ] Write test: requests with malformed token return 401
- [ ] Write test: token validation is pluggable (initially simple token, later JWT/OneList)
- [ ] Implement ApiAuth plug
- [ ] Add API pipeline to router with ApiAuth plug

### Task 5.2: Session API Controller

**Tests:**
- `test/trueassess_web/controllers/api/session_controller_test.exs`

**Implementation:**
- `lib/trueassess_web/controllers/api/session_controller.ex`
- `lib/trueassess_web/controllers/api/session_json.ex`

**Work Items:**
- [ ] Write test: POST /api/assessments/:bank_id/sessions starts session, returns session_id + first questions
- [ ] Write test: GET /api/assessments/sessions/:id returns session state + current question
- [ ] Write test: POST /api/assessments/sessions/:id/answers submits answer, returns next question + certainty
- [ ] Write test: DELETE /api/assessments/sessions/:id abandons session
- [ ] Write test: POST /api/assessments/sessions/:id/complete triggers scoring
- [ ] Write test: all endpoints require authentication
- [ ] Write test: rate limiting — max 10 answer submissions per minute
- [ ] Implement SessionController and JSON view
- [ ] Add API routes to router
- [ ] Write OpenAPI spec documentation

### Task 5.3: Results API Controller

**Tests:**
- `test/trueassess_web/controllers/api/results_controller_test.exs`

**Implementation:**
- `lib/trueassess_web/controllers/api/results_controller.ex`
- `lib/trueassess_web/controllers/api/results_json.ex`

**Work Items:**
- [ ] Write test: GET /api/assessments/sessions/:id/results returns full result with scores
- [ ] Write test: returns 404 if session not completed
- [ ] Write test: returns 403 if gates blocked
- [ ] Write test: includes gate_checks summary in response
- [ ] Write test: includes pathway data if linked
- [ ] Write test: results only accessible by session owner
- [ ] Implement ResultsController and JSON view
- [ ] Add API routes

### Task 5.4: Catalog API Controller

**Tests:**
- `test/trueassess_web/controllers/api/catalog_controller_test.exs`

**Implementation:**
- `lib/trueassess_web/controllers/api/catalog_controller.ex`
- `lib/trueassess_web/controllers/api/catalog_json.ex`

**Work Items:**
- [ ] Write test: GET /api/assessments returns list of available assessments
- [ ] Write test: filters by category query param
- [ ] Write test: includes estimated_time, axis_count, content_tier per assessment
- [ ] Write test: excludes blocked assessments
- [ ] Write test: GET /api/assessments/:bank_id returns single assessment detail with axes
- [ ] Implement CatalogController and JSON view
- [ ] Add API routes

### Task 5.5: API Error Handling & Rate Limiting

**Tests:**
- `test/trueassess_web/plugs/rate_limiter_test.exs`

**Implementation:**
- `lib/trueassess_web/plugs/rate_limiter.ex`
- `lib/trueassess_web/controllers/api/fallback_controller.ex`

**Work Items:**
- [ ] Write test: rate limiter returns 429 after exceeding limit
- [ ] Write test: rate limiter tracks per-user, not per-IP
- [ ] Write test: fallback controller renders proper JSON errors for all Ash error types
- [ ] Write test: fallback handles {:error, :not_found}, {:error, :unauthorized}, {:error, changeset}
- [ ] Write test: all API errors include machine-readable error code
- [ ] Implement RateLimiter plug (ETS-based initially)
- [ ] Implement FallbackController

### Task 5.6: API Integration Tests

**Tests:**
- `test/trueassess_web/controllers/api/full_flow_test.exs`

**Implementation:**
- No new production code — integration tests only

**Work Items:**
- [ ] Write test: full API flow — create session -> submit all answers -> get results
- [ ] Write test: full API flow with gaming detection triggered
- [ ] Write test: full API flow with superset (multiple assessments)
- [ ] Write test: concurrent sessions for same user (different assessments)
- [ ] Write test: session resume via API after connection drop
- [ ] Write test: results include pathway data
- [ ] Write test: error responses are consistent and machine-parseable

---

## PHASE 6: Oban Workers & Background Processing (5 tasks)

Assessment scoring and pathway generation can be computationally expensive for large banks. Offload to Oban workers for reliability and retry semantics.

### Task 6.1: Score Assessment Worker

**Tests:**
- `test/trueassess/workers/score_assessment_test.exs`

**Implementation:**
- `lib/trueassess/workers/score_assessment.ex`

**Work Items:**
- [ ] Write test: worker takes session_id, calls Delivery.compute_scores
- [ ] Write test: worker runs gate checks after scoring
- [ ] Write test: worker updates session status based on gate results
- [ ] Write test: worker retries on transient failure (max 3 attempts)
- [ ] Write test: worker is idempotent (re-running on completed session is no-op)
- [ ] Write test: worker broadcasts completion via PubSub (for LiveView update)
- [ ] Implement ScoreAssessment Oban worker

### Task 6.2: Generate Pathway Worker

**Tests:**
- `test/trueassess/workers/generate_pathway_test.exs`

**Implementation:**
- `lib/trueassess/workers/generate_pathway.ex`

**Work Items:**
- [ ] Write test: worker takes session_id, calls Delivery.link_pathway
- [ ] Write test: worker creates TherapeuticPathway if none exists for bank (stub/template)
- [ ] Write test: worker is triggered after scoring completes successfully
- [ ] Write test: worker handles missing pathway gracefully (marks gate as :no_pathway_needed)
- [ ] Write test: worker broadcasts pathway completion via PubSub
- [ ] Implement GeneratePathway Oban worker

### Task 6.3: Session Cleanup Worker

**Tests:**
- `test/trueassess/workers/cleanup_sessions_test.exs`

**Implementation:**
- `lib/trueassess/workers/cleanup_sessions.ex`

**Work Items:**
- [ ] Write test: worker finds sessions older than 24h with status :in_progress
- [ ] Write test: worker marks stale sessions as :abandoned
- [ ] Write test: worker runs as periodic Oban cron job
- [ ] Write test: worker logs count of abandoned sessions
- [ ] Write test: worker does not touch :completed or already :abandoned sessions
- [ ] Implement CleanupSessions Oban worker with cron schedule

### Task 6.4: Assessment Analytics Worker

**Tests:**
- `test/trueassess/workers/assessment_analytics_test.exs`

**Implementation:**
- `lib/trueassess/workers/assessment_analytics.ex`

**Work Items:**
- [ ] Write test: worker computes per-bank stats (completion rate, avg time, avg certainty)
- [ ] Write test: worker computes gaming detection rate per bank
- [ ] Write test: worker computes score distribution per dimension (for percentile calculation)
- [ ] Write test: worker stores analytics in ETS or dedicated Ash resource
- [ ] Write test: worker runs as periodic Oban cron job (hourly)
- [ ] Implement AssessmentAnalytics Oban worker

### Task 6.5: Chain Integration

**Tests:**
- `test/trueassess/pipeline/assessment_chain_test.exs`

**Implementation:**
- `lib/trueassess/pipeline/chain.ex` (modify)

**Work Items:**
- [ ] Write test: ScoreAssessment triggers GeneratePathway on success
- [ ] Write test: chain blocks GeneratePathway if ScoreAssessment fails
- [ ] Write test: chain registered in Pipeline.Chain @chains map
- [ ] Write test: chain registered in Pipeline.ChainState (kept in sync)
- [ ] Update Chain and ChainState with assessment worker chain

---

## PHASE 7: End-to-End Integration & Hardening (5 tasks)

Full-stack integration tests, error recovery, and performance validation.

### Task 7.1: E2E Happy Path Tests

**Tests:**
- `test/trueassess/assessments/e2e/happy_path_test.exs`

**Implementation:**
- No new production code

**Work Items:**
- [ ] Write test: seed banks -> start session via LiveView -> answer all questions -> view results -> view pathway
- [ ] Write test: same flow via API
- [ ] Write test: superset session — select 3 assessments -> answer optimized set -> 3 separate result sets
- [ ] Write test: deep tier with full anti-gaming (traps, consistency checks, followup injection)
- [ ] Write test: light tier — minimal questions, quick completion
- [ ] Write test: session with content_rating_filter (age-gated assessment, verified user)

### Task 7.2: Error Recovery Tests

**Tests:**
- `test/trueassess/assessments/e2e/error_recovery_test.exs`

**Implementation:**
- No new production code (unless bugs found)

**Work Items:**
- [ ] Write test: crash during scoring — session recoverable, Oban retries
- [ ] Write test: crash during gateway check — re-run produces same result
- [ ] Write test: database connection lost during answer submit — retry succeeds
- [ ] Write test: browser refresh during assessment — LiveView reconnects, resumes correctly
- [ ] Write test: concurrent answer submissions (race condition) — only first accepted
- [ ] Write test: stale session cleanup doesn't affect in-progress active sessions

### Task 7.3: Security Hardening

**Tests:**
- `test/trueassess/assessments/e2e/security_test.exs`

**Implementation:**
- May require updates to Delivery module

**Work Items:**
- [ ] Write test: user A cannot access user B's session
- [ ] Write test: user cannot submit answers to another user's session
- [ ] Write test: user cannot view results of another user's session
- [ ] Write test: API token scoping — token for user A rejected for user B's resources
- [ ] Write test: session_id is UUID (not sequential — prevents enumeration)
- [ ] Write test: answer submission rate limiting prevents automated flooding
- [ ] Write test: question_uids in responses are validated against session's question list (prevent injection)

### Task 7.4: Performance Baseline

**Tests:**
- `test/trueassess/assessments/e2e/performance_test.exs`

**Implementation:**
- No new production code (unless bottlenecks found)

**Work Items:**
- [ ] Write test: session start < 200ms including bank load
- [ ] Write test: answer submission < 100ms including DB write + certainty recalc
- [ ] Write test: scoring < 500ms for 50-question session
- [ ] Write test: gateway checks < 200ms total for all 5 gates
- [ ] Write test: results page load < 300ms including pathway data
- [ ] Write test: 10 concurrent sessions don't degrade response times >2x

### Task 7.5: Monitoring & Observability

**Tests:**
- `test/trueassess/assessments/telemetry_test.exs`

**Implementation:**
- `lib/trueassess/assessments/telemetry.ex`

**Work Items:**
- [ ] Write test: session_started telemetry event emitted with bank_id, tier
- [ ] Write test: answer_submitted telemetry event emitted with timing_ms
- [ ] Write test: scoring_completed telemetry event emitted with duration_ms, dimension_count
- [ ] Write test: gate_checked telemetry event emitted per gate with result
- [ ] Write test: gaming_detected telemetry event emitted with severity and patterns
- [ ] Implement Telemetry module with :telemetry.execute calls
- [ ] Add telemetry event handlers to TrueassessWeb.Telemetry for LiveDashboard

---

## File Inventory

### New Files (Implementation)

| File | Phase | Purpose |
|------|-------|---------|
| `lib/trueassess/assessments/resources/assessment_session.ex` | 1 | Session Ash resource |
| `lib/trueassess/assessments/resources/session_response.ex` | 1 | Response Ash resource |
| `lib/trueassess/assessments/resources/session_result.ex` | 1 | Result Ash resource |
| `lib/trueassess/assessments/resources/session_gate_check.ex` | 1 | Gate check Ash resource |
| `lib/trueassess/assessments/seeds.ex` | 1 | Test data seeding |
| `lib/trueassess/assessments/session_queries.ex` | 1 | Session query helpers |
| `lib/trueassess/assessments/delivery.ex` | 2 | Main orchestrator |
| `lib/trueassess/assessments/delivery/context.ex` | 2 | In-memory session context |
| `lib/trueassess/assessments/pathway_matcher.ex` | 2 | Score -> pathway linkage |
| `lib/trueassess/assessments/gates/session_integrity.ex` | 3 | Gate: session integrity |
| `lib/trueassess/assessments/gates/gaming_detection.ex` | 3 | Gate: gaming detection |
| `lib/trueassess/assessments/gates/score_validity.ex` | 3 | Gate: score validity |
| `lib/trueassess/assessments/gates/result_rendering.ex` | 3 | Gate: result rendering |
| `lib/trueassess/assessments/gates/pathway_completeness.ex` | 3 | Gate: pathway completeness |
| `lib/trueassess/assessments/gates/gate_runner.ex` | 3 | Gate orchestrator |
| `lib/trueassess_web/live/assessment_catalog_live.ex` | 4 | Assessment browser UI |
| `lib/trueassess_web/live/assessment_session_live.ex` | 4 | Assessment taking UI |
| `lib/trueassess_web/live/assessment_results_live.ex` | 4 | Results display UI |
| `lib/trueassess_web/live/pathway_live.ex` | 4 | Therapeutic pathway UI |
| `lib/trueassess_web/live/components/question_component.ex` | 4 | Question renderer |
| `lib/trueassess_web/live/components/certainty_indicator.ex` | 4 | Certainty bar component |
| `lib/trueassess_web/live/components/assessment_layout.ex` | 4 | Responsive layout |
| `lib/trueassess_web/plugs/api_auth.ex` | 5 | API authentication |
| `lib/trueassess_web/plugs/rate_limiter.ex` | 5 | API rate limiting |
| `lib/trueassess_web/controllers/api/session_controller.ex` | 5 | Session API |
| `lib/trueassess_web/controllers/api/session_json.ex` | 5 | Session JSON view |
| `lib/trueassess_web/controllers/api/results_controller.ex` | 5 | Results API |
| `lib/trueassess_web/controllers/api/results_json.ex` | 5 | Results JSON view |
| `lib/trueassess_web/controllers/api/catalog_controller.ex` | 5 | Catalog API |
| `lib/trueassess_web/controllers/api/catalog_json.ex` | 5 | Catalog JSON view |
| `lib/trueassess_web/controllers/api/fallback_controller.ex` | 5 | API error handler |
| `lib/trueassess/workers/score_assessment.ex` | 6 | Scoring Oban worker |
| `lib/trueassess/workers/generate_pathway.ex` | 6 | Pathway Oban worker |
| `lib/trueassess/workers/cleanup_sessions.ex` | 6 | Session cleanup cron |
| `lib/trueassess/workers/assessment_analytics.ex` | 6 | Analytics cron |
| `lib/trueassess/assessments/telemetry.ex` | 7 | Telemetry events |

### New Files (Tests)

| File | Phase |
|------|-------|
| `test/trueassess/assessments/assessment_session_test.exs` | 1 |
| `test/trueassess/assessments/session_response_test.exs` | 1 |
| `test/trueassess/assessments/session_result_test.exs` | 1 |
| `test/trueassess/assessments/session_gate_check_test.exs` | 1 |
| `test/trueassess/assessments/domain_test.exs` | 1 |
| `test/trueassess/assessments/seeds_test.exs` | 1 |
| `test/trueassess/assessments/session_queries_test.exs` | 1 |
| `test/trueassess/assessments/schema_integrity_test.exs` | 1 |
| `test/trueassess/assessments/delivery/session_init_test.exs` | 2 |
| `test/trueassess/assessments/delivery/answer_submission_test.exs` | 2 |
| `test/trueassess/assessments/delivery/adaptive_selection_test.exs` | 2 |
| `test/trueassess/assessments/delivery/certainty_test.exs` | 2 |
| `test/trueassess/assessments/delivery/gaming_integration_test.exs` | 2 |
| `test/trueassess/assessments/delivery/scoring_integration_test.exs` | 2 |
| `test/trueassess/assessments/delivery/pathway_linkage_test.exs` | 2 |
| `test/trueassess/assessments/delivery/full_session_test.exs` | 2 |
| `test/trueassess/assessments/delivery/context_test.exs` | 2 |
| `test/trueassess/assessments/gates/session_integrity_test.exs` | 3 |
| `test/trueassess/assessments/gates/gaming_detection_test.exs` | 3 |
| `test/trueassess/assessments/gates/score_validity_test.exs` | 3 |
| `test/trueassess/assessments/gates/result_rendering_test.exs` | 3 |
| `test/trueassess/assessments/gates/pathway_completeness_test.exs` | 3 |
| `test/trueassess/assessments/gates/gate_runner_test.exs` | 3 |
| `test/trueassess/assessments/delivery/gate_integration_test.exs` | 3 |
| `test/trueassess_web/live/assessment_catalog_live_test.exs` | 4 |
| `test/trueassess_web/live/assessment_session_live_test.exs` | 4 |
| `test/trueassess_web/live/components/question_component_test.exs` | 4 |
| `test/trueassess_web/live/assessment_session_answer_test.exs` | 4 |
| `test/trueassess_web/live/components/certainty_indicator_test.exs` | 4 |
| `test/trueassess_web/live/assessment_session_complete_test.exs` | 4 |
| `test/trueassess_web/live/assessment_results_live_test.exs` | 4 |
| `test/trueassess_web/live/pathway_live_test.exs` | 4 |
| `test/trueassess_web/live/assessment_session_management_test.exs` | 4 |
| `test/trueassess_web/live/assessment_responsive_test.exs` | 4 |
| `test/trueassess_web/plugs/api_auth_test.exs` | 5 |
| `test/trueassess_web/controllers/api/session_controller_test.exs` | 5 |
| `test/trueassess_web/controllers/api/results_controller_test.exs` | 5 |
| `test/trueassess_web/controllers/api/catalog_controller_test.exs` | 5 |
| `test/trueassess_web/plugs/rate_limiter_test.exs` | 5 |
| `test/trueassess_web/controllers/api/full_flow_test.exs` | 5 |
| `test/trueassess/workers/score_assessment_test.exs` | 6 |
| `test/trueassess/workers/generate_pathway_test.exs` | 6 |
| `test/trueassess/workers/cleanup_sessions_test.exs` | 6 |
| `test/trueassess/workers/assessment_analytics_test.exs` | 6 |
| `test/trueassess/pipeline/assessment_chain_test.exs` | 6 |
| `test/trueassess/assessments/e2e/happy_path_test.exs` | 7 |
| `test/trueassess/assessments/e2e/error_recovery_test.exs` | 7 |
| `test/trueassess/assessments/e2e/security_test.exs` | 7 |
| `test/trueassess/assessments/e2e/performance_test.exs` | 7 |
| `test/trueassess/assessments/telemetry_test.exs` | 7 |

### Modified Files

| File | Phase | Change |
|------|-------|--------|
| `lib/trueassess/assessments.ex` | 1 | Add 4 new resources to domain |
| `lib/trueassess_web/router.ex` | 4, 5 | Add assessment routes + API scope |
| `lib/trueassess/pipeline/chain.ex` | 6 | Add assessment worker chain |
| `lib/trueassess/pipeline/chain_state.ex` | 6 | Add assessment worker downstream |
| `lib/trueassess_web/telemetry.ex` | 7 | Add assessment telemetry handlers |

### Migrations

| Migration | Phase |
|-----------|-------|
| `XXXX_create_assessment_sessions` | 1 |
| `XXXX_create_session_responses` | 1 |
| `XXXX_create_session_results` | 1 |
| `XXXX_create_session_gate_checks` | 1 |

---

## Dependencies Between Phases

```
Phase 1 (Resources) ──→ Phase 2 (Orchestrator) ──→ Phase 3 (Gates)
                                                        │
                                                        ├──→ Phase 4 (LiveView UI)
                                                        │
                                                        ├──→ Phase 5 (JSON API)
                                                        │
                                                        └──→ Phase 6 (Oban Workers)
                                                                │
                                                                └──→ Phase 7 (E2E + Hardening)
```

- Phases 4, 5, and 6 can proceed in PARALLEL after Phase 3 completes
- Phase 7 requires all prior phases

---

## Convergence Criteria

Each phase is converged when:
- [ ] All tests pass (`mix test` for the phase's test files)
- [ ] No compilation warnings
- [ ] Credo passes with no issues above :normal
- [ ] Two independent audit passes find zero issues

The full plan is converged when:
- [ ] All 7 phases individually converged
- [ ] Full E2E test suite passes (Phase 7)
- [ ] `mix test` passes with zero failures
- [ ] Performance baselines met (Phase 7.4)
- [ ] Two consecutive clean passes across the entire plan

---

## Estimated Scope

- **36 implementation files** (new)
- **50 test files** (new)
- **5 modified files** (existing)
- **4 database migrations**
- **~350 individual tests** estimated
- **7 phases**, 50 tasks total
