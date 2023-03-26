# Copyright (c) 2022-2023 Mike Cunningham

from decimal import Decimal
from unitconverter.unit import Unit
from unitconverter.units.time import second, minute, hour
from unitconverter.units.length import (inch, foot, mile, nautical_mile,
                                        imperial_nautical_mile)
from unitconverter.utils import (combinations, METRE_NAMES, PER_SECOND,
                                 PER_MINUTE, PER_HOUR)


class Speed(Unit):
    category = 'speed'


# 1 metre/second (m/s) is the base unit
metre_per_second = Speed(
    name='metre per second',
    factor='1',
    symbols='m/s',
    aliases=combinations(METRE_NAMES, PER_SECOND),
    prefix_scaling='si',
    prefix_index=0)

# 1 metre/minute = 1/60 = 0.0166666667 m/s
metre_per_minute = Speed(
    name='metre per minute',
    factor=Decimal('1') / minute.factor,
    symbols='m/min',
    aliases=combinations(METRE_NAMES, PER_MINUTE),
    prefix_scaling='si',
    prefix_index=0)

# 1 metre/hour = 1/3600 = 0.0002777778 m/s
metre_per_hour = Speed(
    name='metre per hour',
    factor=Decimal('1') / hour.factor,
    symbols=['m/hr', 'm/h'],
    aliases=combinations(METRE_NAMES, PER_HOUR),
    prefix_scaling='si',
    prefix_index=0)

# Create kilometre/hour (kph) for convenience
# 1 kph = 1000/3600 = 0.2777777778 m/s
kilometre_per_hour = Speed(
    name='kilometre per hour',
    factor=Decimal('1000') / hour.factor,
    symbols=['kph', 'km/hr', 'km/h'],
    aliases=combinations(combinations(['kilo'], METRE_NAMES), PER_HOUR),
    prefix_scaling='none')  # Use meter_per_hour if you want to scale meters


# Create aliases for American spelling of metre
meter_per_second = metre_per_second
meter_per_minute = metre_per_minute
meter_per_hour = metre_per_hour
kilometer_per_hour = kilometre_per_hour


# 1 inch/second = 0.0254 m/s
inch_per_second = Speed(
    name='inch per second',
    factor=inch.factor / second.factor,
    symbols=['in/s', 'in/sec'],
    aliases=combinations(['inch', 'inches'], PER_SECOND))

# 1 inch/minute = 0.000423333 m/s
inch_per_minute = Speed(
    name='inch per minute',
    factor=inch.factor / minute.factor,
    symbols='in/min',
    aliases=combinations(['inch', 'inches'], PER_MINUTE))

# 1 inch/hour = 7.05556e-6 m/s
inch_per_hour = Speed(
    name='inch per hour',
    factor=inch.factor / hour.factor,
    symbols=['in/hr', 'in/h'],
    aliases=combinations(['inch', 'inches'], PER_HOUR))

# 1 foot/second = 0.3048 m/s
foot_per_second = Speed(
    name='foot per second',
    factor=foot.factor / second.factor,
    symbols=['ft/s', 'ft/sec'],
    aliases=combinations(['foot', 'feet'], PER_SECOND))

# 1 foot/minute = 0.00508 m/s
foot_per_minute = Speed(
    name='foot per minute',
    factor=foot.factor / minute.factor,
    symbols='ft/min',
    aliases=combinations(['foot', 'feet'], PER_MINUTE))

# 1 foot/hour = 0.0000846667 m/s
foot_per_hour = Speed(
    name='foot per hour',
    factor=foot.factor / hour.factor,
    symbols=['ft/hr', 'ft/h'],
    aliases=combinations(['foot', 'feet'], PER_HOUR))

# 1 mile/second = 1609.34 m/s
mile_per_second = Speed(
    name='mile per second',
    factor=mile.factor / second.factor,
    symbols=['mi/sec', 'mi/s'],
    aliases=combinations(['mile', 'miles'], PER_SECOND))

# 1 mile/minute = 26.8224 m/s
mile_per_minute = Speed(
    name='mile per minute',
    factor=mile.factor / minute.factor,
    symbols=['mi/min'],
    aliases=combinations(['mile', 'miles'], PER_MINUTE))

# 1 mile/hour (mph) = 0.44704 m/s
mile_per_hour = Speed(
    name='mile per hour',
    factor=mile.factor / hour.factor,
    symbols=['mph', 'mi/hr', 'mi/h'],
    aliases=combinations(['mile', 'miles'], PER_HOUR))


# The knot is equal to one nautical mile per hour (~0.514 m/s)
knot = Speed(
    name='knot',
    factor=nautical_mile.factor / hour.factor,
    aliases='knots')

# 1 imperial knot = 0.5147733333 m/s
imperial_knot = Speed(
    name='imperial knot',
    factor=imperial_nautical_mile.factor / hour.factor,
    aliases='imperial knots')

# Mach 1 (speed of sound)
mach = Speed(
    name='mach',
    factor='295.0464',
    symbols='Ma')
