# Copyright (c) 2022-2023 Mike Cunningham

from unitconverter.unit import Unit


class ElectricalInductance(Unit):
    category = 'electrical inductance'


# henry is the SI unit of electrical inductance
henry = ElectricalInductance(
    name='henry',
    factor='1',
    symbols='H',
    aliases='henries',
    prefix_scaling='si')
