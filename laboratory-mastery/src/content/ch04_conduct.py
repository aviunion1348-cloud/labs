VIVA_E = [
    ("Why does the conductance of a strong electrolyte increase with concentration?",
     "More ions are present per unit volume, so more charge is carried."),
    ("Why does it not increase linearly at high concentration?",
     "Ion\u2013ion interactions and reduced mobility lower the conductivity per ion."),
    ("What is the effect of temperature on conductance?",
     "It increases, because viscosity falls and ions move more freely."),
    ("Why is the conductometric method unsuitable for concentrated solutions?",
     "The conductance varies too little per unit of added titrant, so the branches are hard to distinguish."),
    ("What is the purpose of a conductometric titration at all?",
     "To locate the equivalence point precisely without an indicator, especially in dilute or coloured systems."),
    ("What does a horizontal branch indicate?",
     "That the conductivity is not changing appreciably during that stage of the titration."),
    ("Why can a weak acid give a curved first branch?",
     "Because its dissociation changes as it is neutralised, so the ionic composition changes non-linearly."),
    ("What determines the angle between the two branches?",
     "The difference in mobility between the ions being removed and the ions being added."),
    ("Why must the electrodes be platinised?",
     "To reduce polarisation and give a stable, reproducible reading."),
    ("Why is alternating current used in conductometry?",
     "Direct current would polarise and electrolyse the solution."),
    ("What is the effect of a systematic cell-constant error?",
     "It scales the conductivity without changing the position of the equivalence point."),
    ("Why does the equivalence point survive a scaling error?",
     "Because the intersection of the branches is a ratio property, insensitive to the multiplicative constant."),
    ("How would you obtain the conductance of the titrant itself?",
     "From the slope and intercept of the post-equivalence branch, or by measuring the titrant directly."),
    ("What is the difference between conductance and conductivity?",
     "Conductance is the reciprocal resistance of a particular cell; conductivity is the intensive property of "
     "the solution."),
    ("Why is the molar conductance a more useful quantity than the raw conductance?",
     "Because it is normalised for concentration, so different solutions can be compared."),
    ("What is the Kohlrausch law of independent migration?",
     "The limiting molar conductance is the sum of the limiting ionic conductances."),
    ("How would a very dilute titration fail?",
     "The conductance would be dominated by the background electrolyte and by dissolved CO_{2}."),
    ("Why should the titration be stirred?",
     "To homogenise the solution so that the reading represents the whole cell, not a local excess."),
    ("Why is the graph plotted as conductance against volume rather than conductance against time?",
     "Because volume is the controlled variable that relates directly to the stoichiometry."),
    ("What would a third branch indicate?",
     "A second reaction stage, such as neutralisation of a second acidic proton or precipitation followed by "
     "further addition."),
]
"""Chapter 4 - Conductometric titration of HCl with NaOH."""
from common import checklist

B = []

B += [
    ("h2", "4.1  A titration followed by electricity instead of colour"),
    ("lead", "Conductometry replaces the eye with a pair of electrodes. You do not look for a colour change; you "
             "watch a number that falls, reaches a minimum and rises again. The point where the slope changes "
             "sign is the equivalence point \u2014 and it can be found in coloured, turbid or otherwise "
             "uncooperative solutions where an indicator would fail."),
    ("p", "The aim from the supplied material is to **determine the strength of a given HCl solution "
          "conductometrically.** The physical principle is stated on the handwritten source page in one line: "
          "conductivity depends on the **number and mobility** of ions. That single sentence generates the whole "
          "curve, and it is worth building the chapter around it."),
    ("eq", "HCl + NaOH \u2192 NaCl + H_{2}O;   net ionic: H^{+} + OH^{\u2212} \u2192 H_{2}O;   "
           "spectators: Na^{+}, Cl^{\u2212}",
     "Equation 4.1 \u2014 the reaction. The important part is not what reacts but **which ions replace which** in "
     "solution."),
    ("defbox", [
        ("Conductance (G)", "The reciprocal of resistance, G = 1/R, measured in siemens (S). It depends on the "
                            "solution //and// on the cell geometry."),
        ("Conductivity (\u03ba)", "Conductance corrected for cell geometry: \u03ba = G \u00d7 (cell constant). An "
                                 "intrinsic property of the solution, in S m^{\u22121}."),
        ("Cell constant", "The ratio of electrode separation to effective electrode area, in m^{\u22121} (or "
                          "cm^{\u22121}). It converts measured conductance into conductivity."),
        ("Ionic mobility", "The drift velocity of an ion per unit electric field, in m^{2} V^{\u22121} "
                           "s^{\u22121}. It determines how much current a given concentration of that ion can "
                           "carry."),
        ("Limiting molar conductivity", "The conductivity of one mole of electrolyte at infinite dilution, "
                                        "summing the contributions of its ions (Kohlrausch)."),
    ]),
    ("box", "key", [
        "**H^{+} is exceptional.** Its mobility in water is several times that of Na^{+}, because it moves by "
        "proton transfer along hydrogen bonds rather than by bodily migration of a hydrated ion.",
        "**Replacing H^{+} with Na^{+} therefore lowers conductance**, even though the concentration of charge "
        "carriers is unchanged.",
        "**After equivalence, OH^{\u2212} accumulates** \u2014 and OH^{\u2212} is also exceptionally mobile. "
        "Conductance rises steeply.",
        "The result is a **V-shaped curve with two straight branches**, whose intersection is the equivalence "
        "point.",
    ], "The four facts that generate the entire curve"),
    ("fig", "conduct", "**Figure 4.1** Conductometric titration assembly. The cell must stay upright, at a "
                       "constant immersion depth, in a solution of constant temperature. The meter is not touched "
                       "during the run \u2014 only additions change."),
]

