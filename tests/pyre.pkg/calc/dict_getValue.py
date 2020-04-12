#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


def test():
    """
    Exercise the interface of dicts
    """
    # get the base node from the {calc} package
    from p2.calc.Node import Node as node

    # make some nodes
    nodes = ((str(n), node.variable(value=n)) for n in range(10))

    # make a dict with these nodes
    s1 = node.dict(value=nodes)
    # check that
    for op, node in zip(s1.operands, nodes):
        # the operands are the exact nodes we supplied
        assert op is node
    # verify that the value is what we expect
    assert s1.getValue() == dict( (str(n),n) for n in range(10))

    # make some numbers
    ints = dict((str(n), n) for n in range(10))
    # make a dict out of them
    s2 = node.dict(value=ints.items())
    # check that all the {s2} operands
    for op in s2.operands:
        # are literals
        assert isinstance(op, node.literal)
    # verify that the value is what we expect
    assert s2.getValue() == ints

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
