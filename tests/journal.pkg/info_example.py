#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


def test():
    """
    Exercise the info channel with a realistic example
    """
    # access the journal
    import j2

    # make a info channel
    channel = j2.info(name="tests.journal.info")
    # but send the output to trash
    channel.device = j2.trash()

    # add some metadats
    channel.meta["time"] = "now"
    # inject
    channel.line("info channel:")
    channel.log("    hello world!")

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
