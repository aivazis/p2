#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


def test():
    """
    Verify the channel initial state
    """
    # access the journal
    import j2

    # make a channel
    channel = j2.firewall(name="tests.journal.firewall")
    # verify the channel name
    assert channel.name == "tests.journal.firewall"
    # the verbosity should be at the default level
    assert channel.verbosity == 1
    # it should be active
    assert channel.state == True
    # and fatal
    assert channel.fatal == True

    # the page should be empty
    assert channel.page == []
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
