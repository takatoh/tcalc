from lark import Lark
from lark.exceptions import UnexpectedInput
from lark.visitors import Interpreter
from os import path
from tcalc.time import Time


here = path.dirname(path.abspath(__file__))
grammer_file = path.join(here, '../grammer/tcalc.lark')
with open(grammer_file) as f:
    TCALC_GRAMMER = f.read()


class Parser():
    def __init__(self):
        self.parser = Lark(TCALC_GRAMMER, start='expr')

    def parse(self, input_data):
        try:
            tree = self.parser.parse(input_data)
        except UnexpectedInput as e:
            print('Syntax error:')
            print(e.get_context(input_data))
            exit(1)
        return tree


class Calculator(Interpreter):
    def expr(self, tree):
        tokens = [self.visit(c) for c in tree.children]
        t1 = tokens[0]
        chunks = [tokens[i:i+2] for i in range(1, len(tokens), 2)]
        for o, t2 in chunks:
            if o == '+':
                t1 = t1 + t2
            elif o == '-':
                t1 = t1 - t2
        return t1

    def val(self, tree):
        return self.visit(tree.children[0])

    def time(self, tree):
        t = Time(tree.children[0].value)
        return t

    def op(self, tree):
        return tree.children[0].value
