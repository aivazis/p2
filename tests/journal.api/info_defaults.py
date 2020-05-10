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

    # verify that info channels are active by default
    assert j2.info.defaultActive == True
    # and non-fatal
    assert j2.info.defaultFatal == False
    # verify that the channel default device is not set
    assert j2.info.defaultDevice == None

    # make a trash can
    trash = j2.trash()
    # make it the default device
    j2.info.defaultDevice = trash
    # and make sure the assignment sticks
    assert j2.info.defaultDevice is trash

    # make a channel
    channel = j2.info("test.channel")
    # verify that its view of its default state is consistent
    assert channel.defaultActive == j2.info.defaultActive
    assert channel.defaultFatal == j2.info.defaultFatal
    # similarly for the default device
    assert channel.defaultDevice == j2.info.defaultDevice

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
