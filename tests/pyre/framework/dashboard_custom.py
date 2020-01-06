#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


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
    Sanity test: make sure the dashboard singleton is accessible
    """
    # access
    import p2
    # verify that the registered dashboard is the one we built
    assert p2.dashboard.custom is True
    # all done
    return


# main
if __name__ == "__main__":
    # skip pyre initialization since we don't rely on the executive
    pyre_dashboard = dashboard
    # do...
    test()


# end of file