B += [
    ("h2", "4.2  Theory: from ionic mobility to a V-shaped graph"),
    ("h3", "4.2.1  Why an electrolyte conducts at all"),
    ("p", "In a metal, current is carried by electrons. In a solution, it is carried by **ions in motion**. When "
          "an electric field is applied between the electrodes, cations drift towards the cathode and anions "
          "towards the anode; the resulting charge transport is the current. The conductance of the solution "
          "depends on three things:"),
    ("num", [
        "**How many ions carry charge** \u2014 that is, concentration and charge number.",
        "**How fast each ion moves** in a given field \u2014 its mobility, which depends on size, charge and "
        "solvation.",
        "**The geometry of the cell** \u2014 how far apart the electrodes are and how much area they present.",
    ]),
    ("p", "The first two are properties of the solution; the third is a property of the instrument. Conductivity "
          "separates them:"),
    ("eq", "G = 1/R;   \u03ba = G \u00d7 (l/A) = G \u00d7 \u03b8",
     "Equation 4.2 \u2014 conductance and conductivity, where \u03b8 = l/A is the cell constant. Note that "
     "conductance is what the meter measures; conductivity is what you compare between instruments."),
    ("h3", "4.2.2  The mobility hierarchy that makes the experiment work"),
    ("tbl", ["Ion", "Limiting ionic conductivity at 25 \u00b0C (S cm^{2} mol^{\u22121})", "Relative mobility",
             "Mechanism of transport"],
     [["H^{+}", "349.8", "\u2248 1 (reference high)", "Proton hopping along the hydrogen-bond network (Grotthuss)"],
      ["OH^{\u2212}", "198.3", "\u2248 0.57", "Proton-hole hopping along the hydrogen-bond network"],
      ["Na^{+}", "50.1", "\u2248 0.14", "Bodily migration of the hydrated ion"],
      ["Cl^{\u2212}", "76.3", "\u2248 0.22", "Bodily migration of the hydrated ion"]],
     [18, 56, 30, 66],
     "**Table 4.1** Limiting ionic conductivities (standard reference values at 25 \u00b0C). The ratio between "
     "H^{+} and Na^{+} \u2014 about seven to one \u2014 is the entire reason the conductance **falls** when NaOH "
     "is added.", ["c", "c", "c", "l"]),
    ("p", "The numbers above are textbook constants, not measurements from your run; they are quoted so that the "
          "shape of the curve can be predicted before the experiment begins. That predictive step is exactly what "
          "an examiner wants to see: you should be able to say what the curve will look like, and why, before you "
          "titrate."),
    ("h3", "4.2.3  Predicting the shape, region by region"),
    ("p", "**Before equivalence.** Each hydroxide added removes one H^{+} and adds one Na^{+}. The number of "
          "charges is unchanged, but a highly mobile carrier is replaced by a sluggish one. So the conductance "
          "falls, essentially linearly with added volume, because the replacement is stoichiometric. The slope is "
          "proportional to (\u03bb(H^{+}) \u2212 \u03bb(Na^{+}))."),
    ("p", "**At equivalence.** All the H^{+} has been consumed. The solution contains only NaCl. The conductance "
          "is **not zero** \u2014 a very common misconception \u2014 because Na^{+} and Cl^{\u2212} still carry "
          "current. It is simply at its minimum."),
    ("p", "**After equivalence.** Each further addition adds NaOH that cannot react, so Na^{+} and OH^{\u2212} "
          "both accumulate. Since OH^{\u2212} is highly mobile, the conductance rises steeply. The slope is "
          "proportional to (\u03bb(Na^{+}) + \u03bb(OH^{\u2212}))."),
    ("eq", "V_{eq} = intersection of the two linear branches",
     "Equation 4.3 \u2014 the operational definition. Note that the branches are extrapolated as straight lines "
     "and intersected, **not** taken from the lowest single point, which is noisy."),
    ("plot", "conduct", "**Figure 4.2** Conductometric titration curve for HCl against NaOH. The descending "
                        "branch is the replacement of H^{+} by Na^{+}; the ascending branch is the accumulation of "
                        "excess OH^{\u2212}. The intersection gives V_{eq}; note that the conductance at "
                        "equivalence is finite, because NaCl still conducts."),
    ("h3", "4.2.4  Why the branches are straight, and when they are not"),
    ("p", "Within each region, the conductance is the sum of contributions from all ions present, each "
          "proportional to its concentration and its molar conductivity. Before equivalence, the amount of each "
          "ion varies linearly with added volume; after equivalence, likewise. Dilution introduces a mild curvature, "
          "which is why real branches are only approximately straight and why the intersection method is preferred "
          "to reading the minimum."),
    ("h3", "4.2.5  From V_{eq} to concentration"),
    ("eq", "C_{HCl} = (C_{NaOH} \u00d7 V_{eq})/V_{HCl}",
     "Equation 4.4 \u2014 the working calculation, identical in form to the pH-metric case because the "
     "stoichiometry is the same 1:1 reaction."),
]

