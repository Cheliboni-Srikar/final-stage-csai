# Presenter Notes

Team DLLM • Complete module • Edition 3.0

Approximately 30 minutes including the suggested thinking time. The separate showcase is under four minutes. Open the PPTX in slideshow mode, use a pen for activities and keep the code output available offline.

## 1 Should Mina trust this recommendation?

Slide 1 | Should Mina trust this recommendation?

Purpose and explanation: Ask for an initial prediction without confirming it yet. A useful program can ask for information instead of returning a room. The module will separate software behaviour from the rules that justify a conclusion. Do not describe the candidate as a confirmed booking.

Timing: approximately 40 seconds including the indicated thinking time.

Activity: Use the worked example; ask learners to predict the next step before explaining.

Debrief: Use the worked explanation above; check that learners can name the relevant input and reason.

Setup and fallback: open the slide locally. Pen and paper are sufficient. Optional code and captured output are in examples/.

Cross references: Guide §§1.2; 2.6; bank MC03; MC18. Tutorial mapping is in the companion coverage map.

Source: CS50 Lecture 0; full URLs on slide 26 and in the guide.

Transition: Continue to What you will be able to do.

## 2 What you will be able to do

Slide 2 | What you will be able to do

Purpose and explanation: No programming or formal logic is required. Route: Software sections 1.1–1.5, then Symbolic AI sections 2.1–2.7. Learners need a pen. Explain that the printed guide adds detail, the bank supplies retrieval practice and the videos demonstrate processes. Keep this roadmap brief.

Timing: approximately 35 seconds including the indicated thinking time.

Activity: Use the worked example; ask learners to predict the next step before explaining.

Debrief: Use the worked explanation above; check that learners can name the relevant input and reason.

Setup and fallback: open the slide locally. Pen and paper are sufficient. Optional code and captured output are in examples/.

Cross references: Guide §§1.1–2.7; bank All. Tutorial mapping is in the companion coverage map.

Source: CS50 Lecture 0; full URLs on slide 26 and in the guide.

Transition: Continue to Software processes information.

## 3 Software processes information

Slide 3 | Software processes information

Purpose and explanation: Hardware is physical. The operating system manages resources. The adviser is application software. A question is a valid output: unknown availability should trigger a request for evidence. Ask learners to classify the keyboard, operating system and adviser. Answers: hardware, system software, application software.

Timing: approximately 60 seconds including the indicated thinking time.

Activity: Use the worked example; ask learners to predict the next step before explaining.

Debrief: Use the worked explanation above; check that learners can name the relevant input and reason.

Setup and fallback: open the slide locally. Pen and paper are sufficient. Optional code and captured output are in examples/.

Cross references: Guide §§1.1–1.2; bank TF01–03; MC01–04. Tutorial mapping is in the companion coverage map.

Source: CS50 Lecture 0; full URLs on slide 26 and in the guide.

Transition: Continue to Algorithm and program.

## 4 Algorithm and program

Slide 4 | Algorithm and program

Purpose and explanation: In this simplified exercise suitability is already given. Trace exactly one branch for each status. The algorithm is the precise procedure; a program implements it in a language. The full expert-system example later checks suitability explicitly. This procedure terminates after one of three responses. Unknown does not fall into the open branch. Transition: specify the desired behaviour before testing it.

Timing: approximately 60 seconds including the indicated thinking time.

Activity: Use the worked example; ask learners to predict the next step before explaining.

Debrief: Use the worked explanation above; check that learners can name the relevant input and reason.

Setup and fallback: open the slide locally. Pen and paper are sufficient. Optional code and captured output are in examples/.

Cross references: Guide §§1.3; bank TF04; MC05; OE01. Tutorial mapping is in the companion coverage map.

Source: CS50 Lecture 0; full URLs on slide 26 and in the guide.

Transition: Continue to Requirements and input validation.

## 5 Requirements and input validation

Slide 5 | Requirements and input validation

Purpose and explanation: A requirement states desired observable behaviour. Validation checks acceptable input under a chosen policy. This model rejects open and closed together. A well-formed open value could still be stale or false in reality. Activity A in the guide asks learners to write a testable closed-room instruction. Explain that validation occurs before inference.

Timing: approximately 90 seconds including the indicated thinking time.

