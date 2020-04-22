#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


def test():
    """
    Verify that channels with the same name have common state
    """
    # access
    from j2 import libjournal

    # make a channel
    ch_1 = libjournal.Debug("test.channel")
    # activate it
    ch_1.activate()

    # make another
    ch_2 = libjournal.Debug("test.channel")
    # verify it is active
    assert ch_2.state == True
    # deactivate it
    ch_2.deactivate()

    # verify that both channels are now inactive
    assert ch_1.state == False
    assert ch_2.state == False

    # and once again, using {__bool__}
    assert bool(ch_1) == False
    assert bool(ch_2) == False

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
