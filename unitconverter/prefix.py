# Copyright (c) 2022-2023 Mike Cunningham

from unitconverter.units import Unit


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
    'si',       # generate SI prefixes (default)
    'all',      # generate SI prefixes and binary prefixes
    'binary',   # generate binary prefixes
    'decimal',  # generate decimal prefixes
    'both',     # generate decimal prefixes and binary prefixes
    'none',     # don't generate any prefixes
]


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

    raise ValueError(f'Unit {unit.name!r} does not support prefix {name!r}.')
