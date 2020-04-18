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
    Exercise the channel state interface
    """
    # get the package
    from j2.Channel import Channel

    # derive a severity
    class Severity(Channel):
        # make and attach an index
        index = collections.defaultdict(Channel.disabled_type)

    # make one
    channel = Severity(name="test.channel")

    # verify its name
    assert channel.name == "test.channel"
    # its state
    assert channel.state == False
    # and again using the conversion to bool
    assert not channel

    # activate it
    channel.activate()
    # and check
    assert channel.state == True

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file