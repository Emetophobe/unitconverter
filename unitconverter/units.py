# Copyright (c) 2022-2023 Mike Cunningham


import tomllib
from pathlib import Path
from collections import defaultdict
from typing import KeysView, ItemsView
from unitconverter.unit import Unit
from unitconverter.locale import Locale, translate_unit


class Units:

    def __init__(self, locale: Locale = Locale.ENGLISH):
        self.load_units(locale)

    def add_unit(self, unit: Unit) -> None:
        """ Add a unit to the dictionary. """
        # Check for duplicate names or symbols
        unitnames = unit.get_names()
        for name in unitnames:
            if name in self.aliases.keys():
                raise ValueError(f'{unit.name} has a duplicate name: {name}'
                                 f' (Original unit: {self.aliases[name]})')

        # Add all names to alias dict
        for name in unitnames:
            self.aliases[name] = unit

        # Add unit to units dict
        self.units[unit.category] = unit

    def get_units(self) -> dict[str, list[Unit]]:
        """ Get a dictionary of all categories and units. """
        return self.units

    def get_unit_list(self) -> list[Unit]:
        """ Get a list of all units. """
        return list(self)

    def load_units(self, locale: Locale) -> None:
        """ Load units from toml files. """
        self.locale = locale
        self.units = defaultdict(list)
        self.aliases = {}

        # Load all toml files in the data directory
        files = Path('data').glob('*.toml')
        for filename in files:
            category = filename.stem.replace('_', ' ')
            with open(filename, 'rb') as infile:
                data = tomllib.load(infile)
                for name, args in data.items():
                    unit = Unit(name, category, **args)
                    unit = translate_unit(unit, locale)
                    self.units[category].append(unit)

        # Check for duplicates before returning
        for _, units in self.units.items():
            for unit in units:
                for name in [unit.name] + unit.symbols + unit.aliases:
                    if name in self.aliases.keys():
                        raise ValueError(f'{unit.name} has a duplicate name: {name}'
                                         f' (Original unit: {self.aliases[name]})')
                    self.aliases[name] = unit

        return units

    def items(self) -> ItemsView:
        return self.units.items()

    def keys(self) -> KeysView:
        return self.units.keys()

    def __iter__(self) -> Unit:
        """ Iterate over all units. """
        for _, units in self.units.items():
            yield from units

    def __len__(self):
        """ Get total number of units. """
        return sum(len(units) for _, units in self.units.items())
