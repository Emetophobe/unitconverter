# Copyright (c) 2022-2023 Mike Cunningham

from unittest import TestCase
from decimal import Decimal
from typing import Optional, Union
from converter import Converter, Unit, format_decimal


METRIC_TABLE = [
    ('1', '', ''),  # base unit
    ('1E-30', 'q', 'quecto'),
    ('1E-27', 'r', 'ronto'),
    ('1E-24', 'y', 'yocto'),
    ('1E-21', 'z', 'zepto'),
    ('1E-18', 'a', 'atto'),
    ('1E-15', 'f', 'femto'),
    ('1E-12', 'p', 'pico'),
    ('1E-9', 'n', 'nano'),
    ('1E-6', 'µ', 'micro'),
    ('1E-3', 'm', 'milli'),
    ('1E-2', 'c', 'centi'),
    ('1E-1', 'd', 'deci'),
    ('1E+1', 'da', 'deca'),
    ('1E+2', 'h', 'hecto'),
    ('1E+3', 'k', 'kilo'),
    ('1E+6', 'M', 'mega'),
    ('1E+9', 'G', 'giga'),
    ('1E+12', 'T', 'tera'),
    ('1E+15', 'P', 'peta'),
    ('1E+18', 'E', 'exa'),
    ('1E+21', 'Z', 'zetta'),
    ('1E+24', 'Y', 'yotta'),
    ('1E+27', 'R', 'ronna'),
    ('1E+30', 'Q', 'quetta'),
]


class AbstractTestCase(TestCase):

    def setUp(self) -> None:
        """ Initialize converter. """
        self.converter = Converter()
        self.base_value = Decimal('1')
        self.tested = set()
        self.category = None

    def parse_unit(self, unit: Union[str, Unit]) -> Unit:
        """ Parse unit. Accepts either a string or a Unit.

        Args:
            unit (str, Unit): a unit name or instance.

        Raises:
            TypeError: if the unit is an invalid type.

        Returns:
            Unit: the unit instance.
        """
        if isinstance(unit, str):
            return self.converter.find_unit(unit)
        elif isinstance(unit, Unit):
            return unit
        else:
            raise TypeError(f'Expected a str or Unit, not a {type(unit).__name__}')

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
        source = self.parse_unit(source)
        dest = self.parse_unit(dest)

        self.assertEqual(source.category, dest.category, 'Invalid category')

        expected = Decimal(expected)
        result = self.converter.convert(value, source, dest)
        self.assertEqual(result, expected, f'Incorrect unit: {dest.name!r}'
                                           f' category: {dest.category!r}')

        self.update_tested(source, dest)

    def assert_rounded(self,
                       source: Union[str, Unit],
                       dest: Union[str, Unit],
                       expected: str,
                       value: Union[str, Decimal] = '1',
                       precision: Optional[int] = None,
                       exponent: bool = False,
                       commas: bool = False
                       ) -> None:
        """ Assert that a unit conversion gives the expected rounded result.

        Args:
            source (str, Unit):
                source name or unit.

            dest (str, Unit):
                destination name or unit.

            expected (str):
                expected value.

            value (str, Decimal):
                value to convert. Defaults to '1'.

            precision (int, optional):
                round to ndigits. Defaults to None.

            exponent (bool, optional):
                convert result to E notation. Defaults to False.

            commas (bool, optional):
                use thousands separators. Defaults to False.
        """
        source = self.parse_unit(source)
        dest = self.parse_unit(dest)

        self.assertEqual(source.category, dest.category, 'Invalid category')

        result = self.converter.convert(value, source, dest)
        result = format_decimal(result, exponent, precision, commas)

        self.assertEqual(result, expected, f'Incorrect unit: {dest.name!r}'
                                           f' category: {dest.category!r}')

        self.update_tested(source, dest)

    def assert_units(self, source: Union[str, Unit], expected: dict) -> None:
        """ Assert that a dictionary of units converts to the expected values.

        Args:
            source (str, Unit): source unit.
            expected (dict): dictionary of expected values.
        """
        for dest, expected in expected.items():
            self.assert_unit(source, dest, expected)

    def assert_metric_scale(self, name: str) -> None:
        """ Assert that unit has a valid metric conversion table.

        Args:
            name (str): the unit name.
        """
        for scale, _, prefix in METRIC_TABLE:
            self.assert_unit(prefix + name, name, scale)

    def assert_all_tested(self):
        """ Assert that all units were tested. """
        self.assertTrue(self.category in self.converter.units.keys(), 'Invalid category')

        for name in self.converter.units[self.category].keys():
            self.assertTrue(name in self.tested, f'Missing {self.category} test:'
                                                 f' {name!r}')

    def update_tested(self, source: Unit, dest: Unit) -> None:
        """ Track which units were tested (or not).

        Args:
            source (Unit): source unit.
            dest (Unit): destination unit.
        """
        self.category = source.category
        self.tested.add(source.name)
        self.tested.add(dest.name)

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
    'METRIC_TABLE',
    'AbstractTestCase',
    'Converter',
    'Unit',
    'format_decimal'
]
