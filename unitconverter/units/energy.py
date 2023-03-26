# Copyright (c) 2022-2023 Mike Cunningham

from unitconverter.unit import Unit


class Energy(Unit):
    category = 'energy'


# SI unit of energy is the joule
joule = Energy(
    name='joule',
    factor='1',
    symbols='J',
    aliases='joules',
    prefix_scaling='si')

# 1 watt second = 1 joule
watt_second = Energy(
    name='watt-second',
    factor='1',
    symbols='Ws',
    aliases=['watt-seconds', 'wattseconds', 'wattsecond'],
    prefix_scaling='si')

# 1 watt minute = 60 joules
watt_minute = Energy(
    name='watt-minute',
    factor='60',
    symbols='Wm',
    aliases=['watt-minutes', 'wattminutes', 'wattminute'],
    prefix_scaling='si')

# 1 watt hour = 3600 joules
watt_hour = Energy(
    name='watt-hour',
    factor='3600',
    symbols='Wh',
    aliases=['watt-hours', 'watthours', 'watthour'],
    prefix_scaling='si')

# 1 gram of TNT is approximately 4184 joules
gram_of_TNT = Energy(
    name='gram of TNT',
    factor='4184',
    symbols='gTNT',
    aliases='grams of TNT',
    prefix_scaling='si',
    prefix_index=0)

# 1 metric ton of TNT is approximately 4.184E+9 joules
ton_of_TNT = Energy(
    name='ton of TNT',
    factor='4.184E+9',
    symbols='tTNT',
    aliases='tons of TNT',
    prefix_scaling='si',
    prefix_index=0)


# Non-metric units


# 1 calorie = 4.184 joules
calorie = Energy(
    name='calorie',
    factor='4.184',
    symbols='cal',
    aliases='calories')

# 1 btu = 1055.06 joules
btu = Energy(
    name='british thermal unit',
    factor='1055.06',
    symbols=['btu', 'btus'],
    aliases='british thermal units')

# A quad is a quadrillion btus or 1.05506E+18 joules
quad = Energy(
    name='quad',
    factor='1.05506E+18',
    aliases=['quadrillion btus', 'quadrillion btu'])


# 1 electron volt = 1.602176633E-19 joules
electron_volt = Energy(
    name='electron volt',
    factor='1.602176633E-19',
    symbols='eV',
    aliases='electron volts')

# 1 erg = 1E-7 joules
erg = Energy(
    name='erg',
    factor='1E-7',
    aliases='ergs')

# 1 therm = 105,506,000 joules
therm = Energy(
    name='therm',
    factor='105506000',
    symbols='thm',
    aliases='therms')

# 1 inch pound = 0.112984829 joules
inch_pound = Energy(
    name='inch-pound',
    factor='0.112984829',
    symbols=['in*lbf', 'in-lbf'])

# 1 foot pound = 1.3558179483 joules
foot_pound = Energy(
    name='foot-pound',
    factor='1.3558179483',
    symbols=['ft*lbf', 'ft-lbf'])
