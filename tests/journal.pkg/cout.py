#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


def test():
    """
    Verify that we can access the {cout} console
    """
    # get the pakcage
    import j2

    # instantiate and verify the name
    assert j2.cout().name == "cout"

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
