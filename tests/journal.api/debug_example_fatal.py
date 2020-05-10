#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


def test():
    """
    Exercise a channel with a realistic example when the channel is fatal
    """
    # the journal
    import j2

    # make a channel
    channel = j2.debug(name="tests.journal.debug")
    # activate it
    channel.active = True
    # make it fatal
    channel.fatal = True
    # but send the output to the trash
    channel.device = j2.trash()

    # add some metadata
    channel.notes["time"] = "now"

    # we asked for this to be fatal, so carefully
    try:
        # inject something
        channel.line("debug channel:")
        channel.log("    hello world!")
        # this should be unreachable
        assert False, "unreachable"
    # if all goes well, the channel raised an error
    except channel.DebugError:
        # all good
        pass

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
