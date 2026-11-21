"""Reusable document blocks: headings, callouts, tables, equations, figures, viva Q&A."""
import os
import re

from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import (
    BaseDocTemplate, Flowable, Frame, KeepTogether, NextPageTemplate, PageBreak,
    PageTemplate, Paragraph, Spacer, Table, TableStyle, CondPageBreak,
)

import style as ST

S = ST.styles()
CONTENT_WIDTH = ST.CONTENT_W * mm
NAVY = ST.NAVY
NAVY_MID = ST.NAVY_MID
STEEL = ST.STEEL
RULE = ST.RULE
PALE_NAVY = ST.PALE_NAVY
PALE_AMBER = ST.PALE_AMBER
AMBER_EDGE = ST.AMBER_EDGE
PALE_GREEN = ST.PALE_GREEN
GREEN_EDGE = ST.GREEN_EDGE
PALE_RED = ST.PALE_RED
RED_EDGE = ST.RED_EDGE
TABLE_ALT = ST.TABLE_ALT
WHITE = ST.WHITE
INK = ST.INK
MUTED = ST.MUTED


# --------------------------------------------------------------------------- text
def _clean(t):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", t)).strip()


class ChapterHead(Flowable):
    """Chapter opener: kicker, serif title, rule, optional standfirst."""

    def __init__(self, number, title, kicker="", width=CONTENT_WIDTH):
        Flowable.__init__(self)
        self.number = number
        self.title = title
        self.kicker = kicker
        self.width = width
        self.height = 0

    def wrap(self, aw, ah):
        self.width = aw
        body = Paragraph(self.title, S["h1"])
        tw, th = body.wrap(aw - 26 * mm, ah)
        self._body = body
        self._tw, self._th = tw, th
        self.height = th + 26
        return (aw, self.height)

    def draw(self):
        c = self.canv
        # top accent bar
        c.setFillColor(colors.HexColor(NAVY))
        c.rect(0, self.height - 2.6, 34 * mm, 2.6, stroke=0, fill=1)
        c.setFillColor(colors.HexColor(RULE))
        c.rect(34 * mm, self.height - 2.6, self.width - 34 * mm, 0.6, stroke=0, fill=1)
        # number + kicker
        y = self.height - 17
        if self.number:
            c.setFont("Sans-Bold", 8.2)
            c.setFillColor(colors.HexColor(STEEL))
            c.drawString(0, y, self.kicker.upper() if self.kicker else "")
            num = self.number
            c.setFont("Serif-Bold", 21)
            c.setFillColor(colors.HexColor(RULE))
            nw = c.stringWidth(num, "Serif-Bold", 21)
            c.drawRightString(self.width, y - 3, num)
            self._indent = 0
        self._body.drawOn(c, 0, self.height - 18 - self._th)


class H2(Flowable):
    """Section heading with TOC registration support (level 1)."""

    def __init__(self, text, level=2, show_rule=True, toc_text=None):
        Flowable.__init__(self)
        self.text = text
        self.level = level
        self.show_rule = show_rule
        self.toc_text = toc_text or _clean(text)
        self._style = S["h2"] if level == 2 else S["h3"]
        self.width = CONTENT_WIDTH

    def wrap(self, aw, ah):
        self.width = aw
        self._p = Paragraph(self.text, self._style)
        w, h = self._p.wrap(aw, ah)
        self.height = h + (3 if self.show_rule else 0)
        return (aw, self.height)

    def draw(self):
        h = self.height - (3 if self.show_rule else 0)
        self._p.drawOn(self.canv, 0, 3 if self.show_rule else 0)
        if self.show_rule:
            c = self.canv
            c.setStrokeColor(colors.HexColor(RULE))
            c.setLineWidth(0.5)
            c.line(0, 1.2, self.width, 1.2)

    def getBookmarkInfo(self):
        return None


def h2(text, toc=None):
    return H2(text, 2, True, toc)


def h3(text):
    return H2(text, 3, False)


def P(text, style="body"):
    return Paragraph(text, S[style])


def Ps(texts, style="body"):
    return [Paragraph(t, S[style]) for t in texts]


def BUL(items, style="bullet", bullet="\u2022"):
    return [Paragraph(t, S[style], bulletText=bullet) for t in items]


def NUM(items, start=1, style="num"):
    out = []
    for i, t in enumerate(items, start):
        out.append(Paragraph(t, S[style], bulletText="%d." % i))
    return out


def EQ(text, note=None):
    out = [Paragraph(text, S["eq"])]
    if note:
        out.append(Paragraph(note, ParagraphStyle(
            "eqnote", parent=S["caption"], fontSize=8.2, spaceBefore=0, spaceAfter=6)))
    return out


# --------------------------------------------------------------------------- callouts
_BOX_KINDS = {
    "note":    (PALE_NAVY, NAVY, "NOTE"),
    "warn":    (PALE_RED, RED_EDGE, "SAFETY"),
    "key":     (PALE_AMBER, AMBER_EDGE, "KEY POINT"),
    "exam":    (PALE_GREEN, GREEN_EDGE, "EXAMINER'S NOTE"),
    "def":     (PALE_NAVY, NAVY_MID, "DEFINITION"),
    "caution": (PALE_AMBER, AMBER_EDGE, "CAUTION"),
    "pitfall": (PALE_RED, RED_EDGE, "COMMON MISTAKE"),
    "source":  ("#F2F2F0", "#6B6B62", "ON THE SOURCE"),
}


