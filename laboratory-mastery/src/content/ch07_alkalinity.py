VIVA_E = [
    ("Why are the samples not acidified before storage?",
     "Acidification would destroy the alkalinity you intend to measure."),
    ("Why should the sample bottle be filled completely?",
     "To minimise the headspace and hence the exchange of carbon dioxide with air."),
    ("What is the effect of a sample containing a high concentration of carbonate on the P endpoint?",
     "P becomes a large fraction of T, approaching T/2 for a carbonate-only sample."),
    ("Why is the methyl-orange endpoint conventionally taken at a lower pH than the phenolphthalein one?",
     "Because the second neutralisation stage, bicarbonate to carbonic acid, only goes to completion in more acidic "
     "solution."),
    ("Why does the titration curve have two buffer regions?",
     "Because the carbonate system has two protonation steps with distinct pK_{a} values."),
    ("What is the significance of a very small titre to the phenolphthalein endpoint?",
     "A small amount of carbonate or hydroxide is present, so the sample is mostly bicarbonate."),
    ("Why does boiling a sample change its alkalinity?",
     "Carbon dioxide is expelled and bicarbonate precipitates as carbonate with calcium."),
    ("Why is alkalinity expressed in equivalents rather than moles?",
     "Because different species consume different numbers of protons per mole."),
    ("How would you express a hydroxide alkalinity in mg L^{−1} of OH^{−}?",
     "Multiply the CaCO_{3} equivalent by M(OH)/50 = 17.01/50."),
    ("How would you express a bicarbonate alkalinity in mg L^{−1} of HCO_{3}^{−}?",
     "Multiply the CaCO_{3} equivalent by M(HCO_{3})/50 = 61.02/50."),
    ("Why is the pH electrode response described as Nernstian?",
     "Because the potential changes by about 59.16 mV per pH unit at 25 \u00b0C."),
    ("What is the alkaline error of a glass electrode?",
     "At high pH the electrode responds partly to sodium ions, giving a reading lower than the true pH."),
    ("What is the acid error?",
     "At very low pH the electrode can read slightly high because of the activity of the acid."),
    ("Why is a combination electrode stored in a potassium chloride solution?",
     "To keep the reference junction hydrated and the filling solution concentrated."),
    ("Why does an unclean electrode drift?",
     "A fouled or blocked junction prevents a stable liquid-junction potential."),
    ("What does a two-point calibration with buffers at 7.0 and 9.2 correct?",
     "It sets both the offset and the slope for the alkaline region of interest."),
    ("Why is alkalinity important in corrosion control?",
     "It buffers the water and, with calcium, determines the saturation index that governs scaling or corrosion."),
    ("What is the difference between alkalinity and caustic alkalinity?",
     "Caustic alkalinity refers specifically to the hydroxide contribution."),
    ("How would you detect the presence of hydroxide alkalinity without the nomograph?",
     "By the relationship between P and T: hydroxide is present only when P > T/2."),
    ("Why is a sample with high alkalinity usually also hard?",
     "Both often derive from carbonate and bicarbonate minerals dissolving in the aquifer, though this correlation "
     "is not a rule."),
]

"""Chapter 7 - pH and alkalinity of water."""
from common import checklist

B = []

B += [
    ("h2", "7.1  Two numbers that are constantly confused"),
    ("lead", "pH and alkalinity are different measurements of different things, and confusing them is the most "
             "common conceptual error in water analysis. pH tells you the //current// acid\u2013base state of the "
             "water. Alkalinity tells you how much acid the water can absorb before its pH changes "
             "substantially \u2014 its buffering capacity. A sample can have high pH and low alkalinity, or near-"
             "neutral pH and high alkalinity."),
    ("p", "The supplied material sets the aim as **determining the pH of different water samples and the "
          "alkalinity of a water sample.** The manual explains pH from the ionisation of water, and describes "
          "alkalinity as arising from hydroxide, carbonate and bicarbonate ions, measured by titration with "
          "standard acid to two successive endpoints \u2014 phenolphthalein (P) and methyl orange (T)."),
    ("eq", "H_{2}O \u21cc H^{+} + OH^{\u2212};   K_{w} = [H^{+}][OH^{\u2212}] = 1.0 \u00d7 10^{\u221214} at "
           "25 \u00b0C",
     "Equation 7.1 \u2014 autoionisation of water, the basis of the pH scale."),
    ("defbox", [
        ("pH", "The negative base-10 logarithm of hydrogen-ion activity. It describes the //intensity// of "
               "acidity or alkalinity."),
        ("Alkalinity", "The acid-neutralising capacity of water \u2014 the amount of acid required to bring it to a "
                       "defined endpoint. It describes //capacity//, not intensity."),
        ("Phenolphthalein alkalinity (P)", "The acid volume required to reach the phenolphthalein endpoint near pH "
                                           "8.3. It measures hydroxide plus half the carbonate."),
        ("Total alkalinity (T)", "The acid volume to the methyl-orange endpoint near pH 4.5. It measures "
                                 "hydroxide, carbonate and bicarbonate together."),
        ("Buffer", "A system that resists pH change on addition of acid or base; alkalinity is a measure of "
                   "buffer capacity in the basic direction."),
        ("CaCO_{3} basis", "The conventional reporting scale, allowing alkalinity from different species to be "
                           "compared on one scale."),
    ]),
    ("box", "key", [
        "**pH is a position on a scale; alkalinity is an amount.** One is logarithmic and dimensionless, the other "
        "is a capacity expressed in mg L^{\u22121} of CaCO_{3}.",
        "**Two endpoints, two meanings.** P measures the strong-base part; T measures everything.",
        "**OH^{\u2212} and HCO_{3}^{\u2212} cannot coexist** in significant amounts \u2014 they react to give "
        "CO_{3}^{2\u2212}. That single chemical fact generates the whole P/T nomograph.",
    ], "Three ideas that make this chapter cohere"),
    ("fig", "alkalinity", "**Figure 7.1** Composition nomograph. Given P and T, the dominant species and their "
                          "individual contributions can be read directly: if P = 0 the sample is bicarbonate-only; "
                          "if P = T it is hydroxide-only; if P = T/2 it is carbonate-only."),
]

