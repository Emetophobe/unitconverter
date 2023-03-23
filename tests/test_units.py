# Copyright (c) 2022-2023 Mike Cunningham

from tests import AbstractTestCase, Unit


class TestUnits(AbstractTestCase):
    """ Test unit data. """

    def setUp(self) -> None:
        super().setUp()
        self.valid_chars = '+-.0123456789E'
        self.aliases = set()

    def test_units(self) -> None:
        """ Test for invalid units. """
        for unit in self.converter.units:
            self.assert_valid_unit(unit)

    def assert_duplicates(self, name: str) -> None:
        """ Assert that name isn't a duplicate name, symbol, or alias.

        Args:
            name (str): the name or alias.
        """
        self.assertFalse(name in self.aliases, f'Duplicate name or alias: {name!r}')
        self.aliases.add(name)

    def assert_valid_unit(self, unit: Unit):
        """ Assert that unit has a valid name and factor. """
        self.assertTrue(unit.name, f'{unit} has an empty unit name.')
        self.assertTrue(unit.factor, f'{unit.name} has an empty unit factor.')
        self.assertTrue(unit.category, f'{unit.name} has an empty category.')

        # Assert that unit factor contains valid decimal characters
        if isinstance(unit.factor, str):
            for char in unit.factor:
                self.assertIn(char, self.valid_chars,
                              f'{unit.name} has an invalid character: {char!r}')

        # Assert that all E notations are signed +/-
        strfactor = str(unit.factor)
        if 'E' in strfactor:
            self.assertTrue('+' in strfactor or '-' in strfactor,
                            f'{unit.name} is missing a +/- symbol: {unit.factor!r}')
