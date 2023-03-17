# Copyright (c) 2022-2023 Mike Cunningham

from tests import AbstractTestCase


class TestElectricalCapacitance(AbstractTestCase):

    def test_farad(self):
        """ Test farad conversions. """
        self.assert_metric_scale('farad')
