# Copyright (c) 2022-2023 Mike Cunningham


from decimal import Decimal
from typing import Self

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
                 prefix_scale=PrefixScale.NONE,
                 prefix_index=0):
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

            prefix_index (int, optional):
                index of word to prefix. Defaults to 0 (prefix first word).

        Raises:
            TypeError: if an argument is the wrong type.
            ValueError: if an argument is the wrong value.
        """
        self.name = name
        self.category = category
        self.symbols = symbols
        self.aliases = aliases

        self.factor = parse_decimal(factor, f'{name!r} has an invalid factor.')
        self.power = parse_decimal(power, f'{name!r} has an invalid power.')
        self.offset = parse_decimal(offset, f'{name!r} has an invalid offset.')

        self._parse_scale(prefix_scale)
        self._parse_index(prefix_index)

    def get_names(self) -> list[str]:
        """ Return a list of all unit names and symbols. """
        return [self.name] + self.symbols + self.aliases

    def scale(self, factor: Decimal | int | str, symbol: str, prefix: str) -> Self:
        """ Create a new unit by applying a prefix scaling factor.

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

        # Update all unit names and calculate new factor
        symbols = [symbol + name for name in self.symbols]
        name = self._add_prefix(prefix, self.name)
        aliases = [self._add_prefix(prefix, name) for name in self.aliases]
        factor = (Decimal(factor) * Decimal(self.factor)) ** Decimal(self.power)

        # Don't allow prefixed units to be prefixed again
        prefix_scale = PrefixScale.NONE

        # Return prefixed unit
        return Unit(name, self.category, symbols, aliases, factor, self.power,
                    self.offset, prefix_scale, self.prefix_index)

    def _add_prefix(self, prefix: str, name: str) -> str:
        """ Add a prefix by splitting a string and inserting at prefix_index. """
        split = name.split(' ')
        split[self.prefix_index] = prefix + split[self.prefix_index]
        return ' '.join(split)

    def _parse_scale(self, prefix_scale: PrefixScale) -> None:
        """ Check if prefix_scale is valid or throw a UnitError. """
        try:
            self.prefix_scale = PrefixScale(prefix_scale)
        except ValueError:
            msg = f'Unit {self.name!r} has an invalid prefix scale: {prefix_scale}'
            raise UnitError(msg)

        self._prefix_scale = prefix_scale

    def _parse_index(self, prefix_index: int) -> None:
        """ Check if prefix_index is valid or throw a UnitError. """
        for alias in [self.name] + self.aliases:  # don't check symbols
            last_index = len(alias.split(' ')) - 1
            if prefix_index < -1 or prefix_index > last_index:
                raise UnitError(f'Unit {self.name!r} has an invalid prefix index:'
                                f' {prefix_index} ({alias!r})')

        self.prefix_index = prefix_index

    def __contains__(self, name: str) -> bool:
        """ Returns True if name matches one of the unit names. """
        return name == self.name or name in self.symbols or name in self.aliases

    def __str__(self) -> str:
        return f'{self.name}, ({", ".join(self.symbols)})'
