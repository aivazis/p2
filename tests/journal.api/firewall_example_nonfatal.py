#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


def test():
    """
    Exercise the firewall channel with a realistic example
    """
    # get the journal
    import j2

    # make a firewall channel
    channel = j2.firewall(name="tests.journal.firewall")
    # make it non-fatal
    channel.fatal = False
    # send the output to j2.trash
    channel.device = j2.trash()

    # add some metadata
    channel.notes["time"] = "now"

    # carefully
    try:
        # inject
        channel.line("firewall:")
        channel.log("    a nasty bug was detected")
    # if the correct exception was raised
    except channel.FirewallError as error:
        # shouldn't get here
        assert False, "unreachable"

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file