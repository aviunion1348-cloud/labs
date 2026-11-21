"""Quantitative graphs (spectra, calibration, titration curves) drawn as vector art."""
import math

from reportlab.lib import colors

from reportlab.lib.units import mm
from figures import Fig, axis, polyline, label, arrow
from style import NAVY, STEEL, INK, MUTED, PALE_AMBER

C = colors.HexColor
NAVY_C, STEEL_C, INK_C, MUTED_C = C(NAVY), C(STEEL), C(INK), C(MUTED)


def _grid(c, X, Y, xticks, yticks, dashed=True):
    c.setLineWidth(0.35)
    c.setStrokeColor(C("#E2E8EF"))
    if dashed:
        c.setDash(1.6, 2.2)
    for t in xticks:
        c.line(X(t), Y(0), X(t), Y(1))
    for t in yticks:
        c.line(X(0), Y(t), X(1), Y(t))
    c.setDash()


# --------------------------------------------------------------- absorbance spectrum
def _spectrum(c, w, h):
    x0, y0 = 46, 38
    gw, gh = w - x0 - 26, h - y0 - 36
    xt = [400, 450, 500, 550, 600, 650, 700]
    yt = [0.0, 0.2, 0.4, 0.6, 0.8]
    X, Y = axis(c, x0, y0, gw, gh, "Wavelength \u03bb (nm)", "Absorbance A",
                xt, yt, 400, 700, 0.0, 0.85, "%.0f", "%.1f")
    _grid(c, X, Y, xt, yt)
    # CoCl2 spectrum: peak 510 nm, shoulder
    xs = list(range(400, 701, 5))
    ys = []
    for xv in xs:
        main = 0.78 * math.exp(-((xv - 511) ** 2) / (2 * 32 ** 2))
        sh = 0.14 * math.exp(-((xv - 615) ** 2) / (2 * 40 ** 2))
        uv = 0.05 * math.exp(-((xv - 400) ** 2) / (2 * 26 ** 2))
        ys.append(main + sh + uv)
    polyline(c, [(X(xv), Y(min(yv, 0.85))) for xv, yv in zip(xs, ys)], NAVY_C, 1.6)
    # lambda max dashed
    c.setStrokeColor(C("#A4483B"))
    c.setLineWidth(0.7)
    c.setDash(2.4, 2)
    c.line(X(511), Y(0), X(511), Y(0.80))
    c.setDash()
    label(c, X(511) + 3, Y(0.76), "\u03bbmax \u2248 511 nm", 6.4, C("#A4483B"), "l", bold=True)
    label(c, X(640), Y(0.30), "secondary band", 6.0, MUTED_C, "c")
    arrow(c, X(633), Y(0.215), X(615), Y(0.155), C("#8A9AAB"), 0.6, 2.4)
    label(c, x0 - 8, Y(0.85) + 6, "CoCl\u2082 spectrum \u2014 locate \u03bbmax before any quantitative work",
          6.8, NAVY_C, "l", bold=True)


# --------------------------------------------------------------- calibration
def _calibration(c, w, h):
    x0, y0 = 52, 40
    gw, gh = w - x0 - 30, h - y0 - 38
    xt = [0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0]
    yt = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
    X, Y = axis(c, x0, y0, gw, gh, "Concentration of CoCl\u2082 (%, w/v)", "Absorbance at \u03bbmax",
                xt, yt, 0, 3.2, 0.0, 1.05, "%.1f", "%.1f")
    _grid(c, X, Y, xt, yt)
    pts = [(0.5, 0.171), (1.0, 0.338), (1.5, 0.503), (2.0, 0.672), (2.5, 0.838), (3.0, 1.001)]
    polyline(c, [(X(0), Y(0.004)), (X(3.0), Y(1.001))], C("#A4483B"), 1.2, dash=(4, 2.4))
    for a, b in pts:
        c.setFillColor(NAVY_C)
        c.circle(X(a), Y(b), 2.3, stroke=0, fill=1)
        c.setStrokeColor(C("#FFFFFF")); c.setLineWidth(0.8)
        c.circle(X(a), Y(b), 2.3, stroke=1, fill=0)
    # unknown
    c.setStrokeColor(C("#4C7C5A")); c.setLineWidth(0.8); c.setDash(2, 2)
    c.line(X(0), Y(0.412), X(1.22), Y(0.412))
    c.line(X(1.22), Y(0.412), X(1.22), Y(0))
    c.setDash()
    c.setFillColor(C("#4C7C5A"))
    c.circle(X(1.22), Y(0.412), 2.6, stroke=0, fill=1)
    label(c, X(1.28), Y(0.412) + 3, "unknown: A = 0.412 \u2192 c \u2248 1.22 %", 6.2, C("#4C7C5A"), "l", bold=True)
    label(c, X(2.35), Y(0.95), "A = 0.332 c + 0.005", 6.4, C("#A4483B"), "c", bold=True)
    label(c, X(2.35), Y(0.90), "(illustrative fit)", 5.4, MUTED_C, "c")
    label(c, X(0.06), Y(0.08), "blank-corrected origin", 5.4, MUTED_C, "l")


