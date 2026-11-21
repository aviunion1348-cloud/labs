"""Chapter 1 - Spectrophotometry of cobalt chloride."""

B = []

# ---------------------------------------------------------------- aim & map
B += [
    ("h2", "1.1  What this experiment is, and why you perform it"),
    ("lead", "You are given a solution of cobalt(II) chloride whose concentration is not stated. "
             "You must find it. The instrument you will use does not measure cobalt at all: it measures "
             "how much light the solution removes from a beam. This chapter builds the bridge between those "
             "two facts \u2014 from the colour of the liquid to a number in per cent (w/v)."),
    ("p", "The experiment has three parts that must be done in order, because each one feeds the next. "
          "First you **find the wavelength at which the solution absorbs most strongly**. Second you "
          "**prove that absorbance is proportional to concentration** at that wavelength, using standards "
          "you prepare yourself. Third you **interpolate the unknown** from that proportional relationship. "
          "Skipping the first step does not make the experiment impossible, but it makes it insensitive; "
          "skipping the second makes the third meaningless, because you would have no basis for converting an "
          "absorbance into a concentration."),
    ("defbox", [
        ("Spectrophotometry", "An instrumental method that measures the fraction of light of a chosen wavelength "
                              "absorbed by a sample, and relates that absorbance to the amount of absorbing "
                              "species present."),
        ("Absorbance (A)", "A logarithmic measure of light attenuation, A = log_{10}(I_{0}/I). It is a pure "
                           "number and carries no units."),
        ("Transmittance (T)", "The fraction of incident light that passes through the sample, T = I/I_{0}. "
                              "Percentage transmittance %T = 100T."),
        ("\u03bb_{max}", "The wavelength at which absorbance reaches a maximum for the species in question. "
                        "It is a property of the coloured species, not of the instrument."),
        ("Blank", "A reference sample containing everything in the solution except the analyte, used to set "
                  "100 % T / zero absorbance."),
        ("Calibration curve", "A graph of absorbance against known concentration, against which an unknown "
                              "absorbance is interpreted."),
    ]),
    ("p", "Colour, in the everyday sense, is not a physical quantity \u2014 so the whole experiment rests on "
          "turning colour into arithmetic. Aqueous cobalt(II) is pink to red because the hydrated "
          "hexaaquacobalt(II) ion, [Co(H_{2}O)_{6}]^{2+}, absorbs in the green\u2013yellow region and transmits "
          "what is left, which the eye reads as pink. The absorption band is broad, with a maximum near 510\u2013"
          "515 nm. That single fact explains the entire design: work near 510 nm, where a small change in cobalt "
          "concentration produces the largest measurable change in absorbance."),
    ("box", "key", [
        "The instrument measures **light**, not cobalt. The calibration line is the dictionary that translates "
        "one into the other.",
        "All quantitative work is done at a **single fixed wavelength**, chosen from the spectrum you measured. "
        "Changing wavelength halfway through the standards invalidates every reading.",
    ], "Three ideas that make the experiment logical"),
    ("fig", "spectro", "**Figure 1.1** Optical path of a single-beam visible spectrophotometer. Light from the "
                       "lamp is dispersed by the monochromator, passes through the sample cell and is detected. "
                       "The blank replaces the sample to define I\u2080."),
    ("h3", "Where this method is used outside the laboratory"),
    ("bul", [
        "**Water analysis:** residual chlorine, iron, fluoride, nitrate and phosphate are all measured "
        "colorimetrically after conversion to a coloured derivative.",
        "**Clinical chemistry:** haemoglobin, bilirubin and creatinine assays are read as absorbance changes, "
        "on the same principle, in every hospital analyser.",
        "**Pharmaceutical quality control:** content uniformity and dissolution testing depend on absorbance "
        "measurements of dissolved drug.",
        "**Environmental monitoring:** colour is one of the classical regulatory parameters for industrial "
        "effluent, precisely because it can be reduced to absorbance.",
        "**Process control:** purity of dye batches and the strength of coloured beverages are monitored "
        "continuously by in-line photometry.",
    ]),
]

