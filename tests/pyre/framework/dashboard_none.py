#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


def test():
    """
    Sanity test: make sure the dashboard singleton is accessible
    """
    # access
    import p2
    # verify that we registered a null dashboard correctly
    assert p2.dashboard is None
    # all done
    return


# main
if __name__ == "__main__":
    # ask the framework to not build a dashboard, therefore skip the boot phase
    pyre_dashboard = None
    # do...
    test()


# end of file
