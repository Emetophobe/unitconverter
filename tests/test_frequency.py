# Copyright (c) 2022-2023 Mike Cunningham

from tests import AbstractTestCase


class TestFrequency(AbstractTestCase):

    def test_hertz(self):
        """ Test hertz conversions. """
        self.assert_metric_scale('hertz')
