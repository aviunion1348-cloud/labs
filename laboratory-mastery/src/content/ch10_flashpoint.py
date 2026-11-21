VIVA_E = [
    ("Why is the cup fitted with a stirrer rather than being shaken?",
     "Shaking would splash liquid into the vapour space and give a false flash; stirring keeps the temperature "
     "uniform without disturbance."),
    ("Why does the shutter open only briefly?",
     "Prolonged opening lets vapour escape and cools the vapour space, changing the conditions for later tests."),
    ("What is the effect of a strong draught on the reading?",
     "It disperses vapour and can also deflect the flame, giving erratic and usually high readings."),
    ("Why are samples with very low flash points excluded from this apparatus?",
     "They would form an ignitable atmosphere below ambient temperature, creating an immediate hazard."),
    ("Why must the thermometer be positioned precisely?",
     "Because the recorded temperature must represent the bulk liquid, not the headspace or the wall."),
    ("What is the significance of a flash point that is lower on a repeat run?",
     "Volatile components may have been lost from the first run, or the second run may have been contaminated."),
    ("Why is the fire point less reproducible than the flash point?",
     "Because it depends on sustained burning, which is harder to judge and depends on the vapour generation rate."),
    ("Why does a water content raise the apparent flash point?",
     "Water vapour dilutes the fuel vapour, so a higher temperature is required to reach the flammable "
     "concentration."),
    ("How does an increase in molecular mass affect the flash point?",
     "It lowers the vapour pressure, so the flash point rises."),
    ("Why do branched alkanes usually flash lower than straight-chain isomers?",
     "Branching lowers intermolecular attraction and raises the vapour pressure."),
    ("Why is the flash point of a mixture not the average of its components?",
     "The more volatile component dominates the vapour composition, so the mixture flashes near the lower value."),
    ("What does a small flash-fire gap suggest?",
     "That the flash point was recorded late, near the fire point, or that the sample is highly volatile."),
    ("What is the function of the lid in a Pensky\u2013Martens cup?",
     "It retains vapour and houses the shutter and the ignition device."),
    ("Why should the apparatus be allowed to cool before cleaning?",
     "Hot solvent and residual vapour create a fire risk, and thermal shock can damage the cup."),
    ("How would an examiner test whether you know the difference between flash and fire point?",
     "By asking what happens after the flash \u2014 whether the flame merely pops or continues to burn."),
    ("Why is the closed-cup value used in transport regulations?",
     "Because transport involves closed containers, so the closed-cup value reflects the realistic hazard."),
    ("What is the flash point of a mixture of diesel and petrol likely to be?",
     "Substantially lower than neat diesel, close to the petrol component \u2014 which is why contamination is a "
     "serious safety issue."),
    ("Why is the method specified to a particular standard, such as a national or international standard?",
     "Because the result is defined by the method, so comparability between laboratories requires identical "
     "procedure."),
    ("What is the effect of a dirty cup on repeatability?",
     "Residues alter the vapour composition and can catalyse ignition, so results become erratic."),
    ("Why is the fire point of a lubricating oil rarely quoted in specifications?",
     "Because the flash point already characterises the volatile hazard, and the fire point adds little practical "
     "information."),
]

"""Chapter 10 - Flash point and fire point by Pensky-Martens apparatus."""
from common import checklist

B = []

