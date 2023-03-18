# Copyright (c) 2022-2023 Mike Cunningham

from tests import AbstractTestCase


class TestElectricPotential(AbstractTestCase):

    def test_volt(self):
        """ Test volt conversions. """
        self.assert_metric_scale('volt')
        self.assert_all_tested()
