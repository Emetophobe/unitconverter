
# Copyright (c) 2022-2023 Mike Cunningham


from decimal import Decimal

from unitconverter.dimensions import get_category
from unitconverter.exceptions import UnitError
from unitconverter.utils import parse_decimal


class Unit:
    """ A unit of measurement. """

    def __init__(self,
                 name: str,
                 category: str,
                 symbol: str = None,
                 plural: str = None,
                 aliases: list[str] = None,
                 factor: Decimal | int | str = 1,
                 power: int = 1,
                 prefix_scale: str = None,
                 prefix_exclude: list[str] = None,
                 is_prefixed: bool = False
                 ) -> None:
        """ Initialize unit.

        Parameters
        ----------
        name : str
            unit name

        category : str
            unit category

        symbol : str, optional
            unit symbol or short form, by default None

        plural : str, optional
            unit plural form, by default None

        factor : Decimal | int | str, optional
            conversion factor, by default 1

        power : int, optional
            scale power, by default 1

        prefix_scale : str, optional
            prefix scale option, by default None

        prefix_exclude : str, optional
            list of prefixes to exclude, by default None

        is_prefixed : bool, optional
            whether the unit is prefixed, by default False

        """
        self.name = name
        self.category = category
        self.symbol = symbol or name
        self.plural = plural or name
        self.aliases = aliases or []

        self.factor = parse_decimal(factor, f'{name} has an invalid factor {factor}')

        self.power = power

        self.prefix_scale = prefix_scale
        self.prefix_exclude = prefix_exclude or []
        self.prefixed = is_prefixed

    def names(self) -> set[str]:
        """ Get unique unit names and symbols. """
        return set([self.name, self.symbol, self.plural] + self.aliases)

    def __mul__(self, other):
        if not isinstance(other, (Unit, CompositeUnit)):
            raise UnitError(f'Cannot multiply Unit and {type(other)}')

        return CompositeUnit([self, other], [], self.factor * other.factor)

    def __truediv__(self, other):
        if not isinstance(other, (Unit, CompositeUnit)):
            raise UnitError(f'Cannot divide Unit and {type(other)}')

        return CompositeUnit([self], [other], self.factor / other.factor)

    def __repr__(self) -> str:
        args = ', '.join(repr(val) for val in self.__dict__.values())
        return f'Unit({args})'

    def __str__(self) -> str:
        return self.name


class CompositeUnit:

    def __init__(self, numers, denoms=None, name=None, category=None,
                 symbol=None, plural=None, factor=None):
        self.numers = numers

        if denoms:
            self.denoms = denoms
        else:
            self.denoms = []

        if factor is None:
            self.factor = self._calculate_factor()
        else:
            self.factor = factor

        self.name = name or self._join_names('name')
        self.category = get_category(category or self._join_names('category'))
        self.symbol = symbol or self._join_names('symbol')
        self.plural = plural or self._join_plural()

    def _join_names(self, attr: str) -> str:
        numer = '*'.join(getattr(numer, attr) for numer in self.numers)
        if not self.denoms:
            return numer

        denom = '*'.join(getattr(denom, attr) for denom in self.denoms)
        return numer + '/' + denom

    def _join_plural(self) -> str:
        """ Create a plural unit name. Only pluralizes the last numerator unit.
            i.e "newton-metre" becomes "newton-metres"
        """
        numers = []
        for index, unit in enumerate(self.numers):
            if index == len(self.numers) - 1:
                numers.append(unit.plural)
            else:
                numers.append(unit.name)

        numer = '*'.join(numers)

        if not self.denoms:
            return numer

        denom = '*'.join(denom.name for denom in self.denoms)
        return numer + '/' + denom

    def _calculate_factor(self) -> Decimal:
        """ Calculate factor by parsing numers and denoms. """
        numer_factor = 1
        for numer in self.numers:
            numer_factor *= numer.factor

        if not self.denoms:
            return numer_factor

        denom_factor = 1
        for denom in self.denoms:
            denom_factor *= denom.factor

        return numer_factor / denom_factor

    def __mul__(self, other):
        if not isinstance(other, (Unit, CompositeUnit)):
            raise UnitError(f'Cannot multiply CompositeUnit and {type(other)}')

        return CompositeUnit([self, other], [], self.factor * other.factor)

    def __truediv__(self, other):
        if not isinstance(other, (Unit, CompositeUnit)):
            raise UnitError(f'Cannot divide CompositeUnit and {type(other)}')

        return CompositeUnit([self], [other], self.factor / other.factor)

    def __repr__(self) -> str:
        args = ", ".join(str(s) for s in self.__dict__.values())
        return f'CompositeUnit({args})'

    def __str__(self) -> str:
        return self.name
