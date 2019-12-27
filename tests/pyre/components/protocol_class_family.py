#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2019 all rights reserved


def test():
    """
    Verify that the protocol family name is recorded and used correctly
    """
    # the protocol superclass
    from p2.components.Protocol import Protocol


    # a protocol with no family name
    class Private(Protocol):
        """
        A private protocol
        """

    # verify that its names are trivial
    assert Private.pyre_name is None
    assert Private.pyre_family is None
    # verify its human readable representation
    assert str(Private) == "protocol 'Private'"


    # a protocol with a family name
    class Public(Protocol, family="tests.protocols.public"):
        """
        A public protocol
        """

    # verify that its names are set to the family name
    assert Public.pyre_name == "tests.protocols.public"
    assert Public.pyre_family == "tests.protocols.public"
    # verify its human readable representation
    assert str(Public) == "protocol 'tests.protocols.public'"

    # all done
    return Private, Public


# main
if __name__ == "__main__":
    # skip pyre initialization since we don't rely on the executive
    pyre_noboot = True
    # run the test
    test()


# end of file