B += [
    ("h2", "4.3  Apparatus"),
    ("tbl", ["Item", "Function", "Consequence of a fault"],
     [["Conductivity meter", "Measures conductance (or conductivity) and displays it",
       "Uncalibrated or wrong range gives meaningless numbers"],
      ["Conductivity cell (platinum or platinised electrodes)", "Defines the cell constant and senses the solution",
       "Dirty, dry or bubbled electrodes give drifting readings"],
      ["Burette", "Delivers standard NaOH in measured increments", "Air bubbles or leaks bias the volumes"],
      ["Pipette (10 mL)", "Delivers the acid aliquot", "A wrong aliquot scales the result"],
      ["Beaker", "Holds the solution so the cell can be immersed", "A beaker too small forces the cell to touch "
       "the wall"],
      ["Magnetic stirrer", "Homogenises the solution", "Poor mixing means the cell measures a local concentration"],
      ["Standard 0.1 N NaOH", "Titrant", "Unstandardised base gives a wrong acid strength"],
      ["Distilled water", "Dilutes the aliquot so the cell is immersed", "Tap water adds background conductance"]],
     [50, 58, 62], "**Table 4.2** Apparatus. The cell is the delicate element; the meter is the unforgiving one.",
     ["l", "l", "l"]),
    ("box", "note", [
        "The supplied material is inconsistent about the increment schedule: one handwritten page describes 2 mL "
        "followed by 0.1 mL steps, another observation sheet records 0.5 mL steps. **Confirm the schedule with your "
        "instructor before starting** and record what you actually did. The physics is unaffected, but the "
        "resolution of the intersection depends on it.",
    ], "A source inconsistency to settle first"),
]

B += [
    ("h2", "4.4  Procedure with reasoning"),
    ("num", [
        "**Rinse and condition the cell** with distilled water and then with a little of the acid solution. Dry "
        "surfaces and residual salts both distort the first reading.",
        "**Pipette the specified aliquot** (the handwritten page says 10 mL) into a beaker and add enough "
        "distilled water to immerse the cell comfortably. The dilution does not change the moles of HCl, so it "
        "does not change V_{eq}; it does lower the initial conductance and the slopes.",
        "**Place the cell upright, immersed to a consistent depth**, clear of the beaker wall and the stirrer bar.",
        "**Stir gently and record the initial conductance** once stable.",
        "**Add NaOH in the prescribed increments.** Add, stir, wait for the reading to stabilise, then record the "
        "conductance against the **cumulative** volume.",
        "**Use smaller increments near the expected minimum**, because that is where the slope changes sign and "
        "where the intersection is defined.",
        "**Continue at least 3\u20135 mL past the minimum**, so that the rising branch is well established. Without "
        "it there is no intersection to find.",
        "**Plot conductance against cumulative volume**, fit straight lines to the two branches, and take their "
        "intersection as V_{eq}.",
        "**Calculate the acid strength** from Equation 4.4.",
    ]),
    ("box", "caution", [
        "**Do not lift the cell out of the solution between readings**, and do not change its depth or "
        "orientation. Conductance depends on the immersed geometry; moving the cell changes the cell constant "
        "mid-experiment and produces a step in the curve that can be mistaken for a chemical effect.",
    ], "The rule that protects the curve"),
    ("box", "exam", [
        "A favourite examiner question: \u201cwhy does the conductance not fall to zero at the equivalence "
        "point?\u201d Because the solution at equivalence is sodium chloride solution \u2014 Na^{+} and "
        "Cl^{\u2212} are still present and still mobile. The conductance is a **minimum**, not a zero.",
        "The second favourite: \u201cwhy continue past the endpoint?\u201d Because a single minimum cannot define "
        "a V-shape. You need both branches to locate their intersection; the minimum alone is a noisy point, not "
        "a structural feature.",
    ], "Two questions asked every time"),
]

