# Copyright (c) 2022-2023 Mike Cunningham

from tests import AbstractTestCase


class TestMagneticFlux(AbstractTestCase):

    def test_weber(self) -> None:
        """ Test weber conversions. """
        self.assert_metric_scale('weber')
        self.assert_unit('weber', 'maxwell', '1E+8')
