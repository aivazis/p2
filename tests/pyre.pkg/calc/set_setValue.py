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

    # make a set
    s = node.set(value=[])
    # access the value
    assert s.getValue() == set()

    # make some nodes
    nodes = tuple( node.variable(value=n) for n in range(10) )
    # and some numbers
    numbers = (1, 2, 3)
    # set the value
    s.setValue(value=nodes+numbers)
    # verify it happened correctly
    assert s.getValue() == {0,1,2,3,4,5,6,7,8,9}

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