B += [
    ("h2", "7.2  Theory: pH, then alkalinity"),
    ("h3", "7.2.1  pH as a measured quantity"),
    ("p", "In pure water at 25 \u00b0C, [H^{+}] = [OH^{\u2212}] = 1.0 \u00d7 10^{\u22127} M, so pH = 7 and the "
          "solution is neutral. Adding an acid raises [H^{+}] and lowers pH; adding a base lowers [H^{+}] and "
          "raises pH. Because the scale is logarithmic, one pH unit is a tenfold change in hydrogen-ion activity "
          "\u2014 which is why a change from pH 6 to pH 4 represents a hundredfold increase in acidity, not a "
          "change of two."),
    ("p", "Neutrality itself is temperature-dependent, because K_{w} changes with temperature. At 25 \u00b0C, "
          "neutral pH is 7.00; at 50 \u00b0C, K_{w} is about 5.5 \u00d7 10^{\u221214}, so neutral pH is about 6.63. "
          "This is worth saying out loud in a viva, because \u201cpH 7 is neutral\u201d is only true at one "
          "temperature."),
    ("h3", "7.2.2  What creates alkalinity"),
    ("p", "Alkalinity in natural water comes predominantly from three species, related by two proton-transfer "
          "equilibria:"),
    ("eq", "CO_{3}^{2\u2212} + H^{+} \u21cc HCO_{3}^{\u2212}   (pK_{a2} \u2248 10.3)"),
    ("eq", "HCO_{3}^{\u2212} + H^{+} \u21cc H_{2}CO_{3} \u21cc CO_{2} + H_{2}O   (pK_{a1} \u2248 6.3)"),
    ("eq", "OH^{\u2212} + H^{+} \u2192 H_{2}O   (complete at pH below about 10)"),
    ("p", "Each of these consumes one mole of H^{+} per mole of species, so each contributes one equivalent of "
          "alkalinity. This is why alkalinity is expressed in equivalents \u2014 and therefore in mg L^{\u22121} "
          "of CaCO_{3}, whose equivalent weight is 50."),
    ("h3", "7.2.3  Why two endpoints, and what each one measures"),
    ("p", "When you titrate an alkaline water sample with standard acid:"),
    ("bul", [
        "**Down to pH 8.3 (phenolphthalein endpoint)** you have neutralised all the free OH^{\u2212} and converted "
        "all the CO_{3}^{2\u2212} to HCO_{3}^{\u2212}. This acid volume is **P**.",
        "**On to pH 4.5 (methyl-orange endpoint)** you have additionally converted all the HCO_{3}^{\u2212} to "
        "CO_{2}. The //total// acid volume from the start is **T**.",
    ]),
    ("p", "Because the carbonate is only half-neutralised at the first endpoint, the P volume contains one "
          "equivalent for each OH^{\u2212} and one for each CO_{3}^{2\u2212}, while the second stage contains a "
          "second equivalent for each CO_{3}^{2\u2212} and one for each original HCO_{3}^{\u2212}. Solving the "
          "resulting pair of equations for the three possible species gives the standard composition table:"),
    ("tbl", ["Condition", "OH^{\u2212} (mg L^{\u22121} as CaCO_{3})", "CO_{3}^{2\u2212}",
             "HCO_{3}^{\u2212}", "Interpretation"],
     [["P = 0", "0", "0", "T", "Bicarbonate only"],
      ["P < T/2", "0", "2P", "T \u2212 2P", "Carbonate + bicarbonate"],
      ["P = T/2", "0", "2P = T", "0", "Carbonate only"],
      ["P > T/2", "2P \u2212 T", "2(T \u2212 P)", "0", "Hydroxide + carbonate"],
      ["P = T", "T", "0", "0", "Hydroxide only"]],
     [24, 34, 28, 24, 60],
     "**Table 7.1** The P/T composition table, in the form given in the supplied material. Note that "
     "OH^{\u2212} and HCO_{3}^{\u2212} never appear together: they react to form CO_{3}^{2\u2212}.",
     ["c", "c", "c", "c", "l"]),
    ("plot", "alkalinity", "**Figure 7.2** Alkalinity titration curve. The phenolphthalein endpoint near pH 8.3 "
                           "marks the conversion of hydroxide and half the carbonate; the methyl-orange endpoint "
                           "near pH 4.5 marks the total. The horizontal span between them is the bicarbonate "
                           "contribution."),
    ("h3", "7.2.4  The calculation"),
    ("p", "If V (mL) of sample is titrated with acid of normality N, the alkalinity in mg L^{\u22121} as "
          "CaCO_{3} is:"),
    ("eq", "Alkalinity (mg L^{\u22121}) = (V_{acid} \u00d7 N \u00d7 50 \u00d7 1000)/V_{sample}",
     "Equation 7.2 \u2014 the general form. With V_{acid} = P you obtain the phenolphthalein alkalinity; with "
     "V_{acid} = T you obtain the total alkalinity."),
    ("p", "The supplied material states the same relationship in the slightly different form "
          "A \u00d7 N \u00d7 50,000/V_{sample}, where A is the acid volume. The two are identical when volumes are "
          "in mL; the factor 1000 converts mL to L and the factor 50 is the equivalent weight of CaCO_{3}."),
    ("box", "exam", [
        "**Trap:** \u201cIs alkalinity the same as pH?\u201d No. A water sample at pH 7.0 with 200 mg L^{\u22121} "
        "bicarbonate alkalinity is well buffered; another at pH 7.0 with almost no bicarbonate has almost no "
        "buffering. Same pH, completely different behaviour when acid is added.",
        "**Trap:** \u201cCan a water have high pH but low alkalinity?\u201d Yes \u2014 for example a sample "
        "containing a little sodium hydroxide but almost no carbonate system. pH is high; capacity is small.",
    ], "Two questions that separate understanding from memorisation"),
]

