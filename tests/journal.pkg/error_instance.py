#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


def test():
    """
    Sanity check: verify that the channel is accessible
    """
    # get the channel
    from j2.Error import Error as error

    # make a channel
    channel = error(name="tests.journal.error")
    # verify the channel name
    assert channel.name == "tests.journal.error"
    # the verbosity should be at the default level
    assert channel.verbosity == 1
    # the channel should be active
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
    # prohibit the journal bindings
    journal_no_libjournal = True
    # run the test
    test()


# end of file
