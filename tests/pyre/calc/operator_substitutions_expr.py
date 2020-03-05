#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


def test():
    """
    Verify that attempting to substitute nodes that aren't there is a no-op
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

    # use them in a simple expression
    s = v1 + v2
    # and use this to build a more complicated one
    d = 2 * s

    # verify that the values are computed correctly
    assert s.getValue() == 3
    assert d.getValue() == 6

    # verify the node observers are as expected
    assert set(v1.observers) == { s }
    assert set(v2.observers) == { s }
    assert set(s.observers) == { d }

    # now, replace {s} with {v1}
    d.substitute(current=s, replacement=v1)

    # the value of {s} should be unchanged
    assert s.getValue() == 3
    # but {d} is different
    assert d.getValue() == 2

    # check the observers
    # {v1} now has two observers
    assert set(v1.observers) == { s, d }
    # nothing has changed for {v2}
    assert set(v2.observers) == { s }
    # {s} is not being observed any more
    assert set(s.observers) == set()

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
