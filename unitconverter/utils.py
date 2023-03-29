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
