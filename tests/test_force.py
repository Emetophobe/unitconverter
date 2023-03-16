# Copyright (c) 2022-2023 Mike Cunningham

from tests import AbstractTestCase


class TestForce(AbstractTestCase):

    def setUp(self) -> None:
        super().setUp()
        self.base_unit = self.converter.find_unit('newton')
        self.units = self.converter.units['force']

    def test_newton(self):
        """ Test newton conversions. """
        expected_values = {
            "newton": "1",
            "quectonewton": "1E+30",
            "rontonewton": "1E+27",
            "yoctonewton": "1E+24",
            "zeptonewton": "1E+21",
            "attonewton": "1E+18",
            "femtonewton": "1E+15",
            "piconewton": "1E+12",
            "nanonewton": "1E+9",
            "micronewton": "1E+6",
            "millinewton": "1E+3",
            "centinewton": "1E+2",
            "decinewton": "1E+1",
            "decanewton": "1E-1",
            "hectonewton": "1E-2",
            "kilonewton": "1E-3",
            "meganewton": "1E-6",
            "giganewton": "1E-9",
            "teranewton": "1E-12",
            "petanewton": "1E-15",
            "exanewton": "1E-18",
            "zettanewton": "1E-21",
            "yottanewton": "1E-24",
            "ronnanewton": "1E-27",
            "quettanewton": "1E-30",
            "dyne": "1E+5",
            "kilogram-force": "0.1019716212977928242570092743",
            "pound-force": "0.2248089236553391444941372081",
            "poundal": "7.233013851209894380674993482",
        }

        # Test all newton conversions
        self.check_units(self.base_unit, self.units, expected_values)
