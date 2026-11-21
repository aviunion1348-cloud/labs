VIVA_E = [
    ("Why is the receiving flask marked at 50 mL rather than being weighed?",
     "The method is defined by a fixed volume, so the calibration constants correspond to that volume."),
    ("What is the effect of a wet cup on the measured time?",
     "Residual water changes the effective viscosity and can cause erratic flow."),
    ("Why is the instrument not used for volatile solvents?",
     "They evaporate and change composition, and their efflux times fall outside the valid range."),
    ("Why does the oil level in the cup fall during the measurement?",
     "Because the oil flows out through the jet; the standard geometry accounts for the changing head."),
    ("Why is the first reading of a series often rejected?",
     "Thermal equilibrium or wetting of the jet may not yet be established."),
    ("Why is the efflux time not proportional to viscosity over the whole range?",
     "Because the short-time corrections and the entrance and exit effects make the relation non-linear."),
    ("What is the significance of an ISO viscosity grade?",
     "It classifies a lubricant by its nominal kinematic viscosity at 40 \u00b0C."),
    ("Why do oil specifications quote viscosity at both 40 and 100 \u00b0C?",
     "To define both the cold-flow behaviour and the film thickness at operating temperature."),
    ("What is the role of the bath medium?",
     "It transfers heat to the oil and holds the temperature constant during the measurement."),
    ("Why is the thermometer placed in the oil rather than in the bath?",
     "Because the oil temperature is the quantity that governs the viscosity."),
    ("What is the effect of dissolved air on the efflux time?",
     "Bubbles disrupt the flow and can shorten the time by reducing the effective volume."),
    ("Why is a Redwood second not a fundamental unit?",
     "It depends on the geometry and calibration of a specific instrument, so it is empirical."),
    ("How would you obtain the activation energy of viscous flow?",
     "Plot ln \u03bd against 1/T and take the slope as \u2212E_{a}/R."),
    ("Why does viscosity decrease with temperature for a liquid but increase for a gas?",
     "Liquid flow is hindered by intermolecular attraction, which weakens on heating; gas viscosity arises from "
     "momentum transfer between molecules and rises with temperature."),
    ("What is the effect of pressure on liquid viscosity?",
     "It is slight at ordinary pressures, but becomes significant at very high pressure."),
    ("Why is a lubricating oil's viscosity index relevant to engine design?",
     "It determines how much the film thickness changes between cold start and hot operation."),
    ("What would a very low measured viscosity for a supposedly heavy oil indicate?",
     "Contamination with a lighter fraction, an error in temperature, or a wrong calibration constant."),
    ("Why is the jet cleaned with solvent rather than water?",
     "Water does not dissolve oil residues and may leave droplets that affect the flow."),
    ("What is the practical consequence of a tilted Redwood cup?",
     "The effective head changes, so the time and hence the viscosity are systematically shifted."),
    ("Why is viscosity described as a transport property?",
     "Because it governs the transport of momentum through the fluid."),
]

"""Chapter 9 - Viscosity of a lubricating oil by Redwood viscometer."""
from common import checklist

B = []

