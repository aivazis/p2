#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


def test():
    """
    Tests for all the exceptions raised by this package
    """

    # get the exceptions
    from p2.framework.exceptions import (
        FrameworkError, BadResourceLocatorError
        )

    # the base exception
    try:
        # raise it
        raise FrameworkError()
    # catch it
    except FrameworkError as error:
        # all good
        pass

    # bad resource locators
    try:
        # raise it
        raise BadResourceLocatorError(uri=None, reason=None)
    # catch it
    except BadResourceLocatorError as error:
        # all good
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
