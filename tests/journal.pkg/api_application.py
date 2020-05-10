#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


def test():
    """
    Verify that channels lower in the hierarchy inherit their parent default state
    """
    # get the library
    import j2

    # make up a name
    name = "app"
    # register it
    j2.application(name)

    # get the chronicler's notes
    notes = j2.chronicler.notes
    # verify that the key is registered and has the correct value
    assert notes["application"] == name

    # all done
    return


# main
if __name__ == "__main__":
    # prohibit the journal bindings
    journal_no_libjournal = True
    # run the test
    test()


# end of file
