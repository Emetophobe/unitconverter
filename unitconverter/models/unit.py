
# Copyright (c) 2022-2025 Mike Cunningham


from decimal import Decimal
from typing import Self

from unitconverter.exceptions import ConverterError
from unitconverter.formatting import parse_decimal, format_display_name, format_type
from unitconverter.models.dimension import Dimension


class Unit:
    """ A unit of measurement. Can be a single unit or a composition of units. """

    def __init__(self,
                 factor: Decimal | int = 1,
                 units: Dimension | dict | str | None = None,
                 dimen: Dimension | dict | None = None
                 ) -> None:
        """ Create a new unit.

        Args:
            factor (Decimal | int, optional): The conversion factor. Defaults to 1.
            units (Dimension | dict | str | None, optional):
                A unit dictionary or a unit name. Defaults to None.
            dimen (Dimension | dict | None, optional):
                A dimension dictionary. Defaults to None.
        """
        self.factor = parse_decimal(factor)
        self.units = Dimension(units)
        self.dimen = Dimension(dimen)

    @property
    def name(self) -> str:
        """ Get a human readable string representation of the unit.

        Returns:
            str: The unit name.
        """
        return format_display_name(self.units)

    def __pow__(self, exponent: int) -> Self:
        """ Raise a unit to a new exponent. Creates a new unit.

        Args:
            exponent (int): An integer value.

        Raises:
            ConverterError: If the exponent isn't a positive or negative integer.

        Returns:
            Unit: The new unit.
        """
        if not exponent or not isinstance(exponent, int):
            raise ConverterError(f"{exponent} is not a positive or negative integer")

        return self.__class__(self.factor ** exponent,
                              self.units ** exponent,
                              self.dimen ** exponent)

    def __mul__(self, other: Self) -> Self:
        """ Multiply this unit with another unit. Creates a new unit.

        Args:
            other (Unit): The second unit.

        Raises:
            ConverterError: If the second unit is invalid.

        Returns:
            Unit: The new unit.
        """
        if not isinstance(other, Unit):
            raise ConverterError(f"Cannot multiply Unit and {format_type(other)})")

        return self.__class__(self.factor * other.factor,
                              self.units * other.units,
                              self.dimen * other.dimen)

    def __truediv__(self, other: Self) -> Self:
        """ Divide this unit with another unit. Creates a new unit.

        Args:
            other (Unit): The second unit.

        Raises:
            ConverterError: If the second unit is invalid.

        Returns:
            Unit: The new unit.
        """
        if not isinstance(other, Unit):
            raise ConverterError(f"Cannot divide Unit and {format_type(other)})")

        return self.__class__(self.factor / other.factor,
                              self.units / other.units,
                              self.dimen / other.dimen)

    def __repr__(self) -> str:
        return f"Unit({self.factor}, {self.units}, {self.dimen})"

    def __str__(self) -> str:
        return self.name
