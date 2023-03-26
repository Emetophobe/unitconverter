# Copyright (c) 2022-2023 Mike Cunningham

from decimal import Decimal
from unitconverter.unit import Unit


# The watt is the SI unit of power
watt = Unit(
    name='watt',
    factor='1',
    symbols='W',
    aliases='watts',
    prefix_scaling='si')

# 1 joule/sec is equal to 1 watt
joule_per_second = Unit(
    name='joule per second',
    factor='1',
    symbols=['J/s', 'j/s'],
    aliases=['joules per second', 'joules/second', 'joule/second', 'joules/sec',
             'joule/sec', 'joules/s', 'joule/s'],
    prefix_scaling='si',
    prefix_index=0)

# 1 joule/min = roughly 0.0166666667 watts
joule_per_minute = Unit(
    name='joule per minute',
    factor=Decimal('1') / Decimal('60'),
    symbols=['J/min', 'j/min'],
    aliases=['joules per minute', 'joules/minute', 'joule/minute', 'joules/min',
             'joule/min'],
    prefix_scaling='si',
    prefix_index=0)

# 1 joule/hour = roughly 0.0002777778 watts
joule_per_hour = Unit(
    name='joule per hour',
    factor=Decimal('1') / Decimal('3600'),
    symbols=['J/hr', 'j/hr', 'J/h', 'j/h'],
    aliases=['joules per hour', 'joules/hour', 'joule/hour', 'joules/hr', 'joule/hr'],
    prefix_scaling='si',
    prefix_index=0)

# 1 metric horsepower (hp) = roughly 735.5 watts
horsepower = Unit(
    name='horsepower',
    factor='735.5',
    symbols='hp',
    aliases=['metric horsepower', 'metric hp'])

# 1 mechanical horsepower (bhp) = roughly 745.7 watts
mechanical_horsepower = Unit(
    name='mechanical horsepower',
    factor='745.7',
    symbols='bhp',
    aliases=['imperial horsepower', 'mechanical hp', 'imperial hp'])
