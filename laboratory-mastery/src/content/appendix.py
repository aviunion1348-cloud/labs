"""Back matter: master formula sheet, cross-experiment viva, provenance audit."""
from common import checklist, qbox

FA = []

FA += [
    ("h2", "A.1  How to use this appendix"),
    ("lead", "Eleven activities use about thirty relationships, and only a handful of them are genuinely different "
             "from one another. Most are variations on three ideas: something is proportional to something else "
             "(Beer\u2013Lambert, Newton\u2019s law), equivalents are conserved (every titration), or a measurement is "
             "converted by a calibration (efflux time, pH, conductance). This appendix collects the relationships in "
             "one place, with units, validity limits and the error each one is most sensitive to."),
    ("p", "The sheet is organised by **what you are calculating**, not by chapter, because in an examination you "
          "rarely know which chapter a question comes from \u2014 you know what quantity is being asked for. A second "
          "table collects the unit conversions that cause most lost marks, and a third lists the numerical constants "
          "used throughout the volume."),
    ("box", "key", [
        "**Every formula on the next pages has a validity condition.** Using the right formula outside its range is "
        "a more serious error than using the wrong formula inside one, because it looks correct.",
        "**Units are part of the formula.** A relation written for mL and mg L^{\u22121} is not valid for L and "
        "g L^{\u22121}.",
        "**Three of these are empirical calibrations, not laws** \u2014 the Redwood conversion, the pH-electrode "
        "slope of 59.16 mV/pH, and every indicator endpoint pH. Say so if you are asked whether they are fundamental.",
    ], "Three cautions before you memorise anything here"),
]

FA += [
    ("h2", "A.2  Concentration, amount and equivalents"),
    ("tbl", ["Quantity", "Relationship", "Units", "Chapter", "Sensitivity"],
     [["Molarity", "M = n/V = (mass/M_{r})/V", "mol L^{\u22121}", "5, 6, 8", "Weighing and volume"],
      ["Normality", "N = M \u00d7 n_{eq}", "eq L^{\u22121}", "5, 6, 7, 8", "The value of n_{eq}"],
      ["Equivalents", "eq = N \u00d7 V", "eq", "all titrations", "Normality and volume"],
      ["Titration relation", "N_{1}V_{1} = N_{2}V_{2}", "\u2014", "5\u20138", "Endpoint judgement"],
      ["Mass concentration", "\u03c1_{B} = m_{B}/V", "g L^{\u22121}", "1, 6, 7, 8", "Volume basis"],
      ["Percent w/v", "% = (g solute/100 mL) ", "%", "1", "w/v vs w/w basis"],
      ["Dilution", "M_{1}V_{1} = M_{2}V_{2}", "mol L^{\u22121} \u00d7 L", "5", "Volumetric glassware"],
      ["Equivalent weight", "M_{r}/n_{eq}", "g eq^{\u22121}", "5\u20138", "Correct n_{eq} for the reaction"],
      ["ppm in dilute water", "1 mg L^{\u22121} \u2248 1 ppm", "\u2014", "6\u20138", "Density assumption"]],
     [30, 40, 26, 22, 36],
     "**Table A.1** Concentration and equivalent relationships. The number of equivalents per mole is the single "
     "most common source of a factor-of-two error in this volume.", ["l", "l", "l", "c", "l"]),
    ("tbl", ["Species", "M_{r} (g mol^{\u22121})", "n_{eq}", "Equivalent weight", "Used in"],
     [["Oxalic acid dihydrate, H_{2}C_{2}O_{4}\u00b72H_{2}O", "126.07", "2", "63.04", "Ch. 5"],
      ["HCl", "36.46", "1", "36.46", "Ch. 3, 5"],
      ["NaOH", "40.00", "1", "40.00", "Ch. 3, 5"],
      ["CaCO_{3}", "100.09", "2", "50.04 (\u2248 50 by convention)", "Ch. 6, 7"],
      ["EDTA (disodium salt dihydrate)", "372.24", "1 (metal binding), 2 as the acid", "186.12 or 372.24",
       "Ch. 6"],
      ["Cl_{2}", "70.90", "2", "35.45", "Ch. 8"],
      ["Na_{2}S_{2}O_{3}\u00b75H_{2}O", "248.18", "1", "248.18", "Ch. 8"],
      ["KMnO_{4} (in acid)", "158.03", "5", "31.61", "reference"],
      ["Diazoaminobenzene", "197.24", "\u2014", "\u2014", "Ch. 11"]],
     [52, 32, 34, 36, 22],
     "**Table A.2** Molar and equivalent masses used in this volume. EDTA is listed twice because the ambiguity is "
     "real: a 1:1 metal complex but a dibasic acid. The supplied material uses the 1:1 convention.",
     ["l", "c", "c", "c", "l"]),
]

