# Copyright (c) 2022-2023 Mike Cunningham


from decimal import Decimal

from unitconverter.exceptions import UnitError
from unitconverter.prefixes import PrefixScale
from unitconverter.utils import parse_decimal


class Unit:
    """ A unit of measurement. """

    def __init__(self,
                 name,
                 category,
                 symbols,
                 aliases,
                 factor,
                 power=1,
                 offset=0,
                 prefix_scale=PrefixScale.NONE):
        """ Initialize unit.

        Args:
            name (str):
                unit name.

            category (str):
                category name.

            symbols (list[str]):
                list of symbols.

            aliases (list[str]):
                list of aliases.

            factor (Decimal | int | str):
                conversion factor.

            power (Decimal | int | str, optional):
                optional power. Defaults to 1.

            offset (Decimal | int | str, optional):
                optional offset. Defaults to 0.

            prefix_scale (PrefixScale, optional):
                prefix scale. Defaults to PrefixScale.NONE.

        Raises:
            TypeError: if an argument is the wrong type.
            ValueError: if an argument is the wrong value.
        """
        self.name = name
        self.category = category
        self.symbols = symbols
        self.aliases = aliases

        self.factor = parse_decimal(factor, f'{name!r} has an invalid factor')
        self.power = parse_decimal(power, f'{name!r} has an invalid power')
        self.offset = parse_decimal(offset, f'{name!r} has an invalid offset')

        try:
            self.prefix_scale = PrefixScale(prefix_scale)
        except ValueError:
            raise UnitError(f'{self.name!r} has an invalid prefix scale: {prefix_scale}')

    def prefix(self, factor: Decimal | int | str, symbol: str, prefix: str) -> 'Unit':
        """ Create a new unit by applying a prefix, i.e "kilo".

        Args:
            factor (Decimal | int | str):
                multiplication factor.

            symbol (str):
                prefix symbol.

            prefix (str):
                prefix name.

        Returns:
            Unit: a new unit instance.
        """
        # Create new name, symbols, aliases, and factor
        name = self._add_prefix(prefix, self.name)
        symbols = [symbol + name for name in self.symbols]
        aliases = [self._add_prefix(prefix, name) for name in self.aliases]
        factor = (Decimal(factor) * Decimal(self.factor)) ** Decimal(self.power)

        # Don't allow prefixed units to be prefixed again
        prefix_scale = PrefixScale.NONE

        # Return prefixed unit
        return Unit(name, self.category, symbols, aliases, factor,
                    self.power, self.offset, prefix_scale)

    def names(self) -> list[str]:
        """ Get a list of all unit names and symbols. """
        return [self.name] + self.symbols + self.aliases

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

    def __str__(self) -> str:
        symbols = f' ({", ".join(self.symbols)})' if self.symbols else ''
        return f'{self.name}{symbols}'

    def __repr__(self) -> str:
        args = ', '.join(repr(s) for s in self.__dict__.values())
        return (f'Unit({args})')
