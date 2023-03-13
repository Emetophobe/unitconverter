# Copyright (c) 2022-2023 Mike Cunningham

from unittest import TestCase
from decimal import Decimal
from converter import Converter


class AbstractTestCase(TestCase):

    def setUp(self):
        self.converter = Converter()
        self.all_units = self.converter.units
        self.base_value = Decimal('1')

    def check_units(self, base_unit, units, expected_values):
        for unitname in units.keys():
            self.assertTrue(unitname in expected_values.keys(),
                            f"Missing key: {unitname}")

            dest_unit = self.converter.find_unit(unitname)
            result = self.converter.convert(self.base_value, base_unit, dest_unit)
            expected = Decimal(expected_values[unitname])

            self.assertEqual(result, expected, 'Value mismatch')

    def decimal_to_str(self, value: Decimal, precision: int = 5) -> None:
        return f"{value:.{precision}f}"


__all__ = [
    'AbstractTestCase'
]