B += [
    ("h2", "9.1  Why viscosity is the number that matters for a lubricant"),
    ("lead", "A lubricant has one job: to keep two moving metal surfaces apart. It does that by being dragged into "
             "the gap and building up a pressure film, and the property that governs how easily it is dragged is "
             "viscosity. Too thin and the film collapses under load, giving metal-on-metal contact and wear. Too "
             "thick and the oil cannot circulate, pumping losses rise, and the machine runs hot. Viscosity is "
             "therefore not an abstract physical constant \u2014 it is the design parameter of the whole machine."),
    ("p", "The supplied material sets the aim as **determination of the viscosity of a given lubricating oil sample "
          "using a Redwood viscometer**, and states the working relation for the Redwood No. I instrument:"),
    ("eq", "\u03bd = 0.264t \u2212 190/t   (cSt)",
     "Equation 9.1 \u2014 the Redwood I conversion given in the supplied material, where t is the efflux time in "
     "seconds and \u03bd is the kinematic viscosity in centistokes. Valid over the instrument\u2019s normal working "
     "range of roughly 30\u20132000 s."),
    ("defbox", [
        ("Dynamic (absolute) viscosity \u03bc", "The internal resistance of a fluid to shear; SI unit Pa s "
                                               "(= 1 kg m^{\u22121} s^{\u22121}); the CGS unit is the poise (P), "
                                               "and 1 P = 0.1 Pa s, 1 cP = 1 mPa s."),
        ("Kinematic viscosity \u03bd", "Dynamic viscosity divided by density, \u03bd = \u03bc/\u03c1; SI unit "
                                       "m^{2} s^{\u22121}; the practical unit is the stoke (St) = 10^{\u22124} "
                                       "m^{2} s^{\u22121}, and 1 cSt = 1 mm^{2} s^{\u22121}."),
        ("Redwood second", "The empirical efflux time of 50 mL of oil through the standard Redwood jet at a "
                           "specified temperature; a convenience unit, not a physical constant."),
        ("Newtonian fluid", "One whose viscosity is independent of shear rate; mineral oils are approximately "
                            "Newtonian at ordinary conditions."),
        ("Viscosity index (VI)", "An empirical measure of how little the viscosity changes with temperature; a high "
                                 "VI means a flatter temperature dependence."),
        ("Pour point", "The lowest temperature at which the oil still flows under defined conditions."),
    ]),
    ("box", "key", [
        "**Kinematic viscosity is dynamic viscosity divided by density** \u2014 hence \u201ckinematic\u201d, because "
        "it has the units of diffusivity, not of force.",
        "**Efflux time \u2192 viscosity is a calibration, not a derivation.** The Redwood conversion is empirical; "
        "the instrument works because it was calibrated against absolute measurements.",
        "**Viscosity falls steeply with temperature** \u2014 roughly a factor of two to three for a 20 \u00b0C rise "
        "in a typical mineral oil \u2014 so the measurement temperature must always be stated.",
        "**1 cSt = 1 mm\u00b2 s\u207b\u00b9.** This identity is worth memorising; it makes the conversion between "
        "instrumental and SI units trivial.",
    ], "Four ideas that frame the experiment"),
    ("fig", "redwood", "**Figure 9.1** Redwood viscometer. The oil is held in a cup with a standard jet at the "
                       "bottom, brought to the measurement temperature in a surrounding bath, and allowed to flow "
                       "into a receiving flask until the 50 mL mark is reached. The efflux time is the raw "
                       "measurement."),
]

B += [
    ("h2", "9.2  Theory: Newton\u2019s law, and what the instrument actually measures"),
    ("h3", "9.2.1  Newton\u2019s law of viscosity"),
    ("p", "Consider a fluid between two parallel plates, one stationary and one moving with velocity u, separated by "
          "a gap y. The fluid adjacent to each plate sticks to it, so a velocity gradient u/y is set up. Newton\u2019s "
          "law states that the shear stress \u03c4 needed to maintain the motion is proportional to that "
          "gradient:"),
    ("eq", "\u03c4 = \u03bc (du/dy)",
     "Equation 9.2 \u2014 Newton\u2019s law of viscosity. The constant of proportionality \u03bc is the dynamic "
     "viscosity. Fluids obeying it at all shear rates are Newtonian."),
    ("p", "The SI unit follows immediately: \u03c4 in Pa (N m^{\u22122}) divided by du/dy in s^{\u22121} gives "
          "Pa s. The older CGS unit, the poise, is dyn s cm^{\u22122} = 0.1 Pa s. Water at 20 \u00b0C has "
          "\u03bc \u2248 1.00 mPa s = 1.00 cP, which is a useful benchmark: a lubricating oil may be 50 to 500 "
          "times more viscous."),
    ("h3", "9.2.2  Why kinematic viscosity is used"),
    ("p", "For flow driven by gravity \u2014 which is exactly what an efflux viscometer does \u2014 the driving force "
          "per unit volume is proportional to \u03c1g, while the resisting force is proportional to \u03bc. The "
          "ratio \u03bc/\u03c1 appears naturally:"),
    ("eq", "\u03bd = \u03bc/\u03c1",
     "Equation 9.3 \u2014 kinematic viscosity. Its unit is m^{2} s^{\u22121}; in the practical form 1 cSt = "
     "10^{\u22126} m^{2} s^{\u22121} = 1 mm^{2} s^{\u22121}."),
    ("p", "This is why viscometers of the efflux type report kinematic viscosity directly: the measurement "
          "integrates the balance between gravity and internal friction over the geometry of the jet, and density "
          "is already built in."),
    ("h3", "9.2.3  The Redwood relation"),
    ("p", "For an ideal capillary or jet, Poiseuille-type reasoning would give efflux time proportional to "
          "kinematic viscosity. Real instruments depart from this at short times because of kinetic-energy and "
          "surface-tension effects, so the calibration takes the empirical form:"),
    ("eq", "\u03bd (cSt) = 0.264t \u2212 190/t   for 40 s < t < 2000 s (Redwood I)",
     "Equation 9.4 \u2014 the same relation as Equation 9.1, written with its validity range. The 0.264 is the "
     "slope of the linear part; the \u2212190/t term corrects for the short-time departures."),
    ("box", "note", [
        "**Why is there a \u2212190/t term?** Because part of the driving head is spent accelerating the liquid and "
        "overcoming surface tension at the jet, and that fraction is proportionally larger when the efflux is fast. "
        "Empirically, the correction is inversely proportional to time. At t = 100 s the correction is 1.9 cSt; at "
        "t = 500 s it is only 0.38 cSt.",
        "**Outside the validity range, the formula stops being trustworthy.** Below about 40 s the efflux is too "
        "fast for the correction to work; above about 2000 s the flow may no longer be reproducible. If your time "
        "falls outside, use a different jet rather than extrapolating.",
    ], "Reading the empirical relation properly"),
    ("h3", "9.2.4  Temperature dependence"),
    ("p", "Viscosity is thermally activated: molecules need free volume to move past one another, and raising the "
          "temperature increases it. Over a limited range the dependence is approximately:"),
    ("eq", "\u03bc = A exp(E_{a}/RT)",
     "Equation 9.5 \u2014 an Arrhenius-type form, so a plot of ln \u03bc against 1/T is approximately linear. A "
     "typical mineral oil loses about half its viscosity for every 20\u201330 \u00b0C rise."),
    ("p", "This is precisely why the experiment is done in a thermostatted bath, and why a result quoted without a "
          "temperature is meaningless. In viva, expect the question \u201cwhy control the temperature?\u201d and "
          "answer it with numbers, not adjectives."),
    ("box", "exam", [
        "**Trap:** \u201cIs Redwood second a unit of viscosity?\u201d No \u2014 it is a unit of efflux //time// in a "
        "particular instrument. It correlates with viscosity only through a calibration.",
        "**Trap:** \u201cWhat is the difference between dynamic and kinematic viscosity?\u201d A factor of density. "
        "Ask which one the instrument reports, and why an efflux instrument reports the kinematic one.",
        "**Trap:** quoting a viscosity without temperature, or in the wrong unit. State both.",
    ], "Three marks lost by careless wording"),
]

