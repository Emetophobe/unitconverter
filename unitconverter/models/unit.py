# Copyright (c) 2022-2025 Mike Cunningham
# https://www.github.com/emetophobe/unitconverter


from fractions import Fraction
from typing import Self

from unitconverter.models.dimension import Dimension
from unitconverter.utils import parse_fraction


class Unit:
    """ A unit can represent a single unit or a composite unit. """

    def __init__(self,
                 name: str | Dimension,
                 factor: Fraction | str | int,
                 dimension: str | Dimension,
                 symbols: list[str] | None = None,
                 aliases: list[str] | None = None,
                 prefixes: str | None = None
                 ) -> None:
        """ Create a new unit.

        Parameters
        ----------
        name : str | Dimension
            A unit name or a dictionary of unit names and exponents.

        factor : Fraction | str | int
            The conversion or multiplication factor.

        dimension : str | Dimension
            A dimension name or dictionary of dimension names and exponents.

        symbols : list[str] | None, optional
            A list of unit symbols, by default None

        aliases : list[str] | None, optional
            A list of additional unit names or aliases, by default None

        prefixes: str | None, optional
            If the unit supports metric or binary prefixes, by default None
        """
        self.units = Dimension(name)
        self.factor = parse_fraction(factor)
        self.dimension = Dimension(dimension)
        self.symbols = symbols or []  # TODO: handle composite symbols
        self.aliases = aliases or []  # TODO: handle composite aliases
        self.prefixes = prefixes

    @property
    def name(self) -> str:
        """ Get the canonical unit name. """
        return self.units.name

    @property
    def names(self) -> list[str]:
        """ Get a list of all unit names and symbols. """
        return [self.name] + self.symbols + self.aliases

    def __mul__(self, other: Self) -> Self:
        """ Multiply a unit with another unit. Returns a new unit. """
        if isinstance(other, Unit):
            return self.__class__(self.units * other.units,
                                  self.factor * other.factor,
                                  self.dimension * other.dimension)
        return NotImplemented

    def __truediv__(self, other: Self) -> Self:
        """ Divide a unit with another unit. Returns a new unit. """
        if isinstance(other, Unit):
            return self.__class__(self.units / other.units,
                                  self.factor / other.factor,
                                  self.dimension / other.dimension)
        return NotImplemented

    def __pow__(self, exponent: int) -> Self:
        """ Raise a unit to a new exponent. Returns a new unit. """
        if isinstance(exponent, int):
            if exponent == 0:
                raise ValueError("exponent must be a non-zero integer")

            return self.__class__(self.units ** exponent,
                                  self.factor ** exponent,
                                  self.dimension ** exponent)

        return NotImplemented

    def __eq__(self, other: object) -> bool:
        """ Compare two units for equality. """
        return (isinstance(other, Unit)
                and self.name == other.name
                and self.factor == other.factor
                and self.dimension == other.dimension
                and self.symbols == other.symbols
                and self.aliases == other.aliases)

    def __repr__(self) -> str:
        return f"Unit({self.name}, {self.factor}, {self.dimension}"

    def __str__(self) -> str:
        return self.name
