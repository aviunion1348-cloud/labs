"""Chapter 2 - Kinetics of acid-catalysed hydrolysis of ethyl acetate."""
from common import checklist

B = []

B += [
    ("h2", "2.1  What this experiment measures, and why it matters"),
    ("lead", "Ester hydrolysis is one of the cleanest reactions in the undergraduate laboratory: one ester and "
             "one water molecule give one acid and one alcohol, with no side products, no colour change and no "
             "precipitate. Nothing about it is visible. Everything must be inferred by titrating the acid that "
             "appears \u2014 which makes it an excellent training ground for the central skill of chemical "
             "kinetics: turning a chemical change into a number that can be plotted."),
    ("p", "The aim from the supplied material is explicit: **to study the kinetics of the acid-catalysed "
          "hydrolysis of ethyl acetate and to evaluate the rate constant.** You are not asked to discover a new "
          "reaction; you are asked to demonstrate that a reaction you cannot see follows a particular "
          "mathematical law, and to extract the constant from that law."),
    ("p", "The reaction is:"),
    ("eq", "CH_{3}COOC_{2}H_{5} + H_{2}O  \u21cc  CH_{3}COOH + C_{2}H_{5}OH",
     "Equation 2.1 \u2014 acid-catalysed hydrolysis of ethyl acetate (ethyl ethanoate). The equilibrium lies well "
     "towards the right in dilute aqueous acid, so the reaction is treated as effectively complete."),
    ("p", "Because a strong acid (HCl) catalyses the reaction, the true rate law at any instant involves the "
          "ester, the water **and** the acid. But water is present in large excess, and the acid concentration is "
          "constant because it is a catalyst. Both of those constant concentrations fold into a single observed "
          "rate constant. What remains is a rate law that is first order in one species only \u2014 the ester. "
          "That is what //pseudo//-first-order means, and it is the intellectual core of the experiment."),
    ("defbox", [
        ("Hydrolysis", "Cleavage of a bond by water. Here, the C\u2013O bond of the ester is broken by attack of "
                       "water, giving a carboxylic acid and an alcohol."),
        ("Rate of reaction", "The change in concentration of a reactant or product per unit time; units "
                            "mol L^{\u22121} s^{\u22121} (or per minute, if time is in minutes)."),
        ("Rate constant (k)", "The proportionality constant in a rate law, at a stated temperature. It "
                              "incorporates all constant concentrations and constants of the mechanism."),
        ("Order", "The exponent on a species in the experimentally determined rate law. First order in ester "
                  "here means rate \u221d [ester]^{1}."),
        ("Pseudo-first-order", "A reaction that is second order overall in its true rate law, but behaves as "
                               "first order because one reactant is in such large excess that its concentration "
                               "is effectively constant."),
        ("Half-life", "The time for half of the reactant to be consumed; for a first-order reaction it is "
                      "t_{1/2} = 0.693/k, independent of starting concentration."),
    ]),
    ("box", "key", [
        "The measured quantity is **not** the ester concentration directly. It is the **alkali titre** of an "
        "aliquot, which is proportional to the amount of acetic acid present.",
        "Three titres define the experiment: **V_{0}** at the start (catalyst acid only), **V_{t}** at time t "
        "(catalyst acid + acetic acid formed), and **V_{\u221e}** at completion (the maximum).",
        "The quantity that decays first-order is **(V_{\u221e} \u2212 V_{t})**, which is proportional to the "
        "unreacted ester remaining.",
    ], "Three ideas that make the whole calculation work"),
    ("fig", "kinetics", "**Figure 2.1** The sampling train. A constant-temperature bath holds the reaction "
                        "mixture; identical aliquots are withdrawn at recorded times, quenched in ice-cold water "
                        "to stop further hydrolysis, and titrated with standard alkali."),
]

