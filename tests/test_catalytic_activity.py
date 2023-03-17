# Copyright (c) 2022-2023 Mike Cunningham

from tests import AbstractTestCase


class TestCatalyticActivity(AbstractTestCase):

    def test_katal(self):
        """ Test katal conversions. """
        self.assert_metric_scale('katal')
        self.assert_unit('katal', 'mole per second', '1')
