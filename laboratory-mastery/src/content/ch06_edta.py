VIVA_E = [
    ("Why is EDTA described as a hexadentate ligand?",
     "It has six donor atoms \u2014 two amine nitrogens and four carboxylate oxygens \u2014 that coordinate one metal ion."),
    ("Why is the EDTA\u2013metal complex so stable?",
     "The chelate effect: ring formation and the release of coordinated water make the formation entropically "
     "favourable."),
    ("Why is the titration slow near the endpoint?",
     "The metal must be extracted from the indicator, and that exchange takes time to establish."),
    ("Why is a small amount of magnesium sometimes added to the buffer?",
     "It provides a sharp indicator endpoint when the sample contains little magnesium."),
    ("What is the effect of a pH that is too high?",
     "Calcium and magnesium hydroxides or carbonates precipitate and are not titrated, giving a low result."),
    ("What is the effect of a pH that is too low?",
     "The fraction of Y^{4\u2212} falls, the conditional constant collapses, and the endpoint becomes poor."),
    ("What is the function of a masking agent?",
     "It complexes interfering metals so that they do not consume EDTA."),
    ("Which metals commonly interfere, and how are they masked?",
     "Iron, aluminium, copper and zinc; cyanide, triethanolamine or thioglycolate are typical masking agents."),
    ("Why is the titration performed in a conical flask and swirled?",
     "To ensure the indicator\u2013metal exchange reaches equilibrium throughout the solution."),
    ("Why is the endpoint described as wine red to blue rather than to colourless?",
     "Because the free indicator is blue in the buffered solution."),
    ("What is the equivalence weight of CaCO_{3}, and why is it 50 rather than 100?",
     "50 g eq^{−1}, because the carbonate is divalent and each mole provides two equivalents."),
    ("Why is hardness expressed as CaCO_{3} rather than as calcium?",
     "To express the total divalent-metal content on one common equivalent scale."),
    ("What is the difference between temporary and permanent hardness?",
     "Temporary hardness is bicarbonate-based and removed by boiling; permanent hardness is due to sulphates and "
     "chlorides and is not."),
    ("Why does boiling remove temporary hardness?",
     "Bicarbonate decomposes to carbonate, carbon dioxide and water, precipitating calcium carbonate."),
    ("Why does hardness matter industrially?",
     "It causes scale in boilers and heat exchangers and consumes soap."),
    ("How is hardness removed by ion exchange?",
     "Calcium and magnesium are exchanged for sodium on a resin."),
    ("What does an EDTA result higher than the expected value suggest?",
     "A stronger-than-labelled titrant, an incorrect sample volume, or an interfering metal."),
    ("What is the purpose of standardising the EDTA solution?",
     "To establish its exact concentration against a primary standard such as CaCO_{3} or a standard calcium "
     "solution."),
    ("Why is the buffer prepared from ammonia and ammonium chloride?",
     "It holds pH near 10 and also provides some complexing of trace metals."),
    ("What does a persistent purple tinge at the endpoint indicate?",
     "Incomplete metal removal from the indicator, or too much indicator."),
]

"""Chapter 6 - Total hardness of water by EDTA complexometric titration."""
from common import checklist

B = []

B += [
    ("h2", "6.1  Why hardness is measured, and what EDTA does about it"),
    ("lead", "Hard water is not dangerous, but it is expensive. It scales kettles, furrs boiler tubes, wastes soap "
             "and interferes with dyeing, brewing and many industrial processes. Measuring hardness means "
             "measuring the calcium and magnesium dissolved in the water \u2014 and the classical way to do that "
             "is to bind those ions with a molecular claw and watch an indicator change colour."),
    ("p", "The aim from the supplied material is to **determine the total hardness of a water sample by "
          "complexometric titration with EDTA.** The two hardness ions are Ca^{2+} and Mg^{2+}. At pH 10 they "
          "form a wine-red complex with the indicator Eriochrome Black T; EDTA binds them more strongly, and when "
          "the last of them is taken up by EDTA the indicator is released and the solution turns blue."),
    ("eq", "M^{2+} + H_{2}Y^{2\u2212} \u2192 [MY]^{2\u2212} + 2H^{+}    (M = Ca, Mg;   Y = EDTA anion)",
     "Equation 6.1 \u2014 the complexation. The 1:1 stoichiometry is the reason EDTA titrations are so clean, and "
     "the release of H^{+} is the reason the solution must be buffered."),
    ("defbox", [
        ("Hardness", "The capacity of water to precipitate soap, caused mainly by dissolved calcium and magnesium "
                     "salts. Reported as an equivalent concentration of CaCO_{3}."),
        ("Temporary hardness", "Hardness due to bicarbonates of calcium and magnesium, removed by boiling as "
                               "insoluble carbonates."),
        ("Permanent hardness", "Hardness due to sulphates, chlorides and nitrates, not removed by boiling; removed "
                               "by ion exchange or by chemical softening."),
        ("EDTA", "Ethylenediaminetetraacetic acid, a hexadentate chelating ligand that wraps around a metal ion "
                 "and binds it through four carboxylate oxygens and two nitrogen atoms."),
        ("Chelate", "A complex in which the ligand binds through more than one donor atom, forming rings; the "
                    "ring structure makes the complex unusually stable."),
        ("Metallochromic indicator", "A dye that forms a coloured complex with a metal ion and changes colour when "
                                     "the metal is removed from it \u2014 here, Eriochrome Black T."),
        ("Masking agent", "A reagent that selectively binds an interfering ion so it cannot react with the "
                          "titrant."),
    ]),
    ("box", "key", [
        "**1:1 stoichiometry** between metal ion and EDTA, regardless of the charge on the metal, because each "
        "EDTA molecule provides six donor atoms.",
        "**pH 10 is mandatory**, because both the complex formation and the indicator colour depend on pH. Below "
        "about pH 9 the endpoint is poor; above about pH 11 magnesium hydroxide begins to precipitate.",
        "**The colour sequence is wine red \u2192 blue**, and the correct endpoint is a //pure// blue with no "
        "purple tinge.",
        "**Hardness is reported as CaCO_{3}** so that different salt compositions can be compared on one scale.",
    ], "Four ideas that make the experiment work"),
    ("fig", "edta", "**Figure 6.1** The indicator colour change. Before equivalence, the metal is held by the "
                    "indicator and the solution is wine red; at equivalence EDTA has taken the metal and free "
                    "indicator is blue."),
]

