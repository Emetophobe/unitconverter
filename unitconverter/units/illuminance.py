# Copyright (c) 2022-2023 Mike Cunningham

from unitconverter.unit import Unit


# SI unit of illuminance
lux = Unit(
    name='lux',
    factor='1',
    symbols='lx',
    prefix_scaling='si')

# 1 metre candle is equal to 1 lux
metre_candle = Unit(
    name='metre-candle',
    factor='1',
    symbols=['m*c', 'm⋅s'],
    aliases=['meter-candle', 'metre candle', 'meter candle'],
    prefix_scaling='si',
    prefix_index=0)

# 1 phot is exactly 10000 lux
phot = Unit(
    name='phot',
    factor='10000',
    symbols='ph',
    aliases='phots')

# 1 nox is exactly 0.001 lux
nox = Unit(
    name='nox',
    factor='0.001',
    symbols='nx')

# 1 watt/m^2 is exactly 683 lux
watt_per_square_metre = Unit(
    name='watt per square metre',
    factor='683',
    symbols=['W/m^2', 'W/m2'],
    aliases=['watts per square metre', 'watts/m^2', 'watts/m2', 'watt/m^2', 'watt/m2'],
    prefix_scaling='si',
    prefix_index=0)

# 1 foot candle is roughly 10.76391 lux
foot_candle = Unit(
    name='foot-candle',
    factor='10.76391',
    symbols=['ft*c', 'ft⋅c', 'f⋅c'],
    aliases='foot candle')
