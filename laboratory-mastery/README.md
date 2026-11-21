# Complete Laboratory Mastery

A single-volume laboratory companion covering the twelve exercises in the supplied
practical syllabus: spectrophotometry, acid-catalysed hydrolysis, pH-metric titration,
conductometric titration, volumetric analysis, EDTA hardness, alkalinity of water,
chlorine estimation, Redwood viscometry, flash point by Pensky–Martens, preparation of
diazoaminobenzene, and a closing chapter on interpreting simulated instrument readings.

**Deliverable:** `Complete-Laboratory-Mastery.pdf` — 181 pages, A4.

## Contents

| Part | Pages |
|---|---|
| Front matter — how to use, syllabus inventory, source-gap register, contents | 1–9 |
| Experiments 1–11 (each: aim, theory, apparatus, procedure, observations, precautions, viva, examiner's checklist) | 10–156 |
| Experiment 12 — three mock papers with mark schemes | 157–167 |
| Appendix A — master formula sheet · Appendix B — questions spanning the whole course · Appendix C — source audit | 168–181 |

Every chapter is self-contained: the science is derived rather than asserted, worked
arithmetic is shown step by step, and each chapter ends with a formula sheet and a
symptom → diagnosis table for viva preparation.

Gaps in the source material are documented rather than invented — see Table 0.3 and
Appendix C.

## Rebuilding

```bash
cd src
pip install reportlab pymupdf matplotlib svglib pillow
python3 build.py ../Complete-Laboratory-Mastery.pdf
```

`src/build.py` is the entry point; `MODULES` lists the front matter, twelve chapters
and three appendices. Content lives in `src/content/`, figures in `src/figures.py`,
plots in `src/plots.py`, typography and page furniture in `src/doc.py` / `src/style.py`.