B += [
    ("h2", "4.5  Observations and calculation"),
    ("tbl", ["S. No.", "NaOH added (mL)", "Cumulative volume (mL)", "Conductance G (mS)", "Remark"],
     [[str(i), "", "", "", ""] for i in range(1, 13)],
     [14, 34, 38, 40, 44],
     "**Table 4.3** Observation table. The supplied source records 0.5 mL additions with some entries overwritten; "
     "those values cannot be treated as data and are not reproduced. Use your own readings.",
     ["c", "c", "c", "c", "l"]),
    ("h3", "4.5.1  Worked illustration"),
    ("p", "Suppose the descending branch passes through (0 mL, 5.60 mS) and (8.0 mL, 2.55 mS), and the ascending "
          "branch through (8.0 mL, 2.55 mS) and (14.0 mL, 5.15 mS). Both lines meet at 8.0 mL, so V_{eq} = 8.0 mL. "
          "With 0.1 N NaOH and a 10.0 mL aliquot:"),
    ("eq", "C_{HCl} = (0.1 \u00d7 8.0)/10.0 = 0.080 N \u2261 0.080 M (HCl is monobasic)"),
    ("p", "In g L^{\u22121}: 0.080 \u00d7 36.46 = 2.92 g L^{\u22121}. The numbers are illustrative and chosen for "
          "clean arithmetic; they are consistent with the shape shown in Figure 4.2, which is itself a computed "
          "illustration."),
    ("p", "An important check: the two slopes should have **opposite signs and unequal magnitudes**. If they are "
          "equal in magnitude, the mobile-ion replacement and the excess-hydroxide accumulation would be "
          "contributing equally \u2014 which is not what the mobility table predicts \u2014 so suspect a "
          "recording error."),
]

B += [
    ("h2", "4.6  Precautions, errors and troubleshooting"),
    ("bul", [
        "Keep the cell upright, at constant depth, and do not remove it mid-run.",
        "Rinse the cell before the run and keep it clean; contaminated electrodes give drifting readings.",
        "Stir gently and consistently, and wait for stable readings.",
        "Keep the temperature constant and record it \u2014 conductivity rises about 2 % per \u00b0C for typical "
        "aqueous solutions.",
        "Use the same increment schedule throughout and record **cumulative** volume.",
        "Continue well past the minimum to establish the rising branch.",
        "Standardise the NaOH and keep it stoppered.",
        "Use distilled, not tap, water for dilution.",
    ]),
    ("tbl", ["Source of error", "Type", "Effect on V_{eq}", "Control"],
     [["Temperature drift", "Systematic", "Shifts both branches; minimum may move", "Record and stabilise T"],
      ["Bubbles clinging to electrodes", "Random", "Erratic readings, apparent minimum displaced",
       "Tap the cell gently; refill"],
      ["Cell depth changed during run", "Systematic step", "Spurious kink in the curve", "Do not move the cell"],
      ["Dirty electrodes", "Systematic", "Lower, drifting conductance", "Clean and condition the cell"],
      ["Tap water used for dilution", "Systematic", "High background conductance, flatter curve",
       "Distilled water only"],
      ["Large increments near equivalence", "Random", "Poorly defined intersection", "Smaller steps near the "
       "minimum"],
      ["Unstandardised NaOH", "Systematic", "Wrong concentration", "Standardise"],
      ["CO_{2} in NaOH", "Systematic", "Lower effective base strength", "Stoppered, fresh solution"]],
     [46, 28, 48, 48], "**Table 4.4** Error budget.", ["l", "l", "l", "l"]),
    ("tbl", ["Symptom", "Likely cause", "Action"],
     [["Conductance rises from the start", "Wrong solution, cell not immersed, or meter on the wrong range",
       "Check the sample, the cell and the meter"],
      ["No minimum, monotonic fall", "Not enough NaOH added past equivalence", "Continue the titration"],
      ["Curve is noisy", "Bubbles, poor stirring, or a dirty cell", "Clean, degas, stir gently"],
      ["Minimum displaced between runs", "Temperature difference or inconsistent cell depth",
       "Standardise the procedure"],
      ["Conductance much higher than expected", "Tap water, contaminated glassware, or too little dilution",
       "Use distilled water; rinse everything"]],
     [44, 62, 64], "**Table 4.5** Troubleshooting chart.", ["l", "l", "l"]),
]

