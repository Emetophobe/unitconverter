# Copyright (c) 2022-2025 Mike Cunningham
# https://www.github.com/emetophobe/unitconverter


import unittest

from unitconverter.models.dimension import Dimension


class TestDimension(unittest.TestCase):
    """ Tests for the Dimension class. """

    def test__init__(self) -> None:
        # Invalid arguments should raise a TypeError
        for invalid_type in ("", 1, 3.14, [], ()):
            with self.assertRaises(TypeError):
                Dimension(invalid_type)  # type: ignore

        dimensionless = Dimension()
        self.assertEqual(dimensionless, {})
        self.assertEqual(dimensionless.name, "")

    def test__mul__(self) -> None:
        area = Dimension("length") * Dimension("length")
        self.assertEqual(area, {"length": 2})
        self.assertEqual(area.name, "length^2")

        with self.assertRaises(TypeError):
            area * "invalid type"  # type: ignore

    def test__truediv__(self) -> None:
        speed = Dimension("length") / Dimension("time")
        self.assertEqual(speed, {"length": 1, "time": -1})
        self.assertEqual(speed.name, "length/time")

        with self.assertRaises(TypeError):
            speed / "invalid type"  # type: ignore

    def test__pow__(self) -> None:
        volume = Dimension("length") ** 3
        self.assertEqual(volume, {"length": 3})
        self.assertEqual(volume.name, "length^3")

        with self.assertRaises(TypeError):
            volume ** "invalid type"  # type: ignore

        with self.assertRaises(ValueError):
            volume ** 0  # type: ignore
