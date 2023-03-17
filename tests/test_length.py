# Copyright (c) 2022-2023 Mike Cunningham

from tests import AbstractTestCase


class TestLength(AbstractTestCase):

    def setUp(self) -> None:
        super().setUp()
        self.base_unit = self.converter.find_unit('meter')
        self.units = self.converter.units['length']

    def test_meter(self):
        """ Test meter conversions. """
        expected_values = {
            "meter": "1",
            "quectometer": "1E+30",
            "rontometer": "1E+27",
            "yoctometer": "1E+24",
            "zeptometer": "1E+21",
            "attometer": "1E+18",
            "femtometer": "1E+15",
            "picometer": "1E+12",
            "nanometer": "1E+9",
            "micrometer": "1E+6",
            "millimeter": "1E+3",
            "centimeter": "1E+2",
            "decimeter": "1E+1",
            "decameter": "1E-1",
            "hectometer": "1E-2",
            "kilometer": "1E-3",
            "megameter": "1E-6",
            "gigameter": "1E-9",
            "terameter": "1E-12",
            "petameter": "1E-15",
            "exameter": "1E-18",
            "zettameter": "1E-21",
            "yottameter": "1E-24",
            "ronnameter": "1E-27",
            "quettameter": "1E-30",
            "angstrom": "1E+10",

            "thousandth of an inch": "39370.07874015748031496062992",
            "foot": "3.280839895013123359580052493",
            "inch": "39.37007874015748031496062992",
            "yard": "1.093613298337707786526684164",
            "mile": "0.0006213711922373339696174341844",

            "furlong": "0.004970969537898671756939473475",
            "chain": "0.04970969537898671756939473475",
            "rod": "0.1988387815159468702775789390",

            # Nautical units
            "fathom": "0.5468066491688538932633420822",
            "cable length": "0.005399568034557235421166306695",
            "imperial cable length": "0.005396071659831642564213252752",
            "US cable length": "0.004555808656036446469248291572",
            "league": "0.0002071238165462932086171792636",
            "nautical mile": "0.0005399568034557235421166306695",

            # Astronomical units
            "planck length": "6.187927353732867176139352124E+34",
            "astronomical unit": "6.684587122268445495995953370E-12",
            "light year": "1.057004238586996733856902766E-16",
            "parsec": "3.240755744239556664614188029E-17",
        }

        # Test all meter conversions
        self.check_units(self.base_unit, self.units, expected_values)