B += [
    ("h2", "9.3  Apparatus"),
    ("tbl", ["Item", "Function", "If it is faulty"],
     [["Redwood viscometer (No. I)", "Holds the oil and provides the standard jet",
       "A worn or burred jet changes the efflux time permanently"],
      ["Thermostatted water bath with heater and stirrer", "Brings the oil to the measurement temperature",
       "Poor circulation means a temperature gradient and a drifting time"],
      ["Thermometer (0.1 \u00b0C)", "Reads the oil temperature", "A slow or offset thermometer biases the result"],
      ["Receiving flask with a 50 mL mark", "Defines the volume collected", "A wrong mark scales the time wrongly"],
      ["Stopwatch", "Times the efflux", "Reaction-time error is significant for short effluxes"],
      ["Levelling screws / spirit level", "Ensures a vertical jet", "A tilted instrument changes the driving head"],
      ["Solvent and lint-free tissue", "Cleans the cup and jet between runs",
       "Residue alters the jet and the next reading"],
      ["Sample oil", "The analyte", "A wet or contaminated sample will not be reproducible"]],
     [50, 58, 62], "**Table 9.1** Apparatus.", ["l", "l", "l"]),
    ("box", "warn", [
        "The bath contains hot water and the cup contains hot oil; both can scald. Handle the cup with tongs or a "
        "cloth, keep the bath below boiling, and never fill the cup above the specified mark. Clean up spills "
        "immediately \u2014 an oil film on the floor is a slip hazard. Dispose of used oil through the approved "
        "waste route, not down the sink.",
    ], "Handling"),
]

B += [
    ("h2", "9.4  Procedure with reasoning"),
    ("num", [
        "**Level the instrument** with the spirit level and check that the jet is vertical. Gravity is the driving "
        "force; a tilted jet changes the head and therefore the time.",
        "**Clean and dry the cup and jet** with solvent. Any residue narrows the jet and lengthens the efflux.",
        "**Fill the cup to the specified level** with the oil sample, avoiding bubbles. Bubbles reduce the effective "
        "volume and make the efflux erratic.",
        "**Set the bath to the required temperature** (typically 40 \u00b0C or 100 \u00b0C for lubricating oils) and "
        "allow the oil to reach it. Thermal equilibration may take 15\u201320 minutes; a thermometer in the oil, not "
        "in the bath, is the check.",
        "**Place the receiving flask under the jet** with the 50 mL mark visible.",
        "**Lift the stopper/ball valve and start the stopwatch simultaneously.** The start is the moment flow "
        "begins, not the moment you decide to press the button.",
        "**Stop the watch when the receiving flask reaches the 50 mL mark**, and close the valve.",
        "**Record the time and the temperature**, then repeat until you have concordant readings, cleaning between "
        "runs.",
        "**Repeat at a second temperature** if the manual requires a temperature\u2013viscosity comparison.",
        "**Convert the mean time** with Equation 9.1 and report the viscosity with its temperature.",
    ]),
    ("box", "pitfall", [
        "**Timing is the dominant random error.** For a 60 s efflux, a 0.3 s reaction-time error is 0.5 %; for a "
        "20 s efflux it is 1.5 %, and the instrument is out of range anyway. Use the same operator, the same "
        "technique, and the same criterion for \u201cfull\u201d.",
        "**The temperature is the dominant systematic error.** A 1 \u00b0C error near 40 \u00b0C changes the "
        "viscosity of a typical oil by roughly 3\u20135 %. No amount of averaging repeats will recover it.",
    ], "Where the error actually lives"),
]