B += [
    ("h2", "10.1  The temperature at which a fuel becomes a hazard"),
    ("lead", "Every flammable liquid has a temperature below which its vapour pressure is too low to form an "
             "ignitable mixture in air, and above which it is not. That temperature is the flash point, and it "
             "determines how a fuel may be stored, transported, labelled and insured. It is one of the few "
             "laboratory measurements whose result is written directly into law."),
    ("p", "The supplied material sets the aim as **determination of flash point and fire point of a given "
          "lubricating oil / fuel sample by Pensky\u2013Martens apparatus**. The observation sheet records the "
          "flash point as the temperature at which a test flame causes a distinct flash in the cup, and the fire "
          "point as the higher temperature at which the vapour continues to burn for at least five seconds."),
    ("defbox", [
        ("Flash point", "The lowest temperature at which a liquid gives off enough vapour to form an ignitable "
                        "mixture with air near its surface, so that a flame applied briefly causes a flash."),
        ("Fire point", "The higher temperature at which the vapour ignites and continues to burn for at least five "
                       "seconds after the ignition source is removed."),
        ("Closed cup", "The sample is enclosed so that vapour is retained; measures the flash point under "
                       "conditions resembling a closed container. Pensky\u2013Martens is a closed-cup method."),
        ("Open cup", "The sample is exposed; vapour escapes, so the measured flash point is higher. Cleveland and "
                     "Abel apparatus are open-cup examples."),
        ("Autoignition temperature", "The temperature at which a substance ignites spontaneously without an "
                                     "external ignition source \u2014 always well above the fire point."),
        ("Flammable limits (LEL/UEL)", "The concentration range of vapour in air within which ignition is possible "
                                       "\u2014 a reminder that vapour concentration, not only temperature, matters."),
    ]),
    ("box", "key", [
        "**Closed cup gives the lower, more conservative value.** Vapour is retained, so the ignitable mixture forms "
        "at a lower temperature than in an open cup. Regulations refer to closed-cup values unless stated otherwise.",
        "**Flash point is not a boiling point.** A liquid can have a flash point of 60 \u00b0C and a boiling point of "
        "200 \u00b0C; the flash point simply marks where sufficient vapour exists above the surface.",
        "**Stirring and heating rate are part of the method**, not optional extras: a different rate gives a "
        "different number.",
        "**Fire point is typically 20\u201360 \u00b0C above the flash point** for the same sample, and it is a much "
        "less sharply defined measurement.",
    ], "Four ideas that define the experiment"),
    ("fig", "pensky", "**Figure 10.1** Pensky\u2013Martens closed-cup apparatus. The sample is heated in a covered "
                      "cup with a stirrer; at each test temperature the shutter is opened briefly and a small pilot "
                      "flame is dipped into the vapour space. A flash is recorded as the flash point."),
]

B += [
    ("h2", "10.2  Theory: vapour pressure, and why a flash happens"),
    ("h3", "10.2.1  Vapour pressure and the ignition condition"),
    ("p", "A liquid in a closed space establishes an equilibrium with its own vapour, and the partial pressure of "
          "that vapour depends strongly on temperature. Ignition requires the vapour concentration in air above the "
          "liquid to lie between the lower and upper flammable limits. As the liquid is heated, its vapour pressure "
          "and hence its concentration rise; the temperature at which the concentration first enters the flammable "
          "range is, by definition, the flash point."),
    ("eq", "ln(P_{sat}) \u2248 A \u2212 B/T   (Clausius\u2013Clapeyron form)",
     "Equation 10.1 \u2014 vapour pressure rises roughly exponentially with temperature, so the approach to the "
     "flash point is steep and the flash is abrupt rather than gradual."),
    ("p", "This steepness is the practical reason flash point can be measured with a few degrees of resolution: the "
          "vapour concentration changes very quickly in the neighbourhood of the flash temperature, so the flame "
          "either does nothing or gives a clear pop."),
    ("h3", "10.2.2  Closed cup versus open cup"),
    ("p", "In a closed cup the vapour space above the sample is enclosed, so equilibrium vapour concentration builds "
          "up and the flash occurs at the temperature at which that concentration reaches the lower flammable limit. "
          "In an open cup, vapour continuously diffuses away, so the same sample requires a higher temperature to "
          "support an ignitable mixture. For many petroleum products the open-cup value is roughly 5\u201320 \u00b0C "
          "higher than the closed-cup value."),
    ("tbl", ["Method", "Type", "Typical use", "Result relative to the other"],
     [["Pensky\u2013Martens", "Closed cup", "Lubricating oils, fuel oils, bituminous materials", "Lower"],
      ["Abel", "Closed cup", "Low-flash-point solvents and kerosene", "Lower"],
      ["Tag", "Closed cup (small)", "Paints, thinners, low-viscosity solvents", "Lower"],
      ["Cleveland", "Open cup", "Asphalt, fuel oils, lubricants above 79 \u00b0C", "Higher"],
      ["Setaflash", "Closed cup (small, rapid)", "Rapid screening, small samples", "Lower"]],
     [36, 40, 68, 40], "**Table 10.1** The main flash-point methods. The two columns that matter in an examination "
                       "are the type and the relative value.", ["l", "l", "l", "l"]),
    ("h3", "10.2.3  What the flash point tells you about a product"),
    ("p", "Flash point is a purity and safety indicator with two distinct uses. In a //fuel//, it distinguishes "
          "grades: diesel with a flash point below the specification limit indicates contamination with a lighter "
          "fraction. In a //lubricant//, a low flash point is a warning that the oil contains light ends that will "
          "volatilise in service, leading to thickening and oil consumption."),
    ("p", "This is why the supplied material\u2019s instruction to record the //smell and appearance// is not "
          "decoration: a kerosene-like smell with a low flash point tells a coherent story."),
    ("box", "exam", [
        "**Trap:** \u201cIs the fire point always measured?\u201d No \u2014 it is a secondary observation. The flash "
        "point is the regulated number; the fire point is recorded when the method calls for it.",
        "**Trap:** \u201cDoes a higher flash point mean a safer fuel?\u201d Usually, but not automatically safer "
        "overall: high flash point can mean the liquid is less volatile and therefore harder to ignite, while a low "
        "flash point also means a higher vapour hazard at ambient temperature. Both directions carry risk.",
        "**Trap:** confusing flash point with autoignition temperature. A diesel engine relies on the latter; a "
        "storage tank is governed by the former.",
    ], "Three source of confusion"),
]

