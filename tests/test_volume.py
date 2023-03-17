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

            "stere": "1",

            "cubic inch": "61023.61003472243410975706501",
            "cubic foot": "35.31472482766414284099898294",
            "cubic yard": "1.307950376362720798372909732",
            "cubic mile": "2.399232245681381957773512476E-10",

            "imperial gill": "7039.016564917682220781570165",
            "US gill": "8453.506979638037738145858500",

            "metric cup": "4E+3",
            "imperial cup": "3519.508282458841110390785083",
            "US cup": "4226.757062911052124368099819",

            "imperial bushel": "27.49617115816622535311957810",
            "US bushel": "28.37756923417453907733171392",

            "imperial fluid ounce": "35195.07972785404600436858927",
            "US fluid ounce": "33814.05650328841699494479855",

            "imperial gallon": "219.9692482990877875273036829",
            "US liquid gallon": "264.1720523581484153798999216",
            "US dry gallon": "227.0209404115435607780461670",

            "imperial pint": "1759.754760576566049755306101",
            "US liquid pint": "2113.378531455526062184049910",
            "US dry pint": "1816.165956523075591687571872",

            "imperial quart": "879.8769931963511501092147318",
            "US liquid quart": "1056.688149136738616562741387",
            "US dry quart": "908.0829370308048974728959945",

            "metric tablespoon": "66666.66666666666666666666667",
            "imperial tablespoon": "56312.01360498248696376885045",
            "US tablespoon": "67627.88432926664322233343252",

            "metric teaspoon": "2E+5",
            "imperial teaspoon": "168936.3832882723686975748169",
            "US teaspoon": "202884.1353535182602415581444"
        }

        self.assert_metric_scale('cubic meter')
        self.assert_units('cubic meter', expected_values)

    def test_rounding(self) -> None:
        """ Test rounding volume units. """
        expected_values = {
            "cubic foot": "3.53147E+1",
            "cubic inch": "6.10236E+4",
            "cubic yard": "1.30795E+0",
            "cubic mile": "2.39923E-10",

            "imperial gill": "7.03902E+3",
            "US gill": "8.45351E+3",

            "metric cup": "4.00000E+3",
            "imperial cup": "3.51951E+3",
            "US cup": "4.22676E+3",

            "imperial fluid ounce": "3.51951E+4",
            "US fluid ounce": "3.38141E+4",

            "imperial gallon": "2.19969E+2",
            "US liquid gallon": "2.64172E+2",
            "US dry gallon": "2.27021E+2",

            "imperial pint": "1.75975E+3",
            "US liquid pint": "2.11338E+3",
            "US dry pint": "1.81617E+3",

            "imperial quart": "8.79877E+2",
            "US liquid quart": "1.05669E+3",
            "US dry quart": "9.08083E+2",

            "metric tablespoon": "6.66667E+4",
            "imperial tablespoon": "5.63120E+4",
            "US tablespoon": "6.76279E+4",

            "metric teaspoon": "2.00000E+5",
            "imperial teaspoon": "1.68936E+5",
            "US teaspoon": "2.02884E+5",
        }

        for name, expected in expected_values.items():
            self.assert_unit('cubic meter', name, expected, exponent=True, precision=5)

    def assert_metric_scale(self, unit: str) -> None:
        """ Overloaded metric scale to handle cubic meters. """
        for scale, _, prefix in METRIC_TABLE:

            name = unit.replace('meter', prefix + 'meter')
            expected = Decimal(scale) ** 3
            self.assert_unit(name, unit, expected)
