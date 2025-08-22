# Copyright (c) 2022-2025 Mike Cunningham
# https://www.github.com/emetophobe/unitconverter


from __future__ import annotations

from decimal import Decimal


from unitconverter.exceptions import ConverterError
from unitconverter.formatting import format_display_name, format_type
from unitconverter.models.dimension import Dimension
from unitconverter.utils import parse_decimal


class BaseUnit:
    """ Abstract base class. Don't use this directly. """

    @property
    def name(self) -> str:
        raise NotImplementedError

    @property
    def symbols(self) -> list[str]:
        raise NotImplementedError

    @property
    def aliases(self) -> list[str]:
        raise NotImplementedError

    @property
    def factor(self) -> Decimal:
        raise NotImplementedError

    @property
    def units(self) -> list[tuple[Unit, int]]:
        raise NotImplementedError

    @property
    def dimension(self) -> Dimension:
        raise NotImplementedError

    @property
    def names(self) -> list[str]:
        """ Get a list of all unit names, symbols, and aliases. """
        return [self.name] + self.symbols + self.aliases

    def __mul__(self, other: BaseUnit) -> BaseUnit:
        """ Multiply a Unit with another Unit. Returns a new CompositeUnit. """
        if isinstance(other, BaseUnit):
            return CompositeUnit(self.units + other.units)

        raise ConverterError(f"Can't multiply {format_type(self)} and {format_type(other)}")

    def __truediv__(self, other: BaseUnit) -> BaseUnit:
        """ Divide a Unit with another Unit. Returns a new CompositeUnit. """
        if isinstance(other, BaseUnit):
            units = [(unit, -exponent) for unit, exponent in other.units]
            return CompositeUnit(self.units + units)

        raise ConverterError(f"Can't divide {format_type(self)} and {format_type(other)}")

    def __pow__(self, exponent: int) -> BaseUnit:
        """ Raise a unit to a new exponent. Returns a Unit or CompositeUnit. """
        if not isinstance(exponent, int) or exponent == 0:
            raise ConverterError("exponent must be a non-zero integer")

        if exponent == 1:
            return self

        units = [(unit, exp * exponent) for unit, exp in self.units]
        return CompositeUnit(units)

    def __repr__(self) -> str:
        return "BaseUnit()"

    def __str__(self) -> str:
        return self.name


class Unit(BaseUnit):
    """ A basic unit of measurement.

        Use Unit() if you want to create units that live outside of a registry.
        Use registry.add_unit() if you want to add units to a specific registry.

    """

    def __init__(self,
                 name: str,
                 symbols: list[str] | None = None,
                 aliases: list[str] | None = None,
                 dimen: Dimension | None = None,
                 factor: Decimal | str | int = 1,
                 prefixes: str | None = None
                 ) -> None:
        """ Create a new unit.

        Parameters
        ----------
        name : str
            The unit name

        symbols : list[str] | None, optional
            A list of unit symbols, by default None

        aliases : list[str] | None, optional
            A list of unit aliases, by default None

        dimension : Dimension | None, optional
            The dimension of the unit, by default None

        factor : Decimal | str | int, optional
            The conversion factor, by default 1

        prefixes : str | None, optional
            If the unit supports metric or binary prefixes, by default None
        """
        self._name = name
        self._symbols = symbols or []
        self._aliases = aliases or []
        self._dimension = Dimension(dimen)
        self._factor = parse_decimal(factor)
        self._prefixes = prefixes

    @property
    def name(self) -> str:
        return self._name

    @property
    def symbols(self) -> list[str]:
        return self._symbols

    @property
    def aliases(self) -> list[str]:
        return self._aliases

    @property
    def factor(self) -> Decimal:
        return self._factor

    @property
    def units(self) -> list[tuple[Unit, int]]:
        return [(self, 1)]

    @property
    def dimension(self) -> Dimension:
        return self._dimension

    def __repr__(self) -> str:
        return (f"Unit({self._name!r}, {self._symbols!r}, {self._aliases!r},"
                f" {self._dimension!r}, {self._factor!r}, {self._prefixes!r})")


class CompositeUnit(BaseUnit):
    """ A composite unit is made up of one or more units and their exponents. """

    def __init__(self, units: list[tuple[Unit, int]], reduce: bool = True) -> None:
        """ Create a composite unit.

        Parameters
        ----------
        units : list[tuple[Unit, int]]
            A list of unit and exponent tuples

        reduce: bool
            Reduce units to simpler terms, by default True
        """
        self._units = self._reduce_units(units) if reduce else units
        self._reduce = reduce

        factor = Decimal(1)
        dimension = Dimension()
        names = []

        # Compute factor, dimension, and name from the list of units
        for unit, exponent in self._units:
            factor *= unit.factor ** exponent
            dimension *= unit.dimension ** exponent
            names.append((unit.name, exponent))

        self._factor = factor
        self._dimension = dimension
        self._name = format_display_name(names)

    @property
    def name(self) -> str:
        return self._name

    @property
    def symbols(self) -> list[str]:
        return []

    @property
    def aliases(self) -> list[str]:
        return []

    @property
    def factor(self) -> Decimal:
        return self._factor

    @property
    def units(self) -> list[tuple[Unit, int]]:
        return self._units

    @property
    def dimension(self) -> Dimension:
        return self._dimension

    def _reduce_units(self, units: list[tuple[Unit, int]]) -> list[tuple[Unit, int]]:
        """ Reduce units if possible. """
        reduced = []
        exponents = []

        for unit, exponent in units:
            if unit not in reduced:
                reduced.append(unit)
                exponents.append(exponent)
            else:
                index = reduced.index(unit)
                exponents[index] += exponent

                if exponents[index] == 0:
                    reduced.pop(index)
                    exponents.pop(index)

        # All composite unit instances must have atleast 1 unit
        if not reduced or not exponents:
            name = format_display_name([(unit.name, exponent) for unit, exponent in units])
            raise ConverterError(f"{name!r} is not a valid unit")

        return list(zip(reduced, exponents))

    def __repr__(self) -> str:
        return f"CompositeUnit({self._units}, {self._reduce})"


# Special "one" unit for things like the reciprocal second (1/s)
one = Unit("1")
