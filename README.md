# Unit Converter (work in progress)

A basic unit converter written in Python.


The following categories are currently supported:


* Absorbed dose (gray, usrad)
* Acceleration (metre/second², foot/second², mile/second²)
* Amount of substance (mole, atom)
* Area (square metre, square mile, acre, hectare, etc...)
* Catalytic activity (katal, mole/second, enzyme unit)
* Data storage (bits, bytes, kilobytes, kibibytes, etc...)
* Data transfer (bits/second, bytes/second)
* Effective dose (sievert, roentgen)
* Electric charge (coloumb, ampere-second, ampere-minute, ampere-hour)
* Electric current (ampere, watt/volt, coulomb/second)
* Electric potential (volt, joule/coulomb, watt/ampere, weber/second)
* Electrical capacitance (farad, coulomb/volt)
* Electrical conductance (siemens, ampere/volt)
* Electrical inductance (henry, weber/ampere)
* Electrical resistance (ohm, volt/ampere)
* Energy (joule, calorie, btu, therm, watt-second, watt-hour, etc...)
* Force (newton, dyne, poundal, gram-force, ton-force, etc...)
* Fuel consumption (litre/metre, litre/100km, gallon/mile)
* Fuel economy (metre/litre, foot/gallon, mile/gallon)
* Frequency (hertz, rpm, cycles/minute, cycles/hour)
* Illuminance (lux, nox, phot, watt/m², metre-candle, foot-candle)
* Length (metre, inch, foot, etc...)
* Luminance (cd/m², nit, stilb, apostilb, etc..)
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

See [supported units](docs/supported_units.txt) for a complete list. Note that composite
units aren't included in this list, such as square inches (area) which can be generated
from an inch (length).

## Features

Units are prefixed (i.e "kilo") based on a prefix scaling option. The default prefix scaling behaviour can be changed on a per-unit basis.

The following prefix options are currently supported:

    none        - don't use prefix scaling (default)
    si          - use SI prefix table
    binary      - use binary prefix table
    bit         - use bit prefix table (kilo to quetta)
    byte        - use bit and binary tables
    all         - use SI and binary tables


Units can also be combined to create composite units. You can create a composite unit from any of the defined units (excluding temperature units). Temperature units use a custom conversion function and don't work with other units for now.

As an example, you can create a speed unit by dividing a `length` unit by a `time` unit:

    $ python convert.py 1 metre/second inches/day -p 2
    1 metre/second = 3401574.8 inches/day





Unit composition is an experimental feature and there are still bugs to be sorted out.



## Requirements

    Python 3.11 or newer

## Installation

    git clone https://github.com/Emetophobe/unitconverter.git

## Usage

    usage: convert.py [-h] [-p ndigits] [-c] [-e] value source dest [dest ...]

    A simple unit converter

    positional arguments:
    value                 integer or decimal value
    source                the source unit
    dest                  one or more destination units

    options:
    -h, --help            show this help message and exit
    -p ndigits, --precision ndigits
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

#### Convert multiple units at once

    $ python3 convert.py 1 metre cm in ft -p 4
    1 metre = 100.0000 cm
            = 39.3701 in
            = 3.2808 ft

#### An error is displayed when converting between incompatible units

    $ python3 convert.py 58 inch gram
    Category mismatch: inch (length) and gram (mass)

#### Multi-word unit names are also supported but they need to be wrapped in quotes

    $ python3 convert.py 1 "cubic metres" litres
    1 cubic metres = 1000 litres

#
### Note: This script is a work in progress. Bug reports or suggestions are welcome.
