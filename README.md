# Unit Converter

A basic unit converter written in Python.

This script is meant to be used as a command line utility. If you're looking for a
python library there are superior alternatives such as [pint][1] or [metrolopy][2].

The following unit categories are currently supported:

* Absorbed dose (gray, usrad)
* Acceleration (metre/second², foot/second², mile/second²)
* Amount of substance (mole, atom)
* Area (square metre, square mile, acre, hectare, etc...)
* Catalytic activity (katal, mole/second, enzyme unit)
* Data storage (bits, bytes, kilobytes, kibibytes, etc...)
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
* Speed (kilometres/hour, miles/hour, metre/second, inch/second, etc...)
* Temperature (kelvin, celsius, fahrenheit, and rankine)
* Time (second, minute, hour, day, week, month, year, etc...)
* Viscosity (pascal-second and poise)
* Volume (cubic metre, litre, quart, gallon, etc...)

## Features

Units are prefixed based on a prefix scaling option. The default prefix
scaling behaviour can be changed on a per-unit basis.

The following prefix options are currently supported:

    none        - don't use prefix scaling (default)
    metric      - use metric prefix table
    binary      - use binary prefix table (kibi to yobi)
    bit         - use bit prefix table (kilo to quetta)
    byte        - use bit and binary tables
    all         - use metric and binary tables


Units can also be combined to create composite units. You can create a composite unit
from any of the defined units (excluding temperature units). Temperature units use
a custom conversion function and don't work with other units for now.

For example you can create a speed unit by dividing any `length` unit by any `time` unit:

    $ python3 convert.py 1 metre/second inches/day -p 2
    1 metre/second = 3401574.8 inches/day

Many other unit combinations are possible:

    $ python3 convert.py 1 watt amp*volt joule/second
    1 watt = 1 amp*volt
           = 1 joule/second

    $ python3 convert.py 1 joule kg*m2*s-2 pascal*metre^3 watt*second coulomb*volt
    1 joule = 1 kg*m2*s-2
            = 1 pascal*metre^3
            = 1 watt*second
            = 1 coulomb*volt

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

#### Unit names can be symbols, plural forms, or other aliases

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

#### Show E notation with `-e`/`--exponent`

    $ python3 convert.py 5 cm nm -e
    5 cm = 5E+7 nm

#### Convert multiple units at once

    $ python3 convert.py 1 metre cm in ft -p 4
    1 metre = 100.0000 cm
            = 39.3701 in
            = 3.2808 ft

#### Multi-word unit names are also supported but they need to be wrapped in quotes

    $ python3 convert.py 1 "US survey acre" km^2 -p 8
    1 US survey acre = 0.00404687 km^2

#
### Note: This script is a work in progress. Bug reports and suggestions are welcome.


[1]: https://github.com/hgrecco/pint/
[2]: https://github.com/nrc-cnrc/MetroloPy/