Activity: 30 seconds: rewrite “be helpful” for a closed room.

Debrief: If the room is known closed, do not recommend it and report the closed status.

Setup and fallback: open the slide locally. Pen and paper are sufficient. Optional code and captured output are in examples/.

Cross references: Guide §§1.4; bank TF05–06; MC06; OE01. Tutorial mapping is in the companion coverage map.

Source: CS50 Lecture 0; full URLs on slide 26 and in the guide.

Transition: Continue to A test needs an expected result.

## 6 A test needs an expected result

Slide 6 | A test needs an expected result

Purpose and explanation: Write expectations from requirements before running code. Testing compares observed and expected outcomes; debugging locates and repairs the cause. An open-room case does not check a transition from open to closed. The supplied adviser starts each call from current inputs. Setup: Python 3, no packages; run examples/study_space_adviser.py from source. Offline fallback: observed-output.txt. Point out R4 still fires in the closed case but R5 does not.

Timing: approximately 80 seconds including the indicated thinking time.

Activity: Use the worked example; ask learners to predict the next step before explaining.

Debrief: Use the worked explanation above; check that learners can name the relevant input and reason.

Setup and fallback: open the slide locally. Pen and paper are sufficient. Optional code and captured output are in examples/.

Cross references: Guide §§1.5; bank TF07–08; MC07–08; OE02. Tutorial mapping is in the companion coverage map.

Source: CS50 Lecture 0; full URLs on slide 26 and in the guide.

Transition: Continue to Can a passing test hide a bug?.

## 7 Can a passing test hide a bug?

Slide 7 | Can a passing test hide a bug?

Purpose and explanation: State that inputs are integers for this example. The middle value is allowed by both conditions. Give 40 seconds before moving to the answer slide; do not reveal the zero-seat answer during the prompt. The purpose is to choose a test that distinguishes desired and actual behaviour.

Timing: approximately 65 seconds including the indicated thinking time.

Activity: 40 seconds: choose an input that exposes the bug.

Debrief: Use the worked explanation above; check that learners can name the relevant input and reason.

Setup and fallback: open the slide locally. Pen and paper are sufficient. Optional code and captured output are in examples/.

Cross references: Guide §§1.5; bank TF21–22; MC21–22; OE07. Tutorial mapping is in the companion coverage map.

Source: CS50 Lecture 0; full URLs on slide 26 and in the guide.

Transition: Continue to Test both sides of the boundary.

## 8 Test both sides of the boundary

Slide 8 | Test both sides of the boundary

Purpose and explanation: Explain each expected/actual pair. The first comparison is the defect. Repeat all four tests after repair; this is regression testing. Run examples/boundary_demo.py or show boundary-output.txt. Passing these cases does not prove handling of text, missing input or every future change. Transfer: for a 2–6 range use 1,2,6,7. Video 03 demonstrates this example with progressive highlights.

Timing: approximately 70 seconds including the indicated thinking time.

Activity: Use the worked example; ask learners to predict the next step before explaining.

Debrief: Zero exposes the lower-bound bug. After repair, all four expected results match.

Setup and fallback: open the slide locally. Pen and paper are sufficient. Optional code and captured output are in examples/.

Cross references: Guide §§1.5; bank MC21–22; OE07. Tutorial mapping is in the companion coverage map.

Source: CS50 Lecture 0; full URLs on slide 26 and in the guide.

Transition: Continue to Symbols describe a particular case.

## 9 Symbols describe a particular case

Slide 9 | Symbols describe a particular case

Purpose and explanation: A predicate names a property or relation; arguments have defined roles. Substitute Mina for x, match the input fact, and derive CanReadNotes(Mina). The derived fact was not supplied as input. Swapping argument positions changes the claim. A variable is a placeholder, not a specific person. A knowledge base holds represented facts or general rules according to the architecture.

Timing: approximately 70 seconds including the indicated thinking time.

Activity: Use the worked example; ask learners to predict the next step before explaining.

Debrief: Use the worked explanation above; check that learners can name the relevant input and reason.

Setup and fallback: open the slide locally. Pen and paper are sufficient. Optional code and captured output are in examples/.

Cross references: Guide §§2.1; bank TF09; MC09; OE03. Tutorial mapping is in the companion coverage map.