VIVA_A = [
    ("What is conductance?", "The reciprocal of resistance, G = 1/R, measured in siemens."),
    ("What is conductivity?", "Conductance corrected for cell geometry, \u03ba = G \u00d7 cell constant, in S "
                              "m^{\u22121}; it is an intrinsic property of the solution."),
    ("What carries current in an electrolyte?", "Mobile ions, not electrons through the bulk liquid."),
    ("What determines the conductance of a solution?", "The concentration, charge and mobility of the ions, the "
                                                       "temperature, and the cell geometry."),
    ("Why is HCl highly conducting?", "It is fully dissociated, and the hydrogen ion has exceptionally high "
                                      "mobility in water."),
    ("Why does conductance fall as NaOH is added?", "Because H^{+} is consumed and replaced by the much less "
                                                    "mobile Na^{+}; the number of charges is unchanged but their "
                                                    "mobility is not."),
    ("Why does conductance rise after equivalence?", "Because excess OH^{\u2212} accumulates, and hydroxide is also "
                                                     "highly mobile."),
    ("What is the shape of the curve?", "Two approximately linear branches with opposite slopes, meeting at a "
                                        "minimum: a shallow V."),
    ("How is the equivalence point found?", "From the intersection of the two extrapolated linear branches."),
    ("Is the conductance zero at equivalence?", "No. The solution contains NaCl, so Na^{+} and Cl^{\u2212} still "
                                                "carry current; the conductance is a minimum, not zero."),
    ("What is the cell constant?", "The ratio l/A of electrode separation to effective electrode area; it converts "
                                   "conductance to conductivity."),
    ("What is the unit of conductance and of conductivity?", "Siemens (S) and siemens per metre (S m^{\u22121}) "
                                                             "respectively."),
    ("Write the net ionic reaction.", "H^{+} + OH^{\u2212} \u2192 H_{2}O; Na^{+} and Cl^{\u2212} are spectators."),
    ("Why is the HCl aliquot diluted?", "So that the cell is fully immersed, and to reduce the initial conductance "
                                        "into a comfortable range; the moles of acid, and hence V_{eq}, are "
                                        "unchanged."),
    ("Does dilution change the equivalence volume?", "No \u2014 it changes the conductance values, not the volume at "
                                                     "which neutralisation is complete."),
    ("Why use distilled water?", "Tap water contains ions that add background conductance and flatten the curve."),
    ("Why must the cell be kept upright?", "To keep the immersed geometry, and hence the cell constant, constant."),
    ("Why must the temperature be constant?", "Ionic mobility, and therefore conductance, changes with temperature "
                                              "\u2014 typically about 2 % per \u00b0C."),
    ("Why is the titration continued past the minimum?", "To establish the rising branch, which is required to "
                                                         "locate the intersection."),
    ("What is ionic mobility?", "The drift velocity of an ion per unit electric field, in m^{2} V^{\u22121} "
                                "s^{\u22121}."),
    ("State Kohlrausch\u2019s law.", "At infinite dilution, the molar conductivity of an electrolyte equals the sum "
                                     "of the limiting molar conductivities of its ions."),
    ("How do you calculate the acid strength?", "C_{HCl} = C_{NaOH} V_{eq} / V_{HCl}, from the 1:1 "
                                                "stoichiometry."),
    ("Why is NaOH standardised?", "Because solid NaOH absorbs water and CO_{2}, so its concentration cannot be "
                                  "known from weighing alone."),
    ("Can a coloured solution be titrated conductometrically?", "Yes \u2014 no indicator is used, so colour is "
                                                                "irrelevant. This is one of the method\u2019s main "
                                                                "advantages."),
]

