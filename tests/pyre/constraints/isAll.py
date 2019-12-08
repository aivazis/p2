#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2019 all rights reserved


"""
Exercise "isAll"
"""


def test():
    # get the package
    import p2.constraints
    # build a constraint
    less = p2.constraints.isLess(value=1)
    greater = p2.constraints.isGreater(value=0)
    constraint = p2.constraints.isAll(less, greater)

    # exercise it with passing values
    constraint.validate(0.1)
    constraint.validate(0.5)
    constraint.validate(0.9)

    # a case that should fail
    stranger = 1
    try:
        constraint.validate(stranger)
    except constraint.ConstraintViolationError as error:
        assert error.constraint in [less, greater]
        assert error.value == stranger

    # and another one
    stranger = 0
    try:
        constraint.validate(stranger)
    except constraint.ConstraintViolationError as error:
        assert error.constraint in [less, greater]
        assert error.value == stranger

    # all done
    return constraint


# main
if __name__ == "__main__":
    # skip pyre initialization since we don't rely on the executive
    pyre_noboot = True
    # do...
    test()


# end of file
