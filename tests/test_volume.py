# Copyright (c) 2022-2023 Mike Cunningham

from tests import AbstractTestCase, format_decimal


class TestVolume(AbstractTestCase):

    def setUp(self) -> None:
        super().setUp()
        self.base_unit = self.converter.find_unit('cubic meter')
        self.units = self.converter.units['volume']

    def test_cubic_meter(self) -> None:
        """ Test cubic meter conversions. """
        expected_values = {
            "cubic meter": "1",
            "cubic yoctometer": "1E+72",
            "cubic zeptometer": "1E+63",
            "cubic attometer": "1E+54",
            "cubic femtometer": "1E+45",
            "cubic picometer": "1E+36",
            "cubic nanometer": "1E+27",
            "cubic micrometer": "1E+18",
            "cubic millimeter": "1E+9",
            "cubic centimeter": "1E+6",
            "cubic decimeter": "1E+3",
            "cubic decameter": "1E-3",
            "cubic hectometer": "1E-6",
            "cubic kilometer": "1E-9",
            "cubic megameter": "1E-18",
            "cubic gigameter": "1E-27",
            "cubic terameter": "1E-36",
            "cubic petameter": "1E-45",
            "cubic exameter": "1E-54",
            "cubic zettameter": "1E-63",
            "cubic yottalmeter": "1E-72",
            "liter": "1E+3",
            "bushel": "28.37756923417453907733171392",
            "bushel (US)": "27.49617115816622535311957810",
            "cubic foot": "35.31472482766414284099898294",
            "cubic inch": "61023.61003472243410975706501",
            "cubic yard": "1.307950376362720798372909732",
            "cubic mile": "2.399232245681381957773512476E-10",
            "cup": "3519.508282458841110390785083",
            "cup (US)": "4226.757062911052124368099819",
            "fluid ounce": "35195.03327690396331269731216",
            "fluid ounce (US)": "33814.05650328841699494479855",
            "gallon": "219.9692482990877875273036829",
            "gallon (US, dry)": "227.0209404115435607780461670",
            "gallon (US, liquid)": "264.1720523581484153798999216",
            "pint": "1759.754760576566049755306101",
            "pint (US, dry)": "1816.165956523075591687571872",
            "pint (US, liquid)": "2113.378531455526062184049910",
            "quart": "879.8769931963511501092147318",
            "quart (US, dry)": "908.0829370308048974728959945",
            "quart (US, liquid)": "1056.688149136738616562741387",
            "tablespoon": "56312.01360498248696376885045",
            "tablespoon (US)": "67627.88432926664322233343252",
            "teaspoon": "168936.3832882723686975748169",
            "teaspoon (US)": "202884.1194890079412902050387",
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
