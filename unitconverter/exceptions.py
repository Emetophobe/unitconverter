# Copyright (c) 2022-2023 Mike Cunningham


class ConverterError(ValueError):
    """ Base exception class for all converter-related errors. """

    def __init__(self, msg: str) -> None:
        self.msg = msg

    def __str__(self) -> str:
        return self.msg


class UnitError(ConverterError):
    """ Invalid unit error. """
    pass


class CategoryError(ConverterError):
    """ Category mismatch error. """

    def __init__(self, source, dest) -> None:
        self.msg = (f'Category mismatch: {source.name} ({source.category})'
                    f' and {dest.name} ({dest.category})')


class DefinitionError(ConverterError):
    """ Invalid unit definition. """
