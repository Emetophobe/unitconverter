# Copyright (c) 2022-2023 Mike Cunningham

from unitconverter.unit import Unit
from unitconverter.utils import combinations, AMPERE_NAMES


class ElectricalConductance(Unit):
    category = 'electrical conductance'


# siemens is the SI unit of electrical conductance
siemens = ElectricalConductance(
    name='siemens',
    factor='1',
    symbols='S',
    prefix_scaling='si')

# 1 amp/volt is equivalent to 1 siemens
ampere_per_volt = ElectricalConductance(
    name='ampere per volt',
    factor='1',
    symbols='A/V',
    aliases=combinations(AMPERE_NAMES, [' per volt', '/volt', '/V']),
    prefix_scaling='si',
    prefix_index=0)