B += [
    ("h2", "10.3  Apparatus"),
    ("tbl", ["Item", "Function", "If it is faulty"],
     [["Pensky\u2013Martens closed cup", "Holds the sample and contains the vapour", "A damaged lid or gasket "
       "leaks vapour and raises the measured flash point"],
      ["Heater with control", "Raises the sample temperature at the specified rate", "An uncontrolled rate "
       "invalidates the result"],
      ["Stirrer (motor driven)", "Homogenises the sample temperature", "Poor stirring gives local hot spots and an "
       "early flash"],
      ["Thermometer (as specified)", "Reads the sample temperature", "A slow or offset thermometer biases the "
       "temperature at which the flash is recorded"],
      ["Ignition flame (small, specified size)", "Initiates ignition", "An oversized flame gives a premature "
       "reading"],
      ["Shutter mechanism", "Opens the vapour space to the test flame only briefly", "Jamming changes the vapour "
       "loss and the reading"],
      ["Timer / stopwatch", "Controls the heating rate and test interval", "Irregular intervals scatter the "
       "results"],
      ["Solvent, tissue", "Cleaning the cup", "Residue from the previous sample contaminates and shifts the "
       "reading"]],
     [48, 58, 64], "**Table 10.2** Apparatus. The supplied source does not specify the heating rate, the stirring "
                   "rate or the test interval; these are method parameters and must be taken from the instrument "
                   "manual or the relevant standard.", ["l", "l", "l"]),
    ("box", "source", [
        "The supplied material names the apparatus and the quantities to record, but **does not state the heating "
        "rate, the stirring rate or the temperature interval between flame applications.** Those three numbers are "
        "part of the method and they change the answer, so they are recorded here as a gap in the source rather "
        "than invented. Use the rate printed on your instrument or in the standard your course follows.",
    ], "A genuine gap in the source"),
    ("box", "warn", [
        "This experiment deliberately creates an ignitable vapour and applies a flame to it. Keep the apparatus "
        "under an extractor hood, keep all other flames and hot surfaces away, and make sure a fire extinguisher "
        "and fire blanket are within reach. Never overfill the cup, never leave the apparatus unattended while "
        "heating, and never lean over the cup while the flame is applied. Treat any unexpected sustained burning as "
        "an incident, not an observation.",
    ], "Fire hazard \u2014 read before starting"),
]

B += [
    ("h2", "10.4  Procedure with reasoning"),
    ("num", [
        "**Clean and dry the cup**, then fill to the marked level. Overfilling raises the vapour concentration and "
        "gives a falsely low flash point; underfilling does the opposite.",
        "**Insert the thermometer** so that its bulb is in the specified position, and check that the stirrer turns "
        "freely.",
        "**Light the test flame** and adjust it to the specified size, then verify the shutter operates smoothly.",
        "**Begin heating at the specified rate**, with the stirrer running at the specified speed. Record the "
        "starting temperature.",
        "**Apply the test flame at the specified temperature intervals**, opening the shutter briefly each time. "
        "Regular intervals are essential: the measurement is defined by the schedule.",
        "**Record the flash point** as the temperature at which a distinct flash appears in the cup. This is the "
        "first genuine flash, not the first faint flicker.",
        "**Continue heating and testing** to find the fire point: the temperature at which the vapour ignites and "
        "burns for at least five seconds.",
        "**Stop heating, remove the flame, and let the apparatus cool** before dismantling and cleaning.",
        "**Record the sample\u2019s appearance and smell** as the source sheet requires, and note the ambient "
        "conditions.",
    ]),
    ("box", "pitfall", [
        "**A false early flash is the classic error.** A draught, a dirty cup, a wet sample, or a droplet of "
        "condensed vapour at the rim can all produce a flash that is not the true flash point. Confirm rather than "
        "accept: a genuine flash is reproducible within a few degrees on a repeat run.",
        "**Two runs, two values, means something is uncontrolled** \u2014 usually the heating rate or the sample "
        "volume. Investigate that before averaging.",
    ], "Where this experiment usually goes wrong"),
]

