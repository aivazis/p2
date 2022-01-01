#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2022 all rights reserved


def test():
    """
    Exercise the interface of sets
    """
    # get the base node from the {calc} package
    from p2.calc.Node import Node as node

    # make some nodes
    nodes = ( node.variable(value=n) for n in range(10) )

    # make a set with these nodes
    s1 = node.set(value=nodes)
    # check that
    for op, node in zip(s1.operands, nodes):
        # the operands are the exact nodes we supplied
        assert op is node
    # verify that the value is what we expect
    assert s1.getValue() == set(range(10))

    # make some numbers
    ints = set(range(10))
    # make a set out of them
    s2 = node.set(value=ints)
    # check that all the {s2} operands
    for op in s2.operands:
        # are literals
        assert isinstance(op, node.literal)
    # verify that the value is what we expect
    assert s2.getValue() == set(range(10))

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