B += [
    ("h2", "7.3  Apparatus"),
    ("tbl", ["Item", "Function", "If it is faulty"],
     [["pH meter with calibrated electrode", "Measures sample pH", "Uncalibrated meter gives a shifted, "
       "meaningless pH"],
      ["Buffer solutions (pH 4.0, 7.0, 9.2)", "Calibrate the meter", "Stale buffers calibrate to the wrong "
       "value"],
      ["Burette + stand", "Delivers standard acid", "Bubbles or leaks bias every volume"],
      ["Pipette (10 or 20 mL)", "Delivers the sample aliquot", "Wrong aliquot scales alkalinity directly"],
      ["Conical flasks", "Hold the sample during titration", "Contamination changes the alkalinity"],
      ["Standard acid (e.g. 0.02 N H_{2}SO_{4} or HCl)", "Titrant", "Unstandardised acid gives a wrong result"],
      ["Phenolphthalein indicator", "Marks the pH 8.3 endpoint", "Stale indicator gives a faint, late endpoint"],
      ["Methyl orange indicator", "Marks the pH 4.5 endpoint", "Poor quality gives a muddy endpoint"],
      ["Beakers, wash bottle", "Sample handling and rinsing", "Tap water contaminates"]],
     [50, 58, 62], "**Table 7.2** Apparatus.", ["l", "l", "l"]),
    ("box", "note", [
        "**Do not use a pH electrode as the endpoint detector for the alkalinity titration unless your manual "
        "says so.** The classical method uses the two indicators, and the definition of P and T is tied to those "
        "two pH values. A pH-meter titration is a legitimate alternative, but you must state which definition you "
        "used, because the reported P and T depend on the endpoint pH chosen.",
    ], "A definition point students miss"),
]

B += [
    ("h2", "7.4  Procedure with reasoning"),
    ("h3", "Part A \u2014 pH measurement"),
    ("num", [
        "**Switch on the meter and allow it to stabilise** (the manual specifies about 15 minutes).",
        "**Calibrate with two buffers** bracketing the expected sample pH \u2014 typically 7.0 and 9.2 for "
        "alkaline waters, or 4.0 and 7.0 for acidic ones.",
        "**Rinse the electrode with distilled water** and blot gently between samples.",
        "**Immerse the electrode in the sample, allow the reading to stabilise, and record the pH** together with "
        "the sample temperature.",
        "**Repeat for each sample**, rinsing between them so that one sample does not contaminate the next.",
    ]),
    ("h3", "Part B \u2014 Alkalinity"),
    ("num", [
        "**Pipette a measured volume of the sample** (the manual suggests 10 mL) into a conical flask.",
        "**Add 1\u20132 drops of phenolphthalein.** If the solution is already colourless, the phenolphthalein "
        "alkalinity is zero \u2014 record P = 0 rather than titrating to a colour that is not there.",
        "**If pink, titrate with standard acid until the pink just disappears.** Record this volume as P.",
        "**Add 2 drops of methyl orange to the same solution** and continue titrating to the first appearance of "
        "a distinct orange (or pink-orange, depending on the manual\u2019s convention). The //total// volume of "
        "acid from the start is T.",
        "**Repeat on two further portions** to obtain concordant values of P and T.",
        "**Calculate P and T alkalinity** as mg L^{\u22121} CaCO_{3}, then use Table 7.1 to apportion the species.",
    ]),
    ("box", "pitfall", [
        "**The second endpoint is cumulative, not additional.** T is the total acid volume from the start of the "
        "titration, not the volume added after the phenolphthalein endpoint. If you record only the additional "
        "volume, you must add P to it; if you record the burette reading, T is the difference from the initial "
        "reading. Mixing these conventions is the most common arithmetic error in this experiment.",
    ], "The cumulative-volume trap"),
]