FA += [
    ("h2", "A.3  Instrumental relationships"),
    ("tbl", ["Quantity", "Relationship", "Validity", "Chapter", "Dominant error"],
     [["Beer\u2013Lambert law", "A = \u03b5lc", "Monochromic light, dilute, non-scattering", "1",
       "Stray light above A \u2248 1"],
      ["Absorbance", "A = log_{10}(I_{0}/I) = \u2212log_{10}T", "Any", "1", "Blank mismatch"],
      ["Transmittance", "T = I/I_{0}", "Any", "1", "Instrument drift"],
      ["Concentration by calibration", "c = A/(\u03b5l) = A/slope", "Within the linear range", "1",
       "Non-linearity"],
      ["Conductance", "G = 1/R", "Any", "4", "Polarisation"],
      ["Conductivity", "\u03ba = G(l/A) = G \u00d7 cell constant", "Any", "4", "Cell constant"],
      ["Molar conductance", "\u039b_{m} = 1000\u03ba/c", "c in mol L^{\u22121}", "4", "Units of c"],
      ["Kohlrausch law", "\u039b_{m}^{0} = \u03bd_{+}\u03bb_{+} + \u03bd_{\u2212}\u03bb_{\u2212}", "Infinite dilution",
       "4", "Table values"],
      ["pH", "pH = \u2212log_{10}a(H^{+})", "Dilute aqueous", "3, 7", "Calibration"],
      ["Electrode slope", "E = E^{0} \u2212 0.05916 pH", "25 \u00b0C", "3", "Temperature"],
      ["Kinematic viscosity", "\u03bd = \u03bc/\u03c1", "Any", "9", "Density"],
      ["Redwood conversion", "\u03bd = 0.264t \u2212 190/t", "40\u20132000 s, Redwood I", "9", "Temperature"],
      ["Newton\u2019s law", "\u03c4 = \u03bc(du/dy)", "Newtonian fluid", "9", "\u2014"],
      ["Vapour pressure", "ln P \u2248 A \u2212 B/T", "Over a limited range", "10", "Range"]],
     [40, 48, 40, 18, 34],
     "**Table A.3** Instrumental and physical relationships. Only two of these are laws in the strict sense "
     "(Beer\u2013Lambert under stated conditions, and Newton\u2019s law); the rest are definitions or calibrations.",
     ["l", "l", "l", "c", "l"]),
]

FA += [
    ("h2", "A.4  Reaction-specific relationships"),
    ("tbl", ["Quantity", "Relationship", "Note", "Chapter"],
     [["Pseudo-first-order rate constant",
       "k = (2.303/t) log[(V_{\u221e} \u2212 V_{0})/(V_{\u221e} \u2212 V_{t})]", "Volumes proportional to "
       "concentration of acid formed", "2"],
      ["First-order half-life", "t_{1/2} = 0.693/k", "Independent of initial concentration", "2"],
      ["Arrhenius form", "k = A exp(\u2212E_{a}/RT)", "ln k against 1/T is linear", "2, 9"],
      ["Acid concentration from titration", "C_{HCl} = C_{NaOH}V_{eq}/V_{HCl}", "1:1 stoicheiometry", "3"],
      ["Hardness", "mg L^{\u22121} as CaCO_{3} = (N V \u00d7 50 \u00d7 1000)/V_{sample}", "N in eq L^{\u22121}, V "
       "in mL", "6"],
      ["Conditional formation constant", "K\u2032 = K \u00d7 \u03b1(Y^{4\u2212}) at that pH", "pH 10 for Ca and Mg",
       "6"],
      ["Alkalinity", "mg L^{\u22121} as CaCO_{3} = (V N \u00d7 50 \u00d7 1000)/V_{sample}", "P for the first "
       "endpoint, T for the total", "7"],
      ["Alkalinity apportionment", "OH = 2P \u2212 T; CO_{3} = 2(T \u2212 P); HCO_{3} = T \u2212 2P",
       "Only for P > T/2", "7"],
      ["Residual chlorine", "mg L^{\u22121} as Cl_{2} = (N V \u00d7 35.45 \u00d7 1000)/V_{sample}", "N of "
       "thiosulphate", "8"],
      ["Iodometry stoicheiometry", "1 Cl_{2} \u2261 1 I_{2} \u2261 2 S_{2}O_{3}^{2\u2212}", "\u2014", "8"],
      ["Percentage yield", "(actual/theoretical) \u00d7 100", "\u2014", "11"],
      ["Theoretical yield (diazo)", "(n_{aniline}/2) \u00d7 197.24", "Two amines per product", "11"]],
     [44, 70, 46, 18],
     "**Table A.4** Reaction-specific relationships. The two titration formulae with a factor of 50 are the same "
     "formula with a different equivalent weight; recognising that saves memorising.",
     ["l", "l", "l", "c"]),
]

FA += [
    ("h2", "A.5  Unit conversions that cost marks"),
    ("tbl", ["Conversion", "Factor", "Where it bites"],
     [["cSt \u2192 m^{2} s^{\u22121}", "\u00d7 10^{\u22126}", "Chapter 9 dynamic viscosity"],
      ["cSt \u2192 mm^{2} s^{\u22121}", "\u00d7 1 (identical)", "Stating the unit"],
      ["Poise \u2192 Pa s", "\u00d7 0.1", "Chapter 9"],
      ["centipoise \u2192 mPa s", "\u00d7 1 (identical)", "Chapter 9"],
      ["S cm^{\u22121} \u2192 S m^{\u22121}", "\u00d7 100", "Chapter 4"],
      ["mL \u2192 L", "\u00d7 10^{\u22123}", "Every titration calculation"],
      ["mg \u2192 g", "\u00d7 10^{\u22123}", "Yield and concentration"],
      ["M \u2192 N", "\u00d7 n_{eq}", "Chapters 5\u20138"],
      ["wt % \u2192 mg L^{\u22121}", "\u00d7 10^{4} \u00d7 \u03c1 (g cm^{\u22123})", "Chapter 1 and water analysis"],
      ["ppm \u2192 mg L^{\u22121} (dilute water)", "\u00d7 1", "Chapters 6\u20138"],
      ["\u00b0C \u2192 K", "+ 273.15", "Arrhenius plots"],
      ["mV per pH unit at 25 \u00b0C", "59.16", "Chapter 3"]],
     [58, 52, 60], "**Table A.5** Conversions. The first four cause the largest number of lost marks in the whole "
                   "volume, because a wrong power of ten is invisible in the final answer.", ["l", "l", "l"]),
]

