#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2019 all rights reserved


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


    class Crazy(Protocol):
        """
        Another empty protocol specification
        """


    class Hazy(Protocol):
        """
        And yet another empty protocol specification
        """


    # a base component
    class Base(Component):
        """
        A simple component
        """

    # the expected protocol mro
    mro = [Protocol, Configurable, object]
    # verify that its protocol specification is exactly as expected
    assert Base.pyre_protocol.mro() == mro


    # a component that implements {Lazy}
    class Larry(Base, implements=Lazy):
        """
        A component that implements {Lazy}
        """

    # the expected protocol mro
    mro = [Lazy, Protocol, Configurable, object]
    # verify that its protocol specification is exactly as expected
    assert Larry.pyre_protocol.mro() == mro


    # a component that implements {Crazy}
    class Moe(Base, implements=Crazy):
        """
        A component that implements {Crazy}
        """

    # the expected protocol mro
    mro = [Crazy, Protocol, Configurable, object]
    # verify that its protocol specification is exactly as expected
    assert Moe.pyre_protocol.mro() == mro


    # our target component
    class Derived(Larry, Moe, implements=Hazy):
        """
        A derived component
        """

    # the expected protocol mro
    mro = [Derived.pyre_protocol, Hazy, Lazy, Crazy, Protocol, Configurable, object]
    # verify that its protocol specification is exactly as expected
    assert Derived.pyre_protocol.mro() == mro

    # all done
    return


# main
if __name__ == "__main__":
    # skip pyre initialization since we don't rely on the executive
    pyre_noboot = True
    # run the test
    test()


# end of file
