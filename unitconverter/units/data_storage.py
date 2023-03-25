# Copyright (c) 2022-2023 Mike Cunningham

from unitconverter.unit import Unit


# byte is the base unit for data storage
byte = Unit(
    name='byte',
    factor='1',
    symbols='B',
    aliases='bytes',
    prefix_scaling='both')     # Scale bytes by decimal and binary prefixes

# 1 bit = 0.125 bytes
bit = Unit(
    name='bit',
    factor='0.125',
    symbols='b',
    aliases='bits',
    prefix_scaling='decimal')  # Scale bits by decimal prefixes
