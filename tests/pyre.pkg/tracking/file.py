#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2022 all rights reserved


def test():
    """
    Verify that the file locator returns the correct location tag
    """
    # access the package
    import p2.tracking

    # make a locator
    locator = p2.tracking.file(source="script.py", line=16, column=2)
    # verify the display
    assert str(locator) == "file='script.py', line=16, column=2"

    # all done
    return locator


# main
if __name__ == "__main__":
    # do...
    test()


# end of file
