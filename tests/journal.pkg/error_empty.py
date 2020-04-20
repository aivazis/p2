#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


def test():
    """
    Verify that empty log messages get handled properly
    """
    # access the journal
    import j2

    # make an error channel
    channel = j2.error(name="tests.journal.error")
    # send the output to trash
    channel.device = j2.trash()

    # inject
    channel.log()

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
