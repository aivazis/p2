#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


def test():
    """
    Verify that content is flushed correctly when the same channel instance is used multiple times
    """
    # get the journal
    import j2

    # make a channel
    channel = j2.debug(name="test.journal.debug")
    # activate it
    channel.activate()
    # but send the output to the trash
    channel.device = j2.trash()

    # for a few times
    for _ in range(10):
        # inject
        channel.log("hello world!")

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
