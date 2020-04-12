#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


def test():
    """
    Verify that replacing nodes in a complicated expression works as expected
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

    # compute their sum
    s = v1 + v2
    # and their difference
    d = v1 - v2

    # form the product
    p = s * d

    # verify that the values are computed correctly
    assert s.getValue() == 3
    assert d.getValue() == -1
    assert p.getValue() == (v1**2 - v2**2).getValue()

    # verify the node observers are as expected
    assert set(v1.observers) == { s, d }
    assert set(v2.observers) == { s, d }
    assert set(s.observers) == { p }
    assert set(d.observers) == { p }

    # now, ask {s} to replace {d} in {p}
    s.replace(d)

    # the value of {s} should be unchanged
    assert s.getValue() == 3
    # {d} as well
    assert d.getValue() == -1
    # but {p} is different
    assert p.getValue() == ((v1 + v2)**2).getValue()

    # check the observers
    # nothing has changed for {v1}
    assert set(v1.observers) == { s, d }
    # nor {v2}
    assert set(v2.observers) == { s, d }
    # {s} is being observed by {p}, as before
    assert set(s.observers) == { p }
    # and {d} is not observed
    assert set(d.observers) == set()

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
