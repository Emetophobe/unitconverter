# Copyright (c) 2022-2023 Mike Cunningham

from unitconverter.unit import Unit


# SI unit of energy is the Joule
joule = Unit(
	name='joule',
	symbols='J',
	aliases='joules',
	factor='1')

calorie = Unit(
	name='calorie',
	symbols='cal',
	aliases='calories',
	factor='4.184')

btu = Unit(
	name='british thermal unit',
	symbols=['btu', 'btus'],
	aliases='british thermal units',
	factor='1055.06')

# A quad is a quadrillion btus
quad = Unit(
	name='quad',
	symbols='',
	aliases='',
	factor='1E+15')

watt_second = Unit(
	name='watt-second',
	symbols='Ws',
	aliases=['watt-seconds', 'wattseconds', 'wattsecond'],
	factor='1')

watt_minute = Unit(
	name='watt-minute',
	symbols='Wm',
	aliases=['watt-minutes', 'wattminutes', 'wattminute'],
	factor='3600')

watt_hour = Unit(
	name='watt-hour',
	symbols='Wh',
	aliases=['watt-hours', 'watthours', 'watthour'],
	factor='3.6E+3')

therm = Unit(
	name='therm',
	symbols='thm',
	aliases='therms',
	factor='105506000.00')

erg = Unit(
	name='erg',
	symbols='',
	aliases='ergs',
	factor='1E-7')

gram_of_TNT = Unit(
	name='gram of TNT',
	symbols='gTNT',
	aliases='grams of TNT',
	factor='4184')

ton_of_TNT = Unit(
	name='ton of TNT',
	symbols='tTNT',
	aliases='tons of TNT',
	factor='4.184E+9')
