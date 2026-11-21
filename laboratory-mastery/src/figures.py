"""Vector schematic diagrams drawn directly on the ReportLab canvas.

Each figure is a Flowable that renders crisp, labelled, print-quality line art
in the document's restrained academic palette.
"""
import math

from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.platypus import Flowable

from style import NAVY, NAVY_MID, STEEL, RULE, INK, MUTED, PALE_NAVY, PALE_AMBER

C = colors.HexColor
NAVY_C, STEEL_C, RULE_C, INK_C, MUTED_C = C(NAVY), C(STEEL), C(RULE), C(INK), C(MUTED)
PALE = C(PALE_NAVY)
PALE_A = C(PALE_AMBER)
GLASS = C("#DCE7F2")
LIQUID = C("#C3D6EA")
LIQUID2 = C("#E4CFC0")
WATER = C("#D7E7F3")


class _Bounds:
    """Proxy canvas that records the vertical extent of everything drawn."""

    def __init__(self, real, rec):
        self.real = real
        self.rec = rec

    def __getattr__(self, name):
        return getattr(self.real, name)

    def _mark(self, y_lo, y_hi):
        self.rec["ymin"] = min(self.rec["ymin"], y_lo)
        self.rec["ymax"] = max(self.rec["ymax"], y_hi)

    def line(self, x1, y1, x2, y2):
        self._mark(min(y1, y2) - 1, max(y1, y2) + 1)
        self.real.line(x1, y1, x2, y2)

    def rect(self, x, y, w, h, **kw):
        self._mark(y, y + h)
        self.real.rect(x, y, w, h, **kw)

    def roundRect(self, x, y, w, h, r, **kw):
        self._mark(y, y + h)
        self.real.roundRect(x, y, w, h, r, **kw)

    def circle(self, x, y, r, **kw):
        self._mark(y - r, y + r)
        self.real.circle(x, y, r, **kw)

    def drawString(self, x, y, t, *a, **kw):
        self._mark(y - 2, y + 7)
        self.real.drawString(x, y, t, *a, **kw)

    def drawCentredString(self, x, y, t, *a, **kw):
        self._mark(y - 2, y + 7)
        self.real.drawCentredString(x, y, t, *a, **kw)

    def drawRightString(self, x, y, t, *a, **kw):
        self._mark(y - 2, y + 7)
        self.real.drawRightString(x, y, t, *a, **kw)

    def beginPath(self, *a, **kw):
        path = self.real.beginPath(*a, **kw)
        proxy = path

        class P:
            def __getattr__(self, nm):
                return getattr(path, nm)

            def moveTo(self, x, y):
                self._m(y)
                path.moveTo(x, y)

            def lineTo(self, x, y):
                self._m(y)
                path.lineTo(x, y)

            def _m(self, y):
                self._o.rec["ymin"] = min(self._o.rec["ymin"], y - 1)
                self._o.rec["ymax"] = max(self._o.rec["ymax"], y + 1)

        pp = P()
        pp._o = self
        return pp


_SCRATCH = {}


def _measure(drawfn, w, h):
    from reportlab.pdfgen.canvas import Canvas
    import io
    if "canvas" not in _SCRATCH:
        _SCRATCH["canvas"] = Canvas(io.BytesIO(), pagesize=(600, 800))
        _SCRATCH["canvas"].setPageCompression(0)
    real = _SCRATCH["canvas"]
    real.saveState()
    real.translate(20, 60)
    rec = {"ymin": 1e9, "ymax": -1e9}
    proxy = _Bounds(real, rec)
    drawfn(proxy, w, h)
    real.restoreState()
    if rec["ymax"] < rec["ymin"]:
        return (0, 0, 0)
    return (rec["ymin"], rec["ymax"], rec["ymax"] - rec["ymin"])


class Fig(Flowable):
    """Base flowable: subclasses implement draw_art(canvas, w, h) in points."""

    def __init__(self, height_pt, drawfn, caption=None, style=None, width_mm=None,
                 scale=1.0):
        Flowable.__init__(self)
        self.h = height_pt
        self.scale = scale
        self.drawfn = drawfn
        self.caption = caption
        self.width = 0
        self.capstyle = style
        self._meas = None

    def wrap(self, aw, ah):
        self.width = aw
        cap_h = 0
        if self.caption:
            from blocks import S
            from reportlab.platypus import Paragraph
            self._cap = Paragraph(self.caption, S["caption"])
            cw, cap_h = self._cap.wrap(aw, ah)
            cap_h += 4
        self.cap_h = cap_h
        if self._meas is None:
            try:
                self._meas = _measure(self.drawfn, aw, self.h)
            except Exception:
                self._meas = (0, self.h, self.h)
        ymin, ymax, span = self._meas
        self._ymin = ymin
        self._span = max(span * self.scale, 24)
        return (aw, self._span + cap_h + 2)

    def draw(self):
        c = self.canv
        k = self.scale
        c.saveState()
        c.translate(0, self.cap_h + 1 - self._ymin * k)
        if k != 1.0:
            c.scale(k, k)
        self.drawfn(c, self.width / k, self.h)
        c.restoreState()
        if self.caption:
            self._cap.drawOn(c, 0, 0)


# ------------------------------------------------------------------ primitives
def glass(c, x, y, w, h, fill=GLASS, lw=1.0):
    c.setLineWidth(lw)
    c.setStrokeColor(STEEL_C)
    c.setFillColor(fill)
    c.roundRect(x, y, w, h, 2.5, stroke=1, fill=1)


def tube(c, x, y, w, h, fill=None):
    c.setLineWidth(0.9)
    c.setStrokeColor(INK_C)
    if fill:
        c.setFillColor(fill)
    c.rect(x, y, w, h, stroke=1, fill=1 if fill else 0)


