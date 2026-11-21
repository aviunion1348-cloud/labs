"""Chapter 12 - Examination simulation: three complete mock papers with mark schemes."""
from common import checklist

B = []

B += [
    ("h2", "12.1  How to use these papers"),
    ("lead", "Knowing an experiment and being able to perform under examination conditions are different "
             "competences. This chapter supplies three complete papers built from the eleven activities in this "
             "volume, with full mark schemes, so that you can rehearse the examination itself rather than only the "
             "content."),
    ("p", "The papers are deliberately structured like the real thing: **Paper 1** tests theory and understanding, "
          "**Paper 2** tests calculation and data handling, and **Paper 3** tests oral fluency under rapid "
          "questioning. Each carries a time allowance and a mark allocation. Attempt each paper closed-book, mark it "
          "honestly with the scheme provided, and only then reread the relevant chapter section."),
    ("tbl", ["Paper", "Content", "Time", "Marks", "What it diagnoses"],
     [["Paper 1", "Theory and short answer, all eleven activities", "90 min", "100",
       "Conceptual gaps and missing derivations"],
      ["Paper 2", "Numerical problems with worked mark schemes", "75 min", "100",
       "Arithmetic, unit handling, and misinterpretation of data"],
      ["Paper 3", "Rapid-fire viva, 60 questions", "45 min", "60",
       "Fluency, precision of language, and the ability to answer in one sentence"]],
     [22, 62, 22, 20, 44], "**Table 12.1** The three papers. Do them in order and on separate days; the value comes "
                           "from the interval between attempt and review.", ["l", "l", "c", "c", "l"]),
    ("box", "exam", [
        "**Mark yourself against the scheme, not against your intentions.** A point is scored only if the required "
        "idea is written down. In the real viva, an idea you have but do not say earns nothing \u2014 the same "
        "principle applies here.",
        "**Record the reason for every lost mark** in one line. After three papers you will see a pattern; that "
        "pattern is your revision list, and it is far more useful than a general reread of the book.",
        "**Do not look anything up mid-paper.** An open book destroys the diagnostic value. Note the question "
        "number and return to it afterwards.",
    ], "Rules that make the simulation worth doing"),
]

