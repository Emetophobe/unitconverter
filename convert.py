#!/usr/bin/env python
# Copyright (c) 2022-2025 Mike Cunningham
# https://www.github.com/emetophobe/unitconverter


import sys
import logging
import argparse

from decimal import DecimalException


from unitconverter.converter import UnitConverter
from unitconverter.exceptions import ConverterError
from unitconverter.formatting import format_quantity
from unitconverter.utils import parse_decimal


def print_error(msg: str, status: int = 1) -> None:
    """ Print an error message and exit. """
    print(msg, file=sys.stderr)
    sys.exit(status)


def main() -> None:
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "quantity",
        help="quantity or value")

    parser.add_argument(
        "source",
        help="the source unit")

    parser.add_argument(
        "target",
        help="one or more target units",
        nargs="+")

    parser.add_argument(
        "-n", "--normalize",
        help="normalize result by stripping trailing zeros",
        action="store_true")

    parser.add_argument(
        "-e", "--exponent",
        help="show E notation if possible (default: False)",
        action="store_true")

    parser.add_argument(
        "-s", "--separators",
        help="show thousands separators if possible (default: False)",
        action="store_true")

    parser.add_argument(
        "-p", "--precision",
        help="set rounding precision (default: %(default)s)",
        metavar="ndigits",
        default=None,
        type=int)

    parser.add_argument(
        "--debug",
        help=argparse.SUPPRESS,
        action="store_true")

    args = parser.parse_args()

    # Try to convert quantity to a decimal
    try:
        args.quantity = parse_decimal(args.quantity)
    except (ConverterError, DecimalException):
        print_error(f"Error: {args.quantity!r} is not a decimal or integer value")

    # Check precision
    if args.precision is not None and (args.precision < 0 or args.precision > 30):
        print_error("Error: Precision must be between 0 and 30")

    # Allow <source> to <target> syntax but check for errors
    if "to" in args.target:
        if args.target.count("to") > 1 or args.target[0] != "to" or len(args.target) == 1:
            print_error("Error: Invalid use of <source> to <target> syntax")
        # Make sure to remove "to" from the target units
        args.target.remove("to")

    # Configure debug logger
    logging.getLogger().setLevel(logging.DEBUG if args.debug else logging.WARNING)
    logging.basicConfig(format="debug: %(message)s")

    results = []

    # Perform conversions
    converter = UnitConverter()
    for target in args.target:
        results.append((converter.convert(args.quantity, args.source, target), target))

    # Display results
    quantity = format_quantity(args.quantity, separators=args.separators)
    padding = " " * len(f"{quantity} {args.source}")

    for index, (result, target) in enumerate(results):
        result = format_quantity(result, args.precision, args.normalize,
                                 args.exponent, args.separators)
        if index == 0:
            print(f"{quantity} {args.source} = {result} {target}")
        else:
            print(f"{padding} = {result} {target}")


if __name__ == "__main__":
    try:
        main()
    except ConverterError as e:
        print_error("Error: " + str(e))
