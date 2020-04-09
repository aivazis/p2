#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


def test():
    """
    Verify the default value for the  debug channel shared state
    """
    # access
    from j2 import libjournal

    # make a debug channel
    channel = libjournal.Debug("test.channel")

    # verify its name
    assert channel.name() == "test.channel"
    # verify that the accessible device is the console
    assert channel.device().name() == "cout"
    # verify that it is inactive
    assert channel.state() == False
    # verify that the accessible device is the console
    assert channel.device().name() == "cout"

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
