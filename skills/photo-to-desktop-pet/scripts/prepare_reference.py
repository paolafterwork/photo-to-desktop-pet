#!/usr/bin/env python3
"""Create an oriented PNG reference without modifying or overwriting a source."""
import argparse
import hashlib
import json
from pathlib import Path

from PIL import Image, ImageOps


def prepare(source, output, max_edge=1600):
    source, output = Path(source).resolve(), Path(output).resolve()
    if not 64 <= max_edge <= 4096:
        raise ValueError('max_edge must be between 64 and 4096')
    if output.suffix.lower() != '.png':
        raise ValueError('Reference output must have a .png extension')
    if source == output or output.exists():
        raise FileExistsError('Choose a new output path; existing files are preserved')
    if source.suffix.lower() in {'.heic', '.heif'}:
        try:
            import pillow_heif
            pillow_heif.register_heif_opener()
        except ImportError as exc:
            raise ValueError('HEIC needs pillow-heif in this interpreter, or a JPEG/PNG export') from exc
    digest = hashlib.sha256(source.read_bytes()).hexdigest()
    with Image.open(source) as opened:
        original_size = list(opened.size)
        image = ImageOps.exif_transpose(opened)
        image = image.convert('RGBA' if 'A' in image.getbands() or 'transparency' in image.info else 'RGB')
        image.thumbnail((max_edge, max_edge), Image.Resampling.LANCZOS)
        output.parent.mkdir(parents=True, exist_ok=True)
        # Exclusive creation prevents accidental overwrite, including racing runs.
        with output.open('xb') as destination:
            image.save(destination, format='PNG')
        return {'ok': True, 'source': str(source), 'source_sha256': digest,
                'original_size': original_size, 'reference': str(output),
                'reference_size': list(image.size)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('source')
    parser.add_argument('--output', required=True)
    parser.add_argument('--max-edge', type=int, default=1600)
    args = parser.parse_args()
    try:
        result = prepare(args.source, args.output, args.max_edge)
    except (OSError, ValueError, Image.DecompressionBombError) as exc:
        print(json.dumps({'ok': False, 'error': str(exc)}, ensure_ascii=False))
        return 1
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
