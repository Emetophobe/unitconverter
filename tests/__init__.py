# Copyright (c) 2022-2023 Mike Cunningham

from decimal import Decimal
from unittest import TestCase
from unitconverter import Unit, Converter, format_decimal


class AbstractTestCase(TestCase):

    def setUp(self) -> None:
        """ Initialize converter """
        self.converter = Converter()

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
        source: Unit = self.converter.parse_unit(source)
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


__all__ = [
    'AbstractTestCase',
    'Converter',
    'Unit',
    'format_decimal'
]
