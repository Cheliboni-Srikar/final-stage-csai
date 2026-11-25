# Software and Symbolic AI Test Bank

Team DLLM • Final learning edition 3.0 • 21 November 2026

## Instructions

24 true/false, 24 single-answer multiple-choice and 8 extended-response questions. Attempt all questions before checking the key. Section numbers match the two-chapter guide. Use a separate sheet for answers. These questions practise the module; they are not an official examination paper.

Start with TF01–TF08 and MC01–MC08 for Software; then work through Symbolic AI. TF21–TF22, MC21–MC22 and OE07 revisit boundary testing. TF23–TF24, MC23–MC24 and OE08 extend reasoning and planning.

For each extended response, write approximately 100 words or more, or an equivalent labelled trace, algorithm, diagram or test table. Explain why steps are justified. Questions come first; all solutions and marking guidance follow.

## Coverage

Software: 10 true/false, 10 multiple-choice, 3 extended responses. Symbolic AI: 14 true/false, 14 multiple-choice, 5 extended responses. All twelve numbered guide sections are represented.

<!--page-->

## True or false 1 to 8

Mark T or F and correct false statements.

**TF01 · §1.1** A phone screen is hardware.

**TF02 · §1.1** A room-booking application is system software.

**TF03 · §1.2** An output can be a question asking for missing information.

**TF04 · §1.3** An algorithm must be written in Python.

**TF05 · §1.4** “Ask for availability when status is unknown” is a testable requirement.

**TF06 · §1.4** Passing input validation proves the room is really open.

**TF07 · §1.5** Write an expected output before running the test.

**TF08 · §1.5** One successful open-room test proves that the program handles a change to closed.

<!--page-->

## True or false 9 to 16

Mark T or F and correct false statements.

**TF09 · §2.1** Enrolled(AI101, Mina) means the same thing as Enrolled(Mina, AI101).

**TF10 · §2.2** Inclusive OR is true when both inputs are true.

**TF11 · §2.2** From IF A THEN B and B alone, A must follow.

**TF12 · §2.3** Forward chaining starts with facts.

**TF13 · §2.3** Backward chaining treats the requested goal as already proved.

**TF14 · §2.3** In Mina’s adviser, missing open establishes closed.

**TF15 · §2.4** The order in which BFS removes states is always a path.

**TF16 · §2.4** With equal action costs, BFS can find a least-cost path by finding a fewest-action path.

<!--page-->

## True or false 17 to 24

Mark T or F and correct false statements.

**TF17 · §2.5** An action needs all its preconditions before it can run in our model.

**TF18 · §2.6** A learner wanting quiet establishes that Room A is quiet.

**TF19 · §2.6** The inference engine applies rules to the current case facts.

**TF20 · §2.7** A correct rule trace can use an outdated room fact.

**TF21 · §1.5** For a whole-number range 1 to 4 inclusive, testing only 2 seats can miss a condition that incorrectly allows 0.

**TF22 · §1.5** Debugging means changing the expected output until a failing test passes.

**TF23 · §2.5** After Walk adds at_desk and removes at_entrance, a socket_working fact remains unless an action changes it.

**TF24 · §2.3** R2 has higher priority than R1 simply because its label contains a larger number.

<!--page-->

## Multiple choice 1 to 4

Choose one answer.

**MC01 · §1.1** Which item is application software?

A. Physical display

B. Room-booking app

C. Operating system

D. Processor

**MC02 · §1.1** What is the operating system’s role here?

A. Manage one application’s room rules

B. Choose which room meets a learner’s needs

C. Manage hardware resources for programs

D. Store only the current case facts

**MC03 · §1.2** Mina enters “I need quiet.” What role does this statement play?

A. Input

B. Processing

C. Output

D. Test result

**MC04 · §1.2** Which is processing?

A. Mina types a room name

B. The screen displays a question

C. The room status is supplied

D. The program compares the facts with its rules

<!--page-->

## Multiple choice 5 to 8

Choose one answer.

**MC05 · §1.3** A written sequence of steps that has not been coded is best described as what?

A. Test case

B. Algorithm

C. Input fact

D. Execution trace

