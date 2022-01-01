#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2022 all rights reserved


def test():
    """
    Exercise basic arithmetic operations among variables
    """
    # get the base node from the {calc} package
    from p2.calc.Node import Node as node

    # make a couple of variables
    v1 = node.variable(value=1)
    v2 = node.variable(value=2)

    # basic arithmetic among variables
    assert (v1 + v2).getValue() == 3
    assert (v1 - v2).getValue() == -1
    assert (v1 * v2).getValue() == 2
    assert (v1 / v2).getValue() == 0.5
    assert (v1 ** v2).getValue() == 1
    assert (v1 % v2).getValue() == 1

    # variables and literals
    assert (v1 + 2).getValue() == 3
    assert (v1 - 2).getValue() == -1
    assert (v1 * 2).getValue() == 2
    assert (v1 / 2).getValue() == 0.5
    assert (v1 ** 2).getValue() == 1
    assert (v1 % 2).getValue() == 1

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
