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

    # make a pair of variables
    v1 = node.variable(value=1)
    v2 = node.variable(value=2)

    # use them in a simple expression
    s = v1 + v2
    # we expect {s} to have two operands
    assert set(s.operands) == { v1, v2 }

    # we expect:
    # {v1} to have a single observer: {s}
    assert list(v1.observers) == [ s ]
    # {v2} to have a single observer: {s}
    assert list(v2.observers) == [ s ]
    # and s to have none
    assert list(s.observers) == []

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
