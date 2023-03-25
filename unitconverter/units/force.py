# Copyright (c) 2022-2023 Mike Cunningham

from unitconverter.unit import Unit


# The newton is the SI unit of force.
newton = Unit(
    name='newton',
    symbols='N',
    aliases='newtons',
    factor='1')

# The dyne is a derived unit of force specified in the older CGS system of units.
# 1 dyne is exactly 0.00001 (1E-5) newtons
dyne = Unit(
    name='dyne',
    symbols='dyn',
    aliases='dynes',
    factor='1E-5')

# 1 poundal = exactly 0.138254954376 newtons
poundal = Unit(
    name='poundal',
    symbols='pdl',
    aliases='poundals',
    factor='0.138254954376')

# 1 gram force = 0.00980665 newtons
gram_force = Unit(
    name='gram-force',
    symbols=['gf', 'p'],
    aliases=['ponds', 'pond'],
    factor='0.00980665')

# 1 ounce force = roughly 0.27801385 newtons
ounce_force = Unit(
    name='ounce-force',
    symbols='ozf',
    factor='0.27801385')

# 1 pound force is roughly 4.448222 newtons
pound_force = Unit(
    name='pound-force',
    symbols='lbf',
    aliases=['pounds of force', 'pound of force', 'lbs of force', 'lbs-force'],
    factor='4.448222')

# 1 kip-force = 1000 pound force or roughly 4448.222 newtons
kip_force = Unit(
    name='kip-force',
    symbols='kipf',
    factor='4448.222')

# 1 tonne force = 9806.65 newtons
tonne_force = Unit(
    name='tonne-force',
    symbols=['t-f', 'tf', 'MgF', 'mp'],
    aliases=['metric ton-force', 'megagram-force', 'megapond'],
    factor='9806.65')

# 1 long ton-force = roughly 9964.0164182 newtons
long_ton_force = Unit(
    name='long ton-force',
    symbols='tnf',
    aliases='tf (long)',
    factor='9964.0164182')

# 1 short ton-force = roughly 8896.4432305 newtons
short_ton_force = Unit(
    name='short ton-force',
    symbols='tonf',
    aliases=['tf (short)'],
    factor='8896.4432305')

# 1 joule/metre is equal to 1 newton
joule_per_metre = Unit(
    name='joule/metre',
    symbols=['J/m', 'j/m'],
    aliases=['joules/metre', 'joules/meter', 'joule/meter'],
    factor='1')
