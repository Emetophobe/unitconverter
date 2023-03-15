# Copyright (c) 2022-2023 Mike Cunningham

from tests import AbstractTestCase


class TestEnergy(AbstractTestCase):

    def setUp(self):
        super().setUp()
        self.base_unit = self.converter.find_unit('joules')
        self.units = self.converter.units['energy']

    def test_joules(self):
        """ Test joule conversions. """
        expected_values = {
            "joules": "1",
            "quectojoules": "1E+30",
            "rontojoules": "1E+27",
            "yoctojoules": "1E+24",
            "zeptojoules": "1E+21",
            "attojoules": "1E+18",
            "femtojoules": "1E+15",
            "picojoules": "1E+12",
            "nanojoules": "1E+9",
            "microjoules": "1E+6",
            "millijoules": "1E+3",
            "centijoules": "1E+2",
            "decijoules": "1E+1",
            "decajoules": "0.1",
            "hectojoules": "0.01",
            "kilojoules": "0.001",
            "megajoules": "0.000001",
            "gigajoules": "1E-9",
            "terajoules": "1E-12",
            "petajoules": "1E-15",
            "exajoules": "1E-18",
            "zettajoules": "1E-21",
            "yottajoules": "1E-24",
            "ronnajoules": "1E-27",
            "quettajoules": "1E-30",
        }

        # Test all joule conversions
        self.check_units(self.base_unit, self.units, expected_values)
