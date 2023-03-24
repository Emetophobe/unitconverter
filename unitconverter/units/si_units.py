# Copyright (c) 2022-2023 Mike Cunningham

"""
	SI base units and derived units are aliased here for convenience.
"""

import sys
from unitconverter.units.amount_substance import mole
from unitconverter.units.angle import steradian, radian
from unitconverter.units.catalytic_activity import katal
from unitconverter.units.electrical import (coulomb, ampere, volt, farad,
											siemens, henry, ohm)
from unitconverter.units.energy import joule
from unitconverter.units.frequency import hertz
from unitconverter.units.force import newton
from unitconverter.units.illuminance import lux
from unitconverter.units.length import meter
from unitconverter.units.luminous_flux import lumen
from unitconverter.units.luminous_intensity import candela
from unitconverter.units.magnetic_flux import weber
from unitconverter.units.magnetic_flux_density import tesla
from unitconverter.units.mass import gram
from unitconverter.units.power import watt
from unitconverter.units.pressure import pascal
from unitconverter.units.radiation import becquerel, gray, sievert
from unitconverter.units.temperature import kelvin, celsius
from unitconverter.units.time import second

# Base units

sys.modules['si_units.second'] = second         # Time
sys.modules['si_units.meter'] = meter           # Length
sys.modules['si_units.gram'] = gram             # Mass (SI uses kg instead g)
sys.modules['si_units.ampere'] = ampere         # Eletric current
sys.modules['si_units.kelvin'] = kelvin         # Temperature
sys.modules['si_units.mole'] = mole             # Amount of substance
sys.modules['si_units.candela'] = candela       # Luminous intensity

# Derived units

sys.modules['si_units.celsius'] = celsius       # Celsius temperature
sys.modules['si_units.hertz'] = hertz           # Frequency
sys.modules['si_units.lux'] = lux               # Illuminance
sys.modules['si_units.lumen'] = lumen           # Luminous flux

sys.modules['si_units.joule'] = joule           # Energy, work, amount of heat
sys.modules['si_units.watt'] = watt             # Power
sys.modules['si_units.pascal'] = pascal         # Pressure
sys.modules['si_units.newton'] = newton         # Force
sys.modules['si_units.katal'] = katal           # Catalytic activity

sys.modules['si_units.coulomb'] = coulomb       # Electric charge
sys.modules['si_units.volt'] = volt             # Electric potential
sys.modules['si_units.farad'] = farad           # Electrical capacitance
sys.modules['si_units.siemens'] = siemens       # Electrical conductance
sys.modules['si_units.henry'] = henry           # Electrical inductance
sys.modules['si_units.ohm'] = ohm               # Electrical resistance

sys.modules['si_units.weber'] = weber           # Magnetic flux
sys.modules['si_units.tesla'] = tesla           # Magnetic flux density

sys.modules['si_units.becquerel'] = becquerel   # Radioactivity
sys.modules['si_units.gray'] = gray             # Absorbed dose
sys.modules['si_units.sievet'] = sievert        # Dose equivalent

sys.modules['si_units.steradian'] = steradian   # Solid angle
sys.modules['si_units.radian'] = radian         # Plane angle
