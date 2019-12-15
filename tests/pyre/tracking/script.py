#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2019 all rights reserved


def script():
    """
    Verify that the script locator returns the correct location tag
    """
    # get the package
    import p2.tracking

    # make a locator
    locator = p2.tracking.script(source=__file__, function="script", line=16)
    # verify the display
    assert str(locator) == f"file='{__file__}', line=16, function='script'"

    # all done
    return locator


# main
if __name__ == "__main__":
    # skip pyre initialization since we don't rely on the executive
    pyre_noboot = True
    # do...
    script()


# end of file