B += [
    ("h2", "7.5  Observations and calculation"),
    ("tbl", ["S. No.", "Sample", "pH", "Temperature (\u00b0C)", "Remark"],
     [["1", "Sample A", "", "", ""], ["2", "Sample B", "", "", ""], ["3", "Sample C", "", "", ""]],
     [14, 40, 26, 34, 56], "**Table 7.3** pH observation table.", ["c", "l", "c", "c", "l"]),
    ("tbl", ["S. No.", "Sample volume (mL)", "Acid to P endpoint (mL)", "Total acid to T endpoint (mL)",
             "P alkalinity (mg L^{\u22121})", "T alkalinity (mg L^{\u22121})"],
     [["1", "10.0", "", "", "", ""], ["2", "10.0", "", "", "", ""], ["3", "10.0", "", "", "", ""]],
     [14, 32, 36, 36, 30, 30],
     "**Table 7.4** Alkalinity observation table. Blank because the supplied source\u2019s handwritten readings are "
     "too faint to transcribe.", ["c", "c", "c", "c", "c", "c"]),
    ("h3", "7.5.1  Worked illustration"),
    ("p", "Suppose a 10.0 mL sample required 1.2 mL of 0.02 N acid to the phenolphthalein endpoint and a total of "
          "4.8 mL to the methyl-orange endpoint."),
    ("eq", "P = (1.2 \u00d7 0.02 \u00d7 50 \u00d7 1000)/10.0 = 120 mg L^{\u22121} as CaCO_{3}"),
    ("eq", "T = (4.8 \u00d7 0.02 \u00d7 50 \u00d7 1000)/10.0 = 480 mg L^{\u22121} as CaCO_{3}"),
    ("p", "Now P/T = 0.25, which is less than 0.5, so the sample is a carbonate\u2013bicarbonate mixture. From Table "
          "7.1: CO_{3}^{2\u2212} = 2P = 240 mg L^{\u22121}; HCO_{3}^{\u2212} = T \u2212 2P = 240 mg L^{\u22121}; "
          "OH^{\u2212} = 0."),
    ("p", "Note the internal check: 240 + 240 = 480, which is T. **Any apportionment that does not sum to T "
          "contains an arithmetic error** \u2014 a self-check worth performing in the examination."),
    ("tbl", ["Quantity", "Expression", "Illustrative value"],
     [["Phenolphthalein alkalinity", "(P \u00d7 N \u00d7 50 \u00d7 1000)/V", "120 mg L^{\u22121}"],
      ["Total alkalinity", "(T \u00d7 N \u00d7 50 \u00d7 1000)/V", "480 mg L^{\u22121}"],
      ["Ratio P/T", "\u2014", "0.25"],
      ["Condition", "P < T/2", "carbonate + bicarbonate"],
      ["Carbonate", "2P", "240 mg L^{\u22121}"],
      ["Bicarbonate", "T \u2212 2P", "240 mg L^{\u22121}"],
      ["Hydroxide", "0", "0"],
      ["Check", "sum = T", "480 = 480 \u2713"]],
     [46, 64, 58], "**Table 7.5** Calculation chain with the internal check.", ["l", "l", "c"]),
]

