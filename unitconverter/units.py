# Copyright (c) 2022-2023 Mike Cunningham


import tomllib
from pathlib import Path
from collections import defaultdict
from typing import KeysView, ItemsView
from unitconverter.unit import Unit
from unitconverter.locale import Locale, translate_unit


class Units:

    def __init__(self, locale: Locale = Locale.ENGLISH):
        """ Initialize units dictionary. """
        self.load_units(locale)

    def add_unit(self, unit: Unit) -> None:
        """ Add a unit to the dictionary. """
        # Check for duplicate names or symbols
        unitnames = unit.get_names()
        for name in unitnames:
            if name in self._aliases.keys():
                raise ValueError(f'{unit.name} has a duplicate name: {name}'
                                 f' (Original unit: {self._aliases[name]})')

        # Add all names to alias dict
        for name in unitnames:
            self._aliases[name] = unit

        # Add unit to units dict
        self._units[unit.category] = unit

    def get_units(self) -> dict[str, list[Unit]]:
        """ Get a dictionary of all categories and units. """
        return self._units

    def get_list(self) -> list[Unit]:
        """ Get a list of all units. """
        return list(self)

    def update_locale(self, locale: Locale = Locale.ENGLISH) -> None:
        """ Update unit locale (English vs American). """
        if self._locale != locale:
            self.load_units(locale)

    def load_units(self, locale: Locale = Locale.ENGLISH) -> None:
        """ Load units from toml files. """
        self._locale = locale
        self._units = defaultdict(list)
        self._aliases = {}

        # Load all toml files in the data directory
        files = Path('data').glob('*.toml')
        for filename in files:
            category = filename.stem.replace('_', ' ')
            with open(filename, 'rb') as infile:
                data = tomllib.load(infile)
                for name, args in data.items():
                    unit = Unit(name, category, **args)
                    if locale == locale.AMERICAN:
                        unit = translate_unit(unit, locale)
                    self._units[category].append(unit)

        # Check for duplicates before returning
        for _, units in self._units.items():
            for unit in units:
                for name in [unit.name] + unit.symbols + unit.aliases:
                    if name in self._aliases.keys():
                        raise ValueError(f'{unit.name} has a duplicate name: {name}'
                                         f' (Original unit: {self._aliases[name]})')
                    self._aliases[name] = unit

    def items(self) -> ItemsView:
        return self._units.items()

    def keys(self) -> KeysView:
        return self._units.keys()

    def __iter__(self) -> Unit:
        """ Iterate over all units. """
        for _, units in self._units.items():
            yield from units

    def __len__(self):
        """ Get total number of units. """
        return sum(len(units) for _, units in self._units.items())