B += [
    ("h2", "2.2  Theory, built from zero"),
    ("h3", "2.2.1  Why an ester reacts with water at all"),
    ("p", "The carbonyl carbon of an ester is electrophilic: the C=O oxygen withdraws electron density, leaving "
          "the carbon partially positive. Water is a nucleophile with two lone pairs. Left alone, water will "
          "attack that carbon, but slowly, because water is a weak nucleophile and the alkoxy group is a poor "
          "leaving group as the alkoxide. Acid catalysis changes both problems at once:"),
    ("num", [
        "**Protonation of the carbonyl oxygen** makes the carbonyl carbon more electrophilic and far more "
        "attractive to water. This is the rate-determining activation step.",
        "**Protonation of the alkoxy oxygen** converts a poor leaving group (RO^{\u2212}) into a good one "
        "(ROH), so the tetrahedral intermediate can collapse cleanly.",
        "The acid is regenerated when the products leave, so it is a genuine catalyst and its concentration does "
        "not change during the run.",
    ]),
    ("p", "The mechanism is the **A_{AC}2** pathway (acid-catalysed, acyl-oxygen cleavage, bimolecular). In "
          "condensed form:"),
    ("eq", "ester + H^{+} \u21cc [protonated ester] \u2192 [tetrahedral intermediate] \u2192 acid + alcohol + "
           "H^{+}"),
    ("p", "Two consequences follow. First, because the rate-determining step is bimolecular in ester and water, "
          "the true rate law is **second order overall**: rate = k_{3}[ester][H_{2}O][H^{+}] at high water "
          "concentration, simplifying to rate = k\u2032[ester][H_{2}O]. Second, because the reaction is an "
          "equilibrium, you need a strategy to reach the //end// point \u2014 which is why the manual heats the "
          "reaction mixture to drive it to completion when V_{\u221e} is measured."),
    ("h3", "2.2.2  The pseudo-first-order approximation, stated precisely"),
    ("p", "In a typical run the ester is roughly 0.02\u20130.05 mol L^{\u22121} and water is the solvent at about "
          "55 mol L^{\u22121}. Even if every ester molecule is hydrolysed, the water consumed is a negligible "
          "fraction of the total. Formally:"),
    ("eq", "[H_{2}O]_{t} = [H_{2}O]_{0} \u2212 x \u2248 [H_{2}O]_{0}",
     "Equation 2.2 \u2014 the excess condition. With x \u2264 0.05 mol L^{\u22121} and [H_{2}O]_{0} \u2248 55 "
     "mol L^{\u22121}, the fractional change is under 0.1 %."),
    ("p", "Because both [H_{2}O] and [H^{+}] are effectively constant, they can be absorbed into a single "
          "observed constant:"),
    ("eq", "rate = k_{obs}[ester],   where  k_{obs} = k_{true}[H_{2}O][H^{+}]",
     "Equation 2.3 \u2014 the observed (pseudo-first-order) rate constant. Note that k_{obs} carries the units of "
     "concentration squared divided by time, but is //reported// as if it were first order, which is precisely "
     "why it is called pseudo."),
    ("p", "This matters for a viva. If an examiner asks \u201cis the reaction first order?\u201d, the complete "
          "answer is: **the observed rate is first order in ester, but the reaction is bimolecular in its "
          "rate-determining step; the apparent first-order behaviour arises only because water is in large "
          "excess.** If you doubled the water concentration by using a mixed solvent, k_{obs} would double, which "
          "proves the water is chemically involved even though it does not appear in the observed rate law."),
    ("h3", "2.2.3  Deriving the integrated rate law, and why the answer involves a titre"),
    ("p", "Start from the differential law and integrate:"),
    ("eq", "\u2212d[ester]/dt = k_{obs}[ester]"),
    ("eq", "\u21d2  \u222b d[ester]/[ester] = \u2212k_{obs} \u222b dt  \u21d2  ln([ester]_{0}/[ester]_{t}) = "
           "k_{obs} t"),
    ("eq", "\u21d2  log_{10}([ester]_{0}/[ester]_{t}) = (k_{obs}/2.303) t",
     "Equation 2.4 \u2014 the integrated first-order law in both natural and common logarithms. The factor 2.303 is "
     "ln 10, and it is the single most common place students lose marks."),
    ("p", "Now the experimental bridge. At any time, the amount of acetic acid formed equals the amount of ester "
          "consumed. The alkali titre measures total acid = catalyst acid + acetic acid formed. Define:"),
    ("tbl", ["Symbol", "Meaning", "Proportional to"],
     [["V_{0}", "alkali titre of the aliquot taken at t = 0", "the HCl catalyst alone"],
      ["V_{t}", "alkali titre of the aliquot taken at time t", "HCl + acetic acid formed by time t"],
      ["V_{\u221e}", "alkali titre after the reaction has been driven to completion",
       "HCl + the acetic acid from //all// the ester"]],
     [16, 82, 72], "**Table 2.1** The three titres. Every term in the rate equation is built from these, which "
                   "is why V_{\u221e} deserves its own careful measurement.", ["c", "l", "l"]),
    ("p", "At time t, the acetic acid formed is proportional to (V_{t} \u2212 V_{0}). At completion, the total "
          "acid from all the ester is proportional to (V_{\u221e} \u2212 V_{0}). Therefore the **unreacted ester "
          "remaining** at time t is proportional to the //difference of those two//:"),
    ("eq", "[ester]_{t} \u221d (V_{\u221e} \u2212 V_{t}),   and   [ester]_{0} \u221d (V_{\u221e} \u2212 V_{0})"),
    ("p", "Substituting into the integrated law:"),
    ("eq", "k_{obs} = (2.303/t) log_{10}[(V_{\u221e} \u2212 V_{0})/(V_{\u221e} \u2212 V_{t})]",
     "Equation 2.5 \u2014 the working equation given in the supplied manual. Its unit is time^{\u22121}, so k is "
     "in min^{\u22121} if t is in minutes."),
    ("p", "A very common variant omits V_{0} on the grounds that the ester solution contributes a small blank "
          "titre. That is only justified if V_{0} has genuinely been measured and is negligible, or if the manual "
          "defines the titres relative to V_{0}. **Use the form your manual specifies and say which form you "
          "used** \u2014 an examiner will accept either with a reason and reject the wrong one with none."),
    ("h3", "2.2.4  The graphical method, and what a straight line proves"),
    ("p", "Equation 2.4 is of the form y = mx with y = log_{10}[(V_{\u221e} \u2212 V_{0})/(V_{\u221e} \u2212 "
          "V_{t})] and x = t. So a plot of that logarithm against time should be a straight line through the "
          "origin, with:"),
    ("eq", "slope = k_{obs}/2.303   \u21d2   k_{obs} = 2.303 \u00d7 slope",
     "Equation 2.6 \u2014 extracting the rate constant from the graph. This is the relation the supplied manual "
     "states explicitly."),
    ("p", "A straight line is evidence that the integrated first-order law describes the data over the measured "
          "interval. It is **not** proof that the mechanism is first order \u2014 other models can fit a limited "
          "range \u2014 but combined with the excess-water argument it is a strong, coherent case. Note also that "
          "a straight line with a non-zero intercept signals that the zero of time is offset (mixing delay) or "
          "that V_{\u221e} is slightly wrong."),
    ("h3", "2.2.5  Why temperature control is not optional"),
    ("p", "The rate constant depends on temperature through the Arrhenius equation:"),
    ("eq", "k = A e^{\u2212E_{a}/RT}   \u21d2   ln k = ln A \u2212 E_{a}/RT",
     "Equation 2.7 \u2014 Arrhenius behaviour. A typical ester hydrolysis activation energy is of the order of "
     "50\u201360 kJ mol^{\u22121}, which makes k change by roughly 10 % for a 2 \u00b0C change near room "
     "temperature."),
    ("p", "That number is the reason a bath is used and the reason the temperature is written on the report "
          "sheet. A run that drifts by 3 \u00b0C will show a systematic curvature in the log plot that looks like "
          "a failure of the first-order model but is really a failure of thermal control."),
]

