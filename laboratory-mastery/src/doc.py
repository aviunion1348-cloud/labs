"""Document template: cover, page furniture, custom clickable TOC and PDF outline."""
import re

from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.platypus import (
    BaseDocTemplate, Frame, PageTemplate, Paragraph, Flowable, PageBreak,
)
from reportlab.platypus import IndexingFlowable

import style as ST
from style import NAVY, NAVY_MID, STEEL, RULE, MUTED, INK
from blocks import S

C = colors.HexColor
CONTENT_W = ST.CONTENT_W * mm

_TAG_RE = re.compile(r"&(?!(?:[a-zA-Z]+|#\d+);)")


def mk(text):
    """Mini-markup: **bold**, //italic//, _{sub}, ^{sup}."""
    if not isinstance(text, str):
        return text
    t = _TAG_RE.sub("&amp;", text)
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t, flags=re.S)
    t = re.sub(r"//(.+?)//", r"<i>\1</i>", t, flags=re.S)
    t = re.sub(r"_\{([^}]*)\}", r'<sub size="68%">\1</sub>', t)
    t = re.sub(r"\^\{([^}]*)\}", r'<super size="68%">\1</super>', t)
    return t


class Bookmark(Flowable):
    def __init__(self, level, title, key, toc_text=None, label=None, in_toc=True):
        Flowable.__init__(self)
        self.level = level
        self.title = title
        self.key = key
        self.toc_text = toc_text or title
        self.label = label or ("CHAPTER" if level == 0 else "")
        self.in_toc = in_toc
        self.width = self.height = 0

    def wrap(self, aw, ah):
        return (0, 0)

    def draw(self):
        pass


class MasterTOC(IndexingFlowable):
    """Two-pass table of contents with dot leaders, links and page numbers."""

    def __init__(self, width=CONTENT_W):
        IndexingFlowable.__init__(self)
        self.width = width
        self._entries = []
        self._last = []

    def isIndexing(self):
        return 1

    def isSatisfied(self):
        return self._entries == self._last

    def beforeBuild(self):
        self._last = self._entries[:]
        self._entries = []

    def notify(self, kind, stuff):
        if kind == "TOCEntry":
            self._entries.append(stuff)

    def clearEntries(self):
        self._entries = []

    # -- layout
    def _rows(self, width):
        rows = []
        for level, text, page, key, label in self._last or [(0, "Contents", 0, None, "")]:
            style = S["toc0"] if level == 0 else S["toc1"]
            plain = re.sub(r"<[^>]+>", "", text)
            maxw = width - 40
            if stringWidth(plain, style.fontName, style.fontSize) > maxw:
                while plain and stringWidth(plain + "\u2026", style.fontName, style.fontSize) > maxw:
                    plain = plain[:-1]
                plain += "\u2026"
            h = style.fontSize * 1.45 + (5.0 if level == 0 else 1.2)
            rows.append((level, plain, str(page), key, style, h, label))
        return rows

    def wrap(self, aw, ah):
        self.width = aw
        rows = self._rows(aw)
        # partition into pages
        pages, cur, used = [], [], 0.0
        limit = ah - 6
        for r in rows:
            if used + r[5] > limit and cur:
                pages.append(cur)
                cur, used = [], 0.0
            cur.append(r)
            used += r[5]
        if cur:
            pages.append(cur)
        self._pages = pages
        first = pages[0] if pages else []
        self._first_h = sum(r[5] for r in first)
        # Report the full height so the frame triggers split() for the
        # continuation pages; draw() only paints the first page.
        self.height = self._first_h + sum(sum(r[5] for r in g) for g in pages[1:])
        return (aw, self.height)

    def split(self, aw, ah):
        """Return the whole contents as page-sized chunks.

        Calling split on the first page too, because a split flowable never has
        its own draw() called — the first chunk carries the first page's rows.
        """
        rows = [r for grp in self._pages for r in grp]
        limit = ah - 24
        out, cur, used, first = [], [], 0.0, True
        for r in rows:
            if used + r[5] > limit and cur:
                out.append(TOCChunk(cur, aw, limit, continued=not first))
                first = False
                cur, used = [], 0.0
            cur.append(r)
            used += r[5]
        if cur:
            out.append(TOCChunk(cur, aw, limit, continued=not first))
        return out or []

    def draw(self):
        pass

