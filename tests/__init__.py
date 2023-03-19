# Copyright (c) 2022-2023 Mike Cunningham

from decimal import Decimal
from unittest import TestCase
from typing import Union
from convert import Converter, Unit, format_decimal


class AbstractTestCase(TestCase):

    def setUp(self) -> None:
        """ Initialize converter """
        self.converter = Converter()
        self.base_value = Decimal('1')

    def get_units(self, category: str) -> list[Unit]:
        """ Get a list of units for the specified category.

        Args:
            category (str): the category name.

        Raises:
            KeyError: if the category is invalid.

        Returns:
            list[Unit]: the list of Units.
        """
        units = []
        for name, properties in self.converter.units[category].items():
            units.append(Unit(name, category, **properties))

        return units

    def assert_unit(self,
                    source: Union[str, Unit],
                    dest: Union[str, Unit],
                    expected: Union[str, Decimal],
                    value: Union[str, Decimal] = '1'
                    ) -> None:
        """ Assert that a unit conversion gives the expected result.

        Args:
            source (str, Unit):
                source name or unit.

            dest (str, Unit):
                destination name or unit.

            expected (str, Decimal):
                expected value.

            value (str, Decimal):
                value to convert. Defaults to '1'.
        """
        source = self.converter.parse_unit(source)
        dest = self.converter.parse_unit(dest)

        self.assertEqual(source.category, dest.category, 'Invalid category')

        expected = Decimal(expected)
        result = self.converter.convert(value, source, dest)
        self.assertEqual(result, expected, f'Incorrect unit: {dest.name!r}'
                                           f' category: {dest.category!r}')

    def assert_units(self, source: Union[str, Unit], expected: dict) -> None:
        """ Assert that a dictionary of units converts to the expected values.

        Args:
            source (str, Unit): source unit.
            expected (dict): dictionary of expected values.
        """
        for dest, expected in expected.items():
            self.assert_unit(source, dest, expected)

    def print_conversions(self, source: Union[str, Unit]) -> None:
        """ Convenience method to print the unit conversion table.

        Args:
            source (str, Unit): source name or unit.
        """
        source = self.parse_unit(source)
        units = self.get_units(source.category)

        for unit in units:
            result = self.converter.convert(self.base_value, source, unit)
            print(f'"{unit.name}": "{result}",')


__all__ = [
    'AbstractTestCase',
    'Converter',
    'Unit',
    'format_decimal'
]