B += [
    ("h2", "2.3  Apparatus and reagents"),
    ("tbl", ["Item", "Function", "Consequence of a fault"],
     [["Stoppered conical flask / reaction bottle", "Holds the reaction mixture at controlled temperature",
       "An open vessel loses ester and HCl by evaporation; concentrations drift"],
      ["Constant-temperature water bath", "Keeps k constant during the run",
       "Uncontrolled temperature makes k drift and curves the log plot"],
      ["Thermometer (0.1 \u00b0C)", "Records the actual run temperature",
       "Without it the result cannot be compared with any other run"],
      ["Pipette, 5 mL (or as specified)", "Delivers identical aliquots",
       "Variable aliquot size destroys comparability between titres"],
      ["Burette + stand", "Delivers standard NaOH for each titration",
       "Air bubble or leaking stopcock biases every titre"],
      ["Conical flasks, ice bath", "Receive and quench the aliquot",
       "Without quenching, hydrolysis continues during the titration"],
      ["Standard NaOH (standardised)", "Titrant; converts acid amount into titre",
       "Unstandardised alkali makes the absolute k meaningless"],
      ["Phenolphthalein", "Endpoint indicator, colourless \u2192 faint pink",
       "Deep pink endpoint overestimates every titre"],
      ["Ethyl acetate (freshly distilled)", "Reactant",
       "Old ester has partly hydrolysed; the starting concentration is wrong"],
      ["Standard HCl", "Catalyst; sets [H^{+}] which enters k_{obs}", "Wrong acid strength changes k_{obs}"],
      ["Stopwatch", "Times the aliquots", "Timing error enters k directly, as 1/t"]],
     [44, 58, 68], "**Table 2.2** Apparatus and reagents. Note how many failure modes are about **constancy** "
                   "\u2014 constant temperature, constant aliquot, constant endpoint, constant titrant.", ["l", "l", "l"]),
    ("box", "warn", [
        "Ethyl acetate is flammable and irritates eyes and airways; HCl is corrosive. Work in a fume hood or "
        "well-ventilated space, wear eye protection and gloves, and keep sources of ignition away. Never pipette "
        "by mouth. Dispose of residues through the organic-waste route specified by your institution.",
    ], "Handling"),
]

B += [
    ("h2", "2.4  Procedure with reasoning"),
    ("p", "The sequence below follows the supplied manual: mix ester and acid at a recorded start time, withdraw "
          "identical aliquots at recorded intervals, quench each in cold water and titrate with standard alkali "
          "to a faint pink phenolphthalein endpoint, then obtain V_{\u221e} by heating the remainder at "
          "70\u201390 \u00b0C for 10\u201315 minutes and titrating a final aliquot."),
    ("num", [
        "**Standardise the NaOH** (or confirm the factor supplied with it). Every titre is converted to an amount "
        "of acid through this concentration; if it is wrong, k is wrong by the same factor \u2014 though note "
        "that in Equation 2.5 the concentration cancels, so the //k// from the ratio method is insensitive to the "
        "alkali strength, while V_{\u221e} definitions and any absolute amounts are not.",
        "**Equilibrate both solutions in the bath** before mixing. If the ester and acid are at different "
        "temperatures, the mixture drifts towards the bath temperature during the first minutes \u2014 exactly "
        "when the rate is highest and the first data points are taken.",
        "**Measure the required volumes accurately** and record the exact composition. You need [ester]_{0} and "
        "[H^{+}] to compare runs.",
        "**Start the stopwatch at the moment of mixing** (or at the moment half the acid has been added, "
        "consistently). The absolute clock is less important than **consistency**, because a constant offset only "
        "shifts the line, while a variable one scatters the points.",
        "**Withdraw the first aliquot (V_{0}) immediately**, before appreciable reaction. This establishes the "
        "catalyst-only titre.",
        "**At each recorded time, withdraw an identical aliquot** and run it immediately into ice-cold distilled "
        "water. Cooling and dilution together slow the reaction enough that the composition is effectively "
        "frozen during titration.",
        "**Titrate each quenched aliquot with standard NaOH to a faint pink endpoint** that persists for about "
        "30 seconds. Use the same shade every time.",
        "**Record the time at the moment of quenching**, not at the moment of titration. The reaction stops when "
        "the aliquot hits the ice water.",
        "**After the last kinetic point, heat the remaining mixture at 70\u201390 \u00b0C for 10\u201315 minutes** "
        "to drive the hydrolysis to completion, cool, and titrate an aliquot of the same size. This is "
        "V_{\u221e}.",
        "**Calculate k at each time point**, tabulate, and inspect for constancy. Then plot the logarithm against "
        "time and obtain k from the slope.",
    ]),
    ("box", "note", [
        "**Why quench in ice-cold water rather than just cold water?** Two effects act together: lowering the "
        "temperature reduces k_{obs}, and diluting the aliquot reduces both [ester] and [H^{+}]. The combination "
        "slows the residual reaction by an order of magnitude or more for the minute or two the titration takes. "
        "Warm water would leave the reaction running while you titrate, so each titre would correspond to an "
        "unknown, later time.",
    ], "The reasoning behind the quench"),
    ("box", "caution", [
        "**Do not skip the V_{\u221e} determination or replace it with the last kinetic titre.** If hydrolysis is "
        "incomplete when you stop, the last titre is not V_{\u221e}, and every calculated k will be systematically "
        "wrong \u2014 because V_{\u221e} appears in both numerator and denominator of the log term. This is the "
        "single largest source of bad results in this experiment.",
    ], "The error that ruins the whole run"),
]

