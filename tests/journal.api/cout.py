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

    # make a j2.trash can
    console = j2.cout()
    # verify its name is what we expect
    assert console.name == "cout"

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file