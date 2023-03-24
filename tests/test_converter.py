# Copyright (c) 2022-2023 Mike Cunningham

import json
from decimal import Decimal
from pathlib import Path
from tests import AbstractTestCase, format_decimal


class TestConverter(AbstractTestCase):
	""" Test Converter class. """

	def test_convert(self) -> None:
		""" Test convert() method. """
		all_units = set(unit.name for unit in self.converter.units)
		tested_units = set()

		# Load dicionaries of expected conversion values
		for filename in Path('tests/data').glob('*.json'):
			with open(filename, 'r', encoding='utf-8') as infile:
				# Test units
				units = json.load(infile)
				self.assert_units(units)

				# Add units to tested units
				for name, conversions in units.items():
					tested_units.add(name)
					for conversion in conversions:
						tested_units.add(conversion['dest'])

		# Calculate and print list of untested units
		untested_units = all_units - tested_units
		self.assertEqual(len(untested_units), 0, self.format_untested(untested_units))

	def test_format_decimal(self):
		""" Test format_decimal() method. """
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
		""" Test parse_unit() method. """
		# Test built-in units
		unit = self.converter.parse_unit('meter')
		self.assertEqual(unit.name, 'meter')

		# Test prefix generated units
		unit = self.converter.parse_unit('kiloliter')
		self.assertEqual(unit.name, 'kiloliter')

		# Test symbol generated units
		unit = self.converter.parse_unit('ml')
		self.assertEqual(unit.name, 'milliliter')

		# Test multi-word prefix generated units
		unit = self.converter.parse_unit('cubic kilometer')
		self.assertEqual(unit.name, 'cubic kilometer')
		self.assertTrue('km^3' in unit.symbols)

		# Test invalid unit names
		with self.assertRaises(ValueError):
			self.converter.parse_unit('invalid_unit')

		# Test invalid prefixes (units that don't support prefix scaling)
		with self.assertRaises(ValueError):
			self.converter.parse_unit('kilodegrees')

		# Test invalid prefixes (units that don't support that type of prefix)
		with self.assertRaises(ValueError):
			self.converter.parse_unit('picobyte')

	def format_untested(self, untested_units: set) -> str:
		""" Create an error message with all untested units. """
		msg = ['\n\nThe following units do not have unit tests:\n']
		for name in sorted(list(untested_units)):
			msg.append(name)
		return '\n'.join(msg)
