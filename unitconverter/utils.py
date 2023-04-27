# Copyright (c) 2022-2023 Mike Cunningham


import re
from decimal import Decimal, DecimalException

from unitconverter.exceptions import ConverterError


def parse_decimal(value: Decimal | int | str, msg: str = None) -> Decimal:
    """ Convert value into a decimal.

    Raises ConverterError if value is a float. Use a string instead
    it will give a more accurate decimal value. See examples below.

    Examples:
    ---------
        This works with str:

            >>> Decimal('.1') + Decimal('.1') + Decimal('.1') == Decimal('.3')
            True

        But not with float:

            >>> Decimal(.1) + Decimal(.1) + Decimal(.1) == Decimal(.3)
            False

        A float also doesn't equal a string:

            >>> Decimal(.1) == Decimal('.1')
            False

        Source: https://www.laac.dev/blog/float-vs-decimal-python/
    """
    if isinstance(value, float):
        raise ConverterError(f'{value} is a float which cannot be mixed with Decimals.'
                             ' See docs/floating_point.txt for more details.')
    try:
        return Decimal(value)
    except DecimalException:
        raise ConverterError(msg or f'{value!r} is not a valid Decimal')


def split_exponent(name: str) -> tuple[str, int]:
    """ Split a unit name and possible exponent.

    Examples
    --------

        >>> split_exponent("metre^2")
        ("metre", 2)

        >>> split_exponent("second")
        ("second", 1)

        >>> split_exponent("second-1")
        ("second", -1)
    """
    result = _pattern.match(name)

    if result.group('exp'):
        return (result.group('unit'), int(result.group('exp')))

    return (result.group('unit'), 1)


# Unit name and exponent pattern
_pattern = re.compile(r'(?P<unit>[a-zA-Z]+[\-]?[a-zA-Z]+){1}[\^]?(?P<exp>[-+]?[0-9]+)?')


def simplify_unit(name: str) -> str:
    """ Simplify unit name by replacing strings/characters.
    Only used for internal lookup of unit names.

    Examples
    --------

        >>> simplify_unit("Nm²/volt^2)
        "Nm2/volt2"

        >>> simplify_unit("joule per gram")
        "joule/gram"

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
    'caliber': 'calibre',
}
