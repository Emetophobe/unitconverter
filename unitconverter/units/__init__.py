# Copyright (c) 2022-2023 Mike Cunningham

from unitconverter.unit import Unit
from unitconverter.units import amount_substance
from unitconverter.units import area
from unitconverter.units import catalytic_activity
from unitconverter.units import data_storage
from unitconverter.units import electric_charge
from unitconverter.units import electric_current
from unitconverter.units import electric_potential
from unitconverter.units import electrical_capacitance
from unitconverter.units import electrical_conductance
from unitconverter.units import electrical_inductance
from unitconverter.units import electrical_resistance
from unitconverter.units import energy
from unitconverter.units import force
from unitconverter.units import frequency
from unitconverter.units import fuel_consumption
from unitconverter.units import illuminance
from unitconverter.units import length
from unitconverter.units import luminous_flux
from unitconverter.units import luminous_intensity
from unitconverter.units import magnetic_flux
from unitconverter.units import magnetic_flux_density
from unitconverter.units import mass
from unitconverter.units import plane_angle
from unitconverter.units import power
from unitconverter.units import pressure
from unitconverter.units import radiation
from unitconverter.units import si_units
from unitconverter.units import signal_intensity
from unitconverter.units import solid_angle
from unitconverter.units import speed
from unitconverter.units import temperature
from unitconverter.units import time
from unitconverter.units import viscosity
from unitconverter.units import volume


def get_modules() -> dict:
    """ Get a dictionary of module categories. """
    return {
        'amount of substance': amount_substance,
        'area': area,
        'catalytic activity': catalytic_activity,
        'data storage': data_storage,
        'electric charge': electric_charge,
        'electric current': electric_current,
        'electric potential': electric_potential,
        'electrical capacitance': electrical_capacitance,
        'electrical conductance': electrical_conductance,
        'electrical inductance': electrical_inductance,
        'electrical resistance': electrical_resistance,
        'energy': energy,
        'force': force,
        'frequency': frequency,
        'fuel consumption': fuel_consumption,
        'illuminance': illuminance,
        'length': length,
        'luminous flux': luminous_flux,
        'luminous intensity': luminous_intensity,
        'magnetic flux': magnetic_flux,
        'magnetic flux density': magnetic_flux_density,
        'mass': mass,
        'plane angle': plane_angle,
        'power': power,
        'pressure': pressure,
        'radiation': radiation,
        'SI units': si_units,
        'signal intensity': signal_intensity,
        'solid angle': solid_angle,
        'speed': speed,
        'temperature': temperature,
        'time': time,
        'viscosity': viscosity,
        'volume': volume,
    }


def find_dupes(units: list[Unit]) -> list[Unit]:
    """ Find duplicate names, symbols, and aliases. """
    aliases = {}
    for unit in units:
        for name in [unit.name] + unit.symbols + unit.aliases:
            if name in aliases.keys():
                raise ValueError(f'Found a duplicate alias: {name}'
                                 f' (Original unit: {aliases[name]})')
            aliases[name] = unit

    return units


def get_units() -> list[Unit]:
    """ Load all predefined units. """
    units = set()
    for category, module in get_modules().items():
        # ignore aliased units
        if category == 'SI units':
            continue

        # Search each module for units
        for item in dir(module):
            if not item.startswith('_'):
                unit = getattr(module, item)
                if isinstance(unit, Unit):
                    if not unit.category:
                        raise ValueError(f'{unit.name} is missing a category.')

                    units.add(unit)

    # Find dupes and return unit list
    return list(find_dupes(units))


def get_categories() -> list[str]:
    """ Get a list of category names. """
    return get_modules().keys()


__all__ = [
    'get_categories',
    'get_units'
]
