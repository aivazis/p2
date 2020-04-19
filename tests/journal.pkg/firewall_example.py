#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


def test():
    """
    Exercise the firewall channel with a realistic example
    """
    # access the journal
    import j2

    # make a firewall channel
    channel = j2.firewall(name="tests.journal.firewall")
    # send the output to trash
    channel.device = j2.trash()

    # add some metadats
    channel.meta["time"] = "now"

    # carefully
    try:
        # inject
        channel.line("firewall:")
        channel.log("    a nasty bug was detected")
        # shouldn't get here
        assert False, "unreachable"
    # if the correct exception was raised
    except channel.FirewallError as error:
        # verify that the description is correct
        assert str(error) == (
            f"file='{__file__}', line=27, function='test': "
            "firewall breached; aborting..."
            )

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
