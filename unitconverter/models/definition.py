# Copyright (c) 2022-2025 Mike Cunningham


from decimal import Decimal

from unitconverter.formatting import parse_decimal
from unitconverter.models.dimension import Dimension


class Definition:
    """
        A unit definition is used to define a unit in the Registry.
    """

    def __init__(self,
                 name: str, symbols: list[str],
                 aliases: list[str],
                 factor: Decimal | int | str,
                 category: str,
                 dimension: Dimension | dict,
                 prefix: str | None = None
                 ) -> None:
        """ Create a unit definition.

        A unit definition is used to define a unit in the Registry. Once a definition has been
        added to the registry you can get the Unit by calling Registry.get_unit("unit name").

        Args:
            name (str):
                The unit name.

            symbols (list[str]):
                A list of unit symbols. Can be an empty list.

            aliases (list[str]):
                A list of unit aliases. Can be an empty list.

            factor (Decimal | int | str):
                The conversion factor.

            category (str):
                The unit category.

            dimension (Dimension | dict):
                The unit dimension.

            prefix (str | None, optional):
                The unit prefix setting. Defaults to None.
        """
        self.name = name
        self.symbols = symbols
        self.aliases = aliases
        self.factor = parse_decimal(factor)
        self.category = category
        self.dimen = Dimension(dimension)
        self.prefix = prefix

    def names(self) -> list[str]:
        """ Get a list of all unit names, symbols, and aliases. """
        return [self.name] + self.symbols + self.aliases

    def __str__(self) -> str:
        return self.name
