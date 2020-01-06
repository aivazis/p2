#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


def test():
    """
    Verify that the implementation specifications of components are created correctly when
    there is an explicit protocol specifies
    """
    # configurable
    from p2.components.Configurable import Configurable
    # component
    from p2.components.Component import Component
    # protocol
    from p2.components.Protocol import Protocol
    # the dashboard
    from p2.framework.Dashboard import Dashboard

    # get the dashboard
    dashboard = Dashboard()
    # and the component registrar
    registrar = dashboard.registrar


    # some protocols
    class Lazy(Protocol):
        """
        An empty protocol specification
        """

    class Crazy(Protocol):
        """
        Another empty protocol specification
        """

    class Hazy(Protocol):
        """
        And yet another empty protocol specification
        """


    # a base component that doesn't have a protocol specification
    class Base(Component):
        """
        A simple component
        """

    # verify it is among the known component
    assert Base in registrar.components
    # verify its implementers are currently empty
    assert set(registrar.components[Base]) == set()
    # go through the pedigree of its protocol
    for protocol in Base.pyre_protocol.pyre_pedigree:
        # and verify it is an implementor of each one
        assert Base in registrar.implementers[protocol]


    # a component that implements {Lazy}
    class Larry(Base, implements=Lazy):
        """
        A component that implements {Lazy}
        """

    # verify it is among the known component
    assert Larry in registrar.components
    # verify its implementers are currently empty
    assert set(registrar.components[Larry]) == set()
    # go through the pedigree of its protocol
    for protocol in Larry.pyre_protocol.pyre_pedigree:
        # and verify it is an implementor of each one
        assert Larry in registrar.implementers[protocol]


    # a component that implements {Crazy}
    class Moe(Base, implements=Crazy):
        """
        A component that implements {Crazy}
        """

    # verify it is among the known component
    assert Moe in registrar.components
    # verify its implementers are currently empty
    assert set(registrar.components[Moe]) == set()
    # go through the pedigree of its protocol
    for protocol in Moe.pyre_protocol.pyre_pedigree:
        # and verify it is an implementor of each one
        assert Moe in registrar.implementers[protocol]


    # our target component
    class Curly(Larry, Moe, implements=Hazy):
        """
        A derived component
        """

    # verify it is among the known component
    assert Curly in registrar.components
    # verify its implementers are currently empty
    assert set(registrar.components[Curly]) == set()
    # go through the pedigree of its protocol
    for protocol in Curly.pyre_protocol.pyre_pedigree:
        # and verify it is an implementor of each one
        assert Curly in registrar.implementers[protocol]

    # since every component implements the trivial protocol, the set of registered component
    # classes should be identical to the set of implementers of {Protocol}
    assert set(registrar.components.keys()) == set(registrar.implementers[Protocol])

    # all done
    return Base, Larry, Moe, Curly


# main
if __name__ == "__main__":
    # skip pyre initialization since we don't rely on the executive
    pyre_noboot = True
    # run the test
    test()


# end of file
