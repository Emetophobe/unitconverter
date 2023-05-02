# Copyright (c) 2022-2023 Mike Cunningham


import logging
import re
from decimal import Decimal, DecimalException

from unitconverter.exceptions import ConverterError, UnitError


# Unit formatting symbols
EXP_SYMBOL = '^'
MULTI_SYMBOL = '*'
DIV_SYMBOL = '/'


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


def format_decimal(value: Decimal,
                   exponent: bool = False,
                   precision: int = None,
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
    precision = f'.{precision}' if precision is not None else ''

    if exponent:
        return f'{value:{precision}E}'

    comma = ',' if commas else ''
    number = f'{value:{comma}{precision}f}'

    # Remove trailing zeroes
    if '.' in number:
        while number[-1] == '0' and number[-2] != '.':
            number = number[:-1]

    return number


def format_name(units: dict[str, int], sort_keys: bool = False) -> str:
    """ Format unit name without divisor (i.e "metre*second^-1") """
    numers = []
    for unit, exp in sorted(units.items()) if sort_keys else units.items():
        numers.append(format_exponent(unit, exp))

    return MULTI_SYMBOL.join(numers)


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
        return MULTI_SYMBOL.join(numers)

    return MULTI_SYMBOL.join(numers) + DIV_SYMBOL + MULTI_SYMBOL.join(denoms)


def format_exponent(name: str, exponent: int) -> str:
    """ Format unit name with optional exponent. """
    if exponent == 1:
        return name

    return f'{name}{EXP_SYMBOL}{exponent}'


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
    try:
        result = _pattern.match(name)
        if result.group('exp'):
            unit, exp = result.group('unit'), int(result.group('exp'))
        else:
            unit, exp = result.group('unit'), 1

        # Try rebuilding the unit name to see if it was split correctly
        rejoined = unit
        if name.endswith(str(exp)):
            rejoined += str(exp)

        logging.debug('split_exponent()')
        logging.debug(f'name  : {name}')
        logging.debug(f'joined: {rejoined}')

        if name != rejoined:
            logging.debug(f'error parsing {name!r}')
            raise UnitError(f'Invalid unit: {name}')

        return unit, exp
    except AttributeError:
        logging.debug(f'split_exponent({name!r}) attribute error when parsing unit')
        raise UnitError(f'Invalid unit: {name}')


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
    if not isinstance(name, str):
        raise UnitError(f'Invalid unit: {name}')

    for key, value in _replacements.items():
        if key in name:
            name = name.replace(key, value)
    return name


# Unit name and exponent patterns
_unit_pattern = r'(?P<unit>[a-zA-Z°Ωµ]+[\-]?[a-zA-Z°Ωµ]+|[a-zA-Z°Ωµ]+){1}'
_exp_pattern = r'(?P<exp>[-+]?[0-9]+)?'
_pattern = re.compile(_unit_pattern + _exp_pattern)


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

    # simplify symbols
    # 'µ': 'mu',
    # '°': 'deg',
    # 'Ω': 'ohm',

    # regional spelling
    'meter': 'metre',
    'liter': 'litre',
    'caliber': 'calibre',
}
