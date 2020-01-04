#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


def script():
    """
    Verify that the simple locator returns the correct location tag
    """
    # access the package
    import p2.tracking

    # make a locator
    locator = p2.tracking.simple(source="simple")
    # verify the display
    assert str(locator) == "simple"

    # all done
    return locator


# main
if __name__ == "__main__":
    # skip pyre initialization since we don't rely on the executive
    pyre_noboot = True
    # do...
    script()


# end of file
