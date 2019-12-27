#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2019 all rights reserved


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

    # instantiate without a name
    private = Private()
    # verify that its names are trivial
    assert private.pyre_name is None
    assert private.pyre_family is None
    # verify its human readable representation
    assert str(private) == "unnamed component, an instance of 'Private'"

    # instantiate with a name
    public = Private(name="public")
    # verify that its names are set to the family name
    assert public.pyre_name == "public"
    assert public.pyre_family is None
    # verify its human readable representation
    assert str(public) == "component 'public', an instance of 'Private'"


    # a component with a family name
    class Public(Component, family="tests.components.public"):
        """
        A public component
        """

    # instantiate without a name
    private = Public()
    # verify that its names are trivial
    assert private.pyre_name is None
    assert private.pyre_family == "tests.components.public"
    # verify its human readable representation
    assert str(private) == "unnamed component, an instance of 'tests.components.public'"

    # instantiate with a name
    public = Public(name="public")
    # verify that its names are set to the family name
    assert public.pyre_name == "public"
    assert public.pyre_family == "tests.components.public"
    # verify its human readable representation
    assert str(public) == "component 'public', an instance of 'tests.components.public'"

    # all done
    return Private, Public


# main
if __name__ == "__main__":
    # skip pyre initialization since we don't rely on the executive
    pyre_noboot = True
    # run the test
    test()


# end of file
