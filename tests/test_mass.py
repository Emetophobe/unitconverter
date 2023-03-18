# Copyright (c) 2022-2023 Mike Cunningham

from tests import AbstractTestCase


class TestMass(AbstractTestCase):

    def test_gram(self) -> None:
        """ Test gram conversions. """
        expected_values = {
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

        # SI uses kilograms as the base unit for historical reasons.
        # I use grams because it makes sense.
        self.assert_metric_scale('gram')
        self.assert_units('gram', expected_values)
        self.assert_all_tested()