**MC06 · §1.4** Which requirement can you test directly?

A. Return a useful answer for every learner

B. Handle room status correctly

C. Ask for status if availability is unknown

D. Avoid confusing messages

**MC07 · §1.5** Today Room A is closed. Yesterday it was recommended. What should happen?

A. Keep yesterday’s result

B. Add a second recommendation

C. Ignore the new fact

D. Recompute from today’s facts

**MC08 · §1.5** Which action is a regression test?

A. Rerun a saved missing-status test after editing the code

B. Change the expected result to match a failure

C. Check only the new successful case

D. Delete old tests after the fix

<!--page-->

## Multiple choice 9 to 12

Choose one answer.

**MC09 · §2.1** Given Enrolled(person, course), what does Enrolled(Mina, AI101) mean?

A. AI101 teaches Mina

B. Mina is enrolled in AI101

C. Mina teaches AI101

D. Mina is a room

**MC10 · §2.2** If A is true and B is false, what are A AND B and A OR B?

A. True, true

B. True, false

C. False, true

D. False, false

**MC11 · §2.2** IF student THEN library access. You know that Lee has library access. Which answer is justified?

A. Lee is definitely a student

B. Lee is definitely not a student

C. No students have access

D. The rule alone does not establish whether Lee is a student

**MC12 · §2.3** R1: quiet AND solo → suitable. R2: suitable AND open → recommend. With only quiet and solo, what is new?

A. Suitable only

B. Recommend only

C. Closed

D. Suitable and recommend

<!--page-->

## Multiple choice 13 to 16

Choose one answer.

**MC13 · §2.3** R2 is suitable AND open → recommend. To prove recommend, what does backward chaining seek first?

A. Quiet and solo immediately, ignoring open

B. Suitable and open

C. Recommend and closed

D. Recommend alone

**MC14 · §2.4** Edges: S→A, S→B, A→G, B→C, C→G. BFS explores A before B and tests the goal on removal. What path is returned?

A. S→A→B→G

B. S→G

C. S→A→G

D. S→B→G

**MC15 · §2.4** Edges: S→A, S→B, A→G, B→C, C→G. What path can DFS find if it follows B first?

A. S→G

B. S→B→G

C. S→A→C→G

D. S→B→C→G

**MC16 · §2.5** Plug requires at desk and socket working. At the entrance, with a working socket, what is missing?

A. At desk

B. Socket working

C. At entrance

D. Laptop plugged

<!--page-->

## Multiple choice 17 to 20

Choose one answer.

**MC17 · §2.6** Where does a rule-based adviser keep current case facts?

A. Knowledge base of general rules

B. Working memory

C. Inference engine

D. User interface

**MC18 · §2.6** R5 requires needs_quiet_power, open_A, quiet_A and power_A. Which missing fact blocks R5 even when Mina needs quiet and power and the room is open and powered?

A. quiet

B. power

C. quiet_A

D. open_A

**MC19 · §2.6** Under our validation policy, what happens if open_A and closed_A are both supplied?

A. Prefer the first fact

B. Recommend anyway

C. Combine both into open

D. Reject the inconsistent case

**MC20 · §2.7** Which design combines learned and symbolic methods?

A. Estimate noise from data, then apply explicit room rules

B. Treat every estimate as certainly true

C. Remove all checks

D. Use only the room number

<!--page-->

## Multiple choice 21 to 24

Choose one answer.

**MC21 · §1.5** The required integer range is 1–4 inclusive, but the code accepts 0–4. Which input directly exposes this lower-bound bug?

A. 0

B. 1

C. 2

D. 4

**MC22 · §1.5** A form changes its accepted integer range to 2–6. Which set tests just outside and at both boundaries?

A. 2,3,4,5

B. 1,2,6,7

C. 0,3,4,8

D. 2,4,6,6

**MC23 · §2.5** Start: at_entrance, desk_free, socket_working. Walk adds at_desk and removes at_entrance. Which state follows?

A. at_entrance, at_desk, desk_free, socket_working

B. at_desk only

C. at_desk, desk_free, socket_working

D. laptop_plugged, desk_free, socket_working

