#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2022 all rights reserved


def test():
    """
    Verify that the extra checks necessary when verifying that a component is compatible with a
    given protocol are implemented correctly
    """
    # access the protocol base class
    from p2.components.Protocol import Protocol
    # and the component base class
    from p2.components.Component import Component

    # the base protocol
    class Library(Protocol):
        """
        Specification for a generic external library
        """

    # a subclass
    class GSL(Library):
        """
        A specific external library
        """

    # another subclass
    class VTK(Library):
        """
        Another specific external library
        """

    # a component that implements one of the protocols
    class VTK8(Component, implements=VTK):
        """
        A specific {VTK} installation
        """

    # check that {VTK8} is compatible with {Library}
    assert VTK8.pyre_isCompatibleWith(spec=Library)
    # and {VTK}
    assert VTK8.pyre_isCompatibleWith(spec=VTK)
    # but not GSL
    assert not VTK8.pyre_isCompatibleWith(spec=GSL)

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
