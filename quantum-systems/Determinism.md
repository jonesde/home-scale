# Determinism and this project

**Status:** survey and position note, dated 2026-11-11. It does not claim that the project's premise is true or false.

## Summary

Standard quantum theory has a deterministic law of evolution and a probabilistic rule for measurement outcomes. Experiments exclude one class of deterministic account: hidden variables that are local, give single outcomes, and are statistically independent of the measurement settings. They do not exclude determinism. A deterministic account survives in three ways, each at a price. Pilot-wave theory gives up locality. Everett's theory gives up single outcomes. Superdeterminism, used by the cellular-automaton program, gives up the independence of settings and hidden variables, as do retrocausal models. The programs that reproduce the quantum statistics predict the same results as the standard theory, so no experiment to date favours one. Objective-collapse models do predict differences; they are not deterministic, and part of their parameter range is excluded. The project's catalog holds 60 effects that are averages, thresholds or static states. Every program gives the same numbers for those, so the catalog cannot bear on the question either way.

## 1. What "deterministic" has to mean here

"Deterministic" covers four separate claims, which the theorems in section 3 treat separately [S1]. The project's premise, "mechanical predictability of states and behaviors" ([README.md](README.md), section 1), is the first of them: the configuration and the rules fix what a system does next. Predictability by an observer is a fifth claim, and determinism does not supply it [S2].

| Claim | Meaning |
|---|---|
| Deterministic evolution | The state at one time, with the law, fixes the state at every other time [S3]. |
| Definite values | Every observable has a value at all times, measured or not [S4]. |
| Locality | The result of a measurement on one system is unaffected by operations on a distant system [S5]. |
| Statistical independence | The measurement settings are statistically independent of the hidden variables; also called measurement independence or freedom of choice [S1]. |

The four come apart: pilot-wave theory is deterministic and nonlocal [S6]. Bell's locality condition contains no assumption of determinism, and every nonlocal model is equivalent to a nonlocal deterministic one, so a Bell violation does not by itself show that outcomes are undetermined [S7].

Determinism is a claim about the law; predictability is a claim about what a finite observer can work out [S2]. Chaotic systems are deterministic, and slightly differing initial states evolve into considerably different states [S8][S9]. Pilot-wave theory shows the same separation: its outcomes are random because the initial configuration of the particles is unknown, and the trajectory of a single particle cannot be observed in an experiment on that particle [S10]. A Bohmian universe, though deterministic, evolves so that "an *appearance* of randomness emerges, precisely as described by the quantum formalism" [S11].

The README words the premise as a statement about the rules, and says that it does not assert the configuration can be measured or single events forecast. An earlier wording, "full predictability once understood", asserted more, namely that the hidden state can be learned well enough to predict single outcomes; the Colbeck–Renner theorem in section 3 limits that claim [S12]. The wording was changed on 2026-11-11 for that reason.

## 2. What the standard theory already says

The standard theory is deterministic between measurements and probabilistic at measurement; whether the whole is deterministic depends on the interpretation [S3][S2].

The Schrödinger equation is deterministic and linear: the state vector at one time uniquely determines it at any other time [S3]. If nothing interrupts that evolution and the wave function is the complete description, quantum mechanics is "a perfectly deterministic theory" [S2]. Indeterminism enters with measurement: the measurement problem is how to reconcile the deterministic evolution with the observed occurrence of random outcomes [S13]. Wave-packet reduction, the process assigned to measurement, is nonlinear and stochastic [S14].

Decoherence does not remove the indeterminism [S13]. Interaction with the environment destroys interference between the pointer states of a system, which explains why interference is suppressed and a preferred basis selected [S15][S16]. It does not explain why one outcome occurs: the superposition still exists in the larger system that includes the environment [S16], and the predictive part of the theory presumes the collapse postulate and Born's rule [S13].

In quantum field theory the usual reading takes fields as basic and a particle as an excitation of a field [S17][S18]. Two arguments support it: no-go theorems rule out localizable particles in relativistic quantum theory [S19], and an interacting system cannot be interpreted in terms of particles [S20]. The dissent is that both arguments also count against the wave-functional form of the field interpretation [S21], and that operator-valued quantum fields cannot be read directly as physical fields [S18].

## 3. Theorems

None of these theorems excludes determinism [S7][S22]. Each excludes a combination of assumptions, and a deterministic account escapes by dropping one of them [S1].

| Theorem | What it assumes | What it concludes | What a deterministic account gives up to escape |
|---|---|---|---|
| Bell 1964; Clauser–Horne–Shimony–Holt (CHSH) 1969 [S5][S23] | Locality; settings independent of the hidden variable λ; single outcomes [S7][S1] | Local models give S ≤ 2 for the CHSH quantity S; quantum mechanics reaches 2√2 and no more (Tsirelson bound) [S7] | Locality, single outcomes, or statistical independence [S1] |
| Kochen–Specker 1967 [S24] | Definite values for all observables; noncontextuality: a value does not depend on how it is measured [S4] | Certain sets of observables cannot consistently be assigned values [S4] | Noncontextuality [S4] |
| Free will theorem [S25][S26] | Axioms SPIN, TWIN and FIN (MIN in 2008); the experimenters' choices are not a function of the past | The particles' responses are not a function of the past | The premise about the choices; the theorem is conditional on it |
| Pusey–Barrett–Rudolph [S27] | A real physical state; independent states for independently prepared systems | The quantum state is not mere information about that state | Nothing on determinism, which is not assumed; the wave function counts as physical, or preparation independence goes |
| Colbeck–Renner [S12] | Quantum theory is correct; settings can be chosen uncorrelated with everything outside their future light cone | No extension of quantum theory predicts outcomes better than the quantum state | Free choice in that light-cone sense |
| Leggett 2003; Gröblacher et al. 2007 [S28][S29] | Outcomes fixed by pre-existing properties; subensembles of definite polarization obeying Malus' law; nonlocality allowed | An inequality that measured correlations violate | The definite-polarization assumption; Bohm's theory lies outside the class |
| Leggett–Garg [S30][S31] | A macroscopic system is always in one of its distinct states and can be measured with arbitrarily small disturbance | An inequality in time that quantum mechanics violates | One of the two assumptions |

**Bell.** Wiseman separates two theorems: the 1964 result is the incompatibility of quantum phenomena with locality and determinism together, and the 1976 result is their incompatibility with local causality alone [S32]. Those who keep locality take the first as a reason to give up determinism [S32]. Brunner et al. add that every nonlocal deterministic model is "necessarily signaling", so a model that is intrinsically no-signalling must contain some randomness [S7].

**Colbeck–Renner.** The theorem classifies pilot-wave theory and does not refute it: such theories "necessarily come at the expense of violating Assumption FR", the light-cone definition of free choice [S12].

## 4. Deterministic and determinism-compatible programs

Three programs are deterministic and reproduce the quantum statistics or aim to: pilot-wave theory, Everett's theory and the cellular automaton [S11][S33][S34]. None has a confirmed prediction that differs from the standard theory [S6][S35]. Collapse models predict differences and are not deterministic [S36].

### 4.1 Pilot-wave theory (de Broglie–Bohm)

**What it says.** Particles move on definite paths choreographed by the wave function; the theory is deterministic [S11].

