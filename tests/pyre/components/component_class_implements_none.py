#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


def test():
    """
    Verify that the implementation specifications of components are created correctly when
    nothing is specified explicitly
    """
    # the component superclass
    from p2.components.Component import Component
    # the protocol superclass
    from p2.components.Protocol import Protocol


    # a component with no explicit implementation specification
    class Base(Component):
        """
        A simple component
        """


    # verify that its protocol specification is exactly the base protocol
    assert Base.pyre_protocol is Protocol

    # all done
    return


# main
if __name__ == "__main__":
    # skip pyre initialization since we don't rely on the executive
    pyre_noboot = True
    # run the test
    test()


# end of file
