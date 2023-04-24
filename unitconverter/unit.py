# Copyright (c) 2022-2023 Mike Cunningham


from decimal import Decimal

from unitconverter.exceptions import UnitError
from unitconverter.utils import parse_decimal


class Unit:
    """ A unit of measurement. """

    def __init__(self,
                 name: str,
                 category: str,
                 symbols: list[str] = None,
                 aliases: list[str] = None,
                 factor: Decimal | int | str = 1,
                 prefix_scale: str = None,
                 prefix_power: int = 1,
                 prefix_exclude: list[str] = None):
        """ Initialize unit

        Parameters
        ----------
        name : str
            unit name

        category : str
            unit category

        symbols : list[str], optional
            list of unit symbols, by default None

        aliases : list[str], optional
            list of additional unit names or aliases, by default None

        factor : Decimal | int | str, optional
            conversion factor, by default 1

        prefix_scale : str, optional
            prefix scale option, by default None

        prefix_power : int, optional
            prefix scale power, by default 1

        prefix_exclude : str, optional
            list of prefixes to exclude, by default None
        """
        self.name = name
        self.category = category
        self.symbols = symbols or []
        self.aliases = aliases or []

        self.factor = parse_decimal(factor, f'{name} has an invalid factor {factor}')

        self.prefix_scale = prefix_scale
        self.prefix_power = prefix_power
        self.prefix_exclude = prefix_exclude or []

    def convert_from(self, value: Decimal) -> Decimal:
        return value * Decimal(self.factor)

    def convert_to(self, value: Decimal) -> Decimal:
        return value / Decimal(self.factor)

    def names(self) -> list[str]:
        """ Get a list of all unit names and symbols. """
        return [self.name] + self.symbols + self.aliases

    def __contains__(self, name: str) -> bool:
        """ Returns True if name matches one of the unit names. """
        return name in self.names()

    def __repr__(self) -> str:
        args = ', '.join(repr(s) for s in self.__dict__.values())
        return f'Unit({args})'

    def __str__(self) -> str:
        return self.name


class TemperatureUnit(Unit):
    """ Temperature units use a custom converter. """

    def __init__(self, name, category, symbols=None, aliases=None, factor=1,
                 prefix_scale=None, prefix_power=1, prefix_exclude=None):
        """ Create a new temperature unit. """
        super().__init__(name, category, symbols, aliases, factor, prefix_scale,
                         prefix_power, prefix_exclude)

    def convert_from(self, value: Decimal) -> Decimal:
        """ Convert from value to kelvin. """
        if self.name == 'kelvin':
            return value
        elif self.name == 'celsius':
            return value + Decimal('273.15')
        elif self.name == 'fahrenheit':
            return (value + Decimal('459.67')) * Decimal(5) / Decimal(9)
        elif self.name == 'rankine':
            return value * Decimal(5) / Decimal(9)
        else:
            raise UnitError(f'Unsupported temperature unit: {self.name}')

    def convert_to(self, value: Decimal) -> Decimal:
        """ Convert kelvin to value. """
        if self.name == 'kelvin':
            return value
        elif self.name == 'celsius':
            return value - Decimal('273.15')
        elif self.name == 'fahrenheit':
            return value * Decimal(9) / Decimal(5) - Decimal('459.67')
        elif self.name == 'rankine':
            return value * Decimal(9) / Decimal(5)
        else:
            raise UnitError(f'Unsupported temperature unit: {self.name}')