B += [
    ("h2", "6.2  Theory, from chelation to the CaCO_{3} scale"),
    ("h3", "6.2.1  Why EDTA binds so strongly"),
    ("p", "EDTA^{4\u2212} has six donor atoms \u2014 two amine nitrogens and four carboxylate oxygens \u2014 "
          "arranged so that it can wrap around a metal ion and satisfy much of its coordination sphere. Because "
          "binding occurs through several atoms at once, the **chelate effect** applies: the entropy gain "
          "associated with releasing several water molecules and forming intramolecular rings makes the formation "
          "constant very large (log K typically 8\u201311 for Ca^{2+} and Mg^{2+} at pH 10)."),
    ("p", "That large constant is what makes a sharp endpoint possible: EDTA takes the metal from the indicator "
          "essentially completely at equivalence, so the colour change is abrupt rather than gradual."),
    ("h3", "6.2.2  The conditional formation constant and why pH matters"),
    ("p", "EDTA is a polyprotic acid, so the fraction of it present as the fully deprotonated Y^{4\u2212} depends "
          "on pH. The //conditional// formation constant is the product of the absolute constant and that "
          "fraction:"),
    ("eq", "K\u2032_{MY} = K_{MY} \u00d7 \u03b1(Y^{4\u2212}) at that pH",
     "Equation 6.2 \u2014 the conditional constant. At pH 10, \u03b1 is large enough that Ca^{2+} and Mg^{2+} are "
     "quantitatively bound; at pH 4, it is far too small and no sharp endpoint is possible."),
    ("p", "This is the quantitative reason for the buffer, and it is the answer an examiner wants when they ask "
          "\u201cwhy pH 10 and not just any pH?\u201d There is a second, competing reason: above about pH 11, "
          "magnesium begins to precipitate as Mg(OH)_{2}, removing it from solution and giving a falsely low "
          "hardness. pH 10 is the compromise where both ions are bound by EDTA and neither is precipitated."),
    ("h3", "6.2.3  The indicator mechanism, in three equilibria"),
    ("p", "Eriochrome Black T (EBT) is itself a weak acid with several protonation states, and it forms a "
          "1:1 complex with Ca^{2+} and Mg^{2+} that is **wine red**. The sequence during titration is:"),
    ("num", [
        "**Before titration:** M^{2+} + EBT \u21cc [M\u2013EBT] (wine red). Some metal is bound to indicator, most "
        "is free in solution.",
        "**During titration:** EDTA preferentially binds free M^{2+}, because the free metal is in vast excess "
        "over the tiny amount bound to indicator.",
        "**At equivalence:** the last of the free metal is consumed and EDTA strips the metal from the indicator, "
        "releasing free EBT, which is **blue**. The colour change is therefore abrupt.",
    ]),
    ("p", "Two practical consequences follow. First, the indicator must be present in **small, consistent "
          "amounts**: it competes with EDTA for the metal, so an excess delays the endpoint and dulls the colour "
          "change. Second, the Mg^{2+} content matters: EBT binds Mg^{2+} more sharply than Ca^{2+}, and a trace "
          "of magnesium is needed for a crisp endpoint. In practice the buffer or the indicator preparation often "
          "supplies it."),
    ("h3", "6.2.4  The CaCO_{3} scale"),
    ("p", "Hardness is conventionally expressed as the mass of CaCO_{3} that would give the same number of "
          "equivalents of divalent ions. Since CaCO_{3} has an equivalent weight of 100.09/2 = 50.04 g eq^{\u22121}:"),
    ("eq", "Hardness (mg L^{\u22121} as CaCO_{3}) = N_{sample} \u00d7 50 \u00d7 1000 = N_{sample} \u00d7 50,000",
     "Equation 6.3 \u2014 the expression given in the supplied manual, where N_{sample} is the normality of the "
     "hardness ions in the titrated sample. Using 50 (rather than 50.04) is the conventional teaching "
     "approximation."),
    ("p", "Working the other way, if you titrate a measured volume V (mL) of water with EDTA of normality N and "
          "titre V_{e} (mL):"),
    ("eq", "Hardness (mg L^{\u22121}) = (N \u00d7 V_{e} \u00d7 50 \u00d7 1000)/V",
     "Equation 6.4 \u2014 the practical form used for an unknown sample, in which 50 is the equivalent weight of "
     "CaCO_{3} divided by 1000 and the factor 1000 converts mL to L."),
    ("tbl", ["Classification", "Hardness (mg L^{\u22121} as CaCO_{3})", "Practical consequence"],
     [["Soft", "0\u201360", "Lathers easily; low scaling potential"],
      ["Moderately hard", "61\u2013120", "Some soap consumption; slight scaling"],
      ["Hard", "121\u2013180", "Noticeable scaling; higher soap use"],
      ["Very hard", "> 180", "Significant scaling and soap consumption; treatment usually required"]],
     [40, 56, 74], "**Table 6.1** Conventional hardness classification. The bands are conventional rather than "
                   "universal; different authorities use slightly different cut-offs, which is worth saying if "
                   "asked.", ["l", "c", "l"]),
]

