# Kimberling replacement-iterate lengths and positions

Haobo Ma (ChronoAI Pte Ltd, Singapore); Wenlin Zhang (National University of Singapore; ChronoAI Pte Ltd, Singapore). November 17, 2026. License: CC BY 4.0.

## Results

`note.tex` proves the all-index length recurrence for the nonoverlapping rule `00 -> 0101`, `1 -> 011`, starting at `00`. It also proves the existence of the two parity limits, their zero and one densities, and all position-limit and position-bound conjectures in OEIS A288474, A288475, A288552 and A288553. Positions start at one; iterate numbers start at zero.

The same cubic recurrence holds for the separate zero and one counts. For every finite seed, writing its greedy parsing as `h(t)0^delta` gives the exact length relation `L(n+3)=L(n+2)+4L(n+1)-2L(n)-2delta` and a homogeneous fourth-order recurrence. Every seed other than the empty word and `0` has the same pair of limiting words, with the parity determined by its first code letter. These are proved extensions, not additional conjectures attributed to the OEIS source. A288276, cross-referenced by two entries, concerns rooted maps and is outside these results.

The [pinned Lean source](https://github.com/the-omega-institute/trureturing/blob/79dfe4f731baccd42dd3c56cf6331a0ddd3cafdb/D5/S1/Words/KimberlingA288476Length.lean) contains `D5.S1.Words.KimberlingA288476Length.result`, proving that every original-input iterate length from `00` equals the independently defined integer recurrence. The generating function, parity limits, densities, position inequalities, symbol-count recurrences and arbitrary-seed conclusions have written proofs in the note. `verify.py` supplies supplementary finite integer/rational checks, including all 511 binary seeds of length at most eight; `verify-output.json` states their exact ranges.

## Build

Use Tectonic 0.17.0:

```sh
tectonic note.tex
```

Alternatively, use a standard LaTeX distribution with the listed packages:

```sh
pdflatex -interaction=nonstopmode -halt-on-error note.tex
pdflatex -interaction=nonstopmode -halt-on-error note.tex
```

The bibliography is included in `note.tex`; no BibTeX step or external figure is needed. For the supplementary checks, use Python 3.10 or later, with no third-party packages:

```sh
python3 verify.py > verify-output.json
```

`metadata.json` records the note identity, creators, license, problem identity and mathematical source link. The source archive contains the five source/supporting files named above and `SHA256SUMS`.
