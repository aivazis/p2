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

    # make an index
    index = Index(Channel.enabled_type)

    # look up a name
    inventory = index.lookup(name="test.index")

    # verify it is an instance of the correct class
    assert isinstance(inventory, Channel.enabled_type)
    # hence the state is on
    assert inventory.state is True
    # and the device is null
    assert inventory.device is None

    # all done
    return


# main
if __name__ == "__main__":
    # prohibit the journal bindings
    journal_no_libjournal = True
    # run the test
    test()


# end of file
