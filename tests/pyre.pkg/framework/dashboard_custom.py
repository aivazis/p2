#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2021 all rights reserved


def dashboard():
    """
    A factory for the framework dashboard
    """
    # the nastiest case is to ask the framework for its own after we told it not to do anything
    from p2.framework.Dashboard import Dashboard
    # instantiate
    dashboard = Dashboard()
    # decorate
    dashboard.custom = True
    # and return it
    return dashboard


def test():
    """
    Verify we can install a custom dashboard correctly
    """
    # access
    import p2
    # verify that the registered dashboard is the one we built
    assert p2.dashboard.custom is True

    # now, get the singleton
    from p2.framework.Dashboard import Dashboard
    # and verify that the instance it returns is our custom dashboard
    assert p2.dashboard is Dashboard()
    # all done
    return


# main
if __name__ == "__main__":
    # set a custom dashboard
    pyre_dashboard = dashboard
    # do...
    test()


# end of file
