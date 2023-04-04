# Copyright (c) 2022-2023 Mike Cunningham


from decimal import Decimal

from unitconverter.exceptions import ConverterError, UnitError
from unitconverter.prefixes import get_prefixes
from unitconverter.registry import iter_units
from unitconverter.unit import Unit
from unitconverter.utils import parse_decimal, simplify_unit


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

    return source.convert(value, dest)


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

    # Get simplified unit name
    simple_name = simplify_unit(name)

    # Check pre-defined list for a matching unit
    for unit in iter_units():
        if simple_name in unit:
            return unit

    # Check generated prefixes
    for unit in iter_units():
        # Get supported prefix table based on unit prefix option
        prefixes = get_prefixes(unit.prefix_scale)

        # Generate prefixes and check for a matching unit
        for factor, symbol, prefix in prefixes:
            prefix_unit = unit.scale(factor, symbol, prefix)
            if simple_name in prefix_unit:
                return prefix_unit

    # Invalid unit name
    raise UnitError(f'Invalid unit: {name}')


def format_decimal(value: Decimal,
                   exponent: bool = False,
                   precision: int = None,
                   commas: bool = False
                   ) -> str:
    """ Format a decimal into a string for display.

    Args:
        value (Decimal): the decimal value.
        exponent (bool, optional): use e notation when possible. Defaults to False.
        precision (int, optional): set rounding precision. Defaults to None.
        commas (bool, optional): use commas for thousands separators. Defaults to False.

    Returns:
        str: the formatted string.
    """
    precision = f'.{precision}' if precision is not None else ''

    if exponent:
        return f'{value:{precision}E}'

    comma = ',' if commas else ''
    return f'{value:{comma}{precision}f}'
