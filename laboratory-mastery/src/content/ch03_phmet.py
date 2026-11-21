"""Chapter 3 - pH-metric titration of a strong acid against a strong base."""
from common import checklist

B = []

B += [
    ("h2", "3.1  What this experiment does"),
    ("lead", "An indicator titration tells you one number: the volume at which a colour changes. A pH-metric "
             "titration tells you the whole story \u2014 how the acidity of the solution responds to every drop "
             "of base. That extra information is what makes the equivalence point visible as a shape in a graph "
             "rather than a judgement about the shade of pink."),
    ("p", "The aim is to **plot the pH titration curve of a strong acid against a strong base and, from it, "
          "determine the strength of the given acid solution.** Everything in the chapter serves that aim: the "
          "electrode calibration (so the numbers are trustworthy), the small additions near the jump (so the "
          "shape is resolved), and the derivative plot (so the equivalence volume can be located with precision "
          "rather than by eye)."),
    ("p", "The chemistry is the simplest in the syllabus, and that simplicity is the point. HCl and NaOH are both "
          "fully dissociated in dilute solution, so the reaction is the combination of hydrogen and hydroxide ions:"),
    ("eq", "HCl + NaOH \u2192 NaCl + H_{2}O;     net ionic:  H^{+} + OH^{\u2212} \u2192 H_{2}O",
     "Equation 3.1 \u2014 strong acid plus strong base. The salt, NaCl, is a spectator: it takes no part in the "
     "neutralisation and does not hydrolyse."),
    ("defbox", [
        ("pH", "The negative base-10 logarithm of hydrogen-ion //activity//: pH = \u2212log_{10} a(H^{+}). In "
               "dilute solution the activity coefficient is close to one, so pH \u2248 \u2212log_{10}[H^{+}]."),
        ("Equivalence point", "The stoichiometric point at which the moles of base added equal the moles of acid "
                              "originally present. It is a fact about the amounts, not about the instrument."),
        ("Endpoint", "The point actually observed \u2014 an indicator colour change, or the steepest part of a "
                     "titration curve. It approximates the equivalence point to within the resolution of the "
                     "method."),
        ("Titration curve", "A plot of pH against volume of titrant added. Its shape is determined by which "
                            "species is in excess."),
        ("First derivative (\u0394pH/\u0394V)", "The rate of change of pH with added volume. It peaks at the "
                                               "inflection point of the curve, which is the equivalence point for "
                                               "this system."),
        ("Buffer", "A solution that resists pH change on addition of small amounts of acid or base; it is why the "
                   "curve is flat in some regions and steep in others."),
    ]),
    ("box", "key", [
        "**Before equivalence** the pH is set by the excess strong acid \u2014 and because that is a "
        "concentration that falls as you dilute, pH rises slowly and predictably.",
        "**At equivalence** essentially all H^{+} and OH^{\u2212} have combined; the pH is that of the NaCl "
        "solution, near 7 at 25 \u00b0C, set by water autoionisation alone.",
        "**After equivalence** the pH is set by the excess strong base and rises quickly, then flattens as the "
        "hydroxide is diluted.",
    ], "The three regions of the curve"),
    ("fig", "titration", "**Figure 3.1** pH-metric titration assembly. The burette delivers standard base; the "
                         "glass electrode is immersed in the stirred solution without touching the vessel. "
                         "Cumulative volume, not increment, is recorded against each stable pH."),
]

