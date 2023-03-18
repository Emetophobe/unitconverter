# Copyright (c) 2022-2023 Mike Cunningham

from tests import AbstractTestCase


class TestElectricalConductance(AbstractTestCase):

    def test_siemens(self):
        """ Test siemens conversions. """
        self.assert_metric_scale('siemens')
        self.assert_all_tested()
