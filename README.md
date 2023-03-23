# Unit Converter (work in progress)

A basic unit converter written in Python.


The following categories are currently supported:


* Amount of substance (moles, atoms)
* Angle (steradian, radian, square degrees)
* Area (square meters, square miles, acres, hectares, etc..)
* Bytes (bits, bytes, kilobytes, kibibytes, etc..)
* Catalytic activity (katal, mol/sec)
* Electrical (ampere, volt, ohm, coulomb, farad, henry, siemens)
* Energy (joule, calorie, btu, therm, watt seconds, watt hours, etc..)
* Force (newtons, dynes, poundals, gram force, ton force, etc..)
* Fuel consumption (mpg, liters/100km, etc..)
* Frequency (hertz)
* Illuminance (lux)
* Length (meters, feet, inches, etc...)
* Luminous flux (lumens)
* Luminous intensity (candela)
* Magnetic flux (weber, maxwell)
* Magnetic flux density (tesla, guass, gamma)
* Mass (grams, pounds, ounces, etc...)
* Power (watts, horsepower, joules/second)
* Pressure (pascal, bar, psi)
* Radiation (becqueral, curie, rutherford, gray, sievert)
* Signal intensity (decibel, bel, neper)
* Temperature (kelvin, celsius, fahrenheit, and rankine)
* Time (seconds, minutes, hours, days, etc...)
* Viscosity (poise, pascal-second)
* Volume (cubic meters, liters, quarts, gallons, cups, etc...)

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

    $ python3 convert.py 12 meters inches -p 5
    12 meters = 472.44094 inches

#### Display thousands separators with `-c`/`--comma`

    $ python3 convert.py 5 cm nm -c
    5 cm = 50,000,000 nm

#### An error is displayed when converting between incompatible units

    $ python3 convert.py 58 inches grams
    Error: unit mismatch: inches=length, grams=mass

#### Multi-word unit names are also supported, but they need to be wrapped in quotes; i.e "cubic meters"

    $ python3 convert.py 1 "cubic meters" liters
    1 cubic meters = 1000 liters

#### Instead of multi-word units you can use the shortform instead:

    $ python3 convert.py 1 m3 liters
    1 m3 = 1000 liters

    $ python3 convert.py 1 m^3 liters
    1 m^3 = 1000 liters


#
### Note: This script is a work in progress. Bug reports or suggestions are welcome.
