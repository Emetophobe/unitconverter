# Copyright (c) 2022-2023 Mike Cunningham

import json
from decimal import Decimal
from pathlib import Path
from tests import AbstractTestCase, format_decimal


class TestConverter(AbstractTestCase):
    """ Test converter """

    def test_parse_unit(self) -> None:
        """ Test unit parsing. """

        unit = self.converter.parse_unit('microinch')
        self.assertEqual(unit.name, 'microinch')

        unit = self.converter.parse_unit('ml')
        self.assertEqual(unit.name, 'milliliter')

        with self.assertRaises(ValueError):
            self.converter.parse_unit('invalid_unit')

    def test_convert(self) -> None:
        """ Test unit conversions. """
        for category, units in self.converter.units.items():
            # Assert that the unit category exists
            self.assertTrue(category in self.converter.units.keys(),
                            f'Invalid category: {category!r}')

            # Assert that the test data exists
            filename = Path(f'tests/data/test_{category.replace(" ", "_")}.json')
            self.assertTrue(filename.exists(), f'Missing test file: {filename}')

            # Load test data
            with open(filename, 'r', encoding='utf-8') as infile:
                expected_values = json.load(infile)

            # Assert that all unit names are in the test dictionary
            for unitname in units.keys():
                self.assertTrue(unitname in expected_values.keys(),
                                f'Missing test unit: {unitname!r} ({category})')

            # Assert that all units convert to the expected values
            base_unit = list(units.keys())[0]
            self.assert_units(base_unit, expected_values)

    def test_format_decimal(self):
        """ Test formatting decimals. """
        value = Decimal('1785137.3268163479138125')

        # Assert decimal to string
        result = format_decimal(value)
        self.assertEqual('1785137.3268163479138125', result, 'Invalid result')

        # Assert decimal to rounded string
        result = format_decimal(value, precision=5)
        self.assertEqual('1785137.32682', result, 'Invalid rounded result')

        # Assert decimal to exponent string
        result = format_decimal(value, exponent=True)
        self.assertEqual('1.7851373268163479138125E+6', result, 'Invalid exponent result')

        # Assert decimal to comma separated string
        result = format_decimal(value, commas=True)
        self.assertEqual('1,785,137.3268163479138125', result, 'Invalid separated result')

        # Assert decimal to rounded exponent string
        result = format_decimal(value, exponent=True, precision=5)
        self.assertEqual('1.78514E+6', result, 'Invalid rounded exponent result')

        # Assert decimal to rounded comma separated string
        result = format_decimal(value, precision=7, commas=True)
        self.assertEqual('1,785,137.3268163', result, 'Invalid rounded separated result')

        # Assert that a ValueError is raised when an incorrect value is passed
        with self.assertRaises(ValueError):
            format_decimal('bad data')

        # Assert that a ValueError is raised when an incorrect precision is passed
        with self.assertRaises(ValueError):
            format_decimal(value, precision="bad precision")
