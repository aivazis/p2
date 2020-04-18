#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


# channels with the same name share state
def test():
    """
    Verify that channels with the same name share state
    """
    # get the package
    from j2.Channel import Channel

    # derive a severity
    class Severity(Channel, inventory_type=Channel.disabled_type):
        """
        A sample derivation
        """

    # make one
    channel_1 = Severity(name="test.channel")
    # verify its name
    assert channel_1.name == "test.channel"
    # its state
    assert channel_1.state == False
    # and again using the conversion to bool
    assert not channel_1

    # activate it
    channel_1.activate()
    # and check
    assert channel_1.state == True

    # make another channel by the same name
    channel_2 = Severity(name="test.channel")
    # verify the name
    assert channel_2.name == "test.channel"
    # verify it's on
    assert channel_2.state == True

    # deactivate it
    channel_2.state = False
    # verify
    assert channel_2.state == False
    # and that the new state is mirrored by channel_1
    assert channel_1.state == False

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
