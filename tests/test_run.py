import os
import sys
import tempfile
import time
import unittest
from pathlib import Path
from unittest.mock import patch

import run


class SolutionTimeoutTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory(dir=Path(__file__).parent)
        self.tempdir_patch = patch("run.tempfile.tempdir", self.temp_dir.name)
        self.tempdir_patch.start()

    def tearDown(self):
        self.tempdir_patch.stop()
        self.temp_dir.cleanup()

    def test_timeout_is_shared_across_all_cases(self):
        language = (
            sys.executable,
            None,
            [
                sys.executable,
                "-c",
                "import time; time.sleep(0.15); print('ok')",
            ],
        )

        with tempfile.NamedTemporaryFile(
            suffix=".slow", dir=self.temp_dir.name
        ) as source:
            started = time.perf_counter()
            with patch.dict(run.LANGUAGES, {".slow": language}):
                failures, elapsed, skipped = run.run_solution(
                    Path(source.name), [("input", "ok")] * 3, 0.3
                )
            wall_time = time.perf_counter() - started

        self.assertFalse(skipped)
        self.assertEqual(["took longer than 0.3 seconds"], failures)
        self.assertLess(elapsed, 1.5)
        self.assertLess(wall_time, 1.5)

    def test_compilation_uses_the_same_timeout_budget(self):
        language = (
            sys.executable,
            [sys.executable, "-c", "import time; time.sleep(3)"],
            [sys.executable, "-c", "print('ok')"],
        )

        with tempfile.NamedTemporaryFile(
            suffix=".compile-slow", dir=self.temp_dir.name
        ) as source:
            started = time.perf_counter()
            with patch.dict(run.LANGUAGES, {".compile-slow": language}):
                failures, _, skipped = run.run_solution(
                    Path(source.name), [("input", "ok")], 0.2
                )
            wall_time = time.perf_counter() - started

        self.assertFalse(skipped)
        self.assertEqual(
            ["took longer than 0.2 seconds while compiling"], failures
        )
        self.assertLess(wall_time, 1.5)

    @unittest.skipIf(os.name == "nt", "process-group signals require POSIX")
    def test_timeout_kills_descendant_processes(self):
        marker = Path(self.temp_dir.name) / "descendant-survived"
        child_code = (
            "import time; from pathlib import Path; "
            f"time.sleep(0.5); Path({str(marker)!r}).write_text('alive')"
        )
        parent_code = (
            "import subprocess, sys, time; "
            f"subprocess.Popen([sys.executable, '-c', {child_code!r}]); "
            "time.sleep(5)"
        )

        _, timed_out = run.run_process(
            [sys.executable, "-c", parent_code], timeout=0.2
        )
        time.sleep(0.6)

        self.assertTrue(timed_out)
        self.assertFalse(marker.exists())


if __name__ == "__main__":
    unittest.main()
