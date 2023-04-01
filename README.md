# Unit Converter (work in progress)

A basic unit converter written in Python.


The following categories are currently supported:


* Absorbed dose (gray, usrad)
* Acceleration (metre/second²)
* Amount of substance (mole, atom)
* Area (square metre, square mile, acre, hectare, etc...)
* Catalytic activity (katal, mol/sec)
* Data storage (bits, bytes, kilobytes, kibibytes, etc...)
* Effective dose (sievert, roentgen)
* Electric charge (coloumb, ampere-second, ampere-minute, ampere-hour)
* Electric current (ampere, watt/volt, coulomb/second)
* Electric potential (volt, watt/ampere, ampere-ohm, joule/coulomb, weber/second)
* Electrical capacitance (farad, coulomb/volt)
* Electrical conductance (siemens, ampere/volt)
* Electrical inductance (henry, weber/ampere)
* Electrical resistance (ohm, volt/ampere)
* Energy (joule, calorie, btu, therm, watt-second, watt-hour, etc...)
* Force (newton, dyne, poundal, gram-force, ton-force, etc...)
* Fuel consumption (litres/100km, km/liter, miles per gallon, etc...)
* Frequency (hertz, rpm, cycles/minute, cycles/hour)
* Illuminance (lux, nox, phot, watt/m², metre-candle, foot-candle)
* Length (metre, inch, foot, etc...)
* Luminous flux (lumen, candela-steradian)
* Luminous intensity (candela, lumen/steradian, candlepower)
* Magnetic flux (weber, maxwell)
* Magnetic flux density (tesla, guass, gamma)
* Mass (gram, pound, ounce, metric ton, etc...)
* Plane angle (radian, gradian, degree, arcsecond, arcminute, turn)
* Power (watt, volt-ampere, joule/second, horsepower, etc...)
* Pressure (pascal, bar, psi, torr, standard atmosphere, etc..)
* Radioactivity (becquerel, curie, rutherford)
* Signal intensity (decibel, bel, and neper)
* Solid angle (steradian, square degree, spat)
* Speed (km/hour, mile/hour, metre/second, inch/second, mach 1, etc...)
* Temperature (kelvin, celsius, fahrenheit, and rankine)
* Time (second, minute, hour, day, week, month, year, etc...)
* Torque (newton-metre)
* Viscosity (poise and pascal-second)
* Volume (cubic metre, litre, quart, gallon, etc...)

See [supported units](docs/supported_units.txt) for a complete list.

## Features

Units can be automatically scaled based on a prefix scaling option.

The following prefix scaling options are supported:

    none        - don't use prefix scaling (default)
    si          - use SI prefix table
    decimal     - use decimal prefix table
    binary      - use binary prefix table
    all         - use SI and binary tables
    both        - use decimal and binary tables

Units can override the default scaling behaviour as needed. SI units for example use the "si" prefix scale. Another example is bytes which uses "both" to generate both decimal prefixes like "kilobytes" and also binary prefixes like "kibibytes".


## Requirements

    Python 3.11 or newer

## Installation

    git clone https://github.com/Emetophobe/unitconverter.git

## Usage

    usage: convert.py [-h] [-p ndigits] [-c] [-e] [-a] value source dest

    A simple unit converter

    positional arguments:
    value                 integer or decimal value.
    source                source unit.
    dest                  destination unit.

    options:
    -h, --help            show this help message and exit
    -p ndigits, --precision ndigits
                          set rounding precision (default: None)
    -c, --commas          show thousands separator (default: False)
    -e, --exponent        show E notation when possible (default: False)
    -a, --american        use American spelling of meter/liter (default: False)


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
