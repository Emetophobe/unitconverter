# Copyright (c) 2022-2025 Mike Cunningham
# https://www.github.com/emetophobe/unitconverter


from unitconverter.exceptions import ConverterError, DuplicateUnitError, InvalidUnitError
from unitconverter.models.prefix import get_prefixes
from unitconverter.models.unit import Unit


class Registry:
    """ The registry is used to store pre-defined units.

        Use add_unit() to add a unit to the registry.
        Use get_unit() to get a unit from the registry.
    """

    def __init__(self, units: dict[str, Unit] | None = None) -> None:
        """ Create a unit registry.

        Parameters
        ----------
        units : dict[str, Unit] | None, optional
            A dictionary of pre-defined units, by default None
        """
        self.units: dict[str, Unit] = {}

        if units:
            for unit in units.values():
                self.add_unit(unit)

    def add_unit(self, unit: Unit) -> Unit:
        """ Add a unit to the registry.

        Parameters
        ----------
        unit : Unit
            The unit instance

        Raises
        ------
        ConverterError
            If the unit contains a duplicate name or symbol
        """
        for name in unit.names:
            self.add_alias(unit, name)

        # Also add prefixed versions if the unit supports it
        for prefix in get_prefixes(unit._prefixes):
            name = prefix.name + unit.name
            symbols = [prefix.symbol + symbol for symbol in unit.symbols]
            aliases = [prefix.name + alias for alias in unit.aliases]
            factor = prefix.factor * unit.factor

            # Make sure prefixes=None to prevent re-prefixing and also infinite
            self.add_unit(Unit(name, symbols, aliases, unit._dimension,
                               factor, prefixes=None))

        return unit

    def add_alias(self, unit: Unit, alias: str) -> None:
        """ Add a unit alias.

        Parameters
        ----------
        unit : Unit
            The unit to alias

        alias : str
            A unique name, symbol, or alias

        Raises
        ------
        ConverterError
            The unit or alias is invalid

        DuplicateUnitError
            The alias is already in use
        """

        if not isinstance(unit, Unit):
            raise ConverterError(f"{unit!r} is not a valid unit type")

        if not isinstance(alias, str) or not alias:
            raise ConverterError(f"{alias!r} is not a valid unit alias")

        if alias in self.units:
            raise DuplicateUnitError(alias, self.units[alias].name)

        # Add the reference
        self.units[alias] = unit

    def get_unit(self, name: str) -> Unit:
        """ Get a unit by name, symbol, or alias.
            Raises InvalidUnitError if the name is undefined.
        """
        try:
            return self.units[name]
        except KeyError:
            raise InvalidUnitError(name)
