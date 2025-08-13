# Copyright (c) 2022-2025 Mike Cunningham
# https://www.github.com/emetophobe/unitconverter


from unitconverter.exceptions import ConverterError
from unitconverter.models.definition import Definition
from unitconverter.models.dimension import Dimension
from unitconverter.models.prefix import get_prefixes
from unitconverter.models.unit import Unit


class Registry:
    """ Used to store and retrieve information about units.

        Use add_definition() to define a Unit in the registry.
        Use get_unit() to retrieve a Unit from the registry.
     """

    def __init__(self,
                 categories: dict[str, Dimension] | None = None,
                 units: dict[str, Definition] | None = None
                 ) -> None:
        """ Create a unit registry.

        Args:
            categories (dict[str, Dimension] | None, optional):
                A dictionary of pre-defined categories and dimensions. Defaults to None.

            units (dict[str, Definition] | None, optional):
                A dictionary of pre-defined units. Defaults to None.
        """
        self.dimensions: dict[str, Dimension] = {}
        self.units: dict[str, Definition] = {}
        self.aliases: dict[str, Definition] = {}

        # Add each category individually to validate it
        if categories:
            for name, dimension in categories.items():
                self.add_category(name, dimension)

        # Add each unit individually to validate it
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
        self.units[definition.name] = definition

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
        # Try to convert a unit string to a unit definition.
        if isinstance(unit, str):
            unit = self.get_definition(unit)

        if not isinstance(unit, Definition):
            raise ConverterError(f"{unit} is not a valid unit definition")

        if not alias or not isinstance(alias, str):
            raise ConverterError(f"{unit} has an invalid alias {alias!r}")

        self.aliases[alias] = unit

    def add_category(self, category: str, dimension: Dimension) -> None:
        """ Add a new category to the dictionary.

        Args:
            category (str): A category name. Must be unique.
            dimension (Dimension): The dimension associated with the category.

        Raises:
            ConverterError: If the category name already exists.
        """
        if category in self.dimensions:
            raise ConverterError(f"{category} is already defined")
        else:
            self.dimensions[category] = dimension

    def get_unit(self, name: str, exponent: int = 1) -> Unit:
        """ Get a unit by name, symbol, or alias.

        Args:
            name (str): A unit name, symbol, or alias.
            exponent (int, optional): Unit exponent. Defaults to 1.

        Raises:
            ConverterError: If no unit could be found.

        Returns:
            Unit: The unit instance.
        """
        try:
            unit = self.aliases[name]
            return Unit(unit.factor, unit.name, unit.dimen) ** exponent
        except KeyError:
            raise ConverterError(f"{name} is not a valid unit")

    def get_definition(self, name: str) -> Definition:
        """ Get a unit definition from a unit name, symbol, or alias.

        Args:
            name (str): A unit name, symbol, or alias.

        Raises:
            ConverterError: If the unit could not be found.

        Returns:
            Definition: The unit definition.
        """
        try:
            return self.aliases[name]
        except KeyError:
            raise ConverterError(f"{name} is not a valid unit")

    def get_category(self, unit: Unit) -> str | None:
        """ Get the category of a pre-defined unit.

        Args:
            unit (Unit): The unit instance.

        Raises:
            ConverterError: If the unit is the wrong type.

        Returns:
            str | None: The category name, or None if the unit isn't defined.
        """
        if not isinstance(unit, Unit):
            raise ConverterError(f"{unit} is not a valid unit")

        try:
            return self.units[unit.name].category
        except KeyError:
            pass

        # Check if there's a single matching category+dimension
        matching = [name for name, dimen in self.dimensions.items() if dimen == unit.dimen]
        if len(matching) == 1:
            return matching[0]

        return None
