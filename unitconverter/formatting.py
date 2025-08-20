# Copyright (c) 2022-2025 Mike Cunningham
# https://www.github.com/emetophobe/unitconverter


import logging

from decimal import Decimal, DecimalException, ROUND_HALF_UP


def format_decimal(value: Decimal,
                   precision: int | None = None,
                   normalize: bool = False,
                   exponent: bool = False,
                   separators: bool = False) -> str:
    """ Format a decimal into a string for display.

    If exponent is True the separators argument is ignored.

    Parameters
    ----------
    number : Decimal
        The decimal to format.

    precision : int | None, optional
        Set rounding precision, by default None

    normalize : bool, optional
        Normalize value by stripping the rightmost trailing zeros, by default False

    exponent : bool, optional
        Show scientific E notation, by default False

    separators : bool, optional
        Show thousands separators (commas), by default False

    Returns
    -------
    str
        The formatted string.
    """
    if precision is not None:
        try:
            value = value.quantize(Decimal(10) ** -precision, ROUND_HALF_UP)
        except DecimalException:
            logging.debug(f"Failed to quantize {value} (precision = {precision})")
            pass

    # Trim trailing zeroes
    if normalize:
        value = value.normalize()

    if exponent:
        return f"{value:E}"

    return f"{value:{"," if separators else ""}f}"


def format_name(units: list[tuple[str, int]], sort_keys: bool = False) -> str:
    """ Format unit name without divisor (i.e "metre*second^-1") """
    names = []
    for unit, exponent in sorted(units) if sort_keys else units:
        names.append(format_exponent(unit, exponent))

    return "*".join(names)


def format_display_name(units: list[tuple[str, int]], sort_keys: bool = False) -> str:
    """ Format unit display name with divisor (i.e "metre/second") """
    numers = []
    denoms = []

    for unit, exponent in sorted(units) if sort_keys else units:
        if exponent > 0:
            numers.append(format_exponent(unit, exponent))
        else:
            denoms.append(format_exponent(unit, -exponent))

    if not numers:
        return format_name(units, sort_keys)

    elif not denoms:
        return "*".join(numers)

    return "*".join(numers) + "/" + "*".join(denoms)


def format_exponent(name: str, exponent: int) -> str:
    """ Format unit name with optional exponent. """
    if exponent != 1:
        return f"{name}^{exponent}"
    else:
        return name


def format_type(obj: object) -> str:
    """ Get a nice string representation of an object. """
    return type(obj).__name__
