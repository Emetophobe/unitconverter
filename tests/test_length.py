# Copyright (c) 2022-2023 Mike Cunningham

from tests import AbstractTestCase


class TestLength(AbstractTestCase):

    def setUp(self) -> None:
        super().setUp()
        self.base_unit = self.converter.find_unit('meters')
        self.units = self.converter.units['length']

    def test_meters(self):
        """ Test meter conversions. """
        expected_values = {
            "meters": "1",
            "centimeters": "1E+2",
            "decimeters": "1E+1",
            "kilometers": "0.001",
            "micrometers": "1E+6",
            "millimeters": "1E+3",
            "nanometers": "1E+9",
            "yoctometers": "1E+24",
            "zeptometers": "1E+21",
            "attometers": "1E+18",
            "femtometers": "1E+15",
            "picometers": "1E+12",
            "decameters": "0.1",
            "hectometers": "0.01",
            "megameters": "0.000001",
            "gigameters": "1E-9",
            "terameters": "1E-12",
            "petameters": "1E-15",
            "exameters": "1E-18",
            "zettameters": "1E-21",
            "yottalmeters": "1E-24",
            "feet": "3.280839895013123359580052493",
            "inches": "39.37007874015748031496062992",
            "miles": "0.0006213711922373339696174341844",
            "yards": "1.093613298337707786526684164",
        }

        # Test all meter conversions
        self.check_units(self.base_unit, self.units, expected_values)
