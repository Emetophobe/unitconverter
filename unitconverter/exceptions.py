# Copyright (c) 2022-2025 Mike Cunningham
# https://www.github.com/emetophobe/unitconverter


class ConverterError(Exception):
    """ Base exception for all converter-related errors. """

    def __init__(self, msg: str, details: str | None = None) -> None:
        self.msg = msg
        self.details = details

    def __str__(self) -> str:
        if self.details:
            return f"{self.msg} {self.details}"
        else:
            return self.msg


class CategoryError(ConverterError):
    """ Incompatible unit categories. """

    def __init__(self, source, dest) -> None:
        super().__init__(f"Can't convert between {source} and {dest}")
