#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


def test():
    """
    Verify that repeated access to the same channel does not accumulate extraneous material
    """
    # access the journal
    import j2

    # make a firewall channel
    channel = j2.firewall(name="tests.journal.firewall")
    # make it non-fatal
    channel.fatal = False
    # send the output to trash
    channel.device = j2.trash()

    # a few times
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
