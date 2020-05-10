#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


def test():
    """
    Verify that the channel wide defaults are as expected
    """
    # access
    import j2

    # verify that debug channels are inactive by default
    assert j2.debug.defaultActive == False
    # and non-fatal
    assert j2.debug.defaultFatal == False
    # verify that the channel default device is not set
    assert j2.debug.defaultDevice == None

    # make a trash can
    trash = j2.trash()
    # make it the default device
    j2.debug.defaultDevice = trash
    # and make sure the assignment sticks
    assert j2.debug.defaultDevice is trash

    # make a debug channel
    channel = j2.debug("test.channel")
    # verify that its view of its default state is consistent
    assert channel.defaultActive == j2.debug.defaultActive
    assert channel.defaultFatal == j2.debug.defaultFatal
    # similarly for the default device
    assert channel.defaultDevice == j2.debug.defaultDevice

    # and now, the instance state
    assert channel.active == channel.defaultActive
    assert channel.fatal == channel.defaultFatal
    assert channel.device == channel.defaultDevice

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
