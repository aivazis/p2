#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


def test():
    """
    Verify that replacing an operator that participates in an expression works as expected
    """
    # get the base node form the {calc} package
    from p2.calc.Node import Node as node

    # the assertions in this test must be done more carefully if nodes have {ordering} since
    # then the equality test becomes a node. the current implementation of {node} does not
    # include {ordering}, so we should be ok with naive checks.

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
    # and use this to build a more complicated one
    d = 2 * s

    # verify that the values are computed correctly
    assert s.getValue() == 3
    assert d.getValue() == 6

    # verify the node observers are as expected
    assert set(v1.observers) == { s }
    assert set(v2.observers) == { s }
    assert set(v3.observers) == set()
    assert set(s.observers) == { d }
    assert set(d.observers) == set()

    # now, replace {s} with {v1}
    v3.replace(obsolete=s)

    # the value of {s} should be unchanged
    assert s.getValue() == 3
    # but {d} is different
    assert d.getValue() == 6

    # check the observers
    # nothing has changed for {v1} since {s} is still alive
    assert set(v1.observers) == { s }
    # same for {v2}
    assert set(v2.observers) == { s }
    # {v3} is now observed by {d}
    assert set(v3.observers) == { d }
    # {s} is not being observed any more
    assert set(s.observers) == set()
    # and, of course, no one is watching {d}
    assert set(d.observers) == set()

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