def BOX(content, kind="note", title=None, width=CONTENT_WIDTH, keep=False):
    """Callout box that may split across pages between paragraphs."""
    bg, edge, default_title = _BOX_KINDS[kind]
    if isinstance(content, str):
        content = [content]
    rows, cmds = [], []
    rows.append([Paragraph((title or default_title).upper(),
                           ParagraphStyle("bt", parent=S["boxtitle"],
                                          textColor=colors.HexColor(edge)))])
    cmds += [("BACKGROUND", (0, 0), (-1, 0), colors.HexColor(bg)),
             ("TOPPADDING", (0, 0), (-1, 0), 6),
             ("BOTTOMPADDING", (0, 0), (-1, 0), 2)]
    for item in content:
        if isinstance(item, str):
            item = Paragraph(item, S["box"])
        rows.append([item])
    rows.append([Spacer(1, 1)])
    t = Table(rows, colWidths=[width - 7 * mm],
              style=TableStyle(cmds + [
                  ("BACKGROUND", (0, 1), (-1, -1), colors.HexColor(bg)),
                  ("LEFTPADDING", (0, 0), (-1, -1), 9),
                  ("RIGHTPADDING", (0, 0), (-1, -1), 9),
                  ("TOPPADDING", (0, 1), (-1, -1), 1.5),
                  ("BOTTOMPADDING", (0, 1), (-1, -2), 1.5),
                  ("BOTTOMPADDING", (0, -1), (-1, -1), 5),
                  ("VALIGN", (0, 0), (-1, -1), "TOP"),
                  ("LINEBEFORE", (0, 0), (0, -1), 2.2, colors.HexColor(edge)),
                  ("RIGHTPADDING", (0, 0), (-1, -1), 7),
              ]))
    t.hAlign = "LEFT"
    t.spaceBefore = 5
    t.spaceAfter = 8
    if keep or len(content) <= 4:
        return KeepTogether([t])
    return t


def FIG(path, caption, width=None, height=None, max_h=95 * mm):
    from reportlab.platypus import Image
    from PIL import Image as PILImage

    iw, ih = PILImage.open(path).size
    w = width or CONTENT_WIDTH * 0.86
    h = w * ih / iw
    if h > max_h:
        h = max_h
        w = h * iw / ih
    img = Image(path, width=w, height=h)
    img.hAlign = "CENTER"
    return KeepTogether([Spacer(1, 3), img, Paragraph(caption, S["caption"])])


def TBL(header, rows, widths, caption=None, align=None, zebra=True, font_size=8.4):
    """Professional table: repeated header, zebra rows, hairline grid."""
    hs = []
    for i, htxt in enumerate(header):
        st = S["thc"] if (align and align[i] == "c") else S["th"]
        hs.append(Paragraph(htxt, st))
    data = [hs]
    for r in rows:
        row = []
        for i, cell in enumerate(r):
            if isinstance(cell, str):
                if align and align[i] == "c":
                    row.append(Paragraph(cell, S["tdc"]))
                elif align and align[i] == "j":
                    row.append(Paragraph(cell, S["tdj"]))
                else:
                    row.append(Paragraph(cell, S["td"]))
            else:
                row.append(cell)
        data.append(row)
    total = float(sum(widths))
    avail = CONTENT_WIDTH / mm
    if total > avail:
        widths = [w * avail / total for w in widths]
    cw = [w * mm for w in widths]
    t = Table(data, colWidths=cw, repeatRows=1, splitByRow=1, hAlign="LEFT")
    cmds = [
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor(NAVY)),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 4.2),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4.2),
        ("TOPPADDING", (0, 0), (-1, -1), 3.4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3.6),
        ("LINEBELOW", (0, 1), (-1, -2), 0.4, colors.HexColor("#D3DAE3")),
        ("LINEBELOW", (0, -1), (-1, -1), 0.9, colors.HexColor(STEEL)),
        ("LINEBELOW", (0, 0), (-1, 0), 0.9, colors.HexColor(NAVY)),
    ]
    if zebra:
        for i in range(2, len(data), 2):
            cmds.append(("BACKGROUND", (0, i), (-1, i), colors.HexColor(TABLE_ALT)))
    t.setStyle(TableStyle(cmds))
    t.spaceBefore = 3
    t.spaceAfter = 4
    out = [t]
    if caption:
        out = [KeepTogether([t, Paragraph(caption, S["tabcap"])])]
        out[0]._content[1].style = ParagraphStyle("tc2", parent=S["tabcap"],
                                                  spaceBefore=3, spaceAfter=9)
    else:
        out.append(Spacer(1, 5))
    return out


# --------------------------------------------------------------------------- viva
def QA(qa_list, start=1, label=None, qstyle="q", astyle="a"):
    """Question-answer pairs; question and answer kept together."""
    out = []
    if label:
        out.append(Paragraph(label, S["qsub"]))
    n = start
    for q, a in qa_list:
        qq = Paragraph('<font color="#4A6D8C">Q%d.</font>&nbsp;&nbsp;%s' % (n, q), S[qstyle])
        aa = Paragraph('<font color="#4A6D8C">A.</font>&nbsp;&nbsp;%s' % a, S[astyle])
        out.append(KeepTogether([qq, aa]))
        n += 1
    return out


def QAcount(qa_list):
    return len(qa_list)


def SPACER(h=4):
    return Spacer(1, h)


def HRULE(space_before=6, space_after=6):
    class _R(Flowable):
        def __init__(self):
            Flowable.__init__(self)
            self.width = 0
            self.height = space_before + space_after

        def wrap(self, aw, ah):
            self.width = aw
            return (aw, self.height)

        def draw(self):
            self.canv.setStrokeColor(colors.HexColor(RULE))
            self.canv.setLineWidth(0.6)
            self.canv.line(0, space_after, self.width, space_after)

    return _R()
