#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2022 all rights reserved


def test():
    """
    Redirect a {debug} session to our custom device
    """
    # access the package
    import jcdev
    # get the journal
    import journal

    # open a file
    stream = open("debug_example.csv", mode="w")
    # instantiate the custom device
    device = jcdev.device(stream=stream)

    # attach the device as the global default
    journal.chronicler.device = device

    # make a channel and activate it
    debug = journal.debug("jcdev.debug").activate()
    # say something
    debug.log("hello from jcdev!")

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
