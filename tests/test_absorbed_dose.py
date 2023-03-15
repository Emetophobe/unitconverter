# Copyright (c) 2022-2023 Mike Cunningham

from tests import AbstractTestCase


class TestAbsorbedDose(AbstractTestCase):

    def setUp(self):
        super().setUp()
        self.base_unit = self.converter.find_unit('gray')
        self.units = self.converter.units['absorbed dose']

    def test_gray(self):
        """ Test gray conversions. """
        expected_values = {
            "gray": "1",
            "quectogray": "1E+30",
            "rontogray": "1E+27",
            "yoctogray": "1E+24",
            "zeptogray": "1E+21",
            "attogray": "1E+18",
            "femtogray": "1E+15",
            "picogray": "1E+12",
            "nanogray": "1E+9",
            "microgray": "1E+6",
            "milligray": "1E+3",
            "centigray": "1E+2",
            "decigray": "1E+1",
            "decagray": "1E-1",
            "hectogray": "1E-2",
            "kilogray": "1E-3",
            "megagray": "1E-6",
            "gigagray": "1E-9",
            "teragray": "1E-12",
            "petagray": "1E-15",
            "exagray": "1E-18",
            "zettagray": "1E-21",
            "yottagray": "1E-24",
            "ronnagray": "1E-27",
            "quettagray": "1E-30",
        }

        # Test all gray conversions
        self.check_units(self.base_unit, self.units, expected_values)
