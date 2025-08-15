# Copyright (c) 2022-2025 Mike Cunningham
# https://www.github.com/emetophobe/unitconverter


from typing import Self

from unitconverter.exceptions import ConverterError
from unitconverter.formatting import format_display_name, format_type


class Dimension(dict):
    """ All units and dimensions can be expressed using a simple exponent dictionary. """

    def __init__(self, units: str | dict[str, int] | None = None) -> None:
        """ Create a new dimension.

        Parameters
        ----------
        units : `str` | `dict[str, int]` | `None`, optional
            A dimension name or dictionary, by default None

        Raises
        ------
        ConverterError
            If the dimen argument was invalid.
        """
        if units:
            if isinstance(units, str):
                super().__init__({units: 1})
            elif isinstance(units, dict):
                super().__init__(units)
            else:
                raise ConverterError(f"{units!r} is not a str or dict")

    def __pow__(self, exponent: int) -> Self:
        """ Raise a dimension to a new power. Returns a new dimension."""
        if not exponent or not isinstance(exponent, int):
            raise ConverterError(f"{exponent} must be a positive or negative integer")

        # Pow just multiplies all exponents
        units = self.copy()
        for name in units.keys():
            units[name] *= exponent

        return self.__class__(units)

    def __mul__(self, other: Self) -> Self:
        """ Multiply two dimensions. Returns a new dimension. """
        if not isinstance(other, Dimension | dict):
            raise ConverterError(f"Cannot multiply Dimension and {format_type(other)})")

        # Multiply just adds exponents from both dictionaries
        units = self.copy()
        for name, exp in other.items():
            units[name] = units.get(name, 0) + exp
            if not units[name]:
                del units[name]

        return self.__class__(units)

    def __truediv__(self, other: object) -> Self:
        """ Divide two dimensions. Returns a new dimension. """
        if not isinstance(other, dict):
            raise ConverterError(f"Cannot divide Dimension and {format_type(other)})")

        # Divide just subtracts exponents from both dictionaries
        units = self.copy()
        for name, exp in other.items():
            units[name] = units.get(name, 0) - exp
            if not units[name]:
                del units[name]

        return self.__class__(units)

    def __repr__(self) -> str:
        return f"Dimension({super().__repr__()})"

    def __str__(self) -> str:
        return format_display_name(self)