B += [
    ("h2", "9.5  Observations and calculation"),
    ("tbl", ["S. No.", "Oil temperature (\u00b0C)", "Efflux time t (s)", "Mean t (s)", "Remark"],
     [["1", "", "", "", ""], ["2", "", "", "", ""], ["3", "", "", "", ""]],
     [14, 34, 32, 26, 56], "**Table 9.2** Observation table. Blank because the supplied sheet contains no "
                           "completed readings.", ["c", "c", "c", "c", "l"]),
    ("h3", "9.5.1  Worked illustration"),
    ("p", "Suppose the mean efflux time at 40 \u00b0C is 285 s:"),
    ("eq", "\u03bd = 0.264 \u00d7 285 \u2212 190/285 = 75.24 \u2212 0.667 = 74.6 cSt"),
    ("p", "A kinematic viscosity of about 75 cSt at 40 \u00b0C corresponds to an ISO VG 68 oil, which is a common "
          "hydraulic and gear lubricant grade. The result is therefore plausible, which is itself part of the "
          "answer \u2014 always ask whether the magnitude makes sense for the sample you were given."),
    ("p", "To convert to dynamic viscosity you need the density at the same temperature:"),
    ("eq", "\u03bc = \u03bd\u03c1 = 74.6 \u00d7 10^{\u22126} m^{2} s^{\u22121} \u00d7 880 kg m^{\u22123} = "
           "0.0656 Pa s = 65.6 mPa s",
     "With a typical mineral-oil density of about 880 kg m^{\u22123} at 40 \u00b0C. Note how the unit conversion "
     "works: cSt \u00d7 10^{\u22126} gives m^{2} s^{\u22121}, and multiplying by kg m^{\u22123} gives Pa s."),
    ("tbl", ["Quantity", "Expression", "Illustrative value"],
     [["Mean efflux time", "from observations", "285 s"],
      ["Linear term", "0.264t", "75.24 cSt"],
      ["Correction term", "190/t", "0.667 cSt"],
      ["Kinematic viscosity", "0.264t \u2212 190/t", "74.6 cSt"],
      ["Density at 40 \u00b0C", "from tables or measurement", "880 kg m^{\u22123}"],
      ["Dynamic viscosity", "\u03bd\u03c1", "0.0656 Pa s"],
      ["Likely ISO grade", "by comparison with the VG table", "ISO VG 68"],
      ["Validity check", "40 s < t < 2000 s", "285 s \u2713"]],
     [44, 62, 62], "**Table 9.3** Calculation chain, including the validity check.", ["l", "l", "c"]),
    ("tbl", ["Temperature (\u00b0C)", "Efflux time (s)", "\u03bd (cSt)", "Remark"],
     [["", "", "", ""], ["", "", "", ""], ["", "", "", ""]],
     [34, 36, 34, 56], "**Table 9.4** Temperature\u2013viscosity table, for the second part of the experiment "
                       "where two temperatures are compared.", ["c", "c", "c", "l"]),
]

B += [
    ("h2", "9.6  Precautions, errors and troubleshooting"),
    ("bul", [
        "Level the instrument and verify the vertical jet before every session.",
        "Clean and dry the cup and jet between runs; oil residue is cumulative.",
        "Fill to the mark consistently and avoid bubbles.",
        "Allow full thermal equilibration; measure the oil temperature, not the bath temperature.",
        "Use the same operator and the same full-mark criterion for all repeats.",
        "Never reuse oil that has been heated repeatedly; it oxidises and thickens.",
        "Keep the bath stirred; a stratified bath gives drifting times.",
        "Record every time, including rejected runs, and say why they were rejected.",
    ]),
    ("tbl", ["Source of error", "Type", "Effect on the result", "Control"],
     [["Temperature error", "Systematic", "3\u20135 % per \u00b0C; larger than any other single effect",
       "Thermostat; measure the oil temperature"],
      ["Reaction time in starting/stopping", "Random", "Under- or overestimates t", "Same operator; practice"],
      ["Dirty jet", "Systematic (positive)", "Longer efflux, higher viscosity", "Solvent clean between runs"],
      ["Tilted instrument", "Systematic", "Changed driving head", "Level with the spirit level"],
      ["Incomplete draining to the mark", "Random", "Scatter between repeats", "Consistent endpoint criterion"],
      ["Bubbles in the oil", "Random", "Erratic efflux", "Allow the sample to settle"],
      ["Oil degradation from repeated heating", "Systematic (positive)", "Rising viscosity", "Fresh sample"],
      ["Extrapolating outside 40\u20132000 s", "Systematic", "Unquantifiable error", "Change jet or instrument"]],
     [50, 26, 48, 48], "**Table 9.5** Error budget.", ["l", "l", "l", "l"]),
    ("tbl", ["Symptom", "Likely cause", "Action"],
     [["Efflux time varies widely between repeats", "Temperature drift, bubbles, or incomplete filling",
       "Re-equilibrate, degas, refill carefully"],
      ["Efflux time is far too short", "Jet too large for the oil, or oil too hot", "Check the jet size and the "
       "temperature"],
      ["Efflux time is very long or flow stops", "Oil too cold, jet blocked, or oil congealed", "Raise the "
       "temperature; clean the jet"],
      ["Bubbles appear in the receiving flask", "Air entrainment from the jet", "Degas the sample; pour slowly"],
      ["Calculated viscosity is negative", "t below the valid range (the 190/t term dominates)", "Do not use the "
       "formula there; change jet"]],
     [46, 58, 66], "**Table 9.6** Troubleshooting chart.", ["l", "l", "l"]),
]

