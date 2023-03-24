# Copyright (c) 2022-2023 Mike Cunningham

from unitconverter.unit import Unit


# The watt is the SI unit of power
watt = Unit(
	name='watt',
	symbols='W',
	aliases='watts',
	factor='1')

# 1 metric horsepower (hp) = roughly 735.5 watts
horsepower = Unit(
	name='horsepower',
	symbols='hp',
	aliases=['metric horsepower', 'metric hp'],
	factor='735.5')

# 1 mechanical horsepower (bhp) = roughly 745.7 watts
mechanical_horsepower = Unit(
	name='mechanical horsepower',
	symbols='bhp',
	aliases=['imperial horsepower', 'mechanical hp', 'imperial hp'],
	factor='745.7')

# 1 joule/sec is equal to 1 watt
joule_per_second = Unit(
	name='joule per second',
	symbols=['J/s', 'j/s'],
	aliases='joules per second',
	prefix_index=0,
	factor='1')

# 1 joule/min = roughly 0.0166666667 watts
joule_per_minute = Unit(
	name='joule per minute',
	symbols=['J/min', 'j/min'],
	aliases='joules per minute',
	prefix_index=0,
	factor='0.0166666667')

# 1 joule/hour = roughly 0.0002777778 watts
joule_per_hour = Unit(
	name='joule per hour',
	symbols=['J/hr', 'j/hr'],
	aliases='joules per hour',
	prefix_index=0,
	factor='0.0002777778')
