# Copyright (c) 2022-2023 Mike Cunningham

from unitconverter.unit import Unit


# SI unit
watt = Unit(
    name='watt',
    symbols='W',
    aliases='watts',
    factor='1')

horsepower = Unit(
	name='horsepower',
	symbols='hp',
	aliases=['metric horsepower', 'metric hp'],
	factor='735.5')

mechanical_horsepower = Unit(
	name='mechanical horsepower',
	symbols='bhp',
	aliases=['imperial horsepower', 'mechanical hp', 'imperial hp'],
	factor='745.7')

# 1 watt is equal to 1 joule/sec
joule_per_second = Unit(
	name='joule per second',
	symbols=['J/s', 'j/s'],
	aliases='joules per second',
	factor='1')
