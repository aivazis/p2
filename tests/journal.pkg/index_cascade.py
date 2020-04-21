#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


def test():
    """
    Verify that we can look up channel names and retrieve the associated inventory
    """
    # access the index
    from j2.Index import Index
    # get the channel so we can use the embedded inventory types
    from j2.Channel import Channel
    # get the trash can
    from j2.Trash import Trash

    # decide on the inventory type
    inventory_type = Channel.enabled_fatal_type
    # make an index
    index = Index(inventory_type)

    # look up a name
    parent = index.lookup(name="test.index.parent")
    # verify it is an instance of the correct class
    assert isinstance(parent, inventory_type)
    # hence the state is on
    assert parent.state is True
    # it is fatal
    assert parent.fatal is True
    # and the device is null
    assert parent.device is None

    # deactivate it
    parent.state = False
    # make it non-fatal
    parent.fatal = False
    # and set the device to a trash can
    parent.device = Trash()

    # lookup a name that is lower in the hierarchy
    child = index.lookup(name="test.index.parent.blah.blah.child")
    # make sure it's an instance of the correct type
    assert isinstance(child, inventory_type)
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
