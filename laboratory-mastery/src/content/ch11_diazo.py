VIVA_E = [
    ("Why is the diazonium salt not isolated?",
     "It is unstable and potentially explosive when dry, so it is used in solution without isolation."),
    ("What is the function of the ice bath beyond temperature control?",
     "It absorbs the heat of mixing of the acid and of the exothermic diazotisation."),
    ("Why is the nitrite solution added below the surface of the liquid?",
     "To avoid local high concentrations and loss of nitrous acid as gas at the surface."),
    ("What is the role of the chloride ion in the diazonium chloride?",
     "It is the counter-ion; it keeps the salt soluble and can later be displaced by other nucleophiles."),
    ("Why is the coupling mixture stirred for a period after the addition?",
     "To allow the sparingly soluble product to form completely and to age into a filterable solid."),
    ("Why is the product washed with cold rather than warm water?",
     "Warm water would dissolve product and reduce the yield."),
    ("Why does the crude product sometimes look orange rather than yellow?",
     "Particle size and traces of azo by-products affect the observed colour of the solid."),
    ("Why is aqueous ethanol used for recrystallisation?",
     "It dissolves the product when hot and gives a good recovery on cooling, while rejecting inorganic salts."),
    ("What is the purpose of scratching the flask?",
     "It provides nucleation sites so that crystallisation starts cleanly rather than as an oil."),
    ("Why does an oily product form if crystallisation is too fast?",
     "Rapid precipitation traps solvent and impurities, producing a non-crystalline mass."),
    ("How would you confirm that coupling occurred through nitrogen?",
     "By the presence of the N\u2013H stretch in the infrared spectrum and by hydrolysis to diazonium salt and "
     "aniline."),
    ("What is the consequence of adding too little acid in the first stage?",
     "Incomplete diazotisation and premature coupling, giving a low and impure yield."),
    ("What is the consequence of adding too much acid in the second stage?",
     "The amine remains protonated and coupling is suppressed entirely."),
    ("Why is an aromatic, rather than aliphatic, amine required?",
     "Only aromatic amines form stable diazonium ions; aliphatic diazonium species decompose immediately."),
    ("Why is the reaction described as an electrophilic substitution overall?",
     "Because the diazonium ion acts as an electrophile attacking the nucleophilic amine nitrogen."),
    ("What is the relation between this preparation and the preparation of an azo dye?",
     "Both use the same diazonium intermediate; the dye results from coupling to an activated aromatic carbon "
     "rather than to an amine nitrogen."),
    ("Why is diazoaminobenzene sometimes used as a radical initiator?",
     "The weak N\u2013N bond allows it to decompose and generate radicals."),
    ("Why should gloves be changed immediately after contact with aniline?",
     "Aniline penetrates nitrile gloves over time and is absorbed through the skin."),
    ("Why are nitrogen-rich compounds treated cautiously near flames?",
     "They can decompose exothermically and violently, sometimes explosively, when heated."),
    ("What would you do if the reaction mixture began to evolve gas rapidly?",
     "Cool it immediately in ice and stop the addition \u2014 that is a decomposition, not a normal step."),
]

"""Chapter 11 - Preparation and characterisation of diazoaminobenzene."""
from common import checklist

B = []

