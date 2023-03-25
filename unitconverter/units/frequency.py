# Copyright (c) 2022-2023 Mike Cunningham

from decimal import Decimal
from unitconverter.unit import Unit


# The hertz is the SI unit of frequency
# 1 hertz is equal to 1 cycle/second
hertz = Unit(
    name='hertz',
    factor='1',
    symbols='Hz',
    prefix_scaling='si')


# 1 rpm is roughly 0.016666667 hertz (60 rpm is equal to 1 hertz)
rpm = Unit(
    name='revolution per minute',
    factor=Decimal('1') / Decimal('60'),
    symbols=['rpm', 'RPM'],
    aliases='revolutions per minute')
