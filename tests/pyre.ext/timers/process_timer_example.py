#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


def test():
    """
    Sanity test: make sure the timer bindings are accessible
    """
    # access the timer bindings
    import p2.ext.p2 as libpyre

    # make a timer
    t = libpyre.ProcessTimer(name="tests.timer")
    # start it
    t.start()

    # do something
    s = sum(range(10**6))

    # stop the timer
    t.stop()

    # get the journal
    import journal
    # make a channel
    channel = journal.debug(name="pyre.timers")
    # activate it
    # channel.activate()
    # log the elapsed time
    channel.log(f"elapsded: {t.ms()}")

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
