# Copyright (c) 2022-2023 Mike Cunningham


from decimal import Decimal, getcontext

from unitconverter.exceptions import CategoryError, UnitError
from unitconverter.formatting import parse_decimal
from unitconverter.parser import parse_unit
from unitconverter.registry import get_category
from unitconverter.unit import Unit


# Set decimal precision
getcontext().prec = 15


def convert(value: Decimal | int | str, source: Unit | str, dest: Unit | str) -> Decimal:
    """ Convert value from source unit to destination unit.

    Parameters
    ----------
    value : Decimal | int | str
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
    value = parse_decimal(value)
    source = parse_unit(source)
    dest = parse_unit(dest)

    source_category = get_category(source)
    dest_category = get_category(dest)

    if not compatible_units(source_category, dest_category):
        raise CategoryError(f'Category mismatch: {source.name} ({source_category})'
                            f' and {dest.name} ({dest_category})')

    # Fuel conversion
    if source_category in FUEL_CATEGORY:
        return convert_fuel(value, source, dest)

    # Temperature conversion
    elif source_category == 'temperature':
        return convert_temperature(value, source, dest)

    # Regular conversion
    value = value * source.factor
    return value / dest.factor


def convert_temperature(value: Decimal, source: Unit, dest: Unit) -> Decimal:
    """ Convert temperature units. """
    value = parse_decimal(value)
    source = parse_unit(source)
    dest = parse_unit(dest)

    if source.dimension != 'temperature':
        raise UnitError(f'Invalid temperature unit: {source.name}')

    if dest.dimension != 'temperature':
        raise UnitError(f'Invalid temperature unit: {dest.name}')

    # Convert from source to kelvin
    if source.name.endswith('kelvin'):
        value = value * source.factor
    elif source.name == 'celsius':
        value = value + Decimal('273.15')
    elif source.name == 'fahrenheit':
        value = (value + Decimal('459.67')) * Decimal(5) / Decimal(9)
    elif source.name == 'rankine':
        value = value * Decimal(5) / Decimal(9)
    else:
        raise UnitError(f'Unsupported temperature unit: {source.name}')

    # Convert from kelvin to dest
    if dest.name.endswith('kelvin'):
        return value / dest.factor
    elif dest.name == 'celsius':
        return value - Decimal('273.15')
    elif dest.name == 'fahrenheit':
        return value * Decimal(9) / Decimal(5) - Decimal('459.67')
    elif dest.name == 'rankine':
        return value * Decimal(9) / Decimal(5)
    else:
        raise UnitError(f'Unsupported temperature unit: {dest.name}')


def convert_fuel(value: Decimal, source: Unit, dest: Unit) -> Decimal:
    """ Convert between fuel economy and fuel consumption units. """
    value = parse_decimal(value)
    source = parse_unit(source)
    dest = parse_unit(dest)

    if source.dimension not in FUEL_CATEGORY:
        raise UnitError(f'Invalid fuel unit: {source}')

    if dest.dimension not in FUEL_CATEGORY:
        raise UnitError(f'Invalid fuel unit: {dest}')

    # Invert fuel consumption (litre/metre) and fuel economy (metre/litre)
    if source.dimension != dest.dimension:
        value = 1 / (value * source.factor)
        return value / dest.factor

    # Convert fuel units normally
    value = value * source.factor
    return value / dest.factor


def compatible_units(source_category: str, dest_category: str) -> bool:
    """ Returns True if the unit categories are compatible. """
    if source_category == dest_category:
        return True
    elif source_category in FUEL_CATEGORY and dest_category in FUEL_CATEGORY:
        return True
    return False


# Compatible fuel categories
FUEL_CATEGORY = ('fuel economy', 'fuel consumption')