VIVA_B = [
    ("Why is H^{+} so mobile?", "Because it does not move as a bare hydrated ion; it hops between water molecules "
                                "by the Grotthuss proton-transfer mechanism, which requires far less "
                                "displacement of matter."),
    ("Why is OH^{\u2212} also highly mobile?", "By the same kind of mechanism, involving transfer of a proton "
                                               "\u201chole\u201d along the hydrogen-bond network."),
    ("Why is Na^{+} slower than H^{+}?", "It moves by ordinary bodily migration of a hydrated ion, carrying its "
                                         "solvation shell with it."),
    ("Why does the descending branch have a negative slope?", "Because each addition replaces a high-mobility ion "
                                                              "with a low-mobility one, reducing conductance."),
    ("Why does the ascending branch have a larger slope than the descending one?", "Because the ascending branch "
                                                                                   "adds both Na^{+} and OH^{\u2212} "
                                                                                   "(a high-mobility ion), whereas the "
                                                                                   "descending branch only swaps "
                                                                                   "mobilities."),
    ("Why is the intersection used rather than the minimum point?", "Because the minimum is a single noisy "
                                                                    "measurement, while the intersection of two "
                                                                    "fitted lines uses all the data and is "
                                                                    "insensitive to one bad reading."),
    ("Why does the meter read conductance rather than conductivity?", "Because the cell geometry is imposed by the "
                                                                      "instrument; the cell constant converts one to "
                                                                      "the other. The shape of the curve is the same "
                                                                      "either way."),
    ("Why must the electrodes be platinised?", "The platinised layer increases the effective surface area and "
                                               "reduces polarisation at the electrodes, giving more stable "
                                               "readings."),
    ("Why is an alternating current used in conductivity measurement?", "To avoid electrolysis and concentration "
                                                                        "polarisation at the electrodes, which would "
                                                                        "change the solution near them."),
    ("Why are the branches not perfectly straight?", "Because dilution changes every concentration as titrant is "
                                                     "added and because ionic activity coefficients vary; the "
                                                     "approximation is good over a limited range."),
    ("Why is the curve steeper when the titrant is more concentrated?", "Because each millilitre then introduces "
                                                                        "more ions, so conductance changes faster "
                                                                        "per unit volume."),
    ("Why does the initial conductance depend on how much water you added?", "Because dilution lowers all "
                                                                             "concentrations, and conductance is "
                                                                             "proportional to concentration."),
    ("Why can conductometric titration detect the endpoint of a precipitation reaction?", "Because the ionic "
                                                                                          "composition changes at "
                                                                                          "the endpoint, changing the "
                                                                                          "slope; the same "
                                                                                          "intersection logic "
                                                                                          "applies."),
    ("What would the curve look like for a weak acid titrated with a strong base?", "The initial conductance "
                                                                                    "rises slightly (the weak acid "
                                                                                    "is poorly ionised, and the salt "
                                                                                    "formed is fully ionised), then "
                                                                                    "rises more steeply after "
                                                                                    "equivalence."),
    ("What would the curve look like for a strong acid titrated with a weak base?", "The conductance falls to a "
                                                                                    "minimum and then rises only "
                                                                                    "gently, because the weak base "
                                                                                    "contributes few ions."),
]

VIVA_C = [
    ("What if the cell touched the beaker wall?", "The effective geometry changes, so the cell constant changes; the "
                                                  "readings would step or drift and the curve would acquire a "
                                                  "spurious kink."),
    ("What if you stopped the titration at the minimum?", "You would have no rising branch, so no intersection. The "
                                                          "best you could do is take the minimum point, which is "
                                                          "much less precise."),
    ("What if the temperature rose during the run?", "Conductance would rise throughout, flattening the descending "
                                                     "branch and steepening the apparent rise; V_{eq} would be "
                                                     "biased."),
    ("What if you used tap water for dilution?", "The high background conductance would compress the relative change, "
                                                 "making the intersection harder to locate."),
    ("What if the electrodes were dirty?", "The effective area and the polarisation behaviour change; readings drift "
                                           "and the slopes become unreliable."),
    ("What if a bubble stuck to an electrode?", "The effective electrode area drops, so conductance reads low until "
                                                "the bubble detaches \u2014 producing a sudden jump in the curve."),
    ("What if you used 0.01 N instead of 0.1 N NaOH?", "V_{eq} would be ten times larger and the curve stretched "
                                                      "horizontally; the calculated concentration would be correct "
                                                      "with the true value used."),
    ("What if the HCl had partially evaporated before the run?", "Its concentration would be higher than assumed, so "
                                                                 "V_{eq} would be larger and the calculated strength "
                                                                 "based on the nominal concentration wrong."),
    ("What if the meter were set to a range that saturates?", "Readings would clip at a maximum, destroying the "
                                                              "shape; choose a range that keeps the whole curve on "
                                                              "scale."),
    ("What if you recorded incremental rather than cumulative volume?", "The x-axis would be wrong and the two "
                                                                       "branches would not intersect at V_{eq}."),
]

