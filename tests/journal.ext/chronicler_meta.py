#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


def test():
    """
    Verify that the device base class constructor is unavailable
    """
    # access
    from j2 import libjournal

    # get the global state
    chronicler = libjournal.Chronicler

    # ask for the global metadata
    meta = chronicler.meta
    # adjust the application name
    meta["application"] = "chronicler"
    # and add some
    meta["author"] = "michael"

    # now, make a channel
    channel = libjournal.Debug(name="tests.journal.chronicler")
    # ask for its metadata
    meta = channel.meta
    # which must include the global settings above
    assert meta["application"] == "chronicler"
    assert meta["author"] == "michael"
    assert meta["channel"] == "tests.journal.chronicler"
    assert meta["severity"] == "debug"

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
