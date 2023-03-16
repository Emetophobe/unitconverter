# Copyright (c) 2022-2023 Mike Cunningham

from tests import AbstractTestCase


class TestMass(AbstractTestCase):

    def setUp(self) -> None:
        super().setUp()
        # SI uses kilograms as the base unit for historical
        # reasons. I use grams because it makes sense.
        self.base_unit = self.converter.find_unit('gram')
        self.units = self.all_units['mass']

    def test_gram(self) -> None:
        """ Test gram conversions. """
        expected_values = {
            "gram": "1",
            "quectogram": "1E+30",
            "rontogram": "1E+27",
            "yoctogram": "1E+24",
            "zeptogram": "1E+21",
            "attogram": "1E+18",
            "femtogram": "1E+15",
            "picogram": "1E+12",
            "nanogram": "1E+9",
            "microgram": "1E+6",
            "milligram": "1E+3",
            "centigram": "1E+2",
            "decigram": "1E+1",
            "decagram": "1E-1",
            "hectogram": "1E-2",
            "kilogram": "1E-3",
            "megagram": "1E-6",
            "gigagram": "1E-9",
            "teragram": "1E-12",
            "petagram": "1E-15",
            "exagram": "1E-18",
            "zettagram": "1E-21",
            "yottagram": "1E-24",
            "ronnagram": "1E-27",
            "quettagram": "1E-30",
            "ounce": "0.03527396583786956534008335944",
            "pound": "0.002204624420183777491666519692",
            "stone": "0.0001574731232746850931217314485",
            "ton (UK)": "9.842065361352906051876148631E-7",
            "ton (US)": "0.000001102311310924387903614869007",
            "tonne": "1E-6",
            "carat": "5",
            "grain": "15.43236073451864152014926179",
            "drachm": "0.5643818607669949487823461354",
            "pennyweight": "0.6430149313725596104420069206",
            "troy ounce": "0.03215072258749015384120758114",
            "troy pound": "0.002679226882290846153433965095",
        }

        # Test all gram conversions
        self.check_units(self.base_unit, self.units, expected_values)
