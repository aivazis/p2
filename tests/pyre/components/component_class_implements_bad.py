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
    # component
    from p2.components.Component import Component
    # protocol
    from p2.components.Protocol import Protocol
    # measure
    from p2.traits.Measure import Measure


    # a protocol
    class Lazy(Protocol):
        """
        An empty protocol specification
        """

        # a required trait
        req = Measure()


    # attempt to
    try:
        # declare a component that claims to implement {Lazy} but doesn't
        class Base(Component, implements=Lazy):
            """
            A simple component
            """

            # trait
            extra = Measure()

        # because the {Base} declaration is bad, we should never get here
        assert False, "declaration of 'Base' should have failed"
    # if this fails, as expected
    except Component.ProtocolNotImplementedError:
        # no problem
        pass

    # all done
    return


# main
if __name__ == "__main__":
    # skip pyre initialization since we don't rely on the executive
    pyre_noboot = True
    # run the test
    test()


# end of file
