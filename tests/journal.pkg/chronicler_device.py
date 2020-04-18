#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


# access to the global device
def test():
    """
    Exercise getting/setting the global device
    """
    # get the package
    import j2

    # get the manager of the global state
    chronicler = j2.chronicler()

    # make a new device
    trash = j2.trash()
    # install it
    chronicler.device = trash

    # verify that it was installed correctly
    assert chronicler.device is trash

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
