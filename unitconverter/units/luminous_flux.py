# Copyright (c) 2022-2023 Mike Cunningham

from unitconverter.unit import Unit


class LuminousFlux(Unit):
    category = 'luminous flux'


# The lumen is the SI unit of luminous flux
lumen = LuminousFlux(
    name='lumen',
    factor='1',
    symbols='lm',
    aliases='lumens',
    prefix_scaling='si')

# 1 candela steradian is equal to 1 lumen
candela_steradian = LuminousFlux(
    name='candela-steradian',
    factor='1',
    symbols=['cd·sr', 'cd*sr', 'cd-sr'],
    aliases='candela steradian',
    prefix_index=0,
    prefix_scaling='si')
