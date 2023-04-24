# Copyright (c) 2022-2023 Mike Cunningham


import unittest
from decimal import Decimal

from unitconverter.exceptions import UnitError
from unitconverter.registry import Registry
from unitconverter.unit import Unit


# Total number of categories
NUM_CATEGORIES = 37


class TestRegistry(unittest.TestCase):
    """ Test unit registry. """

    def setUp(self) -> None:
        """ Initialize units. """
        self.units = Registry()

    def test_add_unit(self) -> None:
        """ Test add_unit() method. """
        # Add a dummy unit
        dummy = Unit('dummy', 'length', ['d'], ['dummies'], factor=1)
        self.units.add_unit(dummy)

        # Duplicate units should raise a UnitError
        with self.assertRaises(UnitError):
            self.units.add_unit(dummy)

    def test_get_unit(self) -> None:
        """ Test get_unit() method. """
        self.units.get_unit('metre')

        # Dummy unit from test_add_unit() should be accessible across tests
        self.units.get_unit('dummy')

        with self.assertRaises(UnitError):
            self.units.get_unit('bad unit')

    def test_get_units(self) -> None:
        """ Test get_units() method. """
        units = [unit for unit in self.units]
        self.assertEqual(self.units.get_units(), units)

    def test_get_categories(self) -> None:
        """ Test get_categories() method. """
        categories = self.units.get_categories()
        self.assertIsInstance(categories, dict)
        self.assertEqual(NUM_CATEGORIES, len(categories),
                         f'there should be {NUM_CATEGORIES} categories')

    def test_get_aliases(self) -> None:
        """ Test get_aliases() method. """
        aliases = {}
        for unit in self.units:
            for name in unit.names():
                aliases[name] = unit

        self.assertEqual(self.units.get_aliases(), aliases)

    def test_iter_units(self) -> None:
        """ Test iter_units() method. """
        units = [unit for unit in self.units.iter_units()]
        self.assertEqual(len(self.units), len(units))

    def test_load_units(self) -> None:
        """ Test _load_units() method. """
        # Load units is called internally to initialize the registry
        # Calling it again should raise a duplicate unit exception
        with self.assertRaises(UnitError):
            self.units._load_units()

    def test_len(self) -> None:
        """ Test __len__ method. """
        units = [unit for unit in self.units]
        self.assertEqual(len(units), len(self.units))

    def test_units(self) -> None:
        """ Test for incorrectly formed units. """
        for unit in self.units:
            self.assert_valid_unit(unit)

    def assert_valid_unit(self, unit: Unit) -> None:
        """ Assert that a unit is correctly formed. """
        self.assertIsInstance(unit, Unit, f'{unit!r} is not a valid Unit')

        msg = f'{unit.name} has an invalid '

        self.assert_string(repr(unit), msg + 'name')
        self.assert_string(unit.category, msg + 'category')
        self.assert_stringlist(unit.symbols, f'{unit.name} has invalid symbols')
        self.assert_stringlist(unit.aliases, f'{unit.name} has invalid aliases')

        self.assert_numeric(unit.factor, msg + 'factor')

        if unit.prefix_scale:  # prefix scale can be None
            self.assertIsInstance(unit.prefix_scale, str, msg + 'prefix_scale')

        self.assertIsInstance(unit.prefix_power, int, msg + 'prefix_power')
        self.assert_stringlist(unit.prefix_exclude, msg + 'prefix_exclude')

    def assert_numeric(self, value: Decimal | int | str, msg: str) -> None:
        """ Assert that a unit has a valid numeric value (Decimal, int, or str). """
        self.assertIsInstance(value, (Decimal, int, str), msg)

        # Assert that all E notations are signed +/-
        strvalue = str(value)
        if 'E' in strvalue:
            self.assertTrue('+' in strvalue or '-' in strvalue,
                            f'{value!r} is missing a +/- symbol (requirement)')

    def assert_string(self, name: str, msg: str) -> None:
        """ Assert that name is a valid string (atleast 1 character). """
        self.assertIsInstance(name, str, msg)
        self.assertGreater(len(name), 0, msg)

    def assert_stringlist(self, names: list[str], msg: str) -> None:
        """ Assert that a list of strings is valid. """
        self.assertIsInstance(names, list, msg)
        for name in names:
            self.assert_string(name, msg)
