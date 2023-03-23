# Copyright (c) 2022-2023 Mike Cunningham

from decimal import Decimal
from typing import Union


class Unit:
    """ A unit of measurement. """

    def __init__(self,
                 name,
                 symbols=None,
                 aliases=None,
                 factor='1',
                 power='1',
                 offset='0',
                 category=None,
                 scaling='si'):
        """ Initialize unit.

        Args:
            name (str):
                _description_

            symbols (str | list, optional):
                _description_. Defaults to None.

            aliases (str | list, optional):
                _description_. Defaults to None.

            factor (str | Decimal, optional):
                _description_. Defaults to '1'.

            power (str | Decimal, optional):
                _description_. Defaults to '1'.

            offset (str | Decimal, optional):
                _description_. Defaults to '0'.

            category (str, optional):
                _description_. Defaults to None.

            scaling (str, optional):
                _description_. Defaults to 'si'.
        """
        self.name = name
        self.symbols = string_or_list(symbols)
        self.aliases = string_or_list(aliases)
        self.factor = Decimal(factor)
        self.power = Decimal(power)
        self.offset = Decimal(offset)
        self.category = category
        self.scaling = scaling

    def new_unit(self, factor: str, symbol: str, prefix: str):
        """ Create a new unit from an existing unit.

        Args:
            factor (str): multiplication factor
            symbol (str): symbol prefix.
            prefix (str): name prefix.

        Returns:
            Unit: a new unit instance.
        """
        factor = Decimal(factor) * Decimal(self.factor)
        name = add_prefix(prefix, self.name)
        symbols = add_prefixes(symbol, self.symbols)
        aliases = add_prefixes(prefix, self.aliases)
        #print('new factor:', factor)
        #print('new name:', name)
        #print('new symbols:', symbols)
        #print('new aliases:', aliases)
        return Unit(name,
                    symbols=symbols,
                    aliases=aliases,
                    factor=Decimal(factor) ** self.power,
                    power=self.power,
                    offset=self.offset,
                    scaling=self.scaling,
                    category=self.category)

    def __contains__(self, name: str) -> bool:
        return name == self.name or name in self.symbols or name in self.aliases

    def __str__(self) -> str:
        return f'{self.name}, {self.factor}, {self.symbols}, {self.aliases}'


def add_prefix(prefix: str, name: str) -> str:
    if not isinstance(name, str):
        raise TypeError('name must be a string.')

    split = name.rsplit(' ', maxsplit=1)
    split[-1] = prefix + split[-1]
    return ' '.join(split)


def add_prefixes(prefix: str, names: list[str]) -> list[str]:
    if not isinstance(names, list):
        raise TypeError('names must be a list of strings.')

    return [add_prefix(prefix, name) for name in names]


def string_or_list(argument: Union[str, list]) -> list[str]:
    """ Get string or list of strings from an argument. """
    if not argument:
        return []
    elif isinstance(argument, str):
        return [argument]
    elif isinstance(argument, list):
        return argument
    else:
        raise TypeError(f'argument must be a str, list, or None')
