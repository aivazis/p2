#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


def test():
    """
    Verify that message injection is handled properly
    """
    # get the channel
    from j2.Null import Null as null
    # and the trash can
    from j2.Trash import Trash as trash

    # make a null channel
    channel = null(name="tests.journal.null")
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
