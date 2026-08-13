# Memory wheels: progressive consolidation under an Ezekiel-shaped stack

Working architecture sketch. Companion to `EzekielAGI.md`.  
Earlier CAS-only draft lived in `MiddleWheel.md` (research-model paste; historical).  
This note is the synthesis: **what to build, in what order, on which substrate.**

Not a Moqui design doc. Not vetted implementation. Organizing frame for further review and research.

---

## 1. Purpose

`EzekielAGI.md` names the big unlike:

> Experience → consolidate → durable knowing  
> vs frozen weights + side databases + human ops

This document sketches **wheels that turn on memory**: nested loops under standing watch, so a single face of “the AI” can **grow**—remember, correct, and (selectively) internalize—without treating every lesson as a full retrain or a disposable chat turn.

**Center of gravity:** progressive memory.  
**Main car (near-term and default):** external structured memory + tools + eval gates.  
**Side car (later, gated):** parametric assimilation (adapters / context distillation / CAS-like ideas)—only after the main car works.

**Not claimed:** solved AGI, clean parametric forget, or continuous live weight updates as the default hippocampus.

---

## 2. Problem (plainly)

A live agent accumulates **working context**: instructions, tool traces, sandbox state, intermediate results. That state lives in the prompt / KV cache. It is powerful, costly, and mostly **volatile**.

| Escape hatch | What it does | What it doesn’t |
|--------------|--------------|-----------------|
| Longer context | Carry more episode state | Consolidate; cost grows with history |
| Naive RAG dump | Park text beside the model | Structure, supersession, intentional remember/correct |
| Occasional LoRA / FT | Some durable skill shift | Continuous, selective, reality-gated growth as native law |
| “Just fine-tune on the logs” | Absorb noise + bias | Safe progressive memory |

**Wanted:** durable patterns (facts-with-provenance, procedures, **errors and their corrections**) move from “gone when the session ends” toward “available next time, and increasingly default behavior”—without stuffing episodic scratch into weights.

That is the **spirit-in-the-wheels** bet: motion and knowing stay coupled. Correction is first-class; erase-from-weights is not the design center.

---

## 3. Three substrates (keep these distinct)

Progressive memory is not one bucket. Mixing them is how designs fail.

| Substrate | Holds | Write | Correct / “forget” | Good for |
|-----------|--------|--------|---------------------|----------|
| **A. Working (inner)** | Episode state, live sensors, current plan | Every step (KV, scratchpad, tool state) | Drop when episode ends; compact/summarize mid-task | What is true *now* in this run |
| **B. External structured (main car)** | Claims, notes, procedures, error→fix cases, entity state | Explicit tool, end-of-task extract, admission gate | **Supersede, deprecate, archive**—reliable | Ideas, citations, playbooks, lessons |
| **C. Parametric (side car)** | Smooth skills, domain priors, “how we usually do X” | Batched PEFT / distillation after eval | Weak unlearning; prefer **rollback adapter**, counter-train, or leave base frozen | Stable behavioral competence, not atomic notepad facts |

**Rule of thumb:** if you must edit it tomorrow with a sentence, it belongs in **B**. If it should change how the model acts even when retrieval misses, consider **C** later. If it is only true for this run, keep it in **A**.

---

## 4. Topology (Ezekiel roles = timescales and duties)

Not a product org chart. Not “middle wheel = distillation GPU.” Wheels are **nested loops**.

```
+-----------------------------------------------------------------------+
|         THRONE — objectives, values, admission & promotion policy       |
+-----------------------------------------------------------------------+
                                    |
+-----------------------------------------------------------------------+
|  OUTER WHEEL — progressive memory (promote into B and, rarely, C)     |
|    main car: structured stores     side car: adapters / distill (late)  |
+-----------------------------------------------------------------------+
                                    ^
                                    | candidates / evals / rollbacks
+-----------------------------------------------------------------------+
|  MIDDLE WHEEL — task/episode (curate context, traces, remember ops)   |
+-----------------------------------------------------------------------+
          ^                                               |
          | evidence                                      v actions / tools
+-----------------------------------------------------------------------+
|  INNER WHEEL — step inference + action (generation, tools, KV/work)   |
+-----------------------------------------------------------------------+
                                    |
+-----------------------------------------------------------------------+
|  RIMS FULL OF EYES — sensors, outcomes, tests, probes, provenance     |
+-----------------------------------------------------------------------+
```

