#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


def test():
    """
    Verify that the device base class constructor is unavailable
    """
    # access
    import j2

    # get the global state
    chronicler = j2.chronicler

    # verify that the default device is the console
    assert chronicler.device.name == "cout"

    # make a j2.trash can
    j2.trash = j2.trash()
    # set it as the device
    chronicler.device = j2.trash
    # verify the assignment sticks
    assert chronicler.device is j2.trash
    # and that the name is correct
    assert chronicler.device.name == "trash"

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