B += [
    ("h2", "7.6  Precautions, errors and troubleshooting"),
    ("bul", [
        "Calibrate the pH meter with fresh buffers and rinse the electrode between samples.",
        "Record the sample temperature with the pH, because both pH and K_{w} depend on it.",
        "Add the same number of indicator drops to every flask.",
        "Record P and T as cumulative volumes from the same burette zero.",
        "Titrate promptly; exposure to air changes dissolved CO_{2} and therefore the alkalinity.",
        "Use a white tile and consistent lighting for the faint endpoints.",
        "Standardise the acid and state its normality.",
        "Do not shake the sample vigorously before measurement; it exchanges CO_{2} with the air.",
    ]),
    ("tbl", ["Source of error", "Type", "Effect", "Control"],
     [["pH electrode not calibrated", "Systematic", "Shifted pH values", "Two-point calibration"],
      ["Sample exposed to air", "Systematic", "CO_{2} uptake changes P and T", "Titrate promptly; minimise "
       "headspace"],
      ["Endpoint misjudged at pH 8.3", "Systematic", "P wrong, so apportionment wrong", "Consistent lighting and "
       "colour criterion"],
      ["T recorded as additional rather than total volume", "Arithmetic", "T too low, wrong apportionment",
       "Record cumulative burette readings"],
      ["Indicator amount varied", "Systematic small", "Endpoint shifts", "Fixed 1\u20132 drops"],
      ["Unstandardised acid", "Systematic", "Directly wrong alkalinity", "Standardise"],
      ["Temperature difference", "Systematic small", "pH shift; equilibria shift", "Record T; measure at room "
       "temperature"]],
     [48, 26, 50, 48], "**Table 7.6** Error budget.", ["l", "l", "l", "l"]),
    ("tbl", ["Symptom", "Likely cause", "Action"],
     [["Phenolphthalein shows no colour at all", "Sample is bicarbonate-only (P genuinely = 0)",
       "Record P = 0; continue to the methyl-orange endpoint"],
      ["Methyl-orange endpoint is muddy", "Indifferent indicator quality, or a strongly coloured sample",
       "Use a fresh indicator; consider a pH-meter endpoint and say so"],
      ["T is less than P", "Recording error: T is cumulative, not additional", "Re-read the burette and recalculate"],
      ["pH reading drifts continuously", "Electrode not equilibrated or not calibrated", "Recalibrate; wait for "
       "stability"],
      ["Alkalinity changes between replicates", "CO_{2} exchange with air, or inconsistent endpoint",
       "Titrate promptly and consistently"]],
     [46, 58, 66], "**Table 7.7** Troubleshooting chart.", ["l", "l", "l"]),
]

VIVA_A = [
    ("Define pH.", "pH = \u2212log_{10} a(H^{+}); in dilute solution, approximately \u2212log_{10}[H^{+}]."),
    ("What is the pH of pure water at 25 \u00b0C?", "7.00, because [H^{+}] = [OH^{\u2212}] = 1.0 \u00d7 "
                                                   "10^{\u22127} M."),
    ("Is pH 7 always neutral?", "No; neutrality corresponds to [H^{+}] = [OH^{\u2212}], and the pH of that "
                                "condition depends on temperature through K_{w}."),
    ("Define alkalinity.", "The acid-neutralising capacity of water \u2014 the amount of acid needed to reach a "
                           "defined endpoint."),
    ("Which species cause alkalinity?", "Hydroxide, carbonate and bicarbonate ions, plus contributions from other "
                                        "weak bases such as phosphate, silicate or borate."),
    ("Is alkalinity the same as pH?", "No. pH measures the current acid\u2013base state; alkalinity measures the "
                                      "capacity to neutralise acid."),
    ("What is phenolphthalein alkalinity?", "The acid volume needed to reach the phenolphthalein endpoint near pH "
                                            "8.3; it measures hydroxide plus half the carbonate."),
    ("What is total alkalinity?", "The acid volume to the methyl-orange endpoint near pH 4.5, measuring hydroxide, "
                                  "carbonate and bicarbonate together."),
    ("Why is alkalinity expressed as CaCO_{3}?", "To provide one common equivalent scale for species with "
                                                 "different molar masses."),
    ("What is the equivalent weight of CaCO_{3}?", "About 50 g eq^{\u22121}."),
    ("Why can OH^{\u2212} and HCO_{3}^{\u2212} not coexist?", "They react: OH^{\u2212} + HCO_{3}^{\u2212} "
                                                             "\u2192 CO_{3}^{2\u2212} + H_{2}O."),
    ("What are the pK_{a} values of the carbonate system?", "pK_{a1} \u2248 6.3 and pK_{a2} \u2248 10.3 at "
                                                            "25 \u00b0C."),
    ("What is a buffer?", "A solution that resists pH change on addition of small amounts of acid or base."),
    ("Why is a pH meter calibrated with two buffers?", "One sets the offset, the second sets the slope; together "
                                                       "they correct the electrode response."),
    ("How does temperature affect pH?", "K_{w} and the electrode slope both change, so both the neutral pH and the "
                                        "measured value shift."),
    ("Write the alkalinity formula.", "(V_{acid} \u00d7 N \u00d7 50 \u00d7 1000)/V_{sample} mg L^{\u22121} as "
                                      "CaCO_{3}."),
    ("What is the significance of P = 0?", "The sample has no hydroxide or carbonate alkalinity; it is "
                                           "bicarbonate-only, and all the alkalinity is measured after the "
                                           "methyl-orange endpoint."),
    ("What does P = T mean?", "The sample contains only hydroxide alkalinity (plus a negligible carbonate "
                              "contribution)."),
    ("What does P = T/2 mean?", "Carbonate-only alkalinity."),
    ("Why is alkalinity important in water treatment?", "It determines dosing requirements for coagulation, "
                                                        "disinfection and corrosion control, and it stabilises "
                                                        "pH."),
]

