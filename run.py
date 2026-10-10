"""Runs every solution against its problem's cases.txt.

    python run.py               # everything
    python run.py prime         # one problem
"""
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path

PROBLEMS = Path(__file__).parent / "problems"

# extension -> (tool that must be installed, compile command or None, run command)
# {src} is the source file, {out} a temp directory for build output.
LANGUAGES = {
    ".py": (sys.executable, None, [sys.executable, "{src}"]),  # the Python running this script
    ".js": ("node", None, ["node", "{src}"]),
    ".c": ("cc", ["cc", "-O2", "-o", "{out}/prog", "{src}"], ["{out}/prog"]),
    ".cpp": ("c++", ["c++", "-std=c++17", "-O2", "-o", "{out}/prog", "{src}"], ["{out}/prog"]),
    ".java": ("javac", ["javac", "-d", "{out}", "{src}"], ["java", "-cp", "{out}", "Solution"]),
    ".go": ("go", ["go", "build", "-o", "{out}/prog", "{src}"], ["{out}/prog"]),
    ".rs": ("rustc", ["rustc", "-O", "-o", "{out}/prog", "{src}"], ["{out}/prog"]),
}

LANGUAGE_EXTENSIONS = {
    "py": ".py",
    "js": ".js",
    "c": ".c",
    "cpp": ".cpp",
    "java": ".java",
    "go": ".go",
    "rs": ".rs",
}


def fill(cmd, src, out):
    return [part.format(src=src, out=out) for part in cmd]


def read_problem_config(problem):
    cases = []
    for line in (problem / "cases.txt").read_text().splitlines():
        if line.strip():
            given, expected = line.rsplit("|", 1)
            cases.append((given.strip(), expected.strip()))

    timeout = 10
    timeout_file = problem / "timeout.txt"

    if timeout_file.exists():
        try:
            value = int(timeout_file.read_text().strip())
            if value > 0:
                timeout = value
        except ValueError:
            pass

    return cases, timeout


def run_solution(src, cases, timeout):
    """Returns failure messages and total execution time."""
    tool, compile_cmd, run_cmd = LANGUAGES[src.suffix]
    if shutil.which(tool) is None:
        print(f"  skip  {src.name} ({tool} isn't installed)")
        return [], 0.0, True
    with tempfile.TemporaryDirectory() as out:
        if compile_cmd:
            result = subprocess.run(
                fill(compile_cmd, src, out),
                capture_output=True,
                text=True
            )
            if result.returncode != 0:
                return [f"didn't compile:\n{result.stderr}"], 0.0, False

        failures = []
        total_time = 0.0

        for given, expected in cases:
            start = time.perf_counter()
            try:
                result = subprocess.run(
                    fill(run_cmd, src, out),
                    input=given + "\n",
                    capture_output=True,
                    text=True,
                    timeout=timeout
                )
                got = result.stdout.strip()
            except subprocess.TimeoutExpired:
                got = f"(took longer than {timeout} seconds)"
            finally:
                total_time += time.perf_counter() - start

            if got != expected:
                failures.append(
                    f"input {given!r}: expected {expected!r}, got {got!r}"
                )

        return failures, total_time, False


def main():
    only = None
    lang = None
    args = sys.argv[1:]

    i = 0
    while i < len(args):
        if args[i] == "--lang":
            if i + 1 >= len(args):
                print("Error: --lang requires a language")
                sys.exit(1)
            lang = args[i + 1].lower()
            i += 2
        elif only is None:
            only = args[i]
            i += 1
        else:
            print(f"Error: unexpected argument {args[i]!r}")
            sys.exit(1)

    if lang is not None and lang not in LANGUAGE_EXTENSIONS:
        available = ", ".join(LANGUAGE_EXTENSIONS)
        print(f"Error: unknown language {lang!r}. Available: {available}")
        sys.exit(1)
    passed = 0
    failed = 0
    skipped = 0
    for problem in sorted(PROBLEMS.iterdir()):
        if only and problem.name != only:
            continue
        print(problem.name)
        cases, timeout = read_problem_config(problem)
        for src in sorted(problem.iterdir()):
            if src.suffix not in LANGUAGES:
                continue
            if lang is not None and src.suffix != LANGUAGE_EXTENSIONS[lang]:
                continue

            failures, total_time, was_skipped = run_solution(src, cases, timeout)
            if was_skipped:
                skipped += 1
            elif failures:
                failed += 1
                print(f"  FAIL  {src.name} ({total_time:.3f}s)")
                for f in failures:
                    print(f"        {f}")
            else:
                passed += 1
                print(f"  ok    {src.name} ({total_time:.3f}s)")
    print(f"\nSummary: {passed} passed, {failed} failed, {skipped} skipped")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