VIVA_D = [
    ("Is the conductance at equivalence really a minimum?", "Yes for this system: it is the point at which the "
                                                            "high-mobility H^{+} has just been exhausted and before "
                                                            "high-mobility OH^{\u2212} begins to accumulate."),
    ("Does the minimum coincide exactly with equivalence?", "For an ideal strong/strong system, yes. In practice "
                                                            "dilution and activity effects can displace it slightly, "
                                                            "which is another reason to use the intersection."),
    ("Why is the cell constant not needed to find V_{eq}?", "Because V_{eq} depends on the //shape// of the curve, "
                                                            "and the cell constant scales all readings by the same "
                                                            "factor; it cancels."),
    ("Would a wrong cell constant affect your reported acid concentration?", "No, provided it was constant during "
                                                                             "the run \u2014 the intersection "
                                                                             "volume is unchanged. It would, however, "
                                                                             "make any absolute conductivity value "
                                                                             "wrong."),
    ("How does temperature enter quantitatively?", "Ionic mobility increases with temperature roughly as viscosity "
                                                   "falls, giving about 2 % per \u00b0C for typical aqueous "
                                                   "solutions."),
    ("Could you titrate a mixture of HCl and acetic acid conductometrically?", "Yes \u2014 the curve has two "
                                                                              "breaks: the strong acid is "
                                                                              "neutralised first, then the weak acid; "
                                                                              "the first break gives HCl directly."),
    ("What is the difference between conductance and conductivity in one sentence?", "Conductance is what the cell "
                                                                                    "measures and depends on its "
                                                                                    "geometry; conductivity is the "
                                                                                    "geometry-corrected property of "
                                                                                    "the solution."),
    ("Why is the ascending branch steeper than the descending branch?", "Because OH^{\u2212} adds new mobile charge "
                                                                        "carriers, whereas the descending branch only "
                                                                        "exchanges carriers of different mobility."),
    ("What is polarisation, and why does it matter?", "Accumulation of ions or reaction products at the electrodes "
                                                      "changes the local composition and produces an apparent "
                                                      "resistance; alternating current and platinised electrodes "
                                                      "minimise it."),
    ("How would you verify V_{eq} independently?", "By repeating the titration with an indicator or pH-metrically "
                                                   "and comparing the two equivalence volumes."),
]

