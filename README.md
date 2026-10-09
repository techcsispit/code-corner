# code-corner

Small programming problems, each solved in a few different languages, plus a script that checks every solution against test cases.

## Running the checks

```text
python3 run.py                    # every problem
python3 run.py prime              # just one problem
python3 run.py --lang py          # only Python solutions
python3 run.py prime --lang cpp   # one problem, one language
```

It needs Python 3. On Windows the command is `python`. Solutions in languages you don't have installed are skipped.

**Supported languages:** `py`, `js`, `c`, `cpp`, `java`, `go`, `rs`

The runner reports timing for each solution and shows a final summary:

```text
Summary: 12 passed, 0 failed, 3 skipped
```

Codespaces has all languages installed. By default, each solution has a total 10-second budget for compilation and all test cases. Individual problems can override this by adding a `timeout.txt` file with the limit in seconds. When the budget expires, the runner stops the solution and any processes it spawned.

## Layout

```
problems/
  prime/
    README.md       what the program has to do
    cases.txt       one test per line: input | expected output
    solution.cpp
    solution.py
```

Every solution reads its input from stdin and prints the answer. Java files are named `Solution.java` with a `Solution` class.

## Contributing

- Add a solution in a language a problem doesn't have yet (`solution.rs`, `solution.c`, ...).
- Add test cases to a `cases.txt`, especially edge cases the README mentions but the cases don't cover yet.
- Add a new problem: a folder with a `README.md`, a `cases.txt` and at least one solution.
- If a solution gives the wrong answer for an input the README says it should handle, that's a bug. Open an issue with the input, the expected output and what you got, then fix it and add the input to `cases.txt`.

Run `python3 run.py` before opening a pull request. It also runs on every pull request.

Part of Source Start by CSI SPIT. MIT licensed.
