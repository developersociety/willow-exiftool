from unittest import TestCase

from willow_exiftool.stripexif import (
    ExifToolAVIF,
    ExifToolHEIC,
    ExifToolJPEG,
    ExifToolPNG,
    ExifToolWEBP,
)


class ExifToolBaseTestCase(TestCase):
    def test_get_command_arguments(self):
        self.assertEqual(
            ExifToolAVIF.get_command_arguments("demo.jpg"),
            ["-EXIF=", "-overwrite_original", "demo.jpg"],
        )


class ExifToolAVIFTestCase(TestCase):
    def test_applies_to(self):
        self.assertTrue(ExifToolAVIF.applies_to("avif"))


class ExifToolHEICTestCase(TestCase):
    def test_applies_to(self):
        self.assertTrue(ExifToolHEIC.applies_to("heic"))


class ExifToolJPEGTestCase(TestCase):
    def test_applies_to(self):
        self.assertTrue(ExifToolJPEG.applies_to("jpeg"))


class ExifToolPNGTestCase(TestCase):
    def test_applies_to(self):
        self.assertTrue(ExifToolPNG.applies_to("png"))


class ExifToolWEBPTestCase(TestCase):
    def test_applies_to(self):
        self.assertTrue(ExifToolWEBP.applies_to("webp"))