B += [
    ("h2", "3.2  Theory: why the curve has the shape it has"),
    ("h3", "3.2.1  Building the curve from concentrations"),
    ("p", "Take 20.0 mL of 0.1 M HCl and titrate with 0.1 M NaOH. At any added volume V (mL), the initial moles "
          "of acid are n_{a} = 0.1 \u00d7 20.0 mmol, and the moles of base added are n_{b} = 0.1 \u00d7 V. The "
          "total volume is (20.0 + V) mL, so dilution is included automatically if you work in moles and divide "
          "by the current volume."),
    ("p", "**Before equivalence (V < 20 mL):** acid is in excess."),
    ("eq", "[H^{+}] = (n_{a} \u2212 n_{b})/(V_{total})   \u21d2   pH = \u2212log_{10}[H^{+}]"),
    ("p", "At V = 0 the pH is 1.00 (for 0.1 M HCl). At V = 18 mL, [H^{+}] = (2.0 \u2212 1.8)/38.0 = 5.3 \u00d7 "
          "10^{\u22123} M, so pH = 2.28. At V = 19.8 mL, [H^{+}] = 0.2/39.8 = 5.0 \u00d7 10^{\u22124} M, pH = "
          "3.30. Notice how little the pH has moved over 19.8 mL of base \u2014 that is the flat region."),
    ("p", "**At equivalence (V = 20 mL):** the solution is 0.05 M NaCl. Neither ion hydrolyses, so the only "
          "source of H^{+} and OH^{\u2212} is water:"),
    ("eq", "[H^{+}] = \u221a(K_{w}) = 1.0 \u00d7 10^{\u22127} M   \u21d2   pH = 7.00  (at 25 \u00b0C)"),
    ("p", "**After equivalence (V > 20 mL):** base is in excess."),
    ("eq", "[OH^{\u2212}] = (n_{b} \u2212 n_{a})/V_{total};   pOH = \u2212log[OH^{\u2212}];   pH = 14 \u2212 pOH"),
    ("p", "At V = 20.2 mL, [OH^{\u2212}] = 0.2/40.2 = 5.0 \u00d7 10^{\u22123} M, so pOH = 2.30 and pH = 11.70. "
          "**In 0.2 mL the pH has moved from 7 to 11.7.** At V = 22 mL, [OH^{\u2212}] = 2.0/42 = 4.8 \u00d7 "
          "10^{\u22122}, pOH = 1.32, pH = 12.68. The steep rise is now over, and the curve flattens again."),
    ("tbl", ["NaOH added (mL)", "Excess species", "Concentration of excess (M)", "pH"],
     [["0.0", "H^{+}", "0.100", "1.00"], ["10.0", "H^{+}", "0.033", "1.48"],
      ["18.0", "H^{+}", "5.3 \u00d7 10^{\u22123}", "2.28"], ["19.8", "H^{+}", "5.0 \u00d7 10^{\u22124}", "3.30"],
      ["19.98", "H^{+}", "5.0 \u00d7 10^{\u22125}", "4.30"], ["20.00", "neither (NaCl)", "\u2014", "7.00"],
      ["20.02", "OH^{\u2212}", "5.0 \u00d7 10^{\u22124}", "10.70"], ["20.2", "OH^{\u2212}", "5.0 \u00d7 "
       "10^{\u22123}", "11.70"],
      ["22.0", "OH^{\u2212}", "4.8 \u00d7 10^{\u22122}", "12.68"], ["30.0", "OH^{\u2212}", "0.020", "12.30"]],
     [30, 34, 52, 26], "**Table 3.1** Calculated pH values for 20.0 mL of 0.1 M HCl titrated with 0.1 M NaOH at "
                       "25 \u00b0C. These are //calculated// from the equations above, not measured \u2014 a "
                       "legitimate teaching table, and clearly labelled as such.",
     ["c", "l", "l", "c"]),
    ("plot", "ph_curve", "**Figure 3.2** Left: the titration curve, with its long flat region, the near-vertical "
                         "jump around the equivalence volume and the flattening at high pH. Right: the "
                         "first-derivative curve, whose maximum coincides with the equivalence volume. Values "
                         "computed from the equations of Table 3.1."),
    ("h3", "3.2.2  Why the jump is so abrupt, in one sentence"),
    ("p", "Because the pH scale is logarithmic, and near equivalence the //sign// of the excess changes: a few "
          "hundredths of a millilitre takes the solution from a hydrogen-ion concentration of 10^{\u22125} M to a "
          "hydroxide-ion concentration of 10^{\u22124} M. Since [H^{+}] has fallen from 10^{\u22125} to "
          "10^{\u221210} M, that is a change of five orders of magnitude \u2014 five pH units \u2014 produced by a "
          "change of a few hundredths of a millilitre in added volume."),
    ("p", "This is the single most useful sentence in the chapter. It explains the vertical jump, it explains why "
          "small additions are needed near equivalence, and it explains why a pH-meter is a better endpoint "
          "detector than an indicator for this system: an indicator would flip colour somewhere within that "
          "enormous jump, but you would have no way to know //where// within it."),
    ("h3", "3.2.3  Locating equivalence: inflection and derivative"),
    ("p", "Two equivalent constructions give the same answer. **The inflection method** finds the point of "
          "steepest slope on the pH\u2013V curve, which is where the second derivative changes sign. **The "
          "derivative method** computes \u0394pH/\u0394V for each consecutive pair of readings, plots it against "
          "the average volume of the interval, and takes the maximum. The derivative is preferred in practice "
          "because a peak is easier to locate precisely than an inflection on a drawn curve, and because the peak "
          "is symmetrical even when the data are sparse."),
    ("eq", "\u0394V = V_{2} \u2212 V_{1};   \u0394pH = pH_{2} \u2212 pH_{1};   slope = \u0394pH/\u0394V;   "
           "V_{avg} = (V_{1} + V_{2})/2",
     "Equation 3.2 \u2014 the tabulated differences. The manual\u2019s observation table has exactly these columns."),
    ("p", "A refinement worth knowing: if the peak lies between two tabulated intervals, the equivalence volume "
          "can be estimated by **linear interpolation of the two largest slopes**, or by the second-derivative "
          "zero-crossing. For a strong acid/strong base titration the peak is sharp, so the simple maximum is "
          "usually adequate."),
    ("h3", "3.2.4  From equivalence volume to acid strength"),
    ("p", "At equivalence the moles of base equal the moles of acid. For monobasic HCl and monobasic NaOH:"),
    ("eq", "C_{HCl} \u00d7 V_{HCl} = C_{NaOH} \u00d7 V_{eq}   \u21d2   C_{HCl} = (C_{NaOH} \u00d7 V_{eq})/V_{HCl}",
     "Equation 3.3 \u2014 the working calculation. This is the //molarity// form; the normality form N_{1}V_{1} = "
     "N_{2}V_{2} is numerically identical here because both species are monovalent."),
    ("box", "exam", [
        "An examiner may ask why the equivalence pH is 7 for this system but not for a weak acid. The answer: "
        "the salt of a strong acid and strong base does not hydrolyse, so at equivalence the only equilibrium is "
        "water autoionisation. For a weak acid, the conjugate base hydrolyses, giving pH > 7 at equivalence \u2014 "
        "which is why phenolphthalein, not methyl orange, is the correct indicator for a weak-acid titration.",
        "A second trap: \u201cyour pH at equivalence reads 6.8, so your titration is wrong.\u201d Not necessarily "
        "\u2014 electrode calibration, temperature, dissolved CO_{2} and residual activity effects can shift the "
        "measured value slightly. What matters is the //volume// at the steepest point, not the pH value there.",
    ], "Two examiner traps"),
]

