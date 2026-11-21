VIVA_E = [
    ("Why is a conical flask used rather than a beaker?",
     "Its sloping sides allow swirling without loss, and the narrow neck reduces splashing."),
    ("Why is the flask rinsed with distilled water rather than titrant?",
     "Rinsing with titrant would add unmeasured moles and bias the result."),
    ("Why must the pipette be rinsed with the solution it will deliver?",
     "Residual water in the pipette would dilute the aliquot and change the delivered amount."),
    ("What is a meniscus and which part do you read?",
     "The curve of the liquid surface; the bottom of the meniscus is read at eye level."),
    ("Why is a white tile placed under the flask?",
     "It makes the indicator colour change easier to judge consistently."),
    ("What does the term \u2018concordant\u2019 mean?",
     "Readings that agree within a small, stated tolerance, typically 0.1 mL."),
    ("Why is a rough titration performed first?",
     "To estimate the endpoint volume so that subsequent titrations can be done quickly to just before it."),
    ("Why is the last portion of titrant added dropwise?",
     "To avoid overshooting a single-drop endpoint."),
    ("What is the difference between a standard solution and a standardised solution?",
     "A standard is prepared to a known concentration by weighing; a standardised solution has its concentration "
     "determined against a standard."),
    ("Why is the molar mass of oxalic acid dihydrate 126.07 rather than 90.04?",
     "Because the dihydrate includes two water molecules in the formula unit."),
    ("What is the consequence of using the anhydrous molar mass by mistake?",
     "The calculated molarity would be about 40 % too high, because the same mass contains fewer moles than "
     "assumed."),
    ("Why is phenolphthalein colourless in acid but pink in base?",
     "Its deprotonated form has an extended conjugated system that absorbs in the visible region."),
    ("Why is the indicator added in small, constant amount?",
     "The indicator itself is a weak acid and consumes a little titrant."),
    ("What is an indicator blank and when does it matter?",
     "The volume of titrant consumed by the indicator; it matters when the titre is small."),
    ("Why does the endpoint not always coincide with the equivalence point?",
     "Because the indicator changes over a pH range rather than at a single point."),
    ("Why is the result quoted to the correct number of significant figures?",
     "Because the precision of the volumetric glassware limits the meaningful digits."),
    ("How would you check the calibration of a 25 mL pipette?",
     "By delivering distilled water and weighing it, then converting mass to volume using the density."),
    ("What is the effect of a bubble in the burette tip?",
     "It is delivered as part of the titre, so the recorded volume overstates the true volume of titrant."),
    ("Why should the burette be read after a short pause?",
     "To let the film of liquid on the walls drain, so the reading is stable."),
    ("Why is temperature control less critical in acid\u2013base titration than in some other measurements?",
     "Because both the titrant concentration and the sample volume change slightly and partly cancel, and no "
     "physical constant is being measured."),
]

"""Chapter 5 - Standardisation of NaOH and determination of HCl strength."""
from common import checklist

B = []

B += [
    ("h2", "5.1  The experiment every other titration depends on"),
    ("lead", "You cannot know an unknown concentration using a titrant whose own concentration you do not know. "
             "This chapter is therefore the foundation of the volumetric experiments: it establishes the strength "
             "of sodium hydroxide against a primary standard, and then uses that standardised base to assay an "
             "unknown acid."),
    ("p", "The supplied material sets the aim as two linked tasks: **standardise NaOH using standard oxalic acid, "
          "and determine the strength of an unknown HCl solution using the standardised NaOH.** Appreciating why "
          "these must be done in that order \u2014 and in that //session// \u2014 is most of what an examiner is "
          "testing."),
    ("eq", "2NaOH + H_{2}C_{2}O_{4} \u2192 Na_{2}C_{2}O_{4} + 2H_{2}O   (standardisation)"),
    ("eq", "NaOH + HCl \u2192 NaCl + H_{2}O   (assay)"),
    ("defbox", [
        ("Standard solution", "A solution of accurately known concentration, prepared by weighing a primary "
                              "standard or by standardising against one."),
        ("Primary standard", "A highly pure, stable, non-hygroscopic substance that can be weighed accurately and "
                             "reacts stoichiometrically. Oxalic acid dihydrate is a classic acid standard."),
        ("Normality (N)", "Gram-equivalents of solute per litre. For monobasic HCl or monobasic NaOH, N = M. For "
                          "oxalic acid, which is dibasic, N = 2M."),
        ("Molarity (M)", "Moles of solute per litre of solution."),
        ("Equivalence factor", "The stoichiometric ratio between titrant and analyte, taken from the balanced "
                               "equation."),
        ("Concordant readings", "Titres that agree within a small spread (typically \u00b10.05\u20130.10 mL), "
                                "indicating consistent technique."),
    ]),
    ("box", "key", [
        "**Why standardise at all?** Solid NaOH is deliquescent (it absorbs water) and also absorbs CO_{2} from "
        "air, forming carbonate. A weighed mass therefore does not correspond to a known amount of hydroxide, and "
        "NaOH is not a primary standard.",
        "**Why oxalic acid?** It is a stable crystalline solid of high purity, it can be weighed accurately, and it "
        "reacts cleanly and stoichiometrically with hydroxide.",
        "**Why the same session?** NaOH solution changes strength as it absorbs CO_{2}; a factor determined weeks "
        "ago may no longer apply.",
    ], "The three \u201cwhy\u201d answers at the heart of this experiment"),
]