**What it reproduces.** All the phenomena of nonrelativistic quantum mechanics, with the same results as the usual interpretation [S22][S37].

**Support.** Its existence shows that an objective description of individual systems is possible [S37]; Bell wrote that in Bohm's papers he "saw the impossible done" [S22]. A simulated ensemble that starts away from the quantum distribution relaxes toward it [S38].

**Criticism.** The theory is nonlocal [S6]. Its relativistic versions use a privileged foliation of space-time and are not Lorentz invariant at the fundamental level [S39][S40]. Hoefer, citing Wallace, says the theory and its extensions "do not yet offer an alternative to the standard quantum field theories of the Standard Model" [S2].

**Field versions.** The guided variables can be field configurations, as in Bohm's treatment of the electromagnetic field; this works for bosonic fields and has not succeeded for fermionic fields [S40]. Of the particle approaches to fermions, two are stochastic and one is deterministic [S40].

**Different prediction.** None in quantum equilibrium [S40]. Out of equilibrium, Valentini predicts anomalous spectra in the cosmic microwave background [S41]. A fit to Planck data improved at the 2–3σ level with temperature data and less when polarization data were added; the authors call the result "statistically inconclusive" [S35]. Goldstein, a proponent, writes that "we have at present no idea what quantum non-equilibrium, should it exist, would look like" [S22].

### 4.2 Everett (many worlds)

**What it says.** Only unitary evolution occurs and all possible outcomes occur; the theory is deterministic, and the world appears indeterministic to observers [S33].

**What it reproduces.** Everett aimed at a formulation from which the conventional interpretation can be deduced [S42]; it makes no testable prediction that differs from standard quantum mechanics [S6].

**Support.** Deutsch, Wallace, and Sebens and Carroll derive the Born rule from decision theory or from self-locating uncertainty [S43][S44][S45].

**Criticism.** Vaidman, a proponent, calls the question of how probability can exist if all outcomes occur "arguably the most serious difficulty" [S33]. Kent argues that no known version accounts for the appearance of probabilities [S46].

**Different prediction.** None [S6].

### 4.3 Cellular automaton and superdeterminism

**What it says.** 't Hooft proposes that quantum mechanics is a tool for analysing a system that is classical and deterministic at its core [S34]. Bell's theorem is avoided by superdeterminism: the hidden variables are not statistically independent of the settings [S47].

**What it reproduces.** Toy models; "an ontological basis for the Standard Model has not yet been found" [S34].

**Support.** The account is local and deterministic [S47]. The dependence it needs is small: giving up 14% of measurement independence reproduces all singlet correlations [S48].

**Criticism.** Shimony, Horne and Clauser objected that scepticism of this kind would "dismiss all results of scientific experimentation" [S1]. Sen and Valentini prove that such models need a finely tuned distribution of hidden variables, and that nonlocal and retrocausal models do not [S49]. Baas and Le Bihan argue that the failure of statistical independence would be global and the picture holistic [S50]. Chen argues that a superdeterministic theory recovering all quantum predictions would be observationally equivalent to Bohmian mechanics and less simple, though its credence should not be zero [S51].

**Different prediction.** Proposed: outcomes of repeated measurements of non-commuting observables on the same prepared state would be correlated, where the standard theory predicts none [S52]. The regime is small, cold devices and short time steps, and the required similarity of the prepared states cannot be calculated without a specific theory [S47]. No experiment designed to test such a model was found for this survey.

### 4.4 Retrocausal models

**What it says.** Some hidden parameters depend on measurement settings in their future, which violates statistical independence with no common cause in the past [S53][S54].

**What it reproduces.** Toy models of specific entanglement phenomena; extension to all quantum phenomena is "a grand challenge", and a treatment of measurement is "not yet clearly in sight" [S53].

**Support.** The models are locally mediated [S53] and not conspiratorial by Sen and Valentini's measures [S49].

**Criticism.** Hossenfelder objects that retrocausality is superdeterminism under another name; the reply is that this depends on the account of causation [S54].

**Different prediction.** The sources used here give none.

### 4.5 Stochastic electrodynamics and stochastic mechanics

Neither program gives a deterministic account that reproduces the quantum statistics [S55][S56]. Stochastic electrodynamics, which is classical electrodynamics of point charges plus random classical radiation scaled by Planck's constant, agrees completely with quantum calculations for charged harmonic oscillators [S57]. In simulations of hydrogen the atom ionises at longer times, with or without relativistic corrections [S55][S58]; Boyer disputes that conclusion [S57]. Nelson's stochastic mechanics derives the Schrödinger equation from particles in Brownian motion [S56]. A quantization condition has to be added by hand [S59], and Nelson reports that the theory is nonlocal and "can give wrong predictions for measurements performed at two different times" [S60].

### 4.6 Objective-collapse models (not deterministic)

Collapse models change the dynamics, so they can be tested against the standard theory [S36]. They add a stochastic, nonlinear term to the Schrödinger equation so that microscopic objects follow quantum theory and macroscopic objects behave classically [S36][S61]. The collapse is random and would make charged particles emit radiation [S62].

A germanium detector at Gran Sasso found no excess and set R₀ > 0.54 × 10⁻¹⁰ m; the parameter-free Diósi–Penrose model gives R₀ = 0.05 × 10⁻¹⁰ m and is ruled out, while versions with free R₀ remain [S62]. For continuous spontaneous localization the bound is λ < 5.2 × 10⁻¹³ s⁻¹ at r_C = 10⁻⁷ m [S63]. The rate of Ghirardi, Rimini and Weber, λ = 10⁻¹⁶ s⁻¹, lies below that bound; Adler's λ = 4 × 10⁻⁸±² s⁻¹ lies above it [S63] and is described as experimentally falsified [S14].

### 4.7 Comparison

| Program | Deterministic? | Local? | Basic objects | What it gives up | Distinguishing test |
|---|---|---|---|---|---|
| Pilot-wave, particles | Yes [S11] | No [S6] | Particles and a wave function | Locality; fundamental Lorentz invariance [S40] | None in equilibrium [S40] |
| Pilot-wave, fields | Yes for bosonic fields; no working fermion version [S40] | No [S40] | Field configurations and a wave functional | The same, and a field account of fermions | The same |
| Everett | Yes [S33] | Bell's theorem does not apply: outcomes are not unique [S1] | Wave function | Single outcomes; an agreed account of probability [S33] | None [S6] |
| Cellular automaton | Yes [S34] | Yes [S47]; critics find holism [S50] | Automaton states | Statistical independence [S47] | Time correlations; proposed, not performed [S52] |
| Retrocausal | The past alone does not fix the parameters [S53] | Yes [S53] | Toy-model parameters | The usual direction of causes in time [S53] | None stated |
| Stochastic electrodynamics | Classical, with a random radiation field [S57] | Not covered here | Point charges and classical fields | A stable hydrogen atom, in simulations [S55] | Hydrogen stability [S55] |
| Stochastic mechanics | No [S56] | No [S60] | Particles in Brownian motion | Locality; correct two-time correlations [S60] | Two-time correlations [S60] |
| Objective collapse | No [S14] | Not covered here | Wave function with random collapses | Unitary evolution [S36] | Radiation and interference bounds [S62][S64] |

