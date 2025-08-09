# Copyright (c) 2022-2025 Mike Cunningham


from decimal import Decimal

from unitconverter.exceptions import ConverterError
from unitconverter.formatting import parse_decimal
from unitconverter.models.definition import Definition


# List of valid prefix options
PREFIX_OPTIONS = [
    "none",         # don"t generate prefixes (default)
    "metric",       # metric prefixes
    "binary",       # binary prefixes
    "bit",          # bit prefixes
    "byte",         # bit prefixes and binary prefixes
    "all",          # all SI prefixes and binary prefixes
]


class Prefix:
    """ A Prefix can be combined with a Definition to make a prefixed definition. """

    def __init__(self, name: str, symbol: str, factor: Decimal | int | str) -> None:
        """ Create a new prefix.

        Args:
            name (str): The prefix name.
            symbol (str): The prefix symbol.
            factor (Decimal | int | str): The multiplication factor.
        """
        self.name = name
        self.symbol = symbol
        self.factor = parse_decimal(factor)

    def __add__(self, other: Definition) -> Definition:
        """ Add a prefix to a unit definition to create a new prefixed definition.

        Args:
            other (Definition): The unit definition to prefix.

        Raises:
            ConverterError: If the definition is invalid.

        Returns:
            Definition: A new prefixed definition.
        """

        if not isinstance(other, Definition):
            raise ConverterError(f"Prefix {self.name} can only be added to a Definition")

        # Create prefixed unit names and factor
        name = self.name + other.name
        symbols = [self.symbol + symbol for symbol in other.symbols]
        aliases = [self.name + alias for alias in other.aliases]
        factor = self.factor * other.factor

        # Make sure prefix=None so that the unit can't be prefixed again
        return Definition(name, symbols, aliases, factor, other.dimen, prefix=None)

    def __repr__(self) -> str:
        return f"Prefix({self.name!r}, {self.symbol!r}, {self.factor!r})"

    def __str__(self):
        return self.name


# SI prefixes
SI_PREFIXES = [
    Prefix("quecto", "q", "1E-30"),
    Prefix("ronto", "r", "1E-27"),
    Prefix("yocto", "y", "1E-24"),
    Prefix("zepto", "z", "1E-21"),
    Prefix("atto", "a", "1E-18"),
    Prefix("femto", "f", "1E-15"),
    Prefix("pico", "p", "1E-12"),
    Prefix("nano", "n", "1E-9"),
    Prefix("micro", "mu", "1E-6"),
    Prefix("milli", "m", "1E-3"),
    Prefix("centi", "c", "1E-2"),
    Prefix("deci", "d", "1E-1"),
    Prefix("deca", "da", "1E+1"),
    Prefix("hecto", "h", "1E+2"),
    Prefix("kilo", "k", "1E+3"),
    Prefix("mega", "M", "1E+6"),
    Prefix("giga", "G", "1E+9"),
    Prefix("tera", "T", "1E+12"),
    Prefix("peta", "P", "1E+15"),
    Prefix("exa", "E", "1E+18"),
    Prefix("zetta", "Z", "1E+21"),
    Prefix("yotta", "Y", "1E+24"),
    Prefix("ronna", "R", "1E+27"),
    Prefix("quetta", "Q", "1E+30"),
]

# Binary prefixes (used by kibibyte to yobibyte)
BINARY_PREFIXES = [
    Prefix("kibi", "Ki", 2 ** 10),
    Prefix("mebi", "Mi", 2 ** 20),
    Prefix("gibi", "Gi", 2 ** 30),
    Prefix("tebi", "Ti", 2 ** 40),
    Prefix("pebi", "Pi", 2 ** 50),
    Prefix("exbi", "Ei", 2 ** 60),
    Prefix("zebi", "Zi", 2 ** 70),
    Prefix("yobi", "Yi", 2 ** 80),
]

# Bit prefixes includes metric prefixes "kilo" to "quetta" (used by the bit unit)
BIT_PREFIXES = METRIC_PREFIXES[14:]

# Byte prefixes includes bit prefixes and binary prefixes (used by the byte unit)
BYTE_PREFIXES = BIT_PREFIXES + BINARY_PREFIXES

# All prefixes includes all metric and binary prefixes
ALL_PREFIXES = SI_PREFIXES + BINARY_PREFIXES


def get_prefixes(option: str | None) -> list[Prefix]:
    """ Get a list of supported prefixes based on the prefix option.

    Args:
        option (str | None): The prefix setting (i.e "metric")

    Raises:
        ConverterError: If the prefix option is invalid.

    Returns:
        list[Prefix]: The list of supported prefixes, or an empty list if not supported.
    """
    if option is None or option == "none":
        return []
    elif option == "si":
        return SI_PREFIXES
    elif option == "binary":
        return BINARY_PREFIXES
    elif option == "bit":
        return BIT_PREFIXES
    elif option == "byte":
        return BYTE_PREFIXES
    elif option == "all":
        return ALL_PREFIXES
    else:
        raise ConverterError(f"{option} is not a valid prefix option")
