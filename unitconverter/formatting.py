# Copyright (c) 2022-2025 Mike Cunningham
# https://www.github.com/emetophobe/unitconverter


from decimal import Decimal, DecimalException

from unitconverter.exceptions import ConverterError


def parse_decimal(value: Decimal | int | str) -> Decimal:
    """ Parse value and return a Decimal.

    Raises ConverterError if value is a float. Use a string instead
    it will give a more accurate decimal value. See examples below:

        This works with str:

            >>> Decimal("0.1") + Decimal("0.1") + Decimal("0.1") == Decimal("0.3")
            True

        But not with float:

            >>> Decimal(0.1) + Decimal(0.1) + Decimal(0.1) == Decimal(0.3)
            False

        A float also doesn"t equal a string:

            >>> Decimal(0.1) == Decimal("0.1")
            False

        Source: https://www.laac.dev/blog/float-vs-decimal-python/
    """
    if isinstance(value, float):
        raise ConverterError(f"{value} is a float which cannot be mixed with Decimals."
                             " See docs/floating_point.txt for more details.")
    try:
        return Decimal(value)
    except DecimalException:
        raise ConverterError(f"{value!r} is not a valid Decimal")


def format_decimal(value: Decimal,
                   exponent: bool = False,
                   precision: int | None = None,
                   commas: bool = False
                   ) -> str:
    """ Format a decimal into a string for display.

    Parameters
    ----------
    value : Decimal
        the decimal value

    exponent : bool, optional
        use E notation when possible, by default False

    precision : int, optional
        set rounding precision, by default None

    commas : bool, optional
        show commas (thousands) separators, by default False

    Returns
    -------
    str
        formatted string
    """
    precision_format = f".{precision}" if precision is not None else ""

    if exponent:
        return f"{value:{precision_format}E}"

    comma = "," if commas else ""
    number = f"{value:{comma}{precision_format}f}"

    # Remove trailing zeroes
    if "." in number:
        while number[-1] == "0" and number[-2] != ".":
            number = number[:-1]

    return number


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


def format_type(obj: object) -> str:
    """ Get a nice string representation of an object. """
    return type(obj).__name__


def format_exponent(name: str, exponent: int) -> str:
    """ Format unit name with optional exponent. """
    if exponent == 1:
        return name
    else:
        return f"{name}^{exponent}"
