"""Examiner's secret checklist: shared builder used by every experiment chapter."""
from blocks import S, BOX
from reportlab.platypus import Paragraph, Spacer, Table, TableStyle, KeepTogether
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.lib.styles import ParagraphStyle

from style import NAVY, STEEL, RULE, PALE_NAVY, PALE_AMBER, AMBER_EDGE, PALE_GREEN, GREEN_EDGE
from doc import mk

C = colors.HexColor


def facts_block(title, facts):
    """Twenty numbered facts in a two-column layout."""
    rows = []
    half = (len(facts) + 1) // 2
    left, right = facts[:half], facts[half:]
    for i in range(half):
        l = left[i]
        r = right[i] if i < len(right) else ""
        rows.append([
            Paragraph('<font color="#8B98A6" name="Sans-Bold" size="6.8">%02d</font>&nbsp;&nbsp;%s'
                      % (i + 1, mk(l)), ParagraphStyle("f1", parent=S["td"], fontSize=8.0, leading=10.2)),
            Paragraph('<font color="#8B98A6" name="Sans-Bold" size="6.8">%02d</font>&nbsp;&nbsp;%s'
                      % (i + 1 + half, mk(r)) if r else "",
                      ParagraphStyle("f2", parent=S["td"], fontSize=8.0, leading=10.2)),
        ])
    t = Table(rows, colWidths=[(mm * 168) / 2, (mm * 168) / 2],
              style=TableStyle([
                  ("VALIGN", (0, 0), (-1, -1), "TOP"),
                  ("LEFTPADDING", (0, 0), (-1, -1), 0),
                  ("RIGHTPADDING", (0, 0), (-1, -1), 7),
                  ("TOPPADDING", (0, 0), (-1, -1), 3.0),
                  ("BOTTOMPADDING", (0, 0), (-1, -1), 3.4),
                  ("LINEBELOW", (0, 0), (-1, -2), 0.3, C("#E4E9EF")),
              ]))
    t.hAlign = "LEFT"
    return [Paragraph(mk(title), S["h4"]), Spacer(1, 2), t, Spacer(1, 6)]


def qbox(title, items, numbered=False, colour=None):
    """Compact numbered or bulleted list in a tinted panel."""
    rows = []
    for i, it in enumerate(items, 1):
        pre = ('<font color="%s" name="Sans-Bold" size="7.0">%d.</font>&nbsp;&nbsp;' % (colour or STEEL, i)
               if numbered else '<font color="%s">\u2013</font>&nbsp;&nbsp;' % (colour or STEEL))
        rows.append([Paragraph(pre + mk(it), ParagraphStyle("qb", parent=S["td"], fontSize=8.2, leading=10.9))])
    t = Table(rows, colWidths=[mm * 160],
              style=TableStyle([
                  ("VALIGN", (0, 0), (-1, -1), "TOP"),
                  ("LEFTPADDING", (0, 0), (-1, -1), 8),
                  ("RIGHTPADDING", (0, 0), (-1, -1), 8),
                  ("TOPPADDING", (0, 0), (-1, -1), 2.2),
                  ("BOTTOMPADDING", (0, 0), (-1, -1), 2.6),
                  ("BACKGROUND", (0, 0), (-1, -1), C("#F7F9FC")),
                  ("LINEBEFORE", (0, 0), (0, -1), 2.0, C(colour or STEEL)),
              ]))
    t.hAlign = "LEFT"
    return [Paragraph(mk(title), S["h4"]), t, Spacer(1, 6)]


def pair_table(title, pairs, left_h="Item", right_h="What it is / why it matters"):
    rows = [[Paragraph(mk(left_h), S["th"]), Paragraph(mk(right_h), S["th"])]]
    for a, b in pairs:
        rows.append([Paragraph(mk(a), S["td"]), Paragraph(mk(b), S["tdj"])])
    t = Table(rows, colWidths=[mm * 46, mm * 122],
              style=TableStyle([
                  ("VALIGN", (0, 0), (-1, -1), "TOP"),
                  ("BACKGROUND", (0, 0), (-1, 0), C(NAVY)),
                  ("LEFTPADDING", (0, 0), (-1, -1), 4.4),
                  ("RIGHTPADDING", (0, 0), (-1, -1), 4.4),
                  ("TOPPADDING", (0, 0), (-1, -1), 3.4),
                  ("BOTTOMPADDING", (0, 0), (-1, -1), 3.6),
                  ("LINEBELOW", (0, 1), (-1, -2), 0.35, C("#DCE3EA")),
                  ("TEXTCOLOR", (0, 1), (0, -1), C("#2B4A6F")),
              ]))
    t.hAlign = "LEFT"
    return [Paragraph(mk(title), S["h4"]), t, Spacer(1, 6)]


def checklist(n, facts, likely, hard, confused, formulas, symptoms, overlooked,
              mistakes, speak, strip, rule_pairs=None, forward=None):
    """Assemble the standard examiner-checklist block for an experiment chapter.

    n: section number prefix, e.g. "1.8"
    formulas: (header, rows, widths) tuple
    """
    out = [("h2", "%s  Examiner\u2019s secret checklist" % n)]
    out.append(("h3", "%s.1  Twenty facts that must be automatic" % n))
    out.append(("raw", facts_block("Twenty facts, two columns", facts)))
    out.append(("h3", "%s.2  The ten most likely questions" % n))
    out.append(("raw", qbox("Asked in almost every viva", likely, numbered=True)))
    out.append(("h3", "%s.3  The ten hardest questions" % n))
    out.append(("raw", qbox("Designed to separate a good answer from a complete one",
                            hard, numbered=True, colour="#A4483B")))
    out.append(("h3", "%s.4  Most commonly confused concepts" % n))
    out.append(("raw", pair_table("Get these pairs right under pressure", confused)))
    out.append(("h3", "%s.5  Formulas, laws and reactions worth memorising" % n))
    hdr, rows, widths = formulas
    out.append(("tbl", hdr, rows, widths, "**Table %sa** Formula sheet for this activity." % n,
                ["l", "l", "l"] + (["l"] if len(hdr) > 3 else [])))
    out.append(("h3", "%s.6  Observations that reveal a mistake" % n))
    out.append(("tbl", ["Observation or symptom", "What it almost certainly means"],
                symptoms, [66, 104],
                "**Table %sb** Symptom to diagnosis. Each row is a ready-made viva answer." % n,
                ["l", "l"]))
    out.append(("h3", "%s.7  Details students overlook but examiners ask" % n))
    out.append(("bul", overlooked))
    out.append(("h3", "%s.8  Practical mistakes that cost marks" % n))
    out.append(("num", mistakes))
    out.append(("cond", 168))
    out.append(("h3", "%s.9  The ninety-second answer" % n))
    out.append(("speak", "Say this if you are asked to explain the activity in one breath", speak))
    out.append(("h3", "%s.10  Last-minute revision strip" % n))
    out.append(("raw", [BOX([mk(x) for x in strip], "key", "Memory strip")]))
    if forward:
        out.append(("h3", "%s.11  What to carry forward from this chapter" % n))
        out.append(("p", "Every activity in this volume shares apparatus, logic or chemistry with at least two "
                         "others. These are the connections an examiner is most likely to probe, and the fastest "
                         "route to a coherent answer when a question crosses two experiments."))
        out.append(("raw", [qbox("Connections worth having ready", forward, numbered=False)]))
    return out