# ---------------------------------------------------------------- theory
B += [
    ("h2", "1.2  The theory, built from the beginning"),
    ("h3", "1.2.1  What happens to light when it enters a coloured solution"),
    ("p", "A beam of light carries energy distributed over a range of wavelengths. When it enters a solution "
          "containing a coloured ion, a fraction of the photons has exactly the energy needed to promote electrons "
          "in that ion from a lower to a higher orbital. Those photons are absorbed \u2014 their energy is retained "
          "by the ion. Photons of other energies pass through essentially unhindered. What emerges is therefore "
          "weaker than what entered, and it is also **selectively weakened**: the missing wavelengths are exactly "
          "the ones the ion can absorb."),
    ("p", "For cobalt(II) in water, the d\u2013d transitions of the 3d^{7} ion are responsible for absorption in the "
          "visible. Because the geometry and ligands of the hydrated ion are loosely defined and constantly "
          "fluctuating in solution, the transition energies are not sharp. The result is a **broad band**, not a "
          "line. Broad bands are analytically convenient: a 5 nm setting error on a broad band costs very little "
          "signal, whereas on a sharp line it could cost everything."),
    ("p", "Two separate things happen to the beam, and the method depends on keeping them separate:"),
    ("bul", [
        "**Absorption** removes photons by transferring their energy to the sample. This is what carries chemical "
        "information, and it is what Beer\u2019s law describes.",
        "**Scattering** redirects photons without absorbing them, and **reflection** sends them back at the cell "
        "walls. Neither carries the concentration information you want. Both are the reason fingerprints, "
        "scratches, bubbles and turbidity are treated as fatal errors rather than minor annoyances.",
    ]),
    ("h3", "1.2.2  From \(I\) and \(I_{0}\) to a number you can plot"),
    ("p", "Transmittance is the obvious first quantity: divide what gets through by what went in. It is also a "
          "poor choice for plotting, for a simple reason. If you double the concentration, you double the "
          "**absorbing centres** in the beam and therefore double the fraction of photons removed \u2014 but "
          "transmittance does not halve. It falls multiplicatively. In a 1 cm cell, one unit of concentration "
          "might transmit 50 %; two units transmit 25 %; three units transmit 12.5 %. A plot of T against c is "
          "an exponential decay, which is impossible to read accurately and impossible to extrapolate."),
    ("p", "Absorbance is defined to undo that multiplication. Taking the logarithm converts the geometric decay "
          "into a straight line:"),
    ("eq", "A = log_{10}(I_{0}/I) = \u2212log_{10} T = 2 \u2212 log_{10}(%T)",
     "Equation 1.1 \u2014 absorbance in terms of transmittance; the last form is the one you use when the "
     "instrument reads in %T."),
    ("p", "The practical consequence is worth memorising as three pairs of numbers. A = 0 corresponds to 100 %T; "
          "A = 1 to 10 %T; A = 2 to 1 %T. Each unit of absorbance is a factor of ten in transmitted light. "
          "For this reason an absorbance of 1.0 is often quoted as the ideal working value \u2014 there is still "
          "plenty of light reaching the detector, and the quantity is still changing usefully with concentration."),
    ("h3", "1.2.3  Beer\u2013Lambert law, and what each symbol really means"),
    ("eq", "A = \u03b5 l c",
     "Equation 1.2 \u2014 the Beer\u2013Lambert law for monochromatic light and a dilute, non-scattering solution."),
    ("tbl", ["Symbol", "Meaning", "Usual unit", "What it controls in your experiment"],
     [["A", "Absorbance", "dimensionless", "The measured quantity; must lie in the instrument\u2019s reliable range"],
      ["\u03b5", "Molar absorptivity (extinction coefficient)", "L mol^{\u22121} cm^{\u22121}",
       "A property of the species at that wavelength; fixed when you fix \u03bb"],
      ["l", "Optical path length", "cm", "Fixed by the cuvette \u2014 never change cuvette mid-series"],
      ["c", "Concentration of the absorbing species", "mol L^{\u22121} (or % w/v, if \u03b5 is redefined)",
       "The unknown you are determining"]],
     [18, 48, 30, 74], "**Table 1.1** The four quantities in Beer\u2013Lambert law. Note that \u03b5 absorbs the "
                       "units of c, so the law is dimensionally consistent whichever concentration unit you use.",
     ["c", "l", "c", "l"]),
    ("p", "The law is really two laws fused into one. **Lambert\u2019s law** says that absorbance is proportional "
          "to path length: double the thickness of absorbing solution and you double the absorption, because you "
          "have doubled the number of absorbing centres in the beam. **Beer\u2019s law** says that absorbance is "
          "proportional to concentration at fixed path length: double the concentration and you again double the "
          "number of centres. Writing both proportionalities together gives A = \u03b5lc, with \u03b5 as the "
          "combined constant."),
    ("h3", "1.2.4  Derivation of the Beer\u2013Lambert law"),
    ("p", "The derivation is short and it tells you exactly when the law will fail, which is why it is worth "
          "following. Consider a slab of solution of thickness dx at depth x. The light intensity there is I. "
          "The probability that a photon is absorbed in that slab is proportional to the number of absorbing "
          "molecules it meets, which is proportional to concentration and to thickness. Therefore:"),
    ("eq", "\u2212dI = k c I dx   \u21d2   \u2212dI/I = k c dx",
     "Equation 1.3 \u2014 differential form: the fractional loss of intensity is proportional to concentration "
     "and path increment."),
    ("p", "Integrating from x = 0 (intensity I_{0}) to x = l (intensity I):"),
    ("eq", "\u222b dI/I (from I\u2080 to I) = \u2212kc \u222b dx (from 0 to l)   \u21d2   ln(I\u2080/I) = kcl"),
    ("eq", "\u21d2   log_{10}(I_{0}/I) = (k/2.303) c l = \u03b5 c l",
     "Equation 1.4 \u2014 integrating and converting to base 10 gives the familiar form, with \u03b5 = k/2.303."),
    ("p", "Every assumption of the law is visible in that derivation, and every deviation from linearity you "
          "will ever see in a laboratory traces back to one of them:"),
    ("bul", [
        "**The absorber must be the only absorber.** If the solvent, the cell or another solute also absorbs at "
        "the chosen wavelength, the measured A is a sum, not a single term. The blank removes the constant part; "
        "it cannot remove an interference that varies with the sample.",
        "**The beam must be monochromatic.** \u03b5 is defined at one wavelength. If the bandpass is wide and "
        "\u03b5 changes steeply across it, the effective \u03b5 drifts with concentration and the line bends.",
        "**The solution must not scatter.** Suspended particles remove light without obeying Beer\u2019s law and "
        "inflate absorbance unpredictably.",
        "**The absorbing species must not change with concentration.** Association, dimerisation, ion pairing, "
        "complexation or pH-driven speciation changes what is actually absorbing; at high cobalt concentrations "
        "the chloro-complexes and hydration equilibria can shift the band.",
        "**The concentration must be low enough.** At high absorbance (roughly A > 1.2\u20131.5, depending on the "
        "instrument) stray light becomes a significant fraction of the transmitted beam and the measured "
        "absorbance saturates below its true value.",
    ]),
    ("h3", "1.2.5  Why \u03bb_{max} is chosen, quantitatively"),
    ("p", "Sensitivity is the rate at which absorbance responds to concentration, and from Beer\u2019s law that "
          "rate is \u03b5l. So you want the wavelength where \u03b5 is largest \u2014 the absorption maximum. "
          "There is a second, less obvious reason: **tolerance to wavelength error**. If the monochromator is "
          "set 2 nm away from the intended wavelength, the error in \u03b5 is proportional to the slope "
          "d\u03b5/d\u03bb. At the peak that slope is zero, so first-order setting errors cancel \u2014 the "
          "measurement is at a stationary point. On the steep flank of the band, the same 2 nm error produces a "
          "large change in \u03b5, and the calibration line silently shifts."),
    ("p", "This is a general principle worth carrying into every optical measurement: **operate at a maximum or "
          "minimum of the response curve when you can.** The physics is stationary there, so small errors in the "
          "independent variable matter least."),
    ("plot", "spectrum", "**Figure 1.2** Absorbance spectrum of aqueous cobalt(II) chloride. The broad band with "
                         "\u03bbmax near 511 nm is the analytical band; the weak feature near 615 nm is a "
                         "spin-forbidden transition of much lower intensity. The curve is illustrative of the "
                         "shape reported in the supplied material, not a measured data set."),
    ("h3", "1.2.6  How the calibration line becomes a concentration"),
    ("p", "With l fixed and \u03bb fixed, Beer\u2019s law reduces to a straight line through the origin: "
          "A = (\u03b5l)c. In practice you fit the line A = mc + b by least squares to your standards. The slope "
          "m has units of absorbance per unit concentration and equals \u03b5l; the intercept b should be "
          "statistically indistinguishable from zero once the blank has been correctly set."),
    ("eq", "c_{unknown} = (A_{unknown} \u2212 b)/m \u00d7 DF",
     "Equation 1.5 \u2014 interpolation on the calibration line. DF is the dilution factor, equal to 1 if the "
     "unknown was measured undiluted."),
    ("p", "The word **interpolation** is doing real work here. Reading a value between your standards is supported "
          "by the data you actually collected. Reading beyond the highest standard is extrapolation, and it "
          "assumes the line continues to behave when nothing in your experiment tests that assumption. If the "
          "unknown reads above your top standard, **dilute it** and multiply by the dilution factor; do not extend "
          "the graph."),
    ("plot", "calibration", "**Figure 1.3** Calibration plot with an interpolated unknown. The dashed line is the "
                            "least-squares fit; the horizontal and vertical construction lines show how an "
                            "absorbance of 0.412 maps to a concentration. Values shown are illustrative only \u2014 "
                            "the supplied material contains blank tables, and no experimental readings are invented here."),
    ("box", "exam", [
        "A common examiner trap: \u201cYour graph does not pass exactly through the origin. Is Beer\u2019s law "
        "wrong?\u201d The correct answer is that a finite intercept usually indicates a **blank or baseline "
        "offset, a matrix effect, or stray light** \u2014 an experimental imperfection \u2014 rather than a failure "
        "of the law. The law predicts proportionality; the intercept is a measure of your instrumental zero.",
        "Second trap: \u201cWhy not simply use A = \u03b5lc with a handbook value of \u03b5 instead of making "
        "standards?\u201d Because handbook \u03b5 values refer to a specified species, solvent, bandpass and "
        "temperature; your instrument, cell and sample matrix differ. The calibration curve calibrates **your** "
        "system.",
    ], "Two examiner traps in the theory"),
]

# ---------------------------------------------------------------- apparatus
B += [
    ("h2", "1.3  Apparatus, and what each part actually does"),
    ("tbl", ["Item", "Function", "What goes wrong if it is faulty, dirty or missing"],
     [["Visible spectrophotometer (single beam)", "Selects a wavelength, passes light through the sample, "
       "detects transmitted intensity and displays A or %T", "Drift from an unwarmed lamp; wrong readings from a "
       "mis-set wavelength or a stray-light-limited detector"],
      ["Cuvettes / matched glass tubes", "Define the optical path length l and hold the sample square to the beam",
       "Scratches, fingerprints, bubbles and mismatched path lengths all corrupt the reading"],
      ["Volumetric (measuring) flasks", "Prepare standards to an exact final volume",
       "A wrong or uncalibrated flask makes every stated concentration wrong by the same factor"],
      ["Beakers, glass rod", "Dissolve and transfer solid CoCl_{2}; stir",
       "Incomplete dissolution leaves undissolved solid and an unknown true concentration"],
      ["Analytical balance", "Weigh the CoCl_{2} that defines the standard concentrations",
       "Zero error or draughts bias every concentration systematically"],
      ["Distilled water", "Solvent and blank medium", "Tap water adds ions and background absorbance"],
      ["Tissue paper (lint-free)", "Wipe the optical faces",
       "Fibres left behind scatter light and raise apparent absorbance"],
      ["Pipette / dropper", "Transfer reproducible volumes for dilution",
       "Inconsistent aliquots change the concentration actually delivered"]],
     [34, 62, 74], "**Table 1.2** Apparatus inventory. The right-hand column is the one examiners use to test "
                   "whether you understand the instrument or have merely memorised a list.", ["l", "l", "l"]),
    ("h3", "1.3.1  How the spectrophotometer produces a number"),
    ("num", [
        "A **tungsten\u2013halogen lamp** provides a continuum across the visible region (roughly 350\u20131000 nm).",
        "A **monochromator** \u2014 a prism or, in modern instruments, a diffraction grating \u2014 disperses that "
        "continuum. A narrow exit slit selects a band of wavelengths, typically 5\u201310 nm wide. This band is "
        "what \u201cmonochromatic\u201d means in practice, and it is why the bandpass specification matters.",
        "A **beam splitter or a moving cell holder** allows the same optical path to be used for blank and sample "
        "in a single-beam instrument; the blank is measured first and its intensity stored as I_{0}.",
        "The **photodetector** (photodiode or photomultiplier) converts transmitted intensity into a current, "
        "which the electronics convert into absorbance using the stored I_{0}.",
        "The **display** shows A or %T. The internal conversion is exactly Equation 1.1 \u2014 which is why setting "
        "100 %T with the blank is the same operation as setting zero absorbance.",
    ]),
    ("box", "note", [
        "**Why a 15-minute warm-up?** The lamp output and the detector response both drift while the instrument "
        "reaches thermal equilibrium. If you blank immediately after switching on, the stored I_{0} corresponds to "
        "a cold lamp; twenty minutes later the lamp is brighter and every absorbance reads falsely low. The "
        "supplied manual specifies a warm-up of about 15 minutes \u2014 treat this as a measurement step, not as "
        "waiting time.",
    ], "Instrument behaviour, not ritual"),
    ("h3", "1.3.2  Cuvettes: the cheapest source of serious error"),
    ("p", "The cuvette is not a container; it is a precision optical component. Its two clear faces must be "
          "parallel and flat, its path length must match its nominal value, and its transmission must be uniform "
          "across the face. Four habits follow, and each one is worth marks in a viva:"),
    ("bul", [
        "**Handle by the frosted sides only.** A fingerprint is a thin film of oil and salt that both absorbs and "
        "scatters; it can add 0.05\u20130.2 absorbance units.",
        "**Fill to the same height every time.** In a single-beam instrument with a tall beam, changing the fill "
        "height changes how much of the beam samples liquid.",
        "**Use the same cuvette, in the same orientation, for blank, standards and unknown.** \u201cMatched\u201d "
        "cuvettes are matched to a tolerance, not to perfection; rotating a cuvette 90\u00b0 can change the "
        "reading by a few thousandths.",
        "**Check for bubbles and never tap the cell over the bench.** A single bubble in the beam can produce "
        "wildly erratic readings that look like instrument noise.",
    ]),
]

