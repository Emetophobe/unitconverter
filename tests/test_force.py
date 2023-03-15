# Copyright (c) 2022-2023 Mike Cunningham

from tests import AbstractTestCase


class TestForce(AbstractTestCase):

    def setUp(self) -> None:
        super().setUp()
        self.base_unit = self.converter.find_unit('newtons')
        self.units = self.converter.units['force']

    def test_force(self):
        """ Test newton conversions. """
        expected_values = {
            "newtons": "1",
            "quectonewtons": "1E+30",
            "rontonewtons": "1E+27",
            "yoctonewtons": "1E+24",
            "zeptonewtons": "1E+21",
            "attonewtons": "1E+18",
            "femtonewtons": "1E+15",
            "piconewtons": "1E+12",
            "nanonewtons": "1E+9",
            "micronewtons": "1E+6",
            "millinewtons": "1E+3",
            "centinewtons": "1E+2",
            "decinewtons": "1E+1",
            "decanewtons": "1E-1",
            "hectonewtons": "1E-2",
            "kilonewtons": "1E-3",
            "meganewtons": "1E-6",
            "giganewtons": "1E-9",
            "teranewtons": "1E-12",
            "petanewtons": "1E-15",
            "exanewtons": "1E-18",
            "zettanewtons": "1E-21",
            "yottanewtons": "1E-24",
            "ronnanewtons": "1E-27",
            "quettanewtons": "1E-30",
            "dynes": "1E+5",
            "kilogram-force": "0.1019716212977928242570092743",
            "pound-force": "0.2248089236553391444941372081",
            "poundals": "7.233013851209894380674993482",
        }

        # Test all newton conversions
        self.check_units(self.base_unit, self.units, expected_values)
