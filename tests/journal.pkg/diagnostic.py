#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


# diagnostic state
def test():
    """
    Exercise the diagnostic state
    """
    # and the diagnostic base class
    from j2.Diagnostic import Diagnostic

    # make one
    d1 = Diagnostic(name="test.channel")
    # verify the name was recorder correctly
    assert d1.name == "test.channel"
    # that its verbosity is set to the default value
    assert d1.verbosity == Diagnostic.verbosity
    # and that it is accessing the correct global state manager
    assert d1.chronicler is Diagnostic.chronicler

    # make another
    d3 = Diagnostic(name="test.channel", verbosity=3)
    # verify the name was recorder correctly
    assert d3.name == "test.channel"
    # that its verbosity is set to the default value
    assert d3.verbosity == 3
    # and that it is accessing the correct global state manager
    assert d3.chronicler is Diagnostic.chronicler

    # all done
    return


# main
if __name__ == "__main__":
    # prohibit the journal bindings
    journal_no_libjournal = True
    # run the test
    test()


# end of file
