#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


def test():
    """
    Verify that the dashboard registrar is an instance of the component registrar
    """
    # access the registrar
    from p2.components.Registrar import Registrar
    # and the dashboard
    from p2.framework.Dashboard import Dashboard

    # instantiate the dashboard
    dashboard = Dashboard()
    # verify the {registrar} attribute is an instance of the component registrar
    assert isinstance(dashboard.registrar, Registrar)

    # all done
    return dashboard


# main
if __name__ == "__main__":
    # skip pyre initialization since we don't rely on the executive
    pyre_noboot = True
    # run the test
    test()


# end of file