B += [
    ("h2", "5.2  Theory: concentration, equivalents and the arithmetic of titration"),
    ("h3", "5.2.1  From a weighed mass to a standard concentration"),
    ("p", "Oxalic acid dihydrate, H_{2}C_{2}O_{4}\u00b72H_{2}O, has a molar mass of 126.07 g mol^{\u22121}. If you "
          "weigh m grams and dissolve to a final volume V (mL), the molarity is:"),
    ("eq", "M = (m / 126.07) \u00d7 (1000/V)"),
    ("p", "Because oxalic acid is **dibasic**, its equivalent weight \u2014 the mass that supplies one mole of "
          "H^{+} \u2014 is half that:"),
    ("eq", "Equivalent weight (oxalic acid) = 126.07/2 = 63.04 g eq^{\u22121}   \u21d2   N = 2M",
     "Equation 5.1 \u2014 the normality of a dibasic acid is twice its molarity. This factor of two is the most "
     "common arithmetic error in the whole chapter."),
    ("tbl", ["Substance", "Formula", "Molar mass (g mol^{\u22121})", "Basicity/acidity", "Equivalent weight "
             "(g eq^{\u22121})"],
     [["Oxalic acid dihydrate", "H_{2}C_{2}O_{4}\u00b72H_{2}O", "126.07", "2 (dibasic)", "63.04"],
      ["Sodium hydroxide", "NaOH", "40.00", "1", "40.00"],
      ["Hydrochloric acid", "HCl", "36.46", "1", "36.46"],
      ["Anhydrous oxalic acid", "H_{2}C_{2}O_{4}", "90.03", "2", "45.02"]],
     [38, 42, 30, 28, 30],
     "**Table 5.1** Reference constants. The distinction between the dihydrate and the anhydrous acid is not "
     "academic: using 90.03 where 126.07 is required shifts your result by 40 %.", ["l", "l", "c", "c", "c"]),
    ("h3", "5.2.2  The titration relation"),
    ("p", "At the equivalence point, the equivalents of acid equal the equivalents of base. In normality form this "
          "is the familiar:"),
    ("eq", "N_{1}V_{1} = N_{2}V_{2}",
     "Equation 5.2 \u2014 the master equation of volumetric analysis. It is valid only when both N values refer to "
     "the same equivalent (that is, when both are true normalities)."),
    ("p", "If you prefer molarity, the stoichiometric coefficients must appear explicitly. For "
          "2NaOH + H_{2}C_{2}O_{4}:"),
    ("eq", "M_{NaOH} V_{NaOH} = 2 \u00d7 M_{oxalic} \u00d7 V_{oxalic}",
     "Equation 5.3 \u2014 the molarity form for a 2:1 reaction. The factor of two appears here rather than in the "
     "normalities, which is why the normality form is less error-prone."),
    ("h3", "5.2.3  Why indicators work, in terms of pH"),
    ("p", "An acid\u2013base indicator is a weak acid whose undissociated form and conjugate base have different "
          "colours. Its colour change occurs over a pH range approximately pK_{In} \u00b1 1. For the endpoint to "
          "coincide with equivalence, that range must lie on the steep part of the titration curve."),
    ("tbl", ["Indicator", "pH range of colour change", "Acid colour", "Base colour", "Suitable for"],
     [["Phenolphthalein", "8.3\u201310.0", "colourless", "pink", "Strong base titrations; NaOH standardisation; "
       "weak acid vs strong base"],
      ["Methyl orange", "3.1\u20134.4", "red", "yellow", "Strong acid vs strong base; not for weak bases"],
      ["Methyl red", "4.4\u20136.2", "red", "yellow", "Strong acid vs weak base"],
      ["Bromothymol blue", "6.0\u20137.6", "yellow", "blue", "Neutralisation near pH 7"]],
     [38, 34, 26, 26, 54], "**Table 5.2** Indicators and their ranges. Choosing an indicator whose transition "
                           "range misses the vertical part of the curve is a classic source of systematic error.",
     ["l", "c", "c", "c", "l"]),
    ("p", "For the standardisation (strong base into weak acid), the equivalence pH is above 7, so "
          "**phenolphthalein** is correct. For the assay of HCl with NaOH (strong/strong), equivalence is near 7 "
          "and phenolphthalein again works well, because its range lies on the steep part of the curve."),
    ("h3", "5.2.4  What \u201cconcordant\u201d means, and why it is required"),
    ("p", "You titrate until three successive readings agree within about 0.05\u20130.10 mL. This is not a "
          "formality: it demonstrates that random error has been reduced below the level that would affect the "
          "result, and it provides an empirical estimate of your precision. Reporting a single titre is "
          "unacceptable because it gives no evidence of reliability; averaging discordant titres is worse, because "
          "it hides a problem rather than solving it."),
]

