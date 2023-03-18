# Copyright (c) 2022-2023 Mike Cunningham

from tests import AbstractTestCase


class TestRadioactivity(AbstractTestCase):

    def test_becquerel(self):
        """ Test becquerel conversions. """
        expected_values = {
            "rutherford": "1E-6",
            "curie": "2.702702702702702702702702703E-11",
            "picocurie": "2.702702702702702702702702703E+1"
        }

        self.assert_metric_scale('becquerel')
        self.assert_units('becquerel', expected_values)
        self.assert_all_tested()