B += [
    ("h2", "11.1  A reaction that draws its own coloured product"),
    ("lead", "Diazonium chemistry is one of the most consequential reactions in synthetic organic chemistry: the "
             "diazonium group is a leaving group, an electrophile, and a coupling partner, which makes it the "
             "gateway to azo dyes, aryl halides and phenols. The experiment here stops at the simplest visible "
             "proof of it \u2014 a bright yellow\u2013orange crystalline solid with a sharp melting point."),
    ("p", "The supplied material sets the aim as **preparation of diazoaminobenzene from aniline and its "
          "characterisation by melting point**, and indicates the expected melting range as **96\u201398 \u00b0C**. "
          "The course of the preparation follows the classical route: aniline is diazotised in acid with sodium "
          "nitrite, and the diazonium ion is then allowed to couple with a second molecule of aniline."),
    ("eq", "C_{6}H_{5}NH_{2} + NaNO_{2} + 2HCl \u2192 C_{6}H_{5}N_{2}^{+}Cl^{\u2212} + NaCl + 2H_{2}O",
     "Equation 11.1 \u2014 diazotisation of aniline. The nitrous acid generated in situ from nitrite and acid "
     "converts the primary aromatic amine into a diazonium salt."),
    ("eq", "C_{6}H_{5}N_{2}^{+}Cl^{\u2212} + C_{6}H_{5}NH_{2} \u2192 C_{6}H_{5}\u2013N=N\u2013NH\u2013C_{6}H_{5} + "
           "HCl",
     "Equation 11.2 \u2014 coupling with a second aniline molecule to give diazoaminobenzene (1,3-diphenyltriazene)."),
    ("defbox", [
        ("Diazotisation", "Conversion of a primary aromatic amine into a diazonium salt by treatment with nitrous "
                          "acid at low temperature."),
        ("Diazonium ion", "Ar\u2013N_{2}^{+}, a stabilised but reactive electrophile; unstable above about 5 "
                          "\u00b0C for most arylamines."),
        ("Coupling", "Electrophilic attack of the diazonium ion on an electron-rich aromatic ring or an amine, "
                     "forming an azo compound."),
        ("Diazoaminobenzene", "C_{6}H_{5}\u2013N=N\u2013NH\u2013C_{6}H_{5}, also called 1,3-diphenyltriazene; a "
                              "yellow\u2013orange solid, m.p. 96\u201398 \u00b0C."),
        ("Melting point range", "The temperature interval between the first appearance of liquid and complete "
                                "melting; a sharp range indicates a pure crystalline solid."),
        ("Mixed melting point", "Melting point of a mixture of the unknown with an authentic sample; no depression "
                                "confirms identity."),
    ]),
    ("box", "key", [
        "**Keep it cold.** The diazonium ion decomposes above roughly 5 \u00b0C, releasing nitrogen and giving "
        "phenol on work-up. Temperature control is the single most important variable in the preparation.",
        "**Acid must be in excess** during diazotisation: nitrous acid is generated from nitrite and acid, and any "
        "shortfall leaves unreacted amine that would couple prematurely.",
        "**The product is visibly coloured** because the \u2013N=N\u2013 group is a chromophore; a yellow\u2013orange "
        "precipitate is the expected sign that coupling has occurred.",
        "**Melting point is the identification**, not the yield. A sharp range at 96\u201398 \u00b0C is the "
        "evidence; a wide or depressed range means impurities or the wrong product.",
    ], "Four ideas that define the experiment"),
    ("fig", "diazo", "**Figure 11.1** The sequence: aniline in acid is cooled in an ice bath, nitrite is added to "
                     "form the diazonium salt, and a second portion of aniline is added so that coupling gives the "
                     "yellow diazoaminobenzene, which is filtered, washed, dried and then melted on a melting-point "
                     "apparatus."),
]

B += [
    ("h2", "11.2  Theory"),
    ("h3", "11.2.1  Nitrous acid and the nitrosating species"),
    ("p", "Sodium nitrite in mineral acid generates nitrous acid, which is itself unstable and exists in "
          "equilibrium with several species. The effective electrophile is the nitrosonium ion, formed in strongly "
          "acidic solution:"),
    ("eq", "NaNO_{2} + HCl \u2192 HNO_{2} + NaCl"),
    ("eq", "HNO_{2} + H^{+} \u21cc H_{2}O + NO^{+}   (nitrosonium ion)"),
    ("eq", "Ar\u2013NH_{2} + NO^{+} \u2192 Ar\u2013NH_{2}^{+}\u2013NO \u2192 Ar\u2013N_{2}^{+} + H_{2}O",
     "Equation 11.3 \u2014 the accepted mechanism: nitrosation of the amine nitrogen, then dehydration to the "
     "diazonium ion. The dehydration step is the slow one and is favoured by strong acid."),
    ("p", "This sequence explains two procedural facts. First, the acid must be present in excess, because the "
          "dehydration step consumes acid. Second, the reaction must be kept cold, because the diazonium ion is "
          "thermally unstable \u2014 it decomposes to a phenol and nitrogen, and the nitrogen evolution can be "
          "violent if the scale is large."),
    ("h3", "11.2.2  Why aniline couples with itself"),
    ("p", "The diazonium ion is a weak electrophile and requires an activated aromatic ring. Aniline is strongly "
          "activated, and in weakly acidic or neutral conditions the free amine attacks the diazonium nitrogen "
          "directly, giving a triazene rather than a C-coupled azo compound:"),
    ("eq", "Ar\u2013N_{2}^{+} + Ar\u2013NH_{2} \u21cc Ar\u2013N=N\u2013NH\u2013Ar + H^{+}"),
    ("p", "Diazoaminobenzene is therefore the //self-coupling// product. In strongly acidic solution the aniline is "
          "protonated and deactivated, so coupling is suppressed \u2014 which is why the acidity is adjusted "
          "between the two stages. This is a fine illustration of pH control as a synthetic tool rather than a "
          "nuisance."),
    ("h3", "11.2.3  Melting point as evidence of identity"),
    ("p", "A pure crystalline solid melts over a narrow range, typically 1\u20132 \u00b0C. Impurities depress the "
          "melting point and broaden the range, because they disrupt the crystal lattice. Two conclusions follow:"),
    ("bul", [
        "**A range of 96\u201398 \u00b0C is consistent with diazoaminobenzene** and indicates a reasonably pure "
        "product.",
        "**A wide or low range indicates impurity**, most commonly unreacted aniline, phenol from diazonium "
        "decomposition, or water and inorganic salt.",
    ]),
    ("p", "Melting point alone is suggestive, not conclusive. The decisive test is a mixed melting point with an "
          "authentic sample: if the mixture melts at the same temperature, the two are the same compound. Where a "
          "spectroscopic method is available, an infrared or nuclear magnetic resonance spectrum would be stronger "
          "still."),
    ("box", "exam", [
        "**Trap:** \u201cWhy is the diazotisation step done in acid, if the coupling needs free amine?\u201d Because "
        "the two stages need different conditions: acid is required to generate and stabilise the diazonium ion, "
        "while coupling requires the unprotonated amine. The sequence is therefore staged, not simultaneous.",
        "**Trap:** \u201cIs diazoaminobenzene an azo dye?\u201d It is an azo compound and is coloured, but it is not "
        "used as a dye; it is a synthetic intermediate and a classical demonstration.",
        "**Trap:** \u201cWhy keep the temperature below 5 \u00b0C?\u201d Because the diazonium ion decomposes "
        "thermally to phenol and nitrogen; cold conditions preserve it long enough to couple.",
    ], "Three questions that test understanding"),
]

