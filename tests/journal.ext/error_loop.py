#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


def test():
    """
    Verify that channels lower in the hierarchy inherit their parent default state
    """
    # get the channel
    from j2.ext.j2 import Error as error
    # and the trash can
    from j2.ext.j2 import Trash as trash

    # make a channel
    channel = error(name="test.journal.error")
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
