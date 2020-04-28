#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


def test():
    """
    Verify that we can inject into a stream based device
    """
    # pick a file name
    filename = "file_example.out"
    # make a stream
    ostr = open(filename, mode="w")

    # get the device
    from j2.Stream import Stream as stream
    # and a channel
    from j2.Debug import Debug as debug

    # instantiate
    device = stream(name=filename, stream=ostr)

    # make a debug channel
    channel = debug(name="tests.journal.debug")
    # activate it
    channel.activate()
    # send the output to the file
    channel.device = device

    # add some metadats
    channel.notes["time"] = "now"
    # inject
    channel.line("debug channel:")
    channel.log("    hello world!")

    # close the stream; not strictly necessary, but let's exercise the interface
    device.close()

    # all done
    return


# main
if __name__ == "__main__":
    # prohibit the journal bindings
    journal_no_libjournal = True
    # run the test
    test()


# end of file
