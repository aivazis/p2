#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2019 all rights reserved


"""
Exercise "isSubset"
"""


def test():
    # get the package
    import p2.constraints
    # build a constraint
    constraint = p2.constraints.isSubset(choices=["one", "two", "three"])

    # exercise with good values
    constraint.validate(["one"])
    constraint.validate(["two"])
    constraint.validate(["three"])
    constraint.validate(["one", "two"])
    constraint.validate(["one", "three"])
    constraint.validate(["two", "three"])
    constraint.validate(["one", "two", "three"])

    # a case that should fail
    stranger = ["zero"]
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
    # do...
    test()


# end of file
