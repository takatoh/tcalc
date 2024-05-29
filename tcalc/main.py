from tcalc.parser import Parser
from os import path
import sys


here = path.dirname(path.abspath(__file__))
grammer_file = path.join(here, '../grammer/tcalc.lark')
with open(grammer_file) as f:
    TCALC_GRAMMER = f.read()


def main():
    parser = Parser()
    expr = ''.join(sys.argv[1:])
    tree = parser.parse(expr)
    print(tree)


main()