B += [
    ("h2", "2.5  Observations and calculation"),
    ("tbl", ["S. No.", "Time t (min)", "Burette reading (mL)", "Titre V_{t} (mL)",
             "(V_{\u221e} \u2212 V_{t}) (mL)", "log_{10}[(V_{\u221e}\u2212V_{0})/(V_{\u221e}\u2212V_{t})]",
             "k (min^{\u22121})"],
     [["1", "0", "", "", "", "0.000", "\u2014"]] + [[str(i), "", "", "", "", "", ""] for i in range(2, 8)] + [
         ["\u221e", "after heating", "", "", "\u2014", "\u2014", "\u2014"]],
     [10, 20, 26, 20, 28, 38, 24],
     "**Table 2.3** Observation table. Fill the last two columns only after V_{\u221e} is known; they are "
     "calculated columns, not observations. The template is deliberately blank because the supplied source "
     "contains no measured values.", ["c", "c", "c", "c", "c", "c", "c"]),
    ("h3", "2.5.1  Interpreting the numbers"),
    ("bul", [
        "**Titre increases with time** because acetic acid accumulates. A titre that decreases means the aliquot "
        "or the recording is wrong.",
        "**V_{\u221e} must exceed every V_{t}** and should be approached asymptotically. If V_{\u221e} is only "
        "slightly above the last V_{t}, the reaction was not driven to completion.",
        "**k should be approximately constant** across the middle of the run. Points very close to V_{\u221e} "
        "become unreliable because (V_{\u221e} \u2212 V_{t}) is small and the ratio is dominated by measurement "
        "error.",
        "**The plot should be linear through the origin** with slope k/2.303.",
    ]),
    ("h3", "2.5.2  Worked illustration (arithmetic only)"),
    ("p", "The following numbers are chosen to make the arithmetic transparent. They are **not** measurements "
          "from the supplied material and must not be reported as such."),
    ("p", "Suppose V_{0} = 2.00 mL, V_{\u221e} = 22.00 mL, and at t = 20 min the titre is V_{t} = 9.60 mL. Then:"),
    ("eq", "(V_{\u221e} \u2212 V_{0}) = 20.00 mL;   (V_{\u221e} \u2212 V_{t}) = 12.40 mL"),
    ("eq", "ratio = 20.00/12.40 = 1.613;   log_{10}(1.613) = 0.2076"),
    ("eq", "k = (2.303/20.0) \u00d7 0.2076 = 0.115 \u00d7 0.2076 = 0.0239 min^{\u22121}"),
    ("p", "If the next point at t = 40 min gives a ratio of 2.60, log = 0.4150, and k = (2.303/40) \u00d7 0.4150 "
          "= 0.0239 min^{\u22121} \u2014 identical, which is exactly what first-order behaviour predicts. "
          "Constancy of k is the numerical equivalent of a straight line."),
    ("p", "Converting to SI: 0.0239 min^{\u22121} = 0.0239/60 s^{\u22121} = 3.98 \u00d7 10^{\u22124} s^{\u22121}. "
          "The half-life follows immediately: t_{1/2} = 0.693/k = 0.693/0.0239 = 29 min. Being able to quote a "
          "half-life from your own k is a strong sign that you understand what the constant means."),
    ("tbl", ["Quantity", "Expression", "Illustrative value"],
     [["Initial titre", "measured", "2.00 mL"],
      ["Completion titre", "after heating at 70\u201390 \u00b0C", "22.00 mL"],
      ["Titre at 20 min", "measured", "9.60 mL"],
      ["Fraction of ester remaining", "(V_{\u221e} \u2212 V_{t})/(V_{\u221e} \u2212 V_{0})", "0.620"],
      ["k at 20 min", "(2.303/t) log[(V_{\u221e}\u2212V_{0})/(V_{\u221e}\u2212V_{t})]", "0.0239 min^{\u22121}"],
      ["k from the slope", "2.303 \u00d7 slope", "0.0239 min^{\u22121}"],
      ["Half-life", "0.693/k", "29 min"],
      ["k in SI", "divide by 60", "3.98 \u00d7 10^{\u22124} s^{\u22121}"]],
     [42, 70, 56], "**Table 2.4** Calculation chain. Note that the fraction remaining falls smoothly; if it "
                   "does not, the model or the data is wrong.", ["l", "l", "c"]),
]

B += [
    ("h2", "2.6  Precautions, errors and troubleshooting"),
    ("bul", [
        "Start timing at mixing, and record time at the moment of quenching.",
        "Use exactly the same aliquot volume every time, from the same pipette.",
        "Keep the reaction flask in the bath, stoppered, at a recorded temperature.",
        "Titrate to the //same// faint pink endpoint every time; a deep pink endpoint biases upward.",
        "Determine V_{\u221e} by the heating step, not by guessing.",
        "Standardise the alkali and check its factor; keep it stoppered to exclude CO_{2}.",
        "Do not interchange ethyl acetate and methyl acetate in the write-up \u2014 the supplied material does so "
        "in one passage, and the products differ (ethanol vs methanol).",
        "Use freshly distilled ester; old material has partly hydrolysed and its effective concentration is unknown.",
    ]),
    ("tbl", ["Source of error", "Type", "Effect on k", "Control"],
     [["Temperature drift during the run", "Systematic", "k drifts; log plot curves", "Bath; equilibrate before mixing"],
      ["Timing offset or reaction delay", "Systematic (offset)", "Intercept, not slope", "Consistent start and stop points"],
      ["V_{\u221e} underestimated (incomplete reaction)", "Systematic", "k biased; curvature", "Heat 10\u201315 min at 70\u201390 \u00b0C"],
      ["Endpoint overshoot", "Systematic (positive)", "Titre high; k biased", "Faint pink, consistent shade"],
      ["Variable aliquot volume", "Random + systematic", "Scatter", "One pipette, same technique"],
      ["Unquenched aliquot", "Systematic", "Titre high, time ambiguous", "Ice-cold dilution immediately"],
      ["Unstandardised NaOH", "Systematic", "Absolute amounts wrong; ratio method self-cancelling",
       "Standardise; note the cancellation"],
      ["Evaporation of ester from an open flask", "Systematic", "Concentration falls; apparent rate changes",
       "Stoppered flask"],
      ["CO_{2} absorption by NaOH", "Systematic", "Effective alkali strength falls", "Stoppered, freshly standardised"]],
     [50, 32, 44, 44], "**Table 2.5** Error budget. Note that several errors cancel in the //ratio// form of "
                       "the equation \u2014 a sophisticated point to make in a viva.", ["l", "l", "l", "l"]),
    ("h3", "2.6.1  Troubleshooting"),
    ("tbl", ["Symptom", "Likely cause", "Action"],
     [["Titre decreases with time", "Aliquots mislabelled, or burette read backwards", "Re-check the record; repeat"],
      ["V_{\u221e} barely above the last titre", "Reaction not driven to completion", "Heat longer; re-titrate"],
      ["Calculated k falls steadily", "Temperature falling, or V_{\u221e} too small", "Check bath and V_{\u221e}"],
      ["Calculated k rises steadily", "Temperature rising, or V_{\u221e} too large", "Check bath and V_{\u221e}"],
      ["Log plot curved upward at late times", "V_{\u221e} underestimated, or slow side reaction", "Re-determine "
       "V_{\u221e}"],
      ["Endpoint hard to see", "Too little indicator, or the aliquot is still warm", "Add 2 drops; cool fully"],
      ["k differs by a factor of 60 from a friend\u2019s", "Minutes vs seconds confusion", "State the unit of t"]],
     [44, 60, 66], "**Table 2.6** Troubleshooting chart.", ["l", "l", "l"]),
]