Source: CS188 Logic/Search; Poole and Mackworth Forward Planning; full URLs on slide 26 and in the guide.

Transition: Continue to How conditions combine.

## 10 How conditions combine

Slide 10 | How conditions combine

Purpose and explanation: Use A=true and B=false: A AND B=false; A OR B=true; NOT A=false. Clarify inclusive OR. Do not treat missing data as a known false value. Our application tracks missing support separately. Formal two-valued truth tables and the application’s incomplete knowledge concern different things.

Timing: approximately 70 seconds including the indicated thinking time.

Activity: 20 seconds: evaluate AND and OR when both inputs are true.

Debrief: Both expressions are true; inclusive OR permits both.

Setup and fallback: open the slide locally. Pen and paper are sufficient. Optional code and captured output are in examples/.

Cross references: Guide §§2.2; bank TF10–11; MC10–11. Tutorial mapping is in the companion coverage map.

Source: CS188 Logic/Search; Poole and Mackworth Forward Planning; full URLs on slide 26 and in the guide.

Transition: Continue to Two reasoning mistakes to avoid.

## 11 Two reasoning mistakes to avoid

Slide 11 | Two reasoning mistakes to avoid

Purpose and explanation: A visitor may have access through another rule. This is why the converse is not entailed. Separately, unknown availability is a lack of knowledge, not an observed closure. Keep these two distinctions clear: rule direction and information completeness. Backward chaining will seek support for a goal, not assume the converse.

Timing: approximately 60 seconds including the indicated thinking time.

Activity: Use the worked example; ask learners to predict the next step before explaining.

Debrief: Use the worked explanation above; check that learners can name the relevant input and reason.

Setup and fallback: open the slide locally. Pen and paper are sufficient. Optional code and captured output are in examples/.

Cross references: Guide §§2.2–2.3; bank TF11; TF14; MC11. Tutorial mapping is in the companion coverage map.

Source: CS188 Logic/Search; Poole and Mackworth Forward Planning; full URLs on slide 26 and in the guide.

Transition: Continue to Forward chaining starts with facts.

## 12 Forward chaining starts with facts

Slide 12 | Forward chaining starts with facts

Purpose and explanation: Define quiet as learner needs quiet, solo as studies alone, open as known-open quiet room. The simplified model assumes this room type is quiet. First match R1 and add suitable. Then match R2 and add recommend. Keep original facts and avoid re-adding a conclusion. Scan until nothing new follows. Rule numbers label rules, not priority. Video 01 03:44 and Video 02 show the same pattern in different domains.

Timing: approximately 85 seconds including the indicated thinking time.

Activity: Use the worked example; ask learners to predict the next step before explaining.

Debrief: Use the worked explanation above; check that learners can name the relevant input and reason.

Setup and fallback: open the slide locally. Pen and paper are sufficient. Optional code and captured output are in examples/.

Cross references: Guide §§2.3; bank TF12; MC12; OE04. Tutorial mapping is in the companion coverage map.

Source: CS188 Logic/Search; Poole and Mackworth Forward Planning; full URLs on slide 26 and in the guide.

Transition: Continue to Backward chaining starts with a goal.

## 13 Backward chaining starts with a goal

Slide 13 | Backward chaining starts with a goal

Purpose and explanation: Work from a goal to candidate rules, then check their premises against evidence. This does not establish the goal automatically. If open is missing, recommend remains unsupported. In larger systems track active goals to avoid cyclic reasoning. The same facts and rules can support the same conclusion through either strategy; the direction of investigation differs.

Timing: approximately 70 seconds including the indicated thinking time.

Activity: Use the worked example; ask learners to predict the next step before explaining.

Debrief: Use the worked explanation above; check that learners can name the relevant input and reason.

Setup and fallback: open the slide locally. Pen and paper are sufficient. Optional code and captured output are in examples/.

Cross references: Guide §§2.3; bank TF13; MC13; OE04. Tutorial mapping is in the companion coverage map.

Source: CS188 Logic/Search; Poole and Mackworth Forward Planning; full URLs on slide 26 and in the guide.

Transition: Continue to Your turn: be the inference engine.

## 14 Your turn: be the inference engine

Slide 14 | Your turn: be the inference engine

