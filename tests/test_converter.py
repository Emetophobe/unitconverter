# Copyright (c) 2022-2023 Mike Cunningham


import json
import unittest
from decimal import Decimal, getcontext

from unitconverter.converter import convert, format_decimal, parse_unit
from unitconverter.exceptions import CategoryError, UnitError


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

        with open('tests/test_data.json', 'r') as infile:
            tests = json.load(infile)

        # Run all tests from the json file
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

        # Test multi-word prefix generated units
        unit = parse_unit('cubic kilometre')
        self.assertEqual(unit.plural, 'cubic kilometres')
        self.assertEqual(unit.symbol, 'km3')

        # Test invalid unit names
        with self.assertRaises(UnitError):
            parse_unit('invalid unit')

        # Test invalid prefixes (units that don't support prefix scaling)
        with self.assertRaises(UnitError):
            parse_unit('kilodegrees')

        # Test invalid prefixes (units that don't support that type of prefix)
        with self.assertRaises(UnitError):
            parse_unit('picobyte')

    def test_format_decimal(self):
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
