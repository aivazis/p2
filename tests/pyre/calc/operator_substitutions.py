#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


def test():
    """
    Verify operators observe their operands
    """
    # get the base node form the {calc} package
    from p2.calc.Node import Node as node

    # the assertions in this test must be done more carefully if nodes have {ordering} since
    # then the equality test becomes a node. the current implementation of {node} does not
    # include {ordering}, so we should be ok with naive checks.

    # get the calculator
    from pyre.calc import calculator
    # make sure node does not derive from {ordering}
    assert not issubclass(node, calculator.ordering)

    # make a few variables
    v1 = node.variable(value=1)
    v2 = node.variable(value=2)
    v3 = node.variable(value=3)

    # use them in a simple expression
    s = v1 + v2

    # we expect {s} to have two operands
    assert set(s.operands) == { v1, v2 }

    # check observers; we expect
    # {v1} to be observed by {s}
    assert set(v1.observers) == { s }
    # {v2} to be observed by {s}
    assert set(v2.observers) == { s }
    # and {v3} to have no observers
    assert set(v3.observers) == {}

    # substitute {v3} for {v1}
    s.substitute(current=v1, replacement=v3)

    # verify the substitution took place
    assert set(s.operands) == { v2, v3 }

    # check observers; we expect
    # {v1} to have no observers
    assert set(v1.observers) == {}
    # {v2} to be observed by {s}
    assert set(v2.observers) == { s }
    # and {v3} to be observed by {s}
    assert set(v3.observers) == { s }


    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
