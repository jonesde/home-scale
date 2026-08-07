# Aluminum vs Copper Rails – Trade-offs & Best Practices
EM-CSAM Micro-Railgun Print Head

## 1. Summary Comparison

| Factor                    | Aluminum                          | Copper                              | Winner for early prototypes |
|---------------------------|-----------------------------------|-------------------------------------|-----------------------------|
| Electrical conductivity   | ~61% of copper                    | 100% (reference)                    | Copper                      |
| Rail heating              | Higher                            | Lower                               | Copper                      |
| Machinability (desktop CNC) | Significantly easier             | More difficult (gummy when pure)    | Aluminum                    |
| Cost & availability       | Lower / excellent                 | Higher                              | Aluminum                    |
| Oxide / contact issues    | Native insulating oxide forms quickly | Much better                         | Copper                      |
| Consistency shot-to-shot  | More variable without special drive | Better                              | Copper                      |
| Suitability for splat tests | Fully adequate                   | Excellent                           | Aluminum (speed of iteration) |
| Long-term / higher performance | Acceptable with compensations  | Preferred                           | Copper                      |

**Overall recommendation**
Use **aluminum** for the first generation of barrels and splat testing. Switch to **copper** once the process is producing coherent deposits and you want maximum electrical performance and lower thermal load.

## 2. Aluminum Rails – Detailed Notes

### Advantages
- Much easier to machine cleanly on a Genmitsu 3020-PRO Ultra class CNC.
- Lower cost and widely available in precise rectangular bar stock.
- Higher rail heating is actually useful during early testing — thermal effects appear sooner and are easier to study.

### Disadvantages & Mitigations
- **Conductivity**: ~37% lower than copper → higher I²R losses and more rail heating. Expect roughly 10–30% less performance (velocity/efficiency) for the same drive settings on a short barrel.
- **Oxide layer**: Forms within seconds in air. It is thin (nanometers) and will be broken down by the main high-current pulse, but it increases contact variability.
  - Mitigation 1: Open the clamshell and lightly abrade + solvent-clean the working faces before a test series.
  - Mitigation 2: Add a short dedicated “ignition” or oxide-clearing pulse (higher voltage, current-limited, 10–100 µs) between preconditioning and the main launch pulse.
  - Mitigation 3: Strengthen the preconditioning phase with brief higher-voltage bursts.

### Preferred Alloy
- **6101** (electrical bus-bar grade) — best balance of conductivity (52–59% IACS) and mechanical strength.
- Alternatives: 1100 or 1350 if maximum conductivity is desired and lower strength is acceptable.
- Avoid 6061-T6 for the rails themselves (conductivity too low).

### Best Practices
- Use rectangular bar (e.g. 0.5–1.5 mm thick × 4–8 mm wide).
- Finish-machine the inner faces *after* the bars are fixed in the channel.
- Clean by opening the clamshell (not through the assembled bore).
- Treat early aluminum barrels as consumable test articles.
- Expect more surface debris and the need for more frequent cleaning than copper.

## 3. Copper Rails – Detailed Notes

### Advantages
- Highest conductivity → lowest rail heating and best electrical efficiency.
- More consistent contact resistance and better shot-to-shot repeatability.
- Preferred once you are pushing for higher velocity or longer barrel life.

### Disadvantages & Mitigations
- Pure copper is gummy and harder to machine on a small CNC.
  - Prefer **tellurium copper (C145)** for much better machinability while retaining high conductivity.
  - Or use hard / half-hard temper C110 / C101.
- Higher material cost.
- Still benefits from in-place finish machining of the working faces.

### Best Practices
- Same rectangular geometry and in-place finishing process as aluminum.
- Clean surfaces before critical tests (less critical than aluminum but still good practice).
- The same clamshell and mounting design works without modification — only the rail stock changes.

## 4. Shared Best Practices (Both Materials)

- **Geometry**: Rectangular bar, not square wire. Wider and thinner is easier to keep straight and finish accurately.
- **Installation**: Place bars in the machined channel, secure them, then finish-machine the critical faces in a single setup. This is the most reliable way to achieve parallelism on a desktop CNC.
- **Clamshell design**: One half carries the channels; the other half is a flat mating surface. This enables easy opening for cleaning, inspection, and rail replacement.
- **Electrical interface**: Bolted connection at the top of the rails to the driver board.
- **Consumable mindset**: Early barrels (especially aluminum) should be treated as replaceable test pieces.
- **Drive flexibility**: Keep the multi-phase drive architecture (preconditioning + optional ignition pulse + main launch) so the same electronics work optimally with both materials.

## 5. Development Sequence Recommendation

1. **Phase 1 (now)**: Aluminum 6101 rectangular rails in PEI clamshells. Focus on geometry, slurry, and drive waveforms. Use ignition pulse and regular cleaning.
2. **Phase 2**: Once coherent “dome-ish” deposits are achieved, build identical geometry barrels with copper (C145 or hard C110) rails for direct performance and thermal comparison.
3. **Phase 3**: Optimize thermal management and rail life based on the copper results; consider more advanced alloys or coatings later if needed.

This approach maximizes iteration speed early while preserving a clean path to higher performance.
