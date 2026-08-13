# Memory wheels: progressive consolidation under an Ezekiel-shaped stack

Working architecture sketch. Companion to `EzekielAGI.md`.  
Research draft—organizing structure and open questions, not a vetted design or implementation plan.

---

## 1. What this is for

`EzekielAGI.md` argues that today’s models are unlike the chariot mainly where it matters most: **wheels that keep turning**—nested loops of memory, test, and revision—so the system **grows** instead of only speaking.

The decisive engineering hole named there:

> Experience → consolidate → durable knowing  
> vs frozen weights + RAG/LoRA trailers + human ops

This note sketches a **full stack** in Ezekiel vocabulary whose **center of gravity is that hole**: progressive memory (parametric and otherwise). Supporting loops are present so the metaphor stays honest; they are not all equally developed here.

**Not claimed:** solved AGI, a complete multi-year agent, or that weight writes replace vetted external memory.

---

## 2. Problem (plainly)

A capable model in a live environment accumulates **working context**: tool traces, sandbox state, instructions, intermediate results. That state lives in the prompt / KV cache. It is powerful and expensive—and mostly **volatile**.

Usual escapes:

| Approach | What it does | What it doesn’t |
|----------|----------------|-----------------|
| Longer context | Carry more episode state | Consolidate into nature; cost grows with history |
| RAG / claim stores | Park facts beside the model | Enter the model’s default behavior |
| Static LoRA / occasional FT | Some durable adaptation | Continuous, reality-gated, selective growth as native law |

**Wanted:** over time, **durable** patterns (domain logic, skills, stable procedures) move from “must be re-prompted or retrieved” toward “how the wheels already go”—without dumping **episodic** scratch into the weights and without catastrophic forgetting.

That movement is the **spirit-in-the-wheels** bet: motion and knowing stay coupled.

---

## 3. Corrected topology

Ezekiel’s image is **nested timescales and standing watch**, not a product org chart. Labels below are roles in a compound runtime—not proof from the text.

```
+-----------------------------------------------------------------------+
|              THRONE — objectives, values, admission policy              |
+-----------------------------------------------------------------------+
                                    |
+-----------------------------------------------------------------------+
|     OUTER WHEEL — progressive memory (consolidate, evaluate, promote) |
+-----------------------------------------------------------------------+
                                    ^
                                    | candidates / gradients / rollbacks
+-----------------------------------------------------------------------+
|     MIDDLE WHEEL — task/episode loop (curate context, stage traces)   |
+-----------------------------------------------------------------------+
          ^                                               |
          | evidence                                      v actions / tools
+-----------------------------------------------------------------------+
|     INNER WHEEL — step inference + action (live generation, KV/work)  |
+-----------------------------------------------------------------------+
                                    |
+-----------------------------------------------------------------------+
|     RIMS FULL OF EYES — env sensors, outcomes, probes, watchdogs      |
+-----------------------------------------------------------------------+
```

### Mapping table

| Vision | Role | What lives here in this sketch |
|--------|------|--------------------------------|
| **Throne** | Governing objectives + **what may become durable** | Goals/constraints; admission rules for parametric write vs stay episodic/external |
| **Outer wheel** | Long loop: **progressive memory** | Assimilate vetted patterns into parameters (full, adapter, or promoted student); evaluate consolidation; checkpoint/rollback |
| **Middle wheel** | Task / episode loop | Context curation; trace buffer; propose consolidation candidates; manage working memory load |
| **Inner wheel** | Step loop: infer and act | Generation, tools, live KV/context; contact with the environment |
| **Rims full of eyes** | Standing watch | Not sensors alone: telemetry, task outcomes, capability probes, forgetting monitors, “was this worth keeping?” |
| **Spirit in the wheels** | Coupling | When outer consolidation succeeds, inner motion carries durable knowing without hauling the whole library in every prompt |

**Prior draft mistake to avoid:** treating “middle wheel” as synonymous with a distillation GPU server, or “inner wheel” as defined by a 70B+8B speculative pair. Those are **optional instruments**. The wheels are **timescales and duties**.

---

## 4. Core mechanism (outer wheel)

**Bet:** Run the inner wheel with rich working context when needed; continuously (or on a schedule) train a path that reproduces **durable** competence **with less** of that context; promote only what passes eyes + throne.

High-level idea (training signal, not sacred math):

- A **context-rich** policy (teacher / target) acts with full episode prefix \(C\) when the task needs it.
- A **context-lean** policy (student / drafter / adapter-on-base) is pressured to match useful behavior as \(C\) is reduced or removed **for assimilable content**.
- The outer wheel updates isolated parameters (adapters or bounded subsets), evaluates, then **promotes or discards**.

Dual model sizes (large teacher, smaller student) are one implementation pattern—not required by the metaphor. Same-size base + LoRA, or teacher = frozen base + context and student = same base + trainable slice, are also on the table for later vetting.

