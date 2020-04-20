#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


def test():
    """
    Verify that the channel buffers get flushed properly after {log}
    """
    # get the trash can
    from j2.Trash import Trash as trash
    # and the channel
    from j2.Warning import Warning as warning

    # make a warning channel
    channel = warning(name="tests.journal.warning")
    # send the output to trash
    channel.device = trash()

    # inject
    channel.log("hello world!")

    # verify that the buffer is empty after the flush
    assert len(channel.page) == 0

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