# ---------------------------------------------------------------- procedure
B += [
    ("h2", "1.4  Procedure, step by step, with the reasoning"),
    ("p", "The sequence below follows the supplied manual: warm-up, blanking, a wavelength scan in 20 nm steps, "
          "selection of \u03bb_{max}, then absorbance of the standards and finally of the unknown. The manual\u2019s "
          "handwritten wavelength entry is not legible, so the exact scan start is confirmed with your instructor; "
          "the structure of the procedure is not in doubt."),
    ("h3", "Part A \u2014 Preparation"),
    ("num", [
        "**Clean the glassware and rinse with distilled water.** Residual acid or detergent changes both the "
        "absorbance and, if it alters pH, the speciation of cobalt.",
        "**Prepare the blank: distilled water only.** The blank must contain everything present in the standards "
        "*except* the analyte. Since CoCl_{2} is simply dissolved in water, the blank is water.",
        "**Prepare the standard series.** The supplied material specifies 0.2 %, 0.5 %, 1.0 %, 1.5 %, 2.0 %, "
        "2.5 % and 3.0 % cobalt chloride solutions. **Confirm the percentage basis with your instructor before "
        "weighing** \u2014 w/v (g per 100 mL) and w/w (g per 100 g) differ by the density of the solution, and the "
        "handwritten source does not resolve which is intended.",
        "**Label every flask with its concentration and the date.** Unlabelled flasks are the classic route to a "
        "calibration line with one point belonging to the wrong standard.",
    ]),
    ("box", "caution", [
        "Cobalt(II) salts are classified as hazardous to health and the environment; cobalt chloride is also "
        "hygroscopic, so weigh quickly and keep the container closed. Do not pipette by mouth, do not pour "
        "cobalt solutions down the sink unless your institution specifically permits it, and follow the "
        "laboratory\u2019s cobalt waste route.",
    ], "Handling note"),
    ("h3", "Part B \u2014 Warm-up and blanking"),
    ("num", [
        "**Switch on and allow about 15 minutes** for the lamp and detector to stabilise.",
        "**Set the mode** to absorbance (or %T, if the manual requires that for the scan) and set the gain or "
        "sensitivity control as the instrument instructions direct.",
        "**Set 0 %T with the shutter closed or the light path blocked.** This defines the electrical zero of the "
        "detector and must be done *before* the 100 %T adjustment.",
        "**Insert the blank, close the lid, and set 100 %T (A = 0).** This stores I_{0}. Never set 100 %T with a "
        "sample in the beam.",
        "**Remove the blank and confirm the reading is stable and sensible.** An unstable blank reading means a "
        "lamp still warming, a loose cuvette or a dirty cell.",
    ]),
    ("box", "pitfall", [
        "Setting 100 %T with an empty holder instead of a water-filled cuvette is the single most common "
        "beginner\u2019s error. The empty holder removes the reflection and absorption of the cell walls and of the "
        "water itself; every subsequent absorbance is then offset, and the whole calibration line shifts down.",
    ], "The classic blanking error"),
    ("h3", "Part C \u2014 Find \u03bb_{max}"),
    ("num", [
        "**Fill the cuvette with one of the mid-range standards** (a mid concentration gives a well-shaped peak "
        "without saturating the detector).",
        "**Scan from the starting wavelength at 20 nm intervals**, recording absorbance at every setting. Move in "
        "one direction only; sweeping back and forth invites backlash error in the monochromator drive.",
        "**Plot absorbance against wavelength** and identify the wavelength of maximum absorbance.",
        "**Refine near the peak** with 5 nm or 2 nm steps if your instrument allows, so that the reported "
        "\u03bb_{max} is not merely the coarse grid point that happened to be highest.",
    ]),
    ("box", "note", [
        "Why 20 nm steps? Because the cobalt band is broad \u2014 tens of nanometres wide \u2014 so a 20 nm grid "
        "locates the peak adequately and covers the visible range in a manageable number of readings. The same "
        "step size on a sharp, narrow band (a rare-earth f\u2013f transition, for instance) would miss the maximum "
        "entirely. **Scan step must be fine relative to the width of the feature you are hunting.**",
    ], "Why the scan step is legitimate"),
    ("h3", "Part D \u2014 Calibration"),
    ("num", [
        "**Fix the instrument at \u03bb_{max}** and do not change it for the rest of the experiment.",
        "**Re-blank** at this wavelength \u2014 the blank\u2019s own absorbance may be small but non-zero at a new "
        "setting.",
        "**Measure each standard from lowest to highest concentration**, recording absorbance. Working upwards "
        "keeps carry-over contamination from a strong solution into a weak one to a minimum.",
        "**Rinse the cuvette with a little of the next solution** before filling it, so the previous, more "
        "concentrated solution is not diluted into the next reading.",
        "**Plot A against c and fit a straight line.** Inspect residuals: a systematic curvature means you have "
        "left the linear range.",
    ]),
    ("h3", "Part E \u2014 The unknown"),
    ("num", [
        "**Measure the unknown at the same wavelength**, with the same cuvette and the same blank correction.",
        "**Check that its absorbance lies inside the range spanned by the standards.** If it is above, dilute a "
        "known volume to a known final volume and record the dilution factor DF.",
        "**Read the concentration from the fitted line**, not by eye from a hand-drawn best-fit, and multiply by "
        "DF if applicable.",
        "**State the result with its uncertainty and units** \u2014 for example \u201c1.22 \u00b1 0.03 % (w/v)\u201d, "
        "quoting whichever basis the standards were prepared on.",
    ]),
]

# ---------------------------------------------------------------- observations
B += [
    ("h2", "1.5  Observations, tables and calculation"),
    ("tbl", ["S. No.", "Wavelength \u03bb (nm)", "Absorbance A", "Remark"],
     [["1", "400", "", "start of scan"], ["2", "420", "", ""], ["3", "440", "", ""],
      ["4", "460", "", ""], ["5", "480", "", ""], ["6", "500", "", ""], ["7", "520", "", "near \u03bbmax"],
      ["8", "540", "", ""], ["9", "560", "", ""], ["10", "580", "", ""], ["11", "600", "", ""],
      ["12", "620", "", ""], ["13", "640", "", ""], ["14", "660", "", ""], ["15", "680", "", ""],
      ["16", "700", "", "end of scan"]],
     [16, 40, 34, 80], "**Table 1.3** Observation table for the wavelength scan. Record actual readings; this "
                       "template leaves the data cells blank because the supplied source contains no measured values.",
     ["c", "c", "c", "l"]),
    ("tbl", ["S. No.", "Standard concentration (%)", "Absorbance at \u03bbmax", "A/c"],
     [["1", "0.2", "", ""], ["2", "0.5", "", ""], ["3", "1.0", "", ""], ["4", "1.5", "", ""],
      ["5", "2.0", "", ""], ["6", "2.5", "", ""], ["7", "3.0", "", ""]],
     [16, 52, 52, 50], "**Table 1.4** Calibration table. The fourth column, A/c, is a diagnostic: it should be "
                       "approximately constant across the series. A systematic fall in A/c at the top of the range "
                       "is the signature of stray light or of chemical change in concentrated solutions.",
     ["c", "c", "c", "c"]),
    ("h3", "1.5.1  Worked sample calculation"),
    ("p", "The following arithmetic is an **illustration of method only**; the numbers are chosen for convenience "
          "and are not measurements from the supplied material."),
    ("p", "Suppose the least-squares fit to the standards in Table 1.4 gives **A = 0.332 c + 0.005**, and the "
          "unknown reads **A = 0.412** in a 1 cm cell. Then:"),
    ("eq", "c = (0.412 \u2212 0.005)/0.332 = 0.407/0.332 = 1.226 % (w/v)"),
    ("p", "If the unknown had been diluted five-fold before measurement to bring it into range, the "
          "concentration of the original sample would be 1.226 \u00d7 5 = 6.13 % (w/v). Note that the dilution "
          "factor is applied to the **result**, not to the absorbance."),
    ("p", "It is worth knowing what the slope means physically. With c in % (w/v) \u2014 that is, g per 100 mL "
          "\u2014 the slope has units of absorbance per % and equals \u03b5l converted to that concentration scale. "
          "For CoCl_{2} (M = 129.84 g mol^{\u22121}), 1 % w/v is 10 g L^{\u22121}, which is 10/129.84 = 0.0770 "
          "mol L^{\u22121}. If the fitted slope is 0.332 per %, then \u03b5l = 0.332/0.0770 = 4.31 L mol^{\u22121}, "
          "and with l = 1 cm, \u03b5 \u2248 4.3 L mol^{\u22121} cm^{\u22121}. Quoting \u03b5 makes your data "
          "comparable with published spectra \u2014 and an examiner may well ask you to do exactly this conversion."),
    ("tbl", ["Quantity", "Expression", "Result (illustrative)"],
     [["Slope of calibration line, m", "\u03b5l (in the chosen concentration units)", "0.332 A per %"],
      ["Intercept, b", "baseline / blank offset", "0.005 A"],
      ["Unknown absorbance", "measured", "0.412 A"],
      ["Unknown concentration", "(A \u2212 b)/m", "1.23 % (w/v)"],
      ["Molar concentration equivalent", "1.23 \u00d7 10/129.84", "0.0947 mol L^{\u22121}"],
      ["Molar absorptivity (l = 1 cm)", "\u03b5 = m \u00d7 129.84/10", "\u2248 4.3 L mol^{\u22121} cm^{\u22121}"]],
     [46, 66, 58], "**Table 1.5** Calculation summary. Keep the chain of units visible at every line \u2014 most "
                   "lost marks in this experiment come from unit slips, not from chemistry.",
     ["l", "l", "c"]),
]