class TOCChunk(Flowable):
    def __init__(self, rows, width, height=None, continued=True):
        Flowable.__init__(self)
        self.rows = rows
        self.width = width
        self.continued = continued
        self.height = height or (sum(r[5] for r in rows) + 16)

    def wrap(self, aw, ah):
        return (self.width, self.height)

    def draw(self):
        if not self.continued:
            _draw_rows(self.canv, self.rows, self.width, self.height)
            return
        c = self.canv
        c.saveState()
        c.setFont("Serif-Bold", 10.5)
        c.setFillColor(C("#2B4A6F"))
        c.drawString(0, self.height - 9, "Contents, continued")
        c.setStrokeColor(C("#DCE3EA"))
        c.setLineWidth(0.4)
        c.line(0, self.height - 13.5, self.width, self.height - 13.5)
        c.restoreState()
        _draw_rows(self.canv, self.rows, self.width, self.height - 16)


def _draw_rows(canv, rows, width, height):
    canv.saveState()
    y = height
    for level, text, page, key, style, h, label in rows:
        y -= h
        baseline = y + (h - style.fontSize) / 2 + 1.4
        if level == 0:
            canv.setFont("Sans-Bold", 6.6)
            canv.setFillColor(C("#A6B4C4"))
            canv.drawString(0, baseline + 8.6, label or "CHAPTER")
            # rule under chapter label line
            canv.setStrokeColor(C("#E3E9EF"))
            canv.setLineWidth(0.4)
            canv.line(0, baseline + 6.4, width, baseline + 6.4)
        fname = style.fontName
        fsize = style.fontSize
        canv.setFont(fname, fsize)
        canv.setFillColor(style.textColor)
        canv.drawString(0 if level == 0 else 13, baseline, text)
        tw = stringWidth(text, fname, fsize)
        pw = stringWidth(page, "Sans", 7.6)
        start = (0 if level == 0 else 13) + tw + 4
        end = width - pw - 5
        if end > start:
            canv.setFillColor(C("#C3CDD8"))
            canv.setFont("Serif", fsize)
            dot = "."
            dw = stringWidth(". ", fname, fsize)
            n = int((end - start) / dw)
            canvas_txt = ". " * max(n, 0)
            canv.drawString(start, baseline, canvas_txt.rstrip())
        canv.setFont("Sans" if level else "Sans-Bold", 7.6 if level else 7.9)
        canv.setFillColor(C(STEEL) if level else C(NAVY))
        canv.drawRightString(width - 2, baseline, page)
    canv.restoreState()


