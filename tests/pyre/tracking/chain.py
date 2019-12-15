#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2019 all rights reserved


def test():
    """
    Verify that locators can be chained correctly
    """
    # get the package
    import p2.tracking

    # make two locators
    first = p2.tracking.simple(source="first")
    second = p2.tracking.simple(source="second")
    # chain them together
    chain = p2.tracking.chain(this=first, next=second)
    # verify the display
    assert str(chain) == "first, second"

    # all done
    return chain


# main
if __name__ == "__main__":
    # skip pyre initialization since we don't rely on the executive
    pyre_noboot = True
    # do...
    test()


# end of file
