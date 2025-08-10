# Copyright (c) 2022-2025 Mike Cunningham


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
        self._units = {}
        self._aliases = {}
        self._categories = {}

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

    def add_category(self, category: str, dimension: Dimension) -> None:
        """ Add a new category to the dictionary.

        Args:
            category (str): A category name. Must be unique.
            dimension (Dimension): The dimension associated with the category.

        Raises:
            ConverterError: If the category name already exists.
        """
        if category in self._categories:
            raise ConverterError(f"{category} is already defined"
                                 " (category names must be unique)")

        self._categories[category] = dimension

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

    def get_categories(self, dimension: Dimension) -> list[str]:
        """ Find all categories matching the specified dimension.

        Args:
            dimension (Dimension): A dimension instance.

        Raises:
            ConverterError: If the argument isn't a valid Dimension.

        Returns:
            list[str]: A list of category names, or an empty list if no category is found.
        """
        if not isinstance(dimension, Dimension):
            raise ConverterError(f"{dimension!r} is not a valid dimension")

        categories = []
        for category, dimen in self._categories.items():
            if dimension == dimen:
                categories.append(category)

        return categories

    def get_category(self, unit: Unit) -> str:
        """ Get the unit category name. """
        if not isinstance(unit, Unit):
            raise ConverterError(f"{unit} is not a valid Unit")

        # First check the unit definition for a category
        try:
            return self.get_definition(unit.name).category
        except ConverterError:
            pass

        # Try creating a category from the dimension
        categories = self.get_categories(unit.dimen)
        if categories:
            return ", ".join(categories)
        else:
            return "unknown category"
