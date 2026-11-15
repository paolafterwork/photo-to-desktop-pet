import importlib.util
import tempfile
import unittest
from pathlib import Path

from PIL import Image

SCRIPTS = Path(__file__).resolve().parents[1] / 'skills/photo-to-desktop-pet/scripts'


def load(name):
    spec = importlib.util.spec_from_file_location(name, SCRIPTS / f'{name}.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


prepare = load('prepare_reference').prepare
render = load('make_review_sheet').render


class ReferenceTests(unittest.TestCase):
    def test_orientation_is_applied_and_original_untouched(self):
        with tempfile.TemporaryDirectory() as folder:
            folder = Path(folder)
            source, output = folder/'source.jpg', folder/'reference.png'
            photo = Image.new('RGB', (80, 40), 'orange')
            exif = Image.Exif()
            exif[274] = 6  # Rotate 90 degrees for display.
            photo.save(source, exif=exif)
            original = source.read_bytes()
            result = prepare(source, output)
            with Image.open(output) as actual:
                self.assertEqual(actual.size, (40, 80))
                self.assertNotIn(274, actual.getexif())
            self.assertEqual(result['reference_size'], [40, 80])
            self.assertEqual(source.read_bytes(), original)

    def test_bounds_and_existing_outputs_are_preserved(self):
        with tempfile.TemporaryDirectory() as folder:
            source, output = Path(folder)/'source.png', Path(folder)/'reference.png'
            Image.new('RGB', (800, 400), 'orange').save(source)
            prepare(source, output, 200)
            with Image.open(output) as actual:
                self.assertEqual(actual.size, (200, 100))
            original = output.read_bytes()
            with self.assertRaises(FileExistsError):
                prepare(source, output)
            self.assertEqual(output.read_bytes(), original)
            with self.assertRaises(FileExistsError):
                prepare(source, source)

    def test_transparency_preserved(self):
        with tempfile.TemporaryDirectory() as folder:
            source, output = Path(folder)/'source.png', Path(folder)/'reference.png'
            im = Image.new('RGBA', (100, 100), (20, 30, 40, 0))
            im.putpixel((50, 50), (255, 100, 0, 255))
            im.save(source)
            prepare(source, output)
            with Image.open(output) as actual:
                self.assertEqual(actual.getpixel((0, 0))[3], 0)
                self.assertEqual(actual.getpixel((50, 50))[3], 255)


class ReviewTests(unittest.TestCase):
    def test_extracts_the_requested_cells_in_order(self):
        with tempfile.TemporaryDirectory() as folder:
            folder = Path(folder)
            atlas_path, out = folder/'atlas.png', folder/'review.png'
            atlas = Image.new('RGBA', (1536, 2288))
            # Simple colored test cells, not generated pet artwork.
            atlas.paste((255, 0, 0, 255), (0, 7*208, 192, 8*208))
            atlas.paste((0, 0, 255, 255), (192, 7*208, 384, 8*208))
            atlas.save(atlas_path)
            self.assertEqual(render(atlas_path, out, [7]), (1152, 236))
            with Image.open(out) as actual:
                self.assertEqual(actual.getpixel((90, 100)), (255, 0, 0))
                self.assertEqual(actual.getpixel((282, 100)), (0, 0, 255))
            with self.assertRaises(FileExistsError):
                render(atlas_path, out, [7])

    def test_rejects_invalid_geometry_and_rows(self):
        with tempfile.TemporaryDirectory() as folder:
            folder = Path(folder)
            atlas = folder/'atlas.png'
            Image.new('RGBA', (100, 100)).save(atlas)
            with self.assertRaises(ValueError):
                render(atlas, folder/'review.png', [0])
            Image.new('RGBA', (1536, 1872)).save(atlas)
            for rows in ([], [9], [-1], [0, 0]):
                with self.assertRaises(ValueError):
                    render(atlas, folder/'review.png', rows)


if __name__ == '__main__':
    unittest.main()