# ---------------------------------------------------------------- errors
B += [
    ("h2", "1.6  Precautions, errors and troubleshooting"),
    ("h3", "1.6.1  Precautions that actually protect the result"),
    ("bul", [
        "Warm the instrument up for the specified time before blanking; **re-blank after any wavelength change**.",
        "Use one cuvette, one orientation and one fill height for blank, standards and unknown.",
        "Handle cuvettes by the frosted faces and wipe the optical faces with lint-free tissue **just before** "
        "insertion.",
        "Prepare and measure standards on the same day, from the same stock, at the same temperature.",
        "Never measure a sample that is turbid; filter or centrifuge first, and note that filtration may also "
        "remove analyte.",
        "Keep the cell compartment lid closed during measurement \u2014 stray room light inflates transmittance.",
        "Record the actual wavelength and bandpass used; without them the result cannot be reproduced.",
        "Wash hands after handling cobalt salts, and dispose of solutions through the approved route.",
    ]),
    ("h3", "1.6.2  Error budget: what shifts the answer, and in which direction"),
    ("tbl", ["Source of error", "Type", "Effect on the reported concentration", "How to control it"],
     [["Fingerprint or smear on cuvette", "Systematic (positive A)", "Overestimated", "Wipe; handle by frosted faces"],
      ["Bubble in the light path", "Random / sporadic", "Unpredictable spikes", "Inspect, tap gently, refill"],
      ["Cuvette rotated or a different cell used", "Systematic", "Offset between points", "Mark the cuvette, fix orientation"],
      ["Blank set with an empty holder", "Systematic (negative A)", "Underestimated throughout", "Blank with solvent in a cell"],
      ["Lamp not warmed up", "Systematic drift", "Inconsistent between first and last readings", "Respect the warm-up"],
      ["Wavelength off \u03bbmax", "Systematic (lower slope)", "Less sensitive; more scatter", "Set \u03bbmax; recalibrate the monochromator if available"],
      ["Wide bandpass on a steep band", "Systematic (nonlinear)", "Curved calibration, biased slope", "Use the specified slit width"],
      ["Standards above the linear range", "Systematic", "Concentrations biased low", "Dilute; stay below A \u2248 1.2"],
      ["Evaporation from open flasks", "Systematic (rising c)", "Overestimated standards", "Stopper flasks; measure promptly"],
      ["Weighing error in standard preparation", "Systematic (proportional)", "All concentrations scaled identically", "Use a calibrated balance; check the basis (w/v vs w/w)"],
      ["Temperature difference between runs", "Systematic (small)", "Band shifts slightly", "Equilibrate standards and sample"]],
     [46, 30, 46, 48], "**Table 1.6** Error budget. Learn at least one systematic and one random error with its "
                       "direction of bias \u2014 examiners ask for exactly that.", ["l", "l", "l", "l"]),
    ("h3", "1.6.3  Troubleshooting chart"),
    ("tbl", ["Symptom", "Most likely cause", "Immediate action"],
     [["Absorbance is negative", "Blank set with a more absorbing reference, or sample and blank interchanged",
       "Re-blank with solvent; check which cell is which"],
      ["Absorbance reads exactly 0.000 for every sample", "Instrument in %T mode reading 100, or the beam is "
       "blocked/obscured, or the detector gain is wrong", "Check mode, shutter and cell seating"],
      ["Readings jump by more than \u00b10.01 between replicates", "Bubble, fingerprint, loose cuvette, or lamp "
       "still warming", "Inspect the cell; wait for thermal equilibrium"],
      ["Calibration curve bends downwards at high c", "Stray light, or chemical change / association at high "
       "concentration", "Dilute the top standards and re-fit over the linear portion"],
      ["Calibration curve bends upwards", "Blank too absorbing, or scatter in the more concentrated solutions",
       "Check blank; filter the standards"],
      ["No peak found in the scan", "Wrong wavelength range, wrong sample, far too dilute a solution",
       "Widen the range; use a mid-range standard; confirm the solution"],
      ["Unknown absorbs above the top standard", "Unknown too concentrated", "Dilute by a recorded factor and re-measure"],
      ["Peak position differs from the expected 510\u2013515 nm", "Monochromator calibration offset, or a "
       "different cobalt species/solvent", "Verify with a holmium or didymium filter; check the solvent"]],
     [42, 62, 66], "**Table 1.7** Troubleshooting. Each entry is phrased as symptom \u2192 cause \u2192 action, "
                   "which is the format examiners like to hear in an oral.", ["l", "l", "l"]),
]

