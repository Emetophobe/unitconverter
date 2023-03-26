# Copyright (c) 2022-2023 Mike Cunningham

from unitconverter.unit import Unit
from unitconverter.utils import combinations, PER_AMPERE


class ElectricPotential(Unit):
    category = 'electric potential'


# volt is the SI unit of electric potential
volt = ElectricPotential(
    name='volt',
    factor='1',
    symbols='V',
    aliases='volts',
    prefix_scaling='si')

# 1 watt/ampere is equivalent to 1 volt
watt_per_ampere = ElectricPotential(
    name='watt per ampere',
    factor='1',
    symbols='W/A',
    aliases=combinations(['watt', 'watts'], PER_AMPERE),
    prefix_scaling='si',
    prefix_index=0)

# 1 abvolt = 1E-8 volts
abvolt = ElectricPotential(
    name='abvolt',
    factor='1E-8',
    symbols='abV',
    aliases='abvolts')


# 1 statvolt = 299.7925 volts
statvolt = ElectricPotential(
    name='statvolt',
    factor='299.7925',
    symbols='stV',
    aliases='statvolts')
