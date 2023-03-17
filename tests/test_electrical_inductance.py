# Copyright (c) 2022-2023 Mike Cunningham

from tests import AbstractTestCase


class TestElectricalInductance(AbstractTestCase):

    def test_henry(self):
        """ Test henry conversions. """
        self.assert_metric_scale('henry')
