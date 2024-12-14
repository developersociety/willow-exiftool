from typing import ClassVar

from willow.optimizers.base import OptimizerBase

__all__ = [
    "ExifToolAVIF",
    "ExifToolBase",
    "ExifToolHEIC",
    "ExifToolJPEG",
    "ExifToolPNG",
    "ExifToolWEBP",
]


class ExifToolBase(OptimizerBase):
    library_name: ClassVar[str] = "exiftool"

    class Meta:
        abstract = True

    @classmethod
    def get_command_arguments(cls, file_path: str, progressive: bool = False) -> list[str]:
        return [
            "-EXIF=",  # strip all Exif data
            "-overwrite_original",  # don't create an _original file
            file_path,
        ]


# Wand AVIF optimizer is AVIF
class ExifToolAVIF(ExifToolBase):
    image_format: ClassVar[str] = "avif"


# Pillow AVIF/HEIC/HEIF optimizer are all named HEIC
class ExifToolHEIC(ExifToolBase):
    image_format: ClassVar[str] = "heic"


class ExifToolJPEG(ExifToolBase):
    image_format: ClassVar[str] = "jpeg"


class ExifToolPNG(ExifToolBase):
    image_format: ClassVar[str] = "png"


class ExifToolWEBP(ExifToolBase):
    image_format: ClassVar[str] = "webp"
