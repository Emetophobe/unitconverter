# Copyright (c) 2022-2023 Mike Cunningham

from tests import AbstractTestCase


class TestPressure(AbstractTestCase):

    def setUp(self):
        super().setUp()
        self.base_unit = self.converter.find_unit('pascal')
        self.units = self.converter.units['pressure']

    def test_pascal(self):
        """ Test pascal conversions. """
        expected_values = {
            "pascal": "1",
            "quectopascal": "1E+30",
            "rontopascal": "1E+27",
            "yoctopascal": "1E+24",
            "zeptopascal": "1E+21",
            "attopascal": "1E+18",
            "femtopascal": "1E+15",
            "picopascal": "1E+12",
            "nanopascal": "1E+9",
            "micropascal": "1E+6",
            "millipascal": "1E+3",
            "centipascal": "1E+2",
            "decipascal": "1E+1",
            "decapascal": "1E-1",
            "hectopascal": "1E-2",
            "kilopascal": "1E-3",
            "megapascal": "1E-6",
            "gigapascal": "1E-9",
            "terapascal": "1E-12",
            "petapascal": "1E-15",
            "exapascal": "1E-18",
            "zettapascal": "1E-21",
            "yottapascal": "1E-24",
            "ronnapascal": "1E-27",
            "quettapascal": "1E-30",
            "bar": "1E-5",
            "barye": "1E+1",
            "psi": "0.0001450376807894691040732382273"
        }

        # Test all pascal conversions
        self.check_units(self.base_unit, self.units, expected_values)
