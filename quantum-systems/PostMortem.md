# Postmortem — 2026-08-17

Lessons from one working day of coaching plus a machine that will keep the grain. This is not a second methodology spec ([README.md](README.md) stays canonical). It is not a claim that the physics bet is proven. Evaluation criteria remain **utility** and **internal consistency** only.

---

## 1. What landed

On 2026-08-17 this directory went from a couple of starter files to a joinable constraint library. Twenty-one commits, about 14k insertions.

Snapshot at the end of the day:

| Layer | Count |
|---|---|
| Formal effects | 59 |
| Extracted implications | 447 |
| Predicted implications | 41 |
| Designs | 12 (8 formal, 4 draft) |
| Requirements | 38 |
| Nodes | 11 forced |
| Applications | 14 |
| Rebuild | one-shot, guards fail the shot |

The live pipeline is `effect → implication → design → requirement`, with a downward arrow for what a machine commits to (including conjecture, labeled). Markdown in `library/` is the science source of truth. The database is a query surface.

---

## 2. Hours if it were a schedulable job

A **clean-desk** count — papers already stacked, voice already locked, no wandering — is about **1,100 human hours** to type what landed: find the words, cut the clauses, hang the junctions. That is “how long to write it if the desk is already honest.”

**Getting** that desk, pre-AI, is another job. Pinning the *cliff* (not a review-article mush) across 59 effects is easily the entire clean-desk total before anyone opens the template. Niche files cost days to weeks each.

**Real people** do this sloppily: fat surveys, lost numbers, Curie glued to *T*<sub>λ</sub>, a seventh family to hide a leftover. Join work lives in memory and email. There is no rebuild guard. First architecture is usually wrong.

If a methodology dictator held the line for years anyway:

- **~8,000–15,000 person-hours** (about **4–8 FTE-years**)
- Central: **~10,000 h / ~5 person-years**

That is already past “a PhD.” It is a small institute project that ships a database *if* it does not become a review volume.

Those numbers still assume the object **survives**. That is the wrong unit.

---

## 3. Why it was not already done

The volume is real. It is not why this did not already exist.

A PhD or a committee emits a *narrative* with a theory-first spine. This tree is the opposite object: 59 self-contained cliff files, extracted clauses that still quote the file, conjectures that are not allowed to pretend they were extracted, machines that are not allowed to swallow leftovers, and a rebuild that fails if you cheat.

Likely failure and giving-up points, in order of how often they kill the artifact:

1. **Theory-first gravity.** The formal apparatus is treated as the machine. §4.4 becomes axioms. Taken constants get a derivation story (*R*<sub>K</sub>, 2.612, *π*²ℏ*c*/240).
2. **Fat grain.** Essays instead of atomic clauses. No two arrows. No way to ask “same machine?” without rereading the book.
3. **Equated kinds.** One thermal number shared across latch, superfluid, melt, and pin. One length shared across optical *δ* and London *λ*.
4. **No guard.** Predicted rows used as evidence. A thirteenth design for every interface. Incomplete mappings filled so the chapter looks closed.
5. **Committee attractor.** More people make the join worse. The locked rules (constraint-only, incomplete stays incomplete, no seventh family) are anti-incentives. Someone quietly violates them to ship a survey.

Hours do not fix those. More time without a locked grain and a failing rebuild is more drift. The scarce resource is one editorial voice that will throw work away.

**Pre-AI, this specific artifact was probably not completable.** You could get 59 essays, or a cold-fusion monograph, or a particle zoo. You would not get a joinable constraint library that still refuses to fill *R*<sub>K</sub> and still files water as capacity.

The day was 8–12 hours of coaching and poking. The thing it replaced is closer to a half-decade of a lab that, in the typical case, never ships this.

---

## 4. The uncommon assumption

The locked bet, from [README.md](README.md):

Quantum entities are modeled as finite-state machines (or deterministic, rule-bound systems). Once internal rules, node states, and constraints are known, behavior is fully predictable. Apparent randomness is incomplete knowledge. Macroscopic “laws” are the averaged, synchronized output of many constrained microscopic machines. **Design** means assembled spec, not intention. No agency, purpose, or programmer language.

That is not a common working assumption. Standard practice treats the formal apparatus as the machine and treats collapse or randomness as primitive or interpretive. Hidden-variable programs share a predictability *taste* but usually aim at Bell, not at a 10–20 nm Ag film.

### Two different jobs

The assumption does almost no **ontological** work in the files. No entry proves that electrons are finite-state machines. *R*<sub>K</sub> stays taken. 2.612 stays taken. That is deliberate. Evaluation is utility and internal consistency only.

It does almost all of the **shape** work. If the things are machines, the only honest extract from a cliff is a spec: buffer, clock, barrier, hold-power, erase. Families are collapse types, not textbook chapters. Incomplete mappings stay incomplete. Conjecture is labeled and cannot be used as evidence.

Without the bet you can still collect handbook numbers. You do not get a warrant to record Schrödinger or BCS as *descriptive data* in §4.4 and then ask whether reflection and photoelectric are the same machine on one surface. Maxwell + *n*,*k* already “explains” a mirror. The unusual move is to treat that explanation as data and demand a hardware envelope.

### How much of a factor

| Layer | How much the bet mattered |
|---|---|
| Words in any one library file | Small. The FSM sentence lives in the methodology, not in §4.3. |
| Why this object exists at all | Large. Selection and discipline filter — a third to a half of “why this, and not a survey.” The rest is grain, guards, and not giving up at the first leftover (QHE, BEC, QPC). |
| Completability | Load-bearing. The bet is why a typical lab would never start, and why, if they started, they would slide back to interpretation or “the Hamiltonian is the spec.” |

The coaching that held today — ignore less-reliable theory-first stuff, do not mint a seventh family, do not file water as a gate — only has a warrant *because* the criteria are utility and consistency under the machine bet. In a normal group that coaching is “being unscientific.” Here it is the method.

The day did not prove predictability. It **acted as if** predictability-once-understood is allowed, and then asked only what the machines cannot do. That permission is uncommon. It is why the day produced spec sheets and predicted exclusions instead of another foundations thread.

---

## 5. Lessons worth keeping

- **Lock the bet and the grain before the catalog.** Template, families-by-collapse, extracted vs predicted, rebuild fails the shot. Do not “write the science first and normalize later.”
- **Keep incompleteness visible.** A Medium mapping is not a failed entry. A taken constant is not a scandal. Filling a gap so the chapter looks closed is the failure.
- **One editorial voice beats a committee.** More authors need a harder guard, not a softer one.
- **Applications are knobs and falsifiers**, not protocols. Isolate the latch before the energy-gate. Water is capacity. Steam is not interstitial H. Do not bury a latch under four writes.
- **Shared *kind* is not a shared number.** Curie, *T*<sub>λ</sub>, *T*<sub>m</sub>, *T*<sub>B</sub>, and *T<sub>c</sub>(n)* are kin. Equating them is a mapping error.
- **The next science step is still to tighten a Medium mapping**, not to add a fourteenth design or a fifteenth application.

If this file disagrees with a formal library entry about a cliff, the library file wins.
