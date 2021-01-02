#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2021 all rights reserved


def test():
    """
    Exercise the interface of variables
    """
    # get the base node from the {calc} package
    from p2.calc.Node import Node as node

    # make a variable
    variable = node.variable(value=0)

    # access the value
    assert variable.getValue() == 0

    # set the value
    variable.setValue(value=1)
    # verify it happened correctly
    assert variable.getValue() == 1

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
