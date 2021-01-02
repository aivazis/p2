#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2021 all rights reserved


def test():
    """
    Verify that nodes get cleaned up correctly
    """
    # get the node base class
    from p2.calc.Node import Node as node
    # verify that it is has extent, and that it is empty
    assert len(node.pyre_extent) == 0

    # make a couple of variables
    v1 = node.variable(value=1)
    v2 = node.variable(value=2)
    # verify that the two nodes are accounted for
    assert len(node.pyre_extent) == 2

    # build an expression
    e = v1**2 + 2*v1*v2 + v2**2
    # we just created an additional 9 nodes (count them!)
    assert len(node.pyre_extent) ==  11

    # all done; all nodes go out of scope here, so they should get destroyed
    return


# main
if __name__ == "__main__":
    # turn on debug support in {calc}
    pyre_debug = {"p2.calc"}

    # get the node base class
    from p2.calc.Node import Node as node
    # get the calculator
    from p2.calc import calculator
    # get {Extent}
    from p2.patterns.Extent import Extent as extent
    # verify the calculator is a subclass of {Extent}
    assert issubclass(calculator, extent)

    # run the test
    test()

    # verify that all nodes have been destroyed
    assert len(node.pyre_extent) == 0


# end of file
