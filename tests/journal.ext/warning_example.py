#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


def test():
    """
    Exercise the warning channel with a realistic example
    """
    # get the trash can
    from j2.ext.j2 import Trash as trash
    # and the channel
    from j2.ext.j2 import Warning as warning

    # make an warning channel
    channel = warning(name="tests.journal.warning")
    # send the output to trash
    channel.device = trash()

    # add some metadata
    channel.notes["time"] = "now"
    # inject
    channel.line("warning channel:")
    channel.log("    hello world!")

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file