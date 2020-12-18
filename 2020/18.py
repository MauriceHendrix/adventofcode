# see https://stackoverflow.com/questions/23879784/parse-mathematical-expressions-with-pyparsing
from timing import timing
from pyparsing import Suppress, Forward, Group, oneOf, pyparsing_common, infixNotation, opAssoc

op_prec = []

def eval(input_expression):
    def calc(l):
        if isinstance(l, int):
            return l
        elif len(l) == 1:
            return calc(l[0])
        elif l[-2] == '+':
            assert len(l) >=3
            return calc(l[0:-2]) + calc(l[-1])
        elif l[-2] == '*':
            assert len(l) >=3
            return calc(l[0:-2]) * calc(l[-1])
        else:
            assert False
    
       
    LPAR,RPAR = map(Suppress, '()')
    expr = Forward()
    factor =  pyparsing_common.integer  | Group(LPAR + expr + RPAR)
    expr = infixNotation(pyparsing_common.integer, op_prec)
   
    return calc(expr.parseString(input_expression))

@timing
def calc_sum(expressions):
    return sum(map(eval, expressions))

if __name__ == "__main__":
    with open('input-18.txt') as expressions:
        expressions = expressions.read().split('\n')
        op_prec = [(oneOf(['+', '*']), 2, opAssoc.LEFT)]
        print(calc_sum(expressions))
        op_prec = [(oneOf(['+']), 2, opAssoc.LEFT), (oneOf(['*']), 2, opAssoc.LEFT)]
        print(calc_sum(expressions))
