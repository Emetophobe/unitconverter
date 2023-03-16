# Copyright (c) 2022-2023 Mike Cunningham

from tests import AbstractTestCase


class TestTime(AbstractTestCase):

    def setUp(self):
        super().setUp()
        self.base_unit = self.converter.find_unit('second')
        self.units = self.all_units['time']

    def test_second(self):
        """ Test second conversions. """
        expected_values = {
            "second": "1",
            "quectosecond": "1E+30",
            "rontosecond": "1E+27",
            "yoctosecond": "1E+24",
            "zeptosecond": "1E+21",
            "attosecond": "1E+18",
            "femtosecond": "1E+15",
            "picosecond": "1E+12",
            "nanosecond": "1E+9",
            "microsecond": "1E+6",
            "millisecond": "1E+3",
            "centisecond": "1E+2",
            "decisecond": "1E+1",
            "decasecond": "1E-1",
            "hectosecond": "1E-2",
            "kilosecond": "1E-3",
            "megasecond": "1E-6",
            "gigasecond": "1E-9",
            "terasecond": "1E-12",
            "petasecond": "1E-15",
            "exasecond": "1E-18",
            "zettasecond": "1E-21",
            "yottasecond": "1E-24",
            "ronnasecond": "1E-27",
            "quettasecond": "1E-30",
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

        # Test all second conversions
        self.check_units(self.base_unit, self.units, expected_values)
