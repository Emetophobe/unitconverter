# Copyright (c) 2022-2023 Mike Cunningham

from tests import AbstractTestCase


class TestAmountSubstance(AbstractTestCase):

    def test_mole(self):
        """ Test mole conversions. """
        self.assert_metric_scale('mole')
        self.assert_unit('mole', 'atom', "602214150000004428050534.2425")
        self.assert_all_tested()
