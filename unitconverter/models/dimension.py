# Copyright (c) 2022-2025 Mike Cunningham
# https://www.github.com/emetophobe/unitconverter


from __future__ import annotations

from unitconverter.exceptions import ConverterError
from unitconverter.formatting import format_display_name


class Dimension(dict):
    """ All unit dimensions can be represented using a custom exponent dictionary. """

    def __init__(self, dimension: str | dict[str, int] | None = None) -> None:
        """ Create a new dimension.

        Parameters
        ----------
        dimension : str | dict[str, int] | None, optional
            A dimension name or dimension dictionary, by default None

        Raises
        ------
        ConverterError
            If the dimension is invalid
        """
        if isinstance(dimension, str) and dimension:
            super().__init__({dimension: 1})
        elif isinstance(dimension, dict):
            super().__init__(dimension)
        elif dimension is not None:
            raise ConverterError(f"{dimension!r} is not a valid dimension")

    @property
    def name(self):
        """ Convert dictionary into a human readable string. """
        return format_display_name(list(self.items()))

    def __pow__(self, exponent: int) -> Dimension:
        """ Raise a dimension to a new power. Returns a new dimension."""
        if not isinstance(exponent, int):
            return NotImplemented

        if exponent == 1:
            return self

        if exponent == 0:
            raise ConverterError(f"{exponent} must be a positive or negative integer")

        # Pow just multiplies all exponents
        dimen = self.copy()
        for name in dimen.keys():
            dimen[name] *= exponent

        return Dimension(dimen)

    def __mul__(self, other: Dimension) -> Dimension:
        """ Multiply a dimension with another dimension. Returns a new dimension. """
        if not isinstance(other, Dimension):
            return NotImplemented

        # Multiply just adds exponents from both dictionaries
        dimension = self.copy()
        for name, exp in other.items():
            dimension[name] = dimension.get(name, 0) + exp
            if not dimension[name]:
                del dimension[name]

        return Dimension(dimension)

    def __truediv__(self, other: Dimension) -> Dimension:
        """ Divide a dimension with another dimension. Returns a new dimension. """
        if not isinstance(other, Dimension):
            return NotImplemented

        dimension = self.copy()
        for name, exp in other.items():
            dimension[name] = dimension.get(name, 0) - exp
            if not dimension[name]:
                del dimension[name]

        return Dimension(dimension)

    def __repr__(self) -> str:
        return f"Dimension({super().__repr__()})"

    def __str__(self) -> str:
        return self.name
