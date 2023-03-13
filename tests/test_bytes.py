# Copyright (c) 2022-2023 Mike Cunningham


from tests import AbstractTestCase


class TestBytes(AbstractTestCase):

    def setUp(self) -> None:
        super().setUp()
        self.base_unit = self.converter.find_unit('bytes')
        self.units = self.converter.units['bytes']

    def test_bytes(self):
        """ Test byte conversions. """
        expected_values = {
            "bytes": "1",
            "bits": "8",
            "kilobytes": "0.001",
            "kibibytes": "0.0009765625",
            "kilobits": "0.008",
            "megabytes": "0.000001",
            "mebibytes": "9.532888465204957102001906578E-7",
            "megabits": "0.000008",
            "gigabytes": "1E-9",
            "gibibytes": "9.310986964618249534450651769E-10",
            "gigabits": "8E-9",
            "terabytes": "1E-12",
            "tebibytes": "9.090909090909090909090909091E-13",
            "terabits": "8E-12",
            "petabytes": "1E-15",
            "pebibytes": "8.880994671403197158081705151E-16",
            "petabits": "8E-15",
            "exabytes": "1E-18",
            "exbibytes": "8.673026886383347788378143972E-19",
            "exabits": "8E-18",
            "zettabytes": "1E-21",
            "zebibytes": "8.467400508044030482641828959E-22",
            "zettabits": "8E-21",
            "yottabytes": "1E-24",
            "yobibytes": "8.271298593879239040529363110E-25",
            "yottabits": "8E-24",
            "ronnabytes": "1E-27",
            "ronnabits": "8E-27",
            "quettabytes": "1E-30",
            "quettabits": "8E-30",
        }

        # Test all byte conversions
        self.check_units(self.base_unit, self.units, expected_values)