B += [
    ("h2", "6.3  Apparatus and reagents"),
    ("tbl", ["Item", "Function", "If it is faulty or missing"],
     [["Burette + stand", "Delivers EDTA", "Leaks and bubbles bias every titre"],
      ["Pipette (20 mL)", "Delivers the water sample", "A wrong aliquot scales hardness directly"],
      ["Conical flasks", "Hold sample and allow swirling", "Contamination adds or removes hardness ions"],
      ["EDTA solution (~0.01 M)", "The titrant/chelating agent", "Must be standardised before use"],
      ["Ammonia buffer (pH 10)", "Holds the pH where both ions are bound and the indicator works",
       "Without it the endpoint is poor or absent"],
      ["Eriochrome Black T indicator", "Signals the endpoint by colour change",
       "Stale indicator gives a weak, late endpoint"],
      ["Standard hard water / CaCO_{3} standard", "Standardises the EDTA", "Without it the EDTA normality is "
       "unknown"],
      ["Distilled water", "Dilution and rinsing", "Tap water adds hardness"],
      ["White tile / paper", "Background for judging the colour", "Endpoint colour is much harder to judge"]],
     [44, 58, 68], "**Table 6.2** Apparatus and reagents.", ["l", "l", "l"]),
    ("box", "warn", [
        "The ammonia buffer is alkaline and gives off ammonia vapour; prepare and use it in a fume hood or "
        "well-ventilated area, and never add acid to it directly. Eriochrome Black T stains skin and clothing. "
        "EDTA solutions are not acutely hazardous but should be disposed of through the laboratory\u2019s aqueous "
        "waste route.",
    ], "Handling"),
]

B += [
    ("h2", "6.4  Procedure with reasoning"),
    ("h3", "Part A \u2014 Standardise the EDTA"),
    ("num", [
        "**Pipette a measured volume of standard hard water** (the supplied material notes 10 mL) into a conical "
        "flask.",
        "**Add about 1\u20132 mL of pH 10 ammonia buffer**, then a small, consistent quantity of Eriochrome Black T. "
        "The solution should turn wine red; if it does not, either the pH is wrong or the indicator is inactive.",
        "**Titrate with EDTA**, swirling continuously, until the wine red changes to a **pure blue** with no "
        "residual purple tinge.",
        "**Record the titre** and repeat until concordant.",
        "**Calculate the EDTA normality** from N_{1}V_{1} = N_{2}V_{2}, using the known hardness of the standard.",
    ]),
    ("h3", "Part B \u2014 Titrate the unknown"),
    ("num", [
        "**Pipette the same volume of the unknown water sample** into a clean flask.",
        "**Add the same volume of buffer and the same amount of indicator** so the endpoint criterion is identical.",
        "**Titrate with the same EDTA solution** to the same pure blue.",
        "**Repeat to concordance**, then calculate the hardness in mg L^{\u22121} as CaCO_{3}.",
    ]),
    ("box", "pitfall", [
        "**The endpoint is judged by hue, not by darkness.** A purple tinge means you have not reached the true "
        "endpoint; a violet-blue that continues to darken means you have passed it. Both are errors, and they "
        "point in opposite directions. Practise the colour change once on a standard before you begin the unknown.",
        "**Adding indicator to a solution at the wrong pH** is the most common reason for \u201cno endpoint at "
        "all\u201d. If the solution is not wine red after the indicator is added, check the buffer first.",
    ], "Two endpoint failures and their causes"),
    ("box", "note", [
        "**Why is the buffer added before the indicator?** Because the indicator\u2019s colour and its affinity for "
        "the metal both depend on pH. Adding indicator to an unbuffered sample and then buffering can leave the "
        "dye in the wrong protonation state and the colour change unreliable.",
        "**Why is the amount of indicator kept small and constant?** Because EBT binds some metal itself. A "
        "variable indicator blank shifts the endpoint by an amount comparable to the differences you are trying "
        "to measure.",
    ], "Two procedural points worth marks"),
]

