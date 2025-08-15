# Copyright (c) 2022-2025 Mike Cunningham
# https://www.github.com/emetophobe/unitconverter


from decimal import Decimal, ROUND_HALF_UP


def format_decimal(value: Decimal,
                   precision: int | None = None,
                   exponent: bool = False,
                   separators: bool = False) -> str:
    """ Format a decimal into a string for display.

    Parameters
    ----------
    number : `Decimal`
        The decimal to format.

    precision : `int` | `None`, optional
        Set rounding precision, by default None

    exponent : `bool`, optional
        Show scientific E notation, by default False

    separators : `bool`, optional
        Show thousands separators (commas), by default False

    Returns
    -------
    str
        The formatted string.
    """
    if precision is not None:
        print(value)
        value = value.quantize(Decimal(10) ** -precision, ROUND_HALF_UP)
        print(value)

    precision_format = f".{precision}" if precision is not None else ""
    if exponent:
        return f"{value:{precision_format}E}"

    comma = "," if separators else ""
    return f"{value:{comma}{precision_format}f}"


def format_name(units: dict[str, int], sort_keys: bool = False) -> str:
    """ Format unit name without divisor (i.e "metre*second^-1") """
    numers = []
    for unit, exp in sorted(units.items()) if sort_keys else units.items():
        numers.append(format_exponent(unit, exp))

    return "*".join(numers)


def format_display_name(units: dict[str, int], sort_keys: bool = False) -> str:
    """ Format unit display name with divisor (i.e "metre/second") """
    numers = []
    denoms = []

    for unit, exp in sorted(units.items()) if sort_keys else units.items():
        if exp > 0:
            numers.append(format_exponent(unit, exp))
        else:
            denoms.append(format_exponent(unit, -exp))

    if not numers:
        return format_name(units, sort_keys)

    elif not denoms:
        return "*".join(numers)

    return "*".join(numers) + "/" + "*".join(denoms)


def format_exponent(name: str, exponent: int) -> str:
    """ Format unit name with optional exponent. """
    if exponent == 1:
        return name
    else:
        return f"{name}^{exponent}"


def format_type(obj: object) -> str:
    """ Get a nice string representation of an object. """
    return type(obj).__name__
