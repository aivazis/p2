#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


def test():
    """
    Exercise the interface of literals
    """
    # get the base node form the {calc} package
    from p2.calc.Node import Node as node

    # make a couple of literals
    l1 = node.literal(value=1)
    l2 = node.literal(value=2)

    # basic arithmetic
    assert (l1 + l2).getValue() == 3
    assert (l1 - l2).getValue() == -1
    assert (l1 * l2).getValue() == 2
    assert (l1 / l2).getValue() == 0.5

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
