# Copyright (c) 2022-2023 Mike Cunningham

from unitconverter.unit import Unit


# The candela is the SI unit of luminous intensity
candela = Unit(
    name='candela',
    symbols='cd',
    aliases='candelas',
    factor='1')

# 1 candlepower is equal to 1 candela
candlepower = Unit(
    name='candlepower',
    symbols='cp',
    aliases='modern candlepower',
    factor='1')

# 1 historic candlepower is equal to 0.981 candela
historic_candlepower = Unit(
    name='historic candlepower',
    symbols='cp-historic',
    factor='0.981')