B += [
    ("h2", "10.5  Observations and calculation"),
    ("tbl", ["S. No.", "Sample", "Appearance / smell", "Flash point (\u00b0C)", "Fire point (\u00b0C)",
             "Remark"],
     [["1", "", "", "", "", ""], ["2", "", "", "", "", ""], ["3", "", "", "", "", ""]],
     [14, 34, 44, 30, 30, 40], "**Table 10.3** Observation table, following the supplied sheet\u2019s layout. "
                               "Blank because the source contains no completed readings.", ["c", "l", "l", "c",
                               "c", "l"]),
    ("h3", "10.5.1  Reading the result rather than calculating it"),
    ("p", "This experiment has almost no arithmetic: the answer is a temperature. What takes its place is "
          "//interpretation//. Three questions should always be answered alongside the number:"),
    ("bul", [
        "**Is the value plausible for the product class?** Diesel fuel typically flashes between about 52 and "
        "96 \u00b0C; kerosene around 38\u201374 \u00b0C; lubricating oils usually above 150 \u00b0C; gasoline is far "
        "below ambient temperature (about \u221243 \u00b0C) and must never be handled in this apparatus.",
        "**Is the flash point consistent with the smell?** A low flash point with a solvent-like smell is coherent; "
        "a low flash point with no smell suggests contamination or a measurement artefact.",
        "**Is the fire point separated from the flash point by a sensible margin?** A gap of a few degrees suggests "
        "the flash point was taken too late; a very large gap is normal for heavy oils.",
    ]),
    ("tbl", ["Quantity", "How obtained", "Illustrative value"],
     [["Flash point", "observed temperature of the first distinct flash", "78 \u00b0C"],
      ["Fire point", "temperature of sustained burning \u2265 5 s", "96 \u00b0C"],
      ["Flash\u2013fire gap", "difference", "18 \u00b0C"],
      ["Classification (example)", "compare with the local flammable-liquid rules", "combustible liquid"],
      ["Consistency check", "compare with the product class", "plausible for a light fuel oil"]],
     [42, 66, 60], "**Table 10.4** Recording frame. The illustrative values are arithmetic examples, not a "
                   "measurement claimed from the source.", ["l", "l", "c"]),
    ("box", "note", [
        "**Flammable or combustible?** The distinction is regulatory and depends on the closed-cup flash point and "
        "the jurisdiction. Rather than quote a threshold from memory, state the measured flash point and say that "
        "the classification follows the applicable standard \u2014 that is both correct and defensible.",
    ], "A classification question worth handling carefully"),
]

B += [
    ("h2", "10.6  Precautions, errors and troubleshooting"),
    ("bul", [
        "Work under an extractor hood with no other ignition sources nearby.",
        "Keep a fire extinguisher and fire blanket immediately available.",
        "Fill exactly to the mark; overfilling is both a hazard and an error.",
        "Use the specified heating rate, stirring rate and test interval.",
        "Apply the test flame briefly and at regular intervals.",
        "Clean the cup thoroughly between samples; residues raise or lower the reading unpredictably.",
        "Do not test very low-flash-point samples in this apparatus.",
        "Let the apparatus cool fully before cleaning.",
    ]),
    ("tbl", ["Source of error", "Type", "Effect on the flash point", "Control"],
     [["Heating rate too fast", "Systematic (positive)", "Sample lags the thermometer; flash reads high",
       "Use the specified rate"],
      ["Heating rate too slow", "Systematic (negative)", "More vapour accumulates; flash reads low", "Specified rate"],
      ["Overfilled cup", "Systematic (negative)", "Less vapour space; earlier ignition", "Fill to the mark"],
      ["Poor stirring", "Systematic (negative)", "Surface hotter than bulk; early flash", "Specified stirring"],
      ["Oversized test flame", "Systematic (negative)", "Ignites a leaner mixture", "Adjust to specification"],
      ["Draughts near the cup", "Random (negative)", "False or erratic flashes", "Hood, screens, still air"],
      ["Dirty cup or residue", "Variable", "Unpredictable shift", "Clean and dry between runs"],
      ["Slow thermometer response", "Systematic (positive)", "Reads a temperature higher than the true one",
       "Use the specified thermometer"],
      ["Wet sample", "Variable", "Steam dilutes vapour; erratic results", "Dry the sample"]],
     [48, 26, 52, 46], "**Table 10.5** Error budget. Note how many of these errors point towards a //low// "
                       "reading \u2014 the unsafe direction.", ["l", "l", "l", "l"]),
    ("tbl", ["Symptom", "Likely cause", "Action"],
     [["Flash at a much lower temperature than expected", "Overfill, draught, dirty cup, or volatile contamination",
       "Re-check the fill, shelter the cup, clean, use a fresh sample"],
      ["No flash at any temperature", "Flame too small, shutter not opening, or the sample is not flammable in "
       "this range", "Check the flame and shutter; reconsider the sample"],
      ["Flash, then nothing on repeat", "Marginal vapour concentration near the limit, or a contaminated sample",
       "Repeat carefully; verify the sample"],
      ["Sustained burning starts immediately", "Fire point reached; the sample is very volatile",
       "Stop heating; this is an incident, not a measurement"],
      ["Thermometer reading jumps", "Stirrer touching the thermometer, or a loose bulb", "Reposition and check"]],
     [46, 60, 64], "**Table 10.6** Troubleshooting chart.", ["l", "l", "l"]),
]

