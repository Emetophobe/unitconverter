# Copyright (c) 2022-2023 Mike Cunningham


from tests import AbstractTestCase


class TestTemperature(AbstractTestCase):

    def setUp(self):
        super().setUp()
        self.base_unit = self.converter.find_unit('kelvin')
        self.units = self.converter.units['temperature']

    def test_kelvin(self):
        """ Test kelvin conversions. """
        expected_values = {
            "kelvin": "1",
            "celsius": "-272.15",
            "fahrenheit": "-457.87",
            "rankine": "1.8",
        }

        # Test all kelvin conversions
        self.check_units(self.base_unit, self.units, expected_values)
