# Copyright (c) 2022-2025 Mike Cunningham
# https://www.github.com/emetophobe/unitconverter


from unitconverter.exceptions import ConverterError
from unitconverter.models.dimension import Dimension
from unitconverter.models.prefix import get_prefixes
from unitconverter.models.unit import Unit


class Registry:
    """ The registry is used to store pre-defined units.

        Use add_unit() to add a unit to the registry.
        Use get_unit() to get a unit from the registry.
    """

    def __init__(self,
                 dimensions: dict[str, Dimension] | None = None,
                 units: dict[str, Unit] | None = None
                 ) -> None:
        """ Create a new registry.

        Parameters
        ----------
        dimensions : `dict[str, Dimension]` | None, optional
            A dictionary of pre-defined dimensions, by default None

        units : `dict[str, Unit]` | None, optional
            A dictionary of pre-defined units, by default None
        """
        self.dimensions: dict[str, Dimension] = {}
        self.units: dict[str, Unit] = {}

        # Add each category individually to validate them
        if dimensions:
            for name, dimension in dimensions.items():
                self.add_dimension(name, dimension)

        # Add each unit individually to validate them
        if units:
            for unit in units.values():
                self.add_unit(unit)

    def add_unit(self, unit: Unit) -> Unit:
        """ Add a unit to the registry.

        Parameters
        ----------
        unit : `Unit`
            The unit instance.

        Raises
        ------
        `ConverterError`
            If the unit contains a duplicate name or symbol.
        """
        for name in unit.names():
            self.add_alias(unit, name)

        # Also add prefixed versions if the unit supports it
        for prefix in get_prefixes(unit.prefixes):
            name = prefix.name + unit.name
            symbols = [prefix.symbol + symbol for symbol in unit.symbols]
            aliases = [prefix.name + alias for alias in unit.aliases]
            factor = prefix.factor * unit.factor

            self.add_unit(Unit(name, symbols, aliases, unit.category, unit.dimen,
                               factor, prefixes=None))

        return unit

    def add_alias(self, unit: Unit, alias: str) -> None:
        """ Add a unit name, symbol, or alias.

        Parameters
        ----------
        unit : `Unit`
            The unit to alias.
        alias : `str`
            A name, symbol, or alias.

        Raises
        ------
        `ConverterError`
            If the unit or alias is invalid.
        """

        if not isinstance(unit, Unit):
            raise ConverterError(f"{unit!r} is not a Unit instance")

        if not isinstance(alias, str) or not alias:
            raise ConverterError(f"{alias!r} is not a valid alias")

        if alias in self.units:
            raise ConverterError(f"{alias} is already defined by {self.units[alias]}")

        # Add the reference
        self.units[alias] = unit

    def add_dimension(self, name: str, dimension: Dimension) -> None:
        """ Add a dimension to the registry.

        Parameters
        ----------
        name : str
            The name of the dimension (i.e length)
        dimension : Dimension
            The dimension to add.

        Raises
        ------
        ConverterError
            If the dimension name is already defined.
        """
        if name in self.dimensions:
            raise ConverterError(f"{name} is already defined")

        self.dimensions[name] = dimension

    def get_unit(self, name: str) -> Unit:
        """ Get a unit by name, symbol, or alias.
            Raises a ConverterError if name is undefined.
        """
        try:
            return self.units[name]
        except KeyError:
            raise ConverterError(f"{name} is not defined")

    def get_dimension(self, name: str) -> Dimension:
        """ Get a dimension by name.
            Raises ConverterError if name is undefined.
        """
        try:
            return self.dimensions[name]
        except KeyError:
            raise ConverterError(f"{name} is not a defined dimension")
