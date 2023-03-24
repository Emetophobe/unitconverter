# Copyright (c) 2022-2023 Mike Cunningham

from decimal import Decimal
from unitconverter.unit import Unit


# The hertz is the SI unit of frequency
# 1 hertz is equal to 1 cycle/second
hertz = Unit(
    name='hertz',
    symbols='Hz',
    factor='1')


# 1 rpm is roughly 0.016666667 hertz (60 rpm is equal to 1 hertz)
rpm = Unit(
    name='revolution per minute',
    symbols=['rpm', 'RPM'],
    aliases='revolutions per minute',
    factor=Decimal('1') / Decimal('60'))