VIVA_A = [
    ("Define viscosity.", "The internal resistance of a fluid to flow, or more precisely to shear."),
    ("State Newton\u2019s law of viscosity.", "\u03c4 = \u03bc (du/dy); the shear stress is proportional to the "
                                             "velocity gradient."),
    ("What is dynamic viscosity, and its units?", "The proportionality constant \u03bc; SI unit Pa s, CGS unit "
                                                  "poise, practical unit cP = mPa s."),
    ("What is kinematic viscosity, and its units?", "\u03bd = \u03bc/\u03c1; SI unit m^{2} s^{\u22121}, practical "
                                                    "unit stoke, with 1 cSt = 1 mm^{2} s^{\u22121}."),
    ("Why does an efflux viscometer report kinematic viscosity?", "Because in gravity-driven flow the driving force "
                                                                  "scales with density while the resistance scales "
                                                                  "with dynamic viscosity; the ratio is built into "
                                                                  "the measurement."),
    ("What is a Redwood second?", "The time for 50 mL of oil to flow through the standard Redwood jet at a "
                                  "specified temperature."),
    ("Write the Redwood I conversion.", "\u03bd = 0.264t \u2212 190/t cSt."),
    ("What does the \u2212190/t term correct for?", "Deviations from linearity at short efflux times, arising from "
                                                    "kinetic-energy and surface-tension effects."),
    ("What is the working range of the Redwood I?", "Roughly 40\u20132000 s of efflux time."),
    ("Why is the temperature controlled?", "Because viscosity depends strongly and non-linearly on temperature; "
                                           "without control the result is not a property of the oil."),
    ("How strongly does viscosity depend on temperature?", "Roughly halving for every 20\u201330 \u00b0C rise, for "
                                                           "a typical mineral oil; the Arrhenius form describes "
                                                           "it."),
    ("What is a Newtonian fluid?", "One whose viscosity does not depend on shear rate at a given temperature."),
    ("What is the viscosity index?", "An empirical number describing how little viscosity changes with "
                                     "temperature; higher means flatter."),
    ("What is the pour point?", "The lowest temperature at which the oil flows under defined conditions."),
    ("Why are oils graded by viscosity?", "Because the film thickness a lubricant can sustain depends primarily on "
                                          "its viscosity at the operating temperature."),
    ("What is 1 poise in SI units?", "0.1 Pa s."),
    ("What is the viscosity of water at 20 \u00b0C, approximately?", "1.0 mPa s = 1.0 cP."),
    ("Why must the receiving flask have a 50 mL mark?", "The method is defined on a 50 mL efflux volume; changing "
                                                        "the volume changes the time."),
    ("Why is the jet standardized?", "Because the efflux time depends on the jet geometry, so the calibration is "
                                     "only valid for the specified dimensions."),
    ("State two applications of viscosity measurement.", "Oil grade verification and quality control; lubricant "
                                                         "selection for machinery."),
    ("What is the difference between saybolt and redwood?", "Both are efflux viscometers with different standard "
                                                            "geometries and empirical conversions."),
    ("Why is viscosity important in pipeline design?", "It sets the pressure drop for a given flow rate, and "
                                                       "therefore the pumping power."),
    ("What happens to too-thin oil in a bearing?", "The film cannot support the load, giving boundary contact, "
                                                   "wear, and heat."),
    ("What happens with too-thick oil?", "Higher pumping losses, poorer circulation and heat removal, and starved "
                                         "supply to tight clearances."),
]