VIVA_A = [
    ("Define flash point.", "The lowest temperature at which a liquid evolves enough vapour to form an ignitable "
                            "mixture with air, so that a flame causes a flash."),
    ("Define fire point.", "The temperature at which the vapour ignites and continues to burn for at least five "
                           "seconds."),
    ("What is the principle of the Pensky\u2013Martens apparatus?", "A closed cup is heated at a controlled rate "
                                                                   "with stirring, and a small flame is introduced "
                                                                   "at intervals until a flash occurs."),
    ("Why is it a closed-cup method?", "Because the vapour is retained in the cup, so the measured flash point "
                                       "corresponds to a closed container and is lower and more conservative."),
    ("Which is higher, open-cup or closed-cup flash point?", "Open cup, because vapour escapes and a higher "
                                                             "temperature is needed to reach an ignitable "
                                                             "concentration."),
    ("What is autoignition temperature?", "The temperature at which a substance ignites spontaneously without an "
                                          "ignition source."),
    ("What are the lower and upper flammable limits?", "The vapour concentration range in air within which ignition "
                                                       "is possible."),
    ("Why is the sample stirred?", "To keep the temperature uniform and to distribute vapour evenly in the space "
                                   "above the liquid."),
    ("Why is the heating rate specified?", "Because the flash point depends on the rate: too fast and the sample "
                                           "lags; too slow and extra vapour accumulates."),
    ("What is recorded besides the temperature?", "The appearance and smell of the sample, as the source sheet "
                                                  "requires, together with the ambient conditions."),
    ("Why is the flash point important for safety?", "It determines the storage, handling and labelling "
                                                      "requirements for a flammable or combustible liquid."),
    ("Why is the flash point important for fuel quality?", "A low flash point in diesel indicates contamination "
                                                           "with a lighter fraction."),
    ("Why is the flash point important for lubricants?", "A low flash point indicates volatile light ends that will "
                                                         "cause oil consumption and thickening in service."),
    ("Name two other flash-point apparatus.", "Abel and Tag closed cup; Cleveland open cup; Setaflash."),
    ("Which apparatus is used for high-flash-point materials?", "Cleveland open cup, or Pensky\u2013Martens with a "
                                                                "suitable range."),
    ("What is the typical relation between flash point and fire point?", "The fire point is usually 20\u201360 "
                                                                         "\u00b0C higher."),
    ("Does the flash point depend on pressure?", "Yes \u2014 reduced pressure lowers the flash point, which is why "
                                                 "the ambient pressure is sometimes recorded."),
    ("Why must the cup be cleaned between samples?", "Residue changes both the vapour composition and the ignition "
                                                     "behaviour."),
    ("Why is a small flame used?", "An oversized flame ignites a leaner mixture and gives a falsely low flash "
                                   "point."),
    ("Can flash point be calculated from boiling point?", "Only approximately, by empirical correlations; the "
                                                          "measurement is required for specification purposes."),
    ("What is the flash point of water?", "Water is not flammable; the concept does not apply."),
    ("Why must very volatile liquids not be tested in this apparatus?", "They would flash below ambient temperature "
                                                                        "and create an immediate fire hazard."),
    ("What is the significance of a flash point below ambient temperature?", "The liquid is continuously giving off "
                                                                             "ignitable vapour and must be handled as "
                                                                             "highly flammable."),
    ("Which is more meaningful for storage regulations, flash or fire point?", "The flash point; the fire point is "
                                                                               "a secondary and less sharply defined "
                                                                               "observation."),
]

