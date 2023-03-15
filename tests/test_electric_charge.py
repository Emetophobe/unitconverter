# Copyright (c) 2022-2023 Mike Cunningham

from tests import AbstractTestCase


class TestElectricCharge(AbstractTestCase):

    def setUp(self):
        super().setUp()
        self.base_unit = self.converter.find_unit('coulomb')
        self.units = self.converter.units['electric charge']

    def test_coulomb(self):
        """ Test coulomb conversions. """
        expected_values = {
            "coulomb": "1",
            "quectocoulomb": "1E+30",
            "rontocoulomb": "1E+27",
            "yoctocoulomb": "1E+24",
            "zeptocoulomb": "1E+21",
            "attocoulomb": "1E+18",
            "femtocoulomb": "1E+15",
            "picocoulomb": "1E+12",
            "nanocoulomb": "1E+9",
            "microcoulomb": "1E+6",
            "millicoulomb": "1E+3",
            "centicoulomb": "1E+2",
            "decicoulomb": "1E+1",
            "decacoulomb": "1E-1",
            "hectocoulomb": "1E-2",
            "kilocoulomb": "1E-3",
            "megacoulomb": "1E-6",
            "gigacoulomb": "1E-9",
            "teracoulomb": "1E-12",
            "petacoulomb": "1E-15",
            "exacoulomb": "1E-18",
            "zettacoulomb": "1E-21",
            "yottacoulomb": "1E-24",
            "ronnacoulomb": "1E-27",
            "quettacoulomb": "1E-30",
        }

        # Test all coulomb conversions
        self.check_units(self.base_unit, self.units, expected_values)
