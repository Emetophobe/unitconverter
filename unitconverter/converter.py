# Copyright (c) 2022-2023 Mike Cunningham


from decimal import Decimal, getcontext

from unitconverter.dimensions import fuel_categories
from unitconverter.exceptions import CategoryError, UnitError
from unitconverter.registry import get_unit
from unitconverter.unit import Unit
from unitconverter.misc import parse_decimal


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

    if not compatible_units(source, dest):
        raise CategoryError(source, dest)

    # Fuel conversion
    if source.category in fuel_categories:
        return convert_fuel(value, source, dest)

    # Temperature converison
    elif source.category == 'temperature':
        return convert_temperature(value, source, dest)

    # Regular conversion
    value = value * source.factor
    return value / dest.factor


def parse_unit(name: str) -> Unit:
    """ Parse unit name and return a Unit.

    Parameters
    ----------
    name : str
        unit name, symbol, or alias

    Returns
    -------
    Unit
        unit instance

    Raises
    ------
    UnitError
        invalid unit name
    """
    if isinstance(name, Unit):
        return name

    # Try to find unit normally
    try:
        return get_unit(name)
    except UnitError:
        pass

    # Try to parse expression into a composite unit
    return parse_composite(name)


def parse_composite(name: str) -> Unit:
    """ Parse unit names and return a composite Unit. """
    names = name.split('/')
    if len(names) == 1:
        numers = _parse_names(names[0])
        denoms = []
    elif len(names) == 2:
        numers = _parse_names(names[0])
        denoms = _parse_names(names[1])
    else:
        raise UnitError(f'Invalid unit: {name} - This script only supports'
                        ' one division per expression (feature still in development)')

    numers = [get_unit(numer) for numer in numers]
    denoms = [get_unit(denom) for denom in denoms]

    # Can't divide units from the same categories i.e metre/inch
    if len(numers) == len(denoms) == 1:
        if numers[0].category == denoms[0].category:
            category = numers[0].category
            raise UnitError(f'Invalid unit: {name} ({category}/{category})')

    # Temperature units can't be composited
    for unit in numers + denoms:
        if unit.category == 'temperature':
            raise UnitError(f'Invalid unit: {name} - Cannot combine temperature'
                            ' units (feature still in development)')

    unit = Unit()

    for numer in numers:
        unit *= numer

    for denom in denoms:
        unit /= denom

    if not unit:
        raise UnitError(f'Invalid unit: {name}')

    return unit


def _parse_names(names: str) -> list[str]:
    """ Split numerators or denominators into a list of unit names. """
    return names.split('*')


def convert_temperature(value: Decimal, source: Unit, dest: Unit) -> Decimal:
    """ Convert temperature units. """
    # Convert from source to kelvin
    if source.name == 'kelvin':
        pass
    elif source.name == 'celsius':
        value = value + Decimal('273.15')
    elif source.name == 'fahrenheit':
        value = (value + Decimal('459.67')) * Decimal(5) / Decimal(9)
    elif source.name == 'rankine':
        value = value * Decimal(5) / Decimal(9)
    else:
        raise UnitError(f'Unsupported temperature unit: {source.name}')

    # Convert from kelvin to dest
    if dest.name == 'kelvin':
        return value
    elif dest.name == 'celsius':
        return value - Decimal('273.15')
    elif dest.name == 'fahrenheit':
        return value * Decimal(9) / Decimal(5) - Decimal('459.67')
    elif dest.name == 'rankine':
        return value * Decimal(9) / Decimal(5)
    else:
        raise UnitError(f'Unsupported temperature unit: {dest.name}')


def convert_fuel(value: Decimal, source: Unit, dest: Unit) -> Decimal:
    """ Convert fuel economy and fuel consumption. """
    if source.category not in fuel_categories:
        raise UnitError(f'Invalid fuel unit: {source}')

    if dest.category not in fuel_categories:
        raise UnitError(f'Invalid fuel unit: {dest}')

    # Invert fuel consumption (litre/metre) and fuel economy (metre/litre)
    if source.category != dest.category:
        value = 1 / (value * source.factor)
        return value / dest.factor

    # Convert fuel units normally
    value = value * source.factor
    return value / dest.factor


def compatible_units(source: Unit, dest: Unit) -> bool:
    """ Returns True if the units are compatible. """
    if source.category == dest.category:
        return True
    elif source.category in fuel_categories and dest.category in fuel_categories:
        return True

    return False
