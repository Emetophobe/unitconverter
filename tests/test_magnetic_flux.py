# Copyright (c) 2022-2023 Mike Cunningham

from tests import AbstractTestCase


class TestMagneticFlux(AbstractTestCase):

    def setUp(self) -> None:
        super().setUp()
        # SI uses kilograms as the base unit for historical
        # reasons. I use grams because it makes sense.
        self.base_unit = self.converter.find_unit('weber')
        self.units = self.all_units['magnetic flux']

    def test_weber(self) -> None:
        """ Test weber conversions. """
        expected_values = {
            "weber": "1",
            "quectoweber": "1E+30",
            "rontoweber": "1E+27",
            "yoctoweber": "1E+24",
            "zeptoweber": "1E+21",
            "attoweber": "1E+18",
            "femtoweber": "1E+15",
            "picoweber": "1E+12",
            "nanoweber": "1E+9",
            "microweber": "1E+6",
            "milliweber": "1E+3",
            "centiweber": "1E+2",
            "deciweber": "1E+1",
            "decaweber": "0.1",
            "hectoweber": "0.01",
            "kiloweber": "0.001",
            "megaweber": "0.000001",
            "gigaweber": "1E-9",
            "teraweber": "1E-12",
            "petaweber": "1E-15",
            "exaweber": "1E-18",
            "zettaweber": "1E-21",
            "yottaweber": "1E-24",
            "ronnaweber": "1E-27",
            "quettaweber": "1E-30",
            "maxwell": "1E+8"
        }

        # Test all weber conversions
        self.check_units(self.base_unit, self.units, expected_values)
