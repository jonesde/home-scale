---
id: slug
title: Effect Name (Optional QSA Gloss)
status: draft
family: collective-field-response
constraints:
  - spatial-buffer
confidence_data: medium
confidence_mapping: unmapped
related: []
updated: YYYY-MM-DD
---

# Effect Name (Optional QSA Gloss)

### 4.1 Effect Name

Concise, conventional name of the phenomenon.

### 4.2 Macroscopic Observation

What is directly measured or experienced at the macroscopic scale. Keep this purely observational.

### 4.3 Established Quantitative Boundaries

Key numerical thresholds, scaling relations, and experimental limits. One fact per bullet. Start each bullet with its evidence tag and end it with its citation key(s):

- **Measured.** What an instrument read, with the number and unit [S1].
- **Model (name of the model).** A value obtained by passing measurements through that model [S2].
- **Convention.** A definition or an agreed cut on a continuous quantity [S3].
- **Computed here.** Arithmetic from cited inputs, with the inputs shown. Add the same calculation to `analysis/computed_checks.py`.

Include a confidence rating for the data themselves (High / Medium / Low) based on reproducibility and precision of the measurements. Name any load-bearing number whose only source could not be opened.

**Data confidence:**

### 4.4 Standard Mathematical Description

The principal equations, parameters, or formal relations used in the literature, each with a citation key.

These are recorded strictly as data that describe observed behavior; they are not treated as foundational axioms.

### 4.5 QSA Mapping

- **Minimum hardware scale / node count / coherence volume**
- **Clock rate / latency**
- **Energy barriers or thresholds**
- **Dominant failure modes** — label each one **Threshold** (switches at a definite value) or **Crossover** (falls off continuously; give the functional form, its scale, and the convention behind any single number).
- **Emergent constant or stable output**

### 4.6 Internal Consistency Notes

Does the mapping close cleanly under the working assumptions?

Record any gaps, tensions, missing constraints, or places where the finite-state-machine picture does not yet account for the data.

### 4.7 Overall Confidence in the QSA Mapping

High / Medium / Low — one-sentence justification focused on how well the extracted specifications fit the observed boundaries and failure modes.

## Related entries

- `other-slug` (queued) — why it is related

## Sources

Rules and the meaning of the Checked column: [README.md](README.md#sourcing-standard).

| Key | Reference | Checked | Supports |
|---|---|---|---|
| S1 | [Authors, *Journal* volume, page (year)](https://example.org) | full-text | Which numbers or statements in this file rest on it. |
