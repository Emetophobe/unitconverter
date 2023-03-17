# Copyright (c) 2022-2023 Mike Cunningham

from tests import AbstractTestCase


class TestDoseEquivalent(AbstractTestCase):

    def test_sievert(self):
        """ Test sievert conversions. """
        self.assert_metric_scale('sievert')
        self.assert_unit('sievert', 'roentgen equivalent man', '1E-2')