B += [
    ("h2", "6.5  Observations and calculation"),
    ("tbl", ["S. No.", "Volume of sample (mL)", "Initial burette (mL)", "Final burette (mL)",
             "EDTA titre (mL)", "Endpoint colour"],
     [["1", "10.0 / 20.0", "", "", "", "pure blue"],
      ["2", "10.0 / 20.0", "", "", "", "pure blue"],
      ["3", "10.0 / 20.0", "", "", "", "pure blue"]],
     [14, 36, 34, 34, 30, 22],
     "**Table 6.3** Observation table. Record the sample volume you actually used; the supplied material mentions "
     "10 mL of standard hard water, and 20 mL is common for the unknown. The table is blank because the source "
     "tables are blank.", ["c", "c", "c", "c", "c", "c"]),
    ("h3", "6.5.1  Worked illustration"),
    ("p", "Suppose 20.0 mL of the unknown required a mean of 8.4 mL of EDTA standardised to 0.0100 M (0.0100 N "
          "under the 1:1 convention for a divalent ion pair)."),
    ("eq", "N_{sample} = (N_{EDTA} \u00d7 V_{EDTA})/V_{sample} = (0.0100 \u00d7 8.4)/20.0 = 4.20 \u00d7 "
           "10^{\u22123} N"),
    ("eq", "Hardness = N_{sample} \u00d7 50,000 = 4.20 \u00d7 10^{\u22123} \u00d7 50,000 = 210 mg L^{\u22121} "
           "as CaCO_{3}"),
    ("p", "That places the sample in the \u201cvery hard\u201d band. Note that the arithmetic is an illustration "
          "only; the numbers are chosen for convenience and are not measurements. Note also that 210 mg L^{\u22121} "
          "is plausible for hard groundwater \u2014 which is a useful sanity check to mention, because a result of "
          "21,000 mg L^{\u22121} signals a decimal slip, not a remarkable well."),
    ("tbl", ["Quantity", "Expression", "Illustrative value"],
     [["EDTA concentration", "standardised", "0.0100 N"],
      ["Sample volume", "pipetted", "20.0 mL"],
      ["Mean EDTA titre", "concordant readings", "8.4 mL"],
      ["Sample normality", "N_{E}V_{E}/V_{S}", "4.20 \u00d7 10^{\u22123} N"],
      ["Hardness as CaCO_{3}", "N \u00d7 50,000", "210 mg L^{\u22121}"],
      ["Classification", "see Table 6.1", "very hard"]],
     [44, 68, 56], "**Table 6.4** Calculation chain.", ["l", "l", "c"]),
]

B += [
    ("h2", "6.6  Precautions, errors and troubleshooting"),
    ("bul", [
        "Add the buffer before the indicator, and check that the solution is wine red before titrating.",
        "Use the same indicator quantity and the same buffer volume in every flask.",
        "Judge the endpoint as pure blue, on a white background, and use the same lighting.",
        "Standardise the EDTA against the standard hard water in the same session.",
        "Rinse all glassware with distilled water, never tap water.",
        "Titrate reasonably promptly; prolonged standing at pH 10 can allow CaCO_{3} to precipitate.",
        "Record the sample volume actually used.",
        "Handle the ammonia buffer in a ventilated area.",
    ]),
    ("tbl", ["Source of error", "Type", "Effect on reported hardness", "Control"],
     [["pH too low", "Systematic", "Weak or late endpoint; low result", "Fresh pH 10 buffer"],
      ["pH too high (> 11)", "Systematic", "Mg(OH)_{2} precipitates; low result", "Do not over-add alkali"],
      ["Excess indicator", "Systematic", "Late, dull endpoint", "Small consistent quantity"],
      ["Endpoint overshoot", "Systematic (positive)", "High result", "Approach the blue dropwise"],
      ["Endpoint not reached (purple)", "Systematic (negative)", "Low result", "Recognise pure blue correctly"],
      ["Untitrated interfering ions (Fe, Al, Cu)", "Systematic", "Variable; often low because they block the "
       "indicator", "Masking agent as specified"],
      ["Contaminated glassware", "Random/systematic", "Variable", "Distilled-water rinse"],
      ["EDTA not standardised", "Systematic", "Directly wrong result", "Standardise against standard hard water"],
      ["Delay before titration", "Systematic", "Precipitation of CaCO_{3}", "Titrate promptly"]],
     [46, 26, 50, 48], "**Table 6.5** Error budget, with the direction of bias \u2014 which is what examiners "
                   "ask for.", ["l", "l", "l", "l"]),
    ("tbl", ["Symptom", "Likely cause", "Action"],
     [["No wine-red colour after the indicator", "pH wrong, or indicator inactive", "Re-check the buffer; use "
       "fresh indicator"],
      ["Endpoint fades back to red", "Metal slowly released from the indicator, or insufficient EDTA added",
       "Continue dropwise; a genuine endpoint holds"],
      ["Endpoint is grey or muddy", "Interfering ions, or too much indicator", "Use the prescribed masking "
       "procedure; reduce indicator"],
      ["Titre much larger than expected", "Sample is genuinely harder, or the EDTA is weaker than assumed",
       "Standardise the EDTA"],
      ["Precipitate in the flask", "pH too high (Mg(OH)_{2}) or carbonate precipitation", "Use fresh buffer; "
       "titrate promptly"],
      ["Titres drift upward across replicates", "Solution standing too long, or CO_{2} uptake", "Titrate "
       "immediately after buffering"]],
     [46, 58, 66], "**Table 6.6** Troubleshooting chart.", ["l", "l", "l"]),
]

