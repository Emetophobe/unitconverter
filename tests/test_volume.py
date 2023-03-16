# Copyright (c) 2022-2023 Mike Cunningham

from tests import AbstractTestCase, format_decimal


class TestVolume(AbstractTestCase):

    def setUp(self) -> None:
        super().setUp()
        self.base_unit = self.converter.find_unit('cubic meters')
        self.units = self.converter.units['volume']

    def test_cubic_meters(self) -> None:
        """ Test cubic meter conversions. """
        expected_values = {
            "cubic meters": "1",
            "cubic yoctometers": "1E+72",
            "cubic zeptometers": "1E+63",
            "cubic attometers": "1E+54",
            "cubic femtometers": "1E+45",
            "cubic picometers": "1E+36",
            "cubic nanometers": "1E+27",
            "cubic micrometers": "1E+18",
            "cubic millimeters": "1E+9",
            "cubic centimeters": "1E+6",
            "cubic decimeters": "1E+3",
            "cubic decameters": "1E-3",
            "cubic hectometers": "1E-6",
            "cubic kilometers": "1E-9",
            "cubic megameters": "1E-18",
            "cubic gigameters": "1E-27",
            "cubic terameters": "1E-36",
            "cubic petameters": "1E-45",
            "cubic exameters": "1E-54",
            "cubic zettameters": "1E-63",
            "cubic yottalmeters": "1E-72",
            "liters": "1E+3",
            "bushels": "28.37756923417453907733171392",
            "bushels (US)": "27.49617115816622535311957810",
            "cubic feet": "35.31472482766414284099898294",
            "cubic inches": "61023.61003472243410975706501",
            "cubic yards": "1.307950376362720798372909732",
            "cups": "3519.508282458841110390785083",
            "cups (US)": "4226.757062911052124368099819",
            "fluid ounces": "35195.03327690396331269731216",
            "fluid ounces (US)": "33814.05650328841699494479855",
            "gallons": "219.9692482990877875273036829",
            "gallons (US, dry)": "227.0209404115435607780461670",
            "gallons (US, liquid)": "264.1720523581484153798999216",
            "pints": "1759.754760576566049755306101",
            "pints (US, dry)": "1816.165956523075591687571872",
            "pints (US, liquid)": "2113.378531455526062184049910",
            "quarts": "879.8769931963511501092147318",
            "quarts (US, dry)": "908.0829370308048974728959945",
            "quarts (US, liquid)": "1056.688149136738616562741387",
            "tablespoons": "56312.01360498248696376885045",
            "tablespoons (US)": "67627.88432926664322233343252",
            "teaspoons": "168936.3832882723686975748169",
            "teaspoons (US)": "202884.1194890079412902050387",
        }

        # Test all cubic meter conversions
        self.check_units(self.base_unit, self.units, expected_values)

    def test_rounding(self) -> None:
        """ Test rounding volume units. """
        expected_values = {
            "bushels": "28.37757",
            "bushels (US)": "27.49617",
            "cubic feet": "35.31472",
            "cubic inches": "61023.61003",
            "cubic yards": "1.30795",
            "cups": "3519.50828",
            "cups (US)": "4226.75706",
            "fluid ounces": "35195.03328",
            "fluid ounces (US)": "33814.05650",
            "gallons": "219.96925",
            "gallons (US, dry)": "227.02094",
            "gallons (US, liquid)": "264.17205",
            "pints": "1759.75476",
            "pints (US, dry)": "1816.16596",
            "pints (US, liquid)": "2113.37853",
            "quarts": "879.87699",
            "quarts (US, dry)": "908.08294",
            "quarts (US, liquid)": "1056.68815",
            "tablespoons": "56312.01360",
            "tablespoons (US)": "67627.88433",
            "teaspoons": "168936.38329",
            "teaspoons (US)": "202884.11949",
        }

        for name, expected in expected_values.items():
            dest_unit = self.converter.find_unit(name)
            result = self.converter.convert(self.base_value, self.base_unit, dest_unit)
            rounded = format_decimal(result, precision=5)
            self.assertEqual(rounded, expected, 'Value mismatch')
