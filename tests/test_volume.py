# Copyright (c) 2022-2023 Mike Cunningham

from decimal import Decimal
from tests import METRIC_TABLE, AbstractTestCase


class TestVolume(AbstractTestCase):

    def test_cubic_meter(self) -> None:
        """ Test cubic meter conversions. """
        expected_values = {
            "quectoliter": "1E+33",
            "rontoliter": "1E+30",
            "yoctoliter": "1E+27",
            "zeptoliter": "1E+24",
            "attoliter": "1E+21",
            "femtoliter": "1E+18",
            "picoliter": "1E+15",
            "nanoliter": "1E+12",
            "microliter": "1E+9",
            "milliliter": "1E+6",
            "centiliter": "1E+5",
            "deciliter": "1E+4",
            "liter": "1E+3",
            "decaliter": "1E+2",
            "hectoliter": "1E+1",
            "kiloliter": "1",
            "megaliter": "1E-3",
            "gigaliter": "1E-6",
            "teraliter": "1E-9",
            "petaliter": "1E-12",
            "exaliter": "1E-15",
            "zettaliter": "1E-18",
            "yottaliter": "1E-21",
            "ronnaliter": "1E-24",
            "quettaliter": "1E-27",

            "drop": "2E+7",
            "stere": "1",

            "cubic inch": "61023.61003472243410975706501",
            "cubic foot": "35.31472482766414284099898294",
            "cubic yard": "1.307950376362720798372909732",
            "cubic mile": "2.399232245681381957773512476E-10",

            "acre-inch": "0.009728558325380519841239388180",
            "acre-foot": "0.0008107131938211453397261716876",
            "acre-foot (US survey)": "0.0008107083294995443124005820015",

            "gill (imperial)": "7039.016564917682220781570165",
            "gill (US)": "8453.506979638037738145858500",

            "cup (metric)": "4E+3",
            "cup (imperial)": "3519.508282458841110390785083",
            "cup (US)": "4226.757062911052124368099819",

            "bushel (imperial)": "27.49617115816622535311957810",
            "bushel (US)": "28.37756923417453907733171392",

            "fluid ounce (imperial)": "35195.07972785404600436858927",
            "fluid ounce (US)": "33814.05650328841699494479855",

            "gallon (imperial)": "219.9692482990877875273036829",
            "gallon (US liquid)": "264.1720523581484153798999216",
            "gallon (US dry)": "227.0209404115435607780461670",

            "pint (imperial)": "1759.754760576566049755306101",
            "pint (US liquid)": "2113.378531455526062184049910",
            "pint (US dry)": "1816.165956523075591687571872",

            "quart (imperial)": "879.8769931963511501092147318",
            "quart (US liquid)": "1056.688149136738616562741387",
            "quart (US dry)": "908.0829370308048974728959945",

            "tablespoon (metric)": "66666.66666666666666666666667",
            "tablespoon (imperial)": "56312.01360498248696376885045",
            "tablespoon (US)": "67627.88432926664322233343252",

            "teaspoon (metric)": "2E+5",
            "teaspoon (imperial)": "168936.3832882723686975748169",
            "teaspoon (US)": "202884.1353535182602415581444"
        }

        self.assert_metric_scale('cubic meter')
        self.assert_units('cubic meter', expected_values)

    def test_rounding(self) -> None:
        """ Test rounding volume units. """
        expected_values = {
            "drop": "2.00000E+7",

            "cubic foot": "3.53147E+1",
            "cubic inch": "6.10236E+4",
            "cubic yard": "1.30795E+0",
            "cubic mile": "2.39923E-10",

            "acre-inch": "0.009728558325380519841239388180",
            "acre-foot": "0.0008107131938211453397261716876",
            "acre-foot (US survey)": "0.0008107083294995443124005820015",

            "cup (metric)": "4.00000E+3",
            "cup (imperial)": "3.51951E+3",
            "cup (US)": "4.22676E+3",

            "gill (imperial)": "7.03902E+3",
            "gill (US)": "8.45351E+3",

            "bushel (imperial)": "2.74962E+1",
            "bushel (US)": "2.83776E+1",

            "fluid ounce (imperial)": "3.51951E+4",
            "fluid ounce (US)": "3.38141E+4",

            "gallon (imperial)": "2.19969E+2",
            "gallon (US liquid)": "2.64172E+2",
            "gallon (US dry)": "2.27021E+2",

            "pint (imperial)": "1.75975E+3",
            "pint (US liquid)": "2.11338E+3",
            "pint (US dry)": "1.81617E+3",

            "quart (imperial)": "8.79877E+2",
            "quart (US liquid)": "1.05669E+3",
            "quart (US dry)": "9.08083E+2",

            "tablespoon (metric)": "6.66667E+4",
            "tablespoon (imperial)": "5.63120E+4",
            "tablespoon (US)": "6.76279E+4",

            "teaspoon (metric)": "2.00000E+5",
            "teaspoon (imperial)": "1.68936E+5",
            "teaspoon (US)": "2.02884E+5",
        }

        for name, expected in expected_values.items():
            self.assert_unit('cubic meter', name, expected, exponent=True, precision=5)

    def assert_metric_scale(self, unit: str) -> None:
        """ Test the metric scale for cubic meters. """
        for scale, _, prefix in METRIC_TABLE:
            name = unit.replace('meter', prefix + 'meter')
            self.assert_unit(name, unit, Decimal(scale) ** 3)
