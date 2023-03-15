# Copyright (c) 2022-2023 Mike Cunningham

from tests import AbstractTestCase


class TestTime(AbstractTestCase):

    def setUp(self):
        super().setUp()
        self.base_unit = self.converter.find_unit('seconds')
        self.units = self.all_units['time']

    def test_seconds(self):
        """ Test second conversions. """
        expected_values = {
            "seconds": "1",
            "yoctoseconds": "1E+24",
            "zeptoseconds": "1E+21",
            "attoseconds": "1E+18",
            "femtoseconds": "1E+15",
            "picoseconds": "1E+12",
            "nanoseconds": "1E+9",
            "microseconds": "1E+6",
            "milliseconds": "1E+3",
            "centiseconds": "1E+2",
            "deciseconds": "1E+1",
            "decaseconds": "1E-1",
            "hectoseconds": "1E-2",
            "kiloseconds": "1E-3",
            "megaseconds": "1E-6",
            "gigaseconds": "1E-9",
            "teraseconds": "1E-12",
            "petaseconds": "1E-15",
            "exaseconds": "1E-18",
            "zettaseconds": "1E-21",
            "yottalseconds": "1E-24",
            "minutes": "0.01666666666666666666666666667",
            "hours": "0.0002777777777777777777777777778",
            "days": "0.00001157407407407407407407407407",
            "weeks": "0.000001653439153439153439153439153",
            "fortnights": "8.267195767195767195767195767E-7",
            "months": "3.805175038051750380517503805E-7",
            "years": "3.170979198376458650431253171E-8",
            "years (gregorian)": "3.168873850681143096456210346E-8",
            "years (julian)": "3.168808781402895023702689685E-8",
            "years (leap)": "3.162315320785266140457397288E-8",
            "decades": "3.170979198376458650431253171E-9",
            "centuries": "3.170979198376458650431253171E-10",
            "millennia": "3.170979198376458650431253171E-11",
        }

        # Test all second conversions
        self.check_units(self.base_unit, self.units, expected_values)
