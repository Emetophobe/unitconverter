# Copyright (c) 2022-2025 Mike Cunningham
# https://www.github.com/emetophobe/unitconverter


from __future__ import annotations

from unitconverter.exceptions import ConverterError
from unitconverter.formatting import format_display_name, format_type


class Dimension(dict):
    """ All units and dimensions can be expressed using a simple exponent dictionary. """

    def __init__(self, dimension: str | dict[str, int] | None = None) -> None:
        """ Create a new dimension.

        Parameters
        ----------
        dimension : `str` | `dict[str, int]` | `None`, optional
            A dimension name or dictionary, by default None

        Raises
        ------
        ConverterError
            If the dimension argument is invalid.
        """
        if dimension:
            if isinstance(dimension, str):
                super().__init__({dimension: 1})
            elif isinstance(dimension, dict):
                super().__init__(dimension)
            else:
                raise ConverterError(f"{dimension!r} is not a valid dimension")

    def __pow__(self, exponent: int) -> Dimension:
        """ Raise a dimension to a new power. Returns a new dimension."""
        if not exponent or not isinstance(exponent, int):
            raise ConverterError(f"{exponent} must be a positive or negative integer")

        # Pow just multiplies all exponents
        dimen = self.copy()
        for name in dimen.keys():
            dimen[name] *= exponent

        return Dimension(dimen)

    def __mul__(self, other: dict) -> Dimension:
        """ Multiply two dimensions. Returns a new dimension. """
        if not isinstance(other, dict):
            raise ConverterError(f"Cannot multiply Dimension and {format_type(other)}")

        # Multiply just adds exponents from both dictionaries
        dimen = self.copy()
        for name, exp in other.items():
            dimen[name] = dimen.get(name, 0) + exp
            if not dimen[name]:
                del dimen[name]

        return Dimension(dimen)

    def __truediv__(self, other: dict) -> Dimension:
        """ Divide two dimensions. Returns a new dimension. """
        if not isinstance(other, dict):
            raise ConverterError(f"Cannot divide Dimension and {format_type(other)}")

        # Divide just subtracts exponents from both dictionaries
        dimen = self.copy()
        for name, exp in other.items():
            dimen[name] = dimen.get(name, 0) - exp
            if not dimen[name]:
                del dimen[name]

        return Dimension(dimen)

    def __repr__(self) -> str:
        return f"Dimension({super().__repr__()})"

    def __str__(self) -> str:
        return format_display_name(self)
