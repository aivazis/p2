#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


def test():
    """
    Verify that repeated access to the same channel does not accumulate extraneous material
    """
    # get the trash can
    from j2.Trash import Trash as trash
    # and the channel
    from j2.Firewall import Firewall as firewall

    # make a firewall channel
    channel = firewall(name="tests.journal.firewall")
    # make it non-fatal
    channel.fatal = False
    # send the output to trash
    channel.device = trash()

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