# ---------------------------------------------------------------- viva
VIVA_A = [
    ("What is the aim of this experiment?",
     "To determine \u03bb_{max} for a cobalt(II) chloride solution, to verify Beer\u2013Lambert behaviour over a "
     "range of concentrations, and to determine the concentration of an unknown cobalt chloride solution from "
     "the resulting calibration line."),
    ("What does a spectrophotometer measure?",
     "The attenuation of light by a sample at a selected wavelength, reported as transmittance or absorbance. It "
     "does not measure concentration directly; the calibration converts one into the other."),
    ("Define absorbance and give its units.",
     "A = log_{10}(I_{0}/I). It is a pure number \u2014 dimensionless \u2014 because it is the logarithm of a "
     "ratio of two intensities. Its \u201cunit\u201d is sometimes written AU (absorbance units), which is a label, "
     "not a physical dimension."),
    ("Define transmittance.",
     "T = I/I_{0}, the fraction of incident light transmitted. Expressed as a percentage it is %T = 100T. "
     "T ranges from 0 (opaque) to 1 (fully transparent)."),
    ("How are absorbance and transmittance related?",
     "A = \u2212log_{10}T. Therefore A = 0 \u2194 T = 1 (100 %), A = 1 \u2194 T = 0.1 (10 %), A = 2 \u2194 "
     "T = 0.01 (1 %). Each unit of absorbance is a tenfold reduction in transmitted intensity."),
    ("State the Beer\u2013Lambert law and define every symbol.",
     "A = \u03b5lc, where A is absorbance (dimensionless), \u03b5 the molar absorptivity (L mol^{\u22121} "
     "cm^{\u22121}), l the path length (cm) and c the concentration (mol L^{\u22121}). The law holds for "
     "monochromatic light, dilute solutions, a single absorbing species and negligible scattering."),
    ("Which of the two names \u2014 Beer and Lambert \u2014 corresponds to which proportionality?",
     "Lambert (and Bouguer) contributed the path-length proportionality: absorbance is proportional to the "
     "thickness of the absorbing layer. Beer contributed the concentration proportionality at fixed thickness."),
    ("Derive the law in one line.",
     "For a slab dx, \u2212dI/I = kc dx. Integrating from 0 to l gives ln(I_{0}/I) = kcl; converting to base 10 "
     "gives log_{10}(I_{0}/I) = (k/2.303)cl = \u03b5cl."),
    ("Why is absorbance logarithmic rather than linear in concentration?",
     "Because each successive layer of solution removes a constant *fraction* of the light reaching it, which is "
     "a multiplicative process. The logarithm converts that geometric attenuation into an additive, linear "
     "quantity."),
    ("What is \u03bb_{max}, and how do you find it?",
     "The wavelength of maximum absorbance for the species. It is found by scanning absorbance against wavelength "
     "and locating the peak, refined with smaller wavelength steps near the maximum."),
    ("Why is the measurement made at \u03bb_{max}?",
     "Two reasons: sensitivity is greatest there because dA/dc = \u03b5l is largest, and the first derivative "
     "d\u03b5/d\u03bb is zero at a peak, so small wavelength-setting errors produce negligible change in the "
     "measured absorbance."),
    ("Why is cobalt chloride solution coloured?",
     "The hydrated Co(II) ion, [Co(H_{2}O)_{6}]^{2+}, has a partially filled 3d shell; d\u2013d transitions absorb "
     "visible light, mainly in the green\u2013yellow region, so the transmitted light appears pink to red."),
    ("Why is the absorption band broad rather than a sharp line?",
     "Because the ligand environment fluctuates and vibronic coupling spreads the transition energy; in solution "
     "the ion exists in a distribution of geometries, giving a band envelope rather than a single line."),
    ("What is the role of the blank?",
     "It sets I_{0} for the measurement by accounting for absorption and reflection by the solvent, the cell walls "
     "and any non-absorbing reagents, so the measured absorbance belongs to the analyte alone."),
    ("Why is distilled water used as the blank here?",
     "Because water is the only other component of the standards and the unknown. Using anything else would "
     "introduce an offset or a spectroscopic interference."),
    ("Why must the instrument be warmed up?",
     "The lamp output and detector sensitivity drift until thermal equilibrium is reached. Blanking a cold "
     "instrument stores an I_{0} that no longer applies minutes later, producing a systematic drift in "
     "absorbance."),
    ("Why must the cuvette be handled only by its frosted faces?",
     "Fingerprints leave an oil and salt film that absorbs and scatters light in the optical path, raising the "
     "apparent absorbance by amounts comparable to the differences you are trying to measure."),
    ("What is the effect of a bubble in the cuvette?",
     "The bubble interrupts the optical path and scatters light, producing an erratic, usually elevated "
     "absorbance reading that may vary between replicates."),
    ("What is the optical path length, and why must it stay constant?",
     "It is the distance the beam travels through the sample, normally 1 cm. Because A = \u03b5lc, a change in "
     "l changes absorbance proportionally and would make standards and unknown incomparable."),
    ("Why does the calibration line not always pass through the origin?",
     "A small intercept can arise from blank mismatch, a baseline offset, a matrix effect, or stray light. It is "
     "an instrumental or chemical imperfection, not a failure of Beer\u2019s law, and it should be reported rather "
     "than forced to zero."),
    ("Why not force the line through the origin?",
     "Because doing so imposes a model that your data may contradict, and it biases every interpolated "
     "concentration. Fit the data you have; discuss the intercept."),
    ("What does the slope of the calibration line represent?",
     "For fixed l and \u03bb it equals \u03b5l in whatever concentration units are plotted. With c in mol L^{\u22121} "
     "and l in cm, the slope is \u03b5 l and can be converted to \u03b5 by dividing by the path length."),
    ("Why is the unknown not extrapolated beyond the standards?",
     "Because the linearity of Beer\u2019s law and the constancy of the chemical species are verified only within "
     "the calibrated range; outside it, curvature and stray-light effects make the extrapolated value unreliable."),
    ("What is the dilution factor, and when is it applied?",
     "DF = final volume / volume of sample taken. It is applied to the concentration read from the calibration "
     "line \u2014 c_{original} = c_{measured} \u00d7 DF \u2014 because dilution changes the measured concentration, "
     "not the absorbance arithmetic."),
    ("What happens if the unknown absorbance exceeds 1.5?",
     "Stray light makes the measured absorbance lower than the true value, so the calibration curve flattens. "
     "The reliable fix is to dilute the sample into the linear range and multiply the result by the dilution factor."),
]

VIVA_B = [
    ("What is monochromatic light, in instrumental terms?",
     "Light confined to a narrow band of wavelengths, defined by the monochromator slit width \u2014 typically a "
     "5\u201310 nm bandpass. Perfectly monochromatic light does not exist in a real instrument, which is one reason "
     "Beer\u2019s law can deviate."),
    ("Why does a wider bandpass increase the risk of nonlinearity?",
     "Because \u03b5 varies across the band. The instrument effectively averages \u03b5 over the band; if \u03b5 "
     "changes steeply there, the average shifts as absorbance (and therefore the effective wavelength weighting) "
     "changes with concentration."),
    ("Why does stray light produce a negative deviation from Beer\u2019s law?",
     "Stray light adds a constant intensity I_{s} to the transmitted beam: A_{measured} = log[(I_{0}+I_{s})/"
     "(I+I_{s})]. At high absorbance, I is small and I_{s} dominates, so the measured absorbance stops increasing "
     "and flattens below the true curve."),
    ("At what absorbance does stray light usually become the limiting factor?",
     "Typically above A \u2248 1.5 for good instruments, and earlier for inexpensive ones. The practical rule is "
     "to keep standards between about 0.1 and 1.2 absorbance units."),
    ("Why is it desirable that the unknown\u2019s absorbance fall in the middle of the calibration range?",
     "Because relative uncertainty in concentration is smallest where absorbance is large compared with its "
     "absolute uncertainty, yet still below the stray-light region \u2014 a compromise near the middle of the "
     "linear range."),
    ("What is the difference between a colorimeter and a spectrophotometer?",
     "A colorimeter uses broad-band filters to isolate a wavelength region; a spectrophotometer uses a "
     "monochromator (prism or grating) to give a narrow, selectable bandpass. Spectrophotometers are therefore "
     "more selective, more sensitive and can record spectra."),
    ("Why is a double-beam instrument less sensitive to lamp drift?",
     "Because it measures the reference and the sample simultaneously (or in rapid alternation), so lamp "
     "intensity fluctuations affect both beams and cancel in the ratio."),
    ("What is the difference between absorbance and optical density?",
     "Optical density is a term historically used for the same logarithmic quantity, A = log_{10}(I_{0}/I). The "
     "two are numerically identical; \u201cabsorbance\u201d is the preferred modern term."),
    ("Does absorbance measure how much light is absorbed?",
     "Not literally. Absorbance is a logarithmic ratio; the actual *fraction* of light absorbed is "
     "1 \u2212 T = 1 \u2212 10^{\u2212A}. At A = 1, 90 % of the light is removed from the beam, not 100 % \u2014 a "
     "classic conceptual trap."),
    ("What is the difference between absorption and attenuation?",
     "Attenuation is any loss of beam intensity (absorption plus scattering plus reflection); absorption is the "
     "conversion of photon energy into internal energy of the sample. Beer\u2019s law, strictly, describes "
     "absorption; attenuation contaminates the measurement."),
    ("Why is the cell compartment kept closed?",
     "To exclude ambient light, which adds to the transmitted intensity measured by the detector and biases "
     "absorbance low."),
    ("How would you check whether a cuvette is scratched?",
     "Fill it with distilled water and read its absorbance at the working wavelength against a blank; a good "
     "cuvette should read near zero. Compare cells against each other to identify a damaged one."),
    ("Why are matched cuvettes used?",
     "Because their path lengths and transmission differ slightly. Matching limits the systematic offset between "
     "cells; the blank correction then removes the residual."),
    ("Why should the cuvette be rinsed with the next solution before filling?",
     "To avoid diluting the new solution with the previous one, which would lower the measured concentration of "
     "each successive standard."),
    ("What does it mean if A/c decreases steadily across your standards?",
     "It indicates a systematic departure from linearity \u2014 usually stray light at high absorbance, or a "
     "chemical change (association, complexation) in the more concentrated solutions."),
    ("Could you determine cobalt without a calibration curve?",
     "In principle yes, if \u03b5, l and the purity of the species were known exactly. In practice the calibration "
     "absorbs all the instrument-specific and matrix-specific uncertainties, which is why it is preferred."),
    ("Why is the wavelength scan performed with a mid-range standard rather than the most concentrated one?",
     "Because the most concentrated standard may exceed the linear range at \u03bb_{max}, flattening the peak and "
     "distorting the apparent \u03bb_{max}; a mid-range solution keeps the whole band inside the reliable range."),
    ("What is the effect of temperature on the spectrum?",
     "Band positions and widths shift slightly, and the molar absorptivity changes. For teaching-level precision "
     "the effect is small, but standards and sample should be at the same temperature."),
    ("Why is the unknown measured last, not first?",
     "So that the calibration is established under exactly the conditions of the measurement, and so that any "
     "instrument drift is detected before the critical reading is taken."),
    ("What is the significance of \u03b5 being a property of the species?",
     "It means the measured absorbance is characteristic of *what* is absorbing, not only of how much. That is "
     "the basis of both quantitative analysis (concentration from A) and qualitative identification (\u03bb_{max} "
     "and band shape suggest the species)."),
    ("Would a solution of cobalt(II) sulphate have the same \u03bb_{max} as the chloride?",
     "Approximately, because the chromophore in dilute aqueous solution is the same [Co(H_{2}O)_{6}]^{2+} ion. "
     "Concentrated chloride solutions differ, because chloride enters the coordination sphere and forms "
     "chloro-complexes, shifting the band."),
    ("Why does adding concentrated HCl to a cobalt chloride solution change its colour?",
     "Chloride displaces water in the coordination sphere, forming [CoCl_{4}]^{2\u2212}, a tetrahedral blue "
     "species; the spectrum and \u03bb_{max} change completely. This is a chemical interference, not an "
     "instrumental one."),
    ("What is the smallest concentration change you could detect with this instrument?",
     "It follows from the calibration: \u03b4c = \u03b4A/m. With a repeatability of about \u00b10.002 A and "
     "m = 0.332 per %, the detection limit in concentration would be roughly 0.006 % \u2014 the arithmetic is "
     "general, the numbers illustrative."),
    ("Why is it wrong to report a concentration to five significant figures?",
     "Because absorbance is typically read to \u00b10.001 and the calibration slope itself carries uncertainty; "
     "three, or at most four, significant figures are consistent with the data. Reporting more is a claim of "
     "precision you do not have."),
]