VIVA_B = [
    ("Why level the instrument?", "The driving head is gravitational; a tilted cup changes it and thus the efflux "
                                  "time."),
    ("Why clean the jet?", "Residue narrows the bore, increasing the time and therefore the calculated viscosity."),
    ("Why must the oil reach the bath temperature before the run?", "Because the measurement must be made at a "
                                                                    "known, uniform temperature; the oil, not the "
                                                                    "bath, is the thermometric object."),
    ("Why degas the sample?", "Bubbles reduce the effective volume and make the flow irregular, adding scatter."),
    ("Why must the same operator take all readings?", "Reaction time is a personal systematic error; varying it "
                                                      "converts a bias into scatter."),
    ("Why fill to a fixed mark?", "The efflux time depends on the head, which depends on the fill level."),
    ("Why is the oil not reused indefinitely?", "Repeated heating oxidises the oil, raising its viscosity and "
                                                "changing the result."),
    ("Why is the bath stirred?", "To eliminate temperature stratification; an unstirred bath gives a drift that "
                                 "looks like instrument instability."),
    ("Why does the efflux slow down as the cup empties?", "Because the driving head decreases as the level falls; "
                                                          "the standard geometry accounts for this, which is why "
                                                          "the volume collected is fixed."),
    ("Why does the calibration become invalid at low efflux times?", "Because the short-time corrections become "
                                                                    "comparable to the linear term, and the "
                                                                    "empirical form is no longer valid."),
    ("Why do we quote cSt and not Pa s in practice?", "Because efflux instruments measure kinematic viscosity, and "
                                                      "because cSt values are convenient numbers for oils."),
    ("How would you convert cSt to mPa s?", "Multiply by the density in g cm^{\u22123} (equivalently, divide by "
                                            "1000 and multiply by density in kg m^{\u22123})."),
    ("Why does viscosity affect the film thickness in a bearing?", "In hydrodynamic lubrication the film thickness "
                                                                   "scales with viscosity and speed and inversely "
                                                                   "with load."),
    ("Why is a viscosity\u2013temperature curve more useful than a single value?", "Because machines operate over a "
                                                                                  "temperature range; the curve "
                                                                                  "shows how the film behaves "
                                                                                  "throughout it."),
]

VIVA_C = [
    ("What if the efflux time were 25 s?", "The instrument is outside its valid range; the \u2212190/t correction "
                                           "becomes large and unreliable, so a smaller jet or a more viscous sample "
                                           "is needed."),
    ("What if the bath were 3 \u00b0C too hot?", "The viscosity would be substantially underestimated \u2014 "
                                                "perhaps by 10\u201315 % \u2014 and the error would not be visible "
                                                "in the repeatability."),
    ("What if you forgot to level the instrument?", "The head would change, shifting the time systematically; the "
                                                    "result would be biased but reproducible."),
    ("What if the oil contained water droplets?", "The emulsion would have a different, erratic viscosity and the "
                                                  "flow would be unstable."),
    ("What if you collected 60 mL instead of 50 mL?", "The time would correspond to a larger volume, so the "
                                                      "viscosity would be overestimated by roughly 20 % if you used "
                                                      "the 50 mL calibration."),
    ("What if the calculated viscosity came out negative?", "The time must be below about 27 s, where 0.264t < "
                                                            "190/t; the reading is invalid, not the oil."),
    ("What if the jet were partly blocked?", "The efflux would be slow and the viscosity overestimated; cleaning "
                                             "restores it."),
    ("What if two operators took the start and stop readings?", "Their differing reaction times add systematic "
                                                                "error at both ends; a single operator is "
                                                                "preferred."),
    ("What if the oil were measured at 100 \u00b0C?", "It is a valid alternative measurement point, but the value "
                                                     "must be reported at that temperature \u2014 it will be far "
                                                     "lower than at 40 \u00b0C."),
    ("What if the sample were a non-Newtonian grease?", "The efflux method would be inappropriate; the result would "
                                                        "depend on shear rate and would not be a material "
                                                        "constant."),
]