VIVA_A = [
    ("What is water hardness?", "The property of water arising mainly from dissolved calcium and magnesium ions, "
                                "measured as the equivalent concentration of CaCO_{3}."),
    ("Which ions cause hardness?", "Principally Ca^{2+} and Mg^{2+}; other divalent and trivalent ions can "
                                   "contribute but are usually minor."),
    ("What is temporary hardness?", "Hardness due to bicarbonates, removed by boiling as insoluble carbonates."),
    ("What is permanent hardness?", "Hardness due to sulphates, chlorides and nitrates, not removed by boiling; "
                                    "removed by ion exchange or softening."),
    ("What does EDTA stand for?", "Ethylenediaminetetraacetic acid."),
    ("Why is EDTA called a chelating agent?", "Because it binds a metal ion through several donor atoms at once, "
                                              "forming ring structures (chelates)."),
    ("How many donor atoms does EDTA have?", "Six: two nitrogen atoms and four carboxylate oxygens."),
    ("What is the metal-to-EDTA ratio?", "1:1 for Ca^{2+} and Mg^{2+}, irrespective of the metal charge, because "
                                         "one EDTA molecule satisfies the coordination requirement."),
    ("Why is the titration carried out at pH 10?", "Because that is where both the EDTA complex formation and the "
                                                   "indicator colour change are quantitative and sharp."),
    ("What is the role of the buffer?", "To maintain pH 10 throughout the titration despite the H^{+} released by "
                                        "complex formation."),
    ("What is Eriochrome Black T?", "A metallochromic indicator that forms a wine-red complex with Ca^{2+} and "
                                    "Mg^{2+} and is blue when free."),
    ("What is the initial colour?", "Wine red, from the metal\u2013indicator complex."),
    ("What is the endpoint colour?", "Pure blue, when EDTA has taken the metal and the indicator is released."),
    ("Why is hardness expressed as CaCO_{3}?", "To provide a common equivalent basis so that waters of different "
                                               "ionic composition can be compared."),
    ("What does ppm mean here?", "Parts per million; for dilute aqueous solutions this is approximately mg L^{\u22121}."),
    ("What is the equivalent weight of CaCO_{3}?", "100.09/2 \u2248 50 g eq^{\u22121}, since the carbonate is "
                                                   "divalent."),
    ("Why is EDTA standardised?", "Because its exact concentration may not be known accurately from preparation, "
                                  "and the result depends directly on it."),
    ("What is used to standardise EDTA?", "A standard hard water of known CaCO_{3} equivalent (or a standard "
                                          "calcium solution)."),
    ("What is a masking agent?", "A reagent that selectively binds an interfering ion, preventing it from reacting "
                                 "with EDTA or the indicator."),
    ("Which ions interfere, and how?", "Fe^{3+}, Al^{3+}, Cu^{2+}, Zn^{2+} and others compete for EDTA or block the "
                                       "indicator, giving low or erratic results."),
    ("What is the formula for hardness in mg L^{\u22121}?", "(N \u00d7 V_{e} \u00d7 50 \u00d7 1000)/V_{sample}, "
                                                            "where N and V_{e} refer to EDTA."),
]

