#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


def test():
    """
    Sanity test: make sure the timer bindings are accessible
    """
    # access the timer bindings
    import p2.ext.p2 as libpyre

    # make a timer
    t = libpyre.WallTimer(name="tests.timer")
    # verify its name
    assert t.name == "tests.timer"

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
