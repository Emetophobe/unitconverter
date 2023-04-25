# Copyright (c) 2022-2023 Mike Cunningham


from decimal import Decimal

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

        self.prefixed = False

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