B += [
    ("h2", "11.3  Apparatus and reagents"),
    ("tbl", ["Item", "Function", "If it is faulty or missing"],
     [["Beaker / conical flask, 250 mL", "Reaction vessel", "Too small a vessel risks overflow on gas evolution"],
      ["Ice bath", "Maintains the diazotisation below 5 \u00b0C", "Without it, the diazonium ion decomposes"],
      ["Thermometer (0\u2013100 \u00b0C)", "Monitors the reaction temperature", "An unmonitored exotherm can ruin the "
       "preparation"],
      ["Dropping funnel / pipette", "Controlled addition of nitrite", "Rapid addition causes local overheating"],
      ["Glass rod", "Stirring and scratching", "Vigorous stirring is needed for a clean precipitate"],
      ["B\u00fcchner funnel, filter flask, pump", "Filtration of the product", "Poor filtration leaves mother liquor in "
       "the crystals"],
      ["Melting-point apparatus (or Thiele tube)", "Melting range determination", "Uncalibrated apparatus gives a "
       "shifted value"],
      ["Capillary tubes", "Hold the sample for melting", "Wet or thick-walled capillaries give a poor reading"],
      ["Aniline (freshly distilled)", "Starting material", "Oxidised, brown aniline gives a dark, impure product"],
      ["Sodium nitrite", "Source of nitrous acid", "Old reagent may be partly carbonate"],
      ["Concentrated HCl", "Generates nitrous acid and controls pH", "Wrong strength changes the stoichiometry"],
      ["Sodium acetate / base for pH adjustment", "Releases free amine for coupling", "Wrong pH suppresses coupling"],
      ["Ice and distilled water", "Cooling and washing", "Tap water introduces ions and impurities"],
      ["Ethanol or aqueous ethanol", "Recrystallisation solvent", "Poor solvent choice gives low recovery"]],
     [50, 56, 64], "**Table 11.1** Apparatus and reagents. Note that the supplied material does not state the "
                   "exact quantities; the table lists the materials, not a recipe to be invented.",
     ["l", "l", "l"]),
    ("box", "source", [
        "**The supplied source gives the aim, the expected melting range (96\u201398 \u00b0C) and the reaction "
        "scheme, but not the reagent quantities or the exact volumes.** Those are method details that vary between "
        "laboratory manuals, and they are not invented here. Use the quantities printed in your own practical "
        "schedule or given by your instructor; the chemistry in this chapter is independent of them.",
    ], "What the source does and does not contain"),
    ("box", "warn", [
        "**Aniline is toxic, and it is absorbed through the skin.** It is a suspected carcinogen and a "
        "methaemoglobin former; handle it in a fume hood, wear nitrile gloves, and change gloves immediately if "
        "contaminated. **Sodium nitrite and nitrous acid generate toxic nitrogen oxides** \u2014 keep the preparation "
        "in a hood. **Diazonium salts are potentially explosive when dry and concentrated**; never isolate them as "
        "solids or heat a diazonium solution. Melting-point capillaries containing a nitrogen-rich compound should "
        "be discarded, not reused. Collect all aromatic waste for approved disposal.",
    ], "Hazards \u2014 this is not a benign preparation"),
]

