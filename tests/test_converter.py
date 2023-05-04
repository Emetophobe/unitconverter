# Copyright (c) 2022-2023 Mike Cunningham


import json
import unittest
from decimal import Decimal, getcontext
from pathlib import Path

from unitconverter.converter import convert, parse_unit
from unitconverter.exceptions import CategoryError, UnitError
from unitconverter.formatting import format_decimal, format_exponent


# Set decimal precision
getcontext().prec = 15


class TestConverter(unittest.TestCase):
    """ Test converting and unit parsing. """

    def test_convert(self) -> None:
        """ Test convert() function. """
        result = convert(1, 'inch', 'cm')
        self.assertIsInstance(result, Decimal)
        self.assertEqual(result, Decimal('2.54'), 'Invalid conversion')

        # Assert that UnitError is raised with invalid unit names
        with self.assertRaises(UnitError):
            convert(1, 'metre', 'invalid unit')

        # Assert that CategoryError is raised with incompatible units
        with self.assertRaises(CategoryError):
            convert(1, 'metre', 'litre')

        # Load test data
        test_files = Path('tests/test_data').glob('*.json')
        for filename in test_files:
            with open(filename, 'r') as infile:
                tests = json.load(infile)

            # Test all conversions
            for source, test_data in tests.items():
                for dest, expected in test_data.items():
                    result = convert(1, source, dest)
                    self.assertEqual(result, Decimal(expected), f'{source} to {dest}')

    def test_parse_unit(self) -> None:
        """ Test parse_unit() function. """
        # Test parsing simple built-in units.
        metre = parse_unit('metre')
        self.assertEqual(metre.name, 'metre')

        # Test prefix generated units
        kilolitre = parse_unit('kilolitre')
        self.assertEqual(kilolitre.name, 'kilolitre')

        # Test symbol generated units
        unit = parse_unit('ml')
        self.assertEqual(unit.name, 'millilitre')

        # Test exponent generated units
        unit = parse_unit('kilometre3')
        self.assertEqual(unit.name, format_exponent('kilometre', 3))
        self.assertEqual(unit.dimension, format_exponent('length', 3))

        # Test invalid unit names
        with self.assertRaises(UnitError):
            parse_unit('invalid unit')

        # Test invalid prefixes (units that don't support prefix scaling)
        with self.assertRaises(UnitError):
            parse_unit('kilodegrees')

        # Test invalid prefixes (units that don't support that type of prefix)
        with self.assertRaises(UnitError):
            parse_unit('picobyte')

    def test_format_decimal(self) -> None:
        """ Test format_decimal() function. """
        value = Decimal('1785137.3268163479138125')

        # Assert decimal to string
        result = format_decimal(value)
        self.assertEqual('1785137.3268163479138125', result, 'Invalid result')

        msg = 'Invalid {} result'

        # Rounded string
        result = format_decimal(value, precision=5)
        self.assertEqual('1785137.32682', result, msg.format('rounded'))

        # Exponent string
        result = format_decimal(value, exponent=True)
        self.assertEqual('1.7851373268163479138125E+6', result, msg.format('exponent'))

        # Comma separated string
        result = format_decimal(value, commas=True)
        self.assertEqual('1,785,137.3268163479138125', result, msg.format('separated'))

        # Rounded exponent string
        result = format_decimal(value, exponent=True, precision=5)
        self.assertEqual('1.78514E+6', result, msg.format('rounded exponent'))

        # Rounded comma separated string
        result = format_decimal(value, precision=7, commas=True)
        self.assertEqual('1,785,137.3268163', result, msg.format('rounded separated'))

        # Removing trailing zeroes
        result = format_decimal(Decimal('1.23456789000000100000'))
        self.assertEqual('1.234567890000001', result, msg.format('trailing zeroes'))

        with self.assertRaises(ValueError):
            format_decimal('bad value')

        with self.assertRaises(ValueError):
            format_decimal(value, precision='bad precision')
