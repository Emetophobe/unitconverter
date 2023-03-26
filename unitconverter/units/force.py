# Copyright (c) 2022-2023 Mike Cunningham

from unitconverter.unit import Unit
from unitconverter.utils import combinations, PER_METRE


# The newton is the SI unit of force.
newton = Unit(
    name='newton',
    symbols='N',
    aliases='newtons',
    factor='1',
    prefix_scaling='si')

# 1 joule/metre is equal to 1 newton
joule_per_metre = Unit(
    name='joule per metre',
    factor='1',
    symbols=['J/m', 'j/m'],
    aliases=combinations(['joule', 'joules'], PER_METRE),
    prefix_scaling='si')

# The dyne is a derived unit of force specified in the older CGS system of units.
# 1 dyne is exactly 0.00001 (1E-5) newtons
dyne = Unit(
    name='dyne',
    factor='1E-5',
    symbols='dyn',
    aliases='dynes',
    prefix_scaling='si')

# 1 gram force = 0.00980665 newtons
gram_force = Unit(
    name='gram-force',
    factor='0.00980665',
    symbols=['gf', 'p'],
    aliases=['ponds', 'pond'],
    prefix_scaling='si')

# 1 tonne force = 9806.65 newtons
tonne_force = Unit(
    name='tonne-force',
    factor='9806.65',
    symbols=['t-f', 'tf', 'MgF', 'mp'],
    aliases=['metric ton-force', 'megagram-force', 'megapond'],
    prefix_scaling='si')


# Imperial units


# 1 poundal = exactly 0.138254954376 newtons
poundal = Unit(
    name='poundal',
    factor='0.138254954376',
    symbols='pdl',
    aliases='poundals')

# 1 ounce force = roughly 0.27801385 newtons
ounce_force = Unit(
    name='ounce-force',
    factor='0.27801385',
    symbols='ozf')

# 1 pound force is roughly 4.448222 newtons
pound_force = Unit(
    name='pound-force',
    factor='4.448222',
    symbols='lbf',
    aliases=['pounds of force', 'pound of force', 'lbs of force', 'lbs-force'])

# 1 kip-force = 1000 pound force or roughly 4448.222 newtons
kip_force = Unit(
    name='kip-force',
    factor='4448.222',
    symbols='kipf')

# 1 long ton-force = roughly 9964.0164182 newtons
long_ton_force = Unit(
    name='long ton-force',
    factor='9964.0164182',
    symbols='tnf',
    aliases='tf (long)')

# 1 short ton-force = roughly 8896.4432305 newtons
short_ton_force = Unit(
    name='short ton-force',
    factor='8896.4432305',
    symbols='tonf',
    aliases=['tf (short)'])
