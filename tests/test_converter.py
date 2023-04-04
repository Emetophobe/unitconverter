# Copyright (c) 2022-2023 Mike Cunningham


import json
import unittest
from decimal import Decimal
from pathlib import Path

from unitconverter.exceptions import CategoryError, UnitError
from unitconverter.converter import convert, parse_unit, format_decimal
from unitconverter.registry import iter_units


class TestConverter(unittest.TestCase):
    """ Test Converter class. """

    def test_convert(self) -> None:
        """ Test convert() function. """
        all_units = set(unit.name for unit in iter_units())
        tested_units = set()

        # Load dicionaries of expected values
        for filename in Path('tests/data').glob('*.json'):
            with open(filename, 'r', encoding='utf-8') as infile:
                # Test units
                units = json.load(infile)
                for source, items in units.items():
                    for dest in items:
                        self.assert_conversion(source, **dest)

                # Update set of tested units
                for name, conversions in units.items():
                    tested_units.add(name)
                    for conversion in conversions:
                        tested_units.add(conversion['dest'])

        # Calculate and print list of untested units
        untested_units = all_units - tested_units
        self.assertEqual(len(untested_units), 0, self.format_untested(untested_units))

    def test_parse_unit(self) -> None:
        """ Test parse_unit() function. """
        # Test parsing simple built-in units.
        metre = parse_unit('metre')
        self.assertEqual(metre.name, 'metre')

        # Test prefix generated units
        kilolitre = parse_unit('kilolitre')
        self.assertEqual(kilolitre.name, 'kilolitre')

        # Assert that CategoryError is raised with incompatible units
        with self.assertRaises(CategoryError):
            convert(1, metre, kilolitre)

        # Test symbol generated units
        unit = parse_unit('ml')
        self.assertEqual(unit.name, 'millilitre')

        # Test multi-word prefix generated units
        unit = parse_unit('cubic kilometre')
        self.assertEqual(unit.name, 'cubic kilometre')
        self.assertTrue('km3' in unit.symbols)

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

        with self.assertRaises(ValueError):
            format_decimal('bad value')

        with self.assertRaises(ValueError):
            format_decimal(value, precision='bad precision')

    def assert_conversion(self, source, dest, expected, value=1):
        """ Assert that a unit conversion gives the expected result. """
        source = parse_unit(source)
        dest = parse_unit(dest)

        msg = f'{source.name!r} and {dest.name!r} have different categories'
        self.assertEqual(source.category, dest.category, msg)

        result = convert(value, source, dest)
        self.assertEqual(Decimal(expected), result, f'Incorrect conversion'
                         f' from {source.name!r} to {dest.name!r}')

    def format_untested(self, untested_units: set) -> str:
        """ Create display message with list of untested units. """
        msg = ['\n\nThe following units do not have unit tests:\n']
        for name in sorted(list(untested_units)):
            msg.append(name)
        return '\n'.join(msg)
