# Copyright (c) 2022-2023 Mike Cunningham

from tests import AbstractTestCase


class TestLuminousFlux(AbstractTestCase):

    def setUp(self) -> None:
        super().setUp()
        self.base_unit = self.converter.find_unit('lumens')
        self.units = self.converter.units['luminous flux']

    def test_lumens(self):
        """ Test lumen conversions. """
        expected_values = {
            "lumens": "1",
            "quectolumens": "1E+30",
            "rontolumens": "1E+27",
            "yoctolumens": "1E+24",
            "zeptolumens": "1E+21",
            "attolumens": "1E+18",
            "femtolumens": "1E+15",
            "picolumens": "1E+12",
            "nanolumens": "1E+9",
            "microlumens": "1E+6",
            "millilumens": "1E+3",
            "centilumens": "1E+2",
            "decilumens": "1E+1",
            "decalumens": "1E-1",
            "hectolumens": "1E-2",
            "kilolumens": "1E-3",
            "megalumens": "1E-6",
            "gigalumens": "1E-9",
            "teralumens": "1E-12",
            "petalumens": "1E-15",
            "exalumens": "1E-18",
            "zettalumens": "1E-21",
            "yottalumens": "1E-24",
            "ronnalumens": "1E-27",
            "quettalumens": "1E-30",
        }

        # Test all lumen conversions
        self.check_units(self.base_unit, self.units, expected_values)
