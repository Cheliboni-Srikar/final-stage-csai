# Run the examples
Python 3 is optional. No external packages, accounts or internet connection are needed.
From the extracted source directory run:
~~~text
python3 examples/study_space_adviser.py
python3 examples/boundary_demo.py
python3 -m unittest discover -s tests -v
~~~
Windows may use `py -3` in place of `python3`. Do not run from inside examples/. The adviser uses current input facts and rejects conflicting status. These fictional models do not book real rooms. Paper fallback: guide §§1.5 and 2.6, with expected results and explanations. Captured execution is in observed-output.txt and boundary-output.txt.
