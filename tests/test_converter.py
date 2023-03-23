# Copyright (c) 2022-2023 Mike Cunningham

import json
from decimal import Decimal
from pathlib import Path
from tests import AbstractTestCase, format_decimal


class TestConverter(AbstractTestCase):
	""" Test convert() and format_decimal() """

	def test_convert(self) -> None:
		""" Test convert method using values from json. """
		for filename in Path('tests/data').glob('*.json'):
			with open(filename, 'r', encoding='utf-8') as infile:
				self.assert_units(json.load(infile))

	def test_format_decimal(self):
		""" Test formatting decimals. """
		value = Decimal('1785137.3268163479138125')

		# Assert decimal to string
		result = format_decimal(value)
		self.assertEqual('1785137.3268163479138125', result, 'Invalid result')

		msg = 'Invalid {} result'

		# Assert decimal to rounded string
		result = format_decimal(value, precision=5)
		self.assertEqual('1785137.32682', result, msg.format('rounded'))

		# Assert decimal to exponent string
		result = format_decimal(value, exponent=True)
		self.assertEqual('1.7851373268163479138125E+6', result, msg.format('exponent'))

		# Assert decimal to comma separated string
		result = format_decimal(value, commas=True)
		self.assertEqual('1,785,137.3268163479138125', result, msg.format('separated'))

		# Assert decimal to rounded exponent string
		result = format_decimal(value, exponent=True, precision=5)
		self.assertEqual('1.78514E+6', result, msg.format('rounded exponent'))

		# Assert decimal to rounded comma separated string
		result = format_decimal(value, precision=7, commas=True)
		self.assertEqual('1,785,137.3268163', result, msg.format('rounded separated'))

		# Assert that a ValueError is raised when an incorrect value is passed
		with self.assertRaises(ValueError):
			format_decimal('bad value')

		# Assert that a ValueError is raised when an incorrect precision is passed
		with self.assertRaises(ValueError):
			format_decimal(value, precision='bad precision')

	def test_parse_unit(self) -> None:
		""" Test unit parsing. """
		unit = self.converter.parse_unit('microinch')
		self.assertEqual(unit.name, 'microinch')

		unit = self.converter.parse_unit('ml')
		self.assertEqual(unit.name, 'milliliter')

		unit = self.converter.parse_unit('cubic kilometer')
		self.assertEqual(unit.name, 'cubic kilometer')
		self.assertTrue('km^3' in unit.symbols)

		with self.assertRaises(ValueError):
			self.converter.parse_unit('invalid_unit')
