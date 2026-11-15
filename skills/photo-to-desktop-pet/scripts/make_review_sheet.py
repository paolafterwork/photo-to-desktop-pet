#!/usr/bin/env python3
"""Render known atlas cells for human review. This is NOT a quality validator."""
import argparse
from pathlib import Path

from PIL import Image, ImageDraw

COUNTS = (6, 8, 8, 4, 5, 8, 6, 6, 6, 8, 8)


def render(atlas_path, output, rows):
    output = Path(output)
    if output.exists():
        raise FileExistsError('Choose a new output path; existing review files are preserved')
    if output.suffix.lower() != '.png':
        raise ValueError('Review output must have a .png extension')
    with Image.open(atlas_path) as opened:
        atlas = opened.convert('RGBA')
    if atlas.size not in {(1536, 1872), (1536, 2288)}:
        raise ValueError('Expected a supported 192x208-cell Pets atlas; use upstream validation')
    row_count = atlas.height // 208
    if not rows or len(set(rows)) != len(rows) or any(r < 0 or r >= row_count for r in rows):
        raise ValueError('Rows must be unique indexes within this atlas')
    width = max(COUNTS[r] for r in rows) * 192
    sheet = Image.new('RGB', (width, len(rows) * 236), '#f5f2ea')
    draw = ImageDraw.Draw(sheet)
    for index, row in enumerate(rows):
        for col in range(COUNTS[row]):
            cell = atlas.crop((col*192, row*208, (col+1)*192, (row+1)*208))
            sheet.paste(cell, (col*192, index*236+28), cell)
            draw.text((col*192+6, index*236+8), f'row {row} / frame {col}', fill='#29251f')
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open('xb') as destination:
        sheet.save(destination, format='PNG')
    return sheet.size


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('atlas')
    parser.add_argument('--rows', required=True, help='Zero-indexed rows, e.g. 3,6,7')
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    try:
        rows = [int(value.strip()) for value in args.rows.split(',')]
        size = render(args.atlas, args.output, rows)
    except (OSError, ValueError) as exc:
        parser.exit(1, f'{exc}\n')
    print(f'Wrote review aid {args.output}, {size[0]}x{size[1]}; not a validation result')


if __name__ == '__main__':
    main()