| Vision | Duty | In this design |
|--------|------|----------------|
| **Throne** | What the stack serves; **what may stick** | Goals; remember/correct policy; prefer B over C; freeze base by default |
| **Outer wheel** | Long loop: consolidate and promote | Admit into **B** routinely; pack and train **C** only when justified; checkpoint/rollback |
| **Middle wheel** | Episode/task loop | Context curation; trace buffer; `memory.write` / extract lessons; stage candidates |
| **Inner wheel** | Step loop | Model + tools + working memory; contact environment |
| **Eyes** | Standing watch | Telemetry, task pass/fail, regression probes, claim-level consistency—not sensors alone |
| **Spirit in the wheels** | Coupling | After promotion, next runs retrieve (B) or act natively (C) without re-hauling the whole history as prompt |

Optional instruments (dual teacher/student models, Unsloth, etc.) hang off the outer side car. They do **not** redefine the inner wheel.

---

## 5. End-state shape (one face to the user)

```
                    User / goals  (throne inputs)
                            │
                            v
                 ┌──────────────────────┐
                 │  Policy + tools      │  inner wheel
                 │  (base model, slow)  │  frozen or rarely touched
                 └──────────┬───────────┘
                            │
              ┌─────────────┼─────────────┐
              v             v             v
         Working (A)   Durable stores (B)   Adapters (C)
         episode/KV    MAIN CAR             SIDE CAR
                       claims, procedures,  PEFT packs when
                       error→fix, state     eyes + throne allow
              │             │             │
              └─────────────┼─────────────┘
                            v
                    Admission + eval (eyes)
                    promote / supersede / reject
```

From outside: one AI that can be told “remember this,” “that was wrong; use Y when Z,” and that can also **propose** lessons after tasks. Inside: almost all durable growth hits **B** first; **C** is an optimization pass on stable patterns, not the notebook.

---

## 6. Main car — external structured memory

### 6.1 Why main

- **Correctable** (supersession beats unlearning).  
- **Inspectable** (provenance, “why do you believe this?”).  
- **Selectable** (retrieve what the task needs; don’t FT the universe).  
- **Realistic now** (agent memory products, claim stores, notebooks + retrieval).  
- Matches `EzekielAGI.md`: memory-first, selective parametric consolidation.

RAG-as-blob is not enough. Structure matters.

### 6.2 Record kinds (illustrative)

| Kind | Role | Example |
|------|------|---------|
| **Claim** | Vetted or provisional fact | “Pump X max rate is … (source, confidence)” |
| **Procedure** | How to do a recurring job | Playbook steps, tool sequence that passed eyes |
| **Error→fix** | Lesson from failure | Tried A → measured B → use C when D; keeps the mistake as teacher |
| **Entity / state** | Long-lived world model slice | Device config, project decisions, open issues |
| **Episode summary** | Compressed history | What happened last run (not full token log) |
| **Directive** | User/self instruction to remember | Explicit `memory.write` with scope and TTL optional |

**Error→fix is first-class.** Prefer remembering the wrong turn *and* the correction over deleting the wrong turn. That helps related future cases and avoids the parametric-forget fantasy.

### 6.3 Write paths

1. **Explicit:** user or agent tool — “remember …”, “correct …”, “deprecate …”.  
2. **End-of-task extract:** middle wheel proposes records from traces + outcomes; eyes/throne admit.  
3. **Scheduled compaction:** merge duplicates, supersede stale claims, archive dead procedures.

Nothing durable lands without a path through **admission** (even if admission is “auto-allow low-risk notes in a sandbox namespace”).

### 6.4 Read paths

- Retrieve by task / entity / similarity; **rerank**; ground answers in returned IDs.  
- Prefer procedures and error→fix when acting, claims when answering.  
- Do not dump the whole store into the prompt (that re-creates context bloat).

### 6.5 Correct, supersede, “forget”

| Intent | Mechanism on B |
|--------|----------------|
| Fix a fact | New claim supersedes old; old marked superseded (history kept) |
| Change a procedure | Version bump; prior version archived |
| “Forget that” | Deprecate/archive + exclude from default retrieval; hard delete rare |
| Learn from a bug | Add error→fix; optionally link superseded claim/procedure |

No requirement to edit base weights for these operations.

---

## 7. Side car — parametric assimilation (CAS-shaped, deferred)

Historical CAS idea (`MiddleWheel.md`): distill context-rich behavior into weights toward a “zero-context” skill state, often via teacher-with-\(C\) vs student-without-\(C\).