B += [
    ("h2", "3.3  Apparatus, and how the electrode produces a number"),
    ("tbl", ["Item", "Function", "Consequence of a fault"],
     [["pH meter with glass electrode", "Converts hydrogen-ion activity into a displayed pH",
       "Uncalibrated or dry electrode gives a shifted or drifting curve"],
      ["Combination/reference electrode", "Completes the electrochemical cell; provides a stable reference "
       "potential", "Blocked junction causes slow, noisy or frozen readings"],
      ["Standard buffers (pH 4.0 and 7.0, ideally 9.2)", "Define offset and slope of the electrode response",
       "Stale buffers calibrate the meter to the wrong pH"],
      ["Burette (with stand, 50 mL)", "Delivers measured volumes of NaOH", "Air bubble or leak biases every "
       "volume"],
      ["Pipette (20 mL)", "Delivers the acid aliquot", "Wrong aliquot volume scales the whole result"],
      ["Beaker + magnetic stirrer", "Hold and homogenise the solution", "Poor mixing gives a locally high pH at "
       "the electrode tip"],
      ["Standard NaOH (standardised)", "Titrant of known concentration", "Unstandardised base gives a wrong acid "
       "strength"],
      ["Distilled water", "Dilutes the aliquot so the bulb is immersed; rinses the electrode",
       "Tap water adds ions and buffers the solution"]],
     [46, 60, 64], "**Table 3.2** Apparatus. The electrode is the instrument\u2019s whole measurement chain; treat "
                   "it as the most delicate item on the bench.", ["l", "l", "l"]),
    ("fig", "phmeter", "**Figure 3.3** The electrode system. A potential develops across the hydrated glass "
                       "membrane in proportion to hydrogen-ion activity; the meter converts that potential to pH "
                       "after calibration."),
    ("h3", "3.3.1  How a glass electrode responds to H^{+}"),
    ("p", "A thin glass membrane, hydrated on its outer surface, allows an ion-exchange equilibrium with H^{+} in "
          "solution. That creates a potential difference across the membrane which follows the **Nernst "
          "equation**:"),
    ("eq", "E = E^{0} + (2.303RT/F) log_{10} a(H^{+})   \u21d2   E = E^{0} \u2212 (2.303RT/F) pH",
     "Equation 3.4 \u2014 Nernst response of the electrode. At 25 \u00b0C, 2.303RT/F \u2248 0.0592 V, so the "
     "electrode changes by about 59.2 mV per pH unit \u2014 the \u201cslope\u201d the calibration establishes."),
    ("p", "Two consequences follow directly from that equation. First, the response is **linear in pH but not in "
          "concentration** \u2014 the electrode responds to activity. Second, the slope is **temperature-dependent** "
          "because T appears in it, which is why a meter with temperature compensation, or at least a recorded "
          "temperature, matters."),
]

B += [
    ("h2", "3.4  Procedure with reasoning"),
    ("num", [
        "**Switch on and warm up the meter**, then calibrate with two buffers that bracket the expected range "
        "(typically pH 4.0 and 7.0). Calibration sets both the offset and the slope; a single buffer sets only "
        "the offset and leaves a slope error undetected.",
        "**Rinse the electrode with distilled water between solutions** and blot gently. Never wipe the bulb: "
        "rubbing removes the hydrated layer that the measurement depends on.",
        "**Pipette the specified acid aliquot** (the supplied page shows 20 mL) into a clean beaker, and add "
        "enough distilled water to immerse the bulb. **This dilution does not change the moles of acid**, so it "
        "does not change the equivalence volume \u2014 but it does change the initial pH and the shape of the "
        "early part of the curve.",
        "**Position the electrode in the solution**, clear of the beaker wall and the stirrer bar. Record the "
        "initial pH once it is stable.",
        "**Add NaOH in measured increments**, stirring gently and consistently. After each addition, wait for the "
        "reading to stabilise before recording the cumulative volume and pH.",
        "**Reduce the increment size as you approach the expected equivalence volume** \u2014 for example 2 mL "
        "steps early, 1 mL in the middle, and 0.1 mL steps through the jump. The steepness of the curve is "
        "precisely where volume resolution matters most.",
        "**Continue past equivalence** by several millilitres so that the upper flat region is established; the "
        "curve must have both plateaus for the jump to be identifiable.",
        "**Tabulate cumulative volume, pH, \u0394V, \u0394pH, \u0394pH/\u0394V and the average volume** for each "
        "interval.",
        "**Plot both graphs**, obtain V_{eq} from the derivative maximum, and calculate the acid concentration "
        "from Equation 3.3.",
    ]),
    ("box", "note", [
        "**Why dilute the acid before titrating?** A 20 mL aliquot in a narrow beaker may not cover the electrode "
        "bulb or the stirrer bar. Adding distilled water raises the liquid level without changing the number of "
        "moles of HCl. The equivalence //volume// is therefore unaffected, but the initial pH rises because the "
        "acid is diluted \u2014 which is why the left-hand plateau of your curve sits higher than a textbook curve "
        "calculated for the undiluted acid.",
    ], "A question students answer badly"),
    ("box", "caution", [
        "**Do not let the electrode touch the bottom of the beaker or the stirrer bar.** The bulb is a thin glass "
        "membrane; contact with a spinning bar will crack it, and a cracked electrode reads erratically and then "
        "fails completely. This is the most common expensive accident in this experiment.",
    ], "The one accident to avoid"),
]

