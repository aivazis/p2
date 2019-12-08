#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2019 all rights reserved
# -*- coding: utf-8 -*-


"""
Exercise "isBetween"
"""


def test():
    # get the package
    import p2.constraints
    # build a constraint
    constraint = p2.constraints.isBetween(low=0, high=1)

    # exercise with good values
    constraint.validate(.1)
    constraint.validate(.1)
    constraint.validate(.9)

    # a case that should fail
    stranger = 0
    try:
        constraint.validate(stranger)
    except constraint.ConstraintViolationError as error:
        assert error.constraint == constraint
        assert error.value == stranger

    # and another one
    stranger = 1
    try:
        constraint.validate(stranger)
    except constraint.ConstraintViolationError as error:
        assert error.constraint == constraint
        assert error.value == stranger

    # all done
    return constraint


# main
if __name__ == "__main__":
    # skip pyre initialization since we don't rely on the executive
    pyre_noboot = True
    # run the test
    test()


# end of file
