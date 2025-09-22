# Copyright (c) 2022-2025 Mike Cunningham
# https://www.github.com/emetophobe/unitconverter


from collections import defaultdict
from collections.abc import Mapping
from typing import Iterator, Self

from unitconverter.formatting import format_display_name


class Dimension(Mapping):
    """ All unit dimensions are represented using a custom exponent dictionary.

        For convenience passing a string creates an equivalent dictionary:

            >> Dimension("time") == Dimension({"time": 1})
            True

        Dimensions can be divided to create new dimensions:

            >> length = Dimension("length")
            >> time = Dimension("time")

            >> speed = length / time

            >> dict(speed)
            {'length': 1, 'time': -1}

            >> str(speed)
            'length/time'

        Multiplication and exponentiation are also supported:

            >> area = length * length
            >> dict(area)
            {'length': 2}

            >> volume = length ** 3
            >> dict(volume)
            {'length': 3}

    """

    def __init__(self,  dimension: str | Self | dict[str, int] | None = None) -> None:
        """ Create a new dimension. """

        if dimension is None:
            dimension = {}

        elif isinstance(dimension, str) and dimension != "":
            dimension = {dimension: 1}

        elif isinstance(dimension, Dimension):
            dimension = dimension.dimension

        elif not isinstance(dimension, dict):
            raise TypeError(f"{dimension!r} is not a valid dimension")

        self.dimension = defaultdict(int, dimension)

    @property
    def name(self):
        """ Get a string representation of the dimension. """
        return format_display_name(list(self.items()))

    def __pow__(self, exponent: int) -> Self:
        """ Raise a dimension to a new power. Returns a new dimension. """
        if not isinstance(exponent, int):
            return NotImplemented

        if exponent == 1:
            return self

        if exponent == 0:
            raise ValueError("exponent must be a non-zero integer")

        # Pow just multiplies all exponents
        dimension = self.dimension.copy()
        for name in dimension.keys():
            dimension[name] *= exponent

        return self.__class__(dimension)

    def __mul__(self, other: Self) -> Self:
        """ Multiply a dimension with another dimension. Returns a new dimension. """
        if not isinstance(other, Dimension):
            return NotImplemented

        dimension = self.dimension.copy()
        for name, exponent in other.items():
            dimension[name] += exponent
            if not dimension[name]:
                del dimension[name]

        return self.__class__(dimension)

    def __truediv__(self, other: Self) -> Self:
        """ Divide a dimension with another dimension. Returns a new dimension. """
        if not isinstance(other, Dimension):
            return NotImplemented

        dimension = self.dimension.copy()
        for name, exponent in other.items():
            dimension[name] -= exponent
            if not dimension[name]:
                del dimension[name]

        return self.__class__(dimension)

    def __getitem__(self, key: str) -> int:
        return self.dimension[key]

    def __iter__(self) -> Iterator:
        return iter(self.dimension)

    def __len__(self) -> int:
        return len(self.dimension)

    def __repr__(self) -> str:
        return f"Dimension({dict(self.dimension)!r})"

    def __str__(self) -> str:
        return self.name