B += [
    ("h2", "5.3  Apparatus"),
    ("tbl", ["Item", "Function", "If it is faulty"],
     [["Burette (50 mL, class A)", "Delivers accurately measured volumes of titrant", "A leaking stopcock or a "
       "worn jet biases every titre"],
      ["Pipette (20 mL, class A)", "Delivers an exact aliquot", "A chipped tip or poor technique changes the "
       "delivered volume"],
      ["Conical flasks (3)", "Hold the aliquots and allow swirling", "A dirty flask contaminates the solution"],
      ["Measuring flask (100/250 mL)", "Prepares the standard solution to an exact volume",
       "An uncalibrated flask makes the standard concentration wrong"],
      ["Analytical balance", "Weighs the primary standard", "Zero error or draughts bias the standard"],
      ["Burette stand and clamp", "Holds the burette vertically", "A tilted burette makes readings harder and "
       "less accurate"],
      ["Phenolphthalein", "Endpoint indicator", "Stale or too little indicator gives a late, faint endpoint"],
      ["Wash bottle (distilled water)", "Rinsing and dilution", "Tap water contaminates and adds ions"],
      ["Funnel", "Filling the burette", "Residual liquid in the funnel must be removed before reading"]],
     [42, 58, 70], "**Table 5.3** Apparatus. Note that three items \u2014 burette, pipette and measuring flask "
                   "\u2014 are the volumetric chain, and an error in any of them propagates directly into the "
                   "result.", ["l", "l", "l"]),
]

B += [
    ("fig", "volumetric", "**Figure 5.1** The volumetric train. A weighed primary standard fixes the titrant "
                            "concentration; the pipette fixes the aliquot; the burette measures the titrant "
                            "delivered. Each of the three transfers is a source of uncertainty, and the standard "
                            "must be established first because everything downstream depends on it."),
    ("h2", "5.4  Procedure with reasoning"),
    ("h3", "Part A \u2014 Prepare the standard oxalic acid"),
    ("num", [
        "**Weigh accurately** the mass needed for the required volume and concentration (for example, to make "
        "250 mL of 0.05 M, weigh 0.05 \u00d7 0.250 \u00d7 126.07 = 1.576 g). Weigh by difference for best accuracy.",
        "**Dissolve in a small volume of distilled water** in a beaker, stirring gently, then transfer "
        "quantitatively to a measuring flask, rinsing the beaker into the flask three times.",
        "**Make up to the mark**, stopper, and invert at least ten times to homogenise. Read the meniscus at eye "
        "level with the mark.",
        "**Calculate the exact concentration** from the mass actually weighed \u2014 not from the nominal target.",
    ]),
    ("h3", "Part B \u2014 Standardise the NaOH"),
    ("num", [
        "**Rinse the burette** with distilled water and then with a little of the NaOH solution; discard the "
        "rinsings. Fill, then run liquid through the tip to expel air.",
        "**Pipette a measured volume of oxalic acid** (typically 20 mL) into a clean conical flask and add 2\u20133 "
        "drops of phenolphthalein. It is colourless in acid.",
        "**Titrate with NaOH**, swirling continuously, until a faint pink colour persists for about 30 seconds.",
        "**Record the initial and final burette readings** and calculate the titre.",
        "**Repeat at least three times**, and take the mean of concordant readings.",
        "**Calculate the NaOH normality** from N_{1}V_{1} = N_{2}V_{2}.",
    ]),
    ("h3", "Part C \u2014 Assay the unknown HCl"),
    ("num", [
        "**Pipette a measured volume of the unknown HCl** into a clean flask and add phenolphthalein.",
        "**Titrate with the standardised NaOH** to the same faint pink endpoint.",
        "**Repeat to concordance**, then calculate the HCl concentration from N_{1}V_{1} = N_{2}V_{2}, using the "
        "NaOH concentration you have just established.",
        "**Convert to g L^{\u22121} and, if required, to % (w/v)** using the molar mass of HCl.",
    ]),
    ("box", "note", [
        "**Why rinse the burette with the titrant and not with water?** A water-wet burette dilutes the first "
        "portion of titrant, so the delivered concentration is lower than stated \u2014 a systematic error that "
        "grows with the proportion of water left behind. The same logic applies to the pipette.",
        "**Why by difference?** Weighing a container before and after transferring the solid avoids the error of "
        "material left adhering to the weighing vessel.",
    ], "Two technique points examiners probe"),
    ("box", "caution", [
        "**Never add a large excess of NaOH near the endpoint to \u201cspeed things up\u201d.** The sudden colour "
        "change means you must overshoot to detect it; approaching dropwise, with swirling, is the only way to stop "
        "at the faint pink. Overshoot biases every titre upward and therefore every calculated concentration "
        "downward.",
    ], "The habit that most affects accuracy"),
]

