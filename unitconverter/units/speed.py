# Copyright (c) 2022-2023 Mike Cunningham

from unitconverter.unit import Unit
from unitconverter.utils import (combinations, METRE_NAMES, PER_SECOND,
                                 PER_MINUTE, PER_HOUR)


# 1 metre/second (m/s) is the base unit
metre_per_second = Unit(
    name='metre per second',
    factor='1',
    symbols='m/s',
    aliases=combinations(METRE_NAMES, PER_SECOND),
    prefix_scaling='si',
    prefix_index=0)

# 1 metre/minute = 1/60 = 0.0166666667 m/s
metre_per_minute = Unit(
    name='metre per minute',
    factor='0.0166666667',
    symbols='m/min',
    aliases=combinations(METRE_NAMES, PER_MINUTE),
    prefix_scaling='si',
    prefix_index=0)

# 1 metre/hour = 1/3600 = 0.0002777778 m/s
metre_per_hour = Unit(
    name='metre per hour',
    factor='0.0002777778',
    symbols=['m/hr', 'm/h'],
    aliases=combinations(METRE_NAMES, PER_HOUR),
    prefix_scaling='si',
    prefix_index=0)

# Create kilometre/hour (kph) for convenience
# 1 kph = 1000/3600 = 0.2777777778 m/s
kilometre_per_hour = Unit(
    name='kilometre per hour',
    factor='0.2777777778',
    symbols=['kph', 'km/hr', 'km/h'],
    aliases=combinations(combinations(['kilo'], METRE_NAMES), PER_HOUR),
    prefix_scaling='none')  # Use meter_per_hour if you want to scale meters


# Create aliases for American spelling of metre
meter_per_second = metre_per_second
meter_per_minute = metre_per_minute
meter_per_hour = metre_per_hour
kilometer_per_hour = kilometre_per_hour


# 1 inch/second = 0.0254 m/s
inch_per_second = Unit(
    name='inch per second',
    factor='0.0254',
    symbols=['in/s', 'in/sec'],
    aliases=combinations(['inch', 'inches'], PER_SECOND))

# 1 inch/minute = 0.000423333 m/s
inch_per_minute = Unit(
    name='inch per minute',
    factor='0.000423333',
    symbols='in/min',
    aliases=combinations(['inch', 'inches'], PER_MINUTE))

# 1 inch/hour = 7.05556e-6 m/s
inch_per_hour = Unit(
    name='inch per hour',
    factor='7.05556e-6',
    symbols=['in/hr', 'in/h'],
    aliases=combinations(['inch', 'inches'], PER_HOUR))

# 1 foot/second = 0.3048 m/s
foot_per_second = Unit(
    name='foot per second',
    factor='0.3048',
    symbols=['ft/s', 'ft/sec'],
    aliases=combinations(['foot', 'feet'], PER_SECOND))

# 1 foot/minute = 0.00508 m/s
foot_per_minute = Unit(
    name='foot per minute',
    factor='0.00508',
    symbols='ft/min',
    aliases=combinations(['foot', 'feet'], PER_MINUTE))

# 1 foot/hour = 0.0000846667 m/s
foot_per_hour = Unit(
    name='foot per hour',
    factor='0.0000846667',
    symbols=['ft/hr', 'ft/h'],
    aliases=combinations(['foot', 'feet'], PER_HOUR))

# 1 mile/second = 1609.34 m/s
mile_per_second = Unit(
    name='mile per second',
    factor='1609.34',
    symbols=['mi/sec', 'mi/s'],
    aliases=combinations(['mile', 'miles'], PER_SECOND))

# 1 mile/minute = 26.8224 m/s
mile_per_minute = Unit(
    name='mile per minute',
    factor='26.8224',
    symbols=['mi/min'],
    aliases=combinations(['mile', 'miles'], PER_MINUTE))

# 1 mile/hour (mph) = 0.44704 m/s
mile_per_hour = Unit(
    name='mile per hour',
    factor='0.44704',
    symbols=['mph', 'mi/hr', 'mi/h'],
    aliases=combinations(['mile', 'miles'], PER_HOUR))


# The knot is equal to one nautical mile per hour (~0.514 m/s)
knot = Unit(
    name='knot',
    factor='0.5144444444',
    aliases='knots')

# 1 imperial knot = 0.5147733333 m/s
imperial_knot = Unit(
    name='imperial knot',
    factor='0.5147733333',
    aliases='imperial knots')

# Mach 1 (speed of sound)
mach = Unit(
    name='mach',
    factor='295.0464',
    symbols='Ma')