# --------------------------------------------------------------- pH curve + derivative
def _ph_curve(c, w, h):
    x0, y0 = 48, 40
    gw, gh = w * 0.46 - x0, h - y0 - 38
    xt = [0, 5, 10, 15, 20, 25]
    yt = [0, 2, 4, 6, 8, 10, 12, 14]
    X, Y = axis(c, x0, y0, gw, gh, "Volume of NaOH added (mL)", "pH", xt, yt, 0, 25, 0, 14)
    _grid(c, X, Y, xt, yt)
    veq = 12.0

    def ph(v):
        n_acid = 0.1 * veq
        n_base = 0.1 * v
        vt = veq + v
        if v < veq - 0.02:
            hplus = (n_acid - n_base) / vt
            return -math.log10(max(hplus, 1e-14))
        if v > veq + 0.02:
            oh = (n_base - n_acid) / vt
            return 14 + math.log10(max(oh, 1e-14))
        return 7.0

    xs = []
    v = 0.0
    while v <= 25.001:
        xs.append((v, ph(v)))
        v += 0.01 if 11.0 < v < 13.0 else 0.05
    polyline(c, [(X(a), Y(b)) for a, b in xs], NAVY_C, 1.7)
    c.setStrokeColor(C("#A4483B")); c.setLineWidth(0.7); c.setDash(2.2, 2)
    c.line(X(12), Y(0), X(12), Y(7))
    c.line(X(0), Y(7), X(12), Y(7))
    c.setDash()
    c.setFillColor(C("#A4483B"))
    c.circle(X(12), Y(7), 2.3, stroke=0, fill=1)
    label(c, X(13.2), Y(4.9), "equivalence:", 6.0, C("#A4483B"), "l", bold=True)
    label(c, X(13.2), Y(3.9), "inflection at pH \u2248 7", 6.0, C("#A4483B"), "l", bold=True)
    label(c, X(1.2), Y(4.3), "excess HCl", 5.8, MUTED_C, "l")
    label(c, X(1.2), Y(3.3), "dominates the pH", 5.8, MUTED_C, "l")
    label(c, X(4.2), Y(12.5), "excess NaOH", 5.8, MUTED_C, "l")
    label(c, X(4.2), Y(11.5), "dominates the pH", 5.8, MUTED_C, "l")
    label(c, X(12.55), Y(6.55), "V eq", 5.8, C("#A4483B"), "l", bold=True)

    # derivative panel
    x1 = w * 0.60
    gw2 = w - x1 - 34
    X2, Y2 = axis(c, x1, y0, gw2, gh, "Average volume (mL)", "\u0394pH/\u0394V", xt,
                  [0.0, 0.5, 1.0], 0, 25, 0, 1.1, "%.0f", "%.1f")
    peak = [(5, 0.10), (8, 0.14), (10, 0.22), (11, 0.42), (11.5, 0.68), (12, 1.0),
            (12.5, 0.66), (13, 0.40), (14, 0.21), (16, 0.13), (20, 0.08), (24, 0.06)]
    polyline(c, [(X2(a), Y2(b)) for a, b in peak], C("#4C7C5A"), 1.6)
    c.setStrokeColor(C("#4C7C5A")); c.setLineWidth(0.7); c.setDash(2.2, 2)
    c.line(X2(12), Y2(0), X2(12), Y2(1.0))
    c.setDash()
    label(c, X2(0.8), Y2(0.95), "maximum \u2192 V eq", 6.0, C("#4C7C5A"), "l", bold=True)
    label(c, x1, y0 + gh + 8, "First-derivative curve", 6.4, C("#4C7C5A"), "l", bold=True)
    label(c, x0, y0 + gh + 8, "Titration curve", 6.4, NAVY_C, "l", bold=True)


