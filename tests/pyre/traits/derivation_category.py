#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


# driver
def test():
    """
    Verify that derivations get the correct category predicates
    """

    # get the derivation class
    from p2.traits.Derivation import Derivation as derivation


    # a client
    class Component:
        """
        Simple class with a derivation
        """

        # declare a derivation
        # in real components, derivations are not instantiated explicitly; instead, they are
        # inferred when the right hand side of a trait declaration contains arithmetic among
        # traits
        attr = derivation()


    # get the attribute; careful not to trigger the descriptor behavior
    attr = Component.__dict__["attr"]
    # verify it's a derivation
    assert isinstance(attr, derivation)
    # verify it has the right category name
    assert attr.category == "derivation"
    # and that the trait predicates have the right values
    assert attr.isBehavior == False
    assert attr.isMeasure == False
    assert attr.isDerivation == True
    assert attr.isProperty == False
    assert attr.isFacility == False
    # all done
    return attr


# bootstrap
if __name__ == "__main__":
    # skip pyre initialization since we don't rely on the executive
    pyre_noboot = True
    # run the test
    test()


# end of file
