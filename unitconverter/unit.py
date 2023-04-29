
# Copyright (c) 2022-2023 Mike Cunningham


from decimal import Decimal
from typing import Self

from unitconverter.dimensions import dimension_name
from unitconverter.exceptions import UnitError
from unitconverter.formatting import parse_decimal, format_display_name


class Unit:

    """ A unit of measurement. Can be a single unit or a composition of units. """

    def __init__(self, factor: Decimal = 1, units: tuple | dict = None) -> None:
        """ Initialize unit. """

        self.factor = parse_decimal(factor)

        if not units:
            self.units = {}
        elif isinstance(units, tuple):
            self.units = {units: 1}
        elif isinstance(units, dict):
            self.units = dict(units)
        else:
            raise UnitError(f'Invalid unit: {units}')

        # Generate unit name and category
        self._name = format_display_name(self.get_units())
        self._category = dimension_name(self.get_dimensions())

    @property
    def name(self):
        return self._name

    @property
    def category(self):
        return self._category

    def get_units(self) -> dict[str, int]:
        """ Return a dictionary of the units and their exponents. """
        return {unit[0]: exp for unit, exp in self.units.items()}

    def get_dimensions(self) -> dict[str, int]:
        """ Return a tuple of the dimensions and their exponents. """
        return {unit[1]: exp for unit, exp in self.units.items()}

    def __pow__(self, other: int) -> Self:
        if not isinstance(other, int):
            raise UnitError(f'Cannot pow Unit and {type(other)})')

        if other == 0:
            raise UnitError('Cannot pow Unit by 0. Must be a positive'
                            ' or negative integer.')

        # Pow just multiplies all exponents
        units = self.units.copy()
        for name in units.keys():
            units[name] *= other

        return Unit(self.factor ** other, units)

    def __mul__(self, other: Self) -> Self:
        if not isinstance(other, Unit):
            raise UnitError(f'Cannot multiply Unit and {type(other)})')

        # Multiply just adds exponents from both dictionaries
        units = self.units.copy()
        for name, exp in other.units.items():
            units[name] = units.get(name, 0) + exp
            if not units[name]:
                del units[name]

        return Unit(self.factor * other.factor, units)

    def __truediv__(self, other: Self) -> Self:
        if not isinstance(other, Unit):
            raise UnitError(f'Cannot divide Unit and {type(other)})')

        # Divide just subtracts exponents from both dictionaries
        units = self.units.copy()
        for name, exp in other.units.items():
            units[name] = units.get(name, 0) - exp
            if not units[name]:
                del units[name]

        return Unit(self.factor / other.factor, units)

    def __iter__(self):
        return iter(self.units)

    def __len__(self) -> int:
        return len(self.units)

    def __eq__(self, other: Self) -> bool:
        if not isinstance(other, Unit):
            return False

        return self.units == other.units

    def __contains__(self, name: str) -> bool:
        return name in self.units

    def __repr__(self) -> str:
        return f'Unit({self.factor}, {self.units})'

    def __str__(self) -> str:
        return self.name


def dump_unit(unit: Unit) -> None:
    """ Helper to print a unit to stdout. """
    print('name:     ', unit.name)
    print('category: ', unit.category)
    print('units:    ', unit.units)
