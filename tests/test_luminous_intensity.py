# Copyright (c) 2022-2023 Mike Cunningham

from tests import AbstractTestCase


class TestLuminousIntensity(AbstractTestCase):

    def test_candela(self):
        """ Test candela conversions. """
        self.assert_metric_scale('candela')