FA += [
    ("h2", "A.6  Constants and reference values"),
    ("tbl", ["Quantity", "Value", "Condition", "Chapter"],
     [["K_{w} of water", "1.0 \u00d7 10^{\u221214}", "25 \u00b0C", "3, 7"],
      ["Neutral pH", "7.00 at 25 \u00b0C; 6.63 at 50 \u00b0C", "Temperature-dependent", "7"],
      ["pK_{a1}, pK_{a2} of carbonic acid", "\u2248 6.3, \u2248 10.3", "25 \u00b0C", "7"],
      ["pK_{a} of HOCl", "\u2248 7.5", "25 \u00b0C", "8"],
      ["Limiting ionic conductance, H^{+}", "349.8 S cm^{2} mol^{\u22121}", "25 \u00b0C", "4"],
      ["Limiting ionic conductance, OH^{\u2212}", "198.3 S cm^{2} mol^{\u22121}", "25 \u00b0C", "4"],
      ["Limiting ionic conductance, Cl^{\u2212}", "76.3 S cm^{2} mol^{\u22121}", "25 \u00b0C", "4"],
      ["Limiting ionic conductance, Na^{+}", "50.1 S cm^{2} mol^{\u22121}", "25 \u00b0C", "4"],
      ["\u03bb_{max} of Co(II) chloride complex", "\u2248 511 nm (weak band \u2248 615 nm)", "Aqueous", "1"],
      ["Viscosity of water", "1.00 mPa s", "20 \u00b0C", "9"],
      ["Density of a typical mineral oil", "\u2248 880 kg m^{\u22123}", "40 \u00b0C", "9"],
      ["Melting point of diazoaminobenzene", "96\u201398 \u00b0C", "Literature", "11"],
      ["Diesel flash point (closed cup)", "\u2248 52\u201396 \u00b0C", "Grade-dependent", "10"],
      ["Kerosene flash point (closed cup)", "\u2248 38\u201374 \u00b0C", "Grade-dependent", "10"]],
     [46, 62, 44, 18],
     "**Table A.6** Constants and reference values used in this volume. Values marked \u2248 are typical rather than "
     "exact, and textbook values vary slightly with the source.", ["l", "l", "l", "c"]),
]

FA += [
    ("h2", "A.7  The ten relationships worth writing on one card"),
    ("bul", [
        "**A = \u03b5lc**, with the working range 0.1\u20131.0 absorbance.",
        "**N_{1}V_{1} = N_{2}V_{2}**, and 1 cSt = 10^{\u22126} m^{2} s^{\u22121} \u2014 the two most reusable "
        "identities in the volume.",
        "**k = (2.303/t) log[(V_{\u221e} \u2212 V_{0})/(V_{\u221e} \u2212 V_{t})]**, with the 2.303 never omitted.",
        "**\u03ba = G(l/A)**, and G = 1/R.",
        "**Every \u2018mg L^{\u22121} as CaCO_{3}\u2019 calculation** is N V \u00d7 50 \u00d7 1000/V_{sample}.",
        "**T is cumulative** in an alkalinity titration; P and T together give the species.",
        "**35.45 = 70.90/2**, the equivalent weight of chlorine.",
        "**\u03bd = 0.264t \u2212 190/t**, valid for 40\u20132000 s in a Redwood I.",
        "**Two anilines per diazoaminobenzene**, so halve the moles before multiplying by 197.24.",
        "**Every answer needs units, a temperature where relevant, and a sanity check.**",
    ]),
    ("box", "exam", [
        "**If you forget a formula in the examination, derive it from units.** Every relation in this appendix can "
        "be reconstructed by asking what units the answer must have \u2014 that is how the Redwood constant, the "
        "factor of 50 and the 35.45 can all be recovered under pressure.",
    ], "The examination fallback"),
]

CROSS = []

CROSS += [
    ("h2", "B.1  Why cross-experiment questions exist"),
    ("lead", "The most discriminating questions in a practical examination are the ones that cannot be answered from "
             "a single chapter. They test whether you have understood the //method// rather than memorised eleven "
             "separate procedures. This appendix collects those questions, grouped by the idea that links them."),
    ("p", "Four themes run through all eleven activities, and almost every cross-experiment question is a variation "
          "on one of them:"),
    ("tbl", ["Theme", "Question it generates", "Activities involved"],
     [["Calibration", "\u201cHow do you know what your instrument reading means?\u201d", "1, 3, 4, 9, 10"],
      ["Conservation of equivalents", "\u201cWhat is actually being counted in your titration?\u201d", "5, 6, 7, 8"],
      ["Control of a dominant variable", "\u201cWhich variable would ruin this if you lost control of it?\u201d",
       "all eleven"],
      ["Evidence of identity", "\u201cHow do you know you made what you think you made?\u201d", "1, 6, 11"]],
     [36, 76, 56], "**Table B.1** The four themes. Learning these four answer structures covers the majority of "
                   "cross-experiment questions.", ["l", "l", "l"]),
]

