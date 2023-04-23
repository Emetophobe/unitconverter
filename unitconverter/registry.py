# Copyright (c) 2022-2023 Mike Cunningham


import tomllib
from collections import defaultdict
from pathlib import Path

from unitconverter.exceptions import UnitError
from unitconverter.utils import simplify_unit
from unitconverter.unit import Unit, TemperatureUnit
from unitconverter.prefixes import create_prefixed_units


class Registry:
    """ Registry of pre-defined units. """

    _units = defaultdict(list)
    _aliases = {}

    def __init__(self):
        """ Load pre-defined units. """
        if not self._units:
            self._load_units()

    def add_unit(self, unit: Unit) -> None:
        """ Add a unit to the registry. """
        # Check for duplicates
        for name in unit.names():
            if name in self._aliases.keys():
                raise UnitError(f'{unit.name} has a duplicate name: {name}'
                                f' (Original unit: {self._aliases[name]})')
            # Track all unit names, symbols, and aliases
            self._aliases[name] = unit

        self._units[unit.category].append(unit)

    def get_unit(self, name: str) -> Unit:
        """ Get a unit by name. """
        simple_name = simplify_unit(name)
        for unit in self:
            if simple_name in unit:
                return unit

        raise UnitError(f'Invalid unit: {name}')

    def get_units(self) -> list[Unit]:
        """ Get a list of all units. """
        return list(self)

    def get_categories(self) -> dict[str, list[Unit]]:
        """ Get a dictionary of categories and units. """
        return dict(self._units)

    def get_aliases(self) -> dict[str, Unit]:
        """ Get a dictionary of unit aliases. """
        return dict(self._aliases)

    def iter_units(self):
        """ Get a units iterator. """
        return iter(self)

    def _load_units(self) -> None:
        """ Load pre-defined units from toml files. """
        for filename in Path('data').glob('*.toml'):
            category = filename.stem.replace('_', ' ')

            with open(filename, 'rb') as infile:
                data = tomllib.load(infile)
                for name, args in data.items():
                    # Temperature units use a custom class
                    if category == 'temperature':
                        unit = TemperatureUnit(name, category, **args)
                    else:
                        unit = Unit(name, category, **args)

                    self.add_unit(unit)

                    # Add generated units
                    units = create_prefixed_units(unit)
                    for prefixed_unit in units:
                        self.add_unit(prefixed_unit)

    def __iter__(self) -> Unit:
        """ Iterate over all units. """
        for _, units in self._units.items():
            yield from units

    def __len__(self):
        """ Get total number of units. """
        return sum(len(units) for _, units in self._units.items())


REGISTRY = Registry()

add_unit = REGISTRY.add_unit
get_unit = REGISTRY.get_unit
get_units = REGISTRY.get_units
get_categories = REGISTRY.get_categories
get_aliases = REGISTRY.get_aliases
iter_units = REGISTRY.iter_units


__all__ = [
    'Registry',
    'add_unit',
    'get_unit',
    'get_units',
    'get_categories',
    'get_aliases',
    'iter_units',
]
