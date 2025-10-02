# Copyright (c) 2022-2025 Mike Cunningham
# https://www.github.com/emetophobe/unitconverter


from unitconverter.exceptions import DuplicateUnitError, InvalidUnitError
from unitconverter.models.prefix import get_prefixes
from unitconverter.models.unit import BaseUnit, Unit


class Registry:
    """ The registry is used to store and retrieve pre-defined units. """

    def __init__(self, units: list[Unit] | None = None) -> None:
        """ Create a unit registry.

        Parameters
        ----------
        units : list[Unit] | None, optional
            A list of units, by default None
        """
        self.units: dict[str, BaseUnit] = {}

        if units is None:
            units = []

        elif not isinstance(units, list):
            raise TypeError(f"{units!r} is not a list of units")

        for unit in units:
            self.add_unit(unit)

    def add_unit(self, unit: Unit) -> None:
        """ Add a unit to the registry.

        If the unit supports metric or binary prefixes then this method
        will also create and register prefixed versions of the unit.

        Parameters
        ----------
        unit : Unit
            The unit instance
        """

        if not isinstance(unit, Unit):
            raise TypeError(f"{unit!r} is not a valid unit")

        # Add all unit names
        for name in unit.names:
            self.add_alias(name, unit)

        # Add prefixed versions of the unit if the unit supports it
        for prefix in get_prefixes(unit.prefixes):
            name = prefix.name + unit.name
            symbols = [prefix.symbol + symbol for symbol in unit.symbols]
            aliases = [prefix.name + alias for alias in unit.aliases]
            factor = prefix.factor * unit.factor

            # Make sure prefixes=None to prevent re-prefixing and infinite recursion
            self.add_unit(Unit(name, symbols, aliases, unit.dimension, factor))

    def add_alias(self, alias: str, unit: BaseUnit) -> None:
        """ Add a unit alias to the registry.

        Parameters
        ----------
        alias : str
            The unit name, symbol, or alias.
        unit : BaseUnit
            The unit instance to alias
        """

        if not alias or not isinstance(alias, str):
            raise TypeError(f"{alias!r} is not a valid unit alias")

        if not isinstance(unit, BaseUnit):
            raise TypeError(f"{unit!r} is not a valid unit")

        if alias in self.units:
            raise DuplicateUnitError(alias, self.units[alias].name)

        # Add the alias
        self.units[alias] = unit

    def get_unit(self, name: str) -> BaseUnit:
        """ Get a unit by name, symbol, or alias. """
        try:
            return self.units[name]
        except KeyError:
            raise InvalidUnitError(name)
