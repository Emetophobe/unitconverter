# Copyright (c) 2022-2025 Mike Cunningham


from typing import Self

from unitconverter.exceptions import DimensionError
from unitconverter.formatting import format_display_name, format_type


class Dimensions(dict):
    """ Used to store units and dimensions and their exponents. """

    def __init__(self, units: str | dict[str, int] | None = None) -> None:
        """ Initialize dictionary. """
        if units:
            if isinstance(units, str):
                super().__init__({units: 1})
            elif isinstance(units, dict):
                super().__init__(units)
            else:
                raise DimensionError(f"{units} is not a valid dimension")

    def __pow__(self, exponent: int) -> Self:
        if not exponent or not isinstance(exponent, int):
            raise DimensionError(f"{exponent} must be a positive or negative integer")

        # Pow just multiplies all exponents
        units = self.copy()
        for name in units.keys():
            units[name] *= exponent

        return self.__class__(units)

    def __mul__(self, other: object) -> Self:
        if not isinstance(other, dict):
            raise DimensionError(f"Cannot multiply Dimensions and {format_type(other)})")

        # Multiply just adds exponents from both dictionaries
        units = self.copy()
        for name, exp in other.items():
            units[name] = units.get(name, 0) + exp
            if not units[name]:
                del units[name]

        return self.__class__(units)

    def __truediv__(self, other: object) -> Self:
        if not isinstance(other, dict):
            raise DimensionError(f"Cannot divide Dimensions and {format_type(other)})")

        # Divide just subtracts exponents from both dictionaries
        units = self.copy()
        for name, exp in other.items():
            units[name] = units.get(name, 0) - exp
            if not units[name]:
                del units[name]

        return self.__class__(units)

    def __repr__(self) -> str:
        return f"Dimensions({super().__repr__()})"

    def __str__(self) -> str:
        return format_display_name(self)
