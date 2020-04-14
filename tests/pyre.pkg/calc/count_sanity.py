#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


#
def test():
    """
    Verify that the count operator works as expected
    """
    # get the node class
    from p2.calc.Node import Node as node

    # make some nodes
    nodes = [ node.variable(value=v) for v in range(0,100,10) ]
    # construct a node that computes their count
    s = node.count(operands=nodes)

    # check the current value
    assert s.getValue() == len(nodes)

    # adjust the values
    for node, value in zip(nodes, range(0, 200, 20)):
        node.setValue(value)

    # check again
    assert s.getValue() == len(nodes)

    # all done
    return


# main
if __name__ == "__main__":
    # request debugging support for the {p2.calc} package
    pyre_debug = { "p2.calc" }
    # run the test
    test()
    # verify reference counts
    from p2.calc.Node import Node as node
    # verify all nodes have been destroyed
    assert len(node.pyre_extent) == 0


# end of file
