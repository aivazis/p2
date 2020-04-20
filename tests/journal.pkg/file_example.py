#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


def test():
    """
    Verify that we can build a stream based device
    """
    # pick a file name
    filename = "file_example.out"
    # make a stream
    ostr = open(filename, mode="w")

    # get the package
    import j2
    # turn it into a journal device
    device = j2.stream(name=filename, stream=ostr)

    # make a debug channel
    channel = j2.debug(name="tests.journal.debug")
    # activate it
    channel.activate()
    # but send the output to trash
    channel.device = device

    # add some metadats
    channel.meta["time"] = "now"
    # inject
    channel.line("debug channel:")
    channel.log("    hello world!")

    # get os services
    import os
    # so we can remove the file
    os.unlink(filename)

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
