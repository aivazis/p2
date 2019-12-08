#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2019 all rights reserved


"""
Exercise "isPositive"
"""


def test():
    # get the package
    import p2.constraints
    # build a constraint
    constrain = p2.constraints.isPositive()

    # exercise with good values
    constrain(1)
    constrain(1.1)
    constrain(2)

    # a case that should fail
    stranger = -1
    try:
        constrain(stranger)
    except constrain.ConstraintViolationError as error:
        assert error.constraint == constrain
        assert error.value == stranger

    # and another one
    stranger = 0
    try:
        constrain(stranger)
    except constrain.ConstraintViolationError as error:
        assert error.constraint == constrain
        assert error.value == stranger

    # all done
    return constrain


# main
if __name__ == "__main__":
    # skip pyre initialization since we don't rely on the executive
    pyre_noboot = True
    # run the test
    test()


# end of file
