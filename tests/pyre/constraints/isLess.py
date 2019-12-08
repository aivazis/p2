#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2019 all rights reserved


"""
Exercise "isLess"
"""


def test():
    # get the package
    import p2.constraints
    # build a constraint
    constraint = p2.constraints.isLess(value=1)

    # exercise with good values
    constraint.validate(0.9)
    constraint.validate(0)

    # a case that should fail
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
