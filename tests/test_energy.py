# Copyright (c) 2022-2023 Mike Cunningham

from tests import AbstractTestCase


class TestEnergy(AbstractTestCase):

    def test_joule(self):
        """ Test joule conversions. """
        expected_values = {
            "watt hour": "0.0002777777777777777777777777778",
            "microwatt hour": "277.7777777777777777777777778",
            "milliwatt hour": "0.2777777777777777777777777778",
            "kilowatt hour": "2.777777777777777777777777778E-7",
            "megawatt hour": "2.777777777777777777777777778E-10",
            "gigawatt hour": "2.777777777777777777777777778E-13",
            "terawatt hour": "2.777777777777777777777777778E-16",
        }

        self.assert_metric_scale('joule')
        self.assert_units('joule', expected_values)
        self.assert_all_tested()
