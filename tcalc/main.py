from tcalc.core import Parser, Calculator
import sys


def main():
    parser = Parser()
    expr = ''.join(sys.argv[1:])
    tree = parser.parse(expr)
    calculator = Calculator()
    answer = calculator.visit(tree)
    print(answer)
