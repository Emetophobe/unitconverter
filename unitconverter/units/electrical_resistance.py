# Copyright (c) 2022-2023 Mike Cunningham

from unitconverter.unit import Unit
from unitconverter.utils import combinations, PER_AMPERE


class ElectricalResistance(Unit):
    category = 'electrical resistance'


# ohm is the SI unit of electrical resistance
ohm = ElectricalResistance(
    name='ohm',
    factor='1',
    symbols='Ω',
    aliases='ohms',
    prefix_scaling='si')

# 1/S is equivalent to 1 ohm
reciprocal_siemens = ElectricalResistance(
    name='reciprocal siemens',
    factor='1',
    symbols='1/S',
    prefix_scaling='si')

# 1 volt/ampere is equivalent to 1 ohm
volt_per_ampere = ElectricalResistance(
    name='volt per ampere',
    factor='1',
    symbols='V/A',
    aliases=combinations(['volt', 'volts'], PER_AMPERE),
    prefix_scaling='si',
    prefix_index=0)

# 1 abohm = 1E-9 ohm
abohm = ElectricalResistance(
    name='abohm',
    factor='1E-9',
    symbols='abΩ',
    aliases='abohms')

# 1 statohm = 8.987552E+11 ohm
statohm = ElectricalResistance(
    name='statohm',
    factor='8.987552E+11',
    symbols='stΩ',
    aliases='statohms')
