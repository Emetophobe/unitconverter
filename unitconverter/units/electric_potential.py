# Copyright (c) 2022-2023 Mike Cunningham

from unitconverter.unit import Unit


class ElectricPotential(Unit):
    category = 'electric potential'


# volt is the SI unit of electric potential
volt = ElectricPotential(
    name='volt',
    factor='1',
    symbols='V',
    aliases='volts',
    prefix_scaling='si')
