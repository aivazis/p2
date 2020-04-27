#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


def test():
    """
    Verify that channels lower in the hierarchy inherit their parent default state
    """
    # get the channel
    from j2.ext.j2 import Debug
    # and the trash can
    from j2.ext.j2 import Trash

    # make a channel
    parent = Debug(name="test.index.parent")
    # verify that the state is off
    assert parent.state is False
    # and the device is at the default value
    assert parent.device is parent.chronicler.device

    # activate it
    parent.state = True
    # and set the device to a trash can
    parent.device = Trash()

    # lookup a name that is lower in the hierarchy
    child = Debug(name="test.index.parent.blah.blah.child")
    # that it's state is the same as the parent
    assert child.state == parent.state
    # and that it inherited the device correctly
    assert child.device is parent.device

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file