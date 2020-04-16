#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


def test():
    """
    Check a few of the canonical X11 color names
    """
    # access the color map
    from j2.ANSI import ANSI

    # ask for a very strange color name
    assert ANSI.x11("a-very-unlikely-color-name") == ""

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
