# Copyright (c) 2022-2023 Mike Cunningham


import unittest

from unitconverter.definitions import UnitDefinition
from unitconverter.exceptions import DefinitionError, UnitError
from unitconverter.registry import REGISTRY as registry
from unitconverter.unit import Unit


class TestRegistry(unittest.TestCase):
    """ Test unit registry. """

    def test_new_unit(self) -> None:
        """ Test new_unit() method. """

        # Add a dummy unit definition
        dummy = UnitDefinition('dummy', 'length', ['dum'], ['dummy unit'])
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
        self.assertEqual(unit.dimension, 'time^3')

        # Composite units should raise a unit error (parse_unit() handles this)
        with self.assertRaises(UnitError):
            unit = registry.get_unit('rod/minute')

        # Invalid unit names
        with self.assertRaises(UnitError):
            registry.get_unit('bad unit')

        # Invalid unit names
        with self.assertRaises(UnitError):
            registry.get_unit(None)

    def test_get_units(self) -> None:
        """ Test get_units() method. """
        units = registry.get_units()
        self.assertIsInstance(units, dict)
        self.assertGreater(len(units), 0, 'number of units')

    def test_get_definition(self) -> None:
        """ Test get_definition() method. """

        kelvin = registry.get_definition('kelvin')
        self.assertEqual(kelvin.category, 'temperature')
        self.assertEqual(kelvin.dimen, {'temperature': 1})

        with self.assertRaises(DefinitionError):
            registry.get_definition('invalid unit')

        with self.assertRaises(DefinitionError):
            registry.get_definition(None)

    def test_get_dimensions(self) -> None:
        """ Test get_dimensions() method. """
        dimensions = registry.get_dimensions()

        self.assertIsInstance(dimensions, dict)
        self.assertGreater(len(dimensions), 0)

        for dimen, category in dimensions.items():
            self.assertIsInstance(dimen, tuple)
            self.assertIsInstance(category, str)

    def test_get_category(self) -> None:
        """ Test get_category() method. """
        unit = Unit(1, {'metre': 1}, {'length': 1, 'time': -1})
        speed = registry.get_category(unit)
        self.assertEqual(speed, 'speed')

        dimensionless = registry.get_category(Unit(1))
        self.assertEqual(dimensionless, 'dimensionless')

        with self.assertRaises(UnitError):
            registry.get_category(None)

    def test_load_units(self) -> None:
        """ Test _load_units() method. """
        # Load units is called once to initialize the registry
        # Calling it again should raise a duplicate unit exception
        with self.assertRaises(DefinitionError):
            registry._load_units()