Purpose and explanation: All rule information is on screen. Give 60 seconds of quiet work or pair discussion. Ask for new facts in order and missing support, starting every case fresh. Do not read the task list while learners are thinking. Ask for one brief response per case, then use the debrief. No online tool is needed.

Timing: approximately 85 seconds including the indicated thinking time.

Activity: 60 seconds: list new facts and the first missing condition.

Debrief: Use the worked explanation above; check that learners can name the relevant input and reason.

Setup and fallback: open the slide locally. Pen and paper are sufficient. Optional code and captured output are in examples/.

Cross references: Guide §§2.3; bank MC12; OE04. Tutorial mapping is in the companion coverage map.

Source: CS188 Logic/Search; Poole and Mackworth Forward Planning; full URLs on slide 26 and in the guide.

Transition: Continue to Debrief: identify the blocked condition.

## 15 Debrief: identify the blocked condition

Slide 15 | Debrief: identify the blocked condition

Purpose and explanation: Trace A in two steps, B in one and C in zero. Open alone cannot establish suitable. Missing support does not establish the opposite conclusion. Follow with a transfer prompt: ticket AND gate_open implies may_enter. With ticket only, what is missing? Gate_open. The point is to reuse the reasoning pattern beyond room selection.

Timing: approximately 60 seconds including the indicated thinking time.

Activity: Use the worked example; ask learners to predict the next step before explaining.

Debrief: A uses R1 then R2. B stops before R2. C stops before R1.

Setup and fallback: open the slide locally. Pen and paper are sufficient. Optional code and captured output are in examples/.

Cross references: Guide §§2.3; bank TF14; MC12; OE04. Tutorial mapping is in the companion coverage map.

Source: CS188 Logic/Search; Poole and Mackworth Forward Planning; full URLs on slide 26 and in the guide.

Transition: Continue to Search represents possible routes.

## 16 Search represents possible routes

Slide 16 | Search represents possible routes

Purpose and explanation: A state represents a situation; edges represent actions. Show the five directed edges: S→A, S→B, A→G, B→C and C→G. Mark states when enqueued and test the goal on removal. Record a parent on first discovery. A frontier contains states waiting for exploration. Distinguish a graph of possible actions from one chosen route.

Timing: approximately 70 seconds including the indicated thinking time.

Activity: Use the worked example; ask learners to predict the next step before explaining.

Debrief: Use the worked explanation above; check that learners can name the relevant input and reason.

Setup and fallback: open the slide locally. Pen and paper are sufficient. Optional code and captured output are in examples/.

Cross references: Guide §§2.4; bank TF15–16; MC14–15; OE05. Tutorial mapping is in the companion coverage map.

Source: CS188 Logic/Search; Poole and Mackworth Forward Planning; full URLs on slide 26 and in the guide.

Transition: Continue to BFS uses a queue.

## 17 BFS uses a queue

Slide 17 | BFS uses a queue

Purpose and explanation: The first enqueued state is removed first. Parent links yield S→A→G. Removal order S,A,B,G is not a path because no edge connects A to B. Ask learners to point to the path on the previous graph. BFS finds a fewest-edge path under the stated assumptions; with equal action costs it is also least-cost.

Timing: approximately 75 seconds including the indicated thinking time.

Activity: Use the worked example; ask learners to predict the next step before explaining.

Debrief: Visited removal order: S,A,B,G. Returned path: S→A→G.

Setup and fallback: open the slide locally. Pen and paper are sufficient. Optional code and captured output are in examples/.

Cross references: Guide §§2.4; bank MC14; OE05. Tutorial mapping is in the companion coverage map.

Source: CS188 Logic/Search; Poole and Mackworth Forward Planning; full URLs on slide 26 and in the guide.

Transition: Continue to Fewest actions is not always fastest.

## 18 Fewest actions is not always fastest

Slide 18 | Fewest actions is not always fastest

Purpose and explanation: DFS follows a branch deeply and does not generally guarantee a shortest path. Here BFS has two actions and DFS via B has three. Under the alternative travel times the B route is faster: three rather than twenty minutes. The earlier fewest-action result remains true; the equal-cost assumption has changed.

Timing: approximately 75 seconds including the indicated thinking time.