B += [
    ("h2", "11.4  Procedure with reasoning"),
    ("h3", "Part A \u2014 Diazotisation"),
    ("num", [
        "**Cool the acid in an ice bath** in the reaction flask until it is below 5 \u00b0C.",
        "**Add the aniline slowly with stirring**, keeping the temperature low. The amine dissolves as its "
        "hydrochloride salt.",
        "**Add the sodium nitrite solution dropwise**, maintaining the temperature below 5 \u00b0C throughout. Slow "
        "addition prevents local overheating and the premature decomposition of the diazonium ion.",
        "**Stir for a further period in the cold** to complete diazotisation. A positive starch\u2013iodide test "
        "for excess nitrous acid indicates that diazotisation is complete.",
        "**Destroy any excess nitrous acid** with a little sulphamic acid or urea if your manual requires it, so "
        "that it does not interfere with the coupling stage.",
    ]),
    ("h3", "Part B \u2014 Coupling and isolation"),
    ("num", [
        "**Add the second portion of aniline**, or adjust the pH so that free amine is available for coupling.",
        "**Stir and allow the yellow\u2013orange precipitate to form.** Cooling improves the yield and the crystal "
        "quality.",
        "**Filter at the pump**, washing the solid with cold water to remove inorganic salts and residual acid.",
        "**Dry the product** in air or in a desiccator. Do not overheat it: diazoaminobenzene can decompose "
        "exothermically if heated strongly.",
        "**Recrystallise from aqueous ethanol** if the melting range is broad, then dry and re-determine the "
        "melting point.",
        "**Determine the melting range** by heating slowly near the expected value, recording both the first drop "
        "of liquid and the temperature at which melting is complete.",
        "**Perform a mixed melting point** with an authentic sample if one is available.",
        "**Weigh the dry product** and record the yield together with the appearance and the melting range.",
    ]),
    ("box", "note", [
        "**Why is the melting point determination done slowly?** Because the sample and the thermometer must be in "
        "thermal equilibrium. A fast ramp makes the recorded temperature lag behind the true melting temperature, "
        "and the error is largest exactly where it matters, at the melting transition.",
        "**Why does the first drop matter more than complete melting?** The literature value refers to the "
        "//beginning// of melting for a pure compound; complete melting is more sensitive to sample size and "
        "heating rate.",
    ], "Two details that decide the reported number"),
]

B += [
    ("h2", "11.5  Observations and calculation"),
    ("tbl", ["S. No.", "Observation", "Record"],
     [["1", "Appearance of diazonium solution", ""],
      ["2", "Appearance of precipitate", "yellow\u2013orange solid"],
      ["3", "Temperature during diazotisation", "below 5 \u00b0C"],
      ["4", "Crude yield (g)", ""],
      ["5", "Melting range of crude product (\u00b0C)", ""],
      ["6", "Melting range after recrystallisation (\u00b0C)", "96\u201398 \u00b0C expected"],
      ["7", "Mixed melting point (\u00b0C)", ""],
      ["8", "Appearance of final product", ""]],
     [16, 84, 68], "**Table 11.2** Observation table. Blank because the supplied sheet contains no completed "
                   "readings.", ["c", "l", "l"]),
    ("h3", "11.5.1  Yield calculation"),
    ("p", "Diazoaminobenzene has the formula C_{12}H_{11}N_{3}, molar mass 197.24 g mol^{\u22121}. One mole of "
          "product requires two moles of aniline and one mole of nitrite, so the theoretical yield is set by "
          "whichever reagent is limiting:"),
    ("eq", "Theoretical yield (g) = (moles of limiting aniline)/2 \u00d7 197.24",
     "Equation 11.4 \u2014 note the division by two: two aniline molecules are incorporated into each product "
     "molecule."),
    ("eq", "Percentage yield = (actual yield/theoretical yield) \u00d7 100"),
    ("p", "Worked illustration: if 0.10 mol of aniline were used and the nitrite were in excess, the theoretical "
          "yield is 0.050 \u00d7 197.24 = 9.86 g. An isolated 6.4 g corresponds to 65 % yield. That is a "
          "respectable figure for a preparation with filtration and recrystallisation losses."),
    ("tbl", ["Quantity", "Expression", "Illustrative value"],
     [["Moles of aniline", "mass/molar mass", "0.10 mol"],
      ["Moles of product (theoretical)", "half the aniline", "0.050 mol"],
      ["Molar mass of product", "C_{12}H_{11}N_{3}", "197.24 g mol^{\u22121}"],
      ["Theoretical yield", "0.050 \u00d7 197.24", "9.86 g"],
      ["Actual yield", "weighed", "6.4 g"],
      ["Percentage yield", "actual/theoretical \u00d7 100", "65 %"],
      ["Melting range check", "compare with 96\u201398 \u00b0C", "identification"]],
     [46, 62, 60], "**Table 11.3** Yield and identification chain. The illustrative masses are arithmetic examples, "
                   "not measurements claimed from the source.", ["l", "l", "c"]),
]

