# Copyright (c) 2022-2023 Mike Cunningham

from tests import AbstractTestCase


class TestSteradian(AbstractTestCase):

    def test_steradian(self):
        """ Test steradian conversions. """
        self.assert_metric_scale('steradian')
