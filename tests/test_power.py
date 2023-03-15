# Copyright (c) 2022-2023 Mike Cunningham

from tests import AbstractTestCase


class TestPower(AbstractTestCase):

    def setUp(self):
        super().setUp()
        self.base_unit = self.converter.find_unit('watts')
        self.units = self.converter.units['power']

    def test_watts(self):
        """ Test watt conversions. """
        expected_values = {
            "watts": "1",
            "quectowatts": "1E+30",
            "rontowatts": "1E+27",
            "yoctowatts": "1E+24",
            "zeptowatts": "1E+21",
            "attowatts": "1E+18",
            "femtowatts": "1E+15",
            "picowatts": "1E+12",
            "nanowatts": "1E+9",
            "microwatts": "1E+6",
            "milliwatts": "1E+3",
            "centiwatts": "1E+2",
            "deciwatts": "1E+1",
            "decawatts": "1E-1",
            "hectowatts": "1E-2",
            "kilowatts": "1E-3",
            "megawatts": "1E-6",
            "gigawatts": "1E-9",
            "terawatts": "1E-12",
            "petawatts": "1E-15",
            "exawatts": "1E-18",
            "zettawatts": "1E-21",
            "yottawatts": "1E-24",
            "ronnawatts": "1E-27",
            "quettawatts": "1E-30",
            "joules per second": "1",
        }

        # Test all watt conversions
        self.check_units(self.base_unit, self.units, expected_values)