VIVA_B = [
    ("Why does the flash point exist at all?", "Because vapour pressure rises exponentially with temperature, so the "
                                               "vapour concentration above the liquid passes through the flammable "
                                               "range at a fairly well-defined temperature."),
    ("Why is the flash abrupt rather than gradual?", "Because the vapour pressure curve is steep in that region, so "
                                                     "the concentration changes rapidly with a few degrees."),
    ("Why does overfilling lower the flash point?", "It reduces the vapour space, so a given amount of vapour "
                                                    "produces a higher concentration and reaches the flammable limit "
                                                    "sooner."),
    ("Why does a draught cause a false flash?", "Moving air carries vapour away or disturbs the flame path, "
                                                "producing an apparent flash that is not the equilibrium "
                                                "behaviour."),
    ("Why must the ignition be applied only briefly?", "Opening the shutter for long releases vapour and cools the "
                                                       "vapour space, changing the conditions for the next test."),
    ("Why are tests applied at fixed temperature intervals?", "Because the method defines the flash point in terms "
                                                              "of a schedule; a different schedule gives a "
                                                              "different number."),
    ("Why is stirring important near the flash point?", "Because the vapour space must represent the bulk liquid; "
                                                        "without stirring the surface is hotter and flashes early."),
    ("Why is the apparent flash verified by a repeat run?", "Because many artefacts (draught, dirt, droplets) "
                                                            "produce a single spurious flash that is not "
                                                            "reproducible."),
    ("Why do we record the smell as well as the temperature?", "It is an independent check on sample identity and "
                                                               "contamination, which the temperature alone cannot "
                                                               "reveal."),
    ("Why is the fire point harder to define than the flash point?", "Because \u2018continues to burn for five "
                                                                      "seconds\u2019 depends on observation and on the "
                                                                      "vapour generation rate, and the transition is "
                                                                      "gradual."),
    ("Why is flash point measured in a closed cup for regulatory purposes?", "Because closed containers are the "
                                                                             "realistic storage condition, and the "
                                                                             "closed-cup value is the more "
                                                                             "conservative."),
    ("How does the presence of dissolved water affect the result?", "Water vapour dilutes the fuel vapour and can "
                                                                    "produce erratic, usually high, results."),
    ("Why does a lubricating oil have a much higher flash point than diesel?", "Because it consists of much heavier "
                                                                               "hydrocarbons with far lower vapour "
                                                                               "pressure at a given temperature."),
    ("Why is the flash point a purity indicator for solvents?", "Because a small amount of a more volatile "
                                                                "component lowers it markedly."),
]

VIVA_C = [
    ("What if you heated much faster than specified?", "The bulk liquid lags the thermometer, so the recorded "
                                                       "temperature is too high; the flash point would be "
                                                       "overestimated."),
    ("What if you overfilled the cup?", "The vapour space is smaller, so the ignitable concentration is reached "
                                        "earlier and the flash point reads low."),
    ("What if the test flame were too large?", "It can ignite a mixture that is below the flammable limit, giving a "
                                               "falsely low flash point."),
    ("What if the sample were contaminated with a solvent?", "The flash point would drop sharply, and the smell "
                                                             "would usually reveal it."),
    ("What if you obtained a flash on the first test at a low temperature?", "Suspect an artefact \u2014 draught, "
                                                                             "residue, or a droplet at the rim; "
                                                                             "verify with a fresh sample."),
    ("What if the sample started burning continuously?", "The fire point has been reached; stop heating and "
                                                         "extinguish rather than continue."),
    ("What if the thermometer were reading 2 \u00b0C high?", "The reported flash point would be 2 \u00b0C high, "
                                                            "which matters when comparing against a specification "
                                                            "limit."),
    ("What if you forgot to stir?", "The surface layer would be hotter than the bulk, giving an early flash and a "
                                    "low result."),
    ("What if the sample were tested at a different ambient pressure?", "The flash point would shift, usually lower "
                                                                        "at reduced pressure; the method assumes "
                                                                        "standard conditions."),
    ("What if no flash occurred at all after prolonged heating?", "The sample may be non-flammable in that range, "
                                                                  "the flame may not be reaching the vapour space, "
                                                                  "or the shutter may not be opening."),
]

