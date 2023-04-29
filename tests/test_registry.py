# Copyright (c) 2022-2023 Mike Cunningham


import unittest

from unitconverter.exceptions import UnitError, DefinitionError
from unitconverter.registry import REGISTRY as registry
from unitconverter.definitions import UnitDef


# Total number of categories and units
NUM_CATEGORIES = 40
NUM_UNITS = 2404


class TestRegistry(unittest.TestCase):
    """ Test unit registry. """

    def test_new_unit(self) -> None:
        """ Test new_unit() method. """

        # Add a dummy unit definition
        dummy = UnitDef('dummy', 'length', ['dum'], ['dummy unit'])
        registry.new_unit(dummy)

        # Adding duplicates should raise a DefinitionError
        with self.assertRaises(DefinitionError):
            registry.new_unit(dummy)

    def test_add_alias(self) -> None:
        """ Test add_alias() method. """

        registry.add_alias('metre', 'metros')

        # Duplicate alias
        with self.assertRaises(DefinitionError):
            registry.add_alias('metre', 'metre')

        # Invalid alias
        with self.assertRaises(DefinitionError):
            registry.add_alias('metre', {'bad alias': 1})

        # Invalid unitdef
        with self.assertRaises(DefinitionError):
            registry.add_alias(5, 'metre')

    def test_add_aliases(self) -> None:
        """ Test add_aliases method. """
        registry.add_aliases('metre', ['metior', 'mètre'])

        # Duplicate alias
        with self.assertRaises(DefinitionError):
            registry.add_aliases('second', ['second', 'sec'])

        # Invalid aliases type
        with self.assertRaises(DefinitionError):
            registry.add_aliases('second', 'should be a list, tuple, or set')

        # Invalid alias
        with self.assertRaises(DefinitionError):
            registry.add_aliases('second', ['secs', None])

        # Invalid unitdef
        with self.assertRaises(DefinitionError):
            registry.add_aliases(None, 'invalid unit def')

    def test_get_unit(self) -> None:
        """ Test get_unit() method. """
        registry.get_unit('metre')

        # Test getting units with an exponent
        unit = registry.get_unit('second^3')
        self.assertEqual(unit.category, 'time^3')

        # Composite units should raise a unit error (parse_unit() handles this)
        with self.assertRaises(UnitError):
            unit = registry.get_unit('rod/minute')
            print(unit)

        # Invalid unit names
        with self.assertRaises(UnitError):
            registry.get_unit('bad unit')

        # Invalid unit names
        with self.assertRaises(UnitError):
            registry.get_unit(None)

    def test_get_units(self) -> None:
        """ Test get_units() method. """
        categories = registry.get_units()
        self.assertIsInstance(categories, dict)
        self.assertEqual(NUM_CATEGORIES, len(categories), 'number of categories')

        total_units = sum(len(units) for units in categories.values())
        self.assertEqual(NUM_UNITS, total_units, 'number of units')

    def test_get_definition(self) -> None:
        """ Test get_definition() method. """

        kelvin = registry.get_definition('kelvin')
        self.assertEqual(kelvin.category, 'temperature')

        with self.assertRaises(DefinitionError):
            registry.get_definition('invalid unit')

        with self.assertRaises(DefinitionError):
            registry.get_definition(None)

    def test_load_units(self) -> None:
        """ Test _load_units() method. """
        # Load units is called once to initialize the registry
        # Calling it again should raise a duplicate unit exception
        with self.assertRaises(DefinitionError):
            registry._load_units()