**Reality contact:** Eyes supply outcomes and probes. If learning is only “imitate the teacher,” the stack is **imitation-with-a-sandbox-nearby**, not yet reality-tested consolidation. A serious build must decide how task success/failure and regression checks enter admission and loss—or honestly call that phase-2.

---

## 5. Supporting loops (brief)

### Inner wheel — step
Act: tokens, tools, sandbox commands. Hold **episodic** state in KV/scratch/tools. Do not treat every token of state as future weight meat.

### Middle wheel — episode / task
- Curate what stays in the working prompt vs external scratch.
- Buffer traces: actions, contexts, outcomes, teacher/student disagreements.
- Stage **candidates** for outer assimilation (stable skills and domain regularities—not run IDs and one-off sensor blips).
- Shrink redundant prompt load when outer promotions make it safe.

### Eyes — watch
- Environment telemetry (physical or simulated).
- Task pass/fail and constraint violations.
- Probes: old capabilities still intact? new skill holds with reduced context?
- Provenance-ish logging: what was absorbed, when, under what evidence (even if lightweight at first).

### Throne — gate
- Objectives the whole stack serves.
- **Admission policy:** semantic/durable vs episodic; risk tolerances; freeze regions of the base.
- Stop conditions: prefer external memory when parametric write is the wrong substrate (EzekielAGI’s memory-first bias stays in force unless evidence says otherwise).

---

## 6. Runtime loop (lean)

```
[1] Inner: act in environment with working context as needed
        |
        v
[2] Eyes: record telemetry, outcomes, anomalies
        |
        v
[3] Middle: buffer traces; curate context; mark consolidation candidates
        |
        v
[4] Outer: train lean path on candidates (async ok); score task + regressions
        |
        v
[5] Throne/eyes: admit, delay, or reject write
        |
        v
[6] Promote checkpoint or rollback; middle may prune durable-redundant prompt
        |
        v
      (repeat)
```

No day/night hard split required; async outer work is enough to call it a living outer tire. Cadence (every step vs hourly vs after task batches) is an engineering choice for later.

---

## 7. “Zero-context” aspiration — and grounding

**Aspiration:** Durable environmental logic and stable reasoning patterns become native enough that they need not be re-supplied forever as prompt or retrieval payload. In the limit, large classes of work approach a **zero redundant durable context** state.

**Grounding (functional caveats):**

| Kind of context | Destination |
|-----------------|-------------|
| Stable skills, domain priors, repeated procedures | Candidates for **outer** parametric (or long-lived adapter) memory |
| Vetted facts, citations, supersession | Often **external** claim/RAG store—not everything must enter weights |
| Episode state, live sensors, run-specific scratch | **Inner/middle** working memory only |

Success is better read as:

> **Shrinking durable-redundant prompt and retrieval load** while holding task quality and base competence  

not as:

> literal empty context for all time and all state.

Absolute “prompt requirements down to zero without forgetting” remains a research north star, not a milestone to declare from architecture prose alone.

---

## 8. Relation to memory-first

`EzekielAGI.md` distance check still applies: best practical stacks today stay **memory-first** (vetted claims, hybrid retrieval, grounded reading) with **selective** parametric consolidation.

This sketch does **not** overturn that. The outer wheel is one consolidation path under the throne—not a mandate for continuous full fine-tuning as a hippocampus substitute. When in doubt, eyes and throne should prefer correctable external memory over irreversible weight soup.

---

## 9. Open questions (for deeper technical vetting later)

- **Update target:** adapters on the serving model vs promoted smaller model vs shared trunk—what is “production”?
- **Training signal:** logit match alone vs attention/feature match vs env reward; how eyes enter the objective.
- **Alignment across unequal contexts/models:** comparing internal states when prefixes differ in length (and when depths differ) needs a real recipe; naive map subtraction does not.
- **Forgetting:** anchor-to-base, replay, frozen subsets, eval gates—prose “lock baseline matrices” is not a mechanism.
- **Candidate selection:** how middle wheel tells durable skill from episodic noise.
- **Teacher degradation:** if the rich path is pruned too fast, the distillation target rots.
- **Cost:** dual forward + continuous train may raise fleet compute even when serve prefixes shrink.
- **Scope of eyes:** sandbox physics only vs critics, tests, and claim-level watch.

---

## 10. Closing

In Ezekiel terms: this is a sketch of **wheels that actually turn on memory**—outer consolidation under eyes and throne—so the inner wheel can go without dragging every past page as prompt.

It is closer to the chariot than a single frozen forward pass. It is still only **one** living subsystem (progressive memory plus supporting loops), not the whole vision.

**Apt focus: spirit-in-the-wheels consolidation. Next work: vet mechanisms, not inflate claims.**