VIVA_D = [
    ("Why is the closed-cup flash point lower than the open-cup value?", "In a closed cup, vapour cannot escape, so "
                                                                         "equilibrium concentration is reached at a "
                                                                         "lower temperature; in an open cup, "
                                                                         "convection and diffusion continuously "
                                                                         "remove vapour."),
    ("What determines the flash point at a molecular level?", "The vapour pressure, which reflects intermolecular "
                                                              "forces and molecular size; higher forces and larger "
                                                              "molecules mean lower vapour pressure and higher flash "
                                                              "point."),
    ("Why does the flash point fall as the pressure falls?", "Because the vapour must supply a given mole fraction "
                                                             "in air; at lower total pressure, a smaller absolute "
                                                             "vapour pressure achieves that fraction."),
    ("How would you estimate the flash point from vapour-pressure data?", "Find the temperature at which the vapour "
                                                                          "pressure equals the partial pressure "
                                                                          "corresponding to the lower flammable limit, "
                                                                          "then correct for the cup geometry, which "
                                                                          "is why the estimate is only approximate."),
    ("Why is the fire point of limited use in specifications?", "Because it is less reproducible than the flash "
                                                                "point and adds little to safety classification; "
                                                                "the flash point already captures the hazard."),
    ("Can two samples with the same flash point behave differently in a fire?", "Yes \u2014 flash point describes "
                                                                                "ignition of vapour, not the heat "
                                                                                "release rate, flame spread or "
                                                                                "toxicity of combustion products."),
    ("How would you distinguish contamination by a lighter fraction?", "Compare the measured flash point with the "
                                                                       "specification for the neat product and "
                                                                       "corroborate it with distillation data or "
                                                                       "vapour pressure."),
    ("Why do regulations use closed-cup methods for transport classification?", "Because transport and storage "
                                                                                 "involve closed containers, so the "
                                                                                 "closed-cup value represents the "
                                                                                 "realistic worst case."),
    ("What is the relation between flash point and Reid vapour pressure?", "Both measure volatility, but at "
                                                                           "different temperatures: the flash point "
                                                                           "marks the ignition condition while the "
                                                                           "vapour pressure characterises the "
                                                                           "volatility at a fixed temperature."),
    ("Why is flash point one of the few measurements with legal force?", "Because it maps directly onto storage, "
                                                                         "transport and labelling requirements, so "
                                                                         "a wrong number is a compliance failure, "
                                                                         "not merely a scientific one."),
]

