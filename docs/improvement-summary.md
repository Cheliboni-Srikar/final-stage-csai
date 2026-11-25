# Improvements in the final learning edition

Team DLLM • Edition 3.0 • 21 November 2026

## Basis for the revision

The six final assignment briefs, the available Video Tutorials Assessment Rubric, existing DLLM material and the user’s requests informed this revision. No teacher comment, classmate trial result or team approval has been invented. Other rubrics and Shared Assignment Rules still need to be checked by the team when supplied.

## Software testing now includes an observable bug

**Before:** The 3 November guide §1.5 used normal, missing, conflicting and updated room-status cases, but did not demonstrate a numeric boundary defect.

**After:** Guide §1.5 adds a whole-number booking range of 1–4. The buggy condition accepts 0–4. A test at 2 passes; 0 reveals the fault. The final example includes expected and actual outputs, the repair and regression checks. See slides 7–8, MC21–MC22 and OE07; Video 03 demonstrates the sequence.

**Nearby evidence:** Original source excerpt: “A test case pairs inputs with an expected result.” Final worked result: input 0; expected reject; faulty result accept; repaired result reject. The executable output below was captured on 21 November 2026.

~~~text
seats | expected | faulty | repaired
    0 | False    | True   | False
    1 | True     | True   | True
    4 | True     | True   | True
    5 | False    | False  | False
The zero-seat test reveals the bug. All four repaired checks pass.
~~~

**Learning value:** Learners see why one passing test can miss a fault and can design a test that distinguishes two conditions.

## Search and planning have separate explanations

**Before:** The 18-slide Stage 2 deck combined DFS, BFS cost and planning on “Search order and action order.”

**After:** Slides 16–18 explain a graph, queue removals, returned path and unequal costs. Slides 19–20 give action preconditions, add/delete effects and a blocked-action task. TF23, MC23 and OE08 check persistence and missing preconditions.

**Nearby evidence:** Before: “1. Walk / Needs: at_entrance, desk_free / Adds at_desk; removes at_entrance” shared a slide with two search methods. After: “WALK: add at desk; remove at entrance / Socket works remains known / PLUG: add laptop plugged / No socket fact? Stop and check.”

**Learning value:** Learners distinguish exploring alternatives from checking whether each action can execute.

## References now agree across the learning materials

**Before:** The Stage 2 conclusion pointed to “Guide Activities 3–6,” while the revised two-chapter guide used Activities A–F.

**After:** Slide 26 points to Activities B, D and F and precise question IDs. The coverage map aligns all twelve guide sections with questions, slides and videos. Video 01 uses the correct two-chapter section numbers; its original effective instruction is retained.

**Learning value:** A learner who misses MC12 can find §2.3 and a worked rule trace immediately.

## Questions distinguish real misconceptions

**Before:** MC18 distractors included the app name, day of the week and booking receipt.

**After:** MC18 uses quiet, power, quiet_A and open_A. The correct answer remains quiet_A; the other facts are already supplied. The answer explains the difference between learner needs and room properties. The bank now contains 24 true/false, 24 multiple-choice and 8 extended responses, with questions before solutions.

**Learning value:** Wrong answers reveal a concept confusion rather than an implausible guess.

## The inference animation keeps attention on the reasoning

**Before:** Earlier versions used a character-name header and an instant room change. The user requested a clearer topic introduction, consistent narration and visible door crossing.

**After:** The retained refined animation introduces symbolic AI, uses one narration voice and shows Jonathan moving through the doorway. The final export removes the top-left name while retaining the lesson title. Given facts and inferred conclusions remain distinct. No horror storyline or team watermark is added.

**Verification boundary:** These are documented editorial and technical changes. An actual non-author learner trial, a teammate full-video viewing and a representative classroom rehearsal are still required; this document does not claim those took place.
