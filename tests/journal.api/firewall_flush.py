#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


def test():
    """
    Verify that channels lower in the hierarchy inherit their parent default state
    """
    # get the journal
    import j2

    # make a channel
    channel = j2.firewall(name="test.journal.firewall")
    # send the output to j2.trash
    channel.device = j2.trash()

    # carefully
    try:
        # inject
        channel.log("hello world!")
        # shouldn't get here
        assert False, "unreachable"
    # if the correct exception was raised
    except channel.FirewallError as error:
        # no problem
        pass

    # verify that the buffer is empty after the flush
    assert len(channel.page) == 0

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
