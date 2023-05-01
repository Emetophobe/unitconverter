
# Copyright (c) 2022-2023 Mike Cunningham


from decimal import Decimal
from typing import Self

from unitconverter.exceptions import UnitError
from unitconverter.formatting import parse_decimal, format_display_name


class UnitDict(dict):
    """ Internal dictionary used to store information about units and dimensions. """

    def __init__(self, units: str | dict = None) -> None:
        """ Initialize dictionary. """
        if units:
            if isinstance(units, str):
                super().__init__({units: 1})
            elif isinstance(units, dict):
                super().__init__(units)
            else:
                raise UnitError(f'Invalid unit or dimension: {units}')

    @property
    def name(self):
        """ Create name from units dictionary. """
        return format_display_name(self)

    def as_tuple(self):
        """ Create a hashable tuple from the dictionary. """
        return tuple(sorted(self.items()))

    def __pow__(self, other: int) -> Self:
        if not isinstance(other, int):
            raise UnitError(f'Cannot pow UnitDict and {type(other)})')

        if other == 0:
            raise UnitError('Cannot pow UnitDict by 0. Must be a positive'
                            ' or negative integer.')

        # Pow just multiplies all exponents
        units = self.copy()
        for name in units.keys():
            units[name] *= other

        return UnitDict(units)

    def __mul__(self, other: Self) -> Self:
        if not isinstance(other, dict):
            raise UnitError(f'Cannot multiply UnitDict and {type(other)})')

        # Multiply just adds exponents from both dictionaries
        units = self.copy()
        for name, exp in other.items():
            units[name] = units.get(name, 0) + exp
            if not units[name]:
                del units[name]

        return UnitDict(units)

    def __truediv__(self, other: Self) -> Self:
        if not isinstance(other, dict):
            raise UnitError(f'Cannot divide UnitDict and {type(other)})')

        # Divide just subtracts exponents from both dictionaries
        units = self.copy()
        for name, exp in other.items():
            units[name] = units.get(name, 0) - exp
            if not units[name]:
                del units[name]

        return UnitDict(units)

    def __repr__(self) -> str:
        return f'UnitDict({super().__repr__()})'

    def __str__(self) -> str:
        return self.name


class Unit:
    """ A unit of measurement. Can be a single unit or a composition of units. """

    def __init__(self,
                 factor: Decimal = 1,
                 units: str | UnitDict | dict = None,
                 dimen: UnitDict | dict = None
                 ) -> None:
        """ Initialize unit. """
        self.factor = parse_decimal(factor)
        self.units = UnitDict(units)
        self.dimen = UnitDict(dimen)

    @property
    def name(self):
        return self.units.name

    @property
    def dimension(self) -> str:
        if self.dimen.name:
            return self.dimen.name
        return 'dimensionless'

    def __pow__(self, other: int) -> Self:
        if not isinstance(other, int):
            raise UnitError(f'Cannot pow Unit and {type(other)})')

        if other == 0:
            raise UnitError('Cannot pow Unit by 0. Must be a positive'
                            ' or negative integer.')

        return Unit(self.factor ** other,
                    self.units ** other,
                    self.dimen ** other)

    def __mul__(self, other: Self) -> Self:
        if not isinstance(other, Unit):
            raise UnitError(f'Cannot multiply Unit and {type(other)})')

        return Unit(self.factor * other.factor,
                    self.units * other.units,
                    self.dimen * other.dimen)

    def __truediv__(self, other: Self) -> Self:
        if not isinstance(other, Unit):
            raise UnitError(f'Cannot divide Unit and {type(other)})')

        return Unit(self.factor / other.factor,
                    self.units / other.units,
                    self.dimen / other.dimen)

    def __eq__(self, other: Self) -> bool:
        if not isinstance(other, Unit):
            return False

        return self.units == other.units and self.dimen == other.dimen

    def __repr__(self) -> str:
        return f'Unit({self.factor}, {self.units}, {self.dimen})'

    def __str__(self) -> str:
        return self.name
