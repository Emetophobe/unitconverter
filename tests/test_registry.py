# Copyright (c) 2022-2025 Mike Cunningham
# https://www.github.com/emetophobe/unitconverter


import unittest

from unitconverter.exceptions import DuplicateUnitError, InvalidUnitError
from unitconverter.models.unit import Unit
from unitconverter.registry import Registry

from tests import metre


class TestRegistry(unittest.TestCase):
    """ Tests for the Registry class. """

    def test___init__(self) -> None:
        registry = Registry()
        self.assertGreater(len(registry.units), 0, "Default registry should have units")

        empty = Registry(units=[])
        self.assertEqual(len(empty.units), 0, "Empty registry should have zero units")

        # Invalid units should raise a TypeError
        with self.assertRaises(TypeError):
            Registry("not a list of units")  # type: ignore

        # Duplicate units should raise a DuplicateUnitError
        units = [Unit("dupe"), Unit("dupe")]
        with self.assertRaises(DuplicateUnitError):
            Registry(units)  # type: ignore

    def test_add_unit(self) -> None:
        registry = Registry(units=[])
        registry.add_unit(metre)

        # Invalid units should raise a TypeError
        with self.assertRaises(TypeError):
            registry.add_unit("not a unit")  # type: ignore

        # Duplicate units should raise a DuplicateUnitError
        with self.assertRaises(DuplicateUnitError):
            registry.add_unit(metre)

    def test_add_alias(self) -> None:
        registry = Registry(units=[metre])
        registry.add_alias("test_metre", metre)
        registry.add_alias("test_metre2", "metre")

        with self.assertRaises(TypeError):
            registry.add_alias(None, "meters")  # type: ignore

        with self.assertRaises(TypeError):
            registry.add_alias("test_metre3", None)  # type: ignore

        with self.assertRaises(InvalidUnitError):
            registry.add_alias("alias", "invalid unit")

        with self.assertRaises(DuplicateUnitError):
            registry.add_alias("metre", "metre")

    def test_get_unit(self) -> None:

        registry = Registry()

        with self.assertRaises(InvalidUnitError):
            registry.get_unit("invalid unit")

        with self.assertRaises(InvalidUnitError):
            registry.get_unit(3.14)  # type: ignore

    def test_parse_unit(self) -> None:
        registry = Registry()

        # Invalid arguments should raise a TypeError
        for invalid_type in ("", 1, 3.14, [], (), {}):
            with self.assertRaises(TypeError):
                registry.parse_unit(invalid_type)  # type: ignore

        # Undefined units should raise an InvalidUnitError
        with self.assertRaises(InvalidUnitError):
            registry.parse_unit("undefined unit")

        joule_per_kg = registry.parse_unit("J/kg")
        self.assertTrue(joule_per_kg.name, "joule/kg")
        self.assertTrue(joule_per_kg.factor, 1)

        square_metre = registry.parse_unit("metre²")
        square_metre2 = registry.parse_unit("metre^2")
        self.assertEqual(square_metre, square_metre2)

        reciprocal_second = registry.parse_unit("second⁻¹")
        reciprocal_second2 = registry.parse_unit("second^-1")
        self.assertEqual(reciprocal_second, reciprocal_second2)

    def test_simplify_unit(self) -> None:
        simplify_unit = Registry()._simplify_unit

        self.assertEqual(simplify_unit("metre¹"), "metre1")
        self.assertEqual(simplify_unit("metre⁻¹"), "metre-1")

    def test_split_exponent(self) -> None:
        split_exponent = Registry()._split_exponent

        self.assertEqual(split_exponent("metre"), ("metre", 1))
        self.assertEqual(split_exponent("metre¹"), ("metre", 1))
        self.assertEqual(split_exponent("metre⁻¹"), ("metre", -1))
