# Copyright (c) 2022-2023 Mike Cunningham


import tomllib
from collections import defaultdict
from pathlib import Path
from typing import ItemsView, KeysView

from unitconverter.exceptions import UnitError
from unitconverter.utils import simplify_unit
from unitconverter.unit import Unit


class Units:
    """ Units holds the dictionary of defined units. """

    _units = defaultdict(list)
    _aliases = {}

    def __init__(self):
        """ Initialize units dictionary. """
        if not self._units:
            self._load_units()

    def add_unit(self, unit: Unit) -> None:
        """ Add a unit to the dictionary. """
        # Check for duplicate names or symbols
        for name in unit.get_names():
            if name in self._aliases.keys():
                raise UnitError(f'{unit.name} has a duplicate name: {name}'
                                f' (Original unit: {self._aliases[name]})')
            # Track aliases
            self._aliases[name] = unit

        # Add unit to category
        self._units[unit.category].append(unit)

    def get_unit(self, name: str) -> Unit:
        """ Get a unit by name. Raises UnitError if unit doesn't exist. """
        simple_name = simplify_unit(name)
        for unit in self:
            if simple_name in unit:
                if name in unit:
                    return unit

        raise UnitError(f'Invalid unit: {name}')

    def get_units(self) -> dict[str, list[Unit]]:
        """ Get a dictionary of all categories and units. """
        return self._units

    def get_list(self) -> list[Unit]:
        """ Get a list of all units. """
        return list(self)

    def items(self) -> ItemsView:
        return self._units.items()

    def keys(self) -> KeysView:
        return self._units.keys()

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