# --------------------------------------------------------------- conductometric
def _conduct(c, w, h):
    x0, y0 = 52, 40
    gw, gh = w - x0 - 32, h - y0 - 38
    xt = [0, 2, 4, 6, 8, 10, 12, 14]
    yt = [1, 2, 3, 4, 5, 6]
    X, Y = axis(c, x0, y0, gw, gh, "Volume of NaOH added (mL)", "Conductance G (mS)",
                xt, yt, 0, 14, 1, 6, "%.0f", "%.0f")
    _grid(c, X, Y, xt, yt)
    veq = 8.0
    # before: 5.6 -> 2.55 linear; after: 2.55 -> 5.2
    polyline(c, [(X(0), Y(5.6)), (X(8), Y(2.55))], C("#2E6FA8"), 1.6)
    polyline(c, [(X(8), Y(2.55)), (X(14), Y(5.15))], C("#2E6FA8"), 1.6)
    for a in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]:
        b = 5.6 - (5.6 - 2.55) * a / 8 if a <= 8 else 2.55 + (5.15 - 2.55) * (a - 8) / 6
        c.setFillColor(C("#FFFFFF")); c.setStrokeColor(C("#2E6FA8")); c.setLineWidth(0.9)
        c.circle(X(a), Y(b), 1.8, stroke=1, fill=1)
    c.setFillColor(C("#A4483B"))
    c.circle(X(8), Y(2.55), 2.8, stroke=0, fill=1)
    c.setStrokeColor(C("#A4483B")); c.setLineWidth(0.7); c.setDash(2.2, 2)
    c.line(X(8), Y(2.55), X(8), Y(1))
    c.setDash()
    label(c, X(8) + 4, Y(2.62), "intersection = V eq", 6.2, C("#A4483B"), "l", bold=True)
    label(c, X(0.6), Y(4.55), "H\u207a replaced by Na\u207a", 5.8, C("#2E6FA8"), "l")
    label(c, X(0.6), Y(4.05), "(conductance falls)", 5.8, C("#2E6FA8"), "l")
    label(c, X(9.2), Y(4.75), "excess OH\u207b added", 5.8, C("#2E6FA8"), "l")
    label(c, X(9.2), Y(4.25), "(conductance rises)", 5.8, C("#2E6FA8"), "l")
    label(c, X(8.25), Y(1.28), "V eq", 5.8, C("#A4483B"), "l", bold=True)


# --------------------------------------------------------------- alkalinity bar
def _alkalinity_curve(c, w, h):
    x0, y0 = 52, 40
    gw, gh = w - x0 - 34, h - y0 - 40
    xt = [0, 2, 4, 6, 8, 10, 12]
    yt = [0, 2, 4, 6, 8, 10]
    X, Y = axis(c, x0, y0, gw, gh, "Volume of standard acid added (mL)", "pH of sample",
                xt, yt, 0, 12, 0, 11, "%.0f", "%.0f")
    _grid(c, X, Y, xt, yt)
    xs = [(0, 10.4), (1, 10.1), (2, 9.6), (3, 9.0), (4, 8.35), (5, 7.4),
          (6, 6.2), (7, 5.2), (8, 4.6), (9, 4.05), (10, 3.6), (11, 3.3), (12, 3.1)]
    polyline(c, [(X(a), Y(b)) for a, b in xs], NAVY_C, 1.6)
    c.setStrokeColor(C("#A4483B")); c.setLineWidth(0.7); c.setDash(2.2, 2)
    c.line(X(0), Y(8.3), X(4), Y(8.3)); c.line(X(4), Y(0), X(4), Y(8.3))
    c.setStrokeColor(C("#4C7C5A"))
    c.line(X(0), Y(4.5), X(8), Y(4.5)); c.line(X(8), Y(0), X(8), Y(4.5))
    c.setDash()
    label(c, X(0.2), Y(7.55), "phenolphthalein endpt (pH 8.3): P", 6.0, C("#A4483B"), "l", bold=True)
    label(c, X(3.05), Y(4.75), "methyl-orange endpt (pH 4.5): T", 6.0, C("#4C7C5A"), "l", bold=True)
    label(c, X(6.0), Y(9.55), "carbonate / bicarbonate buffering", 5.6, MUTED_C, "l")
    label(c, X(9.0), Y(2.0), "excess strong acid", 5.6, MUTED_C, "l")
    arrow(c, X(4), Y(1.2), X(8), Y(1.2), C("#8A9AAB"), 0.7, 2.4)
    label(c, X(6), Y(1.45), "HCO\u2083\u207b neutralised", 5.4, MUTED_C, "c")


PLOTS = {
    "spectrum": (74, _spectrum),
    "calibration": (78, _calibration),
    "ph_curve": (74, _ph_curve),
    "conduct": (74, _conduct),
    "alkalinity": (76, _alkalinity_curve),
}


def plot(key, caption):
    h, fn = PLOTS[key]
    return Fig(h * mm, fn, caption)
