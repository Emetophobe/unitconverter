# Copyright (c) 2022-2025 Mike Cunningham
# https://www.github.com/emetophobe/unitconverter


import logging

from decimal import Decimal, DecimalException, ROUND_HALF_UP
from fractions import Fraction


def format_quantity(quantity: Fraction,
                    precision: int | None = None,
                    normalize: bool = False,
                    fraction: bool = False,
                    exponent: bool = False,
                    separators: bool = False
                    ) -> str:
    """ Format quantity into a string for display.

    If fraction is True all other arguments are ignored.
    If exponent is True the separators argument is ignored.

    Parameters
    ----------
    quantity : Fraction
        The quantity or value

    precision : int | None, optional
        Set rounding precision, by default None

    normalize : bool, optional
        Strip trailing zeros, by default False

    fraction : bool, optional
        Show fraction, by default False

    exponent : bool, optional
        Show scientific e notation, by default False

    separators : bool, optional
        Show thousands separators, by default False

    Returns
    -------
    str
        The formatted quantity
    """

    if fraction:
        return str(quantity)

    value = Decimal(quantity.numerator) / Decimal(quantity.denominator)

    if precision is not None:
        try:
            value = value.quantize(Decimal(10) ** -precision, ROUND_HALF_UP)
        except DecimalException:
            logging.debug(f"Failed to quantize {quantity} (precision = {precision})")
            pass

    if normalize:
        value = value.normalize()

    if exponent:
        return f"{value:e}"

    return f"{value:{"," if separators else ""}f}"


def format_name(units: list[tuple[str, int]], sort_keys: bool = False) -> str:
    """ Format unit name without divisor (i.e "metre*second^-1") """
    names = []
    for unit, exponent in sorted(units) if sort_keys else units:
        names.append(format_exponent(unit, exponent))

    return "*".join(names)


def format_display_name(units: list[tuple[str, int]], sort_keys: bool = False) -> str:
    """ Format unit name with divisor (i.e "metre/second") """
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
