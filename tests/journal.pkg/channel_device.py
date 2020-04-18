#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


# externals
import collections  # for {defaultdict}


# access to instance specific devices
def test():
    """
    Verify that channel instances get their devices from the same source, and that there is no
    crosstalk when setting a channel specific device
    """
    # get the package
    import j2
    # and the channel
    from j2.Channel import Channel
    # the base class has no index, so make one
    index = collections.defaultdict(Channel.disabled_type)
    # and attach it
    Channel.index = index

    # make a trash can
    trash = j2.trash()

    # ask the chronicler for its device
    default = j2.chronicler().device

    # make a couple of channels
    channel_1 = Channel("journal.tests.channel_1")
    channel_2 = Channel("journal.tests.channel_2")

    # verify that their device is currently what chronicler provides
    assert channel_1.device is default
    assert channel_2.device is default

    # set the channel wide default
    Channel.setDefaultDevice(trash)
    # and ask for it back
    shared = Channel.getDefaultDevice()
    # verify that that's what the two channel see now
    assert channel_1.device is shared
    assert channel_2.device is shared

    # set the channel specific devices to different values
    channel_1.device = j2.trash()
    channel_2.device = j2.trash()
    # verify the devices are now different
    assert channel_1.device is not channel_2.device

    # make a new channel that shares state with {channel_1}
    channel_10 = Channel("journal.tests.channel_1")
    # verify it has the same device
    assert channel_10.device is channel_1.device

    # make a new channel that shares state with {channel_2}
    channel_20 = Channel("journal.tests.channel_2")
    # verify it has the same device
    assert channel_20.device is channel_2.device

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