**MC24 · §2.7** An inference trace is correct, but the supplied open_A observation is from yesterday. What is the best next step?

A. Accept the old observation because the rules are correct

B. Reverse R5 to prove open_A

C. Treat missing current data as closed_A

D. Verify current availability and recompute

<!--page-->

## Extended response 1 to 2

**OE01 · §1.2–1.4** Design an adviser for one room that already meets Mina’s needs. Give an input, a processing step and an output. Write the unknown-status requirement. Test it with two inputs.

**OE02 · §1.4–1.5** An app still displays yesterday’s recommendation after Room A closes. Give a normal test, an update test and a conflict test. How would you check a later fix?

<!--page-->

## Extended response 3 to 4

**OE03 · §2.1–2.2** Use Enrolled(person, course), the fact Enrolled(Mina, AI101), and IF Enrolled(x, AI101) THEN CanReadNotes(x). Show the substitution and inference. Can access alone prove enrolment?

**OE04 · §2.3** Use R1: quiet AND solo → suitable and R2: suitable AND open → recommend. Trace the full case forward and backward. Then remove open and start again.

<!--page-->

## Extended response 5 to 6

**OE05 · §2.4–2.5** Use S→A, S→B, A→G, B→C, C→G, equal costs. Trace BFS with A first, marking on enqueue and checking goals on removal. Compare DFS with B first. Then explain why Plug cannot run before Walk if Plug needs at desk.

**OE06 · §2.6–2.7** R4: quiet AND power → needs_quiet_power. R5: needs_quiet_power AND open_A AND quiet_A AND power_A → recommend_A. Trace all five inputs, then remove quiet_A. Name the system components and one limit of the trace.

<!--page-->

## Extended response 7 to 8

**OE07 · §1.5** A form should accept whole-number seat requests from 1 to 4 inclusive. Its condition is 0 ≤ seats ≤ 4. Explain why a test at 2 passes, give four boundary tests with expected and actual results, identify the repair, and describe regression testing.

**OE08 · §2.5–2.7** Start at the entrance with desk_free, but socket status unknown. Walk requires at_entrance and desk_free, adds at_desk and removes at_entrance. Plug needs at_desk and socket_working, and adds laptop_plugged. Trace Walk then Plug, identify missing information, and explain why the goal cannot be assumed.

<!--page-->

## Answer key True or false 1 to 8

**TF01 · True** It is a physical component.

**TF02 · False** It is application software: it performs a task for a user.

**TF03 · True** The system can ask for availability instead of naming a room.

**TF04 · False** It is a plan of steps and can be described in pseudocode or plain language.

**TF05 · True** It specifies both an input condition and an observable response.

**TF06 · False** An acceptable input can still be inaccurate or outdated.

**TF07 · True** An independent expectation can reveal a wrong actual result.

**TF08 · False** A changed input needs a separate update test.

<!--page-->

## Answer key True or false 9 to 16

**TF09 · False** The first position refers to a person and the second to a course.

**TF10 · True** It needs at least one true input and allows both.

**TF11 · False** The rule gives a sufficient condition for B; another condition might also produce B.

**TF12 · True** It applies rules whose conditions are supported and adds new facts.

**TF13 · False** It searches for rules and facts that would support that goal.

**TF14 · False** Missing status leaves availability unknown.

**TF15 · False** Successively removed states may lie on different branches.

**TF16 · True** Each depth adds the same cost per action.

<!--page-->

## Answer key True or false 17 to 24

**TF17 · True** A missing condition blocks that action.

**TF18 · False** A need and a room property describe different things.

**TF19 · True** Working memory holds the case; the engine carries out the reasoning.

**TF20 · True** Logical support does not verify the accuracy or freshness of an input.

**TF21 · True** The middle value does not distinguish the buggy lower bound from the correct one.

**TF22 · False** Debugging locates and repairs the program fault; the expectation must follow the requirement.

**TF23 · True** Unchanged facts persist in this planning model.

**TF24 · False** Rule labels identify rules; they do not specify a priority.

<!--page-->

## Answer key Multiple choice 1 to 8

**MC01 · B** The booking app performs a task for a user. The display and processor are hardware; the operating system supports applications.

