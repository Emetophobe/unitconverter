# Copyright (c) 2022-2023 Mike Cunningham

from tests import AbstractTestCase


class TestTime(AbstractTestCase):

    def test_second(self):
        """ Test second conversions. """
        expected_values = {
            "minute": "0.01666666666666666666666666667",
            "hour": "0.0002777777777777777777777777778",
            "day": "0.00001157407407407407407407407407",
            "week": "0.000001653439153439153439153439153",
            "fortnight": "8.267195767195767195767195767E-7",
            "month": "3.805175038051750380517503805E-7",
            "year": "3.170979198376458650431253171E-8",
            "year (gregorian)": "3.168873850681143096456210346E-8",
            "year (julian)": "3.168808781402895023702689685E-8",
            "year (leap)": "3.162315320785266140457397288E-8",
            "decade": "3.170979198376458650431253171E-9",
            "century": "3.170979198376458650431253171E-10",
            "millennia": "3.170979198376458650431253171E-11",
        }

        self.assert_metric_scale('second')
        self.assert_units('second', expected_values)
        self.assert_all_tested()
