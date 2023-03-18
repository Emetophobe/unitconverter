# Copyright (c) 2022-2023 Mike Cunningham

from decimal import Decimal
from tests import AbstractTestCase, METRIC_TABLE


class TestArea(AbstractTestCase):

    def test_square_meter(self):
        """ Test square meter conversions. """
        expected_values = {
            "are": "1E-2",
            "arpent": "0.0002924923424971666947558226624",
            "acre": "0.0002471053814671653422482439292",
            "acre (US survey)": "0.0002471045524071689972744367869",
            "barn": "1E+28",
            "hectare": "1E-4",
            "hide": "0.000002061855670103092783505154639",
            "homestead": "0.000001544408634179324181168776200",
            "circular inch": "1973.525241769719368993170121",
            "circular mil": "1973525241.769719368993170121",
            "rood": "0.0009884215258686613689929757168",
            "section": "3.861021585478125428288766303E-7",
            "square": "0.1076391041670972230833350556",
            "square chain": "0.002471053814671653422482439292",
            "square inch": "1550.003100006200012400024800",
            "square foot": "10.76391041670972230833350556",
            "square foot (US survey)": "10.76386736114295424114588269",
            "square yard": "1.195990046301080256481500617",
            "square mil": "1550003100.006200012400024800",
            "square mile": "3.861021585424458472628811394E-7",
            "square mile (US survey)": "3.861006141382661958709651829E-7",
            "square nautical mile": "2.915451895043731778425655977E-7",
            "square rod": "0.03953686103474645475971902867",
            "square rod (US survey)": "0.03953686103474645475971902867",
            "township": "1.072505995952342722966012717E-8",
        }

        self.assert_metric_scale('square meter')
        self.assert_units('square meter', expected_values)
        self.assert_all_tested()

    def assert_metric_scale(self, unit: str) -> None:
        """ Test the metric scale for square meters. """
        for scale, _, prefix in METRIC_TABLE:
            name = unit.replace('meter', prefix + 'meter')
            self.assert_unit(name, unit, Decimal(scale) ** 2)
