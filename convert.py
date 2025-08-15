#!/usr/bin/env python
# Copyright (c) 2022-2025 Mike Cunningham
# https://www.github.com/emetophobe/unitconverter


import sys
import logging
import argparse

from decimal import DecimalException


from unitconverter.converter import UnitConverter
from unitconverter.exceptions import ConverterError
from unitconverter.formatting import format_decimal
from unitconverter.utils import parse_decimal


def print_error(msg: str, status: int = 1) -> None:
    """ Helper function to print an error message and exit. """
    print(msg, file=sys.stderr)
    sys.exit(status)


def main() -> None:
    parser = argparse.ArgumentParser(description="A unit converter written in Python")

    parser.add_argument(
        "value",
        help="an integer or decimal value")

    parser.add_argument(
        "source",
        help="the source unit")

    parser.add_argument(
        "dest",
        help="one or more destination units",
        nargs="+")

    parser.add_argument(
        "-p", "--precision",
        help="set rounding precision (default: %(default)s)",
        metavar="ndigits",
        default=None,
        type=int)

    parser.add_argument(
        "-s", "--separators",
        help="show thousands separator (default: False)",
        action="store_true")

    parser.add_argument(
        "-e", "--exponent",
        help="show E notation when possible (default: False)",
        action="store_true")

    parser.add_argument(
        "--debug",
        help=argparse.SUPPRESS,
        action="store_true")

    args = parser.parse_args()

    # Try to convert value to a decimal
    try:
        args.value = parse_decimal(args.value)
    except (ConverterError, DecimalException):
        print_error(f"Error: {args.value!r} is not a valid decimal.")

    # Check precision
    if args.precision is not None and (args.precision < 0 or args.precision > 20):
        print_error("Error: Precision must be between 0 and 20.")

    # Allow <source> to <unit> but check for syntax errors
    # Make sure to remove "to" from the dest units
    if "to" in args.dest:
        if args.dest.count("to") > 1 or args.dest[0] != "to" or len(args.dest) == 1:
            print_error("Error: Invalid use of <source> to <dest> syntax")
        else:
            args.dest.remove("to")

    # Configure debug logger
    logging.getLogger().setLevel(logging.DEBUG if args.debug else logging.WARNING)
    logging.basicConfig(format="debug: %(message)s")

    # Perform conversions
    converter = UnitConverter()
    results = []

    for dest_unit in args.dest:
        results.append((converter.convert(args.value, args.source, dest_unit), dest_unit))

    # Display results
    value = format_decimal(args.value, separators=args.separators)
    padding = " " * len(f"{value} {args.source}")
    for index, (result, dest) in enumerate(results):
        result = format_decimal(result, args.precision, args.exponent, args.separators)
        if index == 0:
            print(f"{value} {args.source} = {result} {dest}")
        else:
            print(f"{padding} = {result} {dest}")


if __name__ == "__main__":
    try:
        main()
    except ConverterError as e:
        print_error("Error: " + str(e))