Activity: 20 seconds: which route is faster with these costs?

Debrief: B is faster at 3 minutes, even though it has more actions.

Setup and fallback: open the slide locally. Pen and paper are sufficient. Optional code and captured output are in examples/.

Cross references: Guide §§2.4; bank TF16; MC15; OE05. Tutorial mapping is in the companion coverage map.

Source: CS188 Logic/Search; Poole and Mackworth Forward Planning; full URLs on slide 26 and in the guide.

Transition: Continue to Planning checks each action.

## 19 Planning checks each action

Slide 19 | Planning checks each action

Purpose and explanation: State the effects before the task: Walk adds at_desk and removes at_entrance; Plug adds laptop_plugged. Unchanged facts persist. Learners must test actions in order against the current state. Video 03 animates the state updates.

Timing: approximately 85 seconds including the indicated thinking time.

Activity: 30 seconds: can PLUG run before WALK? Why?

Debrief: No. The initial state lacks at_desk.

Setup and fallback: open the slide locally. Pen and paper are sufficient. Optional code and captured output are in examples/.

Cross references: Guide §§2.5; bank TF17; MC16; OE05; OE08. Tutorial mapping is in the companion coverage map.

Source: CS188 Logic/Search; Poole and Mackworth Forward Planning; full URLs on slide 26 and in the guide.

Transition: Continue to A valid order changes the state.

## 20 A valid order changes the state

Slide 20 | A valid order changes the state

Purpose and explanation: Walk then Plug succeeds with the complete starting state. If socket_working is removed, Walk still succeeds but Plug is blocked. Lack of a working-socket observation is not proof of a broken socket. Ask which action is last supported. Planning is about valid sequences, not just a list of actions associated with a goal.

Timing: approximately 65 seconds including the indicated thinking time.

Activity: Use the worked example; ask learners to predict the next step before explaining.

Debrief: Complete case: WALK then PLUG. Unknown socket case: WALK only.

Setup and fallback: open the slide locally. Pen and paper are sufficient. Optional code and captured output are in examples/.

Cross references: Guide §§2.5; bank TF23; MC23; OE08. Tutorial mapping is in the companion coverage map.

Source: CS188 Logic/Search; Poole and Mackworth Forward Planning; full URLs on slide 26 and in the guide.

Transition: Continue to Parts of an expert system.

## 21 Parts of an expert system

Slide 21 | Parts of an expert system

Purpose and explanation: Relate each component to the running adviser. The interface supplies needs and room information; the engine checks the rules; the trace records supporting inputs and derived facts. Do not imply the rule base automatically learns from examples. In this implementation, general rules are written explicitly.

Timing: approximately 60 seconds including the indicated thinking time.

Activity: Use the worked example; ask learners to predict the next step before explaining.

Debrief: Use the worked explanation above; check that learners can name the relevant input and reason.

Setup and fallback: open the slide locally. Pen and paper are sufficient. Optional code and captured output are in examples/.

Cross references: Guide §§2.6; bank TF19; MC17; OE06. Tutorial mapping is in the companion coverage map.

Source: CS188 Logic/Search; Poole and Mackworth Forward Planning; full URLs on slide 26 and in the guide.

Transition: Continue to Check needs and room properties.

## 22 Check needs and room properties

Slide 22 | Check needs and room properties

Purpose and explanation: Quiet and power refer to Mina’s needs. Open_A, quiet_A and power_A refer to Room A. This removes the earlier assumed quiet-room type. Start with all five inputs: R4 adds needs_quiet_power, then R5 adds recommend_A. A supported candidate is not a reservation. Show the distinction before tracing the code output.

Timing: approximately 80 seconds including the indicated thinking time.

Activity: Use the worked example; ask learners to predict the next step before explaining.

Debrief: Use the worked explanation above; check that learners can name the relevant input and reason.

Setup and fallback: open the slide locally. Pen and paper are sufficient. Optional code and captured output are in examples/.

Cross references: Guide §§2.6; bank TF18; MC18–19; OE06. Tutorial mapping is in the companion coverage map.

Source: CS188 Logic/Search; Poole and Mackworth Forward Planning; full URLs on slide 26 and in the guide.

Transition: Continue to A need is not a room property.

## 23 A need is not a room property

