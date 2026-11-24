# Proof of Kimberling's replacement-iterate length and position conjectures

**Authors:** Haobo Ma, Wenlin Zhang

We prove Clark Kimberling's length conjecture in OEIS A288476, Comments, revision 2 (June 12, 2017), by replacing its nonoverlapping binary rewriting rule with a three-letter substitution. The iterate lengths satisfy a(n+3)=a(n+2)+4a(n+1)-2a(n), starting with 2,4,8. The same substitution proves existence of the odd and even limiting words and the position conjectures in A288474, A288475, A288552 and A288553. The zero positions divided by their indices tend to the largest root lambda of x^3-x^2-4x+2; the corresponding limit for ones is lambda/(lambda-1). All four stated position bounds hold. For every finite binary seed we also obtain an exact length recurrence; every seed other than the empty word and 0 has the same pair of parity limits, possibly interchanged.

- PDF: [frozen public file](paper.pdf)
- DOI: [https://doi.org/10.5281/zenodo.24486346](https://doi.org/10.5281/zenodo.24486346)
- Concept DOI: [https://doi.org/10.5281/zenodo.24486345](https://doi.org/10.5281/zenodo.24486345)
- License: CC-BY-4.0
- Version: 2
- Mathesis record: [oeis-a288476-replacement-iterate-length](https://mathesis-omega-research.apps.chrono-ai.fun/papers/oeis-a288476-replacement-iterate-length?version=2)

## How to cite

Haobo Ma, Wenlin Zhang (2026). Proof of Kimberling's replacement-iterate length and position conjectures. Mathesis, version 2. https://doi.org/10.5281/zenodo.24486346

## Statement progress

| Statement | Formalization status | Source | Verification basis |
|---|---|---|---|
| Theorem (s1) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/79dfe4f731baccd42dd3c56cf6331a0ddd3cafdb/D5/S1/Words/KimberlingA288476Length.lean) | No public receipt |
| Lemma (s2) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/79dfe4f731baccd42dd3c56cf6331a0ddd3cafdb/D5/S1/Words/KimberlingA288476Length.lean) | No public receipt |
| Corollary (s3) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/79dfe4f731baccd42dd3c56cf6331a0ddd3cafdb/D5/S1/Words/KimberlingA288476Length.lean) | No public receipt |
| Corollary (s4) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/79dfe4f731baccd42dd3c56cf6331a0ddd3cafdb/D5/S1/Words/KimberlingA288476Length.lean) | No public receipt |
| Corollary (s5) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/79dfe4f731baccd42dd3c56cf6331a0ddd3cafdb/D5/S1/Words/KimberlingA288476Length.lean) | No public receipt |

## Contributions

Original authors are listed above. Formalization contributors and attribution are retained in `formalization/nodes.json`; repository pull requests do not confer verification or credit. Submit formalization attempts through the Mathesis attempt path described in [CONTRIBUTING.md](CONTRIBUTING.md).
