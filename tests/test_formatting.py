# Copyright (c) 2022-2023 Mike Cunningham


import unittest
from decimal import Decimal

from unitconverter.exceptions import ConverterError
from unitconverter.formatting import (format_decimal, format_display_name,
                                      format_exponent, format_name,
                                      parse_decimal, simplify_unit,
                                      split_exponent)
from unitconverter.unit import Unit


class TestFormatting(unittest.TestCase):
    """ Test formatting module. """

    def test_parse_decimal(self) -> None:
        """ Test parse_decimal() function. """

        # Only integers, strings, and decimals should be accepted
        parse_decimal(5)
        parse_decimal('3.14')
        parse_decimal(Decimal('3.15'))

        # Floats should raise an exception
        with self.assertRaises(ConverterError):
            parse_decimal(1.23)

        # Invalid decimals should raise an exception
        with self.assertRaises(ConverterError):
            parse_decimal('1.ab')

    def test_format_decimal(self) -> None:
        """ Test format_decimal() function. """
        value = Decimal('1785137.3268163479138125')

        # Assert decimal to string
        result = format_decimal(value)
        self.assertEqual('1785137.3268163479138125', result, 'Invalid result')

        msg = 'Invalid {} result'

        # Rounded string
        result = format_decimal(value, precision=5)
        self.assertEqual('1785137.32682', result, msg.format('rounded'))

        # Exponent string
        result = format_decimal(value, exponent=True)
        self.assertEqual('1.7851373268163479138125E+6', result, msg.format('exponent'))

        # Comma separated string
        result = format_decimal(value, commas=True)
        self.assertEqual('1,785,137.3268163479138125', result, msg.format('separated'))

        # Rounded exponent string
        result = format_decimal(value, exponent=True, precision=5)
        self.assertEqual('1.78514E+6', result, msg.format('rounded exponent'))

        # Rounded comma separated string
        result = format_decimal(value, precision=7, commas=True)
        self.assertEqual('1,785,137.3268163', result, msg.format('rounded separated'))

        # Removing trailing zeroes
        result = format_decimal(Decimal('1.23456789000000100000'))
        self.assertEqual('1.234567890000001', result, msg.format('trailing zeroes'))

        with self.assertRaises(ValueError):
            format_decimal('bad value')

        with self.assertRaises(ValueError):
            format_decimal(value, precision='bad precision')

    def test_format_name(self):
        """ Test format_name() function. """

        metre_per_second = Unit(1, {'metre': 1, 'second': -1}, {'length': 1, 'time': -1})
        self.assertEqual('metre*second^-1', format_name(metre_per_second.units))

        with self.assertRaises(AttributeError):
            format_name('not a dict')

    def test_format_display_name(self):
        """ Test format_display_name() function. """

        metre_per_second = Unit(1, {'metre': 1, 'second': -1}, {'length': 1, 'time': -1})
        self.assertEqual('metre/second', format_display_name(metre_per_second.units))

        with self.assertRaises(AttributeError):
            format_name(None)

    def test_format_exponent(self):
        """ Test format_exponent() function. """
        self.assertEqual('metre', format_exponent('metre', 1))
        self.assertEqual('second^2', format_exponent('second', 2))

    def test_split_exponent(self):
        """ Test split_exponent() function. """
        self.assertEqual(('second', 1), split_exponent('second'))
        self.assertEqual(('metre', 2), split_exponent('metre^2'))
        self.assertEqual(('metre', -2), split_exponent('metre-2'))

    def test_simplify_unit(self):
        """ Test simplify_unit() function. """
        self.assertEqual('Nm2/volt2', simplify_unit("Nm²/volt^2"))
        self.assertEqual("joule/gram", simplify_unit("joule per gram"))