B += [
    ("h2", "3.5  Observations and calculation"),
    ("tbl", ["S. No.", "NaOH added V (mL)", "pH", "\u0394V (mL)", "\u0394pH", "\u0394pH/\u0394V", "V_{avg} (mL)"],
     [[str(i), "", "", "", "", "", ""] for i in range(1, 11)],
     [12, 32, 22, 22, 22, 30, 30],
     "**Table 3.3** Observation table. \u0394V, \u0394pH, \u0394pH/\u0394V and V_{avg} are //calculated// columns; "
     "fill them only after the pH values are recorded. Blank because the supplied source contains no completed "
     "data set.", ["c", "c", "c", "c", "c", "c", "c"]),
    ("h3", "3.5.1  Worked illustration"),
    ("p", "The supplied material\u2019s own illustration uses V_{1} = 8.0 mL, V_{2} = 8.5 mL, pH_{1} = 4.0 and "
          "pH_{2} = 5.0. Then \u0394V = 0.5 mL, \u0394pH = 1.0, \u0394pH/\u0394V = 2.0 pH units per mL and "
          "V_{avg} = 8.25 mL. That arithmetic is reproduced here because it comes from the source; the underlying "
          "readings are not available, so it remains an illustration of //method//."),
    ("p", "Now suppose the maximum of your derivative plot falls at V_{eq} = 19.8 mL, and the NaOH was "
          "standardised to 0.0987 M, with a 20.0 mL acid aliquot:"),
    ("eq", "C_{HCl} = (0.0987 \u00d7 19.8)/20.0 = 0.0977 M"),
    ("p", "The strength in g L^{\u22121} follows from the molar mass of HCl (36.46 g mol^{\u22121}): 0.0977 "
          "\u00d7 36.46 = 3.56 g L^{\u22121}. Quoting both is good practice, and stating which one your manual "
          "wants is better."),
    ("tbl", ["Quantity", "Expression", "Illustrative value"],
     [["Equivalence volume", "maximum of \u0394pH/\u0394V", "19.8 mL"],
      ["Base concentration", "standardised", "0.0987 M"],
      ["Acid aliquot", "pipetted", "20.0 mL"],
      ["Acid concentration", "C_{b}V_{eq}/V_{a}", "0.0977 M"],
      ["Acid strength", "\u00d7 36.46 g mol^{\u22121}", "3.56 g L^{\u22121}"],
      ["pH at equivalence", "measured", "\u2248 7 (near 25 \u00b0C)"]],
     [44, 68, 56], "**Table 3.4** Calculation chain. Every line should be reproducible from the previous one.",
     ["l", "l", "c"]),
]

B += [
    ("h2", "3.6  Precautions, errors and troubleshooting"),
    ("bul", [
        "Calibrate with //fresh// buffers bracketing the range, and rinse between them.",
        "Keep the bulb immersed but clear of the vessel wall and stirrer bar.",
        "Blot the electrode gently; never rub the glass membrane.",
        "Stir gently and consistently, and record the pH only after it stabilises.",
        "Use small increments through the steep region; large steps destroy the resolution you came for.",
        "Record cumulative volume, not incremental volume, or convert explicitly.",
        "Standardise the NaOH; keep it stoppered to exclude CO_{2}.",
        "Record the temperature, because the Nernst slope and K_{w} both depend on it.",
    ]),
    ("tbl", ["Source of error", "Type", "Effect on the result", "Control"],
     [["Meter calibrated with stale buffers", "Systematic", "Whole curve shifted; V_{eq} may be biased",
       "Fresh buffers; two-point calibration"],
      ["Electrode dry or contaminated", "Systematic / random", "Slow, drifting or noisy readings",
       "Store wet; rinse between samples"],
      ["Recording before stabilisation", "Random", "Scattered points near the jump", "Wait for a steady display"],
      ["Large increments near equivalence", "Random", "Poorly located V_{eq}", "0.1 mL steps through the jump"],
      ["Temperature drift", "Systematic", "Slope and K_{w} change; curve shifts", "Record T; thermostat if possible"],
      ["Unstandardised NaOH", "Systematic", "Wrong acid concentration", "Standardise against oxalic acid"],
      ["CO_{2} absorption by NaOH", "Systematic", "Effective base strength lower", "Stoppered, fresh solution"],
      ["Electrode touching the stirrer bar", "Random / damage", "Erratic readings, possible breakage",
       "Position carefully; use a gentle stir"]],
     [48, 30, 48, 44], "**Table 3.5** Error budget.", ["l", "l", "l", "l"]),
    ("h3", "3.6.1  Troubleshooting"),
    ("tbl", ["Symptom", "Likely cause", "Action"],
     [["pH drifts continuously", "Electrode not hydrated, junction blocked, or not yet stable",
       "Soak in buffer; clean the junction; wait"],
      ["Readings jump erratically", "Air bubble on the bulb, loose connector, or electrical interference",
       "Tap gently, check the cable, move away from motors"],
      ["Curve has no clear jump", "Increments too large, or the titrant is much more concentrated than assumed",
       "Repeat with smaller steps near the expected V_{eq}"],
      ["Equivalence pH far from 7", "Calibration error, temperature, dissolved CO_{2}, or a weak acid",
       "Recalibrate; check the sample identity"],
      ["Calculated concentration implausible", "Aliquot volume, base concentration or cumulative volume wrong",
       "Re-check each entry and the units"],
      ["Derivative has two peaks", "Noise near the jump, or two titratable species", "Smooth the data; check the "
       "sample"]],
     [42, 62, 66], "**Table 3.6** Troubleshooting chart.", ["l", "l", "l"]),
]

