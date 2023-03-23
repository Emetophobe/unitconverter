# Copyright (c) 2022-2023 Mike Cunningham

from decimal import Decimal
from typing import Optional, Union


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
		self.symbols = string_to_list(symbols)
		self.aliases = string_to_list(aliases)
		self.factor = Decimal(factor)
		self.power = Decimal(power)
		self.offset = Decimal(offset)
		self.category = category
		self.scaling = scaling


	def add_prefix(self, factor: str, symbol: str, prefix: str):
		""" Create a new unit from an existing unit by applying a prefix.

		Args:
			factor (str): multiplication factor.
			symbol (str): symbol prefix.
			prefix (str): name prefix.

		Returns:
			Unit: a new unit instance.
		"""
		factor = Decimal(factor) * Decimal(self.factor)
		name = add_prefix(prefix, self.name)
		symbols = add_prefixes(symbol, self.symbols)
		aliases = add_prefixes(prefix, self.aliases)
		return Unit(name,
					symbols=symbols,
					aliases=aliases,
					factor=Decimal(factor) ** self.power,
					power=self.power,
					offset=self.offset,
					category=self.category,
					scaling=self.scaling)

	def __contains__(self, name: str) -> bool:
		return name == self.name or name in self.symbols or name in self.aliases

	def __str__(self) -> str:
		return f'{self.name}, {self.factor}, {self.symbols}, {self.aliases}'


def add_prefix(prefix: str, name: str) -> str:
	""" Add a prefix to a string; i.e "kilo" + "meter"

	Args:
		prefix (str): the prefix string or character.
		name (str): the base name; i.e "meter"

	Raises:
		TypeError: if an argument is an invalid type.

	Returns:
		str: the prefixed name.
	"""
	if not isinstance(prefix, str):
		raise TypeError('prefix must be a string.')

	if not isinstance(name, str):
		raise TypeError('name must be a string.')

	# Add prefix to the last word of a multi-word string
	split = name.rsplit(' ', maxsplit=1)
	split[-1] = prefix + split[-1]
	return ' '.join(split)


def add_prefixes(prefix: str, names: list[str]) -> list[str]:
	""" Add prefix to every name in a list.

	Args:
		prefix (str): the prefix string or character.
		names (list[str]): the list of names.

	Raises:
		TypeError: if an argument is an invalid type.

	Returns:
		list[str]: the list of prefixed names.
	"""
	if not isinstance(prefix, str):
		raise TypeError('prefix must be a string.')

	if not isinstance(names, list):
		raise TypeError('names must be a list of strings.')

	return [add_prefix(prefix, name) for name in names]


def string_to_list(argument: Optional[Union[str, list[str]]]) -> list[str]:
	""" Parse argument and return a list of strings.

	Args:
		argument (str | list[str], optional): a string, list of strings, or None.

	Raises:
		TypeError: if the argument is an invalid type.

	Returns:
		list[str]: a list of strings, or an empty list.
	"""
	if not argument:
		return []
	elif isinstance(argument, str):
		return [argument]
	elif isinstance(argument, list):
		return argument
	else:
		raise TypeError(f'argument must be a str, list, or None')
