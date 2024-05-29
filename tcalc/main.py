from tcalc.parser import Parser, Calculator
import sys


def main():
    parser = Parser()
    expr = ''.join(sys.argv[1:])
    tree = parser.parse(expr)
    #print(tree)
    calculator = Calculator()
    answer = calculator.visit(tree)
    print(answer)