VIVA_A = [
    ("State the aim.", "To study the kinetics of the acid-catalysed hydrolysis of ethyl acetate and to "
                       "determine the rate constant of the reaction."),
    ("Write the reaction.", "CH_{3}COOC_{2}H_{5} + H_{2}O \u2192 CH_{3}COOH + C_{2}H_{5}OH, catalysed by "
                            "H^{+} (from HCl)."),
    ("What are the products?", "Acetic acid (ethanoic acid) and ethanol."),
    ("What is hydrolysis?", "A reaction in which water cleaves a bond in the substrate; here the ester C\u2013O "
                            "bond, giving an acid and an alcohol."),
    ("What is the role of HCl?", "It is the catalyst: it protonates the ester carbonyl, activating it towards "
                                 "water attack, and is regenerated at the end of each cycle."),
    ("Why is the reaction called pseudo-first-order?", "Because the true rate law involves ester and water, but "
                                                       "water is in large excess so its concentration stays "
                                                       "effectively constant; the observed rate is then first "
                                                       "order in ester only."),
    ("What does \u201cpseudo\u201d add to \u201cfirst order\u201d?", "It signals that the first-order behaviour is "
                                                                   "an experimental convenience created by the "
                                                                   "excess condition, not the true molecular "
                                                                   "order of the reaction."),
    ("What is the true order of the rate-determining step?", "Bimolecular in ester and water (second order "
                                                             "overall in the simplified model), with acid "
                                                             "concentration also entering k_{obs}."),
    ("Define the rate constant.", "The proportionality constant relating rate to concentration in the rate law, "
                                  "at a specified temperature; for a first-order law its unit is "
                                  "time^{\u22121}."),
    ("What is the unit of k here?", "min^{\u22121}, if time is in minutes (or s^{\u22121} if seconds)."),
    ("Define V_{0}, V_{t} and V_{\u221e}.", "V_{0} is the alkali titre at t = 0 (catalyst acid only); V_{t} the "
                                            "titre at time t (catalyst plus acetic acid formed); V_{\u221e} the "
                                            "titre after complete hydrolysis."),
    ("Why does the titre increase with time?", "Because acetic acid accumulates as the ester is hydrolysed, and "
                                               "the titration measures total acid."),
    ("What does (V_{\u221e} \u2212 V_{t}) represent?", "The acid still to be produced \u2014 that is, the "
                                                      "unreacted ester remaining, on the same proportional scale."),
    ("Why is (V_{\u221e} \u2212 V_{0}) used rather than V_{\u221e} alone?", "Because V_{0} removes the "
                                                                           "catalyst-acid contribution, leaving "
                                                                           "the acid corresponding to all the "
                                                                           "ester."),
    ("Write the working equation.", "k = (2.303/t) log_{10}[(V_{\u221e} \u2212 V_{0})/(V_{\u221e} \u2212 V_{t})]."),
    ("Where does 2.303 come from?", "It is ln 10; the integrated law is naturally in natural logarithms, and "
                                    "converting to base 10 divides the slope by 2.303."),
    ("How is k obtained graphically?", "Plot log_{10}[(V_{\u221e}\u2212V_{0})/(V_{\u221e}\u2212V_{t})] against t; "
                                       "the slope equals k/2.303, so k = 2.303 \u00d7 slope."),
    ("Why calculate k at several times?", "To test whether the model holds and to average out random error; a "
                                          "constant k is the numerical test of first-order behaviour."),
    ("Why is the mixture thermostatted?", "Because k depends strongly on temperature (Arrhenius); a drift in T "
                                          "produces a drift in k that mimics model failure."),
    ("Why is the aliquot quenched in ice-cold water?", "Cooling and dilution reduce the reaction rate sharply so "
                                                       "that the composition is effectively fixed during the "
                                                       "titration."),
    ("Why is the same aliquot volume essential?", "Because the titre is proportional to the amount of acid in the "
                                                  "aliquot; different volumes would not be comparable."),
    ("Why must the endpoint be faint pink rather than deep pink?", "Deep pink means excess alkali has been added, "
                                                                   "so the titre overestimates the acid and k is "
                                                                   "biased."),
    ("How is V_{\u221e} obtained?", "By heating the remaining mixture at 70\u201390 \u00b0C for 10\u201315 minutes "
                                     "to drive hydrolysis to completion, cooling, and titrating an aliquot of the "
                                     "same size."),
    ("What is the half-life, and how do you get it from k?", "t_{1/2} = 0.693/k; for a first-order reaction it is "
                                                             "independent of starting concentration."),
    ("What is the difference between order and molecularity?", "Order is an experimental exponent in the rate "
                                                                "law; molecularity is the number of species "
                                                                "colliding in an elementary step."),
]

