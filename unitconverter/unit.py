# Copyright (c) 2022-2023 Mike Cunningham

from decimal import Decimal, DecimalException
from unitconverter.prefixes import PrefixScaling


class Unit:
    """ A unit of measurement. """
    category = None

    def __init__(self,
                 name,
                 category,
                 symbols,
                 aliases,
                 factor,
                 power=1,
                 offset=0,
                 prefix_scaling=PrefixScaling.NONE,
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

            prefix_scaling (PrefixScaling, optional):
                prefix scaling option. Defaults to PrefixScaling.NONE.

            prefix_index (int, optional): i
                index of word to prefix. Defaults to -1 (last word).

        Raises:
            TypeError: if symbols or aliases is the wrong type.
            ValueError: if prefix_scaling or prefix_index is invalid.
        """
        self.name = name
        self.category = category
        self.symbols = symbols
        self.aliases = aliases

        self.factor = self._parse_decimal(factor)
        self.power = self._parse_decimal(power)
        self.offset = self._parse_decimal(offset)

        # Check if prefix scaling is valid
        try:
            self.prefix_scaling = PrefixScaling(prefix_scaling)
        except ValueError:
            raise ValueError(f'{prefix_scaling!r} is not a valid PrefixScaling option.')

        # Check if prefix index is valid
        last_index = len(name.split(' ')) - 1
        if prefix_index < -1 or prefix_index > last_index:
            raise ValueError(f'prefix index must be between -1 and {last_index}')

        self.prefix_index = prefix_index

    def get_names(self) -> list[str]:
        """ Return a list of all unit names and symbols. """
        return [self.name] + self.symbols + self.aliases

    def add_prefix(self, factor: str, symbol: str, prefix: str):
        """ Create a new unit by applying a prefix (scaling factor).

        Args:
            factor (str):
                multiplication factor.

            symbol (str):
                prefix symbol.

            prefix (str):
                prefix name.

        Returns:
            Unit: a new unit instance.
        """
        # Update names and factor
        name = self._add_prefix(prefix, self.name)
        symbols = [self._add_prefix(symbol, name) for name in self.symbols]
        aliases = [self._add_prefix(prefix, name) for name in self.aliases]
        factor = (Decimal(factor) * Decimal(self.factor)) ** Decimal(self.power)

        # Don't allow prefixed units to be prefixed again
        prefix_scaling = 'none'

        # Create a new prefixed unit
        return Unit(name, self.category, symbols, aliases, factor, self.power,
                    self.offset, prefix_scaling, self.prefix_index)

    def _add_prefix(self, prefix: str, name: str) -> str:
        """ Add a prefix to a string; i.e "kilo" + "metre"

        Args:
            prefix (str): the prefix string or character.
            name (str): the base name; i.e "metre"

        Raises:
            TypeError: if an argument is an invalid type.

        Returns:
            str: the prefixed name.
        """
        if not isinstance(prefix, str):
            raise TypeError('prefix must be a string.')

        if not isinstance(name, str):
            raise TypeError('name must be a string.')

        # Add prefix to the word at prefix index
        split = name.split(' ')
        split[self.prefix_index] = prefix + split[self.prefix_index]
        return ' '.join(split)

    def _parse_decimal(self, argument: Decimal | str) -> Decimal:
        """ Parse argument and return a Decimal. """
        try:
            return Decimal(argument)
        except DecimalException:
            raise ValueError(f'{self.name} passed an invalid decimal: {argument!r}')

    def __contains__(self, name: str) -> bool:
        """ Returns True if name matches one of the unit names. """
        return name == self.name or name in self.symbols or name in self.aliases

    def __str__(self) -> str:
        return f'{self.name}, {self.factor}, {self.symbols}, {self.aliases}'
