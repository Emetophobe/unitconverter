# Copyright (c) 2022-2023 Mike Cunningham

from decimal import Decimal
from typing import Union


# SI prefixes
SI_PREFIXES = [
    ('1E-30', 'q', 'quecto'),
    ('1E-27', 'r', 'ronto'),
    ('1E-24', 'y', 'yocto'),
    ('1E-21', 'z', 'zepto'),
    ('1E-18', 'a', 'atto'),
    ('1E-15', 'f', 'femto'),
    ('1E-12', 'p', 'pico'),
    ('1E-9', 'n', 'nano'),
    ('1E-6', 'µ', 'micro'),
    ('1E-3', 'm', 'milli'),
    ('1E-2', 'c', 'centi'),
    ('1E-1', 'd', 'deci'),
    ('1E+1', 'da', 'deca'),
    ('1E+2', 'h', 'hecto'),
    ('1E+3', 'k', 'kilo'),
    ('1E+6', 'M', 'mega'),
    ('1E+9', 'G', 'giga'),
    ('1E+12', 'T', 'tera'),
    ('1E+15', 'P', 'peta'),
    ('1E+18', 'E', 'exa'),
    ('1E+21', 'Z', 'zetta'),
    ('1E+24', 'Y', 'yotta'),
    ('1E+27', 'R', 'ronna'),
    ('1E+30', 'Q', 'quetta'),
]

# Decimal prefixes (kilo to quetta)
DECIMAL_PREFIXES = [
    ('1E+3', 'k', 'kilo'),
    ('1E+6', 'M', 'mega'),
    ('1E+9', 'G', 'giga'),
    ('1E+12', 'T', 'tera'),
    ('1E+15', 'P', 'peta'),
    ('1E+18', 'E', 'exa'),
    ('1E+21', 'Z', 'zetta'),
    ('1E+24', 'Y', 'yotta'),
    ('1E+27', 'R', 'ronna'),
    ('1E+30', 'Q', 'quetta'),
]

# binary prefixes (i.e kibibyte to yobibyte)
BINARY_PREFIXES = [
    (2 ** 10, 'Ki', 'kibi'),
    (2 ** 20, 'Mi', 'mebi'),
    (2 ** 30, 'Gi', 'gibi'),
    (2 ** 40, 'Ti', 'tebi'),
    (2 ** 50, 'Pi', 'pebi'),
    (2 ** 60, 'Ei', 'exbi'),
    (2 ** 70, 'Zi', 'zebi'),
    (2 ** 80, 'Yi', 'yobi'),
]

# A Unit has one of the following prefix options:
PREFIX_OPTIONS = [
    'none',     # don't generate prefixes (default)
    'all',      # generate SI prefixes and binary prefixes
    'si',       # generate SI prefixes
    'binary',   # generate binary prefixes
    'decimal',  # generate decimal prefixes (kilo to quetta)
    'both',     # generate decimal prefixes and binary prefixes
]


