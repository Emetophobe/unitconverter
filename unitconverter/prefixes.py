# Copyright (c) 2022-2023 Mike Cunningham


from decimal import Decimal

from unitconverter.exceptions import UnitError
from unitconverter.unit import Unit


class Prefix:
    """ A Prefix can be added to a Unit that supports prefix scaling. """

    def __init__(self, name: str, symbol: str, factor: Decimal | int | str) -> None:
        self.name = name
        self.symbol = symbol
        self.factor = Decimal(factor)

    def __add__(self, unit: Unit) -> Unit:
        return add_prefix(self, unit)

    def __repr__(self) -> str:
        return f'Prefix({self.name!r}, {self.symbol!r}, {self.factor!r})'

    def __str__(self):
        return self.name


# List of valid prefix options
PREFIX_OPTIONS = [
    'none',         # don't generate prefixes (default)
    'si',           # SI prefixes
    'binary',       # binary prefixes
    'bit',          # bit prefixes 'kilo' to 'quetta'
    'byte',         # bit prefixes and binary prefixes
    'all',          # all SI prefixes and binary prefixes
]


# SI prefixes
SI_PREFIXES = [
    Prefix('quecto', 'q', '1E-30'),
    Prefix('ronto', 'r', '1E-27'),
    Prefix('yocto', 'y', '1E-24'),
    Prefix('zepto', 'z', '1E-21'),
    Prefix('atto', 'a', '1E-18'),
    Prefix('femto', 'f', '1E-15'),
    Prefix('pico', 'p', '1E-12'),
    Prefix('nano', 'n', '1E-9'),
    Prefix('micro', 'µ', '1E-6'),
    Prefix('milli', 'm', '1E-3'),
    Prefix('centi', 'c', '1E-2'),
    Prefix('deci', 'd', '1E-1'),
    Prefix('deca', 'da', '1E+1'),
    Prefix('hecto', 'h', '1E+2'),
    Prefix('kilo', 'k', '1E+3'),
    Prefix('mega', 'M', '1E+6'),
    Prefix('giga', 'G', '1E+9'),
    Prefix('tera', 'T', '1E+12'),
    Prefix('peta', 'P', '1E+15'),
    Prefix('exa', 'E', '1E+18'),
    Prefix('zetta', 'Z', '1E+21'),
    Prefix('yotta', 'Y', '1E+24'),
    Prefix('ronna', 'R', '1E+27'),
    Prefix('quetta', 'Q', '1E+30'),
]

# Binary prefixes (i.e kibibyte to yobibyte)
BINARY_PREFIXES = [
    Prefix('kibi', 'Ki', 2 ** 10),
    Prefix('mebi', 'Mi', 2 ** 20),
    Prefix('gibi', 'Gi', 2 ** 30),
    Prefix('tebi', 'Ti', 2 ** 40),
    Prefix('pebi', 'Pi', 2 ** 50),
    Prefix('exbi', 'Ei', 2 ** 60),
    Prefix('zebi', 'Zi', 2 ** 70),
    Prefix('yobi', 'Yi', 2 ** 80),
]

# Bit prefixes = SI prefixes kilo to quetta (used by the bit unit)
BIT_PREFIXES = SI_PREFIXES[14:]

# Byte prefixes = bit prefixes and binary prefixes (used by the byte unit)
BYTE_PREFIXES = BIT_PREFIXES + BINARY_PREFIXES

# All prefixes = SI prefixes and binary prefixes
ALL_PREFIXES = SI_PREFIXES + BINARY_PREFIXES


def valid_scale(scale: str) -> bool:
    """ True if scale is a valid prefix option. """
    return scale is None or scale in PREFIX_OPTIONS


def add_prefix(prefix: Prefix, unit: Unit) -> Unit:
    """ Create a new prefixed unit. """
    if not isinstance(prefix, Prefix):
        raise UnitError(f'{prefix} is not a valid Prefix')

    if not isinstance(unit, Unit):
        raise UnitError(f'{unit!r} is not a valid Unit')

    # Get list of supported prefixes
    prefixes = get_prefixes(unit)

    if not prefixes:
        raise UnitError(f"Unit {unit} doesn't support prefix scaling")

    if prefix not in prefixes:
        raise UnitError(f"Unit {unit} doesn't support {prefix} prefix")

    # Create new unit names and factor
    name = _prefix_name(prefix.name, unit.name)
    symbols = [prefix.symbol + symbol for symbol in unit.symbols]
    aliases = [_prefix_name(prefix.name, alias) for alias in unit.aliases]
    factor = (Decimal(unit.factor) * prefix.factor) ** unit.prefix_power

    # Don't allow prefixed units to be prefixed again
    prefix_scale = None

    # Create a new prefixed unit
    unit = Unit(name, unit.category, symbols, aliases, factor, prefix_scale,
                unit.prefix_power, unit.prefix_exclude)
    unit.prefixed = True

    return unit


def get_prefixes(unit: Unit) -> list[Prefix]:
    """ Get a list of supported unit prefixes. Returns an empty list if unsupported. """
    scale = unit.prefix_scale

    if not scale or scale == 'none':
        return []

    if scale == 'si':
        prefixes = SI_PREFIXES
    elif scale == 'binary':
        prefixes = BINARY_PREFIXES
    elif scale == 'bit':
        prefixes = BIT_PREFIXES
    elif scale == 'byte':
        prefixes = BYTE_PREFIXES
    elif scale == 'all':
        prefixes = ALL_PREFIXES
    else:
        raise UnitError(f'Unsupported prefix scale: {scale}')

    # Filter list based on unit prefix exclude list
    return [prefix for prefix in prefixes if prefix.name not in unit.prefix_exclude]


def create_prefixed_units(unit: Unit):
    """ Create a list of prefixed units from a source unit. """
    return [add_prefix(prefix, unit) for prefix in get_prefixes(unit)]


def _prefix_name(prefix: str, name: str) -> str:
    """ Add a prefix to a unit name or alias. """
    # Special case for square and cubic units
    if name.startswith('square '):
        return name[:7] + prefix + name[7:]
    elif name.startswith('cubic '):
        return name[:6] + prefix + name[6:]

    # Prefix other units normally
    return prefix + name