B += [
    ("h2", "12.2  Paper 1 \u2014 Theory and short answer (100 marks, 90 minutes)"),
    ("p", "Answer all questions. Section A carries 1 mark per item, Section B carries 3 marks per question, Section "
          "C carries 8 marks per question. Suggested allocation: 25 minutes on A, 30 on B, 35 on C."),
    ("h3", "Section A \u2014 One mark each (20 marks)"),
    ("qa", [
        ("State the Beer\u2013Lambert law.", "A = \u03b5lc."),
        ("What is the wavelength of maximum absorption of the cobalt(II) chloride complex used in Experiment 1?",
         "Approximately 511 nm, with a weaker band near 615 nm."),
        ("Why is a blank solution measured first in spectrophotometry?",
         "To set the zero of absorbance so that the solvent and cell contribution is subtracted."),
        ("What order of reaction does the acid-catalysed hydrolysis of an ester follow?",
         "Pseudo-first-order, because water is in large excess."),
        ("Define equivalent conductance.", "The conductance of a solution containing one equivalent of electrolyte "
                                          "placed between electrodes 1 cm apart."),
        ("Give the limiting ionic conductance of H^{+} in water.",
         "349.8 S cm^{2} mol^{\u22121}."),
        ("Why does conductance rise after the equivalence point in a strong-acid/strong-base conductometric "
         "titration?", "Because excess OH^{\u2212}, which has a very high mobility, is added."),
        ("State the formula for viscosity from the Redwood I viscometer.", "\u03bd = 0.264t \u2212 190/t cSt."),
        ("What is the difference between flash point and fire point?",
         "Flash point is a transient flash; fire point is sustained burning for at least five seconds."),
        ("Why is the Pensky\u2013Martens apparatus a closed-cup method?",
         "The vapour is retained in a covered cup, giving the lower, conservative value."),
        ("What is the equivalent weight of oxalic acid dihydrate when it is used as a primary standard?",
         "63.04 g eq^{\u22121}, since it is dibasic with molar mass 126.07."),
        ("Why is phenolphthalein unsuitable for the titration of a weak base with a strong acid?",
         "Its colour change near pH 8\u201310 does not match the acidic equivalence point."),
        ("What is the role of Eriochrome Black T in the EDTA titration?",
         "It is a metal-ion indicator that changes from wine red to blue at the endpoint."),
        ("Why is the EDTA titration buffered at pH 10?",
         "To ensure the fully deprotonated Y^{4\u2212} form dominates and the conditional constant is large."),
        ("Express hardness in terms of CaCO_{3}.",
         "Hardness (mg L^{\u22121}) = (N V \u00d7 50 \u00d7 1000)/V_{sample}."),
        ("Define total alkalinity.", "The acid volume required to reach the methyl-orange endpoint near pH 4.5."),
        ("Why can OH^{\u2212} and HCO_{3}^{\u2212} not coexist in significant amounts?",
         "They react to give CO_{3}^{2\u2212} and water."),
        ("Write the reaction of chlorine with iodide.", "Cl_{2} + 2I^{\u2212} \u2192 2Cl^{\u2212} + I_{2}."),
        ("Why is starch added only near the endpoint in iodometry?",
         "The iodine\u2013starch complex is slow to decompose at high iodine concentration, giving a sluggish "
         "endpoint."),
        ("Give the expected melting range of diazoaminobenzene.", "96\u201398 \u00b0C."),
    ], None, 1),
    ("h3", "Section B \u2014 Three marks each (45 marks)"),
    ("qa", [
        ("Explain why the absorbance of a coloured solution is measured at \u03bb_{max}.",
         "At the absorption maximum the curve is flat, so a small error in wavelength produces a small error in "
         "absorbance (1); the sensitivity is also greatest there, so the same concentration gives the largest signal "
         "(1); this improves the precision of the calibration (1)."),
        ("Derive the rate expression used in the hydrolysis experiment.",
         "For a pseudo-first-order reaction, rate = k\u2032[ester] (1); integrating gives ln([ester]_{0}/[ester]_{t}) "
         "= k\u2032t (1); converting to base-10 logarithms and expressing concentrations through the titre volumes "
         "gives k = (2.303/t) log[(V_{\u221e} \u2212 V_{0})/(V_{\u221e} \u2212 V_{t})] (1)."),
        ("Why does the conductometric titration of HCl with NaOH give a V-shaped curve?",
         "Before equivalence, H^{+} is replaced by the much less mobile Na^{+}, so conductance falls (1); after "
         "equivalence, excess OH^{\u2212} is added, and its high mobility makes conductance rise steeply (1); the "
         "minimum marks the equivalence point (1)."),
        ("Explain the purpose of the \u2212190/t term in the Redwood relation.",
         "At short efflux times the flow departs from the ideal linear relation because of kinetic-energy and "
         "surface-tension effects at the jet (1); the departure is proportionally larger when t is small, hence the "
         "inverse dependence (1); the term becomes negligible for long efflux times (1)."),
        ("State three consequences of a heating rate that is too fast in the flash-point determination.",
         "The bulk liquid lags the thermometer, so the recorded temperature is too high (1); the vapour "
         "concentration above the surface is not at equilibrium, so the flash occurs at an irreproducible "
         "temperature (1); the result is a systematic positive bias that no averaging will remove (1)."),
        ("Why must the diazotisation step be kept below 5 \u00b0C?",
         "The diazonium ion is thermally unstable and decomposes to a phenol and nitrogen (1); the decomposition is "
         "exothermic and can become violent on a larger scale (1); keeping the mixture cold preserves the ion long "
         "enough to couple, which is the point of the preparation (1)."),
        ("Distinguish iodometric from iodimetric methods.",
         "Iodometric methods determine an oxidant indirectly: the oxidant liberates iodine from iodide, and the "
         "iodine is titrated with thiosulphate (1.5); iodimetric methods titrate the analyte directly with a standard "
         "iodine solution (1.5)."),
        ("Explain why the alkalinity composition table forbids the coexistence of hydroxide and bicarbonate.",
         "Hydroxide and bicarbonate react quantitatively to form carbonate and water (1); the equilibrium lies "
         "strongly to the right, so both cannot be present in significant amounts (1); the table is therefore a "
         "partition of the possible cases, not a free choice (1)."),
        ("Describe the three-pass reading strategy for this volume and justify it.",
         "First pass: theory, read slowly with a pencil, to build understanding (1); second pass: procedure and "
         "precautions immediately before the session, because at the bench you need actions rather than history (1); "
         "third pass: errors and troubleshooting compared against what actually happened, then the viva bank aloud, "
         "because spoken recall is a different skill from silent reading (1)."),
        ("Give three reasons why a melting point alone is insufficient to identify a compound.",
         "Different compounds can have similar melting points (1); impurities depress and broaden the range, so a "
         "low value is ambiguous (1); a mixed melting point with an authentic sample, or a spectroscopic method, "
         "provides the confirmation that a single value cannot (1)."),
        ("Explain the significance of the conditional formation constant in complexometric titration.",
         "The conditional constant is the product of the absolute constant and the fraction of EDTA present as "
         "Y^{4\u2212} at that pH (1); it therefore describes the effective binding strength under real conditions (1); "
         "at pH 10 it is large enough for a sharp endpoint, while at pH 4 it is far too small (1)."),
        ("Why is the cell constant needed in conductometry?",
         "Measured conductance depends on the electrode area and separation (1); the cell constant, l/A, converts "
         "conductance into conductivity, an intensive property of the solution (1); it is determined with a standard "
         "KCl solution (1)."),
        ("State three functions of a blank determination in this volume.",
         "It corrects for reagent-derived signal, as in the iodine blank of the chlorine experiment (1); it checks "
         "reagent quality, since a large blank signals contamination (1); it establishes the zero of an instrumental "
         "scale, as with the distilled-water blank in spectrophotometry (1)."),
        ("Why does the pH of a buffer change less than that of unbuffered water on adding acid?",
         "A buffer contains a reservoir of conjugate base that consumes added H^{+} (1); the ratio of the conjugate "
         "pair changes only slightly, and pH depends logarithmically on that ratio (1); in unbuffered water the same "
         "acid amount changes [H^{+}] by orders of magnitude (1)."),
        ("Explain why the second endpoint of an alkalinity titration is recorded as a cumulative volume.",
         "The total alkalinity is defined as the acid required to reach pH 4.5 from the original sample (1); the "
         "first endpoint has already consumed acid, so that volume is part of the total (1); recording only the "
         "additional volume would understate T and misassign the species (1)."),
    ], None, 21),
    ("h3", "Section C \u2014 Eight marks each (40 marks; answer five of six)"),
    ("qa", [
        ("Discuss the design of a spectrophotometric determination from sample to reported concentration.",
         "**Choice of wavelength (2):** scan the spectrum, identify \u03bb_{max} for the species of interest, and "
         "confirm that no other component absorbs significantly there. **Calibration (3):** prepare standards "
         "spanning the expected range, measure the blank, plot absorbance against concentration, and check linearity; "
         "the slope is \u03b5l. **Measurement (2):** keep the cell and volume consistent, work within the linear "
         "absorbance range (roughly 0.1\u20131.0), and replicate. **Reporting (1):** give the concentration with its "
         "uncertainty and state whether the basis is w/v or w/w \u2014 the supplied source leaves this unresolved."),
        ("Compare conductometric and pH-metric titrations, and say when each is preferable.",
         "**Principle (2):** pH-metric follows the hydrogen-ion activity, giving an S-shaped curve whose inflection "
         "is the equivalence point; conductometric follows the ionic conductance, giving piecewise-linear branches "
         "whose intersection is the equivalence point. **Sensitivity (2):** conductometry works for very dilute and "
         "very weak acid\u2013base systems where the pH break is small; pH-metry needs a measurable pH change. "
         "**Interferences (2):** conductometry responds to all ions, so it is unsuitable in high background "
         "electrolyte; pH-metry is affected by sodium error at high pH. **Practicalities (2):** conductometry needs "
         "no indicator and tolerates coloured or turbid samples; pH-metry needs calibration and gives the actual pH, "
         "which conductometry cannot."),
        ("Explain the whole error budget of a volumetric titration, with the direction of each contribution.",
         "**Systematic contributions (4):** unstandardised titrant biases every result in one direction; a burette "
         "with a systematic zero error or a leaking stopcock shifts all volumes; indicator choice shifts the endpoint "
         "relative to the equivalence point; temperature differences change the titrant concentration. **Random "
         "contributions (2):** reading the meniscus, judging the endpoint colour, and pipetting variability. "
         "**Arithmetic contributions (2):** forgetting the stoicheiometric ratio, or reporting a normality as a "
         "molarity \u2014 the most frequent single error in student reports."),
        ("A student obtains a hardness of 640 mg L^{\u22121} for a sample expected to be about 200. Diagnose.",
         "**Arithmetic (2):** check the factor of 50 and the conversion of mL to L; a factor-of-two error is "
         "typically an N/M confusion, where the EDTA molarity was used in place of normality. **Sample volume (2):** "
         "a 50 mL aliquot used with a 25 mL factor, or vice versa, scales the answer by two. **Standardisation (2):** "
         "an EDTA solution stronger than labelled gives a proportionally larger titre. **Chemistry (2):** "
         "precipitation of calcium at too high a pH, or interference from other metals, can raise the titre; "
         "buffering at pH 10 and adding a masking agent are the controls."),
        ("Discuss the safety design of the Pensky\u2013Martens and diazotisation experiments.",
         "**Hazard identification (2):** Pensky\u2013Martens creates an ignitable vapour and applies a flame; the "
         "diazo preparation generates a thermally unstable, nitrogen-rich intermediate and uses a toxic, "
         "skin-absorbed amine. **Engineering controls (2):** extractor hood, remote ignition source, enclosed cup, "
         "ice bath, and small scale. **Procedural controls (2):** specified heating rate, no unattended heating, "
         "dropwise addition, temperature monitoring, and a positive test for completion. **Personal and emergency "
         "controls (2):** gloves, eye protection, extinguisher and fire blanket for one; gloves, hood, and immediate "
         "glove change for the other, with approved aromatic waste disposal."),
        ("Explain how you would validate any single result in this volume.",
         "**Internal consistency (2):** replicate and compare with the expected magnitude; check that the "
         "apportioned species sum to the total, that the calibration is linear, and that the melting range is narrow. "
         "**Independent confirmation (2):** a second method \u2014 mixed melting point, a spectroscopic measurement, "
         "a gravimetric check. **Blank and standard (2):** run a reagent blank and a certified reference or a known "
         "standard alongside the sample. **Uncertainty budget (2):** propagate the dominant contributions and state "
         "the result with a defensible uncertainty rather than a spuriously precise figure."),
    ], None, 39),
]

