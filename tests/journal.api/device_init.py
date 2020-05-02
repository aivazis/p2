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

    # attempt to
    try:
        # access the device base class
        j2.Device()
        # which is not Published
        assert False, "unreachable"
    # if it fails
    except AttributeError:
        # all good
        pass

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
