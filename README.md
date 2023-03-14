# Unit Converter

A basic unit converter written in Python.

The following unit categories are currently supported:

* Area (square meters, square miles, acres, hectares, etc..)
* Bytes (bits, bytes, kilobytes, kibibytes, etc..)
* Length (meters, feet, inches, etc...)
* Mass (grams, pounds, ounces, etc...)
* Temperature (celsius, fahrenheit, kelvin, and rankine)
* Time (seconds, minutes, hours, days, etc...)
* Volume (cubic meters, liters, quarts, gallons, cups, etc...)

### This script is a work in progress. Bug reports or suggestions are welcome.


## Requirements

    Python 3.9 or newer.

## Installation

    git clone https://github.com/Emetophobe/unitconverter.git

## Usage

    usage: converter.py [-h] [-p size] [-c] [-l] value source dest

    A simple unit converter.

    positional arguments:
    value                 integer or float value to convert.
    source                name of the source unit.
    dest                  name of the destination unit.

    options:
    -h, --help            show this help message and exit
    -p size, --precision size
                            rounding precision (default: None)
    -c, --comma           show thousands separator (default: False)
    -l, --list            list unit categories and exit


## Examples

### Basic usage

    $ python3 converter.py 1024 bytes kibibytes
    1024 bytes = 1 kibibytes

    $ python3 converter.py 600 seconds minutes
    600 seconds = 10 minutes

### Unit names can be symbols or shortforms

    $ python3 converter.py 10 centimeters meters
    10 centimeters = 0.1 meters

    $ python3 converter.py 10 cm m
    10 cm = 0.1 m

### Set rounding precision with `-p`/`--precision`

    $ python3 converter.py 12 meters inches -p 5
    12 meters = 472.44094 inches

### Display thousands separators with `-c`/`--comma`

    $ python3 converter.py 5 cm nm -c
    5 cm = 50,000,000 nm

### An error is displayed when converting between incompatible units

    $ python3 converter.py 58 inches grams
    Error: unit mismatch: inches=length, grams=mass

### Multi-word unit names are also supported, but for now they need to be wrapped in quotes; i.e `"cubic meters"`.

    $ python3 converter.py 1 "cubic meters" liters
    1 cubic meters = 1000 liters

### Another option is to use shortform to get around this limitation

    $ python3 converter.py 1 m3 liters
    1 m3 = 1000 liters

    $ python3 converter.py 1 m^3 liters
    1 m^3 = 1000 liters
