"""Typography, palette and paragraph styles for the Laboratory Mastery PDF."""
import os
import matplotlib

FONT_DIR = os.path.join(os.path.dirname(matplotlib.__file__), "mpl-data", "fonts", "ttf")

# ---------------------------------------------------------------- palette
NAVY = "#1B3358"        # primary structural colour
NAVY_MID = "#2C5282"
STEEL = "#4A6D8C"
RULE = "#B9C6D4"
INK = "#1A1A1A"
MUTED = "#5A6673"
PALE_NAVY = "#EDF2F8"
PALE_AMBER = "#FBF4E2"
AMBER_EDGE = "#C89B3C"
PALE_GREEN = "#EDF5EF"
GREEN_EDGE = "#4C7C5A"
PALE_RED = "#FAEDEA"
RED_EDGE = "#A4483B"
WHITE = "#FFFFFF"
TABLE_ALT = "#F6F8FB"

FONT_FILES = {
    "Serif": "STIXGeneral.ttf",
    "Serif-Bold": "STIXGeneralBol.ttf",
    "Serif-Italic": "STIXGeneralItalic.ttf",
    "Serif-BoldItalic": "STIXGeneralBolIta.ttf",
    "Sans": "DejaVuSans.ttf",
    "Sans-Bold": "DejaVuSans-Bold.ttf",
    "Mono": "DejaVuSansMono.ttf",
}


def register_fonts():
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont

    for name, fname in FONT_FILES.items():
        pdfmetrics.registerFont(TTFont(name, os.path.join(FONT_DIR, fname)))
    from reportlab.pdfbase.pdfmetrics import registerFontFamily

    registerFontFamily(
        "Serif",
        normal="Serif",
        bold="Serif-Bold",
        italic="Serif-Italic",
        boldItalic="Serif-BoldItalic",
    )


# ---------------------------------------------------------------- geometry (mm)
PAGE = (210, 297)
MARGIN_L = 21
MARGIN_R = 19
MARGIN_T = 23
MARGIN_B = 20
CONTENT_W = PAGE[0] - MARGIN_L - MARGIN_R     # 170 mm