B += [
    ("h2", "11.6  Precautions, errors and troubleshooting"),
    ("bul", [
        "Keep the diazotisation mixture below 5 \u00b0C throughout the addition.",
        "Add nitrite dropwise, with efficient stirring.",
        "Maintain excess acid during diazotisation and adjust pH before coupling.",
        "Use freshly distilled, colourless aniline; brown aniline is already oxidised.",
        "Never isolate or strongly heat dry diazonium salts.",
        "Dry the product gently; strong heating can decompose it.",
        "Heat the melting-point apparatus slowly near the expected transition.",
        "Calibrate or cross-check the melting-point apparatus with a known compound.",
        "Wear gloves and work in a fume hood; aniline penetrates skin.",
        "Dispose of aromatic and diazonium waste through the approved route.",
    ]),
    ("tbl", ["Source of error", "Type", "Effect", "Control"],
     [["Temperature above 5 \u00b0C during diazotisation", "Systematic", "Decomposition to phenol; dark, oily "
       "product; low yield", "Ice bath; slow addition"],
      ["Insufficient acid", "Systematic", "Incomplete diazotisation; premature coupling", "Excess acid; check "
       "before coupling"],
      ["Excess nitrous acid carried into coupling", "Systematic", "Side reactions; impure product", "Destroy "
       "excess with sulphamic acid or urea"],
      ["Old, oxidised aniline", "Systematic", "Dark product, depressed melting point", "Freshly distilled aniline"],
      ["Rapid heating in the melting-point determination", "Systematic (positive)", "Melting range reads high and "
       "wide", "Slow ramp near the transition"],
      ["Wet product", "Systematic (negative)", "Depressed, broadened melting range", "Dry thoroughly but gently"],
      ["Incomplete washing", "Systematic (negative)", "Salt contamination depresses the melting point", "Wash with "
       "cold water"],
      ["Uncalibrated thermometer", "Systematic", "Shifted melting range", "Calibrate against a standard"]],
     [50, 26, 48, 48], "**Table 11.4** Error budget.", ["l", "l", "l", "l"]),
    ("tbl", ["Symptom", "Likely cause", "Action"],
     [["No precipitate forms", "pH too low (amine protonated) or diazotisation incomplete", "Adjust pH; check the "
       "nitrite test"],
      ["Product is dark brown or tarry", "Decomposition, oxidation, or overheating", "Repeat with better cooling "
       "and fresh aniline"],
      ["Melting range broad and low", "Impurity, water, or residual solvent", "Recrystallise and dry again"],
      ["Melting range high", "Heating too fast, or thermometer error", "Repeat slowly with a calibrated "
       "thermometer"],
      ["Vigorous gas evolution during the preparation", "Diazonium decomposition \u2014 a hazard", "Cool "
       "immediately; do not continue the addition"],
      ["Very low yield", "Losses in filtration or recrystallisation", "Check the washings; reduce solvent "
       "volume"]],
     [44, 58, 66], "**Table 11.5** Troubleshooting chart.", ["l", "l", "l"]),
]

VIVA_A = [
    ("What is diazoaminobenzene?", "1,3-Diphenyltriazene, C_{6}H_{5}\u2013N=N\u2013NH\u2013C_{6}H_{5}, a "
                                   "yellow\u2013orange solid with a melting point of 96\u201398 \u00b0C."),
    ("What is diazotisation?", "Conversion of a primary aromatic amine into a diazonium salt with nitrous acid at "
                              "low temperature."),
    ("Write the diazotisation of aniline.", "C_{6}H_{5}NH_{2} + NaNO_{2} + 2HCl \u2192 C_{6}H_{5}N_{2}^{+}Cl^{"
                                            "\u2212} + NaCl + 2H_{2}O."),
    ("Write the coupling step.", "C_{6}H_{5}N_{2}^{+} + C_{6}H_{5}NH_{2} \u2192 C_{6}H_{5}\u2013N=N\u2013NH\u2013"
                                 "C_{6}H_{5} + H^{+}."),
    ("Why is the reaction kept below 5 \u00b0C?", "The diazonium ion is thermally unstable and decomposes to "
                                                  "phenol and nitrogen above that temperature."),
    ("Why is excess acid needed?", "To generate nitrous acid and to drive the dehydration step that forms the "
                                   "diazonium ion."),
    ("Why is sodium nitrite used?", "It generates nitrous acid in situ with the mineral acid."),
    ("What is the role of the second aniline molecule?", "It acts as the nucleophile that couples with the "
                                                         "diazonium ion to form the product."),
    ("Why is the product coloured?", "The \u2013N=N\u2013 azo chromophore absorbs visible light."),
    ("What is the expected melting point?", "96\u201398 \u00b0C."),
    ("Why is the melting point measured?", "To establish the identity and purity of the product."),
    ("What does a sharp melting range indicate?", "A pure crystalline compound."),
    ("What does a depressed, broad range indicate?", "Impurity, or the wrong compound."),
    ("What is a mixed melting point?", "The melting point of a mixture of the product with an authentic sample; no "
                                       "depression confirms identity."),
    ("What is the molar mass of diazoaminobenzene?", "197.24 g mol^{\u22121}."),
    ("How many aniline molecules are incorporated?", "Two \u2014 one provides the diazonium nitrogen and one the "
                                                     "amine nitrogen."),
    ("What is a diazonium salt?", "Ar\u2013N_{2}^{+}X^{\u2212}, a species with a strongly electrophilic terminal "
                                  "nitrogen."),
    ("What is coupling?", "Electrophilic attack of a diazonium ion on an activated aromatic ring or amine to form "
                          "an azo compound."),
    ("Why is aniline activated towards coupling?", "The amino group donates electron density into the ring, making "
                                                   "it nucleophilic."),
    ("What is the hazard of dry diazonium salts?", "They can decompose explosively; they are never isolated dry."),
    ("How is aniline absorbed?", "Readily through the skin as well as by inhalation, which is why gloves and a hood "
                                 "are required."),
    ("Why is the product washed with cold water?", "To remove acid, salts and mother liquor without dissolving the "
                                                   "product."),
    ("What is the limiting reagent in this preparation?", "Whichever is present in the smaller stoichiometric "
                                                          "amount, usually the nitrite or the acid if either is "
                                                          "short."),
    ("Why is freshly distilled aniline preferred?", "Aniline oxidises on storage, and the oxidation products "
                                                    "contaminate the product."),
]