B += [
    ("h2", "12.3  Paper 2 \u2014 Numerical problems (100 marks, 75 minutes)"),
    ("p", "Show the full arithmetic chain for every problem, including units. Each problem carries 10 marks: 4 for "
          "the correct expression, 4 for the substituted arithmetic, and 2 for the unit and the sanity check."),
    ("qa", [
        ("A cobalt(II) chloride solution gives an absorbance of 0.420 in a 1.00 cm cell, and the molar absorptivity at "
         "511 nm is 14.0 L mol^{\u22121} cm^{\u22121}. Find the molarity, then express it as % w/v of "
         "CoCl_{2}\u00b76H_{2}O (M = 237.93).",
         "**Expression:** c = A/(\u03b5l). **Arithmetic:** c = 0.420/(14.0 \u00d7 1.00) = 0.0300 mol L^{\u22121}. "
         "Mass concentration = 0.0300 \u00d7 237.93 = 7.14 g L^{\u22121}. **Result:** 0.0300 M; 7.14 g L^{\u22121} = "
         "**0.714 % w/v**. **Check:** the absorbance lies in the reliable range, so the value is plausible. Note the "
         "w/v assumption; the supplied source does not settle the basis."),
        ("In a hydrolysis run, V_{\u221e} = 48.0 mL, V_{0} = 2.0 mL, and V_{t} = 20.0 mL at t = 15 min. Calculate k "
         "and the half-life.",
         "**Expression:** k = (2.303/t) log[(V_{\u221e} \u2212 V_{0})/(V_{\u221e} \u2212 V_{t})]. **Arithmetic:** "
         "(46.0)/(28.0) = 1.643; log 1.643 = 0.2157; k = (2.303 \u00d7 0.2157)/15 = **0.0331 min^{\u22121}**. "
         "Half-life = 0.693/k = **20.9 min**. **Check:** k is positive and of a physically sensible magnitude for "
         "70\u201390 \u00b0C."),
        ("25.0 mL of HCl required 12.5 mL of 0.100 M NaOH to reach the equivalence point, where the pH was 7.0. Find "
         "the concentration of the acid.",
         "**Expression:** C_{HCl} = C_{NaOH}V_{eq}/V_{HCl} (1:1 stoicheiometry). **Arithmetic:** 0.100 \u00d7 "
         "12.5/25.0 = **0.0500 M**. **Check:** equivalence at pH 7 is consistent with a strong acid\u2013strong base "
         "system."),
        ("A conductivity cell of constant 1.25 cm^{\u22121} reads a resistance of 250 \u03a9 in 0.1 M KCl solution at "
         "25 \u00b0C. Find the conductivity.",
         "**Expression:** \u03ba = G \u00d7 (l/A), with G = 1/R. **Arithmetic:** G = 1/250 = 4.00 \u00d7 "
         "10^{\u22123} S; \u03ba = 4.00 \u00d7 10^{\u22123} \u00d7 1.25 = **5.00 \u00d7 10^{\u22123} S cm^{\u22121}** "
         "= 0.500 S m^{\u22121}. **Check:** the accepted value for 0.1 M KCl near 25 \u00b0C is about 0.0129 "
         "S cm^{\u22121}, so this illustration corresponds to a more dilute solution \u2014 a reminder to state the "
         "concentration alongside the conductivity."),
        ("1.575 g of oxalic acid dihydrate is dissolved and made to 250.0 mL. Find its molarity and normality. Then "
         "20.0 mL of this solution requires 19.8 mL of NaOH; find the NaOH normality.",
         "**Molarity:** 1.575/126.07 = 0.01249 mol in 0.2500 L = **0.04997 M**. **Normality:** dibasic, so N = 2M = "
         "**0.09994 N**. **Titration:** N_{NaOH} = (0.09994 \u00d7 20.0)/19.8 = **0.1010 N**. **Check:** the "
         "standard is essentially 0.1 N, which is the intended preparation."),
        ("A 50.0 mL water sample required 8.40 mL of 0.0100 M EDTA to reach the Eriochrome Black T endpoint. Express "
         "the hardness as mg L^{\u22121} CaCO_{3}.",
         "**Expression:** hardness = (N_{EDTA}V \u00d7 50 \u00d7 1000)/V_{sample}, with N = 2M = 0.0200 N. "
         "**Arithmetic:** 0.0200 \u00d7 8.40 \u00d7 50 \u00d7 1000/50.0 = **168 mg L^{\u22121}**. **Check by "
         "moles:** 8.40 \u00d7 10^{\u22125} mol \u00d7 100.09 g mol^{\u22121} = 8.41 mg in 0.0500 L = 168 mg "
         "L^{\u22121}, consistent. The water is hard but not extreme."),
        ("A 10.0 mL sample requires 1.2 mL of 0.0200 N acid to the phenolphthalein endpoint and 4.8 mL in total to "
         "the methyl-orange endpoint. Find P, T and the species distribution.",
         "**P:** 1.2 \u00d7 0.0200 \u00d7 50 \u00d7 1000/10.0 = **120 mg L^{\u22121}**. **T:** 4.8 \u00d7 0.0200 "
         "\u00d7 50 \u00d7 1000/10.0 = **480 mg L^{\u22121}**. **Ratio:** P/T = 0.25 < 0.5, so carbonate plus "
         "bicarbonate. CO_{3}^{2\u2212} = 2P = **240**; HCO_{3}^{\u2212} = T \u2212 2P = **240**; OH^{\u2212} = 0. "
         "**Check:** 240 + 240 = 480 = T."),
        ("100 mL of water required 0.60 mL of 0.0200 N thiosulphate in the iodometric residual-chlorine "
         "determination. Find the residual chlorine as Cl_{2}.",
         "**Expression:** (N V \u00d7 35.45 \u00d7 1000)/V_{sample}. **Arithmetic:** 0.0200 \u00d7 0.60 \u00d7 "
         "35.45 \u00d7 1000/100 = **4.25 mg L^{\u22121}**. **Check:** plausible for a poorly controlled system; the "
         "simplified factor 70.9 would be wrong here because the sample is 100 mL, not 10 mL."),
        ("An oil gives a mean Redwood efflux time of 285 s at 40 \u00b0C. Find the kinematic viscosity in cSt and the "
         "dynamic viscosity if the density is 880 kg m^{\u22123}.",
         "**Kinematic:** \u03bd = 0.264 \u00d7 285 \u2212 190/285 = 75.24 \u2212 0.667 = **74.6 cSt**. **Dynamic:** "
         "\u03bc = \u03bd\u03c1 = 74.6 \u00d7 10^{\u22126} \u00d7 880 = **0.0656 Pa s** = 65.6 mPa s. **Check:** t "
         "lies inside 40\u20132000 s, and 74.6 cSt at 40 \u00b0C corresponds to roughly an ISO VG 68 oil."),
        ("0.100 mol of aniline is diazotised and coupled to give diazoaminobenzene (M = 197.24). The isolated, dried "
         "product weighs 6.40 g. Find the theoretical and percentage yields.",
         "**Theoretical:** two aniline molecules per product, so 0.0500 mol \u00d7 197.24 = **9.86 g**. "
         "**Percentage:** 6.40/9.86 \u00d7 100 = **64.9 %**. **Check:** the product should melt at 96\u201398 \u00b0C; "
         "a yield in the sixties is normal for a preparation with filtration and recrystallisation losses."),
    ], None, 1),
]

