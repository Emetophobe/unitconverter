# Copyright (c) 2022-2023 Mike Cunningham

from unitconverter.unit import Unit


class SignalIntensity(Unit):
    category = 'signal intensity'


# decibel is the base unit
decibel = SignalIntensity(
    name='decibel',
    factor='1',
    symbols='dB',
    aliases='decibels')

# 1 bel = 10 decibels
bel = SignalIntensity(
    name='bel',
    factor='10',
    aliases='bels')

# 1 neper = 8.686 decibels
neper = SignalIntensity(
    name='neper',
    factor='8.686',
    symbols='Np',
    aliases='nepers')