VIVA_D = [
    ("Derive the units of kinematic viscosity.", "\u03bd = \u03bc/\u03c1 gives (Pa s)/(kg m^{\u22123}) = "
                                                 "(kg m^{\u22121} s^{\u22121})/(kg m^{\u22123}) = m^{2} "
                                                 "s^{\u22121}."),
    ("Why is the Redwood relation empirical rather than derived from Poiseuille flow?", "Because the geometry is a "
                                                                                       "short jet with entrance and "
                                                                                       "exit effects, not a long "
                                                                                       "capillary, so the ideal "
                                                                                       "Hagen\u2013Poiseuille result "
                                                                                       "does not apply and the "
                                                                                       "calibration is fitted to "
                                                                                       "absolute measurements."),
    ("How would you determine the dynamic viscosity without measuring density?", "You cannot \u2014 dynamic "
                                                                                 "viscosity requires density, by "
                                                                                 "definition. Measure it with a "
                                                                                 "pycnometer or hydrometer at the "
                                                                                 "same temperature."),
    ("What is the physical origin of the temperature dependence of viscosity?", "Molecular mobility: flow requires "
                                                                                "free volume and the ability to "
                                                                                "overcome intermolecular "
                                                                                "attractions, both of which improve "
                                                                                "as temperature rises."),
    ("Why does an oil\u2019s viscosity index matter for a multigrade engine oil?", "Because the oil must be thin "
                                                                                  "enough to crank when cold and "
                                                                                  "thick enough to protect when hot; "
                                                                                  "a high VI narrows that spread."),
    ("What is the difference between viscosity and consistency?", "Viscosity is a well-defined material property "
                                                                  "for Newtonian fluids; consistency describes "
                                                                  "semi-solids such as greases and depends on shear "
                                                                  "history."),
    ("How would you obtain the activation energy from your data?", "Measure \u03bd at several temperatures, plot ln "
                                                                   "\u03bd against 1/T, and take the slope as "
                                                                   "\u2212E_{a}/R."),
    ("Why do we speak of \u201cviscosity at 40 \u00b0C\u201d and \u201cat 100 \u00b0C\u201d in oil specifications?",
     "Because those two temperatures bracket the range in which engines and machines actually operate, and together "
     "they define the VI."),
    ("What limits the accuracy of an efflux viscometer?", "Timing reaction, temperature uniformity, jet condition, "
                                                          "and the empirical nature of the conversion \u2014 in "
                                                          "that order."),
    ("Can viscosity be measured without a viscometer?", "Yes \u2014 from the terminal velocity of a falling sphere "
                                                        "(Stokes\u2019 law), from pressure drop in a capillary, or "
                                                        "from the damping of a vibrating element; each relies on a "
                                                        "different flow geometry."),
]

