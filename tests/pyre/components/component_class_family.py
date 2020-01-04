#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


def test():
    """
    Verify that the component family name is recorded and used correctly
    """
    # the component superclass
    from p2.components.Component import Component


    # a component with no family name
    class Private(Component):
        """
        A private component
        """

    # verify that its names are trivial
    assert Private.pyre_name is None
    assert Private.pyre_family is None
    # verify its human readable representation
    assert str(Private) == "component 'Private'"


    # a component with a family name
    class Public(Component, family="tests.components.public"):
        """
        A public component
        """

    # verify that its names are set to the family name
    assert Public.pyre_name == "tests.components.public"
    assert Public.pyre_family == "tests.components.public"
    # verify its human readable representation
    assert str(Public) == "component 'tests.components.public'"

    # all done
    return Private, Public


# main
if __name__ == "__main__":
    # skip pyre initialization since we don't rely on the executive
    pyre_noboot = True
    # run the test
    test()


# end of file
