#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


# make sure the injection interface works as expected
def test():
    """
    Exercise the diagnostic state
    """
    # get the package
    import j2
    # the diagnostic base class
    from j2.Diagnostic import Diagnostic
    # and the global state manager
    chronicler = j2.chronicler()

    # make one
    d1 = Diagnostic(name="test.channel")

    # build a message
    d1.line("hello world!")
    d1.log()

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file