# Copyright (c) 2022-2023 Mike Cunningham

from tests import AbstractTestCase


class TestTemperature(AbstractTestCase):

    def test_kelvin(self):
        """ Test kelvin conversions. """
        expected_values = {
            "celsius": "-272.15",
            "fahrenheit": "-457.87",
            "rankine": "1.8",
        }

        self.assert_metric_scale('kelvin')
        self.assert_units('kelvin', expected_values)
        self.assert_all_tested()
