from lark import Lark
from lark.exceptions import UnexpectedInput
from os import path


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
