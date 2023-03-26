# Copyright (c) 2022-2023 Mike Cunningham

from unitconverter.unit import Unit


class ElectricalResistance(Unit):
    category = 'electrical resistance'


# ohm is the SI unit of electrical resistance
ohm = ElectricalResistance(
    name='ohm',
    factor='1',
    symbols='Ω',
    aliases='ohms',
    prefix_scaling='si')

# 1 ohm = 1/S
reciprocal_siemens = ElectricalResistance(
    name='reciprocal siemens',
    factor='1',
    symbols='1/S',
    prefix_scaling='si')