VIVA_B = [
    ("Why must the buffer be added before the indicator?", "The indicator\u2019s colour and its metal affinity "
                                                           "depend on pH; adding it at the wrong pH gives the wrong "
                                                           "starting colour and an unreliable endpoint."),
    ("Why is ammonia buffer used rather than NaOH?", "NaOH would take the pH above 11, precipitating Mg(OH)_{2}; the "
                                                     "ammonia/ammonium chloride buffer holds pH near 10 without "
                                                     "that risk."),
    ("Why does the indicator amount matter?", "EBT binds some metal itself, so an excess consumes EDTA and delays "
                                              "the endpoint; the amount must be small and constant."),
    ("Why is a trace of magnesium sometimes needed?", "EBT gives a sharper colour change with Mg^{2+} than with "
                                                      "Ca^{2+} alone; a trace ensures a crisp endpoint."),
    ("Why must the endpoint be judged as pure blue?", "Because purple means unreacted metal remains on the "
                                                      "indicator, while an over-titrated violet indicates excess "
                                                      "EDTA; both bias the result."),
    ("Why is the titration performed promptly after buffering?", "At pH 10 calcium carbonate can slowly "
                                                                 "precipitate, which removes hardness ions from "
                                                                 "solution and lowers the titre."),
    ("Why is the sample volume important?", "Hardness is a concentration, so the moles of EDTA consumed must be "
                                            "divided by the volume titrated."),
    ("Why does the complex release H^{+}?", "The metal binds to the deprotonated carboxylate groups; the protons "
                                            "they carried are released into solution, which is why buffering is "
                                            "needed."),
    ("Why is the conditional formation constant useful?", "It expresses the effective binding strength at a given "
                                                          "pH, which is what actually determines whether the "
                                                          "titration is quantitative."),
    ("Why can EDTA titrate a mixture of Ca^{2+} and Mg^{2+} in one step?", "Because both form 1:1 complexes of "
                                                                          "similar stability at pH 10, so the "
                                                                          "titration measures total hardness."),
    ("How would you determine calcium alone?", "Titrate at high pH (about 12\u201313) where magnesium precipitates "
                                               "as Mg(OH)_{2}; the titre then corresponds to calcium only, and "
                                               "magnesium is obtained by difference."),
    ("Why is distilled water used to rinse glassware?", "Tap water contains hardness ions, which would add to the "
                                                        "sample and inflate the result."),
    ("Why is a white background used?", "To make the faint colour difference between wine red, purple and blue "
                                        "detectable."),
    ("Why do we standardise EDTA rather than weighing it directly?", "EDTA is often used as its disodium salt, "
                                                                     "which is slightly hygroscopic, and its "
                                                                     "purity varies; standardisation against a "
                                                                     "known hardness is more reliable."),
    ("What is the effect of temperature on the titration?", "Formation constants and indicator equilibria depend "
                                                           "on temperature; large differences can shift the "
                                                           "endpoint, so samples should be at a consistent "
                                                           "temperature."),
]

VIVA_C = [
    ("What if you forgot the buffer?", "The pH would fall as the titration proceeded, the indicator would not "
                                       "function properly, and the endpoint would be late, indistinct or absent, "
                                       "giving a low result."),
    ("What if the pH were 12?", "Mg(OH)_{2} would precipitate, removing magnesium from the titration and giving a "
                                "falsely low hardness; the indicator would also behave differently."),
    ("What if you added ten times too much indicator?", "The indicator blank would consume EDTA and the colour "
                                                        "change would be slow and dull, biasing the endpoint "
                                                        "upward."),
    ("What if you stopped at purple?", "You would be short of the true endpoint, so the titre and the reported "
                                       "hardness would both be too low."),
    ("What if you overshot to deep blue-violet?", "You would have added excess EDTA, giving a titre and hardness "
                                                  "that are too high."),
    ("What if the sample contained iron(III)?", "It would compete for EDTA and block the indicator, generally "
                                                "causing a low and sluggish endpoint; a masking agent such as "
                                                "triethanolamine is used to suppress it."),
    ("What if the EDTA solution were 10 % weaker than labelled?", "The titre would be 10 % larger and the reported "
                                                                 "hardness 10 % too high \u2014 a purely "
                                                                 "systematic error, invisible without "
                                                                 "standardisation."),
    ("What if you titrated a 10 mL sample but calculated as 20 mL?", "The reported hardness would be half the true "
                                                                   "value."),
    ("What if the sample was left standing for an hour after buffering?", "Calcium carbonate may precipitate, "
                                                                         "lowering the titre and the reported "
                                                                         "hardness."),
    ("What if the water sample was turbid?", "Suspended matter can obscure the endpoint and may adsorb or release "
                                            "ions; filter and note the treatment."),
    ("What if the endpoint returned to red after 30 seconds?", "That usually indicates an incompletely "
                                                               "established endpoint or slow release of metal from "
                                                               "the indicator; continue dropwise until the blue "
                                                               "holds."),
]

