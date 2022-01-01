#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2022 all rights reserved


def test():
    """
    Verify that replacing a variable that participates in a simple expression works as expected
    """
    # get the base node from the {calc} package
    from p2.calc.Node import Node as node

    # assertions that involve node comparisons must be done very carefully if nodes have
    # {ordering} since then the equality test becomes a node. the current implementation of
    # {node} does not include {ordering}, so we should be ok with naive checks.

    # get the calculator
    from p2.calc import calculator
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

    # make sure it computes correctly
    assert s.getValue() == 3

    # check observers; we expect
    # {v1} to be observed by {s}
    assert set(v1.observers) == { s }
    # {v2} to be observed by {s}
    assert set(v2.observers) == { s }
    # and {v3} to have no observers
    assert set(v3.observers) == set()

    # replace {v1} with {v3}
    v3.replace(obsolete=v1)

    # verify the substitution took place
    assert set(s.operands) == { v2, v3 }
    # make sure it computes correctly
    assert s.getValue() == 5

    # check observers; we expect
    # {v1} to have no observers
    assert set(v1.observers) == set()
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