QA_CROSS_A = [
    ("Compare how \u2018blank\u2019 is used in spectrophotometry, in the chlorine determination and in conductometric "
     "titration.",
     "In spectrophotometry the blank contains everything except the absorbing species, and it sets 100 % T, "
     "removing the solvent and cell contribution. In the chlorine determination the blank is a reagent blank: it "
     "measures iodine produced by impurities or dissolved oxygen, and its equivalent chlorine is subtracted from "
     "the result. In conductometry there is no blank in that sense; the correction is the cell constant, "
     "determined with a standard potassium chloride solution. All three are corrections for a contribution that is "
     "not the analyte, but only the first two are additive; the third is multiplicative."),
    ("Compare the dominant systematic error in the hydrolysis experiment with that in the Redwood viscometer.",
     "In hydrolysis the dominant error is temperature: the rate constant changes by several percent per degree, "
     "and the reaction must be thermostatted at 70\u201390 \u00b0C. In the viscometer the dominant error is also "
     "temperature, for the same physical reason \u2014 an activated process \u2014 with roughly three to five percent "
     "per degree at 40 \u00b0C. The parallel is instructive: in both, timing precision is irrelevant compared with "
     "thermal control."),
    ("Both the EDTA titration and the alkalinity titration use an indicator whose colour change defines the "
     "endpoint. Compare the chemistry of the two colour changes.",
     "In the EDTA titration the indicator is a metal-ion complexing agent: Eriochrome Black T is wine red when bound "
     "to calcium or magnesium and blue when free, so the endpoint marks the moment EDTA has stripped the metal from "
     "the indicator \u2014 a competition between two ligands. In the alkalinity titration the indicators are "
     "acid\u2013base species whose protonation state controls their colour, so the endpoint marks a pH, not a metal "
     "concentration. One reports a chemical competition, the other a proton activity."),
    ("Why is a factor of 50 used in both hardness and alkalinity calculations?",
     "Because both express a capacity in equivalents per litre on the calcium carbonate scale, and the equivalent "
     "weight of calcium carbonate is 50 g eq^{\u22121}. In hardness it converts equivalents of divalent metal into "
     "the equivalent mass of CaCO_{3}; in alkalinity it converts equivalents of acid consumed into the same scale. "
     "The identical factor reflects an identical purpose: to put different species on one comparable axis."),
    ("Compare the way an equivalence point is located in the pH-metric titration and in the conductometric "
     "titration.",
     "pH-metrically, the equivalence point is the steepest part of the S-shaped curve, located by the maximum of "
     "\u0394pH/\u0394V \u2014 a point of maximum slope. Conductometrically, the equivalence point is the intersection of "
     "two straight branches \u2014 a point of discontinuous slope. The first requires enough pH change near "
     "equivalence; the second requires the two branches to have measurably different slopes, which depends on the "
     "difference in ionic mobility."),
    ("Both the standardisation of NaOH and the assay of HCl depend on the same arithmetic. Explain why the "
     "standardisation must come first.",
     "The HCl assay measures the amount of base needed, so its result is proportional to the NaOH concentration. "
     "If the NaOH normality were wrong by five percent, every HCl result would be wrong by five percent in the same "
     "direction. Standardising against a primary standard fixes the scale; without it the assay measures only a "
     "ratio to an unknown."),
    ("Why does the volume of sample matter so much in water analysis but hardly at all in a melting-point "
     "determination?",
     "Water analysis reports concentrations \u2014 an amount divided by the volume taken \u2014 so an error in the "
     "aliquot propagates directly into the result. A melting point is an intensive property of the solid; the "
     "sample size affects only the sharpness of the observation, not the value."),
    ("Compare the two experiments in this volume that rely on an efflux or flow measurement.",
     "The Redwood viscometer measures the time for a fixed volume of oil to flow through a jet, and converts the "
     "time to kinematic viscosity by an empirical calibration. The Pensky\u2013Martens determination measures no "
     "flow at all, but relies on vapour generation, which is likewise a thermally activated transport process. The "
     "link is that both are governed by the temperature-dependent mobility of molecules, which is why both demand "
     "tight thermal control \u2014 but only the Redwood measurement is a flow measurement."),
    ("Which activities in this volume produce a result that is defined by a written method rather than by a "
     "physical constant?",
     "The flash point and fire point are defined by the method \u2014 heating rate, stirring rate, test interval, "
     "cup geometry \u2014 so a different method gives a different number. To a lesser extent the Redwood viscosity "
     "and the indicator-based alkalinities are also method-dependent. By contrast the absorbance of a solution, the "
     "rate constant of a reaction and the hardness of a water are properties of the system, not of the procedure."),
    ("Compare the evidence you would accept for the identity of a compound in Chapter 11 with the evidence you "
     "would accept for the identity of a water sample in Chapter 6.",
     "The diazoaminobenzene is evidence about a //molecular species//: a melting range, ideally confirmed by a "
     "mixed melting point, and by spectroscopy. The water sample is evidence about a //mixture//: the hardness is a "
     "sum of contributions from several metals, and no single number identifies which metals are present. One "
     "requires identity; the other requires quantification, and the two call for different confirmation strategies."),
]

