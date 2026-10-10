import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import run


class RunnerExitCodeTests(unittest.TestCase):
    def test_nonzero_exit_fails_even_when_output_matches(self):
        with tempfile.TemporaryDirectory() as directory:
            program = Path(directory) / "solution.py"
            program.write_text(
                "import sys\nprint('expected')\nprint('runtime failure', file=sys.stderr)\nsys.exit(1)\n"
            )
            python_language = (sys.executable, None, [sys.executable, "{src}"])
            with patch.dict(run.LANGUAGES, {".py": python_language}):
                failures, _, skipped = run.run_solution(program, [("", "expected")], 10)

        self.assertFalse(skipped)
        self.assertTrue(failures)
        failure = " ".join(failures)
        self.assertIn("status 1", failure)
        self.assertIn("runtime failure", failure)


if __name__ == "__main__":
    unittest.main()
