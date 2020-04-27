#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


def test():
    """
    Verify the channel initial state
    """
    # access
    from j2.ext.j2 import Debug as debug

    # make a channel
    channel = debug(name="tests.journal.debug")
    # verify the channel name
    assert channel.name == "tests.journal.debug"
    # the verbosity should be at the default level
    assert channel.verbosity == 1
    # the channel should be inactive
    assert channel.state == False
    # the page should be empty
    assert tuple(channel.page) == ()
    # verify the metadata
    assert channel.meta["application"] == "journal"
    assert channel.meta["channel"] == channel.name
    assert channel.meta["severity"] == channel.severity

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file