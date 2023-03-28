# Copyright (c) 2022-2023 Mike Cunningham


class ConverterError(ValueError):
    """ Base class for all converter-related exceptions. """

    def __init__(self, msg: str) -> None:
        self.msg = msg

    def __str__(self) -> str:
        return self.msg


class UnitError(ConverterError):

    def __init__(self, name: str) -> None:
        self.msg = f'Invalid unit: {name}'


class CategoryError(ConverterError):

    def __init__(self, source, dest) -> None:
        self.msg = (f'Category mismatch between {source.name} ({source.category})'
                    f' and {dest.name} ({dest.category})')