QA_CROSS_B = [
    ("A student says both the spectrophotometer and the pH meter \u2018need calibrating\u2019. Are these the same "
     "operation?",
     "Not quite. The spectrophotometer is zeroed against a blank, which sets an offset but does not establish the "
     "scale \u2014 the scale comes from the standards in the calibration series. The pH meter is calibrated with two "
     "buffers, which sets both the offset and the slope of a linear response. The first is a subtraction; the second "
     "is a two-parameter fit."),
    ("Why do several activities in this volume require a standard solution prepared from a solid, and why is that "
     "preferable?",
     "A solid primary standard can be weighed accurately, giving a concentration traceable to mass, which is the "
     "most reliable quantity in the laboratory. Volumetric glassware adds uncertainty at every transfer. Where a "
     "suitable solid exists \u2014 oxalic acid, potassium dichromate, calcium carbonate \u2014 it is preferred over "
     "standardising against another solution."),
    ("Which activities would be invalidated by a five percent error in a single volume, and which would not?",
     "Invalidated: the volumetric HCl assay, the EDTA hardness, the alkalinity, and the chlorine determination, "
     "because each reports a concentration that is directly proportional to a measured volume. Not invalidated: the "
     "pH-metric titration (the equivalence volume, not the absolute volume, sets the result), the spectrophotometric "
     "determination (a volume error affects the standards and samples equally, partly cancelling), and the melting "
     "point."),
    ("Why is the second endpoint of an alkalinity titration a different kind of measurement from the second "
     "titration in an HCl assay?",
     "The alkalinity second endpoint continues the //same// titration: the total acid delivered is the sum of both "
     "stages, and the species distribution is read from the ratio. The HCl assay is a separate determination on a "
     "separate aliquot; the two titres are independent measurements that happen to use the same reagent."),
    ("Why do so many of these experiments specify distilled water, and what would tap water do to each?",
     "Tap water contains calcium, magnesium, bicarbonate, chloride and residual chlorine. In the EDTA titration it "
     "adds hardness; in the alkalinity and chlorine determinations it adds alkalinity and chlorine; in the "
     "spectrophotometric blank it adds absorbing species; in the diazo preparation it adds ions that alter the "
     "precipitation. In conductometry it adds background electrolyte and swamps the titration."),
    ("Compare the role of temperature in four activities in this volume.",
     "In hydrolysis it controls the rate constant (exponential dependence). In conductometry it changes ionic "
     "mobility and therefore the cell constant's effective value. In viscometry it changes viscosity by several "
     "percent per degree. In the flash-point determination it is the measured variable itself. Only in the "
     "volumetric titrations is temperature a minor contributor."),
    ("Why do some methods in this volume give a result in mg L^{\u22121} and others in a percentage?",
     "The unit reflects the question being asked. Water analysis asks how much of a substance is present per volume "
     "of water, because the water is the matrix and the concentration is what matters for health or treatment. A "
     "reagent preparation asks what fraction of the material is the species of interest, because the material "
     "itself is the product. Chapter 1 is the awkward case, because the supplied source does not state which basis "
     "it intends."),
    ("Justify why the chlorine determination uses 35.45 while the thiocyanate-free hardness determination uses 50.",
     "Both are equivalent weights of a two-electron species. Chlorine as Cl_{2} has a molar mass of 70.90 and "
     "accepts two electrons, so its equivalent weight is 35.45. Calcium carbonate has a molar mass of 100.09 and is "
     "divalent, so its equivalent weight is 50.04, conventionally rounded to 50. The pattern \u2014 molar mass "
     "divided by the number of electrons or charges \u2014 is the same."),
    ("A sample gives a sharp endpoint in the EDTA titration but a poor one in the alkalinity titration. What does "
     "that tell you?",
     "The two failures have different causes. A poor EDTA endpoint suggests a metal-exchange problem \u2014 pH "
     "outside the window, too much indicator, or an interfering metal. A poor alkalinity endpoint suggests an "
     "indicator or colour problem \u2014 a strongly coloured sample, too little indicator, or a sample whose buffering "
     "makes the pH change gradual near an endpoint. Sharpness in one says nothing about the other."),
    ("Which single habit, applied to all eleven activities, would improve the reliability of every result you "
     "produce?",
     "Recording the controlled variables at the moment of measurement \u2014 temperature, sample volume, reagent "
     "normality, and the exact endpoint criterion \u2014 because every activity in this volume fails in the same way "
     "when one of those is assumed rather than recorded."),
]

QA_CROSS_C = [
    ("Design a single experiment that would measure both the hardness and the alkalinity of the same water "
     "sample.",
     "Take one sample and split it into three aliquots. On the first, titrate with standard acid using "
     "phenolphthalein and then methyl orange to obtain P and T and hence the carbonate species. On the second, "
     "buffer to pH 10 and titrate with EDTA to the Eriochrome Black T endpoint to obtain total hardness. On the "
     "third, measure pH and temperature. The two titrations are independent and must not be performed sequentially "
     "in the same flask, because the acid used for alkalinity destroys the buffer conditions needed for the EDTA "
     "titration."),
    ("Explain how you would use one of these activities to demonstrate a concept from another.",
     "The conductometric titration demonstrates the mobility concept used throughout: replacing a highly mobile ion "
     "with a less mobile one lowers conductance, and adding a highly mobile ion raises it. The same idea explains "
     "why the hydrolysis experiment titrates with NaOH rather than following conductance directly \u2014 the "
     "conductance change would be dominated by the buffer and by the strong acid already present, and would not "
     "isolate the small amount of acid produced by hydrolysis."),
    ("A laboratory has only a balance, a burette, a pipette and distilled water. Which activities could still be "
     "performed, and which could not?",
     "Possible: the standardisation of NaOH and assay of HCl, the EDTA hardness, the alkalinity, and the "
     "iodometric chlorine determination \u2014 all are volumetric. Impossible: spectrophotometry, pH-metry, "
     "conductometry, viscometry, flash point and the diazo preparation, all of which require specific instruments. "
     "Melting-point characterisation would need a heating block or a Thiele tube."),
    ("Compare the way each of the titration experiments detects its endpoint.",
     "The HCl assay uses a pH indicator that changes colour over a range. The EDTA titration uses a metallochromic "
     "indicator that changes colour when the metal is removed. The alkalinity titration uses two pH indicators to "
     "mark two different pH values. The chlorine determination uses starch, which responds to iodine rather than to "
     "the analyte. The pH-metric and conductometric titrations detect the endpoint //instrumentally//, without any "
     "indicator at all."),
    ("If you had to choose three of these eleven activities to teach a complete course in measurement, which would "
     "you pick and why?",
     "The spectrophotometric determination, because it teaches calibration, blanking and the limits of linearity; "
     "the volumetric standardisation, because it teaches equivalents, primary standards and the arithmetic of "
     "concentration; and the viscometry, because it teaches that the measured quantity is not the reported quantity "
     "\u2014 the conversion is empirical and temperature-bound. Among them they cover the three epistemologies of "
     "this volume: instrumental, stoicheiometric and empirical."),
    ("In which activities is a result reported as a range rather than a single number, and why?",
     "Only the melting point, where the range itself carries information: a narrow range indicates purity, a wide "
     "range indicates impurity, and the reported value is conventionally the beginning of melting. The other "
     "activities report a single value with an implied uncertainty, which is why the replicates matter."),
    ("How would you explain to a school student why the same water sample can be \u2018hard\u2019 and "
     "\u2018alkaline\u2019 at the same time?",
     "Both arise from the same geology. Rainwater carrying dissolved carbon dioxide percolates through limestone, "
     "dissolving calcium carbonate; that single process adds calcium ions, which make the water hard, and "
     "bicarbonate ions, which give it alkalinity. The two measurements are therefore often correlated, although "
     "they measure different things and either can be high without the other."),
    ("Which activity in this volume is the least precise, and which is the most precise, and why?",
     "The least precise is the fire-point determination, which depends on observing sustained burning for five "
     "seconds. The most precise is a volumetric titration with a sharp indicator, where concordant titres routinely "
     "agree to 0.05 mL in 25 mL \u2014 about 0.2 %. The difference is not carelessness; it is the nature of the "
     "quantity being measured."),
    ("All eleven activities end with a sanity check. Give the sanity check for three of them.",
     "Chapter 1: the absorbance of the unknown must lie within the range of the standards. Chapter 6: the hardness "
     "must be plausible for the water type, and the apportioned species must sum to the total in Chapter 7. Chapter "
     "9: the efflux time must lie between 40 and 2000 s, and the resulting viscosity must correspond to a "
     "recognisable oil grade."),
    ("If two of these experiments disagreed about the same water sample, how would you decide which was wrong?",
     "By finding a method that measures the same quantity independently. Hardness by EDTA can be checked "
     "gravimetrically or by atomic spectroscopy; alkalinity can be checked by a pH titration curve; residual "
     "chlorine by a colorimetric DPD method. Agreement between two methods that share no reagents is far stronger "
     "evidence than repeating the same method more carefully."),
]

