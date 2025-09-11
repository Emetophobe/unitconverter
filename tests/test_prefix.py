# Copyright (c) 2022-2025 Mike Cunningham
# https://www.github.com/emetophobe/unitconverter


import unittest

from unitconverter.models.prefix import metric_prefixes, binary_prefixes, get_prefixes


class TestPrefix(unittest.TestCase):
    """ Tests for the Prefix class and related functions. """

    def test_get_prefixes(self) -> None:
        # Invalid prefix options should raise a TypeError
        with self.assertRaises(TypeError):
            get_prefixes("invalid option")

        self.assertEqual(get_prefixes("metric"), metric_prefixes)
        self.assertEqual(get_prefixes("binary"), binary_prefixes)
        self.assertEqual(get_prefixes(None), [])