**MC02 · C** It manages resources such as memory and devices for programs. Choosing a room or managing room rules belongs to the adviser; working memory holds case facts.

**MC03 · A** The adviser receives it before applying its rules.

**MC04 · D** Processing is the operation that transforms the supplied information into a response.

**MC05 · B** A program is an implementation; an algorithm can exist before implementation. A test case checks a behaviour; an input is supplied data; a trace records reasoning.

**MC06 · C** It identifies a specific input and a visible response. The other statements lack a specific observable condition and response.

**MC07 · D** The old result must disappear when it has lost its support.

**MC08 · A** A saved case can reveal a fault that returns after a change.

<!--page-->

## Answer key Multiple choice 9 to 16

**MC09 · B** The person is the first argument and the course is the second.

**MC10 · C** AND needs both; inclusive OR needs only one.

**MC11 · D** Knowing the conclusion does not prove that particular premise.

**MC12 · A** R1 fires, but R2 still lacks open.

**MC13 · B** It turns the two conditions of R2 into subgoals. Suitable and open are the direct conditions; suitable can then be supported by R1.

**MC14 · C** G is first discovered from A; parent links give S→A→G.

**MC15 · D** DFS can follow the deeper B branch before returning to consider A.

**MC16 · A** Both preconditions must hold; the person has not reached the desk.

<!--page-->

## Answer key Multiple choice 17 to 24

**MC17 · B** Working memory records the case being processed.

**MC18 · C** The room itself must be known quiet. A learner’s wish cannot supply that fact. The other options are already supplied; none establishes the room’s quietness.

**MC19 · D** A single room cannot have both statuses in this model.

**MC20 · A** A learned estimate may inform a rule; uncertainty still matters.

**MC21 · A** Zero must be rejected by the requirement but is accepted by the faulty condition.

**MC22 · B** One and seven are just outside; two and six are the endpoints.

**MC23 · C** Only the stated add/delete effects change; the socket and desk facts persist.

**MC24 · D** Correct reasoning cannot establish that an input observation is current.

<!--page-->

## Worked response OE01

1. Input: current availability. The suitability of the room is given in this exercise.
2. Processing: compare the supplied status with the known-open, closed and unknown branches. Output either a candidate or an informative message.
3. Requirement: when availability is unknown, ask for the status before recommending.
4. Test one: known open → offer the room. Test two: unknown → ask if the room is open and do not offer it yet.
5. These expectations come from the requirement. Writing the steps gives an algorithm; implementing them in a language gives a program.

**Marking guidance:** Credit a coherent input/process/output, an observable requirement, and both input–expected result pairs.

**Study check:** Compare your explanation with §1.2–1.4. A different example or wording earns credit when its assumptions and reasoning are valid.

<!--page-->

## Worked response OE02

1. Normal: begin with a suitable room known open. Expect a candidate. This establishes the starting state for the update test.
2. Update: replace open with closed, keeping other facts unchanged. Expect the old recommendation to disappear. If it remains, record the actual result as a failure.
3. Conflict: submit open and closed together. Under our policy, expect rejection before reasoning. This is different from a valid change over time.
4. Repair the update logic. Repeat the saved update test and normal test; repeating earlier checks after a change is regression testing.

**Marking guidance:** Credit expected outcomes for three distinct inputs and a concrete regression check.

**Study check:** Compare your explanation with §1.4–1.5. A different example or wording earns credit when its assumptions and reasoning are valid.

<!--page-->

## Worked response OE03

1. The first argument identifies a person; the second identifies a course. Swapping them would change the claim.
2. Substitute Mina for x. The condition becomes Enrolled(Mina, AI101), exactly the given fact.
3. Apply the rule in its stated direction. Add CanReadNotes(Mina).
4. Now suppose only CanReadNotes(Mina) is given. Enrolment does not follow: a guest-access rule could also grant access. Equally, the absence of an enrolment fact does not by itself establish that Mina is not enrolled.

**Marking guidance:** Credit role meanings, substitution, derived fact and a justified rejection of the converse.

