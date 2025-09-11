# Copyright (c) 2022-2025 Mike Cunningham
# https://www.github.com/emetophobe/unitconverter


import unittest

from unitconverter.exceptions import ConverterError

from tests import metre, second


class TestUnit(unittest.TestCase):
    """ Tests for the Unit class. """

    def test___init__(self) -> None:
        # TODO: Test Unit() construction
        ...

    def test__mul__(self) -> None:
        with self.assertRaises(TypeError):
            metre * "invalid type"  # type: ignore

        square_metre = metre * metre
        self.assertEqual(square_metre.name, "metre^2")
        self.assertEqual(square_metre.dimension, {"length": 2})

    def test__truediv__(self) -> None:
        with self.assertRaises(TypeError):
            metre / "invalid type"  # type: ignore

        mps = metre / second
        self.assertEqual(mps.name, "metre/second")
        self.assertEqual(mps.dimension, {"length": 1, "time": -1})

    def test__pow__(self) -> None:
        with self.assertRaises(TypeError):
            metre ** "invalid type"  # type: ignore

        with self.assertRaises(ValueError):
            metre ** 0  # type: ignore

        cubic_metre = metre ** 3
        self.assertEqual(cubic_metre.name, "metre^3")
        self.assertEqual(cubic_metre.dimension, {"length": 3})