VIVA_A = [
    ("Define pH.", "pH = \u2212log_{10} a(H^{+}); in dilute solution it is approximated as \u2212log_{10}[H^{+}]."),
    ("Why is the pH scale logarithmic?", "Because hydrogen-ion concentrations in real solutions span many orders "
                                         "of magnitude; a logarithmic scale compresses them into a convenient "
                                         "0\u201314 range."),
    ("What is a pH meter?", "An electrochemical instrument that measures the potential of a glass electrode "
                            "system and converts it into pH after calibration."),
    ("State the principle of the glass electrode.", "A potential develops across a hydrated glass membrane in "
                                                    "response to the hydrogen-ion activity of the solution, "
                                                    "following the Nernst equation."),
    ("What is the Nernst slope at 25 \u00b0C?", "About 59.2 mV per pH unit, from 2.303RT/F."),
    ("Why calibrate with two buffers?", "One buffer sets the offset; a second sets the slope, so both systematic "
                                        "errors are corrected and a failing electrode is detected."),
    ("Why rinse the electrode between solutions?", "To prevent carry-over of one solution into the next, which "
                                                   "would contaminate the sample and bias the reading."),
    ("What is the equivalence point?", "The stoichiometric point at which the moles of base added equal the moles "
                                       "of acid originally present."),
    ("What is the endpoint?", "The experimentally observed point \u2014 here the steepest part of the curve \u2014 "
                              "used to estimate the equivalence point."),
    ("Write the neutralisation reaction.", "HCl + NaOH \u2192 NaCl + H_{2}O; net ionic H^{+} + OH^{\u2212} "
                                           "\u2192 H_{2}O."),
    ("What is the stoichiometric ratio?", "1:1, because HCl is monobasic and NaOH monobasic."),
    ("Why is the pH at equivalence approximately 7?", "The salt NaCl does not hydrolyse, so at equivalence the "
                                                       "only equilibrium is water autoionisation, giving pH 7 at "
                                                       "25 \u00b0C."),
    ("Why does the pH rise steeply near equivalence?", "Because the excess changes sign: a tiny addition takes the "
                                                       "solution from a small excess of H^{+} to a small excess of "
                                                       "OH^{\u2212}, a change of many orders of magnitude in "
                                                       "[H^{+}]."),
    ("What does the flat region before equivalence represent?", "The presence of excess strong acid, whose "
                                                                "concentration is only slowly reduced by dilution."),
    ("Why does the curve flatten again after equivalence?", "Because the excess hydroxide is progressively diluted "
                                                            "by the added titrant."),
    ("What is \u0394pH/\u0394V?", "The first derivative of the titration curve \u2014 the rate of change of pH "
                                  "with added volume."),
    ("Why does the derivative peak at equivalence?", "Because the slope of the curve is greatest where the pH "
                                                     "changes fastest, which is the equivalence point."),
    ("Why is the average volume used on the derivative x-axis?", "Because \u0394pH/\u0394V belongs to the interval, "
                                                                 "and its representative volume is the midpoint of "
                                                                 "that interval."),
    ("How do you calculate the acid concentration?", "C_{HCl} = C_{NaOH} V_{eq}/V_{HCl}, from the 1:1 "
                                                     "stoichiometry."),
    ("Why does adding distilled water not change V_{eq}?", "It dilutes the solution but does not change the moles "
                                                           "of acid present, and the moles of base needed to "
                                                           "neutralise them are unchanged."),
    ("Why does adding water change the initial pH?", "Because the acid concentration falls, and pH depends on "
                                                     "concentration, not on amount."),
    ("Is HCl a strong acid?", "Yes \u2014 it is essentially fully dissociated in dilute aqueous solution."),
    ("What is the difference between strong and concentrated?", "Strong refers to the extent of ionisation; "
                                                                "concentrated refers to the amount of solute per "
                                                                "unit volume. A dilute solution of a strong acid "
                                                                "is still fully ionised."),
    ("What salt is formed and what happens to it?", "Sodium chloride; it remains fully dissociated and does not "
                                                    "hydrolyse, so it does not affect the equivalence pH."),
]

