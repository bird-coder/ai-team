"""Exercise the real launcher with a fake Codex executable; no network/model calls."""
import json
import os
from pathlib import Path
import shlex
import shutil
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]


class StartTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix="ai-team-start-test-")
        self.addCleanup(self.tmp.cleanup)
        self.base = Path(self.tmp.name).resolve()
        self.team = self.base / "team with spaces"
        (self.team / "scripts").mkdir(parents=True)
        self.start = self.team / "scripts/start"
        shutil.copy2(ROOT / "scripts/start", self.start)
        self.project = self.base / "project with spaces"
        self.project.mkdir()
        self.bin = self.base / "bin"
        self.bin.mkdir()
        self.capture = self.base / "invocation.json"
        fake = self.bin / "codex"
        fake.write_text(
            "#!/bin/bash\nexec " + shlex.quote(sys.executable)
            + " -c 'import json, os, pathlib, sys; "
            + "pathlib.Path(os.environ[\"AI_TEAM_CAPTURE\"]).write_text("
            + "json.dumps([os.environ.get(\"CODEX_HOME\"), sys.argv[1:]]))' \"$@\"\n"
        )
        fake.chmod(0o755)
        self.env = dict(os.environ, PATH=str(self.bin) + os.pathsep + os.environ['PATH'],
                        AI_TEAM_CAPTURE=str(self.capture))

    def run_start(self, *args):
        return subprocess.run(['bash', str(self.start), *map(str, args)],
                              env=self.env, capture_output=True, text=True)

    def test_project_and_prompt_are_forwarded_exactly(self):
        prompt = 'workflow: development\nquotes " and literal $(touch should-not-exist)'
        result = self.run_start(self.project, prompt)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(self.capture.read_text()),
                         [str(self.team), ['--strict-config', '--cd', str(self.project), '--', prompt]])

    def test_project_without_prompt(self):
        result = self.run_start(self.project)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(self.capture.read_text()),
                         [str(self.team), ['--strict-config', '--cd', str(self.project)]])

    def test_forbidden_roots_never_launch_codex(self):
        for target in [self.team, self.team / 'scripts', self.base]:
            with self.subTest(target=target):
                self.assertEqual(self.run_start(target).returncode, 2)
                self.assertFalse(self.capture.exists())

    def test_symlink_cannot_bypass_team_boundary(self):
        link = self.base / 'team-alias'
        link.symlink_to(self.team, target_is_directory=True)
        self.assertEqual(self.run_start(link).returncode, 2)
        self.assertFalse(self.capture.exists())

    def test_similar_prefix_is_not_a_child(self):
        sibling = self.base / 'team with spaces-other'
        sibling.mkdir()
        self.assertEqual(self.run_start(sibling).returncode, 0)

    def test_invalid_arguments_never_launch_codex(self):
        for args in [(), (self.project, 'prompt', 'extra'), (self.base / 'missing',)]:
            with self.subTest(args=args):
                self.assertNotEqual(self.run_start(*args).returncode, 0)
                self.assertFalse(self.capture.exists())


class ConfigurationTests(unittest.TestCase):
    def test_role_files_parse_and_have_instructions(self):
        try:
            import tomllib
        except ImportError:
            self.skipTest('TOML validation requires Python 3.11+')
        tomllib.loads((ROOT / 'config.toml').read_text())
        for path in (ROOT / 'agents').glob('*.toml'):
            with self.subTest(role=path.stem):
                role = tomllib.loads(path.read_text())
                self.assertEqual(role['name'], path.stem)
                self.assertTrue(role['model'])
                self.assertTrue(role['developer_instructions'].strip())


if __name__ == '__main__':
    unittest.main()
