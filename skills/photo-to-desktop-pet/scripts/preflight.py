#!/usr/bin/env python3
"""Read-only local image-processing preflight; does not test remote capabilities."""
import importlib
import json
import sys


def check():
    errors = []
    if sys.version_info < (3, 10):
        errors.append('Python 3.10+ is required by the upstream Pets scripts.')
    packages = {}
    for module in ('PIL', 'pillow_heif'):
        try:
            loaded = importlib.import_module(module)
            packages[module] = getattr(loaded, '__version__', 'available')
        except ImportError:
            packages[module] = None
    if not packages['PIL']:
        errors.append('Pillow is missing in this interpreter.')
    return {
        'ok': not errors,
        'python': sys.version.split()[0],
        'executable': sys.executable,
        'packages': packages,
        'errors': errors,
        'notes': ['HEIC decoding needs pillow-heif or a supported platform decoder.',
                  'Pets, image generation and desktop UI availability must be checked through host tools.'],
    }


if __name__ == '__main__':
    result = check()
    print(json.dumps(result, ensure_ascii=False, indent=2))
    sys.exit(0 if result['ok'] else 1)
