# Copyright (c) 2022-2023 Mike Cunningham


import tomllib
from collections import defaultdict
from pathlib import Path

from unitconverter.definitions import UnitDef, create_definitions
from unitconverter.exceptions import DefinitionError, UnitError
from unitconverter.misc import simplify_unit, split_exponent
from unitconverter.unit import Unit


class Registry:

    _units = defaultdict(list)
    _aliases = {}

    def __init__(self) -> None:
        """ Initialize pre-defined units. """
        if not self._units:
            self._load_units()

    def new_unit(self, unitdef: UnitDef) -> None:
        """ Add a new unit definition. """

        if not isinstance(unitdef, UnitDef):
            raise DefinitionError(f'{unitdef!r} is not a valid unit definition')

        # Add the unit definition
        self.add_aliases(unitdef, unitdef.names())
        self._units[unitdef.category].append(unitdef)

        # Add prefixed unit definitions (if the unit supports it)
        for prefix_unit in create_definitions(unitdef):
            self.add_aliases(prefix_unit, prefix_unit.names())
            self._units[prefix_unit.category].append(prefix_unit)

    def add_alias(self, unitdef: UnitDef | str, alias: str) -> None:
        """ Add a unit alias. """

        # Make sure the definition is valid
        if isinstance(unitdef, str):
            unitdef = self.get_definition(unitdef)
        elif not isinstance(unitdef, UnitDef):
            raise DefinitionError(f'{unitdef} is not a valid unit definition')

        # Make sure the alias is valid
        if not alias or not isinstance(alias, str):
            raise DefinitionError(f'{unitdef} has an invalid alias: {alias!r}')
        elif alias in self._aliases:
            raise DefinitionError(f'{unitdef} has a duplicate alias: {alias}')

        self._aliases[alias] = unitdef

    def add_aliases(self, unitdef: UnitDef, aliases: set[str]):
        """ Add multiple unit aliases. """
        if not isinstance(aliases, (list, tuple, set)):
            raise DefinitionError(f'{unitdef} has invalid aliases: {aliases!r}'
                                  ' (expected a list, tuple or set)')
        for alias in aliases:
            self.add_alias(unitdef, alias)

    def get_unit(self, name: str) -> Unit:
        """ Get a unit by name. """
        simple_name = simplify_unit(name)

        # Check for pre-defined unit
        if simple_name in self._aliases:
            unit = self._aliases[simple_name]
            return Unit(unit.factor, (unit.name, unit.category))

        # Check if name contains an expression
        if '/' in name or '*' in name:
            raise UnitError(f'Invalid unit: {name}')

        # Split unit name and exponent
        split_name, exp = split_exponent(simple_name)
        if split_name in self._aliases:
            unit = self._aliases[split_name]
            return Unit(unit.factor, (unit.name, unit.category)) ** exp

        raise UnitError(f'Invalid unit: {name}')

    def get_units(self) -> dict[str, list[UnitDef]]:
        """ Get the dictionary of units. """
        return dict(self._units)

    def get_definition(self, name: str) -> UnitDef:
        if name in self._aliases:
            return self._aliases[name]

        raise DefinitionError(f'Invalid definition name: {name}')

    def _load_units(self) -> None:
        """ Load pre-defined units from toml files. """
        for filename in Path('data').glob('*.toml'):
            category = filename.stem.replace('_', ' ')

            with open(filename, 'rb') as infile:
                data = tomllib.load(infile)
                aliases = data.pop('aliases', {})

                # Add unit definitions
                for name, args in data.items():
                    self.new_unit(UnitDef(name, category, **args))

                # Add extra aliases
                for name, aliases in aliases.items():
                    self.add_aliases(name, aliases)


REGISTRY = Registry()

new_unit = REGISTRY.new_unit
add_alias = REGISTRY.add_alias
add_aliases = REGISTRY.add_aliases
get_unit = REGISTRY.get_unit
get_units = REGISTRY.get_units
get_definition = REGISTRY.get_definition


__all__ = [
    'REGISTRY',
    'Registry',
    'new_unit',
    'add_alias',
    'add_aliases',
    'get_unit',
    'get_units',
    'get_definition',
]