def styles():
    from reportlab.lib.styles import ParagraphStyle
    from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER, TA_LEFT, TA_RIGHT
    from reportlab.lib.units import mm

    S = {}

    S["body"] = ParagraphStyle(
        "body", fontName="Serif", fontSize=9.7, leading=13.6, textColor=INK,
        alignment=TA_JUSTIFY, spaceBefore=0, spaceAfter=5.2,
        firstLineIndent=0, allowWidows=0, allowOrphans=0,
        hyphenationLang="en_GB", embeddedHyphenation=1, uriWasteReduce=0.3,
    )
    S["body_first"] = ParagraphStyle("body_first", parent=S["body"], spaceBefore=2)
    S["lead"] = ParagraphStyle(
        "lead", parent=S["body"], fontSize=10.2, leading=14.6, textColor="#2B3440",
        spaceAfter=7,
    )
    # chapters
    S["h1"] = ParagraphStyle(
        "h1", fontName="Serif-Bold", fontSize=19, leading=22.5, textColor=NAVY,
        spaceBefore=0, spaceAfter=2, alignment=TA_LEFT, keepWithNext=1,
    )
    S["h1kicker"] = ParagraphStyle(
        "h1kicker", fontName="Sans-Bold", fontSize=7.2, leading=9, textColor=STEEL,
        spaceAfter=4, alignment=TA_LEFT, keepWithNext=1,
    )
    S["h2"] = ParagraphStyle(
        "h2", fontName="Serif-Bold", fontSize=12.6, leading=15.2, textColor=NAVY,
        spaceBefore=13, spaceAfter=4.5, alignment=TA_LEFT, keepWithNext=1,
    )
    S["h3"] = ParagraphStyle(
        "h3", fontName="Serif-Bold", fontSize=10.1, leading=12.6, textColor="#2B4A6F",
        spaceBefore=9, spaceAfter=3, alignment=TA_LEFT, keepWithNext=1,
    )
    S["h4"] = ParagraphStyle(
        "h4", fontName="Serif-BoldItalic", fontSize=9.7, leading=12, textColor="#33475E",
        spaceBefore=7, spaceAfter=2, alignment=TA_LEFT, keepWithNext=1,
    )
    # lists
    S["bullet"] = ParagraphStyle(
        "bullet", parent=S["body"], leftIndent=11, bulletIndent=2.5, spaceAfter=3.0,
        bulletFontName="Serif", bulletFontSize=9.7, alignment=TA_JUSTIFY,
    )
    S["num"] = ParagraphStyle(
        "num", parent=S["body"], leftIndent=17, bulletIndent=2.5, spaceAfter=3.4,
        bulletFontName="Serif-Bold", bulletFontSize=9.2, alignment=TA_JUSTIFY,
    )
    # viva
    S["q"] = ParagraphStyle(
        "q", fontName="Serif-Bold", fontSize=9.6, leading=13.2, textColor=NAVY,
        spaceBefore=6.2, spaceAfter=1.4, leftIndent=15, firstLineIndent=-15,
        alignment=TA_LEFT, keepWithNext=1,
    )
    S["a"] = ParagraphStyle(
        "a", fontName="Serif", fontSize=9.6, leading=13.2, textColor=INK,
        spaceBefore=0, spaceAfter=2.4, leftIndent=15, firstLineIndent=0,
        alignment=TA_JUSTIFY,
    )
    S["qsub"] = ParagraphStyle(
        "qsub", fontName="Sans-Bold", fontSize=8.3, leading=11, textColor=STEEL,
        spaceBefore=9, spaceAfter=3, keepWithNext=1,
    )
    # boxes
    S["box"] = ParagraphStyle(
        "box", parent=S["body"], fontSize=9.35, leading=13.0, spaceAfter=3.2,
        alignment=TA_JUSTIFY,
    )
    S["boxtitle"] = ParagraphStyle(
        "boxtitle", fontName="Sans-Bold", fontSize=8.0, leading=10.4, textColor=NAVY,
        spaceAfter=3,
    )
    S["eq"] = ParagraphStyle(
        "eq", fontName="Serif", fontSize=10.4, leading=15, alignment=TA_CENTER,
        spaceBefore=4, spaceAfter=4, textColor="#10233D",
    )
    S["caption"] = ParagraphStyle(
        "caption", fontName="Serif", fontSize=8.4, leading=11.2, textColor="#3C4A5A",
        alignment=TA_CENTER, spaceBefore=4, spaceAfter=9,
    )
    S["tabcap"] = ParagraphStyle(
        "tabcap", fontName="Serif", fontSize=8.4, leading=11.2, textColor="#3C4A5A",
        alignment=TA_LEFT, spaceBefore=2, spaceAfter=4, keepWithNext=1,
    )
    S["th"] = ParagraphStyle(
        "th", fontName="Sans-Bold", fontSize=7.7, leading=9.9, textColor=WHITE,
        alignment=TA_LEFT,
    )
    S["thc"] = ParagraphStyle("thc", parent=S["th"], alignment=TA_CENTER)
    S["td"] = ParagraphStyle(
        "td", fontName="Serif", fontSize=8.4, leading=10.6, textColor=INK,
        alignment=TA_LEFT,
    )
    S["tdc"] = ParagraphStyle("tdc", parent=S["td"], alignment=TA_CENTER)
    S["tdj"] = ParagraphStyle("tdj", parent=S["td"], alignment=TA_JUSTIFY)
    S["toc0"] = ParagraphStyle(
        "toc0", fontName="Serif-Bold", fontSize=9.9, leading=13.2, textColor=NAVY,
        spaceBefore=7.5, leftIndent=0, firstLineIndent=0, rightIndent=26,
    )
    S["toc1"] = ParagraphStyle(
        "toc1", fontName="Serif", fontSize=8.9, leading=12.1, textColor="#26313D",
        leftIndent=13, firstLineIndent=0, rightIndent=26, spaceBefore=1.2,
    )
    S["small"] = ParagraphStyle(
        "small", fontName="Serif", fontSize=8.3, leading=11.3, textColor=MUTED,
        alignment=TA_LEFT, spaceAfter=3,
    )
    S["quote"] = ParagraphStyle(
        "quote", fontName="Serif-Italic", fontSize=9.5, leading=13.2, textColor="#33414F",
        alignment=TA_JUSTIFY, leftIndent=14, rightIndent=8, spaceBefore=3, spaceAfter=6,
    )
    S["cover_title"] = ParagraphStyle(
        "ct", fontName="Serif-Bold", fontSize=33, leading=37, textColor=NAVY,
        alignment=TA_LEFT,
    )
    S["cover_sub"] = ParagraphStyle(
        "cs", fontName="Sans", fontSize=11.5, leading=16, textColor="#3C5470",
        alignment=TA_LEFT,
    )
    S["cover_small"] = ParagraphStyle(
        "csm", fontName="Sans", fontSize=8.3, leading=11.6, textColor=MUTED,
        alignment=TA_LEFT,
    )
    return S