def arrow(c, x1, y1, x2, y2, colour=None, lw=0.9, head=3.4, dash=None):
    c.setStrokeColor(colour or STEEL_C)
    c.setLineWidth(lw)
    if dash:
        c.setDash(dash, 2)
    c.line(x1, y1, x2, y2)
    c.setDash()
    a = math.atan2(y2 - y1, x2 - x1)
    c.setFillColor(colour or STEEL_C)
    p = c.beginPath()
    p.moveTo(x2, y2)
    p.lineTo(x2 - head * math.cos(a - 0.42), y2 - head * math.sin(a - 0.42))
    p.lineTo(x2 - head * math.cos(a + 0.42), y2 - head * math.sin(a + 0.42))
    p.close()
    c.drawPath(p, stroke=0, fill=1)


def label(c, x, y, text, size=6.6, colour=None, anchor="l", bold=False,
          italic=False):
    f = "Sans"
    if bold:
        f = "Sans-Bold"
    c.setFont(f, size)
    c.setFillColor(colour or INK_C)
    if anchor == "c":
        c.drawCentredString(x, y, text)
    elif anchor == "r":
        c.drawRightString(x, y, text)
    else:
        c.drawString(x, y, text)
    return c.stringWidth(text, f, size)


def leader(c, x1, y1, x2, y2, text, size=6.4, anchor="l", colour=None, dy=2.2):
    """Annotation with a thin leader line."""
    c.setStrokeColor(C("#8A9AAB"))
    c.setLineWidth(0.45)
    c.line(x1, y1, x2, y2)
    c.setFillColor(colour or C("#8A9AAB"))
    c.circle(x1, y1, 0.9, stroke=0, fill=1)
    label(c, x2 + (2 if anchor == "l" else -2), y2 + dy, text, size,
          colour or C("#33414F"), anchor)


def axis(c, x, y, w, h, xlabel, ylabel, xticks=None, yticks=None,
         xmin=0, xmax=1, ymin=0, ymax=1, xfmt="%.0f", yfmt="%.0f", ticklen=2.2):
    c.setStrokeColor(C("#5C6B7A"))
    c.setLineWidth(0.8)
    c.line(x, y, x, y + h)
    c.line(x, y, x + w, y)
    label(c, x + w / 2, y - 23, xlabel, 7.2, INK_C, "c", bold=False)
    c.saveState()
    c.translate(x - 30, y + h / 2)
    c.rotate(90)
    label(c, 0, 0, ylabel, 7.2, INK_C, "c")
    c.restoreState()
    c.setLineWidth(0.5)
    for t in (xticks or []):
        px = x + w * (t - xmin) / (xmax - xmin)
        c.line(px, y, px, y - ticklen)
        label(c, px, y - 9.5, xfmt % t, 6.0, MUTED_C, "c")
    for t in (yticks or []):
        py = y + h * (t - ymin) / (ymax - ymin)
        c.line(x, py, x - ticklen, py)
        label(c, x - 4, py - 2.1, yfmt % t, 6.0, MUTED_C, "r")
    return (lambda vx: x + w * (vx - xmin) / (xmax - xmin),
            lambda vy: y + h * (vy - ymin) / (ymax - ymin))