B += [
    ("h2", "5.5  Observations and calculation"),
    ("tbl", ["S. No.", "Volume of oxalic acid (mL)", "Initial burette (mL)", "Final burette (mL)",
             "NaOH titre V_{1} (mL)"],
     [["1", "20.0", "", "", ""], ["2", "20.0", "", "", ""], ["3", "20.0", "", "", ""]],
     [16, 40, 38, 38, 38], "**Table 5.4** Standardisation of NaOH. The three titres must be concordant before "
                           "they are averaged.", ["c", "c", "c", "c", "c"]),
    ("tbl", ["S. No.", "Volume of HCl (mL)", "Initial burette (mL)", "Final burette (mL)", "NaOH titre V_{2} (mL)"],
     [["1", "20.0", "", "", ""], ["2", "20.0", "", "", ""], ["3", "20.0", "", "", ""]],
     [16, 40, 38, 38, 38], "**Table 5.5** Assay of the unknown acid.", ["c", "c", "c", "c", "c"]),
    ("h3", "5.5.1  Worked illustration"),
    ("p", "Suppose you weighed 1.576 g of oxalic acid dihydrate and made it up to 250.0 mL:"),
    ("eq", "M_{oxalic} = (1.576/126.07) \u00d7 (1000/250.0) = 0.01250 \u00d7 4.000 = 0.0500 M "
           "\u21d2 N = 0.1000 N"),
    ("p", "If 20.0 mL of this acid required a mean of 19.9 mL of NaOH:"),
    ("eq", "N_{NaOH} = (N_{oxalic} \u00d7 V_{oxalic})/V_{NaOH} = (0.1000 \u00d7 20.0)/19.9 = 0.1005 N"),
    ("p", "Then 20.0 mL of the unknown HCl required a mean of 18.4 mL of this NaOH:"),
    ("eq", "N_{HCl} = (0.1005 \u00d7 18.4)/20.0 = 0.0925 N \u21d2 0.0925 M"),
    ("eq", "strength = 0.0925 \u00d7 36.46 = 3.37 g L^{\u22121} = 0.337 % (w/v)"),
    ("p", "These values are arithmetic illustrations, chosen to make the chain easy to follow. The logic, not the "
          "numbers, is what must be reproduced in the examination."),
    ("tbl", ["Step", "Quantity", "Expression", "Illustrative value"],
     [["1", "Mass of oxalic acid", "weighed by difference", "1.576 g"],
      ["2", "Molarity of oxalic acid", "(m/M) \u00d7 (1000/V)", "0.0500 M"],
      ["3", "Normality of oxalic acid", "2 \u00d7 M", "0.1000 N"],
      ["4", "NaOH normality", "N_{1}V_{1}/V_{2}", "0.1005 N"],
      ["5", "HCl normality", "N_{3}V_{3}/V_{4}", "0.0925 N"],
      ["6", "HCl strength", "N \u00d7 36.46", "3.37 g L^{\u22121}"]],
     [12, 52, 56, 50], "**Table 5.6** The full calculation chain, from weighed solid to reported strength. Each "
                       "step should be checkable independently.", ["c", "l", "l", "c"]),
]

