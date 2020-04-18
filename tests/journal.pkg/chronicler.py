#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


# the journal global state
def test():
    """
    Verify the default global settings
    """
    # get the package
    import j2

    # get the manager of the global state
    chronicler = j2.chronicler()

    # ask it for its metadata
    meta = chronicler.meta
    # verify that the table comes with only one setting
    assert len(meta) == 1
    # that is the default application name
    assert meta["application"] == "journal"

    # get the default device
    device = chronicler.device
    # verify it's an instance of {cout}
    assert isinstance(device, j2.cout)
    # and that it is named correctly
    assert device.name == "cout"

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
