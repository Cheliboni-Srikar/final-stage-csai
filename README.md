# Software and Symbolic AI

Team DLLM • Final learning edition 3.0 • Prepared 21 November 2026

## Start here

Open [the study guide](content/study-guide.md). Begin with Chapter 1 §1.2 and predict the output when room availability is unknown. Then attempt Activity A. No programming or formal logic is assumed; a pen is enough.

Read Chapter 1 Software, then Chapter 2 Symbolic AI. Attempt [the question bank](content/practice-bank.md) before opening its solutions. Use [the coverage map](docs/coverage-map.md) to move to slides and video timestamps. The complete original six-topic scope is retained in two chapters.

## Files

- content/ contains the complete guide, module outline and question bank.
- assets/ contains diagram PNG files and editable SVG originals.
- examples/ contains the optional Python adviser, boundary demonstration, instructions and captured outputs.
- tests/ checks the adviser’s behaviour.
- docs/ records mappings, revisions, AI assistance and release checks.

## Separate teaching submissions

The complete editable slide deck is DLLM_Final_Module_Slides.pptx. The separate video assignment contains DLLM_Video01_Software_and_Symbolic_AI.mp4, DLLM_Video02_Facts_Rules_Inference.mp4 and DLLM_Video03_Tests_and_Valid_Plans.mp4, plus DLLM_Stage3_FinalVideoGuide.pdf. Videos are intentionally not stored in this source snapshot. Use the designated class sharing post after access verification.

## Run offline

Python 3 is optional. No packages or accounts are needed. From this directory:
~~~text
python3 examples/study_space_adviser.py
python3 examples/boundary_demo.py
python3 -m unittest discover -s tests -v
~~~
On Windows use `py -3` if `python3` is not recognized. Paper alternatives and answers are in §§1.5 and 2.6. The fictional adviser does not make real bookings.

## Repository and version

Repository: https://github.com/Cheliboni-Srikar/Version-2.0
Earlier remote snapshot verified: 7a72cc6f8f6697b5defc894df46b9133d74ecae4, 3 November 2026. The final submission report records the new snapshot if successfully published. Older packages remain historical; this edition is the intended new learning version.

## Team roster carried forward

| Member | Recorded role | GitHub identity |
|---|---|---|
| 陈奕凯 | CEO and coordination | Not supplied |
| LIM HAO CHEN | CIO and resources | Not supplied |
| CHELIBONI SARASWATHIBAVANI SRIKAR | Content Lead | Repository account Cheliboni-Srikar; individual confirmation needed |
| 乔尔 | Quality Lead | Not supplied |
| 张朝瞳 | Video and visual lead | Not supplied |

Recorded roles do not prove final contributions. Member identity, independent reviews and final scores require team confirmation. Personal logs and student IDs are excluded from public learning source.

## Known limits and checks

This is an introductory positive-rule model, not a full theorem prover. Unknown is not automatically false. Inputs can be stale. The code uses recomputation for changed cases, not automatic truth maintenance. The bank practises this module, not an official exam blueprint. See [release checks](docs/release-checklist.md) for human evidence still required before submission and [AI assistance](docs/ai-use.md) for production disclosure.
