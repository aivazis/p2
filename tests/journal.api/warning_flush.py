#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


def test():
    """
    Verify that the channel buffers get flushed properly after {log}
    """
    # get the journal
    import j2

    # make an j2.warning channel
    channel = j2.warning(name="tests.journal.warning")
    # send the output to j2.trash
    channel.device = j2.trash()

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
