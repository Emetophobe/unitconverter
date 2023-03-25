# Copyright (c) 2022-2023 Mike Cunningham

from decimal import Decimal
from unitconverter.unit import Unit


# The kelvin is the SI base unit of temperature
kelvin = Unit(
    name='kelvin',
    factor='1',
    symbols='K',
    aliases='kelvins',
    prefix_scaling='si')

# Celsius is a SI derived unit of temperature
# 1 celsius = 274.15 kelvin
celsius = Unit(
    name='celsius',
    factor='1',
    symbols='°C',
	aliases='Celsius',
	offset='273.15')

# Formula for °F to K: (32°F − 32) × 5/9 + 273.15 = 273.15K
# 1 fahrenheit = roughly 255.928 kelvin
fahrenheit = Unit(
    name='fahrenheit',
    factor=Decimal('1') / Decimal('1.8'),
    symbols=['°F', 'f'],
    offset=Decimal('273.15') - Decimal('32') / Decimal('1.8'))

# Formula for °R to K: 1°R × 5/9
# 1 rankine = roughly 0.555556 kelvin
rankine = Unit(
    name='rankine',
    factor=Decimal('5') / Decimal('9'),
    symbols=['°R', '°Ra', 'R'],
    aliases='rankines')
