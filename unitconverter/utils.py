# Copyright (c) 2022-2025 Mike Cunningham
# https://www.github.com/emetophobe/unitconverter


from fractions import Fraction
from unitconverter.exceptions import ConverterError


def parse_fraction(value: Fraction | str | int) -> Fraction:
    """ Parse value and return a Fraction. """
    if isinstance(value, Fraction):
        return value

    if isinstance(value, float):
        raise ConverterError("Cannot mix floats and fractions. For better accuracy"
                             f"wrap float in a string; i.e Fraction(\"{value}\")")
    try:
        return Fraction(value)
    except (TypeError, ValueError):
        raise ConverterError(f"{value!r} is not a fraction or decimal value")
