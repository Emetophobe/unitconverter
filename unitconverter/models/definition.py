# Copyright (c) 2022-2025 Mike Cunningham


from decimal import Decimal

from unitconverter.formatting import parse_decimal
from unitconverter.models.dimension import Dimension


class Definition:
    """
        A unit definition is used to define a unit in the Registry.
    """

    def __init__(self, name: str, symbols: list[str], aliases: list[str], factor: Decimal,
                 dimension: Dimension | dict, prefix: str | None = None) -> None:
        """ Create a unit definition.

        A unit definition is used to define a unit in the Registry. Once a definition has been
        added to the registry you can get the Unit by calling Registry.get_unit("unit name").

        Args:
            name (str): The unit name. Must be unique.
            symbols (list[str]): A list of unit symbols. Must be unique.
            aliases (list[str]): A list of unit aliases. Must be unique.
            factor (Decimal): A conversion factor.
            dimension (Dimension | dict): The unit's dimension.
            prefix (str | None, optional): What prefix option the unit supports. Defaults to None.
        """
        self.name = name
        self.symbols = symbols
        self.aliases = aliases
        self.factor = parse_decimal(factor)
        self.dimen = Dimension(dimension)
        self.prefix = prefix

    def names(self) -> list[str]:
        """ Get a list of all unit names, symbols, and aliases. """
        return [self.name] + self.symbols + self.aliases

    def __str__(self) -> str:
        return self.name