B += [
    ("h2", "5.6  Precautions, errors and troubleshooting"),
    ("bul", [
        "Rinse burette and pipette with the solution they will contain, not with water alone.",
        "Expel air from the burette tip and keep the jet filled.",
        "Read the meniscus at eye level, at its lowest point, against a white background.",
        "Add the last portion dropwise, with continuous swirling.",
        "Take the endpoint as the first faint pink that persists for 30 seconds.",
        "Use the same indicator volume in every flask.",
        "Use the exact mass weighed, not the nominal target mass.",
        "Standardise and assay in the same session; keep NaOH stoppered.",
    ]),
    ("tbl", ["Source of error", "Type", "Effect", "Control"],
     [["Meniscus misread (parallax)", "Systematic", "Titre biased by 0.05\u20130.2 mL", "Read at eye level"],
      ["Endpoint overshoot", "Systematic (positive)", "Titre high; acid strength low", "Dropwise addition; faint "
       "pink only"],
      ["Burette not rinsed with titrant", "Systematic", "Titrant effectively diluted", "Rinse with titrant"],
      ["Air bubble in the tip", "Systematic", "Delivered volume less than read", "Expel air before starting"],
      ["Wrong oxalic acid hydrate used", "Systematic (large)", "Up to 40 % error", "Check the formula and molar "
       "mass"],
      ["Dibasic factor omitted", "Systematic (factor 2)", "Standard half or double the true value", "N = 2M for "
       "oxalic acid"],
      ["Flasks not rinsed with distilled water", "Random", "Contamination", "Rinse all glassware"],
      ["Indicator too dilute or stale", "Systematic", "Late or indistinct endpoint", "Fresh indicator, 2\u20133 "
       "drops"],
      ["NaOH absorbing CO_{2}", "Systematic", "Effective strength falls with time", "Stopper; standardise same "
       "day"]],
     [44, 30, 48, 48], "**Table 5.7** Error budget.", ["l", "l", "l", "l"]),
    ("tbl", ["Symptom", "Likely cause", "Action"],
     [["Endpoint fades after 10 s", "Genuine incomplete neutralisation, or CO_{2} uptake by the solution",
       "Continue dropwise; use freshly boiled distilled water if CO_{2} is suspected"],
      ["Endpoint appears immediately", "Alkali carried over on glassware, or the flask was not clean",
       "Wash and rinse everything"],
      ["Titres drift upward run to run", "Burette leaking, or NaOH absorbing CO_{2}", "Check the stopcock; "
       "restandardise"],
      ["Titres vary by more than 0.2 mL", "Technique: inconsistent endpoint or reading", "Practise the endpoint; "
       "use a white tile"],
      ["Calculated HCl strength implausible", "Factor of two from the dibasic acid, or a unit slip", "Re-derive "
       "from the balanced equations"]],
     [40, 64, 66], "**Table 5.9** Troubleshooting chart.", ["l", "l", "l"]),
]

VIVA_A = [
    ("What is a standard solution?", "A solution whose concentration is accurately known, obtained by weighing a "
                                     "primary standard or by standardising against one."),
    ("What is a primary standard?", "A highly pure, stable, non-hygroscopic substance that can be weighed "
                                    "accurately and reacts stoichiometrically and completely."),
    ("Why is NaOH not a primary standard?", "It is deliquescent and absorbs CO_{2} from air, so a weighed mass "
                                            "does not correspond to a known amount of hydroxide."),
    ("Why is oxalic acid a suitable primary standard?", "It is a stable crystalline solid of high purity, can be "
                                                        "weighed accurately, and reacts cleanly with hydroxide in a "
                                                        "known ratio."),
    ("What is normality?", "Gram-equivalents of solute per litre of solution."),
    ("What is the equivalent weight of oxalic acid dihydrate?", "126.07/2 = 63.04 g eq^{\u22121}, because it is "
                                                                "dibasic."),
    ("What is the normality of a 0.05 M oxalic acid solution?", "0.10 N, because N = 2M for a dibasic acid."),
    ("Why is phenolphthalein used for the standardisation?", "The titration ends in a basic solution, and "
                                                             "phenolphthalein changes colour over pH 8.3\u201310, "
                                                             "which lies on the steep part of the curve."),
    ("What colour change is observed?", "Colourless to faint pink, as the solution becomes slightly alkaline."),
    ("State the titration relation.", "N_{1}V_{1} = N_{2}V_{2} at equivalence."),
    ("Why must titres be concordant?", "Agreement within about 0.05\u20130.10 mL shows that random error is "
                                       "acceptably small and gives an empirical estimate of precision."),
    ("What is the equivalent weight of HCl?", "36.46 g eq^{\u22121}, since it supplies one mole of H^{+} per mole."),
    ("How do you convert molarity to g L^{\u22121}?", "Multiply by the molar mass: g L^{\u22121} = M \u00d7 M_{r}."),
    ("What is the reaction between NaOH and oxalic acid?", "2NaOH + H_{2}C_{2}O_{4} \u2192 Na_{2}C_{2}O_{4} + "
                                                           "2H_{2}O."),
    ("What is the reaction between NaOH and HCl?", "NaOH + HCl \u2192 NaCl + H_{2}O."),
    ("Why is the meniscus read at eye level?", "To avoid parallax error, which biases the volume reading."),
    ("Which part of the meniscus is read?", "The lowest point of the concave meniscus, for colourless or pale "
                                            "solutions."),
    ("Why is the burette rinsed with the titrant?", "Residual water would dilute the titrant and change its "
                                                    "effective concentration."),
    ("Why should the funnel be removed before reading?", "Liquid remaining in the funnel can drip into the burette "
                                                         "and change the delivered volume."),
    ("What is the difference between endpoint and equivalence point?", "Equivalence is the stoichiometric point; "
                                                                       "endpoint is the observed colour change used "
                                                                       "to estimate it."),
]

