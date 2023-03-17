# Copyright (c) 2022-2023 Mike Cunningham

from tests import AbstractTestCase


class TestPressure(AbstractTestCase):

    def test_pascal(self):
        """ Test pascal conversions. """
        expected_values = {
            "bar": "1E-5",
            "barye": "1E+1",
            "psi": "0.0001450376807894691040732382273"
        }

        self.assert_metric_scale('pascal')
        self.assert_units('pascal', expected_values)
