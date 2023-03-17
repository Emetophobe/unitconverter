# Copyright (c) 2022-2023 Mike Cunningham

from tests import AbstractTestCase


class TestLength(AbstractTestCase):

    def test_meter(self):
        """ Test meter conversions. """
        expected_values = {
            "angstrom": "1E+10",

            "inch": "39.37007874015748031496062992",
            "hand": "9.842519685039370078740157480",
            "foot": "3.280839895013123359580052493",
            "yard": "1.093613298337707786526684164",
            "mile": "0.0006213711922373339696174341844",

            # Surveying units
            "chain": "0.04970969537898671756939473475",
            "chain (US survey)": "0.04970959595880638040762400977",
            "furlong": "0.004970969537898671756939473475",
            "furlong (US survey)": "0.004970959595880638040762400977",
            "link": "4.970969537898671756939473475",
            "link (US survey)": "4.970959596869055613114048180",
            "rod": "0.1988387815159468702775789390",
            "rod (US survey)": "0.1988383838391791919191951006",
            "furlong": "0.004970969537898671756939473475",
            "furlong (US survey)": "0.004970959595880638040762400977",

            # Nautical units
            "cable length": "0.005399568034557235421166306695",
            "cable length (imperial)": "0.005396071659831642564213252752",
            "cable length (US)": "0.004555808656036446469248291572",
            "fathom": "0.5468066491688538932633420822",
            "fathom (US survey)": "0.5468055555577427777777865267",
            "league": "0.0002071238165462932086171792636",
            "nautical mile": "0.0005399568034557235421166306695",
            "nautical mile (UK)": "0.0005396118248376847630888244233",

            # Astronomical units
            "planck length": "6.187927353732867176139352124E+34",
            "astronomical unit": "6.684587122268445495995953370E-12",
            "light second": "3.335640951981520495755767145E-9",
            "light minute": "3.860695546274907981198804566E-14",
            "light year": "1.057004238586996733856902766E-16",
            "parsec": "3.240755744239556664614188029E-17",
            "kiloparsec": "3.240779289666400167929923506E-20",
            "megaparsec": "3.240779289666400167929923506E-23",
            "gigaparsec": "3.240779289666400167929923506E-26",

            # Typesetting units
            "twip": "56692.87767377784328954753414",
            "point": "2834.645490730992709858726938",

            # Other
            "caliber": "3937.007874015748031496062992",
            "mil": "39370.07874015748031496062992",
        }

        self.assert_metric_scale('meter')
        self.assert_units('meter', expected_values)