CH10_CHECK = checklist(
    "10.8",
    ["Flash point = lowest temperature giving an ignitable vapour mixture.",
     "Fire point = vapour burns for at least 5 s.",
     "Autoignition temperature is higher and needs no ignition source.",
     "Pensky\u2013Martens is a closed-cup method.",
     "Closed cup < open cup for the same sample.",
     "Flash point arises from the exponential rise of vapour pressure with T.",
     "Ignition requires a concentration between the LFL and UFL.",
     "Fill exactly to the mark.",
     "Use the specified heating rate, stirring rate and test interval.",
     "A draught, a dirty cup or a wet sample causes false flashes.",
     "Overfilling lowers the flash point.",
     "Oversized test flame lowers the flash point.",
     "Too-fast heating raises the flash point.",
     "Fire point typically 20\u201360 \u00b0C above flash point.",
     "Record appearance and smell as well as temperature.",
     "Diesel \u2248 52\u201396 \u00b0C; kerosene \u2248 38\u201374 \u00b0C; lubricating oils above 150 \u00b0C.",
     "Gasoline flashes far below ambient and must not be tested here.",
     "A low flash point in diesel suggests contamination with a light fraction.",
     "A low flash point in a lubricant indicates volatile light ends.",
     "The source does not state heating rate, stirring rate or test interval \u2014 a recorded gap."],
    ["Define flash point and fire point.",
     "Why is Pensky\u2013Martens a closed-cup method?",
     "Which is higher, open or closed cup, and why?",
     "What is autoignition temperature?",
     "State the ignition condition in terms of vapour concentration.",
     "Why is the sample stirred?",
     "Why is the heating rate specified?",
     "Why is an oversized flame a problem?",
     "What is the safety significance of the flash point?",
     "What does a low flash point tell you about a fuel?"],
    ["Explain why the flash is abrupt, using the vapour pressure curve.",
     "Derive the direction of error for a heating rate that is too fast.",
     "Your first reading is 20 \u00b0C below the repeat. Give four causes and a test for each.",
     "Compare closed-cup and open-cup methods physically, not just numerically.",
     "Why does lower ambient pressure lower the flash point?",
     "Explain how an unusually low flash point in lube oil affects engine operation.",
     "Why is the error budget skewed towards unsafe results?",
     "Discuss why flash point, not fire point, is the regulated quantity.",
     "How would you confirm a suspected solvent contamination?",
     "What would you do if the sample ignited continuously during the test?"],
    [("Flash vs fire point", "Transient flash vs sustained burning."),
     ("Flash point vs autoignition temperature", "External ignition required vs spontaneous."),
     ("Closed vs open cup", "Retained vapour vs escaping vapour."),
     ("Flash point vs boiling point", "Ignition of vapour vs bulk vaporisation."),
     ("Flammable vs combustible", "Regulatory classes based on closed-cup flash point."),
     ("LFL vs UEL", "Lean vs rich ignition limits."),
     ("Safety vs quality significance", "Handling classification vs product specification."),
     ("Observed vs specified method", "Rate, stirring and interval define the number.")],
    (["Relation", "Expression", "Note"],
     [["Vapour pressure", "ln P \u2248 A \u2212 B/T", "Clausius\u2013Clapeyron form"],
      ["Ignition condition", "LFL \u2264 [vapour] \u2264 UEL", "In air"],
      ["Flash\u2013fire gap", "\u0394T \u2248 20\u201360 \u00b0C", "Product dependent"],
      ["Closed vs open cup", "closed < open", "Typically 5\u201320 \u00b0C"],
      ["Pressure dependence", "lower P \u2192 lower flash point", "Method assumes standard conditions"],
      ["Unit", "\u00b0C (or \u00b0F in some standards)", "State the scale"],
      ["Reading", "temperature at the first distinct flash", "Confirm with a repeat"],
      ["Fire point criterion", "burning \u2265 5 s", "Observational"]],
     [40, 74, 54]),
    [["Flash far below expectation", "Overfill, draught, dirty cup or volatile contamination"],
     ["No flash at any temperature", "Flame too small, shutter stuck, or non-flammable sample"],
     ["Flash not reproducible", "Marginal vapour concentration or contaminated sample"],
     ["Immediate sustained burning", "Fire point reached; volatile sample"],
     ["Thermometer jumps", "Stirrer fouling the thermometer"],
     ["Smell inconsistent with the flash point", "Contamination or a measurement artefact"]],
    ["Closed cup is the conservative, regulated measurement.",
     "Flash point is set by vapour pressure, not by boiling point.",
     "Rate, stirring and interval are part of the method.",
     "Most careless errors lower the reading \u2014 the unsafe direction.",
     "Confirm any flash with a repeat run.",
     "Record smell and appearance as independent evidence.",
     "Fire point is secondary; flash point is the specification."],
    ["Quoting a flash point without the method (closed or open cup).",
     "Ignoring the heating rate.",
     "Overfilling the cup.",
     "Accepting the first flash without confirmation.",
     "Testing a very volatile liquid in this apparatus.",
     "Confusing flash point with autoignition temperature.",
     "Leaving the apparatus unattended while heating."],
    ["The Pensky\u2013Martens apparatus determines the flash point and fire point of a sample in a closed cup. I fill "
     "the cup to the mark, insert the thermometer, set the stirrer and the test flame, and heat at the rate the "
     "method requires, applying the flame briefly at fixed temperature intervals. The flash point is the temperature "
     "at which a distinct flash appears; the fire point is the higher temperature at which the vapour burns for at "
     "least five seconds. Chemically, heating raises the vapour pressure, and the flash occurs when the vapour "
     "concentration above the liquid first enters the flammable range. Because the vapour is retained, a closed cup "
     "gives a lower, more conservative value than an open cup for the same sample. The critical controls are the "
     "heating rate, the stirring rate, the test interval, the fill level and the flame size \u2014 all of which are "
     "part of the definition \u2014 and any apparent flash is confirmed by a repeat, because draughts and residues "
     "produce spurious low readings."],
    ["**Closed cup: lower, conservative, regulated.**",
     "**Rate, stirring, interval and fill define the number.**",
     "**Vapour pressure sets the flash, not the boiling point.**",
     "**Confirm every flash; most artefacts read low.**"]
)

CH10 = {
    "key": "flashpoint",
    "num": "10",
    "kicker": "Experiment 10  \u00b7  Petroleum testing",
    "title": "Flash Point and Fire Point by Pensky\u2013Martens Apparatus",
    "toc": "Flash point and fire point",
    "standfirst": "A measurement made with a flame, in which the method parameters are the result. This chapter is "
                  "as much about reading a specification as about reading a thermometer.",
    "body": B + [
        ("h2", "10.7  Viva question bank"),
        ("p", "Seventy-eight answered questions, with particular attention to the method parameters the supplied source "
              "does not state."),
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
    ] + CH10_CHECK,
}
