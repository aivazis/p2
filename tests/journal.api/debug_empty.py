#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


def test():
    """
    Verify that empty messages are injected correctly
    """
    # get the channel
    import j2

    # make a channel
    channel = j2.debug(name="test.journal.debug")
    # activate it
    channel.activate()

    # inject an empty message
    channel.log()

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