VIVA_B = [
    ("Why not simply use an indicator?", "An indicator gives one colour change somewhere inside a nine-unit jump "
                                         "and cannot tell you where; the pH curve gives the whole shape and locates "
                                         "the steepest point precisely. For a strong acid/strong base system, "
                                         "either works, but the curve is more informative and more defensible."),
    ("Why is the electrode stored in buffer or KCl solution?", "To keep the glass membrane hydrated and the "
                                                               "junction wet; a dry electrode responds slowly and "
                                                               "drifts."),
    ("Why is the stirring gentle?", "Vigorous stirring creates bubbles and vortices that give unstable readings, "
                                    "and risks striking the electrode."),
    ("Why must the reading stabilise before it is recorded?", "The electrode has a finite response time and the "
                                                              "solution must mix; recording an unsettled value "
                                                              "adds scatter exactly where precision matters."),
    ("Why are smaller increments used near equivalence?", "Because a small volume produces a large pH change there; "
                                                          "fine steps resolve the jump, coarse steps skip over it."),
    ("Why is NaOH standardised rather than weighed directly?", "Solid NaOH absorbs water and CO_{2} from air, so a "
                                                               "weighed mass does not correspond to a known amount "
                                                               "of hydroxide; a standard acid titration gives the "
                                                               "true concentration."),
    ("Why is oxalic acid used as the primary standard?", "It is a stable, pure solid that can be weighed "
                                                         "accurately, and it reacts stoichiometrically with "
                                                         "hydroxide."),
    ("Why keep NaOH stoppered?", "Atmospheric CO_{2} dissolves and forms carbonate, lowering the effective "
                                 "hydroxide concentration and shifting V_{eq}."),
    ("Why is the burette read at eye level?", "To avoid parallax error, which can bias a reading by a tenth of a "
                                              "millilitre or more."),
    ("Why is the tip of the burette cleared of air before starting?", "An air bubble displaces liquid and causes "
                                                                      "the delivered volume to be less than the "
                                                                      "scale reading."),
    ("Why does the electrode have to be immersed to a consistent depth?", "The response depends on the wetted "
                                                                          "area of the membrane, and the junction "
                                                                          "must remain in contact with the "
                                                                          "solution."),
    ("Why is the temperature recorded?", "Both the Nernst slope and K_{w} depend on temperature, so pH values and "
                                         "the equivalence pH are only strictly valid at a stated temperature."),
    ("What would a systematic offset of 0.4 pH units do?", "It would shift the whole curve and move the apparent "
                                                           "equivalence pH, but it would not move the position of "
                                                           "the maximum slope, so V_{eq} would be almost "
                                                           "unaffected."),
    ("Why is the equivalence point better located from the derivative than from the pH value?", "Because the "
                                                                                               "maximum slope is a "
                                                                                               "structural feature of "
                                                                                               "the data, whereas the "
                                                                                               "absolute pH at "
                                                                                               "equivalence is "
                                                                                               "sensitive to "
                                                                                               "calibration."),
    ("What is ionic activity, and why does it matter?", "It is the effective concentration that governs chemical "
                                                        "potential, allowing for non-ideal ion\u2013ion "
                                                        "interactions. Electrodes respond to activity, not to "
                                                        "concentration, which is why pH is defined on activity."),
    ("Why does the curve of a weak acid look different?", "A weak acid buffers over a range around its pK_{a}, "
                                                          "producing a flatter curve with a smaller jump and an "
                                                          "equivalence pH above 7."),
    ("Why is the jump smaller for a weak acid?", "Because at equivalence the conjugate base hydrolyses, buffering "
                                                 "the solution, so the pH change per unit volume is smaller."),
    ("Could you titrate a mixture of HCl and acetic acid this way?", "Yes \u2014 the curve shows two jumps, the "
                                                                     "first for the strong acid and the second for "
                                                                     "the weak acid; the first equivalence volume "
                                                                     "gives HCl directly."),
    ("Why is a combination electrode convenient?", "It contains the glass and reference electrodes in one body, so "
                                                   "only one probe needs to be positioned and rinsed."),
    ("Why is the reference junction important?", "It completes the electrical circuit; a blocked or dry junction "
                                                 "produces slow, noisy or frozen readings."),
]

VIVA_C = [
    ("What if you forgot to calibrate the meter?", "The whole curve would be shifted, and if the slope were also "
                                                   "wrong, the jump could be distorted. The equivalence volume "
                                                   "would still be roughly correct, but the reported pH values "
                                                   "would be meaningless."),
    ("What if you used one buffer instead of two?", "The offset would be corrected but a slope error would go "
                                                    "undetected, so pH values far from the buffer would be wrong "
                                                    "even though the mid-range looked correct."),
    ("What if you added 5 mL increments throughout?", "You would likely step over the jump entirely, and the "
                                                      "derivative would have no defined peak; V_{eq} could be "
                                                      "wrong by millilitres."),
    ("What if the aliquot were 25 mL instead of 20 mL?", "V_{eq} would rise proportionally, but the calculated "
                                                         "concentration would be unchanged if the correct volume "
                                                         "were used in the formula. If you used 20 mL in the "
                                                         "calculation, the result would be 25 % too high."),
    ("What if the NaOH were 0.05 M instead of 0.1 M?", "V_{eq} would double, and the curve would be stretched "
                                                      "horizontally; the calculated concentration would be "
                                                      "correct provided the true concentration were used."),
    ("What if the electrode were left dry overnight?", "Its response would be slow and unstable, and the "
                                                       "calibration might not hold; soak it in buffer before use."),
    ("What if you recorded pH before the reading settled?", "The points near the jump would be scattered, and the "
                                                            "derivative peak would be broadened or split."),
    ("What if the solution were stirred vigorously?", "Bubbles and vortices would give noisy readings, and the "
                                                      "electrode or stirrer bar could be damaged."),
    ("What if CO_{2} were absorbed by the NaOH?", "The effective hydroxide concentration would fall, so the "
                                                  "delivered base would be weaker than stated and V_{eq} would "
                                                  "shift to a larger volume, biasing the acid concentration low."),
    ("What if you extrapolated the two flat regions to find equivalence?", "You would get the wrong answer for a "
                                                                           "strong/strong titration, because the "
                                                                           "jump is symmetric about pH 7 but the "
                                                                           "flat regions are not straight lines; "
                                                                           "the derivative maximum is correct."),
    ("What if the sample were a weak acid instead?", "The equivalence pH would be above 7, the jump smaller, and "
                                                     "the acid concentration calculation would need the "
                                                     "stoichiometry but not the pH; the curve shape would be the "
                                                     "main diagnostic."),
    ("What if two jumps appeared?", "There are two titratable species (for example a strong acid plus a weak acid, "
                                    "or a dibasic acid); each jump gives one equivalence volume."),
    ("What if the burette had an air bubble that cleared during the titration?", "The recorded volumes would not "
                                                                                "correspond to the delivered "
                                                                                "volumes, so the whole curve would "
                                                                                "be shifted after the bubble cleared."),
]

