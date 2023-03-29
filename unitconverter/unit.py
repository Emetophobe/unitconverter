# Copyright (c) 2022-2023 Mike Cunningham


from decimal import Decimal, DecimalException
from typing import Self
from unitconverter.exceptions import UnitError
from unitconverter.prefixes import PrefixScale, get_prefixes


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
                 prefix_index=-1):
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

            prefix_index (int, optional): i
                index of word to prefix. Defaults to -1 (last word).

        Raises:
            TypeError: if an argument is the wrong type.
            ValueError: if an argument is the wrong value.
        """
        self.name = name
        self.category = category
        self.symbols = symbols
        self.aliases = aliases

        self.factor = parse_decimal(factor, f'{name!r} has an invalid factor.')
        self.power = parse_decimal(power,  f'{name!r} has an invalid power.')
        self.offset = parse_decimal(offset,  f'{name!r} has an invalid offset.')

        # Check if prefix scale is valid
        try:
            self.prefix_scale = PrefixScale(prefix_scale)
        except ValueError:
            raise ValueError(f'{name!r} has an invalid prefix scale: {prefix_scale}')

        # Check if prefix index is valid
        last_index = len(name.split(' ')) - 1
        if prefix_index < -1 or prefix_index > last_index:
            raise ValueError(f'{name!r} has an invalid prefix index: {prefix_index}')

        self.prefix_index = prefix_index

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
        # Prefix names and symbols
        name = self._add_prefix(prefix, self.name)
        symbols = [self._add_prefix(symbol, name) for name in self.symbols]
        aliases = [self._add_prefix(prefix, name) for name in self.aliases]

        # Scale factor
        factor = (Decimal(factor) * Decimal(self.factor)) ** Decimal(self.power)

        # Don't allow prefixed units to be prefixed again
        prefix_scale = 'none'

        # Return prefixed unit
        return Unit(name, self.category, symbols, aliases, factor, self.power,
                    self.offset, prefix_scale, self.prefix_index)

    def _add_prefix(self, prefix: str, name: str) -> str:
        """ Add a prefix to a string using the specified prefix_index (word index). """
        split = name.split(' ')
        split[self.prefix_index] = prefix + split[self.prefix_index]
        return ' '.join(split)

    def __contains__(self, name: str) -> bool:
        """ Returns True if name matches one of the unit names. """
        return name == self.name or name in self.symbols or name in self.aliases

    def __str__(self) -> str:
        return f'{self.name}, ({", ".join(self.symbols)})'


def apply_prefix(prefix: str, unit: Unit) -> Unit:
    """ Create a new unit by applying a prefix.

    Args:
        prefix (str): prefix name or symbol.
        unit (Unit): unit to prefix.

    Raises:
        UnitError: if unit could not be prefixed.

    Returns:
        Unit: a new prefixed unit.
    """
    # Get prefix table from unit prefix option
    prefixes = get_prefixes(unit.prefix_scale)
    if not prefixes:
        raise UnitError(f'Unit {unit.name!r} does not support prefix scaling.')

    # Create a new unit from prefix
    for factor, symbol, name in prefixes:
        if prefix in (symbol, name):
            return unit.scale(factor, symbol, name)

    raise UnitError(f'Unit {unit.name!r} does not support prefix {prefix!r}.')


def parse_decimal(value: Decimal | int | str, msg: str = None) -> Decimal:
    """ Parse value and return a Decimal. Raises ValueError if value is invalid. """
    try:
        return Decimal(value)
    except DecimalException:
        raise ValueError(msg or f'{value!r} is not a valid Decimal')
