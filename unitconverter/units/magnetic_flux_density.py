# Copyright (c) 2022-2023 Mike Cunningham

from unitconverter.unit import Unit


class MagneticFluxDensity(Unit):
    category = 'magnetic flux density'


# Tesla is the SI unit of magnetic flux density
tesla = MagneticFluxDensity(
    name='tesla',
    factor='1',
    symbols='T',
    aliases='teslas',
    prefix_scaling='si')

# 1 gamma = 1E-9 teslas
gamma = MagneticFluxDensity(
    name='gamma',
    symbols='y',
    aliases='gammas',
    factor='1E-9')

# 1 guass = 1E-4 teslas
guass = MagneticFluxDensity(
    name='guass',
    symbols='G',
    aliases='gausses',
    factor='1E-4')
