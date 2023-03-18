# Copyright (c) 2022-2023 Mike Cunningham

from decimal import Decimal, DecimalException
from tests import AbstractTestCase, Unit


class TestUnits(AbstractTestCase):

    VALID_CHARS = '+-.0123456789E'

    def setUp(self) -> None:
        super().setUp()
        self.aliases = set()

    def test_units(self) -> None:
        """ Test for invalid units and duplicate names. """
        for unit in self.yield_units():
            self.assert_valid_unit(unit)
            self.assert_duplicates(unit.name)

            for alias in unit.aliases:
                self.assert_duplicates(alias)

    def assert_duplicates(self, name: str) -> None:
        """ Assert that name isn't a duplicate name, symbol, or alias.

        Args:
            name (str): the name or alias.
        """
        self.assertFalse(name in self.aliases, f'Duplicate name or alias: {name!r}')
        self.aliases.add(name)

    def assert_valid_unit(self, unit: Unit):
        """ Assert that unit has a valid name and scale. """
        self.assertTrue(unit.name, f'{unit} has an empty unit name.')
        self.assertTrue(unit.scale, f'{unit.name} has an empty unit scale.')

        # Assert that unit scale contains valid decimal characters
        for char in unit.scale:
            self.assertIn(char, TestUnits.VALID_CHARS,
                          f'{unit.name} has an invalid character: {char!r}')

        # Assert that all E notation is signed +/-
        if 'E' in unit.scale:
            self.assertTrue('+' in unit.scale or '-' in unit.scale,
                            f'{unit.name} is missing a +/- symbol: {unit.scale!r}')

    def yield_units(self) -> Unit:
        """ Iterate over the unit categories and yield Units. """
        for category, units in self.converter.units.items():
            for unitname, properties in units.items():
                yield Unit(unitname, category, **properties)
