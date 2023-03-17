# Copyright (c) 2022-2023 Mike Cunningham

from tests import AbstractTestCase


class TestMagneticFluxDensity(AbstractTestCase):

    def test_tesla(self) -> None:
        """ Test tesla conversions. """
        expected_values = {
            "gamma": "1E+9",
            "guass": "1E+4",
        }

        # Test all tesla conversions
        self.assert_metric_scale('tesla')
        self.assert_units('tesla', expected_values)
