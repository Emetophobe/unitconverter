# Copyright (c) 2022-2023 Mike Cunningham

from unitconverter.unit import Unit
from unitconverter.utils import combinations, PER_AMPERE


class ElectricalInductance(Unit):
    category = 'electrical inductance'


# henry is the SI unit of electrical inductance
henry = ElectricalInductance(
    name='henry',
    factor='1',
    symbols='H',
    aliases='henries',
    prefix_scaling='si')

# 1 weber/ampere is equivalent to 1 henry
weber_per_ampere = ElectricalInductance(
    name='weber per ampere',
    factor='1',
    symbols='Wb/A',
    aliases=combinations(['weber', 'webers'], PER_AMPERE),
    prefix_scaling='si',
    prefix_index=0)

# 1 abhenry = 1E-9 henry
abhenry = ElectricalInductance(
    name='abhenry',
    factor='1E-9',
    symbols='abH',
    aliases='abhenries')

# 1 stathenry = 898755200000 henry
stathenry = ElectricalInductance(
    name='stathenry',
    factor='898755200000',
    symbols='stH',
    aliases='stathenries')
