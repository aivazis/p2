#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


# externals
import collections  # for {defaultdict}


# channel state interface
def test():
    """
    Verify that all channel instances have access to the same index
    """
    # get the package
    from j2.Channel import Channel
    # the base class has no index, so make one
    index = collections.defaultdict(Channel.disabled_type)
    # and attach it
    Channel.index = index

    # make a couple of channels
    channel_1 = Channel(name="test.channel_1")
    channel_2 = Channel(name="test.channel_2")

    # get the index through the first channel
    index_1 = channel_1.index
    # verify it has exactly two channels
    assert len(index_1) == 2
    # one of them is the name of {channel_1}
    assert channel_1.name in index_1
    # and the other is the name of {channel_2}
    assert channel_2.name in index_1

    # repeat, through the second channel
    index_2 = channel_1.index
    # verify it has exactly two channels
    assert len(index_2) == 2
    # one of them is the name of {channel_1}
    assert channel_1.name in index_2
    # and the other is the name of {channel_2}
    assert channel_2.name in index_2

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
