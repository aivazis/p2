#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2021 all rights reserved


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
    # run the test
    test()


# end of file