VIVA_B = [
    ("Why is water in large excess?", "So that the fraction consumed is negligible and its concentration is "
                                      "constant to within about 0.1 %, permitting the pseudo-first-order "
                                      "treatment."),
    ("What would happen if water were not in excess?", "The rate law would be second order overall "
                                                       "(first order in each of ester and water) and the "
                                                       "integrated form would be different; a plot of "
                                                       "log(ester) against t would not be linear over the whole "
                                                       "run."),
    ("Why is HCl used rather than, say, NaOH?", "Hydrolysis is base-catalysed as well, but the experiment studies "
                                                "acid catalysis; acid also protonates the ester and provides a "
                                                "clean, non-consumed catalyst whose concentration is "
                                                "measurable by the same titration."),
    ("Why is the catalyst not consumed?", "It is regenerated when the products are released, so its concentration "
                                          "is constant throughout; that constancy is what allows it to be folded "
                                          "into k_{obs}."),
    ("Why does the acid speed up the reaction?", "Protonation of the carbonyl oxygen increases the "
                                                  "electrophilicity of the carbonyl carbon, and protonation of the "
                                                  "alkoxy oxygen turns a poor leaving group into a good one."),
    ("Why does the titre start at V_{0} rather than zero?", "Because the catalyst acid itself is titrated; V_{0} "
                                                           "is the acid present before any hydrolysis product "
                                                           "forms."),
    ("Why is the reaction followed by titration rather than by a physical method?", "Because the only change is "
                                                                                    "chemical: no colour, gas or "
                                                                                    "conductance change is large "
                                                                                    "enough. Titration of the acid "
                                                                                    "formed is simple and accurate."),
    ("Why is phenolphthalein suitable?", "Its colour change (colourless \u2192 pink) occurs in the weakly alkaline "
                                         "region, so it marks the point at which all the acid has been "
                                         "neutralised."),
    ("Why must the burette be rinsed with the titrant?", "Residual water would dilute the alkali and change its "
                                                         "effective concentration, biasing every titre."),
    ("Why is the reaction mixture stoppered?", "To prevent evaporation of the volatile ester, which would reduce "
                                               "its concentration and change the kinetics mid-run."),
    ("Why does the log plot have to pass through the origin?", "Because at t = 0 the log term is "
                                                               "log[(V_{\u221e}\u2212V_{0})/(V_{\u221e}\u2212V_{0})] "
                                                               "= log 1 = 0. A non-zero intercept indicates a "
                                                               "time offset or an error in V_{\u221e}."),
    ("Why do the last points become unreliable?", "Because (V_{\u221e} \u2212 V_{t}) becomes small, so a small "
                                                  "absolute titre error produces a large relative error in the "
                                                  "ratio and hence in k."),
    ("Why is the heating step at 70\u201390 \u00b0C rather than boiling?", "It is hot enough to complete the "
                                                                          "hydrolysis quickly but avoids bumping, "
                                                                          "excessive evaporation and loss of "
                                                                          "volatile components; the manual "
                                                                          "specifies this range."),
    ("Why is the cooled aliquot titrated immediately?", "To minimise any further hydrolysis and to keep the "
                                                        "titration at a consistent temperature."),
    ("Why does 2.303 \u00d7 slope give k, rather than the slope itself?", "Because the plot uses base-10 "
                                                                          "logarithms; the natural-log slope is k, "
                                                                          "and log_{10} = ln/2.303."),
    ("What does a non-constant k across the run indicate?", "Either the model fails (order is not first), or an "
                                                            "experimental variable drifted (temperature, V_{\u221e}, "
                                                            "timing, aliquot size)."),
    ("Why must you record the temperature on the report?", "Because k is only meaningful at a stated temperature; "
                                                           "without it the value cannot be compared or "
                                                           "reproduced."),
    ("Why is freshly distilled ester preferred?", "Commercial ester slowly hydrolyses on storage, so its true "
                                                  "concentration is uncertain and the starting point of the "
                                                  "kinetics is ill-defined."),
    ("Why is the initial concentration of ester needed at all, if it cancels?", "It does cancel in the ratio form, "
                                                                                "but it is needed to define k_{obs} "
                                                                                "in absolute terms and to compare runs "
                                                                                "at different starting concentrations."),
    ("What is the role of the ice bath in the arithmetic, not just the chemistry?", "It fixes the time at which the "
                                                                                    "composition is sampled, so the "
                                                                                    "recorded t corresponds to the "
                                                                                    "titre, not to the moment of "
                                                                                    "titration."),
]

VIVA_C = [
    ("What if you forgot to record V_{0}?", "You could still calculate k if the ester solution contributes no acid, "
                                            "by using V_{\u221e} in place of (V_{\u221e} \u2212 V_{0}); but that "
                                            "is an assumption, and you would have to state it. The rigorous fix is "
                                            "to repeat the run."),
    ("What if V_{\u221e} were measured too early?", "It would be too small; the denominator (V_{\u221e} \u2212 V_{t}) "
                                                    "would be too small, the log term too large, and k would be "
                                                    "overestimated, with increasing drift at later times."),
    ("What if the temperature rose by 5 \u00b0C during the run?", "k would rise (roughly 10 % per 2 \u00b0C near "
                                                                 "room temperature), so later points would give "
                                                                 "larger k values and the log plot would curve "
                                                                 "upward."),
    ("What if you used a larger aliquot for one point?", "That titre would be proportionally larger than it should "
                                                         "be, giving an anomalously low k; the point should be "
                                                         "identified and the run repeated."),
    ("What if the NaOH were 5 % weaker than labelled?", "Every titre would be larger by about 5 %, so V_{\u221e} and "
                                                        "V_{t} both scale by the same factor \u2014 and in the "
                                                        "//ratio// form the error cancels. The k value is therefore "
                                                        "little affected, though any absolute acid calculation would "
                                                        "be wrong."),
    ("What if you titrated a warm aliquot?", "The reaction would continue during titration and the indicator "
                                             "endpoint would be less sharp; the titre would correspond to an "
                                             "undefined, later time."),
    ("What if you used methyl acetate instead of ethyl acetate?", "The reaction is the same type, but the product "
                                                                  "is methanol rather than ethanol; the rate "
                                                                  "constant would differ because the ester "
                                                                  "structure differs."),
    ("What if the flask were open to the air?", "Ester would evaporate, lowering its concentration and changing "
                                                "k_{obs} in an uncontrolled way; the result would drift between "
                                                "runs."),
    ("What if the log plot is linear but does not pass through the origin?", "There is a time offset (mixing "
                                                                             "delay) or an error in V_{\u221e}; "
                                                                             "the slope, and hence k, is still "
                                                                             "approximately valid."),
    ("What if you plotted titre against time instead of the log term?", "You would get a curve, not a straight "
                                                                        "line; the first-order behaviour would be "
                                                                        "hidden, though the curve shape would still "
                                                                        "be monotonic."),
    ("What if the aliquot were not quenched at all?", "Hydrolysis would continue, so the titre would be higher than "
                                                      "the true value at the recorded time, and k would appear to "
                                                      "increase with time."),
    ("What if you added too much phenolphthalein?", "A large indicator blank consumes alkali and shifts the "
                                                    "endpoint, biasing the titre upward; two drops are enough."),
]

