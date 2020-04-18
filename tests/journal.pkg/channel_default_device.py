#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


# verify that we can control the default device
def test():
    """
    Verify that we can control the default device
    """
    # the package
    import j2
    # get the channel
    from j2.Channel import Channel

    # ask it of the default device
    builtin = Channel.getDefaultDevice()

    # make new device
    custom = j2.trash()
    # install it
    old = Channel.setDefaultDevice(device=custom)

    # check that the default device is what we just installed
    assert Channel.getDefaultDevice() is custom
    # and the device we just replaced was the original built-in one
    assert old is builtin

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
