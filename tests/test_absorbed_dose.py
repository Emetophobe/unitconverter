# Copyright (c) 2022-2023 Mike Cunningham

from tests import AbstractTestCase


class TestAbsorbedDose(AbstractTestCase):

    def test_gray(self):
        """ Test gray metric scale. """
        self.assert_metric_scale('gray')
