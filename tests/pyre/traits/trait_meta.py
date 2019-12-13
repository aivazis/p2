#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2019 all rights reserved


# driver
def test():
    """
    Verify that trait docstrings and tip get recorded correctly
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
        attr.tip = "a simple trait"
        attr.doc = "A simple trait that has scant documentation"


    # get the attribute; careful not to trigger the descriptor behavior
    attr = Component.__dict__["attr"]
    # verify it's a trait
    assert isinstance(attr, trait)
    # verify that the documentation was recorded properly
    assert attr.tip == "a simple trait"
    assert attr.doc.strip() == "A simple trait that has scant documentation"
    # all done
    return attr


# main
if __name__ == "__main__":
    # skip pyre initialization since we don't rely on the executive
    pyre_noboot = True
    # run the test
    test()


# end of file
