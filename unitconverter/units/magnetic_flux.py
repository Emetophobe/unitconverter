# Copyright (c) 2022-2023 Mike Cunningham

from unitconverter.unit import Unit


class MagneticFlux(Unit):
    category = 'magnetic flux'


# Weber is the SI unit of magnetic flux
weber = MagneticFlux(
    name='weber',
    factor='1',
    symbols='Wb',
    aliases='webers',
    prefix_scaling='si')

# 1 maxwell = 1E-8 webers
maxwell = MagneticFlux(
    name='maxwell',
    factor='1E-8',
    symbols='Mx',
    aliases='maxwells',
    prefix_scaling='si')
