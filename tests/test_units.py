# Copyright (c) 2022-2023 Mike Cunningham

from decimal import Decimal
from unitconverter.unit import PREFIX_OPTIONS
from tests import AbstractTestCase, Unit


class TestUnits(AbstractTestCase):
    """ Test predefined units. """

    def test_units(self) -> None:
        """ Test for invalid units. """
        for unit in self.converter.units:
            self.assert_valid_unit(unit)

    def assert_valid_unit(self, unit: Unit) -> None:
        """ Assert that a unit is valid """
        self.assertIsInstance(unit, Unit, type(unit))
        msg = f'{unit!r} ' + 'attribute {} is invalid: {!r}'

        # Assert that the unit name is valid
        self.assertIsInstance(unit.name, str, type(unit.name))
        self.assertTrue(unit.name, msg.format('name', unit.name))

        # Assert that the unit category is valid
        self.assertIsInstance(unit.category, str, type(unit.category))
        self.assertTrue(unit.category, msg.format('category', unit.category))

        # Assert that symbols and aliases are valid (TODO: test values)
        self.assertIsInstance(unit.symbols, list, type(unit.symbols))
        self.assertIsInstance(unit.aliases, list, type(unit.aliases))

        # Assert that all decimal attributes are valid
        self.assert_valid_decimal(unit, unit.factor)
        self.assert_valid_decimal(unit, unit.offset)
        self.assert_valid_decimal(unit, unit.power)

        # Assert that the prefix options are valid
        self.assert_valid_prefix_scaling(unit)
        self.assert_valid_prefix_index(unit)

    def assert_valid_decimal(self, unit: Unit, value: Decimal) -> None:
        """ Assert that a unit has a valid Decimal value. """
        msg = f'{unit.name!r} has an invalid decimal.'
        self.assertIsInstance(value, Decimal, msg)

        # Assert that all E notations are signed +/-
        msg = f'{unit.name!r} is missing a +/- symbol: {value!r}'
        strvalue = str(value)
        if 'E' in strvalue:
            self.assertTrue('+' in strvalue or '-' in strvalue, msg)

    def assert_valid_prefix_scaling(self, unit: Unit) -> None:
        """ Assert that a unit has a valid prefix_scaling attribute. """
        msg = f'{unit.name} has an invalid prefix_scaling: {unit.prefix_scaling!r}'
        self.assertIsInstance(unit.prefix_scaling, str, msg)
        self.assertIn(unit.prefix_scaling, PREFIX_OPTIONS, msg)

    def assert_valid_prefix_index(self, unit: Unit) -> None:
        """ Assert that a unit has a valid prefix_index attribute. """
        msg = f'{unit.name} has an invalid prefix_index: {unit.prefix_index}'
        self.assertIsInstance(unit.prefix_index, int, msg)

        for name in [unit.name] + unit.symbols + unit.aliases:
            word_count = len(name.split(' '))
            self.assertTrue(-1 <= unit.prefix_index < word_count,
                            msg + f'(index is out of range: {name!r})')
