#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2021 all rights reserved


def test():
    """
    Verify that we can disable the dashboard
    """
    # access
    import p2
    # verify that we registered a null dashboard correctly
    assert p2.dashboard is None
    # and that the singleton factory
    from p2.framework.Dashboard import Dashboard
    # has been updated correctly
    assert Dashboard() is None
    # all done
    return


# main
if __name__ == "__main__":
    # ask the framework to not build a dashboard, therefore skip the boot phase
    pyre_dashboard = None
    # do...
    test()


# end of file
