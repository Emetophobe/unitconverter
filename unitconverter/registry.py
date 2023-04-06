# Copyright (c) 2022-2023 Mike Cunningham


import tomllib
from collections import defaultdict
from pathlib import Path

from unitconverter.exceptions import UnitError
from unitconverter.utils import simplify_unit
from unitconverter.unit import Unit


class Registry:
    """ Registry of pre-defined units. """

    _units = defaultdict(list)
    _aliases = {}

    def __init__(self):
        """ Initialize units dictionary. """
        if not self._units:
            self._load_units()

    def add_unit(self, unit: Unit) -> None:
        """ Add a unit to the dictionary. """
        # Check for duplicate names, symbols, or aliases
        for name in unit.get_names():
            if name in self._aliases.keys():
                raise UnitError(f'{unit.name} has a duplicate name: {name}'
                                f' (Original unit: {self._aliases[name]})')
            # Track all names, symbols, and aliases
            self._aliases[name] = unit

        # Add unit to category
        self._units[unit.category].append(unit)

    def get_unit(self, name: str) -> Unit:
        """ Get a unit by name. Raises UnitError if unit doesn't exist. """
        simple_name = simplify_unit(name)
        for unit in self:
            if simple_name in unit:
                return unit

        raise UnitError(f'Invalid unit: {name}')

    def get_units(self) -> dict[str, list[Unit]]:
        """ Get a dictionary of categories and units. """
        return dict(self._units)

    def get_aliases(self) -> dict[str, Unit]:
        """ Get a dictionary of unit aliases. """
        return dict(self._aliases)

    def list_units(self) -> list[Unit]:
        """ Get a list of all units. """
        return list(self)

    def iter_units(self):
        """ Get a units iterator. """
        return iter(self)

    def _load_units(self) -> None:
        """ Load pre-defined units from toml files. """
        files = Path('data').glob('*.toml')
        for filename in files:
            category = filename.stem.replace('_', ' ')
            with open(filename, 'rb') as infile:
                data = tomllib.load(infile)
                for name, args in data.items():
                    self.add_unit(Unit(name, category, **args))

    def __iter__(self) -> Unit:
        """ Iterate over all units. """
        for _, units in self._units.items():
            yield from units

    def __len__(self):
        """ Get total number of units. """
        return sum(len(units) for _, units in self._units.items())


_registry = Registry()

register = _registry.add_unit
get_unit = _registry.get_unit
get_units = _registry.get_units
iter_units = _registry.iter_units
list_units = _registry.list_units


__all__ = [
    'Registry',
    'register',
    'get_unit',
    'get_units',
    'iter_units',
    'list_units',
]
