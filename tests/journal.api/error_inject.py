#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


def test():
    """
    Verify that we can inject simple messages correctly
    """
    # get the journal
    import j2

    # make a channel
    channel = j2.error(name="test.journal.error")
    # make it non-fatal
    channel.fatal = False
    # send the output to the trash
    channel.device = j2.trash()

    # inject
    channel.log("hello world!")

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
