#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


def test():
    """
    Suppress all journal output
    """
    # get the journal
    import j2

    # suppress all outpuut
    j2.quiet()

    # make a channel
    channel = j2.debug(name="tests.journal.debug")
    # activate it
    channel.activate()

    # add some metadata
    channel.notes["time"] = "now"
    # inject
    channel.line("debug channel:")
    channel.log("    hello world!")

    # all done
    return


# main
if __name__ == "__main__":
    # prohibit the journal bindings
    journal_no_libjournal = True
    # run the test
    test()


# end of file
