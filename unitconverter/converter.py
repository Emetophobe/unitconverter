# Copyright (c) 2022-2023 Mike Cunningham


from decimal import Decimal, getcontext

from unitconverter.exceptions import CategoryError, UnitError
from unitconverter.prefixes import get_prefixes
from unitconverter.registry import iter_units
from unitconverter.unit import Unit
from unitconverter.utils import parse_decimal, simplify_unit


# Set decimal precision
getcontext().prec = 10


def convert(value: Decimal, source: Unit | str, dest: Unit | str) -> Decimal:
    """ Convert value from source unit to destination unit.

    Args:
        value (Decimal | int | str):
            value to convert.

        source (Unit | str):
            source unit or name.

        dest (str | Unit):
            destination unit or name.

    Raises:
        UnitError: if a unit is invalid.
        CategoryError: if the units are incompatible.

    Returns:
        Decimal: the result of the conversion.
    """
    value = parse_decimal(value)
    source = parse_unit(source)
    dest = parse_unit(dest)

    if source.category != dest.category:
        raise CategoryError(source, dest)

    value = Decimal(source.offset) + value * Decimal(source.factor)
    return (-Decimal(dest.offset) + value) / Decimal(dest.factor)


def parse_unit(name: str) -> Unit:
    """ Parse unit name and return a Unit.

    Args:
        name (str): unit name, symbol, or alias.

    Raises:
        UnitError: if the unit name is invalid.

    Returns:
        Unit: a unit instance.
    """
    if isinstance(name, Unit):
        return name

    simple_name = simplify_unit(name)

    # Check predefined units
    for unit in iter_units():
        if simple_name in unit:
            return unit

    # Check generated units
    for unit in iter_units():
        # Get list of supported prefixes (if any)
        prefixes = get_prefixes(unit.prefix_scale)

        # Generate prefixes and check for a matching unit
        for prefix in prefixes:
            prefix_unit = unit.prefix(prefix)
            if simple_name in prefix_unit:
                return prefix_unit

    raise UnitError(f'Invalid unit: {name}')


def format_decimal(value: Decimal,
                   exponent: bool = False,
                   precision: int = None,
                   commas: bool = False
                   ) -> str:
    """ Format a decimal into a string for display.

    Args:
        value (Decimal):
            the decimal value.

        exponent (bool, optional):
            show E notation when possible. Defaults to False.

        precision (int, optional):
            set rounding precision. Defaults to None.

        commas (bool, optional):
            show commas (thousands) separators. Defaults to False.

    Returns:
        str: the formatted string.
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