VIVA_B = [
    ("Why are two different indicators used?", "Because the two endpoints correspond to two distinct chemical "
                                               "stages \u2014 carbonate to bicarbonate, then bicarbonate to "
                                               "CO_{2} \u2014 and their difference reveals the species "
                                               "distribution."),
    ("Why is phenolphthalein colourless in acid?", "Its undissociated form is colourless and its deprotonated form "
                                                   "is pink; below about pH 8 it is essentially fully protonated."),
    ("Why is methyl orange yellow in base and red in acid?", "It is a weak acid whose two forms have different "
                                                             "colours; its transition spans roughly pH 3.1\u20134.4."),
    ("Why does the titration need standard acid rather than a pH meter alone?", "The classical definition of P and "
                                                                                "T is tied to those indicator "
                                                                                "endpoints; a pH-meter titration is "
                                                                                "valid but must be defined by its "
                                                                                "endpoint pH."),
    ("Why is the sample not filtered aggressively before titration?", "Filtration can remove or alter dissolved "
                                                                      "species and can exchange CO_{2}; treat the "
                                                                      "sample minimally and consistently."),
    ("Why does exposure to air change alkalinity?", "Atmospheric CO_{2} dissolves and forms carbonic acid, which "
                                                    "consumes alkalinity, or escapes and raises pH, depending on "
                                                    "the sample."),
    ("Why is a white tile used?", "The endpoints are faint colour changes; a consistent, light background makes "
                                  "them judgeable."),
    ("Why are the same number of indicator drops used each time?", "The indicators are weak acids that consume "
                                                                   "titrant; a variable indicator blank would shift "
                                                                   "the endpoint."),
    ("Why is the second endpoint recorded as a total volume?", "Because T is defined as the total acid required "
                                                               "from the original sample to reach pH 4.5, not the "
                                                               "additional acid after P."),
    ("Why can alkalinity be high while pH is near neutral?", "Because alkalinity is a capacity: a bicarbonate-rich "
                                                             "water is well buffered at near-neutral pH."),
    ("Why does boiling change alkalinity?", "Boiling drives off CO_{2} and precipitates CaCO_{3} from bicarbonate, "
                                            "reducing both temporary hardness and alkalinity."),
    ("Why do we record the sample temperature with pH?", "pH is temperature-dependent, so a pH value without a "
                                                         "temperature is incompletely specified."),
    ("Why is the electrode rinsed between samples?", "To prevent carry-over of the previous sample, which would "
                                                     "contaminate the next and shift its pH."),
    ("What is the difference between alkalinity and hardness?", "Hardness is the content of divalent metal ions; "
                                                                "alkalinity is the acid-neutralising capacity. "
                                                                "They are often correlated but are different "
                                                                "measurements."),
]

VIVA_C = [
    ("What if you used only phenolphthalein?", "You would measure P alone and could not report total alkalinity or "
                                               "apportion the species."),
    ("What if the sample were strongly coloured?", "The indicator endpoints would be hard to see; a pH-meter "
                                                   "titration with a stated endpoint pH is the practical "
                                                   "alternative."),
    ("What if the sample were left open overnight?", "CO_{2} exchange with the air would change both pH and "
                                                     "alkalinity, so the result would not represent the original "
                                                     "sample."),
    ("What if you added the methyl orange before the phenolphthalein?", "The mixed indicator colours would obscure "
                                                                        "the first endpoint; the sequence matters."),
    ("What if T came out slightly less than P?", "That is impossible for a real sample and indicates a recording "
                                                 "error, almost always the additional-versus-total confusion."),
    ("What if the acid were 0.1 N instead of 0.02 N?", "The volumes would be five times smaller, and the "
                                                       "alkalinity would be correct if the true normality were "
                                                       "used."),
    ("What if you forgot to record the sample volume?", "Alkalinity cannot be calculated, because it is a "
                                                        "concentration; the data are unusable."),
    ("What if the pH meter read 0.5 units high?", "The reported pH values would be wrong, but the alkalinity "
                                                  "titration would be unaffected because it depends on indicators "
                                                  "rather than on the meter."),
    ("What if a sample had both high hydroxide and high bicarbonate?", "It cannot \u2014 they react. The "
                                                                       "apparent coexistence would indicate a "
                                                                       "measurement or recording error."),
    ("What if you titrated only to pH 7 instead of 4.5?", "You would under-measure T, because bicarbonate is only "
                                                         "partly converted at pH 7."),
]