B += [
    ("h2", "12.4  Paper 3 \u2014 Rapid-fire viva (60 marks, 45 minutes)"),
    ("p", "One mark per question. The examiner expects a single sentence; anything longer wastes your time and risks "
          "contradicting yourself. Answer aloud, with a timer running."),
    ("qa", [
        ("Why is distilled water used as the blank in spectrophotometry?",
         "Because it reproduces the solvent and cell contribution without the absorbing species."),
        ("What does a non-zero intercept in a Beer\u2019s law plot indicate?",
         "A systematic offset \u2014 stray light, a dirty cell, or a blank that does not match the matrix."),
        ("Why is the hydrolysis experiment described as pseudo-first-order?",
         "Because water is present in such excess that its concentration is effectively constant."),
        ("What is the unit of the rate constant you calculated?", "min^{\u22121} for a first-order reaction."),
        ("How do you locate the equivalence point on a conductometric curve?",
         "At the intersection of the two linear branches, extrapolated if necessary."),
        ("Why is a high-frequency conductivity measurement sometimes preferred?",
         "To avoid electrode polarisation, which distorts the measured conductance."),
        ("What is the SI unit of conductivity?", "S m^{\u22121}."),
        ("What cell constant would you expect for electrodes 1 cm^{2} in area and 1 cm apart?",
         "1.0 cm^{\u22121}."),
        ("Why must the burette be rinsed with the titrant before use?",
         "Residual water dilutes the titrant and shifts every volume."),
        ("What is the difference between a primary standard and a secondary standard?",
         "A primary standard is a pure, stable, high-molar-mass solid weighed directly; a secondary standard is "
         "standardised against a primary one."),
        ("Why is oxalic acid a good primary standard?", "It is available pure and dry, stable, and has a high "
                                                        "equivalent weight, so weighing error is small."),
        ("Why is NaOH not a primary standard?", "It is hygroscopic and absorbs atmospheric CO_{2}."),
        ("What does a sharp potentiometric break tell you?",
         "That the reaction is quantitative and the equivalence point is well defined."),
        ("Why is the equivalence pH 7 only for strong acid\u2013strong base titrations?",
         "Because only then do the products leave the solution neutral."),
        ("Which indicator would you use for a weak acid\u2013strong base titration?",
         "Phenolphthalein, whose range lies on the basic side."),
        ("State the operational definition of total hardness.",
         "The sum of calcium and magnesium, expressed as mg L^{\u22121} CaCO_{3}."),
        ("What does a conditional formation constant account for?",
         "The fraction of the ligand actually present in its reactive form at that pH."),
        ("Why is ammonia buffer used rather than a simple buffer?",
         "It also complexes trace metals and helps keep the endpoint sharp."),
        ("What does a wine-red colour that persists through the titration mean?",
         "The endpoint has not been reached, or the indicator concentration is too high."),
        ("Why does the EBT colour change at the endpoint?",
         "EDTA strips the metal from the indicator, freeing the blue form."),
        ("Distinguish alkalinity from hardness in one sentence.",
         "Alkalinity is acid-neutralising capacity; hardness is the divalent metal content."),
        ("What is measured at the methyl-orange endpoint?",
         "The total of hydroxide, carbonate and bicarbonate alkalinity."),
        ("What does P = T mean?", "Hydroxide-only alkalinity."),
        ("What does P = 0 mean?", "Bicarbonate-only alkalinity; the sample could not be titrated to pH 8.3."),
        ("Why does a water sample's pH not tell you its buffering capacity?",
         "pH is an intensity; buffering is a capacity, and the two are independent."),
        ("What is the toxicological concern with residual chlorine?",
         "Disinfection by-products such as trihalomethanes, formed with natural organic matter."),
        ("Why is the iodometric method indirect?", "Because the titration measures liberated iodine, not the "
                                                    "chlorine itself."),
        ("What is the function of the thiosulphate?", "It reduces iodine to iodide while being oxidised to "
                                                      "tetrathionate."),
        ("Why is the starch endpoint reversible if the titration is done correctly?",
         "Because the residual iodine near the endpoint is small and the complex re-forms slowly enough to be seen."),
        ("What is the equivalent weight of Cl_{2}?", "35.45 g eq^{\u22121}."),
        ("Identify an interference that would cause a positive error in residual chlorine.",
         "Any other oxidant \u2014 ozone, permanganate, or chlorite."),
        ("Why is viscosity measured at a specified temperature?",
         "Because it changes steeply with temperature, so the value is otherwise undefined."),
        ("What does a Redwood second measure?", "The efflux time of 50 mL of oil through a standard jet."),
        ("Convert 50 cSt to SI units.", "50 \u00d7 10^{\u22126} m^{2} s^{\u22121} = 5.0 \u00d7 10^{\u22125} "
                                       "m^{2} s^{\u22121}."),
        ("What is the viscosity index?", "An empirical measure of how little viscosity changes with temperature."),
        ("Why does a lubricant need a minimum viscosity?",
         "To maintain a separating film under load."),
        ("Why is a maximum viscosity also necessary?",
         "To allow circulation and limit pumping losses and heat generation."),
        ("Which is higher: open-cup or closed-cup flash point?", "Open cup."),
        ("What does the fire point require that the flash point does not?",
         "Sustained burning for at least five seconds."),
        ("Why is the sample stirred in the Pensky\u2013Martens cup?",
         "To keep the bulk and surface temperatures equal, so the vapour represents the sample."),
        ("Why is the test flame kept small?", "An oversized flame can ignite a mixture below the flammable limit, "
                                              "lowering the apparent flash point."),
        ("What does a flash point of 60 \u00b0C mean in practice?",
         "The liquid gives an ignitable vapour only when heated above 60 \u00b0C in a closed cup."),
        ("What is the difference between flammable and combustible?",
         "A regulatory distinction based on the closed-cup flash point threshold."),
        ("Why is the diazonium ion kept cold?", "It decomposes thermally to phenol and nitrogen."),
        ("What is the electrophile in diazotisation?", "The nitrosonium ion, NO^{+}."),
        ("Why is excess acid required?", "To generate nitrous acid and to drive the dehydration to the diazonium "
                                         "ion."),
        ("Why is coupling done at a higher pH than diazotisation?",
         "Because coupling needs the free, unprotonated amine."),
        ("What does a mixed melting point prove?",
         "Identity \u2014 no depression means the sample is the same compound as the reference."),
        ("What does a broad melting range indicate?", "Impurity, or residual solvent or water."),
        ("Why heat slowly near the melting point?",
         "To let the sample and the thermometer reach thermal equilibrium."),
        ("What is the main safety hazard of aniline?", "Skin absorption and toxicity; it is a suspected "
                                                       "carcinogen."),
        ("Name the two reagents most likely to have silently deteriorated in the chlorine experiment.",
         "Potassium iodide and the starch solution."),
        ("Why should a reagent blank be subtracted rather than ignored?",
         "Because it is an additive systematic contribution present in every measurement."),
        ("What does it mean if two replicates agree but a standard gives a biased value?",
         "The method has a systematic error \u2014 repeatability is not accuracy."),
        ("What is the purpose of a calibration curve?",
         "To convert an instrumental response into a concentration and to establish the linear working range."),
        ("Why is the working range of absorbance roughly 0.1\u20131.0?",
         "Below it the signal is noisy; above it stray light and non-linearity dominate."),
        ("What does a negative calculated result usually indicate?",
         "A sign or convention error, or a reading outside the valid range."),
        ("Why are units as important as the number in an examination answer?",
         "An unqualified number cannot be checked and is treated as incorrect."),
        ("Give one reason why each chapter ends with a ninety-second spoken answer.",
         "Because examination performance is spoken, and spoken fluency is trained differently from silent reading."),
        ("What single habit most improves marks in a viva?",
         "Answering the question asked, in one sentence, before elaborating."),
    ], None, 1),
    ("box", "note", [
        "**Marking Paper 3.** One mark for a correct, complete sentence. Half a mark if the idea is present but "
        "muddled. Zero if the answer avoids the question. Then re-read only the chapters whose questions you missed "
        "\u2014 not the whole volume.",
    ], "How to mark the rapid-fire paper"),
]

