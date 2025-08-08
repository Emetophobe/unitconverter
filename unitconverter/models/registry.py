# Copyright (c) 2022-2025 Mike Cunningham


from unitconverter.exceptions import DefinitionError, UnitError
from unitconverter.models.definition import Definition
from unitconverter.models.prefix import get_prefixes
from unitconverter.models.unit import Unit


class Registry:
    """ Used to store and retrieve unit definitions. """

    def __init__(self, units: dict[str, Definition] | None = None) -> None:
        """ Initialize registry with optional unit definitions. """

        self._units = {}
        self._aliases = {}

        # Add each unit individually to validate them and check for duplicates
        if units:
            for definition in units.values():
                self.add_definition(definition)

    def add_definition(self, definition: Definition) -> None:
        """ Add a unit definition to the registry. """

        # Add aliases and check for dupes
        for alias in definition.names():
            self.add_alias(definition, alias)

        # Add unit definition
        self._units[definition.name] = definition

        # Add prefixed definitions as well if the unit supports it
        for prefix in get_prefixes(definition.prefix):
            self.add_definition(prefix + definition)

    def add_alias(self, unit: Definition | str, alias: str) -> None:
        """ Add a unit alias. Raises a DefinitionError if an argument is invalid. """

        # Make sure the definition is valid
        if isinstance(unit, str):
            unit = self.get_definition(unit)
        elif not isinstance(unit, Definition):
            raise DefinitionError(f"{unit} is not a valid Definition")

        # Make sure the alias is valid
        if not alias or not isinstance(alias, str):
            raise DefinitionError(f"{unit} has an invalid alias {alias}")
        elif alias in self._aliases:
            raise DefinitionError(f"{unit} has a duplicate alias {alias}")

        self._aliases[alias] = unit

    def get_unit(self, name: str, exponent: int = 1) -> Unit:
        """ Get a unit by name. Raises a UnitError if the name is invalid. """
        try:
            unit = self._aliases[name]
            return Unit(unit.factor, unit.name, unit.dimen) ** exponent
        except KeyError:
            raise UnitError(f"{name} is not a valid unit")

    def get_definition(self, name: str) -> Definition:
        """ Get a unit definition from a unit name. """
        try:
            return self._aliases[name]
        except KeyError:
            raise UnitError(f"{name} is not a valid unit")

    def __contains__(self, unit: str) -> bool:
        """ Returns true if a unit name is in the registry. """
        return unit in self._aliases
