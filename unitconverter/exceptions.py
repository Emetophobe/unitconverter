# Copyright (c) 2022-2025 Mike Cunningham
# https://www.github.com/emetophobe/unitconverter


from pathlib import Path


class ConverterError(Exception):
    """ Base exception class for all converter-related errors. """

    def __init__(self, msg: str, details: Path | str | None = None) -> None:
        self.msg = msg
        self.details = details

    def __str__(self) -> str:
        if self.details:
            return f"Error: {self.msg} {self.details}"
        else:
            return f"Error: {self.msg}"


class CategoryError(ConverterError):
    """ Incompatible unit categories. """
    def __init__(self, source: str, source_category: str, dest: str, dest_category: str) -> None:
        super().__init__(f"Can't convert between {source} ({source_category})"
                         f" and {dest} ({dest_category})")