VIVA_D = [
    ("What is activation energy?", "The minimum energy that colliding species must possess for reaction to occur; "
                                   "it appears as E_{a} in the Arrhenius equation."),
    ("How would you determine E_{a}?", "Repeat the run at several temperatures, obtain k at each, and plot ln k "
                                       "against 1/T; the slope is \u2212E_{a}/R."),
    ("What is the pre-exponential factor A?", "A measure of the frequency and orientation of collisions; it "
                                              "includes the attempt frequency and steric factor."),
    ("What is the difference between rate and rate constant?", "Rate is the actual change in concentration per "
                                                               "time and depends on concentrations; the rate "
                                                               "constant is the proportionality in the rate law at "
                                                               "a given temperature."),
    ("Is this an elementary reaction?", "No. Ester hydrolysis proceeds through protonation, nucleophilic attack and "
                                        "collapse of a tetrahedral intermediate; it is a multi-step mechanism."),
    ("What does A_{AC}2 mean?", "Acid-catalysed, acyl-oxygen cleavage, bimolecular: the C\u2013O bond broken is the "
                                "acyl\u2013oxygen bond, and the rate-determining step is bimolecular."),
    ("Why is the equilibrium not driven completely to the right by acid alone?", "Esterification and hydrolysis are "
                                                                                 "opposite directions of the same "
                                                                                 "equilibrium; excess water and "
                                                                                 "removal of alcohol (or heating) "
                                                                                 "favour hydrolysis."),
    ("Could you follow the reaction by conductivity?", "Yes in principle \u2014 the number and mobility of ions "
                                                       "change as acid is consumed and produced \u2014 but with a "
                                                       "strong acid catalyst the change is small compared with "
                                                       "the background, so titration is more sensitive."),
    ("Could you follow it by pH?", "Similarly limited: the catalyst is a strong acid at roughly constant "
                                   "concentration, and the acetic acid formed is weak, so the pH change is modest "
                                   "and partly buffered."),
    ("What is the significance of a constant half-life?", "For a true first-order reaction, successive half-lives "
                                                          "are equal; observing roughly equal half-lives is a "
                                                          "direct experimental signature of first-order kinetics."),
    ("How would you show the reaction is first order in ester?", "Vary the initial ester concentration at fixed "
                                                                 "[H^{+}] and water, and show that k_{obs} is "
                                                                 "unchanged, while the initial rate is "
                                                                 "proportional to [ester]_{0}."),
    ("How would you show the reaction depends on water?", "Change the solvent composition (for example, add a "
                                                          "co-solvent to reduce water activity) and show that "
                                                          "k_{obs} changes; that proves water is chemically "
                                                          "involved despite its absence from the observed rate "
                                                          "law."),
    ("Why is the titre proportional to the amount of acid?", "Because acid and base react in a fixed stoichiometry; "
                                                             "the volume of standard alkali needed is directly "
                                                             "proportional to the moles of acid in the aliquot."),
    ("What is the significance of the intercept in the log plot?", "An intercept indicates a timing offset or an "
                                                                   "error in V_{\u221e}; a model-consistent run "
                                                                   "gives approximately zero."),
]

