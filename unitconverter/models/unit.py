# Copyright (c) 2022-2025 Mike Cunningham
# https://www.github.com/emetophobe/unitconverter


from fractions import Fraction
from typing import Self

from unitconverter.models.dimension import Dimension
from unitconverter.utils import parse_fraction


class Unit:
    """ A unit can represent a single unit or a composite unit. """

    def __init__(self,
                 factor: Fraction | str | int,
                 name: str | Dimension,
                 dimension: str | Dimension | None,
                 symbols: list[str] | None = None,
                 aliases: list[str] | None = None,
                 prefixes: str | None = None
                 ) -> None:
        """ Create a new unit.

        Parameters
        ----------
        factor : Fraction | str | int
            The conversion or multiplication factor.

        name : str | Dimension
            A unit name or a dictionary of unit names and exponents.

        dimension : Dimension | None
            A dimension name or dictionary of dimension names and exponents.

        symbols : list[str] | None, optional
            A list of unit symbols, by default None

        aliases : list[str] | None, optional
            A list of additional unit names or aliases, by default None

        prefixes: str | None, optional
            If the unit supports metric or binary prefixes, by default None
        """
        self.factor = parse_fraction(factor)
        self.units = Dimension(name)
        self.dimension = Dimension(dimension)
        self.symbols = symbols or []
        self.aliases = aliases or []
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
            return self.__class__(self.factor * other.factor,
                                  self.units * other.units,
                                  self.dimension * other.dimension)

        return NotImplemented

    def __truediv__(self, other: Self) -> Self:
        """ Divide a unit with another unit. Returns a new unit. """
        if isinstance(other, Unit):
            return self.__class__(self.factor / other.factor,
                                  self.units / other.units,
                                  self.dimension / other.dimension)

        return NotImplemented

    def __pow__(self, exponent: int) -> Self:
        """ Raise a unit to a new exponent. Returns a new unit. """
        if isinstance(exponent, int):
            if exponent == 0:
                raise ValueError("exponent must be a non-zero integer")

            return self.__class__(self.factor ** exponent,
                                  self.units ** exponent,
                                  self.dimension ** exponent)

        return NotImplemented

    def __eq__(self, other: object) -> bool:
        """ Compare two units for equality. """
        return (isinstance(other, Unit)
                and self.name == other.name
                and self.factor == other.factor
                and self.dimension == other.dimension
                and self.units == other.units)

    def __repr__(self) -> str:
        args = [repr(val) for val in self.__dict__.items()]
        return f"Unit({", ".join(args)})"

    def __str__(self) -> str:
        return self.name
