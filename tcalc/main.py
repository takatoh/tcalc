from tcalc.core import Parser, Calculator
from tcalc import __version__
import argparse


SCRIPT_VERSION = f'v{__version__}'


def main():
    args = parse_arguments()
    parser = Parser()
    expr = ''.join(args.terms)
    tree = parser.parse(expr)
    calculator = Calculator()
    answer = calculator.visit(tree)
    print(answer)


def parse_arguments():
    parser = argparse.ArgumentParser(
        description='Time calculator'
    )
    parser.add_argument(
        'terms',
        action='store',
        nargs='+',
        metavar='TERM',
        help='term or operator'
    )
    parser.add_argument(
        '-V', '--version',
        action='version',
        version=SCRIPT_VERSION,
        help='show version and exit'
    )
    args = parser.parse_args()
    return args
