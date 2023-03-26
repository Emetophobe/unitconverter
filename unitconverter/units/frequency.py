# Copyright (c) 2022-2023 Mike Cunningham

from decimal import Decimal
from unitconverter.unit import Unit
from unitconverter.utils import combinations, PER_SECOND, PER_MINUTE


# The hertz is the SI unit of frequency
# 1 hertz is equal to 1 cycle/second
hertz = Unit(
    name='hertz',
    factor='1',
    symbols='Hz',
    prefix_scaling='si')

# 1 cycle per second is equivalent to 1 hertz
cycle_per_second = Unit(
    name='cycle per second',
    factor='1',
    symbols=['cps', 'CPS'],
    aliases=combinations(['cycle', 'cycles'], PER_SECOND))

# 1 cycle per minute is 1/60 hertz or roughly 0.016666667 hertz
cycle_per_minute = Unit(
    name='cycle per minute',
    factor=Decimal('1') / Decimal('60'),
    symbols=['cpm', 'CPM'],
    aliases=combinations(['cycle', 'cycles'], PER_MINUTE))

# Add rpm for convenience. 1 rpm is the same as 1 cycle/minute
rpm = Unit(
    name='revolution per minute',
    factor=Decimal('1') / Decimal('60'),
    symbols=['rpm', 'RPM'],
    aliases=combinations(['revolution', 'revolutions'], PER_MINUTE))
