# Copyright (c) 2022-2023 Mike Cunningham

from tests import AbstractTestCase


class TestPower(AbstractTestCase):

    def test_watt(self):
        """ Test watt conversions. """
        self.assert_metric_scale('watt')
        self.assert_unit('watt', 'joules per second', '1')
