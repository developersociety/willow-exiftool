from typing import ClassVar

from _typeshed import Incomplete

logger: Incomplete

class OptimizerBase:
    library_name: ClassVar[str]
    image_format: ClassVar[str]
    class Meta:
        abstract: bool

    @classmethod
    def applies_to(cls, image_format: str) -> bool: ...
    @classmethod
    def get_check_library_arguments(cls) -> list[str]: ...
    @classmethod
    def check_library(cls) -> bool: ...
    @classmethod
    def get_command_arguments(cls, file_path: str) -> list[str]: ...
    @classmethod
    def process(cls, file_path: str) -> None: ...
