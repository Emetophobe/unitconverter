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
				 prefix_index=-1,
				 prefix_scaling='si'):
		""" Initialize unit.

		Args:
			name (str):
				unit name.

			symbols (str | list, optional):
				unit symbol or list of symbols. Defaults to None.

			aliases (str | list, optional):
				unit alias or list of aliases. Defaults to None.

			factor (str | Decimal, optional):
				conversion factor. Defaults to '1'.

			power (str | Decimal, optional):
				optional power. Defaults to '1'.

			offset (str | Decimal, optional):
				optional offset. Defaults to '0'.

			category (str, optional):
				_description_. Defaults to None.

			prefix_index (int, optional):
				index of word in a multi-word argument. Defaults to -1 (last word).

			prefix_scaling (str, optional):
				type of prefix scaling that the unit supports. Defaults to 'si'.
		"""
		self.name = name
		self.symbols = self._parse_string_list(symbols)
		self.aliases = self._parse_string_list(aliases)
		self.factor = Decimal(factor)
		self.power = Decimal(power)
		self.offset = Decimal(offset)
		self.category = category

		# Check if prefix index is valid
		items = name.rsplit(' ', maxsplit=1)
		if prefix_index < -1 or prefix_index > len(items)-1:
			raise ValueError(f'prefix index must be between -1 and {len(items)-1}')

		# Prefix scaling options
		self.prefix_index = prefix_index
		self.prefix_scaling = prefix_scaling

	def add_prefix(self, factor: str, symbol: str, prefix: str):
		""" Create a new unit from an existing unit by applying a prefix.

		Args:
			factor (str):
				multiplication factor.

			symbol (str):
				prefix symbol.

			prefix (str):
				prefix name.

		Returns:
			Unit: a new unit instance.
		"""

		# Update names and factor
		name = self._add_prefix(prefix, self.name)
		symbols = [self._add_prefix(symbol, name) for name in self.symbols]
		aliases = [self._add_prefix(prefix, name) for name in self.aliases]
		factor = Decimal(factor) * Decimal(self.factor)

		# Create new unit
		return Unit(name,
					symbols=symbols,
					aliases=aliases,
					factor=Decimal(factor) ** self.power,
					power=self.power,
					offset=self.offset,
					category=self.category,
					prefix_index=self.prefix_index,
					prefix_scaling=self.prefix_scaling)

	def _add_prefix(self, prefix: str, name: str) -> str:
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

		# Add prefix to the word at prefix index
		split = name.rsplit(' ', maxsplit=1)
		split[self.prefix_index] = prefix + split[self.prefix_index]
		return ' '.join(split)

	def _parse_string_list(self, argument: Optional[Union[str, list[str]]]) -> list[str]:
		""" Parse argument and return a list of strings.

		Args:
			argument (str | list[str], optional): a str, list of str, or None.

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

	def __contains__(self, name: str) -> bool:
		""" Returns True if name matches one of the unit names. """
		return name == self.name or name in self.symbols or name in self.aliases

	def __str__(self) -> str:
		return f'{self.name}, {self.factor}, {self.symbols}, {self.aliases}'