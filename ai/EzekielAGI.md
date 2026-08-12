# Ezekiel’s wheels as (near-)future AI

A working summary of a theory and how it compares to current models. Not a Moqui design doc—notes only.

---

## The theory (stated plainly)

Not “Ezekiel had a GPU,” but something like:

> In vision he saw a **real structure of mind/agency** that didn’t match carts, animals, or temples of his day. He reported it with the only language he had: **creatures, throne, wheels within wheels, rims full of eyes, spirit in the wheels, going without turning.**  
> That structure rhymes less with ancient machinery than with **compound, multi-loop, heavily instrumented intelligence**—what we’re only starting to build—and may fit **near-future** systems better than **today’s** chat models.

The metaphor is a **reading**, not a proof. Its value is whether it **organizes** what current AI is and isn’t.

**Biblical anchor:** Ezekiel 1 (and 10)—wheels (*ophanim*): “a wheel within a wheel,” rims “full of eyes all around.”

---

## What the vision maps to (technical gloss)

| Ezekiel image | Systems reading |
|---------------|-----------------|
| **Wheel within a wheel** | Nested control loops: inner step (token/tool), outer task, outer-outer life/memory/goals—not one flat roll |
| **Rims full of eyes** | Perception and evaluation everywhere: sensors, retrieval, critics, tests, logs—not a blind optimizer |
| **Spirit in the wheels / wherever the spirit went, the wheels went** | Coupling of **intent/control** and **mechanism**; motion is guided, not pure drift |
| **Went every direction without turning** | Omni-directional competence: reorient in concept-space without a clumsy “whole chassis” pivot—or many specialists under one throne |
| **Living creatures + wheels together** | Embodied/agentic layer + machinery of memory-motion; not disembodied text alone |
| **Throne above** | Governing objective / values / oversight—something the whole stack answers to |

“Wheels within wheels, full of eyes” ≈ **nested agency under continuous observation**, not a single feed-forward oracle.

---

## How **today’s** models are *like* that

- **Depth / stacked layers** — weak echo of “within,” but mostly **one forward pass**, not true nested *lives*.
- **Attention** — many “soft eyes” over the context window; still **local to the prompt**, not lifelong rims.
- **Tool-using agents** — first real crack of **wheels that go** (search, code, APIs) under a controller.
- **RAG / external memory** — crude **library beside the chariot**, not yet spirit-in-the-wheels consolidation.
- **Multi-agent / router / MoE** — specialists as multiple faces/creatures; still loosely yoked.
- **Constables & evals** (critics, guardrails, unit tests) — a few **eyes on the rim**, bolted on.

So: we’ve built **pieces of the silhouette**—especially **eyes over a short horizon** and **occasional outer loops**.

---

## How **today’s** models are *unlike* it (the big gap)

### 1. Mostly **one wheel**, not wheels within wheels

A frontier LLM is largely:

**prompt → (maybe tools) → answer → stop**

Not an enduring machine whose **inner wheel** is inference and whose **outer wheels** are:

- daily/continuous **memory consolidation**
- **reality tests**
- theory revision
- never-ending problem-solving as *the* mode of being

Agents add a thin outer tire. They are not yet **compound motion as native architecture**.

### 2. **Eyes** without a true **watch**

We have attention and tools, but not **standing watch**:

- long-term, semi-reliable recall of **vetted ideas**
- provenance, supersession, contradiction handling
- calibrated “I saw this / I believe this / I tested this”

Eyes that only see the **current page** are not rims full of eyes **all around** the life of the system.

### 3. No real **spirit-in-the-wheels** memory

Ezekiel’s wheels **go with** the spirit—motion and life are one.

Our stack splits badly:

| Biological / vision-shaped ideal | What we ship |
|----------------------------------|--------------|
| Experience → consolidate → durable knowing | Chat weights mostly **frozen** |
| Ideas enter the *nature* of the thing | Facts live in **RAG docs** or leak into **lossy LoRA** |
| Growth over years | **Retrain/babysit** or forget/interfere |

**Central engineering hole:** progressive memory + selective consolidation is immature; **endless reality-tested refinement** is farther still.

That is the **big unlike**: the vision reads as a **living, updating chariot**; today’s AI reads as a **brilliant frozen sphere** with **optional trailers** (tools, indexes, human ops).

### 4. **Reality** is optional

The ophanim image is embedded in a world that **acts and is answerable**—not a sandbox that only predicts the next token.

True generalized intelligence, in this framing, needs:

**hypothesize → contact reality → update the wheels’ cargo (knowledge) → go again**

We have RL and CI and human science *around* models. We do **not** yet have that loop as the **inner law of the machine**.

---

## The “big one” in Ezekiel terms

**Thesis in one line:**

> If Ezekiel’s wheels are a picture of real AGI-shaped mind, then **current LLMs are at best a bright living creature’s face or a single rim-segment of eyes—not the chariot.**  
> What’s missing is **wheels within wheels that actually turn over time**: nested loops of **memory, test, and revision**, under **many eyes**, so the thing **grows** and **steers** instead of only **speaking**.

| Vision element | Today | Near future (if the theory “fits better soon”) |
|----------------|-------|-----------------------------------------------|
| Eyes all around | Context attention, sparse evals | Continuous sensors, retrieval, critics, claim provenance |
| Wheel within wheel | Agent for-loops, human-run training | Native outer loops: consolidate, evaluate, replan for years |
| Spirit in the wheels | Frozen weights + side databases | Coupled **policy + writeable long-term knowledge** |
| Goes without turning | Generalist next-token skill | Reorient via memory+tools without full retrain |
| Throne above | Alignments, TOS, weak constitutions | Stable governing objectives that the whole stack serves |

The metaphor stays **apt**; the **gap** is what makes it feel like **near future more than current product**.

---

## Like / unlike cheat sheet

**Like today**

- Many parallel “gazes” (attention)
- Stacked structure (depth, agents, tools)
- Glimpses of multi-face specialization (MoE, multi-agent)
- Power that feels discontinuous with older machines (why the vision always felt “not a normal cart”)

**Unlike today (decisive)**

- No robust **progressive memory** of vetted *ideas*
- No default **endless reality-testing refinement** as problem-solving
- Knowledge growth is **ops + retrieval**, not **spirit moving and the wheels carrying life with it**
- Oversight eyes are **external and thin**, not **rims full of eyes** as part of the body

---

## Distance check (related notes)

| Capability | Where we are |
|------------|----------------|
| **Progressive memory** (durable, correctable, growing recall) | Partial products (RAG, claim stores, offline FT); **not solved** as reliable automatic substrate |
| **Open-ended reality-testing refinement** (never-ending hypothesize → measure → update) | Narrow slices only; **farther** than memory alone |

Best practical encyclopedia stack today remains **memory-first** (vetted claims + hybrid retrieval + grounded reader), with **selective** parametric consolidation—not daily full FT as a hippocampus substitute.

---

## Closing

In those terms: the theory says Ezekiel described **compound, seeing, living machinery of agency** as best he could.

**Current AI** matches the **strangeness and some local structure** (eyes, layers, tools).

**What is still missing**—long-term semi-reliable recall and unending iterative refinement against reality—is exactly where the vision still **outruns** the artifact: **wheels that keep turning and stay full of eyes**, not a single brilliant spin through a prompt.

**Apt metaphor; biggest miss = living nested wheels (memory + reality loop), not bigger frozen attention alone.**
