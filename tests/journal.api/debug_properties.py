#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


def test():
    """
    Verify access to the channel properties
    """
    # access
    import j2

    # make a debug channel
    channel = j2.debug("test.channel")

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

    # verify its activation state is off by default
    assert channel.active is False
    # that it can be modified
    channel.active = True
    # and the assignment sticks
    assert channel.active is True

    # verify its not fatal
    assert channel.fatal is False
    # that it can be modified
    channel.fatal = True
    # and the assignment sticks
    assert channel.fatal is True

    # verify that the accessible device is the console
    assert channel.device.name == "cout"
    # make a j2.trash can
    j2.trash = j2.trash()
    # register it as the device
    channel.device = j2.trash
    # and verify that the assignment sticks
    assert channel.device is j2.trash
    # check the name
    assert channel.device.name == "trash"
    # and verify that it's different from the default device held by the class
    assert channel.device is not channel.defaultDevice

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file