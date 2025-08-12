# Copyright (c) 2022-2025 Mike Cunningham
# https://www.github.com/emetophobe/unitconverter


from typing import Self

from unitconverter.exceptions import ConverterError
from unitconverter.formatting import format_display_name, format_type


class Dimension(dict):
    """ All units and dimensions can be expressed using a simple dictionary.

        For example speed is length over time which can be expressed as the dimension LT⁻¹
        An example speed unit would be metre/second which can be inverted to meter*second⁻¹

        Storing the dimension or units as dictionaries would look like this:

            >> dimension = {"length": 1, "time": -1}
            >> units = {"metre": 1, "second": -1}

        There's more to it than that but that's the basics of it. You can also create
        composite units very easily this way by multiplying or dividing units.
    """

    def __init__(self, units: str | dict[str, int] | None = None) -> None:
        """ Create a Dimension dictionary.

        Args:
            units (str | dict[str, int] | None, optional):
                A string or dictionary representation of the units. Defaults to None.

        Raises:
            ConverterError: If the units are invalid.
        """
        if units:
            if isinstance(units, str):
                super().__init__({units: 1})
            elif isinstance(units, dict):
                super().__init__(units)
            else:
                raise ConverterError(f"{units} is not a valid dimension")

    def __pow__(self, exponent: int) -> Self:
        """ Raise a dimension to a new exponent.

        Args:
            exponent (int): The integer value.

        Raises:
            ConverterError: If the exponent isn't valid.

        Returns:
            Self: _description_
        """
        if not exponent or not isinstance(exponent, int):
            raise ConverterError(f"{exponent} must be a positive or negative integer")

        # Pow just multiplies all exponents
        units = self.copy()
        for name in units.keys():
            units[name] *= exponent

        return self.__class__(units)

    def __mul__(self, other: Self) -> Self:
        """ Multiply two dimensions. Returns a new dimension.

        Args:
            other (Dimension): The second dimension.

        Raises:
            ConverterError: If the dimension is invalid.

        Returns:
            Dimension: A new dimension.
        """
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
        """ Divide two dimensions. Returns a new dimension.

        Args:
            other (Dimension): The second dimension.

        Raises:
            ConverterError: If the dimension is invalid.

        Returns:
            Dimension: A new dimension.
        """
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