VIVA_D = [
    ("Is \u201chardness\u201d a single chemical species?", "No \u2014 it is an operational sum of divalent "
                                                          "metal concentrations expressed as CaCO_{3}; the actual "
                                                          "species vary with the water source."),
    ("Why is the endpoint not at the equivalence point exactly?", "Because the indicator itself binds a small "
                                                                 "amount of metal, and a finite excess of EDTA is "
                                                                 "needed to strip it; the indicator blank is the "
                                                                 "difference between endpoint and equivalence."),
    ("Why does EBT change colour at all?", "Protonation and metal binding change the electronic structure of the "
                                           "dye, shifting its absorption band; the free and complexed forms have "
                                           "different colours."),
    ("Would you use EDTA for a monovalent ion such as Na^{+}?", "Not usefully \u2014 the formation constant is far "
                                                                "too small; EDTA is suited to di- and trivalent "
                                                                "cations."),
    ("What is the difference between total, calcium and magnesium hardness?", "Total is Ca plus Mg; calcium "
                                                                             "hardness is measured at high pH where "
                                                                             "Mg is precipitated; magnesium hardness "
                                                                             "is the difference."),
    ("Why is the result quoted to the nearest mg L^{\u22121} rather than to five figures?", "Because the titre "
                                                                                           "precision and the "
                                                                                           "indicator blank limit "
                                                                                           "the accuracy; "
                                                                                           "over-precision is a false "
                                                                                           "claim."),
    ("How does ion exchange soften water?", "Calcium and magnesium are exchanged for sodium on a resin; the "
                                            "hardness ions are retained and later eluted with brine."),
    ("Why does hardness matter industrially?", "It scales heat exchangers and boilers, increases soap consumption, "
                                              "and interferes with textile dyeing, brewing and photographic "
                                              "processing."),
    ("How would you choose a masking agent?", "It must bind the interferent more strongly than EDTA or the "
                                              "indicator does, without binding the analyte; common choices are "
                                              "triethanolamine for Fe and Al, and cyanide for Cu, Ni, Co (used "
                                              "only under strict safety controls)."),
    ("What is the significance of log K \u2248 10.7 for Ca\u2013EDTA?", "It indicates quantitative binding at "
                                                                       "suitable pH, giving a sharp endpoint; a "
                                                                       "much smaller constant would make the "
                                                                       "titration impossible."),
]