## 5. Experiments, each with its theoretical context

Experiments have excluded local hidden variables under statistical independence [S65], noncontextual value assignments [S66], one class of nonlocal realistic theories [S29], macroscopic realism with noninvasive measurement [S67], classical-wave models of light [S68], and part of the collapse-model parameter range [S62]. None has excluded a deterministic program that reproduces the quantum statistics [S2].

| Experiment | What was measured | Result | What it excludes | What it leaves open |
|---|---|---|---|---|
| Freedman and Clauser 1972 [S69]; Aspect et al. 1982 [S70] | Polarization correlations of photon pairs; in 1982 with analyzers switched in flight at incommensurate frequencies near 50 MHz | Bell inequalities violated, by six standard deviations in 1972 [S6] and 5 in 1982 | Local hidden variables, subject to loopholes | Locality loophole until 1982; detection loophole after [S6] |
| Kimble et al. 1977 [S71]; Grangier et al. 1986 [S68] | Photon statistics of resonance fluorescence; detections on both sides of a beam splitter | Antibunching; strong anticorrelation, and interference visibility over 98% with the same source | Semiclassical and classical-wave models of light | Accounts with a quantized field |
| Norman et al. 1988 [S72]; Wilkinson et al. 1997 [S73] | Decay of ⁶⁰Co at times ≲10⁻⁴ t₁/₂ and ⁵⁶Mn over 0.3 t₁/₂ ≤ t ≤ 45 t₁/₂; tunnelling at short times | Exponential for the nuclei; non-exponential at short times in tunnelling | An exactly exponential law | Nothing on determinism: quantum mechanics predicts the deviation |
| Tonomura et al. 1989 [S74]; Fein et al. 2019 [S64] | Interference of single electrons, and of molecules beyond 25,000 Da | The pattern builds up from single electrons; molecular fringes above 90% of expected visibility | A classical explanation; part of the collapse-model range [S64] | Every program without collapse |
| Oberholzer et al. 2002 [S75], via [S76] | Shot noise of a chaotic electron cavity against dwell time | Fano factor 1/4 at long dwell times, lower at short ones | Nothing on determinism | A crossover inside standard quantum mechanics: deterministic particle scattering is noiseless, wave scattering noisy [S76] |
| Berkeland et al. 2004 [S77] | 228,000 quantum jumps of one ⁸⁸Sr⁺ ion | No correlations; entropy reduction < 6.5 × 10⁻⁴ when a jump interval is known | Correlations above that level | Weaker correlations; the test did not target a deterministic model |
| Couder and Fort 2006 [S78]; Andersen et al. 2015 [S79]; Pucci et al. 2018 [S80] | Walking droplets passing slits | 2006: interference-like histograms. Later: a wall effect dominates; the dependence of peak number on slit width is not recovered | The droplets as a reproduction of the quantum double slit | Other analogues, such as orbital quantization [S79] |
| Jacques et al. 2007 [S81] | Single photons in an interferometer set open or closed by a quantum random number generator, space-like separated from the photon's entry | Visibility 94% closed; path error below 1% open | Not stated in the abstract | No source used here gives a deterministic account of delayed choice |
| Gröblacher et al. 2007 [S29] | Photon correlations against a Leggett-type inequality | Violated | One class of nonlocal realistic theories | Other nonlocal theories, Bohm's among them |
| Kirchmair et al. 2009 [S66] | A noncontextuality inequality on trapped ions | Violated for arbitrary states, no detection loophole | Noncontextual models | Contextual hidden variables [S4] |
| Palacios-Laloy et al. 2010 [S82]; Knee et al. 2012 [S83], 2016 [S67] | Leggett–Garg correlations in superconducting circuits and in phosphorus spins in silicon | Violated: 5 standard deviations (2010); ~84 s.d. for 170 nA currents over ~10 ns (2016) | Macroscopic realism with noninvasive measurement | The "clumsiness loophole" [S31], addressed in 2016 by control experiments |
| Scheidl et al. 2010 [S84] | Bell test with random-number generators space-like separated from the pair source [S1] | Violation | Local realism, with the locality and freedom-of-choice loopholes addressed | Deterministic local models: the loopholes close "only within non-determinism" |
| Pironio et al. 2010 [S85]; Bierhorst et al. 2018 [S86] | Random bits certified by a Bell violation | 42 new random numbers at 99% confidence; 1024 bits uniform to within 10⁻¹² | Prediction by a theory that prohibits superluminal signalling and allows independent measurement choices | Theories that deny either condition |
| Kocsis et al. 2011 [S87]; Mahler et al. 2016 [S10] | Weak measurements on photons, post-selected on position | Average trajectories of an ensemble; for entangled pairs they depend on the distant photon | Nothing: the method is operational | Pilot-wave theory, which predicts the same data; single trajectories are not observed |
| Hensen et al. [S88], Giustina et al. [S89], Shalm et al. [S65], all 2015 | Bell tests closing the detection and locality loopholes together, on electron spins 1.3 km apart and on photons | S = 2.42 ± 0.20 in 245 trials, p = 0.039; p ≤ 3.74 × 10⁻³¹; p as small as 5.9 × 10⁻⁹, 2.3 × 10⁻⁷ allowing for predictable settings | Local realism, given statistical independence | Nonlocal deterministic theories, Everett, superdeterminism [S1] |
| Handsteiner et al. 2017 [S90]; Rauch et al. 2018 [S91] | Bell tests with settings from the colour of starlight, then quasar light | ≳ 7.31σ and ≳ 11.93σ; 9.3 standard deviations | A local mechanism acting later than ∼600 years ago; then ∼7.8 Gyr ago, 96% of the space-time volume of the past light cone | The other 4.0%; a correlation set by the initial conditions of the universe [S92] |
| BIG Bell Test 2018 [S93] | 13 tests of local realism with settings from 97,347,490 human choices | Conclusion conditional (next cell) | A common past influence on settings and outcomes, "if human choices are free" | Superdeterminism, which the authors say "cannot be tested" |
| Donadi et al. 2021 [S62]; Carlesso et al. 2022 [S63] | Radiation from an underground germanium detector | No excess; bounds in section 4.6 | The parameter-free Diósi–Penrose model | Collapse models with free parameters |

The freedom-of-choice experiments move a local explanation of the setting correlations back in time, and no further: they exclude a local-realist mechanism acting more recently than about 600 years ago, then about 7.8 Gyr ago, assuming fair sampling and photon colours set at emission and unaltered in flight [S90][S91]. They do not exclude superdeterminism in which the correlation comes from the initial conditions of the universe [S92]. Hossenfelder and Palmer state that such experiments "do not – cannot – rule out Superdeterminism; they merely rule out that the observed correlations in Bell-type tests were locally caused by events in the distant past" [S47]. Two of the teams above call superdeterminism untestable [S65][S93]; its proponents propose the test in section 4.3 [S52].

Public summaries sometimes drop the word "local": the 2022 Nobel press release says quantum mechanics "cannot be replaced by a theory that uses hidden variables" [S94], where the committee's scientific background says "local hidden variables" [S6].

## 6. Fields and particles

