# Copyright (c) 2022-2023 Mike Cunningham

from tests import AbstractTestCase


class TestElectricalConductance(AbstractTestCase):

    def setUp(self):
        super().setUp()
        self.base_unit = self.converter.find_unit('siemens')
        self.units = self.converter.units['electrical conductance']

    def test_siemens(self):
        """ Test siemens conversions. """
        expected_values = {
            "siemens": "1",
            "quectosiemens": "1E+30",
            "rontosiemens": "1E+27",
            "yoctosiemens": "1E+24",
            "zeptosiemens": "1E+21",
            "attosiemens": "1E+18",
            "femtosiemens": "1E+15",
            "picosiemens": "1E+12",
            "nanosiemens": "1E+9",
            "microsiemens": "1E+6",
            "millisiemens": "1E+3",
            "centisiemens": "1E+2",
            "decisiemens": "1E+1",
            "decasiemens": "1E-1",
            "hectosiemens": "1E-2",
            "kilosiemens": "1E-3",
            "megasiemens": "1E-6",
            "gigasiemens": "1E-9",
            "terasiemens": "1E-12",
            "petasiemens": "1E-15",
            "exasiemens": "1E-18",
            "zettasiemens": "1E-21",
            "yottasiemens": "1E-24",
            "ronnasiemens": "1E-27",
            "quettasiemens": "1E-30",
        }

        # Test all siemens conversions
        self.check_units(self.base_unit, self.units, expected_values)
