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
    assert channel.name == "test.channel"
    # check that it is read-only
    try:
        # by attempting to modify
        channel.name = "foo"
        # hence, we can't get here
        assert False, "unreachable"
    # if all goes well
    except AttributeError as error:
        # no problem
        pass

    # verify its verbosity is at 1 by default
    assert channel.verbosity == 1
    # that it can be modified
    channel.verbosity = 5
    # and the assignment sticks
    assert channel.verbosity == 5

    # verify its state is off by default
    assert channel.state is False
    # that it can be modified
    channel.state = True
    # and the assignment sticks
    assert channel.state is True

    # verify that the accessible device is the console
    assert channel.device.name == "cout"
    # make a trash can
    trash = libjournal.Trash()
    # register it as the device
    channel.device = trash
    # and verify that the assignment sticks
    assert channel.device is trash
    # check the name
    assert channel.device.name == "trash"

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
