
# Copyright (c) 2022-2025 Mike Cunningham


from decimal import Decimal
from typing import Self

from unitconverter.dimensions import Dimensions
from unitconverter.exceptions import UnitError
from unitconverter.formatting import parse_decimal, format_display_name, format_type


class Unit:
    """ A unit of measurement. Can be a single unit or a composition of units. """

    def __init__(self,
                 factor: Decimal | int = 1,
                 units: Dimensions | dict | str | None = None,
                 dimen: Dimensions | dict | str | None = None
                 ) -> None:
        """ Initialize unit. """
        self.factor = parse_decimal(factor)
        self.units = Dimensions(units)
        self.dimen = Dimensions(dimen)

    @property
    def name(self) -> str:
        """ Returns a formatted unit name. """
        return format_display_name(self.units)

    @property
    def dimension(self) -> str:
        """ Returns a formatted dimension name. """
        return format_display_name(self.dimen, True) or "dimensionless"

    def __pow__(self, exponent: int) -> Self:
        if not exponent or not isinstance(exponent, int):
            raise UnitError(f"{exponent} is not a positive or negative integer")

        return self.__class__(self.factor ** exponent,
                              self.units ** exponent,
                              self.dimen ** exponent)

    def __mul__(self, other: Self) -> Self:
        if not isinstance(other, Unit):
            raise UnitError(f"Cannot multiply Unit and {format_type(other)})")

        return self.__class__(self.factor * other.factor,
                              self.units * other.units,
                              self.dimen * other.dimen)

    def __truediv__(self, other: Self) -> Self:
        if not isinstance(other, Unit):
            raise UnitError(f"Cannot divide Unit and {format_type(other)})")

        return self.__class__(self.factor / other.factor,
                              self.units / other.units,
                              self.dimen / other.dimen)

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Unit) and self.units == other.units and self.dimen == other.dimen

    def __repr__(self) -> str:
        return f"Unit({self.factor}, {self.units}, {self.dimen})"

    def __str__(self) -> str:
        return self.name
