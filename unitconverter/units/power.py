# Copyright (c) 2022-2023 Mike Cunningham

from decimal import Decimal
from unitconverter.unit import Unit
from unitconverter.utils import combinations, PER_SECOND, PER_MINUTE, PER_HOUR


class Power(Unit):
    category = 'power'


# The watt is the SI unit of power
watt = Power(
    name='watt',
    factor='1',
    symbols='W',
    aliases='watts',
    prefix_scaling='si')

# 1 joule/sec is equal to 1 watt
joule_per_second = Power(
    name='joule per second',
    factor='1',
    symbols=['J/s', 'j/s'],
    aliases=combinations(['joule', 'joules'], PER_SECOND),
    prefix_scaling='si',
    prefix_index=0)

# 1 joule/min = roughly 0.0166666667 watts
joule_per_minute = Power(
    name='joule per minute',
    factor=Decimal('1') / Decimal('60'),
    symbols=['J/min', 'j/min'],
    aliases=combinations(['joule', 'joules'], PER_MINUTE),
    prefix_scaling='si',
    prefix_index=0)

# 1 joule/hour = roughly 0.0002777778 watts
joule_per_hour = Power(
    name='joule per hour',
    factor=Decimal('1') / Decimal('3600'),
    symbols=['J/hr', 'j/hr', 'J/h', 'j/h'],
    aliases=combinations(['joule', 'joules'], PER_HOUR),
    prefix_scaling='si',
    prefix_index=0)

# 1 metric horsepower (hp) = roughly 735.5 watts
horsepower = Power(
    name='horsepower',
    factor='735.5',
    symbols='hp',
    aliases=['metric horsepower', 'metric hp'])

# 1 mechanical horsepower (bhp) = roughly 745.7 watts
mechanical_horsepower = Power(
    name='mechanical horsepower',
    factor='745.7',
    symbols='bhp',
    aliases=['imperial horsepower', 'mechanical hp', 'imperial hp'])