A field-first reading has support inside quantum field theory, and it is a separate question from determinism: Hobson's all-fields account keeps collapse, random outcomes and nonlocality [S18][S95].

The support is the pair of arguments against particles in section 2 [S19][S20]; Hobson adds that unbounded fields are fundamental and particles are epiphenomena arising from fields [S95]. The dissent is also in section 2, and Sassoli de Bianchi adds that quantum "fields" are no more fields than quantum "particles" are particles [S96].

Any field account must reproduce discrete detection events: antibunching is "understandable only in terms of a quantized electromagnetic field" [S71], and the anticorrelation at a beam splitter contradicts "any classical wave model of light" [S68]. Shot noise is a consequence of the quantization of charge [S97]. An interference pattern builds up from single electrons [S74]. Hobson's account gets the discrete event from collapse of the field on interaction [S95]; Halvorson and Clifton argue that field theory can explain "particle detections" without particles [S19].

Among the programs in section 4, the field version of pilot-wave theory is field-first by construction and so far works for bosonic fields only [S40]. Everett's basic object is the wave function [S33], and the cellular automaton's is a set of basis states [S34]; neither takes particles as basic. The particle version of pilot-wave theory and Nelson's stochastic mechanics are particle-first [S11][S56].

## 7. Where this project stands

The catalog is neutral on determinism, the magnet family touches the question at a few points, and the premise has a price that the project has not yet named.

### 7.1 Why the catalog cannot bear on the question

The library holds 60 condensed-matter effects: mirrors, magnets, superconductors, thresholds and thermal averages ([library/INDEX.md](library/INDEX.md)). Every one is an ensemble average, a threshold or a static state. For such quantities the standard theory's prediction is a fixed function of the parameters, and every program in section 4 that reproduces the quantum statistics reproduces all of them.

Of the 457 extracted implications, 133 are relabels (a handbook number under a project name), 242 are envelopes (a class or an inequality), 77 are open (a specification with no number) and 5 involve a computation. All 14 closure requirements, the places where a machine model would have to produce a number, are open. A relabeling of handbook data is consistent with the handbook by construction. The library is therefore neutral: it is not evidence for the premise, and it is not evidence against it.

### 7.2 Where the magnet family touches the question

Two kinds of randomness appear in magnets, and only the second is at issue.

The first is thermal. Wernsdorfer et al. measured the magnetization of individual ferromagnetic nanoparticles (15–30 nm) at 0.1–6 K; the waiting times, switching fields and telegraph noise agree with thermal activation over a single energy barrier, as proposed by Néel and Brown, with an activation volume close to the particle volume [S98]. The random waiting times are fully accounted for by thermal activation over one barrier, and on every account that randomness is ignorance of the microstate of the heat bath. It fits the premise at no cost, and it proves nothing. Both kinds are filed in [library/superparamagnetism.md](library/superparamagnetism.md).

The second is quantum. In the molecular magnet Mn12 (spin S = 10), steps in the hysteresis loop occur every 0.46 T and are attributed to thermally assisted resonant tunneling between quantum spin states; the blocking temperature is about 3 K, and relaxation is Arrhenius down to 2.1 K [S99]. For tunneling of the magnetization the standard theory assigns only a rate. This is the kind of randomness the premise has to account for.

The Landauer measurement puts a rigorous floor under the project's accounting, in which holding a state is free and writing one costs energy. An irreversible single-bit operation dissipates at least k_B T ln 2, which is 2.8 zJ at 300 K [S100]. On Permalloy nanomagnets under 100 nm, Hong et al. measured (6.09 ± 1.43) zJ = (1.45 ± 0.35) k_B T averaged over five trials at 300 K, and (4.2 ± 0.9) zJ in one set of runs; the authors describe the result as consistent with the limit within two standard deviations of experimental uncertainty [S100]. The paper notes that single-domain dots of more than 10⁴ spins can behave as a system with a single informational degree of freedom [S100]. That remark is the closest thing in the literature to what the project calls a latch cell, and it is independent of interpretation.

Two bounds give exact meaning to "clock rate" and "finite number of states". The number of mutually orthogonal states a system can pass through per unit time is bounded by its average energy above the ground state [S101]. The entropy-to-energy ratio of a bounded system of effective radius R is at most 2πR/ħc [S102]. Both hold in standard quantum mechanics and neither implies determinism; they are where the project's finite-state-machine vocabulary could be made exact.

The Minev experiment narrows what "random" refers to and does not remove it. In a superconducting artificial atom a quantum jump was caught and reversed mid-flight [S103]. The abstract states that "the jump evolution when completed is continuous, coherent, and deterministic", and that monitoring an auxiliary level shows whether a jump is about to occur [S103]. The experiment anticipates a jump that is already under way; it does not predict when one will begin [S103].

### 7.3 What the premise commits the project to

The premise has a price, and the project has not said which one it pays. Taking the Bell-test results as facts, a deterministic account has to give up at least one of locality, single outcomes or statistical independence. The project's wording, finite-state machines and randomness as incomplete knowledge, sits closest to the cellular-automaton program, or to pilot-wave theory, where randomness comes from an unknown initial configuration. The project's preference for field descriptions is compatible with Everett, with field-ontology pilot-wave theory and with the cellular automaton. Among the deterministic programs it is in tension only with particle-ontology pilot-wave theory. For a catalog, leaving the price unnamed is acceptable. For any claim about determinism it is not.

### 7.4 What would make the project relevant

The project becomes relevant when single events and their statistics are the observable. That calls for a new family of effects: Bell correlations, single-quantum build-up of interference, decay-time statistics, shot noise and anti-bunching, quantum jumps, and magnetization tunneling. In each entry the mapping section must state what each deterministic program says the hidden state is. The next step is to file the experiments that separate programs: collapse-model bounds, searches for quantum non-equilibrium, and the proposed tests of superdeterminism.

### 7.5 What not to claim

Four claims are not supported and should not be made.

- That the library's internal consistency supports the premise (section 7.1).
- That determinism implies predictability (section 1).
- That Bell tests refute determinism. They refute local hidden variables, given statistical independence (sections 3 and 5).
- That arguments about free will bear on the physics (section 8).

## 8. A note on free will

Arguments about free will do not settle anything in the physics [S47][S92]. Compatibilism is the thesis that free will is compatible with determinism [S104]; in the 2020 PhilPapers Survey 59.16% of respondents accepted or leaned towards it, 18.83% towards libertarianism and 11.21% towards no free will (N = 1758) [S105].

"Free choice" in Bell-type theorems is a statistical-independence assumption [S1]. The BIG Bell Test authors write that a more accurate term "might be 'measurement setting/hidden-variable independence'", and that the condition "can be false even if the choices are fully free" [S93]. Bell held that the output of a deterministic random generator is "a sufficiently free variable for the purpose at hand" [S1]. Hossenfelder and Palmer, who defend superdeterminism, call the free-will objection "a red herring" [S47]; Sen and Valentini, who criticise it, call the objection "incorrect" [S92]. The free will theorem is the exception: its premise is that the choice is not a function of the past, and a determinist does not grant it [S26].

## 9. Sources

