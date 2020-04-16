#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


def test():
    """
    Sanity check: verify that the channel is accessible
    """
    # access the journal
    import j2

    # make a info channel
    channel = j2.info(name="tests.journal.info")
    # but send the output to trash
    channel.device = j2.trash()

    # inject
    channel.log("hello world!")

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
