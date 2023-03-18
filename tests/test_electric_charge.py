# Copyright (c) 2022-2023 Mike Cunningham

from tests import AbstractTestCase


class TestElectricCharge(AbstractTestCase):

    def test_coulomb(self):
        """ Test coulomb conversions. """
        self.assert_metric_scale('coulomb')
        self.assert_all_tested()
