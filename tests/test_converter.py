# Copyright (c) 2022-2023 Mike Cunningham


import json
import unittest
from decimal import Decimal, getcontext
from pathlib import Path

from unitconverter.converter import (compatible_units, convert, convert_fuel,
                                     convert_temperature)
from unitconverter.exceptions import CategoryError, UnitError
from unitconverter.formatting import format_decimal


# Set decimal precision
getcontext().prec = 15


class TestConverter(unittest.TestCase):
    """ Test converter module. """

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

    def test_convert_temperature(self):
        """ Test convert_temperature() function. """
        result = convert_temperature(1, 'microkelvin', 'celsius')
        self.assertEqual(Decimal('-273.149999'), result)

        result = convert_temperature(32, 'celsius', 'fahrenheit')
        self.assertEqual(Decimal('89.6'), result)

        with self.assertRaises(UnitError):
            convert_temperature(1, 'kelvin', 'metre')

        with self.assertRaises(UnitError):
            convert_temperature(1, 'metre', 'celsius')

    def test_convert_fuel(self):
        """ Test convert_fuel() function. """
        result = convert_fuel(10, 'mpg', 'l/100km')
        self.assertEqual(Decimal('28.2480936331822'), result)

        with self.assertRaises(UnitError):
            convert_temperature(1, 'mpg', 'gal')

        with self.assertRaises(UnitError):
            convert_temperature(1, None, 'l/100km')

    def test_compatible_units(self):
        """ Test compatible_units() function. """
        from unitconverter.registry import get_category
        from unitconverter.unit import Unit

        second = Unit(1, 'second', {'time': 1})
        metre = Unit(1, 'metre', {'length': 1})
        inch = Unit('0.0254', 'inch', {'length': 1})

        second_category = get_category(second)
        metre_category = get_category(metre)
        inch_category = get_category(inch)

        self.assertTrue(compatible_units(metre_category, inch_category))
        self.assertFalse(compatible_units(second_category, metre_category))
