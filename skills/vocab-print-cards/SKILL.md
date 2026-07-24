---
name: vocab-print-cards
description: Create printable vocabulary memorization cards, Chinese-to-English fill-in worksheets, and separate answer-key PDFs from English word or phrase lists. Use when the user asks to make 默写卡片, 汉译英填空题, vocabulary cards, answer sheets, one-page A4 4-up repeated worksheets, or to print those vocabulary PDFs.
---

# Vocab Print Cards

## Overview

Use this skill to turn a vocabulary or phrase list into print-ready A4 PDFs:

- a 4-up worksheet page with repeated Chinese-to-English blank cards
- a separate answer-key page
- optional submission to the system printer after validating the PDF

Prefer the bundled script `scripts/make_vocab_cards.py` instead of rewriting ReportLab layout code.

## Workflow

1. Parse the user's list into ordered `(zh, en)` pairs.
   - If the user supplies only English, provide concise learner-friendly Chinese prompts.
   - Preserve the user's English spelling, capitalization, hyphenation, and phrase wording unless there is an obvious typo.
   - For ambiguous phrases, choose the classroom/basic-English meaning and keep Chinese prompts short.
2. Create an input JSON file in the current workspace, usually under `work/`.
3. Run `scripts/make_vocab_cards.py` to generate both worksheet and answer-key PDFs.
4. Render the PDFs with `pdftoppm` when available and inspect the rendered image for clipped text, missing Chinese glyphs, overlap, and page count.
5. Save final PDFs under the user-facing output directory for the current thread.
6. If the user asks to print, query printers with `lpstat -p -d -v`, then submit with `lp`; use escalation when required by the environment.

## Input Format

Use UTF-8 JSON:

```json
[
  {"zh": "打网球", "en": "play tennis"},
  {"zh": "去健身俱乐部", "en": "go to a health club"}
]
```

The script also accepts `{"items": [...]}`.

## Script Usage

```bash
python3 /path/to/vocab-print-cards/scripts/make_vocab_cards.py \
  --input work/items.json \
  --out-dir outputs \
  --basename activity
```

Outputs:

- `<basename>_cards_4up.pdf`
- `<basename>_answer_key.pdf`

Useful options:

- `--worksheet-title "汉译英默写卡"`
- `--answer-title "汉译英默写卡答案"`
- `--subtitle "活动短语"`
- `--printer PRINTER_NAME --print worksheet|answer|both`

## Printing Notes

Only print after the generated PDF has been rendered and visually checked. If no printer is configured, tell the user the PDF path and the printer status. If a default printer exists, use it unless the user specified another printer.

Use one answer-key page for the answers unless the item count requires multiple pages. Do not make the answer key 4-up unless the user asks.
