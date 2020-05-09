#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


def test():
    """
    Verify that the warning channel wide defaults are as expected
    """
    # access
    from j2 import libjournal

    # verify that warning channels are inactive by default
    assert libjournal.Warning.defaultActive == True
    # and non-fatal
    assert libjournal.Warning.defaultFatal == False
    # verify that the channel default device is not set
    assert libjournal.Warning.defaultDevice == None

    # make a trash can
    trash = libjournal.Trash()
    # make it the default device
    libjournal.Warning.defaultDevice = trash
    # and make sure the assignment sticks
    assert libjournal.Warning.defaultDevice is trash

    # make a warning channel
    channel = libjournal.Warning("test.channel")
    # verify that its view of its default state is consistent
    assert channel.defaultActive == libjournal.Warning.defaultActive
    assert channel.defaultFatal == libjournal.Warning.defaultFatal
    # similarly for the default device
    assert channel.defaultDevice == libjournal.Warning.defaultDevice

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