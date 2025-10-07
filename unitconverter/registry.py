# Copyright (c) 2022-2025 Mike Cunningham
# https://www.github.com/emetophobe/unitconverter


from unitconverter.exceptions import DuplicateUnitError, InvalidUnitError
from unitconverter.models.prefix import get_prefixes
from unitconverter.models.unit import Unit


class Registry:
    """ The registry is used to store and retrieve pre-defined units. """

    def __init__(self, units: list[Unit] | tuple[Unit, ...] = ()) -> None:
        """ Create a unit registry.

        Parameters
        ----------
        units : list[Unit] | tuple[Unit, ...], optional
            A list or tuple of units, by default ()
        """
        self.units: dict[str, Unit] = {}

        for unit in units:
            self.add_unit(unit)

    def add_unit(self, unit: Unit) -> None:
        """ Add a unit to the registry.
            Also adds prefixed versions of the unit if the unit has a prefix setting.
        """
        validate_unit(unit)

        # Register all unit names and symbols
        for name in unit.names:
            self.add_alias(unit, name)

        # Register prefixed units if the unit has a list of prefixes
        for prefix in get_prefixes(unit.prefixes):
            factor = prefix.factor * unit.factor
            name = prefix.name + unit.name
            symbols = [prefix.symbol + symbol for symbol in unit.symbols]
            aliases = [prefix.name + alias for alias in unit.aliases]

            self.add_unit(Unit(name, factor, unit.dimension, symbols, aliases))

    def add_alias(self, unit: Unit, alias: str) -> None:
        """ Add a unit alias to the registry. """
        validate_unit(unit)
        validate_alias(alias)

        # Check for duplicate aliases
        if alias in self.units:
            raise DuplicateUnitError(alias, self.units[alias].name)

        # Add the unit reference
        self.units[alias] = unit

    def get_unit(self, name: str) -> Unit:
        """ Get a unit by name, symbol, or alias. """
        try:
            return self.units[name]
        except KeyError:
            raise InvalidUnitError(name) from None

    def clear(self) -> None:
        """ Clear the unit registry. """
        self.units.clear()


def validate_unit(unit: Unit) -> Unit:
    """ Check if the unit is valid. """
    if not isinstance(unit, Unit):
        raise TypeError(f"{unit!r} is not a valid unit")

    return unit


def validate_alias(alias: str) -> str:
    """ Check if a unit alias is valid. """
    if not alias or not isinstance(alias, str):
        raise TypeError(f"{alias!r} is not a valid unit alias")

    return alias