B += [
    ("h2", "12.5  Paper 2 mark scheme, condensed"),
    ("tbl", ["Q", "Final answer", "Dominant pitfall"],
     [["1", "0.0300 M; 0.714 % w/v", "Forgetting the hydrate molar mass, or reporting mol L^{\u22121} as %"],
      ["2", "k = 0.0331 min^{\u22121}; t_{1/2} = 20.9 min", "Using ln instead of log without the 2.303 factor"],
      ["3", "0.0500 M", "Inverting the volume ratio"],
      ["4", "\u03ba = 5.00 \u00d7 10^{\u22123} S cm^{\u22121}", "Using R instead of 1/R"],
      ["5", "0.04997 M; 0.09994 N; 0.1010 N NaOH", "Forgetting that oxalic acid is dibasic"],
      ["6", "168 mg L^{\u22121} CaCO_{3}", "Using molarity where normality is required"],
      ["7", "P = 120; T = 480; CO_{3} = 240; HCO_{3} = 240", "Recording T as an additional volume"],
      ["8", "4.25 mg L^{\u22121} as Cl_{2}", "Applying the 10 mL simplified factor to a 100 mL sample"],
      ["9", "74.6 cSt; 0.0656 Pa s", "Omitting the \u2212190/t term, or forgetting 10^{\u22126} for cSt"],
      ["10", "9.86 g theoretical; 64.9 %", "Using one mole of aniline per mole of product"]],
     [12, 62, 94], "**Table 12.2** Paper 2 answers. If you lost marks on three or more of the same pitfall, that "
                   "single habit is worth more than a reread of the chapter.", ["c", "l", "l"]),
]

