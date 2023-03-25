# Unit Converter (work in progress)

A basic unit converter written in Python.


The following categories are currently supported:


* Amount of substance (moles, atoms)
* Angle (steradian, radian, square degrees)
* Area (square metres, square miles, acres, hectares, etc..)
* Catalytic activity (katal, mol/sec)
* Data storage (bits, bytes, kilobytes, kibibytes, etc..)
* Electrical (ampere, volt, ohm, coulomb, farad, henry, siemens)
* Energy (joule, calorie, btu, therm, watt seconds, watt hours, etc..)
* Force (newtons, dynes, poundals, gram force, ton force, etc..)
* Fuel consumption (mpg, litres/100km, etc..)
* Frequency (hertz, rpm)
* Illuminance (lux, nox, phot, watt/m^2, metre candle, foot candle)
* Length (metres, feet, inches...)
* Luminous flux (lumens, candela-steradian)
* Luminous intensity (candela, candlepower)
* Magnetic flux (weber, maxwell)
* Magnetic flux density (tesla, guass, gamma)
* Mass (grams, pounds, ounces, tons...)
* Power (watts, horsepower, joules/second)
* Pressure (pascal, bar, psi)
* Radiation (becqueral, curie, rutherford, gray, sievert)
* Signal intensity (decibel, bel, neper)
* Speed (km/hour, miles/hour, metres/second, inches/second...)
* Temperature (kelvin, celsius, fahrenheit, and rankine)
* Time (seconds, minutes, hours, days...)
* Viscosity (poise, pascal-second)
* Volume (cubic metres, litres, quarts, gallons, cups...)

## Features

Units are automatically scaled based on a scaling option. This even works with imperial units like inches; i.e "kiloinch".

The following unit scaling options are supported:

    si          - use SI prefix table (default option)
    decimal     - use decimal prefix table
    binary      - use binary prefix table
    all         - use SI and binary tables
    both        - use decimal and binary tables
    none        - unit doesn't support prefix scaling

Certain units override the default scaling behaviour. For example bytes uses "both" to
generate decimal prefixes like "kilobytes" and also binary prefixes like "kibibytes".


## Requirements

    Python 3.9 or newer

## Installation

    git clone https://github.com/Emetophobe/unitconverter.git

## Usage

    usage: convert.py [-h] [-p size] [-c] [-e] value source dest

    A simple unit converter.

    positional arguments:
    value                 integer or float value to convert.
    source                name of the source unit.
    dest                  name of the destination unit.

    options:
    -h, --help            show this help message and exit
    -p size, --precision size
                          set rounding precision (default: None)
    -c, --commas          show thousands separator (default: False)
    -e, --exponent        show E notation when possible (default: False)

## Examples

#### Basic usage

    $ python3 convert.py 1024 bytes kibibytes
    1024 bytes = 1 kibibytes

    $ python3 convert.py 600 seconds minutes
    600 seconds = 10 minutes

#### Unit names can be symbols or shortforms

    $ python3 convert.py 10 cm m
    10 cm = 0.1 m

    $ python3 convert.py 10 amps kA
    10 amps = 0.01 kA

#### Set rounding precision with `-p`/`--precision`

    $ python3 convert.py 12 metres inches -p 5
    12 metres = 472.44094 inches

#### Display thousands separators with `-c`/`--comma`

    $ python3 convert.py 5 cm nm -c
    5 cm = 50,000,000 nm

#### An error is displayed when converting between incompatible units

    $ python3 convert.py 58 inches grams
    Error: unit mismatch: inches=length, grams=mass

#### Multi-word unit names are also supported, but they need to be wrapped in quotes; i.e "cubic metres"

    $ python3 convert.py 1 "cubic metres" litres
    1 cubic metres = 1000 litres

#### Instead of multi-word units you can use the shortform instead:

    $ python3 convert.py 1 m3 litres
    1 m3 = 1000 litres

    $ python3 convert.py 1 m^3 litres
    1 m^3 = 1000 litres


#
### Note: This script is a work in progress. Bug reports or suggestions are welcome.
