# Copyright (c) 2022-2023 Mike Cunningham

from tests import AbstractTestCase


class TestElectricalCapacitance(AbstractTestCase):

    def setUp(self):
        super().setUp()
        self.base_unit = self.converter.find_unit('farad')
        self.units = self.converter.units['electrical capacitance']

    def test_farad(self):
        """ Test farad conversions. """
        expected_values = {
            "farad": "1",
            "quectofarad": "1E+30",
            "rontofarad": "1E+27",
            "yoctofarad": "1E+24",
            "zeptofarad": "1E+21",
            "attofarad": "1E+18",
            "femtofarad": "1E+15",
            "picofarad": "1E+12",
            "nanofarad": "1E+9",
            "microfarad": "1E+6",
            "millifarad": "1E+3",
            "centifarad": "1E+2",
            "decifarad": "1E+1",
            "decafarad": "1E-1",
            "hectofarad": "1E-2",
            "kilofarad": "1E-3",
            "megafarad": "1E-6",
            "gigafarad": "1E-9",
            "terafarad": "1E-12",
            "petafarad": "1E-15",
            "exafarad": "1E-18",
            "zettafarad": "1E-21",
            "yottafarad": "1E-24",
            "ronnafarad": "1E-27",
            "quettafarad": "1E-30",
        }

        # Test all farad conversions
        self.check_units(self.base_unit, self.units, expected_values)
