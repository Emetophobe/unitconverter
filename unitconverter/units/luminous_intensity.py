# Copyright (c) 2022-2023 Mike Cunningham

from unitconverter.unit import Unit


class LuminousIntensity(Unit):
    category = 'luminous intensity'


# The candela is the SI unit of luminous intensity
candela = LuminousIntensity(
    name='candela',
    factor='1',
    symbols='cd',
    aliases='candelas',
    prefix_scaling='si')

# 1 candlepower is equal to 1 candela
candlepower = LuminousIntensity(
    name='candlepower',
    factor='1',
    symbols='cp',
    aliases='modern candlepower')

# 1 historic candlepower is equal to 0.981 candela
historic_candlepower = LuminousIntensity(
    name='historic candlepower',
    factor='0.981')
