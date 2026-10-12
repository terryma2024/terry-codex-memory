from __future__ import annotations

import importlib.util
import json
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SKILL_DIR = Path(__file__).resolve().parents[1]
SCRIPT = SKILL_DIR / "scripts" / "make_vocab_cards.py"


def load_generator_module():
    spec = importlib.util.spec_from_file_location("make_vocab_cards", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError("Unable to load vocabulary-card generator.")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


class UnitCardsCliTest(unittest.TestCase):
    def test_answer_card_uses_answer_instruction(self) -> None:
        """Showing answers must not retain the question-only instruction."""
        generator = load_generator_module()
        self.assertTrue(hasattr(generator, "card_instruction"), "answer instruction helper is missing")
        self.assertEqual(generator.card_instruction(show_answers=True), "参考答案。")

    def test_unit_3q1a_layout_creates_one_page_per_unit(self) -> None:
        """Removing grouped 3q1a support must break the page/output contract."""
        payload = {
            "units": [
                {
                    "title": "Unit 1",
                    "items": [
                        {"zh": "甲", "en": "alpha"},
                        {"zh": "乙", "en": "beta"},
                    ],
                },
                {
                    "title": "Unit 2",
                    "items": [
                        {"zh": "丙", "en": "gamma"},
                    ],
                },
            ]
        }

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            input_path = root / "units.json"
            output_dir = root / "outputs"
            input_path.write_text(json.dumps(payload, ensure_ascii=False), encoding="utf-8")

            result = subprocess.run(
                [
                    sys.executable,
                    str(SCRIPT),
                    "--input",
                    str(input_path),
                    "--out-dir",
                    str(output_dir),
                    "--basename",
                    "sample",
                    "--layout",
                    "unit-3q1a",
                ],
                capture_output=True,
                text=True,
            )

            self.assertEqual(result.returncode, 0, result.stderr)
            output_path = output_dir / "sample_unit_cards_3q1a.pdf"
            self.assertTrue(output_path.is_file())
            page_markers = re.findall(rb"/Type\s*/Page(?!s)", output_path.read_bytes())
            self.assertEqual(len(page_markers), 2)
            self.assertFalse((output_dir / "sample_answer_key.pdf").exists())

    def test_default_layout_keeps_separate_worksheet_and_answer_key(self) -> None:
        payload = [{"zh": "甲", "en": "alpha"}]

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            input_path = root / "items.json"
            output_dir = root / "outputs"
            input_path.write_text(json.dumps(payload, ensure_ascii=False), encoding="utf-8")

            result = subprocess.run(
                [
                    sys.executable,
                    str(SCRIPT),
                    "--input",
                    str(input_path),
                    "--out-dir",
                    str(output_dir),
                    "--basename",
                    "legacy",
                ],
                capture_output=True,
                text=True,
            )

            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertTrue((output_dir / "legacy_cards_4up.pdf").is_file())
            self.assertTrue((output_dir / "legacy_answer_key.pdf").is_file())


if __name__ == "__main__":
    unittest.main()
