# Copyright (c) 2022-2025 Mike Cunningham


import tomllib

from decimal import Decimal
from pathlib import Path

from unitconverter.dimension import Dimension
from unitconverter.exceptions import DefinitionError, UnitError
from unitconverter.prefixes import get_prefixes
from unitconverter.registry import Definition
from unitconverter.unit import Unit


class Registry:

    def __init__(self) -> None:
        """ Initialize dimensions and units. """
        self._dimensions: dict[str, Dimension] = {}
        self._units: dict[str, Definition] = {}
        self._aliases: dict[str, Definition] = {}

        self.load_dimensions()
        self.load_units()

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

    def get_categories(self, unit: Unit) -> list[str]:
        """ Get a list of categories matching the unit's dimensions.
            An empty list is returned if no pre-defined categories match the unit's dimensions."""
        if not isinstance(unit, Unit):
            raise UnitError(f"{unit!r} is not a valid unit")

        categories = []
        for category, dimen in self._dimensions.items():
            if dimen == unit.dimen:
                categories.append(category)

        return categories

    def load_dimensions(self) -> None:
        """ Load common dimension names. """
        with open("data/dimensions.toml", "rb") as fp:
            self._dimensions = tomllib.load(fp, parse_float=Decimal)

    def load_units(self) -> None:
        """ Load pre-defined units. """
        for filename in Path("data/units").rglob("*.toml"):
            with open(filename, "rb") as fp:
                data = tomllib.load(fp, parse_float=Decimal)

            # Make sure to pop dimension to separate it from the unit data
            try:
                dimension = data.pop("dimension")
            except KeyError:
                raise DefinitionError("Unit file is missing dimension", filename)

            # Parse toml dictionary into unit definitions
            for name, args in data.items():
                # Required arguments
                try:
                    factor = args["factor"]
                except KeyError:
                    raise DefinitionError(f"{name} is missing a conversion factor", filename)

                # Optional arguments
                symbols = args.get("symbols", [])
                aliases = args.get("aliases", [])
                prefix = args.get("prefix", None)

                try:
                    definition = Definition(name, symbols, aliases, factor, dimension, prefix)
                    self.add_definition(definition)
                except DefinitionError as e:
                    raise DefinitionError(e.msg, filename)

    def __contains__(self, unit: str) -> bool:
        """ Returns true if a unit name is in the registry. """
        return unit in self._aliases
