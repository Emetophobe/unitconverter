# Copyright (c) 2022-2023 Mike Cunningham


from decimal import Decimal

from unitconverter.exceptions import DefinitionError
from unitconverter.misc import parse_decimal


class UnitDef:
    """ A unit definition is used to define a unit in the Registry.

        Once a definition has been added to the registry a Unit can
        be retrieved by calling Registry.get_unit("name").

    """

    def __init__(self,
                 name: str,
                 category: str,
                 symbols: list[str] = None,
                 aliases: list[str] = None,
                 factor: Decimal | int | str = 1,
                 prefix_scale: str = None,
                 is_prefixed: bool = False
                 ) -> None:
        """ Initialize unit definition. """
        self.name = name
        self.category = category
        self.symbols = symbols or [name]
        self.aliases = aliases or [name]

        self.factor = parse_decimal(factor)

        self.prefix_scale = prefix_scale
        self.is_prefixed = is_prefixed

    def names(self) -> set[str]:
        """ Return a set of unique unit names used to identify this unit. """
        return set([self.name] + self.symbols + self.aliases)

    def __str__(self) -> str:
        return self.name


class Prefix:
    """ A Prefix can be added to a unit definition. """

    def __init__(self, name: str, symbol: str, factor: Decimal | int | str) -> None:
        self.name = name
        self.symbol = symbol
        self.factor = Decimal(factor)

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
        raise DefinitionError(f'Invalid prefix scale: {scale}')


def prefix_definition(prefix: Prefix, unitdef: UnitDef) -> UnitDef:
    """ Create a new prefixed unit definition. """
    if not isinstance(prefix, Prefix):
        raise DefinitionError(f'Invalid prefix: {prefix}!r')

    if not isinstance(unitdef, UnitDef):
        raise DefinitionError(f'Invalid definition: {unitdef!r}')

    # Get supported prefixes
    prefixes = get_prefixes(unitdef.prefix_scale)

    if not prefixes:
        raise DefinitionError(f"{unitdef} doesn't support prefix scaling")

    if prefix not in prefixes:
        raise DefinitionError(f"{unitdef} doesn't support {prefix.name} prefix")

    # Create new unit names and factor
    name = _prefix_name(prefix.name, unitdef.name)
    symbols = [_prefix_name(prefix.symbol, symbol) for symbol in unitdef.symbols]
    aliases = [_prefix_name(prefix.name, alias) for alias in unitdef.aliases]
    factor = (Decimal(unitdef.factor) * prefix.factor)

    # Create a new prefixed definition
    return UnitDef(name, unitdef.category, symbols, aliases, factor, None, True)


def create_definitions(unitdef: UnitDef) -> list[UnitDef]:
    """ Create a list of prefixed definitions from a source definition. """
    unitdefs = []

    for prefix in get_prefixes(unitdef.prefix_scale):
        unitdefs.append(prefix_definition(prefix, unitdef))

    return unitdefs


def _prefix_name(prefix: str, name: str) -> str:
    """ Add a prefix to a unit name, symbol, or alias. """
    if name.startswith('square '):
        return name[:7] + prefix + name[7:]
    elif name.startswith('cubic '):
        return name[:6] + prefix + name[6:]

    return prefix + name
