# Copyright (c) 2022-2023 Mike Cunningham

from unitconverter.unit import Unit


# SI unit of illuminance
lux = Unit(
	name='lux',
	symbols='lx',
	factor='1')

# 1 phot is exactly 10000 lux
phot = Unit(
	name='phot',
	symbols='ph',
	aliases='phots',
	factor='10000')

# 1 nox is exactly 0.001 lux
nox = Unit(
	name='nox',
	factor='0.001')

# 1 watt/m^2 is exactly 683 lux
watt_per_square_meter = Unit(
	name='watt per square meter',
	symbols=['W/m^2', 'W/m2'],
	aliases=['watt per square metre', 'watt/m^2', 'watt/m2'],
	prefix_index=0,
	factor='683')

# 1 meter candle is equal to 1 lux
meter_candle = Unit(
	name='meter candle',
	symbols='m*c',
	aliases='metre candle',
	factor='1')

# 1 foot candle is roughly 10.76391 lux
foot_candle = Unit(
	name='foot-candle',
	symbols=['ft*c', 'fc'],
	aliases='foot candle',
	factor='10.76391')
