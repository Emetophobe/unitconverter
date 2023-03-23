# Copyright (c) 2022-2023 Mike Cunningham

from unitconverter.unit import Unit


# SI unit of energy is the joule
joule = Unit(
	name='joule',
	symbols='J',
	aliases='joules',
	factor='1')

# 1 calorie = 4.184 joules
calorie = Unit(
	name='calorie',
	symbols='cal',
	aliases='calories',
	factor='4.184')

# 1 btu = 1055.06 joules
btu = Unit(
	name='british thermal unit',
	symbols=['btu', 'btus'],
	aliases='british thermal units',
	factor='1055.06')

# A quad is a quadrillion btus or 1.05506E+18 joules
quad = Unit(
	name='quad',
	symbols='',
	aliases=['quadrillion btus', 'quadrillion btu'],
	prefix_scaling='none',  # disable unit scaling
	factor='1.05506E+18')

# 1 watt second = 1 joule
watt_second = Unit(
	name='watt-second',
	symbols='Ws',
	aliases=['watt-seconds', 'wattseconds', 'wattsecond'],
	factor='1')

# 1 watt minute = 60 joules
watt_minute = Unit(
	name='watt-minute',
	symbols='Wm',
	aliases=['watt-minutes', 'wattminutes', 'wattminute'],
	factor='60')

# 1 watt hour = 3600 joules
watt_hour = Unit(
	name='watt-hour',
	symbols='Wh',
	aliases=['watt-hours', 'watthours', 'watthour'],
	factor='3600')

# 1 electron volt = 1.602176633E-19 joules
electron_volt = Unit(
	name='electron volt',
	symbols='eV',
	aliases='electron volts',
	factor='1.602176633E-19')

# 1 erg = 1E-7 joules
erg = Unit(
	name='erg',
	symbols='',
	aliases='ergs',
	factor='1E-7')

# 1 therm = 105,506,000 joules
therm = Unit(
	name='therm',
	symbols='thm',
	aliases='therms',
	factor='105506000')

# 1 inch pound = 0.112984829 joules
inch_pound = Unit(
	name='inch-pound',
	symbols=['in*lbf', 'in-lbf'],
	factor='0.112984829')

# 1 foot pound = 1.3558179483 joules
foot_pound = Unit(
	name='foot-pound',
	symbols=['ft*lbf', 'ft-lbf'],
	factor='1.3558179483')

# 1 gram of TNT is approximately 4184 joules
gram_of_TNT = Unit(
	name='gram of TNT',
	symbols='gTNT',
	aliases='grams of TNT',
	prefix_index=0,  # prefix first word
	factor='4184')

# 1 metric ton of TNT is approximately 4.184E+9 joules
ton_of_TNT = Unit(
	name='ton of TNT',
	symbols='tTNT',
	aliases='tons of TNT',
	prefix_index=0,  # prefix first word
	factor='4.184E+9')
