# Copyright (c) 2022-2023 Mike Cunningham

from tests import AbstractTestCase


class TestBytes(AbstractTestCase):

    def setUp(self) -> None:
        super().setUp()
        self.base_unit = self.converter.find_unit('byte')
        self.units = self.converter.units['bytes']

    def test_byte(self):
        """ Test byte conversions. """
        expected_values = {
            "byte": "1",
            "bit": "8",
            "kilobyte": "1E-3",
            "kibibyte": "0.0009765625",
            "kilobit": "8E-3",
            "megabyte": "1E-6",
            "mebibyte": "9.532888465204957102001906578E-7",
            "megabit": "8E-6",
            "gigabyte": "1E-9",
            "gibibyte": "9.310986964618249534450651769E-10",
            "gigabit": "8E-9",
            "terabyte": "1E-12",
            "tebibyte": "9.090909090909090909090909091E-13",
            "terabit": "8E-12",
            "petabyte": "1E-15",
            "pebibyte": "8.880994671403197158081705151E-16",
            "petabit": "8E-15",
            "exabyte": "1E-18",
            "exbibyte": "8.673026886383347788378143972E-19",
            "exabit": "8E-18",
            "zettabyte": "1E-21",
            "zebibyte": "8.467400508044030482641828959E-22",
            "zettabit": "8E-21",
            "yottabyte": "1E-24",
            "yobibyte": "8.271298593879239040529363110E-25",
            "yottabit": "8E-24",
            "ronnabyte": "1E-27",
            "ronnabit": "8E-27",
            "quettabyte": "1E-30",
            "quettabit": "8E-30",
        }

        # Test all byte conversions
        self.check_units(self.base_unit, self.units, expected_values)
