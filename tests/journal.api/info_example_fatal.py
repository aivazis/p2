#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


def test():
    """
    Exercise the j2.info channel with a realistic example
    """
    # get the journal
    import j2

    # make an j2.info channel
    channel = j2.info(name="tests.journal.info")
    # make it fatal
    channel.fatal = True
    # send the output to j2.trash
    channel.device = j2.trash()

    # add some metadata
    channel.notes["time"] = "now"

    # we asked for this to be fatal, so carefully
    try:
        # to inject something
        channel.line("info channel:")
        channel.log("    hello world!")
        # this should be unreachable
        assert False, "unreachable"
    # if all goes well
    except channel.ApplicationError:
        # all good
        pass

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
