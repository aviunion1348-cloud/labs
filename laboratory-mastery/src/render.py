"""Renderer: turns compact content tuples into Platypus flowables."""
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.platypus import (
    Paragraph, Spacer, PageBreak, KeepTogether, Table, TableStyle, CondPageBreak,
    NextPageTemplate,
)
from reportlab.lib.styles import ParagraphStyle

import style as ST
from style import NAVY, STEEL, RULE, MUTED, PALE_NAVY, PALE_AMBER, AMBER_EDGE
from blocks import (S, ChapterHead, H2, BOX, TBL, FIG, EQ, BUL, NUM, HRULE as HRule,
                    CONTENT_WIDTH)
from doc import mk, Bookmark
from figures import schematic
from plots import plot

C = colors.HexColor


def _fmt(text):
    return mk(text)


def render(items, chapter_title=None, level_offset=0):
    """items: list of (kind, ...) tuples."""
    out = []
    for it in items:
        kind = it[0]
        if kind == "h2":
            title = it[1]
            key = it[2] if len(it) > 2 else None
            out.append(Bookmark(1, title, key or _slug(title), toc_text=title))
            out.append(H2(_fmt(title), 2, True))
        elif kind == "h3":
            out.append(H2(_fmt(it[1]), 3, False))
        elif kind == "p":
            out.append(Paragraph(_fmt(it[1]), S["body"]))
        elif kind == "lead":
            out.append(Paragraph(_fmt(it[1]), S["lead"]))
        elif kind == "bul":
            out.extend(BUL([_fmt(x) for x in it[1]]))
        elif kind == "num":
            out.extend(NUM([_fmt(x) for x in it[1]]))
        elif kind == "eq":
            out.extend(EQ(_fmt(it[1]), _fmt(it[2]) if len(it) > 2 else None))
        elif kind == "box":
            kindname, content = it[1], it[2]
            title = it[3] if len(it) > 3 else None
            if isinstance(content, str):
                content = [_fmt(content)]
            else:
                content = [_fmt(x) for x in content]
            out.append(BOX(content, kindname, _fmt(title) if title else None))
        elif kind == "defbox":
            terms = it[1]
            rows = []
            for term, definition in terms:
                rows.append([Paragraph(_fmt("**%s**" % term), S["td"]),
                             Paragraph(_fmt(definition), S["tdj"])])
            t = Table(rows, colWidths=[34 * mm, CONTENT_WIDTH - 34 * mm],
                      style=TableStyle([
                          ("VALIGN", (0, 0), (-1, -1), "TOP"),
                          ("LEFTPADDING", (0, 0), (-1, -1), 0),
                          ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                          ("TOPPADDING", (0, 0), (-1, -1), 2.0),
                          ("BOTTOMPADDING", (0, 0), (-1, -1), 3.4),
                          ("LINEBELOW", (0, 0), (-1, -2), 0.35, C("#DCE3EA")),
                          ("TEXTCOLOR", (0, 0), (0, -1), C("#2B4A6F")),
                      ]))
            out.append(Spacer(1, 3))
            out.append(t)
            out.append(Spacer(1, 7))
        elif kind == "tbl":
            header, rows, widths = it[1], it[2], it[3]
            caption = it[4] if len(it) > 4 else None
            align = it[5] if len(it) > 5 else None
            out.extend(TBL([_fmt(h) for h in header],
                           [[_fmt(c) if isinstance(c, str) else c for c in r] for r in rows],
                           widths, _fmt(caption) if caption else None, align))
        elif kind == "fig":
            key = it[1]
            caption = it[2]
            out.append(CondPageBreak(60 * mm))
            out.append(schematic(key, _fmt(caption)))
            out.append(Spacer(1, 4))
        elif kind == "plot":
            key, caption = it[1], it[2]
            out.append(CondPageBreak(60 * mm))
            out.append(plot(key, _fmt(caption)))
            out.append(Spacer(1, 4))
        elif kind == "qa":
            qlist = it[1]
            label = it[2] if len(it) > 2 else None
            start = it[3] if len(it) > 3 else 1
            if label:
                out.append(Paragraph(_fmt(label), S["qsub"]))
            n = start
            for q, a in qlist:
                qq = Paragraph('<font color="#4A6D8C" name="Sans-Bold" size="7.6">Q%d</font>'
                               '&nbsp;&nbsp;%s' % (n, _fmt(q)), S["q"])
                aa = Paragraph('<font color="#71839A" name="Sans-Bold" size="7.6">A</font>'
                               '&nbsp;&nbsp;%s' % _fmt(a), S["a"])
                out.append(KeepTogether([qq, aa]))
                n += 1
        elif kind == "qsub":
            out.append(Paragraph(_fmt(it[1]), S["qsub"]))
        elif kind == "checklist":
            # it[1] = dict of section -> list of strings
            data = it[1]
            for title, entries in data:
                out.append(Paragraph(_fmt(title), S["h4"]))
                out.extend(BUL([_fmt(x) for x in entries], bullet="\u2013"))
        elif kind == "speak":
            # 60-90 second spoken explanation in a shaded block
            title = it[1] if len(it) > 1 else "Sixty-second answer"
            body = it[2]
            if isinstance(body, (list, tuple)):
                body = " ".join(x.strip() for x in body)
            out.append(BOX([Paragraph(_fmt(body), ParagraphStyle(
                "spk", parent=S["box"], fontName="Serif-Italic", fontSize=9.5,
                leading=13.4, textColor=C("#22303F")))],
                "key", title))
        elif kind == "quote":
            out.append(Paragraph(_fmt(it[1]), S["quote"]))
        elif kind == "hr":
            out.append(HRule(4, 6))
        elif kind == "space":
            out.append(Spacer(1, it[1] if len(it) > 1 else 6))
        elif kind == "pb":
            out.append(PageBreak())
        elif kind == "cond":
            out.append(CondPageBreak(it[1] * mm))
        elif kind == "raw":
            content = it[1]
            if isinstance(content, tuple):
                content = [content]
            out.extend(content)
        elif kind == "sub":
            out.append(Paragraph(_fmt(it[1]), S["small"]))
        else:
            raise ValueError("unknown block %r" % (kind,))
    return out


def _slug(t):
    import re
    s = re.sub(r"<[^>]+>", "", t).lower()
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s[:40]


def _flatten(seq):
    out = []
    for x in seq:
        if isinstance(x, (list, tuple)):
            out.extend(_flatten(x))
        else:
            out.append(x)
    return out


def chapter(ch):
    """Render one chapter opener + body from a dict."""
    out = [NextPageTemplate("main"), PageBreak()]
    _num = ch.get("num")
    out.append(Bookmark(0, ch["title"], ch["key"], toc_text=ch.get("toc", ch["title"]),
                        label=("CHAPTER " + _num) if _num else "CHAPTER"))
    out.append(ChapterHead(ch.get("num", ""), _fmt(ch["title"]),
                           ch.get("kicker", "")))
    out.append(Spacer(1, 7))
    if ch.get("standfirst"):
        out.append(Paragraph(_fmt(ch["standfirst"]), S["lead"]))
    out.extend(_flatten(render(ch["body"])))
    return out
