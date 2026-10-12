---
name: vocab-print-cards
description: Use when the user asks to make or print 默写卡片, 汉译英填空题, vocabulary cards, answer sheets, repeated A4 4-up worksheets, or one A4 page per unit with 3 question cards and 1 answer card.
---

# Vocab Print Cards

## Overview

Use this skill to turn a vocabulary or phrase list into print-ready A4 PDFs:

- a 4-up worksheet page with repeated Chinese-to-English blank cards
- a separate answer-key page
- one A4 page per unit with 3 question cards and 1 answer card
- optional submission to the system printer after validating the PDF

Prefer the bundled script `scripts/make_vocab_cards.py` instead of rewriting ReportLab layout code.

## Workflow

1. Parse the user's list into ordered `(zh, en)` pairs.
   - If the user supplies only English, provide concise learner-friendly Chinese prompts.
   - Preserve the user's English spelling, capitalization, hyphenation, and phrase wording unless there is an obvious typo.
   - For ambiguous phrases, choose the classroom/basic-English meaning and keep Chinese prompts short.
2. Choose the layout from the user's wording:
   - repeated 4-up worksheet plus separate answer key: use the default layout
   - “每单元一页 / 3 question, 1 answer”: use `--layout unit-3q1a`
3. Create an input JSON file in the current workspace, usually under `work/`.
   - Default layout: a flat `items` list.
   - Unit layout: a `units` list; preserve the requested unit order and title.
4. Run `scripts/make_vocab_cards.py` to generate the requested PDF set.
5. Render every PDF page with `pdftoppm` when available and inspect for clipped text, missing Chinese glyphs, overlap, question/answer placement, and page count.
6. Save final PDFs under the user-facing output directory for the current thread.
7. If the user asks to print, query printers with `lpstat -p -d -v`, then submit with `lp`; use escalation when required by the environment.

## Input Format

Use UTF-8 JSON:

```json
[
  {"zh": "打网球", "en": "play tennis"},
  {"zh": "去健身俱乐部", "en": "go to a health club"}
]
```

The script also accepts `{"items": [...]}`.

For `--layout unit-3q1a`, use grouped input:

```json
{
  "units": [
    {
      "title": "Unit 1",
      "items": [
        {"zh": "打网球", "en": "play tennis"}
      ]
    }
  ]
}
```

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
- with `--layout unit-3q1a`: `<basename>_unit_cards_3q1a.pdf`, one page per unit

Useful options:

- `--worksheet-title "汉译英默写卡"`
- `--answer-title "汉译英默写卡答案"`
- `--subtitle "活动短语"`
- `--layout unit-3q1a`
- `--printer PRINTER_NAME --print worksheet|answer|both`

## Printing Notes

Only print after the generated PDF has been rendered and visually checked. If no printer is configured, tell the user the PDF path and the printer status. If a default printer exists, use it unless the user specified another printer.

Use one answer-key page for the answers unless the item count requires multiple pages. Do not make the answer key 4-up unless the user asks. In `unit-3q1a` mode, the fourth quadrant is the answer card and `--print worksheet` prints the combined unit-card PDF.