VIVA_B = [
    ("Why standardise in the same session as the assay?", "Because NaOH absorbs CO_{2} over time, so a factor "
                                                         "determined earlier may no longer describe the solution "
                                                         "you are using."),
    ("Why not weigh NaOH directly?", "Because it is deliquescent and carbonated; the weighed mass does not "
                                     "represent a known amount of hydroxide."),
    ("Why is the last portion added dropwise?", "Because the pH changes steeply near the endpoint, so a single drop "
                                                "can overshoot; dropwise addition is the only way to stop at the "
                                                "first faint colour."),
    ("Why add only 2\u20133 drops of indicator?", "The indicator is itself a weak acid and consumes a little "
                                                  "titrant; a large amount would introduce a measurable indicator "
                                                  "blank and dull the colour change."),
    ("Why swirl continuously?", "To mix the titrant into the bulk solution promptly, avoiding local excess that "
                                "produces a transient colour change and leads to overtitration."),
    ("Why use a white tile under the flask?", "It provides a consistent background against which the faint pink is "
                                              "detectable."),
    ("Why must the endpoint persist for 30 seconds?", "A transient pink can arise from local alkali before mixing is "
                                                      "complete; persistence confirms that the bulk solution is "
                                                      "alkaline."),
    ("Why do we weigh by difference?", "It accounts for any solid left in the weighing vessel, removing a systematic "
                                       "loss."),
    ("Why make up to the mark and invert repeatedly?", "To ensure the solution is homogeneous, so any aliquot has "
                                                       "exactly the intended concentration."),
    ("Why is the pipette rinsed with the solution it will deliver?", "Residual water would dilute the aliquot and "
                                                                     "change the number of moles delivered."),
    ("Why use three flasks rather than one?", "To obtain concordant readings from independent titrations, which is "
                                              "the only way to estimate precision."),
    ("Why is the HCl assayed after, not before, the standardisation?", "Because its calculation uses the NaOH "
                                                                       "concentration, which is only known after the "
                                                                       "standardisation."),
    ("What happens if CO_{2} dissolves in the NaOH?", "It forms carbonate, which reacts with acid but not in the "
                                                      "same stoichiometry as hydroxide, lowering the effective "
                                                      "strength and shifting the endpoint."),
    ("Why is the titration flask conical rather than a beaker?", "The conical shape allows vigorous swirling without "
                                                                 "splashing and funnels the contents during "
                                                                 "swirling."),
    ("Why does the calculated concentration depend on the exact mass weighed?", "Because the standard's "
                                                                               "concentration is derived from that "
                                                                               "mass; using the nominal target mass "
                                                                               "instead introduces a systematic error."),
]

VIVA_C = [
    ("What if you used anhydrous oxalic acid but assumed the dihydrate?", "Your calculated standard molarity would "
                                                                          "be about 40 % too low, because 90.03 was "
                                                                          "divided into a mass that actually "
                                                                          "corresponded to the dihydrate."),
    ("What if you forgot the factor of two for oxalic acid?", "The normality would be half its true value, so the "
                                                              "NaOH normality would come out half, and the HCl "
                                                              "strength would be reported at half its true value."),
    ("What if you overshot the endpoint by 0.3 mL?", "The titre would be too large, so the calculated NaOH "
                                                    "normality (from a fixed acid volume) would be too high, and the "
                                                    "HCl strength correspondingly wrong."),
    ("What if the burette had an air bubble that cleared during the titration?", "The volume actually delivered would "
                                                                                "exceed the difference in readings, "
                                                                                "inflating the titre."),
    ("What if you used tap water to make up the standard?", "Dissolved ions would react with the titrant and change "
                                                           "the effective concentration; the standard would be "
                                                           "invalid."),
    ("What if the oxalic acid solution were left open for a week?", "Water would evaporate, the concentration would "
                                                                    "rise, and the standardisation would be wrong."),
    ("What if the flask contained residual acid from washing?", "It would consume extra titrant, giving a falsely "
                                                                "high titre and a falsely high calculated "
                                                                "concentration."),
    ("What if the NaOH were prepared weeks earlier?", "It would have absorbed CO_{2} and its effective strength would "
                                                      "have fallen; the standardisation would reveal this, which is "
                                                      "why it is done fresh."),
    ("What if the indicator were added after most of the titrant?", "You would have no warning of approaching the "
                                                                    "endpoint and would almost certainly overshoot."),
]

