# Copyright (c) 2022-2023 Mike Cunningham


import json
import unittest
from decimal import Decimal
from pathlib import Path

from unitconverter.converter import convert, parse_unit
from unitconverter.registry import iter_units


class TestData(unittest.TestCase):
    """ Test pre-defined unit data. """

    def test_data(self) -> None:
        """ Test all pre-defined unit conversions. """
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

    def assert_conversion(self, source: str, dest: str, expected: str,
                          value: Decimal | int | str = 1):
        """ Assert that a unit conversion gives the expected result. """
        source = parse_unit(source)
        dest = parse_unit(dest)

        self.assertEqual(source.category, dest.category, f'{source.name!r} and'
                         f' {dest.name!r} have different categories')

        result = convert(value, source, dest)
        self.assertEqual(Decimal(expected), result, f'Incorrect conversion'
                         f' from {source.name!r} to {dest.name!r}')

    def format_untested(self, untested_units: set) -> str:
        """ Create display message with list of untested units. """
        msg = ['\n\nThe following units do not have unit tests:\n']
        for name in sorted(list(untested_units)):
            msg.append(name)
        return '\n'.join(msg)
