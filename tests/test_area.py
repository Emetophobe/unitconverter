# Copyright (c) 2022-2023 Mike Cunningham

from decimal import Decimal
from tests import AbstractTestCase, METRIC_TABLE


class TestArea(AbstractTestCase):

    def test_square_meter(self):
        """ Test square meter conversions. """
        expected_values = {
            "are": "1E-2",
            "hectare": "1E-4",
            "square inch": "1550.003100006200012400024800",
            "square foot": "10.76391041670972230833350556",
            "square foot (US survey)": "10.76386736114295424114588269",
            "square yard": "1.195990046301080256481500617",
            "square mile": "3.861021585424458472628811394E-7",
            "square nautical mile": "2.915451895043731778425655977E-7",
            "circular inch": "1973.525241769719368993170121",
            "square rod": "0.03953686103474645475971902867",
            "imperial acre": "0.0002471053814671653422482439292",
            "US survey acre": "0.0002471045524071689972744367869",
            "hide": "0.000002061855670103092783505154639",
            "rood": "0.0009884215258686613689929757168",
            "square": "0.1076391041670972230833350556",
            "survey township": "1.072505995952342722966012717E-8",
        }

        self.assert_metric_scale('square meter')
        self.assert_units('square meter', expected_values)

    def assert_metric_scale(self, unit: str) -> None:
        """ Overloaded metric scale to handle square meters. """
        for scale, _, prefix in METRIC_TABLE:

            name = unit.replace('meter', prefix + 'meter')
            expected = Decimal(scale) * Decimal(scale)
            self.assert_unit(name, unit, expected)
