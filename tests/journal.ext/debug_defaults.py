#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


def test():
    """
    Verify that the debug channel wide defaults are as expected
    """
    # access
    from j2 import libjournal

    # make a debug channel
    channel = libjournal.Debug("test.channel")

    # verify that debug channels are inactive by default
    assert channel.defaultState() == False
    # verify that the chanel default device is not set
    assert channel.defaultDevice() == None

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
