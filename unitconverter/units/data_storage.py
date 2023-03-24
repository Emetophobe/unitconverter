# Copyright (c) 2022-2023 Mike Cunningham

from unitconverter.unit import Unit


# byte is the base unit for data storage
byte = Unit(
	name='byte',
	symbols='B',
	aliases='bytes',
	factor='1',
	prefix_scaling='both')     # Scale bytes by decimal and binary prefixes

# 1 bit = 0.125 bytes
bit = Unit(
	name='bit',
	symbols='b',
	aliases='bits',
	factor='0.125',
	prefix_scaling='decimal')  # Scale bits by decimal prefixes
