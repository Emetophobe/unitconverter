# Copyright (c) 2022-2023 Mike Cunningham


from decimal import Decimal

from unitconverter.exceptions import UnitError
from unitconverter.prefixes import PrefixScale, Prefix, get_prefixes


class Unit:
    """ A unit of measurement. """

    def __init__(self,
                 name: str,
                 category: str,
                 symbols: list[str],
                 aliases: list[str],
                 factor: Decimal | int | str,
                 offset: Decimal | int | str = 0,
                 power: Decimal | int | str = 1,
                 prefix_scale: PrefixScale = PrefixScale.NONE):
        """ Initialize unit.

        Args:
            name (str):
                unit name.

            category (str):
                category name.

            symbols (list[str]):
                list of symbols. Can be an empty list.

            aliases (list[str]):
                list of aliases. Can be an empty list.

            factor (Decimal | int | str):
                conversion factor.

            offset (Decimal | int | str, optional):
                conversion offset. Defaults to 0.

            power (Decimal | int | str, optional):
                unit power. Defaults to 1.

            prefix_scale (PrefixScale, optional):
                prefix scale option. Defaults to PrefixScale.NONE.

        Raises:
            UnitError: if the unit is invalid.
        """
        self.name = name
        self.category = category
        self.symbols = symbols
        self.aliases = aliases

        self.factor = factor
        self.offset = offset
        self.power = power

        try:
            self.prefix_scale = PrefixScale(prefix_scale)
        except ValueError:
            raise UnitError(f'{self.name!r} has an invalid prefix scale: {prefix_scale}')

    def names(self) -> list[str]:
        """ Get a list of all unit names and symbols. """
        return [self.name] + self.symbols + self.aliases

    def prefix(self, prefix: Prefix) -> 'Unit':
        """ Create a new prefixed unit.

        Args:
            prefix (Prefix): a prefix instance.

        Raises:
            UnitError: if the unit could not be prefixed.

        Returns:
            Unit: a new prefixed unit.
        """
        self._valid_prefix(prefix)
        factor, symbol, prefix = prefix

        # Create new unit name, symbols, aliases, and factor
        name = self._add_prefix(prefix, self.name)
        symbols = [symbol + name for name in self.symbols]
        aliases = [self._add_prefix(prefix, name) for name in self.aliases]
        factor = (Decimal(factor) * Decimal(self.factor)) ** Decimal(self.power)

        # Don't allow prefixed units to be prefixed again
        prefix_scale = PrefixScale.NONE

        # Return prefixed unit
        return Unit(name, self.category, symbols, aliases, factor, self.offset,
                    self.power, prefix_scale)

    def _valid_prefix(self, prefix: Prefix) -> None:
        """ Check if prefix is valid.

        Args:
            prefix (Prefix): a prefix instance.

        Raises:
            UnitError: if unit doesn't support the specified prefix.
        """
        prefixes = get_prefixes(self.prefix_scale)

        if not prefixes:
            raise UnitError(f"{self.name} doesn't support prefix scaling")

        if prefix not in prefixes:
            raise UnitError(f"{self.name} doesn't support {prefix.name} prefix")

    def _add_prefix(self, prefix: str, name: str) -> str:
        """ Add a prefix to name. """
        # Special case for square and cubic units
        if name.startswith('square '):
            return name[:7] + prefix + name[7:]
        elif name.startswith('cubic '):
            return name[:6] + prefix + name[6:]

        # Prefix other units normally
        return prefix + name

    def __contains__(self, name: str) -> bool:
        """ Returns True if name matches one of the unit names. """
        return name in self.names()

    def __repr__(self) -> str:
        args = ', '.join(repr(s) for s in self.__dict__.values())
        return (f'Unit({args})')

    def __str__(self) -> str:
        return self.name
