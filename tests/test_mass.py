# Copyright (c) 2022-2023 Mike Cunningham

from tests import AbstractTestCase


class TestMass(AbstractTestCase):

    def setUp(self) -> None:
        super().setUp()
        # SI uses kilograms as the base unit for historical
        # reasons. I use grams because it makes sense.
        self.base_unit = self.converter.find_unit('grams')
        self.units = self.all_units['mass']

    def test_grams(self) -> None:
        """ Test gram conversions. """
        expected_values = {
            "grams": "1",
            "yoctograms": "1E+24",
            "zeptograms": "1E+21",
            "attograms": "1E+18",
            "femtograms": "1E+15",
            "picograms": "1E+12",
            "nanograms": "1E+9",
            "micrograms": "1E+6",
            "milligrams": "1E+3",
            "centigrams": "1E+2",
            "decigrams": "1E+1",
            "decagrams": "1E-1",
            "hectograms": "1E-2",
            "kilograms": "1E-3",
            "megagrams": "1E-6",
            "gigagrams": "1E-9",
            "teragrams": "1E-12",
            "petagrams": "1E-15",
            "exagrams": "1E-18",
            "zettagrams": "1E-21",
            "yottalgrams": "1E-24",
            "carats": "5",
            "ounces": "0.03527396583786956534008335944",
            "pounds": "0.002204624420183777491666519692",
            "stones": "0.0001574731232746850931217314485",
            "tons (UK)": "9.842065361352906051876148631E-7",
            "tons (US)": "0.000001102311310924387903614869007",
            "tonnes": "1E-6",
        }

        # Test all gram conversions
        self.check_units(self.base_unit, self.units, expected_values)
