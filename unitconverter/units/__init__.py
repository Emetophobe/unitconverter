# Copyright (c) 2022-2023 Mike Cunningham

from unitconverter.unit import Unit
from unitconverter.units import amount_substance
from unitconverter.units import angle
from unitconverter.units import area
from unitconverter.units import catalytic_activity
from unitconverter.units import data_storage
from unitconverter.units import electrical
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
from unitconverter.units import power
from unitconverter.units import pressure
from unitconverter.units import radiation
from unitconverter.units import si_units
from unitconverter.units import signal_intensity
from unitconverter.units import speed
from unitconverter.units import temperature
from unitconverter.units import time
from unitconverter.units import viscosity
from unitconverter.units import volume


def get_modules() -> dict:
    """ Get a dictionary of module categories. """
    return {
        'amount of substance': amount_substance,
        'angle': angle,
        'area': area,
        'catalytic activity': catalytic_activity,
        'data storage': data_storage,
        'electrical': electrical,
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
        'power': power,
        'pressure': pressure,
        'radiation': radiation,
        'SI units': si_units,
        'signal intensity': signal_intensity,
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


def load_units() -> list[Unit]:
    """ Load all predefined units. """
    modules = get_modules()
    units = set()
    for category, module in modules.items():
        # ignore aliased units
        if category == 'SI units':
            continue

        # Search each module for units
        for item in dir(module):
            if not item.startswith('_'):
                unit = getattr(module, item)
                if isinstance(unit, Unit):
                    # Set default category
                    if not unit.category:
                        unit.category = category
                    units.add(unit)

    return list(units)


def get_units() -> list[Unit]:
    """ Load units and find duplicates. """
    return find_dupes(load_units())


__all__ = [
    'get_units'
]
