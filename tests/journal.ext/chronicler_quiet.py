#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


def test():
    """
    Verify that we can suppress all journal output
    """
    # get the chronicler
    from j2.ext.j2 import Chronicler as chronicler
    # get the channel
    from j2.ext.j2 import Debug as debug

    # quiet all channels
    chronicler.quiet()

    # make a channel
    channel = debug(name="test.journal.debug")
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
    # run the test
    test()


# end of file
