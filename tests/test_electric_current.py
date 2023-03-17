# Copyright (c) 2022-2023 Mike Cunningham

from tests import AbstractTestCase


class TestElectricCurrent(AbstractTestCase):

    def test_ampere(self):
        """ Test ampere conversions. """
        self.assert_metric_scale('ampere')
