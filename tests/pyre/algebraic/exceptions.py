#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2019 all rights reserved


"""
Tests for all the exceptions raised by this package
"""


def test():
    # pull the exceptions
    from p2.algebraic.exceptions import NodeError, CircularReferenceError

    # the base exception
    try:
        raise NodeError()
    except NodeError as error:
        pass

    # circular references
    try:
        raise CircularReferenceError(node=None, path=None)
    except CircularReferenceError as error:
        pass

    # all done
    return


# main
if __name__ == "__main__":
    # skip pyre initialization since we don't rely on the executive
    pyre_noboot = True
    # do...
    test()


# end of file
