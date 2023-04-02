# Copyright (c) 2022-2023 Mike Cunningham


import unittest
from decimal import Decimal
from typing import Any

from unitconverter.prefixes import PrefixScale, get_prefixes
from unitconverter.unit import Unit
from unitconverter.units import Units


class TestUnits(unittest.TestCase):
    """ Test Units class. """

    def setUp(self) -> None:
        """ Initialize units. """
        self.units = Units()

    def test_units(self) -> None:
        """ Test for incorrectly formed units. """
        for unit in self.units:
            self.assert_valid_unit(unit)

    def test_generated_units(self) -> None:
        """ Test generated units. """
        defined = list(self.units)
        aliases = self.units._aliases
        generated = []

        # Exclude units that were created for convenience that
        # conflict with units that support prefix scaling
        excludes = ['kilometre/hour']  # conficts with metre/hour

        for unit in defined:
            # Generate prefixed versions (if supported)
            prefixes = get_prefixes(unit.prefix_scale)
            for factor, symbol, prefix in prefixes:
                scaled_unit = unit.scale(factor, symbol, prefix)
                if scaled_unit.name not in excludes:
                    generated.append(scaled_unit)

        # Search for duplicates
        for unit in generated:
            for name in unit.get_names():
                self.assertTrue(name not in aliases, f'{unit.name} has a duplicate'
                                f' name: {name} original: {aliases.get(name)}')
                aliases[name] = unit

        #  print('Total units', len(defined))
        #  print('Generated units:', len(generated))

    def assert_valid_unit(self, unit: Unit) -> None:
        """ Assert that a unit is correctly formed (has the right attribute types). """
        self.assert_type(unit, Unit, f'{unit!r} is not a valid Unit')

        self.assert_string(unit.name, f'{unit.name} has an invalid name')
        self.assert_string(unit.category, f'{unit.name} has an invalid category')

        self.assert_stringlist(unit.symbols, f'{unit.name} has invalid symbols')
        self.assert_stringlist(unit.aliases, f'{unit.name} has invalid aliases')

        self.assert_decimal(unit.factor, f'{unit.name!r} has an invalid factor')
        self.assert_decimal(unit.offset, f'{unit.name!r} has an invalid offset')
        self.assert_decimal(unit.power, f'{unit.name!r} has an invalid power')

        self.assert_prefix_scale(unit)
        self.assert_prefix_index(unit)

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

    def assert_prefix_scale(self, unit: Unit) -> None:
        """ Assert that prefix_scale is a valid PrefixScale. """
        msg = f'{unit.name} has an invalid prefix_scale: {unit.prefix_scale!r}'
        self.assertIsInstance(unit.prefix_scale, PrefixScale, msg)

    def assert_prefix_index(self, unit: Unit) -> None:
        """ Assert that prefix_index is a valid index. """
        msg = f'{unit.name} has an invalid prefix_index: {unit.prefix_index}'
        self.assert_type(unit.prefix_index, int, msg)

        msg = msg + ' (index is out of range)'
        for name in [unit.name] + unit.aliases:  # don't check symbols
            word_count = len(name.split(' '))
            self.assertTrue(-1 <= unit.prefix_index < word_count, msg)
