#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


# channel state interface
def test():
    """
    Exercise the channel state interface
    """
    # get the package
    from j2.Channel import Channel

    # derive a severity
    class Severity(Channel, inventory_type=Channel.disabled_type):
        """
        A sample derivation
        """

    # make one
    channel = Severity(name="test.channel")

    # verify its name
    assert channel.name == "test.channel"
    # its state
    assert channel.state == False
    # and again using the conversion to bool
    assert not channel

    # activate it
    channel.activate()
    # and check
    assert channel.state == True

    # all done
    return


# main
if __name__ == "__main__":
    # prohibit the journal bindings
    journal_no_libjournal = True
    # run the test
    test()


# end of file