CROSS_CHECK = checklist(
    "B.2",
    ["Four themes: calibration, equivalents, dominant variable, evidence of identity.",
     "A blank subtracts a contribution; a calibration establishes a scale.",
     "A cell constant is a multiplicative correction, not an additive blank.",
     "Temperature is the dominant systematic variable in rate and transport measurements.",
     "Indicator endpoints report either a pH or a chemical competition.",
     "Hardness and alkalinity share a factor of 50 because both use the CaCO_{3} scale.",
     "Every concentration result is proportional to the sample volume.",
     "Intensive properties such as melting point do not depend on sample size.",
     "A method-defined result changes if the method changes.",
     "Standardise the titrant before assaying anything with it.",
     "Distilled water protects all eleven activities from contamination.",
     "A metal-ion indicator competes; an acid\u2013base indicator protonates.",
     "35.45 and 50 are both molar mass divided by charge.",
     "Cross-experiment questions test method, not memory.",
     "Two independent methods are stronger evidence than careful repetition.",
     "A pH-meter calibration fits a slope; a blank does not.",
     "A poor EDTA endpoint and a poor alkalinity endpoint have different causes.",
     "Some quantities are ranges, not numbers, and the range carries information.",
     "Record controlled variables at the moment of measurement.",
     "A sanity check is a comparison with a plausible magnitude."],
    ["What are the four cross-experiment themes?",
     "How does a blank differ from a calibration?",
     "Why does a factor of 50 appear twice?",
     "Why is temperature the dominant variable in two activities?",
     "How does a metal-ion indicator differ from an acid\u2013base indicator?",
     "Which results are method-defined?",
     "Why does sample volume matter in water analysis?",
     "Which activity is least precise, and why?",
     "What makes an independent check stronger than a repeat?",
     "Give the sanity check for three activities."],
    ["Design an experiment that measures hardness and alkalinity on one sample, explaining why the aliquots must be "
     "separate.",
     "Compare the endpoint detection of all five titrimetric activities.",
     "If two experiments disagree, design a decisive third measurement.",
     "Explain why the same rock geology produces both hardness and alkalinity.",
     "Which three activities would you choose to teach measurement, and on what criterion?",
     "Argue whether an indicator endpoint can ever be as reliable as an instrumental one.",
     "Justify the use of a primary standard in one activity and its absence in another.",
     "Explain why the hydrolysis experiment does not use conductometry, even though acid is produced.",
     "Compare additive and multiplicative corrections, with examples.",
     "Which activity in this volume would you trust least if you had only one replicate, and why?"],
    [("Blank vs calibration", "Subtraction vs scale."),
     ("Additive vs multiplicative correction", "Blank vs cell constant."),
     ("Intensive vs extensive", "Melting point vs titre."),
     ("Method-defined vs system-defined", "Flash point vs rate constant."),
     ("Metal-ion vs pH indicator", "Competition vs protonation."),
     ("Single value vs range", "Titre vs melting range."),
     ("Repeat vs independent check", "Precision vs confirmation."),
     ("Precision vs accuracy", "Agreement vs truth.")],
    (["Theme", "Question form", "Activities"],
     [["Calibration", "What does the reading mean?", "1, 3, 4, 9, 10"],
      ["Equivalents", "What is being counted?", "5, 6, 7, 8"],
      ["Dominant variable", "What could ruin this?", "all"],
      ["Evidence of identity", "How do you know?", "1, 6, 11"],
      ["Method dependence", "Would another method agree?", "9, 10, 7"],
      ["Additive correction", "What must be subtracted?", "1, 8"],
      ["Multiplicative correction", "What must be divided out?", "4, 9"],
      ["Sanity check", "Is the magnitude plausible?", "all"]],
     [40, 68, 52]),
    [["Two methods disagree", "One has a systematic error; find an independent third method"],
     ["Result scales with sample volume", "The concentration formula was applied with the wrong volume"],
     ["Result is method-dependent", "The quantity is defined by the procedure"],
     ["Poor endpoint in EDTA only", "pH window, indicator amount, or interfering metal"],
     ["Poor endpoint in alkalinity only", "Colour, indicator amount, or gradual buffering"],
     ["All results shifted in one direction", "A standardisation or calibration error"],
     ["Replicates agree but the value is wrong", "Systematic error, not random scatter"]],
    ["Every activity is a calibration, a count or a calibration-like conversion.",
     "Additive corrections are subtracted; multiplicative ones are divided out.",
     "Temperature dominates rate and transport measurements.",
     "Concentration results are proportional to the sample volume.",
     "Ranges carry information that single numbers cannot.",
     "Independent methods confirm; repeats only reassure.",
     "The four themes answer most cross-experiment questions."],
    ["Confusing a blank with a calibration.",
     "Comparing a pH indicator with a metal-ion indicator as if both report pH.",
     "Forgetting that a method-defined quantity changes with the method.",
     "Assuming agreement between replicates proves accuracy.",
     "Applying a concentration formula to the wrong sample volume.",
     "Treating a melting range as a single number.",
     "Comparing results obtained at different temperatures."],
    ["The eleven activities are held together by four ideas. First, calibration: an instrument reading is "
     "meaningless until something standard converts it, whether that is a blank plus a series of standards in "
     "spectrophotometry, a two-buffer fit on a pH meter, a cell constant in conductometry, or an empirical relation "
     "in viscometry. Second, conservation of equivalents: every titration counts how many equivalents of a reagent "
     "were consumed, which is why normality, not molarity, appears in the formulae. Third, control of a dominant "
     "variable: temperature in rate and transport measurements, pH in chelation, timing in the iodine titration. "
     "Fourth, evidence of identity or of validity: a melting range confirmed by a mixed melting point, a "
     "concentration confirmed by an independent method, a result checked against a plausible magnitude. If I am "
     "asked a question that crosses two chapters, it is almost always asking which of these four ideas is doing the "
     "work."],
    ["**Calibrate, count, control, confirm \u2014 four themes, eleven activities.**",
     "**Blanks are subtracted; cell constants are divided out.**",
     "**A result proportional to sample volume depends on that volume.**",
     "**Independent methods confirm; repeats only reassure.**"]
)