B += [
    ("h2", "12.6  After the papers: building your own revision list"),
    ("p", "The purpose of a mock paper is not the score. It is the list. Convert every lost mark into one of three "
          "categories, because each demands a different response:"),
    ("tbl", ["Category", "Symptom in the paper", "Correct response", "Typical example"],
     [["Knowledge gap", "You could not start the question", "Reread the relevant chapter section and write the "
       "answer from memory", "Forgetting the EBT endpoint colour change"],
      ["Retrieval gap", "You knew it, but it did not come", "Spaced recall practice and spoken rehearsal",
       "Knowing the Beer\u2013Lambert law but blanking on the units of \u03b5"],
      ["Execution gap", "You knew it and wrote it, but the arithmetic or the units failed",
       "Drill the calculation chain until it is automatic", "Dropping the 2.303 factor in the rate calculation"]],
     [30, 56, 52, 48], "**Table 12.3** Three kinds of lost mark. Most students over-diagnose knowledge gaps and "
                       "under-diagnose execution gaps, which are cheaper to fix.", ["l", "l", "l", "l"]),
    ("box", "key", [
        "**Score, diagnose, revise in that order \u2014 never revise first.** A paper marked before you look "
        "anything up tells you something; a paper written with the book open tells you nothing.",
        "**Spend your remaining time where the marks are cheapest.** Execution gaps cost minutes to fix and recur "
        "in every paper; knowledge gaps are expensive but occur once.",
        "**Rehearse aloud.** Papers 1 and 3 measure spoken and written performance; neither improves by reading "
        "silently.",
    ], "Three habits that convert practice into marks"),
]

