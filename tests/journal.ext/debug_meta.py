#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


def test():
    """
    Verify access to the channel metadata
    """
    # access
    from j2 import libjournal

    # make a debug channel
    channel = libjournal.Debug("test.channel")
    # get its metadata
    meta = channel.meta
    # adjust the application name
    meta["application"] = "debug_meta"
    # add something
    meta["author"] = "michael"

    # make sure the adjustments stick by getting the value once again
    meta = channel.meta
    # and comparing against expectations
    assert meta["application"] == "debug_meta"
    assert meta["author"] == "michael"
    assert meta["channel"] == "test.channel"
    assert meta["severity"] == "debug"

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
