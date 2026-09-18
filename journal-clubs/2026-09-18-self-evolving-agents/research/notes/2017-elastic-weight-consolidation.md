# Overcoming catastrophic forgetting in neural networks

## Source and reading scope

Key: `2017-elastic-weight-consolidation`. James Kirkpatrick, Razvan Pascanu, Neil Rabinowitz, Joel Veness, Guillaume Desjardins, Andrei A. Rusu, Kieran Milan, John Quan, Tiago Ramalho, Agnieszka Grabska-Barwinska, Demis Hassabis, Claudia Clopath, Dharshan Kumaran, Raia Hadsell. [arXiv v2, 2017-01-25](https://arxiv.org/abs/1612.00796v2); peer-reviewed PNAS article; author preprint read. Read September 18, 2026: §§1–2, equation 3 and setup in §2.1. Full text accessed; review limited to these sections. No original retained: redistribution permission was not established in this pass.

## Mechanism, interpretation and limits

EWC adds a quadratic penalty weighted by a diagonal Fisher estimate. This preserves a preference for parameters important to earlier tasks while allowing adaptation. The approximation and its empirical scope preclude universal retention guarantees. Classification/Atari results are not imported as quantitative agent evidence. Publisher DOI access failed; the versioned author PDF was read. Publication date/venue were checked in publisher search metadata and the arXiv DOI record.

## Use and discussion

Introduction: parameter interference and importance-weighted protection of earlier learning. What protects old behavior when the changing state is a skill library rather than model weights?

[Citation/coverage scope](../thesis-coverage.md#scholarly-foundations-revision--september-18-2026). These targeted foundation readings do not extend the earlier 55-paper citation-network audit.
