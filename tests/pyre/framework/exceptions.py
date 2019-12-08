#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2019 all rights reserved


"""
Tests for all the exceptions raised by this package
"""

def test():
    # get the exceptions
    from pyre.framework.exceptions import (
        FrameworkError, BadResourceLocatorError
        )

    # the base exception
    try:
        raise FrameworkError()
    except FrameworkError as error:
        pass

    # bad resource locators
    try:
        raise BadResourceLocatorError(uri=None, reason=None)
    except BadResourceLocatorError as error:
        pass

    # all done
    return


# main
if __name__ == "__main__":
    test()


# end of file
