#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2019 all rights reserved


"""
Tests for all the exceptions raised by this package
"""

def test():
    # get the exception
    from p2.constraints.exceptions import ConstraintViolationError

    # exercise it
    try:
        raise ConstraintViolationError(constraint=None, value=None)
    except ConstraintViolationError as error:
        pass

    # all done
    return


# main
if __name__ == "__main__":
    # skip pyre initialization since we don't rely on the executive
    pyre_noboot = True
    # run the test
    test()


# end of file
