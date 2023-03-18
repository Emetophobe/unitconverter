# Copyright (c) 2022-2023 Mike Cunningham

from tests import AbstractTestCase


class TestRadian(AbstractTestCase):

    def test_radian(self):
        """ Test radian conversions. """
        self.assert_metric_scale('radian')
        self.assert_all_tested()