VIVA_D = [
    ("Is the equivalence pH always exactly 7?", "No. It is 7 only for a strong acid/strong base pair at 25 \u00b0C "
                                                "in ideal dilute solution. Temperature, activity coefficients and "
                                                "the nature of the acid and base all shift it."),
    ("Does a pH meter measure concentration?", "No \u2014 it measures activity. In dilute solution the two are "
                                               "nearly equal, but at higher ionic strength the difference becomes "
                                               "significant."),
    ("Why can a pH of 7 be neutral but not always?", "Because neutrality means [H^{+}] = [OH^{\u2212}], and that "
                                                     "condition corresponds to pH 7 only at 25 \u00b0C, where "
                                                     "K_{w} = 10^{\u221214}; at other temperatures the neutral pH "
                                                     "differs."),
    ("Can pH be negative?", "Yes. In concentrated strong acid, [H^{+}] can exceed 1 M, giving a negative pH. The "
                            "scale is not bounded at 0 or 14."),
    ("Why is the pH jump smaller at higher concentration?", "Because the concentration of the excess species is "
                                                            "higher on both sides, so the ratio change across "
                                                            "equivalence is smaller."),
    ("If the pH at equivalence differs from 7, is the titration invalid?", "No. The volume at the point of steepest "
                                                                          "change is still the equivalence volume; "
                                                                          "the absolute pH there is affected by "
                                                                          "calibration and activity."),
    ("Why does the derivative method give a sharper answer than the inflection method?", "Because a maximum is "
                                                                                        "easier to locate than a "
                                                                                        "point where curvature "
                                                                                        "changes, and differentiation "
                                                                                        "suppresses slow baseline "
                                                                                        "drift."),
    ("What is the physical meaning of the area under the derivative curve?", "It equals the total pH change over "
                                                                             "that volume interval \u2014 the "
                                                                             "integral of a derivative returns the "
                                                                             "original function."),
    ("Why does the electrode respond to H^{+} and not, say, Na^{+}?", "The glass composition is designed for "
                                                                     "selectivity towards hydrogen ions, though at "
                                                                     "very high pH or high sodium concentration "
                                                                     "\u201cerrors\u201d appear."),
    ("What is the alkaline error of a glass electrode?", "At high pH and high Na^{+} concentration, the electrode "
                                                         "responds partly to sodium, so the measured pH is lower "
                                                         "than the true value."),
    ("What is the acid error?", "At very low pH, the measured pH can be slightly higher than the true value, "
                                "largely due to changes in the hydrated layer."),
    ("Would this titration work for a polyprotic acid?", "Yes, but the curve would show a jump per titratable "
                                                         "proton, and the peaks would correspond to successive "
                                                         "deprotonations."),
]

