"""Front matter: title verso, contents, orientation pages, syllabus inventory, source audit."""
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import (Paragraph, Spacer, PageBreak, KeepTogether, NextPageTemplate,
                                Flowable, Table, TableStyle, CondPageBreak)

import style as ST
from style import NAVY, STEEL, RULE, MUTED, PALE_NAVY, PALE_AMBER, AMBER_EDGE
from blocks import S, ChapterHead, BOX, TBL, H2, CONTENT_WIDTH
from doc import MasterTOC, Bookmark, mk

C = colors.HexColor


def mtbl(header, rows, widths, caption=None, align=None):
    """TBL with the mini-markup applied (TBL itself does not parse it)."""
    return TBL([mk(h) for h in header],
               [[mk(c) if isinstance(c, str) else c for c in r] for r in rows],
               widths, mk(caption) if caption else None, align)


def front():
    out = []

    # ---------------------------------------------------------- how to use
    out.append(Bookmark(0, "How to use this volume", "howto",
                        toc_text="How to use this volume", label="FRONT MATTER"))
    out.append(ChapterHead("", "How to Use This Volume", "Front matter  \u00b7  Orientation"))
    out.append(Spacer(1, 7))
    out.append(Paragraph(mk(
        "This volume is built from three supplied laboratory guides: //Chemistry Laboratory Master Guide// "
        "(eight experiments), //Complete Laboratory Mastery Guide// (six experiments) and //Complete "
        "Laboratory Mastery Practical and Viva Guide// (six experiments). The three overlap but are not "
        "identical, and each contains material the others do not. Rather than reproduce any one of them, this "
        "volume merges them into a single, sequenced course covering **eleven distinct laboratory activities**, "
        "with the duplication removed and the gaps made explicit."), S["body"]))
    out.append(Paragraph(mk(
        "Every chapter follows the same architecture, so that you always know where you are:"), S["body"]))
    out += mtbl(["Section", "What it gives you", "Use it when"],
               [["Theory from zero", "Every concept built from first principles, with derivations and the limits "
                 "of validity", "You do not understand *why* the experiment works"],
                ["Apparatus", "What each item does, its principle, and what happens if it fails",
                 "The examiner points at a component and says \u201cexplain this\u201d"],
                ["Procedure", "Every step with the reason, the sequence logic and the consequence of skipping it",
                 "You must perform the experiment unaided"],
                ["Observations and calculation", "Blank observation tables, worked sample arithmetic, unit chains",
                 "You are recording data or checking your calculation"],
                ["Precautions, errors, troubleshooting", "Error budget with the direction of bias, symptom \u2192 "
                 "cause \u2192 action tables", "Your result looks wrong, or you are asked about errors"],
                ["Viva question bank", "Between seventy and ninety answered questions per experimental activity, in examiner "
                 "categories, plus cross-questioning chains", "You are preparing for the oral"],
                ["Examiner\u2019s checklist", "Twenty facts, ten likely questions, ten hard questions, confused "
                 "concepts, formula strip, mistakes that cost marks, ninety-second answer",
                 "The night before, and the ten minutes before your turn"]],
               [34, 74, 62], "**Table 0.1** How each chapter is organised. Every chapter uses this exact order, "
                             "so revision becomes navigation rather than search.", ["l", "l", "l"])

    out.append(H2("The three rules this volume follows", 2, True))

    out.append(BOX([mk(x) for x in (
        "**1. Nothing measured is invented.** The supplied material contains blank observation tables, faint "
        "handwriting and missing pages. Where numbers are used to demonstrate a calculation, they are labelled "
        "as illustrative and are chosen for arithmetic convenience, not presented as data.",
        "**2. Every gap is named.** Where a source detail is illegible or a procedure is incomplete, the "
        "chapter says so, in the place where it matters, and tells you what to confirm with your instructor.",
        "**3. Explanation is separated from transcription.** Facts that come from the supplied pages are "
        "reproduced faithfully; the physics, chemistry, derivations, failure modes and examiner traps around "
        "them are added teaching, clearly written as such.",
    )], "note", "Editorial discipline"))

    out.append(Paragraph(mk(
        "A word on **safety**. Several activities involve corrosive acids, toxic cobalt and aniline derivatives, "
        "flammable oils, ignition sources and hot apparatus. This volume explains the science and the reasoning "
        "so that you understand what you are doing. It is not a substitute for your institution\u2019s approved "
        "method, risk assessment, reagent labels or supervisor. Where a source treats a hazardous preparation "
        "conceptually \u2014 notably the diazoaminobenzene synthesis \u2014 this volume does the same and does not "
        "supply an operating recipe."), S["body"]))

    out.append(BOX([mk(x) for x in (
        "Read the chapter theory once slowly, with a pencil. Then read only the procedure and the precautions "
        "before your practical session \u2014 you need the hands, not the history, at the bench. Then, after the "
        "session, read the error and troubleshooting sections against what actually happened to you. Finally, "
        "work the viva bank aloud: answering silently is not the same skill as answering in front of a person.",
    )], "key", "A three-pass reading strategy"))

    # ---------------------------------------------------------- conventions
    out.append(H2("Conventions used throughout this volume", 2, True))
    out.append(Paragraph(mk(
        "A few notational decisions are applied without exception, so that what you see on one page means the same "
        "thing on every other."), S["body"]))
    out += mtbl(["Convention", "Meaning", "Example"],
               [["<i>V</i><sub>sample</sub>, <i>V</i><sub>t</sub>, <i>V</i><sub>\u221e</sub>",
                 "Capital <i>V</i> with a subscript denotes a volume measured in the laboratory",
                 "<i>V</i><sub>t</sub> is the titre at time <i>t</i>"],
                ["N, M", "Normality (equivalents per litre) and molarity (moles per litre) are never used "
                 "interchangeably", "N = 2M for oxalic acid"],
                ["\u03bd, \u03bc, \u03ba, \u039b",
                 "Kinematic viscosity, dynamic viscosity, conductivity and molar conductance \u2014 note that "
                 "\u03ba is conductivity, not conductance", "\u03ba = G \u00d7 cell constant"],
                ["T and P", "In water analysis T is total alkalinity and P is phenolphthalein alkalinity; T also "
                 "denotes transmittance and thermodynamic temperature where stated", "The context is stated each "
                 "time"],
                ["<b>Bold</b>", "A term being defined, or the operative word in a precaution",
                 "never pipette by <b>mouth</b>"],
                ["<i>Italics</i>", "A word used as a word, or a contrast being drawn", "<i>capacity</i>, not "
                 "intensity"],
                ["Grey callout", "A gap or limitation in the supplied source, flagged where it matters",
                 "the \u201cOn the source\u201d boxes"],
                ["Charges", "Ionic charges carry an explicit sign; oxidation or reduction is stated, not implied",
                 "CO<sub>3</sub><super>2\u2212</super>"]],
               [40, 74, 56],
               "**Table 0.1b** Notation. If a symbol in a chapter is ambiguous, this table is the tie-breaker.",
               ["l", "l", "l"])

    out.append(BOX([mk(x) for x in (
        "**If you have ten minutes before a viva**, read the memory strip at the end of the relevant chapter and "
        "the four-theme summary in Appendix B. Those two pages contain the answer structures that most questions "
        "resolve into.",
        "**If you have ten minutes before a practical**, read the procedure and the \u201cpractical mistakes that "
        "cost marks\u201d list. Nothing else.",
    )], "key", "The ten-minute rule"))

    out.append(CondPageBreak(300))
    out.append(H2("Where to start, depending on what you need", 2, True))
    out.append(Paragraph(mk(
        "No reader needs every page at once. Find your situation in the table below and go directly to the "
        "chapter and section named."), S["body"]))
    out += mtbl(["Your situation", "Go to", "Why there"],
               [["Your practical is tomorrow", "The procedure and precautions sections of the relevant chapter, "
                 "plus its \u201cpractical mistakes\u201d list", "At the bench you need actions and traps, not "
                 "history"],
                ["Your viva is tomorrow", "The viva bank and the examiner\u2019s checklist of the relevant chapter, "
                 "then Appendix B", "Spoken recall is trained by speaking, and cross-experiment questions are "
                 "where marks are lost"],
                ["You do not understand the theory", "The \u201ctheory, built from the beginning\u201d section of "
                 "that chapter", "Every derivation starts from zero, deliberately"],
                ["Your result is wrong", "The troubleshooting chart and error budget for that activity",
                 "Symptom-to-cause tables are faster than rereading"],
                ["You are revising broadly", "Chapter 12, then Appendix A", "The papers diagnose, the formula "
                 "sheet consolidates"],
                ["You want to check a fact", "Appendix C and Table 0.3", "Every gap and every policy is documented"]],
               [50, 68, 52],
               "**Table 0.1c** Navigation by need. The book is a reference as much as a course.",
               ["l", "l", "l"])

    out.append(BOX([mk(x) for x in (
        "The observation tables in this volume reproduce the **layout** of the supplied sheets but are left "
        "**blank**, for two reasons. First, the sources contain no completed readings in most cases \u2014 the "
        "spaces are empty or the handwriting is too faint to transcribe reliably. Second, a pre-filled table teaches "
        "nothing: transcribing someone else\u2019s data is not the skill being examined.",
        "Use them by copying the structure into your own notebook before the session, so that you record initial and "
        "final burette readings, sample volume, temperature and the endpoint description in the right order, at the "
        "moment of measurement. The worked illustrations elsewhere in each chapter show what the arithmetic looks "
        "like once the table is filled.",
    )], "note", "A note on the blank tables"))

    # ---------------------------------------------------------- syllabus inventory
    out.append(PageBreak())
    out.append(Bookmark(0, "Syllabus inventory and source audit", "inventory",
                        label="FRONT MATTER",
                        toc_text="Syllabus inventory and source audit"))
    out.append(ChapterHead("", "Syllabus Inventory and Source Audit", "Front matter  \u00b7  Coverage"))
    out.append(Spacer(1, 7))
    out.append(Paragraph(mk(
        "Before any teaching, the complete inventory. Eleven activities appear across the three supplied "
        "documents. The table records which source supplied each, and what the source did and did not contain."),
        S["body"]))
    out += mtbl(["Ch.", "Activity", "Core concepts", "Supplied detail", "Source"],
               [["1", "Spectrophotometry of cobalt chloride", "Absorbance spectrum, \u03bbmax, Beer\u2013Lambert "
                 "law, calibration, unknown concentration", "Apparatus list, warm-up, 20 nm scan, concentration "
                 "series, blank tables", "A, B, C"],
                ["2", "Acid-catalysed hydrolysis of ethyl acetate", "Pseudo-first-order kinetics, integrated rate "
                 "law, titration of acid formed", "Reaction, integrated expression, V\u2080/Vt/V\u221e definition, "
                 "70\u201390 \u00b0C completion step", "A, B"],
                ["3", "pH-metric titration (HCl vs NaOH)", "pH measurement, titration curve, derivative maximum, "
                 "equivalence", "20 mL aliquot, \u0394pH/\u0394V table, curve and derivative described", "A, B, C"],
                ["4", "Conductometric titration (HCl vs NaOH)", "Ionic mobility, conductance, cell constant, "
                 "two-branch curve", "10 mL aliquot, 0.1 N NaOH, increment schedules, partly overwritten "
                 "readings", "B"],
                ["5", "Standardisation of NaOH and assay of HCl", "Primary standard, normality, volumetric "
                 "titration, indicator endpoint", "Oxalic acid standardisation, phenolphthalein, apparatus and "
                 "indicator tables", "C"],
                ["6", "Total hardness of water by EDTA", "Complexometric titration, chelation, metallochromic "
                 "indicator, CaCO\u2083 basis", "pH 10 buffer, Eriochrome Black T, wine red \u2192 blue, "
                 "standardisation, formula", "A, C"],
                ["7", "pH and alkalinity of water", "pH scale, acid-neutralising capacity, P and T alkalinity, "
                 "species nomograph", "Phenolphthalein and methyl-orange endpoints, calculation in CaCO\u2083 "
                 "terms, faint readings", "A, C"],
                ["8", "Residual chlorine in water", "Iodometry, redox stoichiometry, starch endpoint, "
                 "disinfection", "Reactions, N/50 thiosulphate, observation-sheet layout, amended normality",
                 "A, C"],
                ["9", "Viscosity and density of oil (Redwood I)", "Efflux viscometry, kinematic and dynamic "
                 "viscosity, density by specific-gravity bottle", "Apparatus list, 50 mL efflux, "
                 "v = At \u2212 B/t with A = 0.264, B = 190, five readings", "A, B"],
                ["10", "Flash point and fire point of oil", "Vapour pressure, flammability, closed-cup vs "
                 "open-cup methods", "Pensky\u2013Martens components, 5 s sustained burning criterion; the "
                 "opening procedure is missing", "B, C"],
                ["11", "Diazoaminobenzene: concepts and identification", "Aromatic diazonium chemistry, triazene "
                 "linkage, melting point, yield", "Aim, yellow product, m.p. 96\u201398 \u00b0C, filter-paper "
                 "mass method; no quantities or operating recipe", "A"]],
               [9, 40, 44, 55, 14],
               "**Table 0.2** Complete inventory. Source key: **A** = Chemistry Laboratory Master Guide; "
               "**B** = Complete Laboratory Mastery Guide; **C** = Complete Laboratory Mastery Practical and "
               "Viva Guide.", ["c", "l", "l", "l", "c"])

    out.append(H2("What the sources do not contain", 2, True))
    out.append(Paragraph(mk(
        "Honesty about gaps is part of preparation, because a confident wrong answer is worse than a "
        "qualified right one. Each of the following is flagged again in the relevant chapter, at the point "
        "where it affects what you would do."), S["body"]))
    out += mtbl(["Missing or ambiguous detail", "Where it bites", "What to do"],
               [["Hydrolysis page has no completed observation table or numerical titres",
                 "Chapter 2 calculation practice", "Use your own readings; the worked example is labelled "
                 "illustrative"],
                ["Residual-chlorine normality amended by hand on the source page",
                 "Chapter 8 calculation", "Read the actual reagent label and your instructor\u2019s sheet"],
                ["Redwood calibration constants faintly printed; instrument-specific",
                 "Chapter 9 viscosity conversion", "Verify A and B against the instrument certificate"],
                ["Cobalt standard tables blank; scan wavelength handwritten and unclear",
                 "Chapter 1 calibration", "Record the wavelength you actually set"],
                ["Percentage basis of cobalt standards not stated (w/v or w/w)",
                 "Chapter 1 concentration units", "Confirm before weighing; state the basis in your result"],
                ["EDTA observation tables blank", "Chapter 6 titration data", "Record your own initial/final "
                 "burette readings"],
                ["pH/alkalinity readings faint and handwritten", "Chapter 7 calculation", "Do not transcribe; "
                 "re-read the original notebook"],
                ["pH-metric standardisation details incomplete", "Chapter 3", "Standardise NaOH against oxalic "
                 "acid as Chapter 5 describes"],
                ["Conductometric readings partly overwritten", "Chapter 4", "Re-read the original notebook; do "
                 "not guess a value"],
                ["Flash/fire-point opening procedure and apparatus designation absent",
                 "Chapter 10", "Obtain the approved method; only the later procedure is visible"],
                ["Diazoaminobenzene quantities, mixing order and temperature instructions absent by design",
                 "Chapter 11", "Treat conceptually; supervised protocol only"],
                ["One hydrolysis passage says methyl acetate where the aim says ethyl acetate",
                 "Chapter 2", "Ethyl acetate is correct for the aim and procedure; note the inconsistency"]],
               [58, 46, 66], "**Table 0.3** Source-gap register. This table is your defence if an examiner "
                             "challenges a value you did not invent.", ["l", "l", "l"])

    out.append(BOX([mk(x) for x in (
        "**Read the register as a map of what you still have to confirm.** Every row names something the sources "
        "leave open, and every row tells you where in the volume it matters. If your instructor supplies the missing "
        "method \u2014 the flash-point heating rate, the diazo reagent quantities, the conductometric increment "
        "schedule \u2014 write it into the margin of the relevant chapter on the first day, because that is the "
        "version you will be examined on.",
        "**None of these gaps is a defect of the volume; each is a property of the sources.** A guide that "
        "invented "
        "the missing numbers would be easier to read and worse to rely on.",
    )], "note", "How to use the gap register"))

    # ---------------------------------------------------------- contents
    out.append(PageBreak())
    out.append(Bookmark(0, "Contents", "contents", toc_text="Contents", in_toc=False))
    out.append(ChapterHead("", "Contents", "Navigation"))
    out.append(Spacer(1, 4))
    out.append(MasterTOC())
    return out
