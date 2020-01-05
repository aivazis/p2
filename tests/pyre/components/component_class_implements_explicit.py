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


    # a protocol
    class Lazy(Protocol):
        """
        An empty protocol specification
        """

    # another protocol
    class Crazy(Protocol):
        """
        Another empty protocol specification
        """

    # a component that implements {Lazy}
    class Larry(Component, implements=Lazy):
        """
        A component with a simple {implements} specification
        """

    # the expected protocol mro
    mro = [Lazy, Protocol, Configurable, object]
    # verify that its protocol specification is exactly as expected
    assert Larry.pyre_protocol.mro() == mro


    # a component that implements both {Lazy} and {Crazy}
    class Moe(Component, implements=(Lazy,Crazy)):
        """
        A component with a compound {implements} specification
        """

    # the expected protocol mro
    mro = [Moe.pyre_protocol, Lazy, Crazy, Protocol, Configurable, object]
    # verify that its protocol specification is exactly as expected
    assert Moe.pyre_protocol.mro() == mro

    # all done
    return


# main
if __name__ == "__main__":
    # skip pyre initialization since we don't rely on the executive
    pyre_noboot = True
    # run the test
    test()


# end of file
