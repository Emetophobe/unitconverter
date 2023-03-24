# Copyright (c) 2022-2023 Mike Cunningham

from unitconverter.unit import Unit


# Weber is the SI unit of magnetic flux
weber = Unit(
    name='weber',
    symbols='Wb',
    aliases='webers',
    factor='1')

# 1 maxwell = 1E-8 webers
maxwell = Unit(
    name='maxwell',
    symbols='Mx',
    aliases='maxwells',
    factor='1E-8')
