# Copyright (c) 2022-2023 Mike Cunningham

from unittest import TestCase
from decimal import Decimal
from converter import Converter, Unit, format_decimal


class AbstractTestCase(TestCase):

    def setUp(self) -> None:
        self.converter = Converter()
        self.all_units = self.converter.units
        self.base_value = Decimal('1')

    def check_units(self, base_unit: Unit, units: dict, expected_values: dict) -> None:
        for unitname in units.keys():
            self.assertTrue(unitname in expected_values.keys(),
                            f"Missing key: {unitname}")

            dest_unit = self.converter.find_unit(unitname)
            result = self.converter.convert(self.base_value, base_unit, dest_unit)
            expected = Decimal(expected_values[unitname])

            self.assertEqual(result, expected, 'Value mismatch')

    def get_units(self, category: str) -> list[Unit]:
        """ Get the list of Units for a specific category. """
        units = []
        for name, properties in self.all_units[category].items():
            units.append(Unit(name, category, **properties))

        return units

    def print_conversions(self, base_unit: Unit = None, units: dict = None) -> None:
        """ Print unit conversion table. """
        if not base_unit:
            base_unit = self.base_unit

        if not units:
            units = self.units

        for name, properties in units.items():
            dest = Unit(name, base_unit.category, **properties)
            result = self.converter.convert(self.base_value, base_unit, dest)
            print(f'"{dest.name}": "{result}",')


__all__ = [
    'AbstractTestCase',
    'Converter',
    'Unit',
    'format_decimal'
]
