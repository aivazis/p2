#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2021 all rights reserved


def test():
    """
    Sanity check: verify that the base {node} has {tuple}
    """
    # get the base node from the {calc} package
    from p2.calc.Node import Node as node
    # access the tuple class
    node.tuple
    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
