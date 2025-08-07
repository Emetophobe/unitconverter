# Copyright (c) 2022-2025 Mike Cunningham


from pathlib import Path


class ConverterError(ValueError):
    """ Base exception class for all converter-related errors. """

    def __init__(self, msg: str, filename: str | Path | None = None) -> None:
        self.msg = msg
        self.filename = filename

    def __str__(self) -> str:
        if self.filename:
            return f"{self.msg} ({self.filename})"
        else:
            return self.msg


class CategoryError(ConverterError):
    """ Category errors (i.e category mismatch) """
    pass


class DefinitionError(ConverterError):
    """ Exceptions defining units or categories. """
    pass


class DimensionError(ConverterError):
    """ Dimension related errors. """
    pass


class PrefixError(ConverterError):
    """ Prefix related errors. """
    pass


class UnitError(ConverterError):
    """ Unit related errors. """
    pass
