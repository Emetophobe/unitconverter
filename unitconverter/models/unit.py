# Copyright (c) 2022-2025 Mike Cunningham
# https://www.github.com/emetophobe/unitconverter


from __future__ import annotations

from decimal import Decimal


from unitconverter.exceptions import ConverterError
from unitconverter.formatting import format_display_name, format_type
from unitconverter.models.dimension import Dimension
from unitconverter.utils import parse_decimal


class BaseUnit:
    """ Abstract base class. Don't use this directly. """


class Unit(BaseUnit):
    """ A basic unit of measurement.

        Use Unit() if you want to create units that live outside of a registry.
        Use registry.add_unit() if you want to add units to a specific registry.

    """

    def __init__(self,
                 name: str,
                 symbols: list[str],
                 aliases: list[str],
                 category: str,
                 dimen: Dimension,
                 factor: Decimal | str | int = 1,
                 prefixes: str | None = None
                 ) -> None:
        """ Create a new unit.

        Parameters
        ----------
        name : str
            A unit name.
        symbols : list[str]
            A list of unit symbols.
        aliases : list[str]
            A list of unit aliases.
        category : str
            The category of the unit.
        dimen : Dimension
            The dimension of the unit.
        factor : Decimal | str | int, optional
            The conversion factor, by default 1
        prefixes : str | None, optional
            If the unit supports metric or binary prefixes, by default None
        """
        self.name = name
        self.symbols = symbols
        self.aliases = aliases
        self.category = category
        self.dimen = dimen
        self.factor = parse_decimal(factor)
        self.prefixes = prefixes

    def __mul__(self, other: UnitType) -> CompositeUnit:
        """ Multiply a Unit with another Unit. Returns a new CompositeUnit. """
        if isinstance(other, Unit):
            other = CompositeUnit(other.factor, other.name, other.dimen)
            return CompositeUnit(self.factor, self.name, self.dimen) * other

        elif isinstance(other, CompositeUnit):
            return CompositeUnit(self.factor, self.name, self.dimen) * other

        raise ConverterError("Can only multiply a Unit with an another Unit")

    def __truediv__(self, other: UnitType) -> CompositeUnit:
        """ Divide a Unit with another Unit. Returns a new CompositeUnit. """
        if isinstance(other, Unit):
            other = CompositeUnit(other.factor, other.name, other.dimen)
            return CompositeUnit(self.factor, self.name, self.dimen) / other

        elif isinstance(other, CompositeUnit):
            return CompositeUnit(self.factor, self.name, self.dimen) / other

        raise ConverterError("Can only multiply a Unit with an another Unit")

    def __pow__(self, exponent: int) -> CompositeUnit:
        """ Exponentiation returns a new CompositeUnit. """
        if isinstance(exponent, int) or exponent == 0:
            raise ConverterError(f"{exponent!r} must be a positive or negative integer")

        return CompositeUnit(self.factor, self.name, self.dimen) ** exponent

    def names(self) -> list[str]:
        """ Get all unit names, symbols, and aliases. """
        return [self.name] + self.symbols + self.aliases

    def __repr__(self) -> str:
        return (f"Unit({self.name!r}, {self.symbols!r}, {self.aliases!r}, {self.category!r},"
                f" {self.dimen!r}, {self.factor!r}, {self.prefixes!r})")

    def __str__(self) -> str:
        return self.name


class CompositeUnit(BaseUnit):
    """ A composite unit is made up of one or more units.

        For now units and their dimensions are stored in two separate dictionaries
        but this implementation detail will change in the future.
    """

    def __init__(self,
                 factor: Decimal | int = 1,
                 units: Dimension | dict[str, int] | str | None = None,
                 dimen: Dimension | dict[str, int] | None = None
                 ) -> None:
        """ Create a composite unit.

        Parameters
        ----------
        factor : `Decimal` | `int`, optional
            The composite unit factor, by default 1

        units : `Dimension` | `dict[str, int]` | `str` | `None`, optional
            A dictionary of unit names and their exponents, by default None

        dimen : `Dimension` | `dict[str, int]` | `None`, optional
            A dictionary of dimensions and their exponents, by default None
        """
        self.factor = parse_decimal(factor)
        self.units = Dimension(units)
        self.dimen = Dimension(dimen)

    @property
    def name(self) -> str:
        """ Convert dictionary of units into a human readable string. """
        return format_display_name(self.units)

    def __mul__(self, other: Unit | CompositeUnit) -> CompositeUnit:
        """ Multiply this unit with another unit. Returns a new CompositeUnit. """
        if isinstance(other, Unit):
            return CompositeUnit(self.factor * other.factor,
                                 self.units * Dimension(other.name),
                                 self.dimen * other.dimen)

        elif isinstance(other, CompositeUnit):
            return CompositeUnit(self.factor * other.factor,
                                 self.units * other.units,
                                 self.dimen * other.dimen)

        raise ConverterError(f"Cannot multiply CompositeUnit and {format_type(other)})")

    def __truediv__(self, other: Unit | CompositeUnit) -> CompositeUnit:
        """ Divide this unit with another unit. Returns a new CompositeUnit."""
        if isinstance(other, Unit):
            return CompositeUnit(self.factor / other.factor,
                                 self.units / Dimension(other.name),
                                 self.dimen / other.dimen)

        elif isinstance(other, CompositeUnit):
            return CompositeUnit(self.factor / other.factor,
                                 self.units / other.units,
                                 self.dimen / other.dimen)

        raise ConverterError(f"Cannot multiply CompositeUnit and {format_type(other)})")

    def __pow__(self, exponent: int) -> CompositeUnit:
        """ Exponentiation returns a new CompositeUnit. """
        if not exponent or not isinstance(exponent, int):
            raise ConverterError(f"{exponent} is not a positive or negative integer")

        return CompositeUnit(self.factor ** exponent,
                             self.units ** exponent,
                             self.dimen ** exponent)

    def __repr__(self) -> str:
        return f"CompositeUnit({self.factor}, {self.units}, {self.dimen})"

    def __str__(self) -> str:
        return format_display_name(self.units)


# Union of the two unit types for convenience
UnitType = Unit | CompositeUnit

# Special "one" unit for things like the reciprocal second (1/s)
one = Unit("one", [], [], "dimensionless", Dimension(), 1)
