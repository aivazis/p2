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
    from j2.Firewall import Firewall
    # and the trash can
    from j2.Trash import Trash

    # make a channel
    parent = Firewall(name="test.index.parent")
    # verify that the state is on
    assert parent.state is True
    # it is fatal
    assert parent.fatal is True
    # and the device is at the default value
    assert parent.device is Firewall.chronicler.device

    # activate it
    parent.state = True
    # make it non-fatal
    parent.fatal = False
    # and set the device to a trash can
    parent.device = Trash()

    # lookup a name that is lower in the hierarchy
    child = Firewall(name="test.index.parent.blah.blah.child")
    # that it's state is the same as the parent
    assert child.state == parent.state
    assert child.fatal == parent.fatal
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
