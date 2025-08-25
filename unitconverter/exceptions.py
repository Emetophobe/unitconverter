# Copyright (c) 2022-2025 Mike Cunningham
# https://www.github.com/emetophobe/unitconverter


class ConverterError(Exception):
    """ Base exception for all unit converter errors. """

    def __init__(self, msg: str, details: str | None = None) -> None:
        self.msg = msg
        self.details = details

    def __str__(self) -> str:
        if self.details:
            return f"{self.msg} ({self.details})"
        else:
            return self.msg


class ConversionError(ConverterError):
    """ Incompatible unit errors. """

    def __init__(self, source, target) -> None:
        super().__init__(f"Can't convert between {source} and {target}")


class InvalidUnitError(ConverterError):
    """ Invalid/undefined unit errors. """

    def __init__(self, name: str) -> None:
        super().__init__(f"{name!r} is not a defined unit")


class DuplicateUnitError(ConverterError):
    """ Duplicate unit name errors. """

    def __init__(self, name: str, original: str):
        if name != original:
            super().__init__(f"{name} is already defined by {original}")
        else:
            super().__init__(f"{name} is already defined")
