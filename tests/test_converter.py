# Copyright (c) 2022-2023 Mike Cunningham


import json
import unittest
from decimal import Decimal
from pathlib import Path

from unitconverter.exceptions import CategoryError, UnitError
from unitconverter.converter import Converter, format_decimal


class TestConverter(unittest.TestCase):
    """ Test Converter class. """

    def setUp(self) -> None:
        """ Initialize converter """
        self.converter = Converter()

    def test_convert(self) -> None:
        """ Test convert() method. """
        all_units = set(unit.name for unit in self.converter.units)
        tested_units = set()

        # Load dicionaries of expected values
        for filename in Path('tests/data').glob('*.json'):
            with open(filename, 'r', encoding='utf-8') as infile:
                # Test units
                units = json.load(infile)
                self.assert_units(units)

                # Update set of tested units
                for name, conversions in units.items():
                    tested_units.add(name)
                    for conversion in conversions:
                        tested_units.add(conversion['dest'])

        # Calculate and print list of untested units
        untested_units = all_units - tested_units
        self.assertEqual(len(untested_units), 0, self.format_untested(untested_units))

    def test_parse_unit(self) -> None:
        """ Test parse_unit() method. """
        # Test parsing simple built-in units.
        metre = self.converter.parse_unit('metre')
        self.assertEqual(metre.name, 'metre')

        # Test prefix generated units
        kilolitre = self.converter.parse_unit('kilolitre')
        self.assertEqual(kilolitre.name, 'kilolitre')

        # Assert that CategoryError is raised with incompatible units
        with self.assertRaises(CategoryError):
            self.converter.convert(1, metre, kilolitre)

        # Test symbol generated units
        unit = self.converter.parse_unit('ml')
        self.assertEqual(unit.name, 'millilitre')

        # Test multi-word prefix generated units
        unit = self.converter.parse_unit('cubic kilometre')
        self.assertEqual(unit.name, 'cubic kilometre')
        self.assertTrue('km^3' in unit.symbols)

        # Test invalid unit names
        with self.assertRaises(UnitError):
            self.converter.parse_unit('invalid unit')

        # Test invalid prefixes (units that don't support prefix scaling)
        with self.assertRaises(UnitError):
            self.converter.parse_unit('kilodegrees')

        # Test invalid prefixes (units that don't support that type of prefix)
        with self.assertRaises(UnitError):
            self.converter.parse_unit('picobyte')

    def test_format_decimal(self):
        """ Test format_decimal() function. """
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

    def assert_unit(self,
                    source: str,
                    dest: str,
                    expected: str,
                    value: str = '1'
                    ) -> None:
        """ Assert that a unit conversion gives the expected result.

        Args:
            source (str):
                source unit name.

            dest (str):
                destination unit name.

            expected (str, Decimal):
                expected value.

            value (str, Decimal):
                value to convert. Defaults to '1'.
        """
        source = self.converter.parse_unit(source)
        dest = self.converter.parse_unit(dest)

        msg = f'{source.name!r} and {dest.name!r} have different categories'
        self.assertEqual(source.category, dest.category, msg)

        result = self.converter.convert(value, source, dest)

        msg = f'Incorrect conversion from {source.name!r} to {dest.name!r}'
        self.assertEqual(Decimal(expected), result, msg)

    def assert_units(self, test_data: dict) -> None:
        """ Assert that test data converts to the expected values.

        Args:
            source (str):
                source unit name.

            test_data (dict):
                dictionary of source units, destination units, and expected values.
        """
        for source, items in test_data.items():
            for dest in items:
                self.assert_unit(source, **dest)

    def format_untested(self, untested_units: set) -> str:
        """ Create an error message with all untested units. """
        msg = ['\n\nThe following units do not have unit tests:\n']
        for name in sorted(list(untested_units)):
            msg.append(name)
        return '\n'.join(msg)
