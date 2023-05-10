# Copyright (c) 2022-2023 Mike Cunningham


import logging

from unitconverter.unit import Unit
from unitconverter.registry import get_unit
from unitconverter.exceptions import UnitError


def parse_unit(name: str) -> Unit:
    """ Parse unit name and return a Unit instance.

    Examples
    --------

        >>> parse_unit("metre")
        >>> parse_unit("metre/second")
        >>> parse_unit("kg*m²/s³*A²")

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
    if not name:
        raise UnitError(f'Invalid unit: {name!r}')

    if isinstance(name, Unit):
        return name

    # Check if the unit is defined in the registry
    try:
        return get_unit(name)
    except UnitError:
        pass

    # Try to create a composite unit
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

    logging.debug('parse_composite()')
    logging.debug(f'numers: {numers}')
    logging.debug(f'denoms: {denoms}')

    # Can't divide units from the same categories i.e metre/inch
    if len(numers) == len(denoms) == 1:
        if numers[0].dimen == denoms[0].dimen:
            category = numers[0].dimension
            raise UnitError(f'Invalid unit: {name} ({category}/{category})')

    # Check for temperature units which can't be composited
    for unit in numers + denoms:
        if unit.name in ('celsius', 'fahrenheit', 'rankine'):
            raise UnitError(f'Invalid unit: {name} - {unit.name} cannot be composited'
                            ' (only kelvin is supported for now)')

    numer = Unit()
    denom = Unit()

    for unit in numers:
        numer *= unit

    for unit in denoms:
        denom *= unit

    unit = numer / denom

    logging.debug(f'numer: {numer} ({numer.dimension})')
    logging.debug(f'denom: {denom} ({denom.dimension})')
    logging.debug(f'unit : {unit} ({unit.dimension})')

    if not unit:
        raise UnitError(f'Invalid unit: {name}')

    return unit


def _parse_names(names: str) -> list[str]:
    """ Split numerators or denominators into a list of unit names. """
    return names.split('*')