PROV = []

PROV += [
    ("h2", "C.1  What this volume was built from"),
    ("lead", "This volume is a synthesis, not a reproduction. Three supplied laboratory guides were read in full, "
             "their contents inventoried, their overlaps removed and their gaps recorded. This appendix documents "
             "that process so that every claim in the volume can be traced, challenged or corrected."),
    ("p", "The three sources, and the shorthand used throughout this volume:"),
    ("tbl", ["Key", "Source", "Activities contributed", "Character of the material"],
     [["A", "Chemistry Laboratory Master Guide", "1, 2, 3, 6, 7, 8, 9, 11",
       "Procedures and observation sheets, with handwritten amendments and some blank tables"],
      ["B", "Complete Laboratory Mastery Guide", "1, 2, 3, 4, 9, 10",
       "Apparatus descriptions and theory, with the conductometric readings partly overwritten"],
      ["C", "Complete Laboratory Mastery Practical and Viva Guide", "1, 3, 5, 6, 7, 8, 10",
       "Practical and viva material, with formula statements and expected results"]],
     [14, 56, 42, 58],
     "**Table C.1** Source inventory. The three sources overlap substantially on activities 1, 3, 6 and 7, and each "
     "contains at least one activity the others lack.", ["c", "l", "l", "l"]),
    ("h2", "C.2  What was added, and what was not"),
    ("tbl", ["Category", "Policy in this volume", "How you can tell"],
     [["Supplied facts", "Reproduced faithfully: aims, reagents, reactions, formula statements, melting range, "
       "\u03bb_{max}, ionic conductances",
       "Stated as \u2018the supplied material sets the aim as\u2026\u2019 or attributed to the source"],
      ["Derivations and explanations", "Added teaching, built from standard physical chemistry",
       "Written as prose explanation, not attributed to any source"],
      ["Worked calculations", "Illustrative arithmetic, never presented as measured data",
       "Labelled \u2018worked illustration\u2019, with numbers chosen for convenience"],
      ["Observation tables", "Reproduced in layout, left blank where the source is blank or illegible",
       "Captioned with an explicit note that the source contains no readings"],
      ["Missing method details", "Named as gaps, never invented",
       "Flagged in a grey callout at the point where they matter; see Table 0.3"],
      ["Questions and answers", "Written for this volume from the underlying science",
       "Presented as a viva bank, which is by nature authored, not transcribed"]],
     [38, 76, 54],
     "**Table C.2** Editorial policy. The distinction between supplied fact and added explanation is maintained "
     "throughout; where it could not be maintained, the gap is flagged.", ["l", "l", "l"]),
    ("box", "key", [
        "**No experimental value in this volume is invented.** Where a number appears that is not from the sources, "
        "it is either a physical constant available in any textbook, or an explicitly labelled illustrative "
        "calculation.",
        "**No procedure has been completed by guesswork.** Where the sources omit a step \u2014 the Pensky\u2013Martens "
        "opening procedure, the diazo reagent quantities, the conductometric increment schedule \u2014 the omission is "
        "recorded and the reader is directed to the approved method.",
        "**Where the sources contradict themselves, both readings are reported.** The hydrolysis aim says ethyl "
        "acetate while one passage says methyl acetate; the source for activity 4 contains two conflicting increment "
        "schedules.",
    ], "Three commitments"),
]

PROV += [
    ("h2", "C.3  The register of gaps, in full"),
    ("p", "Table 0.3 in the front matter summarises the twelve gaps. This table states each one with the action "
          "taken in the relevant chapter, so that the register can be checked against the text."),
    ("tbl", ["Gap", "Chapter", "Action taken"],
     [["Hydrolysis: no completed observation table or titres", "2",
       "Observation table reproduced blank; worked example labelled illustrative"],
      ["Hydrolysis: \u2018methyl acetate\u2019 in one passage against \u2018ethyl acetate\u2019 in the aim", "2",
       "Ethyl acetate used throughout, following the aim and the procedure; inconsistency noted"],
      ["Cobalt standards: percentage basis (w/v or w/w) not stated", "1",
       "Both possibilities explained; the basis is flagged as needing confirmation"],
      ["Cobalt standards tables blank; scan wavelength handwritten", "1",
       "Blank tables reproduced; reader instructed to record the wavelength actually set"],
      ["pH-metric: standardisation details incomplete", "3",
       "Standardisation described in the general form used in Chapter 5"],
      ["Conductometric: two conflicting increment schedules; readings overwritten", "4",
       "Both schedules described; no value transcribed from the overwritten readings"],
      ["EDTA: observation tables blank", "6",
       "Layout reproduced blank; worked illustration uses labelled arithmetic examples"],
      ["pH and alkalinity: readings faint and handwritten", "7",
       "No values transcribed; the calculation chain is demonstrated with labelled illustrations"],
      ["Residual chlorine: normality amended by hand", "8",
       "Reader instructed to use the standardised value from the reagent label"],
      ["Redwood: calibration constants faintly printed and instrument-specific", "9",
       "Constants stated as supplied (0.264, 190) with a note to verify against the instrument certificate"],
      ["Pensky\u2013Martens: opening procedure, heating rate, stirring rate and test interval absent", "10",
       "Named as a gap; chapter explains why each parameter matters and directs the reader to the standard method"],
      ["Diazoaminobenzene: quantities, mixing order and temperature instructions absent by design", "11",
       "Treated conceptually; no recipe supplied; hazards stated in full"]],
     [66, 16, 86],
     "**Table C.3** The gap register with the action taken in each chapter. Every row of Table 0.3 appears here.",
     ["l", "c", "l"]),
]