VIVA_C = [
    ("What if you forgot to blank the instrument?",
     "The stored I_{0} would correspond to the previous condition (or to no light), and every absorbance would "
     "carry a constant offset. A calibration would still be linear, but the intercept would be wrong and any "
     "result derived from a single-point calculation would be biased."),
    ("What if you used tap water instead of distilled water for the blank?",
     "The blank would itself absorb and scatter slightly; the offset would be small but real, and any ions in the "
     "tap water could interact with cobalt. Distilled water removes both problems."),
    ("What if you measured at 540 nm instead of \u03bb_{max}?",
     "The experiment would still work \u2014 540 nm lies on the flank of the band, where \u03b5 is appreciable \u2014 "
     "but sensitivity would be lower and, because the slope d\u03b5/d\u03bb is large there, small wavelength errors "
     "would translate into larger errors in \u03b5 and in the calibration slope."),
    ("What if you changed the wavelength between measuring the standards and the unknown?",
     "The calibration would no longer apply, because the slope is \u03b5l at a specific \u03bb. The result would be "
     "systematically wrong by the ratio of the two molar absorptivities."),
    ("What if a standard were made up to the wrong volume?",
     "That single point would be off the line. The least-squares fit would be pulled towards it, biasing the "
     "slope; the correct action is to identify the outlier from residuals and remake the standard, not to delete "
     "it silently."),
    ("What if the sample were turbid?",
     "Scattering would add an apparent absorbance that does not obey Beer\u2019s law, and the reported "
     "concentration would be too high. Filter or centrifuge; note that filtration may also remove analyte."),
    ("What if the cobalt solution had partly evaporated before measurement?",
     "Its concentration would be higher than stated, so its absorbance would be too high and the calibration "
     "slope too steep \u2014 unless evaporation affected standards and unknown equally, which it will not."),
    ("What if the cuvette were not fully inserted?",
     "The beam would pass partly outside the cell, bypassing some of the absorbing path; absorbance would read "
     "low and erratically, and often the reading would fluctuate as the cell settles."),
    ("What if you plotted %T against concentration instead of A?",
     "You would obtain a curve, not a line, because transmittance is exponential in concentration. Reading a "
     "concentration from it would be possible but far less precise, and the graph would be hard to interpolate."),
    ("What if the unknown absorbance were below the lowest standard?",
     "You would be extrapolating towards zero. If the fitted line has a reliable intercept, interpolation between "
     "zero and the first standard is defensible; otherwise concentrate the sample or prepare lower standards."),
    ("What if the instrument\u2019s wavelength calibration were in error by 10 nm?",
     "The nominal \u03bb_{max} would be misreported by 10 nm and the working wavelength would sit off-peak. "
     "Sensitivity would fall, and if the error were large enough the calibration could become nonlinear. A "
     "holmium oxide or didymium filter checks wavelength accuracy."),
    ("What if the cobalt chloride had lost water of crystallisation (CoCl_{2}\u00b7 6H_{2}O is hygroscopic)?",
     "The mass weighed would not correspond to the stated formula, so all nominal concentrations would be wrong "
     "by a constant factor. This is why the salt should be kept stoppered, and why the hydrate\u2019s water "
     "content must be known if absolute concentrations are required."),
    ("What if the solution were left in bright sunlight during the experiment?",
     "Photochemical and thermal effects can alter the sample, and ambient light leakage into the cell compartment "
     "adds to the detector signal. Keep solutions in the dark and the compartment closed."),
]

VIVA_D = [
    ("Examiner: Why do you measure at a peak rather than anywhere on the band?",
     "Student: Because absorbance is highest there, so sensitivity is highest."),
    ("Examiner: Sensitivity is not the only reason, is it?",
     "Student: No \u2014 at a maximum, the derivative dA/d\u03bb is zero, so a small error in setting the "
     "wavelength changes the absorbance only to second order. The measurement is at a stationary point, which "
     "makes it robust."),
    ("Examiner: If you doubled the path length, what would happen to the absorbance?",
     "Student: It would double, because A is proportional to l \u2014 that is Lambert\u2019s contribution."),
    ("Examiner: And if you doubled the concentration?",
     "Student: Also double, within the linear range \u2014 that is Beer\u2019s contribution."),
    ("Examiner: Double both?",
     "Student: Four times the absorbance \u2014 but experimentally you would then be at A \u2248 4 \u00d7 your "
     "original value, probably in the stray-light region, where the measured absorbance would fall short of the "
     "prediction. This is exactly why the linear range must be respected."),
    ("Examiner: Your absorbance is 2.0. What fraction of light is transmitted?",
     "Student: 1 %."),
    ("Examiner: And what fraction has been removed from the beam?",
     "Student: 99 % \u2014 but note that \u201cremoved\u201d includes absorption and any scattering or reflection; "
     "Beer\u2019s law only describes the absorption part."),
    ("Examiner: Is absorbance proportional to concentration in general?",
     "Student: Only under the assumptions of the law \u2014 monochromatic light, a single non-interacting "
     "absorbing species, constant \u03b5, negligible scattering, and a concentration low enough that stray light "
     "is unimportant. Outside those conditions the relationship is not strictly proportional."),
    ("Examiner: So is Beer\u2019s law a law or an approximation?",
     "Student: It is a limiting law. It is exact in the limit of monochromatic light, infinite dilution and "
     "non-interacting absorbers; real measurements are approximations to that limit, which is why calibration is "
     "always performed rather than assumed."),
    ("Examiner: Why do you need seven standards when two would define a line?",
     "Student: Two points define a line but cannot test whether the relationship is linear, cannot reveal an "
     "outlier, and give no estimate of scatter. Multiple standards test the model and quantify the uncertainty "
     "in the slope."),
    ("Examiner: Your intercept is 0.05 absorbance units. Is your result wrong?",
     "Student: Not necessarily \u2014 but it must be explained. It could come from a blank mismatch, a baseline "
     "offset or a matrix effect. I would report the intercept, use it in the interpolation, and investigate if "
     "it were large."),
    ("Examiner: What is the single largest source of error in your experiment?",
     "Student: In careful hands, standard preparation \u2014 weighing and volumetric dilution \u2014 because a "
     "proportional error there scales the whole calibration. Cuvette handling is the largest preventable random "
     "error."),
]

VIVA_E = [
    ("Why is it incorrect to say \u201cabsorbance measures the amount of light absorbed\u201d?",
     "Because absorbance is logarithmic and dimensionless; the quantity that measures light removed is the "
     "fraction 1 \u2212 T. At A = 1, 90 % of the light is removed, not 100 %."),
    ("Can two different substances have the same \u03bb_{max}?",
     "Yes. \u03bb_{max} alone is not an identification. Identification requires the whole band shape, \u03b5, and "
     "ideally independent evidence (a chemical test, or another spectroscopic technique)."),
    ("Does a colourless solution have zero absorbance?",
     "Only in the visible region. It may absorb strongly in the ultraviolet \u2014 many colourless organic "
     "compounds do. \u201cColourless\u201d means no absorption in 400\u2013700 nm, not no absorption at all."),
    ("Is absorbance additive when two species absorb at the same wavelength?",
     "Yes, within the linear range: A_{total} = A_{1} + A_{2} = (\u03b5_{1}c_{1} + \u03b5_{2}c_{2})l. This "
     "additivity is the basis of simultaneous multi-component analysis \u2014 and the reason an unaccounted "
     "interference biases the result upward."),
    ("Why does the calibration line sometimes have a negative intercept?",
     "Typically from over-blanking (the blank absorbs slightly more than the sample matrix) or from a baseline "
     "offset in the instrument. It is a zero error, not a violation of the law."),
    ("Can the molar absorptivity be larger than 10^{5} L mol^{\u22121} cm^{\u22121}?",
     "No, for a single-photon process: the practical upper limit for organic dyes is around 10^{5}, set by the "
     "physical cross-section of the molecule. Values much larger than that indicate an error in units or in "
     "concentration."),
    ("Why is absorbance considered a more \u2018honest\u2019 quantity than transmittance for reporting?",
     "Because its uncertainty is roughly constant across the useful range, whereas the relative uncertainty in "
     "transmittance blows up at low T. Absorbance is also additive and linear in concentration, which "
     "transmittance is not."),
    ("If you dilute a sample tenfold, how does absorbance change?",
     "It falls to one tenth, provided the species does not dissociate or associate on dilution \u2014 an "
     "assumption worth checking for weak acids, dyes that aggregate, and complex ions."),
    ("Why do we not simply weigh the cobalt in the unknown sample?",
     "Because the unknown is a solution of unknown volume and composition, and the question is the concentration "
     "of dissolved species, not the total mass of cobalt in a container. The optical method measures the species "
     "in solution, which is the chemically meaningful quantity."),
    ("What would happen if you used a 10 mm cell for the standards and a 5 mm cell for the unknown?",
     "The unknown\u2019s absorbance would be halved for the same concentration, so the interpolated value would be "
     "half the true concentration. Path length must be identical throughout."),
]