CH2_CHECK = checklist(
    "2.8",
    ["Reaction: CH_{3}COOC_{2}H_{5} + H_{2}O \u21cc CH_{3}COOH + C_{2}H_{5}OH (H^{+} catalysed).",
     "Water is the solvent at \u224855 mol L^{\u22121}; its concentration is effectively constant.",
     "Pseudo-first-order: observed rate = k_{obs}[ester].",
     "k_{obs} = k_{true}[H_{2}O][H^{+}] \u2014 constant concentrations folded in.",
     "True rate-determining step is bimolecular (A_{AC}2 mechanism).",
     "Integrated law: log_{10}([ester]_{0}/[ester]_{t}) = (k/2.303)t.",
     "Working equation: k = (2.303/t) log[(V_{\u221e}\u2212V_{0})/(V_{\u221e}\u2212V_{t})].",
     "V_{0} = catalyst only; V_{t} = catalyst + acid formed; V_{\u221e} = completion.",
     "(V_{\u221e} \u2212 V_{t}) is proportional to unreacted ester.",
     "Graphical k = 2.303 \u00d7 slope of log term versus time.",
     "Unit of k is time^{\u22121} (min^{\u22121} if t is in minutes).",
     "Half-life t_{1/2} = 0.693/k, independent of starting concentration.",
     "Arrhenius: k = A exp(\u2212E_{a}/RT); T must be constant and recorded.",
     "Quench in ice-cold water to freeze the composition before titration.",
     "Same aliquot volume, same pipette, every time.",
     "Endpoint is faint pink, not deep pink.",
     "V_{\u221e} requires heating at 70\u201390 \u00b0C for 10\u201315 min.",
     "NaOH must be standardised and kept stoppered (CO_{2}).",
     "Late points are unreliable because (V_{\u221e}\u2212V_{t}) becomes small.",
     "One supplied passage says methyl acetate \u2014 the aim says ethyl acetate."],
    ["Write the reaction, products and catalyst.",
     "Why is the reaction pseudo-first-order?",
     "Define V_{0}, V_{t}, V_{\u221e} and say what each contains.",
     "Write the working rate equation and explain 2.303.",
     "Why is temperature controlled, and how does it enter quantitatively?",
     "Why is the aliquot quenched in ice water?",
     "How is V_{\u221e} determined and why does it matter so much?",
     "How do you obtain k from a graph?",
     "What would a non-constant k indicate?",
     "What is the difference between order and molecularity?"],
    ["Derive the working equation from the integrated first-order law, starting from the definition of the "
     "titres.",
     "Explain exactly which errors cancel in the ratio form and which do not, and why.",
     "If your k values fall steadily with time, list the possible causes and the diagnostic that distinguishes "
     "between them.",
     "Show that the true reaction is second order overall but that the observed law is first order, and state "
     "the condition for that to hold.",
     "How would you measure the activation energy, and what would a curved Arrhenius plot mean?",
     "Why is a non-zero intercept in the log plot a diagnostic rather than a failure of the theory?",
     "Explain why the alkali concentration cancels from the ratio, but not from an absolute acid determination.",
     "How would you prove experimentally that water is involved despite its absence from the observed rate law?",
     "What is the maximum fractional change in [H_{2}O] in your run, and is the excess condition really satisfied?",
     "Compare pseudo-first-order with a true first-order reaction such as radioactive decay."],
    [("Order vs molecularity", "Order is experimental; molecularity applies to an elementary step."),
     ("Rate vs rate constant", "Rate depends on concentrations; k is a constant at fixed T."),
     ("Pseudo-first-order vs first-order", "The former is a limiting case created by excess reagent."),
     ("V_{\u221e} vs last titre", "V_{\u221e} requires demonstrated completion; the last titre does not."),
     ("Phenolphthalein faint vs deep pink", "Faint pink is the endpoint; deep pink is overtitration."),
     ("Time of quenching vs time of titration", "The recorded t belongs to the quench."),
     ("k in min^{\u22121} vs s^{\u22121}", "A factor of 60, and a classic lost-mark error."),
     ("Ethyl acetate vs methyl acetate", "Different alcohol product, different k; only one matches the aim.")],
    (["Relation", "Expression", "Note"],
     [["Rate law (true)", "rate = k_{true}[ester][H_{2}O][H^{+}]", "Second order in the simplified model"],
      ["Observed rate law", "rate = k_{obs}[ester]", "Pseudo-first-order"],
      ["Integrated law", "ln([ester]_{0}/[ester]_{t}) = k t", "Natural log form"],
      ["Base-10 form", "log_{10}(ratio) = (k/2.303)t", "Matches the manual"],
      ["Working equation", "k = (2.303/t)log[(V_{\u221e}\u2212V_{0})/(V_{\u221e}\u2212V_{t})]", "Titre form"],
      ["Graphical k", "k = 2.303 \u00d7 slope", "Slope of log term vs t"],
      ["Half-life", "t_{1/2} = 0.693/k", "Independent of [ester]_{0}"],
      ["Arrhenius", "ln k = ln A \u2212 E_{a}/RT", "Slope \u2212E_{a}/R"]],
     [34, 76, 58]),
    [["Titre decreases with time", "Aliquots mislabelled or burette misread"],
     ["V_{\u221e} only slightly above the last titre", "Reaction not driven to completion"],
     ["k falls steadily through the run", "Temperature falling, or V_{\u221e} too small"],
     ["k rises steadily through the run", "Temperature rising, or V_{\u221e} too large"],
     ["Log plot curves upward at late times", "V_{\u221e} underestimated"],
     ["Endpoint pale and unstable", "Aliquot still warm or too little indicator"],
     ["Values 60\u00d7 too large", "Time recorded in seconds but reported as minutes"],
     ["Large positive intercept", "Timing offset between mixing and first aliquot"]],
    ["The alkali concentration cancels in the ratio form \u2014 know why.",
     "V_{\u221e} is a //measured// quantity that must be justified by heating.",
     "The A_{AC}2 mechanism explains why the acid accelerates the reaction.",
     "The term \u201cpseudo\u201d is a statement about conditions, not about the mechanism.",
     "Ester evaporation is a silent, systematic error.",
     "Half-lives are equal for a true first-order reaction.",
     "The factor 2.303 is ln 10, and it recurs in every base-10 kinetics plot."],
    ["Reporting k without its unit or without the run temperature.",
     "Using the last kinetic titre as V_{\u221e}.",
     "Starting the clock at the first titration rather than at mixing.",
     "Titrating warm, unquenched aliquots.",
     "Drawing the graph without labelling the log term correctly.",
     "Confusing ethyl acetate with methyl acetate in the write-up.",
     "Failing to state which form of the rate equation was used."],
    ["Ethyl acetate hydrolyses in aqueous acid to acetic acid and ethanol. Water is the solvent, so its "
     "concentration is effectively constant, and the acid catalyst is regenerated, so its concentration is "
     "constant too; both fold into a single observed rate constant, making the reaction pseudo-first-order in "
     "ester. I follow the reaction by withdrawing identical aliquots at recorded times, quenching each in "
     "ice-cold water to stop further hydrolysis, and titrating the acetic acid formed with standard sodium "
     "hydroxide to a faint phenolphthalein endpoint. Three titres define the experiment: V_{0} before reaction, "
     "V_{t} at time t, and V_{\u221e} after heating the mixture to 70\u201390 \u00b0C to complete the hydrolysis. "
     "The unreacted ester remaining is proportional to (V_{\u221e} \u2212 V_{t}), so the integrated first-order "
     "law becomes k = (2.303/t) log[(V_{\u221e}\u2212V_{0})/(V_{\u221e}\u2212V_{t})]. A plot of that logarithm "
     "against time is a straight line whose slope gives k = 2.303 \u00d7 slope. Constant temperature, identical "
     "aliquots, prompt quenching, a consistent endpoint and a correctly determined V_{\u221e} are what make the "
     "result trustworthy."],
    ["**Rate = k_{obs}[ester]** \u2192 **integrate** \u2192 **log ratio = (k/2.303)t** \u2192 **slope \u00d7 "
     "2.303 = k**.",
     "**V_{0} catalyst \u00b7 V_{t} catalyst + product \u00b7 V_{\u221e} everything.**",
     "**Quench in ice, titrate to faint pink, keep T constant.**",
     "**No heating, no V_{\u221e}; no V_{\u221e}, no k.**"]
)

CH2 = {
    "key": "hydrolysis",
    "num": "2",
    "kicker": "Experiment 2  \u00b7  Chemical kinetics",
    "title": "Kinetics of Acid-Catalysed Hydrolysis of Ethyl Acetate",
    "toc": "Acid-catalysed hydrolysis of ethyl acetate",
    "standfirst": "A reaction you cannot see, followed entirely by titration. This chapter builds the "
                  "pseudo-first-order treatment from the mechanism upward and turns three titres into a rate "
                  "constant.",
    "body": B + [
        ("h2", "2.7  Viva question bank"),
        ("p", "Seventy-one answered questions, grouped as an examiner would group them. The cross-questioning "
              "chain at the end of the theory bank shows how a single \u201cwhy\u201d can be extended five "
              "questions deep."),
        ("qsub", "A.  Fundamental questions"),
        ("qa", VIVA_A),
        ("qsub", "B.  \u201cWhy\u201d and \u201chow\u201d questions"),
        ("qa", VIVA_B),
        ("qsub", "C.  \u201cWhat if\u201d questions"),
        ("qa", VIVA_C),
        ("qsub", "D.  Tricky and advanced questions"),
        ("qa", VIVA_D),
    ] + CH2_CHECK,
}
