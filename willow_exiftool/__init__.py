def setup() -> None:
    from willow.registry import registry  # noqa:PLC0415

    from .stripexif import (  # noqa:PLC0415
        ExifToolAVIF,
        ExifToolHEIC,
        ExifToolJPEG,
        ExifToolPNG,
        ExifToolWEBP,
    )

    registry.register_optimizer(ExifToolAVIF)
    registry.register_optimizer(ExifToolHEIC)
    registry.register_optimizer(ExifToolJPEG)
    registry.register_optimizer(ExifToolPNG)
    registry.register_optimizer(ExifToolWEBP)


setup()
