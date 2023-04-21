# Copyright (c) 2022-2023 Mike Cunningham


from decimal import Decimal, getcontext

from unitconverter.exceptions import CategoryError
from unitconverter.registry import get_unit
from unitconverter.types import Numeric
from unitconverter.unit import Unit
from unitconverter.utils import parse_numeric


# Set decimal precision
getcontext().prec = 10


def convert(value: Numeric, source: Unit | str, dest: Unit | str) -> Decimal:
    """ Convert value from source unit to destination unit.

    Parameters
    ----------
    value : Numeric
        value to convert

    source : Unit | str
        source unit or name

    dest : Unit | str
        destination unit or name

    Returns
    -------
    Decimal
        result of the conversion

    Raises
    ------
    UnitError
        the source or dest unit is invalid

    CategoryError
        the units are not compatible
    """
    value = parse_numeric(value)
    source = parse_unit(source)
    dest = parse_unit(dest)

    if source.category != dest.category:
        raise CategoryError(source, dest)

    value = Decimal(source.offset) + value * Decimal(source.factor)
    return (-Decimal(dest.offset) + value) / Decimal(dest.factor)


def parse_unit(name: str) -> Unit:
    """ Parse unit name and return a Unit.

    Parameters
    ----------
    name : str
        unit name, symbol, or alias

    Returns
    -------
    Unit
        unit instance from the registry

    Raises
    ------
    UnitError
        invalid unit name
    """
    if isinstance(name, Unit):
        return name

    # Just call Registry.get_name() for now
    return get_unit(name)


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
