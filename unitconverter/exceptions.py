# Copyright (c) 2022-2025 Mike Cunningham


from pathlib import Path


class ConverterError(Exception):
    """ Base exception class for all converter-related errors. """

    def __init__(self, msg: str) -> None:
        self.msg = f"Error: {msg}"

    def __str__(self) -> str:
        return self.msg


class CategoryError(ConverterError):
    """ Category mismatch errors. """
    def __init__(self, source: str, source_category: list[str], dest: str,
                 dest_category: list[str]) -> None:
        s = ", ".join(source_category) if source_category else "undefined category"
        d = ", ".join(dest_category) if dest_category else "undefined category"
        super().__init__(f"{source} ({s}) and {dest} ({d}) are not compatible units")


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
