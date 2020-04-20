#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


def test():
    """
    Exercise the error channel with a realistic example
    """
    # get the trash can
    from j2.Trash import Trash as trash
    # and the channel
    from j2.Error import Error as error

    # make an error channel
    channel = error(name="tests.journal.error")
    # send the output to trash
    channel.device = trash()

    # add some metadats
    channel.meta["time"] = "now"
    # inject
    channel.line("error channel:")
    channel.log("    hello world!")

    # all done
    return


# main
if __name__ == "__main__":
    # prohibit the journal bindings
    journal_no_libjournal = True
    # run the test
    test()


# end of file