VIVA_B = [
    ("Why is the reaction mixture stirred vigorously?", "To disperse the nitrite and prevent local hot spots and "
                                                        "local excess, both of which favour decomposition."),
    ("Why is the nitrite added dropwise?", "A rapid addition generates a local excess and heat, risking diazonium "
                                           "decomposition."),
    ("Why must the acid be in excess during diazotisation but not so acidic as to block coupling?", "Diazotisation "
                                                                                                  "requires acid; "
                                                                                                  "coupling "
                                                                                                  "requires free "
                                                                                                  "amine, so the "
                                                                                                  "conditions are "
                                                                                                  "staged."),
    ("Why is a starch\u2013iodide test used?", "To detect excess nitrous acid, which indicates that diazotisation "
                                               "is complete."),
    ("Why is excess nitrous acid destroyed before coupling?", "Because nitrous acid could nitrosate the amine and "
                                                              "produce side products."),
    ("Why is the product filtered rather than extracted?", "It is a solid that can be isolated directly, avoiding "
                                                           "solvent use and the risk of losing material in an "
                                                           "emulsion."),
    ("Why is recrystallisation used?", "To remove impurities that depress and broaden the melting range."),
    ("Why is the melting-point determination done slowly near the transition?", "To allow thermal equilibrium "
                                                                               "between the sample and the "
                                                                               "thermometer; otherwise the reading "
                                                                               "lags."),
    ("Why is the first drop of liquid recorded?", "The literature value refers to the beginning of melting, and it "
                                                  "is less sensitive to sample size than complete melting."),
    ("Why might the observed melting point be higher than expected?", "The thermometer may read high, or the sample "
                                                                      "may be being heated too fast."),
    ("Why does residual water depress the melting point?", "Water disrupts the crystal lattice, which lowers the "
                                                           "temperature at which the lattice collapses."),
    ("Why is the yield usually below theoretical?", "Losses in filtration, washing, recrystallisation, and side "
                                                    "reactions, particularly diazonium decomposition."),
    ("Why does a tarry product form at higher temperature?", "Decomposition, oxidation and polymerisation products "
                                                             "form; they are dark and have no sharp melting point."),
    ("Why is a nitrogen-rich compound handled with care near a flame?", "Diazonium and diazo compounds can "
                                                                        "decompose exothermically and violently when "
                                                                        "heated dry."),
]

VIVA_C = [
    ("What if the temperature rose to 15 \u00b0C during diazotisation?", "The diazonium ion would partly decompose "
                                                                        "to phenol with nitrogen evolution, lowering "
                                                                        "the yield and contaminating the product."),
    ("What if you forgot the ice bath?", "Expect rapid decomposition, gas evolution, a dark product and a poor "
                                         "melting range; on a large scale this could be violent."),
    ("What if no nitrite test were done?", "You would not know whether diazotisation was complete or whether excess "
                                           "nitrous acid remained, so the coupling stage would be uncontrolled."),
    ("What if the product melted over 88\u2013110 \u00b0C?", "The product is impure or the melting was too fast; "
                                                            "recrystallise and repeat with a slow ramp."),
    ("What if you obtained a red, not yellow, solid?", "A different coupling product, or an impurity; identity must "
                                                       "be confirmed by mixed melting point or spectroscopy."),
    ("What if the yield were quantitative?", "Suspicious \u2014 weigh again after thorough drying; mother liquor and "
                                             "salt are easily retained."),
    ("What if the mixed melting point were depressed?", "The product is not the same compound as the reference, "
                                                        "despite a similar melting point."),
    ("What if you used the wrong amine?", "The product would differ and would not melt at 96\u201398 \u00b0C; the "
                                          "aromatic substitution pattern strongly influences both reactivity and "
                                          "melting point."),
    ("What if the diazonium solution were left to stand overnight?", "It would slowly decompose even in the cold; "
                                                                     "the preparation should be carried through "
                                                                     "without delay."),
    ("What if you heated the melting-point bath rapidly throughout?", "The whole range would be shifted upward and "
                                                                      "broadened, mimicking an impurity."),
]

