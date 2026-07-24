#!/usr/bin/env python3
"""Generate A4 4-up vocabulary worksheet and answer-key PDFs."""

from __future__ import annotations

import argparse
import json
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas


FONT_PATHS = [
    Path("/System/Library/Fonts/Supplemental/Arial Unicode.ttf"),
    Path("/Library/Fonts/Arial Unicode.ttf"),
    Path("/System/Library/Fonts/STHeiti Light.ttc"),
    Path("/System/Library/Fonts/STHeiti Medium.ttc"),
]


@dataclass(frozen=True)
class Item:
    zh: str
    en: str


def register_font() -> str:
    for path in FONT_PATHS:
        if path.exists():
            pdfmetrics.registerFont(TTFont("VocabCardFont", str(path)))
            return "VocabCardFont"
    return "Helvetica"


def load_items(path: Path) -> list[Item]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(data, dict):
        data = data.get("items", [])
    if not isinstance(data, list):
        raise ValueError("Input JSON must be a list or an object with an 'items' list.")

    items: list[Item] = []
    for index, row in enumerate(data, start=1):
        if not isinstance(row, dict) or "zh" not in row or "en" not in row:
            raise ValueError(f"Item {index} must contain 'zh' and 'en' fields.")
        zh = str(row["zh"]).strip()
        en = str(row["en"]).strip()
        if not zh or not en:
            raise ValueError(f"Item {index} has an empty 'zh' or 'en' field.")
        items.append(Item(zh=zh, en=en))
    if not items:
        raise ValueError("Input contains no vocabulary items.")
    return items


def draw_dotted_line(c: canvas.Canvas, x1: float, y1: float, x2: float, y2: float) -> None:
    c.saveState()
    c.setStrokeColor(colors.HexColor("#B8B8B8"))
    c.setDash(2, 3)
    c.setLineWidth(0.45)
    c.line(x1, y1, x2, y2)
    c.restoreState()


def draw_card(
    c: canvas.Canvas,
    x: float,
    y: float,
    w: float,
    h: float,
    font_name: str,
    items: list[Item],
    title: str,
) -> None:
    pad_x = 8 * mm
    top = y + h - 7 * mm
    left = x + pad_x
    right = x + w - pad_x

    c.saveState()
    c.setFillColor(colors.HexColor("#111111"))
    c.setFont(font_name, 11.5)
    c.drawString(left, top, title)

    c.setFont(font_name, 7.5)
    c.drawRightString(right, top + 0.5 * mm, "姓名：________  日期：________")

    c.setFont(font_name, 6.8)
    c.setFillColor(colors.HexColor("#555555"))
    c.drawString(left, top - 5.6 * mm, "根据中文写出英文。")

    available_h = h - 31 * mm
    row_h = min(8.65 * mm, max(5.3 * mm, available_h / max(len(items), 1)))
    row_start = top - 14.0 * mm
    number_w = 7 * mm
    chinese_w = min(40 * mm, max(28 * mm, w * 0.38))
    blank_start = left + number_w + chinese_w
    blank_end = right
    text_size = 8.6 if row_h >= 7 * mm else 7.6
    num_size = 8.2 if row_h >= 7 * mm else 7.2

    c.setStrokeColor(colors.HexColor("#777777"))
    c.setLineWidth(0.45)
    c.setFillColor(colors.HexColor("#111111"))
    for idx, item in enumerate(items, start=1):
        row_y = row_start - (idx - 1) * row_h
        baseline = row_y + 1.4 * mm
        c.setFont(font_name, num_size)
        c.drawRightString(left + number_w - 1.5 * mm, baseline, f"{idx}.")
        c.setFont(font_name, text_size)
        c.drawString(left + number_w, baseline, item.zh)
        c.line(blank_start, row_y + 0.9 * mm, blank_end, row_y + 0.9 * mm)

    c.restoreState()


def make_worksheet(path: Path, items: list[Item], font_name: str, title: str) -> None:
    page_w, page_h = A4
    c = canvas.Canvas(str(path), pagesize=A4)
    c.setTitle(title)
    c.setAuthor("Codex")

    margin = 8 * mm
    gutter = 5 * mm
    cell_w = (page_w - 2 * margin - gutter) / 2
    cell_h = (page_h - 2 * margin - gutter) / 2
    cells = [
        (margin, margin + cell_h + gutter, cell_w, cell_h),
        (margin + cell_w + gutter, margin + cell_h + gutter, cell_w, cell_h),
        (margin, margin, cell_w, cell_h),
        (margin + cell_w + gutter, margin, cell_w, cell_h),
    ]

    draw_dotted_line(c, page_w / 2, margin, page_w / 2, page_h - margin)
    draw_dotted_line(c, margin, page_h / 2, page_w - margin, page_h / 2)
    for cell in cells:
        draw_card(c, *cell, font_name=font_name, items=items, title=title)

    c.showPage()
    c.save()


