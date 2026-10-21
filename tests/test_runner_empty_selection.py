import io
import sys
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

import run


class RunnerEmptySelectionTests(unittest.TestCase):
    def run_main(self, *args):
        output = io.StringIO()
        with patch.object(sys, "argv", ["run.py", *args]):
            with redirect_stdout(output):
                with self.assertRaises(SystemExit) as exit_context:
                    run.main()
        return exit_context.exception.code, output.getvalue()

    def test_unknown_problem_fails_when_nothing_is_executed(self):
        exit_code, output = self.run_main("does-not-exist")

        self.assertEqual(1, exit_code)
        self.assertIn("Summary: 0 passed, 0 failed, 0 skipped", output)
        self.assertIn("Error: no solutions were executed", output)

    def test_language_without_solutions_fails_when_nothing_is_executed(self):
        exit_code, output = self.run_main("prime", "--lang", "rs")

        self.assertEqual(1, exit_code)
        self.assertIn("Summary: 0 passed, 0 failed, 0 skipped", output)
        self.assertIn("Error: no solutions were executed", output)


if __name__ == "__main__":
    unittest.main()
