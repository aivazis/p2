#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2022 all rights reserved


def test():
    """
    Verify that the protocol family name is recorded and used correctly
    """
    # the protocol superclass
    from p2.components.Protocol import Protocol
    # and the dashboard
    from p2.framework.Dashboard import Dashboard

    # get the dashboard
    dashboard = Dashboard()
    # ask it for the protocol registrar
    registrar = dashboard.registrar

    # verify that {Protocol} was registered
    assert Protocol in registrar.protocols
    # there should be no implementers
    assert registrar.implementers[Protocol] == set()


    # a protocol
    class Private(Protocol):
        """
        A private protocol
        """

    # verify that {Public} was registered
    assert Private in registrar.protocols
    # there should be no implementers
    assert registrar.implementers[Private] == set()


    # another protocol
    class Public(Protocol, family="tests.protocols.public"):
        """
        A public protocol
        """

    # verify that {Public} was registered
    assert Public in registrar.protocols
    # there should be no implementers
    assert registrar.implementers[Public] == set()

    # all done
    return Private, Public


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
