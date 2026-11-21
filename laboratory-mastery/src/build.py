#!/usr/bin/env python3
"""Build the Complete Laboratory Mastery PDF."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "content"))

from reportlab.lib.units import mm
from reportlab.platypus import NextPageTemplate, PageBreak, Spacer

import style as ST
from style import register_fonts

register_fonts()

import blocks
from blocks import S
from doc import build_doc, MasterTOC, Bookmark, mk
from cover import Cover
from render import chapter
import frontmatter


MODULES = [("ch01_spectro", "CH1"), ("ch02_hydrolysis", "CH2"),
           ("ch03_phmet", "CH3"), ("ch04_conduct", "CH4"),
           ("ch05_volumetric", "CH5"), ("ch06_edta", "CH6"),
           ("ch07_alkalinity", "CH7"), ("ch08_chlorine", "CH8"),
           ("ch09_redwood", "CH9"), ("ch10_flashpoint", "CH10"),
           ("ch11_diazo", "CH11"), ("ch12_simulation", "CH12"),
           ("appendix", "APPENDIX_A"), ("appendix", "APPENDIX_B"),
           ("appendix", "APPENDIX_C")]


def load_chapters(strict=True):
    import importlib
    out = []
    for mod, attr in MODULES:
        try:
            m = importlib.import_module(mod)
        except ModuleNotFoundError:
            if strict:
                raise
            continue
        out.append(getattr(m, attr))
    return out


def build(path, chapters=None):
    doc = build_doc(path)
    story = [Cover(), NextPageTemplate("front"), PageBreak()]
    story += frontmatter.front()
    for ch in (chapters or load_chapters()):
        story += chapter(ch)
    doc.multiBuild(story)
    return doc


if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else "out/master.pdf"
    only = sys.argv[2:] if len(sys.argv) > 2 else None
    chs = load_chapters()
    if only:
        chs = [c for c in chs if c["key"] in only]
    os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
    build(out, chs)
    print("written", out)
