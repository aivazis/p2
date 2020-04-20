#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


def test():
    """
    Verify that empty log messages get handled properly
    """
    # get the trash can
    from j2.Trash import Trash as trash
    # and the channel
    from j2.Firewall import Firewall as firewall

    # make a firewall
    channel = firewall(name="tests.journal.firewall")
    # send the output to trash
    channel.device = trash()

    # carefully
    try:
        # inject an empty message
        channel.log()
        # shouldn't get here
        assert False, "unreachable"
    # if the correct exception was raised
    except channel.FirewallError as error:
        # all good
        pass

    # all done
    return


# main
if __name__ == "__main__":
    # prohibit the journal bindings
    journal_no_libjournal = True
    # run the test
    test()


# end of file
