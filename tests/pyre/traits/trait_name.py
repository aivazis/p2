#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


# driver
def test():
    """
    Verify that the trait name gets registered correctly
    """

    # get the trait class
    from p2.traits.Trait import Trait as trait


    # a client
    class Component:
        """
        Simple class with a trait
        """

        # declare a trait
        attr = trait()


    # get the attribute; careful not to trigger the descriptor behavior
    attr = Component.__dict__["attr"]
    # verify it's a trait
    assert isinstance(attr, trait)
    # verify it has the right name
    assert attr.name == "attr"
    # verify that the aliases are initialized properly
    assert attr.aliases == { "attr" }
    # all done
    return attr


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
