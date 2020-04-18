#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


# externals
import collections  # for {defaultdict}


# verify that the default channel state is as expected
def test():
    """
    Exercise the default channel state
    """
    # get the package
    from j2.Channel import Channel
    # the base class has no index, so make one
    index = collections.defaultdict(Channel.disabled_type)
    # and attach it
    Channel.index = index

    # make one
    channel = Channel(name="test.channel")

    # get its inventory
    inventory = channel.inventory
    # verify that it is disabled
    assert inventory.state == False
    # and that it has no registered device
    assert inventory.device == None

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