VIVA_F = [
    ("How is spectrophotometry used industrially for quality control?",
     "In pharmaceutical dissolution and content-uniformity testing, in dye-batch strength, in beverage colour "
     "measurement and in water-quality monitoring \u2014 wherever a concentration must be verified quickly and "
     "non-destructively."),
    ("How could you measure cobalt in the presence of nickel?",
     "Choose a wavelength where the two differ strongly in \u03b5, or measure at two wavelengths and solve the "
     "simultaneous equations A_{1} = \u03b5_{Co,1}c_{Co}l + \u03b5_{Ni,1}c_{Ni}l and similarly at \u03bb_{2}, or "
     "separate them chemically first."),
    ("What is a derivative spectrum, and why is it useful?",
     "It is dA/d\u03bb plotted against \u03bb. It suppresses broad background absorption, sharpens overlapping "
     "bands and can locate a weak band on a strong sloping background \u2014 useful for trace analysis in a "
     "complex matrix."),
    ("What is a flow-injection or in-line photometric analyser?",
     "An automated system in which sample is injected into a flowing reagent stream, reacts, and passes "
     "continuously through a flow cell where absorbance is recorded \u2014 the basis of most automated water and "
     "clinical analysers."),
    ("How would you improve the precision of this experiment?",
     "Use matched, higher-quality cells; use a double-beam instrument to cancel lamp drift; prepare standards "
     "gravimetrically; thermostat the cell holder; take replicate readings and average; and use least-squares "
     "fitting with a reported standard error on the slope."),
    ("What is the role of a diode-array spectrophotometer?",
     "It records the entire spectrum simultaneously using a photodiode array detector, so a full spectrum can be "
     "captured in milliseconds \u2014 essential for chromatography detection and for kinetic studies."),
    ("Why is UV\u2013visible spectroscopy often paired with chromatography?",
     "Because the chromatograph separates the mixture and the detector quantifies each separated species by "
     "absorbance \u2014 combining selectivity with sensitivity."),
    ("What is the practical detection limit of a good spectrophotometric method?",
     "Typically absorbance of about 10^{\u22124} can be detected, which for a species with \u03b5 \u2248 10^{4} "
     "corresponds to roughly 10^{\u22128} mol L^{\u22121} in a 1 cm cell \u2014 the arithmetic is worth being able "
     "to do on the spot."),
    ("Why might a laboratory choose a colorimetric method over atomic absorption for cobalt?",
     "Colorimetry is cheap, fast and needs only a spectrophotometer, which most teaching and routine laboratories "
     "already have. Atomic absorption is more selective but requires a hollow-cathode lamp and flame or graphite "
     "furnace."),
    ("What is the main limitation of this experiment as performed?",
     "It measures total dissolved cobalt, not its speciation, and it assumes the standards and unknown have the "
     "same chemical form of cobalt. If the unknown contains a different complex, the calibration is invalid even "
     "though the instrument is working perfectly."),
]

# --- chain cross-examination
CHAIN = [
    ("Examiner: Why do you use a blank?",
     "Student: To set I_{0} so that the absorbance measured belongs to the analyte alone."),
    ("Examiner: What exactly does the blank contain?",
     "Student: Everything in the sample except the analyte \u2014 here, distilled water."),
    ("Examiner: What if the blank contained a little cobalt chloride?",
     "Student: Then I_{0} would be measured through an absorbing solution, so all sample absorbances would read "
     "low by that amount \u2014 a systematic negative offset."),
    ("Examiner: Would the calibration still be linear?",
     "Student: Yes \u2014 a constant offset does not destroy linearity. But the slope would change slightly if the "
     "blank itself absorbs, and the intercept would be negative."),
    ("Examiner: So would your unknown concentration be wrong?",
     "Student: Yes. The slope may be almost unaffected, so the interpolated concentration would be too low by "
     "roughly the blank\u2019s absorbance divided by the slope."),
    ("Examiner: How would you detect that mistake?",
     "Student: The intercept of the calibration line would be significantly negative, and the lowest standard "
     "might even read a negative absorbance."),
    ("Examiner: Could you correct for it after the fact?",
     "Student: Only if I knew the blank\u2019s absorbance independently. Otherwise the correct action is to "
     "repeat the measurement with a proper blank."),
    ("Examiner: What does that tell you about the role of the blank in the error budget?",
     "Student: That it is a systematic error affecting all readings equally \u2014 which makes it more dangerous "
     "than random noise, because repeating the measurement will not reveal it."),
]


# ---------------------------------------------------------------- examiner checklist
from common import facts_block, qbox, pair_table

CHECKLIST_PART1 = [
    ("h2", "1.8  Examiner\u2019s secret checklist"),
]
B2_REST = [
    ("h3", "1.8.1  Twenty facts that must be automatic"),
]
FACTS = [
    "A = log_{10}(I_{0}/I) = \u2212log_{10}T; absorbance is dimensionless.",
    "Beer\u2013Lambert: A = \u03b5lc, valid for monochromatic light and dilute, non-scattering solutions.",
    "A = 1 means 10 %T; A = 2 means 1 %T; each unit is a factor of ten.",
    "\u03bb_{max} for aqueous CoCl_{2} is near 510\u2013515 nm (broad visible band).",
    "Measure at \u03bb_{max}: maximum sensitivity and minimum wavelength-error sensitivity.",
    "Molar absorptivity \u03b5 has units L mol^{\u22121} cm^{\u22121}.",
    "Path length l is fixed by the cuvette; changing cells changes A proportionally.",
    "Blank = solvent + everything except analyte; here distilled water.",
    "Blank the instrument only after the specified warm-up (about 15 min).",
    "Set 0 %T with the shutter closed, then 100 %T with the blank.",
    "Scan in 20 nm steps; refine near the peak with 5 nm steps.",
    "Never change wavelength after calibration has begun.",
    "Handle cuvettes by frosted faces; wipe optical faces with lint-free tissue.",
    "Use one cuvette, one orientation, one fill height throughout.",
    "Keep absorbance of standards between about 0.1 and 1.2.",
    "Dilute the unknown into range; multiply the result by the dilution factor.",
    "Fit A = mc + b; the slope equals \u03b5l in the plotted concentration units.",
    "Interpolate, do not extrapolate, beyond the standards.",
    "Stray light causes negative deviation (flattening) at high absorbance.",
    "Cobalt salts are toxic/environmental hazards: controlled waste disposal.",
]
CHECKLIST_PART2 = [("raw", facts_block("Twenty facts, two columns", FACTS))]

CHECKLIST_PART2 += [("h3", "1.8.2  The ten most likely questions")]
CHECKLIST_PART2 += [("raw", qbox("Asked in almost every viva", [
    "State Beer\u2013Lambert law and define every symbol.",
    "What is absorbance, and how is it related to transmittance?",
    "What is \u03bb_{max} and why do you measure there?",
    "Why is a blank necessary? What does it contain?",
    "Why is the calibration curve a straight line, and when does it fail?",
    "What does the slope of your graph represent?",
    "How did you obtain the concentration of the unknown?",
    "What are the sources of error in this experiment?",
    "Why is the cuvette handled by the frosted sides?",
    "Why must you not extrapolate beyond your standards?",
], numbered=True))]

CHECKLIST_PART2 += [("h3", "1.8.3  The ten hardest questions")]
CHECKLIST_PART2 += [("raw", qbox("Designed to separate a 9 from a 10", [
    "Derive Beer\u2013Lambert law from the differential absorption of a thin slab and state every assumption "
    "the derivation makes.",
    "Explain quantitatively why stray light causes a *negative* deviation from the law, and derive the "
    "expression for the measured absorbance.",
    "If \u03b5 changes steeply across the instrumental bandpass, show why the calibration can curve even though "
    "Beer\u2019s law is obeyed at every wavelength.",
    "Your calibration passes through the origin but your unknown gives a concentration 8 % higher than the "
    "gravimetric value. List the possible causes in order of likelihood and say how each would be tested.",
    "Why is the measurement at \u03bb_{max} robust to wavelength error, in terms of the derivative of the "
    "response curve?",
    "How would you determine cobalt and nickel simultaneously in one solution without separating them?",
    "Convert your calibration slope into a molar absorptivity, showing the unit chain.",
    "What is the physical upper limit on \u03b5, and why does it exist?",
    "Why is absorbance, not transmittance, the quantity that is additive when two species absorb?",
    "Distinguish absorption, attenuation and scattering, and say which one Beer\u2019s law actually describes.",
], numbered=True, colour="#A4483B"))]

