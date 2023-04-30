# Copyright (c) 2022-2023 Mike Cunningham


from pathlib import Path

import tomllib

from unitconverter.definitions import UnitDefinition, create_definitions
from unitconverter.exceptions import DefinitionError, UnitError
from unitconverter.formatting import simplify_unit, split_exponent
from unitconverter.unit import Unit, UnitDict


# Unitless unit
# one = Unit(1, 'one')


class Registry:

    _units = {}
    _aliases = {}
    _dimensions = {}

    def __init__(self) -> None:
        """ Initialize pre-defined units. """
        if not self._units:
            self._load_units()

    def new_unit(self, unitdef: UnitDefinition) -> None:
        """ Add a new unit definition. """
        if not isinstance(unitdef, UnitDefinition):
            raise DefinitionError(f'{unitdef!r} is not a valid unit definition')

        # Add unit definition
        self.add_aliases(unitdef, unitdef.names())
        self._units[unitdef.name] = unitdef

        # Add prefixed unit definitions if the unit supports it
        for prefix_unit in create_definitions(unitdef):
            self.add_aliases(prefix_unit, prefix_unit.names())
            self._units[prefix_unit.name] = prefix_unit

    def add_alias(self, unitdef: str | UnitDefinition, alias: str) -> None:
        """ Add a unit alias. """

        # Make sure the definition is valid
        if isinstance(unitdef, str):
            unitdef = self.get_definition(unitdef)
        elif not isinstance(unitdef, UnitDefinition):
            raise DefinitionError(f'{unitdef} is not a valid unit definition')

        # Make sure the alias is valid
        if not alias or not isinstance(alias, str):
            raise DefinitionError(f'{unitdef} has an invalid alias: {alias!r}')
        elif alias in self._aliases:
            raise DefinitionError(f'{unitdef} has a duplicate alias: {alias}')

        self._aliases[alias] = unitdef

    def add_aliases(self, unitdef: str | UnitDefinition, aliases: list | tuple | set):
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
            return Unit(unit.factor, unit.name, unit.dimen)

        # Check if name contains an expression
        if '/' in name or '*' in name:
            raise UnitError(f'Invalid unit: {name}')

        # Split unit name and exponent
        split_name, exp = split_exponent(simple_name)
        if split_name in self._aliases:
            unit = self._aliases[split_name]
            return Unit(unit.factor, unit.name, unit.dimen) ** exp

        raise UnitError(f'Invalid unit: {name}')

    def get_units(self) -> dict[str, list[UnitDefinition]]:
        """ Get the dictionary of units. """
        return dict(self._units)

    def get_definition(self, name: str) -> UnitDefinition:
        """ Get a unit definition from a unit name. """
        if name in self._aliases:
            return self._aliases[name]

        raise DefinitionError(f'Invalid definition name: {name}')

    def get_dimensions(self) -> dict:
        """ Get the dictionary of dimensions/categories. """
        return dict(self._dimensions)

    def get_category(self, units: Unit | UnitDict) -> str:
        """ Get a category name from unit dimensions. """
        if isinstance(units, Unit):
            dimen = units.dimen
        elif isinstance(units, UnitDict):
            dimen = units
        else:
            raise UnitError(f'{units!r} is not a valid Unit or UnitDict')

        # Look for a matching dimension category
        if dimen.as_tuple() in self._dimensions:
            return self._dimensions[dimen.as_tuple()]

        # Just use the dimension name as a fallback
        return dimen.name

    def _load_units(self) -> None:
        """ Load pre-defined units from toml files. """
        for filename in Path('data').glob('*.toml'):
            category = filename.stem.replace('_', ' ')

            with open(filename, 'rb') as infile:
                data = tomllib.load(infile)

                dimensions = UnitDict(data.pop('dimensions'))
                dimension_key = dimensions.as_tuple()

                # Check for duplicate dimensions
                if dimension_key in self._dimensions:
                    original = self._dimensions[dimension_key]
                    raise DefinitionError(f'Duplicate dimension: {dimensions}'
                                          f' original category: {original}')

                # Save dimension/category info
                self._dimensions[dimension_key] = category

                # Add unit definitions
                for name, args in data.items():
                    try:
                        self.new_unit(UnitDefinition(name, category, dimensions, **args))
                    except DefinitionError as e:
                        raise DefinitionError(f'Invalid definition in {filename}\n'
                                              f'Definition error: {e}')


# Global unit registry
REGISTRY = Registry()

new_unit = REGISTRY.new_unit
add_alias = REGISTRY.add_alias
add_aliases = REGISTRY.add_aliases
get_unit = REGISTRY.get_unit
get_units = REGISTRY.get_units
get_definition = REGISTRY.get_definition
get_dimensions = REGISTRY.get_dimensions
get_category = REGISTRY.get_category


__all__ = [
    'REGISTRY',
    'Registry',
    'new_unit',
    'add_alias',
    'add_aliases',
    'get_unit',
    'get_units',
    'get_definition',
    'get_dimensions',
    'get_category',
]
