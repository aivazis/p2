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
    from j2.Warning import Warning as warning

    # make a channel
    channel = warning(name="tests.journal.warning")
    # verify the channel name
    assert channel.name == "tests.journal.warning"
    # the verbosity should be at the default level
    assert channel.verbosity == 1
    # the channel should be active
    assert channel.active == True
    # the page should be empty
    assert channel.page == []
    # verify the metadata
    assert channel.notes["application"] == "journal"
    assert channel.notes["channel"] == channel.name
    assert channel.notes["severity"] == channel.severity

    # all done
    return


# main
if __name__ == "__main__":
    # prohibit the journal bindings
    journal_no_libjournal = True
    # run the test
    test()


# end of file
