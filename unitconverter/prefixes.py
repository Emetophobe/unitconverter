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
        """ Create a new prefixed unit. """

        # Get supported prefixes
        prefixes = get_prefixes(unit.prefix_scale)

        if not prefixes:
            raise UnitError(f"Unit {unit} doesn't support prefix scaling")

        if self not in prefixes:
            raise UnitError(f"Unit {unit} doesn't support {self.name} prefix")

        # Create new unit names and factor
        name = self._add_prefix(self.name, unit.name)
        symbol = self._add_prefix(self.symbol, unit.symbol)
        plural = self._add_prefix(self.name, unit.plural)
        aliases = [self._add_prefix(self.name, alias) for alias in unit.aliases]

        factor = (Decimal(unit.factor) * self.factor) ** unit.power

        # Create a new prefixed unit
        return Unit(name, unit.category, symbol, plural, aliases, factor, unit.power,
                    None, unit.prefix_exclude, True)

    def _add_prefix(self, prefix: str, name: str) -> str:
        """ Add a prefix to a unit name or alias. """
        # Special case for square and cubic units
        if name.startswith('square '):
            return name[:7] + prefix + name[7:]
        elif name.startswith('cubic '):
            return name[:6] + prefix + name[6:]

        # Prefix other units normally
        return prefix + name

    def __repr__(self) -> str:
        return f'Prefix({self.name!r}, {self.symbol!r}, {self.factor!r})'

    def __str__(self):
        return self.name


def get_prefixes(scale: str) -> list[Prefix]:
    """ Get a list of supported prefixes based on the prefix scale. """
    if not scale or scale == 'none':
        return []

    if scale == 'si':
        return SI_PREFIXES
    elif scale == 'binary':
        return BINARY_PREFIXES
    elif scale == 'bit':
        return BIT_PREFIXES
    elif scale == 'byte':
        return BYTE_PREFIXES
    elif scale == 'all':
        return ALL_PREFIXES
    else:
        raise UnitError(f'Unsupported prefix scale: {scale}')


def create_prefixed_units(unit: Unit):
    """ Create a list of prefixed units from a source unit. """
    units = []
    for prefix in get_prefixes(unit.prefix_scale):
        if prefix.name not in unit.prefix_exclude:
            units.append(prefix + unit)

    return units


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
    Prefix('micro', 'mu', '1E-6'),
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