class NumberedDoc(BaseDocTemplate):
    def __init__(self, filename, **kw):
        BaseDocTemplate.__init__(self, filename, **kw)
        self.cover_pages = 1
        self.body_start_page = None
        self._page_titles = {}
        self.current_chapter = ""
        self._pass = 0

    def beforeDocument(self):
        self._pass += 1
        self.current_chapter = ""
        self._page_titles = {}
        self.body_start_page = None

    def afterFlowable(self, flowable):
        if not isinstance(flowable, Bookmark):
            return
        page = self.page
        if flowable.level == 0 and self.body_start_page is None:
            self.body_start_page = page
        printed = self.page_number(page)
        if flowable.level == 0:
            self.current_chapter = flowable.title
            key = "ch_%s" % flowable.key
            self.canv.bookmarkPage(key)
            self.canv.addOutlineEntry(_plain(flowable.title), key, 0, 0)
            if flowable.in_toc:
                self.notify("TOCEntry", (0, flowable.toc_text, printed, key, flowable.label))
        else:
            key = "sec_%s" % flowable.key
            self.canv.bookmarkPage(key)
            self.canv.addOutlineEntry(_plain(flowable.title), key, 1, 0)
            if flowable.in_toc:
                self.notify("TOCEntry", (1, flowable.toc_text, printed, key, ""))
        self._page_titles[page] = self.current_chapter

    # -- numbering
    def page_number(self, page):
        if self.body_start_page is None:
            return page - self.cover_pages
        return page - self.body_start_page + 1

    def page_label(self, page):
        if page <= self.cover_pages:
            return ""
        if self.body_start_page is None or page < self.body_start_page:
            return _roman(page - self.cover_pages)
        return str(page - self.body_start_page + 1)

    # -- furniture
    def on_cover(self, canv, doc):
        pass

    def on_start(self, canv, doc):
        pass

    def on_end(self, canv, doc):
        page = canv.getPageNumber()
        title = self._page_titles.get(page, self.current_chapter)
        self._furniture(canv, doc, page, title)

    def _furniture(self, canv, doc, page, title):
        if page <= self.cover_pages:
            return
        W, H = ST.PAGE[0] * mm, ST.PAGE[1] * mm
        ml, mr = ST.MARGIN_L * mm, ST.MARGIN_R * mm
        top = H - ST.MARGIN_T * mm
        canv.saveState()
        canv.setStrokeColor(C(RULE))
        canv.setLineWidth(0.5)
        canv.line(ml, top + 5.0 * mm, W - mr, top + 5.0 * mm)
        canv.setFont("Sans", 6.4)
        canv.setFillColor(C("#93A0AE"))
        canv.drawString(ml, top + 6.6 * mm, "COMPLETE LABORATORY MASTERY")
        if title:
            t = _plain(title)
            while canv.stringWidth(t, "Sans", 6.4) > 96 * mm and len(t) > 3:
                t = t[:-2]
            canv.drawRightString(W - mr, top + 6.6 * mm, t.upper())
        # footer
        canv.setStrokeColor(C("#E0E6EC"))
        canv.setLineWidth(0.5)
        canv.line(ml, ST.MARGIN_B * mm - 3.6 * mm, W - mr, ST.MARGIN_B * mm - 3.6 * mm)
        lab = self.page_label(page)
        canv.setFont("Sans-Bold", 7.6)
        canv.setFillColor(C(NAVY))
        canv.drawCentredString(W / 2, ST.MARGIN_B * mm - 8.8 * mm, lab)
        canv.setFont("Sans", 6.0)
        canv.setFillColor(C("#98A5B2"))
        canv.drawString(ml, ST.MARGIN_B * mm - 8.8 * mm, "Practical & advanced viva reference")
        canv.drawRightString(W - mr, ST.MARGIN_B * mm - 8.8 * mm, "Laboratory Mastery Series")
        canv.restoreState()


def _plain(t):
    return re.sub(r"<[^>]+>", "", t)


def _roman(n):
    vals = [(1000, "m"), (900, "cm"), (500, "d"), (400, "cd"), (100, "c"),
            (90, "xc"), (50, "l"), (40, "xl"), (10, "x"), (9, "ix"),
            (5, "v"), (4, "iv"), (1, "i")]
    out = ""
    for v, s in vals:
        while n >= v:
            out += s
            n -= v
    return out


def build_doc(path):
    doc = NumberedDoc(
        path,
        pagesize=(ST.PAGE[0] * mm, ST.PAGE[1] * mm),
        leftMargin=ST.MARGIN_L * mm, rightMargin=ST.MARGIN_R * mm,
        topMargin=ST.MARGIN_T * mm, bottomMargin=ST.MARGIN_B * mm,
        title="Complete Laboratory Mastery: Practical & Advanced Viva Reference",
        author="Laboratory Mastery Series",
        subject="Chemistry and instrumentation laboratory preparation, calculations and viva",
        creator="Laboratory Mastery Series",
        keywords="laboratory practical, viva, spectrophotometry, conductometry, Redwood "
                 "viscometer, Pensky-Martens, EDTA hardness, iodometry, kinetics, alkalinity",
    )
    fw = CONTENT_W
    fh = (ST.PAGE[1] - ST.MARGIN_T - ST.MARGIN_B) * mm
    frame = Frame(ST.MARGIN_L * mm, ST.MARGIN_B * mm, fw, fh, id="main",
                  leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
    full = Frame(0, 0, ST.PAGE[0] * mm, ST.PAGE[1] * mm, id="cover",
                 leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
    doc.addPageTemplates([
        PageTemplate(id="cover", frames=[full], onPage=doc.on_cover),
        PageTemplate(id="front", frames=[frame], onPageEnd=doc.on_end),
        PageTemplate(id="main", frames=[frame], onPageEnd=doc.on_end),
    ])
    return doc
