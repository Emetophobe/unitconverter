# Copyright (c) 2022-2023 Mike Cunningham


from enum import StrEnum
from unitconverter.exceptions import UnitError


class PrefixScale(StrEnum):
    """ Prefix scale determines how individual units are scaled.
    The default is PrefixScale.NONE but this can be overriden on a per-unit basis. """

    NONE = 'none'           # don't generate prefixes (default)
    ALL = 'all'             # generate SI prefixes and binary prefixes
    SI = 'si'               # generate SI prefixes
    BINARY = 'binary'       # generate binary prefixes
    DECIMAL = 'decimal'     # generate positive decimal prefixes (kilo to quetta)
    BOTH = 'both'           # generate decimal prefixes and binary prefixes


class Prefix:

    def __init__(self, factor, symbol, name) -> None:
        self.factor = factor
        self.symbol = symbol
        self.name = name

    def __iter__(self):
        yield self.factor
        yield self.symbol
        yield self.name

    def __repr__(self) -> str:
        return f'Prefix({self.factor!r}, {self.symbol!r}, {self.name!r})'

    def __str__(self) -> str:
        return self.name


# SI prefixes
SI_PREFIXES = [
    Prefix('1E-30', 'q', 'quecto'),
    Prefix('1E-27', 'r', 'ronto'),
    Prefix('1E-24', 'y', 'yocto'),
    Prefix('1E-21', 'z', 'zepto'),
    Prefix('1E-18', 'a', 'atto'),
    Prefix('1E-15', 'f', 'femto'),
    Prefix('1E-12', 'p', 'pico'),
    Prefix('1E-9', 'n', 'nano'),
    Prefix('1E-6', 'µ', 'micro'),
    Prefix('1E-3', 'm', 'milli'),
    Prefix('1E-2', 'c', 'centi'),
    Prefix('1E-1', 'd', 'deci'),
    Prefix('1E+1', 'da', 'deca'),
    Prefix('1E+2', 'h', 'hecto'),
    Prefix('1E+3', 'k', 'kilo'),
    Prefix('1E+6', 'M', 'mega'),
    Prefix('1E+9', 'G', 'giga'),
    Prefix('1E+12', 'T', 'tera'),
    Prefix('1E+15', 'P', 'peta'),
    Prefix('1E+18', 'E', 'exa'),
    Prefix('1E+21', 'Z', 'zetta'),
    Prefix('1E+24', 'Y', 'yotta'),
    Prefix('1E+27', 'R', 'ronna'),
    Prefix('1E+30', 'Q', 'quetta'),
]


# Decimal prefixes (kilo to quetta)
DECIMAL_PREFIXES = SI_PREFIXES[14:]


# Binary prefixes (i.e kibibyte to yobibyte)
BINARY_PREFIXES = [
    Prefix(2 ** 10, 'Ki', 'kibi'),
    Prefix(2 ** 20, 'Mi', 'mebi'),
    Prefix(2 ** 30, 'Gi', 'gibi'),
    Prefix(2 ** 40, 'Ti', 'tebi'),
    Prefix(2 ** 50, 'Pi', 'pebi'),
    Prefix(2 ** 60, 'Ei', 'exbi'),
    Prefix(2 ** 70, 'Zi', 'zebi'),
    Prefix(2 ** 80, 'Yi', 'yobi'),
]


def get_prefixes(scale: PrefixScale) -> list[tuple]:
    """ Get a list of supported prefixes.

    Args:
        scale (PrefixScaling): the prefix scale.

    Raises:
        ValueError: if prefix scale is invalid.

    Returns:
        list[tuple]: a list of prefixes, or an empty list.
    """
    scale = PrefixScale(scale)
    if scale == PrefixScale.NONE:
        return []
    elif scale == PrefixScale.SI:
        return SI_PREFIXES
    elif scale == PrefixScale.ALL:
        return SI_PREFIXES + BINARY_PREFIXES
    elif scale == PrefixScale.BOTH:
        return DECIMAL_PREFIXES + BINARY_PREFIXES
    elif scale == PrefixScale.BINARY:
        return BINARY_PREFIXES
    elif scale == PrefixScale.DECIMAL:
        return DECIMAL_PREFIXES
    else:
        raise UnitError(f'Unsupported prefix scale: {scale}')
