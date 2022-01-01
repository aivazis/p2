#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2022 all rights reserved


def test():
    """
    Exercise the algebra of arithmetic operations among nodes
    """

    # access the various operator
    import operator
    # access the package
    import p2.algebraic

    # declare a node class
    class node(metaclass=p2.algebraic.algebra, basenode=True):
        """
        The base node
        """

        class literal:
            """
            An implementation of literals
            """
            # public data
            value = None
            # metamethods
            def __init__(self, value, **kwds):
                # chain up
                super().__init__(**kwds)
                # save the value
                self.value = value
                # all done
                return

    # declare a couple of nodes
    n1 = node.variable()
    n2 = node.variable()

    # unary operators
    assert +n1 is n1
    check_unary(-n1, operator.neg, n1)
    check_unary(abs(n1), operator.abs, n1)

    # binary operators
    check_binary(n1+n2, operator.add, n1, n2)
    check_binary(n1-n2, operator.sub, n1, n2)
    check_binary(n1*n2, operator.mul, n1, n2)
    check_binary(n1/n2, operator.truediv, n1, n2)
    check_binary(n1//n2, operator.floordiv, n1, n2)
    check_binary(n1**n2, operator.pow, n1, n2)
    check_binary(n1%n2, operator.mod, n1, n2)

    # ternary expressions
    check_ternary(n1 + (n2 - n1), operator.add, operator.sub, n1, n2, n1)
    check_ternary(n1 * (n2 / n1), operator.mul, operator.truediv, n1, n2, n1)
    check_ternary(n2*(n1 - n2), operator.mul, operator.sub, n2, n1, n2)

    # operations with literals
    check_left(1+n2, operator.add, 1, n2)
    check_right(n2+1, operator.add, 1, n2)
    check_left(1-n2, operator.sub, 1, n2)
    check_right(n2-1, operator.sub, 1, n2)
    check_left(2*n1, operator.mul, 2, n1)
    check_right(n1*2, operator.mul, 2, n1)
    check_left(3/n2, operator.truediv, 3, n2)
    check_right(n2/3, operator.truediv, 3, n2)
    check_left(3//n2, operator.floordiv, 3, n2)
    check_right(n2//3, operator.floordiv, 3, n2)
    check_left(3%n2, operator.mod, 3, n2)
    check_right(n2%3, operator.mod, 3, n2)
    check_left(3**n2, operator.pow, 3, n2)
    check_right(n2**3, operator.pow, 3, n2)

    return node


# checkers
def check_unary(expression, operator, operand):
    assert expression.evaluator is operator
    assert expression._operands[0] is operand
    return


def check_binary(expression, operator, op1, op2):
    assert expression.evaluator is operator
    assert expression._operands[0] is op1
    assert expression._operands[1] is op2
    return

def check_ternary(expression, operator1, operator2, op1, op2, op3):
    assert expression.evaluator is operator1
    assert expression._operands[0] is op1
    assert expression._operands[1].evaluator is operator2
    assert expression._operands[1]._operands[0] is op2
    assert expression._operands[1]._operands[1] is op3
    return

def check_left(expression, operator, value, node):
    assert expression.evaluator is operator
    assert expression._operands[0].value == value
    assert expression._operands[1] is node
    return

def check_right(expression, operator, value, node):
    assert expression.evaluator is operator
    assert expression._operands[0] is node
    assert expression._operands[1].value == value
    return


# main
if __name__ == "__main__":
    # do...
    test()


# end of file
