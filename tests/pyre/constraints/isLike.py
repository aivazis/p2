#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2019 all rights reserved


"""
Exercise "isLike"
"""


def test():
    # get the package
    import p2.constraints

    # build a constraint
    phone = r"(\+\d+\s+)?\(?\d{3}\)?(.|\s+)\d{3}[-.]\d{4}"
    constraint = p2.constraints.isLike(regexp=phone)

    # exercise with good values
    constraint.validate("(877) 877-0987")
    constraint.validate("(877) 877.0987")
    constraint.validate("877.877.0987")
    constraint.validate("+1 877.877.0987")

    # a case that should fail
    stranger = "(877) 877-097"
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