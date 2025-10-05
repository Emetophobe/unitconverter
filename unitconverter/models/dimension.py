# Copyright (c) 2022-2025 Mike Cunningham
# https://www.github.com/emetophobe/unitconverter


from typing import Self
from unitconverter.formatting import format_display_name


class Dimension(dict[str, int]):
    """ All unit dimensions are represented using a custom exponent dictionary.

    For convenience passing a string creates a dictionary with 1 as the exponent:

        >>> Dimension("time") == Dimension({"time": 1})
        True

    Dimensions can be divided to create new dimensions:

        >>> length = Dimension("length")
        >>> time = Dimension("time")
        >>> speed = length / time

        >>> dict(speed)
        {'length': 1, 'time': -1}

        >>> str(speed)
        'length/time'

    Multiplication and exponentiation are also supported:

        >>> area = length * length
        >>> dict(area)
        {'length': 2}

        >>> volume = length ** 3
        >>> dict(volume)
        {'length': 3}
    """

    def __init__(self, dimension: str | dict[str, int] | None = None) -> None:
        """ Create a new dimension. """
        if dimension is None:
            super().__init__()
        elif isinstance(dimension, str) and dimension != "":
            super().__init__({dimension: 1})
        elif isinstance(dimension, dict):
            super().__init__(dimension)
        else:
            raise TypeError(f"{dimension!r} is not a valid dimension")

    @property
    def name(self):
        """ Get a string representation of the dimension. """
        return format_display_name(list(self.items()))

    def __mul__(self, other: Self) -> Self:
        """ Multiply a dimension with another dimension. Returns a new dimension. """
        if not isinstance(other, Dimension):
            return NotImplemented

        dimension = self.copy()
        for name, exponent in other.items():
            dimension[name] = dimension.get(name, 0) + exponent
            if not dimension[name]:
                del dimension[name]

        return self.__class__(dimension)

    def __truediv__(self, other: Self) -> Self:
        """ Divide a dimension with another dimension. Returns a new dimension. """
        if not isinstance(other, Dimension):
            return NotImplemented

        dimension = self.copy()
        for name, exponent in other.items():
            dimension[name] = dimension.get(name, 0) - exponent
            if not dimension[name]:
                del dimension[name]

        return self.__class__(dimension)

    def __pow__(self, exponent: int) -> Self:
        """ Raise a dimension to a new power. Returns a new dimension. """
        if not isinstance(exponent, int):
            return NotImplemented

        if exponent == 0:
            raise ValueError("exponent must be a non-zero integer")

        dimension = self.copy()
        for name in dimension.keys():
            dimension[name] *= exponent

        return self.__class__(dimension)

    def __repr__(self) -> str:
        return f"Dimension({super().__repr__()})"

    def __str__(self) -> str:
        return self.name
