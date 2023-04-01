# Copyright (c) 2022-2023 Mike Cunningham


from decimal import Decimal, DecimalException
from unitconverter.exceptions import ConverterError, FloatError


def parse_decimal(value: Decimal | int | str, msg: str = None) -> Decimal:
    """ Convert value into a decimal.

    Raises FloatError if value is a float. Use a string instead it will
    give a more accurate decimal value. See examples below.

    Examples:

        This works with strings:

            >>> Decimal('.1') + Decimal('.1') + Decimal('.1') == Decimal('.3')
            True

        But not with floats:

            >>> Decimal(.1) + Decimal(.1) + Decimal(.1) == Decimal(.3)
            False

            >>> Decimal(.1) == Decimal('.1')
            False

        Source: https://www.laac.dev/blog/float-vs-decimal-python/
    """
    if isinstance(value, float):
        raise FloatError(value)

    try:
        return Decimal(value)
    except DecimalException:
        raise ConverterError(msg or f'{value!r} is not a valid Decimal')


def simplify_unit(name: str) -> str:
    """ Simplify unit name by replacing strings/characters.
    Only used for internal lookup of unit names.

    Example:

        >>> simplify_unit("Nm²/volt^2)
        "Nm2/volt2"

    """
    for key, value in _replacements.items():
        if key in name:
            name = name.replace(key, value)
    return name


# Dictionary of replacements for internal lookup
_replacements = {
    # simplify exponents
    '^': '',
    '⁰': '0',
    '¹': '1',
    '²': '2',
    '³': '3',
    '⁴': '4',
    '⁵': '5',
    '⁶': '6',
    '⁷': '7',
    '⁸': '8',
    '⁹': '9',

    # simplify multiplication
    '⋅': '-',
    '*': '-',

    # simplify division
    ' per ': '/',

    # regional spelling
    'meter': 'metre',
    'liter': 'litre',
}