Format and the meaning of the Checked column: [library/README.md](library/README.md#sourcing-standard). Rows marked "Secondary" are encyclopedia or review entries that were opened and read; `cited-only` rows were not opened and are described through an opened source.

| Key | Reference | Checked | Supports |
|---|---|---|---|
| S1 | [Myrvold, Genovese and Shimony, "Bell's Theorem", *Stanford Encyclopedia of Philosophy* (rev. 2024)](https://plato.stanford.edu/entries/bell-theorem/) | full-text | Secondary. Names of the independence assumption; the three options after a violation; the Shimony–Horne–Clauser objection; Bell on deterministic random generators; context for Scheidl et al. |
| S2 | [Hoefer, "Causal Determinism", *Stanford Encyclopedia of Philosophy* (rev. 2023)](https://plato.stanford.edu/entries/determinism-causal/) | full-text | Secondary. Determinism and predictability are separate; determinism of quantum mechanics depends on interpretation; a deterministic rival can be empirically equivalent; status of the Bohmian field-theory extension. |
| S3 | [Myrvold, "Philosophical Issues in Quantum Theory", *Stanford Encyclopedia of Philosophy* (rev. 2022)](https://plato.stanford.edu/entries/qt-issues/) | full-text | Secondary. The Schrödinger equation is deterministic and linear. |
| S4 | [Held, "The Kochen-Specker Theorem", *Stanford Encyclopedia of Philosophy* (rev. 2022)](https://plato.stanford.edu/entries/kochen-specker/) | full-text | Secondary. Value definiteness and noncontextuality; the theorem's conclusion; contextual hidden variables are not excluded. |
| S5 | [Bell, *Physics Physique Fizika* 1, 195 (1964)](https://doi.org/10.1103/PhysicsPhysiqueFizika.1.195) | abstract | Locality requirement; local hidden variables cannot reproduce the quantum predictions. |
| S6 | [Nobel Committee for Physics, "Scientific Background on the Nobel Prize in Physics 2022" (2022)](https://www.nobelprize.org/uploads/2026/05/advanced-physicsprize-2022-5.pdf) | full-text | Pilot-wave theory is deterministic and nonlocal; Bohm and Everett make no differing predictions; six standard deviations and loopholes of the early Bell tests; the wording "local hidden variables". |
| S7 | [Brunner et al., *Rev. Mod. Phys.* 86, 419 (2014), arXiv:1303.2849](https://arxiv.org/abs/1303.2849) | full-text | Locality condition contains no determinism assumption; S ≤ 2 and the Tsirelson bound 2√2; every model has a deterministic equivalent; nonlocal deterministic models are signalling. |
| S8 | [Lorenz, *J. Atmos. Sci.* 20, 130 (1963)](https://doi.org/10.1175/1520-0469%281963%29020%3C0130%3ADNF%3E2.0.CO%3B2) | abstract | Slightly differing initial states of a deterministic system evolve into considerably different states. |
| S9 | [Bishop, "Chaos", *Stanford Encyclopedia of Philosophy* (rev. 2024)](https://plato.stanford.edu/entries/chaos/) | full-text | Secondary. Chaotic behaviour is deterministic; determinism is not predictability. |
| S10 | [Mahler et al., *Sci. Adv.* 2, e1501466 (2016)](https://doi.org/10.1126/sciadv.1501466) | full-text | Average trajectories that depend on a distant photon; Bohmian randomness as ignorance of the initial configuration; single trajectories unobservable; same predictions as the standard theory. |
| S11 | [Dürr, Goldstein and Zanghì, *J. Stat. Phys.* 67, 843 (1992), arXiv:quant-ph/0308039](https://arxiv.org/abs/quant-ph/0308039) | abstract | Bohmian mechanics as a deterministic theory of particles in which an appearance of randomness emerges. |
| S12 | [Colbeck and Renner, *Nature Commun.* 2, 411 (2011), arXiv:1005.5173](https://arxiv.org/abs/1005.5173) | full-text | No extension of quantum theory improves prediction under free choice defined by light cones; de Broglie–Bohm theory violates that definition. |
| S13 | [Schlosshauer, *Phys. Rep.* 831, 1 (2019), arXiv:1911.06282](https://arxiv.org/abs/1911.06282) | full-text | Statement of the measurement problem; decoherence presumes the collapse postulate and Born's rule. |
| S14 | [Ghirardi and Bassi, "Collapse Theories", *Stanford Encyclopedia of Philosophy* (rev. 2025)](https://plato.stanford.edu/entries/qm-collapse/) | full-text | Secondary. Wave-packet reduction is nonlinear and stochastic; Adler's proposed collapse rate is experimentally falsified. |
| S15 | [Zurek, *Rev. Mod. Phys.* 75, 715 (2003), arXiv:quant-ph/0105127](https://arxiv.org/abs/quant-ph/0105127) | abstract | Decoherence: the environment destroys interference between pointer states. |
| S16 | [Schlosshauer, *Rev. Mod. Phys.* 76, 1267 (2004), arXiv:quant-ph/0312059](https://arxiv.org/abs/quant-ph/0312059) | full-text | Decoherence explains suppressed interference and the preferred basis; the superposition persists in the larger system. |
| S17 | [Bush and Oza, *Rep. Prog. Phys.* 84, 017001 (2021)](https://doi.org/10.1088/1361-6633/abc22c) | abstract | A particle as an excitation of a field is a common notion in quantum field theory. |
| S18 | [Kuhlmann, "Quantum Field Theory", *Stanford Encyclopedia of Philosophy* (rev. 2026)](https://plato.stanford.edu/entries/quantum-field-theory/) | full-text | Secondary. Field interpretation as the usual ontology; operator-valued fields; Baker's objection. |
| S19 | [Halvorson and Clifton, *Philos. Sci.* 69, 1 (2002), arXiv:quant-ph/0103041](https://arxiv.org/abs/quant-ph/0103041) | abstract | No-go theorem against localizable particles; field theory can still explain particle detections. |
| S20 | [Fraser, *Stud. Hist. Phil. Mod. Phys.* 39, 841 (2008)](https://doi.org/10.1016/j.shpsb.2008.05.003) | abstract | An interacting system cannot be interpreted in terms of particles. |
| S21 | [Baker, *Brit. J. Phil. Sci.* 60, 585 (2009)](https://doi.org/10.1093/bjps/axp027) | abstract | Dissent: the arguments against particles also undermine the wave-functional field interpretation. |
| S22 | [Goldstein, "Bohmian Mechanics", *Stanford Encyclopedia of Philosophy* (rev. 2025)](https://plato.stanford.edu/entries/qm-bohm/) | full-text | Secondary, written by a proponent. Bell did not rule out a deterministic reformulation; coverage of nonrelativistic phenomena; Bell's remark on Bohm; doubt about quantum non-equilibrium. |
| S23 | [Clauser, Horne, Shimony and Holt, *Phys. Rev. Lett.* 23, 880 (1969)](https://doi.org/10.1103/PhysRevLett.23.880) | abstract | CHSH form of Bell's theorem for realizable experiments. |
| S24 | [Kochen and Specker, *J. Math. Mech.* 17, 59 (1967)](https://doi.org/10.1512/iumj.1968.17.17004) | cited-only | Original contextuality theorem; its content here is taken from the encyclopedia entry by Held. |
| S25 | [Conway and Kochen, *Found. Phys.* 36, 1441 (2006), arXiv:quant-ph/0604079](https://arxiv.org/abs/quant-ph/0604079) | full-text | Free will theorem: axioms SPIN, TWIN, FIN and the conditional conclusion. |
| S26 | [Conway and Kochen, "The Strong Free Will Theorem", arXiv:0807.3286 (2008)](https://arxiv.org/abs/0807.3286) | full-text | Axiom MIN; a free choice defined as one that is not a function of the past. |
| S27 | [Pusey, Barrett and Rudolph, *Nature Phys.* 8, 475 (2012), arXiv:1111.3328](https://arxiv.org/abs/1111.3328) | full-text | Assumptions and conclusion of the theorem on the reality of the quantum state; determinism is not assumed. |
| S28 | [Leggett, *Found. Phys.* 33, 1469 (2003)](https://doi.org/10.1023/A:1026096313729) | cited-only | Original incompatibility theorem for a class of nonlocal hidden-variable theories; its content here is taken from Gröblacher et al. |
| S29 | [Gröblacher et al., *Nature* 446, 871 (2007), arXiv:0704.2529](https://arxiv.org/abs/0704.2529) | full-text | Assumptions of the tested nonlocal realistic class; violation of the Leggett-type inequality; Bohm's theory lies outside the class. |
| S30 | [Leggett and Garg, *Phys. Rev. Lett.* 54, 857 (1985)](https://doi.org/10.1103/PhysRevLett.54.857) | abstract | Quantum mechanics against macroscopic realism plus noninvasive measurability. |
| S31 | [Emary, Lambert and Nori, *Rep. Prog. Phys.* 77, 016001 (2014), arXiv:1304.5133](https://arxiv.org/abs/1304.5133) | full-text | Statement of the two Leggett–Garg assumptions; meaning of a violation; the clumsiness loophole. |
| S32 | [Wiseman, *J. Phys. A* 47, 424001 (2014), arXiv:1402.0351](https://arxiv.org/abs/1402.0351) | full-text | Bell's 1964 and 1976 theorems, and which assumption each camp gives up. |
| S33 | [Vaidman, "Many-Worlds Interpretation of Quantum Mechanics", *Stanford Encyclopedia of Philosophy* (rev. 2026)](https://plato.stanford.edu/entries/qm-manyworlds/) | full-text | Secondary, written by a proponent. Determinism of the theory; the probability problem; opposition to the Born-rule derivations. |
| S34 | ['t Hooft, *The Cellular Automaton Interpretation of Quantum Mechanics* (Springer, 2016), arXiv:1405.1548](https://arxiv.org/abs/1405.1548) | full-text | The cellular-automaton proposal; superdeterminism; no ontological basis for the Standard Model yet; toy models only. |
| S35 | [Vitenti, Peter and Valentini, *Phys. Rev. D* 100, 043506 (2019), arXiv:1901.08885](https://arxiv.org/abs/1901.08885) | full-text | Fit of a quantum-relaxation spectrum to Planck data: 2–3σ, weaker with polarization, statistically inconclusive. |
| S36 | [Bassi et al., *Rev. Mod. Phys.* 85, 471 (2013), arXiv:1204.4325](https://arxiv.org/abs/1204.4325) | abstract | Continuous spontaneous collapse as a stochastic, nonlinear and falsifiable modification of the Schrödinger equation. |
| S37 | [Bohm, *Phys. Rev.* 85, 166 (1952)](https://doi.org/10.1103/PhysRev.85.166) | abstract | Hidden-variable interpretation gives the same results as the usual one; an objective description of individual systems is possible. |
| S38 | [Valentini and Westman, *Proc. R. Soc. A* 461, 253 (2005), arXiv:quant-ph/0403034](https://arxiv.org/abs/quant-ph/0403034) | abstract | Simulated relaxation of a non-standard ensemble toward the quantum distribution. |
| S39 | [Dürr et al., *Proc. R. Soc. A* 470, 20130699 (2014), arXiv:1307.1714](https://arxiv.org/abs/1307.1714) | abstract | Relativistic Bohmian theories use a privileged foliation of space-time. |
| S40 | [Struyve, *J. Phys.: Conf. Ser.* 306, 012047 (2011), arXiv:1101.5819](https://arxiv.org/abs/1101.5819) | full-text | Field and particle versions of pilot-wave field theory: bosons, fermions, which versions are stochastic, absence of fundamental Lorentz invariance. |
| S41 | [Valentini, *Phys. Rev. D* 82, 063513 (2010), arXiv:0805.0163](https://arxiv.org/abs/0805.0163) | abstract | Quantum non-equilibrium would give anomalous spectra in the cosmic microwave background. |
| S42 | [Everett, *Rev. Mod. Phys.* 29, 454 (1957)](https://doi.org/10.1103/RevModPhys.29.454) | abstract | Aim of the relative-state formulation. |
| S43 | [Deutsch, *Proc. R. Soc. Lond. A* 455, 3129 (1999), arXiv:quant-ph/9906015](https://arxiv.org/abs/quant-ph/9906015) | abstract | Decision-theoretic derivation of quantum probabilities. |
| S44 | [Wallace, "A formal proof of the Born rule from decision-theoretic assumptions", arXiv:0906.2718 (2009)](https://arxiv.org/abs/0906.2718) | abstract | Formal version of the decision-theoretic Born-rule proof. |
| S45 | [Sebens and Carroll, *Brit. J. Phil. Sci.* 69, 25 (2018), arXiv:1405.7577](https://arxiv.org/abs/1405.7577) | abstract | Born rule from self-locating uncertainty. |
| S46 | [Kent, "One world versus many", in *Many Worlds? Everett, Quantum Theory, and Reality* (2010), arXiv:0905.0624](https://arxiv.org/abs/0905.0624) | abstract | Criticism: no known Everettian version accounts for the appearance of probabilities. |
| S47 | [Hossenfelder and Palmer, *Front. Phys.* 8, 139 (2020), arXiv:1912.06462](https://arxiv.org/abs/1912.06462) | full-text | Definition and defence of superdeterminism; free will as a red herring; what cosmic Bell tests rule out; the proposed test and its limit. |
| S48 | [Hall, *Phys. Rev. Lett.* 105, 250404 (2010), arXiv:1007.5518](https://arxiv.org/abs/1007.5518) | abstract | Singlet correlations modelled by giving up 14% of measurement independence. |
| S49 | [Sen and Valentini, *Proc. R. Soc. A* 476, 20200214 (2020), arXiv:2003.12195](https://arxiv.org/abs/2003.12195) | abstract | Superdeterministic models need a finely tuned hidden-variable distribution; nonlocal and retrocausal models do not. |
| S50 | [Baas and Le Bihan, "What does the world look like according to superdeterminism?", arXiv:2009.13908 (2020)](https://arxiv.org/abs/2009.13908) | full-text | Criticism: global failure of statistical independence; holism. |
| S51 | [Chen, "Bell's Theorem, Quantum Probabilities, and Superdeterminism", arXiv:2006.08609 (2020)](https://arxiv.org/abs/2006.08609) | full-text | Observational equivalence with Bohmian mechanics; simplicity argument; credence should not be zero. |
| S52 | [Hossenfelder, *Found. Phys.* 41, 1521 (2011), arXiv:1105.4326](https://arxiv.org/abs/1105.4326) | abstract | Proposed test: correlated outcomes in repeated measurements of non-commuting observables. |
| S53 | [Wharton and Argaman, *Rev. Mod. Phys.* 92, 021002 (2020), arXiv:1906.04313](https://arxiv.org/abs/1906.04313) | full-text | Locally mediated models with parameters that depend on future settings; toy-model status; the open treatment of measurement. |
| S54 | [Friederich and Evans, "Retrocausality in Quantum Mechanics", *Stanford Encyclopedia of Philosophy* (rev. 2023)](https://plato.stanford.edu/entries/qm-retrocausality/) | full-text | Secondary. Retrocausality as a second way to violate measurement independence; the objection that it is superdeterminism renamed, and the reply. |
| S55 | [Nieuwenhuizen and Liska, *Phys. Scr.* T165, 014006 (2015), arXiv:1502.06856](https://arxiv.org/abs/1502.06856) | abstract | Simulated hydrogen atom in stochastic electrodynamics ionises at longer times. |
| S56 | [Nelson, *Phys. Rev.* 150, 1079 (1966)](https://doi.org/10.1103/PhysRev.150.1079) | abstract | Schrödinger equation from particles in Brownian motion with continuous trajectories. |
| S57 | [Boyer, *Atoms* 7, 29 (2019), arXiv:1903.00996](https://arxiv.org/abs/1903.00996) | full-text | Proponent review of stochastic electrodynamics: definition, agreement for harmonic oscillators, dispute over hydrogen. |
| S58 | [Nieuwenhuizen and Liska, *Found. Phys.* 45, 1190 (2015), arXiv:1506.06787](https://arxiv.org/abs/1506.06787) | abstract | Relativistic corrections do not remove the self-ionisation. |
| S59 | [Wallstrom, *Phys. Rev. A* 49, 1613 (1994)](https://doi.org/10.1103/PhysRevA.49.1613) | abstract | A quantization condition must be added by hand to recover the Schrödinger equation. |
| S60 | [Nelson, *J. Phys.: Conf. Ser.* 361, 012011 (2012)](https://doi.org/10.1088/1742-6596/361/1/012011) | full-text | Stochastic mechanics is nonlocal and can give wrong predictions for measurements at two times. |
| S61 | [Ghirardi, Rimini and Weber, *Phys. Rev. D* 34, 470 (1986)](https://doi.org/10.1103/PhysRevD.34.470) | abstract | Modified dynamics giving quantum behaviour for microscopic and classical behaviour for macroscopic objects. |
| S62 | [Donadi et al., *Nature Phys.* 17, 74 (2021), arXiv:2111.13490](https://arxiv.org/abs/2111.13490) | full-text | Gran Sasso bound on R₀; parameter-free Diósi–Penrose model ruled out; free-parameter versions remain. |
| S63 | [Carlesso et al., *Nature Phys.* 18, 243 (2022), arXiv:2203.04231](https://arxiv.org/abs/2203.04231) | full-text | Bound on the collapse rate λ at r_C = 10⁻⁷ m; the rates proposed by Ghirardi, Rimini and Weber and by Adler. |
| S64 | [Fein et al., *Nature Phys.* 15, 1242 (2019)](https://doi.org/10.1038/s41567-019-0663-9) | abstract | Interference of molecules beyond 25,000 Da at more than 90% of the expected visibility; no classical explanation; bounds on collapse models. |
| S65 | [Shalm et al., *Phys. Rev. Lett.* 115, 250402 (2015), arXiv:1511.03189](https://arxiv.org/abs/1511.03189) | full-text | Loophole-free photon test: p-values with and without predictable settings; superdeterminism called untestable; exclusion of local hidden variables. |
| S66 | [Kirchmair et al., *Nature* 460, 494 (2009), arXiv:0904.1655](https://arxiv.org/abs/0904.1655) | abstract | Trapped-ion violation of noncontextuality for arbitrary states, without the detection loophole. |
| S67 | [Knee et al., *Nature Commun.* 7, 13253 (2016), arXiv:1601.03728](https://arxiv.org/abs/1601.03728) | abstract | Flux-qubit test: about 84 standard deviations, 170 nA currents over about 10 ns, control experiments for the clumsiness loophole. |
| S68 | [Grangier, Roger and Aspect, *Europhys. Lett.* 1, 173 (1986)](https://doi.org/10.1209/0295-5075/1/4/004) | abstract | Anticorrelation at a beam splitter contradicts any classical wave model of light; interference visibility over 98% with the same source. |
| S69 | [Freedman and Clauser, *Phys. Rev. Lett.* 28, 938 (1972)](https://doi.org/10.1103/PhysRevLett.28.938) | abstract | First Bell test: polarization correlation of calcium-cascade photons. |
| S70 | [Aspect, Dalibard and Roger, *Phys. Rev. Lett.* 49, 1804 (1982)](https://doi.org/10.1103/PhysRevLett.49.1804) | abstract | Bell test with analyzers switched near 50 MHz; violation by 5 standard deviations. |
| S71 | [Kimble, Dagenais and Mandel, *Phys. Rev. Lett.* 39, 691 (1977)](https://doi.org/10.1103/PhysRevLett.39.691) | abstract | Photon antibunching requires a quantized electromagnetic field. |
| S72 | [Norman, Gazes, Crane and Bennett, *Phys. Rev. Lett.* 60, 2246 (1988)](https://doi.org/10.1103/PhysRevLett.60.2246) | abstract | Exponential decay law holds for ⁶⁰Co and ⁵⁶Mn over the ranges tested. |
| S73 | [Wilkinson et al., *Nature* 387, 575 (1997)](https://www.nature.com/articles/42418) | abstract | Short-time deviation from exponential decay in tunnelling, as quantum mechanics predicts. |
| S74 | [Tonomura et al., *Am. J. Phys.* 57, 117 (1989)](https://doi.org/10.1119/1.16104) | abstract | Build-up of an interference pattern from single electrons. |
| S75 | [Oberholzer, Sukhorukov and Schönenberger, *Nature* 415, 765 (2002)](https://doi.org/10.1038/415765a) | cited-only | Chaotic-cavity shot-noise experiment; described here through Beenakker and Schönenberger. |
| S76 | [Beenakker and Schönenberger, *Physics Today* 56(5), 37 (2003), arXiv:cond-mat/0605025](https://arxiv.org/abs/cond-mat/0605025) | full-text | Chaotic-cavity shot noise: Fano factor 1/4 at long dwell times and its reduction at short ones; deterministic particle scattering is noiseless, wave scattering noisy. |
| S77 | [Berkeland, Raymondson and Tassin, *Phys. Rev. A* 69, 052103 (2004), arXiv:physics/0304013](https://arxiv.org/abs/physics/0304013) | abstract | 228,000 quantum jumps of one ion show no correlations; entropy-reduction bound. |
| S78 | [Couder and Fort, *Phys. Rev. Lett.* 97, 154101 (2006)](https://doi.org/10.1103/PhysRevLett.97.154101) | abstract | Reported diffraction and interference histograms for walking droplets. |
| S79 | [Andersen et al., *Phys. Rev. E* 92, 013006 (2015)](https://doi.org/10.1103/PhysRevE.92.013006) | abstract | Droplet double slit differs from quantum single-particle statistics; orbital quantization is captured. |
| S80 | [Pucci, Harris, Faria and Bush, *J. Fluid Mech.* 835, 1136 (2018)](https://doi.org/10.1017/jfm.2017.790) | abstract | Wall effect dominates droplet slit experiments; dependence of peak number on slit width not recovered. |
| S81 | [Jacques et al., *Science* 315, 966 (2007), arXiv:quant-ph/0610241](https://arxiv.org/abs/quant-ph/0610241) | abstract | Delayed-choice experiment with single photons: visibility 94%, path error below 1%. |
| S82 | [Palacios-Laloy et al., *Nature Phys.* 6, 442 (2010), arXiv:1005.3435](https://arxiv.org/abs/1005.3435) | abstract | Leggett–Garg violation by 5 standard deviations in a superconducting circuit. |
| S83 | [Knee et al., *Nature Commun.* 3, 606 (2012), arXiv:1104.0238](https://arxiv.org/abs/1104.0238) | abstract | Leggett–Garg violation with phosphorus spins in silicon. |
| S84 | [Scheidl et al., *Proc. Natl. Acad. Sci. USA* 107, 19708 (2010), arXiv:0811.3129](https://arxiv.org/abs/0811.3129) | abstract | Bell test with freedom of choice; the loopholes close only within non-determinism. |
| S85 | [Pironio et al., *Nature* 464, 1021 (2010), arXiv:0911.3427](https://arxiv.org/abs/0911.3427) | full-text | 42 new random numbers certified at 99% confidence. |
| S86 | [Bierhorst et al., *Nature* 556, 223 (2018), arXiv:1803.06219](https://arxiv.org/abs/1803.06219) | abstract | 1024 certified random bits and the two conditions under which they are unpredictable. |
| S87 | [Kocsis et al., *Science* 332, 1170 (2011)](https://doi.org/10.1126/science.1202218) | abstract | Weak-measurement average trajectories of single photons, defined for an ensemble. |
| S88 | [Hensen et al., *Nature* 526, 682 (2015), arXiv:1508.05949](https://arxiv.org/abs/1508.05949) | abstract | Loophole-free test with electron spins 1.3 km apart: S, number of trials, p-value. |
| S89 | [Giustina et al., *Phys. Rev. Lett.* 115, 250401 (2015), arXiv:1511.03190](https://arxiv.org/abs/1511.03190) | full-text | Loophole-free photon test: p-value. |
| S90 | [Handsteiner et al., *Phys. Rev. Lett.* 118, 060401 (2017), arXiv:1611.06985](https://arxiv.org/abs/1611.06985) | full-text | Cosmic Bell test with Milky Way stars: significance, assumptions, the 600-year limit. |
| S91 | [Rauch et al., *Phys. Rev. Lett.* 121, 080403 (2018), arXiv:1808.05966](https://arxiv.org/abs/1808.05966) | full-text | Cosmic Bell test with quasars: significance, assumptions, 7.8 Gyr, 96% and 4.0% of the past light cone. |
| S92 | [Sen and Valentini, *Proc. R. Soc. A* 476, 20200212 (2020), arXiv:2003.11989](https://arxiv.org/abs/2003.11989) | full-text | The free-will criticism of superdeterminism is incorrect; cosmic Bell tests do not constrain models whose correlation comes from the initial conditions of the universe. |
| S93 | [BIG Bell Test Collaboration, *Nature* 557, 212 (2018), arXiv:1805.04431](https://arxiv.org/abs/1805.04431) | full-text | Human-choice Bell tests: number of choices and experiments; the condition "if human choices are free"; the independence assumption renamed; superdeterminism called untestable. |
| S94 | [Royal Swedish Academy of Sciences, press release, Nobel Prize in Physics 2022 (4 October 2022)](https://www.nobelprize.org/prizes/physics/2022/press-release/) | full-text | The press-release sentence about hidden variables that omits the word "local". |
| S95 | [Hobson, *Am. J. Phys.* 81, 211 (2013), arXiv:1204.4616](https://arxiv.org/abs/1204.4616) | full-text | All-fields view; it keeps collapse on interaction, random outcomes and nonlocality. |
| S96 | [Sassoli de Bianchi, *Am. J. Phys.* 81, 707 (2013), arXiv:1204.6384](https://arxiv.org/abs/1204.6384) | abstract | Dissent: quantum fields are no more fields than quantum particles are particles. |
| S97 | [Blanter and Büttiker, *Phys. Rep.* 336, 1 (2000), arXiv:cond-mat/9910158](https://arxiv.org/abs/cond-mat/9910158) | abstract | Shot noise is a consequence of the quantization of charge. |
| S98 | [Wernsdorfer et al., *Phys. Rev. Lett.* 78, 1791 (1997)](https://doi.org/10.1103/PhysRevLett.78.1791) | abstract | Switching of single 15–30 nm nanoparticles at 0.1–6 K agrees with thermal activation over one barrier; activation volume close to the particle volume. |
| S99 | [Friedman, Sarachik, Tejada, Maciejewski and Ziolo, *J. Appl. Phys.* 79, 6031 (1996)](https://jrfriedman.people.amherst.edu/Mn12_steps_JAP.pdf) | full-text | Mn12 hysteresis steps every 0.46 T attributed to thermally assisted resonant tunneling; blocking temperature about 3 K; Arrhenius relaxation to 2.1 K. |
| S100 | [Hong, Lambson, Dhuey and Bokor, *Sci. Adv.* 2, e1501492 (2016)](https://escholarship.org/uc/item/5fm3w6xx) | full-text | Landauer limit of 2.8 zJ at 300 K; measured dissipation on Permalloy nanomagnets; more than 10⁴ spins acting as one informational degree of freedom. |
| S101 | [Margolus and Levitin, *Physica D* 120, 188 (1998), arXiv:quant-ph/9710043](https://arxiv.org/abs/quant-ph/9710043) | abstract | Bound on the number of orthogonal states passed through per unit time, set by the average energy above the ground state. |
| S102 | [Bekenstein, *Phys. Rev. D* 23, 287 (1981)](https://doi.org/10.1103/PhysRevD.23.287) | abstract | Entropy-to-energy ratio of a bounded system of effective radius R is at most 2πR/ħc. |
| S103 | [Minev et al., *Nature* 570, 200 (2019), arXiv:1803.00545](https://arxiv.org/abs/1803.00545) | abstract | A quantum jump caught and reversed mid-flight; completed jump evolution continuous, coherent and deterministic; monitoring shows whether a jump is about to occur. |
| S104 | [McKenna and Coates, "Compatibilism", *Stanford Encyclopedia of Philosophy* (rev. 2024)](https://plato.stanford.edu/entries/compatibilism/) | full-text | Secondary. Definition of compatibilism. |
| S105 | [Bourget and Chalmers, 2020 PhilPapers Survey, results page](https://survey2020.philpeople.org/survey/results/all) | full-text | Survey shares for compatibilism, libertarianism and no free will; N = 1758. |
