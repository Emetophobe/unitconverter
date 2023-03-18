# Copyright (c) 2022-2023 Mike Cunningham

from tests import AbstractTestCase


class TestElectricalResistance(AbstractTestCase):

    def test_ohm(self):
        """ Test ohm conversions. """
        self.assert_metric_scale('ohm')
        self.assert_all_tested()
