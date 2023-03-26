# Copyright (c) 2022-2023 Mike Cunningham

from unitconverter.unit import Unit


class ElectricalCapacitance(Unit):
    category = 'electrical capacitance'


# farad is the SI unit of electrical capacitance
farad = ElectricalCapacitance(
    name='farad',
    factor='1',
    symbols='F',
    aliases='farads',
    prefix_scaling='si')
