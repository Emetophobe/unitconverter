# Copyright (c) 2022-2023 Mike Cunningham

from decimal import Decimal
from unitconverter.unit import Unit


# The kelvin is the SI base unit of temperature
kelvin = Unit(
    name='kelvin',
    symbols='K',
    aliases='kelvins',
    factor='1')

# Celsius is a SI derived unit of temperature
# 1 celsius = 274.15 kelvin
celsius = Unit(
    name='celsius',
    symbols='°C',
	aliases='Celsius',
	factor='1',
	offset='273.15',
	prefix_scaling='none')

# Formula for °F to K: (32°F − 32) × 5/9 + 273.15 = 273.15K
# 1 fahrenheit = roughly 255.928 kelvin
fahrenheit = Unit(
    name='fahrenheit',
    symbols=['°F', 'f'],
    factor=Decimal('1') / Decimal('1.8'),
    offset=Decimal('273.15') - Decimal('32') / Decimal('1.8'),
	prefix_scaling='none')

# Formula for °R to K: 1°R × 5/9
# 1 rankine = roughly 0.555556 kelvin
rankine = Unit(
    name='rankine',
    symbols=['°R', '°Ra', 'R'],
    aliases='rankines',
    factor=Decimal('5') / Decimal('9'),
    prefix_scaling='none')
