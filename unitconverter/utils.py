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

        A float also doesn't equal a string:

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
