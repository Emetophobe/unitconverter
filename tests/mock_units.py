# Copyright (c) 2022-2025 Mike Cunningham
# https://www.github.com/emetophobe/unitconverter


from unitconverter.models.dimension import Dimension
from unitconverter.models.unit import Unit


# Mock units used for testing
second = Unit("second", ["s"], ["seconds"], Dimension("time"), prefixes="metric")
metre = Unit("metre", ["m"], ["metres"], Dimension("length"), prefixes="metric")