CH4_CHECK = checklist(
    "4.8",
    ["Conductance G = 1/R, in siemens; conductivity \u03ba = G \u00d7 cell constant, in S m^{\u22121}.",
     "Current in solution is carried by mobile ions.",
     "Conductance depends on ion number, charge, mobility, temperature and cell geometry.",
     "H^{+} has exceptionally high mobility (proton hopping).",
     "OH^{\u2212} is also highly mobile, but less so than H^{+}.",
     "Na^{+} and Cl^{\u2212} are ordinary, slower ions.",
     "Adding NaOH before equivalence replaces H^{+} with Na^{+}: conductance falls.",
     "At equivalence the solution is NaCl: conductance is a minimum, not zero.",
     "After equivalence, excess OH^{\u2212} raises conductance steeply.",
     "The curve is a shallow V of two roughly linear branches.",
     "V_{eq} is the intersection of the extrapolated branches.",
     "The cell must stay upright at constant depth: geometry is part of the measurement.",
     "Temperature must be constant; conductance changes about 2 % per \u00b0C.",
     "Distilled water only \u2014 tap water adds background conductance.",
     "Diluting the aliquot does not change V_{eq}.",
     "Continue 3\u20135 mL past the minimum to define the rising branch.",
     "The cell constant cancels out of the V_{eq} determination.",
     "C_{HCl} = C_{NaOH}V_{eq}/V_{HCl}.",
     "NaOH must be standardised and kept stoppered.",
     "The source gives two different increment schedules; confirm which applies."],
    ["Why does conductance fall and then rise?",
     "Why is H^{+} so mobile, and why does that matter?",
     "Why is the conductance not zero at equivalence?",
     "How is the equivalence point located, and why not from the minimum?",
     "What is the difference between conductance and conductivity?",
     "What is the cell constant, and does it affect V_{eq}?",
     "Why must the cell not be moved during the run?",
     "Why must the temperature be constant?",
     "Why continue past the endpoint?",
     "How is the acid concentration calculated?"],
    ["Derive the qualitative shape of the curve from the mobilities of the four ions involved.",
     "Explain why the ascending branch is steeper than the descending branch, quantitatively if you can.",
     "Show that the cell constant cancels from the determination of V_{eq}, but not from a reported conductivity.",
     "Explain why the conductance at equivalence is finite, and estimate its order of magnitude.",
     "Your curve has a kink rather than a clean V. List the causes in order of likelihood.",
     "What would the curve look like for a weak acid, and why does it differ?",
     "How does dilution affect the slopes, and why does it not affect V_{eq}?",
     "Why does an alternating current give a truer reading than a direct current?",
     "How could you determine the cell constant experimentally?",
     "Compare conductometric and pH-metric location of the equivalence point for this system."],
    [("Conductance vs conductivity", "Measured vs geometry-corrected."),
     ("Minimum vs zero conductance", "NaCl still conducts at equivalence."),
     ("Cell constant vs concentration", "Geometry, not chemistry."),
     ("Cumulative vs incremental volume", "The x-axis must be cumulative."),
     ("H^{+} mobility vs Na^{+} mobility", "About seven to one, and it drives the curve."),
     ("Intersection vs minimum", "Structural feature vs single noisy point."),
     ("Dilution effect on V_{eq} vs on slopes", "None vs lowers both slopes."),
     ("Polarisation vs contamination", "Electrode effect vs solution effect.")],
    (["Relation", "Expression", "Note"],
     [["Conductance", "G = 1/R", "Siemens"],
      ["Conductivity", "\u03ba = G \u00d7 \u03b8 (cell constant)", "S m^{\u22121}"],
      ["Cell constant", "\u03b8 = l/A", "Depends on geometry"],
      ["Kohlrausch", "\u039b\u00b0_{m} = \u03bd_{+}\u03bb\u00b0_{+} + \u03bd_{-}\u03bb\u00b0_{-}", "At infinite "
       "dilution"],
      ["Stoichiometry", "C_{HCl}V_{HCl} = C_{NaOH}V_{eq}", "1:1 reaction"],
      ["Temperature coefficient", "about 2 % per \u00b0C", "For dilute aqueous solutions"],
      ["Slope before", "\u221d (\u03bb(H^{+}) \u2212 \u03bb(Na^{+}))", "Negative"],
      ["Slope after", "\u221d (\u03bb(Na^{+}) + \u03bb(OH^{\u2212}))", "Positive and steeper"]],
     [32, 78, 58]),
    [["Conductance rises from the first addition", "Wrong solution, cell not immersed, or wrong range"],
     ["No minimum, monotonic fall", "Titration stopped before equivalence"],
     ["Noisy, spiky curve", "Bubbles on electrodes, poor stirring, dirty cell"],
     ["Sudden step in the curve", "Cell moved, or bubble detached"],
     ["Minimum displaced between runs", "Temperature difference or different cell depth"],
     ["Very high initial conductance", "Tap water or contaminated glassware"],
     ["Intersection far from the visible minimum", "Branches poorly fitted, or too few points on one branch"]],
    ["Conductance is geometry-dependent; conductivity is not.",
     "The curve is a shape, not a single point \u2014 both branches matter.",
     "The cell constant cancels from V_{eq}.",
     "H^{+} and OH^{\u2212} are the two mobile ions that create the V shape.",
     "Colour and turbidity are irrelevant to this method.",
     "Temperature control is a measurement requirement, not a nicety.",
     "The minimum is noisy; the intersection is robust."],
    ["Lifting the cell out between readings.",
     "Stopping the titration at the minimum.",
     "Recording incremental volume on the x-axis.",
     "Using tap water for dilution.",
     "Reporting \u201cconductance at equivalence = 0\u201d.",
     "Failing to record and control the temperature.",
     "Reading a single \u201cbest\u201d point instead of fitting both branches."],
    ["I titrate a measured aliquot of HCl with standard NaOH and follow the conductance of the solution instead of "
     "its colour. Before equivalence, each hydroxide added removes a highly mobile hydrogen ion and replaces it "
     "with a much slower sodium ion, so the conductance falls in a nearly straight line. At equivalence the "
     "solution contains only sodium chloride, so the conductance is at a minimum \u2014 not zero, because NaCl "
     "still conducts. Beyond equivalence, excess sodium hydroxide accumulates, and since hydroxide is also highly "
     "mobile, the conductance rises steeply. The curve is therefore a shallow V; I fit straight lines to the two "
     "branches and take their intersection as the equivalence volume, rather than trusting the noisy minimum. "
     "Because both ions are monovalent the stoichiometry is 1:1, so C_{HCl} = C_{NaOH}V_{eq}/V_{HCl}. The critical "
     "controls are a clean cell held at constant depth, constant temperature, distilled water, and enough readings "
     "past the minimum to define the rising branch."],
    ["**Fewer mobile ions \u2192 conductance falls. Excess OH^{\u2212} \u2192 conductance rises.**",
     "**Minimum \u2260 zero: NaCl conducts.**",
     "**Intersection of two lines, not the lowest point.**",
     "**Same cell, same depth, same temperature \u2014 or the curve lies.**"]
)

CH4 = {
    "key": "conduct",
    "num": "4",
    "kicker": "Experiment 4  \u00b7  Electroanalytical titration",
    "title": "Conductometric Titration of HCl with NaOH",
    "toc": "Conductometric titration (HCl with NaOH)",
    "standfirst": "No indicator, no colour, no ambiguity about shade. The endpoint appears as a change of slope, "
                  "and it works even in solutions you cannot see through.",
    "body": B + [
        ("h2", "4.7  Viva question bank"),
        ("p", "Seventy-nine answered questions covering the mobility argument, the instrumentation, and the "
              "quantitative consequences of getting the geometry or the temperature wrong."),
        ("qsub", "A.  Fundamental questions"),
        ("qa", VIVA_A),
        ("qsub", "B.  \u201cWhy\u201d and \u201chow\u201d questions"),
        ("qa", VIVA_B),
        ("qsub", "C.  \u201cWhat if\u201d questions"),
        ("qa", VIVA_C),
        ("qsub", "D.  Tricky and advanced questions"),
        ("qa", VIVA_D),
        ("qsub", "E.  Instrumentation and interpretation"),
        ("qa", VIVA_E),
    ] + CH4_CHECK,
}
