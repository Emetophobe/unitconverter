# Copyright (c) 2022-2025 Mike Cunningham


from decimal import Decimal

from unitconverter.dimension import Dimension
from unitconverter.formatting import parse_decimal


class Definition:
    """
        A unit definition is used to define a unit in the Registry.
    """

    def __init__(self, name: str, symbols: list[str], aliases: list[str], factor: Decimal,
                 dimension: Dimension | dict, prefix: str | None = None) -> None:
        """ Initialize unit definition. """
        self.name = name
        self.symbols = symbols
        self.aliases = aliases
        self.factor = parse_decimal(factor)
        self.dimen = Dimension(dimension)
        self.prefix = prefix

    def names(self) -> list[str]:
        """ Returns a list of strings used to identify this unit. """
        return [self.name] + self.symbols + self.aliases

    def __str__(self) -> str:
        return self.name