CH6_CHECK = checklist(
    "6.8",
    ["Hardness is caused mainly by Ca^{2+} and Mg^{2+}.",
     "EDTA is a hexadentate chelating ligand (4 O, 2 N).",
     "Metal\u2013EDTA stoichiometry is 1:1.",
     "Complexation releases H^{+}, hence the need for a buffer.",
     "pH 10 is required for quantitative binding and a sharp endpoint.",
     "Above pH 11, Mg(OH)_{2} precipitates and magnesium is lost.",
     "Eriochrome Black T is wine red when bound to metal, blue when free.",
     "Endpoint: wine red \u2192 pure blue, dropwise.",
     "Excess indicator shifts the endpoint and dulls the colour.",
     "Standardise EDTA against standard hard water in the same session.",
     "1 ppm in dilute water \u2248 1 mg L^{\u22121}.",
     "Hardness is expressed as CaCO_{3} for comparability.",
     "Equivalent weight of CaCO_{3} is about 50 g eq^{\u22121}.",
     "Hardness (mg L^{\u22121}) = N \u00d7 50,000 for a sample where N is the sample normality.",
     "Practical form: (N_{EDTA}V_{EDTA} \u00d7 50 \u00d7 1000)/V_{sample}.",
     "Temporary hardness is bicarbonate-based; permanent is not.",
     "Interfering ions: Fe^{3+}, Al^{3+}, Cu^{2+}, Zn^{2+}.",
     "Titrate promptly after buffering to avoid CaCO_{3} precipitation.",
     "Distilled water only, for all rinsing.",
     "Hardness bands: soft < 60, very hard > 180 mg L^{\u22121}."],
    ["Why is hardness expressed as CaCO_{3}?",
     "Why is pH 10 maintained, and what goes wrong above and below it?",
     "What is the role of the buffer?",
     "Why is Eriochrome Black T used, and what are its two colours?",
     "What is the stoichiometry of the metal\u2013EDTA complex?",
     "Why is the indicator amount kept small?",
     "How is EDTA standardised?",
     "What causes interference, and how is it handled?",
     "Distinguish temporary and permanent hardness.",
     "Write the formula for hardness in mg L^{\u22121}."],
    ["Explain, with the conditional formation constant, why pH 10 and not pH 7.",
     "Why does an indicator blank exist, and in which direction does it bias the result?",
     "Design a procedure to determine calcium and magnesium separately, with the arithmetic.",
     "Your result is 30 % below the expected value. Give four causes and the diagnostic for each.",
     "Explain the chelate effect and why it makes the endpoint sharp.",
     "Why is a trace of magnesium often beneficial, and what happens if there is none?",
     "How would you treat a sample containing 5 mg L^{\u22121} iron(III)?",
     "Show that a 1:1 stoichiometry applies to both Ca^{2+} and Mg^{2+} despite the charge difference.",
     "What is the numerical effect of using 50.04 instead of 50 in the hardness formula?",
     "Compare EDTA titration with the soap-titration method for hardness."],
    [("Temporary vs permanent hardness", "Bicarbonates (boiling) vs other salts (not by boiling)."),
     ("EDTA vs indicator binding", "EDTA binds more strongly, which is why it strips the metal."),
     ("Endpoint vs equivalence", "Indicator blank displaces the endpoint slightly."),
     ("Wine red vs blue", "Metal-bound vs free indicator."),
     ("Total vs calcium hardness", "Both ions vs calcium only at pH 12\u201313."),
     ("purity vs concentration of EDTA", "Standardisation corrects for both."),
     ("mg L^{\u22121} vs ppm", "Numerically equal for dilute water."),
     ("Masking vs sequestering", "Masking hides the interferent from the titration.")],
    (["Relation", "Expression", "Note"],
     [["Complexation", "M^{2+} + H_{2}Y^{2\u2212} \u2192 [MY]^{2\u2212} + 2H^{+}", "1:1"],
      ["Conditional constant", "K\u2032 = K \u00d7 \u03b1(Y^{4\u2212})", "pH-dependent"],
      ["Standardisation", "N_{1}V_{1} = N_{2}V_{2}", "EDTA vs standard hard water"],
      ["Hardness (normality form)", "Hardness = N \u00d7 50 \u00d7 1000", "mg L^{\u22121} as CaCO_{3}"],
      ["Hardness (practical)", "(N_{E}V_{E} \u00d7 50 \u00d7 1000)/V_{S}", "For a measured aliquot"],
      ["mg L^{\u22121} \u2194 ppm", "1 mg L^{\u22121} \u2248 1 ppm", "Dilute aqueous"],
      ["Equivalent weight CaCO_{3}", "100.09/2 \u2248 50.04", "Conventionally 50"],
      ["Total hardness", "Ca hardness + Mg hardness", "By difference"]],
     [42, 72, 54]),
    [["No wine red colour after indicator", "Wrong pH or inactive indicator"],
     ["Endpoint fades back to red", "Endpoint not yet reached; metal releasing from indicator"],
     ["Muddy grey endpoint", "Interfering ions or excess indicator"],
     ["Precipitate in the flask", "pH too high (Mg(OH)_{2}) or CaCO_{3} formation"],
     ["Titre larger than expected", "Harder sample or weaker EDTA"],
     ["Titre rises across replicates", "Solution standing before titration"],
     ["Result exactly half the expected value", "Sample volume used in the calculation is double the actual"]],
    ["pH 10 is a quantitative requirement, not a convention.",
     "The indicator itself consumes EDTA \u2014 keep it small and constant.",
     "Wine red means metal on indicator; pure blue means it has been stripped.",
     "Standardise in the same session; EDTA and buffer both age.",
     "CaCO_{3} is a reporting scale, not the species present.",
     "Titrate promptly after buffering.",
     "The direction of the bias matters as much as the cause."],
    ["Omitting the buffer or adding it after the indicator.",
     "Titrating past pure blue into violet.",
     "Using a variable amount of indicator between flasks.",
     "Forgetting to standardise the EDTA.",
     "Rinsing glassware with tap water.",
     "Reporting mg L^{\u22121} without stating the CaCO_{3} basis.",
     "Leaving the buffered sample standing before titration."],
    ["I determine total hardness by complexometric titration with EDTA. The hardness ions are calcium and "
     "magnesium. I buffer a measured water sample to pH 10 with an ammonia buffer, because that is where EDTA "
     "binds both ions quantitatively and where the indicator works; above about pH 11 magnesium would precipitate "
     "as hydroxide and be lost. I add a small, fixed amount of Eriochrome Black T, which forms a wine-red complex "
     "with the metal ions. I then titrate with standardised EDTA; EDTA binds the free metal ions one-to-one, and "
     "at the endpoint it strips the metal from the indicator, so the solution turns from wine red to pure blue. I "
     "standardise the EDTA beforehand against a standard hard water of known CaCO_{3} equivalent, because the "
     "result depends directly on the titrant concentration. Finally I express the hardness as mg per litre of "
     "CaCO_{3}, using the equivalent weight of 50, so that waters of different composition can be compared. The "
     "critical controls are the buffer, a small constant indicator amount, genuine pure blue as the endpoint, "
     "prompt titration, and distilled water throughout."],
    ["**Buffer to pH 10 \u2192 indicator \u2192 wine red \u2192 EDTA \u2192 pure blue.**",
     "**1:1 metal:EDTA, whatever the charge.**",
     "**CaCO\u2083 is the reporting currency; 50 g per equivalent.**",
     "**Above pH 11, magnesium disappears as hydroxide.**"]
)

CH6 = {
    "key": "edta",
    "num": "6",
    "kicker": "Experiment 6  \u00b7  Complexometric titration",
    "title": "Total Hardness of Water by the EDTA Method",
    "toc": "Total hardness of water by EDTA",
    "standfirst": "A molecular claw, a colour change, and a pH window narrow enough that getting it wrong makes "
                  "the experiment impossible. This chapter explains why both are essential.",
    "body": B + [
        ("h2", "6.7  Viva question bank"),
        ("p", "Seventy-seven answered questions on chelation, the pH window, the indicator blank and the CaCO_{3} "
              "arithmetic."),
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
    ] + CH6_CHECK,
}
