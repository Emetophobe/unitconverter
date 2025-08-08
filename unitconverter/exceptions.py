# Copyright (c) 2022-2025 Mike Cunningham


from pathlib import Path


class ConverterError(Exception):
    """ Base exception class for all converter-related errors. """

    def __init__(self, msg: str) -> None:
        self.msg = f"Error: {msg}"

    def __str__(self) -> str:
        return self.msg


class CategoryError(ConverterError):
    """ Incompatible unit errors. """
    def __init__(self, source: str, source_category: str, dest: str, dest_category: str) -> None:
        super().__init__(f"Can't convert between {source} ({source_category})"
                         f" and {dest} ({dest_category})")


class DefinitionError(ConverterError):
    """ Definition related errors. """
    def __init__(self, msg: str, filename: str | Path | None = None) -> None:
        if filename:
            super().__init__(f"{msg} ({filename})")
        else:
            super().__init__(f"{msg}")


class DimensionError(ConverterError):
    """ Dimension related errors. """
    pass


class PrefixError(ConverterError):
    """ Prefix related errors. """
    pass


class UnitError(ConverterError):
    """ Unit related errors. """
    pass