CH9_CHECK = checklist(
    "9.8",
    ["\u03c4 = \u03bc(du/dy) is Newton\u2019s law of viscosity.",
     "Dynamic viscosity: Pa s (SI), poise (CGS), cP = mPa s.",
     "Kinematic viscosity \u03bd = \u03bc/\u03c1, in m^{2} s^{\u22121} or cSt.",
     "1 cSt = 1 mm^{2} s^{\u22121}.",
     "Redwood second is an efflux time, not a viscosity unit.",
     "Redwood I: \u03bd = 0.264t \u2212 190/t cSt.",
     "Valid range roughly 40\u20132000 s.",
     "The \u2212190/t term corrects short-time departures.",
     "Efflux instruments measure kinematic viscosity.",
     "Viscosity falls steeply with temperature; about half per 20\u201330 \u00b0C.",
     "Temperature control is the dominant systematic error.",
     "Level the instrument and keep the jet vertical.",
     "Clean the jet between runs.",
     "Fill to a fixed mark and avoid bubbles.",
     "Use one operator for start and stop.",
     "Report viscosity with its temperature and unit.",
     "Convert cSt to mPa s by multiplying by density in g cm^{\u22123}.",
     "Water at 20 \u00b0C is about 1.0 mPa s.",
     "A negative calculated viscosity means the reading is out of range.",
     "Repeatedly heated oil oxidises and thickens."],
    ["Define dynamic and kinematic viscosity, with units.",
     "State Newton\u2019s law of viscosity.",
     "What does a Redwood second measure?",
     "Write the Redwood I conversion.",
     "What does the \u2212190/t term represent?",
     "Why is temperature controlled?",
     "Why is the jet vertical?",
     "Why must the oil be degassed?",
     "What is the viscosity index?",
     "How would you convert cSt to Pa s?"],
    ["Derive the SI unit of kinematic viscosity from \u03bd = \u03bc/\u03c1.",
     "Explain why the Redwood relation is empirical, invoking the geometry of the flow.",
     "A 285 s efflux gives what viscosity, and which ISO grade does that suggest?",
     "Show numerically how the correction term shrinks as t grows, and what that implies.",
     "Estimate the error in reported viscosity for a 1 \u00b0C temperature error near 40 \u00b0C.",
     "Compare efflux, falling-sphere and capillary viscometers.",
     "Why is it wrong to quote a viscosity without a temperature?",
     "How would you extract an activation energy from \u03bd(T) data?",
     "Explain the role of viscosity in hydrodynamic lubrication.",
     "What would you do if your efflux time were 20 s?"],
    [("Dynamic vs kinematic", "A factor of density."),
     ("Poise vs Pa s", "1 P = 0.1 Pa s."),
     ("cSt vs mm\u00b2 s\u207b\u00b9", "Identical."),
     ("Redwood second vs cSt", "Time vs viscosity; linked by calibration."),
     ("Newtonian vs non-Newtonian", "Shear-independent vs shear-dependent."),
     ("Viscosity vs consistency", "Defined property vs shear-history-dependent behaviour."),
     ("Absolute vs empirical measurement", "Fundamental geometry vs calibrated instrument."),
     ("Viscosity index vs grade", "Temperature sensitivity vs nominal viscosity class.")],
    (["Relation", "Expression", "Note"],
     [["Newton\u2019s law", "\u03c4 = \u03bc(du/dy)", "Defines \u03bc"],
      ["Kinematic viscosity", "\u03bd = \u03bc/\u03c1", "m^{2} s^{\u22121} or cSt"],
      ["Redwood I", "\u03bd = 0.264t \u2212 190/t", "40\u20132000 s"],
      ["Unit identity", "1 cSt = 1 mm^{2} s^{\u22121}", "Memorise"],
      ["Unit identity", "1 P = 0.1 Pa s", "CGS to SI"],
      ["Unit identity", "1 cP = 1 mPa s", "Water \u2248 1 cP"],
      ["Temperature dependence", "\u03bc = A exp(E_{a}/RT)", "Arrhenius form"],
      ["Conversion", "\u03bc (mPa s) = \u03bd (cSt) \u00d7 \u03c1 (g cm^{\u22123})", "At the same temperature"]],
     [42, 74, 52]),
    [["Wide scatter between repeats", "Temperature drift, bubbles, or inconsistent filling"],
     ["Efflux far too short", "Jet too large or oil too hot"],
     ["Flow very slow or stops", "Oil cold, jet blocked, or oil congealed"],
     ["Negative calculated viscosity", "Efflux below the valid range"],
     ["Reproducible but consistently wrong", "Level, jet condition or calibration"],
     ["Viscosity increases run by run", "Oil oxidising from repeated heating"],
     ["Bubbles in the receiving flask", "Air entrainment at the jet"]],
    ["Efflux time is not viscosity; the calibration converts one to the other.",
     "\u03bd = \u03bc/\u03c1, and 1 cSt = 1 mm\u00b2 s\u207b\u00b9.",
     "Temperature is the dominant systematic error, not timing.",
     "The \u2212190/t term is why the range is limited.",
     "Level, clean, degas, equilibrate \u2014 in that order.",
     "Always report the temperature with the value.",
     "Check the magnitude against a plausible oil grade."],
    ["Quoting a viscosity without its temperature.",
     "Using the Redwood formula for a 20 s efflux.",
     "Treating a Redwood second as a viscosity unit.",
     "Filling to an arbitrary level.",
     "Using oil that has been heated many times.",
     "Ignoring a bubble in the cup.",
     "Confusing cSt with cP."],
    ["The Redwood viscometer measures the time for 50 mL of oil to flow through a standard jet at a controlled "
     "temperature, and this efflux time is converted to kinematic viscosity by the empirical relation \u03bd = 0.264t "
     "\u2212 190/t centistokes, valid from about 40 to 2000 seconds. I level the instrument, clean and dry the cup "
     "and jet, fill to the specified mark with degassed oil, and bring the oil to the bath temperature, checking "
     "with a thermometer in the oil. I then release the flow and start the stopwatch together, stop it at the 50 mL "
     "mark, and repeat until the times are concordant. The reason an efflux instrument reports kinematic and not "
     "dynamic viscosity is that gravity drives the flow, so density is already part of the measurement; dynamic "
     "viscosity is obtained by multiplying by density. The critical controls are temperature \u2014 a one-degree "
     "error shifts the answer by several percent \u2014 a clean jet, a vertical instrument, and consistent timing by "
     "one operator. The result must be reported with its temperature and unit, and checked against a plausible oil "
     "grade."],
    ["**Efflux time \u2192 viscosity only through the calibration.**",
     "**\u03bd = \u03bc/\u03c1; 1 cSt = 1 mm\u00b2 s\u207b\u00b9.**",
     "**Temperature dominates the error budget.**",
     "**Outside 40\u20132000 s the formula lies.**"]
)

CH9 = {
    "key": "viscosity",
    "num": "9",
    "kicker": "Experiment 9  \u00b7  Petroleum testing",
    "title": "Viscosity of a Lubricating Oil by Redwood Viscometer",
    "toc": "Viscosity of lubricating oil",
    "standfirst": "A simple instrument whose simplicity is deceptive: the measurement is a time, but the answer "
                  "depends on temperature, geometry and calibration in ways the stopwatch cannot reveal.",
    "body": B + [
        ("h2", "9.7  Viva question bank"),
        ("p", "Seventy-eight answered questions, including the derivation of the units, the reason for the empirical "
              "conversion, and the temperature dependence that dominates the error budget."),
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
    ] + CH9_CHECK,
}
