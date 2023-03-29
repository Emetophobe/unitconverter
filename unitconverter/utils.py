# Copyright (c) 2022-2023 Mike Cunningham


from decimal import Decimal, DecimalException


def parse_decimal(value: Decimal | int | str, msg: str = None) -> Decimal:
    """ Parse value and return a Decimal. Raises ValueError if value is invalid. """
    if isinstance(value, float):
        raise ValueError(f'{value!r} is a float which should be avoided to prevent'
                         ' precision loss. Use a Decimal, int, or str instead.')
    try:
        return Decimal(value)
    except DecimalException:
        raise ValueError(msg or f'{value!r} is not a valid Decimal')


def simplify_unit(name: str) -> str:
    """ Simplify unit name by replacing characters. """
    for key, value in _replace_chars.items():
        if key in name:
            name = name.replace(key, value)

    return name


# Dictionary of replacement chars for internal lookup
_replace_chars = {
    # simplify multiplication symbols
    '⋅': '-',
    '*': '-',

    # simplify division
    ' per ': '/',

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
}