VIVA_D = [
    ("Why does aniline couple through nitrogen rather than carbon to give a triazene?", "In weekly acidic or "
                                                                                       "neutral media the free "
                                                                                       "amine is the most nucleophilic "
                                                                                       "site, and attack at nitrogen "
                                                                                       "gives the triazene; C-coupling "
                                                                                       "requires a more activated, "
                                                                                       "often substituted ring and "
                                                                                       "different pH."),
    ("How would you prove that coupling occurred through nitrogen?", "By hydrolysis: diazoaminobenzene hydrolyses "
                                                                     "to diazonium salt and aniline, whereas a "
                                                                     "C-coupled azo dye would not; compare with the "
                                                                     "infrared spectrum, where the N\u2013H stretch "
                                                                     "of the triazene is diagnostic."),
    ("Why are diazonium salts stable in acid but not in base?", "In base they form diazohydroxides and diazotates, "
                                                                "which are more prone to decomposition and to "
                                                                "coupling with solvent; acid keeps the ion as a "
                                                                "salt."),
    ("Why is this preparation a useful introduction to azo dye chemistry?", "Because the same diazonium "
                                                                            "intermediate, coupled to phenol or "
                                                                            "naphthol rather than aniline, gives the "
                                                                            "classical azo dyes; the mechanism is "
                                                                            "identical."),
    ("How could you confirm the melting point independently?", "By mixed melting point with an authentic sample, and "
                                                               "by infrared or nuclear magnetic resonance "
                                                               "spectroscopy; the melting point alone is not "
                                                               "conclusive."),
    ("What is the mechanistic role of the acid in the dehydration step?", "It protonates the hydroxyl group of the "
                                                                          "nitrosamine intermediate, converting it "
                                                                          "into a good leaving group so that water "
                                                                          "can depart to give the diazonium ion."),
    ("Why is sodium acetate sometimes added before coupling?", "It raises the pH enough to free the amine from its "
                                                               "hydrochloride without making the solution strongly "
                                                               "basic, which would destroy the diazonium ion."),
    ("What is the thermodynamic driving force for triazene formation?", "Attack of a nucleophilic amine on the "
                                                                        "strongly electrophilic terminal nitrogen of "
                                                                        "the diazonium ion, giving a conjugated, "
                                                                        "stabilised product."),
    ("Why is diazoaminobenzene not a commercial dye?", "Its colour is weak compared with true azo dyes, it is not "
                                                       "substantive to fibres, and it is unstable and toxic; its "
                                                       "value is as an intermediate and a teaching example."),
    ("What safety property makes diazoaminobenzene particularly problematic in a teaching laboratory?", "It is a "
                                                                                                       "suspected "
                                                                                                       "carcinogen "
                                                                                                       "and is "
                                                                                                       "nitrogen-rich, "
                                                                                                       "so it can "
                                                                                                       "decompose "
                                                                                                       "exothermically; "
                                                                                                       "small scale "
                                                                                                       "and careful "
                                                                                                       "waste handling "
                                                                                                       "are "
                                                                                                       "essential."),
]

