# Copyright (c) 2022-2023 Mike Cunningham

from tests import AbstractTestCase


class TestForce(AbstractTestCase):

    def test_newton(self):
        """ Test newton conversions. """
        expected_values = {
            "dyne": "1E+5",
            "poundal": "7.233013851209894380674993482",
            "gram-force": "101.9716212977928242570092743",
            "ounce-force": "3.596942455035521605214703294",
            "pound-force": "0.2248089236553391444941372081",
            "kilogram-force": "0.1019716212977928242570092743",
            "tonne-force": "0.0001019716212977928242570092743",
            "long ton-force": "0.0001003611353123707512991247381",
            "short ton-force": "0.0001124044715498552414550197067",
            "joule/meter": "1"
        }

        self.assert_metric_scale('newton')
        self.assert_units('newton', expected_values)
