# Copyright (c) 2022-2023 Mike Cunningham

from tests import AbstractTestCase


class TestEnergy(AbstractTestCase):

    def setUp(self):
        super().setUp()
        self.base_unit = self.converter.find_unit('joule')
        self.units = self.converter.units['energy']

    def test_joule(self):
        """ Test joule conversions. """
        expected_values = {
            "joule": "1",
            "quectojoule": "1E+30",
            "rontojoule": "1E+27",
            "yoctojoule": "1E+24",
            "zeptojoule": "1E+21",
            "attojoule": "1E+18",
            "femtojoule": "1E+15",
            "picojoule": "1E+12",
            "nanojoule": "1E+9",
            "microjoule": "1E+6",
            "millijoule": "1E+3",
            "centijoule": "1E+2",
            "decijoule": "1E+1",
            "decajoule": "1E-1",
            "hectojoule": "1E-2",
            "kilojoule": "1E-3",
            "megajoule": "1E-6",
            "gigajoule": "1E-9",
            "terajoule": "1E-12",
            "petajoule": "1E-15",
            "exajoule": "1E-18",
            "zettajoule": "1E-21",
            "yottajoule": "1E-24",
            "ronnajoule": "1E-27",
            "quettajoule": "1E-30",
            "watt hour": "0.0002777777777777777777777777778",
            "microwatt hour": "277.7777777777777777777777778",
            "milliwatt hour": "0.2777777777777777777777777778",
            "kilowatt hour": "2.777777777777777777777777778E-7",
            "megawatt hour": "2.777777777777777777777777778E-10",
            "gigawatt hour": "2.777777777777777777777777778E-13",
            "terawatt hour": "2.777777777777777777777777778E-16",
        }

        # Test all joule conversions
        self.check_units(self.base_unit, self.units, expected_values)