CH12 = {
    "key": "simulation",
    "num": "12",
    "kicker": "Examination simulation",
    "title": "Three Mock Papers with Mark Schemes",
    "toc": "Examination simulation",
    "standfirst": "Three complete papers \u2014 theory, numerical, and spoken \u2014 built from the eleven activities in "
                  "this volume, with the marking discipline that turns a score into a revision list.",
    "body": B + [
        ("h2", "12.7  Examiner\u2019s secret checklist"),
        ("h3", "12.7.1  Twenty facts that must be automatic"),
        ("p", "These are the twenty items that recur across all three papers. If any of them requires thought, it is "
              "not yet automatic."),
        ("bul", [
            "A = \u03b5lc, and the working absorbance range is 0.1\u20131.0.",
            "Cobalt(II) chloride absorbs at about 511 nm.",
            "Pseudo-first-order: k = (2.303/t) log[(V_{\u221e} \u2212 V_{0})/(V_{\u221e} \u2212 V_{t})].",
            "Strong acid\u2013strong base equivalence is at pH 7.",
            "\u03ba = G(l/A) with G = 1/R.",
            "Limiting conductances: H^{+} 349.8, OH^{\u2212} 198.3 S cm^{2} mol^{\u22121}.",
            "Oxalic acid dihydrate: M 126.07, equivalent weight 63.04, N = 2M.",
            "Normality \u00d7 volume = equivalents, always.",
            "EDTA at pH 10; EBT changes wine red to blue.",
            "Hardness as CaCO_{3} uses an equivalent weight of 50.",
            "Alkalinity: P at pH 8.3, T at pH 4.5, and T is cumulative.",
            "OH^{\u2212} and HCO_{3}^{\u2212} cannot coexist.",
            "Cl_{2} + 2I^{\u2212} \u2192 2Cl^{\u2212} + I_{2}, and the equivalent weight of Cl_{2} is 35.45.",
            "Starch goes in late; the flask stays stoppered.",
            "\u03bd = 0.264t \u2212 190/t cSt, valid for 40\u20132000 s.",
            "1 cSt = 1 mm^{2} s^{\u22121} = 10^{\u22126} m^{2} s^{\u22121}.",
            "Closed-cup flash point is lower than open-cup.",
            "Fire point requires five seconds of sustained burning.",
            "Diazotisation below 5 \u00b0C; coupling needs free amine.",
            "Diazoaminobenzene melts at 96\u201398 \u00b0C; two anilines per product.",
        ]),
        ("h3", "12.7.2  The ten hardest questions across the whole volume"),
        ("bul", [
            "Derive the pseudo-first-order rate expression from the integrated rate law and the measured volumes.",
            "Explain, with numbers, why a 1 \u00b0C error near 40 \u00b0C matters more than a 0.5 s timing error.",
            "Show that the alkalinity apportionment always sums to T.",
            "Explain why the conditional formation constant, not the absolute one, controls the EDTA endpoint.",
            "Derive the 35.45 g eq^{\u22121} equivalent weight of chlorine and explain why it equals the atomic mass.",
            "Explain why the Redwood relation needs a negative correction term and why the range is bounded.",
            "Justify, in chemical terms, why diazotisation and coupling require different pH conditions.",
            "Distinguish repeatability from accuracy using one experiment in this volume.",
            "Explain why an efflux instrument reports kinematic rather than dynamic viscosity.",
            "Construct a full error budget for any titration, with the direction of every contribution.",
        ]),
        ("h3", "12.7.3  Most commonly confused pairs"),
        ("tbl", ["Pair", "The distinction that matters"],
         [["Equivalence point vs endpoint", "Stoicheiometric reality vs indicator-based observation"],
          ["Molarity vs normality", "mol L^{\u22121} vs equivalents L^{\u22121}; dibasic species differ by two"],
          ["Dynamic vs kinematic viscosity", "A factor of density"],
          ["Flash point vs fire point", "Transient flash vs five seconds of burning"],
          ["Free vs combined chlorine", "HOCl/OCl^{\u2212} vs chloramines"],
          ["P vs T alkalinity", "First endpoint vs cumulative total"],
          ["Repeatability vs accuracy", "Agreement vs truth"],
          ["Knowledge vs execution gap", "Content to learn vs habit to drill"]],
         [50, 118], "**Table 12.4** Pairs that decide marks.", ["l", "l"]),
        ("h3", "12.7.4  The ninety-second answer"),
        ("speak", "Ninety seconds on the whole volume", "The eleven activities in this volume share one structure: a measurable physical or chemical quantity "
                  "is converted into a concentration, a rate or a material property, and then checked for sense. In "
                  "spectrophotometry and conductometry the conversion is instrumental, through a calibration; in the "
                  "titrations it is stoicheiometric, through normality and volume; in the viscosity and flash-point "
                  "experiments it is empirical, through a calibration relation or a regulatory method. In every case "
                  "the same discipline applies: control the dominant systematic variable, whether that is temperature, "
                  "pH, iodine loss or heating rate; measure a blank or a standard; and compare the answer with a "
                  "plausible magnitude before writing it down. The examiner's question is rarely about arithmetic. It "
                  "is almost always about why the measurement means what it does."),
        ("h3", "12.7.5  Last-minute revision strip"),
        ("box", "key", [
            "**Calibrate, blank, replicate, sanity-check \u2014 in that order, in every activity.**",
            "**State the units, the temperature and the basis, or the number is incomplete.**",
            "**The dominant error is usually systematic, not careless.**",
            "**A model answer is a habit; a mark scheme is a checklist.**",
        ], "Memory strip"),
        ("h2", "12.8  A four-week revision plan"),
        ("p", "A diagnostic alone does not produce a pass; a timetable does. The plan below assumes four weeks and "
              "about ninety minutes a day, and it front-loads the work that cannot be crammed. Each week ends with "
              "one paper attempted closed-book so that the plan diagnoses itself."),
        ("tbl", ["Week", "Daily work", "End-of-week test", "What it fixes"],
         [["1", "Chapters 1–4: theory sections only, one per evening; write each derivation from memory the "
           "following morning", "Paper 1, Sections A and B", "Conceptual gaps in the instrumental activities"],
          ["2", "Chapters 5–8: procedure plus error budget; recite the calculation chain aloud each evening",
           "Paper 2, questions 1–7", "Execution gaps in titration arithmetic"],
          ["3", "Chapters 9–12 plus Appendix A; learn the formula sheet by reconstructing it from blank paper",
           "Paper 2 in full, then Paper 3", "Recall speed and unit handling"],
          ["4", "Appendix B in full; reread only the sections your own lost-mark list named", "Paper 1 and Paper 3 "
           "in full, under time", "Cross-experiment fluency and stamina"]],
         [16, 74, 40, 44],
         "**Table 12.5** A four-week plan built on the diagnostic logic of this chapter. The sequence matters: "
         "understanding first, arithmetic second, speed third, synthesis last.",
         ["c", "l", "l", "l"]),
        ("box", "note", [
            "**The night before the examination, do not learn anything new.** Read your own lost-mark list, read the "
            "four memory strips from Chapters 1 to 11, and sleep. The value of the last evening is in consolidation, "
            "not acquisition.",
        ], "The last evening"),
    ],
}
