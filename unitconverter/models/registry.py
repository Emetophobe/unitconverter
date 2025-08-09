# Copyright (c) 2022-2025 Mike Cunningham


from unitconverter.exceptions import ConverterError
from unitconverter.models.definition import Definition
from unitconverter.models.prefix import get_prefixes
from unitconverter.models.unit import Unit


class Registry:
    """ Used to store and retrieve information about units.

        Use add_definition() to define a Unit in the registry.
        Use get_unit() to retrieve a Unit from the registry.
     """

    def __init__(self, units: dict[str, Definition] | None = None) -> None:
        """ Create a unit registry.

        Args:
            units (dict[str, Definition] | None, optional):
                A dictionary of pre-defined units. Defaults to None.
        """
        self._units = {}
        self._aliases = {}

        # Add each unit individually to validate them and check for duplicates
        if units:
            for definition in units.values():
                self.add_definition(definition)

    def add_definition(self, definition: Definition) -> None:
        """ Add a unit definition to the registry.

        Args:
            definition (Definition): The unit definition.

        Raises:
            ConverterError: If the definition is invalid or it contains a duplicate.
        """
        # Add unit names, symbols, and aliases
        for alias in definition.names():
            self.add_alias(definition, alias)

        # Add unit definition
        self._units[definition.name] = definition

        # Add prefixed definitions as well if the unit supports it
        for prefix in get_prefixes(definition.prefix):
            self.add_definition(prefix + definition)

    def add_alias(self, unit: Definition | str, alias: str) -> None:
        """ Add a unit name, symbol, or alias to the registry.

        Args:
            unit (Definition | str): A unit string or unit definition.
            alias (str): A unit name, symbol, or alias.

        Raises:
            ConverterError: If an argument is invalid or if the alias is already defined.
        """
        if not isinstance(unit, (Definition, str)):
            raise ConverterError(f"{unit} is not a valid unit definition")

        if not alias or not isinstance(alias, str):
            raise ConverterError(f"{unit} has an invalid alias {alias!r}")

        # Try to convert a unit string to unit definition.
        if isinstance(unit, str):
            unit = self.get_definition(unit)

        self._aliases[alias] = unit

    def get_unit(self, name: str, exponent: int = 1) -> Unit:
        """ Get unit by name, symbol, or alias.

        Args:
            name (str): A unit name, symbol, or alias.
            exponent (int, optional): Unit exponent. Defaults to 1.

        Raises:
            ConverterError: If no unit could be found.

        Returns:
            Unit: The unit instance.
        """
        try:
            unit = self._aliases[name]
            return Unit(unit.factor, unit.name, unit.dimen) ** exponent
        except KeyError:
            raise ConverterError(f"{name} is not a valid unit")

    def get_definition(self, name: str) -> Definition:
        """ Get a unit definition from a unit name, symbol, or alias.

        Args:
            name (str): A unit name, symbol, or alias.

        Raises:
            ConverterError: If no unit could be found.

        Returns:
            Definition: The unit definition.
        """
        try:
            return self._aliases[name]
        except KeyError:
            raise ConverterError(f"{name} is not a valid unit")
