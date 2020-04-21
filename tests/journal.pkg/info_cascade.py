#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


def test():
    """
    Verify that we can look up channel names and retrieve the associated inventory
    """
    # get the channel
    from j2.Informational import Informational
    # the chronicler
    from j2.Chronicler import Chronicler
    # and the trash can
    from j2.Trash import Trash

    # make a channel
    parent = Informational(name="test.index.parent")
    # verify that the state is on
    assert parent.state is True
    # and the device is at the default value
    assert parent.device is Chronicler().device

    # activate it
    parent.state = True
    # and set the device to a trash can
    parent.device = Trash()

    # lookup a name that is lower in the hierarchy
    child = Informational(name="test.index.parent.blah.blah.child")
    # that it's state is the same as the parent
    assert child.state == parent.state
    # and that it inherited the device correctly
    assert child.device is parent.device

    # all done
    return


# main
if __name__ == "__main__":
    # prohibit the journal bindings
    journal_no_libjournal = True
    # run the test
    test()


# end of file
