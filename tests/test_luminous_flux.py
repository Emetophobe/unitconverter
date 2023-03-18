# Copyright (c) 2022-2023 Mike Cunningham

from tests import AbstractTestCase


class TestLuminousFlux(AbstractTestCase):

    def test_lumen(self):
        """ Test lumen conversions. """
        self.assert_metric_scale('lumen')
        self.assert_all_tested()