def draw_answer_headers(c: canvas.Canvas, font_name: str, page_w: float, top: float, margin_x: float, title: str, subtitle: str) -> float:
    c.setFont(font_name, 18)
    c.setFillColor(colors.HexColor("#111111"))
    c.drawString(margin_x, top, title)

    c.setFont(font_name, 9.5)
    c.setFillColor(colors.HexColor("#555555"))
    c.drawString(margin_x, top - 8 * mm, subtitle)

    table_top = top - 20 * mm
    chinese_x = margin_x + 14 * mm
    english_x = margin_x + 80 * mm

    c.setStrokeColor(colors.HexColor("#D0D0D0"))
    c.setLineWidth(0.55)
    c.line(margin_x, table_top + 6 * mm, page_w - margin_x, table_top + 6 * mm)

    c.setFont(font_name, 10)
    c.setFillColor(colors.HexColor("#555555"))
    c.drawString(chinese_x, table_top + 8 * mm, "中文")
    c.drawString(english_x, table_top + 8 * mm, "英文答案")
    return table_top


def make_answer_key(path: Path, items: list[Item], font_name: str, title: str, subtitle: str) -> None:
    page_w, page_h = A4
    c = canvas.Canvas(str(path), pagesize=A4)
    c.setTitle(title)
    c.setAuthor("Codex")

    margin_x = 24 * mm
    top = page_h - 24 * mm
    row_h = 11 * mm
    table_top = draw_answer_headers(c, font_name, page_w, top, margin_x, title, subtitle)
    num_x = margin_x
    chinese_x = margin_x + 14 * mm
    english_x = margin_x + 80 * mm
    bottom_limit = 22 * mm

    rows_per_page = int((table_top - bottom_limit) // row_h) + 1
    for idx, item in enumerate(items, start=1):
        if idx > 1 and (idx - 1) % rows_per_page == 0:
            c.showPage()
            table_top = draw_answer_headers(c, font_name, page_w, top, margin_x, title, subtitle)
        y = table_top - ((idx - 1) % rows_per_page) * row_h

        c.setStrokeColor(colors.HexColor("#E6E6E6"))
        c.line(margin_x, y - 3 * mm, page_w - margin_x, y - 3 * mm)

        c.setFont(font_name, 11)
        c.setFillColor(colors.HexColor("#333333"))
        c.drawRightString(num_x + 8 * mm, y, f"{idx}.")
        c.drawString(chinese_x, y, item.zh)

        c.setFont(font_name, 11.5)
        c.setFillColor(colors.HexColor("#111111"))
        c.drawString(english_x, y, item.en)

    c.showPage()
    c.save()


def submit_print(files: Iterable[Path], printer: str | None) -> None:
    for file_path in files:
        command = ["lp"]
        if printer:
            command.extend(["-d", printer])
        command.append(str(file_path))
        subprocess.run(command, check=True)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, type=Path, help="UTF-8 JSON file with zh/en vocabulary items.")
    parser.add_argument("--out-dir", required=True, type=Path, help="Directory for generated PDFs.")
    parser.add_argument("--basename", default="vocab", help="Base filename for output PDFs.")
    parser.add_argument("--worksheet-title", default="汉译英默写卡")
    parser.add_argument("--answer-title", default="汉译英默写卡答案")
    parser.add_argument("--subtitle", default="词汇短语")
    parser.add_argument("--printer", help="Printer name for lp. Omit to use system default.")
    parser.add_argument("--print", choices=["none", "worksheet", "answer", "both"], default="none")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    items = load_items(args.input)
    args.out_dir.mkdir(parents=True, exist_ok=True)
    font_name = register_font()

    worksheet = args.out_dir / f"{args.basename}_cards_4up.pdf"
    answer = args.out_dir / f"{args.basename}_answer_key.pdf"
    make_worksheet(worksheet, items, font_name, args.worksheet_title)
    make_answer_key(answer, items, font_name, args.answer_title, args.subtitle)

    if args.print != "none":
        files = []
        if args.print in {"worksheet", "both"}:
            files.append(worksheet)
        if args.print in {"answer", "both"}:
            files.append(answer)
        submit_print(files, args.printer)

    print(f"worksheet={worksheet}")
    print(f"answer_key={answer}")


if __name__ == "__main__":
    main()