class Unit:
    """ A unit of measurement. """

    def __init__(self,
                 name,
                 factor,
                 symbols=None,
                 aliases=None,
                 power='1',
                 offset='0',
                 category=None,
                 prefix_scaling='none',
                 prefix_index=-1):
        """ Initialize unit.

        Args:
            name (str): unit name.

            factor (str | Decimal):
                unit conversion factor.

            symbols (str | list, optional):
                unit symbols. Defaults to None.

            aliases (str | list, optional):
                unit aliases. Defaults to None.

            power (str | Decimal, optional):
                optional power. Defaults to '1'.

            offset (str | Decimal, optional):
                optional offset. Defaults to '0'.

            category (str, optional):
                unit category. Defaults to None. This is set automatically the
                first time get_units() is called.

            prefix_scaling (str, optional):
                prefix scaling option. Defaults to 'none'.

            prefix_index (int, optional): i
                index of word to prefix. Defaults to -1 (last word).

        Raises:
            TypeError: if symbols or aliases is the wrong type.
            ValueError: if prefix_scaling or prefix_index is invalid.
        """
        self.name = name
        self.symbols = self._parse_string_list(symbols)
        self.aliases = self._parse_string_list(aliases)
        self.factor = Decimal(factor)
        self.power = Decimal(power)
        self.offset = Decimal(offset)
        self.category = category

        # Check if prefix scaling is valid
        if prefix_scaling is not None and prefix_scaling not in PREFIX_OPTIONS:
            raise ValueError(f'Unsupported prefix option: {prefix_scaling}')

        # Check if prefix index is valid
        last_index = len(name.split(' ')) - 1
        if prefix_index < -1 or prefix_index > last_index:
            raise ValueError(f'prefix index must be between -1 and {last_index}')

        self.prefix_scaling = prefix_scaling
        self.prefix_index = prefix_index

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
        factor = Decimal(factor) * Decimal(self.factor)

        # Don't allow prefixed units to be prefixed again
        prefix_scaling = 'none'

        # Create new unit
        return Unit(name,
                    factor=Decimal(factor) ** self.power,
                    symbols=symbols,
                    aliases=aliases,
                    power=self.power,
                    offset=self.offset,
                    category=self.category,
                    prefix_scaling=prefix_scaling,
                    prefix_index=self.prefix_index)

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

    def _parse_string_list(self, argument: Union[str, list[str], None]) -> list[str]:
        """ Parse argument and return a list of strings.

        Args:
            argument (str | list[str] | None): a str, list of str, or None.

        Raises:
            TypeError: if the argument is an invalid type.

        Returns:
            list[str]: a list of strings, or an empty list.
        """
        if not argument:
            return []
        elif isinstance(argument, str):
            return [argument]
        elif isinstance(argument, list):
            return argument
        else:
            raise TypeError('argument must be a str, list, or None')

    def __contains__(self, name: str) -> bool:
        """ Returns True if name matches one of the unit names. """
        return name == self.name or name in self.symbols or name in self.aliases

    def __str__(self) -> str:
        return f'{self.name}, {self.factor}, {self.symbols}, {self.aliases}'


def get_prefixes(prefix_option: str) -> list[tuple]:
    """ Get a list of prefixes based on the prefix option (see `PREFIX_OPTIONS`).

    Args:
        prefix_option (str): the prefix option.

    Raises:
        ValueError: if the prefix_option is invalid.

    Returns:
        list[tuple]: a list of prefixes.
    """
    if prefix_option is None or prefix_option == 'none':
        return []
    elif prefix_option == 'si':
        return SI_PREFIXES
    elif prefix_option == 'all':
        return SI_PREFIXES + BINARY_PREFIXES
    elif prefix_option == 'both':
        return DECIMAL_PREFIXES + BINARY_PREFIXES
    elif prefix_option == 'binary':
        return BINARY_PREFIXES
    elif prefix_option == 'decimal':
        return DECIMAL_PREFIXES
    else:
        raise ValueError(f'Unsupported prefix option: {prefix_option}')


def apply_prefix(prefix: str, unit: Unit) -> Unit:
    """ Apply prefix to a unit and return a new unit.

    Args:
        prefix (str): The prefix name or symbol.
        unit (Unit): the base unit.

    Raises:
        ValueError: if an argument is invalid.

    Returns:
        Unit: a new prefixed unit.
    """
    # Get prefix table from unit scaling option
    prefixes = get_prefixes(unit.prefix_scaling)
    if not prefixes:
        raise ValueError(f'Unit {unit.name!r} does not support prefix scaling.')

    # Create a new unit from prefix
    for factor, symbol, name in prefixes:
        if prefix in (symbol, name):
            return unit.add_prefix(factor, symbol, name)

    raise ValueError(f'Unit {unit.name!r} does not support prefix {prefix!r}.')