VIVA_D = [
    ("Why is normality convenient for titrations?", "Because it expresses concentration in reaction-equivalents, so "
                                                    "N_{1}V_{1} = N_{2}V_{2} holds regardless of the stoichiometric "
                                                    "coefficients."),
    ("When does normality fail to simplify things?", "When the reaction stoichiometry is not a simple proton transfer "
                                                     "\u2014 for example in redox titrations where the equivalent "
                                                     "depends on the electron change."),
    ("What is the difference between a standard solution and a standardised solution?", "A standard solution is "
                                                                                       "prepared directly from a "
                                                                                       "primary standard; a "
                                                                                       "standardised solution has its "
                                                                                       "concentration determined by "
                                                                                       "titration against one."),
    ("Why is a blank titration sometimes performed?", "To correct for the titrant consumed by the solvent or "
                                                      "indicator, which becomes significant at very low analyte "
                                                      "concentrations."),
    ("Would the result change if you used a 25 mL pipette instead of 20 mL?", "Not if you use the correct volume in "
                                                                              "the calculation; V_{1} and V_{2} would "
                                                                              "both scale, and the ratio is "
                                                                              "unchanged."),
    ("What is the precision of a class-A burette?", "Typically \u00b10.05 mL over 50 mL, and class-A pipettes "
                                                    "\u00b10.03 mL for 20 mL \u2014 which is why concordance "
                                                    "within 0.05 mL is the expected standard."),
    ("Why does the pH at the equivalence of oxalic acid with NaOH lie above 7?", "The product is sodium oxalate, "
                                                                                 "whose oxalate ion is a weak base; "
                                                                                 "it hydrolyses, raising the pH."),
    ("Why is methyl orange unsuitable for the NaOH standardisation?", "Its transition range is at pH "
                                                                      "3.1\u20134.4, far from the equivalence pH of "
                                                                      "this titration, so it would change colour "
                                                                      "well before equivalence."),
    ("What is the purpose of the second titration, given the first seems to answer the question?", "The first "
                                                                                                  "establishes the "
                                                                                                  "titrant; the second "
                                                                                                  "uses it to measure the "
                                                                                                  "unknown. Without the "
                                                                                                  "first, the second has "
                                                                                                  "no calibration."),
    ("How would you report the precision of your result?", "From the spread of the concordant titres, propagated "
                                                           "through the calculation; for example a mean of 19.90 "
                                                           "\u00b1 0.05 mL."),
]

