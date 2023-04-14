# Copyright (c) 2022-2023 Mike Cunningham


import unittest
from decimal import Decimal
from typing import Any

from unitconverter.exceptions import UnitError
from unitconverter.prefixes import PrefixScale, get_prefixes
from unitconverter.unit import Unit
from unitconverter.registry import Registry


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

    def test_generated_units(self) -> None:
        """ Test generated units. """
        aliases = self.units.get_aliases()

        # Exclude units that were created for convenience that
        # might conflict with units with prefix scaling enabled
        excludes = ['kilometre/hour']  # conficts with metre/hour

        # Generate list of prefixed units
        generated = []
        for unit in self.units:
            prefixes = get_prefixes(unit.prefix_scale)
            for factor, symbol, prefix in prefixes:
                scaled_unit = unit.prefix(factor, symbol, prefix)
                if scaled_unit.name not in excludes:
                    generated.append(scaled_unit)

        # Check for duplicates
        for unit in generated:
            for name in unit.names():
                self.assertTrue(name not in aliases, f'{unit.name} has a duplicate'
                                f' name: {name} original: {aliases.get(name)}')
                aliases[name] = unit

            # Make sure the generated unit is valid
            self.assert_valid_unit(unit)

    def assert_valid_unit(self, unit: Unit) -> None:
        """ Assert that a unit is correctly formed (has the right attribute types). """
        self.assert_type(unit, Unit, f'{unit!r} is not a valid Unit')

        self.assert_string(unit.name, f'{unit.name} has an invalid name')
        self.assert_string(unit.category, f'{unit.name} has an invalid category')
        self.assert_stringlist(unit.symbols, f'{unit.name} has invalid symbols')
        self.assert_stringlist(unit.aliases, f'{unit.name} has invalid aliases')

        self.assert_decimal(unit.factor, f'{unit.name} has an invalid factor')
        self.assert_decimal(unit.offset, f'{unit.name} has an invalid offset')
        self.assert_decimal(unit.power, f'{unit.name} has an invalid power')

        msg = f'{unit.name} has an invalid prefix_scale: {unit.prefix_scale!r}'
        self.assertIsInstance(unit.prefix_scale, PrefixScale, msg)

    def assert_type(self, obj: Any, types: Any | tuple, msg: str = None) -> None:
        """ Assert that an object is the correct type or tuple of types. """
        self.assertIsInstance(obj, types, msg or type(obj))

    def assert_decimal(self, value: Decimal, msg: str) -> None:
        """ Assert that a unit has a valid decimal (factor, power, or offset). """
        self.assert_type(value, Decimal, msg)

        # Assert that all E notations are signed +/-
        msg = f'{value!r} is missing a +/- symbol (requirement)'
        strvalue = str(value)
        if 'E' in strvalue:
            self.assertTrue('+' in strvalue or '-' in strvalue, msg)

    def assert_string(self, name: str, msg: str) -> None:
        """ Assert that name is a valid string (atleast 1 character). """
        self.assert_type(name, str)
        self.assertGreater(len(name), 0, msg)

    def assert_stringlist(self, names: list[str], msg: str) -> None:
        """ Assert that a list of strings is valid. """
        self.assert_type(names, list, msg)
        for name in names:
            self.assert_string(name, msg)
