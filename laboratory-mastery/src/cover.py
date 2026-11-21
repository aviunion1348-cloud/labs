"""Cover and front-matter flowables."""
import math

from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.platypus import Flowable

import style as ST
from style import NAVY, STEEL, RULE, MUTED

C = colors.HexColor


class Cover(Flowable):
    """Full-bleed cover page drawn directly on the canvas."""

    def __init__(self):
        Flowable.__init__(self)
        self.width = ST.PAGE[0] * mm
        self.height = ST.PAGE[1] * mm

    def wrap(self, aw, ah):
        return (self.width, self.height)

    def draw(self):
        c = self.canv
        W, H = self.width, self.height
        ml = 20 * mm
        # background
        c.setFillColor(colors.white)
        c.rect(0, 0, W, H, stroke=0, fill=1)
        # left spine
        c.setFillColor(C(NAVY))
        c.rect(0, 0, 11 * mm, H, stroke=0, fill=1)
        c.setFillColor(C("#2E4E77"))
        c.rect(11 * mm, 0, 1.6 * mm, H, stroke=0, fill=1)
        # fine grid motif (measurement graph paper) faint
        c.setStrokeColor(C("#EDF1F6"))
        c.setLineWidth(0.4)
        for i in range(1, 26):
            c.line(ml, 40 * mm + i * 7 * mm, W - 20 * mm, 40 * mm + i * 7 * mm)
        for i in range(1, 18):
            c.line(ml + i * 10 * mm, 40 * mm, ml + i * 10 * mm, H - 30 * mm)

        # top label
        c.setFillColor(C(STEEL))
        c.setFont("Sans-Bold", 7.6)
        c.drawString(ml + 4 * mm, H - 34 * mm, "LABORATORY MASTERY SERIES  \u00b7  VOLUME I")
        c.setStrokeColor(C(NAVY))
        c.setLineWidth(2.2)
        c.line(ml + 4 * mm, H - 38 * mm, ml + 4 * mm + 22 * mm, H - 38 * mm)

        # title block
        y = H - 62 * mm
        c.setFillColor(C(NAVY))
        c.setFont("Serif-Bold", 40)
        c.drawString(ml + 4 * mm, y, "Complete")
        c.drawString(ml + 4 * mm, y - 14.2 * mm, "Laboratory")
        c.drawString(ml + 4 * mm, y - 28.4 * mm, "Mastery")
        # accent word
        c.setFillColor(C("#A4483B"))
        c.setFont("Serif-Italic", 19)
        c.drawString(ml + 4 * mm, y - 42 * mm, "From zero to examiner-proof")

        # rule
        c.setStrokeColor(C(RULE))
        c.setLineWidth(0.8)
        c.line(ml + 4 * mm, H - 118 * mm, W - 24 * mm, H - 118 * mm)

        # subtitle
        c.setFillColor(C("#2B3F57"))
        c.setFont("Serif", 11.2)
        sub = ["Practical performance  \u00b7  Scientific theory  \u00b7  Worked calculations",
               "Advanced viva preparation  \u00b7  Troubleshooting  \u00b7  Exam simulation"]
        for i, line in enumerate(sub):
            c.drawString(ml + 4 * mm, H - 127 * mm - i * 6.4 * mm, line)

        # contents summary block
        bx, by = ml + 4 * mm, H - 168 * mm
        c.setFillColor(C("#F5F8FB"))
        c.setStrokeColor(C("#E0E7EE"))
        c.setLineWidth(0.6)
        c.rect(bx, by, W - 24 * mm - bx, 34 * mm, stroke=1, fill=1)
        c.setFillColor(C(NAVY))
        c.setFont("Sans-Bold", 6.8)
        c.drawString(bx + 5 * mm, by + 27 * mm, "ELEVEN LABORATORY ACTIVITIES")
        c.setFillColor(C("#3A4B5E"))
        c.setFont("Serif", 8.1)
        rows = [
            "1  Spectrophotometry of cobalt chloride    \u00b7    2  Acid-catalysed hydrolysis kinetics",
            "3  pH-metric titration    \u00b7    4  Conductometric titration    \u00b7    5  Volumetric HCl assay",
            "6  Total hardness by EDTA    \u00b7    7  pH and alkalinity    \u00b7    8  Residual chlorine",
            "9  Redwood viscometry and density    \u00b7    10  Flash and fire point    \u00b7    11  Diazoaminobenzene",
        ]
        for i, r in enumerate(rows):
            c.drawString(bx + 5 * mm, by + 21.5 * mm - i * 5.0 * mm, r)

        # bottom block
        c.setFillColor(C("#FBF4E2"))
        c.setStrokeColor(C("#C89B3C"))
        c.setLineWidth(0.6)
        c.rect(ml + 4 * mm, 44 * mm, W - 24 * mm - ml, 24 * mm, stroke=1, fill=1)
        c.setFillColor(C("#7A5A18"))
        c.setFont("Sans-Bold", 6.6)
        c.drawString(ml + 8 * mm, 61 * mm, "SOURCE DISCIPLINE")
        c.setFillColor(C("#4A3C1E"))
        c.setFont("Serif", 8.0)
        c.drawString(ml + 8 * mm, 55.5 * mm,
                     "Built from the three supplied laboratory guides. Every supplied fact is marked;")
        c.drawString(ml + 8 * mm, 50.7 * mm,
                     "no experimental readings are invented, and every unreadable source detail is flagged.")

        # imprint
        c.setFillColor(C(MUTED))
        c.setFont("Sans", 6.6)
        c.drawString(ml + 4 * mm, 30 * mm,
                     "Prepared for undergraduate chemistry and instrumentation laboratory courses")
        c.setFont("Sans-Bold", 6.8)
        c.setFillColor(C(NAVY))
        c.drawString(ml + 4 * mm, 24 * mm, "ACADEMIC STUDY REFERENCE")
        c.setFont("Sans", 6.6)
        c.setFillColor(C("#8B98A6"))
        c.drawRightString(W - 20 * mm, 24 * mm, "Edition 1.0")

        # decorative apparatus line-art bottom-right
        cx, cy = W - 46 * mm, 74 * mm
        c.setStrokeColor(C("#C9D5E1"))
        c.setLineWidth(1.1)
        # conical flask
        p = c.beginPath()
        p.moveTo(cx - 6, cy + 22); p.lineTo(cx + 6, cy + 22)
        p.lineTo(cx + 17, cy); p.lineTo(cx - 17, cy); p.close()
        c.drawPath(p, stroke=1, fill=0)
        c.line(cx - 6, cy + 22, cx - 6, cy + 27)
        c.line(cx + 6, cy + 22, cx + 6, cy + 27)
        c.setStrokeColor(C("#DCE4EC"))
        for i in range(3):
            c.circle(cx + 30 + i * 8, cy + 8 + i * 4, 1.2, stroke=0, fill=1)