Slide 23 | A need is not a room property

Purpose and explanation: Use a fresh case without quiet_A. Wanting quiet cannot supply the missing room property. Ask whether the room is quiet; do not conclude it is noisy. This is a useful learner task because it exposes a modelling error that simple successful examples can hide.

Timing: approximately 75 seconds including the indicated thinking time.

Activity: 25 seconds: should the system recommend Room A?

Debrief: Not from these rules and facts. Verify quiet_A first.

Setup and fallback: open the slide locally. Pen and paper are sufficient. Optional code and captured output are in examples/.

Cross references: Guide §§2.6; bank TF18; MC18; OE06. Tutorial mapping is in the companion coverage map.

Source: CS188 Logic/Search; Poole and Mackworth Forward Planning; full URLs on slide 26 and in the guide.

Transition: Continue to Explanations still need reliable inputs.

## 24 Explanations still need reliable inputs

Slide 24 | Explanations still need reliable inputs

Purpose and explanation: Positive forward chaining adds consequences; it does not automatically retract an old recommendation. Our program recomputes from supplied current inputs. A trace proves support within the chosen model, not that a room is open now. A learned noise estimator could supply uncertain evidence for explicit rules, but the uncertainty still needs handling.

Timing: approximately 70 seconds including the indicated thinking time.

Activity: Use the worked example; ask learners to predict the next step before explaining.

Debrief: Use the worked explanation above; check that learners can name the relevant input and reason.

Setup and fallback: open the slide locally. Pen and paper are sufficient. Optional code and captured output are in examples/.

Cross references: Guide §§1.5; 2.7; bank TF20; MC24; OE02; OE06. Tutorial mapping is in the companion coverage map.

Source: CS50 Lecture 0; full URLs on slide 26 and in the guide.

Transition: Continue to Return to Mina: what should happen?.

## 25 Return to Mina: what should happen?

Slide 25 | Return to Mina: what should happen?

Purpose and explanation: Pause for a final application answer. R4 can fire, but R5 lacks open_A; ask whether the room is open. Connect all three questions: what is known, which rule applies, which evidence is missing? Next steps: guide Activities B,D,F; bank MC12,MC18,MC21,OE04,OE07; Video 01 essentials, Video 02 transfer, Video 03 testing and planning. Keep answers hidden until learners have attempted the task.

Timing: approximately 85 seconds including the indicated thinking time.

Activity: 30 seconds: give the result and name the blocked condition.

Debrief: Ask whether Room A is open. R5 cannot establish recommend_A without open_A.

Setup and fallback: open the slide locally. Pen and paper are sufficient. Optional code and captured output are in examples/.

Cross references: Guide §§1.5; 2.6–2.7; bank MC18; MC24; OE06. Tutorial mapping is in the companion coverage map.

Source: CS50 Lecture 0; full URLs on slide 26 and in the guide.

Transition: Continue to Practice and sources.

## 26 Practice and sources

Slide 26 | Practice and sources

Purpose and explanation: Sources and optional reading: Harvard CS50x 2025 Lecture 0, https://cs50.harvard.edu/x/2025/notes/0/; UC Berkeley CS188 logic and search, https://inst.eecs.berkeley.edu/~cs188/textbook/logic/forward.html and https://inst.eecs.berkeley.edu/~cs188/textbook/search/uninformed.html; Poole and Mackworth Forward Planning, https://artint.info/html1e/ArtInt_206.html; CLIPS User Guide, https://www.clipsrules.net/documentation/v642/ug642.pdf. The guide contains introductions and offline alternatives. Cases and visuals are DLLM teaching materials prepared with AI assistance. Edition 3.0, 21 November 2026.

Timing: approximately 35 seconds including the indicated thinking time.

Activity: Use the worked example; ask learners to predict the next step before explaining.

Debrief: Use the worked explanation above; check that learners can name the relevant input and reason.

Setup and fallback: open the slide locally. Pen and paper are sufficient. Optional code and captured output are in examples/.

Cross references: Guide §§1.1–2.7; bank Selected above. Tutorial mapping is in the companion coverage map.

Source: CS50 Lecture 0; full URLs on slide 26 and in the guide.

Transition: Finish with a supported conclusion or a precise request for missing evidence.
