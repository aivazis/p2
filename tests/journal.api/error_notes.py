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
    import j2

    # make a error channel
    channel = j2.error("test.channel")
    # get its metadata
    notes = channel.notes
    # adjust the application name
    notes["application"] = "error_meta"
    # add something
    notes["author"] = "michael"

    # make sure the adjustments stick by getting the value once again
    notes = channel.notes
    # and comparing against expectations
    assert notes["application"] == "error_meta"
    assert notes["author"] == "michael"
    assert notes["channel"] == "test.channel"
    assert notes["severity"] == "error"

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
