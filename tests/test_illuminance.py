# Copyright (c) 2022-2023 Mike Cunningham

from tests import AbstractTestCase


class TestIlluminance(AbstractTestCase):

    def test_lux(self):
        """ Test lux conversions. """
        self.assert_metric_scale('lux')
        self.assert_all_tested()