VIVA_D = [
    ("Why is the alkalinity of a bicarbonate solution numerically equal to its bicarbonate concentration in "
     "equivalents?", "Because each bicarbonate ion consumes exactly one proton, so one equivalent of alkalinity "
                     "corresponds to one mole of bicarbonate."),
    ("Why does carbonate contribute twice its concentration to total alkalinity?", "Because it consumes two protons "
                                                                                  "\u2014 one to become "
                                                                                  "bicarbonate and a second to "
                                                                                  "become CO_{2}."),
    ("Why is P = T/2 the signature of a carbonate-only sample?", "Half of the carbonate\u2019s two equivalents are "
                                                                 "consumed before pH 8.3, and the other half "
                                                                 "after."),
    ("Is alkalinity additive?", "Yes, for practical purposes: the contributions of independent bases sum, which is "
                                "why the apportionment table works."),
    ("What is the difference between total alkalinity and total dissolved solids?", "TDS measures all dissolved "
                                                                                   "solids; alkalinity measures only "
                                                                                   "the acid-neutralising species."),
    ("Could alkalinity be negative?", "Not physically. A negative calculated value indicates an error, often a "
                                      "sample that was already acid or a burette reading mistake."),
    ("How would you determine the carbonate and bicarbonate concentrations in mg L^{\u22121} of the actual ions?", 
     "Convert the CaCO_{3} equivalents using the ratio of molar masses: multiply the CaCO_{3} equivalent by "
     "M(ion)/(2 \u00d7 50) for divalent carbonate, or M(ion)/50 for monovalent bicarbonate."),
    ("Why is pH not a measure of total acidity or total alkalinity?", "Because it is logarithmic and reflects only "
                                                                     "the free hydrogen-ion activity, not the "
                                                                     "reservoir of buffering species."),
    ("Why might a water sample with pH 8.5 have almost no alkalinity?", "If the alkalinity is due to a small amount "
                                                                       "of a strong base such as NaOH rather than "
                                                                       "to carbonate species, the pH can be high "
                                                                       "while the capacity is low."),
    ("What happens to alkalinity during alum coagulation?", "Alum consumes alkalinity, lowering pH; that is why "
                                                            "lime is often added to restore it."),
]