CH5_CHECK = checklist(
    "5.8",
    ["NaOH is deliquescent and carbonated: not a primary standard.",
     "Oxalic acid dihydrate is a primary standard; M = 126.07 g mol^{\u22121}.",
     "Oxalic acid is dibasic: equivalent weight 63.04, N = 2M.",
     "Reaction: 2NaOH + H_{2}C_{2}O_{4} \u2192 Na_{2}C_{2}O_{4} + 2H_{2}O.",
     "Assay reaction: NaOH + HCl \u2192 NaCl + H_{2}O.",
     "Master equation: N_{1}V_{1} = N_{2}V_{2} at equivalence.",
     "Molarity form for oxalic acid: M_{NaOH}V_{NaOH} = 2M_{ox}V_{ox}.",
     "Phenolphthalein: colourless \u2192 pink, pH 8.3\u201310.",
     "Methyl orange: red \u2192 yellow, pH 3.1\u20134.4.",
     "Phenolphthalein suits strong base titrations and weak acid/strong base.",
     "Standardise and assay in the same session.",
     "Rinse burette and pipette with the solution they will contain.",
     "Expel air from the burette tip before starting.",
     "Read the meniscus at eye level, lowest point.",
     "Add the last portion dropwise, swirling.",
     "Endpoint = first faint pink persisting 30 s.",
     "Weigh by difference for the primary standard.",
     "Use the exact mass weighed, not the nominal target.",
     "Convert molarity to g L^{\u22121} using 36.46 for HCl.",
     "Three concordant titres within about 0.05\u20130.10 mL."],
    ["Why is NaOH standardised rather than weighed?",
     "Why is oxalic acid suitable as a primary standard?",
     "What is normality, and what is the normality of 0.05 M oxalic acid?",
     "Write both balanced equations.",
     "Why is phenolphthalein used, and what is the colour change?",
     "How do you calculate the NaOH concentration from the standardisation?",
     "How do you calculate the HCl strength from the assay?",
     "Why must titres be concordant?",
     "Why rinse the burette with the titrant?",
     "What is the difference between endpoint and equivalence point?"],
    ["Show, starting from the balanced equation, why N = 2M for oxalic acid but N = M for HCl.",
     "A student reports an HCl strength 40 % low. Give three possible causes with the arithmetic that "
     "distinguishes them.",
     "Explain why the equivalence pH of the oxalic acid titration is above 7, and why that makes phenolphthalein "
     "correct.",
     "Calculate the propagation of a \u00b10.05 mL error in each titre through to the final reported strength.",
     "Why does the normality approach avoid the stoichiometric coefficients, and when does that convenience break "
     "down?",
     "Explain the effect of dissolved CO_{2} on the NaOH factor and on the endpoint.",
     "Why does a primary standard need to be non-hygroscopic, and what goes wrong if it is not?",
     "Compare the relative accuracy of a weighed standard and a standardised solution.",
     "How would you detect that your oxalic acid solution had evaporated partially?",
     "Design a scheme to standardise NaOH using potassium hydrogen phthalate instead, with all the arithmetic."],
    [("Normality vs molarity", "Equivalents vs moles per litre."),
     ("Primary standard vs standardised solution", "Direct preparation vs titration-determined."),
     ("Endpoint vs equivalence", "Observed vs stoichiometric."),
     ("Dihydrate vs anhydrous oxalic acid", "126.07 vs 90.03 g mol^{\u22121}."),
     ("Burette vs pipette function", "Delivers variable vs fixed volume."),
     ("Phenolphthalein vs methyl orange", "Basic vs acidic transition range."),
     ("Concordant vs averaged", "Consistent readings vs a mean of inconsistent ones."),
     ("Standardisation vs assay", "Determines the titrant vs uses it.")],
    (["Relation", "Expression", "Note"],
     [["Molarity from mass", "M = (m/M_{r})(1000/V)", "V in mL"],
      ["Normality of dibasic acid", "N = 2M", "Oxalic acid"],
      ["Titration relation", "N_{1}V_{1} = N_{2}V_{2}", "At equivalence"],
      ["Molarity form", "M_{1}V_{1} = (a/b)M_{2}V_{2}", "a, b from the balanced equation"],
      ["Strength", "g L^{\u22121} = N \u00d7 equivalent weight", "36.46 for HCl"],
      ["Equivalent weight", "M_{r}/(n H^{+} or OH^{\u2212})", "63.04 for oxalic acid dihydrate"],
      ["Mean titre", "sum of concordant titres / number", "Reject outliers with a reason"],
      ["CO_{2} effect", "2NaOH + CO_{2} \u2192 Na_{2}CO_{3} + H_{2}O", "Lowers effective strength"]],
     [36, 74, 58]),
    [["Endpoint fades within seconds", "Incomplete mixing or CO_{2} uptake"],
     ["Endpoint appears instantly", "Alkali contamination of the flask"],
     ["Titres increase run to run", "Leaking stopcock or carbonate formation"],
     ["Spread greater than 0.2 mL", "Inconsistent endpoint or parallax reading"],
     ["Strength exactly half expected", "Dibasic factor omitted"],
     ["Strength about 40 % low", "Anhydrous molar mass used for the dihydrate"],
     ["Burette reading drifts while stationary", "Stopcock leaking"]],
    ["Standardise and assay in one session \u2014 NaOH changes.",
     "The factor of two for oxalic acid is where most marks are lost.",
     "Rinse with the solution, not with water.",
     "Faint pink, 30 seconds, dropwise at the end.",
     "Weigh by difference; calculate from the actual mass.",
     "Concordance is evidence, not a formality.",
     "Normality hides the stoichiometry \u2014 which is why it is convenient and why it is dangerous."],
    ["Using the nominal rather than the weighed mass for the standard.",
     "Forgetting that oxalic acid is dibasic.",
     "Reading the burette at an angle.",
     "Adding the last millilitre in one go.",
     "Averaging discordant titres.",
     "Reporting the strength without units or without the basis (% w/v vs g L^{\u22121}).",
     "Not stating which hydrate of oxalic acid was used."],
    ["This experiment has two linked halves. First I standardise sodium hydroxide, because solid NaOH absorbs water "
     "and carbon dioxide and so is not a primary standard. I prepare a standard solution of oxalic acid dihydrate "
     "from an accurately weighed mass, noting that it is dibasic so its normality is twice its molarity, and "
     "titrate measured aliquots of it with the NaOH using phenolphthalein, which changes from colourless to pink at "
     "pH 8.3\u201310 \u2014 on the steep part of the curve for this titration. From concordant titres I obtain the "
     "NaOH normality using N_{1}V_{1} = N_{2}V_{2}. Second, I pipette a measured volume of the unknown HCl and "
     "titrate it with that now-standardised NaOH to the same faint pink endpoint, and calculate the acid strength "
     "from the same relation, then convert to grams per litre using 36.46. The critical controls are rinsing the "
     "burette and pipette with their own solutions, expelling air from the tip, reading the meniscus at eye level, "
     "adding the last portion dropwise, taking the endpoint as the first faint pink that persists for thirty "
     "seconds, and obtaining three concordant titres."],
    ["**NaOH is not a primary standard \u2192 standardise it.**",
     "**Oxalic acid is dibasic \u2192 N = 2M.**",
     "**N\u2081V\u2081 = N\u2082V\u2082 does all the arithmetic.**",
     "**Faint pink, thirty seconds, dropwise.**"]
)

CH5 = {
    "key": "volumetric",
    "num": "5",
    "kicker": "Experiment 5  \u00b7  Volumetric analysis",
    "title": "Standardisation of NaOH and Assay of Hydrochloric Acid",
    "toc": "Standardisation of NaOH and assay of HCl",
    "standfirst": "The foundation of every volumetric result: a titrant whose strength you have actually "
                  "established, used to measure an acid whose strength you do not know.",
    "body": B + [
        ("h2", "5.7  Viva question bank"),
        ("p", "Seventy-four answered questions, weighted towards the arithmetic and the technique, because that is "
              "where this experiment is won and lost."),
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
    ] + CH5_CHECK,
}
