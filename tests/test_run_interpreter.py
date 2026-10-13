"""Python solutions must run on the interpreter that runs run.py, not on a
hard-coded `python3` (which doesn't exist on a typical Windows install).

    python -m unittest tests.test_run_interpreter
"""
import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import run


class PythonInterpreterTests(unittest.TestCase):
    def test_python_entry_uses_the_current_interpreter(self):
        tool, compile_cmd, run_cmd = run.LANGUAGES[".py"]
        self.assertEqual(sys.executable, tool)
        self.assertIsNone(compile_cmd)
        self.assertEqual(sys.executable, run_cmd[0])

    def test_python_solution_runs_without_python3_on_path(self):
        with tempfile.TemporaryDirectory() as empty_path, \
                tempfile.TemporaryDirectory() as problem:
            src = Path(problem) / "solution.py"
            src.write_text("print(sum(map(int, input().split())))\n")
            # PATH has no python3 (nor python): only the current interpreter is usable.
            with mock.patch.dict(os.environ, {"PATH": empty_path}):
                failures, _, skipped = run.run_solution(src, [("2 3", "5")], 10)
        self.assertFalse(skipped)
        self.assertEqual([], failures)


if __name__ == "__main__":
    unittest.main()
