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
    from j2.ext.j2 import Debug as debug
    # and the trash can
    from j2.ext.j2 import Trash as trash

    # make a channel
    channel = debug(name="test.journal.debug")
    # activate it
    channel.activate()
    # but send the output to trash
    channel.device = trash()

    # inject
    channel.log("hello world!")

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