**Status here:** optional **outer side car**, not the main progressive-memory path. Use when **B** is working and some stable skill is still too slow/heavy to retrieve every time.

### 7.1 What it is good for

- Repeated procedures that should become fluent.  
- Domain style / priors that retrieval only approximates.  
- Shrinking **durable-redundant** prompt load (standing instructions already in B that the model still needs spoon-fed).

### 7.2 What it is bad for

- Atomic facts, citations, user secrets, one-off episode state.  
- Anything that must be corrected with a single sentence tomorrow.  
- Unsupervised firehose of traces (self-bias amplification).

### 7.3 How it should run (when eventually built)

```
[curated pack from B + graded traces]
        →  batched PEFT / context-distill on adapter (or bounded slice)
        →  eyes: task metrics + regression suite + “works with less retrieval?”
        →  throne: promote adapter / keep shadow / discard
        →  base model stays frozen unless a rare, deliberate merge
```

**Prefer async batches** over continuous online backprop while serving.  
**Prefer adapters** over full FT.  
**Prefer outcome-aware selection** (passed eyes) over pure logit imitation of a teacher that still holds the answer in \(C\).

Dual-size teacher/student and attention-map matching are **research options**, not requirements. Naive attention Frobenius match across unequal prefix lengths is ill-posed; park that until a real alignment recipe exists.

### 7.4 Relation to “zero-context”

**Aspiration:** large classes of durable skill need less and less re-prompting and re-retrieval.

**Grounding:**

| Context kind | Destination |
|--------------|-------------|
| Episode / live sensors | **A** only |
| Facts, lessons, playbooks | **B** first |
| Stable fluent skill | **C** candidate after B proves the pattern |

Success metric:

> Shrink **durable-redundant** prompt and retrieval load while holding task quality and base competence.

Not: literal empty context for all state forever.

---

## 8. Remember, correct, autonomy (single-AI behavior)

Assuming the stack is wired as one system:

| Capability | Supported? | How |
|------------|------------|-----|
| User: “remember X” | Yes | Tool → B (admission); C only if later pack includes it |
| User: “that was wrong; use Y” | Yes | Supersede + error→fix in B; optional later C refresh |
| User: “forget X” | Partial | Deprecate in B; adapters rolled back if they encoded X; base best-effort only |
| Self: propose what to keep | Yes | Middle extract + eyes + throne after tasks |
| Self: silent weight drift | **No (by policy)** | No admit → no promote; C never unsupervised firehose |

**Autonomy** means gated self-proposal, not unsupervised self-rewriting. Throne policy can be strict (human approve) or loose (auto-admit low-risk namespaces).

**Forget** is intentionally weak on **C** and unnecessary on most of **B** if supersession and error→fix are healthy. Progressive **correction** is the design center.

---

## 9. Eyes and throne (gates that make memory safe)

Without these, outer loops are self-training cosplay.

### Eyes (examples)

- Environment / sandbox telemetry and constraint violations.  
- Task success criteria (tests, graders, human score).  
- Regression probes: general skills and old procedures still work.  
- Memory hygiene: contradiction detection, stale claim flags.  
- For side car: “competence with reduced retrieval” probes.

### Throne (examples)

- Objectives and hard constraints.  
- **Admission:** what may enter B (and which namespace).  
- **Promotion:** what may enter C; never auto-touch full base by default.  
- Preference: when unsure, stay on B.  
- Stop conditions and rollback authority.

---

## 10. Runtime flow

### 10.1 Step / episode (inner + middle)

```
[1] Inner: act with working context (A) + retrieved durable (B) [+ active adapter C]
        |
        v
[2] Eyes: outcomes, telemetry, anomalies
        |
        v
[3] Middle: update A; optional memory tools; buffer traces
        |
        v
[4] End of task (or checkpoint): propose B writes (claims, procedures, error→fix)
        |
        v
[5] Eyes + throne: admit / edit / reject → B updated
```

### 10.2 Outer promote into B (continuous, lightweight)

```
Traces + extracts → dedupe / supersede / compact → B stays coherent over weeks
```

### 10.3 Outer side car into C (rare, heavy, batched)

```
Stable patterns in B + graded successes
        → pack dataset
        → train adapter
        → eval + regressions
        → promote or discard
        → middle may drop redundant standing prompt once C proven
```

Cadence: B can be every task; C might be weekly/monthly or “when pack is fat enough”—engineering choice, not theology.

---

## 11. Build order (realism tiers)

Do not start with live CAS.

### Tier A — build first (realistic now)