CH3_CHECK = checklist(
    "3.8",
    ["pH = \u2212log_{10} a(H^{+}) \u2248 \u2212log_{10}[H^{+}] in dilute solution.",
     "Reaction: HCl + NaOH \u2192 NaCl + H_{2}O; net H^{+} + OH^{\u2212} \u2192 H_{2}O.",
     "1:1 stoichiometry; C_{a}V_{a} = C_{b}V_{eq}.",
     "Before equivalence the excess strong acid controls pH.",
     "At equivalence the solution is NaCl; pH \u2248 7 at 25 \u00b0C.",
     "After equivalence the excess strong base controls pH.",
     "The jump spans roughly 4 to 10 pH units in a few tenths of a millilitre.",
     "The logarithmic scale is why the jump is abrupt.",
     "Equivalence is located at the maximum of \u0394pH/\u0394V.",
     "Nernst slope at 25 \u00b0C is about 59.2 mV per pH unit.",
     "Calibrate with two buffers bracketing the expected range.",
     "Rinse and blot the electrode; never rub the bulb.",
     "Diluting the aliquot changes the initial pH but not V_{eq}.",
     "Use 0.1 mL steps through the steep region.",
     "Record cumulative volume and stable pH.",
     "Standardise NaOH; it absorbs CO_{2} and water.",
     "Record the temperature \u2014 slope and K_{w} depend on it.",
     "The equivalence pH need not read exactly 7.00 on your meter.",
     "The derivative peak locates V_{eq} more robustly than the pH value there.",
     "Electrode contact with the stirrer bar is the classic breakage accident."],
    ["Sketch the curve and explain its three regions.",
     "What is the equivalence point, and how is it found here?",
     "Why is the pH at equivalence about 7?",
     "Why does the pH change so abruptly near equivalence?",
     "Why must the meter be calibrated, and how?",
     "Why is the acid diluted before titration, and what does it change?",
     "How is the acid concentration calculated from V_{eq}?",
     "Why are small increments used near the end?",
     "What does the derivative plot show?",
     "State the Nernst relation and the meaning of the slope."],
    ["Derive the pH at any point before and after equivalence for this system, and explain each approximation.",
     "Show why the jump spans roughly nine pH units, using actual numbers.",
     "Explain why the equivalence pH shifts with temperature, and by roughly how much.",
     "Your measured pH at equivalence is 6.4. List the possible causes and how each would be detected.",
     "Distinguish equivalence from endpoint and explain why the derivative makes the distinction sharper.",
     "Why does the electrode respond to activity rather than concentration, and when does that matter?",
     "What is the alkaline error, and under what conditions would it affect this experiment?",
     "Explain why the flat regions are not straight lines in a real titration.",
     "How would the curve change if the acid were 0.001 M rather than 0.1 M?",
     "If the burette had a systematic +0.15 mL offset, what would happen to your reported concentration?"],
    [("Equivalence vs endpoint", "Stoichiometric fact vs observed estimate."),
     ("Strong vs concentrated", "Ionisation extent vs amount per volume."),
     ("pH vs pOH", "pH + pOH = 14 only at 25 \u00b0C in dilute solution."),
     ("Activity vs concentration", "The electrode responds to activity."),
     ("Cumulative vs incremental volume", "The curve\u2019s x-axis is cumulative."),
     ("Inflection vs maximum slope", "Same point, two ways of locating it."),
     ("Buffering vs neutralisation", "Buffering resists pH change; neutralisation consumes acid or base."),
     ("Calibration offset vs slope error", "Offset shifts the curve; slope error tilts it.")],
    (["Relation", "Expression", "Note"],
     [["pH", "pH = \u2212log_{10} a(H^{+})", "Definition"],
      ["Water ionisation", "pH + pOH = 14", "At 25 \u00b0C only"],
      ["Nernst slope", "E = E^{0} \u2212 0.0592 pH", "At 25 \u00b0C"],
      ["Before equivalence", "[H^{+}] = (n_{a}\u2212n_{b})/V_{total}", "Excess acid"],
      ["After equivalence", "[OH^{\u2212}] = (n_{b}\u2212n_{a})/V_{total}", "Excess base"],
      ["Equivalence", "C_{a}V_{a} = C_{b}V_{eq}", "1:1 stoichiometry"],
      ["Derivative", "\u0394pH/\u0394V, plotted at V_{avg}", "Peak at V_{eq}"],
      ["Acid strength", "g L^{\u22121} = C \u00d7 36.46", "For HCl"]],
     [38, 74, 56]),
    [["No visible jump in the curve", "Increments too large near equivalence"],
     ["Readings drift steadily upward", "Electrode not hydrated or junction partly blocked"],
     ["Erratic, spiky readings", "Bubble on the bulb, loose connector, or stirrer interference"],
     ["Equivalence pH far from 7", "Calibration offset, temperature, dissolved CO_{2}"],
     ["Curve shifted but jump intact", "Systematic calibration offset; V_{eq} still usable"],
     ["Two derivative peaks", "Two titratable species, or noise near the jump"],
     ["Concentration 20 % too high", "Aliquot volume used in the formula is too small"]],
    ["The jump is abrupt because the pH scale is logarithmic, not because the reaction is violent.",
     "Dilution changes the curve\u2019s position but not V_{eq}.",
     "The derivative peak is more robust than the equivalence pH value.",
     "A single-buffer calibration cannot detect a slope error.",
     "NaOH must be standardised because it is not a primary standard.",
     "Activity, not concentration, is what the electrode actually measures.",
     "An offset shifts the curve; it does not move the steepest point."],
    ["Recording incremental rather than cumulative volume.",
     "Using an unexplained \u201cequivalence pH = 7\u201d as the endpoint criterion.",
     "Skipping the derivative calculation and reading V_{eq} by eye.",
     "Forgetting to state the temperature.",
     "Reporting the acid strength in molarity when the manual asks for g L^{\u22121}, or vice versa.",
     "Failing to standardise NaOH.",
     "Not plotting the second plateau, so the jump cannot be identified."],
    ["I titrate a measured aliquot of HCl with standard NaOH while recording pH after each addition. HCl and NaOH "
     "react 1:1 to give NaCl and water. Before equivalence the pH is set by the excess strong acid and rises "
     "slowly; at equivalence the solution contains only NaCl, so the pH is near 7 at 25 \u00b0C; after equivalence "
     "the excess hydroxide sets the pH and the curve flattens at high pH. Because pH is logarithmic, the curve is "
     "almost vertical near equivalence \u2014 a few hundredths of a millilitre changes [H^{+}] by many orders of "
     "magnitude. To resolve that region I use 0.1 mL increments there. I plot pH against cumulative volume and "
     "also \u0394pH/\u0394V against the average interval volume; the maximum of the derivative locates the "
     "equivalence volume. The acid concentration then follows from C_{a}V_{a} = C_{b}V_{eq}. The critical "
     "controls are a two-buffer calibration, a rinsed and undamaged electrode, stable readings, and a standardised "
     "base."],
    ["**Calibrate \u2192 aliquot \u2192 add in steps \u2192 record stable pH \u2192 derivative peak = V_{eq}**",
     "**Before: acid rules. At: NaCl, pH 7. After: base rules.**",
     "**Log scale \u2192 vertical jump \u2192 small steps.**",
     "**Electrode: rinse, blot, never rub, never touch the bar.**"]
)

CH3 = {
    "key": "phmet",
    "num": "3",
    "kicker": "Experiment 3  \u00b7  Electroanalytical titration",
    "title": "pH-Metric Titration of a Strong Acid with a Strong Base",
    "toc": "pH-metric titration (HCl with NaOH)",
    "standfirst": "One colour change becomes a whole curve. This chapter explains why the pH jumps, how to "
                  "resolve the jump experimentally, and how the derivative turns a shape into a volume.",
    "body": B + [
        ("h2", "3.7  Viva question bank"),
        ("p", "Sixty-nine answered questions. The theory section above already contains the derivations an "
              "examiner is most likely to probe; the bank below tests whether you can retrieve them under "
              "pressure."),
        ("qsub", "A.  Fundamental questions"),
        ("qa", VIVA_A),
        ("qsub", "B.  \u201cWhy\u201d and \u201chow\u201d questions"),
        ("qa", VIVA_B),
        ("qsub", "C.  \u201cWhat if\u201d questions"),
        ("qa", VIVA_C),
        ("qsub", "D.  Tricky and advanced questions"),
        ("qa", VIVA_D),
    ] + CH3_CHECK,
}