def bezier_points(xs, ys, n=160):
    """Simple Catmull-Rom interpolation for smooth curves in canvas figures."""
    pts = list(zip(xs, ys))
    if len(pts) < 3:
        return pts
    out = []
    for i in range(len(pts) - 1):
        p0 = pts[max(i - 1, 0)]
        p1, p2 = pts[i], pts[i + 1]
        p3 = pts[min(i + 2, len(pts) - 1)]
        for k in range(n // (len(pts) - 1) + 1):
            t = k / (n // (len(pts) - 1) + 1)
            t2, t3 = t * t, t * t * t
            xx = 0.5 * ((2 * p1[0]) + (-p0[0] + p2[0]) * t +
                        (2 * p0[0] - 5 * p1[0] + 4 * p2[0] - p3[0]) * t2 +
                        (-p0[0] + 3 * p1[0] - 3 * p2[0] + p3[0]) * t3)
            yy = 0.5 * ((2 * p1[1]) + (-p0[1] + p2[1]) * t +
                        (2 * p0[1] - 5 * p1[1] + 4 * p2[1] - p3[1]) * t2 +
                        (-p0[1] + 3 * p1[1] - 3 * p2[1] + p3[1]) * t3)
            out.append((xx, yy))
    out.append(pts[-1])
    return out


def polyline(c, pts, colour=None, lw=1.4, dash=None, fill=None):
    p = c.beginPath()
    p.moveTo(*pts[0])
    for pt in pts[1:]:
        p.lineTo(*pt)
    if fill:
        p.close()
    c.setStrokeColor(colour or NAVY_C)
    c.setLineWidth(lw)
    c.setFillColor(fill) if fill else None
    if dash:
        c.setDash(dash, 2)
    c.drawPath(p, stroke=1, fill=1 if fill else 0)
    c.setDash()


# ------------------------------------------------------------------ apparatus art
def _beaker(c, x, y, w, h, liq_frac=0.55, liq=LIQUID, lip=True):
    glass(c, x, y, w, h, fill=GLASS)
    c.setFillColor(liq)
    c.rect(x + 1.1, y + 1.1, w - 2.2, (h - 2.2) * liq_frac, stroke=0, fill=1)
    if lip:
        c.setStrokeColor(STEEL_C)
        c.setLineWidth(1.1)
        c.line(x + w - w * 0.16, y + h, x + w + 2.4, y + h + 2.2)


def _burette(c, x, y_top, h, w=6.2, liq_frac=0.0, liq=LIQUID):
    c.setLineWidth(0.9)
    c.setStrokeColor(INK_C)
    c.setFillColor(C("#FFFFFF"))
    c.rect(x, y_top - h, w, h, stroke=1, fill=1)
    # taper + tip
    p = c.beginPath()
    p.moveTo(x, y_top - h)
    p.lineTo(x + w, y_top - h)
    p.lineTo(x + w * 0.62, y_top - h - 7)
    p.lineTo(x + w * 0.38, y_top - h - 7)
    p.close()
    c.setFillColor(C("#FFFFFF"))
    c.drawPath(p, stroke=1, fill=1)
    c.setStrokeColor(INK_C)
    c.line(x + w * 0.5, y_top - h - 7, x + w * 0.5, y_top - h - 13)
    # graduation marks
    c.setLineWidth(0.4)
    c.setStrokeColor(C("#7C8B9B"))
    for i in range(1, 14):
        yy = y_top - h * i / 14.0
        c.line(x, yy, x + (w * 0.55 if i % 2 == 0 else w * 0.3), yy)
    # stopcock
    c.setFillColor(C("#B9C6D4"))
    c.setStrokeColor(C("#7C8B9B"))
    c.circle(x + w / 2, y_top - h - 2, 2.5, stroke=1, fill=1)
    c.line(x + w / 2 - 3.6, y_top - h - 2, x + w / 2 - 1.2, y_top - h - 4.4)
    if liq_frac:
        c.setFillColor(liq)
        c.rect(x + 0.7, y_top - h, w - 1.4, (h - 1) * liq_frac * 0 + (h * liq_frac),
               stroke=0, fill=1)


def _conical(c, x, y, w, h, liq_frac=0.4, liq=LIQUID):
    p = c.beginPath()
    neck = w * 0.24
    p.moveTo(x + (w - neck) / 2, y + h)
    p.lineTo(x + (w + neck) / 2, y + h)
    p.lineTo(x + w, y)
    p.lineTo(x, y)
    p.close()
    c.setStrokeColor(STEEL_C)
    c.setLineWidth(1.0)
    c.setFillColor(GLASS)
    c.drawPath(p, stroke=1, fill=1)
    # liquid
    lh = h * liq_frac
    ll = (w / 2) * (lh / h)
    p2 = c.beginPath()
    p2.moveTo(x + w / 2 - ll, y + lh)
    p2.lineTo(x + w / 2 + ll, y + lh)
    p2.lineTo(x + w, y)
    p2.lineTo(x, y)
    p2.close()
    c.setFillColor(liq)
    c.drawPath(p2, stroke=0, fill=1)
    # graduation
    c.setStrokeColor(C("#8A9AAB"))
    c.setLineWidth(0.4)
    for f in (0.22, 0.32, 0.42):
        yy = y + h * f
        xx = (w / 2) * (f) * 2
        c.line(x + w / 2 - xx + 2, yy, x + w / 2 - xx + 5.5, yy)


def _stand(c, x, y_base, h):
    c.setFillColor(C("#9AA7B4"))
    c.setStrokeColor(C("#7C8B9B"))
    c.rect(x - 13, y_base, 26, 2.6, stroke=1, fill=1)
    c.rect(x - 0.9, y_base + 2.6, 1.8, h, stroke=1, fill=1)


# ------------------------------------------------------------------ FIGURES
def fig_spectrophotometer(c, w, h):
    y0 = h * 0.42 + 14
    # instrument body
    c.setFillColor(PALE)
    c.setStrokeColor(STEEL_C)
    c.setLineWidth(1.0)
    c.roundRect(4, y0 - 16, w - 60, 46, 3, stroke=1, fill=1)
    # lamp
    c.setFillColor(C("#F2E3C4"))
    c.circle(22, y0 + 8, 7, stroke=1, fill=1)
    label(c, 22, y0 + 5, "lamp", 5.8, INK_C, "c")
    arrow(c, 30, y0 + 8, 46, y0 + 8)
    # monochromator prism
    p = c.beginPath()
    p.moveTo(58, y0 + 16); p.lineTo(46, y0 + 0); p.lineTo(70, y0 + 0); p.close()
    c.setFillColor(C("#D6E2EE")); c.setStrokeColor(STEEL_C); c.setLineWidth(0.9)
    c.drawPath(p, stroke=1, fill=1)
    label(c, 58, y0 - 8, "monochromator", 5.8, MUTED_C, "c")
    label(c, 58, y0 - 15.5, "(prism / grating)", 5.2, MUTED_C, "c")
    arrow(c, 72, y0 + 8, 96, y0 + 8)
    # cuvette
    c.setFillColor(GLASS); c.setStrokeColor(STEEL_C)
    c.rect(100, y0 - 4, 10, 24, stroke=1, fill=1)
    c.setFillColor(C("#E9C9D2"))
    c.rect(101, y0 - 3, 8, 14, stroke=0, fill=1)
    label(c, 105, y0 + 27, "cuvette", 5.8, MUTED_C, "c")
    label(c, 105, y0 + 20.5, "(sample, l)", 5.2, MUTED_C, "c")
    arrow(c, 112, y0 + 8, 132, y0 + 8)
    # detector
    c.setFillColor(C("#CFE0D6")); c.setStrokeColor(STEEL_C)
    c.rect(134, y0 - 2, 14, 20, stroke=1, fill=1)
    label(c, 141, y0 - 8, "detector", 5.6, MUTED_C, "c")
    arrow(c, 150, y0 + 8, 164, y0 + 8)
    # readout
    c.setFillColor(C("#FFFFFF")); c.setStrokeColor(STEEL_C)
    c.roundRect(w - 12 - 82, y0 + 18, 82, 30, 2, stroke=1, fill=1)
    c.setFillColor(C("#E8EEF6"))
    c.roundRect(w - 12 - 76, y0 + 24, 70, 17, 1.5, stroke=0, fill=1)
    label(c, w - 12 - 41, y0 + 30, "A = 0.412", 8.2, NAVY_C, "c", bold=True)
    label(c, w - 12 - 41, y0 + 52, "digital read-out", 6.0, MUTED_C, "c")
    # beam labels
    label(c, 38, y0 + 12.5, "I", 7.0, NAVY_C, "c", bold=True)
    c.setFont("Serif", 5)
    label(c, 124, y0 + 12.5, "I", 7.0, NAVY_C, "c", bold=True)



def fig_titration_setup(c, w, h, analyte="HCl", titrant="NaOH", probe="pH electrode"):
    """Compact burette-and-flask assembly drawn to fill the given height."""
    base = 12
    top = h - 8
    span = top - base
    cx = w * 0.30
    # retort stand
    c.setFillColor(C("#9AA7B4"))
    c.setStrokeColor(C("#7C8B9B"))
    c.rect(cx - 46, base, 26, 2.6, stroke=1, fill=1)
    c.rect(cx - 33.4, base + 2.6, 1.8, span * 0.88, stroke=1, fill=1)
    # burette: upper 46 % of the span
    b_top = top - span * 0.06
    b_len = span * 0.46
    _burette(c, cx - 6, b_top, b_top - b_len, liq_frac=0.85)
    label(c, cx - 16, b_top - 6, "burette", 6.4, MUTED_C, "r")
    label(c, cx - 16, b_top - 13, titrant, 6.8, NAVY_C, "r", bold=True)
    # flask below the burette tip
    fl_h = span * 0.30
    fl_y = base + span * 0.10
    _conical(c, cx - 22, fl_y, 44, fl_h, liq_frac=0.45)
    label(c, cx, fl_y + fl_h * 0.55, analyte, 6.6, NAVY_C, "c", bold=True)
    label(c, cx, fl_y - 7, "conical flask", 5.4, MUTED_C, "c")
    # probe, right of the flask
    px = cx + 46
    c.setStrokeColor(C("#7C8B9B")); c.setLineWidth(2.2)
    c.line(px, top - span * 0.10, px, fl_y + fl_h * 0.55)
    c.setFillColor(C("#CBD8E4")); c.setStrokeColor(STEEL_C); c.setLineWidth(0.7)
    c.circle(px, fl_y + fl_h * 0.55, 2.6, stroke=1, fill=1)
    label(c, px + 6, top - span * 0.12, probe, 6.6, NAVY_C, "l", bold=True)
    # meter box
    c.setFillColor(C("#FFFFFF")); c.setStrokeColor(STEEL_C)
    c.roundRect(px + 6, fl_y + fl_h * 0.62, 46, 18, 2, stroke=1, fill=1)
    label(c, px + 29, fl_y + fl_h * 0.62 + 11, "meter", 6.0, MUTED_C, "c")
    label(c, px + 29, fl_y + fl_h * 0.62 + 4.5, "display", 5.2, MUTED_C, "c")
    c.setStrokeColor(C("#9FAEBD")); c.setLineWidth(0.8); c.setDash(2, 2)
    c.line(px + 2.6, fl_y + fl_h * 0.62 + 9, px + 6, fl_y + fl_h * 0.62 + 9)
    c.setDash()
    # stirrer bar
    c.setStrokeColor(C("#7C8B9B")); c.setLineWidth(1.0)
    c.setFillColor(C("#B8C6D4"))
    c.rect(cx - 7, fl_y + 2, 14, 2.4, stroke=1, fill=1)
    label(c, cx, fl_y - 15, "stirrer bar", 5.2, MUTED_C, "c")


def fig_conductometry(c, w, h):
    """Conductometric titration: burette, cell with electrodes, meter."""
    base = 12
    top = h - 8
    span = top - base
    cx = w * 0.30
    # retort stand
    c.setFillColor(C("#9AA7B4")); c.setStrokeColor(C("#7C8B9B"))
    c.rect(cx - 44, base, 26, 2.6, stroke=1, fill=1)
    c.rect(cx - 31.4, base + 2.6, 1.8, span * 0.90, stroke=1, fill=1)
    # burette
    b_top = top - span * 0.04
    b_len = span * 0.48
    _burette(c, cx - 6, b_top, b_len, liq_frac=0.9)
    label(c, cx - 14, b_top - 5, "burette", 6.2, MUTED_C, "r")
    label(c, cx - 14, b_top - 12, "NaOH", 6.8, NAVY_C, "r", bold=True)
    # beaker with solution
    bk_w, bk_h = 46, span * 0.26
    bk_y = base + span * 0.12
    _beaker(c, cx - bk_w / 2, bk_y, bk_w, bk_h, liq_frac=0.62)
    label(c, cx, bk_y + bk_h * 0.72, "HCl + NaCl", 6.0, NAVY_C, "c", bold=True)
    label(c, cx, bk_y - 7, "conductivity cell", 5.4, MUTED_C, "c")
    # electrode plates
    c.setFillColor(C("#9FB0C2")); c.setStrokeColor(C("#6C7E90"))
    c.rect(cx - 11, bk_y + 3, 3, bk_h * 0.70, stroke=1, fill=1)
    c.rect(cx + 8, bk_y + 3, 3, bk_h * 0.70, stroke=1, fill=1)
    # leads from the plates up and across to the meter
    mx = w * 0.68
    c.setStrokeColor(C("#5C6B7A")); c.setLineWidth(1.0)
    c.line(cx - 9.5, bk_y + bk_h * 0.70, cx - 9.5, fl_top := (bk_y + bk_h + span * 0.06))
    c.line(cx + 9.5, bk_y + bk_h * 0.70, cx + 9.5, fl_top)
    c.line(cx - 9.5, fl_top, mx, fl_top)
    c.line(cx + 9.5, fl_top + 4, mx, fl_top + 4)
    # meter
    m_y = fl_top - 14
    c.setFillColor(PALE); c.setStrokeColor(STEEL_C); c.setLineWidth(1.0)
    c.roundRect(mx, m_y, 78, 34, 3, stroke=1, fill=1)
    c.setFillColor(C("#E8EEF6"))
    c.roundRect(mx + 6, m_y + 16, 66, 13, 1.5, stroke=0, fill=1)
    label(c, mx + 39, m_y + 20, "2.84 mS", 7.6, NAVY_C, "c", bold=True)
    label(c, mx + 39, m_y + 6, "conductivity meter", 5.8, MUTED_C, "c")
    c.setFillColor(C("#7C8B9B"))
    c.circle(mx, fl_top + 2, 1.6, stroke=0, fill=1)


def fig_redwood(c, w, h):
    """Cross-section of Redwood Viscometer I."""
    cx = w * 0.42
    base = 10
    # water bath
    c.setFillColor(WATER); c.setStrokeColor(STEEL_C); c.setLineWidth(1.0)
    c.rect(cx - 58, base + 16, 116, 58, stroke=1, fill=1)
    label(c, cx - 54, base + 60, "water bath", 6.4, C("#3B5A72"), "l")
    # oil cup
    c.setFillColor(C("#EFE3C9")); c.setStrokeColor(C("#8A6D3B")); c.setLineWidth(1.1)
    c.rect(cx - 26, base + 34, 52, 40, stroke=1, fill=1)
    label(c, cx, base + 56, "oil cup", 6.2, C("#6B5326"), "c")
    label(c, cx, base + 48, "(brass)", 5.2, C("#6B5326"), "c")
    # oil
    c.setFillColor(C("#E7CF9E"))
    c.rect(cx - 25, base + 35, 50, 30, stroke=0, fill=1)
    # fill pointer
    c.setStrokeColor(C("#A4483B")); c.setLineWidth(0.8)
    c.line(cx - 26, base + 66, cx - 36, base + 66)
    label(c, cx - 38, base + 64, "fill mark", 5.6, C("#A4483B"), "r")
    # agate jet
    c.setFillColor(C("#CFE3E8")); c.setStrokeColor(C("#3F6D7A")); c.setLineWidth(0.8)
    p = c.beginPath()
    p.moveTo(cx - 5, base + 34); p.lineTo(cx + 5, base + 34)
    p.lineTo(cx + 2.2, base + 22); p.lineTo(cx - 2.2, base + 22); p.close()
    c.drawPath(p, stroke=1, fill=1)
    leader(c, cx + 6, base + 26, cx + 40, base + 20, "agate jet (calibrated orifice)")
    # ball valve
    c.setFillColor(C("#B8C6D4")); c.setStrokeColor(C("#6C7E90"))
    c.circle(cx + 14, base + 36, 4.2, stroke=1, fill=1)
    leader(c, cx + 14, base + 40.5, cx + 40, base + 44, "ball valve")
    # thermometer
    c.setStrokeColor(C("#8A9AAB")); c.setLineWidth(1.6)
    c.line(cx - 20, base + 76, cx - 20, base + 52)
    c.setFillColor(C("#C24E3C"))
    c.circle(cx - 20, base + 51.5, 1.8, stroke=0, fill=1)
    label(c, cx - 26, base + 78, "thermometer", 5.8, MUTED_C, "r")
    # stirrer
    c.setStrokeColor(C("#8A9AAB")); c.setLineWidth(0.8)
    c.line(cx + 34, base + 76, cx + 34, base + 30)
    label(c, cx + 37, base + 78, "stirrer", 5.8, MUTED_C, "l")
    # receiver
    _conical(c, cx - 16, base + 0, 32, 16, liq_frac=0.5, liq=C("#E7CF9E"))
    c.setStrokeColor(C("#A4483B")); c.setLineWidth(0.7)
    c.line(cx + 2, base + 8, cx + 8, base + 8)
    label(c, cx + 10, base + 6.5, "50 mL mark", 5.6, C("#A4483B"), "l")
    # levelling screws
    c.setFillColor(C("#9AA7B4")); c.setStrokeColor(C("#6C7E90"))
    for dx in (-52, 50):
        c.rect(cx + dx, base + 11, 6, 5, stroke=1, fill=1)
    label(c, cx - 70, base + 12, "levelling screws", 5.6, MUTED_C, "l")



def fig_pensky(c, w, h):
    cx = w * 0.44
    base = 12
    # bath
    c.setFillColor(WATER); c.setStrokeColor(STEEL_C); c.setLineWidth(1.0)
    c.rect(cx - 62, base + 14, 124, 52, stroke=1, fill=1)
    label(c, cx - 58, base + 56, "air bath / heater", 6.2, C("#3B5A72"), "l")
    # cup
    c.setFillColor(C("#EFE3C9")); c.setStrokeColor(C("#8A6D3B")); c.setLineWidth(1.1)
    c.rect(cx - 30, base + 30, 60, 38, stroke=1, fill=1)
    c.setFillColor(C("#E7CF9E"))
    c.rect(cx - 29, base + 31, 58, 28, stroke=0, fill=1)
    label(c, cx, base + 46, "brass oil cup", 6.2, C("#6B5326"), "c")
    label(c, cx, base + 39, "filled to mark", 5.2, C("#6B5326"), "c")
    # lid
    c.setFillColor(C("#C9D5E1")); c.setStrokeColor(C("#5C6B7A")); c.setLineWidth(1.0)
    c.rect(cx - 34, base + 68, 68, 5, stroke=1, fill=1)
    label(c, cx + 38, base + 69, "lid (standard openings)", 5.8, MUTED_C, "l")
    # thermometer through lid
    c.setStrokeColor(C("#8A9AAB")); c.setLineWidth(1.6)
    c.line(cx - 18, base + 92, cx - 18, base + 50)
    c.setFillColor(C("#C24E3C")); c.circle(cx - 18, base + 49, 1.8, stroke=0, fill=1)
    label(c, cx - 22, base + 94, "thermometer", 5.8, MUTED_C, "r")
    # stirrer
    c.setStrokeColor(C("#8A9AAB")); c.setLineWidth(0.8)
    c.line(cx + 2, base + 92, cx + 2, base + 46)
    c.setFillColor(C("#B8C6D4"))
    c.rect(cx - 4, base + 44, 12, 2, stroke=0, fill=1)
    label(c, cx + 6, base + 94, "stirrer", 5.8, MUTED_C, "l")
    # pilot flame + shutter
    c.setFillColor(C("#F0C05A")); c.setStrokeColor(C("#C08A20")); c.setLineWidth(0.6)
    p = c.beginPath()
    p.moveTo(cx + 26, base + 74); p.lineTo(cx + 31, base + 84)
    p.lineTo(cx + 36, base + 74); p.close()
    c.drawPath(p, stroke=1, fill=1)
    label(c, cx + 40, base + 80, "pilot burner", 5.8, MUTED_C, "l")
    c.setFillColor(C("#B8C6D4")); c.setStrokeColor(C("#5C6B7A"))
    c.rect(cx + 12, base + 70, 3, 7, stroke=1, fill=1)
    label(c, cx + 12, base + 61, "shutter", 5.4, MUTED_C, "c")
    # flame exposure arrow
    arrow(c, cx + 26, base + 78, cx + 6, base + 78, C("#C08A20"), 0.8, 2.6, dash=(2, 2))



def fig_complexometric(c, w, h):
    """EDTA endpoint: wine red -> blue."""
    y = h * 0.28
    positions = [(w * 0.16, "before equivalence", "#8E3B4E", "wine-red"), (w * 0.52, "at equivalence", "#2E6FA8", "blue")]
    for (x, capt, col, name) in positions:
        _conical(c, x, y, 56, 44, liq_frac=0.42, liq=C(col))
        label(c, x + 28, y - 10, capt, 6.2, MUTED_C, "c")
        label(c, x + 28, y - 17, name, 6.4, C(col), "c", bold=True)
    arrow(c, positions[0][0] + 62, y + 20, positions[1][0] - 8, y + 20, NAVY_C, 1.0, 3.4)
    label(c, (positions[0][0] + positions[1][0]) / 2 + 26, y + 24, "EDTA added", 6.2, NAVY_C, "c")



def fig_iodometry_flow(c, w, h):
    steps = [("water sample", "V mL, Cl\u2082 present"),
             ("add KI + acid", "Cl\u2082 + 2I\u207b \u2192 2Cl\u207b + I\u2082"),
             ("liberated I\u2082", "brown / yellow solution"),
             ("titrate S\u2082O\u2083\u00b2\u207b", "starch \u2192 blue"),
             ("endpoint", "blue disappears (colourless)")]
    n = len(steps)
    bw = (w - 16) / n - 8
    yy = h * 0.42
    for i, (t1, t2) in enumerate(steps):
        x = 8 + i * (bw + 8)
        c.setFillColor(PALE if i % 2 == 0 else C("#F3F6FA"))
        c.setStrokeColor(STEEL_C)
        c.setLineWidth(0.8)
        c.roundRect(x, yy - 12, bw, 34, 2, stroke=1, fill=1)
        label(c, x + bw / 2, yy + 12, t1, 6.6, NAVY_C, "c", bold=True)
        # wrap t2 into two lines if long
        words = t2.split(" ")
        lines, cur = [], ""
        for wd in words:
            test = (cur + " " + wd).strip()
            if c.stringWidth(test, "Sans", 5.2) > bw - 6 and cur:
                lines.append(cur)
                cur = wd
            else:
                cur = test
        lines.append(cur)
        for j, ln in enumerate(lines[:3]):
            label(c, x + bw / 2, yy + 3 - j * 6.4, ln, 5.2, MUTED_C, "c")
        if i < n - 1:
            arrow(c, x + bw + 0.5, yy + 5, x + bw + 7.2, yy + 5, C("#8A9AAB"), 0.7, 2.4)



def fig_density_bottle(c, w, h):
    cx = w * 0.22
    base = h * 0.36
    _conical(c, cx, base, 54, 46, liq_frac=0.5, liq=C("#E7CF9E"))
    c.setStrokeColor(INK_C); c.setLineWidth(1.0)
    c.line(cx + 21, base + 46, cx + 21, base + 54)
    c.circle(cx + 21, base + 56, 3.2, stroke=1, fill=1)
    c.setFillColor(C("#C9D5E1"))
    c.circle(cx + 21, base + 56, 3.2, stroke=0, fill=1)
    c.setStrokeColor(C("#A4483B")); c.setLineWidth(0.7)
    c.line(cx + 27, base + 40, cx + 34, base + 40)
    label(c, cx + 36, base + 38, "calibration mark", 5.6, C("#A4483B"), "l")
    label(c, cx + 27, base - 12, "specific gravity bottle", 6.2, MUTED_C, "c")
    # balance
    bx = w * 0.58
    c.setFillColor(PALE); c.setStrokeColor(STEEL_C); c.setLineWidth(1.0)
    c.rect(bx, base + 4, 96, 12, stroke=1, fill=1)
    c.setFillColor(C("#DCE7F2"))
    c.rect(bx + 8, base + 16, 80, 4, stroke=1, fill=1)
    c.circle(bx + 48, base + 22, 9, stroke=1, fill=1)
    c.setFillColor(C("#FFFFFF"))
    c.circle(bx + 48, base + 22, 9, stroke=0, fill=1)
    c.setStrokeColor(STEEL_C)
    c.circle(bx + 48, base + 22, 9, stroke=1, fill=0)
    label(c, bx + 48, base + 20, "g", 7.0, MUTED_C, "c")
    label(c, bx + 48, base - 6, "analytical balance", 6.2, MUTED_C, "c")
    label(c, bx + 48, base - 13, "\u03c1 = (w\u2083 \u2212 w\u2081) / V", 7.0, NAVY_C, "c", bold=True)



def fig_diazo(c, w, h):
    """Diazoaminobenzene structure."""
    cy = h * 0.52
    # rings
    def ring(x, label_):
        R = 15
        pts = [(x + R * math.cos(math.radians(90 + 60 * k)),
                cy + R * math.sin(math.radians(90 + 60 * k))) for k in range(6)]
        p = c.beginPath()
        p.moveTo(*pts[0])
        for pt in pts[1:]:
            p.lineTo(*pt)
        p.close()
        c.setStrokeColor(NAVY_C); c.setLineWidth(1.2)
        c.drawPath(p, stroke=1, fill=0)
        # inner circle
        c.circle(x, cy, R * 0.56, stroke=1, fill=0)
        label(c, x, cy - 26, label_, 6.0, MUTED_C, "c")

    ring(w * 0.20, "aryl (from aniline)")
    ring(w * 0.68, "aryl (from aniline)")
    # linker
    x1, x2 = w * 0.20 + 15, w * 0.68 - 15
    c.setStrokeColor(NAVY_C); c.setLineWidth(1.2)
    c.line(x1, cy, x1 + 15, cy)
    c.line(x2 - 15, cy, x2, cy)
    label(c, x1 + 26, cy + 3.4, "N", 8.0, NAVY_C, "c", bold=True)
    label(c, x1 + 40, cy + 3.4, "N", 8.0, NAVY_C, "c", bold=True)
    label(c, x1 + 55, cy + 3.4, "NH", 8.0, NAVY_C, "c", bold=True)
    # double bonds
    c.setLineWidth(0.9)
    c.line(x1 + 23, cy + 6.6, x1 + 44, cy + 6.6)
    label(c, x1 + 33.5, cy + 9.5, "=", 7.0, NAVY_C, "c")
    c.line(x1 + 56, cy, x1 + 56 - 0, cy)
    label(c, (x1 + x2) / 2, cy - 34, "Ar\u2014N=N\u2014NH\u2014Ar   (diazoamino / triazene linkage)",
          7.4, NAVY_C, "c", bold=True)



def fig_alkalinity_species(c, w, h):
    """P and T alkalinity composition nomograph."""
    sets = [("hydroxide\nonly", 1, 0, 0, "P = T"),
            ("carbonate\nonly", 0, 1, 0, "P = T/2"),
            ("bicarbonate\nonly", 0, 0, 1, "P = 0"),
            ("hydroxide +\ncarbonate", 0.5, 0.5, 0, "P > T/2"),
            ("carbonate +\nbicarbonate", 0, 0.5, 0.5, "P < T/2")]
    cols = [C("#C0703F"), C("#2E6FA8"), C("#4C7C5A")]
    names = ["OH\u207b", "CO\u2083\u00b2\u207b", "HCO\u2083\u207b"]
    y0 = 40.0
    bh = 47.0
    bw = 30.0
    gap = 13.0
    x0 = 10.0
    total_w = 5 * bw + 4 * gap
    x0 = max(x0, (w - total_w) / 2 - 34)
    for i, (name, a, b, c_, note) in enumerate(sets):
        x = x0 + i * (bw + gap)
        tot = a + b + c_ or 1.0
        yy = y0
        # hydroxide (bottom), carbonate (middle), bicarbonate (top)
        for frac, col in ((a, cols[0]), (b, cols[1]), (c_, cols[2])):
            if frac:
                c.setFillColor(col)
                c.rect(x, yy, bw, bh * frac / tot, stroke=0, fill=1)
                yy += bh * frac / tot
        c.setStrokeColor(C("#5C6B7A")); c.setLineWidth(0.9)
        c.rect(x, y0, bw, bh, stroke=1, fill=0)
        # P level line
        pa = a + b
        if pa > 0:
            yp = y0 + bh * pa / tot
            c.setStrokeColor(C("#A4483B")); c.setLineWidth(0.9); c.setDash(2.2, 1.8)
            c.line(x - 5, yp, x + bw + 5, yp)
            c.setDash()
            label(c, x + bw + 6.5, yp - 2.2, "P", 6.4, C("#A4483B"), "l", bold=True)
        # T label above the bar
        label(c, x + bw / 2, y0 + bh + 4.5, "T", 6.6, NAVY_C, "c", bold=True)
        # species name below
        for j, ln in enumerate(name.split("\n")):
            label(c, x + bw / 2, y0 - 8 - j * 6.6, ln, 5.6, INK_C, "c")
        label(c, x + bw / 2, y0 - 8 - len(name.split("\n")) * 6.6 - 1.5,
              note, 6.2, C("#A4483B"), "c", bold=True)

    # legend to the right
    lx = x0 + total_w + 12
    for j, (nm, cc) in enumerate(zip(names, cols)):
        c.setFillColor(cc)
        c.rect(lx, y0 + bh - 8 - j * 10, 7, 7, stroke=0, fill=1)
        label(c, lx + 10, y0 + bh - 7 - j * 10, nm, 6.4, INK_C, "l")
    label(c, lx, y0 + 12, "P = acid volume to", 5.6, C("#A4483B"), "l")
    label(c, lx, y0 + 6, "phenolphthalein endpt", 5.6, C("#A4483B"), "l")


def fig_ph_meter(c, w, h):
    cx = w * 0.34
    base = 14
    # meter
    c.setFillColor(PALE); c.setStrokeColor(STEEL_C); c.setLineWidth(1.0)
    c.roundRect(cx - 70, base + 24, 60, 48, 3, stroke=1, fill=1)
    c.setFillColor(C("#E8EEF6"))
    c.roundRect(cx - 64, base + 46, 48, 20, 1.5, stroke=0, fill=1)
    label(c, cx - 40, base + 53, "pH 7.42", 9.0, NAVY_C, "c", bold=True)
    label(c, cx - 40, base + 32, "pH meter", 6.2, MUTED_C, "c")
    label(c, cx - 40, base + 27, "(calibrated)", 5.4, MUTED_C, "c")
    # electrode
    ex = cx + 6
    c.setStrokeColor(C("#7C8B9B")); c.setLineWidth(3.0)
    c.line(ex, base + 72, ex, base + 34)
    c.setFillColor(C("#D8E4EF")); c.setStrokeColor(STEEL_C); c.setLineWidth(0.8)
    c.circle(ex, base + 32, 3.4, stroke=1, fill=1)
    label(c, ex + 6, base + 60, "glass electrode", 6.2, NAVY_C, "l", bold=True)
    label(c, ex + 6, base + 53, "(H\u207a-sensitive bulb)", 5.4, MUTED_C, "l")
    c.setStrokeColor(C("#5C6B7A")); c.setLineWidth(1.0)
    c.line(ex, base + 74, cx - 10, base + 74)
    c.line(cx - 10, base + 74, cx - 10, base + 72)
    _beaker(c, ex - 14, base + 6, 34, 26, liq_frac=0.55)
    label(c, ex + 3, base + 3, "sample", 5.6, MUTED_C, "c")



def fig_kinetics_setup(c, w, h):
    base = 14
    cx = w * 0.26
    # water bath with flask
    c.setFillColor(WATER); c.setStrokeColor(STEEL_C); c.setLineWidth(1.0)
    c.roundRect(cx - 40, base + 10, 80, 46, 3, stroke=1, fill=1)
    label(c, cx - 36, base + 12, "constant-temperature bath", 5.8, C("#3B5A72"), "l")
    _conical(c, cx - 17, base + 16, 34, 34, liq_frac=0.45)
    label(c, cx, base + 40, "reaction", 5.4, NAVY_C, "c", bold=True)
    label(c, cx, base + 33.5, "mixture", 5.4, NAVY_C, "c", bold=True)
    # stopwatch
    sx = w * 0.62
    c.setFillColor(C("#FFFFFF")); c.setStrokeColor(STEEL_C); c.setLineWidth(1.0)
    c.roundRect(sx, base + 26, 44, 26, 2, stroke=1, fill=1)
    label(c, sx + 22, base + 34, "00:15:00", 7.2, NAVY_C, "c", bold=True)
    label(c, sx + 22, base + 28, "stopwatch", 5.4, MUTED_C, "c")
    # aliquot arrows
    arrow(c, cx + 20, base + 40, sx - 4, base + 42, C("#8A9AAB"), 0.8, 2.6, dash=(2, 2))
    label(c, (cx + 20 + sx) / 2, base + 45, "5 mL aliquot, quenched in ice", 5.6, MUTED_C, "c")
    # second flask (titration)
    _conical(c, sx + 54, base + 10, 30, 26, liq_frac=0.4, liq=C("#EFD9E2"))
    label(c, sx + 69, base + 20, "titrate", 5.6, NAVY_C, "c", bold=True)
    label(c, sx + 69, base + 14, "NaOH", 5.6, NAVY_C, "c", bold=True)



def fig_volumetric_setup(c, w, h):
    fig_titration_setup(c, w, h, analyte="HCl (unknown)", titrant="NaOH (standard)", probe="burette + indicator")


def _pt(x):
    return x * mm


SCHEMES = {
    "spectro": (74, fig_spectrophotometer),
    "titration": (96, fig_titration_setup),
    "conduct": (96, fig_conductometry),
    "redwood": (112, fig_redwood),
    "pensky": (116, fig_pensky),
    "edta": (72, fig_complexometric),
    "iodometry": (66, fig_iodometry_flow),
    "density": (78, fig_density_bottle),
    "diazo": (86, fig_diazo),
    "alkalinity": (104, fig_alkalinity_species),
    "phmeter": (104, fig_ph_meter),
    "kinetics": (96, fig_kinetics_setup),
    "volumetric": (96, fig_volumetric_setup),
}


SCALES = {"redwood": 1.30, "pensky": 1.30, "diazo": 1.35, "spectro": 1.30,
          "edta": 1.30, "iodometry": 1.30, "alkalinity": 1.15, "phmeter": 1.25,
          "kinetics": 1.25}


def schematic(key, caption):
    h, fn = SCHEMES[key]
    return Fig(h * mm, fn, caption, scale=SCALES.get(key, 1.0))
