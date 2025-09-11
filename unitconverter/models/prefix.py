# Copyright (c) 2022-2025 Mike Cunningham
# https://www.github.com/emetophobe/unitconverter


from fractions import Fraction
from unitconverter.utils import parse_fraction


class Prefix:
    """ A prefix can be added to a unit that supports prefixing. """

    def __init__(self, name: str, symbol: str, factor: Fraction | str | int) -> None:
        self.name = name
        self.symbol = symbol
        self.factor = parse_fraction(factor)

    def __repr__(self) -> str:
        return f"Prefix({self.name!r}, {self.symbol!r}, {self.factor!r})"

    def __str__(self):
        return self.name


# SI prefixes
metric_prefixes = [
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

# Binary prefixes (used by bit and byte units)
binary_prefixes = [
    Prefix("kilo", "k", "1E+3"),
    Prefix("mega", "M", "1E+6"),
    Prefix("giga", "G", "1E+9"),
    Prefix("tera", "T", "1E+12"),
    Prefix("peta", "P", "1E+15"),
    Prefix("exa", "E", "1E+18"),
    Prefix("zetta", "Z", "1E+21"),
    Prefix("yotta", "Y", "1E+24"),
    Prefix("kibi", "Ki", 2 ** 10),
    Prefix("mebi", "Mi", 2 ** 20),
    Prefix("gibi", "Gi", 2 ** 30),
    Prefix("tebi", "Ti", 2 ** 40),
    Prefix("pebi", "Pi", 2 ** 50),
    Prefix("exbi", "Ei", 2 ** 60),
    Prefix("zebi", "Zi", 2 ** 70),
    Prefix("yobi", "Yi", 2 ** 80),
]


def get_prefixes(option: str | None) -> list[Prefix]:
    """ Get a list of supported prefixes based on the prefix option. """
    if option is None:
        return []
    elif option == "metric":
        return metric_prefixes
    elif option == "binary":
        return binary_prefixes
    else:
        raise TypeError(f"{option!r} is not a valid prefix option")