CHECKLIST_PART2 += [("h3", "1.8.4  Most commonly confused concepts")]
CHECKLIST_PART2 += [("raw", pair_table("Get these pairs right under pressure", [
    ("Absorbance vs transmittance", "A is logarithmic and additive; T is linear in intensity and multiplicative."),
    ("Absorption vs attenuation", "Absorption converts photon energy in the sample; attenuation also includes "
                                  "scattering and reflection."),
    ("\u03bb_{max} vs working wavelength", "\u03bb_{max} is a property of the species; the working wavelength is a "
                                          "choice, normally equal to \u03bb_{max}."),
    ("Blank vs reference", "A blank is the zero-absorbance reference (analyte absent). A reference standard is a "
                           "known concentration used on the calibration line."),
    ("Colorimeter vs spectrophotometer", "Filter-based broad band vs monochromator-based narrow band."),
    ("Absorbance vs optical density", "Same numerical quantity; different historical name."),
    ("Interpolation vs extrapolation", "Reading within the calibrated range vs reading beyond it."),
    ("Molar absorptivity vs slope", "Slope = \u03b5l; \u03b5 = slope/l, and only when c is in mol L^{\u22121} "
                                    "and l in cm."),
]))]

CHECKLIST_PART2 += [
    ("h3", "1.8.5  Formulas and relations worth memorising"),
    ("tbl", ["Relation", "Expression", "Notes"],
     [["Absorbance from transmittance", "A = \u2212log_{10}T = 2 \u2212 log_{10}(%T)", "Base 10; the factor 2 "
       "converts %T"],
      ["Beer\u2013Lambert law", "A = \u03b5lc", "\u03b5 in L mol^{\u22121} cm^{\u22121}, l in cm, c in mol "
       "L^{\u22121}"],
      ["Concentration from A", "c = A/(\u03b5l)", "Single-point form; needs a known \u03b5"],
      ["Calibration interpolation", "c = (A \u2212 b)/m", "Preferred; m and b from least squares"],
      ["Dilution correction", "c_{original} = c_{measured} \u00d7 (V_{final}/V_{taken})", "Apply after "
       "interpolation"],
      ["Slope to \u03b5", "\u03b5 = m/l", "m in A per mol L^{\u22121}"],
      ["Uncertainty propagation", "\u03b4c/c = \u221a[(\u03b4A/A)^{2} + (\u03b4m/m)^{2}]", "Approximate; assumes "
       "independent errors"],
      ["Fraction of light removed", "1 \u2212 T = 1 \u2212 10^{\u2212A}", "Distinguish from absorbance itself"]],
     [50, 66, 54], "**Table 1.8** Formula sheet for this experiment.", ["l", "l", "l"]),
    ("h3", "1.8.6  Observations that reveal a mistake"),
    ("tbl", ["Observation", "What it almost certainly means"],
     [["Negative absorbance", "Blank set incorrectly, or cells interchanged"],
      ["Identical absorbance for all standards", "Wavelength not fixed, or the same solution used twice"],
      ["Calibration flattens above A \u2248 1.2", "Stray light, or chemical change at high concentration"],
      ["Large intercept", "Blank mismatch, baseline offset, or matrix interference"],
      ["Replicates differ by > 0.01 A", "Bubble, fingerprint, unstable lamp, or loose cell"],
      ["\u03bb_{max} far from 510\u2013515 nm", "Monochromator offset, or a different cobalt species/solvent"],
      ["Unknown absorbance above the top standard", "Unknown too concentrated; dilute and re-measure"]],
     [66, 104], "**Table 1.9** Symptom \u2192 diagnosis. Each of these is a defensible viva answer in itself.",
     ["l", "l"]),
    ("h3", "1.8.7  Details students overlook but examiners ask"),
    ("bul", [
        "The **percentage basis** of the standards (w/v vs w/w) must be stated; the supplied source does not "
        "resolve it. This is a legitimate gap, not a secret.",
        "The **bandpass** of the instrument changes the effective \u03b5; quote it if it is known.",
        "**Refractive index** effects at high solute concentration cause real deviations from Beer\u2019s law.",
        "**Additivity** of absorbance across species is what makes the method work in mixtures \u2014 and what "
        "makes an unaccounted interference dangerous.",
        "The five-fold use of 2.303 (ln \u2192 log_{10}) recurs in kinetics, so learn the conversion once.",
        "A calibration line fitted with a **spreadsheet regression** should report both r^{2} and the standard error "
        "of the slope \u2014 r^{2} alone hides a poor slope estimate.",
    ]),
    ("h3", "1.8.8  Practical mistakes that cost marks"),
    ("num", [
        "Setting 100 %T with an empty holder rather than a solvent-filled cell.",
        "Changing wavelength or cuvette after beginning the calibration.",
        "Not recording \u03bb_{max} on the answer sheet (a stated result is worth marks; an implied one is not).",
        "Reporting a concentration without units or without stating the dilution factor.",
        "Drawing a best-fit line by eye and reading the unknown from the graph instead of using the fitted "
        "equation.",
        "Leaving the observation table in pencil-and-paper form without the actual wavelength used.",
        "Forgetting to mention waste disposal for cobalt solutions when asked for precautions.",
    ]),
    ("h3", "1.8.9  The ninety-second answer"),
    ("speak", "Say this if you are asked to explain the experiment in one breath", [
        "Cobalt(II) chloride solutions are pink because the hydrated Co(II) ion absorbs visible light, with a "
        "broad maximum near 511 nm. I first scan absorbance against wavelength in 20 nm steps to locate that "
        "maximum, because measuring at a peak gives both the greatest sensitivity and the least sensitivity to "
        "wavelength-setting error. I then set the instrument to \u03bb_{max}, blank it with distilled water so "
        "that I_{0} is defined through the solvent and the cell, and measure a series of standards of known "
        "concentration. Plotting absorbance against concentration gives a straight line through the origin, "
        "A = \u03b5lc, which is Beer\u2013Lambert law; the slope is \u03b5l. Finally I measure the unknown under "
        "identical conditions and interpolate its concentration from the fitted line, applying the dilution factor "
        "if I had to dilute it into range. The critical controls are the warm-up, the blank, a single cuvette in a "
        "single orientation, and staying below about 1.2 absorbance units where stray light begins to flatten the "
        "curve.",
    ]),
    ("h3", "1.8.10  Last-minute revision strip"),
]
CHECKLIST_PART2 += [("box", "key", [
    "**log ratio:** A = log\u2081\u2080(I\u2080/I); **then** A = \u03b5lc; **then** calibrate, interpolate, and multiply by the dilution factor.",
    "**0 \u2192 100 %T, 1 \u2192 10 %T, 2 \u2192 1 %T.**",
    "**Peak = sensitivity + robustness.**",
    "**Blank = everything but analyte.**",
    "**One cell, one orientation, one fill height.**",
    "**Stay under A \u2248 1.2.**",
    "**Stray light flattens the top of the curve.**",
], "Memory strip")]

CH1_PLAN = CHECKLIST_PART2
FACTS_TABLE = B2_REST
CH1_CHECKLIST = CHECKLIST_PART1 + CHECKLIST_PART2

CH1 = {
    "key": "spectro",
    "num": "1",
    "kicker": "Experiment 1  \u00b7  Instrumental analysis",
    "title": "Spectrophotometry of Cobalt Chloride",
    "toc": "Spectrophotometry of cobalt chloride",
    "standfirst": "Determine \u03bbmax, verify Beer\u2013Lambert behaviour and find an unknown concentration. "
                  "This chapter builds the measurement from the physics of light absorption upward, then "
                  "converts it into an examination-proof working method.",
    "body": B + [
        ("h2", "1.7  Viva question bank"),
        ("p", "The questions below are grouped in the categories an examiner actually uses: fundamentals, "
              "reasoning (why), mechanism (how and what), what-if scenarios, conceptual traps, and applications. "
              "Answers are written to be spoken aloud \u2014 concise first, then the reasoning. There are 92 "
              "answered questions in this chapter, including a full cross-questioning chain."),
        ("qsub", "A.  Fundamental questions"),
        ("qa", VIVA_A),
        ("qsub", "B.  \u201cWhy\u201d and \u201chow\u201d questions"),
        ("qa", VIVA_B),
        ("qsub", "C.  \u201cWhat if\u201d questions"),
        ("qa", VIVA_C),
        ("qsub", "D.  Examiner cross-questioning chain"),
        ("p", "Read this chain aloud as a dialogue. It demonstrates the pattern an aggressive examiner uses: "
              "accept your answer, then ask what happens when one assumption changes. The chain continues until "
              "the underlying concept \u2014 here, systematic versus random error \u2014 has been exposed."),
        ("qa", CHAIN),
        ("qsub", "E.  Tricky examiner questions"),
        ("qa", VIVA_D),
        ("qsub", "F.  Advanced and applied questions"),
        ("qa", VIVA_E),
    ] + CHECKLIST_PART1 + CHECKLIST_PART2,
}

