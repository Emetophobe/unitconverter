# Copyright (c) 2022-2023 Mike Cunningham

from decimal import Decimal
from unitconverter.unit import Unit


# SI base unit
kelvin = Unit(
	name='kelvin',
	symbols='K',
	aliases='kelvins',
	factor='1')

# SI derived unit
celsius = Unit(
	name='celsius',
	symbols='°C', offset='273.15',
	factor='1')

# Formula for °F to K: (32°F − 32) × 5/9 + 273.15 = 273.15K
fahrenheit = Unit(
	name='fahrenheit',
	symbols=['°F', 'f'],
	factor=Decimal('1') / Decimal('1.8'),
	offset=Decimal('273.15') - Decimal('32') / Decimal('1.8'))

# Formula for °R to K: 1°R × 5/9
rankine = Unit(
	name='rankine',
	symbols=['°R', '°Ra', 'R', 'r'],
	aliases='rankines',
	factor=Decimal('5') / Decimal('9'))