**Study check:** Compare your explanation with §2.1–2.2. A different example or wording earns credit when its assumptions and reasoning are valid.

<!--page-->

## Worked response OE04

1. Forward: start with quiet, solo and open. R1 adds suitable. R2 now has suitable and open and adds recommend. A fresh scan adds nothing new.
2. Backward: start with goal recommend. R2 needs suitable and open. R1 supports suitable from quiet and solo. Open is an input, so both R2 conditions are supported.
3. Remove open and reset derived facts. R1 still adds suitable. R2 lacks open, so recommend is unsupported. Ask whether the room is open. Do not infer closed or keep the old recommendation.

**Marking guidance:** Credit both reasoning directions, the missing condition, and the response for an unknown status.

**Study check:** Compare your explanation with §2.3. A different example or wording earns credit when its assumptions and reasoning are valid.

<!--page-->

## Worked response OE05

1. Start queue [S]. Remove S → [A,B]. Remove A → [B,G]. Remove B → [G,C]. Remove G and stop.
2. Removal order is S,A,B,G. G was first queued from A, which was queued from S. Returned path: S,A,G. No edge joins A to B.
3. DFS choosing B first can return S,B,C,G. That uses three actions rather than two. Under equal costs the two-action BFS route is also least-cost.
4. A plan checks action preconditions. At the entrance, at desk is missing. Walk can establish it; Plug still needs a working socket after the walk.

**Marking guidance:** Credit queue trace, reconstructed path, valid DFS comparison and a precondition check.

**Study check:** Compare your explanation with §2.4–2.5. A different example or wording earns credit when its assumptions and reasoning are valid.

<!--page-->

## Worked response OE06

1. Knowledge base: R4 and R5. Working memory: quiet, power, open_A, quiet_A and power_A. Interface: collects the facts and displays the result.
2. The inference engine applies R4 and adds needs_quiet_power; then R5 adds recommend_A.
3. Start a new case without quiet_A. R4 still fires from the learner needs. R5 now lacks a room property, so Room A is not supported. Ask about its quietness; missing quiet_A does not establish that the room is noisy.
4. The trace explains the model’s answer. It cannot confirm whether an open_A record is current or reserve the room.

**Marking guidance:** Credit the roles, two rule traces, the learner/room distinction and one real limitation.

**Study check:** Compare your explanation with §2.6–2.7. A different example or wording earns credit when its assumptions and reasoning are valid.

<!--page-->

## Worked response OE07

A middle test at 2 passes because both the required range and the faulty condition include 2. It therefore cannot distinguish the two behaviours. Test 0: expected reject, actual accept; this exposes the bug. Test 1: expected accept, actual accept. Test 4: expected accept, actual accept. Test 5: expected reject, actual reject. The lower comparison must be changed to 1 ≤ seats while keeping the upper comparison seats ≤ 4. After changing the code, repeat all four tests, including the previously successful cases. This is regression testing. It checks the repair and guards against a new failure at another boundary. These observations support only the tested behaviour; separate input-format tests are still needed for text or missing values.

**Marking guidance:** 10 points: reason middle passes 2; four expected/actual pairs 4; correct repair 2; regression purpose and limitation 2.

**Study check:** Compare your explanation with §1.5. A different example or wording earns credit when its assumptions and reasoning are valid.

<!--page-->

## Worked response OE08

The initial state contains at_entrance and desk_free. Walk is permitted because both of its preconditions hold. Its effect adds at_desk and removes at_entrance. Desk_free stays in the state because no action changes it. Plug is now considered. At_desk is available, but socket_working is not established. Therefore Plug cannot run in this model and laptop_plugged has not been achieved. The useful next step is to check whether the socket works. Unknown status is not proof that it is broken. If a reliable observation establishes socket_working, Plug can then run and add laptop_plugged. Merely wanting the goal does not supply missing preconditions. A valid plan needs each action to be supported in the state where it executes.

**Marking guidance:** 10 points: Walk conditions 2; add/delete and persistence 3; blocked Plug 2; unknown distinction 1; next action and goal reasoning 2.

**Study check:** Compare your explanation with §2.5–2.7. A different example or wording earns credit when its assumptions and reasoning are valid.