1. Structured stores **B** + memory tools (write, correct, supersede, retrieve).  
2. Error→fix as a normal record type.  
3. End-of-task lesson extract with admission.  
4. Eyes: task grades + basic regressions + provenance on writes.  
5. Prompt/program compilation: repeated B procedures → shorter standing instructions / macros (still not weights).  
6. Trajectory/skill library: save graded successful rollouts for retrieval.

### Tier B — selective parametric (after A is boringly reliable)

7. Curated PEFT packs from admitted B + graded traces.  
8. Domain adapters; shadow deploy; promote under eval.  
9. Offline context/prompt distillation for stable curricula.  
10. Outcome-conditioned preference on traces in graded envs (code, sim, CI).

### Tier C — research side car (optional)

11. Stronger teacher/student context distillation online or near-online.  
12. Continual learning on serving weights (usually still discouraged).  
13. Fancy activation/attention alignment across unequal contexts.  
14. Productized parametric unlearning (don’t depend on it).

**Original CAS continuous dual-model zero-context story ≈ Tier C.** Keep the aspiration; do not block the chariot on it.

---

## 12. Technical realism (summary)

| Piece | Realism | Note |
|-------|---------|------|
| Nested agent loops + async jobs | High | Systems engineering |
| Eyes as CI/evals/logs | High | Coverage is the hard part |
| Progressive memory on **B** | High | Best ROI; correctable |
| Admission + explicit remember | Medium–high | Noisy extractors; designable |
| Batched PEFT on curated packs | Medium–high | Narrow domain + evals |
| Context distillation offline | Medium | Skills/procedures > arbitrary facts |
| Reality-gated learning in cheap graded envs | Medium | Sandbox helps only if frequent and scored |
| Online continuous weight updates | Low–medium | Fragile, costly |
| General autonomous safe parametric growth | Low | Open research |
| Clean forget in weights | Low | Use B supersession + adapter rollback |
| Absolute zero context | Low | Shrink redundancy; keep working memory |

**Architecture language (wheels, eyes, throne): sound.  
CAS-as-primary-mechanism: not the best plan.  
B-first, C-later: the synthesis this doc commits to.**

---

## 13. Anti-patterns

- Fine-tuning on raw session logs without admission.  
- Treating RAG chunk soup as progressive memory.  
- Putting secrets or one-off state into **C**.  
- Calling imitation of a context-rich teacher “reality-tested” without outcome terms.  
- Pruning teacher context before the lean path is proven (target rot).  
- Expecting parametric forget to replace supersession.  
- Building dual-model AMAD before memory tools and evals exist.

---

## 14. Open questions (for later research / manual vetting)

**Main car (B)**  
- Schema: claim vs procedure vs error→fix fields, confidence, provenance graph.  
- Retrieval policy under token budgets.  
- Contradiction and supersession UX (user-facing and internal).  
- How much autonomy on admit by namespace.

**Gates**  
- Minimal regression suite for a given domain.  
- When human-in-the-loop is mandatory.  
- Calibrating “was this worth keeping?”

**Side car (C)**  
- Pack construction from B without leaking episode junk.  
- Adapter lifecycle (shadow, canary, merge, roll back).  
- Training signal: SFT vs preference vs distill; how eyes enter the loss.  
- Measuring durable-redundant context reduction honestly (not just shorter prompts).  
- Whether same-model+LoRA beats large-teacher/small-student for this use.

**Parked CAS math**  
- Equalizing or pooling representations when prefix lengths differ.  
- Cost model: train spend vs serve savings.  
- Forgetting mitigations if base is ever touched (replay, anchor KL, frozen sets).

---

## 15. Relation to other notes

| Doc | Role |
|-----|------|
| `EzekielAGI.md` | Metaphor + gap analysis; memory-first distance check |
| `MiddleWheel.md` | Earlier CAS-heavy research-model draft; not the build plan |
| **This file** | Synthesis: topology + B main car + C side car + tiers + flow |

---

## 16. Closing

In Ezekiel terms: build **rims full of eyes** and an **outer wheel that actually turns**—first by writing a living, correctable memory (**B**), then by rare, gated internalization (**C**)—so the **inner wheel** can go without dragging every past page as prompt.

Spirit-in-the-wheels here means: **lessons stay with the motion**, mostly as structured memory and progressive correction; weights catch up only when the pattern is stable and the eyes agree.

**Main car first. Side car later. Correction over erase. Vet mechanisms; don’t inflate claims.**
