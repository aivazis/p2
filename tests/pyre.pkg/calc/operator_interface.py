#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2022 all rights reserved


def test():
    """
    Exercise the interface of operators
    """
    # get the base node from the {calc} package
    from p2.calc.Node import Node as node

    # use an expression make an operator
    operator = 2 * node.literal(value=1)

    # access the value
    assert operator.getValue() == 2

    # attempt to
    try:
        # set the value
        operator.setValue(value=1)
        # which should fail
        assert False, "unreachable"
    # because there is no base with an implementation
    except AttributeError as error:
        # all good
        pass

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