CH11_CHECK = checklist(
    "11.8",
    ["Diazotisation: ArNH_{2} \u2192 ArN_{2}^{+} with HNO_{2} at low temperature.",
     "Nitrous acid is generated in situ from nitrite and mineral acid.",
     "The nitrosonium ion, NO^{+}, is the effective electrophile.",
     "Keep the diazotisation below 5 \u00b0C.",
     "The diazonium ion decomposes to phenol and nitrogen when warm.",
     "Excess acid is needed, but coupling needs free amine.",
     "Coupling with aniline gives diazoaminobenzene.",
     "Product: C_{6}H_{5}\u2013N=N\u2013NH\u2013C_{6}H_{5}, molar mass 197.24 g mol^{\u22121}.",
     "Expected melting range: 96\u201398 \u00b0C.",
     "Two aniline molecules give one product molecule.",
     "Theoretical yield = (moles aniline/2) \u00d7 197.24.",
     "A sharp melting range indicates purity.",
     "A mixed melting point confirms identity.",
     "Heat the melting apparatus slowly near the transition.",
     "Wash the product with cold water.",
     "Dry gently; do not overheat.",
     "A starch\u2013iodide test detects excess nitrous acid.",
     "Aniline is toxic and skin-absorbed: gloves and hood.",
     "Diazonium salts are never isolated dry.",
     "Discard melting capillaries containing nitrogen-rich residues."],
    ["What is diazotisation?",
     "Write both equations.",
     "Why keep the mixture cold?",
     "Why is excess acid needed?",
     "What is the expected melting point and what does it prove?",
     "What does a broad melting range indicate?",
     "What is a mixed melting point?",
     "What is the molar mass and formula of the product?",
     "Why is the product coloured?",
     "What are the principal hazards?"],
    ["Explain the mechanism of diazotisation through the nitrosonium ion.",
     "Explain why aniline couples through nitrogen to give a triazene.",
     "Why are the two stages run under different acidity conditions?",
     "Calculate the theoretical yield for 0.10 mol aniline and the yield for 6.4 g isolated.",
     "A product melts at 88\u2013107 \u00b0C. Give three causes and the diagnostic test for each.",
     "How would you prove the structure without a melting point?",
     "Why does a rapid heating ramp mimic an impurity?",
     "What is the consequence of failing to destroy excess nitrous acid?",
     "Relate this preparation to azo dye synthesis.",
     "Justify the safety precautions in chemical terms."],
    [("Diazotisation vs coupling", "Formation vs consumption of the diazonium ion."),
     ("Diazonium salt vs diazo compound", "Ionic ArN\u2082\u207a vs neutral Ar\u2013N=N\u2013Ar."),
     ("Azo compound vs azo dye", "Chromophore vs functional colorant."),
     ("Sharp vs broad melting range", "Pure vs impure."),
     ("Melting point vs mixed melting point", "Suggestion vs confirmation."),
     ("Crude vs recrystallised yield", "Before vs after purification."),
     ("First drop vs complete melting", "The literature convention."),
     ("Theoretical vs actual yield", "Stoichiometry vs isolation.")],
    (["Relation", "Expression", "Note"],
     [["Diazotisation", "ArNH_{2} + NaNO_{2} + 2HCl \u2192 ArN_{2}^{+}Cl^{\u2212} + NaCl + 2H_{2}O", "Below 5 "
       "\u00b0C"],
      ["Coupling", "ArN_{2}^{+} + ArNH_{2} \u2192 Ar\u2013N=N\u2013NH\u2013Ar + H^{+}", "Self-coupling"],
      ["Molar mass", "C_{12}H_{11}N_{3} = 197.24", "g mol^{\u22121}"],
      ["Melting point", "96\u201398 \u00b0C", "Literature"],
      ["Theoretical yield", "(n_{aniline}/2) \u00d7 197.24", "Two amines per product"],
      ["Percentage yield", "actual/theoretical \u00d7 100", "\u2014"],
      ["Nitrite test", "starch\u2013iodide gives blue with HNO_{2}", "Completion check"],
      ["Nitrous acid destruction", "HNO_{2} + H_{2}NSO_{3}H \u2192 N_{2} + H_{2}SO_{4} + H_{2}O", "Sulphamic acid"]],
     [38, 82, 46]),
    [["No precipitate", "pH too low or diazotisation incomplete"],
     ["Dark tarry product", "Decomposition or oxidation from overheating"],
     ["Broad, low melting range", "Impurity or residual water"],
     ["High melting range", "Rapid heating or thermometer error"],
     ["Vigorous gas evolution", "Diazonium decomposition \u2014 stop and cool"],
     ["Very low yield", "Losses in filtration and recrystallisation"],
     ["Mixed melting point depressed", "Product is not the expected compound"]],
    ["Cold is the controlling variable in diazotisation.",
     "Two anilines per product: the stoichiometry is 2:1.",
     "Melting point suggests; mixed melting point confirms.",
     "Slow heating is part of the measurement, not a courtesy.",
     "Aniline is a skin-absorbed toxin, not a solvent.",
     "The diazonium ion is an intermediate to be used, not stored.",
     "A wide range means impurity, not bad luck."],
    ["Letting the diazotisation warm above 5 \u00b0C.",
     "Isolating or heating a dry diazonium salt.",
     "Using oxidised brown aniline.",
     "Heating the melting-point bath rapidly.",
     "Reporting a melting point from a wet sample.",
     "Assuming a matching melting point proves identity.",
     "Quantitative yield claimed without drying."],
    ["This preparation involves two stages. First aniline is diazotised: it is dissolved in excess hydrochloric "
     "acid, cooled in an ice bath below five degrees, and sodium nitrite solution is added dropwise so that nitrous "
     "acid is generated in situ and converts the amine, through a nitrosonium intermediate, into the diazonium "
     "chloride. The cold is essential because the diazonium ion decomposes to phenol and nitrogen when warm. Second, "
     "a further portion of aniline is provided, or the acidity is adjusted with sodium acetate, so that free amine "
     "is available; the diazonium ion then couples with it through nitrogen to give diazoaminobenzene, which "
     "separates as a yellow-orange solid. The product is filtered, washed with cold water, dried gently, "
     "recrystallised from aqueous ethanol and identified by its melting range of 96 to 98 degrees, confirmed where "
     "possible by a mixed melting point. The theoretical yield is based on two molecules of aniline per product "
     "molecule, using the molar mass of 197.24, and the main sources of loss are diazonium decomposition and "
     "filtration and recrystallisation losses."],
    ["**Cold first: the diazonium ion dies warm.**",
     "**Acid for diazotisation, free amine for coupling.**",
     "**Two anilines per product \u2014 halve the moles.**",
     "**Melting point suggests; mixed melting point confirms.**"]
)

CH11 = {
    "key": "diazo",
    "num": "11",
    "kicker": "Experiment 11  \u00b7  Organic preparation",
    "title": "Preparation of Diazoaminobenzene",
    "toc": "Preparation of diazoaminobenzene",
    "standfirst": "A two-stage synthesis in which temperature and pH each control a different half of the reaction, "
                  "and a melting range is the only available proof of success.",
    "body": B + [
        ("h2", "11.7  Viva question bank"),
        ("p", "Seventy-eight answered questions on diazotisation, coupling, melting-point technique and the hazards that "
              "make this preparation demanding."),
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
    ] + CH11_CHECK,
}