PROV += [
    ("h2", "C.4  How to check anything in this volume"),
    ("p", "Three kinds of statement appear in the chapters, and each can be checked differently:"),
    ("num", [
        "**A statement attributed to the supplied material.** Check it against the source page. If the chapter and "
        "the source disagree, the source governs for the purposes of your examination, and the chapter should be "
        "corrected.",
        "**A statement of standard chemistry or physics.** Check it against any reputable textbook. Values that vary "
        "between sources \u2014 indicator endpoint pH, expected flash-point ranges, limiting molar conductances \u2014 "
        "are given as typical values with the condition stated.",
        "**An illustrative calculation.** Recompute it. Every one is designed to be reproducible from the numbers "
        "given; if it is not, it is an error in this volume, not in your arithmetic.",
    ]),
    ("box", "note", [
        "**A caution about textbook constants.** The values of K_{w}, the ionic conductances and the pK_{a} values "
        "used here are standard at 25 \u00b0C, but different textbooks round them differently. If your course uses "
        "slightly different values, use your course\u2019s values in an examination and say which you used.",
        "**A caution about method-dependent results.** Flash point, fire point and, to a lesser degree, viscosity "
        "are defined by the procedure. Quoting a value without the method is, in a regulatory context, meaningless.",
    ], "Two cautions for the careful reader"),
    ("h2", "C.5  What this volume deliberately does not include"),
    ("bul", [
        "**Operating recipes for hazardous preparations.** The diazoaminobenzene chapter teaches the chemistry and "
        "the safety, and refers the reader to a supervised protocol for the quantities.",
        "**Transcribed data from illegible sources.** Faint handwriting is not a data source; the chapters show the "
        "method for handling data instead.",
        "**Speculative completions of missing procedures.** Where a step is absent, the chapter says so.",
        "**Regulatory thresholds quoted from memory.** Classification thresholds vary by jurisdiction; the chapters "
        "state the measured value and refer to the applicable standard.",
        "**Photographs or reproductions of the source pages.** The volume is a teaching text, not a facsimile.",
    ]),
    ("h2", "C.6  A closing note on using this volume"),
    ("p", "Eleven activities, several hundred pages and roughly nine hundred answered questions make a "
          "large volume, but it is not meant to be read from end to end. It is meant to be used the way a workshop "
          "is used: you go to the bench that matches the job in front of you. Before a practical session, read the "
          "chapter\u2019s procedure and precautions. After it, read the error budget against what actually happened. "
          "Before an examination, work the viva bank aloud and attempt the mock papers closed-book."),
    ("p", "The measure of success is not that you can recite this volume. It is that, faced with an unfamiliar "
          "measurement, you ask the four questions this volume keeps asking: **what am I actually measuring, what "
          "converts that reading into the quantity I want, which variable would ruin this if I lost control of it, "
          "and how would I know if I were wrong?**"),
    ("box", "key", [
        "**Read the chapter that matches the job in front of you, not the book from cover to cover.**",
        "**Four questions: what am I measuring, what converts it, what could ruin it, how would I know?**",
        "**Where the source is silent, this volume says so \u2014 and says what to do instead.**",
    ], "Memory strip"),
]

APPENDIX_A = {
    "key": "formulas",
    "num": "A",
    "kicker": "Appendix A  \u00b7  Reference",
    "title": "Master Formula Sheet",
    "toc": "Master formula sheet",
    "standfirst": "Every relationship used in this volume, organised by the quantity being calculated rather than by "
                  "chapter, with units, validity limits and the error each is most sensitive to.",
    "body": FA,
}

APPENDIX_B = {
    "key": "crossviva",
    "num": "B",
    "kicker": "Appendix B  \u00b7  Cross-experiment viva",
    "title": "Questions That Span the Whole Course",
    "toc": "Cross-experiment viva",
    "standfirst": "Thirty questions that cannot be answered from a single chapter, grouped under the four ideas that "
                  "link all eleven activities.",
    "body": CROSS + [
        ("h2", "B.2  The questions"),
        ("p", "Grouped by what they test: the method itself, the arithmetic of concentration, and the judgement that "
              "comes after the number."),
        ("qsub", "A.  Method and meaning"),
        ("qa", QA_CROSS_A),
        ("qsub", "B.  Arithmetic and validity"),
        ("qa", QA_CROSS_B),
        ("qsub", "C.  Judgement and synthesis"),
        ("qa", QA_CROSS_C),
    ] + CROSS_CHECK,
}

APPENDIX_C = {
    "key": "provenance",
    "num": "C",
    "kicker": "Appendix C  \u00b7  Provenance",
    "title": "Source Audit and Editorial Record",
    "toc": "Source audit and provenance",
    "standfirst": "What was supplied, what was added, what was flagged as missing, and how to check any statement in "
                  "this volume against the source it came from.",
    "body": PROV,
}
