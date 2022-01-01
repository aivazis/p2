#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2022 all rights reserved


def test():
    """
    Exercise the interface of lists
    """
    # get the base node from the {calc} package
    from p2.calc.Node import Node as node

    # make some nodes
    nodes = ( node.variable(value=n) for n in range(10) )

    # make a list with these nodes
    l1 = node.list(value=nodes)
    # check that
    for op, node in zip(l1.operands, nodes):
        # the operands are the exact nodes we supplied
        assert op is node
    # verify that the value is what we expect
    assert l1.getValue() == list(range(10))

    # make some numbers
    ints = list(range(10))
    # make a list out of them
    l2 = node.list(value=ints)
    # check that all the {s2} operands
    for op in l2.operands:
        # are literals
        assert isinstance(op, node.literal)
    # verify that the value is what we expect
    assert l2.getValue() == list(range(10))

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
