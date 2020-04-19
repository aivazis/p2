#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


def test():
    """
    Verify that message injection is handled properly
    """
    # access the journal
    import j2

    # make a firewall channel
    channel = j2.firewall(name="tests.journal.firewall")
    # send the output to trash
    channel.device = j2.trash()
    # make the firewall non-fatal
    channel.fatal = False

    # inject
    channel.log("hello world!")

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file