# Copyright (c) 2022-2023 Mike Cunningham

from enum import StrEnum


class PrefixScaling(StrEnum):
    """ A unit supports one of the prefix scaling options. """
    NONE = 'none'           # don't generate prefixes (default)
    ALL = 'all'             # generate SI prefixes and binary prefixes
    SI = 'si'               # generate SI prefixes
    BINARY = 'binary'       # generate binary prefixes
    DECIMAL = 'decimal'     # generate positive decimal prefixes (kilo to quetta)
    BOTH = 'both'           # generate decimal prefixes and binary prefixes


def get_prefixes(option: PrefixScaling) -> list[tuple]:
    """ Get a list of prefixes based on the prefix option (see `PrefixScaling`).

    Args:
        prefix_option (str): the prefix option.

    Raises:
        ValueError: if the prefix_option is invalid.

    Returns:
        list[tuple]: a list of prefixes.
    """
    option = PrefixScaling(option)
    if option == PrefixScaling.NONE:
        return []
    elif option == PrefixScaling.SI:
        return SI_PREFIXES
    elif option == PrefixScaling.ALL:
        return SI_PREFIXES + BINARY_PREFIXES
    elif option == PrefixScaling.BOTH:
        return DECIMAL_PREFIXES + BINARY_PREFIXES
    elif option == PrefixScaling.BINARY:
        return BINARY_PREFIXES
    elif option == PrefixScaling.DECIMAL:
        return DECIMAL_PREFIXES
    else:
        raise ValueError(f'Unsupported prefix option: {option}')


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