CH7_CHECK = checklist(
    "7.8",
    ["pH measures intensity of acidity; alkalinity measures capacity.",
     "pH = \u2212log_{10} a(H^{+}); neutral pH depends on temperature.",
     "K_{w} = 1.0 \u00d7 10^{\u221214} at 25 \u00b0C.",
     "Alkalinity arises from OH^{\u2212}, CO_{3}^{2\u2212} and HCO_{3}^{\u2212}.",
     "Phenolphthalein endpoint \u2248 pH 8.3 gives P alkalinity.",
     "Methyl-orange endpoint \u2248 pH 4.5 gives total alkalinity T.",
     "P contains OH^{\u2212} plus half the CO_{3}^{2\u2212}.",
     "T is the cumulative acid volume from the start, not additional.",
     "pK_{a1} \u2248 6.3, pK_{a2} \u2248 10.3 for the carbonate system.",
     "OH^{\u2212} and HCO_{3}^{\u2212} cannot coexist.",
     "P = 0: bicarbonate only. P = T/2: carbonate only. P = T: hydroxide only.",
     "P < T/2: carbonate + bicarbonate. P > T/2: hydroxide + carbonate.",
     "Alkalinity (mg L^{\u22121}) = (V \u00d7 N \u00d7 50 \u00d7 1000)/V_{sample}.",
     "Equivalent weight of CaCO_{3} is about 50.",
     "The apportioned species must sum to T.",
     "Calibrate the pH meter with two buffers.",
     "Record sample temperature with pH.",
     "Titrate promptly to limit CO_{2} exchange.",
     "Indicator amount must be constant.",
     "Alkalinity and hardness are different measurements."],
    ["Define pH and alkalinity, and distinguish them.",
     "Which species cause alkalinity?",
     "What do P and T measure?",
     "Why are two indicators used?",
     "Why is alkalinity expressed as CaCO_{3}?",
     "Write the alkalinity formula.",
     "What does P = 0 tell you?",
     "What does P = T/2 tell you?",
     "Why can OH^{\u2212} and HCO_{3}^{\u2212} not coexist?",
     "Why calibrate a pH meter, and with how many buffers?"],
    ["Derive the P/T composition table from the two neutralisation stages.",
     "Explain why a water sample can have high pH and low alkalinity, with an example.",
     "Your T is smaller than your P. Diagnose, with two possible causes.",
     "Show that the apportioned OH^{\u2212}, CO_{3}^{2\u2212} and HCO_{3}^{\u2212} always sum to T.",
     "Convert a carbonate alkalinity of 240 mg L^{\u22121} as CaCO_{3} into mg L^{\u22121} of CO_{3}^{2\u2212}.",
     "Discuss the effect of temperature on both measured pH and the alkalinity definition.",
     "Why is the methyl-orange endpoint conventionally taken near pH 4.5 rather than 7?",
     "Compare an indicator-based and a pH-meter-based determination of alkalinity.",
     "How does atmospheric CO_{2} exchange bias a standing sample, and in which direction?",
     "Why is alkalinity a more useful treatment-control parameter than pH alone?"],
    [("pH vs alkalinity", "Intensity vs capacity."),
     ("P vs T", "First endpoint vs cumulative total."),
     ("Cumulative vs additional volume", "T is cumulative."),
     ("Alkalinity vs hardness", "Acid-neutralising capacity vs divalent metal content."),
     ("Neutral pH vs 7", "Neutrality is temperature-dependent."),
     ("OH^{\u2212} vs HCO_{3}^{\u2212}", "They react; never both significant."),
     ("Indicator vs meter endpoint", "Defined by pH, but measured differently."),
     ("mg L^{\u22121} as CaCO_{3} vs as ion", "Equivalent scale vs actual species mass.")],
    (["Relation", "Expression", "Note"],
     [["Water ionisation", "K_{w} = [H^{+}][OH^{\u2212}]", "10^{\u221214} at 25 \u00b0C"],
      ["pH and pOH", "pH + pOH = 14", "At 25 \u00b0C"],
      ["Carbonate equilibria", "pK_{a1} \u2248 6.3, pK_{a2} \u2248 10.3", "At 25 \u00b0C"],
      ["Alkalinity", "(V \u00d7 N \u00d7 50 \u00d7 1000)/V_{sample}", "mg L^{\u22121} as CaCO_{3}"],
      ["Apportionment", "2P, T\u22122P, 2P\u2212T, 2(T\u2212P)", "Depends on the P/T ratio"],
      ["Check", "OH + CO_{3} + HCO_{3} = T", "Always"],
      ["mg L^{\u22121} \u2194 ppm", "1 \u2248 1", "Dilute aqueous"],
      ["Ion mass conversion", "m_{ion} = eq \u00d7 M_{ion}/50", "For the monovalent case"]],
     [40, 76, 52]),
    [["Phenolphthalein shows no colour", "Genuine P = 0 (bicarbonate-only sample)"],
     ["T less than P", "T recorded as additional rather than cumulative volume"],
     ["Muddy methyl-orange endpoint", "Poor indicator or strongly coloured sample"],
     ["pH drifts during measurement", "Electrode not calibrated or not equilibrated"],
     ["Alkalinity differs between replicates", "CO_{2} exchange or inconsistent endpoint"],
     ["Reported pH inconsistent with alkalinity", "Conceptual confusion: the two measure different things"],
     ["Very high pH with tiny alkalinity", "Strong base present without carbonate buffering"]],
    ["Alkalinity is capacity; pH is intensity.",
     "T is cumulative from the start of the titration.",
     "The species must sum to T \u2014 use it as a check.",
     "OH^{\u2212} and HCO_{3}^{\u2212} cannot coexist.",
     "The P/T ratio, not the absolute values, identifies the species.",
     "Sample handling changes CO_{2} content, and therefore the answer.",
     "CaCO_{3} is the common currency of water analysis."],
    ["Recording the second endpoint as an additional volume.",
     "Adding methyl orange before phenolphthalein.",
     "Reporting pH without temperature.",
     "Using a stale buffer to calibrate.",
     "Titrating slowly with the flask open to the air.",
     "Reporting alkalinity without the CaCO_{3} basis.",
     "Claiming P and T are the same measurement."],
    ["pH and alkalinity are different things: pH is the current acid\u2013base state on a logarithmic scale, "
     "while alkalinity is the capacity of the water to neutralise acid. I first measure pH with a calibrated meter, "
     "recording the temperature. For alkalinity I titrate a measured sample with standard acid using two "
     "indicators. Phenolphthalein changes near pH 8.3 and marks the point at which all the free hydroxide and half "
     "the carbonate have been neutralised; that acid volume is P. I then add methyl orange and continue to about pH "
     "4.5, at which all the bicarbonate has been converted to carbon dioxide; the cumulative acid volume is T. From "
     "P and T I calculate both alkalinities as mg per litre of CaCO_{3}, using the equivalent weight of 50, and the "
     "ratio P/T tells me which species are present \u2014 bicarbonate only if P is zero, carbonate only if P is "
     "half of T, hydroxide only if P equals T, and mixtures in between. The critical points are that T is "
     "cumulative, that the indicator amounts are constant, and that the sample is titrated promptly so that it does "
     "not exchange carbon dioxide with the air."],
    ["**pH = intensity. Alkalinity = capacity.**",
     "**P at pH 8.3, T at pH 4.5, T cumulative.**",
     "**P/T ratio identifies the species; species must sum to T.**",
     "**Air changes the answer \u2014 titrate promptly.**"]
)

CH7 = {
    "key": "alkalinity",
    "num": "7",
    "kicker": "Experiment 7  \u00b7  Water analysis",
    "title": "pH and Alkalinity of Water",
    "toc": "pH and alkalinity of water",
    "standfirst": "Two measurements that are constantly confused with one another. This chapter separates them "
                  "cleanly, then uses the two-endpoint titration to resolve which alkaline species are present.",
    "body": B + [
        ("h2", "7.7  Viva question bank"),
        ("p", "Seventy-four answered questions, including the derivation of the composition table \u2014 the part "
              "most students memorise without understanding."),
        ("qsub", "A.  Fundamental questions"),
        ("qa", VIVA_A),
        ("qsub", "B.  \u201cWhy\u201d and \u201chow\u201d questions"),
        ("qa", VIVA_B),
        ("qsub", "C.  \u201cWhat if\u201d questions"),
        ("qa", VIVA_C),
        ("qsub", "D.  Tricky and advanced questions"),
        ("qa", VIVA_D),
        ("qsub", "E.  Further questions"),
        ("qa", VIVA_E),
    ] + CH7_CHECK,
}
